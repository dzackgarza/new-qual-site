---
schema: qual/card@1
id: E-CQHYY
kind: problem
title: Bounded functions under uniform and compact convergence topologies
classification:
  areas:
  - topology
  topics:
  - Function Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Show that the set $\mathcal{B}(\mathbb{R}, \mathbb{R})$ of bounded functions $f: \mathbb{R} \to \mathbb{R}$ is closed in $\mathbb{R}^{\mathbb{R}}$ in the uniform topology, but not in the topology of compact convergence.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$\mathcal B(\RR,\RR)$ is closed in the uniform topology.

::: pf-proof

The uniform topology is induced by a metric, so it suffices to show that a uniform limit $f$ of a sequence $f_n \in \mathcal B(\RR,\RR)$ is bounded. Choose $N$ with $\sup_x \abs{f_N(x) - f(x)} < 1$, and let $M_N$ bound $\abs{f_N}$. Then $\abs{f(x)} \le \abs{f_N(x)} + 1 \le M_N + 1$ for all $x$.

:::

:::

::: {.pf-step #s2}

$\mathcal B(\RR,\RR)$ is not closed in the topology of compact convergence.

::: pf-proof

Let $f_n(x) = x$ for $\abs{x} \le n$ and $f_n(x) = 0$ otherwise, and let $f(x) = x$. Each $f_n$ is bounded by $n$, and $f$ is unbounded. For a compact $K \subseteq \RR$ and $n \ge \sup_{x \in K} \abs{x}$, $f_n = f$ on $K$, so $f_n \to f$ uniformly on every compact set. Hence $f$ lies in the closure of $\mathcal B(\RR,\RR)$ in the topology of compact convergence but not in $\mathcal B(\RR,\RR)$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove the two claims.

:::

:::

:::
