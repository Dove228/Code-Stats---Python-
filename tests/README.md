# Code Stats Tests

This directory contains unit tests for the Code Stats project.

## Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_analyzer.py

# Run with coverage
python -m pytest tests/ --cov=src/code_stats
```

## Test Structure

- `test_scanner.py` - Tests for FileScanner class
- `test_analyzer.py` - Tests for CodeAnalyzer class
- `test_exporters.py` - Tests for export functionality
- `test_complexity.py` - Tests for complexity analysis

## Adding Tests

When adding new features, please add corresponding tests:

1. Create test functions with `test_` prefix
2. Use descriptive test names
3. Include docstrings explaining what is being tested
4. Test both positive and negative cases

## Fixtures

Common test fixtures can be found in `conftest.py` if needed.
