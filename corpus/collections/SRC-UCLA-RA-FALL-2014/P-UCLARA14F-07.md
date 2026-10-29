---
schema: qual/card@1
id: P-UCLARA14F-07
kind: problem
title: Conformal map from a slit upper half-plane to the disk
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
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2014 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 7 on page 1 of the official analysis-14F.pdf exam, checked against the Fall 2014 section of UCLA_Solutions.pdf.
---

::: {.problem}
Find an explicit conformal mapping from the upper half-plane slit along the vertical segment,
\[
\{ z \in \CC ; \operatorname{Im} z > 0 \} \setminus (0, 0 + ih], \quad h > 0,
\]
to the unit disc $\{ z \in \CC ; |z| < 1 \}$.
:::

::: {.solution}

Let
\[
\Omega
=
\{z\in\CC:\operatorname{Im}z>0\}
\setminus
\{it:0<t\le h\}.
\]

::: pf

::: {.pf-step #s1-1}

The map
\[
T_1(z)=\frac{ih}{z}
\]
is a conformal bijection from $\Omega$ onto
\[
\Omega_1
=
\{w\in\CC:\operatorname{Re}w>0\}
\setminus[1,\infty).
\]


::: pf-proof

Write $z=x+iy$ with $y>0$. Then
\[
\frac{ih}{z}
=
\frac{hy}{|z|^2}
+
i\frac{hx}{|z|^2},
\]
so
\[
\operatorname{Re}T_1(z)>0.
\]
If $z=it$ with $0<t\le h$, then
\[
T_1(z)=\frac ht\in[1,\infty),
\]
and conversely every point of $[1,\infty)$ has inverse
\[
z=\frac{ih}{w}=i\frac hw
\]
on the removed segment.

The inverse map
\[
w\longmapsto\frac{ih}{w}
\]
sends the right half-plane to the upper half-plane and avoids the slit
precisely when $w\notin[1,\infty)$. Thus $T_1$ is bijective. It is Möbius
and has nonzero derivative on $\Omega$, hence is conformal.

:::

:::

::: {.pf-step #s1-2}

The squaring map
\[
T_2(w)=w^2
\]
is a conformal bijection from $\Omega_1$ onto
\[
\Omega_2
=
\CC
\setminus
\bigl((-\infty,0]\cup[1,\infty)\bigr).
\]


::: pf-proof

On the right half-plane,
\[
-\frac{\pi}{2}<\arg w<\frac{\pi}{2},
\]
so
\[
-\pi<\arg(w^2)<\pi.
\]
Hence squaring maps the right half-plane bijectively onto
\[
\CC\setminus(-\infty,0].
\]
It is injective there because $w$ and $-w$ cannot both lie in the right
half-plane. The removed ray $[1,\infty)$ is carried exactly to
$[1,\infty)$. Since $T_2'(w)=2w\ne0$ on the right half-plane, the map is
conformal.

:::

:::

::: pf-step

The Möbius map
\[
T_3(\zeta)=\frac1\zeta-1
\]
is a conformal bijection from $\Omega_2$ onto
\[
\Omega_3
=
\CC\setminus(-\infty,0].
\]


::: pf-proof

The inverse is
\[
T_3^{-1}(u)=\frac1{u+1}.
\]
For real $\zeta<0$,
\[
\frac1\zeta-1<-1,
\]
while for real $\zeta\ge1$,
\[
-1\le\frac1\zeta-1\le0.
\]
Thus the two removed real rays in $\Omega_2$ map onto the removed negative
real ray in $\Omega_3$. Conversely, if $u\in(-\infty,0]$, then
$1/(u+1)$ lies on one of those two real rays, with $u=-1$ corresponding to
the point at infinity. Hence the inverse maps $\Omega_3$ precisely onto
$\Omega_2$. The derivative
\[
-\frac1{\zeta^2}
\]
never vanishes on $\Omega_2$.

:::

:::

::: pf-step

Let
\[
T_4(u)=\sqrt{u}
\]
be the principal square root on
\[
\CC\setminus(-\infty,0].
\]
Then $T_4$ is a conformal bijection onto the right half-plane
\[
H_R=\{s\in\CC:\operatorname{Re}s>0\}.
\]


::: pf-proof

On the slit plane choose
\[
-\pi<\arg u<\pi.
\]
Then
\[
T_4(u)
=
\sqrt{|u|}\,e^{i\arg(u)/2}
\]
has argument in
\[
\left(-\frac{\pi}{2},\frac{\pi}{2}\right),
\]
so its real part is positive. Conversely, squaring is a conformal bijection
from $H_R$ onto the slit plane, as in step [](#s1-2){.pf-ref}. Thus the principal square
root is its conformal inverse.

:::

:::

::: {.pf-step #s1-5}

The Cayley map
\[
T_5(s)=\frac{s-1}{s+1}
\]
is a conformal bijection from $H_R$ onto the unit disk $\mathbb D$.


::: pf-proof

For $\operatorname{Re}s>0$,
\[
|s-1|^2
=
|s|^2-2\operatorname{Re}s+1
<
|s|^2+2\operatorname{Re}s+1
=
|s+1|^2.
\]
Hence
\[
\left|\frac{s-1}{s+1}\right|<1.
\]
The inverse is
\[
\xi\longmapsto\frac{1+\xi}{1-\xi},
\]
which maps $\mathbb D$ to $H_R$. Thus $T_5$ is a conformal bijection.

:::

:::

::: {.pf-step #s1-6}

The composite
\[
F
=
T_5\circ T_4\circ T_3\circ T_2\circ T_1
\]
is therefore a conformal bijection
\[
\Omega\xrightarrow{\sim}\mathbb D.
\]


::: pf-proof

Each map in steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref} is a conformal bijection onto the next
domain. Their composition is therefore a conformal bijection from the
original slit upper half-plane to the unit disk.

:::

:::

::: {.pf-step #s1-7}

Explicitly,
\[
\boxed{
F(z)
=
\frac{
\sqrt{-1-z^2/h^2}-1
}{
\sqrt{-1-z^2/h^2}+1
}},
\]
where the square root is the principal branch after the preceding maps place
its argument in $\CC\setminus(-\infty,0]$.


::: pf-proof

The first three maps give
\[
T_3(T_2(T_1(z)))
=
\frac1{(ih/z)^2}-1
=
-\frac{z^2}{h^2}-1.
\]
Applying $T_4$ and then $T_5$ gives the displayed formula.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} gives the requested explicit conformal map, and steps [](#s1-1){.pf-ref} through
[](#s1-6){.pf-ref} prove that it has the required source and target.

:::

:::

:::
