---
schema: qual/card@1
id: C-4GQK3
kind: corollary
title: Compositum and intersection of normal extensions
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Splitting Fields
  - Galois Theory
relations: []
review: draft
---

::: {.corollary}
Let $k$ be a field, let $\Omega$ be an algebraic closure of $k$, and let $E_1, E_2 \subseteq \Omega$ be extensions of $k$.
If $E_1/k$ and $E_2/k$ are [[D-LZTAK|normal]], then the compositum $E_1E_2/k$ and the intersection $(E_1 \cap E_2)/k$ are normal.

\begin{tikzcd}
	&& {E_1 E_2} \\
	\\
	{E_1} &&&& {E_2} \\
	&& {E_1 \cap E_2} \\
	\\
	\\
	&& {k}
	\arrow["{\text{normal}}", from=3-5, to=7-3]
	\arrow[from=4-3, to=7-3, dashed, no head, "\text{normal}", near start]
	\arrow["{\text{normal}}"', from=3-1, to=7-3]
	\arrow[from=1-3, to=3-1, no head]
	\arrow[from=1-3, to=3-5, no head]
	\arrow[from=1-3, to=4-3, no head]
	\arrow[from=1-3, to=7-3, curve={height=25pt}, dashed, no head, "\text{normal}"', near start]
	\arrow[from=3-1, to=4-3, no head]
	\arrow[from=4-3, to=3-5, no head]
\end{tikzcd}
:::
