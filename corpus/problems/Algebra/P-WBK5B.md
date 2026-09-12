---
schema: qual/card@1
id: P-WBK5B
kind: problem
title: $\Aut(S_n)=\Inn(S_n)$ for $n\neq 6$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Permutations
relations: []
review: draft
---

::: problem
Show that for $n\ne6$,
\[
\operatorname{Aut}(S_n)=\operatorname{Inn}(S_n).
\]
:::

::: solution
For $n=1,2$ the statement is immediate, so assume $n\ge3$.

<1>1. Every automorphism sends transpositions to transpositions when $n\ne6$.

An involution in $S_n$ has cycle type $2^k1^{n-2k}$. Its conjugacy class has size
\[
\frac{n!}{2^k k!(n-2k)!}.
\]
A transposition has class size $\binom n2$. Automorphisms preserve element order and conjugacy-class size, so the image of a transposition must be an involution satisfying
\[
\frac{n!}{2^k k!(n-2k)!}=\binom n2.
\]
For $k\ge2$ this is equivalent to
\[
\frac{(n-2)!}{2^{k-1}k!(n-2k)!}=1.
\]
For $k=2$ there is no integer solution. For $k=3$ the unique solution is $n=6$. For $k\ge4$, already at the smallest possible $n=2k$ the left side is
\[
\frac{(2k-2)!}{2^{k-1}k!}>1,
\]
and it increases with $n$. Thus, when $n\ne6$, necessarily $k=1$.

<1>2. An automorphism preserving transpositions is inner.

Let
\[
s_i=(i\ i+1),\qquad 1\le i<n.
\]
These generate $S_n$. Put $t_i=\phi(s_i)$. Each $t_i$ is a transposition. Moreover,
\[
\operatorname{ord}(t_it_j)=
\operatorname{ord}(s_is_j)
=
\begin{cases}
3,&|i-j|=1,\\
2,&|i-j|>1.
\end{cases}
\]
Two distinct transpositions have product of order $3$ exactly when their supports meet in one point, and they commute exactly when their supports are disjoint.

Write $t_1=(a_1a_2)$. Since $t_2$ meets $t_1$ in exactly one point, after interchanging $a_1,a_2$ if necessary write $t_2=(a_2a_3)$. Inductively, $t_i$ must meet $t_{i-1}$ but be disjoint from $t_1,\ldots,t_{i-2}$, so
\[
t_i=(a_i a_{i+1})
\]
for distinct $a_1,\ldots,a_n$.

Let $\pi\in S_n$ be defined by $\pi(i)=a_i$. Then
\[
\pi s_i\pi^{-1}=t_i=\phi(s_i)
\]
for every $i$. Since the $s_i$ generate $S_n$,
\[
\phi(g)=\pi g\pi^{-1}
\qquad(g\in S_n).
\]
Hence $\phi$ is inner.

Therefore
\[
\operatorname{Aut}(S_n)=\operatorname{Inn}(S_n)
\]
for all $n\ne6$.
:::
