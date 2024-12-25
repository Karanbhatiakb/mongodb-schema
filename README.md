# mongo-schema-V2

A Python SDK for exporting MongoDB schema metadata without copying the actual data.

## Installation

```bash
pip install mongo-schema-V2
```

## Usage

### Command Line Interface

```bash
mongo-schema-V2 export --uri mongodb://user:password@database.host1.com:27017/admin --databases test2,testIgnore --output schema.json
```

### Python API

```python
from mongo_schema.exporter import MongoSchemaExporter

# Initialize the exporter with MongoDB connection details
exporter = MongoSchemaExporter(uri="mongodb://localhost:27017", database="test_db")

# Export the schema metadata for the specified database
result = exporter.export_schema(sample_size=10)

# Print the result
print(result)
```

### Arguments

- `--uri`: MongoDB connection string
- `--databases`: Comma-separated list of databases to export
- `--output`: Output file path for schema (e.g., `schema.json`)

### Example Output

```bash
Schema exported to schema.json
```

### Permissions

Ensure your user has appropriate read permissions for the specified databases.
