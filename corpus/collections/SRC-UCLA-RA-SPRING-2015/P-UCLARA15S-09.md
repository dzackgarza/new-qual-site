---
schema: qual/card@1
id: P-UCLARA15S-09
kind: problem
title: Bounded harmonic function in $\{|z|>1,\ \operatorname{Re}z>-2\}$ with constant boundary values
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2015, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let
\[
\Omega=\{z\in\CC:|z|>1\text{ and }\operatorname{Re}z>-2\}.
\]
Suppose $u:\Omega\to\RR$ is bounded, continuous, and harmonic on $\Omega$, with $u(z)=1$ when $|z|=1$ and $u(z)=0$ when $\operatorname{Re}z=-2$.
Determine $u(2)$.
:::

::: {.solution}

Set
\[
r\coloneqq2-\sqrt3.
\]
Then $0<r<1$ and
\[
r^2-4r+1=0.
\]

::: pf

::: {.pf-step #s1-1}

The inversion
\[
I(z)=\frac1z
\]
maps $\Omega$ conformally onto
\[
\Omega'
=
\left\{
w\in\DD:
\left|w+\frac14\right|>\frac14
\right\}.
\]


::: pf-proof

The condition $|z|>1$ is equivalent under $w=1/z$ to $|w|<1$. Also
\[
\operatorname{Re}z>-2
\]
becomes
\[
\operatorname{Re}\frac1w>-2.
\]
Since
\[
\operatorname{Re}\frac1w
=
\frac{\operatorname{Re}w}{|w|^2},
\]
the boundary line $\operatorname{Re}z=-2$ becomes
\[
\operatorname{Re}w=-2|w|^2.
\]
Completing the square,
\[
|w|^2+\frac12\operatorname{Re}w=0
\quad\Longleftrightarrow\quad
\left|w+\frac14\right|^2=\frac1{16}.
\]
The point $w=1/2$, corresponding to $z=2\in\Omega$, lies outside this small circle. Hence the inequality selects the component
\[
\left|w+\frac14\right|>\frac14.
\]
Inversion is holomorphic with nonzero derivative on $\Omega$, so it is conformal there.

:::

:::

::: {.pf-step #s1-2}

The disk automorphism
\[
\phi(w)
\coloneqq
\frac{w+r}{1+rw}
\]
maps the outer boundary $|w|=1$ to $|\zeta|=1$ and the inner boundary
\[
\left|w+\frac14\right|=\frac14
\]
to $|\zeta|=r$.


::: pf-proof

Since $r\in(0,1)$, $\phi$ is an automorphism of $\DD$, so it maps the unit circle to itself.

On the inner circle, step [](#s1-1){.pf-ref} gives
\[
\operatorname{Re}w=-2|w|^2.
\]
Therefore
\[
\begin{aligned}
|w+r|^2
&=
|w|^2+2r\operatorname{Re}w+r^2\\
&=
(1-4r)|w|^2+r^2.
\end{aligned}
\]
Since $r^2-4r+1=0$,
\[
1-4r=-r^2,
\]
and hence
\[
|w+r|^2
=
r^2(1-|w|^2).
\]
Similarly,
\[
\begin{aligned}
|1+rw|^2
&=
1+2r\operatorname{Re}w+r^2|w|^2\\
&=
1+(r^2-4r)|w|^2\\
&=
1-|w|^2.
\end{aligned}
\]
Thus
\[
|\phi(w)|^2
=
\frac{|w+r|^2}{|1+rw|^2}
=r^2
\]
on the inner boundary.

:::

:::

::: {.pf-step #s1-3}

The map
\[
F
\coloneqq
\phi\circ I
\]
is a conformal map from $\Omega$ onto the annulus
\[
A_r
\coloneqq
\{\zeta\in\CC:r<|\zeta|<1\}.
\]


::: pf-proof

By step [](#s1-1){.pf-ref}, inversion maps $\Omega$ conformally onto the doubly connected region $\Omega'$. By step [](#s1-2){.pf-ref}, $\phi$ is a homeomorphism of the closed unit disk and carries the two boundary components of $\Omega'$ onto the circles $|\zeta|=1$ and $|\zeta|=r$.

The image $\phi(\Omega')$ is connected and lies between those two boundary circles. It contains
\[
\phi(1/2),
\]
whose modulus is strictly greater than $r$. Therefore the image is exactly the annulus $A_r$.

:::

:::

::: {.pf-step #s1-4}

The function
\[
V(\zeta)
\coloneqq
\frac{\log(|\zeta|/r)}
{\log(1/r)}
\]
is harmonic on $A_r$, equals $0$ on $|\zeta|=r$, and equals $1$ on $|\zeta|=1$.


::: pf-proof

The function $\log|\zeta|$ is harmonic away from $0$, hence on $A_r$. The displayed affine rescaling is therefore harmonic. Its boundary values are
\[
V(\zeta)=0
\quad\text{when }|\zeta|=r
\]
and
\[
V(\zeta)=1
\quad\text{when }|\zeta|=1.
\]

:::

:::

::: {.pf-step #s1-5}

One has
\[
u(z)=V(F(z))
\qquad
(z\in\Omega).
\]


::: pf-proof

By steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}, the function $V\circ F$ is bounded and harmonic on $\Omega$, with boundary value $1$ on $|z|=1$ and boundary value $0$ on $\operatorname{Re}z=-2$.

To prove uniqueness, compose the difference
\[
u-V\circ F
\]
with $F^{-1}$. This gives a bounded harmonic function on the bounded annulus $A_r$ that extends continuously with value $0$ on both boundary circles. The maximum principle applied to this function and to its negative gives that it is identically zero. Hence $u=V\circ F$.

:::

:::

::: {.pf-step #s1-6}

The required value is
\[
\boxed{
u(2)
=
\frac{
\log\!\left(
\dfrac{1+2r}{2r+r^2}
\right)
}{
\log(1/r)
},
\qquad
r=2-\sqrt3
}.
\]


::: pf-proof

Since
\[
I(2)=\frac12,
\]
one has
\[
F(2)
=
\phi(1/2)
=
\frac{1/2+r}{1+r/2}
=
\frac{1+2r}{2+r}.
\]
This number is positive, so
\[
\frac{|F(2)|}{r}
=
\frac{1+2r}{r(2+r)}
=
\frac{1+2r}{2r+r^2}.
\]
Substituting into step [](#s1-4){.pf-ref} and using step [](#s1-5){.pf-ref} gives the boxed value.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} determines $u(2)$.

:::

:::

:::
