---
schema: qual/card@1
id: E-AH7RC
kind: problem
title: Convergence in products via coordinate convergence
classification:
  areas:
  - topology
  topics:
  - Convergence
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Let $\mathbf{x}_1, \mathbf{x}_2, \ldots$ be a sequence of the points of the product space $\prod X_\alpha$.
Show that this sequence converges to the point $\mathbf{x}$ if and only if the sequence $\pi_\alpha(\mathbf{x}_1), \pi_\alpha(\mathbf{x}_2), \ldots$ converges to $\pi_\alpha(\mathbf{x})$ for each $\alpha$.
Is this fact true if one uses the box topology instead of the product topology?
:::

::: {.solution}

::: pf

::: {.pf-step #coord-convergence-forward}
In the product topology, if $\mathbf x_n\to\mathbf x$, then $\pi_\alpha(\mathbf x_n)\to\pi_\alpha(\mathbf x)$ for every $\alpha$.

::: pf-proof
Each projection $\pi_\alpha$ is continuous, and a continuous map carries a convergent sequence to a sequence converging to the image of the limit.
:::

:::

::: {.pf-step #coord-convergence-converse}
In the product topology, if $\pi_\alpha(\mathbf x_n)\to\pi_\alpha(\mathbf x)$ for every $\alpha$, then $\mathbf x_n\to\mathbf x$.

::: pf-proof
A basic neighborhood of $\mathbf x$ is $\prod_\alpha U_\alpha$ with $U_\alpha$ open and $U_\alpha=X_\alpha$ except for $\alpha$ in a finite set $F$.
For each $\alpha\in F$ choose $N_\alpha$ with $\pi_\alpha(\mathbf x_n)\in U_\alpha$ for $n\ge N_\alpha$.
For $n\ge\max_{\alpha\in F}N_\alpha$, every coordinate of $\mathbf x_n$ lies in the corresponding $U_\alpha$, so $\mathbf x_n\in\prod_\alpha U_\alpha$.
:::

:::

::: {.pf-step #box-topology-counterexample}
In the box topology the equivalence fails: in $\RR^\omega$ the sequence $\mathbf x_n=(\frac1n,\frac1n,\frac1n,\ldots)$ converges to $0$ in every coordinate but does not converge to $\mathbf 0$.

::: pf-proof
The set $B=\prod_{k\ge1}(-\frac1k,\frac1k)$ is a box neighborhood of $\mathbf 0$.
The $n$-th coordinate of $\mathbf x_n$ is $\frac1n\notin(-\frac1n,\frac1n)$, so $\mathbf x_n\notin B$ for every $n$.
The implication of step [](#coord-convergence-forward){.pf-ref} still holds, since projections are continuous in the box topology.
:::

:::

::: pf-qed
Steps [](#coord-convergence-forward){.pf-ref} and [](#coord-convergence-converse){.pf-ref} prove the equivalence for the product topology, and step [](#box-topology-counterexample){.pf-ref} answers the question for the box topology.
:::

:::
:::
