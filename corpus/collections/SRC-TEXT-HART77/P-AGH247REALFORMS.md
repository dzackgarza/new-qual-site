---
schema: qual/card@1
id: P-AGH247REALFORMS
kind: problem
title: Real forms of complex schemes and semilinear involutions
classification:
  areas:
  - algebraic-geometry
  topics:
  - Descent
  - Base Change
  - Conics
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against Hartshorne II.4.7 and standard faithfully flat/Galois descent for affine schemes, open immersions, and morphisms.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
For any scheme $X_0$ over $\RR$, let $X = \fiberprod{X_0}{\RR}{\CC}$.
Let $\alpha: \CC \to \CC$ be complex conjugation, and let $\sigma: X \to X$ be the automorphism obtained by keeping $X_0$ fixed and applying $\alpha$ to $\CC$.
Then $X$ is a scheme over $\CC$, and $\sigma$ is a **semilinear** automorphism: the square formed by $\sigma$ on $X$, by $\alpha$ on $\Spec \CC$, and by the two structure morphisms $X \to \Spec \CC$ commutes.
Since $\sigma^2 = \id$, we call $\sigma$ an **involution**.

a. Let $X$ be a separated scheme of finite type over $\CC$, let $\sigma$ be a semilinear involution on $X$, and assume that for any two points $x_1, x_2 \in X$ there is an open affine subset containing both of them.
This last condition holds for example if $X$ is quasi-projective.
Show that there is a unique separated scheme $X_0$ of finite type over $\RR$ with $\fiberprod{X_0}{\RR}{\CC} \cong X$, such that this isomorphism identifies the given involution of $X$ with the one described above.

For the following statements, $X_0$ denotes a separated scheme of finite type over $\RR$, and $X, \sigma$ the corresponding scheme with involution over $\CC$.

b. Show that $X_0$ is affine if and only if $X$ is.

c. If $X_0, Y_0$ are two such schemes over $\RR$, then to give a morphism $f_0: X_0 \to Y_0$ is equivalent to giving a morphism $f: X \to Y$ which commutes with the involutions, i.e. $f \circ \sigma_X = \sigma_Y \circ f$.

d. If $X \cong \AA^1_\CC$, then $X_0 \cong \AA^1_\RR$.

e. If $X \cong \PP^1_\CC$, then either $X_0 \cong \PP^1_\RR$, or $X_0$ is isomorphic to the conic in $\PP^2_\RR$ given by the homogeneous equation $x_0^2 + x_1^2 + x_2^2 = 0$.
:::

::: {.solution}
We write
\[
c:\Spec\mathbb C\longrightarrow\Spec\mathbb C
\]
for complex conjugation.

::: pf

