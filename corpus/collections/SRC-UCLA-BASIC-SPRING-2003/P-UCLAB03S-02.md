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
\[
\sum_{j=1}^{\infty}|a_j|<\infty.
\]
Prove that
\[
\lim_{N\to\infty}\sum_{j=1}^N a_j
\]
exists.
:::

::: {.solution}
Let
\[
s_N=\sum_{j=1}^N a_j.
\]

<1>1. The sequence of partial sums
\[
t_N=\sum_{j=1}^N|a_j|
\]
is Cauchy.

::: {.proof}
The hypothesis
\[
\sum_{j=1}^{\infty}|a_j|<\infty
\]
means precisely that the sequence \((t_N)\) converges in \(\mathbb R\). Every convergent real sequence is Cauchy.
:::

<1>2. The sequence \((s_N)\) is Cauchy.

::: {.proof}
Let \(\varepsilon>0\). By step <1>1, there is \(N_0\) such that whenever \(m>n\ge N_0\),
\[
\sum_{j=n+1}^{m}|a_j|
=
|t_m-t_n|
<\varepsilon.
\]
For such \(m,n\), the triangle inequality gives
\[
|s_m-s_n|
=
\left|\sum_{j=n+1}^{m}a_j\right|
\le
\sum_{j=n+1}^{m}|a_j|
<\varepsilon.
\]
Hence \((s_N)\) is Cauchy.
:::

<1>3. The sequence \((s_N)\) converges to a real number.

::: {.proof}
The real numbers are complete, so every Cauchy sequence in \(\mathbb R\) converges. Apply completeness to step <1>2.
:::

<1>4. Therefore
\[
\boxed{\displaystyle
\lim_{N\to\infty}\sum_{j=1}^{N}a_j
\text{ exists in }\mathbb R.}
\]

::: {.proof}
This is exactly the convergence of the partial-sum sequence established in step <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
