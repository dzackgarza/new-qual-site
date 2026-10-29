---
schema: qual/card@1
id: P-ZUQU7
kind: problem
title: Injective conformal maps of $\{\operatorname{Re} z>0,\ |z-1|>1\}$ onto the
  disc
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Biholomorphisms
  - Fractional Linear Transformations
  - Blaschke Factors
relations: []
review: draft
---

::: {.problem}
Define
$$  
G \definedas \theset{z\in \CC\suchthat \Re(z) > 0, \, \abs{z-1} > 1}
.$$

Find all injective conformal maps of $G$ onto $\DD$.
These may be expressed as compositions of maps, but explain why this list is complete.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The inversion
$$
T(z)=\frac1z
$$
maps $G$ biholomorphically onto the strip
$$
S=\left\{w:0<\Re w<\frac12\right\}.
$$


::: pf-proof

Because $\Re z>0$, the point $z=0$ does not lie in $G$, so $T$ is
holomorphic there. Also
$$
\Re\frac1z=\frac{\Re z}{|z|^2}>0.
$$
The second defining inequality for $G$ is
$$
|z-1|>1
\iff
|z|^2-2\Re z>0
\iff
\frac{\Re z}{|z|^2}<\frac12
\iff
\Re\frac1z<\frac12.
$$
Thus $T(G)=S$. Since inversion is its own inverse, it is a
biholomorphism between these domains.

:::

:::

::: {.pf-step #s1-2}

The exponential map
$$
E(w)=e^{2\pi i w}
$$
maps $S$ biholomorphically onto the upper half-plane $\HH$.


::: pf-proof

Write $w=x+iy$. Then
$$
E(w)=e^{-2\pi y}e^{2\pi i x}.
$$
For $0<x<1/2$, its argument lies in $(0,\pi)$, so $E(S)\subseteq\HH$.
Conversely, every $\zeta\in\HH$ has a unique polar representation
$$
\zeta=\rho e^{i\theta},
\qquad
\rho>0,
\quad
0<\theta<\pi.
$$
Taking
$$
w=\frac{\theta}{2\pi}-\frac{i}{2\pi}\log\rho
$$
gives $w\in S$ and $E(w)=\zeta$, proving surjectivity.

If $E(w_1)=E(w_2)$, then $w_1-w_2\in\ZZ$. But both real parts lie in
$(0,1/2)$, so their difference has real part in $(-1/2,1/2)$; the only
possible integer is $0$. Thus $w_1=w_2$. Since
$E'(w)=2\pi iE(w)\ne0$, the map is biholomorphic.

:::

:::

::: {.pf-step #s1-3}

The Cayley map
$$
C(\zeta)=\frac{\zeta-i}{\zeta+i}
$$
maps $\HH$ biholomorphically onto $\DD$.


::: pf-proof

This is the standard Cayley transform. Directly, if $\Im\zeta>0$, then
$$
|\zeta-i|^2
=|\zeta|^2+1-2\Im\zeta
<|\zeta|^2+1+2\Im\zeta
=|\zeta+i|^2,
$$
so $|C(\zeta)|<1$. Its inverse is
$$
C^{-1}(w)=i\frac{1+w}{1-w},
$$
which maps $\DD$ into $\HH$ and is holomorphic there.

:::

:::

::: {.pf-step #s1-4}

Hence
$$
\Phi(z)
=C(E(T(z)))
=\frac{e^{2\pi i/z}-i}{e^{2\pi i/z}+i}
$$
is a biholomorphism $G\to\DD$.


::: pf-proof

This is the composition of the three biholomorphisms in steps
[](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Every biholomorphism $F:G\to\DD$ has the form
$$
\boxed{
F=A_{a,\theta}\circ\Phi,
\qquad
A_{a,\theta}(w)
=e^{i\theta}\frac{w-a}{1-\bar a w}}
$$
for some $a\in\DD$ and $\theta\in\RR$.


::: pf-proof

Let $F:G\to\DD$ be any biholomorphism. Since $\Phi$ is a
biholomorphism by step [](#s1-4){.pf-ref},
$$
A=F\circ\Phi^{-1}
$$
is an automorphism of the unit disk. Every automorphism of $\DD$ has the
form
$$
A_{a,\theta}(w)
=e^{i\theta}\frac{w-a}{1-\bar a w},
$$
with $a\in\DD$ and $\theta\in\RR$. Hence
$F=A_{a,\theta}\circ\Phi$.

Conversely, each $A_{a,\theta}$ is a disk automorphism, so every displayed
composition is again a biholomorphism from $G$ onto $\DD$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the complete list of injective conformal maps of $G$ onto
$\DD$ and proves its completeness.

:::

:::

:::
