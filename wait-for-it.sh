#!/bin/bash

host="$1"
shift
cmd="$@"

until mysqladmin ping -h "$host" --silent; do
  echo "Waiting for MySQL..."
  sleep 2
done

sleep 10

exec $cmd
