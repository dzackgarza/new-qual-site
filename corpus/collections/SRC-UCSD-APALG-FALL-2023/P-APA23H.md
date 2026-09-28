---
schema: qual/card@1
id: P-APA23H
kind: problem
title: Irreducible decomposition of homogeneous quadrics under $S_5$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
---

::: {.problem}
Let $V$ be the vector space of polynomials $f(x_1, x_2, x_3, x_4, x_5)$ in $5$ variables $\{x_1, \dots, x_5\}$ of homogeneous degree $2$ with complex coefficients.
The symmetric group $S_5$ acts on $V$ by variable permutation.
Find the decomposition of $V$ into $S_5$-irreducibles.
:::

::: {.solution}
Let
\[
V_{\mathrm{sq}}=\operatorname{span}\{x_1^2,\ldots,x_5^2\},
\qquad
V_{\mathrm{sf}}=\operatorname{span}\{x_ix_j:1\le i<j\le5\}.
\]
Then
\[
V=V_{\mathrm{sq}}\oplus V_{\mathrm{sf}}.
\]

<1>1. Both summands are $S_5$-subrepresentations.
::: {.proof}
A permutation of the variables sends a square $x_i^2$ to another square and sends a square-free quadratic monomial $x_ix_j$ with $i\ne j$ to another square-free quadratic monomial. Hence both spans are stable under $S_5$.
Their bases are disjoint subsets of the standard monomial basis of the degree-$2$ homogeneous polynomials, so the sum is direct and equals all of $V$.
:::

<1>2. The square submodule is
\[
V_{\mathrm{sq}}\cong\operatorname{Ind}_{S_4\times S_1}^{S_5}\mathbf1,
\]
so
\[
V_{\mathrm{sq}}\cong S^{(5)}\oplus S^{(4,1)}.
\]
::: {.proof}
The action on the basis $\{x_i^2\}$ is the permutation action on the five points $\{1,\ldots,5\}$. The stabilizer of $x_1^2$ is $S_4\times S_1$, so the permutation module is the indicated induced trivial module.
Under the Frobenius characteristic map its character is
\[
h_4h_1.
\]
Since $h_4=s_{(4)}$, Pieri's rule gives
\[
h_4h_1=s_{(5)}+s_{(4,1)}.
\]
:::

<1>3. The square-free submodule is
\[
V_{\mathrm{sf}}\cong\operatorname{Ind}_{S_3\times S_2}^{S_5}\mathbf1,
\]
so
\[
V_{\mathrm{sf}}\cong S^{(5)}\oplus S^{(4,1)}\oplus S^{(3,2)}.
\]
::: {.proof}
The basis vectors $x_ix_j$ with $i<j$ are indexed by the $2$-element subsets of $\{1,\ldots,5\}$. This action is transitive, and the stabilizer of $\{1,2\}$ is $S_2\times S_3$. Thus the Frobenius characteristic is
\[
h_3h_2=s_{(3)}h_2.
\]
By Pieri's rule, multiplying $s_{(3)}$ by $h_2$ adds a horizontal $2$-strip. The possible resulting partitions are
\[
(5),\qquad(4,1),\qquad(3,2),
\]
each with coefficient $1$.
:::

<1>4. Therefore
\[
\boxed{V\cong 2S^{(5)}\oplus2S^{(4,1)}\oplus S^{(3,2)}.}
\]
::: {.proof}
Combine the decompositions in <1>2 and <1>3.
As a dimension check,
\[
2\cdot1+2\cdot4+5=15=\dim V=\binom{5+2-1}{2}.
\]
:::
:::
