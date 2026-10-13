---
schema: qual/card@1
id: P-TRIV-DE15
kind: problem
title: First-order equation $y'+2y=e^{-t}\theta(t)$ with Heaviside forcing
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 15, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $y ^ { \prime } + 2 y = e ^ { - t } \theta ( t )$ , where θ is the Heaviside function, $\theta ( x ) = 0 { \mathrm { ~ i f ~ } } x < 0$ and $\theta ( x ) = 1 { \mathrm { ~ i f ~ } } x > 0$
:::

::: {.solution}
<1>1. An integrating factor is
$$
e^{2t}.
$$

::: {.proof}
For
$$
y'+2y=e^{-t}\theta(t),
$$
the coefficient of $y$ is the constant $2$, so the standard integrating factor is
$$
\exp\left(
\int2\,dt
\right)
=
e^{2t}.
$$
:::

<1>2. Multiplying by $e^{2t}$ gives
$$
\frac d{dt}
\left(
e^{2t}y
\right)
=
e^t\theta(t).
$$

::: {.proof}
The left-hand side expands as
$$
e^{2t}y'
+
2e^{2t}y,
$$
while the right-hand side is $e^{2t}e^{-t}\theta(t)$.
:::

<1>3. Integrating from $0$ to $t$ gives
$$
e^{2t}y(t)
=
C
+
\int_0^t e^s\theta(s)\,ds.
$$

::: {.proof}
The value $e^{0}y(0)$ is absorbed into the arbitrary constant $C$.
:::

<1>4. If $t<0$, then
$$
\int_0^t e^s\theta(s)\,ds
=0.
$$

::: {.proof}
The integration interval lies in $s<0$ after reversing orientation, and there
$$
\theta(s)=0.
$$
:::

<1>5. If $t>0$, then
$$
\int_0^t e^s\theta(s)\,ds
=
e^t-1.
$$

::: {.proof}
For $s>0$, one has $\theta(s)=1$, so
$$
\int_0^t e^s\,ds
=
e^t-1.
$$
:::

<1>6. Hence the continuous solution family is
$$
\boxed{
y(t)
=
Ce^{-2t}
+
\theta(t)
\left(
e^{-t}-e^{-2t}
\right).
}
$$

::: {.proof}
For $t<0$, steps <1>3--<1>4 give $y=Ce^{-2t}$. For $t>0$, steps <1>3 and <1>5 give
$$
y
=
e^{-2t}
\left(
C+e^t-1
\right)
=
Ce^{-2t}+e^{-t}-e^{-2t}.
$$
These two expressions are combined by the Heaviside function.
:::

<1>7. Equivalently,
$$
\boxed{
y(t)
=
\begin{cases}
Ce^{-2t},&t<0,\\
e^{-t}+(C-1)e^{-2t},&t>0.
\end{cases}
}
$$

::: {.proof}
Expand the Heaviside expression from step <1>6 on the two half-lines.
:::

<1>8. The two branches meet continuously at $t=0$.

::: {.proof}
The left limit is $C$. The right limit is
$$
1+(C-1)=C.
$$
Thus the value assigned to $\theta(0)$ is irrelevant because the Heaviside correction in step <1>6 vanishes at $t=0$.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>6--<1>8 give the complete continuous solution family.
:::
:::
