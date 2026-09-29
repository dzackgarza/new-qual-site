---
schema: qual/card@1
id: P-BKF13-1A
kind: problem
title: Intersection point of the two branches of $x^y=y^x$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 1A in the retained Fall 2013 Berkeley prelim exam
    and independently reviewed the retained solution packet F13_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the off-diagonal parametrization and its unique limiting point on
    the diagonal as the parameter tends to 1.
---

::: {.problem}
The set of pairs of positive real numbers $( x , y )$ with $x ^ { y } = y ^ { x }$ is a union of two smooth curves.\
Find the point where they intersect.
:::

::: {.solution}
Let
$$
D\coloneqq\{(x,x):x>0\}
$$
be the diagonal branch.

::: pf

::: pf-step

Every solution with $x\ne y$ has a unique parameter
$$
t\coloneqq\frac yx>0,
\qquad
t\ne1,
$$
and is of the form
$$
(x,y)
=
\left(
t^{1/(t-1)},
t^{t/(t-1)}
\right).
$$

::: pf-proof

For positive $x,y$, write $y=tx$. Then
$$
x^y=y^x
$$
becomes
$$
x^{tx}=(tx)^x.
$$
Taking the positive $x$th root gives
$$
x^t=tx,
$$
and hence, because $x>0$,
$$
x^{t-1}=t.
$$
If $x\ne y$, then $t\ne1$, so
$$
x=t^{1/(t-1)},
\qquad
y=tx=t^{t/(t-1)}.
$$
The parameter is uniquely $t=y/x$.

:::

:::

::: {.pf-step #s2}

Conversely, for every $t>0$ with $t\ne1$, the point
$$
\gamma(t)
\coloneqq
\left(
t^{1/(t-1)},
t^{t/(t-1)}
\right)
$$
satisfies $x^y=y^x$ and does not lie on $D$.

::: pf-proof

For $\gamma(t)=(x,y)$ one has $y=tx$ and
$x^{t-1}=t$. Therefore
$$
x^t=tx=y,
$$
so
$$
x^y=x^{tx}=(x^t)^x=y^x.
$$
Since $y/x=t\ne1$, one has $x\ne y$, so the point is not on the
diagonal.

:::

:::

::: {.pf-step #s3}

The off-diagonal branch has the limiting point
$$
\lim_{t\to1}\gamma(t)=(e,e).
$$

::: pf-proof

The first coordinate satisfies
$$
\log\left(t^{1/(t-1)}\right)
=\frac{\log t}{t-1}
\longrightarrow1
$$
as $t\to1$. Hence its limit is $e$. For the second coordinate,
$$
\log\left(t^{t/(t-1)}\right)
=t\frac{\log t}{t-1}
\longrightarrow1,
$$
so its limit is also $e$.

:::

:::

::: {.pf-step #s4}

The two branches intersect at exactly
$$
\boxed{(e,e)}.
$$

::: pf-proof

By step [](#s2){.pf-ref}, no point $\gamma(t)$ with $t\ne1$ lies on the diagonal.
Step [](#s3){.pf-ref} shows that the off-diagonal branch extends to $t=1$ at
$(e,e)$, which itself lies on $D$ and satisfies $e^e=e^e$. Therefore
this is the unique intersection point of the two branches.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the requested intersection point.

:::

:::

:::
