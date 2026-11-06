---
schema: qual/card@1
id: P-AGHHYPSECTION
kind: problem
title: A hypersurface section drops the dimension by exactly one
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension
  - Krull Principal Ideal Theorem
  - Hypersurfaces
relations:
- kind: uses
  target: D-5LJUX
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry, §I.1 Exercise 1.8 (scan page
    23 of the retained PDF). What was checked: the hypotheses and conclusion
    against the card — Y an affine variety of dimension r in A^n, H a
    hypersurface with Y not contained in H, every irreducible component of Y
    cap H of dimension r - 1 — all present. The book closes with the cross-
    reference "(See (7.1) for a generalization.)", which the card had dropped;
    restored in the statement, since a bracketed pointer belongs to the
    source's wording. What was not checked: the solution was read only for
    consistency, not re-derived.
---

::: {.problem}
Let $Y$ be an affine variety of dimension $r$ in $\AA^n$, let $H$ be a hypersurface in $\AA^n$, and assume $Y \not\subseteq H$.
Show that every irreducible component of $Y \intersect H$ has dimension $r - 1$ (see (7.1) for a generalization).
:::

::: {.solution}
Write $H = V(f)$.
If $Y\intersect H=\emptyset$, there are no irreducible components and the
claim is vacuous. Assume $Y\intersect H\ne\emptyset$.
Irreducible components of $Y \intersect H$ correspond to the minimal primes $\mfp_i$ of $A(Y)$ containing $\generators{f}$, because $V(\mfp)$ is irreducible exactly when $\mfp$ is prime.

Since $Y \not\subseteq H$, the image of $f$ in $A(Y)$ is nonzero. Since
$Y\intersect H\ne\emptyset$, it is not a unit. The domain $A(Y)$ has no
nonzero zero divisors.
Krull's principal ideal theorem then gives $\height \mfp_i = 1$ for each such minimal prime.

For a finitely generated domain over a field, $\dim A(Y)/\mfp + \height \mfp = \dim A(Y)$, so each component $C_i = V(\mfp_i)$ has
$$
\dim C_i = \dim A(Y) - 1 = r - 1 .
$$
:::
