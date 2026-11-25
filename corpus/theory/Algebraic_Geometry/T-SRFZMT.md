---
schema: qual/card@1
id: T-SRFZMT
kind: theorem
title: Zariski's main theorem, and the factorization of birational maps of surfaces
slogan: 'On smooth projective surfaces, exceptional fibres stay connected and every birational map is built from finitely many blowups and blowdowns.'
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
- kind: uses
  target: T-MORSTEIN
- kind: related-to
  target: T-MORZMT
review: draft
prompts:
- What is Zariski's main theorem?
- How is a birational map of surfaces factored?
---

::: {.theorem title="Connected fibres of a proper birational morphism"}
Let $f \colon X \to Y$ be a proper birational morphism of Noetherian integral schemes with $Y$ normal.
Then every fibre $f^{-1}(y)$ is connected [@Har77, Corollary III.11.4], which prints the statement for a birational projective morphism of noetherian integral schemes; the proper case follows from the Stein-factorization argument on this card.
:::

::: {.theorem title="Elimination of indeterminacy on a surface"}
Let $X$ and $Y$ be smooth projective surfaces over an algebraically closed field, and let $F \colon X \dashrightarrow Y$ be a birational map.
Then there exist a smooth projective surface $W$ and birational morphisms $g \colon W \to X$ and $f \colon W \to Y$ with $F \circ g = f$ on the open subset of $W$ where $F \circ g$ is defined [@Har77, Theorem V.5.5].
:::

::: {.theorem title="Factorization"}
Let $f \colon X' \to X$ be a birational morphism of smooth projective surfaces and let $p$ be a fundamental point of $f^{-1}$.
Then $f$ factors through the blowup of $X$ at $p$ [@Har77, Proposition V.5.3], and [@Har77, Corollary V.5.4] counts the factors: $f$ is a composition of exactly as many monoidal transformations as there are irreducible curves of $X'$ contracted to points.
Consequently every birational map of smooth projective surfaces is a finite sequence of blowups followed by a finite sequence of blowdowns [@Har77, Theorem V.5.5].
:::

::: {.remark}
The connectedness theorem follows from [[T-MORSTEIN|Stein factorization]]: in the Stein factorization of a proper birational map to normal $Y$, the finite birational factor is an isomorphism, so the original morphism has connected fibres.

For a birational morphism of smooth projective surfaces, the exceptional locus is a finite union of curves and its image is a finite set of points. A fibre over such a point can contain several irreducible curves. Surface factorization proceeds one $(-1)$-curve at a time: [[T-SRFCAST|Castelnuovo's contractibility criterion]] contracts one such curve to a smooth point, and induction factors the whole morphism into point blowups.

Fundamental points are the points where the inverse map fails to be defined: the map is a morphism on a largest open $U$, and $X \setminus U$ is that finite set.
The total transform of a fundamental point is connected by the connected-fibres theorem and is positive-dimensional whenever the inverse is undefined there.

The factorization statement is the reason surfaces are classified up to birational equivalence rather than isomorphism, and why the invariants that matter — $p_g$, $q$, the plurigenera, $\kappa$ — are exactly those unchanged by blowup.
:::
