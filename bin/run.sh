#!/bin/bash
RTL_433_ARGS="-p 80 -R 50 -R 40"

cd $(dirname $0)/../
. ../../bin/activate
../bin/rtl_433 -q -F json $RTL_433_ARGS | python3 mqtt_route.py
