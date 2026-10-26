---
schema: qual/card@1
id: P-TRIV-RA18
kind: problem
title: $\int e^{2x}\sin x\,dx$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 18, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
$\mathrm { C a l c u l a t e } \int e ^ { 2 x } \sin { x } d x .$
:::

Let
$$
I=\int e^{2x}\sin x\,dx.
$$

::: pf

::: pf-step

Integration by parts gives
$$
I
=
\frac12e^{2x}\sin x
-
\frac12\int e^{2x}\cos x\,dx.
$$


::: pf-proof

Take $u=\sin x$ and $dv=e^{2x}\,dx$.

:::

:::

::: pf-step

If
$$
J=\int e^{2x}\cos x\,dx,
$$
then
$$
J
=
\frac12e^{2x}\cos x
+
\frac12I.
$$


::: pf-proof

Integrate $J$ by parts with $u=\cos x$ and $dv=e^{2x}\,dx$.

:::

:::

::: pf-step

Substituting step <1>2 into step <1>1 gives
$$
I
=
\frac12e^{2x}\sin x
-
\frac14e^{2x}\cos x
-
\frac14I.
$$


::: pf-proof

Replace the cosine integral in step <1>1 by $J$ from step <1>2.

:::

:::

::: pf-step

Therefore
$$
\boxed{
\int e^{2x}\sin x\,dx
=
\frac{e^{2x}}5
\bigl(2\sin x-\cos x\bigr)
+
C.
}
$$


::: pf-proof

Move $-I/4$ in step <1>3 to the left:
$$
\frac54I
=
\frac12e^{2x}\sin x
-
\frac14e^{2x}\cos x.
$$
Multiplying by $4/5$ gives
$$
I
=
\frac{e^{2x}}5
\bigl(2\sin x-\cos x\bigr)
+
C.
$$

:::

:::

::: pf-qed

Step <1>4 is the required antiderivative.

:::

:::
