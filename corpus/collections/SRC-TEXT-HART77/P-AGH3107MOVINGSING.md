---
schema: qual/card@1
id: P-AGH3107MOVINGSING
kind: problem
title: Serre's linear system with moving singularities
classification:
  areas:
  - algebraic-geometry
  topics:
  - Smooth Morphisms
  - Linear Systems
  - Bertini's Theorem
  - Inseparable Morphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.10.7 in the Hartshorne transcription and two independent
    solution transcriptions. Direct factorization shows that the printed
    two-case classification in part (b) omits a third family: when the unique
    singular point lies on an F_2-line but is not F_2-rational, the cubic is
    that line plus a smooth conic tangent at the singular point. The proof
    below records and proves the corrected three-case classification while
    retaining the valid dimension, inseparability, singularity, and bijection
    assertions.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $k$ be an algebraically closed field of characteristic $2$. Let $P_1, \ldots, P_7 \in \PP_k^2$ be the seven points of the projective plane over the prime field $\FF_2 \subseteq k$. Let $D$ be the linear system of all cubic curves in $X = \PP_k^2$ passing through $P_1, \ldots, P_7$.

a. Show that $D$ is a linear system of dimension $2$ with base points $P_1, \ldots, P_7$, which determines an inseparable morphism of degree $2$ from $X - \theset{P_i}$ to $\PP^2$.

b. Show that every curve $C \in D$ is singular.

    More precisely, either $C$ consists of $3$ lines all passing through one of the $P_i$, or $C$ is an irreducible cuspidal cubic with cusp $P$ distinct from every $P_i$.

Furthermore, the correspondence sending $C$ to the singular point of $C$ is a bijection between $D$ and $\PP^2$. Thus the singular points of elements of $D$ move all over.
:::

::: {.remark title="Erratum to the printed classification in part (b)"}
The assertion that the only reducible members are three concurrent lines is
false over an algebraically closed field strictly larger than $\FF_2$.
For example, if $\lambda\in k\setminus\FF_2$, then
$$
xz(x+z)+\lambda yz(y+z)
=z\bigl(x(x+z)+\lambda y(y+z)\bigr)
$$
is a member of $D$ consisting of the line $z=0$ and a smooth conic tangent to
it at the unique singular point.

The correct classification is:

1. if the singular point is one of the seven $\FF_2$-points, the cubic is the
   union of the three $\FF_2$-lines through that point;
2. if the singular point lies on one of the seven $\FF_2$-lines but is not an
   $\FF_2$-point, the cubic is that line plus a smooth irreducible conic
   tangent to it at the singular point;
3. if the singular point lies on none of the seven $\FF_2$-lines, the cubic is
   irreducible and cuspidal.

The claims that every member is singular and that its unique singular point
gives a bijection $D(k)\leftrightarrow\PP^2(k)$ remain correct.
:::

::: {.solution}
Put
$$
F_0=xy(x+y),
\qquad
F_1=xz(x+z),
\qquad
F_2=yz(y+z).
$$

::: pf

