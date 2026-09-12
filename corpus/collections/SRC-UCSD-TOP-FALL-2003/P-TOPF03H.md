---
schema: qual/card@1
id: P-TOPF03H
kind: problem
title: 'Universal cover of $\RP^3\vee S^2$ and computation of $\pi_2$'
classification:
  areas:
  - topology
  topics:
  - Universal Cover
  - Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Describe the universal cover of $X = \mathbb{RP}^3 \vee S^2$, and use it to compute the abelian group $\pi_2(X)$.
:::

::: {.solution}
<1>1. $\pi_1(\mathbb{RP}^3) = \ZZ/2$ and $\pi_1(S^2) = 1$.
::: {.proof}
$\mathbb{RP}^3$ has universal cover $S^3$ (a double cover), and $S^2$ is simply connected.
:::

<1>2. Hence $\pi_1(X) = \pi_1(\mathbb{RP}^3) * \pi_1(S^2) = \ZZ/2$.
::: {.proof}
van Kampen for the wedge (the wedge point is a common basepoint).
:::

<1>3. The universal cover $\widetilde X$ is obtained by attaching a copy of $S^2$ at each of the two points of $S^3$ lying over the wedge point.
::: {.proof}
the universal cover of $\mathbb{RP}^3$ is $S^3$, and the preimage of the wedge point is two points; over each, we attach a copy of the (simply connected) $S^2$ factor.
:::

<1>4. The universal cover is not literally the one-point wedge $S^3\vee S^2\vee S^2$: the two lifted $S^2$'s are attached at two distinct points of $S^3$. However,
$$
\widetilde X\simeq S^3\vee S^2\vee S^2.
$$
::: {.proof}
Choose an embedded arc in $S^3$ joining the two attachment points and include it as a subcomplex of a CW structure. Collapsing this contractible subcomplex identifies the two attachment points and is a homotopy equivalence. The resulting quotient has the homotopy type $S^3\vee S^2\vee S^2$.
:::

<1>5. $\pi_2(X) \cong \pi_2(\widetilde X)$.
::: {.proof}
the universal cover induces an isomorphism on $\pi_n$ for $n \ge 2$.
:::

<1>6. $\pi_2(\widetilde X)\cong\ZZ\oplus\ZZ$.
::: {.proof}
By <1>4, $\widetilde X\simeq S^3\vee S^2\vee S^2$. This wedge is simply connected, so the Hurewicz theorem gives
$$
\pi_2(\widetilde X)\cong H_2(\widetilde X)\cong H_2(S^3\vee S^2\vee S^2)\cong\ZZ^2.
$$
:::

<1>7. Hence $\pi_2(X) \cong \ZZ \oplus \ZZ$.
::: {.proof}
<1>5 and <1>6.
:::

<1>8. Q.E.D.
::: {.proof}
<1>7.
:::
:::