::: {.pf-step #s1}

Under the hypotheses of part (a), every point of $X$ has a $\sigma$-stable affine open neighborhood.

::: pf-proof

Fix $x\in X$.  By hypothesis there is an affine open
\[
U\subseteq X
\]
containing both $x$ and $\sigma(x)$.
Then
\[
V=U\cap\sigma(U)
\]
contains $x$: since $\sigma(x)\in U$, applying $\sigma$ gives $x\in\sigma(U)$.  Similarly it contains $\sigma(x)$.

The scheme $X$ is separated over the affine scheme $\Spec\mathbb C$, so Hartshorne II.4.3 shows that the intersection of two affine opens is affine.  Thus $V$ is affine.  Finally
\[
\sigma(V)
=
\sigma(U)\cap U
=V,
\]
so $V$ is $\sigma$-stable.

:::

:::

::: {.pf-step #s2}

Let
\[
U=\Spec A\subseteq X
\]
be a $\sigma$-stable affine open.  The involution induces a conjugate-linear ring involution
\[
\tau:A\longrightarrow A,
\]
meaning
\[
\tau(\lambda a)=\overline\lambda\,\tau(a)
\qquad
(\lambda\in\mathbb C).
\]
Put
\[
A_0=A^\tau.
\]
Then the natural map
\[
\boxed{A_0\otimes_{\mathbb R}\mathbb C\xrightarrow{\sim}A}
\]
is an isomorphism.

::: pf-proof

For every $a\in A$, set
\[
u=\frac{a+\tau(a)}2,
\qquad
v=\frac{a-\tau(a)}{2i}.
\]
Because $\tau$ conjugates scalars and $\tau^2=1$,
\[
\tau(u)=u,
\qquad
\tau(v)=v.
\]
Thus $u,v\in A_0$, and
\[
a=u+iv.
\]

This decomposition is unique.  Indeed, if
\[
u+iv=0
\qquad(u,v\in A_0),
\]
applying $\tau$ gives
\[
u-iv=0.
\]
Adding and subtracting yields $u=v=0$.

Hence, as real vector spaces,
\[
A=A_0\oplus iA_0,
\]
which is exactly the assertion that multiplication induces an isomorphism
\[
A_0\otimes_{\mathbb R}\mathbb C\cong A.
\]
It is plainly an isomorphism of rings.

:::

:::

::: {.pf-step #s3}

If $A$ is finitely generated as a $\mathbb C$-algebra, then $A_0=A^\tau$ is finitely generated as an $\mathbb R$-algebra.

::: pf-proof

Choose algebra generators
\[
a_1,\ldots,a_n\in A.
\]
By step [](#s2){.pf-ref}, write
\[
a_j=u_j+iv_j,
\qquad
u_j,v_j\in A_0.
\]
Let
\[
B_0=\mathbb R[u_1,v_1,\ldots,u_n,v_n]\subseteq A_0.
\]
Then
\[
A=\mathbb C[a_1,\ldots,a_n]
\subseteq
\mathbb C[B_0]
\subseteq A,
\]
so
\[
A=\mathbb C[B_0]=B_0\oplus iB_0.
\]

If $a\in A_0$, write $a=b+ic$ with $b,c\in B_0$.  Applying $\tau$ gives
\[
a=b-ic.
\]
Hence $c=0$ and $a=b\in B_0$.  Therefore
\[
A_0=B_0,
\]
which is finitely generated over $\mathbb R$.

:::

:::

::: {.pf-step #s4}

The $\sigma$-stable affine opens of step [](#s1){.pf-ref} may be chosen as a finite cover
\[
X=U_1\cup\cdots\cup U_r.
\]

::: pf-proof

The stable affine neighborhoods from step [](#s1){.pf-ref} cover $X$.  Since $X$ is of finite type over the field $\mathbb C$, it is quasi-compact.  Hence a finite subcover exists.

:::

:::

::: {.pf-step #s5}

For every $i,j$, the overlap
\[
U_{ij}=U_i\cap U_j
\]
is $\sigma$-stable and affine, and its descent
\[
(U_{ij})_0
\]
is an open subscheme of both descended affine schemes
\[
(U_i)_0=\Spec\Gamma(U_i,\mathcal O_X)^\sigma,
\qquad
(U_j)_0=\Spec\Gamma(U_j,\mathcal O_X)^\sigma.
\]

::: pf-proof

Stability is immediate from stability of $U_i$ and $U_j$.  Affineness follows from separatedness by Hartshorne II.4.3.

By step [](#s2){.pf-ref}, each stable affine and each stable overlap carries the standard descent datum for the faithfully flat extension
\[
\mathbb R\subseteq\mathbb C.
\]
The inclusions
\[
U_{ij}\hookrightarrow U_i,
\qquad
U_{ij}\hookrightarrow U_j
\]
commute with the involution.  Faithfully flat descent of morphisms descends them uniquely, and the property of being an open immersion is fpqc local on the base.  Hence the descended maps are open immersions.

This is the standard affine/open-immersion case of fpqc descent; see the Stacks Project, Sections 35.35, 35.37, and Lemma 35.23.18.

:::

:::

::: {.pf-step #s6}

The descended affine schemes $(U_i)_0$ glue along the descended overlaps $(U_{ij})_0$ to a scheme $X_0$ over $\mathbb R$.
Moreover,
\[
\boxed{X_0\times_{\mathbb R}\mathbb C\cong X}
\]
and the standard conjugation involution on the left corresponds to $\sigma$.

::: pf-proof

The original overlaps satisfy the cocycle condition inside $X$.  Faithful flatness of $\mathbb C/\mathbb R$ makes pullback on morphisms faithful, so the descended overlap maps satisfy the same cocycle condition.

Hartshorne II.2.12 therefore glues the $(U_i)_0$ into a scheme $X_0$.

After base change to $\mathbb C$, step [](#s2){.pf-ref} identifies each descended chart with the original chart $U_i$, and the overlap maps base-change to the original inclusions.  Thus the base-changed glued scheme is exactly the gluing of the $U_i$, namely $X$.

On every affine chart the descent datum is the involution $\tau$, so the resulting canonical conjugation on the base change is the given $\sigma$.

:::

:::

::: {.pf-step #s7}

The descended scheme $X_0$ is of finite type and separated over $\mathbb R$.

::: pf-proof

Each affine chart $(U_i)_0$ has finitely generated coordinate ring over $\mathbb R$ by step [](#s3){.pf-ref}.  The cover is finite by step [](#s4){.pf-ref}, so $X_0$ is quasi-compact and locally of finite type, hence of finite type.

Separatedness is fpqc local on the base.  After the faithfully flat base change
\[
\Spec\mathbb C\longrightarrow\Spec\mathbb R,
\]
the morphism $X_0\to\Spec\mathbb R$ becomes the separated morphism
\[
X\to\Spec\mathbb C.
\]
Therefore $X_0$ is separated.

:::

:::

::: {.pf-step #s8}

The descended scheme $X_0$, together with its identification after base change, is unique up to unique isomorphism.

::: pf-proof

Faithfully flat descent of morphisms is fully faithful: two morphisms over $\mathbb R$ are equal if their base changes to $\mathbb C$ are equal, and every morphism over $\mathbb C$ compatible with the descent data descends uniquely.

If $X_0'$ is another descent of $(X,\sigma)$, the identity morphism of $X$ is compatible with the two descent data.  It therefore descends to a unique isomorphism
\[
X_0\xrightarrow{\sim}X_0'.
\]
Its inverse is the descent of the inverse identity after base change.  This proves the uniqueness asserted in part (a).

:::

:::

::: {.pf-step #s9}

If $X_0$ is affine, then $X=X_0\times_{\mathbb R}\mathbb C$ is affine.

::: pf-proof

If
\[
X_0=\Spec A_0,
\]
then
\[
X
\cong
\Spec(A_0\otimes_{\mathbb R}\mathbb C),
\]
which is affine.

:::

:::

::: {.pf-step #s10}

If $X$ is affine, then $X_0$ is affine.

::: pf-proof

The whole affine scheme $X=\Spec A$ is $\sigma$-stable.  Applying the affine descent construction step [](#s2){.pf-ref} gives
\[
\Spec(A^\sigma)
\]
as a real scheme whose complexification, with its conjugation descent datum, is $(X,\sigma)$.

By uniqueness in step [](#s8){.pf-ref},
\[
X_0\cong\Spec(A^\sigma).
\]
Thus $X_0$ is affine.

:::

:::

::: {.pf-step #s11}

Hence
\[
\boxed{X_0\text{ is affine}\iff X\text{ is affine}.}
\]

::: pf-proof

Combine steps [](#s9){.pf-ref} and [](#s10){.pf-ref}.  This proves part (b).

:::

:::

::: {.pf-step #s12}

If
\[
f_0:X_0\longrightarrow Y_0
\]
is a morphism over $\mathbb R$, its base change
\[
f:X\longrightarrow Y
\]
commutes with the involutions.

::: pf-proof

Both involutions are obtained by applying complex conjugation only to the base factor.  Base change of $f_0$ acts on the original factors and is therefore natural with respect to conjugation:
\[
f\circ\sigma_X=\sigma_Y\circ f.
\]

:::

:::

::: {.pf-step #s13}

Conversely, every morphism
\[
f:X\longrightarrow Y
\]
commuting with the involutions descends uniquely to a morphism
\[
f_0:X_0\longrightarrow Y_0.
\]

::: pf-proof

The identity
\[
f\circ\sigma_X=\sigma_Y\circ f
\]
is exactly the compatibility condition with the descent data for the faithfully flat cover
\[
\Spec\mathbb C\to\Spec\mathbb R.
\]
Fully faithful fpqc descent of morphisms therefore gives a unique descended morphism $f_0$.

:::

:::

::: {.pf-step #s14}

This proves the bijection in part (c).

::: pf-proof

Steps [](#s12){.pf-ref} and [](#s13){.pf-ref} construct the two inverse operations, base change and descent.

:::

:::

::: {.pf-step #s15}

Assume
\[
X\cong\mathbb A^1_{\mathbb C}.
\]
Then $X_0$ is affine by part (b), and its coordinate ring is the invariant ring of a conjugate-linear involution
\[
\tau:\mathbb C[t]\longrightarrow\mathbb C[t].
\]
One has
\[
\tau(t)=at+b
\]
for some $a\in\mathbb C^\times$, $b\in\mathbb C$.

::: pf-proof

By part (b), $X_0$ is affine, so the affine descent description step [](#s2){.pf-ref} applies.

The map $\tau$ is semilinear and bijective.  After composing with ordinary complex conjugation on the coefficients, it becomes a $\mathbb C$-algebra automorphism of $\mathbb C[t]$.  Every automorphism of a one-variable polynomial ring sends $t$ to an affine-linear polynomial.  Thus
\[
\tau(t)=at+b,
\qquad a\ne0.
\]

:::

:::

::: {.pf-step #s16}

The involution condition $\tau^2=1$ gives
\[
a\overline a=1,
\qquad
\overline a\,b+\overline b=0.
\]
There exist $c\in\mathbb C^\times$ and $d\in\mathbb C$ such that the affine coordinate
\[
u=ct+d
\]
satisfies
\[
\tau(u)=u.
\]

::: pf-proof

Applying $\tau$ twice to $t$ gives
\[
t
=
\tau(at+b)
=
\overline a(at+b)+\overline b,
\]
which gives the two displayed relations.

The first says $a$ has absolute value $1$.  Choose $c\ne0$ with
\[
\frac c{\overline c}=a;
\]
for example, if $a=e^{i\theta}$ take $c=e^{i\theta/2}$.

Put
\[
r=\overline c\,b.
\]
Using $a=c/\overline c$, the second involution relation becomes
\[
r+\overline r=0,
\]
so $r$ is purely imaginary.  Choose $d$ with
\[
d-\overline d=r,
\]
for example $d=r/2$.

Then
\[
\tau(u)
=
\overline c(at+b)+\overline d
=
ct+r+\overline d
=
ct+d
=u.
\]

:::

:::

::: {.pf-step #s17}

The invariant ring is
\[
\boxed{\mathbb C[t]^\tau=\mathbb R[u].}
\]
Consequently
\[
\boxed{X_0\cong\mathbb A^1_{\mathbb R}.}
\]

::: pf-proof

Since $u=ct+d$ with $c\ne0$,
\[
\mathbb C[t]=\mathbb C[u].
\]
In the coordinate $u$, the involution fixes $u$ and conjugates coefficients.  A polynomial
\[
\sum_j\lambda_ju^j
\]
is fixed exactly when every coefficient satisfies
\[
\lambda_j=\overline{\lambda_j},
\]
i.e. lies in $\mathbb R$.  Thus the invariant ring is $\mathbb R[u]$.

:::

:::

::: {.pf-step #s18}

This proves part (d).

::: pf-proof

Step [](#s17){.pf-ref} is the required classification of the real form of the affine line.

:::

:::

::: {.pf-step #s19}

Assume now
\[
X\cong\mathbb P^1_{\mathbb C}.
\]
Then $X_0$ is a smooth proper geometrically integral curve of genus $0$ over $\mathbb R$.

::: pf-proof

After the faithfully flat base change $\mathbb R\subseteq\mathbb C$, the scheme $X_0$ becomes $\mathbb P^1_{\mathbb C}$.

Smoothness, properness, and geometric integrality descend under faithfully flat field extension.  Thus $X_0$ is a smooth proper geometrically integral curve over $\mathbb R$.

Its geometric genus is the genus of its complexification, namely
\[
g(\mathbb P^1)=0.
\]

:::

:::

::: {.pf-step #s20}

The real points of $X_0$ correspond exactly to the fixed complex points of $\sigma$.

::: pf-proof

A real point is a morphism
\[
p_0:\Spec\mathbb R\longrightarrow X_0.
\]
After base change it gives a morphism
\[
p:\Spec\mathbb C\longrightarrow X
\]
which commutes with conjugation, hence whose image point is fixed by $\sigma$.

Conversely, a complex point fixed by $\sigma$ gives a morphism $p:\Spec\mathbb C\to X$ compatible with the descent data.  Part (c) descends it uniquely to a real point of $X_0$.

:::

:::

::: {.pf-step #s21}

If $X_0(\mathbb R)\ne\varnothing$, then
\[
\boxed{X_0\cong\mathbb P^1_{\mathbb R}.}
\]

::: pf-proof

A smooth proper genus-zero curve over a field with a rational point is isomorphic to the projective line.

For completeness, if $P\in X_0(\mathbb R)$, Riemann--Roch gives
\[
\ell(P)=2.
\]
The complete linear system $|P|$ therefore defines a nonconstant morphism
\[
X_0\longrightarrow\mathbb P^1_{\mathbb R}
\]
of degree $1$.  A degree-one finite morphism between smooth proper integral curves is an isomorphism.

:::

:::

::: {.pf-step #s22}

If $X_0(\mathbb R)=\varnothing$, then $X_0$ is isomorphic to a smooth plane conic with no real point.

::: pf-proof

Every smooth proper geometrically integral genus-zero curve is a Severi--Brauer curve.  Equivalently, its anticanonical system has degree $2$ and dimension $2$, and embeds it as a smooth conic
\[
C\subseteq\mathbb P^2_{\mathbb R}.
\]

The isomorphism preserves rational points, so the conic has no $\mathbb R$-point.

:::

:::

::: {.pf-step #s23}

Every smooth plane conic over $\mathbb R$ with no real point is isomorphic over $\mathbb R$ to
\[
\boxed{x_0^2+x_1^2+x_2^2=0.}
\]

::: pf-proof

A smooth plane conic over $\mathbb R$ is defined by a nondegenerate real ternary quadratic form
\[
q(x_0,x_1,x_2).
\]
By Sylvester's law of inertia, after a real linear change of coordinates and multiplication of the equation by a nonzero scalar, $q$ is diagonal with coefficients $\pm1$.

If both signs occurred, the equation $q=0$ would have a nonzero real solution, hence the conic would have a real point.  Since there is no real point, the quadratic form is definite.  Multiplying by $-1$ if necessary, it is positive definite, and another real linear change of coordinates gives
\[
q=x_0^2+x_1^2+x_2^2.
\]
Thus the conic is isomorphic to the displayed one.

:::

:::

::: {.pf-step #s24}

Hence, when $X\cong\mathbb P^1_{\mathbb C}$,
\[
\boxed{
X_0\cong\mathbb P^1_{\mathbb R}
\quad\text{or}\quad
X_0\cong V(x_0^2+x_1^2+x_2^2)\subseteq\mathbb P^2_{\mathbb R}.
}
\]

::: pf-proof

If $X_0$ has a real point, apply step [](#s21){.pf-ref}.  If it does not, apply steps [](#s22){.pf-ref} and [](#s23){.pf-ref}.  These cases are mutually exclusive because the displayed anisotropic conic has no nonzero real solution.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref} prove part (a), steps [](#s9){.pf-ref}, [](#s10){.pf-ref} and [](#s11){.pf-ref} prove part (b), steps [](#s12){.pf-ref}, [](#s13){.pf-ref} and [](#s14){.pf-ref} prove part (c), steps [](#s15){.pf-ref}, [](#s16){.pf-ref}, [](#s17){.pf-ref} and [](#s18){.pf-ref} prove part (d), and steps [](#s19){.pf-ref}, [](#s20){.pf-ref}, [](#s21){.pf-ref}, [](#s22){.pf-ref}, [](#s23){.pf-ref} and [](#s24){.pf-ref} prove part (e).

:::

:::

:::
