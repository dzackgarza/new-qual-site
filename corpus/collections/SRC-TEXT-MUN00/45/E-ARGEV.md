---
schema: qual/card@1
id: E-ARGEV
kind: problem
title: Pointwise bounded collections that fail equicontinuity
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §45 Exercise 4 (printed p. 280) was located; the sets searched are listed in
    the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked against Munkres, Topology (2000), §45
    Exercise 4, printed p. 280, and Exercise 9 of §21, printed p. 134, whose functions are exactly
    1/(n^3[x - 1/n]^2 + 1). Part (a): equicontinuity at every x_0 < 1 is shown by splitting the indices at
    an N with a^N, x_0^N < eps/2 on [0,a], and handling the finitely many smaller indices by continuity;
    at x_0 = 1 the functions x^n and the constant 1 separate. Part (b): the card now also verifies the
    premise of the exercise for this family, which it had only assumed. The family is pointwise bounded
    by 1, no subsequence converges uniformly because the pointwise limit is 0 while sup of f_n is
    f_n(1/n) = 1, and the failure of equicontinuity is located at 0, with equicontinuity proved at every
    other point by an explicit bound on f_n off a neighbourhood of 0 and by continuity for the finitely
    many remaining indices. The earlier version's argument for x_0 < 1 in part (a) was a sketch (it spoke
    of "finitely many small n" being uniformly continuous without producing the neighbourhood); it is now
    the explicit estimate.
---

::: {.exercise}

(a) Let $f_n: I \to \RR$ be the function $f_n(x) = x^n$.
The collection $\mathcal{F} = \theset{f_n}$ is pointwise bounded but the sequence $(f_n)$ has no uniformly convergent subsequence; at what point or points does $\mathcal{F}$ fail to be equicontinuous?

(b) Repeat (a) for the functions $f_n$ of Exercise 9 of §21.
:::

::: {.solution}
For $f_n(x)=x^n$ on $I=[0,1]$: the family is equicontinuous at every $x_0<1$. Let $\varepsilon>0$ and choose $a$ with $x_0<a<1$. For $x\in[0,a]$ and $n\ge N$ with $a^N<\varepsilon/2$ and $x_0^N<\varepsilon/2$ we have
$$
\abs{x^n-x_0^n}\le x^n+x_0^n\le a^n+x_0^n<\varepsilon ,
$$
and for the finitely many $n<N$ continuity of $x\mapsto x^n$ at $x_0$ gives a neighbourhood on which $\abs{x^n-x_0^n}<\varepsilon$. The intersection of these finitely many neighbourhoods with $[0,a]$ is a neighbourhood of $x_0$ in $I$ that works for every $n$. At $x_0=1$ equicontinuity fails: for every neighbourhood of $1$ in $I$ there is $x<1$ in it, and then $x^n\to0$ while $f_n(1)=1$, so taking $n$ large gives $\abs{f_n(x)-f_n(1)}>1/2$.

For the sequence of [[E-BTI7W]], the functions of Exercise 9 of §21,
$$
f_n(x)=\frac1{n^3(x-1/n)^2+1},
$$
the collection is pointwise bounded, since $0<f_n(x)\le1$, and no subsequence converges uniformly: $f_n\to0$ pointwise, so a uniform limit would be $0$, while $f_n(1/n)=1$ gives $\sup_x\abs{f_n(x)}=1$ for every $n$.

The family fails equicontinuity exactly at $0$. At $0$: $f_n(0)=1/(n+1)\to0$ while $f_n(1/n)=1$ and $1/n\to0$, so for $\varepsilon=1/2$ no neighbourhood of $0$ works. At $x_0\ne0$: choose $r>0$ with $\abs{x}\ge c>0$ for all $x$ in $J=[x_0-r,x_0+r]$. For $n\ge 2/c$ and $x\in J$ we have $\abs{x-1/n}\ge c/2$, so
$$
0<f_n(x)\le\frac{1}{n^3c^2/4+1}\longrightarrow0
$$
uniformly on $J$; hence for $n\ge N$ both $f_n(x)$ and $f_n(x_0)$ are less than $\varepsilon/2$, and for the finitely many $n<N$ continuity at $x_0$ gives a smaller neighbourhood on which $\abs{f_n(x)-f_n(x_0)}<\varepsilon$. So the family is equicontinuous at every $x_0\ne0$.
:::
