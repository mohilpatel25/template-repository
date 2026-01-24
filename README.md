# Template Repository

This repository serves as a template for creating new Python repositories with modern tooling. It is configured with `uv` for dependency management and `ruff` for linting/formatting.

## Features

- **Dependency Management**: Uses `uv` for fast package management.
- **Linting & Formatting**: configured with `ruff`.
- **Testing**: `pytest` with coverage reports.
- **Helper Scripts**:
    - `bin/lint`: Runs formatters and linters.
    - `bin/ci`: Runs the full CI suite (lint + tests).
- **GitHub Actions**: integrated CI pipeline.

## Setup Instructions

### 1. Install uv

Follow the [official installation guide](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) to install `uv`.

### 2. Clone the repository

```bash
git clone https://github.com/mohilpatel25/template-repository.git
cd template-repository
```

### 3. Install Dependencies

```bash
uv sync
```

## Development

### Running Tests and Linting

We provide helper scripts to make development easier:

- **Run all checks (Lint + Test)**:
  ```bash
  ./bin/ci
  ```

- **Run Linting only**:
  ```bash
  ./bin/lint
  ```

- **Run Tests manually**:
  ```bash
  uv run pytest
  ```

## Customization

- **Dependencies**: Add new dependencies using `uv add <package>`.
- **CI/CD**: Modify `.github/workflows/ci.yml` to adjust the pipeline.
- **Tools**: Configure tools in `pyproject.toml`.
