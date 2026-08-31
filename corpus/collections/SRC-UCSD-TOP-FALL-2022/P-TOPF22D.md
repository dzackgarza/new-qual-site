---
schema: qual/card@1
id: P-TOPF22D
kind: problem
title: "Connected closed non-orientable 3-manifold has infinite fundamental group"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Manifolds
  - Orientation
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Show that a connected closed non-orientable $3$-manifold must have infinite fundamental group.
:::

::: {.solution}
<1>1. Universal cover of a manifold with finite fundamental group:
<2>1. Suppose for contradiction that $\pi_1(M)$ is finite.
Let $p: \widehat{M} \to M$ be the universal covering space of $M$.
Because $\pi_1(M)$ is finite and $M$ is compact, $\widehat{M}$ is a compact, connected, simply-connected 3-manifold without boundary.
<2>2. Since $\widehat{M}$ is simply-connected, $\widehat{M}$ is orientable.
By Poincaré Duality and the Hurewicz Theorem:
- $H_0(\widehat{M}; \mathbb{Z}) \cong \mathbb{Z}$,
- $H_1(\widehat{M}; \mathbb{Z}) \cong \pi_1(\widehat{M})^{\mathrm{ab}} = \{0\}$,
- $H_2(\widehat{M}; \mathbb{Z}) \cong H^1(\widehat{M}; \mathbb{Z}) \cong \operatorname{Hom}(H_1(\widehat{M}), \mathbb{Z}) \oplus \operatorname{Ext}(H_0(\widehat{M}), \mathbb{Z}) = \{0\}$,
- $H_3(\widehat{M}; \mathbb{Z}) \cong \mathbb{Z}$.

<1>2. Lefschetz Fixed Point Theorem on deck transformations:
<2>1. The fundamental group $G = \pi_1(M)$ acts freely on $\widehat{M}$ as the group of deck transformations, with quotient $M \cong \widehat{M} / G$.
<2>2. Let $g \in G$ with $g \neq e$.
Because the action of $G$ is free, $g$ has no fixed points on $\widehat{M}$.
By the Lefschetz Fixed Point Theorem, the Lefschetz number of $g$ must vanish:
\[
\Lambda(g) = 0.
\]
<2>3. Compute the Lefschetz number of $g$:
\[
\Lambda(g) = \operatorname{tr}\left(g_* \big|_{H_0(\widehat{M})}\right) - \operatorname{tr}\left(g_* \big|_{H_1(\widehat{M})}\right) + \operatorname{tr}\left(g_* \big|_{H_2(\widehat{M})}\right) - \operatorname{tr}\left(g_* \big|_{H_3(\widehat{M})}\right).
\]
Since $H_0(\widehat{M}) \cong \mathbb{Z}$ and $g$ preserves the single connected component, $g_*|_{H_0} = 1$.
On top homology $H_3(\widehat{M}) \cong \mathbb{Z}$, $g_*|_{H_3} = \deg(g) \in \{\pm 1\}$.
Thus:
\[
\Lambda(g) = 1 - 0 + 0 - \deg(g) = 1 - \deg(g).
\]
<2>4. Setting $\Lambda(g) = 0$ gives $1 - \deg(g) = 0$, so:
\[
\deg(g) = +1 \quad \text{for every } g \in G.
\]

<1>3. Contradiction to non-orientability:
<2>1. Since $\deg(g) = +1$ for every $g \in G$, every deck transformation preserves the orientation of $\widehat{M}$.
<2>2. The quotient of an orientable manifold by a group of orientation-preserving free homeomorphisms is orientable, so $M = \widehat{M}/G$ must be orientable.
This contradicts the hypothesis that $M$ is non-orientable.

<1>4. Conclusion:
$\pi_1(M)$ must be infinite. Q.E.D.
:::
