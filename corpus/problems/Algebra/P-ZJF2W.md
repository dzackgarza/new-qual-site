---
schema: qual/card@1
id: P-ZJF2W
kind: problem
title: When the Galois group of a polynomial is contained in $A_n$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Permutations
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
If we think of the Galois group of a polynomial as contained in $S_n$, when is it contained in $A_n$?
:::

::: {.solution}
Assume $f\in K[x]$ is separable of degree $n$ and $\operatorname{char}K\ne2$. Let its roots in the splitting field be
\[
\alpha_1,\dots,\alpha_n,
\]
and let
\[
\delta=\prod_{i<j}(\alpha_i-\alpha_j).
\]
Then
\[
\Delta(f)=\delta^2\in K.
\]
For $\sigma$ in the Galois group, viewed as a permutation of the roots,
\[
\sigma(\delta)=\operatorname{sgn}(\sigma)\delta.
\]
Therefore
\[
G\subseteq A_n
\iff \sigma(\delta)=\delta\quad\forall\sigma\in G
\iff \delta\in K.
\]
Because $\operatorname{char}K\ne2$ and $\delta\ne0$,
\[
\delta\in K
\iff \Delta(f)=\delta^2\text{ is a square in }K.
\]
Hence
\[
\boxed{G\subseteq A_n\iff \Delta(f)\in K^{\times2}}.
\]
The separability and characteristic assumptions are essential for this standard criterion in this form.
:::
