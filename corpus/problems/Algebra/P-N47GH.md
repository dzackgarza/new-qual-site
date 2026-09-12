---
schema: qual/card@1
id: P-N47GH
kind: problem
title: The character table of $S_4$
classification:
  areas:
  - algebra
  topics:
  - Character Theory
  - Representation Theory
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Write the complete character table for the symmetric group $S_4$, giving the construction and justification for each irreducible character.
:::

::: solution
The conjugacy classes of $S_4$ are indexed by cycle type:
\[
1^4,\quad 2\,1^2,\quad 2^2,\quad 3\,1,\quad 4,
\]
with class sizes $1,6,3,8,6$.

There are therefore five irreducible complex characters. Two are the trivial and sign characters. The permutation representation on $\mathbb C^4$ has character equal to the number of fixed points; subtracting the trivial representation gives the standard character
\[
\chi_{\mathrm{std}}=(3,1,-1,0,-1).
\]
Tensoring with sign gives
\[
\chi_{\mathrm{std}}\otimes\mathrm{sgn}=(3,-1,-1,0,1).
\]
Finally $V_4\trianglelefteq S_4$ and $S_4/V_4\cong S_3$. Pulling back the $2$-dimensional irreducible character of $S_3$ gives
\[
\chi_2=(2,0,2,-1,0).
\]
Thus the complete table is
\[
\begin{array}{c|ccccc}
&1^4&2\,1^2&2^2&3\,1&4\\
\hline
\mathbf 1&1&1&1&1&1\\
\mathrm{sgn}&1&-1&1&1&-1\\
\chi_2&2&0&2&-1&0\\
\chi_{\mathrm{std}}&3&1&-1&0&-1\\
\chi_{\mathrm{std}}\otimes\mathrm{sgn}&3&-1&-1&0&1
\end{array}
\]
The squared dimensions sum to $1+1+4+9+9=24=|S_4|$, and the displayed rows are pairwise orthonormal with respect to the class-function inner product, so these are all irreducibles.
:::
