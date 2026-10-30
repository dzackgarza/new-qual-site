---
schema: qual/card@1
id: P-HM21B18-FIN-12
kind: problem
title: Fourier series and Parseval sum for the Pacific-rim step function
classification: {areas: [applied-algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
On $[-\pi,\pi]$, let
$$
f(x)=
\begin{cases}
1,&\abs{x}>1,\\
-1,&\abs{x}\le1.
\end{cases}
$$

Use the course convention
$$
f(x)=\frac{a_0}{\sqrt2}
+\sum_{n=1}^\infty\bigl(a_n\cos(nx)+b_n\sin(nx)\bigr).
$$

(a) Find the Fourier series of $f$.

(b) Find
$$
a_0^2+\sum_{n=1}^\infty(a_n^2+b_n^2).
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every sine coefficient is zero.


::: pf-proof

The function $f$ is even, while $\sin(nx)$ is odd. Hence
$f(x)\sin(nx)$ is odd and
$$
b_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin(nx)\,dx=0
$$
for every $n\geq1$.

:::

:::

::: {.pf-step #s1-2}

For every $n\geq1$,
$$
a_n=-\frac{4\sin n}{\pi n}.
$$


::: pf-proof

By evenness,
$$
\begin{aligned}
a_n
&=\frac2\pi\int_0^\pi f(x)\cos(nx)\,dx\\
&=\frac2\pi\left(
-\int_0^1\cos(nx)\,dx
+\int_1^\pi\cos(nx)\,dx
\right).
\end{aligned}
$$
Since $\sin(n\pi)=0$,
$$
\begin{aligned}
a_n
&=\frac2\pi\left(
-\frac{\sin n}{n}
+\frac{\sin(n\pi)-\sin n}{n}
\right)\\
&=-\frac{4\sin n}{\pi n}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

The constant coefficient is
$$
a_0=\frac{\sqrt2(\pi-2)}{\pi}.
$$


::: pf-proof

With the stated convention,
$$
a_0
=\frac1\pi\int_{-\pi}^{\pi}
f(x)\frac1{\sqrt2}\,dx.
$$
Using evenness,
$$
\begin{aligned}
a_0
&=\frac{\sqrt2}{\pi}
\left(-\int_0^1 1\,dx+\int_1^\pi1\,dx\right)\\
&=\frac{\sqrt2}{\pi}(-1+\pi-1)
=\frac{\sqrt2(\pi-2)}{\pi}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

The Fourier series is
$$
\boxed{
f(x)\sim
\frac{\pi-2}{\pi}
-\frac4\pi\sum_{n=1}^\infty
\frac{\sin n}{n}\cos(nx).}
$$


::: pf-proof

Substitute steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} into
$$
\frac{a_0}{\sqrt2}
+\sum_{n=1}^\infty(a_n\cos(nx)+b_n\sin(nx)).
$$
The constant term is
$a_0/\sqrt2=(\pi-2)/\pi$, giving the displayed series.
At continuity points it converges to $f(x)$; at the jump points
$x=\pm1$ it converges to the midpoint value $0$.

:::

:::

::: {.pf-step #s1-5}

The sum of the squares of all Fourier coefficients is
$$
\boxed{2}.
$$


::: pf-proof

For the inner product underlying the stated coefficient normalization,
Parseval's identity gives
$$
a_0^2+\sum_{n=1}^\infty(a_n^2+b_n^2)
=\frac1\pi\int_{-\pi}^{\pi}\abs{f(x)}^2\,dx.
$$
Since $\abs{f(x)}=1$ everywhere,
$$
\frac1\pi\int_{-\pi}^{\pi}1\,dx=2.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the Fourier series and step [](#s1-5){.pf-ref} gives the requested
Parseval sum.

:::

:::

:::
