---
schema: qual/card@1
id: P-TOPF04D
kind: problem
title: "First homology of a compact nonorientable 3-manifold is infinite"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Manifolds
  - Orientation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $M$ be a compact connected nonorientable $3$-manifold.
Show the first integral homology group of $M$ is infinite.
:::

::: {.solution}
**Goal.** For a compact connected nonorientable $3$-manifold $M$, show $H_1(M;\ZZ)$ is infinite.

<1>1. $H_1(M;\ZZ)$ is infinite iff $b_1(M) \definedas \dim H_1(M;\QQ) > 0$.
::: {.proof}
$H_1(M;\ZZ)$ is finitely generated (compact manifold), and it is infinite iff its free part has positive rank, which is exactly $b_1(M)$.
:::

<1>2. $b_3(M) = 0$.
<2>1. $H_3(M;\ZZ) = \ZZ/2$ for a closed nonorientable $3$-manifold.
::: {.proof}
the top homology of a closed connected $n$-manifold is $\ZZ$ if orientable and $\ZZ/2$ if nonorientable.
:::
<2>2. Hence $H_3(M;\QQ) = H_3(M;\ZZ) \otimes \QQ = 0$.
::: {.proof}
$\ZZ/2 \otimes \QQ = 0$.
:::

<1>3. $\chi(M) = 0$.
<2>1. Let $\tilde M \to M$ be the orientation double cover; $\tilde M$ is a closed orientable $3$-manifold.
::: {.proof}
every nonorientable manifold has a connected orientable double cover.
:::
<2>2. $\chi(\tilde M) = 0$.
::: {.proof}
for a closed orientable odd-dimensional manifold, Poincaré duality gives $b_i = b_{3-i}$, so $\chi = \sum_{i=0}^3 (-1)^i b_i = 0$ (terms cancel in pairs).
:::
<2>3. $\chi(\tilde M) = 2\chi(M)$, so $\chi(M) = 0$.
::: {.proof}
Euler characteristic is multiplicative under finite covers.
:::

<1>4. $b_1(M) > 0$.
<2>1. $\chi(M) = b_0 - b_1 + b_2 - b_3$.
::: {.proof}
the Euler characteristic is the alternating sum of Betti numbers.
:::
<2>2. $b_0 = 1$ (connected) and $b_3 = 0$ (by <1>2).
::: {.proof}
$M$ is connected, and <1>2.2.
:::
<2>3. Hence $0 = \chi(M) = 1 - b_1 + b_2$, so $b_1 = 1 + b_2 \ge 1 > 0$.
::: {.proof}
substitute into <1>4.1.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.3 gives $b_1(M) > 0$, so by <1>1, $H_1(M;\ZZ)$ is infinite.
:::
:::
