---
schema: qual/card@1
id: P-UGR7G
kind: problem
title: $\int\frac{1}{9+x^2}\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
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
    its answer: the substitution and the resulting primitive were checked by differentiating the answer, which recovers the printed integrand
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. The primitive is verified by differentiation after the stated linear substitution.
---

::: {.problem}
Evaluate
$$
\int\frac{dx}{9+x^2}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #substitution}

With $x=3u$, so that $dx=3\,du$, the integrand becomes
$\frac{3\,du}{9+9u^2}=\frac{1}{3}\cdot\frac{du}{1+u^2}$.

::: pf-proof

Substituting $x=3u$ in $9+x^2$ gives $9+9u^2=9(1+u^2)$, and $dx=3\,du$; the
quotient is $\frac{3\,du}{9(1+u^2)}=\frac13\frac{du}{1+u^2}$.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\int\frac{dx}{9+x^2}=\frac13\arctan\left(\frac{x}{3}\right)+C}$
on $\RR$.

::: pf-proof

By step [](#substitution){.pf-ref} the integral is
$\frac13\int\frac{du}{1+u^2}=\frac13\arctan u+C$ with $u=x/3$, since
$\arctan'u=\frac{1}{1+u^2}$. Directly, $\frac{d}{dx}\left(\frac13\arctan\frac
x3\right)=\frac13\cdot\frac{1/3}{1+(x/3)^2}=\frac{1}{9+x^2}$, using the chain
rule; the integrand is continuous on $\RR$, so this is the general primitive.

:::

:::

:::


:::
