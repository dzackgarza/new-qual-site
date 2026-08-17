---
schema: qual/card@1
id: E-NKDKF
kind: exercise
title: "Primitives imply vanishing integral"
classification:
  areas:
  - complex-analysis
  topics:
  - contour-integration
  - cauchy-integral-theorem
relations: []
review: draft
---
:::{.exercise title="Primitives imply vanishing integral"}
Show that if $f$ has a primitive $F$ on $\Omega$ then $\int_\gamma f = 0$ for every closed curve $\gamma \subseteq \Omega$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show that if $f$ has a primitive $F$ on $\Omega$ (i.e. $F' = f$ on $\Omega$), then $\int_\gamma f = 0$ for every closed curve $\gamma \subseteq \Omega$.

<1>1. If $\gamma$ is a smooth curve from $a$ to $b$ parametrized by $z(t)$, $t \in [0,1]$, then $\int_\gamma f = F(b) - F(a)$.
    Proof: By the chain rule, $\dv{t}F(z(t)) = F'(z(t)) z'(t) = f(z(t)) z'(t)$, so $\int_\gamma f = \int_0^1 f(z(t))z'(t)\,dt = \int_0^1 \dv{t}F(z(t))\,dt = F(z(1)) - F(z(0)) = F(b) - F(a)$.

<1>2. For a closed curve $\gamma$, the endpoints coincide, so $\int_\gamma f = F(a) - F(a) = 0$.
    Proof: <1>1 with $b = a$: a closed curve has $z(1) = z(0)$.

<1>3. The claim extends to piecewise smooth closed curves by summing over the smooth pieces.
    Proof: Subdivide $\gamma$ into smooth arcs; the integral is the sum of the arc integrals, and the endpoint terms telescope to $0$ around the closed loop.

<1>4. Q.E.D.
    Proof: <1>1–<1>3 prove the claim for (piecewise) smooth closed curves, which is the standard meaning of $\int_\gamma f$ in this context.

:::
