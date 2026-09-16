---
schema: qual/card@1
id: P-TRIV-PR12
kind: problem
title: Poisson arrivals at a counter with dead time
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 12, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash contains one or more nonprinting control bytes at this source position; they were removed from the authored card as nonsemantic extraction artifacts.
---

::: problem
In nuclear physics, the intensity of a particle source is measured with Geiger-Muller counters.
A particle entering the counter generates a discharge in it that lasts time τ , during which the counter does not record any particles entering the counter.
Find the probability that the counter will count all particles entering it during time t if the following conditions are fulfilled:

(a) the particles enter the counter independently;

(b) the probability that during the time interval from t to $t + \Delta t .$ , k particles entered the counter is given by

$$
p _ { k } ( t , t + \Delta t ) = \frac { ( a \Delta t ) ^ { k } e ^ { - a \Delta t } } { k ! } ,\tag{43}
$$

where a is the rate.
:::
