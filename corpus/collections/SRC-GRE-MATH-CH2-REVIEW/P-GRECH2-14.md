---
schema: qual/card@1
id: P-GRECH2-14
kind: problem
title: Derivative at $0$ of $2|x-1|+(x-1)^2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 14 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
If $f(x) = 2|x - 1| + (x - 1)^2$, what is the value of $f'(0)$?

(A) $4$
(B) $2$
(C) $0$
(D) $-2$
(E) $-4$
:::

::: {.solution}
<1>1. In a neighborhood of $x=0$,
$$
f(x)=2(1-x)+(x-1)^2.
$$

::: {.proof}
For every $x<1$,
$$
|x-1|=1-x.
$$
In particular this identity holds throughout a neighborhood of $0$, so substituting it into the definition of $f$ gives the displayed formula.
:::

<1>2. In that neighborhood,
$$
f'(x)=2x-4.
$$

::: {.proof}
Differentiate the expression from step <1>1:
$$
f'(x)=-2+2(x-1)=2x-4.
$$
:::

<1>3. Therefore
$$
\boxed{f'(0)=-4},
$$
so the answer is (E).

::: {.proof}
Substituting $x=0$ into the derivative from step <1>2 gives $f'(0)=-4$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested derivative value and corresponding choice.
:::
:::
