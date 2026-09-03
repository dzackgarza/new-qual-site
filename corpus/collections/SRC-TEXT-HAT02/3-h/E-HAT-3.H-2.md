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
---

Compute the homology groups with local coefficients $H_n(M; M_{\mathbb{Z}})$ for a closed nonorientable surface $M$.

::: {.solution}
<1>1. Setup and Poincaré Duality with local coefficients:
<2>1. Let $M = N_g$ ($g \ge 1$) be a closed connected nonorientable surface of genus $g$ (homeomorphic to $\#^g \mathbb{RP}^2$).
Let $\mathcal{L} = \mathcal{M}_\mathbb{Z}$ be the orientation local coefficient system with fiber $\mathbb{Z}$, where loops act by $\pm 1$ according to their orientation character $w_1: \pi_1(M) \to \{\pm 1\}$.
<2>2. By Poincaré Duality for manifolds with local coefficients, for any closed $n$-manifold:
\[
H_k(M; \mathcal{L}) \cong H^{n-k}(M; \mathbb{Z}).
\]
For $n = 2$, this gives $H_k(M; \mathcal{L}) \cong H^{2-k}(M; \mathbb{Z})$.

<1>2. Cohomology of $M$ with standard $\mathbb{Z}$ coefficients:
<2>1. The integral homology groups of $M = N_g$ are:
- $H_0(M; \mathbb{Z}) \cong \mathbb{Z}$,
- $H_1(M; \mathbb{Z}) \cong \mathbb{Z}^{g-1} \oplus \mathbb{Z}_2$,
- $H_2(M; \mathbb{Z}) \cong 0$,
- $H_k(M; \mathbb{Z}) = 0$ for $k > 2$.
<2>2. Applying the Universal Coefficient Theorem for Cohomology $H^k(M) \cong \operatorname{Hom}(H_k(M), \mathbb{Z}) \oplus \operatorname{Ext}(H_{k-1}(M), \mathbb{Z})$:
- $H^0(M; \mathbb{Z}) \cong \operatorname{Hom}(\mathbb{Z}, \mathbb{Z}) \cong \mathbb{Z}$,
- $H^1(M; \mathbb{Z}) \cong \operatorname{Hom}(\mathbb{Z}^{g-1} \oplus \mathbb{Z}_2, \mathbb{Z}) \oplus \operatorname{Ext}(\mathbb{Z}, \mathbb{Z}) \cong \mathbb{Z}^{g-1}$,
- $H^2(M; \mathbb{Z}) \cong \operatorname{Hom}(0, \mathbb{Z}) \oplus \operatorname{Ext}(\mathbb{Z}^{g-1} \oplus \mathbb{Z}_2, \mathbb{Z}) \cong 0 \oplus \mathbb{Z}_2 \cong \mathbb{Z}_2$,
- $H^k(M; \mathbb{Z}) = 0$ for $k > 2$.

<1>3. Computation of $H_n(M; \mathcal{L})$:
<2>1. Applying the Poincaré Duality isomorphisms $H_k(M; \mathcal{L}) \cong H^{2-k}(M; \mathbb{Z})$:
\[
H_n(M; \mathcal{M}_\mathbb{Z}) \cong \begin{cases}
\mathbb{Z} & n = 2, \\
\mathbb{Z}^{g-1} & n = 1, \\
\mathbb{Z}_2 & n = 0, \\
0 & n \ge 3 \text{ or } n < 0.
\end{cases}
\]

<1>4. Verification via the twisted cellular chain complex:
<2>1. In the standard CW structure of $N_g$ (one 0-cell, $g$ 1-cells $a_1, \dots, a_g$, and one 2-cell attached along $a_1^2 \cdots a_g^2$), the orientation twist gives:
- $d_1(a_i) = (-1 - 1) e^0 = -2 e^0$, so $\operatorname{Im}(d_1) = 2\mathbb{Z}$, yielding $H_0 \cong \mathbb{Z} / 2\mathbb{Z} \cong \mathbb{Z}_2$.
- $d_2(e^2) = \sum_{i=1}^g (1 + (-1)) a_i = 0$, so $\ker(d_2) = \mathbb{Z}$, yielding $H_2 \cong \mathbb{Z}$.
- $H_1 \cong \ker(d_1) / \operatorname{Im}(d_2) = \mathbb{Z}^{g-1} / 0 \cong \mathbb{Z}^{g-1}$.

<1>5. Conclusion:
$H_2(M; \mathcal{M}_\mathbb{Z}) \cong \mathbb{Z}$, $H_1(M; \mathcal{M}_\mathbb{Z}) \cong \mathbb{Z}^{g-1}$, $H_0(M; \mathcal{M}_\mathbb{Z}) \cong \mathbb{Z}_2$, and $H_n(M; \mathcal{M}_\mathbb{Z}) = 0$ for $n \ge 3$. Q.E.D.
:::
