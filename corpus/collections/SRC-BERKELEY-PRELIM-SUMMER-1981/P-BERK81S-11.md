---
schema: qual/card@1
id: P-BERK81S-11
kind: problem
title: Two positive solutions and the small branch of an implicit logarithmic equation
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Wrote L=log(1/epsilon) and F_epsilon(x)=
    x(1+L-(1/2)log x). Its derivative has one zero at
    x_*=e epsilon^{-2}; F_epsilon increases from 0 to the maximum
    e/(2 epsilon^2) and then decreases to -infinity, giving exactly two
    roots for small epsilon. Fixed test points show the smaller root tends
    to zero, while F_epsilon(M epsilon^s) tends to zero for every s,M>0,
    forcing x(epsilon)>M epsilon^s eventually.
---

::: {.problem}
Show that, for every sufficiently small $\varepsilon>0$, the equation
\[
x\left(1+\log\frac1{\varepsilon\sqrt{x}}\right)=1,
\qquad x>0,
\]
has exactly two solutions.
Let $x(\varepsilon)$ be the smaller solution.
Show that
\[
x(\varepsilon)\to0
\qquad(\varepsilon\to0^+),
\]
but for every $s>0$,
\[
\varepsilon^{-s}x(\varepsilon)\to\infty
\qquad(\varepsilon\to0^+).
\]
:::

::: {.solution}
For
$$
0<\varepsilon<1,
$$
set
$$
L=\log\frac1\varepsilon>0
$$
and define
$$
F_\varepsilon(x)
=
x
\left(
1+L-\frac12\log x
\right),
\qquad
x>0.
$$
The equation in the problem is
$$
F_\varepsilon(x)=1.
$$

<1>1. One has
$$
\lim_{x\to0^+}F_\varepsilon(x)=0.
$$

::: {.proof}
Write
$$
F_\varepsilon(x)
=
(1+L)x-\frac12x\log x.
$$
The first term tends to zero, and the standard limit
$$
x\log x\longrightarrow0
\qquad
(x\to0^+)
$$
gives the same for the second term.
:::

<1>2. One has
$$
\lim_{x\to\infty}F_\varepsilon(x)=-\infty.
$$

::: {.proof}
Factor out $x$:
$$
F_\varepsilon(x)
=
x
\left(
1+L-\frac12\log x
\right).
$$
The factor in parentheses tends to $-\infty$ as $x\to\infty$, and is
eventually negative. Multiplication by the positive quantity $x\to\infty$
therefore sends the product to $-\infty$.
:::

<1>3. The derivative is
$$
F_\varepsilon'(x)
=
L+\frac12-\frac12\log x.
$$

::: {.proof}
Differentiate
$$
x
\left(
1+L-\frac12\log x
\right):
$$
\begin{aligned}
F_\varepsilon'(x)
&=
1+L-\frac12\log x-\frac12\\
&=
L+\frac12-\frac12\log x.
\end{aligned}
$$
:::

<1>4. The derivative vanishes at exactly one point,
$$
\boxed{
x_*
=
e^{2L+1}
=
e\varepsilon^{-2}.
}
$$

::: {.proof}
By step <1>3,
$$
F_\varepsilon'(x)=0
$$
if and only if
$$
\log x=2L+1.
$$
Exponentiating gives
$$
x=e^{2L+1}.
$$
Since
$$
e^L=\varepsilon^{-1},
$$
this equals $e\varepsilon^{-2}$.
:::

<1>5. The function $F_\varepsilon$ is strictly increasing on
$$
(0,x_*)
$$
and strictly decreasing on
$$
(x_*,\infty).
$$

::: {.proof}
The expression in step <1>3 is positive exactly when
$$
\log x<2L+1,
$$
equivalently $x<x_*$, and negative exactly when $x>x_*$.
:::

<1>6. The maximum value of $F_\varepsilon$ is
$$
\boxed{
F_\varepsilon(x_*)
=
\frac{e}{2\varepsilon^2}.
}
$$

::: {.proof}
By step <1>4,
$$
\log x_*=2L+1.
$$
Hence
$$
\begin{aligned}
F_\varepsilon(x_*)
&=
x_*
\left(
1+L-\frac12(2L+1)
\right)\\
&=
\frac{x_*}{2}\\
&=
\frac{e}{2\varepsilon^2}.
\end{aligned}
$$
:::

<1>7. For every sufficiently small $\varepsilon>0$, the equation
$$
F_\varepsilon(x)=1
$$
has exactly two positive solutions.

