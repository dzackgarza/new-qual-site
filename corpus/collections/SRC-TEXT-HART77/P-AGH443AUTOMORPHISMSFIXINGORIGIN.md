---
schema: qual/card@1
id: P-AGH443AUTOMORPHISMSFIXINGORIGIN
kind: problem
title: Automorphisms of $(X,P_0)$ come from affine substitutions $x'=ax+b$, $y'=cy$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Embeddings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.3 together with Lemma IV.4.4, Lemma IV.4.5,
    Theorem IV.4.6, and Corollary IV.4.7. The explicit projective lifts below
    were checked directly against the Legendre equation in all four cases,
    including the characteristic-three order-twelve case.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let the elliptic curve $X$ be embedded in $\PP^2$ so as to have the equation $y^2=x(x-1)(x-\lambda)$.
Show that any automorphism of $X$ leaving $P_0=(0,1,0)$ fixed is induced by an automorphism of $\PP^2$ coming from the automorphism of the affine $(x, y)$-plane given by
$$
\begin{cases}
x' = a x+b \\
y' = c y .
\end{cases}
$$
In each of the four cases of (4.7), describe these automorphisms of $\PP^2$ explicitly, and hence determine the structure of the group $G=\Aut(X, P_0)$.
:::

::: {.solution}
Put
$$
f(x)=x(x-1)(x-\lambda),
$$
so on the affine chart $z=1$ the curve is
$$
y^2=f(x),
$$
and
$$
P_0=[0:1:0]
$$
is the unique point at infinity.

<1>1. At $P_0$ the functions $x$ and $y$ have poles of orders $2$ and $3$,
respectively, and
$$
L(2P_0)=\langle1,x\rangle,
\qquad
L(3P_0)=\langle1,x,y\rangle.
$$

::: {.proof}
The projective equation is
$$
Y^2Z=X(X-Z)(X-\lambda Z).
$$
The line at infinity $Z=0$ meets $X$ only at $P_0$, with intersection
multiplicity $3$.  Hence the affine functions $x=X/Z$ and $y=Y/Z$ have no
poles away from $P_0$.  The equation shows that their pole orders satisfy
$$
2\operatorname{ord}_{P_0}(y)
=
3\operatorname{ord}_{P_0}(x),
$$
and the morphism
$$
x:X\longrightarrow\PP^1
$$
has degree $2$, so
$$
\operatorname{ord}_{P_0}(x)=-2,
\qquad
\operatorname{ord}_{P_0}(y)=-3.
$$

Since $g(X)=1$, Riemann--Roch gives
$$
\ell(nP_0)=n
$$
for every $n\ge1$.  The displayed functions therefore give bases of the
two spaces.
:::

<1>2. If
$$
\sigma\in G=\Aut(X,P_0),
$$
then for some
$$
a,c\in k^\times,
\qquad
b,d,e\in k,
$$
one has
$$
\sigma^*x=ax+b,
\qquad
\sigma^*y=cy+dx+e.
$$

::: {.proof}
Because $\sigma$ fixes $P_0$, pullback preserves the filtration by pole order
at $P_0$.  Step <1>1 therefore gives
$$
\sigma^*x\in L(2P_0)=\langle1,x\rangle.
$$
Its pole order is still exactly $2$, so the coefficient of $x$ is nonzero:
$$
\sigma^*x=ax+b,
\qquad a\ne0.
$$
Likewise
$$
\sigma^*y\in L(3P_0)=\langle1,x,y\rangle,
$$
and exact pole order $3$ forces the coefficient of $y$ to be nonzero.  This
gives the asserted form.
:::

<1>3. In fact
$$
\boxed{
\sigma^*x=ax+b,
\qquad
\sigma^*y=cy
}
$$
with $a,c\ne0$.

::: {.proof}
Apply $\sigma^*$ to the equation $y^2=f(x)$.  Using step <1>2 gives
$$
(cy+dx+e)^2=f(ax+b).
$$
The right-hand side belongs to $k(x)$.  Since
$$
k(X)=k(x)\oplus k(x)y
$$
as a vector space over $k(x)$, comparison of the coefficient of $y$ gives
$$
2c(dx+e)=0.
$$
Here $c\ne0$ and $\operatorname{char}k\ne2$, hence
$$
d=e=0.
$$
:::

<1>4. Every $\sigma\in G$ is induced by the projective linear automorphism
$$
[X:Y:Z]
\longmapsto
[aX+bZ:cY:Z].
$$
Conversely, this transformation preserves $X$ precisely when
$$
\tau(x)=ax+b
$$
permutes the set
$$
\{0,1,\lambda\}
$$
and
$$
c^2=a^3.
$$

::: {.proof}
The displayed projective map is invertible because $a,c\ne0$, and on the
chart $Z=1$ it is exactly
$$
(x,y)\longmapsto(ax+b,cy).
$$
It also fixes $P_0$.

It preserves the equation if and only if
$$
c^2f(x)=f(ax+b).
$$
The roots of the left side are $0,1,\lambda$, so this identity forces the
affine map $\tau(x)=ax+b$ to permute those three points.  Conversely, if
$\tau$ permutes them, then both sides are cubic polynomials with the same
three roots.  Comparing leading coefficients gives
$$
f(ax+b)=a^3f(x),
$$
so the equality is equivalent to $c^2=a^3$.

Since $k$ is algebraically closed and $\operatorname{char}k\ne2$, there are
exactly two choices of $c$ for each admissible $\tau$, differing by the
involution
$$
\iota:(x,y)\longmapsto(x,-y).
$$
:::

<1>5. If
$$
j(X)\ne0,1728,
$$
then
$$
\boxed{G\cong\ZZ/2}
$$
and
$$
G=\{1,\iota\}.
$$

