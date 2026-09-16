---
schema: qual/card@1
id: E-SS8.EX-15
kind: problem
title: "Here are two properties enjoyed by automorphisms of the upper half-plane"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
15. Here are two properties enjoyed by automorphisms of the upper half-plane.

(a) Suppose $\Phi$ is an automorphism of H that fixes three distinct points on the real axis.
Then Φ is the identity.

(b) Suppose $( x _ { 1 } , x _ { 2 } , x _ { 3 } )$ and $( y _ { 1 } , y _ { 2 } , y _ { 3 } )$ are two pairs of three distinct points on the real axis with

$$
x _ {1} <   x _ {2} <   x _ {3} \quad \text { and } \quad y _ {1} <   y _ {2} <   y _ {3}.
$$

Prove that there exists (a unique) automorphism Φ of H so that $\Phi ( x _ { j } ) = y _ { j }$ ， $j = 1 , 2 , 3$ . The same conclusion holds if $y _ { 3 } < y _ { 1 } < y _ { 2 }$ or $y _ { 2 } < y _ { 3 } < y _ { 1 }$
:::

::: {.solution}
Every automorphism of the upper half-plane has the form
\[
\Phi(z)=\frac{az+b}{cz+d},
\qquad a,b,c,d\in\mathbb R,
\qquad ad-bc>0.
\]

For part (a), a fixed point satisfies
\[
cz^2+(d-a)z-b=0.
\]
If three distinct real numbers are fixed, this quadratic polynomial has three distinct roots and hence is identically zero. Thus $c=b=0$ and $d=a$, so $\Phi(z)=z$.

For part (b), given three distinct real numbers $(x_1,x_2,x_3)$, define
\[
M_x(z)=\frac{(x_3-x_1)(z-x_2)}{(x_3-x_2)(z-x_1)}.
\]
Then
\[
M_x(x_1)=\infty,\qquad M_x(x_2)=0,\qquad M_x(x_3)=1.
\]
Its determinant has the sign of
\[
(x_3-x_1)(x_3-x_2)(x_2-x_1).
\]
For $x_1<x_2<x_3$ this sign is positive, so $M_x$ maps $\mathbb H$ to itself.

Define $M_y$ analogously. Under each of the three stated cyclic orderings of $(y_1,y_2,y_3)$,
\[
(y_3-y_1)(y_3-y_2)(y_2-y_1)>0,
\]
so $M_y$ also belongs to $\operatorname{Aut}(\mathbb H)$. Hence
\[
\Phi=M_y^{-1}\circ M_x
\]
is an automorphism of $\mathbb H$ satisfying $\Phi(x_j)=y_j$ for $j=1,2,3$.

If $\Psi$ is another such automorphism, then $\Psi^{-1}\circ\Phi$ fixes $x_1,x_2,x_3$, so part (a) implies $\Psi^{-1}\circ\Phi=\mathrm{id}$. Therefore $\Phi$ is unique.
:::
