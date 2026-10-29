---
schema: qual/card@1
id: P-UCLAB13F-02
kind: problem
title: Discontinuity sets of monotone functions
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Fall 2013.
---

::: {.problem}
Let $f:\RR\to\RR$ be nondecreasing.

(a) Prove that the set of points where $f$ is discontinuous is countable.

(b) Let $S\subset\RR$ be countable. Prove that there exists a nondecreasing function $f:\RR\to\RR$ whose set of discontinuities is exactly $S$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $x\in\RR$, the one-sided limits
\[
f(x^-)=\sup_{t<x}f(t)
\qquad\text{and}\qquad
f(x^+)=\inf_{t>x}f(t)
\]
exist in $\RR\cup\{\pm\infty\}$, and
\[
f(x^-)\le f(x)\le f(x^+).
\]


::: pf-proof

Because $f$ is nondecreasing, the set
\[
\{f(t):t<x\}
\]
is bounded above by $f(x)$, so its supremum exists in $\RR$.
Similarly,
\[
\{f(t):t>x\}
\]
is bounded below by $f(x)$, so its infimum exists in $\RR$.
Monotonicity gives the displayed inequalities.

:::

:::

::: {.pf-step #s1-2}

The function $f$ is continuous at $x$ if and only if
\[
f(x^-)=f(x)=f(x^+).
\]


::: pf-proof

If $f$ is continuous at $x$, both one-sided limits equal $f(x)$.

Conversely, suppose the three values agree.
Given $\varepsilon>0$, by the definition of the left supremum choose $a<x$ such that
\[
f(x)-\varepsilon<f(a)\le f(x),
\]
and by the definition of the right infimum choose $b>x$ such that
\[
f(x)\le f(b)<f(x)+\varepsilon.
\]
For every $t\in(a,b)$, monotonicity gives
\[
f(a)\le f(t)\le f(b),
\]
so
\[
|f(t)-f(x)|<\varepsilon.
\]
Thus $f$ is continuous at $x$.

:::

:::

::: {.pf-step #s1-3}

If $f$ is discontinuous at $x$, then
\[
f(x^-)<f(x^+).
\]


::: pf-proof

By step [](#s1-1){.pf-ref},
\[
f(x^-)\le f(x)\le f(x^+).
\]
If the endpoints were equal, then all three quantities would be equal, and step [](#s1-2){.pf-ref} would imply continuity. Hence discontinuity forces strict inequality.

:::

:::

::: {.pf-step #s1-4}

If $x<y$, then the open intervals
\[
\bigl(f(x^-),f(x^+)\bigr)
\qquad\text{and}\qquad
\bigl(f(y^-),f(y^+)\bigr)
\]
are disjoint.


::: pf-proof

For $x<y$, monotonicity gives
\[
f(x^+)\le f(y^-).
\]
Indeed, if $x<t<y$, then
\[
f(x^+)\le f(t)\le f(y^-)
\]
after taking the relevant infimum and supremum.
Thus the first open interval lies entirely to the left of the second.

:::

:::

::: {.pf-step #s1-5}

The set of discontinuities of $f$ is countable.


::: pf-proof

For every discontinuity point $x$, step [](#s1-3){.pf-ref} gives a nonempty open interval
\[
I_x=(f(x^-),f(x^+)).
\]
Choose a rational number
\[
q_x\in I_x.
\]
By step [](#s1-4){.pf-ref}, the intervals $I_x$ for distinct discontinuity points are disjoint, so the chosen rationals $q_x$ are distinct.
Thus the map
\[
x\longmapsto q_x
\]
injects the discontinuity set into $\QQ$.
Since $\QQ$ is countable, so is the discontinuity set.

:::

:::

::: {.pf-step #s1-6}

For part (b), enumerate the countable set $S$ without repetition as
\[
S=\{s_1,s_2,\ldots\},
\]
with the finite case handled by stopping the list.
Define
\[
f(x)=\sum_{n=1}^{\infty}2^{-n}\mathbf 1_{[s_n,\infty)}(x).
\]


::: pf-proof

For every $x$,
\[
0\le
2^{-n}\mathbf 1_{[s_n,\infty)}(x)
\le
2^{-n}.
\]
Since
\[
\sum_{n=1}^{\infty}2^{-n}<\infty,
\]
the series defining $f(x)$ converges absolutely and uniformly by the Weierstrass $M$-test.

:::

:::

::: {.pf-step #s1-7}

The function $f$ from step [](#s1-6){.pf-ref} is nondecreasing.


::: pf-proof

Each step function
\[
x\longmapsto \mathbf 1_{[s_n,\infty)}(x)
\]
is nondecreasing.
All coefficients $2^{-n}$ are positive.
Therefore for $x\le y$, every summand at $x$ is at most the corresponding summand at $y$, and summing gives
\[
f(x)\le f(y).
\]

:::

:::

::: {.pf-step #s1-8}

The function $f$ is discontinuous at every point $s_k\in S$.


::: pf-proof

The $k$th summand
\[
2^{-k}\mathbf 1_{[s_k,\infty)}
\]
has a jump of size $2^{-k}$ at $s_k$, while every other summand is nondecreasing and therefore cannot cancel that upward jump.
More explicitly,
\[
f(s_k)-\sup_{x<s_k}f(x)\ge2^{-k}>0.
\]
Hence $f$ is discontinuous at $s_k$.

:::

:::

::: {.pf-step #s1-9}

The function $f$ is continuous at every
\[
x\notin S.
\]


::: pf-proof

Fix $x\notin S$ and $\varepsilon>0$.
Choose $N$ so large that
\[
\sum_{n>N}2^{-n}<\frac{\varepsilon}{2}.
\]
The finite set
\[
\{s_1,\ldots,s_N\}
\]
does not contain $x$, so there exists $\delta>0$ such that the interval
\[
(x-\delta,x+\delta)
\]
contains none of these finitely many points.

Thus for $|y-x|<\delta$, the first $N$ step functions have the same value at $x$ and $y$.
Hence
\[
\begin{aligned}
|f(y)-f(x)|
&\le
\sum_{n>N}
2^{-n}
\left|
\mathbf1_{[s_n,\infty)}(y)
-
\mathbf1_{[s_n,\infty)}(x)
\right|\\
&\le
\sum_{n>N}2^{-n}\\
&<
\frac{\varepsilon}{2}
<
\varepsilon.
\end{aligned}
\]
Thus $f$ is continuous at $x$.

:::

:::

::: {.pf-step #s1-10}

The discontinuity set of $f$ is exactly $S$.


::: pf-proof

Step [](#s1-8){.pf-ref} shows every point of $S$ is a discontinuity, while step [](#s1-9){.pf-ref} shows every point outside $S$ is a continuity point.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves part (a), and steps [](#s1-6){.pf-ref} through [](#s1-10){.pf-ref} prove part (b).

:::

:::

:::
