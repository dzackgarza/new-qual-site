---
schema: qual/card@1
id: P-TIE-F09-12
kind: problem
title: Conformal map of the disk minus a tangent disk onto the unit disk
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 12.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Checked the matching Azoff and retained UGA/Tie source appearances. The
    Cayley map (1+z)/(1-z) sends the region between the two circles tangent at
    1 exactly to the strip 0<Re w<1. The map exp(pi i w) sends that strip
    biholomorphically to the upper half-plane, and a final Cayley transform
    gives the unit disk. The recorded sources contain no worked solution.
---

::: {.problem}
Find a conformal map from $D = \{ z : \ | z | < 1 , \ | z - 1 / 2 | > 1 / 2 \}$ to the unit disk $\ \Delta = \{ z :$ $| z | < 1 \}$
:::

::: {.solution}
Let
$$
D=\left\{z\in\CC:\abs z<1,\ \abs{z-\frac12}>\frac12\right\}
$$
and define
$$
M(z)=\frac{1+z}{1-z}.
$$
Also put
$$
S=\{w\in\CC:0<\operatorname{Re}w<1\}.
$$

::: pf

::: {.pf-step #m-conformal-bijection}
The map
$$
M:D\longrightarrow S
$$
is a conformal bijection.

::: pf-proof
For $z\neq1$,
$$
\operatorname{Re}M(z)
=
\frac{1-\abs z^2}{\abs{1-z}^2}.
$$
Hence
$$
\abs z<1
\quad\Longleftrightarrow\quad
\operatorname{Re}M(z)>0.
$$
Moreover,
$$
\begin{aligned}
1-\operatorname{Re}M(z)
&=
\frac{\abs{1-z}^2-(1-\abs z^2)}{\abs{1-z}^2}\\
&=
\frac{2(\abs z^2-\operatorname{Re}z)}{\abs{1-z}^2}\\
&=
\frac{2\left(\abs{z-\frac12}^2-\frac14\right)}
{\abs{1-z}^2}.
\end{aligned}
$$
Thus
$$
\abs{z-\frac12}>\frac12
\quad\Longleftrightarrow\quad
\operatorname{Re}M(z)<1.
$$
These two equivalences show that $M(D)\subseteq S$.

Solving for $z$ gives
$$
M^{-1}(w)=\frac{w-1}{w+1}.
$$
For $w\in S$ one has $w\neq-1$, and applying the two displayed equivalences
to $z=M^{-1}(w)$ gives
$$
\abs z<1,
\qquad
\abs{z-\frac12}>\frac12.
$$
Hence $M^{-1}(S)\subseteq D$, proving bijectivity.

Finally,
$$
M'(z)=\frac{2}{(1-z)^2}\neq0
$$
on $D$, so $M$ is conformal.
:::

::: {.pf-step #e-conformal-bijection}
The map
$$
E:S\longrightarrow\mathcal H,
\qquad
E(w)=e^{\pi i w},
$$
where
$$
\mathcal H=\{\zeta\in\CC:\operatorname{Im}\zeta>0\},
$$
is a conformal bijection.

::: pf-proof
Write
$$
w=u+iv,
\qquad
0<u<1.
$$
Then
$$
E(w)=e^{-\pi v}e^{i\pi u},
$$
whose argument lies in $(0,\pi)$. Therefore $E(w)\in\mathcal H$.

Conversely, every
$$
\zeta=re^{i\theta}\in\mathcal H,
\qquad
r>0,
\quad
0<\theta<\pi,
$$
has the preimage
$$
w=\frac{\theta}{\pi}-i\frac{\log r}{\pi}\in S.
$$
Thus $E$ is onto.

If $E(w_1)=E(w_2)$, then
$$
w_1-w_2\in2\ZZ.
$$
The real parts of $w_1,w_2$ both lie in $(0,1)$, so their difference has
real part in $(-1,1)$. Hence the only possible element of $2\ZZ$ is $0$,
and $w_1=w_2$. Thus $E$ is injective.

Since
$$
E'(w)=\pi i e^{\pi i w}\neq0,
$$
the map is conformal.
:::

<1>3. The map
$$
C:\mathcal H\longrightarrow\DD,
\qquad
C(\zeta)=\frac{\zeta-i}{\zeta+i},
$$
is a conformal bijection.

::: {.proof}
For $\zeta=x+iy$ with $y>0$,
$$
\abs{\zeta+i}^2-\abs{\zeta-i}^2=4y>0,
$$
so
$$
\abs{C(\zeta)}<1.
$$
Writing $\eta=C(\zeta)$ and solving for $\zeta$ gives
$$
C^{-1}(\eta)=i\frac{1+\eta}{1-\eta},
$$
and the inverse Cayley map sends $\DD$ into $\mathcal H$. Hence $C$ is
bijective. Its derivative
$$
C'(\zeta)=\frac{2i}{(\zeta+i)^2}
$$
never vanishes on $\mathcal H$, so $C$ is conformal.
:::

<1>4. A conformal bijection from the given domain onto the unit disk is
$$
\boxed{
F(z)
=
\frac{
\exp\!\left(\pi i\frac{1+z}{1-z}\right)-i
}{
\exp\!\left(\pi i\frac{1+z}{1-z}\right)+i
}.
}
$$

::: {.proof}
By steps <1>1--<1>3,
$$
F=C\circ E\circ M
$$
is a composition of conformal bijections
$$
D\xrightarrow{M}S\xrightarrow{E}\mathcal H\xrightarrow{C}\DD.
$$
Therefore $F$ is a conformal bijection from $D$ onto the unit disk.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested map.
:::
:::
