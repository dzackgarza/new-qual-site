---
schema: qual/card@1
id: P-AMH-ALG-SG16-03
kind: problem
title: Elements commuting with the cosets of a subgroup form a subgroup
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
(January 2016) Let $G$ be a group, let $H\subseteq G$ be a subgroup, and define the set
\[
K=\{x\in G\mid Hx=xH\}.
\]
Prove that $K$ is a subgroup of $G$.
:::

::: {.solution}
<1>1. The identity lies in $K$.
::: {.proof}
Since
$$
He=H=eH,
$$
one has $e\in K$.
:::

<1>2. The set $K$ is closed under products.
::: {.proof}
Let $a,b\in K$. Then
$$
Ha=aH
\qquad\text{and}\qquad
Hb=bH.
$$
Therefore
$$
H(ab)
=(Ha)b
=(aH)b
=a(Hb)
=a(bH)
=(ab)H.
$$
Hence $ab\in K$.
:::

<1>3. The set $K$ is closed under inverses.
::: {.proof}
Let $a\in K$, so
$$
Ha=aH.
$$
Multiplying this equality on the left and right by $a^{-1}$ gives
$$
a^{-1}H=Ha^{-1}.
$$
Thus $a^{-1}\in K$.
:::

<1>4. Therefore
$$
\boxed{K\le G}.
$$
::: {.proof}
By step <1>1, $K$ is nonempty; step <1>2 gives closure under products, and step <1>3 gives closure under inverses. Hence $K$ is a subgroup of $G$.
:::

<1>5. Q.E.D.
::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
