---
schema: qual/card@1
id: P-GRECH1-15
kind: problem
title: Relate quadratic coefficients under squaring roots
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

<1>1. $r+s=-b$ and $rs=1$.

::: {.proof}
These are Viète's formulas for the monic quadratic $x^2+bx+1$.
:::

<1>2. $r^2+s^2=b^2-2$.

::: {.proof}
Using step <1>1,
$$
r^2+s^2=(r+s)^2-2rs=(-b)^2-2=b^2-2.
$$
:::

<1>3. The coefficient is
$$
\boxed{B=2-b^2},
$$
so the answer is (A).

::: {.proof}
By hypothesis, the roots of $x^2+Bx+1$ are $r^2$ and $s^2$. Their sum is therefore $-B$ by Viète's formulas. Step <1>2 gives
$$
-B=b^2-2,
$$
which is equivalent to the displayed value of $B$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested expression and corresponding choice.
:::
:::
