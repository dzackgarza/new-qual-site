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

## Part (a)

Fix
\[
0<r<1
\]
and assume
\[
\inf_{|z|=r}|f(z)|>0.
\]

::: pf

::: pf-step

The function \(f\) has no zeros on the circle \(|z|=r\).


::: pf-proof

The stated positive lower bound on \(|f|\) excludes zeros there.

:::

:::

::: pf-step

The function \(f\) has only finitely many zeros in the closed disk
\[
\{|z|\le r\}.
\]


::: pf-proof

Zeros of a nonzero holomorphic function are isolated. Since
\[
f(0)\ne0,
\]
the function is not identically zero. An infinite set of zeros in the compact disk would have an accumulation point there, contradicting the identity theorem.

:::

:::

::: pf-step

The denominator
\[
r^2-\overline a z
\]
does not vanish on \(|z|\le r\).


::: pf-proof

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

:::

::: pf-step

On the boundary circle \(|z|=r\),
\[
\boxed{|B_a(z)|=1}.
\]


::: pf-proof

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

:::

::: pf-step

At \(z=0\),
\[
\boxed{
|B_a(0)|
=
\frac{|a|}{r}}.
\]


::: pf-proof

\[
B_a(0)
=
\frac{r(0-a)}{r^2}
=
-\frac ar.
\]

:::

:::

::: pf-step

The function \(g\) extends holomorphically to \(|z|<r\) and has no zeros there.


::: pf-proof

Each \(B_{a_j}\) has exactly one zero at \(a_j\), with the same multiplicity contribution used in the list of zeros. Dividing by the product cancels all zeros of \(f\) in \(|z|<r\). Step <1>3 shows the Blaschke denominators introduce no singularities in the disk. Thus the quotient extends holomorphically and is zero-free.

:::

:::

::: pf-step

The function
\[
\log|g(z)|
\]
is harmonic on \(|z|<r\).


::: pf-proof

A zero-free holomorphic function has locally a holomorphic logarithm, whose real part is \(\log|g|\). Hence \(\log|g|\) is harmonic.

:::

:::

::: pf-step

By the mean-value property,
\[
\boxed{
\log|g(0)|
=
\frac1{2\pi}
\int_0^{2\pi}
\log|g(re^{i\theta})|\,d\theta}.
\]


::: pf-proof

Apply the harmonic mean-value property to \(\log|g|\) on the disk of radius \(r\).

:::

:::

::: pf-step

On \(|z|=r\),
\[
\boxed{|g(z)|=|f(z)|}.
\]


::: pf-proof

By step <1>4, every factor \(B_{a_j}\) has modulus \(1\) on the boundary circle.

:::

:::

::: pf-step

At the origin,
\[
|g(0)|
=
|f(0)|
\prod_{j=1}^{N}
\frac r{|a_j|}.
\]


::: pf-proof

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

:::

::: pf-step

Therefore
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


::: pf-proof

Use steps <1>8--<1>10 and take logarithms of the product in step <1>10.

:::

:::

::: pf-step

Every term in the sum in step <1>11 is positive.


::: pf-proof

Each zero satisfies
\[
|a_j|<r,
\]
so
\[
r/|a_j|>1.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
\frac1{2\pi}
\int_0^{2\pi}
\log|f(re^{i\theta})|\,d\theta
\ge
\log|f(0)|}.
\]


::: pf-proof

Drop the nonnegative sum from step <1>11.

:::

:::

::: pf-step

The set of radii
\[
\{|a|:f(a)=0,\ a\in D\}
\]
is countable.


::: pf-proof

The zeros of a nonzero holomorphic function are discrete in \(D\). A discrete subset of a second-countable space is countable.

:::

:::

::: pf-step

Therefore one can choose a sequence
\[
r_n\uparrow1
\]
such that \(f\) has no zeros on \(|z|=r_n\).


::: pf-proof

Avoid the countable set of zero moduli from step <1>14 while choosing \(r_n\to1\).

:::

:::

::: pf-step

For every \(n\),
\[
\boxed{
\frac1{2\pi}
\int_0^{2\pi}
\log|f(r_ne^{i\theta})|\,d\theta
\ge
\log|f(0)|}.
\]


::: pf-proof

Since \(f\) is continuous on the compact circle \(|z|=r_n\) and has no zeros there, its modulus has a positive minimum. Apply part (a), step <1>13.

:::

:::

::: pf-step

Since \(f\) is continuous on the compact closed disk, it is uniformly continuous.


::: pf-proof

Every continuous function on a compact metric space is uniformly continuous.

:::

:::

::: pf-step

Define
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


::: pf-proof

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

:::

::: pf-step

Let
\[
M
=
\max_{|z|\le1}|f(z)|.
\]
Then
\[
\boxed{0<M<\infty}.
\]


::: pf-proof

Continuity on the compact closed disk gives a finite maximum. Since
\[
f(0)\ne0,
\]
the maximum is positive.

:::

:::

::: pf-step

For every \(n\),
\[
\int_0^{2\pi}
\log|f(r_ne^{i\theta})|\,d\theta
\le
|E|\log\delta_n
+
(2\pi-|E|)\log M.
\]


::: pf-proof

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

:::

::: pf-step

Since
\[
|E|>0
\]
and
\[
\delta_n\to0,
\]
the right-hand side in step <1>20 tends to \(-\infty\).


::: pf-proof

\[
\log\delta_n\to-\infty,
\]
and it is multiplied by the positive number \(|E|\). The remaining term is constant in \(n\).

:::

:::

::: pf-step

Therefore
\[
\boxed{
\frac1{2\pi}
\int_0^{2\pi}
\log|f(r_ne^{i\theta})|\,d\theta
\to
-\infty}.
\]


::: pf-proof

Use steps <1>20--<1>21.

:::

:::

::: pf-step

This contradicts the uniform lower bound in step <1>16.


::: pf-proof

Step <1>16 says every average is at least the finite number
\[
\log|f(0)|.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{|E|=0}.
\]


::: pf-proof

The assumption \(|E|>0\) led to the contradiction in step <1>23.

:::

:::

::: pf-qed

Step <1>13 proves part (a), and step <1>24 proves part (b).

:::

:::
