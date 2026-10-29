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

::: {.problem}
Show that for $n\ne6$,
$$
\Aut(S_n)=\Inn(S_n).
$$
:::

::: {.solution}

For $n\le 2$ the group $S_n$ has no nontrivial automorphism, so assume $n\ge3$. Let $\phi\in\Aut(S_n)$ and $s_i=(i\ i+1)$ for $1\le i<n$; the $s_i$ generate $S_n$.

::: pf

::: {.pf-step #transp}

If $n\ne6$, then $\phi$ sends every transposition to a transposition.

::: pf-proof

An automorphism preserves element order and conjugacy-class size, so $\phi(s_1)$ is an involution of cycle type $2^k1^{n-2k}$ whose class size equals that of the transpositions:
$$
\frac{n!}{2^k k!(n-2k)!}=\binom n2 .
$$
For $k\ge2$ this is equivalent to
$$
\frac{(n-2)!}{2^{k-1}k!(n-2k)!}=1.
$$
For $k=2$ it reads $(n-2)(n-3)=8$, which has no integer solution. For $k=3$ it reads $(n-2)(n-3)(n-4)(n-5)=24$, whose unique solution with $n\ge6$ is $n=6$. For $k\ge4$, at the smallest possible $n=2k$ the left side is $\frac{(2k-2)!}{2^{k-1}k!}>1$, and it increases with $n$. Hence $k=1$ when $n\ne6$. All transpositions are conjugate, so the same holds for each of them.

:::

:::

::: {.pf-step #chain}

There are distinct $a_1,\ldots,a_n$ with $\phi(s_i)=(a_i\ a_{i+1})$ for $1\le i<n$.

::: pf-proof

Put $t_i=\phi(s_i)$; by step [](#transp){.pf-ref} each $t_i$ is a transposition. Since $\phi$ preserves orders, $t_it_j$ has order $3$ when $\abs{i-j}=1$ and order $2$ when $\abs{i-j}>1$. Two distinct transpositions have product of order $3$ exactly when their supports meet in one point, and commute exactly when their supports are disjoint. Write $t_1=(a_1\ a_2)$, labelled so that $t_2=(a_2\ a_3)$. For $i\ge3$, $t_i$ meets $t_{i-1}=(a_{i-1}\ a_i)$ in one point and is disjoint from $t_{i-2}\ni a_{i-1}$ and from $t_1,\ldots,t_{i-3}$, so $t_i=(a_i\ a_{i+1})$ with $a_{i+1}\notin\{a_1,\ldots,a_i\}$.

:::

:::

::: pf-step

$\phi$ is inner.

::: pf-proof

Let $\pi\in S_n$ be defined by $\pi(i)=a_i$, with the $a_i$ of step [](#chain){.pf-ref}. Then $\pi s_i\pi^{-1}=(a_i\ a_{i+1})=\phi(s_i)$ for every $i$. Since the $s_i$ generate $S_n$, $\phi(g)=\pi g\pi^{-1}$ for every $g\in S_n$.

:::

:::

:::

:::
