---
schema: qual/card@1
id: P-JIAQR
kind: problem
title: $\int\frac{x}{1+x^4}\,dx$
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
    its answer: the substitution u = x^2 and the resulting primitive, checked by differentiating the answer
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. The substitution and the primitive, verified by differentiation.
---

::: {.problem}
Evaluate
$$
\int\frac{x}{1+x^4}\,dx.
$$
:::

::: {.solution}

The integrand is defined and continuous on $\RR$, since $1+x^4\ge1$.

::: pf

::: {.pf-step #substitution}

With $u=x^2$, $du=2x\,dx$ and $1+x^4=1+u^2$, so
$\dfrac{x\,dx}{1+x^4}=\dfrac12\cdot\dfrac{du}{1+u^2}$.

::: pf-proof

The derivative of $x^2$ is $2x$, so $x\,dx=\frac12du$, and $x^4=(x^2)^2=u^2$;
hence the integrand is $\frac12\cdot\frac{1}{1+u^2}$ in the variable $u$.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\int\frac{x}{1+x^4}\,dx=\frac12\arctan(x^2)+C}$ on $\RR$.

::: pf-proof

By step [](#substitution){.pf-ref} the integral is
$\frac12\int\frac{du}{1+u^2}=\frac12\arctan u+C=\frac12\arctan(x^2)+C$, using
$\arctan'u=\frac{1}{1+u^2}$. Directly,
$\frac{d}{dx}\frac12\arctan(x^2)=\frac12\cdot\frac{2x}{1+x^4}=\frac{x}{1+x^4}$
by the chain rule, and the integrand is continuous on the connected interval
$\RR$.

:::

:::

:::


:::
