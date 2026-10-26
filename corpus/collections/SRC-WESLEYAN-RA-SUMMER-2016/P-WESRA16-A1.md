---
schema: qual/card@1
id: P-WESRA16-A1
kind: problem
title: 'A $[0,1]$-valued measurable function is either essentially an indicator or has a positive-measure middle level set'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Group A, problem A1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Let $f:\mathbb R^d\to[0,1]$ be Lebesgue measurable and set
\[
W_n=\{x:2^{-n}\le f(x)\le1-2^{-n}\}.
\]
Prove that either

1. there is a measurable $X\subset\mathbb R^d$ such that $f=\mathbf1_X$ almost everywhere, or

2. $\lambda(W_n)>0$ for some $n$.
:::

Let
$$
M=\{x\in\mathbb R^d:0<f(x)<1\}.
$$

::: pf

::: pf-step

One has
$$
M=\bigcup_{n=1}^\infty W_n.
$$


::: pf-proof

If $x\in W_n$, then
$$
2^{-n}\leq f(x)\leq1-2^{-n},
$$
so $0<f(x)<1$ and hence $x\in M$.

Conversely, suppose $x\in M$. Then $f(x)>0$ and $1-f(x)>0$. Since $2^{-n}\to0$, there exists $n$ such that
$$
2^{-n}\leq\min\{f(x),1-f(x)\}.
$$
Equivalently,
$$
2^{-n}\leq f(x)\leq1-2^{-n},
$$
so $x\in W_n$.

:::

:::

::: pf-step

If $\lambda(W_n)=0$ for every $n$, then
$$
\lambda(M)=0.
$$


::: pf-proof

By step <1>1 and countable subadditivity,
$$
\lambda(M)
=\lambda\left(\bigcup_{n=1}^\infty W_n\right)
\leq\sum_{n=1}^\infty\lambda(W_n)
=0.
$$

:::

:::

::: pf-step

If $\lambda(W_n)=0$ for every $n$, then there is a measurable set $X\subseteq\mathbb R^d$ such that
$$
f=\mathbf1_X
$$
almost everywhere.


::: pf-proof

Set
$$
X=\{x:f(x)=1\}.
$$
Since $f$ is measurable, $X$ is measurable. Outside the null set $M$ from step <1>2, the value $f(x)$ lies in $[0,1]\setminus(0,1)=\{0,1\}$. Hence for $x\notin M$,
$$
f(x)=1
\quad\Longleftrightarrow\quad
x\in X,
$$
so
$$
f(x)=\mathbf1_X(x).
$$
Thus $f=\mathbf1_X$ almost everywhere.

:::

:::

::: pf-step

One of the two alternatives in the problem always holds.


::: pf-proof

If $\lambda(W_n)>0$ for some $n$, then alternative (2) holds. Otherwise $\lambda(W_n)=0$ for every $n$, and step <1>3 gives alternative (1).

:::

:::

::: pf-qed

Step <1>4 proves the required dichotomy.

:::

:::
