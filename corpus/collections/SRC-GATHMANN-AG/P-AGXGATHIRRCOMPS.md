---
schema: qual/card@1
id: P-AGXGATHIRRCOMPS
kind: problem
title: Irreducible components of $V(x-yz,\, xz-y^2) \subset \AA^3/\CC$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducible Components
  - Coordinate Rings
  - Integral Domains
relations: []
review: draft
---

::: {.problem}
Find the irreducible components of
$$
X = V(x - yz, xz - y^2) \subset \AA^3/\CC
.$$
:::

::: {.solution}
Let $R \definedas \CC[x,y,z]$, $X_1 \definedas V(x-yz,\, y)$ and $X_2 \definedas V(x-yz,\, z^2-y)$.

::: pf

::: {.pf-step #decomposition}
$X = X_1 \union X_2$.

::: pf-proof
Since $xz - y^2 = z(x-yz) + (yz^2 - y^2)$, the ideals $\generators{x-yz,\, xz-y^2}$ and $\generators{x-yz,\, y(z^2-y)}$ are equal.
A point satisfies $x = yz$ and $y(z^2-y) = 0$ exactly when it satisfies $x = yz$ and either $y = 0$ or $z^2 = y$.
Hence $X = X_1 \union X_2$.
:::

:::

::: {.pf-step #first-irreducible}
$X_1$ is irreducible.

::: pf-proof
The ideal $\generators{x-yz,\, y}$ equals $\generators{x,\, y}$, and $R/\generators{x,y} \cong \CC[z]$ is an integral domain.
So $\generators{x,y}$ is prime, and by the Nullstellensatz $I(X_1) = \generators{x,y}$.
The coordinate ring $A(X_1) \cong \CC[z]$ is an integral domain, so $X_1$ is irreducible.
:::

:::

::: {.pf-step #second-irreducible}
$X_2$ is irreducible.

::: pf-proof
Eliminating $x = yz$ and then $y = z^2$ gives
$$
R/\generators{x-yz,\, z^2-y} \cong \CC[y,z]/\generators{z^2-y} \cong \CC[z],
$$
an integral domain.
So $\generators{x-yz,\, z^2-y}$ is prime, and by the Nullstellensatz it is $I(X_2)$.
The coordinate ring $A(X_2) \cong \CC[z]$ is an integral domain, so $X_2$ is irreducible.
:::

:::

::: {.pf-step #no-containment}
Neither of $X_1$, $X_2$ contains the other.

::: pf-proof
The point $(0,0,1)$ lies in $X_1$ but not in $X_2$, because $z^2 - y = 1 \neq 0$ there.
The point $(1,1,1)$ lies in $X_2$ but not in $X_1$, because $y = 1 \neq 0$ there.
:::

:::

::: {.pf-step}
The irreducible components of $X$ are the line $X_1 = \theset{(0,0,t)}$ and the twisted cubic $X_2 = \theset{(t^3,t^2,t)}$.

::: pf-proof
By steps [](#decomposition){.pf-ref}, [](#first-irreducible){.pf-ref} and [](#second-irreducible){.pf-ref}, $X$ is a union of two irreducible closed subsets.
By step [](#no-containment){.pf-ref} the union is irredundant, so by uniqueness of the irredundant decomposition into irreducible closed subsets these are the irreducible components.
The parametrizations follow from $x = y = 0$ on $X_1$, and from $y = z^2$, $x = yz = z^3$ on $X_2$.
:::

:::

:::
:::
