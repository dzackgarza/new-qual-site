---
schema: qual/card@1
id: P-BERK81S-09
kind: problem
title: Fourier series and Parseval identity for the periodic function $x^3$
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
    The periodic function is odd, so its constant and cosine Fourier
    coefficients vanish; b_n=(2/pi)∫_0^pi x^3 sin(nx) dx. The function is
    piecewise C^1 on each period, so Dirichlet's theorem gives convergence
    everywhere, to f at continuity points and to 0 at the jump points
    congruent to pi mod 2pi. Parseval then gives
    sum b_n^2=(1/pi)∫_{-pi}^pi x^6 dx=2pi^6/7.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be the $2\pi$-periodic function satisfying $f(x)=x^3$ for $-\pi\le x<\pi$.

1. Prove that the Fourier series of $f$ has the form
   \[
   \sum_{n=1}^{\infty}b_n\sin(nx),
   \]
   and give an integral formula for $b_n$ without evaluating it.

2. Prove that the Fourier series converges for every $x$.

3. Prove that
   \[
   \sum_{n=1}^{\infty}b_n^2=\frac{2\pi^6}{7}.
   \]
:::

::: {.solution}
Use the Fourier-coefficient convention
$$
a_0=\frac1\pi\int_{-\pi}^{\pi}f(x)\,dx,
$$
$$
a_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos(nx)\,dx,
$$
and
$$
b_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin(nx)\,dx.
$$

::: pf

::: pf-step

The periodic function $f$ is odd almost everywhere.

::: pf-proof

For $-\pi<x<\pi$,
$$
f(-x)=(-x)^3=-x^3=-f(x).
$$
The endpoint values form a set of measure zero and do not affect the
Fourier coefficients.

:::

:::

::: {.pf-step #s2}

One has
$$
a_0=0.
$$

::: pf-proof

The function $f$ is odd almost everywhere on $[-\pi,\pi]$, so its integral
over that symmetric interval is zero.

:::

:::

::: {.pf-step #s3}

For every $n\geq1$,
$$
a_n=0.
$$

::: pf-proof

The function $f$ is odd almost everywhere, while $\cos(nx)$ is even.
Therefore $f(x)\cos(nx)$ is odd almost everywhere, and its integral over
$[-\pi,\pi]$ is zero.

:::

:::

::: {.pf-step #s4}

For every $n\geq1$,
$$
\boxed{
b_n
=
\frac2\pi
\int_0^\pi x^3\sin(nx)\,dx.
}
$$

::: pf-proof

The functions $x^3$ and $\sin(nx)$ are both odd, so their product is even.
Thus
$$
\begin{aligned}
b_n
&=
\frac1\pi
\int_{-\pi}^{\pi}x^3\sin(nx)\,dx\\
&=
\frac2\pi
\int_0^\pi x^3\sin(nx)\,dx.
\end{aligned}
$$

:::

:::

::: {.pf-step #s5}

The Fourier series of $f$ has the form
$$
\boxed{
\sum_{n=1}^{\infty}b_n\sin(nx).
}
$$

::: pf-proof

The general real Fourier series is
$$
\frac{a_0}{2}
+
\sum_{n=1}^{\infty}
\bigl(
a_n\cos(nx)+b_n\sin(nx)
\bigr).
$$
Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} show that the constant and cosine coefficients vanish.

:::

:::

::: {.pf-step #s6}

The function $f$ is piecewise $C^1$ on every period and has finite
one-sided limits at every point.

::: pf-proof

On each interval
$$
(-\pi+2k\pi,\pi+2k\pi),
\qquad
k\in\ZZ,
$$
the function is a translate of the polynomial $x^3$, hence is smooth.
At the endpoints the one-sided limits exist and are finite.

:::

:::

::: {.pf-step #s7}

At every point where $f$ is continuous, its Fourier series converges
to $f(x)$.

::: pf-proof

By step [](#s6){.pf-ref}, the hypotheses of the Dirichlet convergence theorem hold.
At a continuity point, the two one-sided limits agree with $f(x)$, so
their average is $f(x)$.

:::

:::

::: {.pf-step #s8}

At every discontinuity point
$$
x=(2k+1)\pi,
\qquad
k\in\ZZ,
$$
the Fourier series converges to $0$.

::: pf-proof

At each such point the one-sided limits are $\pi^3$ and $-\pi^3$, whose
average is $0$. The Dirichlet convergence theorem therefore gives
convergence to $0$.

:::

:::

::: {.pf-step #s9}

The Fourier series converges for every real $x$.

::: pf-proof

Every real point is either a continuity point, handled by step [](#s7){.pf-ref}, or a
jump point, handled by step [](#s8){.pf-ref}.

:::

:::

::: {.pf-step #s10}

Parseval's identity reduces here to
$$
\sum_{n=1}^{\infty}b_n^2
=
\frac1\pi
\int_{-\pi}^{\pi}\abs{f(x)}^2\,dx.
$$

::: pf-proof

The function $f$ is bounded on one period and therefore belongs to
$L^2([-\pi,\pi])$. Parseval's identity states
$$
\frac1\pi
\int_{-\pi}^{\pi}\abs{f(x)}^2\,dx
=
\frac{a_0^2}{2}
+
\sum_{n=1}^{\infty}
\left(
a_n^2+b_n^2
\right).
$$
Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} make all $a$-terms vanish.

:::

:::

::: {.pf-step #s11}

One has
$$
\frac1\pi
\int_{-\pi}^{\pi}\abs{f(x)}^2\,dx
=
\frac{2\pi^6}{7}.
$$

::: pf-proof

On $[-\pi,\pi)$,
$$
\abs{f(x)}^2=x^6.
$$
Therefore
$$
\begin{aligned}
\frac1\pi
\int_{-\pi}^{\pi}\abs{f(x)}^2\,dx
&=
\frac1\pi
\int_{-\pi}^{\pi}x^6\,dx\\
&=
\frac2\pi
\int_0^\pi x^6\,dx\\
&=
\frac2\pi
\frac{\pi^7}{7}\\
&=
\frac{2\pi^6}{7}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s12}

Therefore
$$
\boxed{
\sum_{n=1}^{\infty}b_n^2
=
\frac{2\pi^6}{7}.
}
$$

::: pf-proof

Combine steps [](#s10){.pf-ref} and [](#s11){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} prove part (1), step [](#s9){.pf-ref} proves part (2), and step
[](#s12){.pf-ref} proves part (3).

:::

:::

:::
