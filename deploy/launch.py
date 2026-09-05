#!/usr/bin/env python
"""HeyJoe launcher: run the unmodified backlot app bound to 0.0.0.0 for Docker."""
import uvicorn
uvicorn.run("backlot.server:app", host="0.0.0.0", port=4750, log_level="warning")
