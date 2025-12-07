import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import config
import os

WATCH_DIR = config.MODERATION_PATH

class ReloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.start_bot()

    def start_bot(self):
        if self.process:
            self.process.kill()
            print("♻ Restarting Void Sentinel...")

        self.process = subprocess.Popen(["python", "bot.py"])

    def on_modified(self, event):
        # Only reload when moderation folder files change
        if WATCH_DIR.replace("/", os.sep) in event.src_path:
            print(f"🔄 Change detected: {event.src_path}")
            self.start_bot()


if __name__ == "__main__":
    print("🔥 Hot Reload Active (Monitoring Moderation Commands Only)")

    handler = ReloadHandler()
    observer = Observer()
    observer.schedule(handler, WATCH_DIR, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        if handler.process:
            handler.process.kill()
    observer.join()
