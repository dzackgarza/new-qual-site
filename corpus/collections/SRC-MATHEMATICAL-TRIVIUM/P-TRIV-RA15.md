---
schema: qual/card@1
id: P-TRIV-RA15
kind: problem
title: $\int\cot x\,dx$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 15, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
$\mathrm { C a l c u l a t e } \int \frac { d x } { \tan x }$
:::

::: {.solution}
<1>1. One has
$$
\frac1{\tan x}
=
\frac{\cos x}{\sin x}.
$$

::: {.proof}
Since
$$
\tan x=\frac{\sin x}{\cos x},
$$
taking the reciprocal gives the identity wherever the integrand is defined.
:::

<1>2. Set
$$
u=\sin x.
$$
Then
$$
du=\cos x\,dx.
$$

::: {.proof}
Differentiate $u=\sin x$.
:::

<1>3. Therefore
$$
\int\frac{dx}{\tan x}
=
\int\frac{du}{u}
=
\boxed{\log|\sin x|+C}.
$$

::: {.proof}
Use steps <1>1--<1>2 and the antiderivative
$$
\int\frac{du}{u}=\log|u|+C.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required antiderivative on each interval where
$\sin x\neq0$.
:::
:::
