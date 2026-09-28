---
schema: qual/card@1
id: P-BKS80-1
kind: problem
title: Fourier series and pointwise sum of the periodic sawtooth
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the Fourier coefficients by parity and integration by parts,
    proved failure of the uniform Cauchy criterion with a block of tails at
    x=pi-1/N, and applied the Dirichlet convergence theorem at continuity
    points and the jump points congruent to pi modulo 2pi.
---

::: {.problem}
Let $f:\RR\to\RR$ be the $2\pi$-periodic function satisfying $f(x)=x$ for $-\pi\le x<\pi$.

1. Prove that its Fourier series is
   \[
   \sum_{n=1}^{\infty}\frac{2(-1)^{n+1}\sin(nx)}{n}.
   \]
2. Prove that this series does not converge uniformly.
3. For each $x\in\RR$, find the sum of the series.
:::

::: {.solution}
<1>1. The cosine Fourier coefficients of $f$ vanish, and its sine
coefficients are
$$
b_n=\frac{2(-1)^{n+1}}{n}
\qquad(n\ge1).
$$

::: {.proof}
Changing a function at the endpoint $\pi$ does not affect its Fourier
coefficients, so the coefficients may be computed from $f(x)=x$ on
$[-\pi,\pi]$. Since $x$ is odd,
$$
a_0
=
\frac1\pi\int_{-\pi}^{\pi}x\,dx
=
0
$$
and, for $n\ge1$,
$$
a_n
=
\frac1\pi\int_{-\pi}^{\pi}x\cos(nx)\,dx
=
0,
$$
because $x\cos(nx)$ is odd. Also $x\sin(nx)$ is even, so
$$
\begin{aligned}
b_n
&=
\frac1\pi\int_{-\pi}^{\pi}x\sin(nx)\,dx\\
&=
\frac2\pi\int_0^\pi x\sin(nx)\,dx\\
&=
\frac2\pi
\left[
-\frac{x\cos(nx)}n+\frac{\sin(nx)}{n^2}
\right]_{0}^{\pi}\\
&=
-\frac{2(-1)^n}{n}
=
\frac{2(-1)^{n+1}}n.
\end{aligned}
$$
:::

<1>2. Therefore the Fourier series of $f$ is
$$
\boxed{
\sum_{n=1}^{\infty}
\frac{2(-1)^{n+1}\sin(nx)}{n}.
}
$$

::: {.proof}
Insert the coefficients from step <1>1 into the real Fourier-series
formula.
:::

<1>3. The series in step <1>2 does not satisfy the uniform Cauchy
criterion on $\RR$.

::: {.proof}
For an integer $N\ge1$, set
$$
x_N\coloneqq\pi-\frac1N.
$$
For $N\le n\le2N$,
$$
\sin(nx_N)
=
\sin\left(n\pi-\frac nN\right)
=
(-1)^{n+1}\sin\left(\frac nN\right).
$$
Hence the corresponding block of the series is
$$
\sum_{n=N}^{2N}
\frac{2(-1)^{n+1}\sin(nx_N)}n
=
2\sum_{n=N}^{2N}
\frac{\sin(n/N)}n.
$$
Let
$$
c\coloneqq\min_{1\le t\le2}\sin t.
$$
Since $[1,2]\subset(0,\pi)$, one has $c>0$. Thus
$$
2\sum_{n=N}^{2N}\frac{\sin(n/N)}n
\ge
2c\sum_{n=N}^{2N}\frac1n
\ge
2c(N+1)\frac1{2N}
\ge
c.
$$
Therefore tails with arbitrarily large starting index have supremum at
least $c$, so the uniform Cauchy criterion fails.
:::

<1>4. The Fourier series does not converge uniformly.

::: {.proof}
Uniform convergence of a series of functions implies the uniform Cauchy
criterion. Step <1>3 shows that criterion fails.
:::

<1>5. At every point where $f$ is continuous, the Fourier series converges
to $f(x)$; at each jump point
$$
x=(2k+1)\pi,
\qquad k\in\ZZ,
$$
it converges to $0$.

::: {.proof}
The periodic function $f$ is piecewise $C^1$. By the Dirichlet convergence
theorem, its Fourier series converges at each $x$ to
$$
\frac{f(x^-)+f(x^+)}2.
$$
Away from the odd multiples of $\pi$, the function is continuous, so this
value is $f(x)$. At $x=(2k+1)\pi$, periodicity gives one-sided limits
$$
f(x^-)=\pi,
\qquad
f(x^+)=-\pi,
$$
whose average is $0$.
:::

<1>6. Explicitly, the sum $S$ of the series is
$$
\boxed{
S(x)=
\begin{cases}
x-2k\pi,
& (2k-1)\pi<x<(2k+1)\pi\text{ for some }k\in\ZZ,\\
0,
&x=(2k+1)\pi\text{ for some }k\in\ZZ.
\end{cases}
}
$$

::: {.proof}
On the open interval
$$
((2k-1)\pi,(2k+1)\pi),
$$
periodicity and the defining formula on $[-\pi,\pi)$ give
$$
f(x)=x-2k\pi.
$$
Combine this with step <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>2 proves part (1), step <1>4 proves part (2), and step <1>6
answers part (3).
:::
:::
