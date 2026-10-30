---
schema: qual/card@1
id: P-CAEXAMPREP-05
kind: problem
title: A logarithmic improper integral
classification: {areas: [complex-analysis], topics: [Contour Integration]}
relations: []
review: draft
audit:
  - event: source-checked
    by: gpt-5.6-sol
    date: 2026-09-14
    note: Checked against the deterministic MinerU Flash extraction assets/attachments/Complex_Analysis_Exam_Prep_Solutions_extracted.md.
---

::: {.problem}
Show that for $p>0$ and $q>0$,
$$
\int_0^\infty \frac{\log(px)}{q^2+x^2}\,dx
=\frac{\pi}{2q}\log(pq).
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The integrals
$$
\int_0^\infty\frac{\abs{\log t}}{1+t^2}\,dt
\qquad\text{and}\qquad
\int_0^\infty\frac{dt}{1+t^2}
$$
are finite, and
$$
\int_0^\infty\frac{dt}{1+t^2}=\frac\pi2.
$$


::: pf-proof

On $(0,1]$, one has $(1+t^2)^{-1}\le1$, and
$$
\int_0^1\abs{\log t}\,dt=1.
$$
On $[1,\infty)$, $(1+t^2)^{-1}\le t^{-2}$, and $\int_1^\infty (\log t)t^{-2}\,dt<\infty$ by integration by parts. Hence the logarithmic integral is absolutely convergent. The second integral is
$$
\left[\arctan t\right]_{0}^{\infty}=\frac\pi2.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
\int_0^\infty\frac{\log t}{1+t^2}\,dt=0.
$$


::: pf-proof

Let
$$
J=\int_0^\infty\frac{\log t}{1+t^2}\,dt,
$$
which is absolutely convergent by step [](#s1-1){.pf-ref}. In the substitution $t=1/u$,
$$
\begin{aligned}
J
&=\int_\infty^0
\frac{-\log u}{1+u^{-2}}\left(-\frac{du}{u^2}\right)\\
&=-\int_0^\infty\frac{\log u}{1+u^2}\,du\\
&=-J.
\end{aligned}
$$
Thus $2J=0$, so $J=0$.

:::

:::

::: {.pf-step #s1-3}

For $p,q>0$,
$$
\boxed{
\int_0^\infty \frac{\log(px)}{q^2+x^2}\,dx
=\frac{\pi}{2q}\log(pq)}.
$$


::: pf-proof

Substitute $x=qt$. Then
$$
\begin{aligned}
\int_0^\infty \frac{\log(px)}{q^2+x^2}\,dx
&=\frac1q\int_0^\infty\frac{\log(pq)+\log t}{1+t^2}\,dt\\
&=\frac{\log(pq)}q\int_0^\infty\frac{dt}{1+t^2}
+\frac1q\int_0^\infty\frac{\log t}{1+t^2}\,dt.
\end{aligned}
$$
Step [](#s1-1){.pf-ref} evaluates the first integral as $\pi/2$, and step [](#s1-2){.pf-ref} makes the second integral zero. This gives the claimed formula.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves the required identity.

:::

:::

:::

::: {.remark title="Variations"}
The case $p=1$, $q=a$ is
$$
\int_0^\infty \frac{\log x}{x^2+a^2}\,dx=\frac{\pi\log a}{2a},\qquad a>0.
$$
:::
