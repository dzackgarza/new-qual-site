---
schema: qual/card@1
id: E-2NLYP
kind: problem
title: A presentation for the fundamental group of the connected sum of the projective plane and the torus
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 74 Exercise 1, printed p. 453. The presentation from Theorem 74.2 and Theorem 70.1 at the common boundary circle. What was corrected: the closing paragraph derived P^2#T = 3P^2 from "Dyck's Theorem", which is not the source of that statement; it is Theorem 77.5 together with chi(P^2#T) = -1, and the card now says so. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 74 Exercise 1, printed p. 453. The presentation from Theorem 74.2 and Theorem 70.1 at the common boundary circle. What was corrected: the closing paragraph derived P^2#T = 3P^2 from "Dyck's Theorem", which is not the source of that statement; it is Theorem 77.5 together with chi(P^2#T) = -1, and the card now says so. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

Find a presentation for the fundamental group of $P^2 \# T$.
:::

::: {.solution}

Here $P^2$ is the real projective plane and $T = T^2$ is the torus.

::: pf

::: pf-step
Cell complex and polygonal scheme construction:

::: pf-proof

::: pf-step
The standard polygonal scheme for $P^2$ is a 2-gon with boundary word $a^2$, deformation retracting on a punctured disk to the loop $a$.
:::

::: pf-step
The standard polygonal scheme for $T^2$ is a 4-gon with boundary word $b c b^{-1} c^{-1}$, deformation retracting on a punctured disk to the wedge of loops $b$ and $c$.
:::

::: pf-step
The connected sum $P^2 \# T$ is formed by removing an open 2-disk from each surface and gluing along the resulting boundary circles $S^1$.
:::

::: pf-step
The resulting 2-manifold has a CW structure with:
- One 0-cell $x_0$.
- Three 1-cells (generating loops) $a, b, c$.
- One 2-cell attached along the boundary path obtained by concatenating the original boundary schemes:
  $$w = a^2 b c b^{-1} c^{-1}.$$
:::

:::

:::

::: pf-step
Presentation via Seifert-van Kampen Theorem:
$\pi_1(P^2 \# T) \cong \langle a, b, c \mid a^2 b c b^{-1} c^{-1} = 1 \rangle$.

::: pf-proof

::: pf-step
Decompose $P^2 \# T = U \cup V$ where $U \simeq P^2 \setminus \{\text{pt}\}$ and $V \simeq T^2 \setminus \{\text{pt}\}$.
:::

::: pf-step
$U$ deformation retracts to $S^1$ with $\pi_1(U) = \langle a \mid - \rangle$, and the boundary cycle corresponds to $a^2$.
:::

::: pf-step
$V$ deformation retracts to $S^1 \vee S^1$ with $\pi_1(V) = \langle b, c \mid - \rangle$, and the boundary cycle corresponds to $b c b^{-1} c^{-1}$.
:::

::: pf-step
The intersection $U \cap V \simeq S^1$ is connected, with generator $\gamma$ mapping to $a^2 \in \pi_1(U)$ and $(b c b^{-1} c^{-1})^{-1} \in \pi_1(V)$.
:::

::: pf-step
By the Seifert-van Kampen theorem, the amalgamated free product is:
$$\pi_1(P^2 \# T) \cong \pi_1(U) *_{\pi_1(U \cap V)} \pi_1(V) \cong \langle a, b, c \mid a^2 = c b c^{-1} b^{-1} \rangle \cong \langle a, b, c \mid a^2 b c b^{-1} c^{-1} = 1 \rangle.$$
:::

:::

:::

::: pf-step
Equivalent presentation from the classification theorem:
$P^2\#T$ is non-orientable, and $\chi(P^2\#T)=\chi(P^2)+\chi(T)-2=1+0-2=-1$; since the non-orientable closed surface with $\chi=2-k$ equal to $-1$ has $k=3$, the classification theorem, Theorem 77.5, gives $P^2\#T\cong P^2\#P^2\#P^2$. That surface has the presentation:
$$\pi_1(P^2 \# T) \cong \langle x, y, z \mid x^2 y^2 z^2 = 1 \rangle.$$
:::

::: pf-step
Conclusion:
A presentation for $\pi_1(P^2 \# T)$ is $\langle a, b, c \mid a^2 b c b^{-1} c^{-1} = 1 \rangle$.
:::

:::

:::
