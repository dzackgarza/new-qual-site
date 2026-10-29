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
Let $H$ be a subgroup of a finite group $G$, and let $(\rho, W)$ be a representation of $H$ over $\CC$.
How is the induced representation $\operatorname{Ind}_H^G(W)$ defined? State its dimension, character formula (Frobenius formula), and Frobenius Reciprocity.
:::

::: {.solution}
Regard $W$ as a left $\CC[H]$-module, and let $g_1,\ldots,g_m$ be representatives for the left cosets of $H$ in $G$.

::: pf

::: pf-step
The induced representation is
$$
\operatorname{Ind}_H^G W
=\CC[G]\otimes_{\CC[H]}W,
$$
with $G$ acting by left multiplication on the first factor.

::: pf-proof
This is the definition.
:::

:::

::: pf-step
$\dim\operatorname{Ind}_H^GW=[G:H]\dim W$.

::: pf-proof
As a right $\CC[H]$-module,
$$
\CC[G]=\bigoplus_{i=1}^m g_i\CC[H],
$$
so $\CC[G]\otimes_{\CC[H]}W=\bigoplus_{i=1}^m g_i\otimes W$ has dimension $m\dim W=[G:H]\dim W$.
:::

:::

::: pf-step
If $\chi$ is the character of $W$, extended by $0$ off $H$, then for $g\in G$
$$
\chi_{\operatorname{Ind}}(g)
=\frac1{\abs{H}}\sum_{x\in G}\chi(x^{-1}gx)
=\sum_{\substack{i\\g_i^{-1}gg_i\in H}}
\chi(g_i^{-1}gg_i).
$$

::: pf-proof
The element $g$ sends the summand $g_i\otimes W$ to $g_j\otimes W$, where $gg_iH=g_jH$; only the summands with $g_i^{-1}gg_i\in H$ contribute to the trace, and on such a summand $g$ acts as $g_i^{-1}gg_i$ acts on $W$.
This gives the second sum.
Each $x\in g_iH$ gives $\chi(x^{-1}gx)=\chi(g_i^{-1}gg_i)$ because $\chi$ is a class function on $H$, and each coset has $\abs{H}$ elements; this gives the first sum.
:::

:::

::: pf-step
For every representation $U$ of $G$, Frobenius reciprocity is the natural isomorphism
$$
\Hom_G(\operatorname{Ind}_H^GW,U)
\cong
\Hom_H(W,\Res_H^GU),
$$
and for characters $\chi$ of $H$ and $\psi$ of $G$,
$$
\inner{\operatorname{Ind}_H^G\chi}{\psi}_G
=
\inner{\chi}{\Res_H^G\psi}_H.
$$

::: pf-proof
The isomorphism is the tensor--hom adjunction $\Hom_{\CC[G]}(\CC[G]\otimes_{\CC[H]}W,U)\cong\Hom_{\CC[H]}(W,U)$.
Taking dimensions of both sides gives the character identity.
:::

:::

:::
:::
