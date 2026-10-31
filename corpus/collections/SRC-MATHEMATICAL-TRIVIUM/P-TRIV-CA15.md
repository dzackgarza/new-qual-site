---
schema: qual/card@1
id: P-TRIV-CA15
kind: problem
title: $\int_{-\infty}^\infty \frac{e^{i\alpha x}}{(3-ix)(1+ix)}\,dx$ by residues
classification:
  areas: [complex-analysis]
  topics:
  - Residue Theorem
  - Fourier Transform
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 15, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
For real $\alpha$, compute $\int_{-\infty}^{\infty} \frac{e^{i\alpha x}}{(3 - ix)(1 + ix)}\, \mathrm{d}x$.
:::

::: {.remark}
The source does not state the domain of the parameter $\alpha$. The standard
Fourier-transform interpretation, and the contour choice according to the sign
of $\alpha$, use $\alpha\in\RR$.
:::

::: {.solution}

Let
$$
F_\alpha(z)
=
\frac{e^{i\alpha z}}
{(3-iz)(1+iz)}.
$$

::: pf

::: pf-step

The poles of $F_\alpha$ are
$$
z=i
\qquad\text{and}\qquad
z=-3i.
$$


::: pf-proof

The equations
$$
1+iz=0
$$
and
$$
3-iz=0
$$
give respectively $z=i$ and $z=-3i$.

:::

:::

::: {.pf-step #s1-2}

The residue at $z=i$ is
$$
\operatorname{Res}_{z=i}F_\alpha(z)
=
\frac{e^{-\alpha}}{4i}.
$$


::: pf-proof

Since
$$
1+iz=i(z-i),
$$
one has
$$
\operatorname{Res}_{z=i}F_\alpha(z)
=
\frac{e^{i\alpha i}}
i(3-i i)
=
\frac{e^{-\alpha}}{4i}.
$$

:::

:::

::: {.pf-step #s1-3}

The residue at $z=-3i$ is
$$
\operatorname{Res}_{z=-3i}F_\alpha(z)
=
-\frac{e^{3\alpha}}{4i}.
$$


::: pf-proof

The derivative of $3-iz$ is $-i$, and
$$
1+i(-3i)=4.
$$
Hence
$$
\operatorname{Res}_{z=-3i}F_\alpha(z)
=
\frac{e^{i\alpha(-3i)}}{(-i)4}
=
-\frac{e^{3\alpha}}{4i}.
$$

:::

:::

::: {.pf-step #s1-4}

If $\alpha>0$, then
$$
\boxed{
\int_{-\infty}^{\infty}
\frac{e^{i\alpha x}}
{(3-ix)(1+ix)}\,dx
=
\frac\pi2 e^{-\alpha}.
}
$$


::: pf-proof

Close the real segment by an upper semicircle. On the upper half-plane,
$$
\abs{e^{i\alpha z}}
=
e^{-\alpha\operatorname{Im}z}
\leq1.
$$
On the arc $\abs{z}=R$,
$$
\abs{3-iz}
\geq
R-3
$$
and
$$
\abs{1+iz}
\geq
R-1.
$$
Thus the arc integral is bounded in absolute value by
$$
\frac{\pi R}{(R-3)(R-1)}
\longrightarrow0.
$$
The only enclosed pole is $i$. Hence by step [](#s1-2){.pf-ref},
$$
\int_{-\infty}^{\infty}
\frac{e^{i\alpha x}}
{(3-ix)(1+ix)}\,dx
=
2\pi i
\frac{e^{-\alpha}}{4i}
=
\frac\pi2 e^{-\alpha}.
$$

:::

:::

::: {.pf-step #s1-5}

If $\alpha<0$, then
$$
\boxed{
\int_{-\infty}^{\infty}
\frac{e^{i\alpha x}}
{(3-ix)(1+ix)}\,dx
=
\frac\pi2 e^{3\alpha}.
}
$$


::: pf-proof

Close in the lower half-plane. There
$$
\abs{e^{i\alpha z}}
\leq1
$$
because $\alpha<0$ and $\operatorname{Im}z\leq0$. The same denominator
estimate as in step [](#s1-4){.pf-ref} makes the lower-arc integral tend to zero.

The contour is clockwise and encloses only the pole $-3i$. Therefore, using
step [](#s1-3){.pf-ref},
$$
\begin{aligned}
\int_{-\infty}^{\infty}
\frac{e^{i\alpha x}}
{(3-ix)(1+ix)}\,dx
&=
-2\pi i
\left(
-\frac{e^{3\alpha}}{4i}
\right)\\
&=
\frac\pi2 e^{3\alpha}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-6}

If $\alpha=0$, then
$$
\int_{-\infty}^{\infty}
\frac{dx}{(3-ix)(1+ix)}
=
\frac\pi2.
$$


::: pf-proof

Close in the upper half-plane. The rational integrand is $O(\abs{z}^{-2})$, so
the semicircular arc tends to zero. The residue at $i$ is $1/(4i)$ by
step [](#s1-2){.pf-ref} with $\alpha=0$. Thus the residue theorem gives $\pi/2$.

:::

:::

::: {.pf-step #s1-7}

Hence, for every real $\alpha$,
$$
\boxed{
\int_{-\infty}^{\infty}
\frac{e^{i\alpha x}}
{(3-ix)(1+ix)}\,dx
=
\begin{cases}
\dfrac\pi2 e^{-\alpha},&\alpha\geq0,\\[6pt]
\dfrac\pi2 e^{3\alpha},&\alpha\leq0.
\end{cases}
}
$$


::: pf-proof

Steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} give the three sign cases. At $\alpha=0$, both displayed
formulas equal $\pi/2$.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required integral.

:::

:::

:::
