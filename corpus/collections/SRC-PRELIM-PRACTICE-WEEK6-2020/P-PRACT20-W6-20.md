---
schema: qual/card@1
id: P-PRACT20-W6-20
kind: problem
title: Standard deviation of the density $\frac34(1-x^2)$ on $[-1,1]$
classification:
  areas:
  - prelim
  topics:
  - Probability
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    No source document is retained for this card. The collection
    SRC-PRELIM-PRACTICE-WEEK6-2020 has an empty provenance list, and the only
    retained pages of the practice sheet are the three page images
    assets/attachments/prelim-practice-week6-2020/page-4.png, page-5.png and
    page-11.png, none of which carries this problem; so there is no printed page
    to compare the statement with. What was checked is the statement as it stands
    on the card: the statement was read and the computation redone: the density integrates to 1, the mean vanishes by oddness, the second moment is 1/5 and the standard deviation is 1/sqrt 5
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. Normalisation of the density, the vanishing mean by symmetry, the second moment by an elementary integral, and the square root
---

::: {.problem}
Let $X$ be a random variable with density function $f(x) = \frac{3}{4}(1 - x^{2})$, for $x \in [-1, 1]$ (and $f(x) = 0$ elsewhere).
What is the standard deviation of $X$?
:::

::: {.solution}

Let $X$ have density $f(x)=\frac34(1-x^2)$ on $[-1,1]$ and $0$ elsewhere; the
standard deviation is $\sqrt{\operatorname{Var}X}$ with
$\operatorname{Var}X=E[X^2]-(E[X])^2$.

::: pf

::: {.pf-step #mean}

$f$ is a probability density and $E[X]=0$.

::: pf-proof

$\int_{-1}^1\frac34(1-x^2)\,dx=\frac34\big(2-\frac23\big)=\frac34\cdot\frac43=1$,
so $f$ integrates to $1$ and is nonnegative on $[-1,1]$, hence is a density.
The function $x\mapsto xf(x)=\frac34(x-x^3)$ is odd on the symmetric interval
$[-1,1]$, so its integral vanishes and $E[X]=0$.

:::

:::

::: {.pf-step #second}

$E[X^2]=\frac15$.

::: pf-proof

By symmetry,
$E[X^2]=\int_{-1}^1x^2\frac34(1-x^2)\,dx=\frac34\cdot2\int_0^1(x^2-x^4)\,dx=\frac32\Big(\frac13-\frac15\Big)=\frac32\cdot\frac{2}{15}=\frac15$.
Hence $\operatorname{Var}X=\frac15-0=\frac15$.

:::

:::

::: {.pf-step #sd}

The standard deviation is $\boxed{\frac{1}{\sqrt5}}$.

::: pf-proof

The standard deviation is the square root of the variance, so it is
$\sqrt{1/5}=1/\sqrt5\approx0.447$. Since the density is supported on $[-1,1]$
and is even, this is consistent with the variance being a mean square of a
quantity bounded by $1$.

:::

:::

:::


:::
