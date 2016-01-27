#!/usr/bin/env bash

for m in $(seq 100); do python3 simulate.py 10 fair_collision $m 0 300; done > 10_fair_0.0 &&
for m in $(seq 100); do python3 simulate.py 10 bad_collision $m 0 300; done > 10_bad_0.0 &&
for m in $(seq 100); do python3 simulate.py 10 very_bad_collision $m 0 300; done > 10_very_bad_0.0 &&
for m in $(seq 100); do python3 simulate.py 10 altruistic_collision $m 0 300; done > 10_altruistic_0.0
