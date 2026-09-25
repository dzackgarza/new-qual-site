---
schema: qual/card@1
id: P-BKS05-1A
kind: problem
title: Summable successive differences imply a Cauchy sequence
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against fresh deterministic MinerU Flash extractions of the UC Berkeley Spring 2005 exam and its companion solution packet; unambiguous duplicated-statement extraction defects were normalized.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked the retained solution: use a tail of the
    convergent successive-difference series for (a), and a_n=(-1)^n/n
    as a convergent counterexample for (b).
---

::: {.problem}
(a) Let $( a _ { n } ) _ { 1 } ^ { \infty }$ be a sequence in R such that

$$
\sum _ { n = 1 } ^ { \infty } \left| a _ { n + 1 } - a _ { n } \right| < \infty .
$$

Prove that $( a _ { n } ) _ { 1 } ^ { \infty }$ is a Cauchy sequence.

(b) Is the converse true?
Give a proof or a counterexample.
:::

::: {.solution}
<1>1. Under the hypothesis in part (a), the sequence $(a_n)$ is
Cauchy.

::: {.proof}
Let $\varepsilon>0$. Since
$$
\sum_{k=1}^{\infty}|a_{k+1}-a_k|
$$
converges, there is $N$ such that
$$
\sum_{k=N}^{\infty}|a_{k+1}-a_k|<\varepsilon.
$$
If $n>m\geq N$, then
$$
\begin{aligned}
|a_n-a_m|
&=
\left|\sum_{k=m}^{n-1}(a_{k+1}-a_k)\right|\\
&\leq
\sum_{k=m}^{n-1}|a_{k+1}-a_k|\\
&\leq
\sum_{k=N}^{\infty}|a_{k+1}-a_k|\\
&<
\varepsilon.
\end{aligned}
$$
Thus $(a_n)$ is Cauchy.
:::

<1>2. The converse in part (b) is false.

::: {.proof}
Take
$$
a_n\coloneqq\frac{(-1)^n}{n}.
$$
Then $a_n\to0$, so $(a_n)$ is Cauchy. However,
$$
|a_{n+1}-a_n|
=
\frac{2n+1}{n(n+1)}.
$$
Moreover,
$$
\lim_{n\to\infty}
\frac{(2n+1)/(n(n+1))}{1/n}
=
2.
$$
Hence the limit comparison test with the harmonic series gives
$$
\sum_{n=1}^{\infty}|a_{n+1}-a_n|
=
\infty.
$$
Thus a Cauchy sequence need not have summable successive absolute
differences.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>1 proves part (a), and step <1>2 answers part (b).
:::
:::
