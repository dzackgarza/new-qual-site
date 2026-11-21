---
schema: qual/card@1
id: P-RASP21E
kind: problem
title: 'Intersection of two $L^2$ balls'
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 5 of the official UCSD Spring 2021 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Find all $f \in L^2([-1,1])$ such that
$$
\int_{-1}^{1} \abs{f(x) - \sqrt{3}\,x}^2\,dx \leq \frac{1}{4}
$$
and
$$
\int_{-1}^{1} \abs{f(x) - \sqrt{5}\,x^2}^2\,dx \leq \frac{9}{4}.
$$
:::


::: {.solution}

No retained solution set covers this exercise: the card's own Hilbert-space argument follows, with the orthogonality and norms, the equality case of the triangle inequality, and the identification of $f$ as separate steps.

Let $u(x)=\sqrt3 x$ and $v(x)=\sqrt5 x^{2}$ in $L^{2}([-1,1])$.

::: pf

::: {.pf-step #norms}
$\norm{u}=\norm{v}=\sqrt2$ and $\langle u,v\rangle=0$, so $\norm{u-v}=2$.

::: pf-proof
$\int_{-1}^{1}x^{2}dx=\tfrac23$ gives $\norm{u}^{2}=3\cdot\tfrac23=2$, and $\int_{-1}^{1}x^{4}dx=\tfrac25$ gives $\norm{v}^{2}=5\cdot\tfrac25=2$; $\langle u,v\rangle=\sqrt{15}\int_{-1}^{1}x^{3}dx=\sqrt{15}\cdot0=0$ because $x^{3}$ is odd. Hence $\norm{u-v}^{2}=\norm{u}^{2}+\norm{v}^{2}=4$.
:::

:::

::: {.pf-step #conditions}
The hypotheses are $\norm{f-u}\le\tfrac12$ and $\norm{f-v}\le\tfrac32$.

::: pf-proof
$\int\abs{f-\sqrt3 x}^{2}=\norm{f-u}^{2}\le\tfrac14$ if and only if $\norm{f-u}\le\tfrac12$; and $\int\abs{f-\sqrt5x^{2}}^{2}\le\tfrac94$ if and only if $\norm{f-v}\le\tfrac32$.
:::

:::

::: {.pf-step #equality}
Both inequalities are equalities: $\norm{f-u}=\tfrac12$ and $\norm{f-v}=\tfrac32$.

::: pf-proof
The triangle inequality and the bounds of step [](#conditions){.pf-ref} give $2=\norm{u-v}\le\norm{u-f}+\norm{f-v}\le\tfrac12+\tfrac32=2$, so every term is forced to be its extreme value.
:::

:::

::: {.pf-step #identify}
$f=\tfrac34 u+\tfrac14 v$, and this $f$ satisfies the two conditions.

::: pf-proof
Equality in the triangle inequality for a strictly convex normed space means $u-f$ and $f-v$ are nonnegative multiples of one another: $u-f=t(f-v)$ with $t\ge0$. Taking norms and using step [](#equality){.pf-ref}, $t=\tfrac12\big/\tfrac32=\tfrac13$, so $\tfrac13(f-v)=u-f$, that is $\tfrac43 f=u+\tfrac13v$ and $f=\tfrac34 u+\tfrac14 v$. Then $u-f=\tfrac14(u-v)$ has norm $\tfrac14\cdot2=\tfrac12$ and $f-v=\tfrac34(v-u)$ has norm $\tfrac34\cdot2=\tfrac32$, so both conditions hold.
:::

:::

::: {.pf-qed}
The unique solution is $f(x)=\tfrac{3\sqrt3}{4}x+\tfrac{\sqrt5}{4}x^{2}$, by steps [](#identify){.pf-ref} and [](#equality){.pf-ref}. Equivalently, the closed balls of radii $\tfrac12$ about $u$ and $\tfrac32$ about $v$ meet in exactly one point, the one dividing the segment $[u,v]$ in the ratio $1:3$.
:::

:::

:::
