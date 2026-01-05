# E-shop (D1 Repository Pattern)

School project for PV (4th Year) - E-shop with SQL database.

## Requirements
- Python 3.x
- MySQL Server

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Import the database schema:
   - Use the `src/database/schema.sql` file in your MySQL client.
3. Configure the database connection in `config.json`.

## Running the Application
Always run the application from the project root directory as a module:
```bash
python -m src.main
```