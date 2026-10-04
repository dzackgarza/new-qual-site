---
schema: qual/card@1
id: P-TRIV-RA16
kind: problem
title: $\int\log x\,dx$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 16, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
$\mathrm { C a l c u l a t e } \int \log { x d x } .$
:::

::: {.solution}
Assume $x>0$.

<1>1. Use integration by parts with
$$
u=\log x,
\qquad
dv=dx.
$$

::: {.proof}
Then
$$
du=\frac{dx}{x},
\qquad
v=x.
$$
:::

<1>2. Therefore
$$
\int\log x\,dx
=
x\log x
-
\int1\,dx.
$$

::: {.proof}
Apply
$$
\int u\,dv=uv-\int v\,du
$$
using step <1>1.
:::

<1>3. Hence
$$
\boxed{
\int\log x\,dx
=
x\log x-x+C.
}
$$

::: {.proof}
Evaluate the remaining integral in step <1>2.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required antiderivative.
:::
:::
