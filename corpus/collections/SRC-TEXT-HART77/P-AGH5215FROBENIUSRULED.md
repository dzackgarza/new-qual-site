---
schema: qual/card@1
id: P-AGH5215FROBENIUSRULED
kind: problem
title: A ruled surface in characteristic 3 with a nonample divisor satisfying the numerical criterion
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
    Read Hartshorne V.2.15, the retained Egbert companion calculation, the
    earlier characteristic-three quartic computation, the purely inseparable
    curve theorem, and the ruled-surface intersection formulas. Parts (a) and
    (b) admit a direct cohomological proof. In part (c), Frobenius pullback of
    the extension splits and produces an integral degree-three purely
    inseparable multisection of class 3C_0-3f. The printed adjective
    "nonsingular" is incompatible with adjunction: this class has arithmetic
    genus 4, while its normalization is the genus-3 quartic C. The proof below
    records and proves the corrected statement.
- event: source-corrected
  by: chatgpt
  date: 2026-09-19
  note: >-
    Part (c)'s "nonsingular curve" is corrected by an erratum to "integral
    curve whose normalization is C"; adjunction gives p_a(Y)=4 whereas the
    normalization has genus 3.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
---

::: {.problem}
Let $C$ be the plane curve $x^3 y+y^3 z+z^3 x=0$ over a field $k$ of characteristic 3 (V, Ex. 2.4).

a. Show that the action of the $k$-linear Frobenius morphism $f$ on $H^1\left(C, \mathcal{O}_C\right)$ is identically 0 (Cf. (V, 4.21)).

b. Fix a point $P \in C$, and show that there is a nonzero $\xi \in H^1(\mathcal{L}(-P))$ such that $f^* \xi=0$ in $H^1(\mathcal{L}(-3 P))$.

c. Now let $\mathcal{E}$ be defined by $\xi$ as an extension
\[
0 \rightarrow \mathcal{O}_C \rightarrow \mathcal{E} \rightarrow \mathcal{L}(P) \rightarrow 0,
\]
and let $X$ be the corresponding ruled surface over $C$. Show that $X$ contains a nonsingular curve $Y \equiv 3 C_0-3 f$, such that $\pi: Y \rightarrow C$ is purely inseparable.

    Show that the divisor $D=2 C_0$ satisfies the hypotheses of (2.21.b), but is not ample.
:::

::: {.remark title="Erratum to part (c)"}
The curve of class
$$
3C_0-3f
$$
constructed from the Frobenius-split extension is **not nonsingular**.  The
correct conclusion is that there is an integral curve $Y$ of this class whose
normalization is $C$, and for which
$$
\pi|_Y:Y\longrightarrow C
$$
is purely inseparable of degree $3$.

Indeed, the proof below gives $e=-1$ and $g(C)=3$, so
$$
K_X\equiv-2C_0+5f.
$$
Adjunction then gives
$$
2p_a(Y)-2
=(3C_0-3f)\cdot(C_0+2f)
=6,
$$
hence
$$
p_a(Y)=4.
$$
But the normalization is the genus-$3$ curve $C$. Thus $Y$ has total
$\delta$-invariant $1$ and cannot be nonsingular.
:::

::: {.solution}
As in Hartshorne's notation, write
$$
\mathcal L(A)=\OO_C(A)
$$
for the invertible sheaf associated to a divisor $A$ on $C$.

Write
$$
F=x^3y+y^3z+z^3x.
$$
By [[P-AGH424FUNNYQUARTIC]], the plane quartic
$$
C=V(F)\subseteq\PP^2
$$
is nonsingular; hence it has genus $3$.

<1>1. There is a natural identification
$$
H^1(C,\OO_C)\cong H^2(\PP^2,\OO_{\PP^2}(-4)).
$$

::: {.proof}
The quartic equation gives
$$
0
\longrightarrow
\OO_{\PP^2}(-4)
\xrightarrow{\cdot F}
\OO_{\PP^2}
\longrightarrow
\OO_C
\longrightarrow0.
$$
Since
$$
H^1(\PP^2,\OO_{\PP^2})=0
\qquad\text{and}\qquad
H^2(\PP^2,\OO_{\PP^2})=0,
$$
the connecting map in cohomology is the displayed isomorphism.
:::

