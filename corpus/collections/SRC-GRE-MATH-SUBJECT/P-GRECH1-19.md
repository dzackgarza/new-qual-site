---
schema: qual/card@1
id: P-GRECH1-19
kind: problem
title: Formula for the inverse hyperbolic sine
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 19 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription. The book extraction repeated choice (C) as (D); the chapter-1.pdf extraction and the book's solution give log(x + sqrt(x^2+1)).
---

::: {.problem}
The hyperbolic sine function, denoted $\sinh$, is defined by the equation:

$$
\sinh x = \frac{e^x - e^{-x}}{2}
$$

Find a formula for $\sinh^{-1} x$.

(A) $\log(1 - \sqrt{x^2 + 1})$
(B) $\log(1 + \sqrt{x^2 + 1})$
(C) $\log(x - \sqrt{x^2 + 1})$
(D) $\log(x + \sqrt{x^2 + 1})$
(E) $\log(\sqrt{x^2 + 1} - x)$
:::

::: {.solution}

Let $y=\sinh^{-1}x$, so that $x=\sinh y$.

::: pf

::: {.pf-step #s1-1}

$e^y$ satisfies
$$
(e^y)^2-2xe^y-1=0.
$$


::: pf-proof

From the definition of hyperbolic sine,
$$
x=\frac{e^y-e^{-y}}2.
$$
Multiplying by $2e^y$ gives
$$
2xe^y=e^{2y}-1,
$$
which is the claimed quadratic equation in $e^y$.

:::

:::

::: {.pf-step #s1-2}

$e^y=x+\sqrt{x^2+1}$.


::: pf-proof

Solving the quadratic in step [](#s1-1){.pf-ref} gives
$$
e^y=x\pm\sqrt{x^2+1}.
$$
Since $\sqrt{x^2+1}>\abs{x}$, the quantity $x-\sqrt{x^2+1}$ is negative, while $x+\sqrt{x^2+1}$ is positive. Because $e^y>0$, only the positive sign is possible.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{\sinh^{-1}x=\log\left(x+\sqrt{x^2+1}\right)},
$$
so the answer is (D).


::: pf-proof

Taking logarithms in step [](#s1-2){.pf-ref} gives
$$
y=\log\left(x+\sqrt{x^2+1}\right).
$$
The expression inside the logarithm is positive by step [](#s1-2){.pf-ref}, so this is defined for every real $x$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested inverse formula and corresponding choice.

:::

:::

:::
