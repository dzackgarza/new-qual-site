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

::: {.problem}
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

<1>4. $f$ induces an isomorphism on every homology group.
::: {.proof}
On $H_2$, the two sphere generators map to the chosen basis of $H_2(X)\cong\ZZ^2$, so $f_*$ is an isomorphism. Both spaces are path connected, hence $f_*:H_0(S^2\vee S^2)\to H_0(X)$ is the canonical isomorphism $\ZZ\to\ZZ$. Both $H_1$ groups vanish because the spaces are simply connected, and all homology groups in degrees at least $3$ vanish by hypothesis and by the homology of $S^2\vee S^2$.
:::

<1>5. Both $X$ and $S^2 \vee S^2$ are simply connected CW complexes, so by Whitehead's theorem $f$ is a homotopy equivalence.
::: {.proof}
a map between simply connected CW complexes inducing an isomorphism on all homology groups is a homotopy equivalence.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::
