---
schema: qual/card@1
id: P-APASP07J
kind: problem
title: "Invariants of Z/3 acting on a two-dimensional vector space and Hilbert series"
classification:
  areas:
  - applied-algebra
  topics:
  - Commutative Algebra
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $G = \mathbb{Z}/3$ act on a two-dimensional vector space as a diagonal matrix with diagonal entries being $\theta, \theta^{-1}$, where $\theta = e^{2\pi i/3}$.

(a) Find a system of generators for $k[x,y]^G$.

(b) Calculate the Hilbert series for $k[x,y]^G$.

(c) Find at least one relation among the generators in (a). Give a precise description how you would find all possible relations (you need not carry out the calculations).
:::

::: {.solution}
Let $g$ be a generator of $G=C_3$. On the vector space, $g$ acts with eigenvalues $\theta$ and $\theta^{-1}$. On the dual coordinate functions the eigenvalues are inverted, so after possibly interchanging the names of $x$ and $y$ we may write
\[
g\cdot x=\theta x,
\qquad
g\cdot y=\theta^{-1}y.
\]
Thus a monomial $x^a y^b$ transforms by the scalar
\[
\theta^{a-b}.
\]
It is invariant exactly when
\[
a-b\equiv0\pmod3.
\]

If $a\equiv b\pmod3$, write the common residue as $r\in\{0,1,2\}$:
\[
a=3q+r,
\qquad
b=3s+r.
\]
Then
\[
x^a y^b=(x^3)^q(y^3)^s(xy)^r.
\]
Hence
\[
\boxed{k[x,y]^G=k[x^3,xy,y^3]}.
\]
So one system of generators is
\[
A=x^3,
\qquad B=xy,
\qquad C=y^3.
\]

The same residue decomposition shows that, as a graded $k[x^3,y^3]$-module,
\[
k[x,y]^G
=
k[x^3,y^3]
\oplus xy\,k[x^3,y^3]
\oplus x^2y^2\,k[x^3,y^3].
\]
Since $x^3$ and $y^3$ have degree $3$, while the three module generators have degrees $0,2,4$, the Hilbert series is
\[
\boxed{
H_{k[x,y]^G}(t)
=
\frac{1+t^2+t^4}{(1-t^3)^2}.
}
\]
Equivalently,
\[
H_{k[x,y]^G}(t)
=
\frac{1-t^6}{(1-t^2)(1-t^3)^2}.
\]

The generators satisfy the relation
\[
B^3=(xy)^3=x^3y^3=AC,
\]
so
\[
\boxed{B^3-AC=0}.
\]
In fact this generates all relations. Consider the surjective graded homomorphism
\[
\Phi:k[A,B,C]\longrightarrow k[x,y]^G,
\qquad
A\mapsto x^3,\quad B\mapsto xy,\quad C\mapsto y^3.
\]
The polynomial $B^3-AC$ lies in $\ker\Phi$. Modulo this relation, every monomial can be reduced to one with $B$-exponent $0,1,$ or $2$, so every residue class is a $k[A,C]$-linear combination of
\[
1,\ B,\ B^2.
\]
Their images are
\[
1,\ xy,\ x^2y^2,
\]
which are linearly independent over $k[x^3,y^3]$ because their monomials have distinct common exponent residues modulo $3$. Therefore no further relation exists, and
\[
\ker\Phi=(B^3-AC).
\]

A systematic Gröbner-basis method for finding all relations is to introduce new variables $A,B,C$ and form
\[
J=(A-x^3,\ B-xy,\ C-y^3)
\subset k[x,y,A,B,C].
\]
With an elimination order in which $x,y$ are larger than $A,B,C$, the elimination theorem gives
\[
J\cap k[A,B,C]=\ker\Phi.
\]
Computing a Gröbner basis and retaining the polynomials involving only $A,B,C$ therefore finds all algebraic relations among the invariant generators.
:::
