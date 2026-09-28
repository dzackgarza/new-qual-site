---
schema: qual/card@1
id: P-AGH5214IRRCURVESCHARP
kind: problem
title: Irreducible curves and ample divisors on a ruled surface in characteristic $p$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.2.14, the retained Egbert companion calculation, the
    ruled-surface canonical/intersection formulas, the normalization genus
    inequality, and Nakai--Moishezon. The companion's alpha is interpreted as
    the separable degree s of the normalization map to the base. Writing the
    total degree as a=s p^r makes the characteristic-p split precise: for
    a<p one has s=a, while for a>=p the weaker bound in the exercise follows
    already from s>=1. The ampleness proof below then checks every irreducible
    curve using exactly the three alternatives from part (a).
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
---

::: {.problem}
Let $X$ be a ruled surface over a curve $C$ of genus $g$, with invariant $e<0$, and assume that $\operatorname{char} k=p>0$ and $g \geqslant 2$.

a. If $Y \equiv a C_0+b f$ is an irreducible curve $\neq C_0, f$, then either

    - $a=1, b \geqslant 0$, or
    - $2 \leqslant a \leqslant p-1, b \geqslant \frac{1}{2} a e$, or
    - $a \geqslant p, b \geqslant \frac{1}{2} a e+1-g$.

b. If $a>0$ and $b>a\left(\frac{1}{2} e+(1 / p)(g-1)\right)$, then any divisor $D \equiv a C_0+b f$ is ample. On the other hand, if $D$ is ample, then $a>0$ and $b>\frac{1}{2} a e$.
:::

::: {.solution}
Recall the numerical formulas for the normalized ruled surface:
$$
C_0^2=-e,
\qquad
C_0\cdot f=1,
\qquad
f^2=0,
$$
and
$$
K_X\equiv-2C_0+(2g-2-e)f.
$$

<1>1. If
$$
Y\equiv aC_0+bf
$$
is an irreducible curve distinct from a fibre, then
$$
a=Y\cdot f\ge1.
$$

::: {.proof}
The ruling
$$
\pi:X\longrightarrow C
$$
restricts to a nonconstant finite morphism from $Y$ to $C$ unless $Y$ is
contained in a fibre. Its degree is the intersection number with a general
fibre:
$$
\deg(\pi|_Y)=Y\cdot f=a.
$$
Since $Y$ is not a fibre, this degree is positive.
:::

<1>2. If $a=1$, then $Y$ is a section and
$$
\boxed{b\ge0}.
$$

::: {.proof}
The finite morphism
$$
Y\longrightarrow C
$$
has degree one. Since $Y$ is integral and $C$ is nonsingular, hence normal,
it is an isomorphism. Thus $Y$ is a section.

Let
$$
0\longrightarrow N
\longrightarrow\mathcal E
\longrightarrow L
\longrightarrow0
$$
be the quotient-line-bundle sequence corresponding to this section. The
divisor formula for a section of $\PP(\mathcal E)$ gives
$$
\OO_X(Y)
\cong
\OO_X(C_0)\tensor\pi^*N^{-1}.
$$
Numerically,
$$
Y\equiv C_0+(-\deg N)f,
$$
so
$$
b=-\deg N.
$$

Because $\mathcal E$ is normalized, every line subbundle of $\mathcal E$
has degree at most zero: an inclusion of a positive-degree line bundle $N$
would give a nonzero section of the negative twist
$\mathcal E\tensor N^{-1}$. Hence
$$
\deg N\le0,
$$
and therefore $b\ge0$.
:::

<1>3. Assume $a\ge2$. Let
$$
\nu:\widetilde Y\longrightarrow Y
$$
be the normalization and let
$$
\varphi=\pi\circ\nu:\widetilde Y\longrightarrow C.
$$
If $s$ is the separable degree of $\varphi$, then
$$
\deg\varphi=a=s p^r
$$
for some $r\ge0$, and
$$
2g(\widetilde Y)-2\ge s(2g-2).
$$

::: {.proof}
The total degree is $a$ by step <1>1. In characteristic $p$, the degree of a
finite morphism of nonsingular curves factors as its separable degree times
its inseparable degree, and the latter is a power of $p$:
$$
a=s p^r.
$$

Factor $\varphi$ into its purely inseparable part and its separable part.
Over the algebraically closed ground field, a finite purely inseparable map
between nonsingular projective curves is a Frobenius power up to Frobenius
twist, so it preserves the genus. Riemann--Hurwitz applied to the separable
part therefore gives
$$
2g(\widetilde Y)-2
=
s(2g-2)+\deg R
\ge
s(2g-2),
$$
where $R$ is the effective ramification divisor.
:::

<1>4. For $a\ge2$ one has
$$
\boxed{
(a-1)(2b-ae)
\ge
-2(a-s)(g-1).}
$$

::: {.proof}
The arithmetic genus of the integral curve $Y$ dominates the genus of its
normalization:
$$
p_a(Y)\ge g(\widetilde Y)
$$
[[D-G1AEH]]. Hence step <1>3 gives
$$
2p_a(Y)-2\ge s(2g-2).
$$

