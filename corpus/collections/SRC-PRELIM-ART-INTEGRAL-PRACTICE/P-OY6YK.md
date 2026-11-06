---
schema: qual/card@1
id: P-OY6YK
kind: problem
title: Integrals of $\frac{x^2+2x+1}{x\sqrt{x^2-1}}$ and $\frac{x+16}{\sqrt{x^2-4x+8}}$
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
  note: Replaced branch-sensitive inverse-secant notation by an arctangent primitive and restored constants/domains.
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
    its answer: the termwise split with its three primitives and the completion of the square with the shifted linear term, each checked by differentiating
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. A termwise split with three verified primitives, and a completion of the square.
---

::: {.problem}
Evaluate, on intervals where the real-valued integrands are defined,
$$
\int\frac{x^2+2x+1}{x\sqrt{x^2-1}}\,dx
$$
and
$$
\int\frac{x+16}{\sqrt{x^2-4x+8}}\,dx.
$$
:::

::: {.solution}

Each integrand is real and continuous on each interval of its domain: the
first where $\abs x>1$, the second on $\RR$ because $x^2-4x+8=(x-2)^2+4>0$.

::: pf

::: {.pf-step #split}

$\displaystyle\int\frac{x^2+2x+1}{x\sqrt{x^2-1}}\,dx=\sqrt{x^2-1}+2\ln\abs{x+\sqrt{x^2-1}}+\arctan\sqrt{x^2-1}+C$.

::: pf-proof

Dividing termwise by $x\sqrt{x^2-1}$ gives
$\frac{x}{\sqrt{x^2-1}}+\frac{2}{\sqrt{x^2-1}}+\frac{1}{x\sqrt{x^2-1}}$, an
identity of functions on the domain. The three primitives are $\sqrt{x^2-1}$,
since $\frac{d}{dx}\sqrt{x^2-1}=\frac{x}{\sqrt{x^2-1}}$;
$2\ln\abs{x+\sqrt{x^2-1}}$, since
$\frac{d}{dx}\ln\abs{x+\sqrt{x^2-1}}=\frac{1}{\sqrt{x^2-1}}$; and
$\arctan\sqrt{x^2-1}$, since with $w=\sqrt{x^2-1}$ one has
$\frac{d}{dx}\arctan
w=\frac{x/w}{1+w^2}=\frac{x}{w\,x^2}=\frac{1}{x\sqrt{x^2-1}}$. Summing gives
the stated primitive on each component of $\{\abs x>1\}$.

:::

:::

::: {.pf-step #completing}

$\displaystyle\int\frac{x+16}{\sqrt{x^2-4x+8}}\,dx=\sqrt{x^2-4x+8}+18\ln\abs{x-2+\sqrt{x^2-4x+8}}+C$.

::: pf-proof

Complete the square: $x^2-4x+8=(x-2)^2+4$ and $x+16=(x-2)+18$, so with $w=x-2$
the integral is $\int\frac{(w+18)\,dw}{\sqrt{w^2+4}}$. The first part is
$\int\frac{w\,dw}{\sqrt{w^2+4}}=\sqrt{w^2+4}$ because
$\frac{d}{dw}\sqrt{w^2+4}=\frac{w}{\sqrt{w^2+4}}$, and the second is
$18\ln\abs{w+\sqrt{w^2+4}}$, as in the standard primitive
$\int\frac{dw}{\sqrt{w^2+c^2}}=\ln\abs{w+\sqrt{w^2+c^2}}$ with $c=2$, verified
by differentiating. Substituting $w=x-2$ gives the stated form.

:::

:::

:::


:::
