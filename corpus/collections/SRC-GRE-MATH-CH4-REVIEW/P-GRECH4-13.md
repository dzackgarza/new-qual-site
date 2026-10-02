---
schema: qual/card@1
id: P-GRECH4-13
kind: problem
title: Orthogonal trajectories of tangent circles
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 4 review Question 13 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch4-review/, replacing the earlier chapter-4.pdf transcription.
---

::: {.problem}
Consider the family $F$ of circles in the $xy$-plane, $(x - c)^2 + y^2 = c^2$, that are tangent to the $y$-axis at the origin. Which of the following gives the differential equation that is satisfied by the family of curves orthogonal to $F$?

(A) $y' = \frac{x}{x - y}$
(B) $y' = \frac{x}{y - x}$
(C) $y' = \frac{xy}{x - y}$
(D) $y' = \frac{2xy}{x^2 - y^2}$
(E) $y' = \frac{2xy}{y^2 - x^2}$
:::

::: {.solution}
<1>1. Away from the origin, the parameter $c$ on a circle of the family is
$$
c=\frac{x^2+y^2}{2x}.
$$

::: {.proof}
Expanding the family equation gives
$$
(x-c)^2+y^2=c^2
\iff
x^2-2cx+y^2=0.
$$
At a non-origin point of one of these circles, $x\ne0$, so solving for $c$ gives the displayed formula.
:::

<1>2. The slope of a circle in the family at a regular point is
$$
\frac{dy}{dx}
=\frac{y^2-x^2}{2xy}.
$$

::: {.proof}
Implicit differentiation of
$$
(x-c)^2+y^2=c^2
$$
with $c$ fixed gives
$$
2(x-c)+2yy'=0,
$$
hence
$$
y'=\frac{c-x}{y}.
$$
Substituting the expression for $c$ from step <1>1 gives
$$
y'
=
\frac{\frac{x^2+y^2}{2x}-x}{y}
=\frac{y^2-x^2}{2xy}.
$$
:::

<1>3. The differential equation for the orthogonal trajectories is
$$
\boxed{y'=\frac{2xy}{x^2-y^2}},
$$
so the answer is (D).

::: {.proof}
At a regular intersection, orthogonal curves have slopes whose product is $-1$. Thus the orthogonal slope is the negative reciprocal of the slope in step <1>2:
$$
-\frac{1}{(y^2-x^2)/(2xy)}
=\frac{2xy}{x^2-y^2}.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested differential equation and corresponding choice.
:::
:::
