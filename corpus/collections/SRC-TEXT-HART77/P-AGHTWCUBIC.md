---
schema: qual/card@1
id: P-AGHTWCUBIC
kind: problem
title: The twisted cubic is an affine variety of dimension one
classification:
  areas:
  - algebraic-geometry
  topics:
  - Twisted Cubic
  - Dimension
  - Coordinate Rings
relations:
- kind: uses
  target: D-5LJUX
- kind: uses
  target: PR-7OT2Z
review: draft
---

::: {.problem}
Let $Y \subseteq \AA^3$ be the set $Y = \theset{ (t, t^2, t^3) \st t \in k }$.

- Show that $Y$ is an affine variety of dimension $1$.

- Find generators for the ideal $I(Y)$.

- Show that $A(Y)$ is isomorphic to a polynomial ring in one variable over $k$.

We say $Y$ is given by the \dfn{parametric representation} $x = t,\ y = t^2,\ z = t^3$.
:::

::: {.solution}
**The ideal.** Let $\mathfrak a = \generators{y - x^2,\ z - x^3}$. Clearly $\mathfrak a \subseteq I(Y)$.
Modulo $\mathfrak a$ every polynomial is congruent to a polynomial $g(x)$, so if $h \in I(Y)$ then $h \equiv g(x)$ with $g(t) = h(t,t^2,t^3) = 0$ for every $t \in k$.
Since $k$ is infinite, $g = 0$, so $h \in \mathfrak a$. Hence $I(Y) = \generators{y - x^2,\ z - x^3}$.

**The coordinate ring.** The same reduction shows that $x \mapsto t,\ y \mapsto t^2,\ z \mapsto t^3$ induces an isomorphism
$$
A(Y) = k[x,y,z]/I(Y) \cong k[t] .
$$

**That $Y$ is a variety of dimension $1$.** The set $Y = Z(y - x^2,\ z - x^3)$ is closed, and $I(Y)$ is prime because $A(Y) \cong k[t]$ is a domain, so $Y$ is irreducible.
Finally $\dim Y = \krulldim A(Y) = \krulldim k[t] = 1$.
:::
