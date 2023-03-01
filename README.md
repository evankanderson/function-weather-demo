# function-weather-demo
A sample application using Knative Functions to fetch weather for many cities using the fan-out eventing pattern.

## Setup

```bash
# Install Redis Operator to simplify provisioning
kubectl apply -f manifests

# Create Redis cluster
kubectl apply -f resources

# Create ingester, enricher, and viewer workloads
kubectl apply -f ingest/config/workload.yaml -f fetch/config/workload.yaml -f redis-view/workload.yaml
```

# Using
