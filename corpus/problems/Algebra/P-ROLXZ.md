---
schema: qual/card@1
id: P-ROLXZ
kind: problem
title: Kernels of irreducible representations and exactness of induction
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Semisimplicity
  - Exact Sequences
relations: []
review: draft
---

::: {.problem}
Let $H\le G$ and let representations be modules over a commutative coefficient ring $R$.

1. What can be said about the kernel of an irreducible representation of $G$?
2. What is the kernel of a direct sum of representations?
3. Is induction $\operatorname{Ind}_H^G$ left exact, right exact, or exact?
:::

::: {.solution}
Let $\rho:G\to\operatorname{Aut}_R(V)$ be a representation.

<1>1. Its kernel
\[
\ker\rho=\{g\in G:\rho(g)=1_V\}
\]
is a normal subgroup of $G$. If $\rho$ is irreducible, no stronger group-theoretic condition on the kernel holds in general; equivalently, $\rho$ factors through a faithful irreducible representation of $G/\ker\rho$.

<1>2. For representations $\rho_i$,
\[
\ker\Bigl(\bigoplus_i\rho_i\Bigr)=\bigcap_i\ker\rho_i,
\]
because an element acts trivially on the direct sum exactly when it acts trivially on every summand.

<1>3. Induction is
\[
\operatorname{Ind}_H^G(M)=R[G]\otimes_{R[H]}M.
\]
Choose representatives for the right cosets $H\backslash G$. Then $R[G]$ is a free right $R[H]$-module, one copy of $R[H]$ for each right coset. Hence it is flat as a right $R[H]$-module. Tensoring with a flat module is exact, so
\[
\operatorname{Ind}_H^G:R[H]\text{-Mod}\longrightarrow R[G]\text{-Mod}
\]
is exact: it is both left and right exact.
:::
