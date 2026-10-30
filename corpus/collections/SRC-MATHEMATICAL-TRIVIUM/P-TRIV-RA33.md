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

::: pf

::: pf-step

The derivative is
$$
\gamma'(t)
=
\bigl(-r\sin t,r\cos t,a\bigr).
$$


::: pf-proof

Differentiate each coordinate with respect to $t$.

:::

:::

::: {.pf-step #s1-2}

The speed is constant:
$$
\norm{\gamma'(t)}
=
\sqrt{r^2+a^2}.
$$


::: pf-proof

Compute
$$
\begin{aligned}
\norm{\gamma'(t)}^2
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

:::

::: {.pf-step #s1-3}

The arc length from parameter $0$ to parameter $\phi$ is
$$
L(\phi)
=
\int_0^\phi
\norm{\gamma'(t)}
\,dt.
$$


::: pf-proof

This is the standard arc-length formula for a parametrized curve.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
L(\phi)
=
\phi\sqrt{r^2+a^2}.
}
$$


::: pf-proof

Substitute the constant speed from step [](#s1-2){.pf-ref} into step [](#s1-3){.pf-ref}:
$$
L(\phi)
=
\sqrt{r^2+a^2}
\int_0^\phi dt
=
\phi\sqrt{r^2+a^2}.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required length function.

:::

:::

:::
