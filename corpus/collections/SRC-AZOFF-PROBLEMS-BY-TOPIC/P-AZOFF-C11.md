---
schema: qual/card@1
id: P-AZOFF-C11
kind: problem
title: Conformal map of a slit lens onto the upper half-plane
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Conformal mapping, Problem 11, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used M(z)=(z-i)/(z+i) to send the lens to the wedge
    3pi/4<arg w<5pi/4; the removed segment [0,i) maps to [-1,0). The fourth
    power maps the wedge biholomorphically to the plane slit along the
    nonpositive real axis and maps the removed segment to (0,1], leaving the
    slit plane C minus (-infinity,1]. Translating by -1 and taking the
    principal square root gives the right half-plane, then multiplication by
    i gives the upper half-plane. The source compilation contains no worked
    solution.
---

::: {.problem}
Find a bijective conformal map from

$$
G : = \{ z \in \mathbb { C } : | z - 1 | < { \sqrt { 2 } } , ~ | z + 1 | < { \sqrt { 2 } } \} ~ \backslash ~ [ 0 , i )
$$

onto the open upper half plane.
:::

::: {.solution}
Let
$$
L=
\{z\in\CC:\abs{z-1}<\sqrt2,\ \abs{z+1}<\sqrt2\}
$$
be the unslit lens and define
$$
M(z)=\frac{z-i}{z+i}.
$$
Also put
$$
W=
\{w\in\CC:3\pi/4<\arg w<5\pi/4\},
$$
where the argument on $W$ is chosen in that interval.

<1>1. The map
$$
M:L\longrightarrow W
$$
is a conformal bijection.

::: {.proof}
Write
$$
z=x+iy
$$
and
$$
M(z)=u+iv.
$$
Since
$$
\abs{z+i}^2=x^2+(y+1)^2,
$$
direct calculation gives
$$
u
=
\frac{\abs z^2-1}{\abs{z+i}^2},
\qquad
v
=
\frac{-2x}{\abs{z+i}^2}.
$$
Therefore
$$
u+v
=
\frac{\abs z^2-1-2x}{\abs{z+i}^2}
=
\frac{\abs{z-1}^2-2}{\abs{z+i}^2}
$$
and
$$
u-v
=
\frac{\abs z^2-1+2x}{\abs{z+i}^2}
=
\frac{\abs{z+1}^2-2}{\abs{z+i}^2}.
$$
Thus
$$
z\in L
\quad\Longleftrightarrow\quad
u+v<0
\ \text{ and }\
u-v<0.
$$
These two inequalities describe exactly the wedge
$$
3\pi/4<\arg w<5\pi/4.
$$

The inverse Möbius map is
$$
M^{-1}(w)=i\frac{1+w}{1-w}.
$$
Since $1\notin W$, it is defined on all of $W$, and the displayed
equivalences show that $M^{-1}(W)\subseteq L$. Hence $M$ is bijective.

Finally,
$$
M'(z)=\frac{2i}{(z+i)^2}\neq0
$$
on $L$, because $-i$ is a boundary point of the lens. Thus $M$ is conformal.
:::

<1>2. The removed slit satisfies
$$
M([0,i))=[-1,0).
$$

::: {.proof}
For
$$
z=iy,
\qquad
0\leq y<1,
$$
one has
$$
M(iy)
=
\frac{y-1}{y+1}.
$$
As $y$ runs from $0$ to $1$, this runs monotonically from $-1$ toward $0$
without attaining $0$. Hence the image is exactly $[-1,0)$.
:::

<1>3. The fourth-power map
$$
P:W\longrightarrow
\CC\sm(-\infty,0],
\qquad
P(w)=w^4,
$$
is a conformal bijection.

::: {.proof}
If
$$
w=re^{i\theta},
\qquad
3\pi/4<\theta<5\pi/4,
$$
then
$$
3\pi<4\theta<5\pi.
$$
Subtracting $4\pi$ gives an argument in $(-\pi,\pi)$, so $w^4$ lies in the
plane slit along the nonpositive real axis.

Conversely, for
$$
\xi=Re^{i\phi},
\qquad
R>0,
\quad
-\pi<\phi<\pi,
$$
there is a unique fourth root
$$
w=R^{1/4}e^{i(\phi+4\pi)/4}
$$
whose argument lies in $(3\pi/4,5\pi/4)$. Thus $P$ is bijective.

Since
$$
P'(w)=4w^3\neq0
$$
on $W$, it is conformal.
:::

<1>4. The composition
$$
Q(z)=M(z)^4-1
$$
is a conformal bijection from the slit lens $G$ onto
$$
\CC\sm(-\infty,0].
$$

::: {.proof}
By steps <1>1--<1>3,
$$
P\circ M
$$
maps the unslit lens $L$ bijectively onto
$$
\CC\sm(-\infty,0].
$$
Step <1>2 gives
$$
P(M([0,i)))
=
(0,1].
$$
Therefore removing the slit from $L$ removes exactly $(0,1]$ from the
slit-plane image:
$$
(P\circ M)(G)
=
\CC\sm(-\infty,1].
$$
Subtracting $1$ yields
$$
Q(G)=\CC\sm(-\infty,0].
$$
Translation preserves conformality and bijectivity.
:::

<1>5. On
$$
\CC\sm(-\infty,0]
$$
take the principal logarithm and define
$$
s(\xi)
=
\exp\!\left(\frac12\Log\xi\right).
$$
Then
$$
s:\CC\sm(-\infty,0]
\longrightarrow
R,
\qquad
R=\{\eta\in\CC:\operatorname{Re}\eta>0\},
$$
is a conformal bijection.

::: {.proof}
For the principal argument
$$
-\pi<\Arg\xi<\pi,
$$
the argument of $s(\xi)$ lies in
$$
\left(-\frac{\pi}{2},\frac{\pi}{2}\right),
$$
so $s(\xi)\in R$.

Conversely, every $\eta\in R$ has argument in that interval, so
$$
\xi=\eta^2
$$
has principal argument in $(-\pi,\pi)$ and satisfies $s(\xi)=\eta$.
Thus $s$ is bijective.

Also
$$
s'(\xi)=\frac{s(\xi)}{2\xi}\neq0,
$$
so it is conformal.
:::

<1>6. A bijective conformal map from $G$ onto the upper half-plane is
$$
\boxed{
F(z)
=
i\exp\!\left[
\frac12
\Log\!\left(
\left(\frac{z-i}{z+i}\right)^4-1
\right)
\right],
}
$$
where $\Log$ is the principal logarithm.

::: {.proof}
By steps <1>4--<1>5,
$$
s\circ Q
$$
maps $G$ conformally and bijectively onto the right half-plane. Multiplication
by $i$ sends the right half-plane onto
$$
\mathcal H=\{w\in\CC:\operatorname{Im}w>0\}.
$$
Hence the displayed $F$ is the required conformal bijection.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 gives the requested map.
:::
:::
