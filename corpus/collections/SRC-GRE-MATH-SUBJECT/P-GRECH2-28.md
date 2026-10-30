---
schema: qual/card@1
id: P-GRECH2-28
kind: problem
title: Antiderivative of $x^2/\sqrt{1-x^2}$
classification:
  areas: [prelim]
  topics:
  - Trigonometric Substitution
  - Antiderivatives
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 28 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Integrate $\int \frac{x^2 dx}{\sqrt{1-x^2}}$.

(A) $\frac{1}{2} \left( \arcsin x - \sqrt{1-x^2} \right) + c$
(B) $\frac{1}{2} \left( \arcsin x + x\sqrt{1-x^2} \right) + c$
(C) $\frac{1}{2} \left( x \arcsin x - \sqrt{1-x^2} \right) + c$
(D) $\frac{1}{2} \left( \arcsin x - x\sqrt{1-x^2} \right) + c$
(E) $\frac{1}{2} \left( x \arcsin x + \sqrt{1-x^2} \right) + c$
:::

::: {.solution}

Set $x=\sin\theta$ with $\theta=\arcsin x$.

::: pf

::: {.pf-step #s1-1}

The integral becomes
$$
\int \sin^2\theta\,d\theta.
$$


::: pf-proof

On the principal range of $\arcsin$, one has
$$
\cos\theta=\sqrt{1-\sin^2\theta}=\sqrt{1-x^2}\ge0
$$
and
$$
dx=\cos\theta\,d\theta.
$$
Therefore
$$
\frac{x^2\,dx}{\sqrt{1-x^2}}
=\frac{\sin^2\theta\cos\theta\,d\theta}{\cos\theta}
=\sin^2\theta\,d\theta.
$$

:::

:::

::: {.pf-step #s1-2}

An antiderivative is
$$
\frac12\left(\theta-\sin\theta\cos\theta\right)+C.
$$


::: pf-proof

Using
$$
\sin^2\theta=\frac{1-\cos2\theta}{2},
$$
step [](#s1-1){.pf-ref} gives
$$
\int\sin^2\theta\,d\theta
=\frac\theta2-\frac{\sin2\theta}{4}+C
=\frac12\left(\theta-\sin\theta\cos\theta\right)+C.
$$

:::

:::

::: {.pf-step #s1-3}

Returning to $x$ gives
$$
\boxed{\frac12\left(\arcsin x-x\sqrt{1-x^2}\right)+C},
$$
so the answer is (D).


::: pf-proof

Since $\theta=\arcsin x$, $\sin\theta=x$, and $\cos\theta=\sqrt{1-x^2}$, substitution into step [](#s1-2){.pf-ref} gives the displayed antiderivative.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested antiderivative and corresponding choice.

:::

:::

:::
