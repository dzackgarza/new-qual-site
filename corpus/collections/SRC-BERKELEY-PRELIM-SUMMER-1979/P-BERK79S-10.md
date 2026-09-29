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

::: pf

::: {.pf-step #s1}

Every solution satisfies
$$
y''-2y'+y=0.
$$

::: pf-proof

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

:::

::: {.pf-step #s2}

The characteristic polynomial of the equation in step [](#s1){.pf-ref} is
$$
r^2-2r+1=(r-1)^2.
$$

::: pf-proof

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

:::

::: {.pf-step #s3}

Every real solution of the equation in step [](#s1){.pf-ref} has the form
$$
y(t)=(a+bt)e^t
$$
for some $a,b\in\RR$.

::: pf-proof

Step [](#s2){.pf-ref} gives the repeated characteristic root
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

:::

::: {.pf-step #s4}

For a solution from step [](#s3){.pf-ref}, the second equation forces
$$
x(t)=(a+b+bt)e^t.
$$

::: pf-proof

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

:::

::: {.pf-step #s5}

For every $a,b\in\RR$, the pair
$$
\boxed{
\begin{aligned}
y(t)&=(a+bt)e^t,\\
x(t)&=(a+b+bt)e^t
\end{aligned}
}
$$
satisfies the original system.

::: pf-proof

From step [](#s4){.pf-ref},
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

:::

::: {.pf-step #s6}

Every solution of the original system occurs uniquely in the form
given in step [](#s5){.pf-ref}.

::: pf-proof

Step [](#s1){.pf-ref} shows that the $y$-component of every solution must solve the
second-order equation there. Step [](#s3){.pf-ref} gives its complete two-parameter
solution family, and step [](#s4){.pf-ref} uniquely determines $x$ from $y$. Hence no
other solutions occur.

:::

:::

::: pf-qed

Steps [](#s5){.pf-ref} and [](#s6){.pf-ref} give exactly all required pairs.

:::

:::

:::
