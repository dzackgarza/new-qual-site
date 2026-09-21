---
schema: qual/card@1
id: P-AZOFF-C08
kind: problem
title: Conformal map of the slit disk $\mathbb D\setminus[0,1)$ onto the disk
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Conformal mapping, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used the square-root branch with 0<Arg z<2pi to unfold the slit disk onto
    the upper half-disk. The map (1+w)/(1-w) sends that half-disk to the first
    quadrant, squaring sends the quadrant to the upper half-plane, and the
    inverse Cayley transform sends the half-plane to the disk. The source
    compilation contains no worked solution.
---

::: {.problem}
Let D be the region obtained by removing the interval [0, 1) from the unit disk $| z | < 1$ . Find a conformal map from D onto the open unit disk.
:::

::: {.solution}
Let
$$
D=\DD\sm[0,1).
$$
On
$$
\CC\sm[0,\infty)
$$
take the logarithm branch
$$
\Log z=\log\abs z+i\Arg z,
\qquad
0<\Arg z<2\pi,
$$
and define
$$
s(z)=\exp\!\left(\frac12\Log z\right).
$$

<1>1. The map
$$
s:D\longrightarrow
U,
\qquad
U=\{w\in\CC:\abs w<1,\ \operatorname{Im}w>0\},
$$
is a conformal bijection.

::: {.proof}
For $z\in D$,
$$
\abs{s(z)}=\sqrt{\abs z}<1
$$
and
$$
0<\arg s(z)=\frac12\Arg z<\pi.
$$
Thus $s(z)\in U$.

Conversely, if
$$
w\in U,
$$
then
$$
0<\arg w<\pi.
$$
Set
$$
z=w^2.
$$
Then $\abs z<1$ and
$$
0<\arg z<2\pi,
$$
so $z\in D$. By the chosen branch,
$$
s(z)=w.
$$
Thus $s$ is onto, and the identity
$$
z=s(z)^2
$$
shows that it is injective.

Since
$$
s'(z)=\frac{s(z)}{2z}\neq0
$$
on $D$, the map is conformal.
:::

<1>2. The map
$$
M:U\longrightarrow Q_1,
\qquad
M(w)=\frac{1+w}{1-w},
$$
where
$$
Q_1=\{\zeta\in\CC:\operatorname{Re}\zeta>0,\ \operatorname{Im}\zeta>0\},
$$
is a conformal bijection.

::: {.proof}
For $w\in U$,
$$
\operatorname{Re}M(w)
=
\frac{1-\abs w^2}{\abs{1-w}^2}
>
0
$$
and
$$
\operatorname{Im}M(w)
=
\frac{2\operatorname{Im}w}{\abs{1-w}^2}
>
0.
$$
Hence $M(U)\subseteq Q_1$.

The inverse is
$$
M^{-1}(\zeta)=\frac{\zeta-1}{\zeta+1}.
$$
For $\zeta=u+iv\in Q_1$,
$$
\abs{\zeta+1}^2-\abs{\zeta-1}^2=4u>0,
$$
so $\abs{M^{-1}(\zeta)}<1$, and
$$
\operatorname{Im}M^{-1}(\zeta)
=
\frac{2v}{\abs{\zeta+1}^2}
>
0.
$$
Thus $M^{-1}(Q_1)\subseteq U$, proving bijectivity.

Finally,
$$
M'(w)=\frac{2}{(1-w)^2}\neq0
$$
on $U$, so $M$ is conformal.
:::

<1>3. The squaring map
$$
P:Q_1\longrightarrow\mathcal H,
\qquad
P(\zeta)=\zeta^2,
$$
where
$$
\mathcal H=\{\xi\in\CC:\operatorname{Im}\xi>0\},
$$
is a conformal bijection.

::: {.proof}
If $\zeta=u+iv\in Q_1$, then
$$
\operatorname{Im}(\zeta^2)=2uv>0.
$$
Conversely, each $\xi\in\mathcal H$ has exactly one square root with argument
in
$$
\left(0,\frac{\pi}{2}\right),
$$
so exactly one square root lies in $Q_1$. Hence $P$ is bijective.

Since
$$
P'(\zeta)=2\zeta\neq0
$$
on $Q_1$, it is conformal.
:::

<1>4. The Cayley map
$$
C:\mathcal H\longrightarrow\DD,
\qquad
C(\xi)=\frac{\xi-i}{\xi+i},
$$
is a conformal bijection.

::: {.proof}
For $\xi=x+iy$ with $y>0$,
$$
\abs{\xi+i}^2-\abs{\xi-i}^2=4y>0,
$$
so $\abs{C(\xi)}<1$. Its inverse is
$$
C^{-1}(\eta)=i\frac{1+\eta}{1-\eta},
$$
which maps $\DD$ into $\mathcal H$. Hence $C$ is bijective. Also
$$
C'(\xi)=\frac{2i}{(\xi+i)^2}\neq0
$$
on $\mathcal H$, so it is conformal.
:::

<1>5. Put
$$
q(z)=
\left(
\frac{1+s(z)}{1-s(z)}
\right)^2.
$$
A conformal bijection from the slit disk $D$ onto the unit disk is
$$
\boxed{
F(z)=\frac{q(z)-i}{q(z)+i},
\qquad
s(z)=\exp\!\left(\frac12\Log z\right),
\quad
0<\Arg z<2\pi.
}
$$

::: {.proof}
By steps <1>1--<1>4,
$$
F=C\circ P\circ M\circ s
$$
is a composition of conformal bijections
$$
D\xrightarrow{s}U\xrightarrow{M}Q_1
\xrightarrow{P}\mathcal H\xrightarrow{C}\DD.
$$
Therefore $F$ is a conformal bijection from $D$ onto $\DD$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the requested map.
:::
:::
