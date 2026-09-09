---
schema: qual/card@1
id: P-WY2K6
kind: problem
title: Lagrange's theorem
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
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

::: problem
State and prove **Lagrange's Theorem** for finite groups: if $G$ is a finite group and $H \le G$ is a subgroup, then $|H|$ divides $|G|$ and $|G| = [G : H] \cdot |H|$.
:::

::: solution
The left cosets of $H$ in $G$ partition $G$. Indeed, define
\[
x\sim y\iff x^{-1}y\in H.
\]
This is an equivalence relation, and the equivalence class of $g\in G$ is exactly
\[
gH=\{gh:h\in H\}.
\]
Hence
\[
G=\bigsqcup_{i=1}^{[G:H]} g_iH
\]
for any choice of left-coset representatives $g_i$.

For each $g\in G$, left multiplication
\[
H\to gH,\qquad h\mapsto gh
\]
is a bijection, so every left coset has cardinality $|H|$. Therefore
\[
|G|
=\sum_{i=1}^{[G:H]}|g_iH|
=[G:H]|H|.
\]
In particular, $|H|$ divides $|G|$.
:::
