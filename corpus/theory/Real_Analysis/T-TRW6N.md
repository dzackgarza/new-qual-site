---
schema: qual/card@1
id: T-TRW6N
kind: theorem
title: Bounded convergence theorem
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Measure Theory
relations: []
review: draft
---

::: {.theorem}
Let $a<b$, let $m$ be Lebesgue measure on $\RR$, and let $f_n\colon\RR\to\RR$ for $n\geq1$ be [[D-DHFN4|Lebesgue measurable]] functions that vanish outside $[a,b]$.
Suppose there is $M\geq0$ with $\abs{f_n(x)}\leq M$ for all $n$ and all $x$, and that $f_n\to f$ pointwise for a function $f\colon\RR\to\RR$.
Then
$$
\lim_{n\to\infty}\int f_n\,dm=\int f\,dm.
$$
:::

::: {.proof}
As a pointwise limit of measurable functions, $f$ is measurable; it vanishes outside $[a,b]$ and satisfies $\abs{f}\leq M$, so $f_n$ and $f$ are integrable.
Let $\varepsilon>0$.
By [[FT-OGS76|Egorov's theorem]] applied on $[a,b]$, there is a closed set $B\subseteq[a,b]$ with $m(A)<\varepsilon$ for $A\coloneqq[a,b]\setminus B$, such that $f_n\to f$ [[D-YZC3C|uniformly]] on $B$.
Then
$$
\abs{\int_B (f_n-f)\,dm}\leq(b-a)\sup_{x\in B}\abs{f_n(x)-f(x)}\longrightarrow0,
$$
and, since $\abs{f_n-f}\leq 2M$,
$$
\abs{\int_A (f_n-f)\,dm}\leq 2M\,m(A)<2M\varepsilon.
$$
Since $f_n-f$ vanishes outside $A\cup B$,
$$
\limsup_{n\to\infty}\abs{\int f_n\,dm-\int f\,dm}\leq 0+2M\varepsilon.
$$
As $\varepsilon>0$ was arbitrary, $\int f_n\,dm\to\int f\,dm$.
:::

::: {.remark}
The theorem is a special case of the [[FT-LCR5P|dominated convergence theorem]], with dominating function $M\chi_{[a,b]}$.
:::
