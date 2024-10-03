# Template Repository with pre-commit checks and GitHub Actions

This repository serves as a template for creating new repositories with integrated pre-commit hooks and GitHub Actions. The setup ensures consistent code quality by enforcing pre-commit checks and running tests automatically when a pull request (PR) is made to the `main` branch.

## Features

- **Pre-commit Hooks**: Automatically check code before commits are accepted.
- **GitHub Actions Integration**: Automatically runs:
  - Pre-commit checks on every PR.
  - Test suite to validate code changes.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/mohilpatel25/template-repository.git
cd template-repository
```

### 2. Install Pre-commit

To enable pre-commit checks locally, install the `pre-commit` package and set it up:

```bash
pip install pre-commit
pre-commit install
```

This will ensure pre-commit hooks are executed every time you make a commit.

### 3. Modify as a Template

Once cloned, you can use this repository as a template for new projects. Modify the code, tests, or add new pre-commit hooks based on your project requirements.

### 4. Run Pre-commit Manually

You can manually run pre-commit hooks at any time by executing:

```bash
pre-commit run --all-files
```

### 5. GitHub Actions Workflow

The repository includes a GitHub Actions workflow located in `.github/workflows/ci.yml`. This workflow:

- Runs pre-commit checks automatically on all PRs targeting the `main` branch.
- Runs tests to ensure code integrity.

Ensure your test suite is properly set up and modify the workflow to suit your project needs.

## Customizing Pre-commit Hooks

Pre-commit hooks are configured in the `.pre-commit-config.yaml` file. To add or remove hooks, modify this file and run:

```bash
pre-commit autoupdate
```

## Customizing GitHub Actions

Update the `.github/workflows/ci.yml` file to make changes to the actions.
