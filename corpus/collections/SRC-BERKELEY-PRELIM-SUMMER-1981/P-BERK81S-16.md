---
schema: qual/card@1
id: P-BERK81S-16
kind: problem
title: A continuous-kernel integral operator sends $L^2$-Cauchy sequences to uniformly convergent sequences
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
    Bounded the continuous kernel uniformly on the compact square. Then
    Cauchy--Schwarz gives
    sup_x |g_n(x)-g_m(x)| <= M ||f_n-f_m||_2. The assumed L^2-Cauchy
    property therefore makes (g_n) uniformly Cauchy; taking pointwise
    limits in R turns the uniform Cauchy estimate into uniform convergence.
---

::: {.problem}
Let $f_n:[0,1]\to\mathbb R$ be continuous and suppose
\[
\int_0^1\bigl(f_n(x)-f_m(x)\bigr)^2\,dx\to0
\qquad(n,m\to\infty).
\]
Let $K:[0,1]\times[0,1]\to\mathbb R$ be continuous, and define
\[
g_n(x)=\int_0^1K(x,y)f_n(y)\,dy.
\]
Prove that $\{g_n\}$ converges uniformly on $[0,1]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There is a constant $M\geq0$ such that
$$
\abs{K(x,y)}
\leq
M
$$
for every $(x,y)\in[0,1]^2$.

::: pf-proof

The kernel $K$ is continuous on the compact set $[0,1]^2$. Hence the
continuous function
$$
(x,y)\longmapsto\abs{K(x,y)}
$$
attains a finite maximum. Let that maximum be $M$.

:::

:::

::: {.pf-step #s2}

For every $m,n$ and every $x\in[0,1]$,
$$
\abs{g_n(x)-g_m(x)}
\leq
M
\left(
\int_0^1
\bigl(f_n(y)-f_m(y)\bigr)^2
\,dy
\right)^{1/2}.
$$

::: pf-proof

By the definition of $g_n$,
$$
\begin{aligned}
\abs{g_n(x)-g_m(x)}
&=
\abs{
\int_0^1
K(x,y)
\bigl(f_n(y)-f_m(y)\bigr)
\,dy
}\\
&\leq
\left(
\int_0^1
\abs{K(x,y)}^2
\,dy
\right)^{1/2}
\left(
\int_0^1
\bigl(f_n(y)-f_m(y)\bigr)^2
\,dy
\right)^{1/2}
\end{aligned}
$$
by Cauchy--Schwarz. Step [](#s1){.pf-ref} gives
$$
\int_0^1
\abs{K(x,y)}^2
\,dy
\leq
\int_0^1M^2\,dy
=
M^2,
$$
which yields the stated estimate.

:::

:::

::: {.pf-step #s3}

One has
$$
\sup_{x\in[0,1]}
\abs{g_n(x)-g_m(x)}
\longrightarrow
0
$$
as $m,n\to\infty$.

::: pf-proof

The right-hand side of the estimate in step [](#s2){.pf-ref} is independent of $x$.
Therefore
$$
\sup_{x\in[0,1]}
\abs{g_n(x)-g_m(x)}
\leq
M
\left(
\int_0^1
\bigl(f_n(y)-f_m(y)\bigr)^2
\,dy
\right)^{1/2}.
$$
By hypothesis, the integral tends to zero as $m,n\to\infty$, so the
displayed supremum does also.

:::

:::

::: {.pf-step #s4}

For every $x\in[0,1]$, the sequence
$$
\bigl(g_n(x)\bigr)_{n\geq1}
$$
converges in $\RR$.

::: pf-proof

Step [](#s3){.pf-ref} shows in particular that, for fixed $x$,
$$
\abs{g_n(x)-g_m(x)}
\longrightarrow
0
$$
as $m,n\to\infty$. Thus $\bigl(g_n(x)\bigr)$ is a Cauchy sequence in the
complete metric space $\RR$, so it converges.

:::

:::

::: {.pf-step #s5}

Define
$$
g(x)
=
\lim_{n\to\infty}g_n(x)
$$
for $x\in[0,1]$. Then
$$
\boxed{
g_n\longrightarrow g
\text{ uniformly on }[0,1].
}
$$

::: pf-proof

Let $\varepsilon>0$. By step [](#s3){.pf-ref}, there is $N$ such that
$$
\abs{g_n(x)-g_m(x)}
<
\varepsilon
$$
for every $x\in[0,1]$ whenever $m,n\geq N$.

Fix $n\geq N$ and $x\in[0,1]$. Letting $m\to\infty$ and using the
definition of $g(x)$ from step [](#s4){.pf-ref} gives
$$
\abs{g_n(x)-g(x)}
\leq
\varepsilon.
$$
This holds for every $x\in[0,1]$, so
$$
\sup_{x\in[0,1]}
\abs{g_n(x)-g(x)}
\leq
\varepsilon
$$
whenever $n\geq N$. This is uniform convergence.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
