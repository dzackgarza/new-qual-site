---
schema: qual/card@1
id: E-ZN7P4
kind: problem
title: Continuous images of connected sets are connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Prove that if $f: X \to Y$ is a continuous map between topological spaces and $X$ is connected, then the image $f(X)$ is connected in $Y$.
:::

::: {.solution}

Give $f(X)$ the subspace topology, and suppose $f(X)=U\cup V$ with $U,V$ disjoint, nonempty, and open in $f(X)$.

::: pf

::: {.pf-step #preimages}

$f^{-1}(U)$ and $f^{-1}(V)$ are disjoint, open in $X$, and cover $X$.

::: pf-proof

The corestriction $f:X\to f(X)$ is continuous, which gives openness. Disjointness and covering follow from $U\cap V=\varnothing$ and $U\cup V=f(X)$.

:::

:::

::: pf-step

$f(X)$ is connected.

::: pf-proof

Both preimages are nonempty because $U$ and $V$ are nonempty subsets of the image of $f$. By step [](#preimages){.pf-ref} they separate $X$, contradicting connectedness of $X$.

:::

:::

:::

:::
