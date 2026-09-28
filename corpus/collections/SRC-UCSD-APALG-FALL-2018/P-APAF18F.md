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
<1>1. Under the Frobenius characteristic map,
\[
\operatorname{ch}(V)=s_{(3)}s_{(1,1,1)}s_{(1)}.
\]
::: {.proof}
For symmetric groups, induction from a Young subgroup corresponds under the Frobenius characteristic map to multiplication of Schur functions. The three factors of the inducing representation have characteristics $s_{(3)}$, $s_{(1,1,1)}$, and $s_{(1)}$, respectively.
:::

<1>2. One has
\[
s_{(3)}s_{(1,1,1)}=s_{(4,1,1)}+s_{(3,1,1,1)}.
\]
::: {.proof}
Since $s_{(1,1,1)}=e_3$, the vertical-strip Pieri rule says that $s_{(3)}e_3$ is the sum of $s_\mu$ over partitions $\mu$ obtained from $(3)$ by adding three boxes with no two in the same row. There are exactly two possibilities:
\[
(4,1,1),\qquad (3,1,1,1).
\]
Each occurs with multiplicity one.
:::

<1>3. Multiplication by $s_{(1)}=h_1$ gives
\[
\begin{aligned}
s_{(4,1,1)}s_{(1)}
&=s_{(5,1,1)}+s_{(4,2,1)}+s_{(4,1,1,1)},\\
s_{(3,1,1,1)}s_{(1)}
&=s_{(4,1,1,1)}+s_{(3,2,1,1)}+s_{(3,1,1,1,1)}.
\end{aligned}
\]
::: {.proof}
The one-box Pieri rule says that multiplying by $h_1$ adds one box in every possible way that still gives a partition. For $(4,1,1)$ the three distinct resulting partitions are $(5,1,1)$, $(4,2,1)$, and $(4,1,1,1)$. For $(3,1,1,1)$ they are $(4,1,1,1)$, $(3,2,1,1)$, and $(3,1,1,1,1)$.
:::

<1>4. Therefore
\[
\boxed{
V\cong
S^{(5,1,1)}
\oplus S^{(4,2,1)}
\oplus 2S^{(4,1,1,1)}
\oplus S^{(3,2,1,1)}
\oplus S^{(3,1,1,1,1)}.}
\]
::: {.proof}
Combine <1>1--<1>3 and collect the repeated summand $s_{(4,1,1,1)}$, which appears once from each Pieri expansion.
:::

<1>5. The endomorphism algebra has dimension
\[
\boxed{\dim_{\mathbb C}\operatorname{End}_{S_7}(V)=8}.
\]
::: {.proof}
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
By <1>4 the multiplicities are $1,1,2,1,1$, hence
\[
1^2+1^2+2^2+1^2+1^2=8.
\]
:::
:::
