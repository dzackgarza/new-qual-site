---
schema: qual/card@1
id: P-GREPT-20
kind: problem
title: "Point where the partial derivatives of $x^y$ agree"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 20 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $f(x, y) = x^y$, for $x > 0$. Then $\evaluated{\frac{\partial f}{\partial x}}_P = \evaluated{\frac{\partial f}{\partial y}}_P$ at the point $P = (e, y_0)$, where $y_0 =$

(A) $1$
(B) $\sqrt{e}$
(C) $e$
(D) $e^2$
(E) $e^e$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $x>0$,
$$
\frac{\partial f}{\partial x}=yx^{y-1}
\qquad\text{and}\qquad
\frac{\partial f}{\partial y}=x^y\log x.
$$


::: pf-proof

Holding $y$ fixed and differentiating $x^y$ with respect to $x$ gives the
first formula. For the second, write
$$
x^y=e^{y\log x}
$$
and differentiate with respect to $y$.

:::

:::

::: {.pf-step #s1-2}

At $P=(e,y_0)$, equality of the two partial derivatives is equivalent
to
$$
y_0=e.
$$


::: pf-proof

Substituting $x=e$ into the formulas of step [](#s1-1){.pf-ref} gives
$$
y_0e^{y_0-1}=e^{y_0}\log e=e^{y_0}.
$$
Since $e^{y_0-1}>0$, dividing by it gives $y_0=e$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
y_0=\boxed{e},
$$
so the answer is (C).


::: pf-proof

Step [](#s1-2){.pf-ref} determines the unique value for which the two partial derivatives
agree at the prescribed point.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value.

:::

:::

:::
