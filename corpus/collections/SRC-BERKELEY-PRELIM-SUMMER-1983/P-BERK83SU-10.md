---
schema: qual/card@1
id: P-BERK83SU-10
kind: problem
title: Periodic Wirtinger inequality for a zero-mean function
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The zero-mean hypothesis removes the constant Fourier coefficient.
    Periodicity cancels the integration-by-parts boundary terms, so the
    nth cosine and sine coefficients of f' are n b_n and -n a_n.
    Parseval then gives integral f'^2=pi sum n^2(a_n^2+b_n^2), which
    dominates integral f^2=pi sum(a_n^2+b_n^2).
---

::: {.problem}
Let $f:[0,2\pi]\to\mathbb R$ be twice differentiable and satisfy
\[
\int_0^{2\pi}f(x)\,dx=0,
\qquad
f(2\pi)=f(0).
\]
Prove that
\[
\int_0^{2\pi}f(x)^2\,dx
\le
\int_0^{2\pi}f'(x)^2\,dx.
\]
:::

::: {.solution}
For $n\geq1$, define the real Fourier coefficients
$$
a_n
=
\frac1\pi\int_0^{2\pi}f(x)\cos(nx)\,dx,
\qquad
b_n
=
\frac1\pi\int_0^{2\pi}f(x)\sin(nx)\,dx,
$$
and put
$$
a_0=\frac1\pi\int_0^{2\pi}f(x)\,dx.
$$

::: pf

::: {.pf-step #s1}

One has
$$
a_0=0.
$$

::: pf-proof

This is exactly the zero-mean hypothesis.

:::

:::

::: {.pf-step #s2}

For every $n\geq1$, the cosine and sine Fourier coefficients of
$f'$ are respectively
$$
n b_n
\qquad\text{and}\qquad
-n a_n.
$$

::: pf-proof

::: {.pf-step #s2-1}

The cosine coefficient of $f'$ is $n b_n$.

::: pf-proof

Integration by parts and $f(2\pi)=f(0)$ give
$$
\begin{aligned}
\frac1\pi
\int_0^{2\pi}f'(x)\cos(nx)\,dx
&=
\frac1\pi
\left[f(x)\cos(nx)\right]_0^{2\pi}
+
\frac n\pi
\int_0^{2\pi}f(x)\sin(nx)\,dx\\
&=
n b_n.
\end{aligned}
$$

:::

:::

::: {.pf-step #s2-2}

The sine coefficient of $f'$ is $-n a_n$.

::: pf-proof

Again by integration by parts,
$$
\begin{aligned}
\frac1\pi
\int_0^{2\pi}f'(x)\sin(nx)\,dx
&=
\frac1\pi
\left[f(x)\sin(nx)\right]_0^{2\pi}
-
\frac n\pi
\int_0^{2\pi}f(x)\cos(nx)\,dx\\
&=
-n a_n,
\end{aligned}
$$
because the boundary term vanishes.

:::

:::

::: pf-qed

Steps [](#s2-1){.pf-ref} and [](#s2-2){.pf-ref} prove step [](#s2){.pf-ref}.

:::

:::

:::

::: {.pf-step #s3}

Parseval's identity gives
$$
\int_0^{2\pi}f(x)^2\,dx
=
\pi\sum_{n=1}^{\infty}(a_n^2+b_n^2).
$$

::: pf-proof

For the real Fourier coefficients of $f$, Parseval's identity is
$$
\int_0^{2\pi}f(x)^2\,dx
=
\pi
\left(
\frac{a_0^2}{2}
+
\sum_{n=1}^{\infty}(a_n^2+b_n^2)
\right).
$$
Step [](#s1){.pf-ref} gives $a_0=0$.

:::

:::

::: {.pf-step #s4}

Parseval's identity also gives
$$
\int_0^{2\pi}f'(x)^2\,dx
=
\pi\sum_{n=1}^{\infty}n^2(a_n^2+b_n^2).
$$

::: pf-proof

The constant Fourier coefficient of $f'$ is
$$
\frac1\pi\int_0^{2\pi}f'(x)\,dx
=
\frac{f(2\pi)-f(0)}{\pi}
=0.
$$
By step [](#s2){.pf-ref}, its $n$th cosine and sine coefficients are $n b_n$ and
$-n a_n$. Parseval's identity for $f'$ therefore gives
$$
\begin{aligned}
\int_0^{2\pi}f'(x)^2\,dx
&=
\pi\sum_{n=1}^{\infty}
\left((n b_n)^2+(-n a_n)^2\right)\\
&=
\pi\sum_{n=1}^{\infty}n^2(a_n^2+b_n^2).
\end{aligned}
$$

:::

:::

::: {.pf-step #s5}

Therefore
$$
\boxed{
\int_0^{2\pi}f(x)^2\,dx
\leq
\int_0^{2\pi}f'(x)^2\,dx
}.
$$

::: pf-proof

For every $n\geq1$,
$$
n^2(a_n^2+b_n^2)
\geq
a_n^2+b_n^2.
$$
Summing this inequality and applying steps [](#s3){.pf-ref} and [](#s4){.pf-ref} gives the
result.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required inequality.

:::

:::

:::
