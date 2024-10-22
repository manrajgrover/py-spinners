# Development

We need to clone the project and prepare the virtual environment using poetry

## Setup

```bash
git clone https://github.com/d-chris/py-spinners.git -b develop --recurse-submodules

cd py-spinners

poetry --version || pip install poetry --user
poetry install --with dev
```

This will install all requirements to use `py-spinners`.

To install development dependencies, run:

```bash
pre-commit --version || pip install pre-commit --user
pre-commit install
```

## Testing

For devolopment activate your virtual environment and for testing run pytest

```bash
poetry shell
pytest
```

Before submitting a pull request, make sure the code passes all the tests and is clean of lint errors, to test all with all python version in parallel:

```bash
poetry run tox -p
```

For checking lint issues:

```bash
pre-commit run pylint --all-files
```
