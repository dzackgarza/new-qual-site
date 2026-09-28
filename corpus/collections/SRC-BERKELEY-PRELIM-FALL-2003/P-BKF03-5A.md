---
schema: qual/card@1
id: P-BKF03-5A
kind: problem
title: The metric $\int_0^1 \lvert f-g\rvert/(1+\lvert f-g\rvert)\,dx$ on $C[0,1]$ is not complete
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
  note: Checked against Problem 5A of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the pointwise triangle inequality for t/(1+t) and the Cauchy sequence converging only to 1/x away from zero.
---

::: {.problem}
Let C denote the space of continuous functions on [0, 1]. Define

$$
d ( f , g ) = \int _ { 0 } ^ { 1 } { \frac { | f ( x ) - g ( x ) | } { 1 + | f ( x ) - g ( x ) | } } d x .
$$

(a) Show that d is a metric on $C .$

(b) Show that $( C , d )$ is not a complete metric space.
:::


::: {.solution}
Define
\[
\phi(t):=\frac{t}{1+t}\qquad(t\ge0).
\]
Then
\[
d(f,g)=\int_0^1\phi(|f(x)-g(x)|)\,dx.
\]

<1>1. The function $d$ is nonnegative, symmetric, and satisfies $d(f,g)=0$ if and only if $f=g$.
::: {.proof}
Nonnegativity and symmetry are immediate from the definition.
If $f=g$, then $d(f,g)=0$.
Conversely, suppose $d(f,g)=0$.
The integrand
\[
x\longmapsto \phi(|f(x)-g(x)|)
\]
is continuous and nonnegative.
If $f(x_0)\ne g(x_0)$ at some point $x_0$, then the integrand is positive at $x_0$ and hence, by continuity, is bounded below by a positive constant on some interval of positive length.
Its integral would then be positive, a contradiction.
Thus $f=g$.
:::

<1>2. The function $d$ satisfies the triangle inequality.
::: {.proof}
The function $\phi$ is increasing on $[0,\infty)$.
For nonnegative $a,b$,
\[
\phi(a+b)=\frac{a+b}{1+a+b}
=\frac{a}{1+a+b}+\frac{b}{1+a+b}
\le\frac{a}{1+a}+\frac{b}{1+b}
=\phi(a)+\phi(b).
\]
For $f,g,h\in C[0,1]$, set pointwise
\[
a=|f-g|,\qquad b=|g-h|,\qquad c=|f-h|.
\]
Since $c\le a+b$, monotonicity and the preceding inequality give
\[
\phi(c)\le\phi(a+b)\le\phi(a)+\phi(b).
\]
Integrating over $[0,1]$ yields
\[
d(f,h)\le d(f,g)+d(g,h).
\]
Thus $d$ is a metric.
:::

<1>3. Define, for $n\ge1$,
\[
f_n(x)=\begin{cases}
n^2x,&0\le x\le1/n,\\[2mm]
1/x,&1/n\le x\le1.
\end{cases}
\]
Then $f_n\in C[0,1]$ and $(f_n)$ is $d$-Cauchy.
::: {.proof}
At $x=1/n$, the two formulas agree because $n^2(1/n)=n=1/(1/n)$, so $f_n$ is continuous.

If $x\ge\max\{1/m,1/n\}$, then $f_m(x)=f_n(x)=1/x$.
Hence the integrand defining $d(f_m,f_n)$ vanishes outside
\[
[0,\max\{1/m,1/n\}].
\]
Since $0\le\phi(t)<1$,
\[
d(f_m,f_n)\le\max\{1/m,1/n\}\longrightarrow0
\]
as $m,n\to\infty$.
Thus $(f_n)$ is Cauchy.
:::

<1>4. The sequence $(f_n)$ does not converge in $(C[0,1],d)$.
::: {.proof}
Suppose $d(f_n,f)\to0$ for some $f\in C[0,1]$.
Fix $a\in(0,1]$.
We claim that $f(a)=1/a$.

If not, then the continuous function
\[
x\longmapsto f(x)-1/x
\]
is nonzero at $a$.
Hence there exist an interval $J\subset(0,1]$ containing $a$ and a constant $\varepsilon>0$ such that
\[
|f(x)-1/x|\ge\varepsilon
\qquad(x\in J).
\]
For all sufficiently large $n$, one has $1/n<\inf J$, so $f_n(x)=1/x$ throughout $J$.
Therefore
\[
d(f_n,f)\ge\int_J\frac{\varepsilon}{1+\varepsilon}\,dx
=|J|\frac{\varepsilon}{1+\varepsilon}>0,
\]
contradicting $d(f_n,f)\to0$.
Thus $f(a)=1/a$ for every $a\in(0,1]$.

But no continuous function on $[0,1]$ can agree with $1/x$ on $(0,1]$, since $1/x\to\infty$ as $x\downarrow0$.
This contradiction proves that $(f_n)$ has no limit in $C[0,1]$.
:::

Hence $(C[0,1],d)$ is not complete.
:::

