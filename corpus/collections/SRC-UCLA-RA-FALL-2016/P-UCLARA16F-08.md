---
schema: qual/card@1
id: P-UCLARA16F-08
kind: problem
title: Jensen's inequality and boundary zeros of disk algebra functions
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $f$ be a continuous complex-valued function on the closed unit disk $\overline D$ such that $f$ is holomorphic on the open disk $D=\{z\in\mathbb C:|z|<1\}$ and $f(0)\ne0$.

(a) Show that if $0<r<1$ and $\inf_{|z|=r}|f(z)|>0$, then
\[
\frac1{2\pi}\int_0^{2\pi}\log|f(re^{i\theta})|\,d\theta\ge\log|f(0)|.
\]

(b) Show that
\[
\bigl|\{\theta\in[0,2\pi]:f(e^{i\theta})=0\}\bigr|=0,
\]
where $|E|$ denotes the Lebesgue measure of $E\subset[0,2\pi]$.
:::

::: {.solution}
## Part (a)

Fix
\[
0<r<1
\]
and assume
\[
\inf_{|z|=r}|f(z)|>0.
\]

<1>1. The function \(f\) has no zeros on the circle \(|z|=r\).

::: {.proof}
The stated positive lower bound on \(|f|\) excludes zeros there.
:::

<1>2. The function \(f\) has only finitely many zeros in the closed disk
\[
\{|z|\le r\}.
\]

::: {.proof}
Zeros of a nonzero holomorphic function are isolated. Since
\[
f(0)\ne0,
\]
the function is not identically zero. An infinite set of zeros in the compact disk would have an accumulation point there, contradicting the identity theorem.
:::

Let
\[
a_1,\dots,a_N
\]
be the zeros of \(f\) in \(|z|<r\), listed with multiplicity.

For \(a\) with \(|a|<r\), define the radius-\(r\) Blaschke factor
\[
\boxed{
B_a(z)
=
\frac{r(z-a)}{r^2-\overline a z}}.
\]

<1>3. The denominator
\[
r^2-\overline a z
\]
does not vanish on \(|z|\le r\).

::: {.proof}
For \(|z|\le r\),
\[
|\overline a z|
\le
|a|r
<
r^2.
\]
Hence
\[
r^2-\overline a z\ne0.
\]
:::

<1>4. On the boundary circle \(|z|=r\),
\[
\boxed{|B_a(z)|=1}.
\]

::: {.proof}
If \(|z|=r\), then
\[
|r^2-\overline a z|
=
|z|\,|z-a|
=
r|z-a|.
\]
Therefore
\[
|B_a(z)|
=
\frac{r|z-a|}{|r^2-\overline a z|}
=
1.
\]
:::

<1>5. At \(z=0\),
\[
\boxed{
|B_a(0)|
=
\frac{|a|}{r}}.
\]

::: {.proof}
\[
B_a(0)
=
\frac{r(0-a)}{r^2}
=
-\frac ar.
\]
:::

Define
\[
\boxed{
g(z)
=
\frac{f(z)}
{\prod_{j=1}^{N}B_{a_j}(z)}}.
\]

<1>6. The function \(g\) extends holomorphically to \(|z|<r\) and has no zeros there.

::: {.proof}
Each \(B_{a_j}\) has exactly one zero at \(a_j\), with the same multiplicity contribution used in the list of zeros. Dividing by the product cancels all zeros of \(f\) in \(|z|<r\). Step <1>3 shows the Blaschke denominators introduce no singularities in the disk. Thus the quotient extends holomorphically and is zero-free.
:::

<1>7. The function
\[
\log|g(z)|
\]
is harmonic on \(|z|<r\).

::: {.proof}
A zero-free holomorphic function has locally a holomorphic logarithm, whose real part is \(\log|g|\). Hence \(\log|g|\) is harmonic.
:::

<1>8. By the mean-value property,
\[
\boxed{
\log|g(0)|
=
\frac1{2\pi}
\int_0^{2\pi}
\log|g(re^{i\theta})|\,d\theta}.
\]

::: {.proof}
Apply the harmonic mean-value property to \(\log|g|\) on the disk of radius \(r\).
:::

<1>9. On \(|z|=r\),
\[
\boxed{|g(z)|=|f(z)|}.
\]

::: {.proof}
By step <1>4, every factor \(B_{a_j}\) has modulus \(1\) on the boundary circle.
:::

<1>10. At the origin,
\[
|g(0)|
=
|f(0)|
\prod_{j=1}^{N}
\frac r{|a_j|}.
\]

::: {.proof}
Using step <1>5,
\[
\left|
\prod_{j=1}^{N}B_{a_j}(0)
\right|
=
\prod_{j=1}^{N}
\frac{|a_j|}{r}.
\]
Since \(f(0)\ne0\), none of the zeros \(a_j\) equals \(0\). Divide.
:::

