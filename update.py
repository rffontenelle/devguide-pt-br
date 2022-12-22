#!/usr/bin/python3
"""Tool for updating devguide translation guide for the given language.
Very inspired in python-docs-fr's merge.py script. See original script in:
https://git.afpy.org/AFPy/python-docs-fr/
"""

from pathlib import Path
from shutil import copytree, ignore_patterns, rmtree
import argparse
import subprocess
import os


def run(*args: str | Path, **kwargs) -> subprocess.CompletedProcess:
    """Run a shell command with subprocess.run() with check=True and
    encoding="UTF-8".
    """
    return subprocess.run(list(args), encoding="UTF-8", check=True, **kwargs)


def create_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Update Devguide translation files')
    parser.add_argument(
        "-l",
        "--language",
        default="pt_BR",
        help="Language code to update translations for"
    )
    parser.add_argument(
        "--devguide_repo",
        default=Path("venv/devguide"),
        type=Path,
        help="Use this given devguide clone.",
    )
    return parser.parse_args()


def setup_repo(repo_path: Path, branch: str):
    """Ensure the repository is up to date if previously clones, or clone it.
    """
    if repo_path.is_dir():
        """Ensure we're up-to-date."""
        run("git", "-C", repo_path, "checkout", branch)
        run("git", "-C", repo_path, "pull", "--ff-only")


if __name__ == "__main__":
    args = create_parser()
    setup_repo(args.devguide_repo, "main")
    language_dir = Path(args.devguide_repo / 'locales' / args.language / 'LC_MESSAGES')
    rmtree(args.devguide_repo / "_build", ignore_errors=True)
    rmtree(args.devguide_repo / "locales", ignore_errors=True)
    run(
        *["sphinx-build", "-jauto", "-QDgettext_compact=0", "-bgettext", ".", "_build/pot"],
        cwd=args.devguide_repo
    )
    # copy files to inside devguide checkout to upd́ate, then copy the updated ones
    os.makedirs(language_dir, exist_ok=True)
    copytree(
        '.', language_dir, ignore=ignore_patterns('devguide', '.*', 'venv', __file__),
        dirs_exist_ok=True
    )
    run(
        *["sphinx-intl", "update", "-dlocales", "-p_build/pot", "-l", args.language],
        cwd=args.devguide_repo
    )
    copytree(language_dir, '.', dirs_exist_ok=True)
    rmtree(args.devguide_repo / "_build")
    run("powrap", "-m")
