---
schema: qual/card@1
id: P-GRECH6-19
kind: problem
title: Solutions of $x^{12}-x^{10}=2$ in $\ZZ_{11}$
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
  note: "Re-transcribed from Chapter 6 review Question 19 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/extracted/chapter-6.md, replacing the earlier paraphrased transcription."
---

::: {.problem}
How many elements $x$ in the field $\ZZ_{11}$ satisfy the equation $x^{12} - x^{10} = 2$?

(A) $1$
(B) $2$
(C) $3$
(D) $4$
(E) $5$
:::

::: {.solution}
<1>1. Any solution $x\in\ZZ_{11}$ is nonzero and therefore satisfies $x^{10}=1$.

::: {.proof}
The element $x=0$ does not satisfy the equation because its left-hand side is $0$, not $2$. Hence any solution lies in $\ZZ_{11}^{\times}$. Fermat's little theorem then gives $x^{10}=1$.
:::

<1>2. For nonzero $x$, the original equation is equivalent to
$$
x^2=3
$$
in $\ZZ_{11}$.

::: {.proof}
Factor the left-hand side as
$$
x^{12}-x^{10}=x^{10}(x^2-1).
$$
Using step <1>1, the equation becomes $x^2-1=2$, which is equivalent to $x^2=3$.
:::

<1>3. The equation $x^2=3$ has exactly the two solutions $x=5$ and $x=6$ in $\ZZ_{11}$.

::: {.proof}
Directly,
$$
5^2=25\equiv3\pmod{11},
\qquad
6^2=36\equiv3\pmod{11}.
$$
These are distinct. The polynomial $X^2-3$ has degree $2$ over the field $\ZZ_{11}$, so it has at most two roots. Hence there are no others.
:::

<1>4. Therefore the number of solutions is
$$
\boxed{2},
$$
so the answer is (B).

::: {.proof}
Step <1>3 gives the complete solution set.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested number.
:::
:::
