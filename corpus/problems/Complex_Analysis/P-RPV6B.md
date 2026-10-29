---
schema: qual/card@1
id: P-RPV6B
kind: problem
title: An analytic function is constant if $|f|$, $\Re(f)$, or $\arg(f)$ is constant,
  or if $\overline{f}$ is analytic
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Open Mapping Theorem
  - Maximum Modulus Principle
relations: []
review: draft
---

::: {.problem}
Let $f(z)$ be analytic in a domain, and prove that $f$ is constant if it satisfies any of the following conditions:

(a) $\abs{f(z)}$ is constant.

(b) $\Re(f(z))$ is constant.

(c) $\arg(f(z))$ is constant.

(d) $\overline{f(z)}$ is analytic.

How do you generalize (a) and (b)?
:::

::: {.solution title="(a)"}
Let $\Omega$ be the domain and suppose $\abs f\equiv r$.

::: pf

::: {.pf-step #circle}

$f(\Omega)$ has empty interior in $\CC$.

::: pf-proof

$f(\Omega)$ lies in the circle $\theset{\abs w=r}$, which contains no open disk.

:::

:::

::: pf-step

$f$ is constant.

::: pf-proof

If $f$ were nonconstant on the connected open set $\Omega$, the open mapping theorem would make $f(\Omega)$ a nonempty open set, contradicting step [](#circle){.pf-ref}.

:::

:::

:::

:::

::: {.solution title="(b)"}
Write $f=u+iv$ with $u\equiv c$.

::: pf

::: pf-step

$f$ is constant.

::: pf-proof

$u_x=u_y=0$, so the Cauchy--Riemann equations give $v_x=-u_y=0$ and $v_y=u_x=0$. Hence $f'=u_x+iv_x\equiv0$ on the connected set $\Omega$.

:::

:::

:::

:::

::: {.solution title="(c)"}
Suppose $\arg f\equiv\theta_0$ on $\Omega$.

::: pf

::: pf-step

$f$ is constant.

::: pf-proof

$f(\Omega)$ lies in the ray $\theset{te^{i\theta_0} : t>0}$, which has empty interior in $\CC$. As in solution (a), the open mapping theorem forces $f$ to be constant.

:::

:::

:::

:::

::: {.solution title="(d)"}

::: pf

::: {.pf-step #real-part}

$\Re f$ is constant.

::: pf-proof

$g\coloneqq\frac12(f+\overline f)=\Re f$ is analytic and real-valued. Writing $g=U+iV$ with $V\equiv0$, the Cauchy--Riemann equations give $U_x=V_y=0$ and $U_y=-V_x=0$, so $U=\Re f$ is constant on the connected set $\Omega$.

:::

:::

::: pf-step

$f$ is constant.

::: pf-proof

Apply part (b), using step [](#real-part){.pf-ref}.

:::

:::

:::

:::

::: {.solution title="Generalization of (a) and (b)"}

::: pf

::: pf-step
If $f$ is analytic on a domain $\Omega$ and $f(\Omega)$ has empty interior in $\CC$, then $f$ is constant.
Parts (a) and (b) are the cases where $f(\Omega)$ lies in a circle $\theset{\abs w=r}$ or a line $\theset{\Re w=c}$; more generally $f$ is constant whenever $f(\Omega)$ lies in a smooth curve, and a real-valued analytic function on a domain is constant.

::: pf-proof
If $f$ were nonconstant, the open mapping theorem would make $f(\Omega)$ a nonempty open set, which has nonempty interior.
A circle, a line, a ray and any smooth curve have empty interior in $\CC$, and a real-valued $f$ has $f(\Omega)\subseteq\RR$.
:::

:::

:::

:::
