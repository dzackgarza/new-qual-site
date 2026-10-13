---
schema: qual/card@1
id: P-WESCA04-P4
kind: problem
title: "An analytic function satisfying $v=u^2$ is constant"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1.3, problem 4 (August 2, 2004) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Suppose $f=u+iv$ is analytic on a domain $D\subset\mathbb C$ and
\[
v(z)=u(z)^2
\qquad(z\in D).
\]
Show that $f$ is constant on $D$.
:::

::: {.solution}
<1>1. Since $f=u+iv$ is analytic, the Cauchy--Riemann equations give
\[
u_x=v_y,
\qquad
u_y=-v_x.
\]

::: {.proof}
The real and imaginary parts of a holomorphic function are continuously
differentiable and satisfy the Cauchy--Riemann equations.
:::

<1>2. Since
\[
v=u^2,
\]
one has
\[
v_x=2u,u_x,
\qquad
v_y=2u,u_y.
\]

::: {.proof}
Differentiate the identity
\[
v(x,y)=u(x,y)^2
\]
with respect to $x$ and $y$.
:::

<1>3. Combining steps <1>1 and <1>2 gives
\[
u_x=2u,u_y
\]
and
\[
u_y=-2u,u_x.
\]

::: {.proof}
Substitute
\[
v_y=2u,u_y
\]
into
\[
u_x=v_y,
\]
and substitute
\[
v_x=2u,u_x
\]
into
\[
u_y=-v_x.
\]
:::

<1>4. One has
\[
u_x=0
\]
throughout $D$.

::: {.proof}
Substitute the second equation of step <1>3 into the first:
\[
u_x
=
2u(-2u,u_x)
=
-4u^2u_x.
\]
Hence
\[
(1+4u^2)u_x=0.
\]
Since
\[
1+4u^2>0
\]
for real-valued $u$, it follows that
\[
u_x=0.
\]
:::

<1>5. One also has
\[
u_y=0
\]
throughout $D$.

::: {.proof}
Use the second equation of step <1>3:
\[
u_y
=
-2u,u_x.
\]
Step <1>4 gives
\[
u_x=0,
\]
so
\[
u_y=0.
\]
:::

<1>6. The function $u$ is constant on $D$.

::: {.proof}
The gradient of $u$ vanishes identically:
\[
\nabla u
=
(u_x,u_y)
=
(0,0).
\]
Because $D$ is a domain, hence connected and path-connected, $u$ is constant
along every path in $D$ and therefore constant on $D$.
:::

<1>7. The function $v$ is constant on $D$.

::: {.proof}
By hypothesis,
\[
v=u^2.
\]
Since $u$ is constant by step <1>6, so is $v$.
:::

<1>8. Therefore
\[
\boxed{
f=u+iv
\text{ is constant on }D.
}
\]

::: {.proof}
Both its real and imaginary parts are constant by steps <1>6--<1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the desired conclusion.
:::
:::
