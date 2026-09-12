---
schema: qual/card@1
id: T-SRFZMT
kind: theorem
title: Zariski's main theorem, and the factorization of birational maps of surfaces
classification:
  areas:
  - algebraic-geometry
  topics:
  - Birational Geometry
  - Blowups
  - Surfaces
relations:
- kind: uses
  target: T-SRFCAST
review: draft
prompts:
- What is Zariski's main theorem?
- How is a birational map of surfaces factored?
---

::: {.theorem title="Zariski's main theorem"}
Let $f \colon X \to Y$ be a birational projective morphism of Noetherian integral schemes with $Y$ normal.
Then every fibre $f^{-1}(y)$ is connected.
:::

::: {.theorem title="Elimination of indeterminacy (Hironaka)"}
Let $X$ and $Y$ be smooth projective varieties and $F \colon X \dashrightarrow Y$ a birational map. Then there exist a smooth projective variety $W$ and birational morphisms $g \colon W \to X$ and $f \colon W \to Y$ fitting into
\[
\begin{tikzcd}
& W \arrow[dl, "g"'] \arrow[dr, "f"] & \\
X \arrow[rr, dashed, "F"] & & Y
\end{tikzcd}
\]
where $W$, $f$ and $g$ are as in Theorem 15.4. In particular every birational map is dominated by a common smooth blowup.
:::

::: {.theorem title="Factorization"}
Let $f \colon X' \to X$ be a birational morphism of smooth projective surfaces and let $p$ be a fundamental point of $f^{-1}$.
Then $f$ factors through the blowup of $X$ at $p$.
Consequently every birational map of smooth projective surfaces is a finite sequence of blowups followed by a finite sequence of blowdowns.
:::

::: {.remark}
The version to state first is the connectedness one, because that is the theorem; the surface statement is what it is used for.
A birational morphism of smooth surfaces is an isomorphism away from finitely many points, and at each such point the fibre is connected of dimension one — so it is a curve that gets contracted, and contraction of a curve to a smooth point is a blowup.

Fundamental points are the points where the inverse map fails to be defined: the map is a morphism on a largest open $U$, and $X \setminus U$ is that finite set.
The total transform of such a point is what Zariski's theorem says is connected and positive-dimensional.

The factorization statement is the reason surfaces are classified up to birational equivalence rather than isomorphism, and why the invariants that matter — $p_g$, $q$, the plurigenera, $\kappa$ — are exactly those unchanged by blowup.
:::
