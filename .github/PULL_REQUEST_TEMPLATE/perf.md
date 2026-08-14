Closes #{issue}

# What parts of the code was having performance problems?

- {___}

# Describe the changes made

- {___}

# List some before and after performance metrics

| Metric | Before | After | Improvement |
|:-------|:-------|:------|:------------|
| {___}  | {___}  | {___} | {___}       |

# What testing environment was used, and on what system?

Environment: {docker | local}

CPU: {___}

GPU: {___}

RAM: {___}

Storage type: {HDD | SATA SSD | NVMe SSD}

OS: {___}

# If applicable, what tests were created or updated for this code?

- {___}

# If applicable, what documentation was updated for the new code?

- {___}

# List any breaking changes, and their associated migration functions

- {___}

# Pre merge checklist

- [ ] The code is commented in a way that makes it easier to understand
- [ ] All tests have passed with this new code
- [ ] If needed, tests have been created or updated for the new code
- [ ] If needed, documentation has been updated
- [ ] All temporary console logs have been removed
- [ ] Target branch is set to develop