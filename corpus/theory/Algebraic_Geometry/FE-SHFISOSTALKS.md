---
schema: qual/card@1
id: FE-SHFISOSTALKS
kind: example
title: Two sheaves with isomorphic stalks that are not isomorphic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Stalks
  - Direct Image Functor
relations:
- kind: uses
  target: D-VJFAP
review: draft
prompts:
- Give an example of two sheaves with isomorphic stalks at every point that are not isomorphic.
- Is the pushforward of a locally constant sheaf always locally constant?
---

::: {.example}
Let $X = Y = S^1 \subset \CC$ be the unit circle, and let $f \colon X \to Y$ be the two-sheeted covering map $f(z) = z^2$.
Let $S$ be a nontrivial abelian group (such as $\ZZ$ or $\ZZ/2\ZZ$), and let $\mcf = \ul{S}_X$ be the constant sheaf with value group $S$ on $X$.

At every point $y \in Y$, a sufficiently small connected open neighborhood $V \ni y$ has preimage $f^{-1}(V) = U_1 \amalg U_2$ consisting of two disjoint open intervals, on each of which $f$ restricts to a homeomorphism.
Therefore
\[
(f_* \mcf)(V) = \mcf(f^{-1}(V)) = \mcf(U_1) \oplus \mcf(U_2) \cong S \oplus S .
\]
Taking the direct limit over shrinking neighborhoods of $y$ gives the stalk
\[
(f_* \mcf)_y \cong S \oplus S .
\]
Now consider the constant sheaf $\mcg = \ul{S \oplus S}_Y$ on $Y$.
The stalk $\mcg_y$ is also $S \oplus S$ at every point $y \in Y$.
Thus $f_* \mcf$ and $\mcg$ have isomorphic stalks at every point of $Y$.

However, $f_* \mcf$ and $\mcg$ are not isomorphic as sheaves.
Their global sections differ:
\[
\Gamma(Y, \mcg) = \mcg(Y) \cong S \oplus S ,
\]
since $Y = S^1$ is connected, whereas
\[
\Gamma(Y, f_* \mcf) = \mcf(f^{-1}(Y)) = \mcf(X) \cong S ,
\]
because $X = S^1$ is also connected.
Since $S \not\cong S \oplus S$, no isomorphism exists between $f_* \mcf$ and $\mcg$.

Moreover, $f_* \mcf$ is not a locally constant sheaf on $Y$: any locally constant sheaf on $S^1$ whose stalks are isomorphic to $S \oplus S$ and whose monodromy is the transposition of the two sheets would have global sections isomorphic to the invariants $(S \oplus S)^{\ZZ/2\ZZ} \cong S$, exactly as computed here.
:::

::: {.remark}
The exam pitfall this addresses is the false deduction that a morphism of sheaves is an isomorphism if and only if stalks are abstractly isomorphic.
A map $f \colon \mcf \to \mcg$ is an isomorphism if and only if the induced stalk maps $f_x \colon \mcf_x \to \mcg_x$ are isomorphisms *for a specified morphism*. Without an ambient morphism between the sheaves, abstract isomorphism of stalks at all points does not imply isomorphism of the sheaves.
:::
