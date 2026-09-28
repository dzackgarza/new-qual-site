---
schema: qual/card@1
id: E-FJHDQ
kind: problem
title: $\abs{f(z)}\le\abs{\frac{z-i}{z+i}}$ for holomorphic $f:\HH\to\DD$ with $f(i)=0$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.exercise}
Show that if $f:\HH\to \DD$ is holomorphic and $f(i) = 0$ then $\abs{f(z)} \leq \abs{z-i\over z+i}$.

:::

::: {.solution}
Let $g(z) \da {z-i\over z+i}: \HH\to \DD$ be the Cayley map, a biholomorphism with inverse $g\inv(w) = i{1+w\over 1-w}: \DD\to \HH$, and let $F \da f\circ g\inv:\DD\to\DD$.
Then $F(0) = f(g\inv(0)) = f(i) = 0$ by assumption, so the Schwarz lemma gives $\abs{F(w)} \leq \abs{w}$ for $w\in\DD$.
For $z\in\HH$, take $w=g(z)$: 
\[
\abs{f(z)}=\abs{F(g(z))}\le\abs{g(z)}=\abs{z-i\over z+i}
.\]
:::
