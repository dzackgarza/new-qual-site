---
schema: qual/card@1
id: P-WDSNU
kind: problem
title: Regular representation
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Group Rings
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
What is the regular representation of a finite group $G$?
State its character, decomposition into irreducible representations, and connection to the group algebra $\mathbb{C}[G]$.
:::

::: {.solution}
The left regular representation of a finite group $G$ is the action on its group algebra
\[
\mathbb C[G]
\]
by left multiplication:
\[
g\cdot e_h=e_{gh}.
\]
It has dimension $|G|$ and is faithful.

Its character is
\[
\chi_{\mathrm{reg}}(g)=
\begin{cases}
|G|,&g=1,\\
0,&g\ne1.
\end{cases}
\]
Indeed, for $g\ne1$, left multiplication fixes no basis vector $e_h$.

Let $V_1,\dots,V_r$ be the irreducible complex representations, with characters $\chi_i$ and dimensions $d_i$. The multiplicity of $V_i$ in the regular representation is
\[
\langle\chi_{\mathrm{reg}},\chi_i\rangle
=\frac1{|G|}|G|\chi_i(1)=d_i.
\]
Hence
\[
\mathbb C[G]\cong\bigoplus_i V_i^{\oplus d_i}
\]
as a left $G$-module, and therefore
\[
|G|=\sum_i d_i^2.
\]
As a semisimple algebra, Artin--Wedderburn gives
\[
\mathbb C[G]\cong\prod_i M_{d_i}(\mathbb C).
\]
:::
