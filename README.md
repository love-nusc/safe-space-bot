# safe-space-bot

## How to run:

### Docker (Recommended)
1. Download [Docker](https://www.docker.com/products/docker-desktop/) (Docker Desktop recommended)
2. Go to [BotFather](https://telegram.me/BotFather) and create a bot.
3. Create a `.env` file with the given telegram bot key.
4. Create a Docker image: `docker build .`
5. Run the Docker image with the dotenv file: `docker run --env-file <image_name>`
   - You can see the list of Docker images with `docker image list`
6. See the Telegram bot working!