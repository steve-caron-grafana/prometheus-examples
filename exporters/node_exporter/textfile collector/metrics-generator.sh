#!/bin/bash

# Set this variable to the directory where you put the metrics prom files.
TEXTFILE_COLLECTOR_DIR=/home/ubuntu/custom-prom-metrics

# Write out metrics to a temporary file.
END="$(date +%s)"
cat << EOF > "$TEXTFILE_COLLECTOR_DIR/hw-metrics.prom.$$"
cpu_temp{cpu="1"} $((90 + RANDOM % 10))
cpu_temp{cpu="2"} $((90 + RANDOM % 10))
fan_speed{fan="A"} $((500 + RANDOM % 50))
fan_speed{fan="B"} $((500 + RANDOM % 50))
EOF

# Rename the temporary file atomically.
# This avoids the node exporter seeing half a file.
mv "$TEXTFILE_COLLECTOR_DIR/hw-metrics.prom.$$" \
  "$TEXTFILE_COLLECTOR_DIR/hw-metrics.prom"