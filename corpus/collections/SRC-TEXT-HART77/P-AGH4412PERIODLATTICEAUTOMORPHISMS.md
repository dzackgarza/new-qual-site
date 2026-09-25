---
schema: qual/card@1
id: P-AGH4412PERIODLATTICEAUTOMORPHISMS
kind: problem
title: The values of $\tau$ giving extra automorphisms or a degree $2$ endomorphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.12 together with Theorem IV.4.15B, Proposition
    IV.4.18, Theorem IV.4.19, and Exercise IV.4.11. The low-degree
    classification below uses the defining inequalities of Hartshorne's
    fundamental region G and the norm formula deg(f_alpha)=|alpha|^2.
    For the final matching of the three period representatives with the three
    j-values of Exercise IV.4.5, also checked the Hilbert class polynomials of
    discriminants -4, -8, and -7.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Again let $X$ be an elliptic curve over $\CC$ determined by the elliptic functions with periods $1, \tau$, and assume that $\tau$ lies in the region $G$ of (4.15B).

a. If $X$ has any automorphisms leaving $P_0$ fixed other than $\pm 1$, show that either $\tau=i$ or $\tau=\omega$, as in (4.20.1) and (4.20.2). This gives another proof of the fact (4.7) that there are only two curves, up to isomorphism, having automorphisms other than $\pm 1$.

b. Now show that there are exactly three values of $\tau$ for which $X$ admits an endomorphism of degree 2. Can you match these with the three values of $j$ determined in (Ex.
4.5)? Answers: $\tau=i$; $\tau=\sqrt{-2}$; $\tau=\frac{1}{2}(-1+\sqrt{-7})$.
:::

::: {.solution}
Put
$$
\Lambda=\ZZ+\ZZ\tau,
\qquad
\tau=x+iy,
\qquad
y>0.
$$
Hartshorne's region $G$ satisfies
$$
-\frac12\le x<\frac12,
\qquad
\abs{\tau}\ge1,
$$
with the boundary convention in Theorem IV.4.15B. In particular,
$$
y^2
=
\abs{\tau}^2-x^2
\ge
1-\frac14
=
\frac34.
$$

<1>1. Let $\alpha\in R=\Endo(X,P_0)$ correspond to multiplication by $\alpha$ on $\CC/\Lambda$.
Write
$$
\alpha=a+b\tau,
\qquad
\alpha\tau=c+d\tau,
$$
with $a,b,c,d\in\ZZ$.
If $\alpha\notin\ZZ$, then $b\ne0$ and
$$
\boxed{
b\tau^2+(a-d)\tau-c=0.
}
$$

::: {.proof}
Proposition IV.4.18 says precisely that
$$
R=\{\alpha\in\CC:\alpha\Lambda\subseteq\Lambda\}.
$$
Since $1,\tau$ is a $\ZZ$-basis of $\Lambda$, the two displayed integral expressions for $\alpha$ and $\alpha\tau$ are necessary and sufficient.
Eliminating $\alpha$ gives the boxed quadratic equation.
If $b=0$, then $\alpha=a\in\ZZ$.
:::

<1>2. If $\deg f_\alpha\le2$ and $\alpha\notin\ZZ$, then
$$
\boxed{b=\pm1.}
$$

::: {.proof}
By [[P-AGH4411COMPLEXMULTIPLICATION|Exercise IV.4.11(a)]],
$$
\deg f_\alpha=\abs{\alpha}^2.
$$
Since
$$
\Im(\alpha)=by,
$$
we have
$$
b^2y^2\le\abs{\alpha}^2\le2.
$$
The bound $y^2\ge3/4$ therefore gives
$$
b^2\le\frac83<4.
$$
Thus $0<\abs b<2$, so $b=\pm1$.
:::

<1>3. After replacing $\alpha$ by $-\alpha$ if necessary, assume $b=1$.
Then there is an integer
$$
t=d-a
$$
such that
$$
\tau^2-t\tau-c=0,
$$
and
$$
\boxed{
t=2x,
\qquad
-c=\abs{\tau}^2,
\qquad
\abs{\alpha}^2=a^2+at-c.
}
$$
Moreover $t\in\{-1,0\}$ for the points of $G$ relevant below.

::: {.proof}
With $b=1$, step <1>1 gives
$$
\tau^2+(a-d)\tau-c=0,
$$
which is the first assertion.
Since this polynomial has real integral coefficients and $\tau\notin\RR$, its other root is $\bar\tau$.
Vieta's formulas give
$$
\tau+\bar\tau=t,
\qquad
\tau\bar\tau=-c.
$$
Thus $t=2x$ and $-c=\abs\tau^2$.
Also
$$
\abs{a+\tau}^2
=
a^2+a(\tau+\bar\tau)+\tau\bar\tau
=
a^2+at-c.
$$
Because $-1/2\le x<1/2$ and $t=2x\in\ZZ$, one has $t\in\{-1,0\}$.
The excluded right boundary $x=1/2$ is precisely the boundary convention making the representative in $G$ unique.
:::