<1>2. Under the identification in step <1>1, Frobenius on
$H^1(C,\OO_C)$ is represented by
$$
\alpha\longmapsto F^2\alpha^3
$$
on $H^2(\PP^2,\OO_{\PP^2}(-4))$.

::: {.proof}
Pulling the quartic sequence of step <1>1 back by the characteristic-$3$
Frobenius changes
$$
\OO_{\PP^2}(-4)
$$
to
$$
\OO_{\PP^2}(-12)
$$
and sends a cohomology class $\alpha$ to $\alpha^3$.  The Frobenius-thickened
quartic is cut out by $F^3$, and $C$ is a closed subscheme of that
thickening. The induced restriction from the thickening to $C$ is represented
on the left terms by multiplication by
$$
F^{3-1}=F^2.
$$
Naturality of the connecting homomorphism therefore gives exactly
$$
\alpha\longmapsto F^2\alpha^3.
$$
:::

<1>3. The Frobenius action on
$$
H^1(C,\OO_C)
$$
is identically zero.

::: {.proof}
Using the standard Cech cover of $\PP^2$, a basis of
$$
H^2(\PP^2,\OO_{\PP^2}(-4))
$$
is represented by
$$
\frac1{x^2yz},
\qquad
\frac1{xy^2z},
\qquad
\frac1{xyz^2}.
$$
A Laurent monomial represents zero in this top Cech cohomology as soon as
one of the exponents of $x,y,z$ is nonnegative.

For example, cubing the first basis vector gives
$$
x^{-6}y^{-3}z^{-3}.
$$
Every monomial of
$$
F^2=(x^3y+y^3z+z^3x)^2
$$
makes at least one exponent nonnegative after multiplication by this Laurent
monomial. Explicitly the six monomial types are
$$
x^6y^2,
\quad
y^6z^2,
\quad
z^6x^2,
\quad
x^3y^4z,
\quad
x^4yz^3,
\quad
xy^3z^4,
$$
and multiplication gives respectively an $x$-, $y$-, $z$-, $y$-, $z$-, or
$y$-exponent at least zero. Hence
$$
F^2(x^{-6}y^{-3}z^{-3})=0
$$
in $H^2(\PP^2,\OO(-4))$.

The other two basis vectors are obtained by cyclic permutation, and $F$ is
cyclically symmetric. Their images vanish as well. Step <1>2 therefore shows
that Frobenius acts as zero on $H^1(C,\OO_C)$. This proves part (a).
:::

<1>4. For every point $P\in C$, the natural map
$$
H^1(C,\OO_C(-P))
\longrightarrow
H^1(C,\OO_C)
$$
is an isomorphism, while
$$
\ker\left(
H^1(C,\OO_C(-3P))
\longrightarrow
H^1(C,\OO_C)
\right)
$$
has dimension $2$.

::: {.proof}
From
$$
0\to\OO_C(-P)\to\OO_C\to\OO_P\to0,
$$
the map
$$
H^0(C,\OO_C)\longrightarrow H^0(P,\OO_P)
$$
is an isomorphism. Hence the induced map on $H^1$ is an isomorphism.

For $3P$, Riemann--Roch gives
$$
h^1(C,\OO_C(-3P))=5,
$$
because the line bundle has negative degree and genus $3$. Also
$$
h^1(C,\OO_C)=3.
$$
The exact sequence
$$
0\to\OO_C(-3P)\to\OO_C\to\OO_{3P}\to0
$$
shows that the map on $H^1$ is surjective. Its kernel therefore has
dimension
$$
5-3=2.
$$
:::

<1>5. There exists
$$
0\ne\xi\in H^1(C,\OO_C(-P))
$$
such that
$$
f^*\xi=0
\quad\text{in}\quad
H^1(C,\OO_C(-3P)).
$$

