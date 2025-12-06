[pydantic doc :-](https://docs.pydantic.dev/latest/)

## What is Pydatic:

- Pydantic is a Python library that validates and converts data using type hints.
- It ensures that the incoming data is clean, correct, and in the right format.\*\*

## 📘 Why is Pydantic SUPER USEFUL in AI & ML?

- Your API receives JSON data — Pydantic validates it
- Your model outputs data — Pydantic checks it
- Your config files need proper types — Pydantic fixes them
- Your agent pipelines need structured data — Pydantic ensures it

## SHORT SUMMARY (YOUR QUICK NOTES)
- ✔ Pydantic = Data Validation Library
- ✔ Ensures data types are correct
- ✔ Auto-converts values
- ✔ Raises clean and readable errors
- ✔ Used everywhere in FastAPI, GenAI, ML & Agentic AI
- ✔ Behaves like a strict but helpful data bouncer


### field_validator
- A function that validates or modifies a single field before storing it.

    - Validates one field
    - Runs before model creation
    - Ideal for: email check, trimming strings, checking range, etc.


### model_validator
- A function that validates or modifies the entire model,
using all fields together.

    - Validates whole model

    - Runs after all fields are available
    - Ideal for: password match, dependent fields, global rules

### Field (pydantic module)
- Pydantic’s Field() is used to add validation rules, metadata, default values, constraints, and documentation to individual fields inside a Pydantic model.

- It helps define:
    - Default values
    - Minimum/maximum limits
    - Regex patterns
    - Descriptions
    - Examples
    - Titles
    - Aliases
    - And much more

### computed_field 
- computed_field is a Pydantic decorator used to create read-only fields whose values are automatically calculated from other fields in the model.