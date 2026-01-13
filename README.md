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
   in case of python not being installed run:
   
   winget install Python.Python.3.14

   after that restart your console window   
2. Import the database schema:
   - Use the `src/database/schema.sql` file in your MySQL client.
     
     before running the script create the schema, default name in config is eshop_db
     
     after creating it set it as default schema by right clicking it and selecting the right option
     
3. Configure the database connection in `config.json`.

## Running the Application
Always run the application from the project root directory as a module:
```bash
python -m src.main
```
