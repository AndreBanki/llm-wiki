# watch_clips.py
# Monitors raw/clips/ for new .md files and shows a Windows notification.
# Usage: python watch_clips.py
# Requires: pip install watchdog winotify

import time
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WORKSPACE = Path(__file__).parent
CLIPS_DIR = WORKSPACE / "raw" / "clips"
VSCODE_CMD = "code"


class ClipHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        path = Path(event.src_path)
        if path.suffix != ".md" or path.name == "ingested.md":
            return

        print(f"[{time.strftime('%H:%M:%S')}] New clip detected: {path.name}")
        self._notify(path.name)
        self._open_vscode()

    def _notify(self, filename: str):
        try:
            from winotify import Notification, audio
            toast = Notification(
                app_id="LLM Wiki",
                title="New Clip — Ready to Ingest",
                msg=filename,
                duration="short",
            )
            toast.set_audio(audio.Default, loop=False)
            toast.show()
        except ImportError:
            print("(winotify not installed — skipping toast)")

    def _open_vscode(self):
        subprocess.Popen([VSCODE_CMD, str(WORKSPACE)], shell=True)


if __name__ == "__main__":
    print(f"Watching: {CLIPS_DIR}")
    observer = Observer()
    observer.schedule(ClipHandler(), str(CLIPS_DIR), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

