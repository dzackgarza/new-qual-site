---
schema: qual/card@1
id: P-TRIV-CA28
kind: problem
title: Large-$x$ asymptotics of the Hankel function $H^{(1)}_\nu$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 28, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
\*The Henkel function of the first kind has the following integral representation: $H _ { \nu } ^ { ( 1 ) } ( x ) = \frac { 1 } { \pi i } \int _ { 0 + i \epsilon } ^ { - \infty + i \epsilon } \exp \left[ \frac { x } { 2 } \left( z - \frac { 1 } { z } \right) \right] \frac { \mathrm { d } z } { z ^ { \nu + 1 } }$ . The i factor is present since we have a branch cut along the negative real axis.
Find the asymptotic behavior as $x \gg 1$
:::

::: {.solution}

Write
$$
\Phi(z)
=
\frac12
\left(
z-\frac1z
\right).
$$

::: pf

::: pf-step

The saddle points of $\Phi$ are
$$
z=\pm i.
$$


::: pf-proof

One has
$$
\Phi'(z)
=
\frac12
\left(
1+\frac1{z^2}
\right).
$$
Thus
$$
\Phi'(z)=0
\iff
z^2=-1.
$$

:::

:::

::: pf-step

For the contour defining $H_\nu^{(1)}$, the relevant saddle is
$$
z_0=i.
$$


::: pf-proof

The contour lies above the negative-real-axis branch cut and may be deformed
through the upper half-plane without crossing the cut. Hence it passes through
the upper saddle $i$ rather than the lower saddle $-i$.

:::

:::

