<!-- ## Magix Support Lab Management API -->

### File and Folder Structure

```shell
/migrations # Migration files
/apis # Routes
    /base.py # Where all the routes are grouped
    /routes # Routes
/config # Main configuration
    /config.py # configurations
/core
    /entity # entity
    /protocol # abstract of repository
    /services # services
/exceptions # Custom exceptions
/infrastructure
    /models # Database table models
    /repository # All database related operations/functions
    /session.py # Database session
    /base_class.py # Base Class for table models
    /base_mixin.py # Base Mixin for timestamp and created by
    /base_repo.py # Base Class for repository with basic CRUD features
    /base.py # Where all table models are grouped
/schemas # Request and response models
/utils # Services
    /hashing.py # Hashing
    /JWTtoken.py # JWTtoken
    /oauth2.py # Oauth2
main.py # App Entry Point
.env.example # Example for ".env"
```

### Development setup

First create a directory then create a virtual environment in it (PLEASE USE VIRTUAL ENVIRONMENT).

```shell
python3 -m venv <your-env-name>
```

To activate your virtual environment go to

#### On Window :

```shell
<your-env-name>\Scripts\activate.bat
```

#### On Unix or MacOs :

```shell
source <your-env-name>/bin/activate
```

Finally git clone the repository.

```shell
git clone https://github.com/thamardaw/magix-support-lab-management-api.git
```

Then go into the cloned folder and install requirements (we will be continue working on this directory). While installing setup the ".env" file.

```shell
pip install -r requirements.txt
```

<!-- For our database migrations we will be using alembic. Don't worry it is already in requirements.txt so it is installed. Now let's initailize alembic.

```shell
alembic init alembic
```

After initailized, some changes need to make.

Go to alembic.ini and add your database string / URI.

```shell
sqlalchemy.url = <your-database-string>
```

Then go to alembic/env.py.

```shell
# comment out "target_metadata = None" and add this
from infrastructure.base import Base
target_metadata = Base.metadata
```

All changes need for alembic is done. Let's generate your migrations with alembic's help. You will have to run this command every time you add new models or you make changes to your models.

```shell
# this auto generate the migration files
alembic revision --autogenerate -m "init"
# to create or update the models to database
alembic upgrade head
``` -->

Migrate your models into database.

```shell
# to create or update the models to database
alembic upgrade head
```

Now let's start your server.

```shell
uvicorn main:app --reload
```

#### Useful commands

if you installed new packages during development, don't forget to update the requirement.

```shell
pip freeze > requirements.txt
```

This command is for auto generating the migration files if you add new models or make changes to your existing model. Then don't forget to mirgrate the changes.

```shell
alembic revision --autogenerate -m "init"
```
