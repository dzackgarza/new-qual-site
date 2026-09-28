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

<1>1. The periodic function $f$ is odd almost everywhere.

::: {.proof}
For $-\pi<x<\pi$,
$$
f(-x)=(-x)^3=-x^3=-f(x).
$$
The endpoint values form a set of measure zero and do not affect the
Fourier coefficients.
:::

<1>2. One has
$$
a_0=0.
$$

::: {.proof}
The function $f$ is odd almost everywhere on $[-\pi,\pi]$, so its integral
over that symmetric interval is zero.
:::

<1>3. For every $n\geq1$,
$$
a_n=0.
$$

::: {.proof}
The function $f$ is odd almost everywhere, while $\cos(nx)$ is even.
Therefore $f(x)\cos(nx)$ is odd almost everywhere, and its integral over
$[-\pi,\pi]$ is zero.
:::

<1>4. For every $n\geq1$,
$$
\boxed{
b_n
=
\frac2\pi
\int_0^\pi x^3\sin(nx)\,dx.
}
$$

::: {.proof}
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

<1>5. The Fourier series of $f$ has the form
$$
\boxed{
\sum_{n=1}^{\infty}b_n\sin(nx).
}
$$

::: {.proof}
The general real Fourier series is
$$
\frac{a_0}{2}
+
\sum_{n=1}^{\infty}
\bigl(
a_n\cos(nx)+b_n\sin(nx)
\bigr).
$$
Steps <1>2--<1>3 show that the constant and cosine coefficients vanish.
:::

<1>6. The function $f$ is piecewise $C^1$ on every period and has finite
one-sided limits at every point.

::: {.proof}
On each interval
$$
(-\pi+2k\pi,\pi+2k\pi),
\qquad
k\in\ZZ,
$$
the function is a translate of the polynomial $x^3$, hence is smooth.
At the endpoints the one-sided limits exist and are finite.
:::

<1>7. At every point where $f$ is continuous, its Fourier series converges
to $f(x)$.

::: {.proof}
By step <1>6, the hypotheses of the Dirichlet convergence theorem hold.
At a continuity point, the two one-sided limits agree with $f(x)$, so
their average is $f(x)$.
:::

<1>8. At every discontinuity point
$$
x=(2k+1)\pi,
\qquad
k\in\ZZ,
$$
the Fourier series converges to $0$.

::: {.proof}
At each such point the one-sided limits are $\pi^3$ and $-\pi^3$, whose
average is $0$. The Dirichlet convergence theorem therefore gives
convergence to $0$.
:::

<1>9. The Fourier series converges for every real $x$.

::: {.proof}
Every real point is either a continuity point, handled by step <1>7, or a
jump point, handled by step <1>8.
:::

<1>10. Parseval's identity reduces here to
$$
\sum_{n=1}^{\infty}b_n^2
=
\frac1\pi
\int_{-\pi}^{\pi}\abs{f(x)}^2\,dx.
$$

::: {.proof}
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
Steps <1>2--<1>3 make all $a$-terms vanish.
:::

<1>11. One has
$$
\frac1\pi
\int_{-\pi}^{\pi}\abs{f(x)}^2\,dx
=
\frac{2\pi^6}{7}.
$$

::: {.proof}
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

<1>12. Therefore
$$
\boxed{
\sum_{n=1}^{\infty}b_n^2
=
\frac{2\pi^6}{7}.
}
$$

::: {.proof}
Combine steps <1>10--<1>11.
:::

<1>13. Q.E.D.

::: {.proof}
Steps <1>4--<1>5 prove part (1), step <1>9 proves part (2), and step
<1>12 proves part (3).
:::
:::
