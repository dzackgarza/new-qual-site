---
schema: qual/card@1
id: P-TOPS25H
kind: problem
title: $\pi_3$ of the Poincaré homology sphere wedged with $S^3$
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the three containers state why their subclaims suffice, and the 7
    leaf steps that asserted their claim with no justification each carry a sentence deriving it. The
    trailing Q.E.D. was dropped. The mathematics is unchanged: the universal cover of $P\vee S^3$ is a
    wedge of $121$ three-spheres because the fibre has $120$ points and each carries one lifted sphere,
    covering maps are isomorphisms on $\pi_n$ for $n\ge2$, a wedge of $3$-spheres is $2$-connected,
    Hurewicz identifies $\pi_3$ with $H_3$, and $H_3$ of the wedge is $\ZZ^{121}$. Checked against the
    statement on the card, from the UCSD Spring 2025 topology qualifying exam. Nothing in the statement
    was changed.

---

::: {.problem}
Let $P$ be the Poincaré homology sphere, a 3-manifold whose fundamental group has order 120 and whose universal cover is $S^3$.
Compute $\pi_3$ of the wedge sum $P \vee S^3$.
:::

::: {.solution}

::: pf

::: pf-step
Fundamental group and universal covering space of $X = P \vee S^3$:

::: pf-proof

::: pf-step
By the Seifert–van Kampen Theorem:
$$
\pi_1(X) = \pi_1(P \vee S^3) \cong \pi_1(P) * \pi_1(S^3) \cong G * 0 \cong G,
$$
where $G = I^*$ is the binary icosahedral group of order $\cardinality{G} = 120$.

::: pf-proof
van Kampen applied to a wedge of two CW complexes gives the free product of the fundamental groups, and $\pi_1(S^3)=0$.
:::

:::

::: pf-step
The universal cover $\widetilde{X}$ of $X = P \vee S^3$ is obtained by unwrapping the universal cover $p_P: S^3 \to P$ (which is a $120$-sheeted covering):
The preimage of the basepoint $x_0 = P \cap S^3$ in the $S^3$ covering $P$ consists of $\cardinality{G} = 120$ distinct points.
At each of these $120$ points, a lift of the simply-connected wedge summand $S^3$ is attached.
Thus $\widetilde{X}$ is homeomorphic to a wedge sum of $1 + 120 = 121$ copies of $S^3$:
$$
\widetilde{X} \cong \bigvee_{j=1}^{121} S^3.
$$

::: pf-proof
The fibre over the basepoint of the universal cover has one point per element of $\pi_1(X)=G$; over the simply connected summand each sheet contributes a copy of $S^3$ attached at its preimage point, giving one sphere over $P$ and $120$ over the sphere, hence $121$ in all.
:::

:::

:::

:::

::: pf-step
Isomorphism on higher homotopy groups:

::: pf-proof

::: pf-step
For any covering space $p: \widetilde{X} \to X$ and any $n \ge 2$, the covering projection induces an isomorphism:
$$
p_*: \pi_n(\widetilde{X}) \xrightarrow{\sim} \pi_n(X).
$$
In particular, $\pi_3(P \vee S^3) \cong \pi_3(\widetilde{X})$.

::: pf-proof
A covering map is a fibration with discrete fibre, so it induces an isomorphism on $\pi_n$ for every $n\ge2$.
:::

:::

:::

:::

::: pf-step
Computation of $\pi_3(\widetilde{X})$ via the Hurewicz Theorem:

::: pf-proof

::: pf-step
$\widetilde{X} = \bigvee_{j=1}^{121} S^3$ is 2-connected:
$$
\pi_1(\widetilde{X}) = 0, \qquad \pi_2(\widetilde{X}) = 0.
$$

::: pf-proof
A wedge of $3$-spheres is simply connected because each summand is, and its second homotopy group vanishes because it is simply connected with $H_2=0$, by Hurewicz.
:::

:::

::: pf-step
By the Hurewicz Theorem, the Hurewicz homomorphism $h: \pi_3(\widetilde{X}) \to H_3(\widetilde{X}; \ZZ)$ is an isomorphism:
$$
\pi_3(\widetilde{X}) \cong H_3\left( \bigvee_{j=1}^{121} S^3; \ZZ \right).
$$

::: pf-proof
Hurewicz applies to a simply connected space with vanishing $\pi_2$ and gives an isomorphism in the first degree in which homotopy is non-zero, here degree $3$.
:::

:::

::: pf-step
By the additivity of homology on wedge sums of CW complexes:
$$
H_3\left( \bigvee_{j=1}^{121} S^3; \ZZ \right) \cong \bigoplus_{j=1}^{121} H_3(S^3; \ZZ) \cong \ZZ^{121}.
$$

::: pf-proof
Homology of a wedge of simply connected CW complexes is the direct sum of the reduced homologies, and each $S^3$ contributes $\ZZ$ in degree $3$.
:::

:::

:::

:::

::: pf-step
Conclusion:
$\pi_3(P \vee S^3) \cong \ZZ^{121}$.


::: pf-proof
Combining the isomorphism on homotopy groups induced by the covering, the Hurewicz isomorphism and the computation of $H_3$.
:::

:::

:::

:::
