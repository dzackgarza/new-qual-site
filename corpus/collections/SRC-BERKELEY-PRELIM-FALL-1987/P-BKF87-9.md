---
schema: qual/card@1
id: P-BKF87-9
kind: problem
title: The integral $\int_0^{2\pi}\frac{\cos^2(3\theta)}{5-4\cos(2\theta)}\,d\theta$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Evaluate
\[
\int_0^{2\pi}
\frac{\cos^2(3\theta)}{5-4\cos(2\theta)}\,d\theta.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $0<r<1$ and real $\phi$,
$$
\frac{1-r^2}{1-2r\cos\phi+r^2}
=
1+2\sum_{k=1}^{\infty}r^k\cos(k\phi).
$$

::: pf-proof

Since $\abs r<1$,
$$
\sum_{k=1}^{\infty}r^ke^{ik\phi}
=
\frac{re^{i\phi}}{1-re^{i\phi}}.
$$
Taking twice the real part and adding $1$ gives
$$
\begin{aligned}
1+2\sum_{k=1}^{\infty}r^k\cos(k\phi)
&=
1+2\Re\left(\frac{re^{i\phi}}{1-re^{i\phi}}\right)\\
&=
\frac{1-r^2}{1-2r\cos\phi+r^2}.
\end{aligned}
$$
The series converges uniformly in $\phi$ because
$$
\sum_{k=1}^{\infty}2r^k<\infty.
$$

:::

:::

::: {.pf-step #s2}

One has the uniformly convergent expansion
$$
\frac1{5-4\cos(2\theta)}
=
\frac13
\left(
1+2\sum_{k=1}^{\infty}2^{-k}\cos(2k\theta)
\right).
$$

::: pf-proof

Take
$$
r=\frac12,
\qquad
\phi=2\theta
$$
in step [](#s1){.pf-ref}. Since
$$
5-4\cos(2\theta)
=
4\left(1-2r\cos(2\theta)+r^2\right)
$$
and
$$
1-r^2=\frac34,
$$
division gives exactly the displayed formula.

:::

:::

::: {.pf-step #s3}

One has
$$
\int_0^{2\pi}\frac{d\theta}{5-4\cos(2\theta)}
=
\frac{2\pi}{3}.
$$

::: pf-proof

Integrate the uniformly convergent series in step [](#s2){.pf-ref} term by term. For every $k\geq1$,
$$
\int_0^{2\pi}\cos(2k\theta)\,d\theta=0.
$$
Only the constant term remains, giving
$$
\frac13\int_0^{2\pi}1\,d\theta
=
\frac{2\pi}{3}.
$$

:::

:::

::: {.pf-step #s4}

One has
$$
\int_0^{2\pi}
\frac{\cos(6\theta)}{5-4\cos(2\theta)}
\,d\theta
=
\frac{\pi}{12}.
$$

::: pf-proof

Multiply the series in step [](#s2){.pf-ref} by $\cos(6\theta)$ and integrate term by term. Orthogonality of the cosine functions gives zero for every term except $k=3$. Hence
$$
\begin{aligned}
\int_0^{2\pi}
\frac{\cos(6\theta)}{5-4\cos(2\theta)}
\,d\theta
&=
\frac13\cdot2\cdot2^{-3}
\int_0^{2\pi}\cos^2(6\theta)\,d\theta\\
&=
\frac13\cdot\frac14\cdot\pi\\
&=
\frac{\pi}{12}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s5}

The required integral is
$$
\boxed{\frac{3\pi}{8}}.
$$

::: pf-proof

Using
$$
\cos^2(3\theta)
=
\frac{1+\cos(6\theta)}2,
$$
steps [](#s3){.pf-ref} and [](#s4){.pf-ref} give
$$
\begin{aligned}
\int_0^{2\pi}
\frac{\cos^2(3\theta)}{5-4\cos(2\theta)}
\,d\theta
&=
\frac12
\left(
\frac{2\pi}{3}
+
\frac{\pi}{12}
\right)\\
&=
\frac{3\pi}{8}.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required evaluation.

:::

:::

:::
