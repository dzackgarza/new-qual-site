---
schema: qual/card@1
id: E-JQFDG
kind: exercise
title: "Equality of different integrals"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Equality of different integrals"}
Suppose $f$ is holomorphic on $\Omega$, a simply connected region, and suppose $\gamma \subseteq \Omega$.
Using the Cauchy integral formula, show that
\[
\int_\gamma {f'(z) \over z-a}\dz = \int_\gamma {f(z) \over (z-a)^2 }\dz
.\]
Also prove this when $\Omega$ is *not* simply connected.

#complex/exercise/completed

:::

:::{.solution}
Use the integral formula directly:
\[
\int_\gamma {f'(z) \over z-a}\dz = 2\pi i f'(a)
.\]

On the other hand, use Cauchy's formula for derivatives:
\[
\int_\gamma {f(z) \over (z-a)^2}\dz = 2\pi i f^{(1)}(a)
,\]
and these values are equal.

If $\Omega$ is not simply connected, note that by the quotient rule
\[
\dd{}{z} {f(z) \over z-a} = {f'(z)\over z-a} - {f(z) \over (z-a)^2}
.\]

Thus
\[
\int_\gamma {f'(z) \over z-a} - \int_\gamma {f(z) \over (z-a)^2}\dz 
&= \int_\gamma \qty{ {f'(z) \over z-a} - {f(z) \over (z-a)^2} }\dz \\
&= \int_\gamma \dd{}{z} {f(z) \over z-a} \dz \\
&= G(\gamma(1)) - G(\gamma(0)) \\
&= G(p) - G(p) \\
&= 0
,\]
where $G(z) \da {f(z) \over z-a}$ is a primitive for the integrand by definition.



:::

