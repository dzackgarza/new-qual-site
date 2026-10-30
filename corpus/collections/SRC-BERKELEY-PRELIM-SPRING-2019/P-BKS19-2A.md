---
schema: qual/card@1
id: P-BKS19-2A
kind: problem
title: Solutions of autonomous ODEs $y'=f(y)$ are monotone
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2019 uniqueness argument. The equilibrium case is correct; the solution below also makes explicit that a solution with no critical point has derivative of constant sign.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified local uniqueness for the $C^1$ vector field, the equilibrium case, and the intermediate-value argument for the sign of $y'$.
---

::: {.problem}
Let $f:\RR\to\RR$ be bounded and continuously differentiable.
Show that every solution $y$ of
$$
y'=f(y)
$$
is monotone.
:::

::: {.solution}

Let $I$ be the interval on which the solution $y$ is defined.

::: pf

::: {.pf-step #s1-1}

If $y'(t_0)=0$ for some $t_0\in I$, then $y$ is constant on $I$.


::: pf-proof

The differential equation gives
$$
f(y(t_0))=y'(t_0)=0.
$$
Hence the constant function
$$
z(t)\coloneqq y(t_0)
$$
is also a solution of $z'=f(z)$ and satisfies $z(t_0)=y(t_0)$. Since $f$ is continuously differentiable, it is locally Lipschitz, so the initial-value problem has a unique solution. Therefore $y=z$ throughout their common interval of definition, namely $I$. Thus $y$ is constant.

:::

:::

::: {.pf-step #s1-2}

If $y'(t)\neq0$ for every $t\in I$, then $y$ is strictly monotone on $I$.


::: pf-proof

The derivative
$$
y'(t)=f(y(t))
$$
is continuous. If it took both a positive and a negative value on the interval $I$, the intermediate value theorem would give a point $t_0\in I$ with $y'(t_0)=0$, contrary to the hypothesis. Hence either $y'>0$ everywhere or $y'<0$ everywhere. The mean value theorem then shows that $y$ is respectively strictly increasing or strictly decreasing.

:::

:::

::: {.pf-step #s1-3}

Every solution of $y'=f(y)$ is monotone.


::: pf-proof

If $y'$ vanishes anywhere, step [](#s1-1){.pf-ref} makes $y$ constant. If $y'$ never vanishes, step [](#s1-2){.pf-ref} makes $y$ strictly monotone. These cases exhaust all solutions.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required conclusion.

:::

:::

:::
