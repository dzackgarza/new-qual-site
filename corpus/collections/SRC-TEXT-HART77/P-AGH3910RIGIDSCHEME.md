---
schema: qual/card@1
id: P-AGH3910RIGIDSCHEME
kind: problem
title: Rigidity of the projective line and its global deformations
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Morphisms
  - Infinitesimal Deformations
  - Rigidity
  - Base Change
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.9.10 together with the deformation classification used
    in III.9.13.2 and the surrounding flat-family results. Independently
    checked the standard generic-conic obstruction for part (b), including a
    characteristic-two variant, and the finite-flat normalization/section
    argument for part (c). The proof does not assume that a smooth genus-zero
    family already has a section over the original base.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
A scheme $X_0$ over a field $k$ is rigid if it has no infinitesimal deformations.

a. Show that $\PP_k^1$ is rigid, using (9.13.2).

b. One might think that if $X_0$ is rigid over $k$, then every global deformation of $X_0$ is locally trivial.
Show that this is not so, by constructing a proper, flat morphism $f: X \to \AA^2$ over $k$ algebraically closed, such that $X_0 \cong \PP_k^1$, but there is no open neighborhood $U$ of $0$ in $\AA^2$ for which $f^{-1}(U) \cong U \times \PP^1$.

c. Show, however, that one can trivialize a global deformation of $\PP^1$ after a flat base extension, in the following sense.
Let $f: X \to T$ be a flat projective morphism, where $T$ is a nonsingular curve over $k$ algebraically closed.
Assume there is a closed point $t \in T$ such that $X_t \cong \PP_k^1$.
Then there exists a nonsingular curve $T'$, and a flat morphism $g: T' \to T$ whose image contains $t$, such that if $X' = \fiberprod{X}{T}{T'}$ is the base extension, then the new family $f': X' \to T'$ is isomorphic to $\PP_{T'}^1 \to T'$.
:::

::: {.solution}
Write $o=(0,0)\in\AA_k^2$.

<1>1. The projective line $\PP_k^1$ is rigid.

::: {.proof}
For a smooth scheme, first-order deformations are classified by
$$
H^1(X,\mct_X)
$$
as in [[T-DEFEXT|the deformation classification used in Hartshorne III.9.13.2]].
The dual Euler sequence on $\PP^1$ gives
$$
\mct_{\PP^1}\cong\OO_{\PP^1}(2)
$$
[[T-MODEULER|Euler sequence]].
Since
$$
H^1(\PP_k^1,\OO(2))=0
$$
[@Har10a, Theorem III.5.1], the set of first-order deformation classes has one
element, namely the trivial deformation.
Thus $\PP_k^1$ is rigid.
:::

<1>2. There is a proper flat family of conics over $\AA_k^2$ whose fibre over $o$ is $\PP_k^1$ but whose generic fibre has no rational point.

::: {.proof}
Put
$$
S=\Spec k[a,b].
$$
We give a construction in every characteristic.

Assume first that $\operatorname{char}k\ne2$ and let
$$
X=V\bigl((a-1)x^2+(b-1)y^2+z^2\bigr)
\subseteq S\times_k\PP_k^2.
$$
Let $f:X\to S$ be the projection.
It is projective, hence proper.
Moreover $D_+(x)$ and $D_+(y)$ cover $X$: if $x=y=0$, the equation gives
$z=0$, which is impossible in projective space.
On either chart the coordinate ring is a quotient by a monic quadratic in
$z$; for example
$$
k[a,b,y,z]/\bigl((a-1)+(b-1)y^2+z^2\bigr)
$$
on $D_+(x)$ is free over $k[a,b,y]$ with basis $1,z$.
Hence both charts are flat over $k[a,b]$, and therefore $f$ is flat.

At the origin the fibre is
$$
-x^2-y^2+z^2=0.
$$
Its three partial derivatives have no common projective zero, so it is a
smooth plane conic. Since $k$ is algebraically closed, it is isomorphic to
$\PP_k^1$.

Now put
$$
A=a-1,\qquad B=b-1,\qquad K=k(A,B).
$$
The generic conic
$$
A x^2+B y^2+z^2=0
$$
has no $K$-rational point. Indeed, if it had one, clear denominators and divide
out a common factor to obtain a primitive triple
$$
x,y,z\in k[A,B]
$$
satisfying the equation. Reducing modulo $A$ gives
$$
B\bar y^2+\bar z^2=0
$$
in $k[B]$. If $(\bar y,\bar z)\ne(0,0)$, then $-B$ is a square in $k(B)$,
contrary to its odd valuation at the prime $(B)$. Thus $A$ divides both $y$
and $z$. The original equation then shows that $A$ divides $x^2$, hence $x$.
This contradicts primitivity.

