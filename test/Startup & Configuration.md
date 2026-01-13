## Scenario 1: Startup & Configuration

**Objective:** Verify application starts and connects to database.
**Pre-conditions:** MySQL server running, Database `eshop_db` created.

1.  **Configure:** Edit `config.json` with incorrect password.
2.  **Run:** Execute `python -m src.main`.
3.  **Expected:** Application prints error message or fails gracefully (check logs/console).
4.  **Fix:** Edit `config.json` to have correct database name and login + password.
5.  **Run:** Execute `python -m src.main`.
6.  **Expected:** Application starts and serves at `http://127.0.0.1:5000`.
