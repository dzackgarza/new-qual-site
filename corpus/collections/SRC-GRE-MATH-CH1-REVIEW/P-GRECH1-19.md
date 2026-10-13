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

\[
\sinh x = \frac{e^x - e^{-x}}{2}
\]

Find a formula for $\sinh^{-1} x$.

(A) $\log(1 - \sqrt{x^2 + 1})$
(B) $\log(1 + \sqrt{x^2 + 1})$
(C) $\log(x - \sqrt{x^2 + 1})$
(D) $\log(x + \sqrt{x^2 + 1})$
(E) $\log(\sqrt{x^2 + 1} - x)$
:::

::: {.solution}
Let $y=\sinh^{-1}x$, so that $x=\sinh y$.

<1>1. $e^y$ satisfies
$$
(e^y)^2-2xe^y-1=0.
$$

::: {.proof}
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

<1>2. $e^y=x+\sqrt{x^2+1}$.

::: {.proof}
Solving the quadratic in step <1>1 gives
$$
e^y=x\pm\sqrt{x^2+1}.
$$
Since $\sqrt{x^2+1}>|x|$, the quantity $x-\sqrt{x^2+1}$ is negative, while $x+\sqrt{x^2+1}$ is positive. Because $e^y>0$, only the positive sign is possible.
:::

<1>3. Therefore
$$
\boxed{\sinh^{-1}x=\log\left(x+\sqrt{x^2+1}\right)},
$$
so the answer is (D).

::: {.proof}
Taking logarithms in step <1>2 gives
$$
y=\log\left(x+\sqrt{x^2+1}\right).
$$
The expression inside the logarithm is positive by step <1>2, so this is defined for every real $x$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested inverse formula and corresponding choice.
:::
:::
