# Python Web Application

## Framework Choice
I chose **Flask** because it is a lightweight and beginner-friendly web framework suitable for small applications.

## Best Practices
- Modular code structure: Routes are defined clearly in `app.py`.
- Code readability: Followed PEP 8 standards.
- Dependency management: Used `requirements.txt` for tracking dependencies.
- Testing: Verified the application updates the time correctly.

## Testing and Code Quality
- Manual testing in the browser confirmed the correct Moscow time display.
- Debugging enabled during development to catch errors early.

# Unit Testing Best Practices

## Best Practices Applied
- Focused on testing critical functionalities.
- Used `unittest` for its simplicity and integration with CI tools.
- Ensured tests are isolated and independent.
- Verified both successful and edge cases.

## Unit Tests Summary
- Created tests for `home()` function to check if it outputs a valid time string.
