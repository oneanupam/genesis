# Pycore

This repository contains simple and practical python scripts to help understand python scripting concepts.

## Prerequisites

### Software Requirement

Resources in this repository are meant for use with Python 3.x (check the version using `python3 --version` or `python --version`) and pip3 (check the version using `pip3 --version` or `pip --version`). If you don't have the compatible version, download it from official python repository.

- [python3](https://www.python.org/downloads/) >= 3.14.6
- [pip3](https://pypi.org/project/pip/) >= 26.1.2
- [pre-commit](https://pre-commit.com/) >= 4.2.0

```bash
# Upgrade to the latest version using the following command:
python -m pip install --upgrade pip
```

> [!NOTE]
> See [Download Section](https://www.python.org/downloads/) on how to install Python.

### Bootstrap Virtual Environment

It is a best practice to create a virtual environment for your application to avoid any conflict in dependencies between multiple applications. Hence, it is recommended to create a virtual environment (using python's default package "venv" or of your choice) and install all the dependencies. Follow below according to your operating system.

```bash
# Linux OS
python3 -m venv example-app-venv
source example-app-venv/bin/activate # to reload the file
pip install -r requirements.txt

# Windows OS
python -m venv example-app-venv
example-app-venv\Scripts\activate
pip install -r requirements.txt
```

> [!NOTE]
> Activation makes the virtual environment the default Python interpreter for the duration of a shell session. Because, This will prepend that directory to your PATH, so that running python will invoke the virtual environment’s Python interpreter. As an indication of virtual environment activation, current shell prompt will prepend the name of the virtual environment you are currently using.
>
> To deactivate the environment, simply type `deactivate` and you will return to your normal shell.
>
> Within the virtual environment, you can use the command `pip` instead of `pip3` and `python` instead of `python3`.

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

Run the below commnad from the git repo root to set up the git hook scripts into your git hooks. It will be installed at .git/hooks/pre-commit

```bash
pre-commit install
pre-commit install --config <file> # If config file has non-standard name
pre-commit validate-config # Validate .pre-commit-config.yaml files
```

now pre-commit will run automatically on git commit. Usually, it runs only for the changed files. Its good to run the hooks against all the files when adding new hooks. To manually run all pre-commit hooks on a repo, use below -

```bash
# to run hooks on all files
pre-commit run --all-files

# to run hooks on all files using a non-standard naming config file
pre-commit run --all-files --config .pre-commit-config-old.yaml

# to run individual hook
pre-commit run <hook_id>
```

Once you have pre-commit installed, adding pre-commit plugins to your project is done with the .pre-commit-config.yaml configuration file. You can generate a very basic configuration using `pre-commit sample-config`. Every time you clone a project using pre-commit running pre-commit install should always be the first thing you do.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or new suggestions. Read the [contributing.md](CONTRIBUTING.md) before starting.

## License

This project is licensed under the [MIT License](LICENSE).
