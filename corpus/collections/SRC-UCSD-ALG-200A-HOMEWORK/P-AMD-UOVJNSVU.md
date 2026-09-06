---
schema: qual/card@1
id: P-AMD-UOVJNSVU
kind: problem
title: Splitting of conjugacy classes of $S_n$ under $A_n$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Permutations
  - Group Actions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 3, Exercise 2. Restored
    both parts of the source statement, including n >= 3 and the criterion in
    terms of the complete disjoint-cycle length list, including 1-cycles.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Identified splitting with C_{S_n}(sigma) being contained in A_n. An even
    cycle or a repeated odd cycle supplies an odd centralizer element; when all
    cycle lengths are odd and distinct, every centralizer element preserves
    each cycle support and restricts there to a power of an odd cycle, hence is
    even.
---

::: {.problem}
Let $n\ge3$, and let $\mathcal K$ be a conjugacy class in $S_n$.
Restrict the conjugation action of $S_n$ on itself to the subgroup $A_n$.

1. Show that either $\mathcal K$ is a single $A_n$-orbit, or $\mathcal K$ is the union of two $A_n$-orbits of equal size.

2. Suppose the disjoint-cycle type of $\mathcal K$ has cycle lengths
   \[
   k_1,\ldots,k_d,
   \]
   including $1$-cycles.
   Show that the second case occurs if and only if the integers $k_1,\ldots,k_d$ are odd and pairwise distinct.
:::

::: {.solution}
Fix $\sigma\in\mathcal K$, and write
\[
C=C_{S_n}(\sigma)
\]
for its centralizer in $S_n$.

<1>1. The set of $A_n$-orbits contained in $\mathcal K$ is a transitive $S_n$-set.
::: {.proof}
The group $S_n$ acts transitively on $\mathcal K$ by conjugation, and $A_n\normal S_n$.
If $\mathcal O$ is an $A_n$-orbit in $\mathcal K$ and $g\in S_n$, then normality gives
\[
g\mathcal O
=g(A_n\cdot\tau)
=(gA_ng^{-1})\cdot(g\tau g^{-1})
=A_n\cdot(g\tau g^{-1}),
\]
which is again an $A_n$-orbit.
Because the original $S_n$-action on $\mathcal K$ is transitive, this induced action on the set of $A_n$-orbits is also transitive.
:::

<1>2. The stabilizer in $S_n$ of the $A_n$-orbit $A_n\cdot\sigma$ is $A_nC$.
::: {.proof}
For $g\in S_n$,
\[
g(A_n\cdot\sigma)=A_n\cdot\sigma
\]
if and only if
\[
g\sigma g^{-1}=a\sigma a^{-1}
\]
for some $a\in A_n$.
This is equivalent to
\[
a^{-1}g\in C,
\]
or equivalently $g\in A_nC$.
Since $A_n\normal S_n$, the product $A_nC$ is a subgroup.
:::

<1>3. The class $\mathcal K$ is either one $A_n$-orbit or two $A_n$-orbits of equal size.
::: {.proof}
By <1>1 and <1>2, the number of $A_n$-orbits in $\mathcal K$ is
\[
[S_n:A_nC].
\]
Because $[S_n:A_n]=2$ and
\[
A_n\le A_nC\le S_n,
\]
this index is either $1$ or $2$.

If there are two orbits, <1>1 says an element of $S_n$ carries either orbit bijectively onto the other by conjugation.
Hence the two orbits have equal cardinality.
:::

<1>4. The class $\mathcal K$ splits into two $A_n$-orbits if and only if
\[
C\le A_n.
\]
::: {.proof}
By <1>3, splitting occurs exactly when
\[
[S_n:A_nC]=2,
\]
that is, exactly when
\[
A_nC=A_n.
\]
This is equivalent to $C\le A_n$.
:::

<1>5. If the cycle type of $\sigma$ contains an even cycle length, then $C$ contains an odd permutation.
::: {.proof}
Let $c$ be an even-length cycle occurring in the disjoint-cycle decomposition of $\sigma$.
Since the cycles in that decomposition are disjoint, $c$ commutes with $\sigma$, so
\[
c\in C.
\]
A cycle of length $k$ has sign $(-1)^{k-1}$.
For even $k$, this sign is $-1$, so $c$ is odd.
:::

<1>6. If an odd cycle length occurs at least twice, then $C$ contains an odd permutation.
::: {.proof}
Suppose two cycles of the same odd length $k$ occur:
\[
c=(a_1\ a_2\ \cdots\ a_k),
\qquad
d=(b_1\ b_2\ \cdots\ b_k).
\]
Define
\[
\tau=(a_1\ b_1)(a_2\ b_2)\cdots(a_k\ b_k).
\]
Then conjugation by $\tau$ interchanges $c$ and $d$ and fixes every other disjoint cycle of $\sigma$.
Hence
\[
\tau\sigma\tau^{-1}=\sigma,
\]
so $\tau\in C$.

The permutation $\tau$ is a product of $k$ disjoint transpositions.
Since $k$ is odd, $\tau$ is odd.
:::

<1>7. If $C\le A_n$, then all cycle lengths of $\sigma$ are odd and pairwise distinct.
::: {.proof}
If an even cycle length occurred, <1>5 would give an odd element of $C$.
Thus every cycle length is odd.

If a cycle length were repeated, it would therefore be a repeated odd length, and <1>6 would again give an odd element of $C$.
Hence the cycle lengths are pairwise distinct.
:::

<1>8. Suppose all cycle lengths of $\sigma$ are odd and pairwise distinct.
Then every element of $C$ preserves the support of each cycle of $\sigma$.
::: {.proof}
Let $\tau\in C$, and let $x$ lie in a cycle of $\sigma$ of length $k$.
Because $\tau\sigma=\sigma\tau$,
\[
\tau(\sigma^m x)=\sigma^m\tau(x)
\]
for every integer $m$.
Thus $\tau$ carries the $\sigma$-orbit of $x$ bijectively onto the $\sigma$-orbit of $\tau(x)$, preserving its cardinality $k$.

There is only one cycle of length $k$, by hypothesis.
Therefore $\tau(x)$ lies in the same cycle support as $x$.
Hence every cycle support is invariant under $\tau$.
:::

<1>9. Under the hypotheses of <1>8, every element of $C$ is even.
::: {.proof}
Let
\[
\sigma=c_1c_2\cdots c_d
\]
be its disjoint-cycle decomposition, where $c_i$ has odd length $k_i$.
By <1>8, any $\tau\in C$ preserves the support of every $c_i$.

On the support of a single cycle $c_i$, any permutation commuting with $c_i$ is a power of $c_i$.
Indeed, if $x$ is one point of that support and
\[
\tau(x)=c_i^r(x),
\]
then for every $m$,
\[
\tau(c_i^m x)=c_i^m\tau(x)=c_i^{m+r}x,
\]
so $\tau=c_i^r$ on that support.

Therefore $\tau$ is a product of powers of the disjoint cycles $c_i$.
Each $c_i$ is even because $k_i$ is odd, and hence every power of $c_i$ is even.
Thus $\tau$ is even.
Consequently
\[
C\le A_n.
\]
:::

<1>10. The class $\mathcal K$ splits into two equal $A_n$-orbits if and only if its cycle lengths are odd and pairwise distinct.
::: {.proof}
By <1>4, splitting is equivalent to $C\le A_n$.
Step <1>7 proves that this condition forces all cycle lengths to be odd and pairwise distinct, while <1>9 proves the converse.
:::
:::
