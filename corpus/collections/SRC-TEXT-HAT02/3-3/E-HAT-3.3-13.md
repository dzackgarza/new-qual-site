---
schema: qual/card@1
id: E-HAT-3.3-13
kind: exercise
title: "No retraction onto subsurface of high genus"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

Let $M_h' \subset M_g$ be a compact subsurface of genus $h$ with one boundary circle, so $M_h'$ is homeomorphic to $M_h$ with an open disk removed.
Show there is no retraction $M_g \to M_h'$ if $h > g/2$.

::: {.solution}
<1>1. Suppose there is a retraction $r : M_g \to M_h'$.
::: {.proof}
assume such a retraction exists.
:::

<1>2. Let $i : M_h' \to M_g$ be the inclusion; then $r \circ i = \operatorname{id}_{M_h'}$.
::: {.proof}
definition of retraction.
:::

<1>3. Hence on $H_1$, $r_* \circ i_* = \operatorname{id}$, so $i_* : H_1(M_h') \to H_1(M_g)$ is injective.
::: {.proof}
<1>2 (if $r_* \circ i_* = \operatorname{id}$ then $i_*$ is injective).
:::

<1>4. $H_1(M_h') \cong \ZZ^{2h}$ and $H_1(M_g) \cong \ZZ^{2g}$.
::: {.proof}
$M_h'$ is a genus-$h$ surface with one boundary circle, so $H_1(M_h') \cong \ZZ^{2h}$; $M_g$ is a closed genus-$g$ surface, so $H_1(M_g) \cong \ZZ^{2g}$.
:::

<1>5. $i_*$ injective forces $2h \le 2g$, i.e. $h \le g$.
::: {.proof}
<1>3 and <1>4 (an injective map $\ZZ^{2h} \to \ZZ^{2g}$ requires $2h \le 2g$).
:::

<1>6. This alone does not rule out $h > g/2$; we need a stronger argument using the intersection form.
::: {.proof}
<1>5 is too weak.
:::

<1>7. The image of $i_*$ is a Lagrangian (isotropic) subspace of $H_1(M_g)$ with respect to the intersection form.
::: {.proof}
the boundary circle of $M_h'$ is null-homologous in $M_g$ (it bounds the complement $M_g \setminus M_h'$), so the image of $H_1(M_h')$ is isotropic for the intersection form; more precisely, the image has rank $2h$ and is isotropic, hence Lagrangian (half-dimensional).
:::

<1>8. A Lagrangian subspace of $H_1(M_g) \cong \ZZ^{2g}$ has rank $g$.
::: {.proof}
the intersection form is nondegenerate and symplectic, so a maximal isotropic subspace has half the dimension, i.e. rank $g$.
:::

<1>9. Hence $2h \le g$, i.e. $h \le g/2$.
::: {.proof}
<1>7 and <1>8 (the image of $i_*$ has rank $2h$ and is contained in a Lagrangian subspace of rank $g$).
:::

<1>10. Therefore if $h > g/2$, no retraction exists.
::: {.proof}
<1>9 (contrapositive).
:::

<1>11. Q.E.D.
::: {.proof}
<1>10.
:::
:::
