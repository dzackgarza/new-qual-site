---
schema: qual/card@1
id: E-23ASH
kind: problem
title: Small functions in the nowhere-differentiability open sets
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §49 Exercise 2 was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. The exercise has to be read with the book's own set U_n,
    defined on printed p. 301: for n >= 2, f lies in U_n iff for some h with 0 < h <= 1/n one has Delta_h f > n,
    where Delta_h f is the infimum over x of the larger of the two step-h difference quotients. What was
    corrected: the card had stated U_n as a pointwise condition, with a step t allowed to depend on the point x
    and only on the bound |x - t| < 1/n, and had checked that condition for its sawtooth; the book's condition is
    that one single step h works uniformly at every point, and the card's own sawtooth does not satisfy the
    pointwise condition it had written either, since at a point where the height is eps/2 the step-h secant
    along the rising side can vanish. The solution now proves the book's condition: with mesh delta = 1/(2k) and
    step h = delta/2 = 1/(4k), at most one of the intervals [x-h,x] and [x,x+h] contains a vertex in its
    interior, so the other lies in a single linear piece of slope eps/delta, and choosing 2k eps > n and
    4k >= n gives Delta_h f > n with h <= 1/n, while 0 <= f <= eps.
---

::: {.exercise}

Given $n$ and $\epsilon$, define a continuous function $f: I \to \RR$ such that $f \in U_n$ and $\abs{f(x)} \leq \epsilon$ for all $x$.
:::

::: {.solution}
In §49 the set $U_n$, for $n\ge2$, is defined as follows. For $0<h\le 1/2$ and $x\in I$, let $\Delta f(x,h)$ be the larger, in absolute value, of the two difference quotients $(f(x+h)-f(x))/h$ and $(f(x-h)-f(x))/(-h)$ that are defined (at least one is, since $h\le1/2$), and let
$$
\Delta_h f=\inf\{\Delta f(x,h) \mid x\in I\}.
$$
Then $f\in U_n$ if and only if $\Delta_h f>n$ for some $h$ with $0<h\le 1/n$. So what must be produced is a single step $h\le1/n$ at which every point of $I$ has a secant slope exceeding $n$ in absolute value, not a step depending on the point.

Let $n\ge2$ and $\varepsilon>0$ be given, and choose an integer $k$ with
$$
2k\varepsilon>n \qquad\text{and}\qquad 4k\ge n ,
$$
which is possible. Put
$$
\delta=\frac{1}{2k},\qquad h=\frac{\delta}{2}=\frac{1}{4k}\le\frac1n ,
$$
and let $t_j=j\delta$ for $j=0,1,\dots,2k$, so that $t_0=0$ and $t_{2k}=1$. Define $f:I\to\RR$ to be the continuous piecewise linear function with
$$
f(t_j)=\begin{cases}\varepsilon,& j \text{ odd},\\ 0,& j\text{ even},\end{cases}
$$
and linear on each $[t_{j-1},t_j]$.

Plainly $0\le f(x)\le\varepsilon$ for all $x$: on each subinterval $f$ is linear between $0$ and $\varepsilon$.

We show $\Delta f(x,h)\ge\varepsilon/\delta=2k\varepsilon>n$ for every $x\in I$, which gives $\Delta_h f>n$ and $f\in U_n$.

Fix $x\in I$. The two intervals $[x-h,x]$ and $[x,x+h]$ have length $h=\delta/2$ each. If both had a vertex in the interior, say $t\in(x-h,x)$ and $t'\in(x,x+h)$, then $t<x<t'$ and $t'-t<2h=\delta$, which is impossible because distinct vertices are at distance at least $\delta$. So at least one of the two intervals has no vertex in its interior, hence lies inside one of the linear pieces, on which $f$ has slope $\pm\varepsilon/\delta$; the corresponding difference quotient therefore has absolute value exactly $\varepsilon/\delta$. Hence
$$
\Delta f(x,h)\ge\frac{\varepsilon}{\delta}=2k\varepsilon>n .
$$
Since $x$ was arbitrary, $\Delta_h f>n$ with $h=1/(4k)\le 1/n$, so $f\in U_n$.

Therefore $f\in U_n$ and $\abs{f(x)}\le\varepsilon$ for all $x\in I$.
:::
