---
schema: qual/card@1
id: E-24ETT
kind: exercise
title: $g(\{|z|<r\})\subseteq f(\{|z|<r\})$ when $f$ is injective holomorphic and
  $f(0)=g(0)$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Biholomorphisms
  - Conformal Maps
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Suppose $f, g: \DD\to \Omega$ are holomorphic with $f$ injective and $f(0) = g(0)$.

Show that 
\[  
\Forall 0 < r < 1,\qquad g\qty{\theset{\abs{z} < r}} \subseteq f\qty{\theset{\abs{z} < r}}
.\]

> The first part of this problem asks for a statement of the Schwarz lemma.

:::

:::{.solution}
Since $f$ is injective, it has a left-inverse $f\inv$, and $F\da f\inv g$ is well-defined.
Since $F:\DD\to \DD$ and $F(0) = 0$, Schwarz applies and $\abs{F(z)} \leq z$ on $\DD$.
Unwinding:
\[
\abs{(f\inv \circ g)(z)} \leq \abs{z} \implies \abs{g(z)} \leq \abs{f(z)} \qquad \forall \DD\in \ZZ
.\]
This says that $g(\DD) \subseteq f(\DD)$, and in particular this holds on all $\DD_r(0)$, so $g(\DD_r(0)) \subseteq f(\DD_r(0))$.
:::
