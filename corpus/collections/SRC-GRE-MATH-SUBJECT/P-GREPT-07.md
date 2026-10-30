---
schema: qual/card@1
id: P-GREPT-07
kind: problem
title: "Chain rule for $f=xy(x-y)$ with $x=t(t-u)$, $y=u(u-t)$"
classification:
  areas: [prelim]
  topics:
  - Chain Rule
  - Partial Derivatives
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 7 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $f(x, y) = xy(x - y)$, where $x(t, u) = t(t - u)$ and $y(t, u) = u(u - t)$. What is the value of $\frac{\partial f}{\partial t}$ at the point $(t, u) = (1, -1)$?

(A) $-8$
(B) $-4$
(C) $2$
(D) $4$
(E) $8$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The partial derivatives needed for the chain rule are
$$
f_x=2xy-y^2,
\qquad
f_y=x^2-2xy,
$$
and
$$
x_t=2t-u,
\qquad
y_t=-u.
$$


::: pf-proof

Since $f(x,y)=x^2y-xy^2$, differentiating with respect to $x$ and $y$
gives the first two formulas. From $x=t(t-u)=t^2-tu$ and
$y=u(u-t)=u^2-ut$, differentiating with respect to $t$ while holding $u$
fixed gives the second pair.

:::

:::

::: {.pf-step #s1-2}

At $(t,u)=(1,-1)$ one has
$$
(x,y)=(2,2),
$$
and hence
$$
f_x=4,
\qquad
f_y=-4,
\qquad
x_t=3,
\qquad
y_t=1.
$$


::: pf-proof

Substitution gives
$$
x=1(1-(-1))=2,
\qquad
y=(-1)(-1-1)=2.
$$
The remaining values follow by substituting $(x,y,t,u)=(2,2,1,-1)$ into
the formulas of step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\evaluated{\frac{\partial f}{\partial t}}_{(1,-1)}=\boxed{8},
$$
so the answer is (E).


::: pf-proof

By the multivariable chain rule and steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref},
$$
\frac{\partial f}{\partial t}
=f_xx_t+f_yy_t
=4(3)+(-4)(1)=8.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value.

:::

:::

:::
