---
schema: qual/card@1
id: P-GRECH3-22
kind: problem
title: Value at the unique local minimum
classification:
  areas:
  - real-analysis
  topics:
  - Critical Points
  - Multivariable Optimization
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 22 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
The function $f(x,y)=x^3+y^3-3xy$ has a local minimum at exactly one point, $P$. What's the value of $f$ at $P$?

(A) $-6$
(B) $-3$
(C) $-2$
(D) $-1$
(E) $0$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The only critical points of $f$ are
$$
(0,0)\qquad\text{and}\qquad(1,1).
$$


::: pf-proof

The first partial derivatives are
$$
f_x=3x^2-3y,\qquad
f_y=3y^2-3x.
$$
At a critical point,
$$
y=x^2,\qquad x=y^2.
$$
Substituting $y=x^2$ into $x=y^2$ gives
$$
x=x^4,
$$
so
$$
x(x^3-1)=0.
$$
Thus $x=0$ or $x=1$, and then $y=x^2$ gives the two displayed points.

:::

:::

::: {.pf-step #s1-2}

The point $(0,0)$ is a saddle point, while $(1,1)$ is a strict local minimum.


::: pf-proof

The Hessian matrix is
$$
H_f(x,y)=
\begin{pmatrix}
6x & -3\\
-3 & 6y
\end{pmatrix},
$$
whose determinant is
$$
\Delta(x,y)=36xy-9.
$$
At $(0,0)$,
$$
\Delta(0,0)=-9<0,
$$
so the point is a saddle. At $(1,1)$,
$$
\Delta(1,1)=27>0
\qquad\text{and}\qquad
f_{xx}(1,1)=6>0,
$$
so the second-derivative test gives a strict local minimum there. By step [](#s1-1){.pf-ref} there are no other critical points, hence no other local minima.

:::

:::

::: {.pf-step #s1-3}

At the unique local minimum,
$$
\boxed{f(1,1)=-1},
$$
so the answer is (D).


::: pf-proof

By step [](#s1-2){.pf-ref}, the minimum point is $P=(1,1)$. Therefore
$$
f(P)=1^3+1^3-3(1)(1)=-1.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value and corresponding choice.

:::

:::

:::
