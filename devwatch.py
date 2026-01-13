import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

ROOT = os.getcwd()
OUT  = os.path.join(ROOT, "_changes")

IGNORE = {
    ".git",
    "_changes",
    "/vendor/", # root-level vendor directory only
    #"vendor/", # nested vendor directory
    "node_modules",
    "storage",
}

def is_ignored(path):
    """
    path: relative path using os.sep
    """
    # normalize path separators
    norm_path = path.replace(os.sep, "/")

    for ignore in IGNORE:
        if ignore.startswith("/"):
            # ignore only if at root
            if norm_path.startswith(ignore.lstrip("/")):
                return True
        else:
            # ignore anywhere
            if f"/{ignore}/" in f"/{norm_path}/":
                return True
    return False

class Handler(FileSystemEventHandler):

    def on_created(self, event):
        self.process(event, "ADD")

    def on_modified(self, event):
        self.process(event, "MOD")

    def process(self, event, label):
        if event.is_directory:
            return

        rel = os.path.relpath(event.src_path, ROOT)

        if is_ignored(rel):
            return

        src = event.src_path
        dst = os.path.join(OUT, rel)

        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)

        print(f"[{label}] {rel}")
        print(f"[COPY] → _changes/{rel}")

if __name__ == "__main__":
    print("Watching project...\n")

    observer = Observer()
    observer.schedule(Handler(), ROOT, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping...")
        observer.stop()

    observer.join()
