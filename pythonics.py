from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Tree, Markdown, Log, Link
import subprocess
from pathlib import Path
from rich.text import Text
from hashlib import sha256
from textual.reactive import reactive
import asyncio
import tokenize
import argparse

def get_exo_infos(path):
    with open(path, 'r') as fileObj:
        tokens = tokenize.generate_tokens(fileObj.readline)
        for toktype, tok, _, _, _ in tokens:
            if toktype == tokenize.STRING and tok.startswith('"""'):
                # Remove leading and trailing triple quotes
                description = tok.strip('"').strip()
                return description
    return None

def check_script_status(path: Path) -> bool:
    try:
        subprocess.run(["python", str(path)], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False
    
def get_instructions() -> str: 
    with open('./Exercices/README.md', 'r') as file:
      return file.read()

class PythonLearningApp(App):
    CSS_PATH = "styles.tcss"  # You can style with a simple tcss file
    file_hashes: dict[Path, str] = {}
    current_file: reactive[Path | None] = reactive(None)

    def __init__(self, editor: str) :
        self.editor = editor
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Horizontal(
            
            Vertical(
                Markdown(get_instructions()),
                Log(),
                id="left",),

            Vertical(
                Tree("Exercices"),
                id="right",
            ),
        )

    def run_script(self, path: Path) -> str:
      result = subprocess.run(
          ["python", str(path)],
          capture_output=True,
          text=True
      )
      return result.stdout + result.stderr

    async def on_mount(self):
      tree = self.query_one(Tree)
      self.build_tree(tree.root, Path("./Exercices"))
      tree.root.expand()
      self.background_task = asyncio.create_task(self.watch_files())

    def find_node_by_path(self, node, path: Path):
        if node.data == path:
            return node
        for child in node.children:
            result = self.find_node_by_path(child, path)
            if result:
                return result
        return None
    
    def refresh_tree_status(self, path: Path, success: bool):
        tree = self.query_one(Tree)
        node = self.find_node_by_path(tree.root, path)

        if node:
            name = " ".join(path.name.removesuffix('.py').split("_")[1:]).capitalize()
            label = Text.assemble(("●","green" if success else "red"), " ", (name, "bold"))
            node.set_label(label)

    async def watch_files(self):
        i = 0
        while True:
            i += 1
            await asyncio.sleep(2)
            for path in self.file_hashes:
                try:
                    new_hash = sha256(path.read_bytes()).hexdigest()
                    if new_hash != self.file_hashes[path]:
                        self.file_hashes[path] = new_hash
                        # File changed!
                        status = check_script_status(path)
                        self.refresh_tree_status(path, status)

                        if path == self.current_file:
                            output = self.run_script(path)
                            logs = self.query_one(Log)
                            logs.clear()
                            logs.write(output)
                except FileNotFoundError:
                    continue  # File might've been deleted
                except: 
                    continue

    def build_tree(self, node, path: Path):
        for entry in sorted(path.iterdir()):
          if entry.is_dir():
              name = " ".join(entry.name.split("_")[1:]).capitalize()
              child = node.add(name, expand=True)
              self.build_tree(child, entry)
          elif entry.suffix == ".py":
              content = entry.read_bytes()
              self.file_hashes[entry] = sha256(content).hexdigest()
              status = check_script_status(entry)
              name = " ".join(entry.name.removesuffix('.py').split("_")[1:]).capitalize()
              label = Text.assemble(("●","green" if status else "red"), " ", (name, "bold"))
              node.add_leaf(label, data=entry)

    async def on_tree_node_selected(self, message: Tree.NodeSelected):
        path = message.node.data
        if isinstance(path, Path) and path.suffix == ".py":
            self.current_file = path
            output = self.run_script(path)
            logs = self.query_one(Log)
            logs.clear()
            logs.write(output)
            self.query_one(Markdown).update(f"{get_exo_infos(path)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Pythonics")
    parser.add_argument("--editor", "-e", help="The editor in which files are oppened", default="nano", type=str)
    args = parser.parse_args()
    app = PythonLearningApp(args.editor)
    app.run()
