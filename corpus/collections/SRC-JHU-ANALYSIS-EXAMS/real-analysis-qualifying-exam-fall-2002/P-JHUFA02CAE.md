---
schema: qual/card@1
id: P-JHUFA02CAE
kind: problem
title: "The sum of the odd sine series and the Basel problem"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Series
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 5 of the preserved JHU Fall 2002 Real Analysis qualifying exam packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

5.i. Find the sum of the series $\begin{array} { r } { \sum _ { n = 1 } ^ { \infty } \frac { \sin { ( 2 n - 1 ) x } } { 2 n - 1 } \mathrm { o n } \left( 0 , 2 \pi \right) } \end{array}$

ii.
Show that $\begin{array} { r } { \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { ( 2 n - 1 ) ^ { 2 } } } = { \frac { \pi ^ { 2 } } { 8 } } } \end{array}$

## Complex Analysis Core Qualifying Exam, Fall 2002

Do 5 of the 6 problems.
Indicate clearly which 5 you want graded; if it is not clear, we will grade $\# 1 \mathrm { - } 5$ . Each problem counts for 20 points.
In the case where there are two parts, the score is subdivided as indicated.
Note: for the purposes of the exam, holomorphic is the same as complex analytic.

::: {.solution}
<1>1. Identify the odd sine series as the Fourier series of a square wave.
::: {.proof}
Define the $2\pi$-periodic function
\[
q(x)=
\begin{cases}
1,&0<x<\pi,\\
-1,&\pi<x<2\pi,
\end{cases}
\]
with arbitrary values at integer multiples of $\pi$. Its cosine coefficients vanish, and its sine coefficients are
\[
b_k=\frac1\pi\int_0^{2\pi}q(x)\sin(kx)\,dx.
\]
For even $k$, $b_k=0$. For odd $k$,
\[
b_k=\frac4{\pi k}.
\]
Hence the Fourier series of $q$ is
\[
q(x)\sim \frac4\pi\sum_{n=1}^\infty
\frac{\sin((2n-1)x)}{2n-1}.
\]

The function $q$ is piecewise $C^1$, so the Dirichlet convergence theorem gives convergence at every point to the midpoint of the one-sided limits. Therefore, for $0<x<2\pi$,
\[
\sum_{n=1}^\infty\frac{\sin((2n-1)x)}{2n-1}
=
\begin{cases}
\dfrac\pi4,&0<x<\pi,\\[4pt]
0,&x=\pi,\\[4pt]
-\dfrac\pi4,&\pi<x<2\pi.
\end{cases}
\]
:::

<1>2. Apply Parseval's identity.
::: {.proof}
Since $q^2=1$ almost everywhere,
\[
\int_0^{2\pi}|q(x)|^2\,dx=2\pi.
\]
Parseval's identity for the real Fourier coefficients gives
\[
\frac1\pi\int_0^{2\pi}|q(x)|^2\,dx
=\sum_{k=1}^\infty b_k^2,
\]
because the constant and cosine coefficients vanish. Thus
\[
2
=\sum_{n=1}^\infty
\left(\frac4{\pi(2n-1)}\right)^2
=\frac{16}{\pi^2}
\sum_{n=1}^\infty\frac1{(2n-1)^2}.
\]
Therefore
\[
\boxed{
\sum_{n=1}^\infty\frac1{(2n-1)^2}=\frac{\pi^2}{8}.}
\]
:::
:::
