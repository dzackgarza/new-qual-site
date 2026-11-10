---
schema: qual/card@1
id: E-9V5EM
kind: problem
title: Powers converge pointwise but not uniformly on $[0,1]$
classification:
  areas:
  - topology
  topics:
  - Uniform Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §21 Exercise 6, printed p. 134, with the
    definitions of pointwise and uniform convergence and Theorem 21.6; the stored statement
    is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 21.6, PDF p. 25. The pointwise limit is 0 off 1
    and 1 at 1, and the convergence is not uniform: at x = epsilon^{1/N} the N-th function
    is epsilon away from the limit. One misprint in the published answer is corrected: its
    limit function names 0 only at 0 instead of on [0,1). (tmp/sources/munkres-solutions-
    positron-ch2.pdf).
---

::: {.exercise}

Define $f_n: [0,1] \to \RR$ by the equation $f_n(x) = x^n$.
Show that the sequence $(f_n(x))$ converges for each $x \in [0,1]$, but that the sequence $(f_n)$ does not converge uniformly.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.6, PDF p. 25** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both halves are theirs, with the limit function printed there corrected: it is $f(x)=0$ for $0\le x<1$ and $f(1)=1$.

Let $f_{n}(x)=x^{n}$ on $[0,1]$.

*Pointwise convergence.* $f_{n}(0)=0$ for all $n$, and if $0<x<1$ then $x^{n}\to0$; $f_{n}(1)=1$ for all $n$. So $(f_{n}(x))$ converges for each $x$, with limit
$$
f(x)=\begin{cases}0,&0\le x<1,\\ 1,&x=1.\end{cases}
$$

*The convergence is not uniform.* Let $0<\varepsilon<1$ and $N\in\ZZ_{+}$; with $x=\varepsilon^{1/N}\in(0,1)$ we have
$$
\abs{f_{N}(x)-f(x)}=\abs{x^{N}-0}=\varepsilon,
$$
so for every $N$ there is a point at distance $\ge\varepsilon$ from the limit, and the convergence is not uniform. Equivalently, by Theorem 21.6 (printed p. 132) a uniformly convergent sequence of continuous functions has continuous limit, and $f$ is discontinuous at $1$.
:::
