# Project overview and usage instructions

"""
# MongoDB Database Setup for FastAPI Project

This folder contains scripts for creating and managing MongoDB collections for the `MyProjectDB` database used by the FastAPI backend.

## 📁 Structure

- `.env.example`: Template for MongoDB connection string
- `db_setup.py`: Creates initial collections
- `test_insert.py`: Adds sample data to a collection
- `list_collections.py`: Lists all collections
- `drop_collections.py`: Deletes all collections (for resetting DB)
- `requirements.txt`: Dependencies

## 🛠 Setup Instructions

1. Copy `.env.example` to `.env` and update with your real MongoDB URI.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Create collections:
    ```bash
    python db_setup.py
    ```
4. (Optional) Insert test data:
    ```bash
    python test_insert.py
    ```
5. (Optional) View collections:
    ```bash
    python list_collections.py
    ```
6. (Optional) Drop/reset collections:
    ```bash
    python drop_collections.py
    ```

## 🔒 Security Note
- Never commit `.env` to GitHub
- Use `.env.example` for sharing structure with the team
- Limit IP access and create secure MongoDB users for deployment

"""
