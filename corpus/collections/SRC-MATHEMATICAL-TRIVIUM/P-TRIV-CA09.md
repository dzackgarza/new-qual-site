---
schema: qual/card@1
id: P-TRIV-CA09
kind: problem
title: Conformal map from the unit disk onto the left half-plane
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 9, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find an analytic map that sends the unit disk $( | z | < 1 )$ onto the left half plane $( \mathrm { R e } ( z ) < 0 )$
:::

::: {.solution}
Define
$$
\Phi(z)
=
-\frac{1+z}{1-z}.
$$

<1>1. The function $\Phi$ is analytic on the unit disk.

::: {.proof}
Its only pole is at $z=1$, which lies on the boundary of the unit disk and
not inside it.
:::

<1>2. For every $|z|<1$,
$$
\operatorname{Re}\Phi(z)
=
-\frac{1-|z|^2}{|1-z|^2}.
$$

::: {.proof}
Multiply numerator and denominator by $1-\overline z$:
$$
\begin{aligned}
\Phi(z)
&=
-\frac{(1+z)(1-\overline z)}
{|1-z|^2}\\
&=
-\frac{
1-|z|^2+z-\overline z
}{
|1-z|^2}.
\end{aligned}
$$
The term $z-\overline z$ is purely imaginary, so taking real parts gives the
formula.
:::

<1>3. The image of the unit disk under $\Phi$ lies in the left half-plane.

::: {.proof}
If $|z|<1$, then
$$
1-|z|^2>0.
$$
By step <1>2,
$$
\operatorname{Re}\Phi(z)<0.
$$
:::

<1>4. Solving $w=\Phi(z)$ for $z$ gives
$$
z
=
\frac{1+w}{w-1}.
$$

::: {.proof}
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

<1>5. If
$$
\operatorname{Re}w<0,
$$
then
$$
\left|
\frac{1+w}{w-1}
\right|<1.
$$

::: {.proof}
The inequality is equivalent to
$$
|1+w|<|1-w|.
$$
Squaring both sides gives
$$
1+2\operatorname{Re}w+|w|^2
<
1-2\operatorname{Re}w+|w|^2,
$$
which is exactly
$$
\operatorname{Re}w<0.
$$
:::

<1>6. The map $\Phi$ is onto the left half-plane.

::: {.proof}
Let $w$ satisfy
$$
\operatorname{Re}w<0.
$$
Define
$$
z=\frac{1+w}{w-1}.
$$
By step <1>5, $|z|<1$. Step <1>4 shows that
$$
\Phi(z)=w.
$$
Thus every point of the left half-plane has a preimage in the unit disk.
:::

<1>7. Therefore
$$
\boxed{
\Phi(z)
=
-\frac{1+z}{1-z}
}
$$
is an analytic map from the unit disk onto the left half-plane.

::: {.proof}
Step <1>1 gives analyticity, step <1>3 gives containment of the image, and
step <1>6 gives surjectivity.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the requested map and verification.
:::
:::
