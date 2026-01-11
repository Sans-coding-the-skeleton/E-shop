"""
Project: E-shop (D1 Repository Pattern)
Author: [Your Name]
Date: 2026-01-05
School: SPŠE Ječná
Description: Main entry point for the application.
"""

from src.app import app

def main():
    print("Starting E-shop Application...")
    print("Go to http://127.0.0.1:5000 to use the application.")
    app.run(debug=True)

if __name__ == "__main__":
    main()
