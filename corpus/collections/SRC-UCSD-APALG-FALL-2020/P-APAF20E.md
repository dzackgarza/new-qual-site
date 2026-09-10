---
schema: qual/card@1
id: P-APAF20E
kind: problem
title: Irreducible decomposition of square-free cubic monomials under $S_6$, and restriction to $S_5$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let the symmetric group $S_6$ act on the space of complex-coefficient homogeneous polynomials in $x_1,\ldots,x_6$ of degree $3$ by substitution of variables.
Let $V$ be the subspace spanned by $\{x_i x_j x_k\mid 1\le i<j<k\le 6\}$.

(a) What is the decomposition of $V$ into irreducible representations?

(b) Restrict $V$ to $S_5\subset S_6$ (the subgroup of permutations of $\{1,2,3,4,5\}$). Write its character (explicitly, like a row in a character table).
:::

::: {.solution}
<1>1. The $S_6$-module $V$ is the permutation representation on the $3$-element subsets of $\{1,\ldots,6\}$.
::: {.proof}
The basis monomial $x_ix_jx_k$ is determined by the subset $\{i,j,k\}$. Permuting variables sends
\[
x_ix_jx_k\longmapsto x_{\sigma(i)}x_{\sigma(j)}x_{\sigma(k)},
\]
so the action is exactly the permutation action on $3$-subsets.
The stabilizer of $\{1,2,3\}$ is the Young subgroup $S_3\times S_3$, so
\[
V\cong\operatorname{Ind}_{S_3\times S_3}^{S_6}\mathbf 1.
\]
:::

<1>2. The Frobenius characteristic of $V$ is
\[
\operatorname{ch}(V)=s_{(3)}s_{(3)}.
\]
::: {.proof}
Under Frobenius characteristic, induction from $S_3\times S_3$ corresponds to multiplication of symmetric functions. The trivial representation of $S_3$ corresponds to $s_{(3)}=h_3$.
:::

<1>3. By the Pieri rule,
\[
s_{(3)}s_{(3)}
=s_{(6)}+s_{(5,1)}+s_{(4,2)}+s_{(3,3)}.
\]
Hence
\[
\boxed{V\cong S^{(6)}\oplus S^{(5,1)}\oplus S^{(4,2)}\oplus S^{(3,3)}.}
\]
::: {.proof}
Since $s_{(3)}=h_3$, multiplying $s_{(3)}$ by $h_3$ adds a horizontal strip of three boxes to the diagram $(3)$. The possible resulting partitions are exactly
\[
(6),\quad(5,1),\quad(4,2),\quad(3,3),
\]
each with multiplicity one.
Their dimensions are $1,5,9,5$, whose sum is
\[
20=\binom63=\dim V,
\]
which also checks the decomposition.
:::

<1>4. On restriction to $S_5$, the module decomposes as the direct sum of the permutation modules on $3$-subsets and on $2$-subsets of $\{1,\ldots,5\}$.
::: {.proof}
Under the standard embedding $S_5\subset S_6$, the point $6$ is fixed. A $3$-subset of $\{1,\ldots,6\}$ either does not contain $6$, in which case it is a $3$-subset of $\{1,\ldots,5\}$, or it contains $6$, in which case removing $6$ identifies it with a $2$-subset of $\{1,\ldots,5\}$. These two sets are $S_5$-stable.
:::

<1>5. Let $\sigma\in S_5$ have cycle lengths $d_1,\ldots,d_r$. The number of $k$-subsets of $\{1,\ldots,5\}$ fixed by $\sigma$ is the coefficient of $t^k$ in
\[
\prod_{j=1}^r(1+t^{d_j}).
\]
::: {.proof}
A subset is fixed by $\sigma$ exactly when it is a union of cycles of $\sigma$. For each cycle of length $d_j$, one chooses either to exclude the whole cycle or include all $d_j$ of its elements. The generating function for these choices is therefore the displayed product.
:::

<1>6. Thus the character of $V\downarrow_{S_5}^{S_6}$ is
\[
\begin{array}{c|rrrrrrr}
\text{cycle type}&(1^5)&(2,1^3)&(2^2,1)&(3,1^2)&(3,2)&(4,1)&(5)\\ \hline
\chi_{V\downarrow S_5}&20&8&4&2&2&0&0
\end{array}.
\]
::: {.proof}
By <1>4, the character value is the number of fixed $3$-subsets plus the number of fixed $2$-subsets. Using <1>5:
\[
\begin{array}{c|c|c|c}
\text{cycle type}&[t^2]&[t^3]&[t^2]+[t^3]\\ \hline
(1^5)&10&10&20\\
(2,1^3)&4&4&8\\
(2^2,1)&2&2&4\\
(3,1^2)&1&1&2\\
(3,2)&1&1&2\\
(4,1)&0&0&0\\
(5)&0&0&0
\end{array}
\]
for the polynomial $\prod_j(1+t^{d_j})$. This gives the displayed row.
:::
:::
