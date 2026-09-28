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
---

::: {.problem}
Let $Y$ be an affine variety of dimension $r$ in $\AA^n$, let $H$ be a hypersurface in $\AA^n$, and assume $Y \not\subseteq H$.
Show that every irreducible component of $Y \intersect H$ has dimension $r - 1$.
:::

::: {.solution}
Write $H = V(f)$.
Irreducible components of $Y \intersect H$ correspond to the minimal primes $\mfp_i$ of $A(Y)$ containing $\gens{f}$, because $V(\mfp)$ is irreducible exactly when $\mfp$ is prime.

Since $Y \not\subseteq H$, the image of $f$ in $A(Y)$ is nonzero, and $A(Y)$ is a domain, so $f$ is neither a unit nor a zero divisor.
Krull's principal ideal theorem then gives $\height \mfp_i = 1$ for each such minimal prime.

For a finitely generated domain over a field, $\dim A(Y)/\mfp + \height \mfp = \dim A(Y)$, so each component $C_i = V(\mfp_i)$ has
\[
\dim C_i = \dim A(Y) - 1 = r - 1 .
\]
:::
