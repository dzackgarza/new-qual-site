---
schema: qual/card@1
id: P-UCLARA16F-08
kind: problem
title: Jensen's inequality and boundary zeros of disk algebra functions
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Subharmonic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $f$ be a continuous complex-valued function on the closed unit disk $\overline D$ such that $f$ is holomorphic on the open disk $D=\{z\in\CC:\abs{z}<1\}$ and $f(0)\ne0$.

(a) Show that if $0<r<1$ and $\inf_{\abs{z}=r}\abs{f(z)}>0$, then
$$
\frac1{2\pi}\int_0^{2\pi}\log\abs{f(re^{i\theta})}\,d\theta\ge\log\abs{f(0)}.
$$

(b) Show that
$$
\setmeasure{\{\theta\in[0,2\pi]:f(e^{i\theta})=0\}}=0,
$$
where $\setmeasure{E}$ denotes the Lebesgue measure of $E\subset[0,2\pi]$.
:::

::: {.solution}

## Part (a)

Fix
$$
0<r<1
$$
and assume
$$
\inf_{\abs{z}=r}\abs{f(z)}>0.
$$

::: pf

::: pf-step

The function $f$ has no zeros on the circle $\abs{z}=r$.


::: pf-proof

The stated positive lower bound on $\abs{f}$ excludes zeros there.

:::

:::

::: pf-step

The function $f$ has only finitely many zeros in the closed disk
$$
\{\abs{z}\le r\}.
$$


::: pf-proof

Zeros of a nonzero holomorphic function are isolated. Since
$$
f(0)\ne0,
$$
the function is not identically zero. An infinite set of zeros in the compact disk would have an accumulation point there, contradicting the identity theorem.

:::

:::

