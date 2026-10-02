# Contributing Changes

- Make a fork of this repository under your account.
- Use Clone or Download to open the repo on your computer.
- Use Git or GitHub Desktop to checkout the `import-2.1.x` branch.
- Make a copy of the branch, giving it a unique name.
- Add new configurations and/or make changes to existing ones.
- Commit your changes and push them to your fork.
- Submit a Pull Request to the `import-2.1.x` branch.

## Marlin Pull Requests

When a Marlin pull request (PR) includes any configuration files changes, coordinate
the Configurations PR with the Marlin PR so their CI tests can work together:

1. Note the Marlin PR number, such as `98789`. This is the key.
2. Create a Configurations work branch from `import-2.1.x` with the exact name
   `pr-98789`, replacing the number with the Marlin PR number.
3. Push that branch.
4. Optionally open a Configurations PR against `import-2.1.x`.
5. The Configurations branch `pr-98789` should be retained while the Marlin PR is open.
   - The Marlin `ci-build-tests.yml` workflow recognizes this naming pattern and will
     fetch any Configurations needed for CI Build Tests from branch `pr-98789`.
     If no `pr-98789` is found tests wull run against `bugfix-2.1.x`, as usual.
   - The Configurations `build-pr.yml` workflow recognizes this naming pattern and
     fetches the Marlin PR using GitHub's `refs/pull/98789/head` reference.
6. You can re-run CI tests on the Marlin PR after step 3, if needed.
