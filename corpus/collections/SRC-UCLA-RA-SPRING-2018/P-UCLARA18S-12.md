---
schema: qual/card@1
id: P-UCLARA18S-12
kind: problem
title: Bergman reproducing formula for bounded holomorphic functions on the disk
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 12. Let $f(z)$ be bounded and holomorphic on the unit disc
$$
\DD=\{z:\abs{z}<1\}.
$$
Prove that for every $w\in\DD$,
$$
f(w)=\frac1\pi\int_{\DD}\frac{f(z)}{(1-\overline z w)^2}\,dA(z),
$$
where $dA(z)$ means integration with respect to Lebesgue measure.
:::

::: {.solution}

Write the Taylor series of $f$ at the origin as
$$
f(z)=\sum_{n=0}^{\infty}a_nz^n.
$$

::: pf

::: {.pf-step #s1-1}

For every $n\ge0$,
$$
\boxed{
\int_{\DD}
f(z)\overline z^{\,n}\,dA(z)
=
\frac{\pi}{n+1}a_n}.
$$


::: pf-proof

Because $f$ is bounded and $\DD$ has finite area, the function
$$
f(z)\overline z^{\,n}
$$
is integrable. In polar coordinates,
$$
\begin{aligned}
\int_{\DD}
f(z)\overline z^{\,n}\,dA(z)
&=
\int_0^1
\int_0^{2\pi}
f(re^{i\theta})
r^n e^{-in\theta}
r\,d\theta\,dr.
\end{aligned}
$$
For fixed $0<r<1$, the Taylor series of $f$ converges uniformly on the
circle $\abs{z}=r$, so
$$
\begin{aligned}
\int_0^{2\pi}
f(re^{i\theta})e^{-in\theta}\,d\theta
&=
\sum_{m=0}^{\infty}
a_mr^m
\int_0^{2\pi}
e^{i(m-n)\theta}\,d\theta\\
&=
2\pi a_nr^n.
\end{aligned}
$$
Therefore
$$
\begin{aligned}
\int_{\DD}
f(z)\overline z^{\,n}\,dA(z)
&=
2\pi a_n
\int_0^1r^{2n+1}\,dr\\
&=
2\pi a_n
\frac1{2n+2}\\
&=
\frac{\pi}{n+1}a_n.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

For fixed $w\in\DD$,
$$
\boxed{
\frac1{(1-\overline zw)^2}
=
\sum_{n=0}^{\infty}
(n+1)\overline z^{\,n}w^n}
$$
uniformly for $z\in\DD$.


::: pf-proof

The differentiated geometric series gives
$$
\frac1{(1-\xi)^2}
=
\sum_{n=0}^{\infty}(n+1)\xi^n
\qquad(\abs{\xi}<1).
$$
Take
$$
\xi=\overline zw.
$$
Since $\abs{z}<1$,
$$
\abs{\xi}
\le
\abs{w}
<1.
$$
Moreover,
$$
\abs{(n+1)\overline z^{\,n}w^n}
\le
(n+1)\abs{w}^n,
$$
and
$$
\sum_{n=0}^{\infty}(n+1)\abs{w}^n
<\infty.
$$
The Weierstrass $M$-test therefore gives uniform convergence in $z$.

:::

:::

::: {.pf-step #s1-3}

One may integrate the series in step [](#s1-2){.pf-ref} term by term against
$f(z)\,dA(z)$.


::: pf-proof

Let
$$
\norm{f}_\infty
=
\sup_{z\in\DD}\abs{f(z)}
<\infty.
$$
The terms satisfy
$$
\abs{f(z)(n+1)\overline z^{\,n}w^n}
\le
\norm{f}_\infty
(n+1)\abs{w}^n.
$$
The right-hand side is summable in $n$ and independent of $z$, while
$\DD$ has finite area. Equivalently, the kernel series converges
uniformly by step [](#s1-2){.pf-ref} and $f\in L^1(\DD)$. Hence integration and
summation may be interchanged.

:::

:::

::: {.pf-step #s1-4}

For every $w\in\DD$,
$$
\begin{aligned}
\frac1\pi
\int_{\DD}
\frac{f(z)}
{(1-\overline zw)^2}
\,dA(z)
&=
\sum_{n=0}^{\infty}a_nw^n.
\end{aligned}
$$


::: pf-proof

By steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref},
$$
\begin{aligned}
\frac1\pi
\int_{\DD}
\frac{f(z)}
{(1-\overline zw)^2}
\,dA(z)
&=
\frac1\pi
\sum_{n=0}^{\infty}
(n+1)w^n
\int_{\DD}
f(z)\overline z^{\,n}\,dA(z).
\end{aligned}
$$
Apply step [](#s1-1){.pf-ref}:
$$
\begin{aligned}
&=
\frac1\pi
\sum_{n=0}^{\infty}
(n+1)w^n
\frac{\pi}{n+1}a_n\\
&=
\sum_{n=0}^{\infty}a_nw^n.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
f(w)
=
\frac1\pi
\int_{\DD}
\frac{f(z)}
{(1-\overline zw)^2}
\,dA(z)}
\qquad(w\in\DD).
$$


::: pf-proof

The Taylor series of the holomorphic function $f$ converges to $f(w)$
for every $w\in\DD$. Thus the series on the right-hand side of
step [](#s1-4){.pf-ref} equals $f(w)$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required reproducing formula.

:::

:::

:::
