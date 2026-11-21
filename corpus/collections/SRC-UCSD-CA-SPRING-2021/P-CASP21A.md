---
schema: qual/card@1
id: P-CASP21A
kind: problem
title: 'Solutions of $z^3\sin z+5z^2+2=0$ in the unit disc'
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Polynomial Roots
  - Argument Principle
relations: []
review: draft
---

::: {.problem}
How many solutions, counted with multiplicities, does the equation
$$
z^3 \sin z + 5z^2 + 2 = 0
$$
have in the unit disc $\abs{z} < 1$?
:::

::: {.solution}

No retained solution set covers this exercise: the card's own application of Rouché's theorem follows, with the two estimates on the circle and the count of the comparison polynomial as separate steps.

::: pf

::: {.pf-step #analytic}
$g(z)=z^{3}\sin z+5z^{2}+2$ and $f(z)=5z^{2}+2$ are analytic on a neighbourhood of the closed unit disc, and $\abs{g(z)-f(z)}<\abs{f(z)}$ for $\abs{z}=1$.

::: pf-proof
Both are entire: a polynomial and $z^{3}$ times the entire function $\sin z$. On $\abs{z}=1$ one has $\abs{g-f}=\abs{z^{3}\sin z}=\abs{\sin z}\le\sinh 1<2$, since $\abs{\sin z}\le\sinh\abs{z}$ and $\sinh1<2$; and $\abs{f}=\abs{5z^{2}+2}\ge5\abs{z}^{2}-2=3$. So $\abs{g-f}<2<3\le\abs{f}$.
:::

:::

::: {.pf-step #rouche}
$g$ and $f$ have the same number of zeros in $\DD=\theset{\abs{z}<1}$, counted with multiplicity.

::: pf-proof
$g$ and $f$ are analytic near the closed disc $\overline{\DD}$ and satisfy the strict inequality $\abs{g-f}<\abs{f}$ on the boundary circle $\abs{z}=1$ by step [](#analytic){.pf-ref}; Rouché's theorem then gives the stated equality.
:::

:::

::: {.pf-step #count}
$f(z)=5z^{2}+2$ has exactly two zeros in $\DD$, counted with multiplicity.

::: pf-proof
$5z^{2}+2=0$ exactly for $z^{2}=-2/5$, that is $z=\pm i\sqrt{2/5}$, two distinct points, each a simple zero since $(5z^{2}+2)'=10z\ne0$ there. And $\abs{\pm i\sqrt{2/5}}=\sqrt{2/5}<1$, so both lie in $\DD$.
:::

:::

::: {.pf-qed}
By steps [](#rouche){.pf-ref} and [](#count){.pf-ref} the equation $z^{3}\sin z+5z^{2}+2=0$ has exactly $2$ solutions in $\abs{z}<1$, counted with multiplicity.
:::

:::

:::
