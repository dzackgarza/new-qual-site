---
schema: qual/card@1
id: P-BKF05-2B
kind: problem
title: Dirichlet convergence for a monotone sine integral
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2005 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained alternating-half-period proof and made
    the final arbitrary-R step explicit by bounding the remaining partial
    half-period by a_N, which tends to zero.
---

::: {.problem}
Let \(f:[0,\infty)\to\mathbb R\) be continuous, nonnegative, nonincreasing, and satisfy
\[
\lim_{x\to\infty}f(x)=0.
\]
Show that the improper integral
\[
\int_0^\infty f(x)\sin x\,dx
\]
converges.
:::

::: {.solution}

For each integer $n\ge0$, define
$$
a_n=
\int_{n\pi}^{(n+1)\pi}
f(x)\abs{\sin x}\,dx.
$$

::: pf

::: {.pf-step #an-nonneg-nonincreasing}
The sequence $(a_n)$ is nonnegative and nonincreasing.

::: pf-proof
After the substitution $x=t+n\pi$,
$$
a_n
=
\int_0^\pi
f(t+n\pi)\sin t\,dt,
$$
because $\sin t\ge0$ on $[0,\pi]$. Since $f$ is nonnegative,
$a_n\ge0$. Since $f$ is nonincreasing,
$$
f(t+(n+1)\pi)\le f(t+n\pi)
$$
for $0\le t\le\pi$, and therefore $a_{n+1}\le a_n$.
:::

:::

::: {.pf-step #an-to-zero}
One has
$$
a_n\longrightarrow0.
$$

::: pf-proof
For $0\le t\le\pi$, monotonicity gives
$$
0\le f(t+n\pi)\le f(n\pi).
$$
Hence
$$
0\le a_n
\le
f(n\pi)\int_0^\pi\sin t\,dt
=
2f(n\pi).
$$
The hypothesis $f(x)\to0$ as $x\to\infty$ therefore implies
$a_n\to0$.
:::

:::

::: {.pf-step #IN-converges}
The sequence
$$
I_N\coloneqq
\int_0^{N\pi}f(x)\sin x\,dx
$$
converges as $N\to\infty$.

::: pf-proof
On the interval $[n\pi,(n+1)\pi]$, the sign of $\sin x$ is
$(-1)^n$. Therefore
$$
\begin{aligned}
I_N
&=
\sum_{n=0}^{N-1}
\int_{n\pi}^{(n+1)\pi}f(x)\sin x\,dx
\\
&=
\sum_{n=0}^{N-1}(-1)^n a_n.
\end{aligned}
$$
By steps [](#an-nonneg-nonincreasing){.pf-ref} and [](#an-to-zero){.pf-ref}, the sequence $(a_n)$ is nonnegative,
nonincreasing, and tends to zero. The alternating-series theorem
therefore shows that the displayed series, and hence $I_N$, converges.
:::

:::

::: {.pf-step #partial-period-bound}
If $N\pi\le R<(N+1)\pi$, then
$$
\abs{
\int_0^R f(x)\sin x\,dx-I_N
}
\le a_N.
$$

::: pf-proof
The difference is the integral over the final partial half-period:
$$
\begin{aligned}
\abs{
\int_0^R f(x)\sin x\,dx-I_N
}
&=
\abs{
\int_{N\pi}^R f(x)\sin x\,dx
}
\\
&\le
\int_{N\pi}^R f(x)\abs{\sin x}\,dx
\\
&\le
\int_{N\pi}^{(N+1)\pi}
f(x)\abs{\sin x}\,dx
\\
&=
a_N.
\end{aligned}
$$
:::

:::

::: {.pf-step #integral-converges}
The improper integral
$$
\boxed{
\int_0^\infty f(x)\sin x\,dx
\text{ converges}
}.
$$

::: pf-proof
Let $L=\lim_{N\to\infty}I_N$, whose existence is given by step [](#IN-converges){.pf-ref}.
For $R\to\infty$, let $N$ be the integer with
$N\pi\le R<(N+1)\pi$. Then $N\to\infty$, and step [](#partial-period-bound){.pf-ref} gives
$$
\abs{
\int_0^R f(x)\sin x\,dx-L
}
\le
a_N+\abs{I_N-L}.
$$
Both terms tend to zero by steps [](#an-to-zero){.pf-ref} and [](#IN-converges){.pf-ref}. Hence the truncated
integrals converge to $L$ as $R\to\infty$.
:::

:::

::: pf-qed
Step [](#integral-converges){.pf-ref} is the required convergence statement.
:::

:::

:::