::: {.pf-step #s1-3}

At the saddle,
$$
\Phi(i)=i
$$
and
$$
\Phi''(i)=-i.
$$


::: pf-proof

Directly,
$$
\Phi(i)
=
\frac12(i+i)
=i.
$$
Also
$$
\Phi''(z)=-z^{-3}.
$$
Since
$$
i^{-3}=i,
$$
one obtains
$$
\Phi''(i)=-i.
$$

:::

:::

::: {.pf-step #s1-4}

A local steepest-descent coordinate at $i$ is
$$
z
=
i
+
e^{-i\pi/4}
\frac{u}{\sqrt x}.
$$


::: pf-proof

With
$$
\delta
=
e^{-i\pi/4}
\frac{u}{\sqrt x},
$$
one has
$$
\delta^2
=
-i\frac{u^2}{x}.
$$
Hence the quadratic saddle term is
$$
x\frac{\Phi''(i)}2\delta^2
=
x\frac{-i}{2}
\left(
-i\frac{u^2}{x}
\right)
=
-\frac{u^2}{2},
$$
which is real and negative.

:::

:::

::: {.pf-step #s1-5}

Along this local coordinate,
$$
x\Phi(z)
=
ix
-
\frac{u^2}{2}
+
O\left(
\frac{\abs{u}^3}{\sqrt x}
\right).
$$


::: pf-proof

Taylor-expand $\Phi$ at $i$:
$$
\Phi(i+\delta)
=
\Phi(i)
+
\frac{\Phi''(i)}2\delta^2
+
O(\delta^3).
$$
Use steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} and multiply by $x$.

:::

:::

::: {.pf-step #s1-6}

The amplitude satisfies
$$
z^{-\nu-1}
=
i^{-\nu-1}
\left(
1+O(x^{-1/2}\abs{u})
\right)
$$
near the saddle, with
$$
i^{-\nu-1}
=
e^{-i\pi(\nu+1)/2}.
$$


::: pf-proof

The chosen branch is analytic near $z=i$. Hence $z^{-\nu-1}$ has a Taylor
expansion there. Since the branch argument of $i$ is $\pi/2$,
$$
i^{-\nu-1}
=
e^{-(\nu+1)i\pi/2}.
$$

:::

:::

::: {.pf-step #s1-7}

With the contour orientation inherited from the original integral, the
local steepest-descent parameter $u$ runs from $+\infty$ to $-\infty$.


::: pf-proof

The direction
$$
e^{-i\pi/4}
$$
points from the saddle toward the lower-right. The original contour runs from
the endpoint near $0$ toward the negative real direction. After deformation
through $i$, it therefore approaches the saddle along the lower-right branch
and leaves along the opposite upper-left branch.

Thus in the parametrization
$$
z
=
i
+
e^{-i\pi/4}
\frac{u}{\sqrt x},
$$
the incoming part has $u>0$ and the outgoing part has $u<0$. Hence the
oriented local integral runs from $+\infty$ to $-\infty$.

:::

:::

::: {.pf-step #s1-8}

The leading saddle contribution is
$$
H_\nu^{(1)}(x)
\sim
\frac{e^{ix}}{\pi i}
i^{-\nu-1}
\left(
-e^{-i\pi/4}
\right)
\sqrt{\frac{2\pi}{x}}.
$$


::: pf-proof

By steps [](#s1-5){.pf-ref} through [](#s1-7){.pf-ref},
$$
\begin{aligned}
H_\nu^{(1)}(x)
&\sim
\frac1{\pi i}
e^{ix}
i^{-\nu-1}
\frac{e^{-i\pi/4}}{\sqrt x}
\int_{+\infty}^{-\infty}
e^{-u^2/2}\,du\\
&=
\frac{e^{ix}}{\pi i}
i^{-\nu-1}
\left(
-e^{-i\pi/4}
\right)
\frac1{\sqrt x}
\int_{-\infty}^{\infty}
e^{-u^2/2}\,du.
\end{aligned}
$$
The Gaussian integral equals $\sqrt{2\pi}$.

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\boxed{
H_\nu^{(1)}(x)
\sim
\sqrt{\frac{2}{\pi x}}
\exp\left[
i\left(
x
-
\frac{\pi\nu}{2}
-
\frac\pi4
\right)
\right]
}
$$
as $x\to+\infty$.


::: pf-proof

Use
$$
i^{-\nu-1}
=
e^{-i\pi(\nu+1)/2}
$$
in step [](#s1-8){.pf-ref}. Also
$$
-\frac1i=i.
$$
Hence the phase factor is
$$
i
e^{-i\pi(\nu+1)/2}
e^{-i\pi/4}
=
e^{-i\pi\nu/2-i\pi/4}.
$$
The absolute prefactor simplifies as
$$
\frac{\sqrt{2\pi}}{\pi\sqrt x}
=
\sqrt{\frac{2}{\pi x}}.
$$

:::

:::

::: {.pf-step #s1-10}

More generally, the full large-$x$ expansion has the form
$$
H_\nu^{(1)}(x)
\sim
\sqrt{\frac{2}{\pi x}}
e^{i(x-\pi\nu/2-\pi/4)}
\sum_{k=0}^{\infty}
\frac{i^k}{k!(8x)^k}
\prod_{j=1}^{k}
\left(
4\nu^2-(2j-1)^2
\right).
$$


::: pf-proof

The saddle expansion produces an asymptotic series in integer powers of
$x^{-1}$. Write
$$
H_\nu^{(1)}(x)
\sim
e^{ix}x^{-1/2}
\sum_{k=0}^{\infty}a_kx^{-k}.
$$
The Hankel function satisfies Bessel's equation
$$
x^2y''
+
xy'
+
(x^2-\nu^2)y
=
0.
$$
Substitution of the ansatz gives
$$
A''+2iA'
+
\frac{1/4-\nu^2}{x^2}A
=
0,
$$
where
$$
A(x)=\sum_{k\ge0}a_kx^{-k}.
$$
Equating coefficients of $x^{-k-2}$ yields
$$
a_{k+1}
=
i
\frac{
4\nu^2-(2k+1)^2
}{
8(k+1)
}
a_k.
$$
Step [](#s1-9){.pf-ref} fixes
$$
a_0
=
\sqrt{\frac2\pi}
e^{-i\pi\nu/2-i\pi/4}.
$$
Iterating the recurrence gives the displayed series.

:::

:::

::: pf-step

In particular,
$$
H_\nu^{(1)}(x)
\sim
\sqrt{\frac{2}{\pi x}}
e^{i(x-\pi\nu/2-\pi/4)}
\left[
1
+
i\frac{4\nu^2-1}{8x}
-
\frac{
(4\nu^2-1)(4\nu^2-9)
}{
2!(8x)^2
}
+
\cdots
\right].
$$


::: pf-proof

Expand the first terms of the series in step [](#s1-10){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} gives the leading asymptotic behavior, and step [](#s1-10){.pf-ref} gives the full
asymptotic expansion.

:::

:::

:::
