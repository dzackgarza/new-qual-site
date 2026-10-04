---
schema: qual/card@1
id: P-TRIV-RA32
kind: problem
title: Arc length of $y=\log\cos x$ on $[0,\pi/6]$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 32, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
A body moves in (xy)-plane along the trajectory y = log cos x. Find the path length of the body when $x \in [ 0 , \frac { \pi } { 6 } ]$
:::

::: {.solution}
<1>1. For
$$
y=\log(\cos x),
$$
one has
$$
y'=-\tan x.
$$

::: {.proof}
Differentiate by the chain rule:
$$
\frac{d}{dx}\log(\cos x)
=
\frac{-\sin x}{\cos x}
=
-\tan x.
$$
:::

<1>2. The arc length is
$$
L
=
\int_0^{\pi/6}
\sqrt{1+(y')^2}
\,dx.
$$

::: {.proof}
This is the standard arc-length formula for a graph $y=y(x)$.
:::

<1>3. On the interval $[0,\pi/6]$,
$$
\sqrt{1+\tan^2x}
=
\sec x.
$$

::: {.proof}
Use
$$
1+\tan^2x=\sec^2x.
$$
Since $\cos x>0$ on the interval,
$$
\sqrt{\sec^2x}=\sec x.
$$
:::

<1>4. Therefore
$$
L
=
\int_0^{\pi/6}\sec x\,dx.
$$

::: {.proof}
Substitute steps <1>1--<1>3 into the arc-length formula.
:::

<1>5. An antiderivative of $\sec x$ is
$$
\log|\sec x+\tan x|.
$$

::: {.proof}
Differentiate:
$$
\frac{d}{dx}\log(\sec x+\tan x)
=
\frac{\sec x\tan x+\sec^2x}{\sec x+\tan x}
=
\sec x.
$$
:::

<1>6. Hence
$$
L
=
\log\left(
\sec\frac\pi6+\tan\frac\pi6
\right)
-
\log1.
$$

::: {.proof}
Evaluate the antiderivative from step <1>5 between $0$ and $\pi/6$.
:::

<1>7. Since
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

::: {.proof}
The endpoint sum is
$$
\frac2{\sqrt3}
+
\frac1{\sqrt3}
=
\sqrt3.
$$
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required path length.
:::
:::
