from prometheus_client import start_http_server, Summary, Counter, Gauge, Histogram
from prometheus_client.utils import INF
import random
import time

# Create a metric to track time spent and requests made.

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Create 3 additional example metrics, one of type Counter, one of type Gauge with 2 labels associated and one of type Histogram with 10 buckets

COUNTER = Counter('my_counter', 'Example metric of type Counter')
GAUGE = Gauge('my_gauge', 'Example metric of type Gauge with 2 labels', ['label1', 'label2']) 
HISTOGRAM = Histogram('my_histogram', 'Example metric of type Histogram', buckets=(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, INF))

# The Summary class provides a time() function we use as a decorator for process_request()

@REQUEST_TIME.time()
def process_request(t):

    """A dummy function that takes some time."""

    time.sleep(t)

if __name__ == '__main__':

    # Start up the server to expose the metrics.

    start_http_server(8000)

    # Initialize the labels

    GAUGE.labels(label1='A', label2='something')
    GAUGE.labels(label1='B', label2='something')

    # Generate some requests, set gauge and histogram to random values and increase counters

    while True:

        process_request(random.random())
        GAUGE.labels(label1='A', label2='something').set(4.0 + random.random())
        GAUGE.labels(label1='B', label2='something').set(5.0 + random.random())
        COUNTER.inc()
        HISTOGRAM.observe(random.random() * 100.0)