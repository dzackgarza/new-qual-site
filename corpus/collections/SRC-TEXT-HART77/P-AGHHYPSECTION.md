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

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 1.8, PDF p. 1: since $f$ is neither a unit nor a zero divisor in $A(Y)$, every minimal prime containing it has height one by (1.11A), and the component's coordinate ring is $B/P$ with $\dim(B/P)=r-1$ by (1.8A).
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 1.8, PDF p. 2, and Jinhyun Park, *Algebraic Geometry by Robin Hartshorne: Exercises solutions*, Exercise 1.8, PDF p. 4, run the same argument, Park through a primary decomposition of $(f)$ in $A(Y)$ and its minimal primes.
The proof above names the correspondence between components of $Y\cap H$ and minimal primes of $A(Y)$ over $(f)$ — which all three use and none states — and then applies Krull's principal ideal theorem and the dimension formula exactly as they do.
Agree.
:::
