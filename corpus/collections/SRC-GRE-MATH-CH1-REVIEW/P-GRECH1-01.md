---
schema: qual/card@1
id: P-GRECH1-01
kind: problem
title: Sum of roots of a radical equation
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
  note: Re-transcribed from Chapter 1 review Question 1 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
Find the sum of the roots of the equation $\sqrt{x-1} + \sqrt{2x-1} = x$.

(A) $1$
(B) $2$
(C) $4$
(D) $5$
(E) $6$
:::

::: {.solution}
<1>1. Every real solution satisfies $x\geq1$.

::: {.proof}
The radical $\sqrt{x-1}$ is real only when $x-1\geq0$.
:::

<1>2. Every solution satisfies
$$
2\sqrt{2x-1}=x+1.
$$

::: {.proof}
Move the second radical to the right:
$$
\sqrt{x-1}=x-\sqrt{2x-1}.
$$
Squaring gives
$$
x-1=x^2-2x\sqrt{2x-1}+2x-1,
$$
hence
$$
2x\sqrt{2x-1}=x^2+x.
$$
By step <1>1, $x\geq1$, so division by $x$ is valid and gives the claim.
:::

<1>3. Every solution belongs to $\{1,5\}$.

::: {.proof}
Squaring the equation from step <1>2 gives
$$
4(2x-1)=(x+1)^2,
$$
so
$$
x^2-6x+5=0
\iff
(x-1)(x-5)=0.
$$
:::

<1>4. Both $1$ and $5$ satisfy the original equation.

::: {.proof}
For $x=1$,
$$
\sqrt{1-1}+\sqrt{2-1}=0+1=1.
$$
For $x=5$,
$$
\sqrt{5-1}+\sqrt{10-1}=2+3=5.
$$
Thus no extraneous root introduced by squaring remains.
:::

<1>5. The sum of the roots is
$$
\boxed{6},
$$
so the answer is (E).

::: {.proof}
By steps <1>3 and <1>4, the complete set of roots is $\{1,5\}$, whose sum is
$1+5=6$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the requested sum and choice.
:::
:::
