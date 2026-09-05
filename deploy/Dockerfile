# HeyJoe Filmmaker — OpenMontage Backlot web UI (read-only storyboard of productions)
# Upstream: calesthio/OpenMontage (AGPL-3.0) — running UNMODIFIED, per licensing decision
FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt watchfiles
COPY . .
# Backlot server on 0.0.0.0:4750; projects dir is a named volume so productions persist
ENV PYTHONUNBUFFERED=1
EXPOSE 4750
COPY deploy/launch.py /app/launch.py
CMD ["python", "/app/launch.py"]
