#!/bin/sh
gunicorn --worker-class geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 app:app --bind=0.0.0.0:5000 --reload
