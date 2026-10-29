---
schema: qual/card@1
id: P-PRACT20-W5-13
kind: problem
title: Boolean rings are commutative
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 13).
---

::: {.problem}
Suppose that $r^2 = r$ for all $r$ in a ring $R$. Show that $R$ is commutative.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $r\in R$,
$$
2r=0.
$$


::: pf-proof

The element $r+r$ is also idempotent, so
$$
(r+r)^2=r+r.
$$
Expanding and using $r^2=r$ gives
$$
r^2+r^2+r^2+r^2=r+r,
$$
hence
$$
4r=2r.
$$
Subtracting $2r$ in the additive group of $R$ yields
$$
2r=0.
$$

:::

:::

::: {.pf-step #s1-2}

For every $r,s\in R$,
$$
rs+sr=0.
$$


::: pf-proof

The element $r+s$ is idempotent, so
$$
(r+s)^2=r+s.
$$
Expanding gives
$$
r^2+rs+sr+s^2=r+s.
$$
Using $r^2=r$ and $s^2=s$ and cancelling $r+s$ yields
$$
rs+sr=0.
$$

:::

:::

::: {.pf-step #s1-3}

For every $r,s\in R$,
$$
\boxed{rs=sr}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
rs=-sr.
$$
Step [](#s1-1){.pf-ref} applied to the element $sr$ gives
$$
sr+sr=0,
$$
so
$$
-sr=sr.
$$
Therefore $rs=sr$.

:::

:::

::: {.pf-step #s1-4}

Hence $R$ is commutative.


::: pf-proof

Step [](#s1-3){.pf-ref} shows that every pair of elements commutes.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
