---
schema: qual/card@1
id: P-PRACT20-W3-09
kind: problem
title: The $100$th derivative of $3/(x^2+5x+4)$ at $x=2$
classification:
  areas:
  - prelim
  topics:
  - Taylor Series
  - Partial Fractions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 3 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem asks for the hundredth derivative at 2 of the same rational function, and the printed solution gives the same value
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's partial fractions and its expansion of each term about x = 2 are transcribed, with the coefficient-to-derivative step justified by the Taylor coefficient formula.
---

::: {.problem}
Find $f^{(100)}(2)$ for $f(x) = \frac{3}{x^{2} + 5x + 4}$.
:::

::: {.solution}

Let $f(x)=\dfrac{3}{x^2+5x+4}=\dfrac{3}{(x+1)(x+4)}$; find its $100$-th
derivative at $x=2$.

::: pf

::: {.pf-step #partialfractions}

$f(x)=\dfrac{1}{1+x}-\dfrac{1}{4+x}$.

::: pf-proof

$\frac{1}{1+x}-\frac{1}{4+x}=\frac{(4+x)-(1+x)}{(1+x)(4+x)}=\frac{3}{(1+x)(4+x)}$,
which is $f$.

:::

:::

::: {.pf-step #expansion}

About $x=2$,
$$
f(x)=\frac13\sum_{n\ge0}\frac{(-1)^n(x-2)^n}{3^n}-\frac16\sum_{n\ge0}\frac{(-1)^n(x-2)^n}{6^n},
$$
so the coefficient of $(x-2)^{100}$ is
$(-1)^{100}\big(\tfrac{1}{3^{101}}-\tfrac{1}{6^{101}}\big)$.

::: pf-proof

$\frac{1}{1+x}=\frac{1}{3+(x-2)}=\frac13\cdot\frac{1}{1+\frac{x-2}{3}}=\frac13\sum_n\big(-\frac{x-2}{3}\big)^n$,
a geometric series converging for $\abs{x-2}<3$; similarly
$\frac{1}{4+x}=\frac{1}{6+(x-2)}=\frac16\sum_n\big(-\frac{x-2}{6}\big)^n$,
converging for $\abs{x-2}<6$. In the common disc the sum of the two series is
$f$, and the coefficient of $(x-2)^n$ in the first is $\frac{(-1)^n}{3^{n+1}}$
and in the second $\frac{(-1)^n}{6^{n+1}}$, so for $n=100$ the coefficient is
$\frac{1}{3^{101}}-\frac{1}{6^{101}}$.

:::

:::

::: {.pf-step #derivative}

$\boxed{f^{(100)}(2)=100!\left(\frac{1}{3^{101}}-\frac{1}{6^{101}}\right)}$.

::: pf-proof

For a function given near $2$ by a power series $\sum_nc_n(x-2)^n$, the
coefficient is $c_n=\frac{f^{(n)}(2)}{n!}$, since differentiating $n$ times
and evaluating at $2$ isolates the $n$-th term. Hence
$f^{(100)}(2)=100!\,c_{100}=100!\big(\frac{1}{3^{101}}-\frac{1}{6^{101}}\big)$,
which is the printed answer, approximately $6.0361\times10^{109}$.

:::

:::

:::


:::
