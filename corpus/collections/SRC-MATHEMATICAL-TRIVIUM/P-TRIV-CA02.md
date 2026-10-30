---
schema: qual/card@1
id: P-TRIV-CA02
kind: problem
title: Cartesian forms of $e^{i\theta}$, $3e^{i\pi/4}$, $\frac12 e^{i\pi}$, $2e^{2i\pi/3}$ and $e^{-3i\pi/4}$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 2, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Write the following complex numbers in cartesian form
$$
e^{i\theta}, \qquad 3e^{i\pi/4}, \qquad \frac{1}{2}e^{i\pi}, \qquad 2e^{2i\pi/3}, \qquad e^{-3i\pi/4}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Euler's formula gives
$$
e^{i\theta}
=
\cos\theta+i\sin\theta.
$$


::: pf-proof

This is the standard identity
$$
e^{it}=\cos t+i\sin t
$$
for real $t$.

:::

:::

::: {.pf-step #s1-2}

One has
$$
3e^{i\pi/4}
=
\boxed{
\frac{3\sqrt2}{2}
+
i\frac{3\sqrt2}{2}
}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
3e^{i\pi/4}
=
3\left(
\cos\frac\pi4
+
i\sin\frac\pi4
\right).
$$
Since
$$
\cos\frac\pi4
=
\sin\frac\pi4
=
\frac{\sqrt2}{2},
$$
the displayed value follows.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\frac12e^{i\pi}
=
\boxed{-\frac12}.
$$


::: pf-proof

Since
$$
\cos\pi=-1
\qquad\text{and}\qquad
\sin\pi=0,
$$
Euler's formula gives
$$
e^{i\pi}=-1.
$$

:::

:::

::: {.pf-step #s1-4}

One has
$$
2e^{2i\pi/3}
=
\boxed{-1+i\sqrt3}.
$$


::: pf-proof

Euler's formula gives
$$
2e^{2i\pi/3}
=
2\left(
\cos\frac{2\pi}{3}
+
i\sin\frac{2\pi}{3}
\right).
$$
Now
$$
\cos\frac{2\pi}{3}
=
-\frac12,
\qquad
\sin\frac{2\pi}{3}
=
\frac{\sqrt3}{2}.
$$
Multiplying by $2$ gives the result.

:::

:::

::: {.pf-step #s1-5}

One has
$$
e^{-3i\pi/4}
=
\boxed{
-\frac{\sqrt2}{2}
-
i\frac{\sqrt2}{2}
}.
$$


::: pf-proof

By Euler's formula,
$$
e^{-3i\pi/4}
=
\cos\left(-\frac{3\pi}{4}\right)
+
i\sin\left(-\frac{3\pi}{4}\right).
$$
Using evenness of cosine and oddness of sine,
$$
\cos\left(-\frac{3\pi}{4}\right)
=
-\frac{\sqrt2}{2},
$$
and
$$
\sin\left(-\frac{3\pi}{4}\right)
=
-\frac{\sqrt2}{2}.
$$

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref} give the Cartesian forms of all five numbers.

:::

:::

:::
