---
schema: qual/card@1
id: P-APAF22D
kind: problem
title: Specht modules in the permutation representation on triples in $\{1,\ldots,10\}$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Permutations
relations: []
review: draft
---

::: problem
Let $X$ be the set of triples $(i, j, k)$ of integers such that $i, j, k \in \{1, \ldots, 10\}$ with the diagonal action of the symmetric group $S_{10}$:
\[
\sigma \cdot (i, j, k) = (\sigma(i), \sigma(j), \sigma(k)).
\]
Let $V$ be the corresponding permutation representation over the complex numbers.
When decomposed into a sum of irreducible representations, which Specht modules appear in $V$ and what are their multiplicities?
:::

::: {.solution}
Partition the set of ordered triples according to their equality pattern.

<1>1. The all-equal triples form one transitive $S_{10}$-orbit isomorphic to $S_{10}/S_9$, the triples with exactly two equal coordinates form three transitive orbits each isomorphic to $S_{10}/S_8$, and the triples with three distinct coordinates form one transitive orbit isomorphic to $S_{10}/S_7$.
::: {.proof}
The all-equal orbit consists of $(i,i,i)$; the stabilizer of $(1,1,1)$ fixes $1$ and is therefore $S_9$.

For triples with exactly two equal entries, the repeated positions are one of $(1,2)$, $(1,3)$, or $(2,3)$, and these patterns are preserved by the diagonal action. For example, the stabilizer of $(1,1,2)$ fixes $1$ and $2$ individually, hence is $S_8$. The same holds for the other two patterns.

For the all-distinct orbit, the stabilizer of $(1,2,3)$ fixes $1,2,3$ individually and is $S_7$.
:::

<1>2. Hence, as a permutation module,
\[
V\cong
\operatorname{Ind}_{S_9}^{S_{10}}\mathbf 1
\oplus 3\operatorname{Ind}_{S_8}^{S_{10}}\mathbf 1
\oplus \operatorname{Ind}_{S_7}^{S_{10}}\mathbf 1,
\]
where $S_9,S_8,S_7$ are understood as the Young subgroups
\[
S_9\times S_1,
\qquad
S_8\times S_1\times S_1,
\qquad
S_7\times S_1\times S_1\times S_1.
\]
::: {.proof}
A transitive permutation representation on $G/H$ is the induced trivial representation $\operatorname{Ind}_H^G\mathbf 1$. Apply this to the five orbits in <1>1 and take their direct sum.
:::

<1>3. Under the Frobenius characteristic map,
\[
\operatorname{ch}(V)
=h_9h_1+3h_8h_1^2+h_7h_1^3.
\]
::: {.proof}
For a Young subgroup $S_{\mu_1}\times\cdots\times S_{\mu_r}$, the Frobenius characteristic of the induced trivial representation is
\[
h_{\mu_1}\cdots h_{\mu_r}.
\]
Apply this to the three summands in <1>2.
:::

<1>4. Repeated application of Pieri's rule gives
\[
\begin{aligned}
h_9h_1&=s_{(10)}+s_{(9,1)},\\
h_8h_1^2
&=s_{(10)}+2s_{(9,1)}+s_{(8,2)}+s_{(8,1,1)},\\
h_7h_1^3
&=s_{(10)}+3s_{(9,1)}+3s_{(8,2)}+3s_{(8,1,1)}\\
&\qquad+s_{(7,3)}+2s_{(7,2,1)}+s_{(7,1,1,1)}.
\end{aligned}
\]
::: {.proof}
Since $h_r=s_{(r)}$, multiplying by $h_1=s_{(1)}$ adds one box to a Young diagram in every possible way, with multiplicity equal to the number of paths through successive one-box additions. Applying this once, twice, and three times to the one-row diagrams $(9)$, $(8)$, and $(7)$ gives the displayed expansions.
:::

<1>5. Therefore
\[
\boxed{
\begin{aligned}
V\cong{}&5S^{(10)}
\oplus10S^{(9,1)}
\oplus6S^{(8,2)}
\oplus6S^{(8,1,1)}\\
&\oplus S^{(7,3)}
\oplus2S^{(7,2,1)}
\oplus S^{(7,1,1,1)}.
\end{aligned}}
\]
::: {.proof}
Substitute the three Pieri expansions from <1>4 into
\[
h_9h_1+3h_8h_1^2+h_7h_1^3
\]
and collect coefficients.

As a consistency check, the dimensions of the three orbit modules are
\[
10+3(10\cdot9)+10\cdot9\cdot8=10+270+720=1000=|X|,
\]
which is the dimension of the original permutation representation.
:::
:::
