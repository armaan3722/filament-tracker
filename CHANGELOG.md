# Changelog

## [Unreleased]

### Added
- Version tracking for firmware updates to printers and ams
- Creating, editing, and viewing info for projects and categories
- Creating print jobs
- Printer seconds used tracking
- Creating parts usage events

### Changed
- Storing user data in proper directory
- Creating default data files if there is no user data

### Internal
- Removed old impossible to access files from v0.1.0
- Separated interface.py into 5 different files
- Issue and PR templates created
- Moved code into src/filament_tracker
- Added uv_build backend to pyproject
- Reformated all code with ruff
- Environment variables added
- Refactored all variable, function, file, folder, and csv column names to snake_case
- Added metadata.json
- Added type hints and docstrings

## [0.4.0] - 2026-03-18

### Added
- Purchasing, editing, and viewing info for parts

## [0.3.0] - 2026-03-16

### Added
- Seller information tracking to all purchasing
- Purchasing, editing, and viewing info for filament, filament dryers, and reusable spools
- Creating drying events that automatically update filament time last dried

## [0.2.0] - 2026-03-08

### Added
- Adding, editing, and viewing info for printers, hotends, buildplates, and ams
- Creating maintenance events for printers, hotends, buildplates, and ams
- Viewing purchases
- Multi item purchases

### Removed
- All v0.1.0 interface code
- All v0.1.0 data files

## [0.1.0] - 2026-02-27

### Added
- Adding new filament rolls to database
- Editing and updating all info for filament rolls
- Viewing all info for filament rolls
- Adding prints to print history, and automatically reducing amount of filament left
- Viewing print history

### Internal
- Created csv helper functions