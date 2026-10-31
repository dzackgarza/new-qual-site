---
schema: qual/card@1
id: P-TRIV-RA18
kind: problem
title: $\int e^{2x}\sin x\,dx$
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
  note: Checked against Real Analysis, Problem 18, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Calculate $\int e^{2x}\sin x\, dx$.
:::

::: {.solution}

Let
$$
I=\int e^{2x}\sin x\,dx.
$$

::: pf

::: {.pf-step #s1-1}

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

::: {.pf-step #s1-2}

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

::: {.pf-step #s1-3}

Substituting step [](#s1-2){.pf-ref} into step [](#s1-1){.pf-ref} gives
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

Replace the cosine integral in step [](#s1-1){.pf-ref} by $J$ from step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

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

Move $-I/4$ in step [](#s1-3){.pf-ref} to the left:
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

Step [](#s1-4){.pf-ref} is the required antiderivative.

:::

:::

:::
