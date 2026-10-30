---
schema: qual/card@1
id: P-GRECH4-06
kind: problem
title: Integral curve through a specified point
classification:
  areas:
  - real-analysis
  topics:
  - Separable Equations
  - Integral Curves
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 4 review Question 6 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch4-review/, replacing the earlier chapter-4.pdf transcription.
---

::: {.problem}
Let $g\colon \RR \to \RR$ be a differentiable and integrable function. The integral curve of the differential equation

$$
[y + g(x)]\,dx + [x - g(y)]\,dy = 0
$$

that passes through the point $(1, 1)$ must also pass through which of the following points?

(A) $(0, 0)$
(B) $(2, \frac{1}{2})$
(C) $(\frac{1}{2}, 2)$
(D) $(-1, -1)$
(E) $(0, 1)$
:::

::: {.solution}

Let $G$ be an antiderivative of $g$.

::: pf

::: {.pf-step #s1-1}

The differential equation is exact, with potential
$$
F(x,y)=xy+G(x)-G(y).
$$


::: pf-proof

Set
$$
M(x,y)=y+g(x),
\qquad
N(x,y)=x-g(y).
$$
Then
$$
M_y=1=N_x,
$$
so the form is exact. Moreover,
$$
F_x=y+G'(x)=y+g(x)=M
$$
and
$$
F_y=x-G'(y)=x-g(y)=N.
$$
Thus $dF=M\,dx+N\,dy$.

:::

:::

::: {.pf-step #s1-2}

The integral curve through $(1,1)$ is contained in the level set
$$
F(x,y)=1.
$$


::: pf-proof

Along an integral curve, the differential equation gives $dF=0$ by step [](#s1-1){.pf-ref}, so $F$ is constant. At the specified point,
$$
F(1,1)
=1\cdot1+G(1)-G(1)
=1.
$$

:::

:::

::: {.pf-step #s1-3}

The point that must also lie on this level set is
$$
\boxed{(-1,-1)},
$$
so the answer is (D).


::: pf-proof

By the definition of $F$,
$$
F(-1,-1)
=(-1)(-1)+G(-1)-G(-1)
=1.
$$
Thus step [](#s1-2){.pf-ref} shows that $(-1,-1)$ lies on the same integral curve level set, independently of the particular function $g$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required point and corresponding choice.

:::

:::

:::
