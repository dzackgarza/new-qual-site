---
schema: qual/card@1
id: E-SMI-8000E-NR6
kind: problem
title: Unions of chains of proper ideals are proper
classification:
  areas:
  - algebra
  topics:
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the chain-union statement with the local 8000e PDF and extraction, Noetherian-rings problem 6."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Used total ordering to place any two elements in one chain member, and used the identity element to show the union remains proper."
---

::: {.exercise}
If $\ts{I_j}$ is any linearly ordered indexed set of proper ideals in a ring $R$ — i.e. for any two ideals $I_j$ and $I_k$, one is contained in the other — then their union is a proper ideal.
:::


::: {.solution}
Let
$$
J=\bigcup_j I_j.
$$

<1>1. The union $J$ is an ideal of $R$.
::: {.proof}
First, $0\in I_j$ for every $j$, so $0\in J$.

Let $x,y\in J$. Then $x\in I_j$ and $y\in I_k$ for some $j,k$. Because the
family is linearly ordered by inclusion, either
$$
I_j\subseteq I_k
$$
or
$$
I_k\subseteq I_j.
$$
In either case there is one chain member containing both $x$ and $y$. Since
that member is an ideal, it contains
$$
x-y.
$$
Thus $x-y\in J$.

If $r\in R$ and $x\in J$, choose $j$ with $x\in I_j$. Then
$$
rx\in I_j\subseteq J.
$$
Hence $J$ is an ideal.
:::

<1>2. The ideal $J$ is proper.
::: {.proof}
If $J=R$, then in particular
$$
1\in J.
$$
Thus $1\in I_j$ for some $j$, which would imply
$$
I_j=R,
$$
contradicting the hypothesis that every $I_j$ is proper. Therefore
$$
J\ne R.
$$
:::

Hence
$$
\boxed{\bigcup_j I_j\text{ is a proper ideal of }R.}
$$
:::
