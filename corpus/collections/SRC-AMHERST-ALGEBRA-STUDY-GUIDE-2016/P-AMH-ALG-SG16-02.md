---
schema: qual/card@1
id: P-AMH-ALG-SG16-02
kind: problem
title: Proper subgroups of a group of order $pq$ are cyclic
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
Let $p,q\ge 2$ be prime numbers, and let $G$ be a group of order $\cardinality{G}=pq$.
Let $H\subsetneq G$ be a proper subgroup (i.e., $H$ is a subgroup but is not the full group $G$). Prove that $H$ is cyclic.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
The order of $H$ is one of
$$
1,\ p,\ q.
$$

::: pf-proof
By Lagrange's theorem,
$$
\cardinality{H}\mid \cardinality{G}=pq.
$$
Thus
$$
\cardinality{H}\in\{1,p,q,pq\}.
$$
Since $H\subsetneq G$, one has $\cardinality{H}<pq$, so the case $\cardinality{H}=pq$ is excluded.
:::

:::

::: {.pf-step #s1-2}
In every remaining case, $H$ is cyclic.

::: pf-proof
If $\cardinality{H}=1$, then
$$
H=\{e\}=\langle e\rangle.
$$
If $\cardinality{H}=p$ or $\cardinality{H}=q$, then $H$ has prime order. Any nonidentity element of a finite group of prime order has order equal to the whole group order by Lagrange's theorem, and hence generates the group. Therefore $H$ is cyclic.
:::

:::

::: pf-step
Therefore
$$
\boxed{H\text{ is cyclic}}.
$$

::: pf-proof
Step [](#s1-1){.pf-ref} exhausts the possible orders of $H$, and step [](#s1-2){.pf-ref} proves cyclicity in each case.
:::

:::

:::

:::
