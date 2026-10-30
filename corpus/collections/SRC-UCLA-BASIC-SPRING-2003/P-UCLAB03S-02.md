---
schema: qual/card@1
id: P-UCLAB03S-02
kind: problem
title: Absolute convergence implies convergence for a real series
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 of the official UCLA Basic Examination, May 2003 PDF.
---

::: {.problem}
Let $a_1,a_2,a_3,\ldots$ be real numbers satisfying
$$
\sum_{j=1}^{\infty}\abs{a_j}<\infty.
$$
Prove that
$$
\lim_{N\to\infty}\sum_{j=1}^N a_j
$$
exists.
:::

::: {.solution}

Let
$$
s_N=\sum_{j=1}^N a_j.
$$

::: pf

::: {.pf-step #s1-1}

The sequence of partial sums
$$
t_N=\sum_{j=1}^N\abs{a_j}
$$
is Cauchy.


::: pf-proof

The hypothesis
$$
\sum_{j=1}^{\infty}\abs{a_j}<\infty
$$
means precisely that the sequence $(t_N)$ converges in $\RR$. Every convergent real sequence is Cauchy.

:::

:::

::: {.pf-step #s1-2}

The sequence $(s_N)$ is Cauchy.


::: pf-proof

Let $\varepsilon>0$. By step [](#s1-1){.pf-ref}, there is $N_0$ such that whenever $m>n\ge N_0$,
$$
\sum_{j=n+1}^{m}\abs{a_j}
=
\abs{t_m-t_n}
<\varepsilon.
$$
For such $m,n$, the triangle inequality gives
$$
\abs{s_m-s_n}
=
\abs{\sum_{j=n+1}^{m}a_j}
\le
\sum_{j=n+1}^{m}\abs{a_j}
<\varepsilon.
$$
Hence $(s_N)$ is Cauchy.

:::

:::

::: {.pf-step #s1-3}

The sequence $(s_N)$ converges to a real number.


::: pf-proof

The real numbers are complete, so every Cauchy sequence in $\RR$ converges. Apply completeness to step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{\displaystyle
\lim_{N\to\infty}\sum_{j=1}^{N}a_j
\text{ exists in }\RR.}
$$


::: pf-proof

This is exactly the convergence of the partial-sum sequence established in step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
