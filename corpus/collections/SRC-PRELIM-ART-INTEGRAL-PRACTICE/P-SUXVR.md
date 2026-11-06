---
schema: qual/card@1
id: P-SUXVR
kind: problem
title: Antiderivatives of $1/(x^2\sqrt{x^2-a^2})$ and $1/(x\sqrt{x^2-a^2})$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometric Substitution
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Replaced branch-dependent inverse-secant forms by branch-safe primitives and restored constants.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    No source document is retained for this card. The collection
    SRC-PRELIM-ART-INTEGRAL-PRACTICE has an empty provenance list, its own
    remark records that the drill sheet's original paper was not found, and
    searching assets/attachments/ and the migration records finds no copy of the
    sheet, so there is no page to read and the printed statement could not be
    compared with a source document. What was checked here is the statement and
    its answer: the general primitive by the quotient rule, the two special cases as instances of it, the scaled case by direct differentiation, and the last by the substitution u = sqrt(x^2 - 16)
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. The general primitive verified by the quotient rule, its two special cases, a separately verified scaled case, and a substitution for the last integral.
---

::: {.problem}
Evaluate, on intervals where the real-valued integrands are defined,
$$
\int\frac{dx}{x^2\sqrt{x^2-a^2}},
$$
together with the special cases $a=2$, $a=3$, and
$$
\int\frac{dx}{x^2\sqrt{4x^2-1}}.
$$
Also evaluate
$$
\int\frac{dx}{2x\sqrt{x^2-16}}.
$$
:::

::: {.solution}

Let $a$ be a nonzero real constant; the integrands are real and continuous on
the intervals where the square roots are defined and nonzero.

::: pf

::: {.pf-step #general}

For $a\ne0$,
$\displaystyle\int\frac{dx}{x^2\sqrt{x^2-a^2}}=\frac{\sqrt{x^2-a^2}}{a^2x}+C$.

::: pf-proof

Differentiate $f(x)=\frac{\sqrt{x^2-a^2}}{x}$ by the quotient rule:
$f'(x)=\frac{x\cdot\frac{x}{\sqrt{x^2-a^2}}-\sqrt{x^2-a^2}}{x^2}=\frac{\frac{x^2-(x^2-a^2)}{\sqrt{x^2-a^2}}}{x^2}=\frac{a^2}{x^2\sqrt{x^2-a^2}}$.
Dividing by $a^2$, which is nonzero, gives the stated primitive, and the
integrand is continuous on each interval of its domain because
$\sqrt{x^2-a^2}\ne0$ there, so the primitives on each such interval are this
function plus a constant.

:::

:::

::: {.pf-step #special}

$\displaystyle\int\frac{dx}{x^2\sqrt{x^2-4}}=\frac{\sqrt{x^2-4}}{4x}+C$ and
$\displaystyle\int\frac{dx}{x^2\sqrt{x^2-9}}=\frac{\sqrt{x^2-9}}{9x}+C$.

::: pf-proof

These are step [](#general){.pf-ref} with $a=2$, so that $a^2=4$, and with
$a=3$, so that $a^2=9$; in both cases $a\ne0$ and the formula applies
verbatim.

:::

:::

::: {.pf-step #scaled}

$\displaystyle\int\frac{dx}{x^2\sqrt{4x^2-1}}=\frac{\sqrt{4x^2-1}}{x}+C$.

::: pf-proof

Differentiate $g(x)=\frac{\sqrt{4x^2-1}}{x}$:
$g'(x)=\frac{x\cdot\frac{4x}{\sqrt{4x^2-1}}-\sqrt{4x^2-1}}{x^2}=\frac{\frac{4x^2-(4x^2-1)}{\sqrt{4x^2-1}}}{x^2}=\frac{1}{x^2\sqrt{4x^2-1}}$,
which is the integrand, so $g$ is a primitive. This is not the substitution
$x\mapsto2x$ of step [](#general){.pf-ref}, whose $a=1$ case gives
$\frac{\sqrt{x^2-1}}{x}$.

:::

:::

::: {.pf-step #arctan}

$\displaystyle\int\frac{dx}{2x\sqrt{x^2-16}}=\frac18\arctan\left(\frac{\sqrt{x^2-16}}{4}\right)+C$
on $x>4$ and on $x<-4$.

::: pf-proof

Put $u=\sqrt{x^2-16}$, so $u^2=x^2-16$ and $u\,du=x\,dx$, giving
$dx=\frac{u\,du}{x}$; then
$\frac{dx}{2x\sqrt{x^2-16}}=\frac{u\,du}{2x^2u}=\frac{du}{2(u^2+16)}$, whose
primitive is $\frac12\cdot\frac14\arctan\frac u4$ by the standard formula
$\int\frac{du}{u^2+c^2}=\frac1c\arctan\frac uc$ with $c=4$. Substituting back
gives the stated form, which needs no inverse secant and so avoids the branch
choice that $\sec^{-1}(x/4)$ would involve.

:::

:::

:::


:::
