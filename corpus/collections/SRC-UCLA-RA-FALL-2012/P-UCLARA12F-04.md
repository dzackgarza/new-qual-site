---
schema: qual/card@1
id: P-UCLARA12F-04
kind: problem
title: Supremum growth of Fourier partial sums
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Series
  - Uniform Boundedness Principle
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Fix $f\in C(\circlegroup)$, where $\circlegroup=\RR/(2\pi\ZZ)$, and let $s_n$ denote the $n$th partial sum of the Fourier series of $f$.
Prove that
$$
\lim_{n\to\infty}\frac{\norm{s_n}_{L^\infty(\circlegroup)}}{\log n}=0.
$$
:::

::: {.solution}

Let
$$
D_n(t)=\sum_{k=-n}^n e^{ikt}
=\frac{\sin((n+\tfrac12)t)}{\sin(t/2)}
$$
be the Dirichlet kernel. Then
$$
s_n(x)=\frac1{2\pi}\int_{-\pi}^{\pi}f(x-t)D_n(t)\,dt.
$$

::: pf

::: {.pf-step #s1-1}

There is an absolute constant $C_0$ such that
$$
\frac1{2\pi}\norm{D_n}_{L^1(-\pi,\pi)}
\le C_0(1+\log n)
$$
for every $n\ge2$.


::: pf-proof

For $\abs{t}\le\pi$,
$$
\abs{D_n(t)}
\le 2n+1
$$
by the finite-sum formula. Also, since
$$
\abs{\sin(t/2)}\ge \frac{\abs{t}}{\pi}
$$
for $\abs{t}\le\pi$, the quotient formula gives
$$
\abs{D_n(t)}\le\frac{\pi}{\abs{t}}
$$
for $t\ne0$. Hence
$$
\abs{D_n(t)}\le C\min\left(n,\frac1{\abs{t}}\right)
$$
for an absolute constant $C$. Therefore
$$
\begin{aligned}
\norm{D_n}_1
&\le
2C\left(\int_0^{1/n}n\,dt
+\int_{1/n}^{\pi}\frac{dt}{t}\right)\\
&\le C'(1+\log n).
\end{aligned}
$$
Dividing by $2\pi$ proves the claim.

:::

:::

::: {.pf-step #s1-2}

For every continuous $g$ on $\circlegroup$,
$$
\norm{s_n(g)}_\infty
\le C_0(1+\log n)\norm{g}_\infty.
$$


::: pf-proof

Using the convolution formula and step [](#s1-1){.pf-ref},
$$
\begin{aligned}
\abs{s_n(g)(x)}
&\le\frac1{2\pi}
\int_{-\pi}^{\pi}\abs{g(x-t)}\,\abs{D_n(t)}\,dt\\
&\le\frac1{2\pi}\norm{g}_\infty\norm{D_n}_1\\
&\le C_0(1+\log n)\norm{g}_\infty.
\end{aligned}
$$
Taking the supremum over $x$ gives the estimate.

:::

:::

::: pf-step

Let $\varepsilon>0$. There is a trigonometric polynomial $P$ such that
$$
\norm{f-P}_\infty<\varepsilon.
$$


::: pf-proof

Trigonometric polynomials are uniformly dense in $C(\circlegroup)$ by the Stone--Weierstrass theorem.

:::

:::

::: {.pf-step #s1-4}

If $N$ is the degree of $P$, then for every $n\ge N$,
$$
s_n(P)=P.
$$


::: pf-proof

The Fourier series of a trigonometric polynomial has only finitely many nonzero coefficients. Once the partial sum includes all frequencies occurring in $P$, it equals $P$ identically.

:::

:::

::: {.pf-step #s1-5}

For every $n\ge N$,
$$
\norm{s_n(f)}_\infty
\le
\norm{P}_\infty
+C_0(1+\log n)\varepsilon.
$$


::: pf-proof

By linearity and step [](#s1-4){.pf-ref},
$$
s_n(f)=P+s_n(f-P).
$$
Therefore step [](#s1-2){.pf-ref} gives
$$
\begin{aligned}
\norm{s_n(f)}_\infty
&\le\norm{P}_\infty+\norm{s_n(f-P)}_\infty\\
&\le\norm{P}_\infty+C_0(1+\log n)\norm{f-P}_\infty\\
&<\norm{P}_\infty+C_0(1+\log n)\varepsilon.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-6}

One has
$$
\boxed{
\lim_{n\to\infty}
\frac{\norm{s_n}_{L^\infty(\circlegroup)}}{\log n}=0.}
$$


::: pf-proof

Divide the estimate from step [](#s1-5){.pf-ref} by $\log n$ and let $n\to\infty$:
$$
\limsup_{n\to\infty}
\frac{\norm{s_n(f)}_\infty}{\log n}
\le C_0\varepsilon.
$$
Since $\varepsilon>0$ was arbitrary, the limsup is $0$. The quotient is nonnegative, so the limit is $0$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
