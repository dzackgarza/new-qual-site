---
schema: qual/card@1
id: P-BKS12-9B
kind: problem
title: Infinitely many integer solutions of $x^2-2y^2=7$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 6 of the retained Spring 2012 solution PDF and independently reviewed its Pell-type family.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked integrality, preservation of x^2-2y^2 under multiplication by 3+2sqrt(2), and strict growth of the resulting solutions.
---

::: {.problem}
Show that there are infinitely many integer solutions of $x ^ { 2 } - 2 y ^ { 2 } = 7$
:::

::: {.solution}
For $n\geq0$, define real numbers $x_n,y_n$ by
$$
x_n+y_n\sqrt2
\coloneqq
(3+\sqrt2)(3+2\sqrt2)^n.
$$

<1>1. The numbers $x_n$ and $y_n$ are integers for every $n\geq0$.

::: {.proof}
For $n=0$,
$$
x_0=3,
\qquad
y_0=1.
$$
If
$$
x_n+y_n\sqrt2
$$
has integer coefficients, then
$$
\begin{aligned}
x_{n+1}+y_{n+1}\sqrt2
&=
(x_n+y_n\sqrt2)(3+2\sqrt2)\\
&=
(3x_n+4y_n)
+
(2x_n+3y_n)\sqrt2.
\end{aligned}
$$
Thus
$$
x_{n+1}=3x_n+4y_n,
\qquad
y_{n+1}=2x_n+3y_n,
$$
which are integers. Induction proves the claim.
:::

<1>2. For every $n\geq0$,
$$
x_n^2-2y_n^2=7.
$$

::: {.proof}
Multiply the defining identity by its conjugate:
$$
\begin{aligned}
x_n^2-2y_n^2
&=
(3+\sqrt2)(3-\sqrt2)
\bigl((3+2\sqrt2)(3-2\sqrt2)\bigr)^n\\
&=
(9-2)(9-8)^n\\
&=
7.
\end{aligned}
$$
:::

<1>3. The sequences $x_n$ and $y_n$ are positive and strictly increasing.

::: {.proof}
The initial values $x_0=3$ and $y_0=1$ are positive. If $x_n,y_n>0$, the
recurrences from step <1>1 give
$$
x_{n+1}
=
3x_n+4y_n
>
x_n
$$
and
$$
y_{n+1}
=
2x_n+3y_n
>
y_n.
$$
Induction proves positivity and strict increase.
:::

<1>4. The pairs
$$
\boxed{(x_n,y_n),\qquad n=0,1,2,\ldots}
$$
are infinitely many distinct integer solutions of
$$
x^2-2y^2=7.
$$

::: {.proof}
Step <1>1 gives integrality and step <1>2 gives the equation. Step <1>3
shows that the first coordinates $x_n$ are strictly increasing, so the
pairs are all distinct.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 supplies infinitely many integer solutions.
:::
:::
