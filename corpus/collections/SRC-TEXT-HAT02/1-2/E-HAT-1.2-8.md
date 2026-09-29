---
schema: qual/card@1
id: E-HAT-1.2-8
kind: problem
title: Fundamental group of two tori identified along a circle
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Compute the fundamental group of the space obtained from two tori $S^1 \times S^1$ by identifying a circle $S^1 \times \{x_0\}$ in one torus with the corresponding circle $S^1 \times \{x_0\}$ in the other torus.
:::

::: {.solution}
::: pf

::: pf-step
Decomposition of $X = T_1 \sqcup_C T_2$:

::: pf-proof

::: pf-step
Let $T_1 = S^1 \times S^1$ and $T_2 = S^1 \times S^1$ be two tori, and let $C \cong S^1$ be the identified circle $S^1 \times \{x_0\}$.

::: pf-proof
setup.
:::

:::

::: pf-step
Choose open neighborhoods $U$ of $T_1$ and $V$ of $T_2$ in $X$ that deformation retract onto $T_1$ and $T_2$ respectively, with $U \cap V$ deformation retracting onto $C \cong S^1$.

::: pf-proof
collar neighborhood of subcomplexes.
:::

:::

::: pf-step
The fundamental groups are:
\[
\pi_1(T_1) \cong \mathbb{Z}^2 = \langle a_1, b_1 \mid [a_1, b_1] = 1 \rangle, \quad
\pi_1(T_2) \cong \mathbb{Z}^2 = \langle a_2, b_2 \mid [a_2, b_2] = 1 \rangle, \quad
\pi_1(C) \cong \mathbb{Z} = \langle c \rangle.
\]

::: pf-proof
fundamental group of a torus is $\mathbb{Z} \times \mathbb{Z}$.
:::

:::

::: pf-step
The induced maps from the intersection $\pi_1(C)$ are given by $i_1(c) = a_1$ and $i_2(c) = a_2$.

::: pf-proof
$C$ is the coordinate circle corresponding to generator $a_i$.
:::

:::

:::

:::

::: {.pf-step #s2}
Application of the Seifert–van Kampen Theorem:

::: pf-proof

::: pf-step
By the Seifert–van Kampen Theorem, $\pi_1(X)$ is the amalgamated free product:
\[
\pi_1(X) \cong \pi_1(T_1) *_{\pi_1(C)} \pi_1(T_2) \cong \langle a_1, b_1, a_2, b_2 \mid [a_1, b_1] = 1, \, [a_2, b_2] = 1, \, a_1 = a_2 \rangle.
\]

::: pf-proof
Seifert–van Kampen Theorem.
:::

:::

::: pf-step
Setting $a = a_1 = a_2$, this presentation simplifies to:
\[
\pi_1(X) \cong \langle a, b_1, b_2 \mid [a, b_1] = 1, \, [a, b_2] = 1 \rangle.
\]

::: pf-proof
Tietze transformation eliminating $a_2$.
:::

:::

:::

:::

::: {.pf-step #s3}
Group-theoretic identification:

::: pf-proof

::: pf-step
In the presentation $\langle a, b_1, b_2 \mid [a, b_1] = 1, \, [a, b_2] = 1 \rangle$, the element $a$ commutes with both $b_1$ and $b_2$, so $a$ generates a central cyclic subgroup $\langle a \rangle \cong \mathbb{Z}$.

::: pf-proof
commutation relations.
:::

:::

::: pf-step
There are no relations between $b_1$ and $b_2$, so they generate a free group $F_2 = \langle b_1, b_2 \rangle$.

::: pf-proof
presentation of free products and direct products.
:::

:::

::: pf-step
Thus $\pi_1(X) \cong \mathbb{Z} \times F_2$, the direct product of the integers with the free group on two generators.

::: pf-proof
universal property of direct products.
:::

:::

:::

:::

::: pf-step
Conclusion: $\pi_1(X) \cong \langle a, b_1, b_2 \mid [a, b_1] = 1, \, [a, b_2] = 1 \rangle \cong \mathbb{Z} \times F_2$.

::: pf-proof
steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.
:::

:::

:::
:::
