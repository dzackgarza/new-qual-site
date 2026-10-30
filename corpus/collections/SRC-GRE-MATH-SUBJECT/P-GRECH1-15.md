---
schema: qual/card@1
id: P-GRECH1-15
kind: problem
title: Relate quadratic coefficients under squaring roots
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Vieta's Formulas
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 15 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
If the roots of the equation $x^2 + Bx + 1 = 0$ are the squares of the roots of the equation $x^2 + bx + 1 = 0$, which of the following expresses $B$ in terms of $b$?

(A) $2 - b^2$
(B) $1 - b^2$
(C) $b^2 - 1$
(D) $b^2$
(E) $b^2 - 2$
:::

::: {.solution}

Let $r$ and $s$ be the roots of $x^2+bx+1$.

::: pf

::: {.pf-step #s1-1}

$r+s=-b$ and $rs=1$.


::: pf-proof

These are Viète's formulas for the monic quadratic $x^2+bx+1$.

:::

:::

::: {.pf-step #s1-2}

$r^2+s^2=b^2-2$.


::: pf-proof

Using step [](#s1-1){.pf-ref},
$$
r^2+s^2=(r+s)^2-2rs=(-b)^2-2=b^2-2.
$$

:::

:::

::: {.pf-step #s1-3}

The coefficient is
$$
\boxed{B=2-b^2},
$$
so the answer is (A).


::: pf-proof

By hypothesis, the roots of $x^2+Bx+1$ are $r^2$ and $s^2$. Their sum is therefore $-B$ by Viète's formulas. Step [](#s1-2){.pf-ref} gives
$$
-B=b^2-2,
$$
which is equivalent to the displayed value of $B$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested expression and corresponding choice.

:::

:::

:::
