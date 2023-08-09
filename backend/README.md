# Genshin Impact Characters Analyzer Backend

## Description

The server part of the application, which is responsible for the game logic and works with the database.

## Install dependencies

The server part is downloaded automatically when the repository is cloned.

However, to run it, you will need libraries, the list of which is attached as a `requirements.txt` file.

Use the following command to install them:

```pycon
cd backend
pip install -r requirements.txt
```

## Run

The backend is written using the FastAPI framework. The application is launched using uvicorn.

Use this command to start the server side of the application:

```pycon
cd backend
python start.py
```

Also, a less preferred launch version (because the settings are read from the CLI, and not from .env):

```pycon
cd backend
python -m uvicorn app.main:characters_analyzer --reload --host <host> --port 8080
```

***

## Documentation

### Code documentation

The project code is covered by documentation, which can be viewed by running:

```pycon
cd backend
python -m pydoc <name>
```

Where `name` is the name of a module, package, function, class, etc.

### API documentation

Also, using the capabilities built into FastAPI, the API documentation was generated, available at the link:

* **Swagger OpenAPI:** `http://<host>:8080/docs`;

* **ReDoc:** `http://<host>:8080/redoc`.