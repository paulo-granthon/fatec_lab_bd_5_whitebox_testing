# Whitebox Testing

This project demonstrates whitebox testing using Python and `pytest`. The core
of the project consists of five example functions located in the
`example_functions` directory, which are tested for code coverage, path
coverage, and other whitebox testing principles in the `tests` directory.

## Project Structure

```css
whitebox_testing_project/
├── example_functions/
│   ├── function1.py
│   ├── function2.py
│   ├── function3.py
│   ├── function4.py
│   └── function5.py
├── tests/
│   ├── test_function1.py
│   ├── test_function2.py
│   ├── test_function3.py
│   ├── test_function4.py
│   └── test_function5.py
├── requirements.txt
├── Makefile
└── README.md
```

### Directories and Files

- `example_functions/`: Contains the example functions that are being tested with
  whitebox testing techniques.
- `tests/`: Contains test files for each example function. These tests focus on
  exploring all execution paths and ensuring full code coverage.
- `requirements.txt`: A list of Python packages required to run the project
  (includes `pytest`).
- `Makefile`: A file containing various commands to manage testing tasks, such as
  running tests with coverage reports.

## Requirements

Before running the tests, ensure you have Python 3.6+ installed.

### Installing Dependencies

You can install the required dependencies by creating a virtual environment and
installing the packages listed in `requirements.txt`. This can be done manually or
using the provided `Makefile`.

## Running the Project

You have two ways to run the project:

### 1. Using the `Makefile` (Recommended)

The `Makefile` automates the process of setting up the environment, installing
dependencies, and running the tests. It includes the following commands:

- **`make test`**: Runs all tests with coverage, reporting the results in the
  terminal.
- **`make test-html`**: Runs all tests with coverage and generates an HTML report.
- **`make test-xml`**: Runs all tests with coverage and generates an XML report
  (useful for CI tools).
- **`make clean`**: Cleans up the generated HTML report.

1. Clone the repository:
2. Run the tests using the `Makefile`:

   ```css
   make test
   ```

   This command will run all tests with coverage and display the results in the
   terminal. If you need a more detailed report, you can use `make test-html` or
   `make test-xml`.

3. To clean up the generated HTML reports:

   ```css
   make clean
   ```

### 2. Manually Setting Up and Running the Project

If you prefer to manually set up the environment and run the tests:

1. Clone the repository:
2. Create a virtual environment:

   ```css
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   - On Linux/Mac:

     ```css
     source venv/bin/activate
     ```

   - On Windows:

     ```css
     venv\Scripts\activate
     ```

4. Install the dependencies:

   ```css
   pip install -r requirements.txt
   ```

5. Run the tests with `pytest`:

   ```css
   pytest
   ```

## Example Functions

Here is an overview of the example functions tested in the project:

- **function1**: Performs various conditional checks based on two input values.
- **function2**: Uses loops and conditionals to perform mathematical operations.
- **function3**: Involves multiple conditional branches depending on input values.
- **function4**: Uses recursion to calculate a result based on input.
- **function5**: Checks input values against a series of conditions and performs
  different actions.

## Whitebox Testing Approach

In this project, **whitebox testing** is applied by ensuring that all branches,
paths, and code statements of the functions are tested. The tests are designed to
cover:

- **Code coverage**: Ensuring every line of code is executed during testing.
- **Path coverage**: Ensuring all possible execution paths are tested.
- **Branch coverage**: Ensuring both true and false branches of conditional
  statements are tested.

Each test case aims to explore the internal workings of the functions and verify
that the implementation is correct and performs as expected under various conditions.
