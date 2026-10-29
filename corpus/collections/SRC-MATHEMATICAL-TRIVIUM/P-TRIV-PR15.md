---
schema: qual/card@1
id: P-TRIV-PR15
kind: problem
title: Random variables with $\mathbf{E}\xi^2=\mathbf{E}\xi^3=\mathbf{E}\xi^4$ are $\{0,1\}$-valued
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 15, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash contains one or more nonprinting control bytes at this source position; they were removed from the authored card as nonsemantic extraction artifacts.
---

::: {.problem}
Prove that if for some discrete random variable ξ, $\mathbf { E } \xi ^ { 2 } = \mathbf { E } \xi ^ { 3 } = \mathbf { E } \xi ^ { 4 }$ , then $\xi$ can only take values 0 or 1.
:::

::: {.solution}

Assume the stated moments are finite.

::: pf

::: {.pf-step #s1-1}

The moment equalities imply
$$
\mathbf E\bigl[\xi^2(\xi-1)^2\bigr]=0.
$$


::: pf-proof

Expand the nonnegative polynomial:
$$
\xi^2(\xi-1)^2=\xi^4-2\xi^3+\xi^2.
$$
Taking expectations and using
$$
\mathbf E\xi^2=\mathbf E\xi^3=\mathbf E\xi^4
$$
gives zero.

:::

:::

::: pf-step

The random variable
$$
Z=\xi^2(\xi-1)^2
$$
is nonnegative almost surely.


::: pf-proof

Both factors $\xi^2$ and $(\xi-1)^2$ are squares, so their product is nonnegative for every real value of $\xi$.

:::

:::

::: {.pf-step #s1-3}

Hence
$$
Z=0
$$
almost surely.


::: pf-proof

A nonnegative random variable with expectation zero must vanish almost surely. Indeed, if $P(Z>0)>0$, then for some integer $n\geq1$ one has $P(Z\geq1/n)>0$, which would imply
$$
\mathbf EZ\geq\frac1nP(Z\geq1/n)>0,
$$
contradicting step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{P(\xi\in\{0,1\})=1}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\xi^2(\xi-1)^2=0
$$
almost surely. A real number $r$ satisfies $r^2(r-1)^2=0$ exactly when $r=0$ or $r=1$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion. The argument in fact does not require discreteness.

:::

:::

:::
