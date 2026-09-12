---
schema: qual/card@1
id: E-YSJOS
kind: problem
title: Verifying the building blocks of the nowhere-differentiable function
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
---

::: {.exercise}

Check the stated properties of the functions $f$, $g$, and $k$ of Example 1 of §49.
:::

::: {.solution}
Write \(I=[0,1]\).  For \(0<h\le 1/2\), Munkres defines \(\Delta f(x,h)\) to be the larger, in absolute value, of the two secant quotients of step \(h\) that are defined at \(x\).

For
\[
f(x)=4\alpha x(1-x)
\]
and \(h=1/4\), the forward quotient is
\[
\frac{f(x+h)-f(x)}h=4\alpha(1-2x-h)
=\alpha(3-8x),
\]
while the backward quotient is
\[
\frac{f(x-h)-f(x)}{-h}=4\alpha(1-2x+h)
=\alpha(5-8x).
\]
Whenever both are defined, their difference is \(2\alpha\), so at least one has absolute value at least \(\alpha\).  Near an endpoint only one quotient may be defined; if \(0\le x<1/4\), then \(|3-8x|\ge1\), and if \(3/4<x\le1\), then \(|5-8x|\ge1\).  Hence
\[
\Delta f(x,1/4)\ge\alpha\qquad(x\in I).
\]
In particular, if \(\alpha>4\), then \(f\in U_4\).

The function \(g\) in Figure 49.1 is the tent function
\[
g(x)=
\begin{cases}
\alpha x,&0\le x\le1/2,\\
\alpha(1-x),&1/2\le x\le1.
\end{cases}
\]
Every linear piece has slope of absolute value \(\alpha\).  Fix \(0<h\le1/4\) and \(x\in I\).  If \(x\le1/2\), then either \(x+h\le1/2\), so the forward quotient has absolute value \(\alpha\), or else \(x\ge1/2-h\), in which case \(x-h\ge0\) and the backward interval \([x-h,x]\) lies in the left linear piece, so the backward quotient has absolute value \(\alpha\).  The case \(x\ge1/2\) is symmetric.  Therefore
\[
\Delta g(x,h)\ge\alpha
\]
for every \(x\) and every \(0<h\le1/4\).  Thus, if \(\alpha>n\) and \(1/n\le1/4\), choosing any \(0<h\le1/n\) gives \(g\in U_n\).

The function \(k\) is the two-tooth sawtooth obtained by joining successively
\[
(0,0),\quad (1/4,\alpha/4),\quad(1/2,0),\quad
(3/4,\alpha/4),\quad(1,0).
\]
Again every linear piece has slope \(\pm\alpha\).  If \(0<h\le1/8\), then for every \(x\in I\), at least one of the two intervals \([x-h,x]\) or \([x,x+h]\) that is defined is contained in one of the four linear pieces: the vertices are spaced by \(1/4\), while \(h\le1/8\).  Along that interval the corresponding secant quotient has absolute value \(\alpha\).  Hence
\[
\Delta k(x,h)\ge\alpha
\qquad(0<h\le1/8).
\]
Consequently \(k\in U_n\) whenever \(\alpha>n\) and \(n\ge8\) (take, for example, \(h=1/n\)).

These are exactly the properties asserted for \(f,g,k\) in Example 1.
:::
