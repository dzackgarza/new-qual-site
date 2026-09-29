---
schema: qual/card@1
id: P-APAF18F
kind: problem
title: Induced Specht module from $S_3\times S_3\times S_1$ in $S_7$
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

::: {.problem}
For a partition $\lambda\vdash n$, let $S^\lambda$ be the corresponding irreducible $S_n$-module.
Let $H=S_3\times S_3\times S_1$, so that $H$ is a subgroup of $S_7$.
Let $V$ be the induced representation
\[
V=\bigl(S^{(3)}\otimes S^{(1,1,1)}\otimes S^{(1)}\bigr)\uparrow_H^{S_7}.
\]

(a) Find the decomposition of $V$ into irreducible $S_7$-modules.

(b) What is the dimension of the endomorphism ring $\operatorname{End}_{S_7}(V)$?
:::

::: {.solution}

::: pf

::: {.pf-step #frobenius-characteristic-of-induction}
Under the Frobenius characteristic map,
\[
\operatorname{ch}(V)=s_{(3)}s_{(1,1,1)}s_{(1)}.
\]

::: pf-proof
For symmetric groups, induction from a Young subgroup corresponds under the Frobenius characteristic map to multiplication of Schur functions. The three factors of the inducing representation have characteristics $s_{(3)}$, $s_{(1,1,1)}$, and $s_{(1)}$, respectively.
:::

:::

::: {.pf-step #pieri-product-of-first-two}
One has
\[
s_{(3)}s_{(1,1,1)}=s_{(4,1,1)}+s_{(3,1,1,1)}.
\]

::: pf-proof
Since $s_{(1,1,1)}=e_3$, the vertical-strip Pieri rule says that $s_{(3)}e_3$ is the sum of $s_\mu$ over partitions $\mu$ obtained from $(3)$ by adding three boxes with no two in the same row. There are exactly two possibilities:
\[
(4,1,1),\qquad (3,1,1,1).
\]
Each occurs with multiplicity one.
:::

:::

::: {.pf-step #pieri-product-with-h1}
Multiplication by $s_{(1)}=h_1$ gives
\[
\begin{aligned}
s_{(4,1,1)}s_{(1)}
&=s_{(5,1,1)}+s_{(4,2,1)}+s_{(4,1,1,1)},\\
s_{(3,1,1,1)}s_{(1)}
&=s_{(4,1,1,1)}+s_{(3,2,1,1)}+s_{(3,1,1,1,1)}.
\end{aligned}
\]

::: pf-proof
The one-box Pieri rule says that multiplying by $h_1$ adds one box in every possible way that still gives a partition. For $(4,1,1)$ the three distinct resulting partitions are $(5,1,1)$, $(4,2,1)$, and $(4,1,1,1)$. For $(3,1,1,1)$ they are $(4,1,1,1)$, $(3,2,1,1)$, and $(3,1,1,1,1)$.
:::

:::

::: {.pf-step #decomposition-of-v}
Therefore
\[
\boxed{
V\cong
S^{(5,1,1)}
\oplus S^{(4,2,1)}
\oplus 2S^{(4,1,1,1)}
\oplus S^{(3,2,1,1)}
\oplus S^{(3,1,1,1,1)}.}
\]

::: pf-proof
Combine steps [](#frobenius-characteristic-of-induction){.pf-ref}, [](#pieri-product-of-first-two){.pf-ref} and [](#pieri-product-with-h1){.pf-ref} and collect the repeated summand $s_{(4,1,1,1)}$, which appears once from each Pieri expansion.
:::

:::

::: {.pf-step #dimension-of-endomorphism-ring}
The endomorphism algebra has dimension
\[
\boxed{\dim_{\mathbb C}\operatorname{End}_{S_7}(V)=8}.
\]

::: pf-proof
Over $\mathbb C$, $S_7$-representations are semisimple. If
\[
V\cong\bigoplus_\lambda m_\lambda S^\lambda,
\]
with pairwise nonisomorphic irreducibles $S^\lambda$, then Schur's lemma gives
\[
\operatorname{End}_{S_7}(V)
\cong\bigoplus_\lambda M_{m_\lambda}(\mathbb C),
\]
so
\[
\dim\operatorname{End}_{S_7}(V)=\sum_\lambda m_\lambda^2.
\]
By step [](#decomposition-of-v){.pf-ref} the multiplicities are $1,1,2,1,1$, hence
\[
1^2+1^2+2^2+1^2+1^2=8.
\]
:::

:::

::: pf-qed
Steps [](#decomposition-of-v){.pf-ref} and [](#dimension-of-endomorphism-ring){.pf-ref} answer parts (a) and (b).
:::

:::

:::
