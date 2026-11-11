---
schema: qual/card@1
id: E-MPUGI
kind: problem
title: Products with a locally compact Hausdorff factor preserve quotient maps
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §46 Exercise 9 was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked against Theorem 46.11 (the adjunction between
    maps X x Z -> Y and maps Z -> C(X,Y) for the compact-open topology), which the exercise says the proof
    uses, and against the defining property of a quotient map (§22: a map out of the quotient is continuous iff
    its composite with the quotient map is). Part (a): i_X x p is constant on the fibres of q, so it factors
    through the quotient Y as a bijection f with f o q = i_X x p, and f is continuous by the quotient property.
    Part (b): with G(b)(x) = g(x,b) and Q(a)(x) = q(x,a), the identity q = g o (i_X x p) gives Q = G o p
    pointwise. Part (c): q is continuous, so its adjoint Q is continuous by Theorem 46.11; p is quotient and
    Q = G o p, so G is continuous; applying Theorem 46.11 to G gives that g is continuous; hence f is a
    continuous bijection with continuous inverse, so i_X x p = f o q is a quotient map. Nothing needed
    correction.
---

::: {.exercise}

Here is an application of Theorem 46.11 to quotient maps.
(Compare [[E-S57IX]].)

Theorem.
If $p: A \to B$ is a quotient map and $X$ is locally compact Hausdorff, then $i_X \times p: X \times A \to X \times B$ is a quotient map.

(a) Let $Y$ be the quotient space induced by $i_X \times p$; let $q: X \times A \to Y$ be the quotient map.
Show there is a bijective continuous map $f: Y \to X \times B$ such that $f \circ q = i_X \times p$.

(b) Let $g = f^{-1}$.
Let $G: B \to \mathcal{C}(X, Y)$ and $Q: A \to \mathcal{C}(X, Y)$ be the maps induced by $g$ and $q$, respectively.
Show that $Q = G \circ p$.

(c) Show that $Q$ is continuous; conclude that $G$ is continuous, so that $g$ is continuous.
:::

::: {.solution}
Let $q:X\times A\to Y$ be the quotient induced by $i_X\times p$.

(a) The map $i_X\times p$ is constant exactly on the fibers of $q$, hence factors uniquely as
$$
X\times A\xrightarrow qY\xrightarrow fX\times B.
$$
The induced $f$ is bijective and continuous by the defining property of the quotient topology.

(b) Let $g=f^{-1}$. Give $C(X,Y)$ the compact-open topology. Theorem 46.11 states that, for $X$ locally compact Hausdorff and any space $Z$, a map $F:X\times Z\to Y$ is continuous if and only if the induced map $\hat F:Z\to C(X,Y)$, $\hat F(z)(x)=F(x,z)$, is continuous. The map $g$ induces
$$
G:B\to C(X,Y),\qquad G(b)(x)=g(x,b),
$$
and $q$ induces
$$
Q:A\to C(X,Y),\qquad Q(a)(x)=q(x,a).
$$
Since $f q=i_X\times p$, equivalently $q=g(i_X\times p)$, we have
$$
Q(a)(x)=g(x,p(a))=G(p(a))(x),
$$
so $Q=G\circ p$.

(c) The map $q:X\times A\to Y$ is continuous. Since $X$ is locally compact Hausdorff, Theorem 46.11 says its adjoint $Q:A\to C(X,Y)$ is continuous. Because $p$ is quotient and $Q=G\circ p$, the quotient criterion implies $G$ is continuous. Applying Theorem 46.11 again, the adjoint $g:X\times B\to Y$ is continuous. Hence the continuous bijection $f$ has continuous inverse, so $f$ is a homeomorphism. Therefore $i_X\times p$ is the composite of the quotient map $q$ with a homeomorphism, and is quotient.
:::
