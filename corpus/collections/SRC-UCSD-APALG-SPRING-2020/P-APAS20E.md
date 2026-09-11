---
schema: qual/card@1
id: P-APAS20E
kind: problem
title: Permutation representations of $S_7$ on $4$-subsets and ordered complements
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Permutations
  - Symmetric Functions
relations: []
review: draft
---

::: problem
(a) Let $X$ be the set of $4$-element subsets of $\{1,\ldots,7\}$ with the action of the symmetric group $S_7$ via permuting values.
What is the decomposition of the permutation representation $\mathbb{C}[X]$ into irreducible representations?

(b) Let $Y$ be the set of pairs $(S,\sigma)$ where $S$ is a $4$-element subset of $\{1,\ldots,7\}$ and $\sigma$ is an ordering of $\{1,\ldots,7\}\setminus S$, again with the action of the symmetric group $S_7$ via permuting values.
What is the decomposition of the permutation representation $\mathbb{C}[Y]$ into irreducible representations?

(c) Explain what computation regarding polynomial functors the above two problems can be used to solve.
:::

::: solution
For (a), the action of \(S_7\) on \(4\)-element subsets is transitive. The stabilizer of \(\{1,2,3,4\}\) is the Young subgroup \(S_4\times S_3\). Hence
\[
\mathbb C[X]\cong \operatorname{Ind}_{S_4\times S_3}^{S_7}\mathbf1.
\]
Under the Frobenius characteristic map,
\[
\operatorname{ch}\mathbb C[X]=h_4h_3=s_{(4)}s_{(3)}.
\]
By Pieri's rule,
\[
h_4h_3=s_{(7)}+s_{(6,1)}+s_{(5,2)}+s_{(4,3)}.
\]
Therefore
\[
\boxed{\mathbb C[X]\cong
S^{(7)}\oplus S^{(6,1)}\oplus S^{(5,2)}\oplus S^{(4,3)}.}
\]
The dimensions \(1+6+14+14=35\) agree with \(|X|=\binom74=35\).

For (b), fixing a \(4\)-set and an ordering of its \(3\)-element complement leaves only the permutations of the \(4\)-set. Thus the stabilizer of a point of \(Y\) is \(S_4\times S_1\times S_1\times S_1\), and
\[
\mathbb C[Y]\cong
\operatorname{Ind}_{S_4\times S_1^3}^{S_7}\mathbf1.
\]
Hence
\[
\operatorname{ch}\mathbb C[Y]=h_4h_1^3=s_{(4)}s_{(1)}^3.
\]
Applying Pieri's rule three times gives
\[
\begin{aligned}
h_4h_1^3={}&s_{(7)}+3s_{(6,1)}+3s_{(5,2)}+3s_{(5,1,1)}\\
&+s_{(4,3)}+2s_{(4,2,1)}+s_{(4,1,1,1)}.
\end{aligned}
\]
Therefore
\[
\boxed{\begin{aligned}
\mathbb C[Y]\cong{}&S^{(7)}\oplus3S^{(6,1)}\oplus3S^{(5,2)}\oplus3S^{(5,1,1)}\\
&\oplus S^{(4,3)}\oplus2S^{(4,2,1)}\oplus S^{(4,1,1,1)}.
\end{aligned}}
\]
The total dimension is \(210=35\cdot3!=|Y|\).

For (c), multiplication of Frobenius characteristics records tensor products of homogeneous polynomial functors. Thus the decomposition in (a), namely the Schur expansion of \(h_4h_3\), gives the decomposition
\[
\operatorname{Sym}^4\otimes\operatorname{Sym}^3
\cong
\mathbb S_{(7)}\oplus\mathbb S_{(6,1)}\oplus\mathbb S_{(5,2)}\oplus\mathbb S_{(4,3)}
\]
in sufficiently large vector-space dimension. Likewise the decomposition in (b), the Schur expansion of \(h_4h_1^3\), computes the irreducible Schur-functor decomposition of
\[
\operatorname{Sym}^4\otimes (\mathrm{Id})^{\otimes3}.
\]
Thus the two permutation-representation calculations determine these polynomial-functor decompositions.
:::
