---
schema: qual/card@1
id: P-RPV6B
kind: problem
title: "Let $f(z)$ be analytic in a domain, and prove that $f$ is constant if\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Let $f(z)$ be analytic in a domain, and prove that $f$ is constant if it satisfies any of the following conditions:

a. $\abs{f(z)}$ is constant.
b. $\Re(f(z))$ is constant.
c. $\arg(f(z))$ is constant.
d. $\bar{f(z)}$ is analytic.

How do you generalize (a) and (b)?

:::

:::{.solution title="1"}
\envlist

Slick proof: use that no curve $\gamma \subseteq \CC$ is open in $\CC$.

If $\abs{f} = c = r^2$ for some $r$, then the image of $f$ is contained in the curve $\bd \DD_r(0)$.
Since $f$ is holomorphic on the source domain $\Omega$, $f$ is an open map, so if $f$ is nonconstant the $f(\Omega)$ is open.
But $f(\Omega) \subseteq \bd \DD_r(0)$ can not be open, so $f$ must be constant.

The usual more direct proof: write $\abs{f(z)} = u^2 = v^2 = r^2$.
The claim is that both $u$ and $v$ are constant.
Take partial derivatives and clear the factor of 2:
\[
\del_x: \quad uu_x + vv_x &= 0\\
\del_y: \quad uu_y + vv_y &= 0
.\]
Now apply CR: $u_x= v_y, u_y=-v_x$, then
\[
uu_x - vu_y &=0 \\
uu_y + vu_x &=0
.\]
Multiply the first by $u_x$ and the second by $u_y$, then add
\[
uu_x^2 - vu_y u_x &= 0 \\
uu_y^2 + vu_x u_y &=0 \\
\implies u(u_x^2 + u_y^2) &=0
.\]
A similar calculation yields $v(v_x^2 + v_y^2) = 0$, so
If $u(x,y) = v(x, y) = 0$ at any point, then $\abs{f} = 0$ and $f\equiv 0$, so we're done.
Otherwise, $u,v$ do not simultaneously vanish, so we must have
\[
0 = u_x^2 + u_y^2 &\implies 0 = u_x = u_y \implies u \text{ constant }\\
0 = v_x^2 + v_y^2 &\implies 0 = v_x = v_y \implies v \text{ constant }
,\]
so $f=u+iv$ is constant.





:::

:::{.solution title="2"}
Write $f=u+iv$, so $u\equiv c$ is constant.
Then $u_x = u_y = 0$, and CR yields $v_y = u_x = 0$ and $v_y = -u_x = 0$, so $v$ is constant, making $f$ constant.
:::

:::{.solution title="3"}
Slick proof: apply the open mapping theorem again, since $\Arg(f) = \theta_0$ implies that $\im(f) \subseteq \gamma$ for the curve $\gamma \da \ts{t e^{i\theta_0}\st t\in \RR}$ which has no open subsets.

Note that this implies that any $\RR\dash$valued holomorphic function is constant.
:::

:::{.solution title="4"}
Write $f=u+iv$ so $\bar f = u +i\tilde v$ where $\tilde v \da -v$.
Then $u, \tilde v$ are constant, so in particular $\Re(f)$ is constant and by 2 $f$ is constant.
:::
