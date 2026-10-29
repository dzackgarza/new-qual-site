---
schema: qual/card@1
id: P-WESRA11-1
kind: problem
title: 'Integral convergence need not imply almost-everywhere convergence'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. Flash drops the subscript on $f_n$ inside the displayed integral; the card restores it from the sequence named in the same sentence.
---

::: {.problem}
Prove or give a counterexample: if $f_n$ are continuous on $[0,1]$, $0\le f_n\le1$, and
$$
\lim_{n\to\infty}\int_0^1 f_n\,dm=0,
$$
then $f_n(x)\to0$ almost everywhere.
:::

::: {.solution}

For $k\ge1$ and $0\le j<2^k$, let
$$
I_{k,j}=\left[\frac{j}{2^k},\frac{j+1}{2^k}\right]
$$
and define
$$
g_{k,j}(x)
=\max\!\left\{0,1-2^k\operatorname{dist}(x,I_{k,j})\right\},
\qquad 0\le x\le1.
$$
Enumerate the functions $g_{k,j}$ level by level, first all $j$ for $k=1$, then all $j$ for $k=2$, and so on, and call the resulting sequence $(f_n)$.

::: pf

::: {.pf-step #s1-1}

Every $f_n$ is continuous and satisfies $0\le f_n\le1$.


::: pf-proof

For a closed interval $I$, the function $x\mapsto\operatorname{dist}(x,I)$ is continuous. The displayed formula for $g_{k,j}$ is therefore continuous, and the maximum construction makes its values lie in $[0,1]$.

:::

:::

::: {.pf-step #s1-2}

If $f_n=g_{k,j}$, then
$$
\int_0^1 f_n\,dm\le 3\cdot2^{-k}.
$$


::: pf-proof

The function $g_{k,j}$ vanishes whenever $\operatorname{dist}(x,I_{k,j})\ge2^{-k}$. Thus its support in $[0,1]$ has length at most
$$
|I_{k,j}|+2\cdot2^{-k}=3\cdot2^{-k}.
$$
Since $0\le g_{k,j}\le1$, its integral is at most the measure of its support.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\boxed{\lim_{n\to\infty}\int_0^1 f_n\,dm=0}.
$$


::: pf-proof

Only finitely many functions occur before level $k$, namely $\sum_{r<k}2^r$. Hence the level $k=k(n)$ of $f_n$ tends to infinity with $n$. Step [](#s1-2){.pf-ref} then gives
$$
0\le\int_0^1 f_n\,dm\le3\cdot2^{-k(n)}\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-4}

For every $x\in[0,1]$, the sequence $(f_n(x))$ has infinitely many terms equal to $1$.


::: pf-proof

For every level $k$, the dyadic intervals $I_{k,j}$ cover $[0,1]$. Choose $j_k$ with $x\in I_{k,j_k}$. Then
$$
g_{k,j_k}(x)=1
$$
because $\operatorname{dist}(x,I_{k,j_k})=0$. The enumeration includes one such term at every level $k$, hence infinitely many of them.

:::

:::

::: {.pf-step #s1-5}

The assertion is $\boxed{\text{false}}$; in fact, the constructed sequence fails to converge to $0$ at every point of $[0,1]$.


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref} verify all hypotheses of the assertion. Step [](#s1-4){.pf-ref} shows that for every $x$, the values $f_n(x)$ cannot converge to $0$, because an infinite subsequence is identically $1$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} supplies the required counterexample.

:::

:::

:::
