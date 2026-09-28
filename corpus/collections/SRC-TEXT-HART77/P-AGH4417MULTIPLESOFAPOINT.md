---
schema: qual/card@1
id: P-AGH4417MULTIPLESOFAPOINT
kind: problem
title: Computing $nP$ on the curve $y^2+y=x^3-x$
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
    Read Hartshorne IV.4.17 with the generalized Weierstrass group law and
    discriminant formulas. Cross-checked the addition formula and
    discriminant convention against standard elliptic-curve references.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X$ be the curve $y^2+y=x^3-x$ of (4.23.8).

a. If $Q=(a, b)$ is a point on the curve, compute the coordinates of the point $P+Q$, where $P=(0,0)$, as a function of $a, b$.
Use this formula to find the coordinates of $nP$, $n=1,2, \ldots, 10$.
Check: $6P = (6,14)$.

b. This equation defines a nonsingular curve over $\FF_p$ for all $p \neq 37$.
:::

::: {.solution}
Write
$$
y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6
$$
with
$$
a_1=a_2=a_6=0,
\qquad
a_3=1,
\qquad
a_4=-1.
$$

<1>1. If $Q=(a,b)$ and $a\ne0$, then
$$
\boxed{
P+Q=
\left(
\frac{b^2}{a^2}-a,
-\frac ba\left(\frac{b^2}{a^2}-a\right)-1
\right).
}
$$

::: {.proof}
The line through $P=(0,0)$ and $Q=(a,b)$ is
$y=\lambda x$ with $\lambda=b/a$.  Substitution gives
$$
x\bigl(x^2-\lambda^2x-(\lambda+1)\bigr)=0.
$$
If $R$ is the third intersection point, Vieta gives
$$
x(R)=\lambda^2-a,
\qquad
y(R)=\lambda x(R).
$$
On this Weierstrass equation
$$
-(x,y)=(x,-y-1).
$$
Since $P+Q=-R$, the displayed formula follows.
:::

<1>2. The points with first coordinate $0$ are $P=(0,0)$ and
$-P=(0,-1)$, and
$$
\boxed{2P=(1,0)}.
$$

::: {.proof}
At $x=0$ the equation is $y(y+1)=0$.  For the tangent computation, put
$$
G(x,y)=y^2+y-x^3+x.
$$
Since $G_x(P)=G_y(P)=1$, the tangent at $P$ is $y=-x$.  Its third
intersection with $X$ is $(1,-1)$, whose inverse is $(1,0)$.
:::

<1>3. The first ten multiples of $P$ are
$$
\boxed{
\begin{array}{c|c}
n & nP\\ \hline
1&(0,0)\\
2&(1,0)\\
3&(-1,-1)\\
4&(2,-3)\\
5&\left(\frac14,-\frac58\right)\\
6&(6,14)\\
7&\left(-\frac59,\frac8{27}\right)\\
8&\left(\frac{21}{25},-\frac{69}{125}\right)\\
9&\left(-\frac{20}{49},-\frac{435}{343}\right)\\
10&\left(\frac{161}{16},-\frac{2065}{64}\right).
\end{array}
}
$$

::: {.proof}
Step <1>2 gives the first two entries.  Applying step <1>1 successively
gives
$$
\begin{aligned}
P+(1,0)&=(-1,-1),\\
P+(-1,-1)&=(2,-3),\\
P+(2,-3)&=\left(\frac14,-\frac58\right),\\
P+\left(\frac14,-\frac58\right)&=(6,14),\\
P+(6,14)&=\left(-\frac59,\frac8{27}\right),\\
P+\left(-\frac59,\frac8{27}\right)
&=\left(\frac{21}{25},-\frac{69}{125}\right),\\
P+\left(\frac{21}{25},-\frac{69}{125}\right)
&=\left(-\frac{20}{49},-\frac{435}{343}\right),\\
P+\left(-\frac{20}{49},-\frac{435}{343}\right)
&=\left(\frac{161}{16},-\frac{2065}{64}\right).
\end{aligned}
$$
In particular $6P=(6,14)$, as required.
:::

<1>4. The discriminant of the generalized Weierstrass equation is
$$
\boxed{\Delta=37.}
$$

::: {.proof}
For the coefficients
$$
a_1=a_2=a_6=0,
\qquad
a_3=1,
\qquad
a_4=-1,
$$
the standard quantities are
$$
b_2=0,
\qquad
b_4=-2,
\qquad
b_6=1,
\qquad
b_8=-1.
$$
Therefore
$$
\begin{aligned}
\Delta
&=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6\\
&=-8(-2)^3-27\\
&=37.
\end{aligned}
$$
:::

<1>5. For every prime $p\ne37$, the reduction of
$$
y^2+y=x^3-x
$$
over $\FF_p$ is nonsingular.

::: {.proof}
A generalized Weierstrass cubic is nonsingular over a field exactly when
its discriminant is nonzero in that field. By step <1>4, the discriminant
of this integral model reduces to the class of $37$ in $\FF_p$. Thus it is
nonzero for every $p\ne37$, proving part (b).
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 prove part (a), and steps <1>4--<1>5 prove part (b).
:::
:::
