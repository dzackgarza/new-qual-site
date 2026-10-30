---
schema: qual/card@1
id: P-TIE-S15-21
kind: problem
title: Conformal maps of crescents, lunes, and slit disks
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 21.
---

::: {.problem}
Find a conformal map

1. from $\{z \st \abs{z - 1/2} > 1/2,\ \Re(z) > 0\}$ to $\halfplane$;

2. from $\{z \st \abs{z - 1/2} > 1/2,\ \abs{z} < 1\}$ to $\DD$;

3. from the intersection of the disk $\abs{z + i} < \sqrt{2}$ with $\halfplane$ to $\DD$;

4. from $\DD \setminus [a, 1)$ to $\DD \setminus [0, 1)$ $(0 < a < 1)$. Short solution possible using a Blaschke factor;

5. from $\{z \st \abs{z} < 1,\ \Re(z) > 0\} \setminus (0, 1/2]$ to $\halfplane$.
:::

::: {.solution}

Write
$$
\HH\coloneqq\{w\in\CC:\operatorname{Im}w>0\}.
$$

::: pf

::: {.pf-step #s1-1}

For
$$
D_1
\coloneqq
\{z:\abs{z-\tfrac12}>\tfrac12,\ \operatorname{Re}z>0\},
$$
the map
$$
\boxed{
F_1(z)
\coloneqq
\exp\left(\frac{\pi i}{z}\right)
}
$$
is a conformal bijection $D_1\to\HH$.


::: pf-proof

For $z\ne0$,
$$
\abs{z-\tfrac12}^2>\frac14
$$
is equivalent to
$$
\abs z^2-\operatorname{Re}z>0,
$$
hence to
$$
\operatorname{Re}\frac1z<1.
$$
Also
$$
\operatorname{Re}z>0
$$
is equivalent to
$$
\operatorname{Re}\frac1z>0.
$$
Thus
$$
z\longmapsto w=\frac1z
$$
maps $D_1$ conformally onto the vertical strip
$$
0<\operatorname{Re}w<1.
$$
For such $w$,
$$
\arg e^{\pi i w}
=
\pi\operatorname{Re}w
\in(0,\pi),
$$
so the exponential maps the strip into $\HH$.

It is injective on the strip: if
$$
e^{\pi i w_1}=e^{\pi i w_2},
$$
then $w_1-w_2=2k$ for some $k\in\ZZ$, impossible for two points whose real parts both lie in $(0,1)$ unless $k=0$. It is surjective because every $\zeta\in\HH$ has a logarithm
$$
\log\zeta
=
\log\abs\zeta+i\arg\zeta,
\qquad
0<\arg\zeta<\pi,
$$
and
$$
w
\coloneqq
\frac{\arg\zeta}{\pi}
-
\frac{i}{\pi}\log\abs\zeta
$$
lies in the strip and satisfies $e^{\pi i w}=\zeta$.

:::

:::

::: {.pf-step #s1-2}

For
$$
D_2
\coloneqq
\{z:\abs{z-\tfrac12}>\tfrac12,\ \abs z<1\},
$$
define
$$
W_2(z)
\coloneqq
\exp\left(
\pi i
\left(
\frac{2}{1-z}-1
\right)
\right).
$$
Then
$$
\boxed{
F_2(z)
\coloneqq
\frac{W_2(z)-i}{W_2(z)+i}
}
$$
is a conformal bijection $D_2\to\DD$.


::: pf-proof

Set
$$
u=\frac1{1-z}.
$$
On the unit circle,
$$
\abs z=1
$$
becomes
$$
\abs{u-1}=\abs u,
$$
equivalently
$$
\operatorname{Re}u=\frac12.
$$
On the circle
$$
\abs{z-\tfrac12}=\frac12,
$$
substitution $z=1-1/u$ gives
$$
\abs{u-2}=\abs u,
$$
equivalently
$$
\operatorname{Re}u=1.
$$
A point such as $z=-1/2$ lies in $D_2$ and maps to $u=2/3$, so
$$
\frac12<\operatorname{Re}u<1
$$
on the domain. Hence
$$
v=2u-1
$$
maps $D_2$ conformally onto
$$
0<\operatorname{Re}v<1.
$$
By step [](#s1-1){.pf-ref},
$$
e^{\pi i v}
$$
maps this strip conformally onto $\HH$. Finally,
$$
\zeta\longmapsto\frac{\zeta-i}{\zeta+i}
$$
is a Möbius conformal bijection $\HH\to\DD$. Their composition is $F_2$.

:::

:::

::: {.pf-step #s1-3}

Let
$$
D_3
\coloneqq
\{z:\abs{z+i}<\sqrt2,\ \operatorname{Im}z>0\}.
$$
Set
$$
T(z)
\coloneqq
\frac{z-1}{z+1}.
$$
Then
$$
\boxed{
F_3(z)
\coloneqq
\frac{-T(z)^4-i}{-T(z)^4+i}
}
$$
is a conformal bijection $D_3\to\DD$.


::: pf-proof

The real axis and the circle
$$
\abs{z+i}=\sqrt2
$$
meet at $z=\pm1$. Thus $T$ sends both boundary curves to straight rays through $0$, because it sends the two intersection points $1,-1$ to $0,\infty$.

For $z=0$, which lies on the real boundary segment,
$$
T(0)=-1,
$$
so that boundary ray has argument $\pi$. At the upper point
$$
z=i(\sqrt2-1)
$$
of the circular boundary,
$$
T(z)=e^{3\pi i/4}.
$$
Hence $T$ maps $D_3$ conformally onto the wedge
$$
\frac{3\pi}{4}
<
\arg w
<
\pi.
$$
The map
$$
w\longmapsto -w^4
$$
maps this wedge conformally onto $\HH$: its argument runs from
$$
0
$$
to
$$
\pi.
$$
Finally the Cayley map
$$
\zeta\longmapsto\frac{\zeta-i}{\zeta+i}
$$
maps $\HH$ conformally onto $\DD$. The displayed $F_3$ is the composition.

:::

:::

::: {.pf-step #s1-4}

For $0<a<1$, define
$$
\boxed{
F_4(z)
\coloneqq
\frac{z-a}{1-az}.
}
$$
Then
$$
F_4:
\DD\setminus[a,1)
\longrightarrow
\DD\setminus[0,1)
$$
is a conformal bijection.


::: pf-proof

Since $a\in(0,1)$ is real,
$$
F_4(z)
=
-\psi_a(z),
$$
where
$$
\psi_a(z)
=
\frac{a-z}{1-az}
$$
is a disk automorphism. Thus $F_4$ is also a disk automorphism.

For real $x\in[a,1)$,
$$
F_4(x)
=
\frac{x-a}{1-ax}.
$$
This is real, equals $0$ at $x=a$, tends to $1$ as $x\uparrow1$, and has derivative
$$
\frac{1-a^2}{(1-ax)^2}>0.
$$
Hence it maps the slit $[a,1)$ bijectively onto $[0,1)$. Removing the slit on both sides therefore yields the asserted conformal bijection.

:::

:::

::: {.pf-step #s1-5}

Let
$$
D_5
\coloneqq
\{z:\abs z<1,\ \operatorname{Re}z>0\}
\setminus(0,\tfrac12].
$$
Define
$$
B(w)
\coloneqq
\frac{w-\frac14}{1-\frac14w},
$$
and let
$$
Q(\zeta)
\coloneqq
\sqrt{\zeta}
$$
be the branch on
$$
\DD\setminus(-1,0]
$$
for which
$$
\operatorname{Re}Q(\zeta)>0.
$$
Then
$$
\boxed{
F_5(z)
\coloneqq
\left(
\frac{Q(B(z^2))-i}{Q(B(z^2))+i}
\right)^2
}
$$
is a conformal bijection $D_5\to\HH$.


::: pf-proof

Because
$$
-\frac\pi2
<
\arg z
<
\frac\pi2
$$
on the right half-disk, the squaring map is injective there and maps it conformally onto
$$
\DD\setminus(-1,0].
$$
The removed slit
$$
(0,\tfrac12]
$$
maps to
$$
(0,\tfrac14].
$$
Thus
$$
z\longmapsto z^2
$$
maps $D_5$ conformally onto
$$
\DD\setminus(-1,\tfrac14].
$$

The disk automorphism $B$ fixes the real axis and sends
$$
\frac14\longmapsto0,
\qquad
-1\longmapsto-1.
$$
It is increasing on $(-1,1)$, so it maps
$$
(-1,\tfrac14]
$$
onto
$$
(-1,0].
$$
Hence $B$ sends the preceding slit disk conformally onto
$$
\DD\setminus(-1,0].
$$

On this slit disk, the chosen square root $Q$ is a conformal bijection onto the right half-disk
$$
\{u:\abs u<1,\ \operatorname{Re}u>0\}.
$$
Indeed, squaring maps that half-disk bijectively back to
$$
\DD\setminus(-1,0].
$$

Finally set
$$
M(u)
\coloneqq
\frac{u-i}{u+i}.
$$
The two boundary curves of the right half-disk, the imaginary diameter and the unit semicircle, meet at $\pm i$, which $M$ sends to $0,\infty$. Hence $M$ maps the right half-disk onto a wedge. Since
$$
M(0)=-1,
\qquad
M(1)=-i,
$$
the wedge is
$$
-\pi
<
\arg \zeta
<
-\frac\pi2.
$$
Squaring maps this wedge conformally onto $\HH$. Therefore
$$
u\longmapsto M(u)^2
$$
maps the right half-disk conformally onto $\HH$, and composing the four conformal bijections gives the displayed $F_5$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref} construct and verify a conformal map for each of the five requested domains.

:::

:::

:::
