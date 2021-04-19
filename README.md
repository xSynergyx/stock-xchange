# Sprint 1 Heroku link: https://intense-tor-77466.herokuapp.com
# Stock XChange
An app to bring together a community of investors ready and willing to help each other grow.

## Requirements
1. `npm install`
2. `pip install -r requirements.txt`
3. `npm install --save react-router-dom`
4. `npm install --save react-google-login`
5. `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs` (enter yes on all prompts)
6. `pip install psycopg2-binary`
7. `pip install Flask-SQLAlchemy==2.1`

## Setup
1. Run `echo "DANGEROUSLY_DISABLE_HOST_CHECK=true" > .env.development.local` in the project directory

## Run Application
1. Run command in terminal (in your project directory): `python app.py`
2. Run command in another terminal, `cd` into the project directory, and run `npm run start`
3. Preview web page in browser '/'

## Technologies, Frameworks, Libraries, and APIs
### Modules
+ Flask, Requests, Python-dotenv, Random, Time, Datetime, and Pandas
### IEX Cloud API
1. On the [IEX Cloud page](https://iexcloud.io/) make a free account
2. Once signed up and logged in, go to your account dashboard and click on API Tokens
3. You are given a real api key that counts against your monthly api calls and a sandbox api key that gives you unlimited calls with fake data. To access the real API token, click the 'Sandbox View' switch to off. To access the sandbox token, switch it to off

### New York Times API
1. On the [NYTimes page](https://developer.nytimes.com/) make a free NYT developer account
2. After logging in, go to 'Apps' and click 'New Apps'
3. Create the app and enable all APIs and create the API key

### Google Login API
1. On the Google [credentials page](https://console.cloud.google.com/apis/credentials) create a project
2. Then click 'Create credentials' and select 'OAuth Client ID'
3. Name the OAuth client
4. Get the Client ID
4. Provide required Redirect URI's (local routes can be added for development)

## Deploy to Heroku

1. Create a Heroku app: `heroku create --buildpack heroku/python`
2. Add nodejs buildpack: `heroku buildpacks:add --index 1 heroku/nodejs`
3. Push to Heroku: `git push heroku {optional_branch_name}:main`

### Heroku Database setup
1. Create remote DB: `heroku addons:create heroku-postgresql:hobby-dev`
2. Get database URL: `heroku config`
3. export database URL: `export DATABASE_URL='{insert_database_url_here}` (no curly braces)

## Linting 
+ E1101 (import-error) because unites files function correctly, which means that the file successfully imported
+ W0603 (global-statement)
+ C0413 (wrong-import-position) because in order for the app.py to work correctly we have to import a table after some sqlalchemy configuration code
+ W1508 (invalid-envvar-default)
+ C0200 (consider-using-enumerate)
+ R0801 (duplicate-code)
+ E1101 (no-member)
