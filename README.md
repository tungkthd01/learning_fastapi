# How to Work With GitHub and Multiple Accounts:

    https://code.tutsplus.com/tutorials/quick-tip-how-to-work-with-github-and-multiple-accounts--net-22574

## Push remote with other username

git push https://tungkthd01@github.com/tungkthd01/learning_fastapi.git main
git push "https://your_other_username_at_github@github.com/username/provided path.git/" branch

# Setup vscode in local

## Create venv:

`python -m venv .venv`

active venv windows

`.\.venv\Scripts\activate`

## Get packages with pip

`pip freeze > requirements.txt`

## install packages in local

` pip install -r requirement.txt`

## run fast api

`uvicorn api.main:app --reload --port=9000 --host=0.0.0.0`

# Use alembic

create alembic:
`alembic init alembic`

create revison alembic
`alembic revision --autogenerate -m "create tiet_khi table" `

Run create table in database
`alembic upgrade head`
