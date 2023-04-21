# ModelOps Prototyping Playground

This repo aims to provide example setups that can be used to build towards streamlined Model Ops workflows. This initial version provides a docker-compose setup that provides the following services:
* **trino** server - unified SQL query interface
* **iceberg service** - high performance columnar table storage capability
* **hive metastore** collects metadata from connected data sources for heuristic query performance optimization
* **minio server** - cloud provider agnostic object storage system with S3 compatible interface

All of these services can be accessed via the trino interface. An [example notebook](notebooks/demo-trino.ipynb) showing output of an example connection and initial queries is provided for demonstration.

## Getting started

