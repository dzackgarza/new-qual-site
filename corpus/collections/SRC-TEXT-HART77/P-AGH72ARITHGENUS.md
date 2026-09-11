---
schema: qual/card@1
id: P-AGH72ARITHGENUS
kind: problem
title: Arithmetic genus $p_a(Y) = (-1)^r(P_Y(0) - 1)$ of hypersurfaces and products
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hilbert Polynomials
  - Arithmetic Genus
  - Complete Intersections
relations: []
review: draft
---

::: problem
Let $Y$ be a variety of dimension $r$ in $\PP^n$, with Hilbert polynomial $P_Y$.
Define the *arithmetic genus* of $Y$ to be
$$
p_a(Y) = (-1)^r \left( P_Y(0) - 1 \right).
$$
This is an important invariant which is independent of the projective embedding of $Y$.

1. Show that $p_a(\PP^n) = 0$.

2. If $Y$ is a plane curve of degree $d$, show that $p_a(Y) = \frac{1}{2}(d-1)(d-2)$.

3. More generally, if $H$ is a hypersurface of degree $d$ in $\PP^n$, show that $p_a(H) = \binom{d-1}{n}$.

4. If $Y$ is a complete intersection of surfaces of degrees $a, b$ in $\PP^3$, show that $p_a(Y) = \frac{1}{2}ab(a + b - 4) + 1$.

5. Let $Y^r \subseteq \PP^n$ and $Z^s \subseteq \PP^m$ be projective varieties, and embed $Y \times Z \subseteq \PP^n \times \PP^m \to \PP^N$ by the Segre embedding.
   Show that
$$
p_a(Y \times Z) = p_a(Y) p_a(Z) + (-1)^s p_a(Y) + (-1)^r p_a(Z).
$$
:::
