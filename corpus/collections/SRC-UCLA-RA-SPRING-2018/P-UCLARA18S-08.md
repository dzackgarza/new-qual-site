---
schema: qual/card@1
id: P-UCLARA18S-08
kind: problem
title: Sharp bound on $\abs{\partial_xu(0)}$ for harmonic $u:\DD\to[0,1]$
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 8. Determine the supremum of
$$
\abs{\frac{\partial u}{\partial x}(0,0)}
$$
among all harmonic functions $u:\DD\to[0,1]$, where
$$
\DD=\{z\in\CC:\abs{z}<1\}.
$$
Prove that your answer is correct.
:::

::: {.solution}

::: pf

::: pf-step

It suffices to consider nonconstant $u$.


::: pf-proof

If $u$ is constant, then
$$
u_x(0,0)=0.
$$
Thus constant functions cannot increase the supremum.

:::

:::

::: {.pf-step #s1-2}

If $u:\DD\to[0,1]$ is nonconstant and harmonic, then
$$
0<u(z)<1
\qquad(z\in\DD).
$$


::: pf-proof

If $u$ attained either its minimum $0$ or maximum $1$ at an interior
point, the strong minimum or maximum principle for harmonic functions would
force $u$ to be constant. Hence a nonconstant $u$ takes values in the
open interval $(0,1)$.

:::

:::

::: pf-step

There is a holomorphic function
$$
F=u+iv:\DD\to
S
\coloneqq
\{w\in\CC:0<\operatorname{Re}w<1\}
$$
whose real part is $u$, and $v$ may be chosen so that
$$
F(0)=u(0)\in(0,1).
$$


::: pf-proof

The unit disk is simply connected, so the harmonic function $u$ admits a
harmonic conjugate $v$. Then
$$
F=u+iv
$$
is holomorphic. Adding a real constant to $v$ multiplied by $i$, i.e.
adding a purely imaginary constant to $F$, does not change its real part.
Choose that constant so that
$$
v(0)=0.
$$
Step [](#s1-2){.pf-ref} shows that the image lies in the vertical strip $S$.

:::

:::

::: pf-step

Define
$$
T:S\longrightarrow\DD,
\qquad
T(w)
=
\frac{e^{i\pi w}-i}{e^{i\pi w}+i}.
$$
Then $T$ is a conformal bijection.


::: pf-proof

If $0<\operatorname{Re}w<1$, then
$$
e^{i\pi w}
$$
has argument strictly between $0$ and $\pi$, hence lies in the upper
half-plane. The Cayley map
$$
\zeta\longmapsto\frac{\zeta-i}{\zeta+i}
$$
is a conformal bijection from the upper half-plane to $\DD$.
Their composition is $T$.

:::

:::

::: {.pf-step #s1-5}

Let
$$
t=F(0)=u(0)\in(0,1),
\qquad
\alpha=T(t).
$$
Then Schwarz--Pick gives
$$
\boxed{
\abs{F'(0)}
\le
\frac{1-\abs{\alpha}^2}{\abs{T'(t)}}}.
$$


::: pf-proof

Let
$$
\psi_\alpha(\zeta)
=
\frac{\zeta-\alpha}{1-\overline\alpha\,\zeta},
$$
the disk automorphism sending $\alpha$ to $0$. Then
$$
G
=
\psi_\alpha\circ T\circ F
:
\DD\to\DD
$$
is holomorphic and
$$
G(0)=0.
$$
Schwarz's lemma gives
$$
\abs{G'(0)}\le1.
$$
By the chain rule,
$$
\abs{G'(0)}
=
\abs{\psi_\alpha'(\alpha)}
\abs{T'(t)}
\abs{F'(0)}.
$$
Since
$$
\abs{\psi_\alpha'(\alpha)}
=
\frac1{1-\abs{\alpha}^2},
$$
the displayed estimate follows.

:::

:::

::: {.pf-step #s1-6}

For $t\in(0,1)$,
$$
\boxed{
\frac{1-\abs{T(t)}^2}{\abs{T'(t)}}
=
\frac{2\sin(\pi t)}{\pi}
\le
\frac2\pi}.
$$


::: pf-proof

Set
$$
\zeta=e^{i\pi t},
$$
so $\abs{\zeta}=1$ and
$$
\operatorname{Im}\zeta=\sin(\pi t)>0.
$$
From
$$
T(t)
=
\frac{\zeta-i}{\zeta+i},
$$
one gets
$$
1-\abs{T(t)}^2
=
\frac{\abs{\zeta+i}^2-\abs{\zeta-i}^2}{\abs{\zeta+i}^2}
=
\frac{4\sin(\pi t)}{\abs{\zeta+i}^2}.
$$
Also
$$
\frac{d}{d\zeta}
\frac{\zeta-i}{\zeta+i}
=
\frac{2i}{(\zeta+i)^2},
$$
so
$$
\abs{T'(t)}
=
\frac{2\pi}{\abs{\zeta+i}^2}.
$$
Dividing gives
$$
\frac{1-\abs{T(t)}^2}{\abs{T'(t)}}
=
\frac{2\sin(\pi t)}{\pi}
\le
\frac2\pi.
$$

:::

:::

::: {.pf-step #s1-7}

Every admissible harmonic function satisfies
$$
\boxed{
\abs{u_x(0,0)}
\le
\frac2\pi}.
$$


::: pf-proof

By the Cauchy--Riemann equations,
$$
F'(0)
=
u_x(0,0)-iu_y(0,0),
$$
so
$$
\abs{u_x(0,0)}
\le
\abs{F'(0)}.
$$
Combine steps [](#s1-5){.pf-ref} and [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Let $H=T^{-1}:\DD\to S$ be the inverse conformal map,
$$
H(z)
=
\frac1{i\pi}
\Log\!\left(
i\frac{1+z}{1-z}
\right),
$$
where $\Log$ is the holomorphic logarithm on the upper half-plane. Then
$$
H(0)=\frac12
\qquad\text{and}\qquad
H'(0)=-\frac{2i}{\pi}.
$$


::: pf-proof

Solving
$$
z
=
\frac{\zeta-i}{\zeta+i}
$$
for $\zeta$ gives
$$
\zeta
=
i\frac{1+z}{1-z}.
$$
Since $\zeta=e^{i\pi w}$,
$$
w
=
\frac1{i\pi}\Log\zeta,
$$
which is the displayed formula.

At $z=0$,
$$
\Log i
=
\frac{i\pi}{2},
$$
so $H(0)=1/2$. Differentiating,
$$
H'(z)
=
\frac1{i\pi}
\left(
\frac1{1+z}
+
\frac1{1-z}
\right),
$$
hence
$$
H'(0)
=
\frac2{i\pi}
=
-\frac{2i}{\pi}.
$$

:::

:::

::: {.pf-step #s1-9}

Define
$$
\widetilde H(z)=H(iz)
$$
and
$$
u_*(z)=\operatorname{Re}\widetilde H(z).
$$
Then $u_*:\DD\to(0,1)$ is harmonic and
$$
\boxed{
\frac{\partial u_*}{\partial x}(0,0)
=
\frac2\pi}.
$$


::: pf-proof

Since multiplication by $i$ is an automorphism of $\DD$,
$$
\widetilde H:\DD\to S
$$
is holomorphic, so its real part $u_*$ is harmonic and takes values in
$(0,1)$.

By step [](#s1-8){.pf-ref},
$$
\widetilde H'(0)
=
iH'(0)
=
i\left(-\frac{2i}{\pi}\right)
=
\frac2\pi.
$$
For a holomorphic function, the real part of the derivative is the
$x$-derivative of its real part. Therefore
$$
(u_*)_x(0,0)
=
\operatorname{Re}\widetilde H'(0)
=
\frac2\pi.
$$

:::

:::

::: {.pf-step #s1-10}

Hence the supremum is
$$
\boxed{\frac2\pi}.
$$


::: pf-proof

Step [](#s1-7){.pf-ref} gives $2/\pi$ as an upper bound, while step [](#s1-9){.pf-ref} constructs an
admissible harmonic function attaining that value.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required sharp result.

:::

:::

:::
