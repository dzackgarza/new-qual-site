---
schema: qual/card@1
id: P-UCLARA11S-10
kind: problem
title: Extremal derivative for a holomorphic map from a half-disk to the disk
classification: {areas: [real-analysis], topics: []}
relations: []
review: draft
---

::: {.problem}
Let $\DD=\{z:|z|<1\}$ and
\[
\Omega=\{z\in\DD:\operatorname{Im}z>0\}.
\]
Evaluate
\[
\sup\left\{\operatorname{Re}f'(i/2): f:\Omega\to\DD\text{ is holomorphic}\right\}.
\]
:::

::: {.solution}

Set
\[
z_0=\frac i2.
\]

::: pf

::: {.pf-step #s1-1}

The Möbius transformation
\[
M(z)
\coloneqq
\frac{1+z}{1-z}
\]
maps $\Omega$ biholomorphically onto the first quadrant
\[
Q
\coloneqq
\{w:\operatorname{Re}w>0,\ \operatorname{Im}w>0\}.
\]


::: pf-proof

The standard Cayley transform $M$ maps the unit disk biholomorphically onto the right half-plane, so
\[
|z|<1
\quad\Longrightarrow\quad
\operatorname{Re}M(z)>0.
\]
Because $M$ has real coefficients and positive determinant,
\[
\operatorname{Im}M(z)
=
\frac{2\operatorname{Im}z}{|1-z|^2}.
\]
Thus
\[
\operatorname{Im}z>0
\quad\Longrightarrow\quad
\operatorname{Im}M(z)>0.
\]
Hence $M(\Omega)\subset Q$.

Conversely, $M^{-1}$ maps the right half-plane to $\DD$ and the upper half-plane to itself, so every point of $Q$ has preimage in $\Omega$.

:::

:::

::: {.pf-step #s1-2}

The map
\[
S(w)=w^2
\]
maps $Q$ biholomorphically onto the upper half-plane
\[
\halfplane
\coloneqq
\{\zeta:\operatorname{Im}\zeta>0\}.
\]


::: pf-proof

Every $w\in Q$ has argument in $(0,\pi/2)$, so $w^2$ has argument in $(0,\pi)$ and therefore lies in $\halfplane$.

Conversely, every $\zeta\in\halfplane$ has a unique square root with argument in $(0,\pi/2)$, so $S:Q\to\halfplane$ is bijective. Its derivative
\[
S'(w)=2w
\]
never vanishes on $Q$, so the inverse is holomorphic.

:::

:::

::: pf-step

Therefore
\[
\Phi(z)
\coloneqq
\left(
\frac{1+z}{1-z}
\right)^2
\]
is a biholomorphism
\[
\Phi:\Omega\to\halfplane.
\]


::: pf-proof

Combine steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

At
\[
z_0=\frac i2,
\]
one has
\[
M(z_0)
=
\frac35+\frac45i
\]
and
\[
q_0
\coloneqq
\Phi(z_0)
=
-\frac7{25}+\frac{24}{25}i.
\]


::: pf-proof

Compute
\[
M(i/2)
=
\frac{1+i/2}{1-i/2}
=
\frac{(1+i/2)^2}{1+1/4}
=
\frac{3/4+i}{5/4}
=
\frac35+\frac45i.
\]
Squaring gives
\[
q_0
=
\left(\frac35+\frac45i\right)^2
=
-\frac7{25}+\frac{24}{25}i.
\]

:::

:::

::: {.pf-step #s1-5}

The derivative of $\Phi$ at $z_0$ satisfies
\[
|\Phi'(z_0)|
=
\frac{16}{5}.
\]


::: pf-proof

Since
\[
M'(z)
=
\frac{2}{(1-z)^2},
\]
one has
\[
\Phi'(z)
=
2M(z)M'(z)
=
\frac{4M(z)}{(1-z)^2}.
\]
At $z_0=i/2$,
\[
|M(z_0)|=1
\]
and
\[
|1-z_0|^2
=
1+\frac14
=
\frac54.
\]
Therefore
\[
|\Phi'(z_0)|
=
\frac4{|1-z_0|^2}
=
\frac4{5/4}
=
\frac{16}{5}.
\]

:::

:::

::: {.pf-step #s1-6}

Let
\[
G:\halfplane\to\DD
\]
be holomorphic. Then
\[
|G'(q_0)|
\le
\frac{1-|G(q_0)|^2}{2\operatorname{Im}q_0}
\le
\frac1{2\operatorname{Im}q_0}.
\]


::: pf-proof

Set
\[
a=G(q_0).
\]
Let
\[
\psi_a(\zeta)
\coloneqq
\frac{\zeta-a}{1-\overline a\zeta},
\]
the disk automorphism sending $a$ to $0$, and let
\[
\chi(w)
\coloneqq
\frac{w-q_0}{w-\overline{q_0}},
\]
the upper-half-plane automorphism onto the disk sending $q_0$ to $0$.

Then
\[
H
\coloneqq
\psi_a\circ G\circ\chi^{-1}
\]
maps $\DD$ holomorphically to itself and satisfies $H(0)=0$. Schwarz's lemma gives
\[
|H'(0)|\le1.
\]
Now
\[
|\psi_a'(a)|
=
\frac1{1-|a|^2},
\]
while
\[
|\chi'(q_0)|
=
\frac1{2\operatorname{Im}q_0},
\]
so
\[
|(\chi^{-1})'(0)|
=
2\operatorname{Im}q_0.
\]
The chain rule therefore gives
\[
\frac{|G'(q_0)|}{1-|a|^2}
\cdot
2\operatorname{Im}q_0
\le1,
\]
which is the first inequality. The second follows from $1-|a|^2\le1$.

:::

:::

::: {.pf-step #s1-7}

If
\[
f:\Omega\to\DD
\]
is holomorphic, then
\[
|f'(z_0)|
\le
\frac53.
\]


::: pf-proof

Define
\[
G
\coloneqq
f\circ\Phi^{-1}:\halfplane\to\DD.
\]
Then
\[
f=G\circ\Phi,
\]
so
\[
|f'(z_0)|
=
|G'(q_0)|\,|\Phi'(z_0)|.
\]
By step [](#s1-6){.pf-ref},
\[
|G'(q_0)|
\le
\frac1{2\operatorname{Im}q_0}.
\]
Using steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref},
\[
\operatorname{Im}q_0
=
\frac{24}{25},
\qquad
|\Phi'(z_0)|
=
\frac{16}{5}.
\]
Therefore
\[
|f'(z_0)|
\le
\frac{16/5}{2(24/25)}
=
\frac53.
\]

:::

:::

::: {.pf-step #s1-8}

Hence
\[
\operatorname{Re}f'(z_0)
\le
\frac53
\]
for every admissible $f$.


::: pf-proof

For every complex number $w$,
\[
\operatorname{Re}w\le|w|.
\]
Apply step [](#s1-7){.pf-ref} to $w=f'(z_0)$.

:::

:::

::: {.pf-step #s1-9}

The bound $5/3$ is attained.


::: pf-proof

Use the map
\[
\chi(w)
=
\frac{w-q_0}{w-\overline{q_0}}
\]
from step [](#s1-6){.pf-ref} and define
\[
f_0
=
e^{i\theta}\chi\circ\Phi,
\]
where $\theta\in\RR$ is chosen so that
\[
f_0'(z_0)
\]
is positive real.

The function $f_0$ maps $\Omega$ holomorphically into $\DD$. Since
\[
|\chi'(q_0)|
=
\frac1{2\operatorname{Im}q_0},
\]
steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} give
\[
|f_0'(z_0)|
=
\frac{|\Phi'(z_0)|}{2\operatorname{Im}q_0}
=
\frac53.
\]
The phase $e^{i\theta}$ makes this derivative equal to the positive real number $5/3$.

:::

:::

::: {.pf-step #s1-10}

Therefore
\[
\boxed{
\sup\left\{
\operatorname{Re}f'(i/2):
f:\Omega\to\DD
\text{ holomorphic}
\right\}
=
\frac53.
}
\]


::: pf-proof

Step [](#s1-8){.pf-ref} gives the upper bound and step [](#s1-9){.pf-ref} attains it.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required value.

:::

:::

:::
