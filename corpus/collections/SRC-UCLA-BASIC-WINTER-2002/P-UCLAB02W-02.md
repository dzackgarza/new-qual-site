---
schema: qual/card@1
id: P-UCLAB02W-02
kind: problem
title: Direct proof of sequential compactness of the unit interval
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 of the official UCLA Basic Examination, Winter 2002 PDF. The printed sentence ends "every infinite sequence has a convergent" and omits the word "subsequence"; the preceding phrase "sequentially compact" determines the intended statement.
---

::: {.problem}
Prove directly that the unit interval $[0,1]$ is sequentially compact: every infinite sequence in $[0,1]$ has a convergent subsequence.

Do not merely quote a general theorem such as Heine--Borel.
:::

::: {.solution}
Let $(x_n)_{n\ge1}$ be an arbitrary sequence in $[0,1]$.

<1>1. There is a nested sequence of closed intervals
$$
I_1\supseteq I_2\supseteq I_3\supseteq\cdots
$$
such that $I_k$ has length $2^{-k}$ and contains infinitely many terms of the sequence $(x_n)$.

::: {.proof}
Bisect $[0,1]$ into two closed intervals of length $1/2$. At least one of them contains infinitely many terms of the sequence; call such an interval $I_1$.

Inductively, suppose $I_k$ has been chosen and contains infinitely many terms of the sequence. Bisect $I_k$ into two closed subintervals of equal length. At least one of these contains infinitely many sequence terms; choose one and call it $I_{k+1}$. Then $I_{k+1}\subseteq I_k$, its length is $2^{-(k+1)}$, and it contains infinitely many terms.
:::

<1>2. There exists a strictly increasing sequence of indices
$$
n_1<n_2<n_3<\cdots
$$
such that
$$
x_{n_k}\in I_k
$$
for every $k$.

::: {.proof}
Choose $n_1$ with $x_{n_1}\in I_1$. Suppose $n_k$ has been chosen. Since $I_{k+1}$ contains infinitely many terms of the original sequence, there is some index $n_{k+1}>n_k$ with $x_{n_{k+1}}\in I_{k+1}$. This recursively constructs the desired subsequence.
:::

<1>3. The subsequence $(x_{n_k})$ is Cauchy.

::: {.proof}
Let $\varepsilon>0$. Choose $N$ so large that $2^{-N}<\varepsilon$. If $m,k\ge N$, then by nestedness,
$$
x_{n_m},x_{n_k}\in I_N.
$$
The diameter of $I_N$ is its length, namely $2^{-N}$. Therefore
$$
\abs{x_{n_m}-x_{n_k}}\le 2^{-N}<\varepsilon.
$$
Thus $(x_{n_k})$ is Cauchy.
:::

<1>4. The subsequence $(x_{n_k})$ converges to a point of $[0,1]$.

::: {.proof}
The real numbers are complete, so the Cauchy sequence from step <1>3 converges to some $x\in\RR$. Every term $x_{n_k}$ lies in the closed set $[0,1]$, and a closed subset of $\RR$ contains the limits of its convergent sequences. Hence $x\in[0,1]$.
:::

<1>5. Q.E.D.

::: {.proof}
The original sequence in $[0,1]$ was arbitrary. Step <1>4 constructs a convergent subsequence of it whose limit lies in $[0,1]$. Therefore $[0,1]$ is sequentially compact.
:::
:::
