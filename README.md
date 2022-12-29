# Template for Telegram Bots

Template repo for Telegram bots using the library python-telegram-bot.

[![Deploy docs](https://github.com/Jordilavila/Template_For_Telegram_Bots/actions/workflows/deploy-docs.yml/badge.svg?branch=main)](https://github.com/Jordilavila/Template_For_Telegram_Bots/actions/workflows/deploy-docs.yml)

## 🛠️ How to use

1. Clone this repo or make a fork of it
2. Install the dependencies with `pip install -r requirements.txt`
3. Create a new bot with the BotFather and get the token
4. Create an enviroment file with `cp .env.example .env` and fill the token
5. Run the bot with `python3 my_telegram_bot.py`

### 📝 Environment variables

The environment variables are stored in the `.env` file. The following variables are required:

- TELEGRAM_BOT_TOKEN: The token

The other variables are set by default. You can change them if you want but it's not necessary and it's not recommended.

###  Prerelase

The prerelease version is the version that is in development. It's not recommended to use it in production.
The prereleases are automated with GitHub Actions. The prerelease version is the version of the main branch.

### Release

The release version is the version that is stable. It's recommended to use it in production.
The releases are automated with GitHub Actions. The release version is the version of the main branch.

### Notify on Telegram when a new release is available

You can use your bot to notify when a new release is available of your code or any other project. You can do it with the GitHub Action [auto-release.yml](.github/workflows/auto-release.yml). Simply add the following secrets to your repo:

- TELEGRAM_TO: The chat id of the user or group where you want to send the notification.
- TELEGRAM_TOKEN: The token of your bot.

And then, uncomment the following lines in the file [auto-release.yml](.github/workflows/auto-release.yml):

```yaml
notify_on_telegram:
  name: "Notify on Telegram"
  runs-on: "ubuntu-latest"
  needs: "tagged-release"
  steps:
    - name: "Send Telegram message"
      uses: "appleboy/telegram-action@master"
      with:
        to: "${{ secrets.TELEGRAM_TO }}"
        token: "${{ secrets.TELEGRAM_TOKEN }}"
        format: "html"
        dissable_web_page_preview: true
        message: |
          "Updates in <strong>${{ github.event.repository.name }}</strong>!

          A new version has been published: <code>${{ github.ref_name }}</code>"

          You can see the changes in the <a href="https://github.com/${{ github.repository }}/releases/latest">changeLog</a>.
```

And that's all. Now, when you create a new release, the bot will notify you.

### Auto documentation

You can use the GitHub Action [deploy-docs](.github/workflows/deploy-docs.yml) to automatically generate the documentation of your code and publish it in GitHub Pages. You need the `mkdocs.yml` file and the file `mkdocs-requirements.txt` in the root of your repo. You can see both examples in this repo.

The theme of the documentation is [mkdocs-material](https://squidfunk.github.io/mkdocs-material/). You can change it if you want.

## 📚 Dependencies

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

## 📖 Documentation

- [python-telegram-bot](https://python-telegram-bot.readthedocs.io/en/stable/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

## 📝 License

This project is under the Creative Commons Zero v1.0 Universal license. See the [LICENSE](LICENSE) file for more details.