::: {.proof}
Corollary IV.4.7 says that in this case no nonidentity affine automorphism of
$\PP^1$ fixing $\infty$ permutes the three finite branch points
$0,1,\lambda$.  Thus step <1>4 leaves only the two lifts of the identity on
the $x$-line, namely
$$
(x,y)\longmapsto(x,y)
\qquad\text{and}\qquad
(x,y)\longmapsto(x,-y).
$$
The second has order $2$.
:::

<1>6. Suppose
$$
j(X)=1728,
\qquad
\operatorname{char}k\ne3.
$$
Then
$$
\boxed{G\cong\ZZ/4}.
$$

::: {.proof}
By Corollary IV.4.7 one has
$$
\lambda\in\left\{-1,2,\frac12\right\}.
$$
In the three respective cases, the nontrivial affine symmetry of the finite
branch set is
$$
\tau(x)=
\begin{cases}
-x,&\lambda=-1,\\
2-x,&\lambda=2,\\
1-x,&\lambda=\frac12.
\end{cases}
$$
In every case its linear coefficient is $a=-1$.  Choose
$$
i\in k,
\qquad
i^2=-1.
$$
Then step <1>4 gives a lift
$$
g:(x,y)\longmapsto(\tau(x),iy),
$$
induced on $\PP^2$ by
$$
[X:Y:Z]\longmapsto
\begin{cases}
[-X:iY:Z],&\lambda=-1,\\
[-X+2Z:iY:Z],&\lambda=2,\\
[-X+Z:iY:Z],&\lambda=\frac12.
\end{cases}
$$
Now
$$
g^2=\iota,
$$
so $g$ has order $4$.  Corollary IV.4.7 gives $|G|=4$, hence
$$
G=\langle g\rangle\cong\ZZ/4.
$$
:::

<1>7. Suppose
$$
j(X)=0,
\qquad
\operatorname{char}k\ne3.
$$
Then
$$
\boxed{G\cong\ZZ/6}.
$$

::: {.proof}
Choose a primitive cube root of unity
$$
\omega^3=1,
\qquad
\omega\ne1.
$$
Corollary IV.4.7 gives
$$
\lambda=-\omega
\qquad\text{or}\qquad
\lambda=-\omega^2.
$$
The affine map cycling the three branch points is respectively
$$
\tau(x)=
\begin{cases}
\omega^2x+1,&\lambda=-\omega,\\
\omega x+1,&\lambda=-\omega^2.
\end{cases}
$$
Indeed, in either case
$$
0\longmapsto1\longmapsto\lambda\longmapsto0.
$$
Its coefficient $a$ satisfies $a^3=1$, so step <1>4 gives the order-$3$
lift
$$
r:(x,y)\longmapsto(\tau(x),y).
$$
On $\PP^2$ this is
$$
[X:Y:Z]\longmapsto
\begin{cases}
[\omega^2X+Z:Y:Z],&\lambda=-\omega,\\
[\omega X+Z:Y:Z],&\lambda=-\omega^2.
\end{cases}
$$
The involution $\iota$ commutes with $r$, and
$$
\langle r\rangle\cap\langle\iota\rangle=1.
$$
Thus
$$
\langle r,\iota\rangle
\cong
\ZZ/3\times\ZZ/2
\cong
\ZZ/6.
$$
Corollary IV.4.7 gives $|G|=6$, so this subgroup is all of $G$.
:::

<1>8. Finally suppose
$$
\operatorname{char}k=3,
\qquad
j(X)=0=1728.
$$
Then, after taking
$$
\lambda=-1,
$$
one has
$$
\boxed{
G\cong(\ZZ/3)\rtimes(\ZZ/4),
}
$$
where a generator of $\ZZ/4$ acts on $\ZZ/3$ by inversion.

::: {.proof}
In characteristic $3$ the branch set is
$$
\{0,1,-1\}=\FF_3.
$$
Its full affine symmetry group consists of
$$
x\longmapsto ax+b,
\qquad
a\in\{1,-1\},
\quad
b\in\FF_3,
$$
and has order $6$.

Let
$$
r:(x,y)\longmapsto(x+1,y).
$$
Since
$$
(x+1)^3-(x+1)=x^3-x
$$
in characteristic $3$, this preserves
$$
y^2=x^3-x
$$
and has order $3$.  On projective coordinates,
$$
r:[X:Y:Z]\longmapsto[X+Z:Y:Z].
$$

Choose $i\in k$ with $i^2=-1$ and put
$$
s:(x,y)\longmapsto(-x,iy).
$$
This is induced by
$$
s:[X:Y:Z]\longmapsto[-X:iY:Z].
$$
Step <1>4 shows that it preserves $X$, and
$$
s^2=\iota,
$$
so $s$ has order $4$.  On the $x$-line, reflection conjugates translation
by $1$ to translation by $-1$, hence
$$
srs^{-1}=r^{-1}.
$$
Therefore
$$
\langle r,s\rangle
=
\left\langle
r,s\mid r^3=s^4=1,\ srs^{-1}=r^{-1}
\right\rangle
\cong
(\ZZ/3)\rtimes(\ZZ/4).
$$
It has $12$ elements, represented uniquely by
$$
r^a s^b,
\qquad
0\le a<3,
\quad
0\le b<4.
$$
Corollary IV.4.7 gives $|G|=12$, so this is the full automorphism group.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 prove that every automorphism fixing $P_0$ is induced by a
projective transformation of the required form.  Steps <1>5--<1>8 give the
explicit transformations and the group structure in each of the four cases
of Corollary IV.4.7.
:::
:::
