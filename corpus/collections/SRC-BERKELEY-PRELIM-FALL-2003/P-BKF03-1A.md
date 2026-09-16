---
schema: qual/card@1
id: P-BKF03-1A
kind: problem
title: Unique entire solution of $f''=zf$ with $f(0)=f'(0)=1$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 1A of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the coefficient recurrence, global convergence of both nonzero mod-3 subseries, and uniqueness from the Taylor coefficients.
---

::: {.problem}
Show that the differential equation

$$
f ^ { \prime \prime } ( z ) = z f ( z ) , \qquad f ( 0 ) = 1 , \qquad f ^ { \prime } ( 0 ) = 1
$$

has an unique entire solution in the complex plane.
:::

::: {.solution}
Seek a power-series solution
\[
f(z)=\sum_{n=0}^{\infty}a_nz^n.
\]

<1>1. Any analytic solution must satisfy
\[
a_0=1,\qquad a_1=1,\qquad a_2=0,
\]
and, for every $k\ge3$,
\[
a_k=\frac{a_{k-3}}{k(k-1)}.
\]
::: {.proof}
The initial conditions give $a_0=f(0)=1$ and $a_1=f'(0)=1$.
Also
\[
f''(z)=\sum_{n=0}^{\infty}(n+2)(n+1)a_{n+2}z^n,
\]
whereas
\[
zf(z)=\sum_{n=1}^{\infty}a_{n-1}z^n.
\]
Comparing the constant terms in $f''=zf$ gives $2a_2=0$, hence $a_2=0$.
Comparing coefficients of $z^n$ for $n\ge1$ gives
\[
(n+2)(n+1)a_{n+2}=a_{n-1}.
\]
Writing $k=n+2$ yields the recurrence.
:::

<1>2. The recurrence defines a power series with infinite radius of convergence.
::: {.proof}
It gives
\[
a_{3m}=\prod_{j=1}^{m}\frac1{3j(3j-1)},
\qquad
a_{3m+1}=\prod_{j=1}^{m}\frac1{3j(3j+1)},
\qquad
a_{3m+2}=0.
\]
For fixed $z\in\mathbb C$, the ratio of successive terms in the first nonzero subseries is
\[
\frac{|a_{3m+3}z^{3m+3}|}{|a_{3m}z^{3m}|}
=\frac{|z|^3}{(3m+3)(3m+2)}\longrightarrow0.
\]
For the second nonzero subseries,
\[
\frac{|a_{3m+4}z^{3m+4}|}{|a_{3m+1}z^{3m+1}|}
=\frac{|z|^3}{(3m+4)(3m+3)}\longrightarrow0.
\]
Thus both subseries converge absolutely for every $z$, and the third subseries is zero.
Hence the full series has infinite radius of convergence and defines an entire function.
:::

<1>3. The entire function defined in <1>2 solves the differential equation and initial conditions.
::: {.proof}
Because its radius of convergence is infinite, the series may be differentiated termwise twice on all of $\mathbb C$.
The coefficient identities from <1>1 then give $f''(z)=zf(z)$ coefficient by coefficient.
The values $a_0=a_1=1$ give $f(0)=f'(0)=1$.
:::

<1>4. The entire solution is unique.
::: {.proof}
Let $g$ be any entire solution, with Taylor expansion $g(z)=\sum b_nz^n$ at $0$.
Repeating the coefficient comparison in <1>1 forces
\[
b_0=1,\qquad b_1=1,\qquad b_2=0,\qquad b_k=\frac{b_{k-3}}{k(k-1)}\quad(k\ge3).
\]
Thus $b_n=a_n$ for every $n$ by induction.
Therefore $g=f$ on $\mathbb C$.
:::
:::
