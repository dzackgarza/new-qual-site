---
schema: qual/card@1
id: P-TRIV-RA33
kind: problem
title: Arc length of a helix
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 33, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
A helix is written in a parametric form as follows,

$$
x = r \cos \phi , y = r \sin \phi , z = a \phi ,\tag{12}
$$

where $r , a > 0$ are constants and $\phi$ varies from $0$ to $\infty$.
Find the length of the helix as a function of $\phi$
:::

::: {.solution}
Let
$$
\gamma(t)
=
\bigl(r\cos t,r\sin t,at\bigr),
\qquad
0\leq t\leq\phi.
$$

<1>1. The derivative is
$$
\gamma'(t)
=
\bigl(-r\sin t,r\cos t,a\bigr).
$$

::: {.proof}
Differentiate each coordinate with respect to $t$.
:::

<1>2. The speed is constant:
$$
\|\gamma'(t)\|
=
\sqrt{r^2+a^2}.
$$

::: {.proof}
Compute
$$
\begin{aligned}
\|\gamma'(t)\|^2
&=
r^2\sin^2t
+
r^2\cos^2t
+
a^2\\
&=
r^2+a^2.
\end{aligned}
$$
Taking the positive square root gives the speed.
:::

<1>3. The arc length from parameter $0$ to parameter $\phi$ is
$$
L(\phi)
=
\int_0^\phi
\|\gamma'(t)\|
\,dt.
$$

::: {.proof}
This is the standard arc-length formula for a parametrized curve.
:::

<1>4. Therefore
$$
\boxed{
L(\phi)
=
\phi\sqrt{r^2+a^2}.
}
$$

::: {.proof}
Substitute the constant speed from step <1>2 into step <1>3:
$$
L(\phi)
=
\sqrt{r^2+a^2}
\int_0^\phi dt
=
\phi\sqrt{r^2+a^2}.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required length function.
:::
:::
