---
schema: qual/card@1
id: P-JHUSP03CAA
kind: problem
title: Meromorphic functions on the sphere and rational boundary-modulus extensions
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both parts with Spring 2003 Complex Analysis problem 1, including the pole-at-infinity hypothesis and the unit-circle boundary modulus condition."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Proved rationality from finitely many principal parts and polynomial growth at infinity, then glued the reciprocal-reflection across the unit circle by Morera and applied the sphere result."
---

(a) Let $f : \mathbb{C} \to \mathbb{C}$ be meromorphic with a pole at infinity.
Show that $f$ must be a rational function.

(b) Use the above to prove the following: if $f : \Delta \to \mathbb{C}$ is holomorphic with a continuous extension to the boundary of $\Delta$ such that $|f(z)| = 1$ for all $|z| = 1$, then $f(z)$ is the restriction of a rational function.


::: solution
<1>1. A meromorphic function on the sphere is rational; in particular, part (a) holds.
::: proof
Assume first the hypothesis of part (a): $f$ is meromorphic on $\mathbb C$ and
has a pole at infinity. Then there is $R>0$ such that $f$ is holomorphic for
$|z|>R$. Hence every finite pole lies in the compact disk $|z|\le R$.
Poles are isolated, so there can be only finitely many of them, say
$a_1,\dots,a_m$.

For each $a_j$, let $P_j(1/(z-a_j))$ be the principal part of the Laurent
series of $f$ at $a_j$, and set
$$
g(z)=f(z)-\sum_{j=1}^m P_j\!\left(\frac1{z-a_j}\right).
$$
All finite principal parts have been removed, so $g$ is entire. Each subtracted
term tends to zero at infinity. Since $f$ has a pole at infinity, $g$ has at
worst a pole at infinity as well. Thus there are constants $C,N$ with
$|g(z)|\le C(1+|z|^N)$ for large $|z|$. Cauchy's coefficient estimates then
force every Taylor coefficient of $g$ above degree $N$ to vanish. Hence $g$ is
a polynomial. Therefore $f$ is a polynomial plus finitely many principal-part
rational functions, and is rational.

The same proof also covers the case where infinity is removable: then $g$ is
bounded near infinity, so Liouville's theorem makes it constant. Thus every
function meromorphic on the Riemann sphere is rational.
:::

<1>2. The boundary condition in part (b) produces a meromorphic function on the sphere.
::: proof
Let $f$ be as in part (b). Define for $|z|>1$
$$
F(z)=\frac{1}{\overline{f(1/\overline z)}}.
$$
The function
$$
f^*(w)=\overline{f(\overline w)}
$$
is holomorphic on the unit disk, so on $|z|>1$ the expression is
$F(z)=1/f^*(1/z)$ and is meromorphic there. Its poles correspond exactly to
zeros of $f^*$ in the disk.

On $|z|=1$, one has $1/\overline z=z$, and the boundary hypothesis gives
$$
\frac1{\overline{f(z)}}=f(z).
$$
Hence the inside definition $F=f$ and the outside reciprocal-reflection have
the same continuous boundary values on the unit circle.

It remains to justify holomorphic gluing at boundary points. On a sufficiently
small triangle crossing the unit circle but avoiding the finitely many outside
poles, split the triangle along the circle. Cauchy's theorem applies on each
side, and the integrals over the common circular arcs cancel because the two
continuous traces agree. Approximating the split pieces by curves a positive
distance from the circle and passing to the limit gives zero integral around
the original triangle. Morera's theorem therefore makes $F$ holomorphic across
the circle. Thus $F$ is meromorphic on $\mathbb C$.

At infinity, write $f(w)=w^k h(w)$ near zero, where $k\ge0$ and $h(0)\ne0$.
Then for large $z$,
$$
F(z)=\frac{z^k}{h^*(1/z)},
$$
so infinity is removable when $k=0$ and is a pole when $k>0$. Hence $F$ is
meromorphic on the Riemann sphere.
:::

<1>3. The reflected extension is rational, proving part (b).
::: proof
By step <1>1, the meromorphic sphere function $F$ from step <1>2 is rational.
On the unit disk its definition is exactly the original $f$. Therefore $f$ is
the restriction to $\Delta$ of a rational function, as required.
:::
:::
