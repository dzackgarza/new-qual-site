---
schema: qual/card@1
id: P-AZOFF-C04
kind: problem
title: Conformal map of the right half-plane outside $|z-i|\le 1$ onto the upper half-plane
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Conformal mapping, Problem 4, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Sent the two boundary circles through 0 and 2i to coordinate rays with
    M(z)=z/(2i-z). Explicit real and imaginary part formulas show M maps the
    domain bijectively onto the third quadrant. Squaring is a conformal
    bijection from that quadrant onto the upper half-plane, giving
    (z/(2i-z))^2. The source compilation contains no worked solution.
---

::: {.problem}
Find a conformal map from $D : = \left\{ z \in \mathbb { C } : | z - i | > 1 , \mathrm { R e } ( z ) > 0 \right\}$ onto the open upper half plane.
:::

::: {.solution}
Let
$$
D=\{z\in\CC:\abs{z-i}>1,\ \operatorname{Re}z>0\}
$$
and let
$$
Q_3=\{w\in\CC:\operatorname{Re}w<0,\ \operatorname{Im}w<0\}.
$$
Define
$$
M(z)=\frac{z}{2i-z}.
$$

::: pf

::: pf-step

The map $M$ sends $D$ into $Q_3$.

::: pf-proof

Write
$$
z=x+iy\in D
$$
and put
$$
\Delta=\abs{2i-z}^2=x^2+(2-y)^2>0.
$$
Multiplying numerator and denominator by the conjugate of $2i-z$ gives
$$
\operatorname{Re}M(z)
=
\frac{1-\abs{z-i}^2}{\Delta}
<
0
$$
because $\abs{z-i}>1$, and
$$
\operatorname{Im}M(z)
=
\frac{-2x}{\Delta}
<
0
$$
because $x>0$. Hence $M(z)\in Q_3$.

:::

:::

::: {.pf-step #s2}

The map
$$
M:D\longrightarrow Q_3
$$
is a conformal bijection with inverse
$$
M^{-1}(w)=\frac{2iw}{1+w}.
$$

::: pf-proof

Solving
$$
w=\frac{z}{2i-z}
$$
for $z$ gives the displayed inverse.

Conversely, let
$$
w=u+iv\in Q_3
$$
and set
$$
z=\frac{2iw}{1+w}.
$$
Since $u<0$ and $v<0$, one has $w\neq-1$, so the formula is defined. Put
$$
\Gamma=\abs{1+w}^2=(1+u)^2+v^2.
$$
Direct calculation gives
$$
\operatorname{Re}z
=
\frac{-2v}{\Gamma}
>
0.
$$
Also
$$
z-i=i\frac{w-1}{w+1},
$$
so
$$
\abs{z-i}^2
=
\frac{\abs{w-1}^2}{\abs{w+1}^2}.
$$
Because
$$
\abs{w-1}^2-\abs{w+1}^2=-4u>0,
$$
we obtain
$$
\abs{z-i}>1.
$$
Thus $z\in D$, proving that the displayed inverse maps $Q_3$ into $D$.

Finally,
$$
M'(z)=\frac{2i}{(2i-z)^2}\neq0
$$
on $D$, so $M$ is conformal.

:::

:::

::: {.pf-step #s3}

The squaring map
$$
S:Q_3\longrightarrow\mathcal H,
\qquad
S(w)=w^2,
$$
where
$$
\mathcal H=\{\zeta\in\CC:\operatorname{Im}\zeta>0\},
$$
is a conformal bijection.

::: pf-proof

If
$$
w=u+iv\in Q_3,
$$
then
$$
\operatorname{Im}(w^2)=2uv>0,
$$
so $S(Q_3)\subseteq\mathcal H$.

Every $\zeta\in\mathcal H$ has argument
$$
0<\theta<\pi.
$$
Its two square roots have arguments
$$
\frac{\theta}{2}
\qquad\text{and}\qquad
\frac{\theta}{2}+\pi.
$$
Exactly the second lies in
$$
\pi<\arg w<\frac{3\pi}{2},
$$
which is $Q_3$. Hence every $\zeta\in\mathcal H$ has exactly one square root
in $Q_3$, proving bijectivity.

Since
$$
S'(w)=2w\neq0
$$
on $Q_3$, the map is conformal.

:::

:::

::: {.pf-step #s4}

A conformal bijection from $D$ onto the upper half-plane is
$$
\boxed{
F(z)
=
\left(\frac{z}{2i-z}\right)^2
}.
$$

::: pf-proof

By steps [](#s2){.pf-ref} and [](#s3){.pf-ref},
$$
F=S\circ M
$$
is a composition of conformal bijections
$$
D\xrightarrow{M}Q_3\xrightarrow{S}\mathcal H.
$$
Therefore $F$ is a conformal bijection from $D$ onto $\mathcal H$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the requested map.

:::

:::

:::
