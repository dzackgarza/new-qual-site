---
schema: qual/card@1
id: P-GRECH2-15
kind: problem
title: Tangent slope of $e^x\arccos x/\cos x$ at its $y$-intercept
classification:
  areas: [prelim]
  topics:
  - Differentiation
  - Tangent Lines
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 15 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
If

$$
f(x) = \frac{e^x \arccos x}{\cos x}
$$

then the slope of the line tangent to the graph of $f$ at its $y$-intercept is

(A) $-\frac{\pi}{2}$
(B) $-1$
(C) $\frac{\pi}{2} - 1$
(D) $1$
(E) $\frac{\pi}{2} + 1$
:::

::: {.solution}

The $y$-intercept occurs at $x=0$, so the required slope is $f'(0)$.

::: pf

::: {.pf-step #s1-1}

Writing
$$
f(x)=e^x(\arccos x)\sec x,
$$
one has
$$
f'(x)
=e^x(\arccos x)\sec x
-\frac{e^x\sec x}{\sqrt{1-x^2}}
+e^x(\arccos x)\sec x\tan x.
$$


::: pf-proof

Apply the product rule to the three factors $e^x$, $\arccos x$, and $\sec x$, using
$$
\frac{d}{dx}\arccos x=-\frac1{\sqrt{1-x^2}}
$$
and
$$
\frac{d}{dx}\sec x=\sec x\tan x.
$$

:::

:::

::: {.pf-step #s1-2}

The tangent slope is
$$
\boxed{f'(0)=\frac\pi2-1},
$$
so the answer is (C).


::: pf-proof

Substitute
$$
e^0=1,\qquad \arccos0=\frac\pi2,\qquad \sec0=1,\qquad \tan0=0
$$
into step [](#s1-1){.pf-ref}. This gives
$$
f'(0)=\frac\pi2-1+0.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the slope at the $y$-intercept and corresponding choice.

:::

:::

:::
