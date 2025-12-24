FROM python:3.12-slim AS builder

WORKDIR /app
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim

WORKDIR /app
ENV PATH="/venv/bin:$PATH"
COPY --from=builder /venv /venv
COPY src/ src/

ENTRYPOINT ["python", "-m", "src.main"]