If $\operatorname{char}k=2$, use instead
$$
X=V\bigl(x^2+xy+a y^2+(b-1)z^2\bigr)
\subseteq S\times_k\PP_k^2.
$$
Here $D_+(y)$ and $D_+(z)$ cover $X$, and on either chart the equation is
monic in $x$, so the same free-module argument proves flatness.
The fibre at $o$ is
$$
x^2+xy+z^2=0.
$$
Its partial derivatives are $y,x,0$, and their only common affine zero
$x=y=0$ does not lie on the projective conic; hence this fibre is again a
smooth conic and therefore $\PP_k^1$.

For the generic fibre put $B=b-1$ and $K=k(a,B)$. Suppose
$$
x^2+xy+a y^2+Bz^2=0
$$
had a $K$-point. If $y=0$, then $B$ would be a square in $K$, impossible
because its $B$-adic valuation is $1$. Thus $y\ne0$; setting
$$
u=x/y,\qquad v=z/y
$$
gives
$$
u^2+u+a=Bv^2.
$$
If $\operatorname{ord}_B(u)<0$, the left side has even negative valuation
$2\operatorname{ord}_B(u)$, whereas the right side has odd valuation
$1+2\operatorname{ord}_B(v)$, impossible. Hence
$\operatorname{ord}_B(u)\ge0$. This forces $\operatorname{ord}_B(v)\ge0$ as
well, since otherwise the right side has negative valuation while the left
side does not. Reducing modulo $B$ would then give
$$
\bar u^2+\bar u=a
$$
in $k(a)$. But $a$ is not of the form $w^2+w$: a rational function $w$ with
$w^2+w=a$ can have no finite pole, hence is a polynomial, and then a
nonconstant $w^2+w$ has even degree whereas $a$ has degree one.
This contradiction proves that the generic conic has no rational point also
in characteristic two.
:::

<1>3. The family in step <1>2 is not trivial over any Zariski neighborhood of $o$.

::: {.proof}
The base $S=\AA_k^2$ is integral, so every nonempty open neighborhood
$U\subseteq S$ of $o$ contains the generic point $\eta$.
If
$$
X_U\cong U\times\PP^1,
$$
then after base change to $\eta$ the generic fibre would be
$$
X_\eta\cong\PP^1_{k(a,b)}.
$$
In particular it would have a $k(a,b)$-rational point, contradicting step
<1>2. Thus no such neighborhood $U$ exists.
This proves part (b).
:::

<1>4. In part (c), after replacing $T$ by an open neighborhood of $t$, the morphism $f$ is smooth and every geometric fibre is a projective line.

::: {.proof}
Because $f$ is flat and of finite presentation and the fibre $X_t\cong\PP_k^1$
is smooth, $f$ is smooth at every point of $X_t$. The smooth locus is open in
$X$. Its complement is closed, and because $f$ is projective its image in $T$
is closed. Removing that image shrinks $T$ around $t$ and makes $f$ smooth.

For the coherent sheaf $\OO_X$, flatness over $T$ and
[[T-COHBC|semicontinuity and constancy of Euler characteristic]] give
$$
\chi(\OO_{X_s})=\chi(\OO_{X_t})=1
$$
near $t$. Since $H^1(\PP^1,\OO)=0$, upper semicontinuity permits a further
shrinking for which
$$
h^1(X_s,\OO_{X_s})=0,\qquad h^0(X_s,\OO_{X_s})=1.
$$
The two dimensions are therefore constant near $t$. Since $T$ is reduced,
cohomology and base change makes $f_*\OO_X$ locally free of rank one and makes
its formation commute with residue-field extension. Hence every geometric
fibre has only constant global functions and is connected. The smooth proper
fibres have genus zero, and over an algebraically closed residue field they are
therefore isomorphic to $\PP^1$.
:::

<1>5. After a finite flat base change by a nonsingular curve, the family acquires a section.

::: {.proof}
Let $K=k(T)$ and let $X_\eta$ be the generic fibre. It is a nonempty projective
curve over $K$, so choose a closed point $p\in X_\eta$ and put
$$
L=\kappa(p).
$$
Then $L/K$ is a finite field extension.

