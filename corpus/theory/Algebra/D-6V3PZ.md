---
schema: qual/card@1
id: D-6V3PZ
kind: definition
title: Möbius function
classification:
  areas:
  - algebra
  topics:
  - Number Theory
relations: []
review: draft
---

::: {.definition}
For a positive integer
$$
n=\prod_{i=1}^r p_i^{e_i}
$$
with distinct primes $p_i$, the \dfn{Möbius function}
$$
\mu\colon \ZZ_{>0}\longrightarrow\ZZ
$$
is defined by
$$
\mu(n)=
\begin{cases}
1,&n=1,\\
(-1)^r,&e_1=\cdots=e_r=1,\\
0,&e_i\geq2\text{ for some }i.
\end{cases}
$$
:::

::: {.proposition}
For every positive integer $n$,
$$
\sum_{d\mid n}\mu(d)=
\begin{cases}
1,&n=1,\\
0,&n>1.
\end{cases}
$$
:::

::: {.proof}
For $n=1$ the sum is $\mu(1)=1$.
If $n>1$ has distinct prime divisors $p_1,\ldots,p_r$, then only squarefree divisors contribute.
Such divisors are indexed by subsets $S\subseteq\theset{1,\ldots,r}$, with contribution $(-1)^{\abs{S}}$.
Hence
$$
\sum_{d\mid n}\mu(d)
=
\sum_{S\subseteq\theset{1,\ldots,r}}(-1)^{\abs{S}}
=(1-1)^r
=0.
$$
:::
