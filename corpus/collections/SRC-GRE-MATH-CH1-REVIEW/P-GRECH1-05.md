---
schema: qual/card@1
id: P-GRECH1-05
kind: problem
title: Evaluate a composition using an inverse function
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
  note: Re-transcribed from Chapter 1 review Question 5 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
Let $f$ be a real-valued function whose inverse is given by the equation:

\[
f^{-1}(x) = x(1 + x^2) + (1 - x^2)
\]

What's the value of $f(f^{-1}(f(2)))$?

(A) $-2$
(B) $-1$
(C) $1$
(D) $2$
(E) $7$
:::

::: {.solution}
<1>1. $f^{-1}(1)=2$.

::: {.proof}
Substituting $x=1$ into the given formula gives
$$
f^{-1}(1)=1(1+1^2)+(1-1^2)=2.
$$
:::

<1>2. $f(2)=1$.

::: {.proof}
Apply $f$ to the equality in step <1>1. Since $f\circ f^{-1}$ is the identity on the domain of $f^{-1}$,
$$
f(2)=f\bigl(f^{-1}(1)\bigr)=1.
$$
:::

<1>3. The requested value is
$$
f\bigl(f^{-1}(f(2))\bigr)=\boxed{1},
$$
so the answer is (C).

::: {.proof}
The inverse identity gives
$$
f\bigl(f^{-1}(f(2))\bigr)=f(2),
$$
and step <1>2 evaluates the right-hand side.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested value and choice.
:::
:::
