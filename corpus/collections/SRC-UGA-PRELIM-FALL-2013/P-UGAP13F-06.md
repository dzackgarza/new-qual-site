---
schema: qual/card@1
id: P-UGAP13F-06
kind: problem
title: Bound the partial sums of $\sum 1/j^2$ and decide whether they are Cauchy
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
For $k\in\NN$, let
$$
s_k=1+\frac1{2^2}+\cdots+\frac1{k^2}.
$$
Show that
$$
s_k\le 2-\frac1k.
$$
Prove or disprove: $(s_k)$ is a Cauchy sequence.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every integer $j\ge2$,
$$
\frac1{j^2}
\le
\frac1{j(j-1)}
=
\frac1{j-1}-\frac1j.
$$


::: pf-proof

Since $j-1\le j$ and both are positive,
$$
j(j-1)\le j^2,
$$
so taking reciprocals gives the inequality. The identity is the elementary partial-fraction decomposition
$$
\frac1{j(j-1)}=\frac1{j-1}-\frac1j.
$$

:::

:::

::: {.pf-step #s1-2}

For every $k\ge1$,
$$
\boxed{s_k\le2-\frac1k}.
$$


::: pf-proof

For $k=1$, both sides equal $1$. For $k\ge2$, step [](#s1-1){.pf-ref} gives
$$
\begin{aligned}
s_k
&=1+\sum_{j=2}^k\frac1{j^2}\\
&\le1+\sum_{j=2}^k\left(\frac1{j-1}-\frac1j\right)\\
&=1+1-\frac1k\\
&=2-\frac1k.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

The sequence $(s_k)$ is $\boxed{\text{Cauchy}}$.


::: pf-proof

Let $n>m\ge1$. By step [](#s1-1){.pf-ref},
$$
\begin{aligned}
|s_n-s_m|
&=\sum_{j=m+1}^n\frac1{j^2}\\
&\le\sum_{j=m+1}^n\left(\frac1{j-1}-\frac1j\right)\\
&=\frac1m-\frac1n\\
&<\frac1m.
\end{aligned}
$$
Given $\varepsilon>0$, choose $N\in\NN$ with $N>1/\varepsilon$. If $n,m\ge N$, relabeling if necessary so that $n\ge m$, the preceding estimate gives
$$
|s_n-s_m|<\frac1m\le\frac1N<\varepsilon.
$$
Hence $(s_k)$ satisfies the Cauchy criterion.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves the required bound, and step [](#s1-3){.pf-ref} proves that $(s_k)$ is Cauchy.

:::

:::

:::
