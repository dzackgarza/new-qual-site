---
schema: qual/card@1
id: E-MYMF4
kind: exercise
title: The first homology of the connected sum of the projective plane and the torus
classification:
  areas:
  - topology
  topics:
  - Homology of Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Calculate $H_1(P^2 \# T)$.
Assuming that the list of compact surfaces given in Theorem 75.5 is a complete list, to which of these surfaces is $P^2 \# T$ homeomorphic?
:::

::: {.solution}
<1>1. Cellular presentation and computation of $H_1(P^2 \# T)$:
<2>1. The connected sum $X = P^2 \# T$ admits a standard CW decomposition with one 0-cell, three 1-cells $c, a, b$, and one 2-cell attached along the boundary loop $c^2 [a, b] = c^2 a b a^{-1} b^{-1}$.
::: {.proof}
connected sum of polygonal schemas for $P^2$ ($c^2$) and $T$ ($aba^{-1}b^{-1}$).
:::
<2>2. The cellular chain complex for $X$ is:
\[
0 \longrightarrow \mathbb{Z} \xrightarrow{\partial_2} \mathbb{Z}c \oplus \mathbb{Z}a \oplus \mathbb{Z}b \xrightarrow{\partial_1} \mathbb{Z} \longrightarrow 0.
\]
::: {.proof}
cellular homology definition.
:::
<2>3. The boundary map $\partial_2: C_2(X) \to C_1(X)$ maps the generator of $C_2(X)$ to:
\[
\partial_2(e^2) = 2c + a + b - a - b = 2c.
\]
::: {.proof}
abelianizing the boundary loop word $c^2 a b a^{-1} b^{-1}$.
:::
<2>4. The first homology group is:
\[
H_1(P^2 \# T) = \frac{\mathbb{Z}c \oplus \mathbb{Z}a \oplus \mathbb{Z}b}{\operatorname{im}(\partial_2)} = \frac{\mathbb{Z}c}{2\mathbb{Z}c} \oplus \mathbb{Z}a \oplus \mathbb{Z}b \cong \mathbb{Z}_2 \oplus \mathbb{Z} \oplus \mathbb{Z} \cong \mathbb{Z}^2 \oplus \mathbb{Z}_2.
\]
::: {.proof}
quotient of free abelian groups.
:::

<1>2. Identification with standard compact surface:
<2>1. $P^2 \# T$ is non-orientable because it contains an embedded Möbius band from the $P^2$ summand.
::: {.proof}
non-orientability of $P^2$.
:::
<2>2. Compute the Euler characteristic using $\chi(A \# B) = \chi(A) + \chi(B) - 2$:
\[
\chi(P^2 \# T) = \chi(P^2) + \chi(T) - 2 = 1 + 0 - 2 = -1.
\]
::: {.proof}
$\chi(P^2) = 1$ and $\chi(T) = 0$.
:::
<2>3. By the Classification Theorem for compact surfaces, every closed connected non-orientable surface is homeomorphic to the connected sum of $k$ projective planes $k P^2 = P^2 \# \cdots \# P^2$, which has Euler characteristic $\chi(k P^2) = 2 - k$.
::: {.proof}
Theorem 75.5.
:::
<2>4. Setting $2 - k = -1$ gives $k = 3$.
Thus $P^2 \# T \cong P^2 \# P^2 \# P^2 = 3P^2$ (the connected sum of three projective planes, Dyck's surface).
::: {.proof}
Dyck's Theorem / classification invariants.
:::

<1>3. Conclusion:
$H_1(P^2 \# T) \cong \mathbb{Z}^2 \oplus \mathbb{Z}_2$, and $P^2 \# T$ is homeomorphic to $P^2 \# P^2 \# P^2$ ($3 P^2$). Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