::: {.proof}
Frobenius pullback gives a commutative square
$$
\begin{CD}
H^1(C,\OO_C(-P)) @>>> H^1(C,\OO_C)\\
@V{f^*}VV @VV{f^*}V\\
H^1(C,\OO_C(-3P)) @>>> H^1(C,\OO_C).
\end{CD}
$$
The right vertical arrow is zero by step <1>3. Thus the image of the left
vertical arrow is contained in the two-dimensional kernel identified in
step <1>4.

But the source has dimension
$$
h^1(C,\OO_C(-P))=h^1(C,\OO_C)=3.
$$
Hence the left vertical map has nonzero kernel. Choose
$$
0\ne\xi
$$
in that kernel. This proves part (b).
:::

<1>6. Let $\mathcal E$ be the extension determined by $\xi$:
$$
0
\longrightarrow
\OO_C
\longrightarrow
\mathcal E
\longrightarrow
\OO_C(P)
\longrightarrow0.
$$
Then $\mathcal E$ is normalized and the ruled surface
$$
X=\PP(\mathcal E)
$$
has invariant
$$
\boxed{e=-1}.
$$

::: {.proof}
The inclusion of $\OO_C$ gives a nonzero global section of $\mathcal E$.
Let $M$ be a line bundle of negative degree.

If $\deg M\le-2$, then both $M$ and $M(P)$ have negative degree, so the
twisted extension has no global sections.

If $\deg M=-1$ and $M\not\cong\OO_C(-P)$, then $M(P)$ is a nontrivial
degree-zero line bundle and again has no global sections. Finally, for
$$
M=\OO_C(-P),
$$
the connecting map
$$
H^0(C,\OO_C)\longrightarrow H^1(C,\OO_C(-P))
$$
in the twisted extension sends $1$ to the extension class $\xi$, which is
nonzero. Thus the quotient section of the twisted sequence does not lift,
and
$$
H^0(C,\mathcal E(-P))=0.
$$
Therefore $\mathcal E$ is normalized.

Since
$$
\det\mathcal E\cong\OO_C(P),
$$
one has
$$
e=-\deg\det\mathcal E=-1.
$$
The quotient
$$
\mathcal E\twoheadrightarrow\OO_C(P)
$$
defines the normalized section $C_0$, and
$$
C_0^2=-e=1.
$$
:::

<1>7. Frobenius pullback splits the extension:
$$
f^*\mathcal E
\cong
\OO_C\oplus\OO_C(3P).
$$

::: {.proof}
Pulling back the extension of step <1>6 gives
$$
0
\longrightarrow
\OO_C
\longrightarrow
f^*\mathcal E
\longrightarrow
\OO_C(3P)
\longrightarrow0.
$$
Its extension class is precisely
$$
f^*\xi\in H^1(C,\OO_C(-3P)),
$$
which vanishes by the choice made in step <1>5. Hence the sequence splits.
:::

<1>8. A splitting in step <1>7 produces a morphism
$$
\varphi:C\longrightarrow X
$$
such that
$$
\pi\circ\varphi=f
$$
and
$$
\varphi^*\OO_X(C_0)\cong\OO_C.
$$

::: {.proof}
Choose the quotient supplied by the splitting,
$$
f^*\mathcal E\twoheadrightarrow\OO_C.
$$
By the universal property of the projective bundle of one-dimensional
quotients, this quotient is equivalent to a morphism
$$
\varphi:C\longrightarrow\PP(\mathcal E)=X
$$
lying over the base map $f$.

For the normalized section $C_0$, the kernel of
$$
\mathcal E\twoheadrightarrow\OO_C(P)
$$
is $\OO_C$, so the standard section-divisor formula gives
$$
\OO_X(C_0)\cong\OO_X(1).
$$
The pullback of the tautological quotient bundle along $\varphi$ is the
chosen quotient line bundle $\OO_C$. Hence
$$
\varphi^*\OO_X(C_0)\cong\OO_C.
$$
:::

<1>9. Let $Y\subset X$ be the scheme-theoretic image of $\varphi$. Then
$Y$ is integral, $\varphi:C\to Y$ is its normalization, and
$$
\boxed{Y\equiv3C_0-3f}.
$$

