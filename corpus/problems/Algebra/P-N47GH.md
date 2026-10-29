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

::: {.problem}
Write the complete character table for the symmetric group $S_4$, giving the construction and justification for each irreducible character.
:::

::: {.solution}
Characters are listed by their values on the conjugacy classes of $S_4$, which are indexed by cycle type $1^4$, $2\,1^2$, $2^2$, $3\,1$, $4$, with sizes $1,6,3,8,6$.

::: pf

::: {.pf-step #count}
$S_4$ has exactly five irreducible complex characters.

::: pf-proof
The number of irreducible characters equals the number of conjugacy classes.
:::

:::

::: {.pf-step #linear}
The trivial character $\mathbf 1=(1,1,1,1,1)$ and the sign character $\operatorname{sgn}=(1,-1,1,1,-1)$ are irreducible.

::: pf-proof
They are one-dimensional; a permutation is odd exactly when it has an odd number of even-length cycles.
:::

:::

::: {.pf-step #std}
$\chi_{\mathrm{std}}=(3,1,-1,0,-1)$ and $\chi_{\mathrm{std}}\otimes\operatorname{sgn}=(3,-1,-1,0,1)$ are irreducible characters.

::: pf-proof
The permutation representation on $\CC^4$ has character the number of fixed points, $(4,2,0,1,0)$; subtracting $\mathbf 1$ gives $\chi_{\mathrm{std}}$.
Then $\inner{\chi_{\mathrm{std}}}{\chi_{\mathrm{std}}}=\frac{1}{24}(9+6+3+0+6)=1$, so $\chi_{\mathrm{std}}$ is irreducible, and multiplying by the linear character $\operatorname{sgn}$ preserves irreducibility.
:::

:::

::: {.pf-step #two}
$\chi_2=(2,0,2,-1,0)$ is an irreducible character.

::: pf-proof
The Klein subgroup $V_4=\{e,(12)(34),(13)(24),(14)(23)\}$ is normal in $S_4$ and $S_4/V_4\cong S_3$.
Pulling back the $2$-dimensional irreducible character $(2,0,-1)$ of $S_3$ gives an irreducible character of $S_4$.
A double transposition maps to the identity, a transposition and a $4$-cycle map to transpositions, and a $3$-cycle maps to a $3$-cycle, which gives the values.
:::

:::

::: pf-step
The character table of $S_4$ is
$$
\begin{array}{c|ccccc}
&1^4&2\,1^2&2^2&3\,1&4\\
\hline
\mathbf 1&1&1&1&1&1\\
\operatorname{sgn}&1&-1&1&1&-1\\
\chi_2&2&0&2&-1&0\\
\chi_{\mathrm{std}}&3&1&-1&0&-1\\
\chi_{\mathrm{std}}\otimes\operatorname{sgn}&3&-1&-1&0&1
\end{array}
$$

::: pf-proof
The five characters of steps [](#linear){.pf-ref}, [](#std){.pf-ref} and [](#two){.pf-ref} are pairwise distinct, so by step [](#count){.pf-ref} they are all the irreducible characters; as a check, $1+1+4+9+9=24=\abs{S_4}$.
:::

:::

:::

:::
