---
schema: qual/card@1
id: P-UCLAB12W-03
kind: problem
title: Bolzano–Weierstrass theorem on the unit interval
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Winter 2012.
---

::: {.problem}
Prove that every sequence $(a_n)$ with $a_n\in[0,1]$ has a convergent subsequence.
:::

::: {.solution}
Let $(a_n)_{n\ge1}$ be a sequence in $[0,1]$.

<1>1. There exists a nested sequence of closed intervals
$$
I_1\supseteq I_2\supseteq\cdots
$$
such that $I_k$ has length $2^{-k}$ and contains infinitely many terms of $(a_n)$.

::: {.proof}
Bisect $[0,1]$ into two closed intervals of length $1/2$. At least one contains infinitely many terms of the sequence; choose one and call it $I_1$.

Inductively, if $I_k$ contains infinitely many terms, bisect it into two closed intervals of equal length. At least one contains infinitely many terms; choose it as $I_{k+1}$. Then $I_{k+1}\subseteq I_k$, its length is $2^{-(k+1)}$, and it contains infinitely many sequence terms.
:::

<1>2. There are strictly increasing indices
$$
n_1<n_2<\cdots
$$
such that
$$
a_{n_k}\in I_k
$$
for every $k$.

::: {.proof}
Choose $n_1$ with $a_{n_1}\in I_1$. Having chosen $n_k$, use the fact that $I_{k+1}$ contains infinitely many sequence terms to choose $n_{k+1}>n_k$ with $a_{n_{k+1}}\in I_{k+1}$.
:::

<1>3. The subsequence $(a_{n_k})$ is Cauchy.

::: {.proof}
Let $\varepsilon>0$. Choose $N$ with $2^{-N}<\varepsilon$. If $k,m\ge N$, then nestedness gives
$$
a_{n_k},a_{n_m}\in I_N.
$$
Hence
$$
\abs{a_{n_k}-a_{n_m}}
\le
\operatorname{length}(I_N)
=2^{-N}
<\varepsilon.
$$
:::

<1>4. The subsequence $(a_{n_k})$ converges to a point of $[0,1]$.

::: {.proof}
By completeness of $\RR$, the Cauchy sequence from step <1>3 converges to some $a\in\RR$. Since every term lies in the closed interval $[0,1]$, its limit also lies in $[0,1]$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 constructs a convergent subsequence of the arbitrary original sequence.
:::
:::
