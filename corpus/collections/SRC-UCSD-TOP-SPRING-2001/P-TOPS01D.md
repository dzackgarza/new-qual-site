---
schema: qual/card@1
id: P-TOPS01D
kind: problem
title: "A simply-connected CW-complex with H_2 = Z+Z and no homology above degree 2 is a bouquet of two spheres"
classification:
  areas:
  - topology
  topics:
  - Homotopy Type
  - Cell Complexes
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $X$ be a (path-connected) simply-connected CW-complex with $H_2(X) \cong \mathbb{Z} \oplus \mathbb{Z}$ and $H_{\geq 3}(X) = 0$.
Prove that $X$ is homotopy-equivalent to the "bouquet of two spheres" $S^2 \vee S^2$.
:::

::: {.solution}
<1>1. $X$ is simply connected, so by the Hurewicz theorem $\pi_2(X) \cong H_2(X) \cong \ZZ \oplus \ZZ$.
::: {.proof}
Hurewicz theorem (the first nonzero homotopy group is isomorphic to the first nonzero homology group).
:::

<1>2. Choose generators $f_1, f_2 : S^2 \to X$ representing a basis of $\pi_2(X) \cong \ZZ^2$.
::: {.proof}
<1>1.
:::

<1>3. These combine to a map $f : S^2 \vee S^2 \to X$.
::: {.proof}
the wedge is the coproduct, so two maps out of $S^2$ give a map out of the wedge.
:::

<1>4. $f$ induces an isomorphism on $H_2$, and is the zero map on $H_0$, $H_1$, and $H_{\ge 3}$.
::: {.proof}
$H_2(S^2 \vee S^2) = \ZZ^2$ and $f$ sends the two generators to the basis $f_1, f_2$; $H_1 = 0$ on both sides (both simply connected), and $H_{\ge 3} = 0$ on both sides.
:::

<1>5. Hence $f$ induces an isomorphism on all homology groups.
::: {.proof}
<1>4.
:::

<1>6. Both $X$ and $S^2 \vee S^2$ are simply connected CW complexes, so by Whitehead's theorem $f$ is a homotopy equivalence.
::: {.proof}
a map between simply connected CW complexes inducing an isomorphism on all homology groups is a homotopy equivalence.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
