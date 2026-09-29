---
schema: qual/card@1
id: P-BERK95S-05
kind: problem
title: Every solution of $y'=f(y)$ is monotone when $f$ is bounded and $C^1$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be bounded and continuously differentiable. Show that every solution of
\[
y'(x)=f(y(x))
\]
is monotone.
:::

::: {.solution}
Let $y$ be a solution on an interval $I$.

::: pf

::: {.pf-step #s1}

If $y'(x_0)=0$ at some $x_0\in I$, then $y$ is constant on
$I$.

::: pf-proof

From the differential equation,
$$
0=y'(x_0)=f(y(x_0)).
$$
Set $c\coloneqq y(x_0)$. Then the constant function
$$
z(x)\equiv c
$$
also satisfies $z'=f(z)$.

Because $f$ is $C^1$, it is locally Lipschitz. Hence the initial-value
problem
$$
u'=f(u),
\qquad
u(x_0)=c
$$
has locally unique solutions. Thus $y=z$ on a neighborhood of $x_0$.

More generally, let
$$
E\coloneqq\{x\in I:y(x)=c\}.
$$
The set $E$ is closed by continuity. If $x\in E$, then
$f(y(x))=f(c)=0$, so the same local-uniqueness argument shows that
$y\equiv c$ near $x$; hence $E$ is open in $I$. Since $I$ is
connected and $E$ is nonempty, $E=I$.

:::

:::

::: {.pf-step #s2}

Every nonconstant solution has derivative of one strict sign on
$I$.

::: pf-proof

If $y$ is nonconstant, step [](#s1){.pf-ref} shows that
$$
y'(x)\ne0
\qquad(x\in I).
$$
The derivative
$$
y'=f\circ y
$$
is continuous. A continuous nonvanishing real-valued function on the
connected interval $I$ has constant sign. Thus either
$y'(x)>0$ for every $x\in I$ or $y'(x)<0$ for every $x\in I$.

:::

:::

::: {.pf-step #s3}

Every solution is monotone.

::: pf-proof

A constant solution is monotone. By step [](#s2){.pf-ref}, every nonconstant
solution is either strictly increasing or strictly decreasing.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves the assertion.

:::

:::

:::
