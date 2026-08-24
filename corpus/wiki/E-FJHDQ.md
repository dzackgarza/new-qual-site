---
schema: qual/card@1
id: E-FJHDQ
kind: exercise
title: The standard function juggling trick
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

:::{.exercise title="The standard function juggling trick"}
Show that if $f:\HH\to \DD$ is holomorphic and $f(i) = 0$ then $\abs{f(z)} \leq \abs{z-i\over z+i}$.

:::

:::{.solution}
Note that
\[
\abs{f(z)} \leq \abs{g(z)} \impliedby \abs{(f\circ g\inv)(z)} \leq \abs{z}
,\]
so one can use the Schwarz lemma on $F \da f\circ g\inv$.
Noting that $g(z) \da {z-i\over z+i}: \HH\to \DD$ is the Cayley map, the inverse is $g\inv(z) = i{1-z\over 1+z}: \DD\to \HH$. 
Then $F(0) = f(g\inv(0)) = f(i) = 0$ by assumption, so Schwarz yield $\abs{F(z)} \leq \abs{z}$.
:::
