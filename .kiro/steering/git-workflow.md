---
inclusion: always
---

# Git Workflow and Branch Management

## Branch Strategy

This project follows a **clean main branch** strategy with two primary branches:

### Main Branch (`main`)
- **Purpose**: Production-ready code only
- **Commit History**: Must be clean and meaningful
- **Protection**: Never commit directly to main
- **Merges**: Only accept squashed/consolidated commits from develop

### Develop Branch (`develop`)
- **Purpose**: Active development and integration
- **Commit History**: Should be organized and logical (not messy)
- **Testing**: All features must be tested before merging to main
- **Commits**: Use conventional commits format for clarity

## Commit Guidelines for Develop Branch

Even though develop allows multiple commits, they should still be **organized and meaningful**.

### Conventional Commits Format

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Commit Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, no logic change)
- **refactor**: Code refactoring (no feature change or bug fix)
- **perf**: Performance improvements
- **test**: Adding or updating tests
- **build**: Build system or dependencies changes
- **ci**: CI/CD configuration changes
- **chore**: Other changes (maintenance tasks)

### Scope (Optional)

Specify what part of the codebase is affected:
- `switcher`: Main switching logic
- `install`: Installation/setup code
- `docs`: Documentation
- `ci`: CI/CD workflows
- `deps`: Dependencies

### Examples of Good Commits in Develop

```bash
# Feature
feat(switcher): add support for Python 3.14
feat(install): add optional uv package manager installation

# Bug fix
fix(switcher): resolve multiple version switching issue
fix(install): handle missing distutils package gracefully

# Documentation
docs(readme): add installation examples
docs(api): update function docstrings

# Refactoring
refactor(switcher): extract package installation logic
refactor: simplify error handling code

# Tests
test(switcher): add tests for version switching
test: add property-based tests for edge cases

# CI/CD
ci(publish): update PyPI publishing workflow
ci(test): add Python 3.14-dev to test matrix

# Chore
chore: update version to 0.1.3
chore(deps): update dependencies
```

### Rules for Develop Branch Commits

#### ✅ DO
- **One logical change per commit** - Don't mix features, fixes, and refactoring
- **Use conventional commit format** - Makes history searchable and clear
- **Write descriptive commit messages** - Explain what and why, not just what
- **Keep commits atomic** - Each commit should be a complete, working change
- **Test before committing** - Ensure code works before committing
- **Group related changes** - Multiple files for one feature = one commit

#### ❌ DON'T
- **Mix unrelated changes** - Don't combine feature + fix + docs in one commit
- **Commit broken code** - Each commit should leave the code in a working state
- **Use vague messages** - Avoid "update code", "fix stuff", "changes"
- **Commit too frequently** - Don't commit every single line change
- **Commit too infrequently** - Don't bundle a week's work into one commit

### Commit Size Guidelines

#### Too Small ❌
```bash
git commit -m "add import"
git commit -m "add function"
git commit -m "add docstring"
git commit -m "fix typo"
```

#### Too Large ❌
```bash
git commit -m "add feature, fix bugs, update docs, refactor code"
```

#### Just Right ✅
```bash
git commit -m "feat(switcher): add Python 3.14 support

- Add Python 3.14 to supported versions list
- Update installation logic to handle 3.14 packages
- Add fallback for missing optional packages
- Update documentation with 3.14 examples"
```

### Organizing Your Work

Before committing, organize your changes logically:

```bash
# Check what you've changed
git status
git diff

# Stage related changes together
git add colab_env_switcher/switcher.py
git commit -m "feat(switcher): add version validation"

git add README.md examples/
git commit -m "docs: add Python 3.14 examples"

git add .github/workflows/test.yml
git commit -m "ci(test): add Python 3.14 to test matrix"
```

### Interactive Staging

Use interactive staging to commit parts of files separately:

```bash
# Stage changes interactively
git add -p

# This lets you choose which changes to include in each commit
```

### Amending Commits (Before Pushing)

If you forgot something in your last commit:

```bash
# Add the forgotten changes
git add forgotten_file.py

# Amend the last commit (don't do this after pushing!)
git commit --amend --no-edit
```

### Commit Message Template

Create a commit message template for consistency:

```bash
# Create template file
cat > ~/.gitmessage << 'EOF'
# <type>(<scope>): <subject>
# 
# <body>
# 
# <footer>
# 
# Types: feat, fix, docs, style, refactor, perf, test, build, ci, chore
# Scope: switcher, install, docs, ci, deps
# Subject: imperative mood, lowercase, no period
# Body: explain what and why (optional)
# Footer: breaking changes, issue references (optional)
EOF

# Configure git to use it
git config --global commit.template ~/.gitmessage
```

## Merging Develop to Main

When merging `develop` into `main`, you MUST consolidate all commits into a single, meaningful commit.

