---
schema: qual/card@1
id: P-ZBTCU
kind: problem
title: The Sylow theorems
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - p-Groups
relations: []
review: draft
---

::: problem
State the three Sylow theorems.
:::

::: solution
Let $G$ be a finite group and let
\[
|G|=p^n m,
\qquad
p\nmid m.
\]
A subgroup of order $p^n$ is called a Sylow $p$-subgroup.

The Sylow theorems are:

<1>1. Existence.
There exists a subgroup
\[
P\le G
\]
of order $p^n$.

<1>2. Conjugacy and containment.
Every $p$-subgroup of $G$ is contained in a Sylow $p$-subgroup, and any two Sylow $p$-subgroups are conjugate in $G$.

<1>3. Number of Sylow subgroups.
If $n_p$ denotes the number of Sylow $p$-subgroups, then
\[
n_p\equiv1\pmod p
\]
and
\[
n_p\mid m.
\]

In particular,
\[
n_p=1
\iff
\text{the Sylow $p$-subgroup is normal in $G$}.
\]
:::
