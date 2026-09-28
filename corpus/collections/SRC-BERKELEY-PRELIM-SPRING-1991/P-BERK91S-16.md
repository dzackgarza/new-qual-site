---
schema: qual/card@1
id: P-BERK91S-16
kind: problem
title: A unipotent complex operator is similar to its inverse
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $A$ be a linear transformation on an $n$-dimensional complex vector space with characteristic polynomial
\[
(x-1)^n.
\]
Prove that $A$ is similar to $A^{-1}$.
:::

::: {.solution}
Put $N\coloneqq A-I$ and $M\coloneqq A^{-1}-I$.

<1>1. For every integer $k\ge 1$,
$$
\ker M^k=\ker N^k.
$$

::: {.proof}
The characteristic polynomial of $N$ is $x^n$, so the
Cayley--Hamilton theorem gives $N^n=0$. Thus $A=I+N$ is invertible.
Moreover,
$$
M=A^{-1}-I=-A^{-1}(A-I)=-A^{-1}N.
$$
Since $A^{-1}$ commutes with $N$, for every $k\ge1$,
$$
M^k=(-1)^kA^{-k}N^k.
$$
The operator $A^{-k}$ is invertible, so $M^kv=0$ if and only if
$N^kv=0$. Hence the kernels are equal.
:::

<1>2. The nilpotent operators $N$ and $M$ are similar.

::: {.proof}
Step <1>1 with $k=n$ shows that $M^n=0$, so both operators are
nilpotent. For a nilpotent operator $T$, if
$d_k\coloneqq\dim\ker T^k$ and $d_0\coloneqq0$, then
$d_k-d_{k-1}$ is the number of Jordan blocks of $T$ having size at
least $k$. Thus the sequence of dimensions
$\dim\ker T^k$ determines the multiset of nilpotent Jordan-block
sizes. Step <1>1 gives the same sequence for $N$ and $M$, so they have
the same Jordan form and are similar.
:::

<1>3. $A$ is similar to $A^{-1}$.

::: {.proof}
By step <1>2 there is an invertible linear map $S$ such that
$S^{-1}NS=M$. Therefore
$$
S^{-1}AS
=S^{-1}(I+N)S
=I+M
=A^{-1}.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required similarity.
:::
:::
