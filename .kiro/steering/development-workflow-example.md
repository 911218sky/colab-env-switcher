---
inclusion: always
---

# Development Workflow Example

This document shows a real-world example of how to work on a feature following our Git workflow.

## Scenario: Adding Python 3.15 Support

Let's walk through adding support for Python 3.15 (hypothetical future version).

### Step 1: Start from Develop

```bash
# Make sure you're on develop and it's up to date
git checkout develop
git pull origin develop
```

### Step 2: Create Feature Branch

```bash
# Create a feature branch
git checkout -b feature/python-3.15-support
```

### Step 3: Make Changes (Organized Commits)

#### Commit 1: Update Core Logic

```bash
# Edit the switcher code
# File: colab_env_switcher/switcher.py
# - Add 3.15 to version validation
# - Update installation logic

git add colab_env_switcher/switcher.py
git commit -m "feat(switcher): add Python 3.15 support

- Add Python 3.15 to supported versions
- Update package installation logic for 3.15
- Add fallback handling for experimental packages"
```

#### Commit 2: Update Documentation

```bash
# Edit documentation files
# Files: README.md, examples/colab_example.ipynb

git add README.md examples/colab_example.ipynb
git commit -m "docs: add Python 3.15 to documentation

- Update README with Python 3.15 in supported versions
- Add Python 3.15 example to Jupyter notebook
- Add note about experimental status"
```

#### Commit 3: Update CI/CD

```bash
# Edit workflow files
# File: .github/workflows/test.yml

git add .github/workflows/test.yml
git commit -m "ci(test): add Python 3.15-dev to test matrix

- Add Python 3.15-dev to GitHub Actions test matrix
- Mark as allowed to fail (experimental version)"
```

#### Commit 4: Update Version

```bash
# Update version files
# Files: setup.py, pyproject.toml, __init__.py

git add setup.py pyproject.toml colab_env_switcher/__init__.py
git commit -m "chore: bump version to 0.1.3

Prepare for release with Python 3.15 support"
```

### Step 4: Push Feature Branch

```bash
git push origin feature/python-3.15-support
```

### Step 5: Create Pull Request

Create a PR from `feature/python-3.15-support` to `develop` with description:

```markdown
## Add Python 3.15 Support

### Changes
- Added Python 3.15 to supported versions
- Updated documentation and examples
- Added CI/CD testing for Python 3.15-dev
- Bumped version to 0.1.3

### Testing
- [x] Tested locally with Python 3.15-dev
- [x] All existing tests pass
- [x] Documentation updated

### Related Issues
Closes #123
```

### Step 6: Merge to Develop

After review and approval:

```bash
# Merge the PR (on GitHub or locally)
git checkout develop
git merge feature/python-3.15-support --no-ff
git push origin develop

# Delete feature branch
git branch -d feature/python-3.15-support
git push origin --delete feature/python-3.15-support
```

### Step 7: Prepare for Release (When Ready)

When develop has accumulated enough changes for a release:

```bash
# Switch to main
git checkout main
git pull origin main

# Squash merge from develop
git merge develop --squash

# Create consolidated release commit
git commit -m "Release v0.1.3 - Add Python 3.15 support and improvements

This release adds support for Python 3.15 and includes several improvements.

Features:
- Add Python 3.15 support (experimental)
- Improved package installation fallback logic
- Better error messages for experimental versions

Documentation:
- Updated README with Python 3.15 examples
- Added Python 3.15 to Jupyter notebook examples
- Clarified experimental version status

CI/CD:
- Added Python 3.15-dev to test matrix
- Configured experimental version testing

Technical Changes:
- Enhanced version validation logic
- Improved error handling for missing packages
- Updated dependencies

Author: 911218sky (sky@sky1218.com)"

# Tag the release
git tag -a v0.1.3 -m "Version 0.1.3 - Python 3.15 support"

# Push to remote
git push origin main
git push origin v0.1.3

# Sync develop with main
git checkout develop
git merge main
git push origin develop
```

## Example: Multiple Features in Develop

### Scenario: Working on Multiple Things

```bash
# Feature 1: Add logging
git checkout develop
git checkout -b feature/add-logging

# Make changes
git add colab_env_switcher/switcher.py
git commit -m "feat(switcher): add logging support

- Add logging for version switching operations
- Add debug mode for troubleshooting
- Log package installation attempts"

git add README.md
git commit -m "docs: document logging feature

- Add logging configuration examples
- Document debug mode usage"

git push origin feature/add-logging
# Create PR to develop

# Feature 2: Improve error messages (while feature 1 is in review)
git checkout develop
git checkout -b feature/better-errors

# Make changes
git add colab_env_switcher/switcher.py
git commit -m "feat(switcher): improve error messages

- Add specific error messages for common issues
- Include troubleshooting tips in error output
- Add links to documentation in errors"

git push origin feature/better-errors
# Create PR to develop
```

## Example: Bug Fix in Develop

```bash
# Bug discovered in develop
git checkout develop
git checkout -b fix/version-detection

# Fix the bug
git add colab_env_switcher/switcher.py
git commit -m "fix(switcher): correct version detection logic

- Fix regex pattern for version parsing
- Handle edge cases with version strings
- Add validation for malformed version numbers"

# Add test
git add tests/test_switcher.py
git commit -m "test(switcher): add version detection tests

- Add tests for valid version formats
- Add tests for invalid version formats
- Add edge case tests"

git push origin fix/version-detection
# Create PR to develop
```

## Viewing Clean History

After following this workflow, your develop branch will have a clean, organized history:

```bash
git log --oneline develop

# Output:
# a1b2c3d feat(switcher): add Python 3.15 support
# e4f5g6h docs: add Python 3.15 to documentation
# i7j8k9l ci(test): add Python 3.15-dev to test matrix
# m0n1o2p chore: bump version to 0.1.3
# q3r4s5t fix(switcher): correct version detection logic
# u6v7w8x test(switcher): add version detection tests
# y9z0a1b feat(switcher): add logging support
# c2d3e4f docs: document logging feature
```

And your main branch will have a super clean history:

```bash
git log --oneline main

# Output:
# 12ff2ca Release v0.1.3 - Add Python 3.15 support and improvements
# 34gg5hh Release v0.1.2.post1 - Stable release
# 56ii7jj Release v0.1.0 - Initial release
```

## Summary

### Develop Branch
- Multiple organized commits
- Each commit is one logical change
- Use conventional commit format
- Group related changes together
- Keep commits atomic and working

### Main Branch
- Single consolidated commit per release
- Detailed release notes in commit message
- Tagged with version number
- Clean, professional history

This workflow ensures both branches are professional and maintainable, just like major open-source projects!
