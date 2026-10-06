---
schema: qual/card@1
id: P-WESCA08-II2
kind: problem
title: 'Two contour integrals on large circles'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Evaluate
\[
\int_{|z-i|=10}\left(z+\frac1z\right)^4\,dz
\]
and
\[
\int_{|z|=4}\left(\frac{\sin z}{z}\right)^{100}\,dz.
\]
:::

::: {.solution}
<1>1. Expand the first integrand:
\[
\boxed{
\left(z+\frac1z\right)^4
=
z^4+4z^2+6+\frac4{z^2}+\frac1{z^4}}.
\]

::: {.proof}
Apply the binomial theorem:
\[
\begin{aligned}
\left(z+\frac1z\right)^4
&=
z^4
+4z^3\frac1z
+6z^2\frac1{z^2}
+4z\frac1{z^3}
+\frac1{z^4}\\
&=
z^4+4z^2+6+\frac4{z^2}+\frac1{z^4}.
\end{aligned}
\]
:::

<1>2. The only singularity of the first integrand is
\[
z=0,
\]
and it lies inside the circle
\[
|z-i|=10.
\]

::: {.proof}
The expansion in step <1>1 shows that the only negative powers occur at
\(z=0\). Moreover,
\[
|0-i|=1<10.
\]
:::

<1>3. The residue at \(z=0\) is zero:
\[
\boxed{
\operatorname{Res}_{z=0}
\left(z+\frac1z\right)^4
=0}.
\]

::: {.proof}
The residue is the coefficient of \(z^{-1}\) in the Laurent expansion.
Step <1>1 contains no \(z^{-1}\)-term.
:::

<1>4. Therefore
\[
\boxed{
\int_{|z-i|=10}
\left(z+\frac1z\right)^4\,dz
=0}.
\]

::: {.proof}
By the residue theorem,
\[
\int_{|z-i|=10}
\left(z+\frac1z\right)^4\,dz
=
2\pi i\,
\operatorname{Res}_{z=0}
\left(z+\frac1z\right)^4.
\]
Apply step <1>3.
:::

<1>5. Define
\[
g(z)
=
\begin{cases}
\dfrac{\sin z}{z},&z\ne0,\\[6pt]
1,&z=0.
\end{cases}
\]
Then \(g\) is entire.

::: {.proof}
The Taylor series
\[
\sin z
=
z-\frac{z^3}{3!}+\frac{z^5}{5!}-\cdots
\]
gives, for \(z\ne0\),
\[
\frac{\sin z}{z}
=
1-\frac{z^2}{3!}+\frac{z^4}{5!}-\cdots.
\]
The right-hand side is a power series converging on all of \(\mathbb C\),
and its value at \(0\) is \(1\). Thus the apparent singularity at \(0\) is
removable and the specified extension is entire.
:::

<1>6. Hence
\[
\boxed{
g(z)^{100}}
\]
is entire.

::: {.proof}
A finite product of entire functions is entire.
:::

<1>7. On the circle \(|z|=4\),
\[
g(z)^{100}
=
\left(\frac{\sin z}{z}\right)^{100}.
\]

::: {.proof}
The circle \(|z|=4\) does not contain \(z=0\), so the defining formula for
\(g\) there is exactly
\[
g(z)=\frac{\sin z}{z}.
\]
:::

<1>8. Therefore
\[
\boxed{
\int_{|z|=4}
\left(\frac{\sin z}{z}\right)^{100}\,dz
=0}.
\]

::: {.proof}
By steps <1>6--<1>7, the integrand on the contour is the restriction of the
entire function \(g^{100}\). Cauchy's integral theorem gives zero around the
closed circle.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>4 and <1>8 evaluate the two requested contour integrals.
:::
:::
