---
schema: qual/card@1
id: E-SS1.EX-13
kind: problem
title: Holomorphic $f$ with constant $\Re f$, $\Im f$, or $\abs{f}$ is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Open Mapping Theorem
  - Holomorphic Functions
relations: []
review: draft
---

::: {.exercise}
If $f$ is holomorphic on $\Omega$ and any of the following hold, then $f$ is constant:

1. $\Re(f)$ is constant.

2. $\Im(f)$ is constant.

3. $\abs{f}$ is constant.
:::

::: {.solution}
Here $\Omega$ is a region, that is, open and connected. Write $f=u+iv$ with $u,v$ real.

::: pf

::: {.pf-step #s1}

(1) If $u$ is constant on $\Omega$, then $f$ is constant.

::: pf-proof

At each point $f'=\partial f/\partial x=u_x+iv_x$, and the Cauchy--Riemann equation $v_x=-u_y$ gives $f'=u_x-iu_y=0$. So $f'=0$ on the connected set $\Omega$, and $f$ is constant.

:::

:::

::: {.pf-step #s2}

(2) If $v$ is constant on $\Omega$, then $f$ is constant.

::: pf-proof

The function $-if$ is holomorphic with real part $v$, so step [](#s1){.pf-ref} makes $-if$, and hence $f$, constant.

:::

:::

::: {.pf-step #s3}

(3) If $\abs{f} = c$ on $\Omega$, then $f$ is constant.

::: pf-proof

::: {.pf-step #s3-1}

If $c=0$, then $f=0$.

::: pf-proof

$\abs{f(z)} = 0$ if and only if $f(z) = 0$.

:::

:::

::: pf-step

If $c>0$, then $\bar f$ is holomorphic on $\Omega$.

::: pf-proof

Since $\abs{f}=c>0$, $f$ has no zeros on $\Omega$, and $f\bar{f} = \abs{f}^2 = c^2$ gives $\bar{f}=c^2/f$, a quotient of holomorphic functions with nonvanishing denominator.

:::

:::

::: pf-qed

In the case $c>0$, both $f$ and $\bar f$ are holomorphic, so $\partial f/\partial\bar z=0$ and $\overline{f'}=\overline{\partial f/\partial z}=\partial\bar f/\partial\bar z=0$. Hence $f'=0$ on the connected set $\Omega$, and $f$ is constant. The case $c=0$ is step [](#s3-1){.pf-ref}.

:::

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} are the three cases.

:::

:::

:::
