#!/usr/bin/env bash

for p in $(seq 9); do for m in $(seq 100); do python3 simulate.py 10 fair_collision bad_collision $m 0.$p 300; done > result/10_fair_bad_$p.csv ; done
for p in $(seq 9); do for m in $(seq 100); do python3 simulate.py 10 fair_collision very_bad_collision $m 0.$p 300; done > result/10_fair_verybad_$p.csv ; done
for p in $(seq 9); do for m in $(seq 100); do python3 simulate.py 10 altruistic_collision bad_collision $m 0.$p 300; done > result/10_alt_bad_$p.csv ; done
for p in $(seq 9); do for m in $(seq 100); do python3 simulate.py 10 altruistic_collision very_bad_collision $m 0.$p 300; done > result/10_alt_verybad_$p.csv ; done
for p in $(seq 9); do for m in $(seq 100); do python3 simulate.py 10 fair_collision altruistic_collision $m 0.$p 300; done > result/10_fair_alt_$p.csv ; done
for p in $(seq 9); do for m in $(seq 100); do python3 simulate.py 10 bad_collision very_bad_collision $m 0.$p 300; done > result/10_bad_verybad_$p.csv ; done