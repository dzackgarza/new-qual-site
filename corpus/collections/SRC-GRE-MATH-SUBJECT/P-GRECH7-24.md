---
schema: qual/card@1
id: P-GRECH7-24
kind: problem
title: Complex solutions of $e^{2z}=i$
classification:
  areas: [complex-analysis]
  topics:
  - Complex Exponential
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 24 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
What are the complex roots of the equation $e^{2z} = i$?

(A) $\left(\frac{i}{2}\right)\left(-\frac{\pi}{2} + 2n\pi\right)$
(B) $(2i)\left(-\frac{\pi}{2} + n\pi\right)$
(C) $\left(\frac{i}{2}\right)\left(\frac{\pi}{2} + n\pi\right)$
(D) $(2i)\left(\frac{\pi}{2} + 2n\pi\right)$
(E) $\left(\frac{i}{2}\right)\left(\frac{\pi}{2} + 2n\pi\right)$
:::

::: {.solution}

Write $z=x+iy$ with $x,y\in\RR$.

::: pf

::: {.pf-step #s1-1}

Any solution satisfies $x=0$.


::: pf-proof

Taking absolute values in
$$
e^{2z}=i
$$
gives
$$
e^{2x}=\abs{i}=1.
$$
Since the real exponential is injective, $2x=0$, hence $x=0$.

:::

:::

::: {.pf-step #s1-2}

The imaginary part satisfies
$$
2y=\frac\pi2+2n\pi,
\qquad n\in\ZZ.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, the equation becomes
$$
e^{2iy}=i.
$$
The arguments of $i$ are exactly
$$
\frac\pi2+2n\pi,
\qquad n\in\ZZ,
$$
so the displayed congruence for $2y$ follows.

:::

:::

::: {.pf-step #s1-3}

Therefore all solutions are
$$
\boxed{z=\frac{i}{2}\left(\frac\pi2+2n\pi\right),\qquad n\in\ZZ},
$$
so the answer is (E).


::: pf-proof

Solving step [](#s1-2){.pf-ref} for $y$ gives
$$
y=\frac12\left(\frac\pi2+2n\pi\right).
$$
Together with $x=0$ from step [](#s1-1){.pf-ref}, this yields the displayed formula for $z$. Substitution gives
$$
e^{2z}=e^{i(\pi/2+2n\pi)}=i,
$$
so every listed value is indeed a solution.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the complete solution set.

:::

:::

:::
