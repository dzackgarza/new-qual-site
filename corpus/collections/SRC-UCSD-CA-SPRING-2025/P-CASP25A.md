---
schema: qual/card@1
id: P-CASP25A
kind: problem
title: 'If $\abs{f(0)}+\abs{f''(0)}<\min_{\abs z=1}\abs f$, then $f$ has at least two zeros in $\DD$'
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Holomorphic Functions
  - Zeros
relations: []
review: draft
---

::: {.problem}
Let $f$ be a holomorphic function in a neighborhood of the closed unit disc $\overline{\DD}$, and suppose that
$$
\abs{f(0)} + \abs{f'(0)} < \inf\{\abs{f(z)} : \abs{z} = 1\}.
$$
Show that $f$ has at least two zeros (counting multiplicity) in $\DD$.

(Hint: Make use of the function $g(z) = f(0) + f'(0)z - f(z)$.)
:::

::: {.solution}

The argument is the card's own, following the printed hint and Rouché's theorem; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $f$ be holomorphic on a neighbourhood of $\overline{\DD}$ with
$$
\abs{f(0)}+\abs{f'(0)}<\inf_{\abs{z}=1}\abs{f(z)},
$$
and put $g(z)=f(0)+f'(0)z-f(z)$.

::: pf

::: {.pf-step #boundary}
$\abs{f(0)+f'(0)z}<\abs{f(z)}$ for $\abs{z}=1$.

::: pf-proof
For $\abs{z}=1$, $\abs{f(0)+f'(0)z}\le\abs{f(0)}+\abs{f'(0)}$, and that is strictly less than $\abs{f(z)}$ by the hypothesis; note that $\inf_{\abs{z}=1}\abs{f(z)}>0$, so $f$ has no zero on the unit circle.
:::

:::

::: {.pf-step #rouche}
$g$ and $-f$ have the same number of zeros in $\DD$, counted with multiplicity.

::: pf-proof
Both are holomorphic on a neighbourhood of $\overline{\DD}$, and on the circle $\abs{z}=1$ one has $\abs{g(z)-(-f(z))}=\abs{f(0)+f'(0)z}<\abs{f(z)}=\abs{-f(z)}$ by step [](#boundary){.pf-ref}. Rouché's theorem then gives that $g$ and $-f$ have the same number of zeros in $\DD$, counted with multiplicity.
:::

:::

::: {.pf-step #zero-order}
$g$ has a zero of order at least $2$ at $0$, unless $g\equiv0$, in which case $f$ is linear and the hypothesis fails.

::: pf-proof
$g(0)=f(0)-f(0)=0$ and $g'(z)=f'(0)-f'(z)$, so $g'(0)=0$; hence the order of vanishing of $g$ at $0$ is at least $2$ unless $g$ is identically $0$ on the connected neighbourhood of $\overline{\DD}$. If $g\equiv0$ then $f(z)=f(0)+f'(0)z$ is linear with $a=f(0)$ and $b=f'(0)$; choosing $\abs{z}=1$ so that $bz=-\abs{b}a/\abs{a}$ when $a\ne0$ gives $\abs{f(z)}=\abs{\abs{a}-\abs{b}}\le\abs{a}+\abs{b}$, so $\inf_{\abs{z}=1}\abs{f}\le\abs{f(0)}+\abs{f'(0)}$ and the hypothesis fails; and if $a=0$ then $\abs{f(0)}+\abs{f'(0)}=\abs{b}$ while $f$ vanishes at $0$, so the infimum on the circle is $0$ and the hypothesis fails as well.
:::

:::

::: {.pf-step #conclusion}
$f$ has at least two zeros in $\DD$, counted with multiplicity.

::: pf-proof
If $g\equiv0$ then the hypothesis fails by step [](#zero-order){.pf-ref}, so $g$ has a zero of order at least $2$ at $0\in\DD$. By step [](#rouche){.pf-ref}, $f$ and $g$ have the same number of zeros in $\DD$ counted with multiplicity, because $-f$ and $f$ have the same zeros. Hence $f$ has at least two.
:::

:::

:::
:::