::: {.proof}
Choose $\varepsilon$ so small that
$$
\frac{e}{2\varepsilon^2}>1.
$$
By steps <1>1, <1>5, and <1>6, the function increases strictly from the
limiting value $0$ at the left endpoint to a value greater than $1$ at
$x_*$. The intermediate value theorem and strict monotonicity therefore
give exactly one solution in $(0,x_*)$.

By steps <1>2, <1>5, and <1>6, the function then decreases strictly from a
value greater than $1$ at $x_*$ to $-\infty$. Hence there is exactly one
solution in $(x_*,\infty)$. These are the only positive solutions.
:::

<1>8. Let $x(\varepsilon)$ denote the smaller solution. For every fixed
$\delta>0$,
$$
F_\varepsilon(\delta)\longrightarrow\infty
\qquad
(\varepsilon\to0^+).
$$

::: {.proof}
For fixed $\delta>0$,
$$
F_\varepsilon(\delta)
=
\delta
\left(
1+\log\frac1\varepsilon
-\frac12\log\delta
\right).
$$
The only term depending unboundedly on $\varepsilon$ is
$$
\delta\log\frac1\varepsilon,
$$
which tends to $+\infty$.
:::

<1>9. The smaller solution satisfies
$$
\boxed{
x(\varepsilon)\longrightarrow0
}
$$
as $\varepsilon\to0^+$.

::: {.proof}
Fix $\delta>0$. Since
$$
x_*=e\varepsilon^{-2}\longrightarrow\infty,
$$
one has $\delta<x_*$ for all sufficiently small $\varepsilon$. By step
<1>8, also
$$
F_\varepsilon(\delta)>1
$$
for all sufficiently small $\varepsilon$.

On $(0,x_*)$, the function is strictly increasing by step <1>5, and the
smaller root is the unique point there at which
$$
F_\varepsilon(x)=1.
$$
Thus
$$
0<x(\varepsilon)<\delta
$$
for all sufficiently small $\varepsilon$. Since $\delta>0$ was arbitrary,
the claimed limit follows.
:::

<1>10. Fix
$$
s>0
\qquad\text{and}\qquad
M>0.
$$
Then
$$
F_\varepsilon(M\varepsilon^s)
\longrightarrow0
\qquad
(\varepsilon\to0^+).
$$

::: {.proof}
Since
$$
\log(M\varepsilon^s)
=
\log M-sL,
$$
one has
$$
\begin{aligned}
F_\varepsilon(M\varepsilon^s)
&=
M\varepsilon^s
\left(
1+L-\frac12\log M+\frac{s}{2}L
\right)\\
&=
M\varepsilon^s
\left(
1-\frac12\log M
+
\left(
1+\frac{s}{2}
\right)L
\right).
\end{aligned}
$$
The standard limit
$$
\varepsilon^s\log\frac1\varepsilon\longrightarrow0
$$
shows that the right-hand side tends to zero.
:::

<1>11. For every fixed $s>0$ and $M>0$, one has
$$
x(\varepsilon)>M\varepsilon^s
$$
for all sufficiently small $\varepsilon>0$.

::: {.proof}
By step <1>10,
$$
F_\varepsilon(M\varepsilon^s)<1
$$
for all sufficiently small $\varepsilon$.
Also
$$
M\varepsilon^s<x_*=e\varepsilon^{-2}
$$
for all sufficiently small $\varepsilon$. Thus both
$M\varepsilon^s$ and the smaller solution lie on the strictly increasing
branch from step <1>5. Since
$$
F_\varepsilon(M\varepsilon^s)<1
=
F_\varepsilon(x(\varepsilon)),
$$
strict monotonicity gives
$$
M\varepsilon^s<x(\varepsilon).
$$
:::

<1>12. For every $s>0$,
$$
\boxed{
\varepsilon^{-s}x(\varepsilon)
\longrightarrow
\infty
}
$$
as $\varepsilon\to0^+$.

::: {.proof}
Fix $s>0$. Step <1>11 says that for every $M>0$,
$$
\frac{x(\varepsilon)}{\varepsilon^s}>M
$$
for all sufficiently small $\varepsilon$. This is exactly divergence of
the ratio to $+\infty$.
:::

<1>13. Q.E.D.

::: {.proof}
Step <1>7 proves the two-solution assertion, step <1>9 proves the first
limit, and step <1>12 proves the second limit.
:::
:::
