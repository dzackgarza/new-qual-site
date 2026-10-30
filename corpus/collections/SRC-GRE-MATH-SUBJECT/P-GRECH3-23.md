---
schema: qual/card@1
id: P-GRECH3-23
kind: problem
title: Minimum distance to a quadratic curve
classification:
  areas:
  - real-analysis
  topics:
  - Multivariable Optimization
  - Lagrange Multipliers
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 23 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree. Choices (D) and (E) read as two digits before the square root in both extractions."
---

::: {.problem}
Find the minimum distance from the origin to the curve $3x^2+4xy+3y^2=20$.

(A) $1$
(B) $3\sqrt{2}$
(C) $2$
(D) $2\,3\sqrt{2}$
(E) $5\,3\sqrt{2}$
:::

::: {.remark}
The source prints choices (D) and (E) as the digits $2,3$ and $5,3$ followed by $\sqrt{2}$, with no fraction bar.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every point on the curve satisfies
$$
x^2+y^2\ge4.
$$


::: pf-proof

For all real $x,y$,
$$
5(x^2+y^2)-(3x^2+4xy+3y^2)
=2(x-y)^2
\ge0.
$$
Hence
$$
3x^2+4xy+3y^2\le5(x^2+y^2).
$$
On the given curve the left-hand side is $20$, so
$$
20\le5(x^2+y^2),
$$
which gives $x^2+y^2\ge4$.

:::

:::

::: {.pf-step #s1-2}

The lower bound in step [](#s1-1){.pf-ref} is attained on the curve.


::: pf-proof

Equality in step [](#s1-1){.pf-ref} occurs when $x=y$. Substituting $y=x$ into the curve equation gives
$$
3x^2+4x^2+3x^2=10x^2=20,
$$
so $x^2=2$. Thus the points
$$
(\sqrt2,\sqrt2)
\qquad\text{and}\qquad
(-\sqrt2,-\sqrt2)
$$
lie on the curve and satisfy $x^2+y^2=4$.

:::

:::

::: {.pf-step #s1-3}

The minimum distance from the origin to the curve is
$$
\boxed{2},
$$
so the answer is (C).


::: pf-proof

The distance from the origin to $(x,y)$ is $\sqrt{x^2+y^2}$. Step [](#s1-1){.pf-ref} gives the lower bound $2$, and step [](#s1-2){.pf-ref} exhibits points on the curve where this bound is attained.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested minimum distance and corresponding choice.

:::

:::

:::
