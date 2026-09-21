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

<1>1. One has
$$
a_0=0.
$$

::: {.proof}
This is exactly the zero-mean hypothesis.
:::

<1>2. For every $n\geq1$, the cosine and sine Fourier coefficients of
$f'$ are respectively
$$
n b_n
\qquad\text{and}\qquad
-n a_n.
$$

<2>1. The cosine coefficient of $f'$ is $n b_n$.

::: {.proof}
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

<2>2. The sine coefficient of $f'$ is $-n a_n$.

::: {.proof}
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

<2>3. Q.E.D.

::: {.proof}
Steps <2>1 and <2>2 prove step <1>2.
:::

<1>3. Parseval's identity gives
$$
\int_0^{2\pi}f(x)^2\,dx
=
\pi\sum_{n=1}^{\infty}(a_n^2+b_n^2).
$$

::: {.proof}
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
Step <1>1 gives $a_0=0$.
:::

<1>4. Parseval's identity also gives
$$
\int_0^{2\pi}f'(x)^2\,dx
=
\pi\sum_{n=1}^{\infty}n^2(a_n^2+b_n^2).
$$

::: {.proof}
The constant Fourier coefficient of $f'$ is
$$
\frac1\pi\int_0^{2\pi}f'(x)\,dx
=
\frac{f(2\pi)-f(0)}{\pi}
=0.
$$
By step <1>2, its $n$th cosine and sine coefficients are $n b_n$ and
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

<1>5. Therefore
$$
\boxed{
\int_0^{2\pi}f(x)^2\,dx
\leq
\int_0^{2\pi}f'(x)^2\,dx
}.
$$

::: {.proof}
For every $n\geq1$,
$$
n^2(a_n^2+b_n^2)
\geq
a_n^2+b_n^2.
$$
Summing this inequality and applying steps <1>3 and <1>4 gives the
result.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required inequality.
:::
:::
