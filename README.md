# pymongo-schema

A Python SDK for exporting MongoDB schema metadata without copying the actual data.

## Installation

```bash
pip install pymongo-schema
```

## Usage

### Export MongoDB Schema

Export the schema of specified databases to a JSON file:

```bash
pymongo-schema export --uri mongodb://user:password@database.host1.com:27017/admin --databases test2,testIgnore --output schema.json
```

### Arguments

- `--uri`: MongoDB connection string
- `--databases`: Comma-separated list of databases to export
- `--output`: Output file path for schema (e.g., `schema.json`)

### Example Output

When exporting, you'll see:
```bash
Schema exported to schema.json
```

### Permissions

Ensure your user has appropriate read permissions for the specified databases.