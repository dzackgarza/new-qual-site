---
schema: qual/card@1
id: P-BKS84-6
kind: problem
title: Convergence criterion for the iteration $x_{n+1}=a+x_n^2$
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
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Checked necessity from the limiting fixed-point equation and sufficiency by monotone iteration below the smaller fixed point.
---

::: {.problem}
Let $a>0$ and define
\[
x_0=0,
\qquad
x_{n+1}=a+x_n^2.
\]
Find a necessary and sufficient condition on $a$ for the finite limit
\[
\lim_{n\to\infty}x_n
\]
to exist.
:::

::: {.solution}
<1>1. If $(x_n)$ has a finite limit, then
$$
a\leq\frac14.
$$

::: {.proof}
Suppose
$$
x_n\longrightarrow L\in\RR.
$$
Passing to the limit in
$$
x_{n+1}=a+x_n^2
$$
gives
$$
L=a+L^2.
$$
Thus $L$ is a real root of
$$
t^2-t+a=0.
$$
Its discriminant must be nonnegative:
$$
1-4a\geq0.
$$
Therefore $a\leq1/4$.
:::

<1>2. Assume
$$
0<a\leq\frac14
$$
and set
$$
r\coloneqq\frac{1-\sqrt{1-4a}}2.
$$
Then
$$
0<r\leq\frac12
\qquad\text{and}\qquad
a+r^2=r.
$$

::: {.proof}
The displayed value $r$ is the smaller real root of
$$
t^2-t+a=0.
$$
Since $0<a\leq1/4$, one has
$0\leq\sqrt{1-4a}<1$, which gives $0<r\leq1/2$. The root equation is
equivalent to $a+r^2=r$.
:::

<1>3. For every $n\geq0$,
$$
0\leq x_n\leq r.
$$

::: {.proof}
The claim holds for $n=0$ because $x_0=0$. If $0\leq x_n\leq r$, then
$$
0
<
x_{n+1}
=
a+x_n^2
\leq
a+r^2
=
r
$$
by step <1>2. Induction proves the claim.
:::

<1>4. The sequence $(x_n)$ is strictly increasing.

::: {.proof}
First,
$$
x_1=a>0=x_0.
$$
If $x_n>x_{n-1}\geq0$, then
$$
x_{n+1}-x_n
=
x_n^2-x_{n-1}^2
=
(x_n-x_{n-1})(x_n+x_{n-1})
>
0.
$$
Induction gives $x_{n+1}>x_n$ for every $n$.
:::

<1>5. If $0<a\leq1/4$, then
$$
\lim_{n\to\infty}x_n
=
r
=
\frac{1-\sqrt{1-4a}}2.
$$

::: {.proof}
Steps <1>3--<1>4 show that $(x_n)$ is increasing and bounded above, hence
it converges to some finite $L$. As in step <1>1,
$$
L=a+L^2,
$$
so $L$ is one of the two roots
$$
r
=
\frac{1-\sqrt{1-4a}}2,
\qquad
s
=
\frac{1+\sqrt{1-4a}}2.
$$
Step <1>3 gives $L\leq r$, while $r\leq s$. Hence $L=r$.
:::

<1>6. The necessary and sufficient condition is
$$
\boxed{0<a\leq\frac14}.
$$

::: {.proof}
Necessity is step <1>1, and sufficiency is step <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is exactly the requested criterion.
:::
:::
