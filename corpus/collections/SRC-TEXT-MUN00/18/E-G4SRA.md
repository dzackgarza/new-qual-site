---
schema: qual/card@1
id: E-G4SRA
kind: problem
title: Products of continuous maps are continuous
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $f: A \to B$ and $g: C \to D$ be continuous functions.
Let us define a map $f \times g: A \times C \to B \times D$ by the equation

$$
(f \times g)(a \times c) = f(a) \times g(c).
$$

Show that $f \times g$ is continuous.
:::

::: {.solution}
A basis for $B\times D$ consists of sets $U\times V$ with $U\subseteq B$ open and $V\subseteq D$ open. For such a basic set,
\[
(f\times g)^{-1}(U\times V)=f^{-1}(U)\times g^{-1}(V).
\]
Since $f$ and $g$ are continuous, the two factors on the right are open in $A$ and $C$, so their product is open in $A\times C$. Thus inverse images of basis elements are open, hence $f\times g$ is continuous.
:::
