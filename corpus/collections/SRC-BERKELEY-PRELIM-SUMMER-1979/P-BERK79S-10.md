---
schema: qual/card@1
id: P-BERK79S-10
kind: problem
title: All solutions of the linear system $x'=2x-y$, $y'=x$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used y'=x to eliminate x. Then
    y''=x'=2x-y=2y'-y, so (D-1)^2y=0 and
    y=(a+bt)e^t. Differentiating recovers
    x=(a+b+bt)e^t, and direct substitution verifies that every such pair is
    a solution.
---

::: {.problem}
Find all pairs of $C^\infty$ functions $x,y:\mathbb R\to\mathbb R$ satisfying
\[
x'(t)=2x(t)-y(t),
\qquad
y'(t)=x(t).
\]
:::

::: {.solution}
<1>1. Every solution satisfies
$$
y''-2y'+y=0.
$$

::: {.proof}
The second equation gives
$$
y'=x.
$$
Differentiating,
$$
y''=x'.
$$
The first equation then yields
$$
y''
=
2x-y
=
2y'-y.
$$
Rearranging gives the claimed second-order equation.
:::

<1>2. The characteristic polynomial of the equation in step <1>1 is
$$
r^2-2r+1=(r-1)^2.
$$

::: {.proof}
Substituting the trial function
$$
y(t)=e^{rt}
$$
into
$$
y''-2y'+y=0
$$
gives
$$
(r^2-2r+1)e^{rt}=0.
$$
Since $e^{rt}\neq0$, the characteristic equation is the displayed
polynomial equation.
:::

<1>3. Every real solution of the equation in step <1>1 has the form
$$
y(t)=(a+bt)e^t
$$
for some $a,b\in\RR$.

::: {.proof}
Step <1>2 gives the repeated characteristic root
$$
r=1
$$
of multiplicity $2$. The standard solution basis for a repeated root is
$$
e^t,\qquad te^t.
$$
Hence
$$
y(t)=ae^t+bte^t=(a+bt)e^t.
$$
:::

<1>4. For a solution from step <1>3, the second equation forces
$$
x(t)=(a+b+bt)e^t.
$$

::: {.proof}
Since
$$
x=y',
$$
differentiate:
$$
\begin{aligned}
x(t)
&=
\frac{d}{dt}\bigl((a+bt)e^t\bigr)\\
&=
be^t+(a+bt)e^t\\
&=
(a+b+bt)e^t.
\end{aligned}
$$
:::

<1>5. For every $a,b\in\RR$, the pair
$$
\boxed{
\begin{aligned}
y(t)&=(a+bt)e^t,\\
x(t)&=(a+b+bt)e^t
\end{aligned}
}
$$
satisfies the original system.

::: {.proof}
From step <1>4,
$$
y'(t)=x(t).
$$
Also,
$$
\begin{aligned}
x'(t)
&=
\frac{d}{dt}\bigl((a+b+bt)e^t\bigr)\\
&=
be^t+(a+b+bt)e^t\\
&=
(a+2b+bt)e^t,
\end{aligned}
$$
while
$$
\begin{aligned}
2x(t)-y(t)
&=
2(a+b+bt)e^t-(a+bt)e^t\\
&=
(a+2b+bt)e^t.
\end{aligned}
$$
Thus
$$
x'=2x-y
$$
as well.
:::

<1>6. Every solution of the original system occurs uniquely in the form
given in step <1>5.

::: {.proof}
Step <1>1 shows that the $y$-component of every solution must solve the
second-order equation there. Step <1>3 gives its complete two-parameter
solution family, and step <1>4 uniquely determines $x$ from $y$. Hence no
other solutions occur.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>5--<1>6 give exactly all required pairs.
:::
:::
