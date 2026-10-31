---
schema: qual/card@1
id: E-HAT-4.2-31
kind: problem
title: "Split sequences from nullhomotopic fiber inclusions"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 31; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
For a fiber bundle $F \to E \to B$ such that the inclusion $F \hookrightarrow E$ is homotopic to a constant map, show that the long exact sequence of homotopy groups breaks up into split short exact sequences giving isomorphisms $\pi_n(B) \approx \pi_n(E) \oplus \pi_{n-1}(F)$.
In particular, for the Hopf bundles $S^3 \to S^7 \to S^4$ and $S^7 \to S^{15} \to S^8$ this yields isomorphisms $\pi_n(S^4) \approx \pi_n(S^7) \oplus \pi_{n-1}(S^3)$ and $\pi_n(S^8) \approx \pi_n(S^{15}) \oplus \pi_{n-1}(S^7)$.
Thus $\pi_7(S^4)$ and $\pi_{15}(S^8)$ contain $\ZZ$ summands.
:::

::: {.solution}
Write $i:F\to E$ and $p:E\to B$, and take $n\ge2$. Since $i$ is nullhomotopic, its maps on homotopy groups vanish. The bundle sequence therefore contains
$$
0\longrightarrow\pi_n(E)\xrightarrow{p_*}\pi_n(B)\xrightarrow{\partial}\pi_{n-1}(F)\longrightarrow0.
$$

Fix a based nullhomotopy $H:F\times I\to E$ of $i$. Its projection $pH$ is constant at the two ends of the cylinder, so it induces a map $\overline H:\Sigma F\to B$. Define
$$
s:\pi_{n-1}(F)\longrightarrow\pi_n(B),\qquad
s([a])=[\overline H\circ\Sigma a].
$$
The fixed nullhomotopy makes $s$ independent of the representative $a$. Suspension is a homomorphism on these homotopy groups, so $s$ is a homomorphism. Lifting the suspended map over the two cone halves by the original fiber map and by $H$ shows from the definition of the connecting homomorphism that $\partial s([a])=[a]$, after choosing the suspension orientation. Thus the short exact sequence splits. For $n=2$, its surjectivity also shows that $\pi_1(F)$ is abelian, as required by the displayed direct sum.

In each of the stated Hopf bundles the fiber inclusion is nullhomotopic, since a map from the fiber sphere into the higher-dimensional total sphere is nullhomotopic. Hence
$$
\pi_n(S^4)\cong\pi_n(S^7)\oplus\pi_{n-1}(S^3),\qquad
\pi_n(S^8)\cong\pi_n(S^{15})\oplus\pi_{n-1}(S^7).
$$
Taking $n=7$ and $n=15$ respectively gives a $\ZZ$ summand in each asserted group.
:::
