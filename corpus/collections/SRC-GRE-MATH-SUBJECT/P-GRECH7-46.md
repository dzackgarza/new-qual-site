---
schema: qual/card@1
id: P-GRECH7-46
kind: problem
title: Solutions of $\cos z=3$
classification:
  areas: [complex-analysis]
  topics:
  - Complex Trigonometric Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 46 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The five choices are garbled identically in both extractions and no longer differ as printed; the book's Chapter 8 solution gives z = 2k pi - i log(3 +/- 2 sqrt 2).
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The retained choices all print $\sqrt{2i}$ for $\sqrt2$, and (B)=(C), (A)=(D)=(E), so no printed choice is correct. The statement now asks for all solutions without choices.
---

::: {.problem}
Find all complex numbers $z$ with $\cos z=3$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If
$$
w=e^{iz},
$$
then $\cos z=3$ is equivalent to
$$
w^2-6w+1=0.
$$


::: pf-proof

Using
$$
\cos z=\frac{e^{iz}+e^{-iz}}{2},
$$
the equation becomes
$$
e^{iz}+e^{-iz}=6.
$$
Multiplying by $e^{iz}=w\ne0$ gives
$$
w^2+1=6w,
$$
which is the displayed quadratic equation.

:::

:::

::: {.pf-step #s1-2}

The two possible values of $w$ are
$$
w=3\pm2\sqrt2.
$$


::: pf-proof

The quadratic formula applied to step [](#s1-1){.pf-ref} gives
$$
w=\frac{6\pm\sqrt{36-4}}{2}
=\frac{6\pm4\sqrt2}{2}
=3\pm2\sqrt2.
$$
Both values are positive real numbers, and their product is $1$.

:::

:::

::: {.pf-step #s1-3}

For either value of $w$ in step [](#s1-2){.pf-ref}, all solutions of $e^{iz}=w$ are
$$
z=2k\pi-i\log w,
\qquad k\in\ZZ.
$$


::: pf-proof

Since $w>0$, the solutions of $e^{iz}=w$ satisfy
$$
iz=\log w+2k\pi i,
\qquad k\in\ZZ.
$$
Multiplying by $-i$ gives the displayed formula.

:::

:::

::: pf-step

Hence the complete solution set is
$$
\boxed{z=2k\pi-i\log(3\pm2\sqrt2),\qquad k\in\ZZ}.
$$


::: pf-proof

Substitute the two values of $w$ from step [](#s1-2){.pf-ref} into step [](#s1-3){.pf-ref}. Conversely, every number obtained this way satisfies $e^{iz}=3\pm2\sqrt2$ and hence the quadratic relation in step [](#s1-1){.pf-ref}, so it satisfies $\cos z=3$.

:::

:::

:::

:::
