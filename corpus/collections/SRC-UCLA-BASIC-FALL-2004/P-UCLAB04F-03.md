---
schema: qual/card@1
id: P-UCLAB04F-03
kind: problem
title: Uniform convergence and convergence of Riemann integrals
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 of the official UCLA Basic Exam Fall 2004 PDF.
---

::: {.problem}
Show that if $f_n\to f$ uniformly on the bounded closed interval $[a,b]$, then
$$
\int_a^b f_n(x)\,dx
\longrightarrow
\int_a^b f(x)\,dx.
$$
:::

::: {.solution}

The displayed integrals require the usual implicit hypothesis that each $f_n$ is Riemann integrable. Under that hypothesis, uniform convergence also implies that $f$ is Riemann integrable.

::: pf

::: {.pf-step #s1-1}

The uniform limit $f$ is Riemann integrable on $[a,b]$.


::: pf-proof

Let $\varepsilon>0$. Choose $N$ such that
$$
\norm{f-f_N}_\infty
<
\frac{\varepsilon}{4(b-a)}.
$$
Since $f_N$ is Riemann integrable, there is a partition $P$ of $[a,b]$ such that
$$
U(f_N,P)-L(f_N,P)<\frac{\varepsilon}{2}.
$$

Set
$$
\delta=\norm{f-f_N}_\infty.
$$
On every subinterval $I$ of $P$,
$$
\sup_I f\le \sup_I f_N+\delta
$$
and
$$
\inf_I f\ge \inf_I f_N-\delta.
$$
Hence
$$
U(f,P)-L(f,P)
\le
U(f_N,P)-L(f_N,P)+2\delta(b-a)
<
\varepsilon.
$$
By the Darboux criterion, $f$ is Riemann integrable.

:::

:::

::: {.pf-step #s1-2}

For every $n$,
$$
\abs{
\int_a^b f_n(x)\,dx
-
\int_a^b f(x)\,dx
}
\le
(b-a)\norm{f_n-f}_\infty.
$$


::: pf-proof

The function $f_n-f$ is Riemann integrable by step [](#s1-1){.pf-ref} and linearity of the Riemann integral. Since
$$
-\norm{f_n-f}_\infty
\le
f_n(x)-f(x)
\le
\norm{f_n-f}_\infty
$$
for every $x\in[a,b]$, monotonicity of the integral gives
$$
-(b-a)\norm{f_n-f}_\infty
\le
\int_a^b(f_n-f)
\le
(b-a)\norm{f_n-f}_\infty.
$$
Taking absolute values yields the claim.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\boxed{
\int_a^b f_n(x)\,dx
\longrightarrow
\int_a^b f(x)\,dx
}.
$$


::: pf-proof

Uniform convergence means
$$
\norm{f_n-f}_\infty\to0.
$$
Therefore the right side of the estimate in step [](#s1-2){.pf-ref} tends to $0$, forcing the difference of the integrals to tend to $0$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} justifies the existence of the limiting integral, and step [](#s1-3){.pf-ref} proves the stated convergence.

:::

:::

:::
