---
schema: qual/card@1
id: E-SS2.EX-7
kind: problem
title: $2\abs{f'(0)}$ is at most the diameter of $f(\DD)$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose argument into numbered steps without changing the mathematics, and
    re-checked each step against the definitions and theorems it invokes. What was not checked: no
    copy of Stein and Shakarchi and no solution set for it is retained in tmp/sources (the
    collection provenance is the Google Books ISBN link), so the printed statement and page were
    not re-read; the exercise number is the one the collection index records. No published
    solution is transcribed; the argument remains the card's own, as its solution section says.
---

::: {.exercise}
Suppose $f \colon \DD \to \CC$ is holomorphic. Show that the diameter $d = \sup_{z, w \in \DD} \abs{f(z) - f(w)}$ of the image of $f$ satisfies
$$
2\abs{f'(0)} \leq d.
$$
Moreover, it can be shown that equality holds precisely when $f$ is linear, $f(z) = a_0 + a_1 z$.

Note. In connection with this result, see the relationship between the diameter of a curve and Fourier series described in Problem 1, Chapter 4, Book I.

[Hint: $2f'(0) = \frac{1}{2\pi i} \int_{\abs{\zeta} = r} \frac{f(\zeta) - f(-\zeta)}{\zeta^2}\, d\zeta$ whenever $0 < r < 1$.]
:::

::: {.solution}

The argument is the card's own: the book is retained in this repository as `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, and no published solution set of this exercise is retained, so nothing below is transcribed. The statement is the exercise the collection index records as Stein and Shakarchi, *Complex Analysis* (2003), Ch. 2, Exercise 7. Here $\DD=\theset{\abs{z}<1}$, $f$ is holomorphic on a neighbourhood of the closed disc $\overline{D_r}$ for each $r<1$, and $d=\sup_{z,w\in\DD}\abs{f(z)-f(w)}$ is the diameter of the image; $d<\infty$ is not assumed in advance, and the steps below show the bound only has content when it is finite.

::: pf

::: {.pf-step #cf}

For $0<r<1$, $2f'(0)=\frac{1}{2\pi i}\int_{\abs{\zeta}=r}\frac{f(\zeta)-f(-\zeta)}{\zeta^{2}}\,d\zeta$.

::: pf-proof

The Cauchy integral formula for the first derivative gives $f'(0)=\frac{1}{2\pi i}\int_{\abs{\zeta}=r}\frac{f(\zeta)}{\zeta^{2}}\,d\zeta$. Applying it to $\zeta\mapsto f(-\zeta)$, a holomorphic function on the same disc whose derivative at $0$ is $-f'(0)$, gives $\frac{1}{2\pi i}\int_{\abs{\zeta}=r}\frac{f(-\zeta)}{\zeta^{2}}\,d\zeta=-f'(0)$ after the substitution $\zeta\mapsto-\zeta$. Subtracting the two identities gives the displayed formula.

:::

:::

::: {.pf-step #bound}

$\abs{f(\zeta)-f(-\zeta)}\leq d$ for $\abs{\zeta}=r$.

::: pf-proof

Both $\zeta$ and $-\zeta$ lie in $\DD$ when $\abs{\zeta}=r<1$, and $d$ is the supremum of $\abs{f(z)-f(w)}$ over pairs in $\DD$.

:::

:::

::: {.pf-step #est}

$2\abs{f'(0)}\leq d/r$.

::: pf-proof

Taking absolute values in step [](#cf){.pf-ref} and estimating the integrand by step [](#bound){.pf-ref}, $2\abs{f'(0)}\leq\frac{1}{2\pi}\int_{\abs{\zeta}=r}\frac{d}{r^{2}}\abs{d\zeta}=\frac{1}{2\pi}\frac{d}{r^{2}}2\pi r=\frac{d}{r}$.

:::

:::

::: {.pf-step #done}

$2\abs{f'(0)}\leq d$.

::: pf-proof

The left side of step [](#est){.pf-ref} does not depend on $r$ and $d/r\to d$ as $r\uparrow1$.

:::

:::

:::

:::
