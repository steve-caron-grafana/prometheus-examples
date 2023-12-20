# Node exporter textfile colllector example

This directory contains examples and example configuration for the Prometheus node exporter [textfile collector](https://github.com/prometheus/node_exporter/blob/master/README.md#textfile-collector). Inspired from this [article](https://www.robustperception.io/using-the-textfile-collector-from-a-shell-script/).

## metrics-generator shell script

This simple script generates 2 metrics with random values, each with 2 dimensions (label values), in the [Prometheus text-based exposition format](https://prometheus.io/docs/instrumenting/exposition_formats/#text-based-format) and write those in a `.prom` text file so they can be collected by the node exporter.

Initially, the metrics are written to a temporary file which is then moved/renamed to a `.prom` file. The reason this is done in 2 steps is to prevent the node exporter only partially reading the new values as they are generated line by line. Moving the temporary file at once make sure the operation is atomic. Another way to do this could be to use **sponge** from [moreutils](https://joeyh.name/code/moreutils/) instead.

To generate metrics continuously (e.g. every minute), you can add this script to a cron job:

```crontab -e```

and append this line, replacing `<working_directory>` with the directory path you cloned the repo in.

`* * * * * <working_directory>/exporters/node_exporter/textfile collector/metrics-generator.sh`

## Node exporter configutation for the textfile collector

To use the **textfile** collector with the node exporter, you need to set the following flag on the command line launching the exporter: `--collector.textfile.directory=<prom file directory>`, replacing `<prom file directory>` with the path to the directory where the `.prom` files are located.

## Grafana agent configuration for the textfile collector

If you use the Grafana agent with the [node_exporter integration](https://grafana.com/docs/agent/latest/static/configuration/integrations/node-exporter-config/), the textfile collector is enabled by default and you only need to specify the directory in the agent config file. For example:

```
integrations:
  node_exporter:
    enabled: true
    textfile_directory: "<prom file directory>"
```

and then restart the agent.
