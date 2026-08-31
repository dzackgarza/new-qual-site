---
schema: qual/card@1
id: P-TOPS13B
kind: problem
title: "Low-dimensional homotopy groups of S^3 x S^4 x S^5"
classification:
  areas:
  - topology
  topics:
  - Homotopy Groups
  - Spheres
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
What is $\pi_n(S^3 \times S^4 \times S^5)$ for $n \leq 3$?
:::

::: {.solution}
**Goal.** Compute $\pi_n(S^3 \times S^4 \times S^5)$ for $n \le 3$.

<1>1. $\pi_n(X \times Y) \cong \pi_n(X) \times \pi_n(Y)$.
::: {.proof}
a map $S^n \to X \times Y$ is a pair of maps $S^n \to X$ and $S^n \to Y$, and homotopies correspond componentwise.
:::

<1>2. $\pi_n(S^k) = 0$ for $n < k$.
::: {.proof}
any map $S^n \to S^k$ with $n < k$ is null-homotopic (cellular approximation: it factors through the $n$-skeleton of $S^k$, which is a point).
:::

<1>3. $\pi_n(S^n) = \ZZ$.
::: {.proof}
the Hurewicz theorem identifies $\pi_n(S^n)$ with $H_n(S^n) = \ZZ$.
:::

<1>4. Compute each factor for $n \le 3$.
<2>1. $\pi_n(S^3)$: $\pi_1 = \pi_2 = 0$, $\pi_3 = \ZZ$.
::: {.proof}
by <1>2 and <1>3.
:::
<2>2. $\pi_n(S^4)$: $\pi_1 = \pi_2 = \pi_3 = 0$.
::: {.proof}
by <1>2, since $n < 4$ for $n \le 3$.
:::
<2>3. $\pi_n(S^5)$: $\pi_1 = \pi_2 = \pi_3 = 0$.
::: {.proof}
by <1>2, since $n < 5$ for $n \le 3$.
:::

<1>5. Combine.
<2>1. $\pi_1(S^3 \times S^4 \times S^5) = 0$.
::: {.proof}
$0 \times 0 \times 0$.
:::
<2>2. $\pi_2(S^3 \times S^4 \times S^5) = 0$.
::: {.proof}
$0 \times 0 \times 0$.
:::
<2>3. $\pi_3(S^3 \times S^4 \times S^5) = \ZZ$.
::: {.proof}
$\ZZ \times 0 \times 0$.
:::

<1>6. Q.E.D.
::: {.proof}
$\pi_n = 0$ for $n = 1, 2$, and $\pi_3 = \ZZ$.
:::
:::
