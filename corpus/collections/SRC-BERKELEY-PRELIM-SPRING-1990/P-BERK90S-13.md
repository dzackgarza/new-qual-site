---
schema: qual/card@1
id: P-BERK90S-13
kind: problem
title: Repeated Rolle theorem from vanishing derivatives at one endpoint
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared infinite differentiability, the positive integer n, all endpoint vanishings, and the interior zero of the derivative of order n+1 with Problem 13 in the retained MinerU Flash extraction of Spring90.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
  note: Constructed a strictly descending chain of derivative zeros by repeated applications of the mean value theorem to intervals with left endpoint zero.
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: Checked continuity and differentiability at every stage, the derivative index range through n+1, the induction base, and strict interior containment of the final zero.
---

::: {.problem}
Let $f:\RR\to\RR$ be infinitely differentiable. Suppose for some positive integer $n$ that
$$
f(1)=f(0)=f'(0)=f''(0)=\cdots=f^{(n)}(0)=0.
$$
Prove that there is $x\in(0,1)$ such that
$$
f^{(n+1)}(x)=0.
$$
:::

::: {.hint}
Put $x_0\coloneqq1$ and use the convention $f^{(0)}\coloneqq f$.
Construct points $x_k\in(0,x_{k-1})$ with $f^{(k)}(x_k)=0$,
for $1\leq k\leq n+1$. At the $k$th stage, apply Rolle's theorem
to $f^{(k-1)}$ on $[0,x_{k-1}]$. The vanishing at $0$ is a
hypothesis, and the vanishing at $x_{k-1}$ comes from the
preceding stage, starting with $f(x_0)=f(1)=0$.
:::

::: {.solution}
Write $f^{(0)}\coloneqq f$ and $x_0\coloneqq1$.

::: pf

::: {.pf-step #s1}

Let $1\leq k\leq n+1$ and $t\in(0,1]$. If
$f^{(k-1)}(t)=0$, then there exists $s\in(0,t)$ such that
$f^{(k)}(s)=0$.

::: pf-proof

Since $f$ is infinitely differentiable, $f^{(k-1)}$ is continuous
on $[0,t]$ and differentiable on $(0,t)$. The inequality
$0\leq k-1\leq n$ and the hypotheses give $f^{(k-1)}(0)=0$.
By the [[T-RA-WORKSHOP-D5-4-2|mean value theorem]], there is
$s\in(0,t)$ with
$$
f^{(k)}(s)
=\frac{f^{(k-1)}(t)-f^{(k-1)}(0)}{t}=0.
$$

:::

:::

::: {.pf-step #s2}

There exist points $x_1,\ldots,x_{n+1}$ such that
$$
1=x_0>x_1>\cdots>x_{n+1}>0,
\qquad f^{(k)}(x_k)=0\quad(0\leq k\leq n+1).
$$

::: pf-proof

The initial point satisfies $f^{(0)}(x_0)=f(1)=0$. Suppose
$1\leq k\leq n+1$ and $x_{k-1}\in(0,1]$ has been chosen with
$f^{(k-1)}(x_{k-1})=0$. Apply step [](#s1){.pf-ref} with $t=x_{k-1}$
and choose the resulting point as $x_k$. Then
$0<x_k<x_{k-1}$ and $f^{(k)}(x_k)=0$. Induction constructs
all the stated points.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} gives $x_{n+1}\in(0,1)$ with
$f^{(n+1)}(x_{n+1})=0$, as required.

:::

:::

:::
