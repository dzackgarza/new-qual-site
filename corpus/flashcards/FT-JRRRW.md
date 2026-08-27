---
schema: qual/card@1
id: FT-JRRRW
kind: theorem
title: Uniform Boundedness Principle
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Norms
relations: []
review: draft
---

::: {.theorem}
If $\mathcal{F}$ is a family of bounded operators $T_n:X\to Y$ between Banach spaces with 
$$  
\forall x\in X, \qquad \sup_{T_n \in \mathcal{F}} \norm{T_n(x)}_Y < \infty
,$$
then $\sup_{T_n\in \mathcal{F}} \norm{T_n}_X < \infty$.

> Slogan: pointwise bounded sequences of operators are uniformly bounded.
:::
