---
schema: qual/card@1
id: T-AFFCOMM
kind: theorem
title: The affine communication lemma
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Open Covers
  - Schemes
relations:
- kind: uses
  target: D-VKR54
- kind: uses
  target: PR-SCHUNITCOVER
- kind: related-to
  target: D-MORLOCAL
review: draft
prompts:
- State and prove the affine communication lemma.
- Why is integrality not an affine-local property?
---

::: {.theorem title="Affine communication lemma"}
Let $X$ be a scheme and $P$ a property of affine open subschemes of $X$ such that

1. if $\Spec A \subseteq X$ has $P$ and $f \in A$, then $\Spec A_f \subseteq X$ has $P$, and

2. if $\Spec A \subseteq X$ is an affine open, $f_1, \ldots, f_n \in A$ generate the unit ideal, and every $\Spec A_{f_i}$ has $P$, then $\Spec A$ has $P$.

If $X$ has a cover by affine opens $\Spec A_i$ with $P$, then every affine open of $X$ has $P$.
:::

<1>1. Let $U = \Spec A$ and $V = \Spec B$ be affine opens of $X$. Every point $p \in U \cap V$ has an open neighbourhood $W \subseteq U \cap V$ that is distinguished in both: $W = \Spec A_a = \Spec B_b$ for some $a \in A$, $b \in B$.

::: {.proof}
Choose $f \in A$ with $p \in \Spec A_f \subseteq U \cap V$, and then $g \in B$ with $p \in \Spec B_g \subseteq \Spec A_f$.
The restriction of $g$ to the affine scheme $\Spec A_f$ is an element $g' = h / f^m$ of $A_f$ with $h \in A$, and $\Spec B_g$ is the locus in $\Spec A_f$ where $g'$ does not vanish, which is $\Spec (A_f)_{g'} = \Spec A_{fh}$.
So $W = \Spec B_g$ is distinguished in $U$, with $a = fh$, and in $V$, with $b = g$.
:::

<1>2. Every affine open $U = \Spec A$ of $X$ is covered by distinguished opens $\Spec A_a$ that have $P$.

::: {.proof}
Each $p \in U$ lies in some $\Spec A_i$ of the given cover. By step <1>1 there is $W = \Spec A_a = \Spec (A_i)_b$ containing $p$, and $W$ has $P$ by hypothesis 1 applied to $\Spec A_i$.
:::

<1>3. Q.E.D.

::: {.proof}
$U = \Spec A$ is quasicompact, so by step <1>2 it is covered by finitely many $\Spec A_{a_j}$ with $P$.
They cover $\Spec A$, so the $a_j$ generate the unit ideal ([[PR-SCHUNITCOVER]]), and hypothesis 2 gives $P$ for $U$.
:::

::: {.example}
Being Noetherian, and for a scheme over a ring $R$ being of finite type over $R$, satisfy both hypotheses, so they can be checked on one affine cover; so do properties defined on stalks, such as being reduced.
:::

::: {.example}
Integrality does not satisfy hypothesis 2.
For nonzero integral domains $A$ and $B$, the elements $e_1 = (1, 0)$ and $e_2 = (0, 1)$ of $A \times B$ generate the unit ideal, and $(A \times B)_{e_1} \cong A$ and $(A \times B)_{e_2} \cong B$ are integral domains, but $A \times B$ is not, since $e_1 e_2 = 0$.
Geometrically, $\Spec(A \times B) = \Spec A \sqcup \Spec B$ is covered by integral affine opens and is not irreducible.
:::
