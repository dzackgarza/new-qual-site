---
schema: qual/card@1
id: P-GRECH7-26
kind: problem
title: Harmonic conjugate of $x-3x^2y+y^3$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 26 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. Both extractions read 3x^{2y}; the book's Chapter 8 solution reads v = x - 3x^2y + y^3.
---

::: {.problem}
Which of the following is a harmonic conjugate $u(x, y)$ of the harmonic function $v = x - 3x^2y + y^3$?

(A) $x^3 - 3xy^2 + y$
(B) $-x^3 + 3xy^2 - y$
(C) $-y^3 + 3x^2y - x$
(D) $y^3 - 3x^2y + x$
(E) $-x^3 + 3xy^2$
:::

::: {.solution}
<1>1. If $u$ is a harmonic conjugate of
$$
v(x,y)=x-3x^2y+y^3,
$$
then the Cauchy--Riemann equations require
$$
u_x=-3x^2+3y^2
$$
and
$$
u_y=-1+6xy.
$$

::: {.proof}
For an analytic function $f=u+iv$, the Cauchy--Riemann equations are
$$
u_x=v_y,
\qquad
u_y=-v_x.
$$
Here
$$
v_y=-3x^2+3y^2
$$
and
$$
v_x=1-6xy,
$$
which gives the displayed requirements.
:::

<1>2. Integrating the first equation in step <1>1 with respect to $x$ gives
$$
u(x,y)=-x^3+3xy^2+g(y)
$$
for some function $g$ of $y$ alone.

::: {.proof}
An antiderivative in $x$ of $-3x^2+3y^2$ is
$$
-x^3+3xy^2.
$$
The integration constant may depend on the parameter $y$, giving $g(y)$.
:::

<1>3. The second Cauchy--Riemann equation forces
$$
g(y)=-y+C
$$
for some real constant $C$.

::: {.proof}
Differentiating the expression in step <1>2 with respect to $y$ gives
$$
u_y=6xy+g'(y).
$$
Comparing with $u_y=-1+6xy$ from step <1>1 yields $g'(y)=-1$, hence $g(y)=-y+C$.
:::

<1>4. Thus one harmonic conjugate is
$$
\boxed{u(x,y)=-x^3+3xy^2-y},
$$
so the answer is (B).

::: {.proof}
Take $C=0$ in step <1>3. Adding a real constant gives the other harmonic conjugates, and the displayed choice is exactly option (B).
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested harmonic conjugate.
:::
:::
