# Python Zero to Hero App Walkthrough

I have built a Streamlit application that guides you from Python basics to more advanced concepts.

## Features
- **Interactive Learning**: Read about a concept and immediately run code to see it in action.
- **Topic Navigation**: Use the sidebar to switch between different Python topics.
- **Safe Execution**: Code is executed in a controlled environment, capturing output and errors.

## Project Structure
- `app.py`: The main application entry point.
- `content.py`: Contains the educational content (theory and code examples).
- `utils.py`: Handles the code execution logic.
- `test_utils.py`: Verifies that the code execution logic works correctly.

## How to Run

1.  Open your terminal.
2.  Navigate to the project directory:
    ```bash
    cd c:\Users\Sivesh\py_projects\python_zero_to_hero
    ```
3.  Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
4.  The app should open in your default web browser.

## Verification
I have verified the core logic using `test_utils.py`, which confirms that:
- Standard print statements are captured correctly.
- Errors (like division by zero) are caught and displayed nicely.
