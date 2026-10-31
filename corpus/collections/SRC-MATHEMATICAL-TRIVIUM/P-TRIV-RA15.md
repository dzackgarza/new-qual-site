---
schema: qual/card@1
id: P-TRIV-RA15
kind: problem
title: $\int\cot x\,dx$
classification:
  areas: [real-analysis]
  topics:
  - Antiderivatives
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 15, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Calculate $\int \frac{dx}{\tan x}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

One has
$$
\frac1{\tan x}
=
\frac{\cos x}{\sin x}.
$$


::: pf-proof

Since
$$
\tan x=\frac{\sin x}{\cos x},
$$
taking the reciprocal gives the identity wherever the integrand is defined.

:::

:::

::: {.pf-step #s1-2}

Set
$$
u=\sin x.
$$
Then
$$
du=\cos x\,dx.
$$


::: pf-proof

Differentiate $u=\sin x$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\int\frac{dx}{\tan x}
=
\int\frac{du}{u}
=
\boxed{\log\abs{\sin x}+C}.
$$


::: pf-proof

Use steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} and the antiderivative
$$
\int\frac{du}{u}=\log\abs{u}+C.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required antiderivative on each interval where
$\sin x\neq0$.

:::

:::

:::
