---
schema: qual/card@1
id: P-BERK89S-15
kind: problem
title: A $20\times20$ zero-diagonal $\pm1$ matrix is nonsingular
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Reduced the integer matrix modulo $2$, identified it with $I+J$, and used
    $J^2=0$ in characteristic two to obtain an explicit inverse.
---

::: {.problem}
Let $B=(b_{ij})_{i,j=1}^{20}$ be a real $20\times20$ matrix satisfying
\[
b_{ii}=0
\]
for every $i$, and
\[
b_{ij}\in\{1,-1\}
\]
for $i\ne j$. Prove that $B$ is nonsingular.
:::

::: {.solution}
Let $\overline B$ denote the reduction of $B$ modulo $2$, regarded as a
$20\times20$ matrix over $\FF_2$, and let $J$ be the $20\times20$ all-ones
matrix over $\FF_2$.

::: pf

::: {.pf-step #reduction-identity}
One has
$$
\overline B=I+J.
$$

::: pf-proof
Every diagonal entry of $B$ is $0$, while every off-diagonal entry is either
$1$ or $-1$. Modulo $2$, both $1$ and $-1$ become $1$. Thus
$\overline B$ has zero diagonal and all off-diagonal entries equal to $1$.

The matrix $J$ has every entry equal to $1$, so over the field of
characteristic two, $I+J$ has diagonal entries $1+1=0$ and off-diagonal
entries $1$. Hence $\overline B=I+J$.
:::

:::

::: {.pf-step #reduction-invertible}
The matrix $\overline B$ is invertible over $\FF_2$.

::: pf-proof
Every entry of $J^2$ is the sum of twenty copies of $1$. Since
$20=0$ in $\FF_2$,
$$
J^2=0.
$$
Therefore, using step [](#reduction-identity){.pf-ref},
$$
\overline B^2
=(I+J)^2
=I+2J+J^2
=I.
$$
Thus $\overline B$ is its own inverse.
:::

:::

::: {.pf-step #det-odd}
The integer $\det B$ is odd and in particular nonzero.

::: pf-proof
Reduction modulo $2$ commutes with the determinant, so
$$
\det(\overline B)=\overline{\det B}\in\FF_2.
$$
By step [](#reduction-invertible){.pf-ref}, $\overline B$ is invertible, hence
$\det(\overline B)\neq0$. Therefore $\det B$ is not divisible by $2$, so it
is odd. In particular, $\det B\neq0$.
:::

:::

::: {.pf-step #b-nonsingular}
The matrix $B$ is nonsingular.

::: pf-proof
By step [](#det-odd){.pf-ref}, $\det B\neq0$, which is equivalent to invertibility of the
real square matrix $B$.
:::

:::

::: pf-qed
Step [](#b-nonsingular){.pf-ref} is the required conclusion.
:::

:::
:::
