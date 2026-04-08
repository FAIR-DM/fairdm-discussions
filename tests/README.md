# FairDM Discussions - Tests

This directory contains the test suite for the fairdm-discussions plugin.

## Structure

The test directory mirrors the structure of the `fairdm_discussions/` package:

```
tests/
├── __init__.py
├── conftest.py                     # Pytest fixtures
├── test_apps.py                    # App configuration tests
├── test_e2e.py                     # End-to-end integration tests
├── test_integration.py             # django-comments-xtd integration tests
├── test_plugins.py                 # Plugin registration and view tests
├── test_serializers.py             # Custom serializer tests
├── test_settings.py                # Settings configuration tests
└── test_templatetags/
    ├── __init__.py
    └── test_fairdm_discussions.py  # Template tag tests
```

## Running Tests

### Run all tests:
```bash
poetry run pytest
```

### Run with verbose output:
```bash
poetry run pytest -v
```

### Run specific test file:
```bash
poetry run pytest tests/test_plugins.py
```

### Run specific test:
```bash
poetry run pytest tests/test_plugins.py::TestDiscussionPluginRegistration::test_discussion_plugin_registered_to_models
```

### Run with coverage:
```bash
poetry run pytest --cov --cov-report=html
```

View the coverage report by opening `htmlcov/index.html` in your browser.

### Run tests matching a pattern:
```bash
poetry run pytest -k "plugin"
```

### Run with output from print statements:
```bash
poetry run pytest -s
```

## Test Categories

### Plugin Tests (`test_plugins.py`)
- Plugin registration to all FairDM models
- Plugin attributes and configuration
- Menu integration
- URL generation
- Permission checks (waffle switch)
- View rendering
- Context data
- Class inheritance

### Serializer Tests (`test_serializers.py`)
- Custom serializer fields (user_name, user_url)
- Anonymous user handling
- User with full name handling
- Standard comment fields

### Integration Tests (`test_integration.py`)
- Comment creation on all FairDM model types
- Multiple comments per object
- Comment retrieval
- Threaded (nested) comments

### End-to-End Tests (`test_e2e.py`)
- Complete workflow from view access to comment creation
- Menu appearance across all models
- Waffle switch workflow
- Multiple users commenting
- URL consistency

### App Configuration Tests (`test_apps.py`)
- App config name and installation
- Custom serializer registration in app.ready()

### Settings Tests (`test_settings.py`)
- COMMENTS_APP configuration
- INSTALLED_APPS verification
- django-comments-xtd settings
- Icon configuration

### Template Tag Tests (`test_templatetags/test_fairdm_discussions.py`)
- comments_xtd_frontend tag rendering
- Version string in output
- Static URL generation

## Fixtures

The `conftest.py` file provides the following fixtures:

- `user` - Standard test user
- `admin_user` - Admin/superuser
- `discussion_enabled` - Waffle switch enabled
- `discussion_disabled` - Waffle switch disabled
- `project` - Test project instance
- `dataset` - Test dataset instance
- `sample` - Test sample instance
- `measurement` - Test measurement instance

## Coverage Requirements

- Aim for >90% code coverage
- All new features must include tests
- Test both happy paths and error cases
- Test edge cases and boundary conditions

## Writing New Tests

When adding new tests:

1. Follow the existing structure (mirror `fairdm_discussions/` directory)
2. Use descriptive test names: `test_<what_it_tests>`
3. Use pytest fixtures from `conftest.py`
4. Mark database tests with `@pytest.mark.django_db`
5. Use Arrange-Act-Assert structure
6. Add docstrings explaining what the test verifies

Example:
```python
@pytest.mark.django_db
def test_new_feature(project, user, discussion_enabled):
    """Test that new feature works correctly."""
    # Arrange
    expected_result = "some value"
    
    # Act
    actual_result = some_function(project, user)
    
    # Assert
    assert actual_result == expected_result
```

## Continuous Integration

Tests are designed to run in CI/CD environments:
- No hardcoded paths or environment assumptions
- Database migrations handled automatically
- All dependencies installed via `poetry install`
- Tests are deterministic (no random failures)
