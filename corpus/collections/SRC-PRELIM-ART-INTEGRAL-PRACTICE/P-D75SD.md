---
schema: qual/card@1
id: P-D75SD
kind: problem
title: $\int\sin(x)\cos(\cos(x))\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - u-Substitution
  - Trigonometry
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
    its answer: the substitution u = cos x and the resulting primitive, checked by differentiating the answer through the chain rule
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
\int \sin x\,\cos(\cos x)\,dx.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #substitution}

With $u=\cos x$, $du=-\sin x\,dx$, so $\sin x\cos(\cos x)\,dx=-\cos u\,du$.

::: pf-proof

$\frac{du}{dx}=-\sin x$ by the derivative of the cosine, and substituting
$u=\cos x$ in the integrand turns $\sin x\cos(\cos x)\,dx$ into $-\cos u\,du$;
the substitution is legitimate on any interval on which $\cos$ is smooth,
which is all of $\RR$.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\int\sin x\cos(\cos x)\,dx=-\sin(\cos x)+C}$ on $\RR$.

::: pf-proof

By step [](#substitution){.pf-ref} the integral is $-\int\cos u\,du=-\sin
u+C$, and substituting back $u=\cos x$ gives $-\sin(\cos x)+C$. Directly,
$\frac{d}{dx}\left(-\sin(\cos x)\right)=-\cos(\cos x)\cdot(-\sin x)=\sin
x\cos(\cos x)$ by the chain rule, and the integrand is continuous on $\RR$, so
these are all the primitives.

:::

:::

:::


:::
