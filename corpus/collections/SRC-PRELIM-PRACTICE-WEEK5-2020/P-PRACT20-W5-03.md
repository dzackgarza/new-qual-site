---
schema: qual/card@1
id: P-PRACT20-W5-03
kind: problem
title: $C[0,1]$ is not an integral domain
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
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 3).
---

::: {.problem}
The continuous functions on $[0, 1]$ form a ring under pointwise addition and pointwise multiplication. Show that this ring is not an integral domain.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Define
$$
f(x)=\max\left\{0,\frac12-x\right\},
\qquad
g(x)=\max\left\{0,x-\frac12\right\}.
$$
Then $f,g\in C([0,1])$ and neither function is zero.


::: pf-proof

Each function is the maximum of two continuous real-valued functions, hence
is continuous. Moreover,
$$
f(0)=\frac12\ne0,
\qquad
g(1)=\frac12\ne0.
$$
Thus both are nonzero elements of the ring.

:::

:::

::: {.pf-step #s1-2}

Their pointwise product is identically zero:
$$
fg=0.
$$


::: pf-proof

If $x\le1/2$, then
$$
g(x)=0.
$$
If $x\ge1/2$, then
$$
f(x)=0.
$$
Thus for every $x\in[0,1]$ at least one factor vanishes, so
$$
f(x)g(x)=0.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{C([0,1])\text{ is not an integral domain}}.
$$


::: pf-proof

An integral domain has no nonzero zero divisors. Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} exhibit
two nonzero ring elements whose product is zero.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required conclusion.

:::

:::

:::
