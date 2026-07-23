---
schema: qual/card@1
id: E-E7SZ7
kind: exercise
title: "Primitives imply vanishing integral"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Primitives imply vanishing integral"}
Show that if $f$ has a primitive $F$ on $\Omega$ then $\displaystyle\int_\gamma f = 0$ for every closed curve $\gamma \subseteq \Omega$.

#complex/exercise/completed

:::

:::{.solution}
Let $F$ be a primitive of $f$, so $\dd{}{z}F = f$.
Then
\[
\int_\gamma f(z) \dz = F(\gamma(1)) - F(\gamma(0)) = F(p) - F(p) = 0
.\]
More explicitly, let $z(t): [a, b]\to \CC$ be any parameterization of $\gamma$, then
\[
\int_\gamma f(z) \dz 
&= \int_a^b f(z(t)) z'(t)\dt \\
&= \int_a^b F'(z(t))z'(t) \dt \\
&= \int_a^b \tilde F'(t)\dt && \text{ where } \tilde F(t) \da F(z(t)) \text{ by the chain rule} \\
&= F(z(b)) - F(z(a)) && \text{ by FTC} \\
&= 0
,\]
since $z(b) = z(a)$ for a closed curve.


:::

