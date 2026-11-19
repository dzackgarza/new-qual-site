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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.4.17, printed p. 94,
    rendered as page images from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne IV.4.17, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed the ten multiples from the group law on $y^2+y=x^3-x$ in exact rational arithmetic (all ten agree with the printed list, $6P=(6,14)$ included), the closed form for $P+Q$ at four values of $Q$, and $\Delta=-8b_4^3-27b_6^2=64-27=37$ from $b_4=-2$, $b_6=1$.
    Not checked: Yang's Solutions outside printed p. 94; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The card now carries a published-solution remark naming Yang Pi-Yeh's
    Solution 4.4.17 at printed p. 94; it had none before. No
    step, statement or hypothesis of the card changes.
---

::: {.problem}
Let $X$ be the curve $y^2+y=x^3-x$ of (4.23.8).

(a) If $Q=(a, b)$ is a point on the curve, compute the coordinates of the point $P+Q$, where $P=(0,0)$, as a function of $a, b$.
Use this formula to find the coordinates of $nP$, $n=1,2, \ldots, 10$.
Check: $6P = (6,14)$.

(b) This equation defines a nonsingular curve over $\FF_p$ for all $p \neq 37$.
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

::: pf

::: {.pf-step #s1}

If $Q=(a,b)$ and $a\ne0$, then
$$
\boxed{
P+Q=
\left(
\frac{b^2}{a^2}-a,
-\frac ba\left(\frac{b^2}{a^2}-a\right)-1
\right).
}
$$

::: pf-proof

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

:::

::: {.pf-step #s2}

The points with first coordinate $0$ are $P=(0,0)$ and
$-P=(0,-1)$, and
$$
\boxed{2P=(1,0)}.
$$

::: pf-proof

At $x=0$ the equation is $y(y+1)=0$.  For the tangent computation, put
$$
G(x,y)=y^2+y-x^3+x.
$$
Since $G_x(P)=G_y(P)=1$, the tangent at $P$ is $y=-x$.  Its third
intersection with $X$ is $(1,-1)$, whose inverse is $(1,0)$.

:::

:::

::: {.pf-step #s3}

The first ten multiples of $P$ are
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

::: pf-proof

Step [](#s2){.pf-ref} gives the first two entries.  Applying step [](#s1){.pf-ref} successively
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

:::

::: {.pf-step #s4}

The discriminant of the generalized Weierstrass equation is
$$
\boxed{\Delta=37.}
$$

::: pf-proof

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

:::

::: {.pf-step #s5}

For every prime $p\ne37$, the reduction of
$$
y^2+y=x^3-x
$$
over $\FF_p$ is nonsingular.

::: pf-proof

A generalized Weierstrass cubic is nonsingular over a field exactly when
its discriminant is nonzero in that field. By step [](#s4){.pf-ref}, the discriminant
of this integral model reduces to the class of $37$ in $\FF_p$. Thus it is
nonzero for every $p\ne37$, proving part (b).

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove part (a), and steps [](#s4){.pf-ref} and [](#s5){.pf-ref} prove part (b).

:::

:::

:::

::: {.remark title="Published solution"}
Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.4.17, printed p. 94, first records the addition law for a general Weierstrass equation, in the three cases $P_1=-P_2$, $P_1=P_2$ and $P_1\ne\pm P_2$, with $\lambda=\frac{3x_1^2+2a_2x_1+a_4-a_1y_1}{2y_1+a_1x_1+a_3}$ and $\nu=\frac{-x_1^3+a_4x_1+2a_6-a_3y_1}{2y_1+a_1x_1+a_3}$ in the doubling case and the chord-slope forms otherwise; those are the standard formulas and they are right. Specialising to $y^2+y=x^3-x$ at $P=(0,0)$ it prints $P+Q=\bigl(\frac{-a^3+ab+b^2}{a^2},\,-\frac{b^3}{a^3}+\frac ba-a+b-1\bigr)$, and that closed form is wrong in both coordinates. With $\lambda=b/a$ and $\nu=0$ the law gives $x_3=\frac{b^2}{a^2}-a$ and $y_3=-\lambda x_3-1=-\frac{b^3}{a^3}+b-1$; the corrected pair reproduces the entry's own list wherever it can be tested --- $Q=2P$, $3P$, $4P$ and $6P$ give $3P$, $4P$, $5P$ and $7P$ --- while the printed pair gives $(-1,-2)$, $(3,-1)$, $(\frac{16}{9},-\frac{91}{27})$ and $(-\frac54,-\frac{33}{8})$ there. The list $P,\dots,10P$ itself was recomputed from the law and every entry agrees, $6P=(6,14)$ included; and $\Delta=37$ is right, so the reduction is nonsingular for every $p\ne37$.
:::