<1>11. Therefore
\[
\boxed{
\frac1{2\pi}
\int_0^{2\pi}
\log|f(re^{i\theta})|\,d\theta
=
\log|f(0)|
+
\sum_{j=1}^{N}
\log\frac r{|a_j|}}.
\]

::: {.proof}
Use steps <1>8--<1>10 and take logarithms of the product in step <1>10.
:::

<1>12. Every term in the sum in step <1>11 is positive.

::: {.proof}
Each zero satisfies
\[
|a_j|<r,
\]
so
\[
r/|a_j|>1.
\]
:::

<1>13. Hence
\[
\boxed{
\frac1{2\pi}
\int_0^{2\pi}
\log|f(re^{i\theta})|\,d\theta
\ge
\log|f(0)|}.
\]

::: {.proof}
Drop the nonnegative sum from step <1>11.
:::

## Part (b)

Let
\[
E
=
\{\theta\in[0,2\pi]:
f(e^{i\theta})=0\}.
\]

<1>14. The set of radii
\[
\{|a|:f(a)=0,\ a\in D\}
\]
is countable.

::: {.proof}
The zeros of a nonzero holomorphic function are discrete in \(D\). A discrete subset of a second-countable space is countable.
:::

<1>15. Therefore one can choose a sequence
\[
r_n\uparrow1
\]
such that \(f\) has no zeros on \(|z|=r_n\).

::: {.proof}
Avoid the countable set of zero moduli from step <1>14 while choosing \(r_n\to1\).
:::

<1>16. For every \(n\),
\[
\boxed{
\frac1{2\pi}
\int_0^{2\pi}
\log|f(r_ne^{i\theta})|\,d\theta
\ge
\log|f(0)|}.
\]

::: {.proof}
Since \(f\) is continuous on the compact circle \(|z|=r_n\) and has no zeros there, its modulus has a positive minimum. Apply part (a), step <1>13.
:::

Suppose, toward a contradiction, that
\[
|E|>0.
\]

<1>17. Since \(f\) is continuous on the compact closed disk, it is uniformly continuous.

::: {.proof}
Every continuous function on a compact metric space is uniformly continuous.
:::

<1>18. Define
\[
\delta_n
=
\sup_{\theta\in E}
|f(r_ne^{i\theta})|.
\]
Then
\[
\boxed{\delta_n\to0}.
\]

::: {.proof}
For \(\theta\in E\),
\[
f(e^{i\theta})=0.
\]
Also
\[
|r_ne^{i\theta}-e^{i\theta}|
=
1-r_n\to0
\]
uniformly in \(\theta\). Uniform continuity from step <1>17 therefore gives
\[
\sup_{\theta\in E}
|f(r_ne^{i\theta})-f(e^{i\theta})|
\to0.
\]
The second term is zero on \(E\).
:::

<1>19. Let
\[
M
=
\max_{|z|\le1}|f(z)|.
\]
Then
\[
\boxed{0<M<\infty}.
\]

::: {.proof}
Continuity on the compact closed disk gives a finite maximum. Since
\[
f(0)\ne0,
\]
the maximum is positive.
:::

<1>20. For every \(n\),
\[
\int_0^{2\pi}
\log|f(r_ne^{i\theta})|\,d\theta
\le
|E|\log\delta_n
+
(2\pi-|E|)\log M.
\]

::: {.proof}
On \(E\),
\[
|f(r_ne^{i\theta})|
\le
\delta_n,
\]
so
\[
\log|f(r_ne^{i\theta})|
\le
\log\delta_n.
\]
On the complement of \(E\),
\[
|f(r_ne^{i\theta})|
\le
M,
\]
so the logarithm is at most \(\log M\). Integrate the two bounds over the two measurable pieces.
:::

<1>21. Since
\[
|E|>0
\]
and
\[
\delta_n\to0,
\]
the right-hand side in step <1>20 tends to \(-\infty\).

::: {.proof}
\[
\log\delta_n\to-\infty,
\]
and it is multiplied by the positive number \(|E|\). The remaining term is constant in \(n\).
:::

<1>22. Therefore
\[
\boxed{
\frac1{2\pi}
\int_0^{2\pi}
\log|f(r_ne^{i\theta})|\,d\theta
\to
-\infty}.
\]

::: {.proof}
Use steps <1>20--<1>21.
:::

<1>23. This contradicts the uniform lower bound in step <1>16.

::: {.proof}
Step <1>16 says every average is at least the finite number
\[
\log|f(0)|.
\]
:::

<1>24. Hence
\[
\boxed{|E|=0}.
\]

::: {.proof}
The assumption \(|E|>0\) led to the contradiction in step <1>23.
:::

<1>25. Q.E.D.

::: {.proof}
Step <1>13 proves part (a), and step <1>24 proves part (b).
:::
:::
