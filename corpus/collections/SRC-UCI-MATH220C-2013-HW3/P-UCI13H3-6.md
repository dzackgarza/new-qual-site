---
schema: qual/card@1
id: P-UCI13H3-6
kind: problem
title: When analyticity of $f^2$ forces analyticity of $f$
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Prove or disprove each of the statements:

a) If $f$ is a function on the unit disc $D$ such that $f(z)^2$ is analytic on $D$, then $f$ itself is analytic.

b) If $f$ is a continuously differentiable function on $D$, and if $f(z)^2$ is analytic on $D$, then $f$ itself is analytic.
:::

::: {.solution}
A continuously differentiable function is analytic exactly when $\partial_{\overline z}f=0$, and $\partial_{\overline z}(f^2)=2f\,\partial_{\overline z}f$.

::: pf

::: {.pf-step #part-a}
(a) The first statement is false.

::: pf-proof
On the unit disc $D$ define
$$
f(z)=\begin{cases}z, & \operatorname{Im}z\ge0,\\ -z, & \operatorname{Im}z<0.\end{cases}
$$
Then $f(z)^2=z^2$ for every $z\in D$, which is analytic, while $f$ is not continuous at any point of $(-1,1)\subseteq\RR$: from above the limit there is $x$ and from below it is $-x$, and these differ for $x\ne0$.
So the square of $f$ can be analytic without $f$ being analytic.
:::

:::

::: {.pf-step #part-b}
(b) The second statement is true.

::: pf-proof
Suppose $f$ is continuously differentiable on $D$ and $f^2$ is analytic, and put $u=\partial_{\overline z}f$, which is continuous because $f$ is continuously differentiable.
Since $\partial_{\overline z}(f^2)=2fu$ vanishes, we have $f(z)u(z)=0$ at every $z\in D$.
If $u(z_0)\ne0$ for some $z_0$, then by continuity $u\ne0$ on a neighbourhood $V$ of $z_0$, so $f=0$ on $V$ and hence $f^2=0$ on $V$; by the identity theorem $f^2$ vanishes on the whole component of $D$ containing $z_0$, giving $f=0$ and $u=0$ on $V$, a contradiction.
Therefore $u=0$ on $D$, that is $f$ satisfies the Cauchy--Riemann equations; being continuously differentiable, $f$ is analytic.
:::

:::

:::

:::
