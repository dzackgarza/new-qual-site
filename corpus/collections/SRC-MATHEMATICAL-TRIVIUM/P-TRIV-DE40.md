---
schema: qual/card@1
id: P-TRIV-DE40
kind: problem
title: First-order PDE $xf_x-yf_y=0$ by characteristics
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 40, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the most general solution of $x\frac{\partial f}{\partial x} - y\frac{\partial f}{\partial y} = 0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The characteristic equations are
$$
\frac{dx}{ds}=x,
\qquad
\frac{dy}{ds}=-y,
\qquad
\frac{df}{ds}=0.
$$


::: pf-proof

These are the characteristic equations associated to the transport vector field $x\partial_x-y\partial_y$. The PDE states that the directional derivative of $f$ along this field vanishes.

:::

:::

::: {.pf-step #s1-2}

Along every characteristic,
$$
xy=\text{constant}.
$$


::: pf-proof

Differentiate the product along a characteristic:
$$
\frac d{ds}(xy)=x'y+xy'=xy-x y=0.
$$
Thus $xy$ is a first integral of the characteristic field.

:::

:::

::: {.pf-step #s1-3}

The value of $f$ is constant along each characteristic.


::: pf-proof

The third equation in step [](#s1-1){.pf-ref} is $df/ds=0$.

:::

:::

::: {.pf-step #s1-4}

Hence on any connected region where the characteristics are parametrized by the invariant $xy$, the general solution is
$$
\boxed{f(x,y)=\Phi(xy)},
$$
where $\Phi$ is arbitrary.


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}, $f$ may depend only on the characteristic label $xy$. Conversely, if $f=\Phi(xy)$, then
$$
f_x=y\Phi'(xy),
\qquad
f_y=x\Phi'(xy),
$$
and therefore
$$
xf_x-yf_y=xy\Phi'(xy)-xy\Phi'(xy)=0.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives and directly verifies the general characteristic solution.

:::

:::

:::
