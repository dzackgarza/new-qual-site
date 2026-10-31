---
schema: qual/card@1
id: P-TRIV-RA16
kind: problem
title: $\int\log x\,dx$
classification:
  areas: [real-analysis]
  topics:
  - Antiderivatives
  - Integration by Parts
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 16, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Calculate $\int \log x\, dx$.
:::

::: {.solution}

Assume $x>0$.

::: pf

::: {.pf-step #s1-1}

Use integration by parts with
$$
u=\log x,
\qquad
dv=dx.
$$


::: pf-proof

Then
$$
du=\frac{dx}{x},
\qquad
v=x.
$$

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\int\log x\,dx
=
x\log x
-
\int1\,dx.
$$


::: pf-proof

Apply
$$
\int u\,dv=uv-\int v\,du
$$
using step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Hence
$$
\boxed{
\int\log x\,dx
=
x\log x-x+C.
}
$$


::: pf-proof

Evaluate the remaining integral in step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required antiderivative.

:::

:::

:::
