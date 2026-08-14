---
schema: qual/card@1
id: E-3ZHRE
kind: exercise
title: "Entire functions satisfying a bound"
classification:
  areas:
  - complex-analysis
  topics:
  - liouville-s-theorem
  - entire-functions
  - casorati-weierstrass
  - counterexamples
relations: []
review: draft
---
:::{.exercise title="Entire functions satisfying a bound"}
Find all entire functions $f$ that satisfy
\[
\abs{f(z)} \geq e^{\abs{z}} && \forall z\in \CC
.\]

:::

:::{.solution}
Claim: there are no such functions.
Consider $g(z) \da f(z)/e^z$, which is entire since $e^z$ is nonvanishing.
Now $g$ is entire and $\abs{g} \geq 1$ everywhere, so $\im(g) \intersect \DD$ is empty.
This contradicts Casorati-Weierstrass, which requires that $\im g$ be dense in $\CC$.

Alternatively, note $f\neq 0$ by the inequality, so $1/f$ is bounded and entire and thus constant.
However, $f(z) = c$ contradicts the inequality, since $e^{\abs{z}}\to \infty$ as $\abs{z}\to \infty$.

Alternatively, note that $e^{\abs{z}} \geq 1$ for all $z$, so $\im(f) \intersect \DD$ is empty, again contradicting Casorati-Weierstrass.
:::
