check the container:
`docker compose ps`

if its not there, use `docker compose up -d` (the `-d` is to run it in the background detached and just return the command output)

to run the code use `uv run --env-file .env <filename>.py` 

