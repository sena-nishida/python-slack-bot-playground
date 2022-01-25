# python-slack-bot-playground

## Requirements

- Python3
- Slack
- Heroku

## Usage

### 1. Prepare source code.

Fork [this](https://github.com/Doarakko/python-slack-bot-playground) repository.

```sh
git clone https://github.com/<id>/python-slack-bot-playground
```

### 2. Create Slack App using `manifest.yml`.

Go to [here](https://api.slack.com/apps) and create from an app manifest.

Get App-Level Token(xapp-aaaa) with connections:write and Bot User OAuth Token(xoxb-bbbb).

### 3. Edit `.env`.

```sh
cp .env.example .env
```

Enter SLACK_APP_TOKEN and SLACK_BOT_TOKEN.

### 4. Install library

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 5. Run

```sh
python app.py
```

## Deploy on Heroku

### 1. Commit and push.

```
git add -A
git commit -m "Go"
git push origin main
```


### 2. Create Heroku app and set config and buildpack.

Create app from [here](https://dashboard.heroku.com/new-app).

Set `SLACK_APP_TOKEN` and `SLACK_BOT_TOKEN`, add Python buildpack from `Settings` tab.

### 3. Deploy

Connect to GitHub and choose repository from `Deploy` tab.

Click `Enable Automatic Deploys` and `Deploy Branch`.
