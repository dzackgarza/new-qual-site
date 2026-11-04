---
schema: qual/card@1
id: E-HAT-3.H-2
kind: problem
title: "Homology of nonorientable surfaces with local coefficients"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof repaired: the card invoked Poincare duality for an arbitrary local system, which is false -- for M = N_g with the trivial system H_2(M;Z)=0 while H^0(M;Z)=Z. The step is replaced by the duality that actually applies, Theorem 3H.6 for the orientation system, with the fundamental class supplied by Example 3H.3. The groups the card computes are unchanged.
---

::: {.problem}
Compute the homology groups with local coefficients $H_n(M; M_{\ZZ})$ for a closed nonorientable surface $M$.
:::

::: {.solution}
::: pf

::: pf-step
Setup and Poincaré Duality with local coefficients:

::: pf-proof

::: pf-step
Let $M = N_g$ ($g \ge 1$) be a closed connected nonorientable surface of genus $g$ (homeomorphic to $\#^g \RP^2$).
Let $\mathcal{L} = \mathcal{M}_\ZZ$ be the orientation local coefficient system with fiber $\ZZ$, where loops act by $\pm 1$ according to their orientation character $w_1: \pi_1(M) \to \{\pm 1\}$.
:::

::: pf-step
Duality must be applied to the *orientation* system, not to an arbitrary one. In the generality stated,
Poincaré duality with local coefficients is false: for $M=N_g$ and $\mathcal{L}=\ZZ$ the trivial
system, $H_2(M;\ZZ)=0$ (Theorem 3.26: $H_n(M;\ZZ)$ is $\ZZ$ for $M$ closed, connected and orientable and $0$ otherwise; Example 3H.3 uses exactly this), whereas $H^0(M;\ZZ)=\ZZ$ because $M$ is connected; so
"$H_k(M;\mathcal L)\cong H^{n-k}(M;\ZZ)$ for any closed $n$-manifold and any local system" fails
already for $k=n=2$. What is true, and all that is used, is the following.

Write $\widetilde{\ZZ}=M_\ZZ$ for the system with fibre $\ZZ$ on which a loop acts by $+1$ or $-1$
according to its orientation character $w_1\colon\pi_1M\to\{\pm1\}$; this is the $\mathcal L$ of the
present computation, and $M$ is closed, connected and nonorientable.

(i) *Fundamental class.* By Example 3H.3 (the exact sequence of the twofold orientable cover
$\widetilde M\to M$): $H_n(M;\widetilde{\ZZ})\approx H_n(\widetilde M)\approx\ZZ$; Hatcher identifies
the resulting class as a fundamental class for the nonorientable manifold $M$. In the paragraph
preceding Theorem 3H.6 he states the version of duality that the cap product with a fundamental class
gives for a bundle of rings $E$, under the assumption "that there exists a fundamental class
$[M]\in H_n(M;E)$ restricting to a generator of $H_n(M,M-\{x\};E)$ for all $x\in M$", and notes that
the class just constructed from $H_n(M;\widetilde{\ZZ})$ can be viewed as such a class — the *pure
imaginary fundamental class* $[M]\in H_n(M;E)$ for $E$ the bundle of rings $\ZZ[i]$ with conjugation
acting by $\omega=w_1$.

(ii) *The duality in the form used.* Cap product with that class is an isomorphism
$$
[M]\frown(-)\colon H^{k}(M;\ZZ)\;\xrightarrow{\ \approx\ }\;H_{n-k}(M;\widetilde{\ZZ})
$$
(Theorem 3H.6, first displayed isomorphism). Replacing $k$ by $n-j$ gives, for all $j$,
$$
H_j(M;\mathcal M_{\ZZ})=H_j(M;\widetilde{\ZZ})\;\cong\;H^{\,n-j}(M;\ZZ).
$$
For the surface $n=2$ this is exactly $H_j(M;\mathcal L)\cong H^{2-j}(M;\ZZ)$, $j=0,1,2$.

(For an *orientable* closed connected $n$-manifold the analogous statement with $\mathcal L=\ZZ$ is ordinary Poincaré duality, Theorem 3.30; the $M$ of this exercise is nonorientable, so Theorem 3H.6 is the applicable form.)
:::

:::

:::

::: pf-step
Cohomology of $M$ with standard $\ZZ$ coefficients:

::: pf-proof

::: pf-step
The integral homology groups of $M = N_g$ are:
- $H_0(M; \ZZ) \cong \ZZ$,
- $H_1(M; \ZZ) \cong \ZZ^{g-1} \oplus \ZZ_2$,
- $H_2(M; \ZZ) \cong 0$,
- $H_k(M; \ZZ) = 0$ for $k > 2$.
:::

::: pf-step
Applying the Universal Coefficient Theorem for Cohomology $H^k(M) \cong \operatorname{Hom}(H_k(M), \ZZ) \oplus \operatorname{Ext}(H_{k-1}(M), \ZZ)$:
- $H^0(M; \ZZ) \cong \operatorname{Hom}(\ZZ, \ZZ) \cong \ZZ$,
- $H^1(M; \ZZ) \cong \operatorname{Hom}(\ZZ^{g-1} \oplus \ZZ_2, \ZZ) \oplus \operatorname{Ext}(\ZZ, \ZZ) \cong \ZZ^{g-1}$,
- $H^2(M; \ZZ) \cong \operatorname{Hom}(0, \ZZ) \oplus \operatorname{Ext}(\ZZ^{g-1} \oplus \ZZ_2, \ZZ) \cong 0 \oplus \ZZ_2 \cong \ZZ_2$,
- $H^k(M; \ZZ) = 0$ for $k > 2$.
:::

:::

:::

::: pf-step
Computation of $H_n(M; \mathcal{L})$:

::: pf-proof

::: pf-step
Applying the Poincaré Duality isomorphisms $H_k(M; \mathcal{L}) \cong H^{2-k}(M; \ZZ)$:
$$
H_n(M; \mathcal{M}_\ZZ) \cong \begin{cases}
\ZZ & n = 2, \\
\ZZ^{g-1} & n = 1, \\
\ZZ_2 & n = 0, \\
0 & n \ge 3 \text{ or } n < 0.
\end{cases}
$$
:::

:::

:::

::: pf-step
Verification via the twisted cellular chain complex:

::: pf-proof

::: pf-step
In the standard CW structure of $N_g$ (one 0-cell, $g$ 1-cells $a_1, \dots, a_g$, and one 2-cell attached along $a_1^2 \cdots a_g^2$), the orientation twist gives:
- $d_1(a_i) = (-1 - 1) e^0 = -2 e^0$, so $\operatorname{Im}(d_1) = 2\ZZ$, yielding $H_0 \cong \ZZ / 2\ZZ \cong \ZZ_2$.
- $d_2(e^2) = \sum_{i=1}^g (1 + (-1)) a_i = 0$, so $\ker(d_2) = \ZZ$, yielding $H_2 \cong \ZZ$.
- $H_1 \cong \ker(d_1) / \operatorname{Im}(d_2) = \ZZ^{g-1} / 0 \cong \ZZ^{g-1}$.
:::

:::

:::

::: pf-step
Conclusion:
$H_2(M; \mathcal{M}_\ZZ) \cong \ZZ$, $H_1(M; \mathcal{M}_\ZZ) \cong \ZZ^{g-1}$, $H_0(M; \mathcal{M}_\ZZ) \cong \ZZ_2$, and $H_n(M; \mathcal{M}_\ZZ) = 0$ for $n \ge 3$.
:::

:::

:::
