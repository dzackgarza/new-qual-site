---
schema: qual/card@1
id: P-CAFA19D
kind: problem
title: 'Roots of $z^7-2z^5+b$ in $\DD$ and in $1\leq\abs z<2$'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, (a) and (b) as top-level steps with (b) as the
    QED step. Re-checked: on $\abs z=1$ the bound $\abs{z^7+b}\le1+\abs b<2=\abs{-2z^5}$ gives five
    zeros inside by Rouché; the critical points are exactly the zeros of
    $z^4(7z^2-10)$, namely $0$ and $\pm\sqrt{10/7}$; at $z^2=10/7$ the root condition forces
    $\abs b=\frac47(10/7)^{5/2}>1$, contradicting $\abs b<1$; with $b=0$ the only zero in $\DD$ is
    $0$ of multiplicity $5$; and on $\abs z=2$ the bound $\abs{-2z^5+b}<65<128=\abs{z^7}$ gives seven
    zeros inside, so two in the annulus. Repaired: an earlier version of the last step said the
    critical points were "$0,\pm\sqrt{10/7}$ and the first two lie in $\DD$ or are $0$", which does
    not exclude $\pm\sqrt{10/7}$ from the annulus — the step now handles $b\ne0$ and $b=0$
    separately and notes that for $b=0$ the annulus zeros $\pm\sqrt2$ satisfy $7\cdot2-10\ne0$. No
    defect found in the statement. The collection's provenance is the Fall 2019 examination paper,
    so no retained solution set covers the problem.
---

::: {.problem}
Let $b \in \DD$ and set $f(z) = z^7 - 2z^5 + b$.

(a) How many roots (counting multiplicity) does $f$ have in $\DD$?
How many simple roots does $f$ have in $\DD$?

(b) How many simple roots does $f$ have in $\{1 \leq \abs{z} < 2\}$?
:::

::: {.solution}
The collection's provenance is the examination paper, so no retained solution set covers the problem and the argument is the card's own; both counts are Rouché's theorem on the two circles, together with a check of the critical points. Write $f(z)=z^7-2z^5+b$ with $\abs b<1$.

::: pf

::: {.pf-step #inner-count}
(a) On $\abs z=1$ one has $\abs{z^7+b}<\abs{-2z^5}$, so $f$ has five zeros in $\DD$, counted with multiplicity.

::: pf-proof
For $\abs z=1$, $\abs{z^7+b}\le\abs z^7+\abs b=1+\abs b<2=\abs{-2z^5}$. Both functions are holomorphic on a neighbourhood of the closed disc and the inequality is strict on the boundary circle, so Rouché's theorem gives $f$ and $-2z^5$ the same number of zeros in $\DD$; $-2z^5$ has the zero $0$ of multiplicity $5$.
:::

:::

::: {.pf-step #critical}
The critical points of $f$ are $0$ and $\pm\sqrt{10/7}$, and none of them is a zero of $f$ when $b\ne0$.

::: pf-proof
$f'(z)=7z^6-10z^4=z^4(7z^2-10)$, which vanishes exactly at $0$ and at $z^2=10/7$. At $0$ one has $f(0)=b\ne0$. If $z^2=10/7$ and $f(z)=0$, then $b=-z^5(z^2-2)$ and
$$
\abs b=\abs z^5\abs{z^2-2}=\Bigl(\frac{10}{7}\Bigr)^{5/2}\cdot\frac47=\frac{4}{7}\Bigl(\frac{10}{7}\Bigr)^{5/2}>1,
$$
since $(10/7)^{5/2}>1$; this contradicts $\abs b<1$.
:::

:::

::: {.pf-step #simple-inner}
(a) If $b\ne0$ all five zeros in $\DD$ are simple; if $b=0$ there are no simple zeros in $\DD$.

::: pf-proof
A zero is non-simple exactly when it is a critical point. If $b\ne0$, step [](#critical){.pf-ref} excludes every critical point from the zero set, so the five zeros of step [](#inner-count){.pf-ref} are simple. If $b=0$, then $f(z)=z^5(z^2-2)$, whose zeros are $0$ and $\pm\sqrt2$; only $0$ lies in $\DD$, with multiplicity $5$, so no zero in $\DD$ is simple.
:::

:::

::: {.pf-step}
(b) Exactly two simple zeros lie in the annulus $\{1\le\abs z<2\}$.

::: pf-proof
On $\abs z=2$, $\abs{-2z^5+b}\le2\cdot32+\abs b<65<128=\abs{z^7}$, so Rouché gives $f$ and $z^7$ seven zeros in $\abs z<2$, counted with multiplicity. By step [](#inner-count){.pf-ref} five of them lie in $\DD$, and none lies on $\abs z=1$ because the strict inequality of step [](#inner-count){.pf-ref} holds there; hence exactly $7-5=2$ lie in $1\le\abs z<2$. They are simple: a non-simple zero is a critical point, so it is $0$ or $\pm\sqrt{10/7}$, and $0$ is not in the annulus while $\pm\sqrt{10/7}$, which do lie in it, are not zeros of $f$ when $b\ne0$ by step [](#critical){.pf-ref}; when $b=0$ the zeros there are $\pm\sqrt2$, and $7\cdot2-10=4\ne0$ shows that these are not critical points. Step [](#simple-inner){.pf-ref} covers the multiplicities in $\DD$.
:::

:::

:::
:::
