---
schema: qual/card@1
id: P-HGRO31
kind: problem
title: Sylow theorems
classification:
  areas: [algebra]
  topics: [Sylow Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
State the Sylow theorems.
:::

::: {.solution}
Let $G$ be a finite group, let $p$ be a prime, and write $\abs{G}=p^nm$ with
$p\nmid m$. A \dfn{Sylow $p$-subgroup} of $G$ is a subgroup of order $p^n$.

**Existence.** $G$ has a Sylow $p$-subgroup.

**Containment and conjugacy.** Every $p$-subgroup of $G$ is contained in a
Sylow $p$-subgroup, and any two Sylow $p$-subgroups of $G$ are conjugate in
$G$.

**Number.** The number $n_p$ of Sylow $p$-subgroups satisfies
$$
n_p\equiv1\pmod p\qquad\text{and}\qquad n_p\mid m.
$$
Since the Sylow $p$-subgroups form one conjugacy class, a Sylow $p$-subgroup
is normal if and only if $n_p=1$.
:::
