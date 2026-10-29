---
schema: qual/card@1
id: P-UCLAB02F-05
kind: problem
title: Optimal Lipschitz bound from bounded partial derivatives
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Fall 2002 PDF.
---

::: {.problem}
Suppose $f:\RR^2\to\RR$ has partial derivatives at every point and both partial derivatives are bounded in absolute value by $A>0$.

(a) Show that there is an $M>0$ such that
$$
|f(x,y)-f(x_1,y_1)|
\le M\sqrt{(x-x_1)^2+(y-y_1)^2}
$$
for all $(x,y),(x_1,y_1)\in\RR^2$.

(b) What is the smallest value of $M$, in terms of $A$, for which this always works?

(c) Give an example for which that value of $M$ makes the inequality an equality.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For all $(x,y),(x_1,y_1)\in\RR^2$,
$$
|f(x,y)-f(x_1,y_1)|
\le
A|x-x_1|+A|y-y_1|.
$$


::: pf-proof

Insert the intermediate point $(x_1,y)$ and use the triangle inequality:
$$
|f(x,y)-f(x_1,y_1)|
\le
|f(x,y)-f(x_1,y)|
+
|f(x_1,y)-f(x_1,y_1)|.
$$
For the one-variable function $u\mapsto f(u,y)$, the derivative is the first partial derivative of $f$, whose absolute value is at most $A$. The mean value theorem therefore gives
$$
|f(x,y)-f(x_1,y)|
\le
A|x-x_1|.
$$
Likewise, applying the mean value theorem to $v\mapsto f(x_1,v)$ gives
$$
|f(x_1,y)-f(x_1,y_1)|
\le
A|y-y_1|.
$$
Combining these inequalities proves the claim.

:::

:::

::: {.pf-step #s1-2}

One may take
$$
M=A\sqrt2.
$$


::: pf-proof

By step [](#s1-1){.pf-ref} and the Cauchy--Schwarz inequality,
$$
\begin{aligned}
|f(x,y)-f(x_1,y_1)|
&\le
A\bigl(|x-x_1|+|y-y_1|\bigr)\\
&\le
A\sqrt2\sqrt{(x-x_1)^2+(y-y_1)^2}.
\end{aligned}
$$
Thus the required estimate holds with $M=A\sqrt2$.

:::

:::

::: {.pf-step #s1-3}

No smaller universal value of $M$ can work.


::: pf-proof

Consider
$$
f(x,y)=A(x+y).
$$
Then
$$
f_x=f_y=A,
$$
so the hypotheses are satisfied. Taking $(x_1,y_1)=(0,0)$ and $(x,y)=(1,1)$ gives
$$
|f(1,1)-f(0,0)|=2A
$$
and
$$
\sqrt{(1-0)^2+(1-0)^2}=\sqrt2.
$$
Any valid universal constant must therefore satisfy
$$
2A\le M\sqrt2,
$$
so
$$
M\ge A\sqrt2.
$$
Together with step [](#s1-2){.pf-ref}, this proves that $A\sqrt2$ is optimal.

:::

:::

::: {.pf-step #s1-4}

For
$$
f(x,y)=A(x+y),
$$
the optimal estimate becomes an equality for any two points whose difference vector is a nonzero scalar multiple of $(1,1)$.


::: pf-proof

Let
$$
(x-x_1,y-y_1)=(t,t).
$$
Then
$$
|f(x,y)-f(x_1,y_1)|
=
2A|t|,
$$
while
$$
A\sqrt2\sqrt{(x-x_1)^2+(y-y_1)^2}
=
A\sqrt2\sqrt{2t^2}
=
2A|t|.
$$
Thus equality holds.

:::

:::

::: {.pf-step #s1-5}

Therefore the smallest possible constant is
$$
\boxed{M=A\sqrt2}.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} proves this constant always works, step [](#s1-3){.pf-ref} proves no smaller universal constant can work, and step [](#s1-4){.pf-ref} supplies an equality example.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} answers parts (a)--(c).

:::

:::

:::
