---
schema: qual/card@1
id: P-GRECH1-23
kind: problem
title: "Evaluate $\\tan(2\\arcsin(1/3))$"
classification:
  areas:
  - algebra
  topics:
  - Inverse Trigonometric Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 23 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
Simplify $\tan(2 \arcsin \frac{1}{3})$.

(A) $\frac{2\sqrt{2}}{9}$
(B) $\frac{\sqrt{2}}{3}$
(C) $\frac{3}{4}$
(D) $\frac{4\sqrt{2}}{7}$
(E) $\frac{6}{5}$
:::

::: {.solution}

Set $\theta=\arcsin(1/3)$.

::: pf

::: {.pf-step #s1-1}

$\tan\theta=\frac{1}{2\sqrt2}$.


::: pf-proof

Since $\theta\in[-\pi/2,\pi/2]$ and $\sin\theta=1/3>0$, one has $0<\theta<\pi/2$, so $\cos\theta>0$. Hence
$$
\cos\theta
=\sqrt{1-\sin^2\theta}
=\sqrt{1-\frac19}
=\frac{2\sqrt2}{3}.
$$
Therefore
$$
\tan\theta
=\frac{\sin\theta}{\cos\theta}
=\frac{1/3}{2\sqrt2/3}
=\frac{1}{2\sqrt2}.
$$

:::

:::

::: {.pf-step #s1-2}

The requested value is
$$
\boxed{\tan(2\theta)=\frac{4\sqrt2}{7}},
$$
so the answer is (D).


::: pf-proof

Using the tangent double-angle formula and step [](#s1-1){.pf-ref},
$$
\tan(2\theta)
=\frac{2\tan\theta}{1-\tan^2\theta}
=\frac{1/\sqrt2}{1-1/8}
=\frac{8}{7\sqrt2}
=\frac{4\sqrt2}{7}.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested simplified value and corresponding choice.

:::

:::

:::
