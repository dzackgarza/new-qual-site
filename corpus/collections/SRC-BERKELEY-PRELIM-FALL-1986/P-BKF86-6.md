---
schema: qual/card@1
id: P-BKF86-6
kind: problem
title: Decay of solutions of $f'+qf=0$ versus $f'+pf=0$ when $|q|\le|p|$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
---

::: {.problem}
Prove the following theorem, or find a counterexample: If $p$ and $q$ are continuous real-valued functions on $\mathbb R$ such that $|q(x)|\le|p(x)|$ for all $x$, and if every solution $f$ of the differential equation
\[
f'+qf=0
\]
satisfies $\lim_{x\to+\infty}f(x)=0$, then every solution $f$ of the differential equation
\[
f'+pf=0
\]
satisfies $\lim_{x\to+\infty}f(x)=0$.
:::

::: {.solution}
<1>1. Take
$$
\boxed{q(x)=1,\qquad p(x)=-1}
$$
for every $x\in\RR$.

::: {.proof}
Both functions are continuous, and for every $x\in\RR$,
$$
\abs{q(x)}=1=\abs{p(x)}.
$$
Thus the required pointwise inequality $\abs{q(x)}\leq\abs{p(x)}$ holds.
:::

<1>2. Every solution of
$$
f'+qf=0
$$
tends to $0$ as $x\to+\infty$.

::: {.proof}
For the choice in step <1>1, the equation is
$$
f'+f=0.
$$
Multiplying by $e^x$ gives
$$
\bigl(e^x f(x)\bigr)'=0,
$$
so every solution has the form
$$
f(x)=Ce^{-x}
$$
for some constant $C$. Hence $\lim_{x\to+\infty}f(x)=0$.
:::

<1>3. The corresponding equation
$$
f'+pf=0
$$
has a solution that does not tend to $0$ as $x\to+\infty$.

::: {.proof}
For the choice in step <1>1, this equation is
$$
f'-f=0.
$$
The function
$$
f(x)=e^x
$$
is a solution, and $\lim_{x\to+\infty}e^x=+\infty$. Thus this solution does not tend to $0$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 verify all hypotheses of the proposed theorem, while step <1>3 shows that its conclusion fails. Therefore the boxed pair in step <1>1 is a counterexample.
:::
:::