By adjunction [[T-SRFADJ]],
$$
2p_a(Y)-2=Y\cdot(Y+K_X).
$$
Using the numerical formulas at the start,
$$
\begin{aligned}
Y\cdot(Y+K_X)
&=(aC_0+bf)\cdot
\bigl((a-2)C_0+(b+2g-2-e)f\bigr)\\
&=(a-1)(2b-ae)+2a(g-1).
\end{aligned}
$$
Comparing with $2s(g-1)$ and rearranging gives the claimed inequality.
:::

<1>5. If
$$
2\le a\le p-1,
$$
then
$$
\boxed{b\ge\frac12ae}.
$$

::: {.proof}
Since $a<p$, no nontrivial power of $p$ divides the inseparable degree in
$$
a=s p^r.
$$
Thus $r=0$ and $s=a$. Step <1>4 becomes
$$
(a-1)(2b-ae)\ge0.
$$
Because $a-1>0$,
$$
2b-ae\ge0,
$$
which is the desired inequality.
:::

<1>6. If
$$
a\ge p,
$$
then
$$
\boxed{b\ge\frac12ae+1-g}.
$$

::: {.proof}
The separable degree satisfies
$$
1\le s\le a.
$$
From step <1>4,
$$
2b-ae
\ge
-2\frac{a-s}{a-1}(g-1).
$$
Since
$$
0\le\frac{a-s}{a-1}\le1,
$$
one obtains
$$
2b-ae\ge-2(g-1).
$$
Equivalently,
$$
b\ge\frac12ae+1-g.
$$
Together with steps <1>2 and <1>5, this proves part (a).
:::

<1>7. Now let
$$
D\equiv aC_0+bf
$$
satisfy
$$
a>0,
\qquad
b>a\left(\frac e2+\frac{g-1}{p}\right).
$$
Then
$$
D^2>0,
\qquad
D\cdot f>0,
\qquad
D\cdot C_0>0.
$$

::: {.proof}
First,
$$
D\cdot f=a>0.
$$
Also
$$
D^2=-a^2e+2ab
=
a(2b-ae).
$$
The hypothesis gives
$$
2b-ae>\frac{2a(g-1)}p>0,
$$
so $D^2>0$.

Finally,
$$
D\cdot C_0=b-ae.
$$
Since $e<0$,
$$
b-ae
>
-\frac12ae+\frac{a(g-1)}p
>0.
$$
:::

<1>8. Under the hypotheses of step <1>7,
$$
D\cdot Y>0
$$
for every irreducible curve
$$
Y\ne C_0,f.
$$

::: {.proof}
Write
$$
Y\equiv cC_0+df.
$$
Part (a), already proved, gives exactly three possibilities. In all cases
$$
D\cdot Y=-ace+ad+bc.
$$

If $c=1$, then $d\ge0$, so
$$
D\cdot Y
=
-ae+ad+b
\ge
-ae+b.
$$
The hypothesis implies $b>ae/2$, and $e<0$, hence
$$
-ae+b>-\frac12ae>0.
$$

If $2\le c\le p-1$, then
$$
d\ge\frac12ce.
$$
Therefore
$$
\begin{aligned}
D\cdot Y
&\ge
-ace+\frac12ace+bc\\
&=c\left(b-\frac12ae\right)\\
&>0.
\end{aligned}
$$

Finally, if $c\ge p$, then
$$
d\ge\frac12ce+1-g.
$$
Hence
$$
\begin{aligned}
D\cdot Y
&\ge
-ace+a\left(\frac12ce+1-g\right)+bc\\
&=
c\left(b-\frac12ae\right)-a(g-1).
\end{aligned}
$$
The hypothesis says
$$
b-\frac12ae>\frac{a(g-1)}p,
$$
so
$$
D\cdot Y
>
a(g-1)\left(\frac cp-1\right)
\ge0.
$$
The inequality is strict, so $D\cdot Y>0$ also when $c=p$.
:::

<1>9. The divisor $D$ in step <1>7 is ample.

::: {.proof}
Step <1>7 gives $D^2>0$ and positive intersection with $C_0$ and $f$.
Step <1>8 gives positive intersection with every other irreducible curve on
$X$. The Nakai--Moishezon criterion [[T-SRFNAKAI]] therefore gives
$$
\boxed{D\text{ is ample}.}
$$
This proves the forward implication in part (b).
:::

<1>10. Conversely, if
$$
D\equiv aC_0+bf
$$
is ample, then
$$
\boxed{a>0,
\qquad
b>\frac12ae}.
$$

::: {.proof}
Ampleness and Nakai--Moishezon give
$$
D\cdot f>0.
$$
Since
$$
D\cdot f=a,
$$
one has $a>0$.

Again by Nakai--Moishezon,
$$
D^2>0.
$$
But
$$
D^2=a(2b-ae).
$$
Since $a>0$, this forces
$$
2b-ae>0,
$$
or
$$
b>\frac12ae.
$$
This proves the converse implication in part (b).
:::

<1>11. Q.E.D.

::: {.proof}
Steps <1>1--<1>6 prove part (a), and steps <1>7--<1>10 prove part (b).
:::
:::
