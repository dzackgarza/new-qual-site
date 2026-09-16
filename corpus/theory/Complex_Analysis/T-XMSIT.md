---
schema: qual/card@1
id: T-XMSIT
kind: theorem
title: Schwarz lemma
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Maximum Modulus Principle
relations:
- kind: variant-of
  target: T-DAETF
review: draft
---

::: {.theorem ref="SchwarzzLemma"}
Let $f\colon\DD\to\DD$ be [[D-E7A5W|holomorphic]] with $f(0)=0$.
Then

1. $\abs{f(z)}\leq\abs{z}$ for all $z\in\DD$, and

2. $\abs{f'(0)}\leq1$.

If $\abs{f(z_0)}=\abs{z_0}$ for some $z_0\in\DD\setminus\{0\}$, or if $\abs{f'(0)}=1$, then $f$ is a rotation: there is $\lambda\in\CC$ with $\abs{\lambda}=1$ such that $f(z)=\lambda z$ for all $z\in\DD$.
:::