<1>4. If $X$ has an automorphism fixing $P_0$ other than $\pm1$, then
$$
\boxed{
\tau=i
\quad\text{or}\quad
\tau=\omega=\frac{-1+\sqrt{-3}}2.
}
$$

::: {.proof}
An automorphism has degree $1$.
If its multiplier $\alpha$ were an integer, then
$$
1=\abs\alpha^2=\alpha^2,
$$
so $\alpha=\pm1$.
Thus a new automorphism has $\alpha\notin\ZZ$, and steps <1>2--<1>3 apply.
Since
$$
1=\abs\alpha^2=a^2+at-c,
$$
we have
$$
c=a^2+at-1.
$$

If $t=0$, then $c=a^2-1$.
The quadratic
$$
\tau^2-c=0
$$
must have nonreal roots, so its discriminant $4c$ is negative.
Hence $a=0$, $c=-1$, and
$$
\tau^2+1=0.
$$
The root in the upper half-plane is $\tau=i$.

If $t=-1$, then
$$
c=a^2-a-1,
$$
and nonreality gives
$$
1+4c=4a^2-4a-3<0.
$$
Thus $a=0$ or $a=1$; in either case $c=-1$, so
$$
\tau^2+\tau+1=0.
$$
The root in the upper half-plane is
$$
\tau=\frac{-1+\sqrt{-3}}2=\omega.
$$

Conversely, multiplication by $i$ preserves $\ZZ+\ZZ i$, and multiplication by $\omega$ preserves $\ZZ+\ZZ\omega$.
Both have norm $1$ and are different from $\pm1$.
This proves part (a).
:::

<1>5. If $X$ has an endomorphism of degree $2$, then
$$
\boxed{
\tau=i,
\qquad
\tau=\sqrt{-2},
\qquad
\tau=\frac{-1+\sqrt{-7}}2.
}
$$

::: {.proof}
No integer multiplier has degree $2$, since an integer $n$ has degree $n^2$.
Hence $\alpha\notin\ZZ$, and steps <1>2--<1>3 apply.
Now
$$
2=\abs\alpha^2=a^2+at-c,
$$
so
$$
c=a^2+at-2.
$$

If $t=0$, then $c=a^2-2$.
Nonreality of the roots gives
$$
4c=4a^2-8<0,
$$
so $a\in\{-1,0,1\}$.
For $a=\pm1$ one has $c=-1$ and therefore
$$
\tau=i.
$$
For $a=0$ one has $c=-2$ and therefore
$$
\tau=\sqrt{-2}.
$$

If $t=-1$, then $c=a^2-a-2$.
The discriminant condition is
$$
1+4c
=
4a^2-4a-7
<0,
$$
so $a=0$ or $a=1$.
In either case $c=-2$, and hence
$$
\tau^2+\tau+2=0.
$$
The root in the upper half-plane is
$$
\tau=\frac{-1+\sqrt{-7}}2.
$$
There are no other possibilities.
:::

<1>6. Each of the three values in step <1>5 actually has a degree-$2$ endomorphism.

::: {.proof}
For $\tau=i$, multiplication by
$$
1+i
$$
preserves $\ZZ+\ZZ i$ and has squared absolute value $2$.

For $\tau=\sqrt{-2}$, multiplication by $\tau$ preserves $\ZZ+\ZZ\tau$ because $\tau^2=-2$, and
$$
\abs{\tau}^2=2.
$$

For
$$
\tau=\frac{-1+\sqrt{-7}}2,
$$
one has $\tau^2+\tau+2=0$.
Hence multiplication by $\tau$ preserves $\ZZ+\ZZ\tau$, and again
$$
\abs{\tau}^2=\tau\bar\tau=2.
$$
Exercise IV.4.11(a) therefore gives degree $2$ in all three cases.
:::

<1>7. The three period values match the three $j$-values of [[P-AGH445DEGREETWOENDOMORPHISM|Exercise IV.4.5]] as follows:
$$
\boxed{
\begin{array}{c|c|c}
\tau & \text{CM discriminant} & j\\ \hline
i & -4 & 1728=2^6\cdot3^3\\
\sqrt{-2} & -8 & 8000=2^6\cdot5^3\\
\dfrac{-1+\sqrt{-7}}2 & -7 & -3375=-3^3\cdot5^3.
\end{array}
}
$$

::: {.proof}
For $\tau=i$, Example IV.4.20.1 already gives
$$
j(i)=1728.
$$
The other two lattices have endomorphism rings containing the quadratic orders of discriminants $-8$ and $-7$, respectively: their defining equations are
$$
\tau^2+2=0
$$
and
$$
\tau^2+\tau+2=0.
$$
The corresponding class-number-one Hilbert class polynomials are
$$
H_{-8}(T)=T-8000,
\qquad
H_{-7}(T)=T+3375.
$$
Thus the associated singular moduli are $8000$ and $-3375$.
These are exactly the two remaining $j$-values found in Exercise IV.4.5.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>4 proves part (a), steps <1>5--<1>6 prove the complete list in part (b), and step <1>7 matches the three period representatives with the three $j$-values from Exercise IV.4.5.
:::
:::
