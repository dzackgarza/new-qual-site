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
Find $\int _ { 0 } ^ { \infty } x ^ { n } e ^ { - x } d x , n \in \mathbb { Z } , n > 0 .$
:::

::: {.solution}
For $n\geq0$, define
$$
I_n=
\int_0^\infty x^n e^{-x}\,dx.
$$

<1>1. One has
$$
I_0=1.
$$

::: {.proof}
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

<1>2. For every integer $n\geq1$,
$$
I_n=nI_{n-1}.
$$

::: {.proof}
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

<1>3. Therefore
$$
I_n=n!.
$$

::: {.proof}
Iterating step <1>2 gives
$$
I_n
=
n(n-1)\cdots1\,I_0.
$$
Use step <1>1.
:::

<1>4. Hence
$$
\boxed{
\int_0^\infty x^n e^{-x}\,dx=n!.
}
$$

::: {.proof}
This is step <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required value.
:::
:::
