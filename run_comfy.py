import os
import subprocess
import sys

COMFY_DIR = r"C:\Users\sugam\Downloads\ctrlcat\ComfyUI"
VENV_PYTHON = os.path.join(COMFY_DIR, ".venv", "Scripts", "python.exe")
MAIN_SCRIPT = os.path.join(COMFY_DIR, "main.py")

def run_comfy():
    return subprocess.Popen(
        [VENV_PYTHON, MAIN_SCRIPT, "--cpu"],
        cwd=COMFY_DIR
    )

def listen_for_r(proc):
    try:
        while True:
            key = input("Press 'r' + Enter to restart ComfyUI: ").strip().lower()
            if key == 'r':
                proc.terminate()
                proc.wait()
                print("Restarting ComfyUI...")
                return
    except KeyboardInterrupt:
        proc.terminate()
        sys.exit(0)

if __name__ == "__main__":
    while True:
        proc = run_comfy()
        listen_for_r(proc)