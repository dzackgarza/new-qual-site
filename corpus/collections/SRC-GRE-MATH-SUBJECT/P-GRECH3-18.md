---
schema: qual/card@1
id: P-GRECH3-18
kind: problem
title: Multivariable chain rule from tabulated derivatives
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
  note: "Checked against Chapter 3 review Question 18 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
Let $f$, $g$, and $h$ be functions of two variables that are differentiable everywhere such that $z=f(x,y)$, where $x=g(u,v)$ and $y=h(u,v)$. When $u=0$ and $v=1$, the values of $x$ and $y$ are $2$ and $1$, respectively. Let $P_0$ denote the point $(u,v)=(0,1)$, and let $Q_0$ denote the point $(x,y)=(2,1)$. Given the following data,
$$
\evaluated{\frac{\partial f}{\partial x}}_{Q_0}=11,\quad
\evaluated{\frac{\partial f}{\partial y}}_{Q_0}=-3,\quad
\evaluated{\frac{\partial g}{\partial u}}_{P_0}=1,\quad
\evaluated{\frac{\partial h}{\partial u}}_{P_0}=-3,\quad
\evaluated{\frac{\partial g}{\partial v}}_{P_0}=\evaluated{\frac{\partial h}{\partial v}}_{P_0}=2,
$$
what's the value of $\frac{\partial z}{\partial v}$ at $P_0$?

(A) $-21$
(B) $16$
(C) $15$
(D) $12$
(E) $-10$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The chain rule gives
$$
\frac{\partial z}{\partial v}
=
\frac{\partial f}{\partial x}\frac{\partial g}{\partial v}
+
\frac{\partial f}{\partial y}\frac{\partial h}{\partial v}.
$$


::: pf-proof

Since
$$
z=f(x,y),\qquad x=g(u,v),\qquad y=h(u,v),
$$
the composite is
$$
z(u,v)=f\bigl(g(u,v),h(u,v)\bigr).
$$
Differentiating this composite with respect to $v$ gives the displayed multivariable chain-rule formula.

:::

:::

::: {.pf-step #s1-2}

At $P_0=(0,1)$,
$$
\boxed{\frac{\partial z}{\partial v}=16},
$$
so the answer is (B).


::: pf-proof

At $P_0$, the intermediate point is $Q_0=(2,1)$. Substituting the supplied derivative values into step [](#s1-1){.pf-ref} gives
$$
\evaluated{\frac{\partial z}{\partial v}}_{P_0}
=
\evaluated{\frac{\partial f}{\partial x}}_{Q_0}
\evaluated{\frac{\partial g}{\partial v}}_{P_0}
+
\evaluated{\frac{\partial f}{\partial y}}_{Q_0}
\evaluated{\frac{\partial h}{\partial v}}_{P_0}
=(11)(2)+(-3)(2)
=16.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested partial derivative and corresponding choice.

:::

:::

:::
