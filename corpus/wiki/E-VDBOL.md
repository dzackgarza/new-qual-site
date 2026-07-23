---
schema: qual/card@1
id: E-VDBOL
kind: exercise
title: "Combining with Rouche"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Combining with Rouche"}
Use Rouché's theorem and the Schwarz lemma to prove the following: if $f:\DD\to \bar{ \DD}$ is holomorphic with $f(0) = 0$, then there are exactly $m$ solutions (counted with multiplicity) to $f(z) = (2z)^m$ in the disc $\abs{z} < 1/2$.

#complex/exercise/completed

:::

:::{.solution}
First note that the image of $f$ is in fact $\DD$ rather than $\bar{\DD}$, using the open mapping theorem and that the domain $\DD$ is open.
So Schwarz applies to $f$.
Write $g(z) \da f(z) - (2z)^m$, the claim is that $g$ has $m$ zeros.
Toward applying Rouché, identify 

- The big part of $g$: $M(z) \da -(2z)^m$ 
- The small part of $g$: $m(z) \da g(z) - M(z) = f(z)$.

Now
\[
\abs{m(z)} \da \abs{f(z)} \leq \abs{z} = {1\over 2} < \abs{m(z)} = \abs{2z}^m = 1 \qquad \text{on } \abs{z} = {1\over 2}
,\]
so Rouché applies: $\size Z_m = \size Z_M$ on $\abs{z} < {1\over 2}$, where $m(z) = f(z)$ and $M(z) = -(2z)^m$ which has exactly $m$ zeros.

> Note that this works with $g(z) \da (cz)^m$ and $R = {1\over c}$.

:::
