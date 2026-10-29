---
schema: qual/card@1
id: P-GSKRZ
kind: problem
title: Inner automorphisms, and cycle-type-preserving automorphisms of $S_n$ are inner
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Permutations
  - Conjugacy
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---
::: {.problem}
Let $G$ be a group.
An automorphism $\phi: G \rightarrow G$ is called *inner* if the automorphism is given by conjugation by a fixed group element $g$, i.e.,
$$
\phi=\phi_{g}: h \mapsto g h g^{-1} .
$$

a. Prove that the set of inner automorphisms forms a normal subgroup of the group of all automorphisms of $G$.

b. Give an example of a finite group with an automorphism which is not inner.

c. Denote by $S_{n}$ the group of permutations of the set $\{1, \ldots, n\}$.
Suppose that $g \in S_{n}$ sends $i$ to $g_{i}$ for $i=1, \ldots, n .$ Let $(a, b)$ denote as usual the cycle notation for the transposition which permutes $a$ and $b$.
For $i \in\{1, \ldots, n-1\}$, compute $\phi_{g}((i, i+1))$.

d. Suppose that an automorphism $\phi \in \operatorname{Aut}\left(S_{n}\right)$ preserves cycle type, i.e., that for every element $s$ of $S_{n}, s$ and $\phi(s)$ have the same cycle type.
Show that $\phi$ is inner.

> Hint: Consider the images of generators $\phi((1,2)), \phi((2,3)), \cdots, \phi((n-1, n))$.
:::

::: {.solution}
Write $s_i=(i,i+1)$ for $1\leq i<n$.

::: pf

::: {.pf-step #s1}

The inner automorphisms form a normal subgroup $\operatorname{Inn}(G)\trianglelefteq\operatorname{Aut}(G)$.

::: pf-proof

The assignment $g\mapsto(h\mapsto ghg^{-1})$ is a homomorphism $G\to\operatorname{Aut}(G)$ with image $\operatorname{Inn}(G)$. For any $\psi\in\operatorname{Aut}(G)$ one has $\psi\phi_g\psi^{-1}=\phi_{\psi(g)}$, so the image is normal.

:::

:::

::: {.pf-step #s2}

The inversion map on $C_3$ is a non-inner automorphism.

::: pf-proof

Inversion is an automorphism of the cyclic group $C_3$ and is nontrivial. Because $C_3$ is abelian, all of its inner automorphisms are trivial.

:::

:::

::: {.pf-step #s3}

For $g\in S_n$,
$$
\boxed{\phi_g(s_i)=(g(i),g(i+1))}.
$$

::: pf-proof

For every $j$, the permutation $gs_ig^{-1}$ swaps $g(i)$ with $g(i+1)$ and fixes the other points. Hence it is the displayed transposition.

:::

:::

::: {.pf-step #s4}

Every cycle-type-preserving automorphism $\phi$ of $S_n$ is inner.

::: pf-proof

The cases $n\leq2$ are immediate because $S_n$ is trivial or cyclic of order two, with trivial automorphism group. Suppose $n\geq3$. Write $t_i=\phi(s_i)$. Each $t_i$ is a transposition by cycle-type preservation. Since $\phi$ is an automorphism, the $t_i$ are distinct and generate $S_n$. The elements $s_i,s_j$ commute exactly when $|i-j|>1$, while $s_is_{i+1}$ has order three. Accordingly, the $t_i$ and $t_j$ have disjoint supports when $|i-j|>1$, whereas consecutive $t_i,t_{i+1}$ have supports intersecting in exactly one point.

For $n\geq4$, consider $t_1$ and $t_2$. Their supports share a point, which can be named $a_2$; write $t_1=(a_1,a_2)$ and $t_2=(a_2,a_3)$ with three distinct points. Since $t_3$ meets the support of $t_2$ but is disjoint from the support of $t_1$, it contains $a_3$ and another point $a_4$ distinct from $a_1,a_2,a_3$. Proceed inductively: if $t_j=(a_j,a_{j+1})$ for $1\leq j<i$, then $t_i$ meets the support of $t_{i-1}$ but is disjoint from every $t_j$ with $j\leq i-2$. In particular, $t_i$ contains $a_i$ rather than $a_{i-1}$ and its second point $a_{i+1}$ is distinct from every previously chosen point (otherwise $t_i$ would meet some earlier nonconsecutive $t_j$). Thus $t_i=(a_i,a_{i+1})$, with all $a_j$ distinct. When $n=3$, the same conclusion follows already from the pair $t_1,t_2$.

There are $n$ distinct elements $a_1,\ldots,a_n$ of $\{1,\ldots,n\}$, so they define a permutation $g$ with $g(i)=a_i$. By step [](#s3){.pf-ref}, $\phi_g(s_i)=(a_i,a_{i+1})=\phi(s_i)$ for every $i$. The adjacent transpositions generate $S_n$, hence $\phi=\phi_g$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} establish parts (a)--(d), respectively.

:::

:::

:::
