---
schema: qual/card@1
id: P-TRIV-RA32
kind: problem
title: Arc length of $y=\log\cos x$ on $[0,\pi/6]$
classification:
  areas: [real-analysis]
  topics:
  - Arc Length
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 32, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
A body moves in $(xy)$-plane along the trajectory $y = \log\cos x$. Find the path length of the body when $x \in [0, \frac{\pi}{6}]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For
$$
y=\log(\cos x),
$$
one has
$$
y'=-\tan x.
$$


::: pf-proof

Differentiate by the chain rule:
$$
\frac{d}{dx}\log(\cos x)
=
\frac{-\sin x}{\cos x}
=
-\tan x.
$$

:::

:::

::: {.pf-step #s1-2}

The arc length is
$$
L
=
\int_0^{\pi/6}
\sqrt{1+(y')^2}
\,dx.
$$


::: pf-proof

This is the standard arc-length formula for a graph $y=y(x)$.

:::

:::

::: {.pf-step #s1-3}

On the interval $[0,\pi/6]$,
$$
\sqrt{1+\tan^2x}
=
\sec x.
$$


::: pf-proof

Use
$$
1+\tan^2x=\sec^2x.
$$
Since $\cos x>0$ on the interval,
$$
\sqrt{\sec^2x}=\sec x.
$$

:::

:::

::: pf-step

Therefore
$$
L
=
\int_0^{\pi/6}\sec x\,dx.
$$


::: pf-proof

Substitute steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} into the arc-length formula.

:::

:::

::: {.pf-step #s1-5}

An antiderivative of $\sec x$ is
$$
\log\abs{\sec x+\tan x}.
$$


::: pf-proof

Differentiate:
$$
\frac{d}{dx}\log(\sec x+\tan x)
=
\frac{\sec x\tan x+\sec^2x}{\sec x+\tan x}
=
\sec x.
$$

:::

:::

::: pf-step

Hence
$$
L
=
\log\left(
\sec\frac\pi6+\tan\frac\pi6
\right)
-
\log1.
$$


::: pf-proof

Evaluate the antiderivative from step [](#s1-5){.pf-ref} between $0$ and $\pi/6$.

:::

:::

::: {.pf-step #s1-7}

Since
$$
\sec\frac\pi6
=
\frac2{\sqrt3}
$$
and
$$
\tan\frac\pi6
=
\frac1{\sqrt3},
$$
one obtains
$$
\boxed{
L
=
\log\sqrt3
=
\frac12\log3.
}
$$


::: pf-proof

The endpoint sum is
$$
\frac2{\sqrt3}
+
\frac1{\sqrt3}
=
\sqrt3.
$$

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required path length.

:::

:::

:::
