---
schema: qual/card@1
id: P-TRIV-RA23
kind: problem
title: $\int_0^{x_0}\sqrt{1-x^2/x_0^2}\,dx$
classification:
  areas: [real-analysis]
  topics:
  - Definite Integrals
  - Substitution
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 23, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find $\int_0^{x_0} \sqrt{1 - \frac{x^2}{x_0^2}}\, dx$.
:::

::: {.solution}

Assume $x_0>0$.

::: pf

::: {.pf-step #s1-1}

Set
$$
u=\frac{x}{x_0}.
$$
Then
$$
x=x_0u,
\qquad
dx=x_0\,du.
$$


::: pf-proof

This is the linear change of variables $x=x_0u$.

:::

:::

::: {.pf-step #s1-2}

The limits transform as
$$
x=0\longmapsto u=0,
\qquad
x=x_0\longmapsto u=1.
$$


::: pf-proof

Substitute the endpoints into $u=x/x_0$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\int_0^{x_0}
\sqrt{1-\frac{x^2}{x_0^2}}\,dx
=
x_0
\int_0^1\sqrt{1-u^2}\,du.
$$


::: pf-proof

Substitute the relations from steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\int_0^1\sqrt{1-u^2}\,du
=
\frac\pi4.
$$


::: pf-proof

The graph
$$
v=\sqrt{1-u^2},
\qquad
0\leq u\leq1,
$$
is the upper-right quarter of the unit circle
$$
u^2+v^2=1.
$$
Hence the integral is the area of a quarter of a unit disk:
$$
\frac14\pi(1)^2
=
\frac\pi4.
$$

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{
\int_0^{x_0}
\sqrt{1-\frac{x^2}{x_0^2}}\,dx
=
\frac{\pi x_0}{4}.
}
$$


::: pf-proof

Combine steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required value.

:::

:::

:::
