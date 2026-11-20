# Takes the screenshots of the build steps inside a container, so the host desktop is not used.
# Build context: the project root. The browser tooling is not a dependency of the project.
FROM python:3.13-slim

WORKDIR /app
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright
RUN apt-get update && apt-get install -y --no-install-recommends libatomic1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY pyproject.toml README.md ./
COPY src ./src
RUN python -m pip install --upgrade pip \
    && python -m pip install . playwright \
    && python -m playwright install --with-deps chromium

COPY tools/screenshots/capture.py ./capture.py
RUN useradd --create-home shots && mkdir /out && chown shots /out
USER shots
ENV OUT_DIR=/out
CMD ["python", "capture.py"]
