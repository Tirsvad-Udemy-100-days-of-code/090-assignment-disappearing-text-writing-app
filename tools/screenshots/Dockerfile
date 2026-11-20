# Takes the screenshots of the build steps inside a container, so the host desktop is not used.
# Build context: the project root. The browser tooling is not a dependency of the project.
FROM python:3.13-slim

WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends libatomic1 \
    && rm -rf /var/lib/apt/lists/*
COPY pyproject.toml README.md ./
COPY src ./src
RUN python -m pip install --upgrade pip \
    && python -m pip install . playwright \
    && python -m playwright install --with-deps chromium

COPY tools/screenshots/capture.py ./capture.py
ENV OUT_DIR=/out
# Root is needed to write into the folder mapped from the host; the container is throwaway.
# nosemgrep: dockerfile.security.missing-user.missing-user
CMD ["python", "capture.py"]
