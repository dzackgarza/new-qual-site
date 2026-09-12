---
schema: qual/card@1
id: P-ODNWF
kind: problem
title: An ideal of a PID containing an irreducible $a$ equals $Ra$
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Ideals
  - Factorization
relations: []
review: draft
---

::: {.problem}
Let $R$ be a PID, let $I\subsetneq R$ be a proper ideal, and suppose $a\in I$ is irreducible. Prove that
\[
I=(a).
\]
:::

::: {.solution}
Since $R$ is a PID, write $I=(d)$. Because $a\in I$, there exists $r\in R$ with
\[
a=dr.
\]
As $a$ is irreducible, either $d$ is a unit or $r$ is a unit. The first possibility would give $I=(d)=R$, contradicting that $I$ is proper. Hence $r$ is a unit, so $d$ and $a$ are associates. Therefore
\[
I=(d)=(a).
\]
:::
