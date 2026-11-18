---
schema: qual/card@1
id: E-SS1.EX-9
kind: problem
title: The Cauchy-Riemann equations in polar coordinates
classification:
  areas:
    - complex-analysis
  topics: [Cauchy-Riemann, Complex Logarithm]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-10
  - event: solution-written
    by: claude
    date: 2026-11-18
    note: >-
      Restructured the prose solution into Lamport steps. The collection's provenance is the publisher's catalogue record only, with no retained text and no retained solution set, so the statement is taken as the card prints it; the argument is the card's own. Checked: the chain rule in both directions, the two polar equations obtained from the Cartesian ones and the converse, and for the principal logarithm the four partial derivatives $u_r=1/r$, $u_\theta=0$, $v_r=0$, $v_\theta=1$, which satisfy the polar equations on the slit plane.
---

::: {.exercise}
Show that in polar coordinates, the Cauchy-Riemann equations take the form

$$
\frac{\partial u}{\partial r} = \frac{1}{r} \frac{\partial v}{\partial \theta} \quad \text{and} \quad \frac{1}{r} \frac{\partial u}{\partial \theta} = -\frac{\partial v}{\partial r}.
$$

Use these equations to show that the logarithm function defined by

$$
\log z = \log r + i\theta \quad \text{where } z = re^{i\theta} \text{ with } -\pi < \theta < \pi
$$

is holomorphic in the region $r > 0$ and $-\pi < \theta < \pi$.
:::

::: {.solution}
No retained text and no retained solution set for this collection: its provenance is the publisher's catalogue record, so the statement is taken as the card prints it, and the argument is the card's own. The polar form is obtained from the Cartesian one by the chain rule, and the principal logarithm is checked against it directly.

::: pf

::: {.pf-step #chain}
With $z=x+iy=re^{i\theta}$ and $f=u+iv$, the chain rule gives $u_r=u_x\cos\theta+u_y\sin\theta$ and $u_\theta=-ru_x\sin\theta+ru_y\cos\theta$, and the same formulas with $v$ in place of $u$.

::: pf-proof
The change of variables $x=r\cos\theta$, $y=r\sin\theta$ is differentiable for $r>0$, and differentiating $u(r\cos\theta,r\sin\theta)$ with respect to $r$ and $\theta$ gives the displayed expressions.
:::
:::

::: {.pf-step #first}
If $u_x=v_y$ and $u_y=-v_x$ at a point with $r>0$, then $u_r=\frac1r v_\theta$ there.

::: pf-proof
By step [](#chain){.pf-ref}, $\frac1r v_\theta=-v_x\sin\theta+v_y\cos\theta$; substituting $v_x=-u_y$ and $v_y=u_x$ turns this into $u_y\sin\theta+u_x\cos\theta=u_r$.
:::
:::

::: {.pf-step #second}
Under the same hypothesis $\frac1r u_\theta=-v_r$.

::: pf-proof
Again by step [](#chain){.pf-ref}, $v_r=v_x\cos\theta+v_y\sin\theta=-u_y\cos\theta+u_x\sin\theta=-\frac1r u_\theta$, the last identity from the formula for $u_\theta$.
:::
:::

::: {.pf-step #converse}
Conversely, if the two polar equations hold at a point with $r>0$ and the partials are continuous, then the Cartesian Cauchy--Riemann equations hold there.

::: pf-proof
The relations between the partial derivatives in the two coordinate systems form an invertible linear system, because the Jacobian of $(r,\theta)\mapsto(x,y)$ is $r\neq0$; reversing the computations of steps [](#first){.pf-ref} and [](#second){.pf-ref} recovers $u_x=v_y$ and $u_y=-v_x$.
:::
:::

::: {.pf-step #log}
For $u(r,\theta)=\log r$ and $v(r,\theta)=\theta$ the polar Cauchy--Riemann equations hold wherever $r>0$ and $-\pi<\theta<\pi$.

::: pf-proof
Here $u_r=1/r$, $u_\theta=0$, $v_r=0$ and $v_\theta=1$, so $u_r=\frac1r v_\theta$ and $\frac1r u_\theta=0=-v_r$ at every point of the region.
:::
:::

::: {.pf-step #holomorphic}
$\log z=\log r+i\theta$ is holomorphic on $r>0$, $-\pi<\theta<\pi$.

::: pf-proof
$(r,\theta)\mapsto re^{i\theta}$ is a $C^1$ diffeomorphism of the region onto the slit plane, so $u$ and $v$ are $C^1$ functions of $(x,y)$ there; by step [](#converse){.pf-ref} they satisfy the Cartesian Cauchy--Riemann equations, and a $C^1$ function satisfying them is holomorphic.
:::
:::

:::
:::
