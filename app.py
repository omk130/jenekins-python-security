"""
Simple greeting module for Jenkins pipeline demo.
"""

def greet(name):
    """Print a greeting message for the given name."""
    print(f"Hello {name}")


if __name__ == "__main__":
    greet("Jenkins")

