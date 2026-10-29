---
schema: qual/card@1
id: P-TOPF24G
kind: problem
title: 'Fundamental group and $\pi_2$ of $\RP^3 \# \RP^3$'
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
What is the fundamental group of $X = \RP^3 \# \RP^3$?
Give a description of the universal cover $\widetilde{X}$ of $X$ and use this to calculate $\pi_2(X)$.
:::

::: {.solution}
::: pf

::: pf-step
Computation of $\pi_1(X)$:

::: pf-proof

::: pf-step
By definition of the connected sum of 3-manifolds, $X = M_1 \# M_2$ is formed by deleting the interior of an open 3-ball $B^3$ from each copy of $\RP^3$ to obtain $M_1' = M_2' = \RP^3 \setminus \operatorname{int}(D^3)$, and gluing along their boundary 2-spheres:
$$X = M_1' \cup_{S^2} M_2'.$$
:::

::: pf-step
Since $\operatorname{codim}(D^3) = 3 \ge 3$, removing an open 3-ball does not affect the fundamental group:
$$\pi_1(M_1') \cong \pi_1(\RP^3) \cong \ZZ/2\ZZ, \qquad \pi_1(M_2') \cong \pi_1(\RP^3) \cong \ZZ/2\ZZ.$$
:::

::: pf-step
The neck $S^2$ is simply connected ($\pi_1(S^2) = 0$).
:::

::: pf-step
Applying the Seifert–van Kampen Theorem to the open collar neighborhood decomposition of $X$:
$$\pi_1(X) \cong \pi_1(M_1') *_{\pi_1(S^2)} \pi_1(M_2') \cong (\ZZ/2\ZZ) *_{\{e\}} (\ZZ/2\ZZ) \cong \ZZ/2\ZZ * \ZZ/2\ZZ \cong D_\infty,$$
which is the infinite dihedral group $D_\infty = \langle a, b \mid a^2 = b^2 = 1 \rangle$.
:::

:::

:::

::: pf-step
Description of the universal cover $\widetilde{X}$:

::: pf-proof

::: pf-step
The universal cover of $M_1' = \RP^3 \setminus \operatorname{int}(D^3)$ is $\widetilde{M}_1' = S^3 \setminus (D_1^3 \cup D_2^3)$ (the 3-sphere with two antipodal open 3-balls removed).
:::

::: pf-step
The space $\widetilde{M}_1' = S^3 \setminus (D_1^3 \cup D_2^3)$ is homeomorphic to the cylinder $S^2 \times [-1, 1]$, which deformation retracts to $S^2$.
:::

::: pf-step
The Cayley graph of the group $G = \ZZ/2\ZZ * \ZZ/2\ZZ$ with respect to the generators $\{a, b\}$ is an infinite line (a 1D tree with vertices indexed by $\ZZ$).
:::

::: pf-step
The universal cover $\widetilde{X}$ is the tree-like plumbing of building blocks according to the Cayley tree: it is formed by gluing countably infinitely many copies of $S^2 \times [-1, 1]$ end-to-end along their boundary 2-spheres.
:::

::: pf-step
Collapsing the cylinder intervals gives a homeomorph/deformation retraction of the entire infinite chain to
$$\widetilde{X} \cong S^2 \times \RR.$$
:::

::: pf-step
Thus the universal cover $\widetilde{X}$ is homeomorphic to $S^2 \times \RR$, which deformation retracts to $S^2$.
:::

:::

:::

::: pf-step
Computation of $\pi_2(X)$:

::: pf-proof

::: pf-step
For any covering space $p: \widetilde{X} \to X$, the induced homomorphism on homotopy groups $p_*: \pi_k(\widetilde{X}) \to \pi_k(X)$ is an isomorphism for all $k \ge 2$.
:::

::: pf-step
In particular, for $k = 2$:
$$\pi_2(X) \cong \pi_2(\widetilde{X}).$$
:::

::: pf-step
Since $\widetilde{X} \simeq S^2 \times \RR \simeq S^2$:
$$\pi_2(\widetilde{X}) \cong \pi_2(S^2 \times \RR) \cong \pi_2(S^2) \oplus \pi_2(\RR) \cong \ZZ \oplus 0 \cong \ZZ.$$
:::

::: pf-step
Therefore $\pi_2(X) \cong \ZZ$.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$\pi_1(X) \cong \ZZ/2\ZZ * \ZZ/2\ZZ$, the universal cover is $\widetilde{X} \cong S^2 \times \RR \simeq S^2$, and $\pi_2(X) \cong \ZZ$.
:::

:::

:::
:::
