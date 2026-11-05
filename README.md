# Python-Test

## Configuration

Set `FLASK_SECRET_KEY` to a long, random value when running the application in
an environment where sessions must remain valid across restarts:

```bash
export FLASK_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"
python app.py
```

When the variable is not set, the application generates a random key for the
current process instead of using a shared hard-coded secret.