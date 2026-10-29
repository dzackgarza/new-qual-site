---
schema: qual/card@1
id: P-TRIV-RA20
kind: problem
title: $\int_0^\infty x^ne^{-x}\,dx=n!$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 20, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find $\int _ { 0 } ^ { \infty } x ^ { n } e ^ { - x } d x , n \in \ZZ , n > 0 .$
:::

::: {.solution}

For $n\geq0$, define
$$
I_n=
\int_0^\infty x^n e^{-x}\,dx.
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
I_0=1.
$$


::: pf-proof

Directly,
$$
I_0
=
\int_0^\infty e^{-x}\,dx
=
\left[-e^{-x}\right]_0^\infty
=1.
$$

:::

:::

::: {.pf-step #s1-2}

For every integer $n\geq1$,
$$
I_n=nI_{n-1}.
$$


::: pf-proof

Integrate by parts with
$$
u=x^n,
\qquad
dv=e^{-x}\,dx.
$$
Then
$$
du=nx^{n-1}\,dx,
\qquad
v=-e^{-x}.
$$
Hence
$$
I_n
=
\left[-x^n e^{-x}\right]_0^\infty
+
n\int_0^\infty x^{n-1}e^{-x}\,dx.
$$
The boundary term vanishes because
$$
x^n e^{-x}\to0
$$
as $x\to\infty$, and it is $0$ at $x=0$. Thus
$$
I_n=nI_{n-1}.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
I_n=n!.
$$


::: pf-proof

Iterating step [](#s1-2){.pf-ref} gives
$$
I_n
=
n(n-1)\cdots1\,I_0.
$$
Use step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Hence
$$
\boxed{
\int_0^\infty x^n e^{-x}\,dx=n!.
}
$$


::: pf-proof

This is step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required value.

:::

:::

:::