### Step-by-Step Process

1. **Ensure develop is ready**
   ```bash
   git checkout develop
   git status
   # Make sure all tests pass
   ```

2. **Merge with squash (consolidate commits)**
   ```bash
   git checkout main
   git merge develop --squash
   ```

3. **Create a meaningful commit message**
   ```bash
   git commit -m "Release vX.Y.Z - Brief description

   Features:
   - Feature 1 description
   - Feature 2 description

   Bug Fixes:
   - Fix 1 description
   - Fix 2 description

   Technical Changes:
   - Technical change 1
   - Technical change 2

   Breaking Changes (if any):
   - Breaking change description
   "
   ```

4. **Tag the release**
   ```bash
   git tag -a vX.Y.Z -m "Version X.Y.Z - Release description"
   ```

5. **Push to remote**
   ```bash
   git push origin main
   git push origin vX.Y.Z
   ```

6. **Sync develop with main**
   ```bash
   git checkout develop
   git merge main
   git push origin develop
   ```

## Commit Message Format for Main Branch

### Structure
```
<type>: <short summary>

<detailed description>

<optional sections: Features, Bug Fixes, Technical Changes, Breaking Changes>
```

### Types
- `Release vX.Y.Z` - For version releases
- `Hotfix vX.Y.Z` - For urgent production fixes
- `Merge` - For branch merges (rare, prefer squash)

### Example Good Commit
```
Release v0.1.2.post1 - Stable release with multiple improvements

This release consolidates all improvements from the 0.1.x series.

Features:
- Quick Python version switching (Python 3.7-3.14)
- Automatic pip installation for new Python versions
- Optional uv package manager installation
- Support for multiple version switches in same session

Bug Fixes:
- Fixed multiple version switching not working correctly
- Smart package installation handles missing dependencies gracefully
- Better error messages for unsupported versions

Technical Changes:
- Uses update-alternatives --set for reliable version switching
- Individual package installation with graceful fallback
- Automated CI/CD with GitHub Actions
- Comprehensive error handling

Author: 911218sky (sky@sky1218.com)
```

## Rules for Main Branch

### ✅ DO
- Keep commit history clean and readable
- Use squash merges from develop
- Write detailed, meaningful commit messages
- Tag all releases
- Include version numbers in commit messages
- Document breaking changes clearly

### ❌ DON'T
- Commit directly to main (except hotfixes)
- Merge without squashing
- Use vague commit messages like "fix bug" or "update code"
- Push untested code
- Rewrite published history (unless absolutely necessary)

## Hotfix Process

For urgent production fixes:

1. **Create hotfix branch from main**
   ```bash
   git checkout main
   git checkout -b hotfix/description
   ```

2. **Make the fix and test**
   ```bash
   # Make changes
   git add .
   git commit -m "Hotfix: Description of the fix"
   ```

3. **Merge to main**
   ```bash
   git checkout main
   git merge hotfix/description --no-ff
   git tag -a vX.Y.Z -m "Hotfix X.Y.Z"
   git push origin main
   git push origin vX.Y.Z
   ```

4. **Merge back to develop**
   ```bash
   git checkout develop
   git merge main
   git push origin develop
   ```

5. **Delete hotfix branch**
   ```bash
   git branch -d hotfix/description
   ```

## Version Numbering

Follow [Semantic Versioning](https://semver.org/):

- **MAJOR.MINOR.PATCH** (e.g., 1.2.3)
- **MAJOR.MINOR.PATCH.postN** (e.g., 0.1.2.post1) - For post releases
- **MAJOR.MINOR.PATCH.devN** (e.g., 0.1.3.dev1) - For development versions

### When to Increment
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)
- **post**: Republish with same functionality (metadata/docs changes)

## Checking Commit History

Before merging to main, verify the commit history is clean:

```bash
# View main branch history
git log --oneline main

# Should show clean, meaningful commits like:
# 12ff2ca Release v0.1.2.post1 - Stable release
# a1b2c3d Release v0.1.1 - Bug fixes
# d4e5f6g Release v0.1.0 - Initial release
```

## Emergency: Cleaning Up Main Branch

If main branch becomes messy, you can reset it (use with caution):

```bash
# Create a clean branch from current state
git checkout --orphan main-clean
git add .
git commit -m "Clean commit message with all changes"

# Replace main
git branch -D main
git branch -m main-clean main
git push origin main --force

# Update tags if needed
git tag -d old-tag
git tag -a new-tag -m "Tag message"
git push origin new-tag
```

## Summary

- **Main branch = Clean history**
- **Develop branch = Active development**
- **Always squash when merging to main**
- **Write detailed commit messages**
- **Tag all releases**
- **Test before merging**

This workflow ensures main branch remains professional and easy to understand for all contributors and users.
