---
schema: qual/card@1
id: P-BKS19-3B
kind: problem
title: Convergence of the iteration $x_{n+1}=1/(1+x_n)$
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
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
---

::: {.problem}
Show that
$$
x_{n+1}=(1+x_n)^{-1}
$$
converges and find its limit for any $x_0>0$.
:::

::: {.solution}
Let
$$
\alpha=\frac{\sqrt5-1}{2}.
$$

::: pf

::: {.pf-step #s1}

Every term $x_n$ is positive.

::: pf-proof

The hypothesis gives $x_0>0$. If $x_n>0$, then
$$
x_{n+1}=\frac{1}{1+x_n}>0.
$$
The claim follows by induction.

:::

:::

::: {.pf-step #s2}

The number $\alpha$ is the unique positive fixed point of the map
$$
T(x)=\frac{1}{1+x}.
$$

::: pf-proof

The fixed-point equation is
$$
\alpha=\frac{1}{1+\alpha},
$$
equivalently
$$
\alpha^2+\alpha-1=0.
$$
Its two roots are
$$
\frac{-1\pm\sqrt5}{2},
$$
and exactly one of them is positive, namely $\alpha=(\sqrt5-1)/2$. In particular,
$$
\frac{1}{1+\alpha}=\alpha
\qquad\text{and}\qquad
0<\alpha<1.
$$

:::

:::

::: {.pf-step #s3}

For every $n\geq0$,
$$
\abs{x_{n+1}-\alpha}
\leq
\alpha\abs{x_n-\alpha}.
$$

::: pf-proof

Using step [](#s2){.pf-ref},
$$
\begin{aligned}
\abs{x_{n+1}-\alpha}
&=
\left\lvert
\frac{1}{1+x_n}-\frac{1}{1+\alpha}
\right\rvert\\
&=
\frac{\abs{x_n-\alpha}}{(1+x_n)(1+\alpha)}.
\end{aligned}
$$
By step [](#s1){.pf-ref}, $x_n>0$, so $1+x_n\geq1$. Therefore
$$
\frac{1}{(1+x_n)(1+\alpha)}
\leq
\frac{1}{1+\alpha}
=
\alpha,
$$
where the last equality is step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

For every $n\geq0$,
$$
\abs{x_n-\alpha}
\leq
\alpha^n\abs{x_0-\alpha}.
$$

::: pf-proof

This follows by induction from step [](#s3){.pf-ref}. The case $n=0$ is equality. If the estimate holds at $n$, then
$$
\abs{x_{n+1}-\alpha}
\leq
\alpha\abs{x_n-\alpha}
\leq
\alpha^{n+1}\abs{x_0-\alpha}.
$$

:::

:::

::: {.pf-step #s5}

The sequence converges and
$$
\boxed{\displaystyle\lim_{n\to\infty}x_n=\frac{\sqrt5-1}{2}}.
$$

::: pf-proof

By step [](#s2){.pf-ref}, $0<\alpha<1$, so
$$
\alpha^n\abs{x_0-\alpha}\longrightarrow0.
$$
Step [](#s4){.pf-ref} therefore gives
$$
\abs{x_n-\alpha}\longrightarrow0,
$$
which is exactly $x_n\to\alpha$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} proves convergence and gives the requested limit.

:::

:::

:::