::: {.pf-step #s1-3}

The denominator
$$
r^2-\overline a z
$$
does not vanish on $\abs{z}\le r$.


::: pf-proof

For $\abs{z}\le r$,
$$
\abs{\overline a z}
\le
\abs{a}r
<
r^2.
$$
Hence
$$
r^2-\overline a z\ne0.
$$

:::

:::

::: {.pf-step #s1-4}

On the boundary circle $\abs{z}=r$,
$$
\boxed{\abs{B_a(z)}=1}.
$$


::: pf-proof

If $\abs{z}=r$, then
$$
\abs{r^2-\overline a z}
=
\abs{z}\,\abs{z-a}
=
r\abs{z-a}.
$$
Therefore
$$
\abs{B_a(z)}
=
\frac{r\abs{z-a}}{\abs{r^2-\overline a z}}
=
1.
$$

:::

:::

::: {.pf-step #s1-5}

At $z=0$,
$$
\boxed{
\abs{B_a(0)}
=
\frac{\abs{a}}{r}}.
$$


::: pf-proof

$$
B_a(0)
=
\frac{r(0-a)}{r^2}
=
-\frac ar.
$$

:::

:::

::: pf-step

The function $g$ extends holomorphically to $\abs{z}<r$ and has no zeros there.


::: pf-proof

Each $B_{a_j}$ has exactly one zero at $a_j$, with the same multiplicity contribution used in the list of zeros. Dividing by the product cancels all zeros of $f$ in $\abs{z}<r$. Step [](#s1-3){.pf-ref} shows the Blaschke denominators introduce no singularities in the disk. Thus the quotient extends holomorphically and is zero-free.

:::

:::

::: pf-step

The function
$$
\log\abs{g(z)}
$$
is harmonic on $\abs{z}<r$.


::: pf-proof

A zero-free holomorphic function has locally a holomorphic logarithm, whose real part is $\log\abs{g}$. Hence $\log\abs{g}$ is harmonic.

:::

:::

::: {.pf-step #s1-8}

By the mean-value property,
$$
\boxed{
\log\abs{g(0)}
=
\frac1{2\pi}
\int_0^{2\pi}
\log\abs{g(re^{i\theta})}\,d\theta}.
$$


::: pf-proof

Apply the harmonic mean-value property to $\log\abs{g}$ on the disk of radius $r$.

:::

:::

::: {.pf-step #s1-9}

On $\abs{z}=r$,
$$
\boxed{\abs{g(z)}=\abs{f(z)}}.
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, every factor $B_{a_j}$ has modulus $1$ on the boundary circle.

:::

:::

::: {.pf-step #s1-10}

At the origin,
$$
\abs{g(0)}
=
\abs{f(0)}
\prod_{j=1}^{N}
\frac r{\abs{a_j}}.
$$


::: pf-proof

Using step [](#s1-5){.pf-ref},
$$
\abs{
\prod_{j=1}^{N}B_{a_j}(0)
}
=
\prod_{j=1}^{N}
\frac{\abs{a_j}}{r}.
$$
Since $f(0)\ne0$, none of the zeros $a_j$ equals $0$. Divide.

:::

:::

::: {.pf-step #s1-11}

Therefore
$$
\boxed{
\frac1{2\pi}
\int_0^{2\pi}
\log\abs{f(re^{i\theta})}\,d\theta
=
\log\abs{f(0)}
+
\sum_{j=1}^{N}
\log\frac r{\abs{a_j}}}.
$$


::: pf-proof

Use steps [](#s1-8){.pf-ref} through [](#s1-10){.pf-ref} and take logarithms of the product in step [](#s1-10){.pf-ref}.

:::

:::

::: pf-step

Every term in the sum in step [](#s1-11){.pf-ref} is positive.


::: pf-proof

Each zero satisfies
$$
\abs{a_j}<r,
$$
so
$$
r/\abs{a_j}>1.
$$

:::

:::

::: {.pf-step #s1-13}

Hence
$$
\boxed{
\frac1{2\pi}
\int_0^{2\pi}
\log\abs{f(re^{i\theta})}\,d\theta
\ge
\log\abs{f(0)}}.
$$


::: pf-proof

Drop the nonnegative sum from step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-14}

The set of radii
$$
\{\abs{a}:f(a)=0,\ a\in D\}
$$
is countable.


::: pf-proof

The zeros of a nonzero holomorphic function are discrete in $D$. A discrete subset of a second-countable space is countable.

:::

:::

::: pf-step

Therefore one can choose a sequence
$$
r_n\uparrow1
$$
such that $f$ has no zeros on $\abs{z}=r_n$.


::: pf-proof

Avoid the countable set of zero moduli from step [](#s1-14){.pf-ref} while choosing $r_n\to1$.

:::

:::

::: {.pf-step #s1-16}

For every $n$,
$$
\boxed{
\frac1{2\pi}
\int_0^{2\pi}
\log\abs{f(r_ne^{i\theta})}\,d\theta
\ge
\log\abs{f(0)}}.
$$


::: pf-proof

Since $f$ is continuous on the compact circle $\abs{z}=r_n$ and has no zeros there, its modulus has a positive minimum. Apply part (a), step [](#s1-13){.pf-ref}.

:::

:::

::: {.pf-step #s1-17}

Since $f$ is continuous on the compact closed disk, it is uniformly continuous.


::: pf-proof

Every continuous function on a compact metric space is uniformly continuous.

:::

:::

::: pf-step

Define
$$
\delta_n
=
\sup_{\theta\in E}
\abs{f(r_ne^{i\theta})}.
$$
Then
$$
\boxed{\delta_n\to0}.
$$


::: pf-proof

For $\theta\in E$,
$$
f(e^{i\theta})=0.
$$
Also
$$
\abs{r_ne^{i\theta}-e^{i\theta}}
=
1-r_n\to0
$$
uniformly in $\theta$. Uniform continuity from step [](#s1-17){.pf-ref} therefore gives
$$
\sup_{\theta\in E}
\abs{f(r_ne^{i\theta})-f(e^{i\theta})}
\to0.
$$
The second term is zero on $E$.

:::

:::

::: pf-step

Let
$$
M
=
\max_{\abs{z}\le1}\abs{f(z)}.
$$
Then
$$
\boxed{0<M<\infty}.
$$


::: pf-proof

Continuity on the compact closed disk gives a finite maximum. Since
$$
f(0)\ne0,
$$
the maximum is positive.

:::

:::

::: {.pf-step #s1-20}

For every $n$,
$$
\int_0^{2\pi}
\log\abs{f(r_ne^{i\theta})}\,d\theta
\le
\setmeasure{E}\log\delta_n
+
(2\pi-\setmeasure{E})\log M.
$$


::: pf-proof

On $E$,
$$
\abs{f(r_ne^{i\theta})}
\le
\delta_n,
$$
so
$$
\log\abs{f(r_ne^{i\theta})}
\le
\log\delta_n.
$$
On the complement of $E$,
$$
\abs{f(r_ne^{i\theta})}
\le
M,
$$
so the logarithm is at most $\log M$. Integrate the two bounds over the two measurable pieces.

:::

:::

::: {.pf-step #s1-21}

Since
$$
\setmeasure{E}>0
$$
and
$$
\delta_n\to0,
$$
the right-hand side in step [](#s1-20){.pf-ref} tends to $-\infty$.


::: pf-proof

$$
\log\delta_n\to-\infty,
$$
and it is multiplied by the positive number $\setmeasure{E}$. The remaining term is constant in $n$.

:::

:::

::: pf-step

Therefore
$$
\boxed{
\frac1{2\pi}
\int_0^{2\pi}
\log\abs{f(r_ne^{i\theta})}\,d\theta
\to
-\infty}.
$$


::: pf-proof

Use steps [](#s1-20){.pf-ref} through [](#s1-21){.pf-ref}.

:::

:::

::: {.pf-step #s1-23}

This contradicts the uniform lower bound in step [](#s1-16){.pf-ref}.


::: pf-proof

Step [](#s1-16){.pf-ref} says every average is at least the finite number
$$
\log\abs{f(0)}.
$$

:::

:::

::: {.pf-step #s1-24}

Hence
$$
\boxed{\setmeasure{E}=0}.
$$


::: pf-proof

The assumption $\setmeasure{E}>0$ led to the contradiction in step [](#s1-23){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-13){.pf-ref} proves part (a), and step [](#s1-24){.pf-ref} proves part (b).

:::

:::

:::
