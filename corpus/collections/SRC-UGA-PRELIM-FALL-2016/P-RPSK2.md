---
schema: qual/card@1
id: P-RPSK2
kind: problem
title: The line integral of $(2x+y)\,dx+y\,dy$ from $(2,1)$ to $(3,5)$ and path independence
classification:
  areas:
  - prelim
  topics:
  - Line Integrals
relations: []
review: draft
---

::: {.problem}
(a) Choose a path $C$ from $(2,1)$ to $(3,5)$ and compute
$$
\int_C(2x+y)\,dx+y\,dy.
$$

(b) Give and apply a criterion that shows whether this integral is path independent.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own computation follows, with the parametrization, the integrand in $t$, and a second path exhibiting path dependence as separate steps.

::: pf

::: {.pf-step #parametrize}
The segment from $(2,1)$ to $(3,5)$ is $r(t)=(2+t,\,1+4t)$ for $0\le t\le1$, with $dx=dt$ and $dy=4\,dt$.

::: pf-proof
The convex combination $r(t)=(1-t)(2,1)+t(3,5)$ equals $\big(2+t,1+4t\big)$, and its coordinate derivatives are $1$ and $4$; $r(0)=(2,1)$ and $r(1)=(3,5)$.
:::

:::

::: {.pf-step #compute}
$\int_C(2x+y)\,dx+y\,dy=20$.

::: pf-proof
On $C$ the integrand is $\big(2(2+t)+(1+4t)\big)\,dt+(1+4t)\cdot4\,dt=(5+6t+4+16t)\,dt=(9+22t)\,dt$, so the integral is $\int_{0}^{1}(9+22t)\,dt=9+\tfrac{22}{2}=20$.
:::

:::

::: {.pf-step #criterion}
(b) On $\RR^{2}$ path independence of $\int(2x+y)\,dx+y\,dy$ would force $P_{y}=Q_{x}$ for $P=2x+y$, $Q=y$; here $P_{y}=1$ and $Q_{x}=0$, so the integral is not path independent.

::: pf-proof
If the integral were path independent with continuous coefficients on the simply connected open set $\RR^{2}$, then it would be the differential of a $C^{2}$ potential $F$ with $F_{x}=P$, $F_{y}=Q$, and then $P_{y}=F_{xy}=F_{yx}=Q_{x}$ by equality of mixed partials. Here $P_{y}=1\ne0=Q_{x}$, so no such $F$ exists and the criterion fails.
:::

:::

::: {.pf-step #witness}
A second path from $(2,1)$ to $(3,5)$ gives a different value, so the failure in step [](#criterion){.pf-ref} is not a defect of the test.

::: pf-proof
Go from $(2,1)$ to $(3,1)$ along $y=1$ and then to $(3,5)$ along $x=3$. On the first segment $dy=0$ and $\int_{2}^{3}(2x+1)\,dx=\big[x^{2}+x\big]_{2}^{3}=12-6=6$; on the second $dx=0$ and $\int_{1}^{5}y\,dy=\tfrac{25-1}{2}=12$. The sum is $18\ne20$.
:::

:::

::: {.pf-qed}
Part (a) is step [](#compute){.pf-ref} ($20$), and (b) is the criterion of step [](#criterion){.pf-ref} together with the explicit second value of step [](#witness){.pf-ref}: the integral is path dependent.
:::

:::

:::