Let
$$
\nu:\overline T\longrightarrow T
$$
be the normalization of $T$ in $L$. Since $T$ is a nonsingular curve,
$\overline T$ is a normal noetherian curve and hence nonsingular. The map
$\nu$ is finite and dominant. It is also flat: locally on $T$, the coordinate
ring of $\overline T$ is a finite torsion-free module over a DVR, hence is
free. Thus $\nu$ is finite flat and surjective; choose
$\bar t\in\overline T$ above $t$.

Put
$$
\overline X=X\times_T\overline T.
$$
The point $p$ becomes an $L$-rational point of the generic fibre of
$\overline X$, and hence gives a rational section of
$\overline X\to\overline T$.
Because this morphism is proper and $\overline T$ is a nonsingular curve, the
valuative criterion for properness extends that rational section uniquely over
every local DVR $\OO_{\overline T,s}$. Separatedness makes the local extensions
glue, giving a global section
$$
\sigma:\overline T\longrightarrow\overline X.
$$
:::

<1>6. On a suitable open neighborhood $T'$ of $\bar t$ in $\overline T$, the section identifies the pulled-back family with $\PP^1_{T'}$.

::: {.proof}
Let $\bar f:\overline X\to\overline T$ be the projection.
The section $D=\sigma(\overline T)$ is an effective Cartier divisor because
$\bar f$ is a smooth relative curve. Put
$$
\mcl=\OO_{\overline X}(D).
$$
On every fibre $C$ the divisor $D|_C$ is one rational point, so
$$
\mcl|_C\cong\OO_{\PP^1}(1).
$$
Consequently
$$
h^0(C,\mcl|_C)=2,\qquad h^1(C,\mcl|_C)=0.
$$
By [[T-COHBC|cohomology and base change]], the sheaf
$$
\mce=\bar f_*\mcl
$$
is locally free of rank two near $\bar t$ and commutes with base change there.
Choose an open neighborhood $T'\subseteq\overline T$ of $\bar t$ on which
$$
\mce|_{T'}\cong\OO_{T'}^{\oplus2},
$$
and put
$$
X'=\overline X\times_{\overline T}T'.
$$

The evaluation map
$$
\bar f^*\mce\longrightarrow\mcl
$$
is surjective on the fibre over $\bar t$, because it is the evaluation map of
the complete linear system $|\OO_{\PP^1}(1)|$. Its cokernel is coherent; its
support is closed, and properness of $\bar f$ makes the image of that support
closed in $\overline T$. Shrinking $T'$ once more if necessary therefore
makes the evaluation map surjective over all of $X'$.

After base change to $X'$, this quotient defines a $T'$-morphism
$$
h:X'\longrightarrow\PP(\mce|_{T'})
$$
by the projective-bundle quotient construction of
[[P-AGH278SECTIONSPE]]. On each fibre this is the morphism defined by the
complete linear system $|\OO_{\PP^1}(1)|$, hence an isomorphism.

The morphism $h$ is proper because $X'$ is proper over $T'$ and
$\PP(\mce|_{T'})$ is separated over $T'$. Since its fibre maps are
isomorphisms, $h$ is quasi-finite and therefore finite. The scheme $X'$ is
integral: it is smooth over the integral curve $T'$ with geometrically
integral fibres. The generic fibre map is an isomorphism, so $h$ is birational.
Finally $\PP(\mce|_{T'})$ is regular, hence normal, because it is a projective
line bundle over the nonsingular curve $T'$. A finite birational morphism to a
normal scheme is an isomorphism. Therefore
$$
X'\cong\PP(\mce|_{T'})\cong\PP^1_{T'}.
$$
:::

<1>7. The resulting map to the original curve has all the required properties.

::: {.proof}
The curve $T'$ is an open subscheme of the nonsingular curve $\overline T$,
so it is nonsingular. The composite
$$
g:T'\hookrightarrow\overline T\xrightarrow{\nu}T
$$
is flat: the first map is an open immersion and $\nu$ is finite flat.
Its image contains $t$ because $\bar t\in T'$ lies over $t$.
Step <1>6 gives
$$
X\times_TT'\cong\PP^1_{T'}
$$
over $T'$.
This proves part (c).
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>1 proves (a), steps <1>2--<1>3 give the nontrivial global deformation
required in (b), and steps <1>4--<1>7 construct the flat base extension and
trivialization required in (c).
:::
:::
