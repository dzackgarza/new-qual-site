---
schema: qual/card@1
id: P-NAGQY
kind: problem
title: Character table of a finite group and the cyclotomic field containing its entries
classification:
  areas:
  - algebra
  topics:
  - Character Theory
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
For a finite group $G$, what is its complex character table? In what fields do its entries lie?
:::

::: {.solution}
Let $g_1,\ldots,g_r$ be representatives of the conjugacy classes of $G$ and $\chi_1,\ldots,\chi_r$ the irreducible complex characters, and let $e$ be the exponent of $G$.

::: pf

::: pf-step
The character table of $G$ is the $r\times r$ matrix $(\chi_i(g_j))_{i,j}$, with rows indexed by the irreducible complex characters and columns by the conjugacy classes.

::: pf-proof
Characters are class functions, so $\chi_i(g_j)$ does not depend on the chosen representative, and the number of irreducible characters equals the number $r$ of conjugacy classes.
:::

:::

::: {.pf-step #roots}
If $g\in G$ has order $m$ and $\rho$ is a representation with character $\chi$, then $\chi(g)$ is a sum of $m$-th roots of unity.

::: pf-proof
$\rho(g)^m=I$, so $\rho(g)$ is diagonalizable with eigenvalues that are $m$-th roots of unity, and $\chi(g)=\tr\rho(g)$ is their sum.
:::

:::

::: pf-step
Every entry of the character table is an algebraic integer in $\boxed{\QQ(\zeta_e)}$, and hence in $\QQ(\zeta_{\abs{G}})$.

::: pf-proof
Every element order divides $e$, so by step [](#roots){.pf-ref} every entry is a sum of $e$-th roots of unity, which are algebraic integers in $\QQ(\zeta_e)$.
Since $e\mid\abs{G}$, $\QQ(\zeta_e)\subseteq\QQ(\zeta_{\abs{G}})$.
:::

:::

:::

:::

::: {.remark}
The entries need not be rational or real: the character table of $\ZZ/3\ZZ$ contains $\zeta_3$.
:::
