---
schema: qual/card@1
id: P-WVWEP
kind: problem
title: $|\GL_2(\FF_q)|$ and its representations
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Finite Fields
  - Representation Theory
relations: []
review: draft
---

::: {.problem}
Let $G=\GL_2(\FF_q)$.

(a) Compute $|G|$.

(b) Describe standard ways to construct finite-dimensional complex representations of $G$.

(c) Determine the one-dimensional complex representations of $G$.

(d) State the corresponding simplicity theorem for $\PSL_2(\FF_q)$.
:::

::: {.solution}

::: pf

::: pf-step

(a) $|\GL_2(\FF_q)|=\boxed{(q^2-1)(q^2-q)=q(q-1)^2(q+1)}$.

::: pf-proof

A matrix is invertible exactly when its columns form a basis of $\FF_q^2$. The first column can be any nonzero vector, giving $q^2-1$ choices, and the second column can be any vector outside the span of the first, giving $q^2-q$ choices.

:::

:::

::: pf-step

(b) Complex representations of $G$ arise from permutation representations of $G$-sets, the regular representation, induction from subgroups such as the Borel subgroup and the split and nonsplit tori, tensor products, duals, and the irreducible constituents of these.

::: pf-proof

The natural action on $\FF_q^2$ is a representation over $\FF_q$, not over $\CC$, since a field of characteristic $p$ does not embed in $\CC$. A finite $G$-set $X$ instead gives the complex permutation representation $\CC[X]$. For example, $G$ acts on the projective line $\PP^1(\FF_q)$, which has $q+1$ points, and $\CC[\PP^1(\FF_q)]$ is the sum of the trivial representation and the $q$-dimensional Steinberg representation.

:::

:::

::: pf-step

(c) For $q>2$ the one-dimensional complex representations are the $q-1$ maps $\chi\circ\det$ with $\chi:\FF_q^\times\to\CC^\times$ a character; for $q=2$ there are two.

::: pf-proof

A one-dimensional representation factors through the abelianization. For $q>2$, the commutator subgroup of $\GL_2(\FF_q)$ is $\SL_2(\FF_q)$, so $\det$ induces $\GL_2(\FF_q)^{\mathrm{ab}}\cong\FF_q^\times$. Since $\FF_q^\times$ is cyclic of order $q-1$, it has exactly $q-1$ complex characters. For $q=2$, $\GL_2(\FF_2)\cong S_3$ has abelianization $C_2$, which has two characters.

:::

:::

::: pf-step

(d) $\PSL_2(\FF_q)$ is simple for $q\ge4$; the exceptions are $\PSL_2(\FF_2)\cong S_3$ and $\PSL_2(\FF_3)\cong A_4$.

::: pf-proof

This is the standard simplicity theorem for $\PSL_2$. For example, $\PSL_2(\FF_4)\cong A_5$.

:::

:::

:::

:::
