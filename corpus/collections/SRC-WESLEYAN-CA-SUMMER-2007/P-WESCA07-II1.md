---
schema: qual/card@1
id: P-WESCA07-II1
kind: problem
title: "An entire map with unit Jacobian is affine with unit-modulus slope"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Section II, problem 1 (Summer 2007) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Let $f=u+iv$ be entire and suppose
\[
u_xv_y-u_yv_x=1.
\]
Show that
\[
f(z)=az+b
\]
for constants $a,b\in\mathbb C$ with $|a|=1$.
:::

::: {.solution}
<1>1. For a holomorphic function $f=u+iv$,
$$
u_xv_y-u_yv_x
=|f'(z)|^2.
$$

::: {.proof}
The Cauchy--Riemann equations give
$$
v_y=u_x,
\qquad
v_x=-u_y.
$$
Therefore
$$
u_xv_y-u_yv_x
=u_x^2+u_y^2.
$$
Also
$$
f'(z)=u_x+i v_x=u_x-i u_y,
$$
so
$$
|f'(z)|^2=u_x^2+u_y^2.
$$
:::

<1>2. The hypothesis implies
$$
|f'(z)|=1
$$
for every $z\in\CC$.

::: {.proof}
Combine the given Jacobian identity with step <1>1.
:::

<1>3. The derivative $f'$ is constant.

::: {.proof}
The function $f'$ is entire because $f$ is entire. Step <1>2 shows that it is bounded. By Liouville's theorem,
$$
f'(z)\equiv a
$$
for some constant $a\in\CC$. Moreover $|a|=1$.
:::

<1>4. There is a constant $b\in\CC$ such that
$$
\boxed{f(z)=az+b,
\qquad |a|=1.}
$$

::: {.proof}
Since $f'\equiv a$, the derivative of $f(z)-az$ is identically zero. Hence $f(z)-az$ is constant on the connected plane; call the constant $b$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required form of $f$.
:::
:::
