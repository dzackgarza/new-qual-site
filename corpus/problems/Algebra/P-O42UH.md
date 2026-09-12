---
schema: qual/card@1
id: P-O42UH
kind: problem
title: Groups of order 21
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
---

::: problem
Classify groups of order $21$ up to isomorphism.
:::

::: {.solution}
Let $|G|=21=3\cdot7$.

<1>1. The Sylow $7$-subgroup is normal.
::: {.proof}
If $n_7$ is the number of Sylow $7$-subgroups, then
\[
n_7\equiv1\pmod7,\qquad n_7\mid3.
\]
Hence $n_7=1$. Write this subgroup as $P\cong C_7$.
:::

<1>2. Every such group is a semidirect product $C_7\rtimes C_3$.
::: {.proof}
Let $Q$ be a Sylow $3$-subgroup. Then $Q\cong C_3$, $P\cap Q=1$, and $|PQ|=21$, so
\[
G\cong P\rtimes Q.
\]
The action is a homomorphism
\[
C_3\longrightarrow \operatorname{Aut}(C_7)\cong C_6.
\]
:::

<1>3. There are exactly two isomorphism types.
::: {.proof}
The action is either trivial or has image the unique subgroup of order $3$ in $C_6$.

For the trivial action,
\[
G\cong C_7\times C_3\cong C_{21}.
\]
For a nontrivial action, choose generators $a$ of $C_7$ and $b$ of $C_3$. Up to replacing $b$ by $b^{-1}$, the action is
\[
bab^{-1}=a^2,
\]
since $2$ has order $3$ modulo $7$. Thus the unique nonabelian isomorphism type has presentation
\[
\langle a,b\mid a^7=b^3=1,\ bab^{-1}=a^2\rangle.
\]
The two possible nontrivial embeddings $C_3\hookrightarrow C_6$ differ by an automorphism of $C_3$, so they give isomorphic semidirect products.
:::

Therefore exactly two groups of order $21$ exist up to isomorphism: $C_{21}$ and the nonabelian group $C_7\rtimes C_3$.
:::
