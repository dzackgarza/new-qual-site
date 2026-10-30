---
schema: qual/card@1
id: P-GRECH1-16
kind: problem
title: Imaginary parts of the roots of a cubic
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Complex Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 16 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
Find the largest value of $b$ such that $1 + bi$ satisfies the equation

$$
x^3 - 3x^2 + 6x - 4 = 0
$$

given that every root of this equation has the form $1 + bi$ (where $b$ is real).

(A) $1$
(B) $\sqrt{2}$
(C) $\sqrt{3}$
(D) $2$
(E) $3$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The cubic factors as
$$
x^3-3x^2+6x-4=(x-1)(x^2-2x+4).
$$


::: pf-proof

Multiplying out the right-hand side gives
$$
x^3-2x^2+4x-x^2+2x-4
=x^3-3x^2+6x-4.
$$

:::

:::

::: {.pf-step #s1-2}

The three roots are
$$
1,\qquad 1+i\sqrt3,\qquad 1-i\sqrt3.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives the real root $x=1$. For the quadratic factor,
$$
x=\frac{2\pm\sqrt{4-16}}2
=\frac{2\pm\sqrt{-12}}2
=1\pm i\sqrt3.
$$

:::

:::

::: {.pf-step #s1-3}

The largest real $b$ for which $1+bi$ is a root is
$$
\boxed{\sqrt3},
$$
so the answer is (C).


::: pf-proof

By step [](#s1-2){.pf-ref}, the three corresponding values of $b$ are $0$, $\sqrt3$, and $-\sqrt3$. Their largest value is $\sqrt3$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value and corresponding choice.

:::

:::

:::
