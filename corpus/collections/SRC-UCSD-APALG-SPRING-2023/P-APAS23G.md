---
schema: qual/card@1
id: P-APAS23G
kind: problem
title: $S_5$ on ordered pairs; irreducible decomposition and $\dim \operatorname{End}_{S_5}(\mathbb{C}[X])$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Permutations
relations: []
review: draft
---

::: {.problem}
The symmetric group $S_5$ acts on the set $X$ of ordered pairs $(i, j)$ of (not necessarily distinct!)
elements of $\{1, 2, 3, 4, 5\}$.
Let $\mathbb{C}[X]$ be the associated permutation representation.

(1) Find the decomposition of $\mathbb{C}[X]$ into irreducible $S_5$-modules.

(2) Find the dimension of the endomorphism algebra $\operatorname{End}_{S_5}(\mathbb{C}[X])$.
:::

::: {.solution}
Split $X$ into the two $S_5$-orbits
\[
X_{=}=\{(i,i):1\le i\le5\},
\qquad
X_{\ne}=\{(i,j):i\ne j\}.
\]
Thus
\[
\mathbb C[X]\cong \mathbb C[X_=]\oplus\mathbb C[X_{\ne}].
\]

The diagonal orbit is the natural permutation representation on five points, so
\[
\mathbb C[X_=]\cong S^{(5)}\oplus S^{(4,1)}.
\]

The stabilizer of the ordered pair $(1,2)$ is the subgroup $S_3$ permuting $\{3,4,5\}$, equivalently the Young subgroup $S_3\times S_1\times S_1$. Hence
\[
\mathbb C[X_{\ne}]
\cong
\operatorname{Ind}_{S_3\times S_1\times S_1}^{S_5}\mathbf1.
\]
Under the Frobenius characteristic map this has characteristic
\[
h_3h_1^2=s_{(3)}s_{(1)}^2.
\]
Apply Pieri twice:
\[
s_{(3)}s_{(1)}=s_{(4)}+s_{(3,1)},
\]
so
\[
h_3h_1^2
=s_{(5)}+2s_{(4,1)}+s_{(3,2)}+s_{(3,1,1)}.
\]
Therefore
\[
\boxed{
\mathbb C[X]
\cong
2S^{(5)}\oplus3S^{(4,1)}\oplus S^{(3,2)}\oplus S^{(3,1,1)}.
}
\]
As a dimension check,
\[
2\cdot1+3\cdot4+5+6=25=|X|.
\]

If a semisimple $G$-module decomposes as $\bigoplus_i m_iV_i$ with pairwise nonisomorphic irreducibles $V_i$, then
\[
\operatorname{End}_G(V)\cong\prod_i M_{m_i}(\mathbb C).
\]
Hence
\[
\dim\operatorname{End}_{S_5}(\mathbb C[X])
=2^2+3^2+1^2+1^2
=\boxed{15}.
\]
:::
