---
schema: qual/card@1
id: P-DQNN6
kind: problem
title: We say a sequence $\{a_n\}$ in $[0,1]$ is equi-distributed if for all…
classification:
  areas:
  - real-analysis
  topics:
  - density
  - measure-theory
  - convergence-of-integrals
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
We say a sequence $\{a_n\}$ in $[0,1]$ is equi-distributed if for all interval $[c,d] \subset [0,1]$, $\lim_{n\to\infty} \frac{|\{a_1,\dots,a_n\}\cap[c,d]|}{n} = d-c$.
Prove that $\{a_n\}$ in $[0,1]$ is equi-distributed iff $\lim_{n\to\infty} \int f d\mu_n = \int f dm$ for all $f \in C[0,1]$, where $\mu_n = \frac{1}{n}\sum_{k=1}^n \delta_{a_k}$.
:::
