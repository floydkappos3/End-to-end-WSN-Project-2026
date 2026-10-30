# End-to-End Wireless Sensor Network

**TinyOS / nesC · Java · MongoDB · Python / Flask · Jupyter**

University coursework connecting embedded sensing, data ingestion, a web dashboard and a regression notebook.

## Data pipeline

TelosB / IRIS sensor nodes → TinyOS base station → Java ingestion → MongoDB → Flask dashboard and notebook analysis.

## What is included

| Layer | Implementation |
| --- | --- |
| Embedded sensing | TinyOS sampler/base applications and sensor interfaces under `examples/Sensing/` |
| Data collection | [Java ingestion application](examples/Sensing/java/SensingApp.java) |
| Storage | MongoDB collection `wsn_database.sensor_data` |
| Visualization | [Flask dashboard](app.py): latest 100 records or full history; refreshes every 3 seconds |
| Analysis | [Linear regression notebook](Question4_LinearRegression.ipynb) |

## Quick start: dashboard

Use a local Python environment with Flask and PyMongo installed. Start MongoDB on `localhost:27017` and populate the collection through the Java acquisition path.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install flask pymongo
python app.py
```

Open `http://localhost:5000`. The dashboard requires records with `id`, `count`, `temp`, `humidity`, `photo` and `solar` fields.

For mote setup, flashing commands, SerialForwarder and the original coursework report, see the [preserved setup guide and report](docs/SETUP_AND_COURSEWORK_REPORT.md).

## Academic provenance

This repository is a fork of [IoTLabUpatras/End-to-end-WSN-Project-2026](https://github.com/IoTLabUpatras/End-to-end-WSN-Project-2026). The starter examples and setup instructions come from that teaching repository; this fork also contains the coursework report, acquisition work, Flask dashboard and analysis notebook. The commit history records changes; the whole starter codebase is not claimed as original work.

## Reproducibility

The repository includes historical hardware setup instructions and generated build outputs. Hardware flashing, MongoDB ingestion and notebook execution were not rerun during the documentation update on 30 October 2026.
