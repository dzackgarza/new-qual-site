---
schema: qual/card@1
id: E-8GBZO
kind: problem
title: The box topology implication in the maps-into-products theorem
classification:
  areas:
  - topology
  topics:
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

One of the implications stated in Theorem 19.6 holds for the box topology.
Which one?
:::

::: {.solution}
For $f\colon A\to\prod_{\alpha\in J}X_\alpha$ with coordinate functions $f_\alpha=\pi_\alpha\circ f$, the theorem states that $f$ is continuous if and only if every $f_\alpha$ is continuous.

::: pf

::: {.pf-step #forward-implication}
In the box topology, each projection $\pi_\alpha$ is continuous, so $\boxed{f\text{ continuous}\Rightarrow\text{every }f_\alpha\text{ continuous}}$.

::: pf-proof
For $U$ open in $X_\alpha$, $\pi_\alpha^{-1}(U)=U\times\prod_{\beta\ne\alpha}X_\beta$ is a product of open sets, hence box-open.
A composite of continuous maps is continuous.
:::

:::

::: {.pf-step #reverse-implication-fails}
The map $f\colon\mathbb R\to\mathbb R^\omega$, $f(t)=(t,t,t,\ldots)$, has continuous coordinates but is not continuous for the box topology.

::: pf-proof
Each $f_n$ is the identity of $\mathbb R$.
The set $B=\prod_{n\ge1}(-\frac1n,\frac1n)$ is box-open, and
$$
f^{-1}(B)=\bigcap_{n\ge1}\left(-\tfrac1n,\tfrac1n\right)=\{0\},
$$
which is not open in $\mathbb R$.
:::

:::

::: pf-qed
Step [](#forward-implication){.pf-ref} proves the implication that holds, and step [](#reverse-implication-fails){.pf-ref} shows that the other implication fails.
:::

:::

:::
