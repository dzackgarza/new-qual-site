---
schema: qual/card@1
id: P-AMD-VH5QRTV2
kind: problem
title: A punctured torus retracts to two circles but not to its boundary
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Retracts
  - Surfaces
relations: []
review: draft
---

::: {.problem}
Let $X$ be a torus minus a hole.
Explain why $X$ is homotopy-equivalent to $S^1\vee S^1$.
Use the fundamental group to show that there does not exist a retraction $r\colon X\to\partial X$.
:::

::: {.solution}

::: pf

::: pf-step

A torus with an open disk removed deformation-retracts onto a wedge of two circles.

::: pf-proof

Use the usual square model of the torus and remove a small open disk around the unique vertex of the quotient. The remaining punctured torus has a standard spine consisting of the two generating loops $a$ and $b$ meeting at one point. Collapsing the complementary collar onto this spine gives a deformation retraction
$$
X\simeq S^1\vee S^1.
$$
Thus $\pi_1(X)\cong F(a,b)$.

:::

:::

::: {.pf-step #s2}

Under this identification, the boundary loop of the puncture represents the commutator
$$
[a,b]=aba^{-1}b^{-1}
$$
in $\pi_1(X)$.

::: pf-proof

The boundary word of the standard fundamental polygon for the torus is $aba^{-1}b^{-1}$. Removing a disk about the vertex turns this boundary word into the boundary component of the punctured torus.

:::

:::

::: pf-step

There is no retraction $r:X\to\partial X$.

::: pf-proof

Suppose such a retraction existed, and let $i:\partial X\hookrightarrow X$ be the inclusion. Then
$$
r_*\circ i_*=\operatorname{id}_{\pi_1(\partial X)}.
$$
Since $\pi_1(\partial X)\cong\mathbb Z$ is abelian, every homomorphism
$$
r_*:F(a,b)\to\mathbb Z
$$
kills the commutator subgroup, hence $r_*([a,b])=0$. But by step [](#s2){.pf-ref}, $i_*$ sends a generator of $\pi_1(\partial X)$ to $[a,b]$, so $r_*i_*$ sends that generator to $0$, contradicting that it is the identity.

:::

:::

:::

:::
