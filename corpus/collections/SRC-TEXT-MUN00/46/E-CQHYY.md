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
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §46 Exercise 3 was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked against the definitions of the uniform topology
    and the topology of compact convergence in §46 and Theorem 43.6. Closedness in the uniform topology is
    tested by sequences, legitimate because that topology is metrizable: a uniform limit of functions bounded
    by M_N is bounded by M_N + 1. Not closed in the topology of compact convergence: the functions f_n equal
    to x on [-n,n] and 0 elsewhere are bounded, hence in B(R,R), and they converge to the unbounded function x
    uniformly on every compact set, so x lies in the closure of B(R,R) and not in it. Note that these f_n need
    not be continuous, and are not required to be: B(R,R) is a subspace of R^R. Nothing needed correction.
---

::: {.exercise}

Show that the set $\mathcal{B}(\RR, \RR)$ of bounded functions $f: \RR \to \RR$ is closed in $\RR^{\RR}$ in the uniform topology, but not in the topology of compact convergence.
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
