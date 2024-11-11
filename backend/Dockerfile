# maintainer info
FROM python:3.12-slim-bullseye
LABEL maintainer="carrergt@gmail.com"

WORKDIR /app
RUN apt update && apt install -y libmagic-dev && pip3 install uv

CMD ["uv","run","fastapi", "run", "--port", "8000"]