::: {.pf-step #s1}

The vector space of cubic forms vanishing at all seven points of $\PP^2(\FF_2)$ has basis $F_0,F_1,F_2$.

::: pf-proof

Write a general homogeneous cubic as
$$
\begin{aligned}
F={}&a x^3+b y^3+c z^3+d x^2y+e x^2z+fxy^2\\
&+g y^2z+h xz^2+i yz^2+jxyz.
\end{aligned}
$$
Vanishing at the three coordinate points gives
$$
a=b=c=0.
$$
Vanishing at
$$
[1:1:0],\quad[1:0:1],\quad[0:1:1]
$$
gives
$$
d=f,\qquad e=h,\qquad g=i.
$$
Finally, evaluating at $[1:1:1]$ gives
$$
j=0,
$$
because the other six mixed terms occur in equal pairs and
$\operatorname{char}k=2$.
Thus
$$
F=dF_0+eF_1+gF_2.
$$
The three displayed forms are visibly linearly independent, so they form a
basis.

Hence the projective linear system is
$$
D=\PP\langle F_0,F_1,F_2\rangle\cong\PP^2,
$$
and therefore
$$
\boxed{\dim D=2}.
$$

:::

:::

::: {.pf-step #s2}

The base locus of $D$ is exactly the seven points $\PP^2(\FF_2)$.

::: pf-proof

A point $[x:y:z]$ is in the base locus exactly when
$$
xy(x+y)=xz(x+z)=yz(y+z)=0.
$$
For every pair of coordinates this says that either one coordinate is zero or
the two are equal. Thus all nonzero coordinates of the point are equal.
After projective rescaling they are all equal to $1$.

Therefore every base point has homogeneous coordinates with entries in
$\{0,1\}$, not all zero. These are exactly the seven points of
$\PP^2(\FF_2)$. Conversely each such point plainly annihilates all three
$F_i$.

:::

:::

::: {.pf-step #s3}

The linear system defines on the complement of the base locus the morphism
$$
\varphi:\PP^2\setminus\PP^2(\FF_2)\longrightarrow\PP^2,
\qquad
[x:y:z]\longmapsto[F_2:F_1:F_0].
$$

::: pf-proof

Step [](#s2){.pf-ref} says precisely that $F_0,F_1,F_2$ do not vanish simultaneously on
the displayed open subset, so the three sections define a morphism there.
The reversal of the coordinate order is only a projective automorphism of the
target and is convenient for the calculation below.

:::

:::

::: {.pf-step #s4}

Geometrically, $\varphi(P)$ is the line through $P$ and its Frobenius image $P^{(2)}$.

::: pf-proof

For
$$
P=[x:y:z],
\qquad
P^{(2)}=[x^2:y^2:z^2],
$$
the cross product of the two coordinate vectors is
$$
\begin{aligned}
P\times P^{(2)}
&=[yz^2-zy^2:\;zx^2-xz^2:\;xy^2-yx^2]\\
&=[yz(y+z):\;xz(x+z):\;xy(x+y)]\\
&=[F_2:F_1:F_0],
\end{aligned}
$$
where minus equals plus in characteristic $2$.
Thus these are the coefficients of the unique line through $P$ and
$P^{(2)}$.

The cross product vanishes exactly when $P=P^{(2)}$ projectively, i.e. at the
seven $\FF_2$-points, which are precisely the deleted base points.

:::

:::

::: {.pf-step #s5}

The morphism $\varphi$ is generically finite, purely inseparable, and of degree $2$.

::: pf-proof

Let
$$
K=k(A,B)
$$
be the function field of the target chart consisting of lines
$$
L_{A,B}: AX+BY+Z=0.
$$
By step [](#s4){.pf-ref}, a point $[x:y:z]$ in the generic fibre lies both on $L_{A,B}$
and, after Frobenius, on the same line. Hence
$$
Ax+By+z=0,
\qquad
Ax^2+By^2+z^2=0.
$$
Substitute
$$
z=Ax+By.
$$
On the chart $y\ne0$, put $r=x/y$. The second equation becomes
$$
(A+A^2)r^2+(B+B^2)=0,
$$
so
$$
r^2=\frac{B+B^2}{A+A^2}.
$$
The right-hand side is not a square in $K$: at the prime divisor $B=0$ it
has valuation $1$, while a square has even valuation. Therefore
$$
T^2-\frac{B+B^2}{A+A^2}
$$
is irreducible and purely inseparable over $K$.

Conversely $r$ determines the generic source point by
$$
[x:y:z]=[r:1:Ar+B].
$$
Hence the induced extension of function fields has degree two and is purely
inseparable. Thus
$$
\boxed{\deg\varphi=2,\qquad\varphi\text{ inseparable}.}
$$
This proves part (a).

:::

:::

::: {.pf-step #s6}

Every member of $D$ has a unique singular point, and this gives a bijection
$$
D(k)\xrightarrow{\sim}\PP^2(k).
$$

::: pf-proof

Write a member as
$$
C_{a,b,c}=V(G_{a,b,c}),
$$
where
$$
G_{a,b,c}
=aF_0+bF_1+cF_2.
$$
In characteristic $2$ its partial derivatives are
$$
\frac{\partial G}{\partial x}=a y^2+b z^2,
$$
$$
\frac{\partial G}{\partial y}=a x^2+c z^2,
$$
$$
\frac{\partial G}{\partial z}=b x^2+c y^2.
$$
For $[a:b:c]\ne[0:0:0]$ the coefficient matrix of these three equations in
$x^2,y^2,z^2$ has rank two. Its kernel is generated by
$$
[c:b:a].
$$
Because $k$ is algebraically closed of characteristic $2$, Frobenius
$$
k\longrightarrow k,
\qquad
u\longmapsto u^2
$$
is bijective. Hence there is a unique projective point
$$
P_{a,b,c}=[\sqrt c:\sqrt b:\sqrt a]
$$
at which all three partial derivatives vanish.

Euler's identity for a cubic gives
$$
xG_x+yG_y+zG_z=3G=G
$$
in characteristic $2$. Thus $G(P_{a,b,c})=0$, so this point is indeed a
singular point of $C_{a,b,c}$.

The assignment
$$
[a:b:c]\longmapsto[\sqrt c:\sqrt b:\sqrt a]
$$
is a bijection on $k$-points: coordinate reversal is an automorphism and the
inverse of Frobenius is a bijection of the algebraically closed field $k$.
Therefore every member is singular at exactly one point, and
$$
\boxed{D(k)\leftrightarrow\PP^2(k)}
$$
by its singular point.

:::

:::

::: {.pf-step #s7}

For an $\FF_2$-line $L$, the member $C_{a,b,c}$ contains $L$ if and only if its singular point $P_{a,b,c}$ lies on $L$.

::: pf-proof

The group $\PGL_3(\FF_2)$ preserves the set of seven base points and acts
transitively on the seven $\FF_2$-lines. It therefore suffices to treat the
line
$$
L=V(z).
$$
Restricting $G_{a,b,c}$ to $z=0$ gives
$$
G_{a,b,c}(x,y,0)=a,xy(x+y).
$$
Thus $z$ divides $G_{a,b,c}$ exactly when $a=0$.
On the other hand
$$
P_{a,b,c}=[\sqrt c:\sqrt b:\sqrt a]
$$
lies on $z=0$ exactly when $a=0$.
This proves the equivalence for $z=0$, and equivariance under
$\PGL_3(\FF_2)$ proves it for every $\FF_2$-line.

:::

:::

::: {.pf-step #s8}

If the singular point is one of the seven base points, the cubic is the union of the three $\FF_2$-lines through that point.

::: pf-proof

Let $P=P_{a,b,c}\in\PP^2(\FF_2)$. Exactly three $\FF_2$-lines pass through
$P$. By step [](#s7){.pf-ref} each of their linear equations divides $G_{a,b,c}$.
Their product already has degree three, so, up to a nonzero scalar,
$$
G_{a,b,c}=L_1L_2L_3.
$$
Hence $C_{a,b,c}$ is precisely the union of those three concurrent lines.

:::

:::

::: {.pf-step #s9}

If the singular point lies on an $\FF_2$-line but is not an $\FF_2$-point, the cubic is that line plus a smooth irreducible conic tangent to it at the singular point.

::: pf-proof

Such a point $P$ lies on exactly one $\FF_2$-line: two distinct
$\FF_2$-lines intersect in an $\FF_2$-point. By step [](#s7){.pf-ref} the equation has
exactly one $\FF_2$-linear factor, say
$$
G=LQ,
$$
where $Q$ has degree two.

Suppose $Q$ were reducible. Then over the algebraically closed field $k$ the
cubic would be a product of three lines, counted with multiplicity. A repeated
line would make the singular locus positive-dimensional in characteristic
$2$, contrary to the uniqueness proved in step [](#s6){.pf-ref}. Thus the three lines
would be distinct. Since their union has only one singular point, they would
all have to pass through $P$.

But a non-$\FF_2$ line contains at most one $\FF_2$-point, since two distinct
$\FF_2$-points determine an $\FF_2$-line. Because $P$ is not an
$\FF_2$-point, at most one of three concurrent lines through $P$ can be an
$\FF_2$-line. Their union would therefore contain at most
$$
3+1+1=5
$$
of the seven base points, contradiction.

Hence $Q$ is irreducible. An irreducible conic over an algebraically closed
field is smooth. The line $L$ and conic $Q$ can meet only at singular points
of their union, and step [](#s6){.pf-ref} says there is only $P$. Bézout's theorem gives
$$
I_P(L,Q)=2,
$$
so $L$ is tangent to $Q$ at $P$.

:::

:::

::: {.pf-step #s10}

If the singular point lies on none of the seven $\FF_2$-lines, the cubic is irreducible.

::: pf-proof

Suppose $G= LQ$ with $L$ linear and $Q$ quadratic.
By step [](#s7){.pf-ref}, $L$ cannot be an $\FF_2$-line. Therefore $L$ contains at most
one of the seven $\FF_2$-points, so $Q$ must contain at least six of them.

We claim that no nonzero conic contains six of the seven points of
$\PP^2(\FF_2)$. The group $\PGL_3(\FF_2)$ is transitive on the seven points,
so assume the omitted point is $[1:0:0]$. Write
$$
Q=A x^2+B y^2+C z^2+Dxy+Exz+Fyz.
$$
Vanishing at
$$
[0:1:0],\ [0:0:1],\ [1:1:0],\ [1:0:1],\ [0:1:1],\ [1:1:1]
$$
gives successively
$$
B=C=0,
\qquad
D=E=A,
\qquad
F=0,
\qquad
A+D+E=A=0.
$$
Thus all coefficients vanish, contradiction.

So $G$ has no linear factor. Every reducible cubic over an algebraically
closed field has a linear factor, hence $C_{a,b,c}$ is irreducible.

:::

:::

::: {.pf-step #s11}

In the situation of step [](#s10){.pf-ref}, the unique singularity is a cusp.

::: pf-proof

Let
$$
P=[r:s:t]=[\sqrt c:\sqrt b:\sqrt a]
$$
be the singular point. Translate locally by
$$
x=r+X,
\qquad
y=s+Y,
\qquad
z=t+Z.
$$
Because all first derivatives vanish at $P$, the tangent cone is the quadratic
part of the expansion. Directly from the three summands of $G$ it is
$$
Q_2
=(as+bt)X^2+(ar+ct)Y^2+(br+cs)Z^2.
$$
Over the algebraically closed field $k$ this is the square of a linear form.

The quadratic part is not zero. If it vanished, the cubic would have
multiplicity three at $P$; a plane cubic of multiplicity three at a point is a
product of three lines through that point over an algebraically closed field,
contradicting irreducibility from step [](#s10){.pf-ref}.

Thus $P$ is a double point with a repeated tangent line. An irreducible
singular plane cubic has arithmetic genus one and normalization genus zero, so
its unique double point has $\delta=1$. A double point with $\delta=1$ and a
repeated tangent is a cusp rather than a node [[D-CRVPLSING]]. Hence
$C_{a,b,c}$ is an irreducible cuspidal cubic with cusp $P$.

:::

:::

::: pf-qed

for the corrected statement.

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove part (a). Step [](#s6){.pf-ref} proves that every member is
singular and that the singular-point correspondence is a bijection with
$\PP^2(k)$. Steps [](#s7){.pf-ref}, [](#s8){.pf-ref}, [](#s9){.pf-ref}, [](#s10){.pf-ref} and [](#s11){.pf-ref} prove the corrected three-case classification
recorded in the erratum above, and in particular show that the singular points
move over all of $\PP^2$.

:::

:::

:::
