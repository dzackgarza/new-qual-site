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
---

::: problem
Let $P$ be the Poincaré homology sphere, a 3-manifold whose fundamental group has order 120 and whose universal cover is $S^3$.
Compute $\pi_3$ of the wedge sum $P \vee S^3$.
:::

::: {.solution}
<1>1. Fundamental group and universal covering space of $X = P \vee S^3$:
<2>1. By the Seifert–van Kampen Theorem:
\[
\pi_1(X) = \pi_1(P \vee S^3) \cong \pi_1(P) * \pi_1(S^3) \cong G * 0 \cong G,
\]
where $G = I^*$ is the binary icosahedral group of order $|G| = 120$.
Proof: Seifert–van Kampen Theorem for wedge sums.
<2>2. The universal cover $\widetilde{X}$ of $X = P \vee S^3$ is obtained by unwrapping the universal cover $p_P: S^3 \to P$ (which is a $120$-sheeted covering):
The preimage of the basepoint $x_0 = P \cap S^3$ in the $S^3$ covering $P$ consists of $|G| = 120$ distinct points.
At each of these $120$ points, a lift of the simply-connected wedge summand $S^3$ is attached.
Thus $\widetilde{X}$ is homeomorphic to a wedge sum of $1 + 120 = 121$ copies of $S^3$:
\[
\widetilde{X} \cong \bigvee_{j=1}^{121} S^3.
\]
Proof: covering space construction for wedge sums with a simply connected summand.

<1>2. Isomorphism on higher homotopy groups:
<2>1. For any covering space $p: \widetilde{X} \to X$ and any $n \ge 2$, the covering projection induces an isomorphism:
\[
p_*: \pi_n(\widetilde{X}) \xrightarrow{\sim} \pi_n(X).
\]
In particular, $\pi_3(P \vee S^3) \cong \pi_3(\widetilde{X})$.
Proof: long exact sequence of homotopy groups for a covering space (fibration with discrete fiber).

<1>3. Computation of $\pi_3(\widetilde{X})$ via the Hurewicz Theorem:
<2>1. $\widetilde{X} = \bigvee_{j=1}^{121} S^3$ is 2-connected:
\[
\pi_1(\widetilde{X}) = 0, \qquad \pi_2(\widetilde{X}) = 0.
\]
Proof: wedge sum of simply connected CW complexes with cells only in dimensions $0$ and $3$.
<2>2. By the Hurewicz Theorem, the Hurewicz homomorphism $h: \pi_3(\widetilde{X}) \to H_3(\widetilde{X}; \mathbb{Z})$ is an isomorphism:
\[
\pi_3(\widetilde{X}) \cong H_3\left( \bigvee_{j=1}^{121} S^3; \mathbb{Z} \right).
\]
Proof: Hurewicz Theorem for 2-connected spaces.
<2>3. By the additivity of homology on wedge sums of CW complexes:
\[
H_3\left( \bigvee_{j=1}^{121} S^3; \mathbb{Z} \right) \cong \bigoplus_{j=1}^{121} H_3(S^3; \mathbb{Z}) \cong \mathbb{Z}^{121}.
\]
Proof: cellular homology of wedge sums.

<1>4. Conclusion:
$\pi_3(P \vee S^3) \cong \mathbb{Z}^{121}$. Q.E.D.
Proof: <1>1 through <1>3.
:::
