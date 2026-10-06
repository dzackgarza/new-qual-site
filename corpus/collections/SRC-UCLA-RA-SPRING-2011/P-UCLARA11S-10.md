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
Let $\mathbb D=\{z:|z|<1\}$ and
\[
\Omega=\{z\in\mathbb D:\operatorname{Im}z>0\}.
\]
Evaluate
\[
\sup\left\{\operatorname{Re}f'(i/2): f:\Omega\to\mathbb D\text{ is holomorphic}\right\}.
\]
:::

::: {.solution}
Set
\[
z_0=\frac i2.
\]

<1>1. The Möbius transformation
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

::: {.proof}
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

Conversely, $M^{-1}$ maps the right half-plane to $\mathbb D$ and the upper half-plane to itself, so every point of $Q$ has preimage in $\Omega$.
:::

<1>2. The map
\[
S(w)=w^2
\]
maps $Q$ biholomorphically onto the upper half-plane
\[
\mathbb H
\coloneqq
\{\zeta:\operatorname{Im}\zeta>0\}.
\]

::: {.proof}
Every $w\in Q$ has argument in $(0,\pi/2)$, so $w^2$ has argument in $(0,\pi)$ and therefore lies in $\mathbb H$.

Conversely, every $\zeta\in\mathbb H$ has a unique square root with argument in $(0,\pi/2)$, so $S:Q\to\mathbb H$ is bijective. Its derivative
\[
S'(w)=2w
\]
never vanishes on $Q$, so the inverse is holomorphic.
:::

<1>3. Therefore
\[
\Phi(z)
\coloneqq
\left(
\frac{1+z}{1-z}
\right)^2
\]
is a biholomorphism
\[
\Phi:\Omega\to\mathbb H.
\]

::: {.proof}
Combine steps <1>1 and <1>2.
:::

<1>4. At
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

::: {.proof}
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

<1>5. The derivative of $\Phi$ at $z_0$ satisfies
\[
|\Phi'(z_0)|
=
\frac{16}{5}.
\]

::: {.proof}
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

<1>6. Let
\[
G:\mathbb H\to\mathbb D
\]
be holomorphic. Then
\[
|G'(q_0)|
\le
\frac{1-|G(q_0)|^2}{2\operatorname{Im}q_0}
\le
\frac1{2\operatorname{Im}q_0}.
\]

::: {.proof}
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
maps $\mathbb D$ holomorphically to itself and satisfies $H(0)=0$. Schwarz's lemma gives
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

<1>7. If
\[
f:\Omega\to\mathbb D
\]
is holomorphic, then
\[
|f'(z_0)|
\le
\frac53.
\]

::: {.proof}
Define
\[
G
\coloneqq
f\circ\Phi^{-1}:\mathbb H\to\mathbb D.
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
By step <1>6,
\[
|G'(q_0)|
\le
\frac1{2\operatorname{Im}q_0}.
\]
Using steps <1>4 and <1>5,
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

<1>8. Hence
\[
\operatorname{Re}f'(z_0)
\le
\frac53
\]
for every admissible $f$.

::: {.proof}
For every complex number $w$,
\[
\operatorname{Re}w\le|w|.
\]
Apply step <1>7 to $w=f'(z_0)$.
:::

<1>9. The bound $5/3$ is attained.

::: {.proof}
Use the map
\[
\chi(w)
=
\frac{w-q_0}{w-\overline{q_0}}
\]
from step <1>6 and define
\[
f_0
=
e^{i\theta}\chi\circ\Phi,
\]
where $\theta\in\mathbb R$ is chosen so that
\[
f_0'(z_0)
\]
is positive real.

The function $f_0$ maps $\Omega$ holomorphically into $\mathbb D$. Since
\[
|\chi'(q_0)|
=
\frac1{2\operatorname{Im}q_0},
\]
steps <1>4--<1>5 give
\[
|f_0'(z_0)|
=
\frac{|\Phi'(z_0)|}{2\operatorname{Im}q_0}
=
\frac53.
\]
The phase $e^{i\theta}$ makes this derivative equal to the positive real number $5/3$.
:::

<1>10. Therefore
\[
\boxed{
\sup\left\{
\operatorname{Re}f'(i/2):
f:\Omega\to\mathbb D
\text{ holomorphic}
\right\}
=
\frac53.
}
\]

::: {.proof}
Step <1>8 gives the upper bound and step <1>9 attains it.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>10 is the required value.
:::
:::
