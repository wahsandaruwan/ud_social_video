# Contributing to Universal Video Downloader

Thank you for your interest in contributing! We welcome contributions from anyone.  
This document outlines how you can contribute, the branch workflow, and best practices for collaborating in this project.

---

## Branch Strategy

- **main**: Stable, production-ready code. Only core maintainers merge here.
- **prod**: Final production releases and deployments. Only maintainers merge here.
- **stag**: Staging branch for QA/testing before release. Only maintainers merge here.
- **dev**: Active development branch. All new contributions and PRs must target this branch.
- **feature/bugfix branches**: All contributors should create their own branches based on `dev` for their work (e.g., `feature/my-feature`, `bugfix/fix-download-error`).

---

## How to Contribute

1. **Clone the dev Branch Only**
   - Clone the repository and checkout the `dev` branch:
     ```bash
     git clone -b dev https://github.com/wahsandaruwan/universal-video-downloader.git
     cd universal-video-downloader
     ```

2. **Create Your Own Branch**
   - Base your branch on `dev`:
     ```bash
     git checkout dev
     git pull origin dev
     git checkout -b feature/my-feature
     ```
   - Name your branch according to what you are working on (e.g., `feature/new-ui`, `bugfix/fix-error`).

3. **Make Your Changes**
   - Commit regularly and use clear, descriptive commit messages.

4. **Test Your Changes**
   - Make sure your code works as expected and does not break existing functionality.
   - Test on all platforms (Windows, macOS, Linux) if possible.

5. **Keep Your Branch Up to Date**
   - Periodically update your branch with the latest changes from `dev`:
     ```bash
     git fetch origin
     git checkout dev
     git pull origin dev
     git checkout feature/my-feature
     git merge dev
     ```

6. **Open a Pull Request**
   - When your work is ready, push your branch to your fork or the repo:
     ```bash
     git push origin feature/my-feature
     ```
   - Go to the GitHub repository and open a pull request **into the `dev` branch**.
   - Fill out the PR template and provide a clear description of your changes.

---

## Pull Request Guidelines

- **PRs must target `dev`**, not `main`, `stag`, or `prod`.
- Provide a description of your change and any related issue numbers.
- Reference issues your PR fixes or relates to (e.g., "Closes #42").
- If your change affects the UI, attach screenshots if possible.
- Make sure your code passes all CI checks (linting, build, tests).
- At least one review is required before merging.

---

## Branch Protection & Access

- Direct pushes to `main`, `prod`, `stag`, and `dev` are restricted to core maintainers.
- All changes must come in via pull requests to `dev`.
- Maintainers will review, request changes if necessary, and merge when ready.

---

## Coding Standards

- Write clean, readable Python code.
- Follow [PEP8](https://pep8.org/) style guidelines.
- Document public functions and classes.
- Use meaningful variable and function names.

---

## Reporting Issues

- Use [GitHub Issues](https://github.com/wahsandaruwan/universal-video-downloader/issues) for bugs, suggestions, and feature requests.
- Please provide:
  - Steps to reproduce
  - Platform details (Windows/Mac/Linux, Python version)
  - Screenshots or error logs (if applicable)

---

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## License

By contributing, you agree your code will be released under the [MIT License](LICENSE).

---

Thank you for helping improve Universal Video Downloader!