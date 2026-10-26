---
schema: qual/card@1
id: P-TRIV-RA34
kind: problem
title: Polar equation and asymptotics of the hyperbolic spiral
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 34, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in theta to 0 and the split sin t against Real Analysis Problem 34 on page 10 of the source PDF.
---

::: {.problem}
A hyperbolic spiral is written in a parametric form as follows: $x = \frac{\alpha}{t}\cos t$, $y = \frac{\alpha}{t}\sin t$, where $\alpha > 0$ is a constant and $t$ varies from $0$ to $\infty$.
Write the equation of this spiral in a polar coordinate system in the form $r = r(\theta)$.
Draw it schematically.
Investigate the limit of $x$, $y$ and $r$ as $\theta \to 0$.
:::

::: pf

::: pf-step

In polar coordinates,
$$
x=r\cos\theta,
\qquad
y=r\sin\theta.
$$


::: pf-proof

This is the definition of polar coordinates.

:::

:::

::: pf-step

Comparing the given parametrization with step <1>1 gives
$$
\theta=t
$$
and
$$
r=\frac{\alpha}{t}.
$$


::: pf-proof

The factors multiplying cosine and sine in the parametrization are equal, so
the radial coordinate is
$$
r=\sqrt{x^2+y^2}
=
\frac{\alpha}{t}.
$$
The angular variable is the same parameter appearing in $\cos t$ and $\sin t$.
For a spiral, the polar angle is understood as the unwrapped angle rather than
modulo $2\pi$.

:::

:::

::: pf-step

Therefore the polar equation is
$$
\boxed{r(\theta)=\frac{\alpha}{\theta}},
\qquad
\theta>0.
$$


::: pf-proof

Eliminate $t$ from the two identities in step <1>2.

:::

:::

::: pf-step

As $\theta$ increases, the radius decreases monotonically from
$+\infty$ to $0$.


::: pf-proof

From step <1>3,
$$
r'(\theta)
=
-\frac{\alpha}{\theta^2}<0.
$$
Also,
$$
\lim_{\theta\to0^+}r(\theta)=\infty
$$
and
$$
\lim_{\theta\to\infty}r(\theta)=0.
$$

:::

:::

::: pf-step

Thus the schematic shape is an inward-winding counterclockwise spiral:
it begins arbitrarily far from the origin for small positive $\theta$, crosses
each ray infinitely many times as the unwrapped angle grows, and approaches
the origin as $\theta\to\infty$.


::: pf-proof

The angle equals $\theta$, so increasing $\theta$ rotates counterclockwise,
while step <1>4 shows that the radius decreases continuously to $0$.

:::

:::

::: pf-step

As $\theta\to0^+$,
$$
\boxed{r\to\infty}.
$$


::: pf-proof

This is immediate from
$$
r=\frac{\alpha}{\theta}
$$
with $\alpha>0$.

:::

:::

::: pf-step

As $\theta\to0^+$,
$$
\boxed{x\to+\infty}.
$$


::: pf-proof

Using step <1>3,
$$
x
=
r\cos\theta
=
\frac{\alpha\cos\theta}{\theta}.
$$
Since
$$
\cos\theta\to1
$$
and $\theta\to0^+$, the quotient tends to $+\infty$.

:::

:::

::: pf-step

As $\theta\to0^+$,
$$
\boxed{y\to\alpha}.
$$


::: pf-proof

One has
$$
y
=
\frac{\alpha\sin\theta}{\theta}.
$$
Using
$$
\lim_{\theta\to0}\frac{\sin\theta}{\theta}=1,
$$
the limit is $\alpha$.

:::

:::

::: pf-step

Consequently the spiral has the horizontal asymptote
$$
\boxed{y=\alpha}
$$
at its far-away end $x\to+\infty$.


::: pf-proof

Steps <1>7--<1>8 show that $x\to+\infty$ while $y\to\alpha$.

:::

:::

::: pf-qed

Steps <1>3, <1>5, and <1>6--<1>9 give the polar equation, schematic behavior,
and requested limits.

:::

:::
