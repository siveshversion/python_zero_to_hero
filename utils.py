import sys
import contextlib
import io
import traceback

def execute_code(code):
    """
    Executes the provided Python code and returns the output.
    Captures stdout and stderr.
    """
    output_buffer = io.StringIO()
    
    try:
        # Redirect stdout to capture print statements
        with contextlib.redirect_stdout(output_buffer):
            # Execute the code
            exec(code, {'__name__': '__main__'})
        return output_buffer.getvalue()
    except Exception:
        # Capture the traceback if an error occurs
        return f"{output_buffer.getvalue()}\nError:\n{traceback.format_exc()}"
