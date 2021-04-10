# Stock XChange
An app to bring together a community of investors ready and willing to help each other grow.

## Requirements
1. `npm install`
2. `pip install -r requirements.txt`
3. `npm install react-router-dom`

## Setup
1. Run `echo "DANGEROUSLY_DISABLE_HOST_CHECK=true" > .env.development.local` in the project directory

## Run Application
1. Run command in terminal (in your project directory): `python app.py`
2. Run command in another terminal, `cd` into the project directory, and run `npm run start`
3. Preview web page in browser '/'

## Deploy to Heroku

1. Create a Heroku app: `heroku create --buildpack heroku/python`
2. Add nodejs buildpack: `heroku buildpacks:add --index 1 heroku/nodejs`
3. Push to Heroku: `git push heroku main`

## Linting 
+ W0603
+ C0413 (wrong-import-position) because in order for the app.py to work correctly we have to import a table after some sqlalchemy configuration code
+ W1508 