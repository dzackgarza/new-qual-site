---
schema: qual/card@1
id: P-BKS12-1B
kind: problem
title: Fourier series of an indicator function and the sum $\sum\sin n/n$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with pages 3--4 of the retained Spring 2012 solution PDF and independently reviewed the Fourier-coefficient computation.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the real Fourier series, Dirichlet convergence at x=0, and the evaluation of sum sin(n)/n.
---

::: {.problem}
Find the Fourier series of the function with period 2π that is 1 if $| x | < \epsilon$ and 0 if $\epsilon \le | x | < \pi$ Find the sum

$$
{ \frac { \sin 1 } { 1 } } + { \frac { \sin 2 } { 2 } } + { \frac { \sin 3 } { 3 } } + \cdots
$$
:::

::: {.solution}
Let $F_\varepsilon$ denote the stated $2\pi$-periodic function. First
consider the nontrivial case
$$
0<\varepsilon<\pi.
$$

<1>1. The function $F_\varepsilon$ is even, so all sine Fourier
coefficients vanish.

::: {.proof}
On the fundamental interval $(-\pi,\pi)$, the value of
$F_\varepsilon(x)$ depends only on $\abs{x}$. Thus
$$
F_\varepsilon(-x)=F_\varepsilon(x).
$$
Since $\sin(nx)$ is odd, the product
$$
F_\varepsilon(x)\sin(nx)
$$
is odd, so its integral over $[-\pi,\pi]$ is zero.
:::

<1>2. The constant Fourier coefficient satisfies
$$
\frac{a_0}{2}
=
\frac{\varepsilon}{\pi}.
$$

::: {.proof}
By definition,
$$
a_0
=
\frac1\pi
\int_{-\pi}^{\pi}F_\varepsilon(x)\,dx
=
\frac1\pi
\int_{-\varepsilon}^{\varepsilon}1\,dx
=
\frac{2\varepsilon}{\pi}.
$$
:::

<1>3. For every integer $n\geq1$,
$$
a_n
=
\frac{2\sin(n\varepsilon)}{\pi n}.
$$

::: {.proof}
Using evenness,
$$
\begin{aligned}
a_n
&=
\frac1\pi
\int_{-\pi}^{\pi}
F_\varepsilon(x)\cos(nx)\,dx\\
&=
\frac2\pi
\int_0^\varepsilon\cos(nx)\,dx\\
&=
\frac{2\sin(n\varepsilon)}{\pi n}.
\end{aligned}
$$
:::

<1>4. For $0<\varepsilon<\pi$, the Fourier series is
$$
\boxed{
\frac{\varepsilon}{\pi}
+
\frac2\pi
\sum_{n=1}^{\infty}
\frac{\sin(n\varepsilon)}{n}\cos(nx)
}.
$$

::: {.proof}
Combine steps <1>1--<1>3 with the real Fourier expansion
$$
\frac{a_0}{2}
+
\sum_{n=1}^{\infty}
\bigl(a_n\cos(nx)+b_n\sin(nx)\bigr).
$$
At points of continuity of $F_\varepsilon$ this series converges to
$F_\varepsilon$, and at the jump points it converges to the midpoint of
the two one-sided limits, by the Dirichlet convergence theorem.
:::

<1>5. In the degenerate parameter ranges, the Fourier series is
identically $0$ for $\varepsilon\leq0$ and identically $1$ for
$\varepsilon\geq\pi$.

::: {.proof}
On the fundamental interval $\abs{x}<\pi$, if $\varepsilon\leq0$ then
the condition $\abs{x}<\varepsilon$ never holds, so the function is zero.
If $\varepsilon\geq\pi$, then $\abs{x}<\varepsilon$ holds throughout the
fundamental interval, so the periodic function is $1$ away from the
irrelevant endpoint representatives. Its Fourier series is therefore the
constant series $1$.
:::

<1>6. One has
$$
\boxed{
\sum_{n=1}^{\infty}\frac{\sin n}{n}
=
\frac{\pi-1}{2}
}.
$$

::: {.proof}
Set
$$
\varepsilon=1
$$
in step <1>4. Since
$$
0<1<\pi
$$
and $x=0$ is a point of continuity with
$$
F_1(0)=1,
$$
the Dirichlet convergence theorem gives
$$
1
=
\frac1\pi
+
\frac2\pi
\sum_{n=1}^{\infty}\frac{\sin n}{n}.
$$
Multiplying by $\pi/2$ and rearranging gives the displayed value.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>4 and <1>5 give the Fourier series, and step <1>6 evaluates the
requested sum.
:::
:::
