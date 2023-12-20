# Node exporter textfile colllector example

This directory contains examples and example configuration for the Prometheus node exporter [textfile collector](https://github.com/prometheus/node_exporter/blob/master/README.md#textfile-collector). Inspired from this [article](https://www.robustperception.io/using-the-textfile-collector-from-a-shell-script/).

## metrics-generator shell script

This simple script generates 2 metrics with random values, each with 2 dimensions (label values), in the [Prometheus text-based exposition format](https://github.com/prometheus/docs/blob/main/content/docs/instrumenting/exposition_formats.md#text-based-format) and write those in a .prom text file so they can be collected by the node exporter.

Initially, the metrics are written to a temporary file which is then moved/renamed to .prom. The reason this is done in 2 steps is prevent the node exporter only partially reading the new values as they are generated line by line. Moving the temporary file at once make sure the operation is atomic. Another way to do this could be to use `sponge` from [moreutils](https://joeyh.name/code/moreutils/) instead.

