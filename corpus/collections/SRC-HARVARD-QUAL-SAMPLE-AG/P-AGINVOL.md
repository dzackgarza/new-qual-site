---
schema: qual/card@1
id: P-AGINVOL
kind: problem
title: Involutions of an elliptic curve over $\CC$, their fixed points, and the quotient
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Involutions
  - Quotients
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is McMullen's sequence on involutions of a complex elliptic curve, their quotient, fixed points, and the identification of the branched quotient with the Riemann sphere.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
What are the involutions of an elliptic curve over $\CC$?

What are the fixed points of such an involution, and what quotient does it produce?

How would you show that quotient is $\CP^1$?
:::

::: {.solution}
Fix an origin $0\in E$, so that the elliptic curve is a complex Lie group.

<1>1. Every holomorphic automorphism $\varphi:E\to E$ has a unique form
\[
\varphi=t_a\circ u,
\qquad
a=\varphi(0),
\qquad
u(0)=0,
\]
where $t_a(x)=x+a$ is translation and $u$ is a group automorphism of $E$.
::: {.proof}
Set
\[
u=t_{-a}\circ\varphi.
\]
Then $u(0)=0$, and clearly $\varphi=t_a\circ u$; uniqueness follows by evaluating at $0$.

To see that an automorphism fixing $0$ is a group automorphism, write
\[
E\cong\mathbb C/\Lambda.
\]
The map $u$ lifts to a holomorphic map $U:\mathbb C\to\mathbb C$ with $U(0)=0$.  Its derivative $U'$ is $\Lambda$-periodic and hence descends to a holomorphic function on the compact Riemann surface $E$.  Therefore $U'$ is constant, so
\[
U(z)=cz
\]
for some $c\in\mathbb C$.  Since $u$ is an automorphism, $c\Lambda=\Lambda$.  Thus $u$ is induced by multiplication by $c$ and is a group automorphism.
:::

<1>2. The nonidentity involutions of $E$ are exactly the following two types:

1. translations
\[
t_a(x)=x+a,
\qquad
0\ne a\in E[2];
\]

2. involutions
\[
\sigma_a(x)=a-x,
\qquad
a\in E.
\]
::: {.proof}
Let $\varphi=t_a\circ u$ be an involution.  By <1>1, after uniformizing $E=\mathbb C/\Lambda$, the origin-fixing automorphism $u$ is multiplication by some $c$ with $c\Lambda=\Lambda$.  The linear part of $\varphi^2$ is $u^2$, so
\[
c^2=1.
\]
Hence $c=1$ or $c=-1$.

If $u=1$, then
\[
\varphi^2=t_{2a},
\]
so $\varphi$ is a nontrivial involution exactly when
\[
0\ne a\in E[2].
\]

If $u=-1$, then
\[
\varphi(x)=a-x=\sigma_a(x),
\]
and
\[
\sigma_a^2(x)=a-(a-x)=x
\]
for every $a\in E$.
:::

<1>3. A nontrivial translation involution $t_a$, with $a\in E[2]\setminus\{0\}$, has no fixed points, and its quotient is again an elliptic curve.
::: {.proof}
A fixed point would satisfy
\[
x+a=x,
\]
which forces $a=0$, contrary to the hypothesis.  Thus the quotient map
\[
E\longrightarrow E/\langle t_a\rangle
\]
is an unramified double cover.

If the quotient has genus $g'$, Riemann--Hurwitz gives
\[
2g(E)-2
=2(2g'-2).
\]
Since $g(E)=1$, this is
\[
0=2(2g'-2),
\]
so $g'=1$.  The quotient is therefore another elliptic curve; equivalently, this quotient map is a degree-two isogeny.
:::

<1>4. The involution
\[
\sigma_a(x)=a-x
\]
has exactly four fixed points, namely the four solutions of
\[
2x=a.
\]
::: {.proof}
The fixed-point equation is
\[
a-x=x,
\]
equivalently $2x=a$.  Multiplication by $2$,
\[
[2]:E\longrightarrow E,
\]
is surjective over $\mathbb C$ and has kernel
\[
E[2]\cong(\mathbb Z/2\mathbb Z)^2,
\]
which has four elements.  Thus every fibre of $[2]$ has four points, so $2x=a$ has exactly four solutions.
:::

<1>5. The quotient
\[
E/\langle\sigma_a\rangle
\]
has genus $0$ and hence is isomorphic to $\mathbb{CP}^1$.
::: {.proof}
The quotient map has degree $2$.  By <1>4 it is simply ramified at four points, so the total ramification contribution in Riemann--Hurwitz is $4$.  If the quotient has genus $g'$, then
\[
2g(E)-2
=2(2g'-2)+4.
\]
Since $g(E)=1$,
\[
0=2(2g'-2)+4=4g',
\]
hence $g'=0$.  Every compact Riemann surface of genus $0$ is biholomorphic to the Riemann sphere
\[
\widehat{\mathbb C}=\mathbb{CP}^1.
\]
:::

<1>6. The quotient in <1>5 can also be identified explicitly with $\mathbb{CP}^1$.
::: {.proof}
Choose $b\in E$ with
\[
2b=a.
\]
Then translation by $b$ conjugates $\sigma_a$ to the standard negation involution:
\[
t_{-b}\circ\sigma_a\circ t_b(x)
=a-x-2b
=-x.
\]
Thus it is enough to identify
\[
E/\{\pm1\}.
\]

Put $E$ in a Weierstrass form
\[
y^2=4x^3-g_2x-g_3.
\]
The group inverse is
\[
(x,y)\longmapsto(x,-y).
\]
The $x$-coordinate therefore defines a degree-two map
\[
E\longrightarrow\mathbb{CP}^1
\]
whose generic fibre is the pair
\[
\{(x,y),(x,-y)\}.
\]
Hence its fibres are precisely the orbits of the involution, so it is the quotient map
\[
E\longrightarrow E/\{\pm1\}\cong\mathbb{CP}^1.
\]
Its four branch points are the four fixed points $E[2]$ of negation.
:::

<1>7. Q.E.D.
::: {.proof}
Step <1>2 classifies the involutions, steps <1>3 and <1>4 identify their fixed-point behaviour, and steps <1>5--<1>6 identify the quotient arising from the fixed-point involution with $\mathbb{CP}^1$.
:::
:::
