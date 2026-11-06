---
schema: qual/card@1
id: P-NKCDN
kind: problem
title: $\int e^x\cos x\,dx$ and $\int\sin(\ln x)\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Integration by Parts
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
    its answer: both primitives, the first by two integrations by parts and the second by the substitution u = ln x reducing it to the first, each checked by differentiating
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. Two integrations by parts for the first, and a substitution reducing the second to it.
---

::: {.problem}
Evaluate
$$
\int e^x\cos x\,dx
\qquad\text{and}\qquad
\int\sin(\ln x)\,dx,
\quad x>0.
$$
:::

::: {.solution}

The first integrand is continuous on $\RR$; the second on $x>0$, where $\ln x$
is defined.

::: pf

::: {.pf-step #exponential-cosine}

$\displaystyle\int e^x\cos x\,dx=\frac12e^x(\cos x+\sin x)+C$.

::: pf-proof

Integrating by parts with $u=\cos x$, $dv=e^xdx$ gives $I=e^x\cos x+\int
e^x\sin x\,dx$, and a second integration by parts with $u=\sin x$ gives $\int
e^x\sin x\,dx=e^x\sin x-I$. Substituting, $I=e^x\cos x+e^x\sin x-I$, so
$2I=e^x(\cos x+\sin x)$ and $I=\frac12e^x(\cos x+\sin x)+C$; differentiating
the answer returns $e^x\cos x$, which checks it.

:::

:::

::: {.pf-step #log-sine}

$\displaystyle\int\sin(\ln x)\,dx=\frac x2\left(\sin(\ln x)-\cos(\ln
x)\right)+C$ on $x>0$.

::: pf-proof

With $u=\ln x$, $x=e^u$ and $dx=e^u\,du$, so the integral is $\int e^u\sin
u\,du$, whose primitive is $\frac12e^u(\sin u-\cos u)$ computed exactly as in
step [](#exponential-cosine){.pf-ref} with $\cos$ and $\sin$ interchanged.
Substituting back $u=\ln x$ and $e^u=x$ gives the stated form; differentiating
it gives $\frac12(\sin u-\cos u)+\frac12(\cos u+\sin u)=\sin u=\sin(\ln x)$ by
the chain rule.

:::

:::

:::


:::
