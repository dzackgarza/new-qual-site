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
(March 2007) Let $p,q\ge 2$ be prime numbers, and let $G$ be a group of order $|G|=pq$.
Let $H\subsetneq G$ be a proper subgroup (i.e., $H$ is a subgroup but is not the full group $G$). Prove that $H$ is cyclic.
:::

::: {.solution}
<1>1. The order of $H$ is one of
$$
1,\ p,\ q.
$$
::: {.proof}
By Lagrange's theorem,
$$
|H|\mid |G|=pq.
$$
Thus
$$
|H|\in\{1,p,q,pq\}.
$$
Since $H\subsetneq G$, one has $|H|<pq$, so the case $|H|=pq$ is excluded.
:::

<1>2. In every remaining case, $H$ is cyclic.
::: {.proof}
If $|H|=1$, then
$$
H=\{e\}=\langle e\rangle.
$$
If $|H|=p$ or $|H|=q$, then $H$ has prime order. Any nonidentity element of a finite group of prime order has order equal to the whole group order by Lagrange's theorem, and hence generates the group. Therefore $H$ is cyclic.
:::

<1>3. Therefore
$$
\boxed{H\text{ is cyclic}}.
$$
::: {.proof}
Step <1>1 exhausts the possible orders of $H$, and step <1>2 proves cyclicity in each case.
:::

<1>4. Q.E.D.
::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
