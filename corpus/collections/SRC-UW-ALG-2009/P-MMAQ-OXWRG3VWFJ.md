---
schema: qual/card@1
id: P-MMAQ-OXWRG3VWFJ
kind: problem
title: Groups of order 2009 and Galois extensions of degree 2009
classification:
  areas:
    - algebra
  topics:
    - Groups
    - Classification
relations: []
review: draft
audit:
  - event: solution-written
    by: OpenAI
    date: 2026-09-10
---

::: {.problem}
(a) Classify groups of order $2009=7^2\times 41$.

(b) Suppose that $F$ is a field and $K/F$ is a Galois extension of degree 2009. How many intermediate fields are there -- that is, how many fields $L$ are there with $F\subset L\subset K$, both inclusions proper?
(There may be several cases to consider.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every group $G$ of order
$$
2009=7^2\cdot41
$$
has a unique Sylow $41$-subgroup.

::: pf-proof

Let $n_{41}$ be the number of Sylow $41$-subgroups. The Sylow theorems give
$$
n_{41}\equiv1\pmod{41},
\qquad
n_{41}\mid49.
$$
The divisors of $49$ are $1,7,49$, and neither $7$ nor $49$ is congruent to $1$ modulo $41$. Hence
$$
n_{41}=1.
$$
Thus the Sylow $41$-subgroup $Q$ is normal. Since $\cardinality{Q}=41$, it is cyclic:
$$
Q\cong C_{41}.
$$

:::

:::

::: {.pf-step #s2}

Every such $G$ also has a unique Sylow $7$-subgroup.

::: pf-proof

Let $n_7$ be the number of Sylow $7$-subgroups. Then
$$
n_7\equiv1\pmod7,
\qquad
n_7\mid41.
$$
Thus $n_7$ is $1$ or $41$. But
$$
41\equiv6\pmod7,
$$
so $41$ is impossible. Hence
$$
n_7=1.
$$
Thus the Sylow $7$-subgroup $P$ is normal and has order $49$.

:::

:::

::: {.pf-step #s3}

The group $G$ is the direct product
$$
G\cong P\times Q.
$$

::: pf-proof

The normal subgroups $P$ and $Q$ have coprime orders, so
$$
P\cap Q=1.
$$
For $p\in P$ and $q\in Q$, the commutator $[p,q]$ lies in $P$ because $P\trianglelefteq G$, and also lies in $Q$ because $Q\trianglelefteq G$. Hence
$$
[p,q]\in P\cap Q=1.
$$
Thus $P$ and $Q$ commute elementwise. Moreover,
$$
\cardinality{PQ}=\frac{\cardinality{P}\cardinality{Q}}{\cardinality{P\cap Q}}=49\cdot41=\cardinality{G},
$$
so $PQ=G$. Therefore $G$ is the internal direct product $P\times Q$.

:::

:::

::: {.pf-step #s4}

Up to isomorphism, there are exactly two possibilities for $P$:
$$
P\cong C_{49}
\qquad\text{or}\qquad
P\cong C_7\times C_7.
$$

::: pf-proof

Every group of order $p^2$ is abelian. Indeed, a nontrivial finite $p$-group has nontrivial center. If $\cardinality{Z(P)}=p^2$, then $P$ is abelian. If $\cardinality{Z(P)}=p$, then $P/Z(P)$ has order $p$ and is cyclic; a group whose quotient by its center is cyclic is abelian, again forcing $Z(P)=P$. Thus $P$ is abelian.

The classification of finite abelian groups of order $7^2$ gives exactly the two possibilities
$$
C_{49}
\qquad\text{and}\qquad
C_7\times C_7.
$$

:::

:::

::: {.pf-step #classification}

Consequently the two groups of order $2009$ are
$$
C_{49}\times C_{41}\cong C_{2009}
$$
and
$$
(C_7\times C_7)\times C_{41}.
$$

::: pf-proof

Combine steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}. Since $49$ and $41$ are coprime, the product of the cyclic groups $C_{49}$ and $C_{41}$ is cyclic of order $2009$.

:::

:::

::: {.pf-step #cyclic-count}

If $G\cong C_{2009}$, then $G$ has exactly $4$ nontrivial proper subgroups.

::: pf-proof

A cyclic group has exactly one subgroup for each positive divisor of its order. Since
$$
2009=7^2\cdot41,
$$
the number of positive divisors is
$$
(2+1)(1+1)=6.
$$
These correspond to subgroup orders
$$
1,\ 7,\ 49,\ 41,\ 7\cdot41,\ 2009.
$$
Removing the trivial subgroup and $G$ itself leaves exactly
$$
6-2=4
$$
nontrivial proper subgroups.

:::

:::

::: {.pf-step #s7}

Let
$$
G=(C_7\times C_7)\times C_{41}.
$$
Every subgroup $H\le G$ has the form
$$
H=A\times B
$$
for uniquely determined subgroups
$$
A\le C_7\times C_7,
\qquad
B\le C_{41}.
$$

::: pf-proof

Let $E=C_7\times C_7$ and $Q=C_{41}$. Any Sylow $7$-subgroup of $H$ consists entirely of elements of $7$-power order, hence lies in $E\times1$. Likewise any Sylow $41$-subgroup of $H$ lies in $1\times Q$.

Since $H$ has order dividing $7^2\cdot41$, its Sylow subgroups have coprime orders and are normal in $H$; indeed the $41$-Sylow subgroup is unique, and the $7$-part is the set of all elements whose $Q$-component is trivial. Thus $H$ is the direct product of its $7$-part and its $41$-part. Writing these as $A\times1$ and $1\times B$ gives
$$
H=A\times B.
$$
The two factors are recovered as intersections with $E\times1$ and $1\times Q$, so they are unique.

:::

:::

::: {.pf-step #s8}

The group $E=C_7\times C_7$ has exactly $10$ subgroups.

::: pf-proof

View $E$ as the $2$-dimensional vector space $\FF_7^2$. Its subgroups are exactly its linear subspaces. There is one zero subspace, one whole space, and the $1$-dimensional subspaces. The number of $1$-dimensional subspaces is
$$
\frac{7^2-1}{7-1}=8,
$$
because there are $7^2-1=48$ nonzero vectors and each line contains $7-1=6$ nonzero vectors. Hence the total number of subgroups is
$$
1+8+1=10.
$$

:::

:::

::: {.pf-step #s9}

The group $C_{41}$ has exactly $2$ subgroups.

::: pf-proof

A group of prime order has only the trivial subgroup and the whole group.

:::

:::

::: {.pf-step #noncyclic-count}

Therefore
$$
(C_7\times C_7)\times C_{41}
$$
has exactly $18$ nontrivial proper subgroups.

::: pf-proof

By steps [](#s7){.pf-ref}, [](#s8){.pf-ref} and [](#s9){.pf-ref}, subgroups correspond bijectively to pairs $(A,B)$ with
$$
A\le C_7\times C_7,
\qquad
B\le C_{41}.
$$
Thus the total number of subgroups is
$$
10\cdot2=20.
$$
Removing the trivial subgroup and $G$ itself leaves
$$
20-2=18
$$
nontrivial proper subgroups.

:::

:::

::: pf-step

Let $K/F$ be Galois of degree $2009$. The number of intermediate fields $F\subsetneq L\subsetneq K$ is $\boxed{4}$ if $\Gal(K/F)$ is cyclic and $\boxed{18}$ if $\Gal(K/F)\cong C_7\times C_7\times C_{41}$.

::: pf-proof

The group $G=\Gal(K/F)$ has order $[K:F]=2009$. By the fundamental theorem of Galois theory, $L\mapsto\Gal(K/L)$ is an inclusion-reversing bijection from intermediate fields of $K/F$ to subgroups of $G$, with $F\mapsto G$ and $K\mapsto1$. So the intermediate fields with both inclusions proper correspond to the subgroups $1\subsetneq H\subsetneq G$.
By step [](#classification){.pf-ref}, $G$ is one of the two groups, and steps [](#cyclic-count){.pf-ref} and [](#noncyclic-count){.pf-ref} count these subgroups.

:::

:::

:::

:::