::: {.proof}
Because $C$ is proper and
$$
\pi\circ\varphi=f
$$
is finite, $\varphi$ is proper and quasi-finite, hence finite. Its
scheme-theoretic image $Y$ is therefore an integral projective curve.

Let
$$
m=\deg(C\to Y),
$$
and write
$$
Y\equiv aC_0+bf.
$$
Since
$$
f=(\pi|_Y)\circ\varphi
$$
has degree $3$,
$$
3=ma.
$$
Also step <1>8 gives
$$
0=\deg\varphi^*\OO_X(C_0)=m(C_0\cdot Y).
$$
Hence
$$
C_0\cdot Y=0.
$$
As $C_0^2=1$, this says
$$
a+b=0.
$$

Thus either
$$
(m,a,b)=(1,3,-3)
$$
or
$$
(m,a,b)=(3,1,-1).
$$
The second possibility is impossible: an integral curve of numerical class
$$
C_0-f
$$
would have degree one over $C$, hence would be a section, whereas the
normalized-bundle argument of [[P-AGH5214IRRCURVESCHARP]], step <1>2, shows
that every section $C_0+bf$ has $b\ge0$.

Therefore $m=1$ and
$$
Y\equiv3C_0-3f.
$$
Since $C$ is nonsingular and the finite map $C\to Y$ is birational, it is
the normalization of $Y$.
:::

<1>10. The morphism
$$
\pi|_Y:Y\longrightarrow C
$$
is purely inseparable of degree $3$.

::: {.proof}
Step <1>9 identifies the function field of $Y$ with that of its normalization
$C$. Under this identification, the induced extension of function fields for
$\pi|_Y$ is exactly the extension induced by
$$
f:C\longrightarrow C.
$$
The characteristic-$3$ Frobenius is purely inseparable of degree $3$.
Therefore so is $\pi|_Y$.
:::

<1>11. The curve $Y$ is singular; more precisely,
$$
p_a(Y)=4,
\qquad
g(\widetilde Y)=3.
$$

::: {.proof}
The base curve is a nonsingular plane quartic, so $g=3$. Step <1>6 gives
$e=-1$, hence the canonical divisor of the ruled surface is numerically
$$
K_X\equiv-2C_0+(2g-2-e)f=-2C_0+5f.
$$
Using step <1>9 and adjunction,
$$
\begin{aligned}
2p_a(Y)-2
&=Y\cdot(Y+K_X)\\
&=(3C_0-3f)\cdot(C_0+2f)\\
&=6.
\end{aligned}
$$
Thus
$$
p_a(Y)=4.
$$
Its normalization is $C$ by step <1>9, so its geometric genus is $3$.
Consequently $Y$ is singular, proving the correction recorded above.
:::

<1>12. The divisor
$$
D=2C_0
$$
satisfies the numerical hypotheses referred to in (2.21.b), namely
$$
a>0,
\qquad
b>\frac12ae,
$$
but $D$ is not ample.

::: {.proof}
For
$$
D=2C_0
$$
one has
$$
a=2,
\qquad
b=0,
\qquad
e=-1.
$$
Thus
$$
a>0
$$
and
$$
b=0>\frac12(2)(-1)=-1.
$$
So the numerical hypotheses of (2.21.b) are satisfied.

On the other hand, step <1>9 gives the integral curve
$$
Y\equiv3C_0-3f.
$$
Hence
$$
D\cdot Y
=
2C_0\cdot(3C_0-3f)
=
6-6
=0.
$$
An ample divisor has strictly positive intersection with every irreducible
curve by Nakai--Moishezon [[T-SRFNAKAI]]. Therefore
$$
\boxed{D\text{ is not ample}.}
$$
This is exactly the characteristic-$3$ failure that the exercise exhibits.
:::

<1>13. Q.E.D. for the corrected statement.

::: {.proof}
Steps <1>1--<1>3 prove part (a), steps <1>4--<1>5 prove part (b), and steps
<1>6--<1>12 prove the corrected form of part (c) and the non-ampleness
counterexample.
:::
:::
