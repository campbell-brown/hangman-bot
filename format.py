import argparse
import os
import subprocess
import sys

FORMAT_DIR = os.path.dirname(os.path.realpath(__file__))

EXCLUDED_DIRECTORIES = [
    # do not exclude anything
]

EXCLUDED_DIRECTORIES_ARGS = f"^/({'|'.join(EXCLUDED_DIRECTORIES)})"

parser = argparse.ArgumentParser()
parser.add_argument(
    "--check",
    "-c",
    action="store_true",
    help="Check the formatting instead of fixing it.",
)
args = parser.parse_args()

run_black = ["python", "-m", "black", "--line-length", "120", FORMAT_DIR]

if len(EXCLUDED_DIRECTORIES) > 0:
    run_black += ["--exclude", EXCLUDED_DIRECTORIES_ARGS]

if args.check:
    run_black.append("--check")

# Run black using subprocess
process = subprocess.run(run_black, check=False)

sys.exit(process.returncode)
