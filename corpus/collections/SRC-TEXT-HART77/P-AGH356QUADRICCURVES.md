---
schema: qual/card@1
id: P-AGH356QUADRICCURVES
kind: problem
title: Curves on a nonsingular quadric surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Quadric Surface
  - Divisors
  - Arithmetic Genus
  - Projective Normality
relations: []
review: draft
---

::: {.problem}
Let $Q$ be the nonsingular quadric surface $xy=zw$ in $X=\PP_k^3$ over a field $k$. We will consider locally principal closed subschemes $Y$ of $Q$. These correspond to Cartier divisors on $Q$ by (II, 6.17.1). On the other hand, we know that $\Pic Q \cong \ZZ \oplus \ZZ$, so we can talk about the type $(a, b)$ of $Y$ (II, 6.16) and (II, 6.6.1).

Let us denote the invertible sheaf $\mcl(Y)$ by $\mco_Q(a, b)$. Thus for any $n \in \ZZ$, $\mco_Q(n)=\mco_Q(n, n)$.

a. Use the special cases $(q, 0)$ and $(0, q)$, with $q>0$, when $Y$ is a disjoint union of $q$ lines $\PP^1$ in $Q$, to show:

    (1) if $\abs{a-b} \leq 1$, then $H^1(Q, \mco_Q(a, b))=0$;

    (2) if $a, b<0$, then $H^1(Q, \mco_Q(a, b))=0$;

    (3) if $a \leq -2$, then $H^1(Q, \mco_Q(a, 0)) \neq 0$.

b. Now use these results to show:

    (1) if $Y$ is a locally principal closed subscheme of type $(a, b)$, with $a, b>0$, then $Y$ is connected;

    (2) now assume $k$ is algebraically closed. Then for any $a, b>0$, there exists an irreducible nonsingular curve $Y$ of type $(a,b)$. Use (II, 7.6.2) and (II, 8.18).

    (3) an irreducible nonsingular curve $Y$ of type $(a, b)$, $a, b>0$ on $Q$ is projectively normal (II, Ex. 5.14) if and only if $\abs{a-b} \leq 1$. In particular, this gives lots of examples of nonsingular, but not projectively normal curves in $\PP^3$. The simplest is the one of type $(1,3)$, which is just the rational quartic curve (I, Ex. 3.18).

c. If $Y$ is a locally principal subscheme of type $(a, b)$ in $Q$, show that
\[
p_a(Y)=ab-a-b+1.
\]

Hint: Calculate Hilbert polynomials of suitable sheaves, and again use the special case $(q, 0)$ which is a disjoint union of $q$ copies of $\PP^1$. See (V, 1.5.2) for another method.
:::
