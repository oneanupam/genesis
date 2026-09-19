# Genesis

This repository contains a collection of simple, practical Python scripts designed to help learners understand core scripting concepts and everyday programming patterns.

## Prerequisites

### Software Requirements

Install the required tools before contributing to this project:

- [Python 3](https://www.python.org/downloads/) >= 3.14.6
- [pip](https://pypi.org/project/pip/) >= 26.1.2
- [pre-commit](https://pre-commit.com/) >= 4.2.0

```bash
# Upgrade pip before installing project dependencies
python -m pip install --upgrade pip
```

> [!NOTE]
> To confirm your environment, run `python3 --version` or `python --version`, and `pip3 --version` or `pip --version`. See the [Python download page](https://www.python.org/downloads/) for installation instructions.

### Set Up a Virtual Environment

It is recommended to create an isolated virtual environment for this project to avoid dependency conflicts with other Python projects.

```bash
# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Windows
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

> [!NOTE]
> Activating the virtual environment updates your shell PATH so `python` and `pip` point to the environment for the current session. To leave the environment, run `deactivate`.

## Repo Layout

At a high level, these folders make up the `github.com/oneanupam/python-training-lab` repository.

- [`.github/`](./.github) - This folder contains the codeowners, pull request template and github action yaml files.
- [`.vscode/`](./.vscode) - It contains project-specific settings and configurations to customize how VS Code behaves for the workspace.
- [`build/`](./build) - This folder contains the build config files to build/deploy the application code.
- [`docs/`](./docs) - This folder contains the documentations related to the repository.
- [`src/`](./src) - This folder contains the application code or scripts.
- [`.pre-commit-config.yaml`](.pre-commit-config.yaml) - This file contains the plugin configuration for pre-commit.
- [`.editorconfig`](.editorconfig) - This file has the configuration for the editorconfig plugin.

## Run pre-commit
This repository already includes a `.pre-commit-config.yaml`. Run the following commands to install the hooks locally:

```bash
python -m pip install pre-commit
pre-commit install
pre-commit validate-config
```

This installs the hook into `.git/hooks/pre-commit`. Once installed, pre-commit runs automatically when you commit changes. By default, it checks only the files included in the commit.

To run all hooks manually, use:

```bash
pre-commit run --all-files
pre-commit run <hook_id>
```

## Contributing

Contributions and suggestions are welcome. Before opening an issue or pull request:

1. Review the [contribution guidelines](CONTRIBUTING.md).
2. Install the pre-commit hooks and run them against your changes.
3. Open an issue for bugs or ideas, or submit a pull request with a clear description of the change.

## License

This project is licensed under the [MIT License](LICENSE).

## References

* **MDN Web Docs.** "Understanding Semantic HTML." [developer.mozilla.org](https://mozilla.org)
* **GitHub Docs.** "Basic writing and formatting syntax." [://github.com](https://://github.com/en/get-started/writing-on-github)

