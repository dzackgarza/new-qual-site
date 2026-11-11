---
schema: qual/card@1
id: E-YSJOS
kind: problem
title: Secant-quotient bounds for the building blocks of a nowhere-differentiable function
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §49 Exercise 1 (printed p. 304) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against Example 1 of §49, printed
    p. 301, and the definition of Delta f(x,h) and of U_n on the same page. The three computations were
    verified: for f(x) = 4 alpha x(1-x) with h = 1/4 the two one-sided quotients are alpha(3 - 8x) and
    alpha(5 - 8x), whose difference is 2 alpha, so the larger is at least alpha in absolute value, and at an
    endpoint the single defined quotient has absolute value at least alpha; for the tent g and for the two-tooth
    sawtooth k every linear piece has slope of absolute value alpha, and an interval of length at most half the
    vertex spacing lies in a single piece. What was corrected: the card had restricted the conclusions to
    n >= 4 for g and n >= 8 for k, because it took h = 1/n and needed h <= 1/4 and h <= 1/8; the book asserts
    both for every n with alpha > n, and the card now takes h = min{1/n, 1/4} and h = min{1/n, 1/8}. The
    argument that one of the two intervals has no vertex in its interior is now given, in place of the bare
    statement that the vertices are spaced further apart than the step.
---

::: {.exercise}

Check the stated properties of the functions $f$, $g$, and $k$ of Example 1 of §49.
:::

::: {.solution}
Write $I=[0,1]$.  For $0<h\le 1/2$, let $\Delta f(x,h)$ be the larger, in absolute value, of the two secant quotients of step $h$ that are defined at $x$.

For
$$
f(x)=4\alpha x(1-x)
$$
and $h=1/4$, the forward quotient is
$$
\frac{f(x+h)-f(x)}h=4\alpha(1-2x-h)
=\alpha(3-8x),
$$
while the backward quotient is
$$
\frac{f(x-h)-f(x)}{-h}=4\alpha(1-2x+h)
=\alpha(5-8x).
$$
Whenever both are defined, their difference is $2\alpha$, so at least one has absolute value at least $\alpha$.  Near an endpoint only one quotient may be defined; if $0\le x<1/4$, then $\abs{3-8x}\ge1$, and if $3/4<x\le1$, then $\abs{5-8x}\ge1$.  Hence
$$
\Delta f(x,1/4)\ge\alpha\qquad(x\in I).
$$
In particular, if $\alpha>4$, then $f\in U_4$.

The function $g$ in Figure 49.1 is the tent function
$$
g(x)=
\begin{cases}
\alpha x,&0\le x\le1/2,\\
\alpha(1-x),&1/2\le x\le1.
\end{cases}
$$
Every linear piece has slope of absolute value $\alpha$.  Fix $0<h\le1/4$ and $x\in I$.  If $x\le1/2$, then either $x+h\le1/2$, so the forward quotient has absolute value $\alpha$, or else $x\ge1/2-h$, in which case $x-h\ge0$ and the backward interval $[x-h,x]$ lies in the left linear piece, so the backward quotient has absolute value $\alpha$.  The case $x\ge1/2$ is symmetric.  Therefore
$$
\Delta g(x,h)\ge\alpha
$$
for every $x$ and every $0<h\le1/4$.  So for $\alpha>n$ and any $n$, the step $h=\min\{1/n,1/4\}$ satisfies $h\le1/n$ and $h\le1/4$, hence $\Delta_h g\ge\alpha>n$ and $g\in U_n$.

The function $k$ is the two-tooth sawtooth obtained by joining successively
$$
(0,0),\quad (1/4,\alpha/4),\quad(1/2,0),\quad
(3/4,\alpha/4),\quad(1,0).
$$
Again every linear piece has slope $\pm\alpha$.  Let $0<h\le1/8$ and $x\in I$. If both intervals $[x-h,x]$ and $[x,x+h]$ had a vertex in the interior, say $t<x<t'$, then $t'-t<2h\le1/4$, which is impossible because distinct vertices are at distance exactly $1/4$. So one of the two intervals has no vertex in its interior and is therefore contained in one of the four linear pieces.  Along that interval the corresponding secant quotient has absolute value $\alpha$.  Hence
$$
\Delta k(x,h)\ge\alpha
\qquad(0<h\le1/8).
$$
Consequently, for $\alpha>n$ and any $n$, the step $h=\min\{1/n,1/8\}$ gives $\Delta_h k\ge\alpha>n$, so $k\in U_n$.

These are exactly the properties asserted for $f,g,k$ in Example 1.
:::
