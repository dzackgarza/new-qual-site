---
schema: qual/card@1
id: P-UWZPY
kind: problem
title: Induced representations of $G$ from a subgroup $H$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $H$ be a subgroup of a finite group $G$, and let $(\rho, W)$ be a representation of $H$ over $\mathbb{C}$.
How is the induced representation $\operatorname{Ind}_H^G(W)$ defined? State its dimension, character formula (Frobenius formula), and Frobenius Reciprocity.
:::

::: {.solution}
Regard $W$ as a left $\mathbb C[H]$-module. The induced representation is
\[
\operatorname{Ind}_H^G W
=\mathbb C[G]\otimes_{\mathbb C[H]}W,
\]
with $G$ acting by left multiplication on the first factor.

If $g_1,\dots,g_m$ are representatives for the left cosets of $H$ in $G$, then
\[
\mathbb C[G]=\bigoplus_{i=1}^m g_i\mathbb C[H]
\]
as a right $\mathbb C[H]$-module. Hence
\[
\dim\operatorname{Ind}_H^GW=[G:H]\dim W.
\]

If $\chi$ is the character of $W$, extended by $0$ off $H$, then for $g\in G$ the induced character is
\[
\chi_{\operatorname{Ind}}(g)
=\frac1{|H|}\sum_{x\in G}\chi(x^{-1}gx).
\]
Equivalently,
\[
\chi_{\operatorname{Ind}}(g)
=\sum_{\substack{i\\g_i^{-1}gg_i\in H}}
\chi(g_i^{-1}gg_i).
\]

Frobenius reciprocity is the natural adjunction
\[
\operatorname{Hom}_G(\operatorname{Ind}_H^GW,U)
\cong
\operatorname{Hom}_H(W,\operatorname{Res}_H^GU),
\]
and at the character level
\[
\langle\operatorname{Ind}_H^G\chi,\psi\rangle_G
=
\langle\chi,\operatorname{Res}_H^G\psi\rangle_H.
\]
:::
