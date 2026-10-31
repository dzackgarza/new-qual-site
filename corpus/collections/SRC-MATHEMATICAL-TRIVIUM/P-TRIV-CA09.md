---
schema: qual/card@1
id: P-TRIV-CA09
kind: problem
title: Conformal map from the unit disk onto the left half-plane
classification:
  areas: [complex-analysis]
  topics:
  - Conformal Maps
  - Mobius Transformations
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 9, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find an analytic map that sends the unit disk ($\abs{z} < 1$) onto the left half plane ($\Re(z) < 0$).
:::

::: {.solution}

Define
$$
\Phi(z)
=
-\frac{1+z}{1-z}.
$$

::: pf

::: {.pf-step #s1-1}

The function $\Phi$ is analytic on the unit disk.


::: pf-proof

Its only pole is at $z=1$, which lies on the boundary of the unit disk and
not inside it.

:::

:::

::: {.pf-step #s1-2}

For every $\abs{z}<1$,
$$
\operatorname{Re}\Phi(z)
=
-\frac{1-\abs{z}^2}{\abs{1-z}^2}.
$$


::: pf-proof

Multiply numerator and denominator by $1-\overline z$:
$$
\begin{aligned}
\Phi(z)
&=
-\frac{(1+z)(1-\overline z)}
{\abs{1-z}^2}\\
&=
-\frac{
1-\abs{z}^2+z-\overline z
}{
\abs{1-z}^2}.
\end{aligned}
$$
The term $z-\overline z$ is purely imaginary, so taking real parts gives the
formula.

:::

:::

::: {.pf-step #s1-3}

The image of the unit disk under $\Phi$ lies in the left half-plane.


::: pf-proof

If $\abs{z}<1$, then
$$
1-\abs{z}^2>0.
$$
By step [](#s1-2){.pf-ref},
$$
\operatorname{Re}\Phi(z)<0.
$$

:::

:::

::: {.pf-step #s1-4}

Solving $w=\Phi(z)$ for $z$ gives
$$
z
=
\frac{1+w}{w-1}.
$$


::: pf-proof

Starting from
$$
w
=
-\frac{1+z}{1-z},
$$
one gets
$$
w(1-z)=-1-z.
$$
Rearranging yields
$$
z(1-w)=-(1+w),
$$
which is equivalent to the displayed formula.

:::

:::

::: {.pf-step #s1-5}

If
$$
\operatorname{Re}w<0,
$$
then
$$
\abs{
\frac{1+w}{w-1}
}<1.
$$


::: pf-proof

The inequality is equivalent to
$$
\abs{1+w}<\abs{1-w}.
$$
Squaring both sides gives
$$
1+2\operatorname{Re}w+\abs{w}^2
<
1-2\operatorname{Re}w+\abs{w}^2,
$$
which is exactly
$$
\operatorname{Re}w<0.
$$

:::

:::

::: {.pf-step #s1-6}

The map $\Phi$ is onto the left half-plane.


::: pf-proof

Let $w$ satisfy
$$
\operatorname{Re}w<0.
$$
Define
$$
z=\frac{1+w}{w-1}.
$$
By step [](#s1-5){.pf-ref}, $\abs{z}<1$. Step [](#s1-4){.pf-ref} shows that
$$
\Phi(z)=w.
$$
Thus every point of the left half-plane has a preimage in the unit disk.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
\Phi(z)
=
-\frac{1+z}{1-z}
}
$$
is an analytic map from the unit disk onto the left half-plane.


::: pf-proof

Step [](#s1-1){.pf-ref} gives analyticity, step [](#s1-3){.pf-ref} gives containment of the image, and
step [](#s1-6){.pf-ref} gives surjectivity.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the requested map and verification.

:::

:::

:::
