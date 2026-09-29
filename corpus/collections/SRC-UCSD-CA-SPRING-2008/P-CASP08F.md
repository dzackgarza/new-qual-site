---
schema: qual/card@1
id: P-CASP08F
kind: problem
title: "Rational functions with prescribed limits on disjoint regions"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Prove that there exists a sequence of rational functions $R_n$ analytic in $\mathbb{C} \setminus \{3/2\}$, satisfying both of the following:

(i) $\lim_{n \to \infty} R_n(z) = 1$ for all $z \in \mathbb{D}$.

(ii) $\lim_{n \to \infty} R_n(z) = 2$ for $2 \leq |z| \leq 3$.
:::

::: {.solution}

::: pf

::: pf-step

The two compact sets $\overline{\DD}$ and $A = \{2 \le |z| \le 3\}$ are disjoint, and $\mathbb C \setminus \{3/2\}$ is connected.

::: pf-proof

$\overline{\DD} \cap A = \varnothing$, and $\mathbb C \setminus \{3/2\}$ is connected (a punctured plane).

:::

:::

::: {.pf-step #s2}

Define a function $h$ on a neighborhood of $\overline{\DD} \cup A$ by $h = 1$ on a neighborhood of $\overline{\DD}$ and $h = 2$ on a neighborhood of $A$.

::: pf-proof

since $\overline{\DD}$ and $A$ are disjoint compact sets, they have disjoint neighborhoods, so $h$ is well-defined and holomorphic (locally constant).

:::

:::

::: {.pf-step #s3}

By Runge's theorem, for each $n$ there is a rational function $R_n$ with poles only at $3/2$ such that $|R_n(z) - h(z)| < 1/n$ for all $z \in \overline{\DD} \cup A$.

::: pf-proof

Runge's theorem (rational approximation with prescribed poles at $3/2$ on the connected set $\mathbb C \setminus \{3/2\}$).

:::

:::

::: {.pf-step #s4}

Hence $R_n(z) \to 1$ uniformly on $\overline{\DD}$ and $R_n(z) \to 2$ uniformly on $A$.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

In particular, $R_n(z) \to 1$ for all $z \in \DD$ and $R_n(z) \to 2$ for all $2 \le |z| \le 3$.

::: pf-proof

Step [](#s4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref}.

:::

:::

:::
