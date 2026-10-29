---
schema: qual/card@1
id: P-CAEXAMPREP-13
kind: problem
title: Temperature in the upper half-disk with mixed boundary data
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/Complex_Analysis_Exam_Prep_Solutions_extracted.md.
---

::: {.problem}
Let $A$ be the upper half of the unit disk $|z|<1$.
Find the temperature $T$ inside $A$ if the circular portion of the boundary is insulated, while on the diameter
$$
T=0\quad(0<x<1),
\qquad
T=10\quad(-1<x<0).
$$
:::

::: {.solution}

For $z=re^{i\theta}\in A$, take
$$
0<r<1,
\qquad
0<\theta<\pi,
$$
so $\theta=\operatorname{Arg}z$ is the branch of the argument on the upper half-plane.

::: pf

::: {.pf-step #s1-1}

Define
$$
T(re^{i\theta})=\frac{10}{\pi}\theta.
$$
Then $T$ is harmonic in $A$.


::: pf-proof

In polar coordinates,
$$
\Delta T
=T_{rr}+\frac1rT_r+\frac1{r^2}T_{\theta\theta}.
$$
The displayed function is independent of $r$ and linear in $\theta$, so
$$
T_r=T_{rr}=T_{\theta\theta}=0.
$$
Hence $\Delta T=0$ throughout $A$.

:::

:::

::: {.pf-step #s1-2}

The prescribed temperatures on the diameter are attained:
$$
T=0\quad(0<x<1),
\qquad
T=10\quad(-1<x<0).
$$


::: pf-proof

Approaching the positive real segment from within $A$ gives $\theta\to0$, hence $T\to0$. Approaching the negative real segment gives $\theta\to\pi$, hence
$$
T\to\frac{10}{\pi}\pi=10.
$$

:::

:::

::: {.pf-step #s1-3}

The circular boundary $|z|=1$, $\operatorname{Im}z>0$, is insulated.


::: pf-proof

On the circular arc the outward unit normal is the radial direction. Since $T_r=0$ by step [](#s1-1){.pf-ref},
$$
\frac{\partial T}{\partial n}=\frac{\partial T}{\partial r}=0
$$
there. Thus the normal heat flux vanishes, which is exactly the insulation condition.

:::

:::

::: {.pf-step #s1-4}

Therefore the temperature is
$$
\boxed{
T(z)=\frac{10}{\pi}\operatorname{Arg}z,
\qquad 0<\operatorname{Arg}z<\pi}.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives a steady-state temperature field, step [](#s1-2){.pf-ref} verifies the Dirichlet data on the diameter, and step [](#s1-3){.pf-ref} verifies the Neumann condition on the insulated circular arc.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required temperature field.

:::

:::

:::
