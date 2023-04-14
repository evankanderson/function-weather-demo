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

# Using / Running the Demo

To run the demo, simply upload a CSV file in `city, state, zip` format to the
URL of the ingest resource as a POST.  Note that if you are using `curl`, you
need to use the `--data-binary` flag to avoid doing form encoding.  For example:

```bash
curl --data-binary @cities.csv https://ingest.myns.mytapcluster.dev
```

You can then open the Redis Commander URL, and you should see the different
zipcodes populate as the job runs.
