# SHIELD Portal

## Overview

Minimal Flask portal serving templates and static assets.

## Quick start

1. Install dependencies in a virtual environment.
2. Create a `.env` file (see example below).
3. Run `flask run`.

## Example `.env`
```
FLASK_ENV=development
SECRET_KEY=[redacted]
```

## Security note

A real admin panel secret was once committed here by mistake. It has been revoked and replaced. Always store secrets in environment variables and exclude `.env` from version control.
