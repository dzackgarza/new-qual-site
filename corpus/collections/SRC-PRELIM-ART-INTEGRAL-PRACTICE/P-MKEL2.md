---
schema: qual/card@1
id: P-MKEL2
kind: problem
title: $\int\frac{dx}{e^x+e^{-x}}$ and $\int\frac{dx}{\sqrt{e^{2x}-1}}$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - u-Substitution
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Corrected the sign of the arcsine antiderivative in the second integral.
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
    its answer: the identity relating the first two integrands, both substitutions and the identity relating the two forms of the third primitive, each checked by differentiating
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. Two substitutions, a second substitution giving an equivalent primitive, and the constant relating them computed from a right triangle.
---

::: {.problem}
Evaluate
$$
\int\frac{dx}{e^x+e^{-x}},
\qquad
\int\frac{e^x}{1+e^{2x}}\,dx,
$$
and, on the real domain $x>0$,
$$
\int\frac{dx}{\sqrt{e^{2x}-1}}.
$$
:::

::: {.solution}

All three integrands are continuous on their stated domains, and
$e^x+e^{-x}>0$ and $1+e^{2x}>0$ everywhere.

::: pf

::: {.pf-step #hyperbolic}

$\dfrac{1}{e^x+e^{-x}}=\dfrac{e^x}{1+e^{2x}}$, so the first two integrals are
the same, and with $u=e^x$ both equal $\arctan(e^x)+C$.

::: pf-proof

Multiplying numerator and denominator of $\frac1{e^x+e^{-x}}$ by $e^x$ gives
$\frac{e^x}{e^{2x}+1}$, which is the second integrand. With $u=e^x$,
$du=e^x\,dx$ and $e^{2x}=u^2$, so
$\int\frac{e^x\,dx}{1+e^{2x}}=\int\frac{du}{1+u^2}=\arctan
u+C=\arctan(e^x)+C$; directly,
$\frac{d}{dx}\arctan(e^x)=\frac{e^x}{1+e^{2x}}$, and the derivative equals
$\frac{1}{e^x+e^{-x}}$ by the identity.

:::

:::

::: {.pf-step #radical}

On $x>0$, with $u=e^{-x}$, $\sqrt{e^{2x}-1}=\dfrac{\sqrt{1-u^2}}{u}$ and
$dx=-\dfrac{du}{u}$, so
$\displaystyle\int\frac{dx}{\sqrt{e^{2x}-1}}=-\arcsin(e^{-x})+C$.

::: pf-proof

$u=e^{-x}\in(0,1)$ for $x>0$, and
$e^{2x}-1=\frac{1}{u^2}-1=\frac{1-u^2}{u^2}$, whose square root is
$\frac{\sqrt{1-u^2}}{u}$ because $u>0$; also $du=-e^{-x}dx=-u\,dx$, so
$dx=-\frac{du}{u}$. Hence the integrand is
$\frac{-du/u}{\sqrt{1-u^2}/u}=-\frac{du}{\sqrt{1-u^2}}$, whose primitive is
$-\arcsin u+C$; the derivative of $-\arcsin(e^{-x})$ is
$-\frac{1}{\sqrt{1-e^{-2x}}}\cdot(-e^{-x})=\frac{e^{-x}}{\sqrt{1-e^{-2x}}}=\frac{1}{\sqrt{e^{2x}-1}}$,
which is the integrand.

:::

:::

::: {.pf-step #equivalent}

The same integral on $x>0$ is $\arctan\sqrt{e^{2x}-1}+C'$, and the two
primitives differ by the constant $\pi/2$.

::: pf-proof

With $v=\sqrt{e^{2x}-1}$ one has $v^2+1=e^{2x}$ and
$dv=\frac{e^{2x}}{v}dx=\frac{v^2+1}{v}dx$, so $dx=\frac{v\,dv}{v^2+1}$ and the
integrand is $\frac{dv}{v^2+1}$, whose primitive is $\arctan v$. For the
relation, $\sin(\pi/2-\arctan v)=\cos(\arctan
v)=\frac{1}{\sqrt{1+v^2}}=e^{-x}$, so $\pi/2-\arctan v=\arcsin(e^{-x})$, that
is $-\arcsin(e^{-x})=\arctan v-\pi/2$.

:::

:::

:::


:::
