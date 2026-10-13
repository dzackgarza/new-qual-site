---
schema: qual/card@1
id: P-GRECH6-04
kind: problem
title: A forced congruence modulo 13
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
  note: "Re-transcribed from Chapter 6 review Question 4 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/extracted/chapter-6.md, replacing the earlier paraphrased transcription."
---

::: {.problem}
If $x$, $y$, and $z$ are positive integers such that $4x - 5y + 2z$ is divisible by $13$, then which one of the following must also be divisible by $13$?

(A) $x + 13y - z$
(B) $6x - 10y - z$
(C) $x - y - 2z$
(D) $-7x + 12y + 3z$
(E) $-5x + 3y - 4z$
:::

::: {.solution}
<1>1. The hypothesis is
$$
4x-5y+2z\equiv0\pmod{13}.
$$

::: {.proof}
An integer is divisible by $13$ exactly when it is congruent to $0$ modulo $13$.
:::

<1>2. Under the hypothesis in step <1>1,
$$
-7x+12y+3z\equiv0\pmod{13}.
$$

::: {.proof}
Modulo $13$,
$$
\begin{aligned}
-7x+12y+3z
&\equiv 32x-40y+16z\\
&=8(4x-5y+2z)\\
&\equiv0.
\end{aligned}
$$
Here the first congruence holds because the coefficient differences are $-39$, $52$, and $-13$, all divisible by $13$.
:::

<1>3. None of choices (A), (B), (C), or (E) is forced by the hypothesis.

::: {.proof}
Take $(x,y,z)=(2,2,1)$. Then
$$
4x-5y+2z=8-10+2=0,
$$
so the hypothesis holds. The four expressions in choices (A), (B), (C), and (E) then have values
$$
27,\qquad -9,\qquad -2,\qquad -8,
$$
respectively, none of which is divisible by $13$.
:::

<1>4. Therefore the expression that must be divisible by $13$ is
$$
\boxed{-7x+12y+3z},
$$
so the answer is (D).

::: {.proof}
Step <1>2 proves that choice (D) is always divisible by $13$, while step <1>3 rules out every other choice.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 identifies the unique required expression.
:::
:::
