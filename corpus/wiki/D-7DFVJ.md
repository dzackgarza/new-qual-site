---
schema: qual/card@1
id: D-7DFVJ
kind: definition
title: "Meromorphic"
classification:
  areas:
  - complex-analysis
  topics:
  - meromorphic-functions
  - poles
relations: []
review: draft
---

::: {.definition title="Meromorphic"}
A function $f:\Omega\to\CC$ is *meromorphic* iff there exists a sequence $\theset{z_n}$ such that

- $\theset{z_n}$ has no limit points in $\Omega$.

- $f$ is holomorphic in $\Omega\setminus\theset{z_n}$.

- $f$ has poles at the points $\theset{z_n}$.

Equivalently, $f$ is holomorphic on $\Omega$ with a discrete set of points delete which are all poles of $f$.
:::
