---
schema: qual/card@1
id: P-AGH2121VARSHEAVES
kind: problem
title: Ideal sheaves on varieties and the failure of exactness of global sections
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Ideal Sheaves
  - Global Sections
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.1.21 statement and source-order placement after II.1.20.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a variety over an algebraically closed field $k$, and let $\OO_X$ be the sheaf of regular functions on $X$.

a. Let $Y$ be a closed subset of $X$.
For each open set $U \subseteq X$, let $\mci_Y(U)$ be the ideal in the ring $\OO_X(U)$ consisting of those regular functions which vanish at all points of $Y \intersect U$.
Show that the presheaf $U \mapsto \mci_Y(U)$ is a sheaf.
It is called the **sheaf of ideals** $\mci_Y$ of $Y$, and it is a subsheaf of the sheaf of rings $\OO_X$.

b. If $Y$ is a subvariety, show that the quotient sheaf $\OO_X / \mci_Y$ is isomorphic to $i_* \OO_Y$, where $i: Y \to X$ is the inclusion and $\OO_Y$ is the sheaf of regular functions on $Y$.

c. Now let $X = \PP^1$ and let $Y$ be the union of two distinct points $P, Q \in X$.
Then with $\mcf = i_* \OO_P \oplus i_* \OO_Q$ there is an exact sequence of sheaves on $X$
\[
0 \to \mci_Y \to \OO_X \to \mcf \to 0.
\]
Show however that the induced map on global sections $\Gamma(X, \OO_X) \to \Gamma(X, \mcf)$ is not surjective.
This shows that the global section functor $\Gamma(X, \wait)$ is not exact.

d. Again let $X = \PP^1$ and let $\OO$ be the sheaf of regular functions.
Let $\mck$ be the constant sheaf on $X$ associated to the function field $K$ of $X$.
Show that there is a natural injection $\OO \to \mck$.
Show that the quotient sheaf $\mck / \OO$ is isomorphic to the direct sum of sheaves $\bigoplus_{P \in X} i_P(I_P)$, where $I_P$ is the group $K/\OO_P$ and $i_P(I_P)$ denotes the skyscraper sheaf given by $I_P$ at the point $P$.

e. Finally, show that in the case of (d) the sequence
\[
0 \to \Gamma(X, \OO) \to \Gamma(X, \mck) \to \Gamma(X, \mck/\OO) \to 0
\]
is exact.
:::

::: {.remark}
Part (e) is an analogue of the first Cousin problem in several complex variables; see Gunning and Rossi.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For a closed subset $Y\subseteq X$, the assignment
\[
\mathcal I_Y(U)
=
\{f\in\mathcal O_X(U):f|_{Y\cap U}=0\text{ pointwise}\}
\]
is a subpresheaf of rings of $\mathcal O_X$.

::: pf-proof

If $V\subseteq U$ and
\[
f\in\mathcal I_Y(U),
\]
then for every
\[
P\in Y\cap V
\subseteq
Y\cap U
\]
one has
\[
(f|_V)(P)=f(P)=0.
\]
Thus
\[
f|_V\in\mathcal I_Y(V).
\]
The set $\mathcal I_Y(U)$ is clearly an ideal of $\mathcal O_X(U)$, since sums of functions vanishing on $Y\cap U$ vanish there and multiplying by an arbitrary regular function preserves vanishing.

:::

:::

::: {.pf-step #s2}

The presheaf $\mathcal I_Y$ is a sheaf, hence a sheaf of ideals in $\mathcal O_X$.

::: pf-proof

Let
\[
U=\bigcup_iU_i
\]
and suppose compatible sections
\[
f_i\in\mathcal I_Y(U_i)
\]
are given.
Since $\mathcal O_X$ is a sheaf, the $f_i$ glue uniquely to
\[
f\in\mathcal O_X(U).
\]

For any point
\[
P\in Y\cap U,
\]
choose $i$ with $P\in U_i$.
Then
\[
f(P)=f_i(P)=0.
\]
Thus
\[
f\in\mathcal I_Y(U).
\]
Uniqueness is inherited from $\mathcal O_X$.
Hence $\mathcal I_Y$ is a sheaf.

:::

:::

::: {.pf-step #s3}

If $Y$ is a subvariety and
\[
i:Y\hookrightarrow X
\]
is the inclusion, restriction of regular functions gives a sheaf morphism
\[
\rho:\mathcal O_X\longrightarrow i_*\mathcal O_Y
\]
whose kernel is $\mathcal I_Y$.

::: pf-proof

For every open $U\subseteq X$, restriction gives
\[
\rho_U:\mathcal O_X(U)
\longrightarrow
\mathcal O_Y(U\cap Y).
\]
These maps commute with further restrictions, so they define a sheaf morphism.

By definition,
\[
f\in\ker\rho_U
\]
exactly when $f$ vanishes as a regular function on $U\cap Y$, equivalently when it vanishes at every point of $U\cap Y$.
This is precisely
\[
f\in\mathcal I_Y(U).
\]
Thus
\[
\ker\rho=\mathcal I_Y.
\]

:::

:::

::: {.pf-step #s4}

The morphism $\rho$ is surjective as a morphism of sheaves.

::: pf-proof

It suffices to check surjectivity on stalks.

If $P\notin Y$, then
\[
(i_*\mathcal O_Y)_P=0,
\]
so surjectivity is automatic.

Let $P\in Y$.
Choose an affine open neighborhood
\[
P\in V=\operatorname{Spec}A\subseteq X
\]
such that
\[
Y\cap V=V(I)=\operatorname{Spec}(A/I)
\]
for the ideal defining the subvariety locally.
The map on stalks is then
\[
A_{\mathfrak p}
\longrightarrow
(A/I)_{\mathfrak p/I},
\]
which is surjective.
Hence $\rho$ is surjective at every stalk.

:::

:::

::: {.pf-step #s5}

Therefore
\[
\boxed{
\mathcal O_X/\mathcal I_Y
\cong
i_*\mathcal O_Y.
}
\]

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} give an exact sequence
\[
0\longrightarrow\mathcal I_Y
\longrightarrow\mathcal O_X
\xrightarrow{\rho}i_*\mathcal O_Y
\longrightarrow0.
\]
The sheaf first-isomorphism theorem gives the displayed quotient isomorphism.

:::

:::

::: {.pf-step #s6}

Let now
\[
X=\mathbb P^1_k,
\qquad
Y=\{P,Q\}
\]
for distinct $k$-points $P,Q$, and let
\[
\mathcal F=i_{P*}\mathcal O_P\oplus i_{Q*}\mathcal O_Q.
\]
Then
\[
0\longrightarrow\mathcal I_Y
\longrightarrow\mathcal O_X
\longrightarrow\mathcal F
\longrightarrow0
\]
is exact.

::: pf-proof

The reduced subvariety $Y$ is the disjoint union of the two points $P$ and $Q$, so
\[
\mathcal O_Y
\cong
\mathcal O_P\oplus\mathcal O_Q
\]
as a sheaf on $Y$.
Therefore
\[
i_*\mathcal O_Y
\cong
i_{P*}\mathcal O_P\oplus i_{Q*}\mathcal O_Q
=\mathcal F.
\]
Apply the exact sequence from step [](#s5){.pf-ref}.

:::

:::

::: {.pf-step #s7}

The induced map on global sections
\[
\Gamma(X,\mathcal O_X)
\longrightarrow
\Gamma(X,\mathcal F)
\]
is not surjective.

::: pf-proof

Every global regular function on the projective integral curve $\mathbb P^1_k$ is constant, so
\[
\Gamma(X,\mathcal O_X)=k.
\]
On the other hand,
\[
\Gamma(X,\mathcal F)
\cong
k\oplus k.
\]
The restriction map sends
\[
c\longmapsto(c,c).
\]
Its image is the diagonal subspace of $k\oplus k$, which does not contain, for example,
\[
(1,0).
\]
Hence the map is not surjective.

:::

:::

::: {.pf-step #s8}

Thus the global-section functor is left exact but not exact.

::: pf-proof

Applying global sections to the short exact sequence of step [](#s6){.pf-ref} gives
\[
0\to
\Gamma(X,\mathcal I_Y)
\to
\Gamma(X,\mathcal O_X)
\to
\Gamma(X,\mathcal F),
\]
which is exact at the first two terms because $\Gamma$ is left exact.
Step [](#s7){.pf-ref} shows that the last map need not be surjective, so $\Gamma$ is not right exact and hence not exact.

:::

:::

::: {.pf-step #s9}

Continue with $X=\mathbb P^1_k$.
Let
\[
K=k(X)
\]
be its function field and let $\mathcal K$ be the constant sheaf associated to the abelian group $K$.
There is a natural injection
\[
\boxed{\mathcal O_X\hookrightarrow\mathcal K.}
\]

::: pf-proof

Every nonempty open subset of the irreducible variety $X$ is irreducible, so the constant sheaf $\mathcal K$ has
\[
\mathcal K(U)=K
\]
for every nonempty open $U$.

A regular function on a nonempty open $U$ is, by definition, a rational function regular at every point of $U$.
Thus there is a natural injective map
\[
\mathcal O_X(U)\hookrightarrow K=\mathcal K(U).
\]
These inclusions commute with restriction, giving the sheaf morphism.
It is injective on every open set, hence a monomorphism.

:::

:::

::: {.pf-step #s10}

For every point $P\in X$, the stalk of the quotient sheaf is
\[
\boxed{
(\mathcal K/\mathcal O_X)_P
\cong
K/\mathcal O_{X,P}
=:I_P.
}
\]

::: pf-proof

Sheaf stalks are exact.
Taking the stalk at $P$ of
\[
0\longrightarrow\mathcal O_X
\longrightarrow\mathcal K
\longrightarrow\mathcal K/\mathcal O_X
\longrightarrow0
\]
gives
\[
0\longrightarrow\mathcal O_{X,P}
\longrightarrow\mathcal K_P
\longrightarrow
(\mathcal K/\mathcal O_X)_P
\longrightarrow0.
\]
Since $X$ is irreducible,
\[
\mathcal K_P=K,
\]
so the quotient stalk is $K/\mathcal O_{X,P}$.

:::

:::

::: {.pf-step #s11}

A section of $\mathcal K/\mathcal O_X$ over an open set $U$ has nonzero germ at only finitely many points of $U$.

::: pf-proof

The support of any section of a sheaf is closed in $U$.
We show more directly that it is finite.

Every point of $U$ has a neighborhood on which the section is represented by a section of $\mathcal K$, hence by one rational function in $K$.
Since $X=\mathbb P^1_k$ is noetherian, the open set $U$ is quasicompact, so finitely many such neighborhoods cover $U$.

A rational function on the nonsingular projective curve $\mathbb P^1$ has only finitely many poles.
On a neighborhood where the quotient section is represented by a rational function $f$, its germ is zero at every point where $f$ is regular.
Thus the support on that neighborhood is contained in the finite pole set of $f$.

Taking the finite union over a finite cover shows that the support of the original section is finite.

:::

:::

::: {.pf-step #s12}

Sending a section to its germs defines a sheaf morphism
\[
\Phi:
\mathcal K/\mathcal O_X
\longrightarrow
\bigoplus_{P\in X}i_P(I_P).
\]

::: pf-proof

By Hartshorne II.1.11, direct sums of sheaves on the noetherian space $X$ are computed sectionwise as filtered direct limits of finite direct sums.
Hence
\[
\left(\bigoplus_{P\in X}i_P(I_P)\right)(U)
\cong
\bigoplus_{P\in U}I_P,
\]
the group of finite-support tuples.

Given
\[
s\in(\mathcal K/\mathcal O_X)(U),
\]
define
\[
\Phi_U(s)=(s_P)_{P\in U}.
\]
By step [](#s11){.pf-ref} this tuple has finite support, so it belongs to the direct sum.
Taking germs is compatible with restriction, so the maps $\Phi_U$ form a sheaf morphism.

:::

:::

::: {.pf-step #s13}

The morphism $\Phi$ is an isomorphism:
\[
\boxed{
\mathcal K/\mathcal O_X
\cong
\bigoplus_{P\in X}i_P(I_P).
}
\]

::: pf-proof

It suffices to check the map on stalks.

At a point $Q\in X$, step [](#s10){.pf-ref} gives
\[
(\mathcal K/\mathcal O_X)_Q=I_Q.
\]
On the right, the stalk of the $Q$th skyscraper is $I_Q$, while every skyscraper supported at a different closed point has zero stalk at $Q$.
Thus
\[
\left(\bigoplus_{P\in X}i_P(I_P)\right)_Q
\cong I_Q.
\]
Under these identifications, $\Phi_Q$ is the identity map on $I_Q$.
Therefore $\Phi$ is an isomorphism at every stalk, hence an isomorphism of sheaves.

:::

:::

::: {.pf-step #s14}

Consequently,
\[
\Gamma(X,\mathcal K/\mathcal O_X)
\cong
\bigoplus_{P\in X}K/\mathcal O_{X,P}.
\]

::: pf-proof

Take global sections of the isomorphism in step [](#s13){.pf-ref}. As noted in step [](#s12){.pf-ref}, the direct sum is computed sectionwise on the noetherian space $X$, so its global sections are the direct sum of the skyscraper groups.

:::

:::

::: {.pf-step #s15}

Every finite collection of principal parts on $\mathbb P^1$ is the collection of principal parts of a single rational function.

::: pf-proof

Choose the affine coordinate
\[
x
\]
on
\[
\mathbb A^1=\mathbb P^1\setminus\{\infty\}.
\]
Let a finite tuple
\[
(\xi_P)_P
\in
\bigoplus_{P\in X}K/\mathcal O_{X,P}
\]
be given.

At a finite point
\[
P=a\in k,
\]
the local parameter is
\[
x-a.
\]
Every class
\[
\xi_a\in K/\mathcal O_{X,a}
\]
has a unique representative consisting of its finite polar part
\[
p_a(x)
=
\sum_{m=1}^{N_a}
\frac{c_{a,m}}{(x-a)^m}.
\]

At infinity, take the local parameter
\[
t=1/x.
\]
Every class
\[
\xi_\infty\in K/\mathcal O_{X,\infty}
\]
has a unique finite polar representative
\[
p_\infty(t)
=
\sum_{m=1}^{N_\infty}d_mt^{-m}
=
\sum_{m=1}^{N_\infty}d_mx^m.
\]

Now define
\[
f(x)
=
p_\infty(1/x)
+
\sum_{a\in k}p_a(x),
\]
where only the finitely many $a$ in the support of the given tuple occur.

For a fixed finite point $a$, every summand $p_b$ with $b\ne a$ is regular at $a$, and the polynomial $p_\infty(1/x)$ is also regular there.
Thus the principal part of $f$ at $a$ is exactly $p_a$.

At infinity, every term
\[
\frac{1}{(x-a)^m}
\]
tends to zero in the parameter $t=1/x$ and is regular there, while the polynomial part has precisely the prescribed principal part $p_\infty$.
Hence $f$ realizes every prescribed component $\xi_P$.

:::

:::

::: {.pf-step #s16}

The map on global sections
\[
\Gamma(X,\mathcal K)
\longrightarrow
\Gamma(X,\mathcal K/\mathcal O_X)
\]
is surjective.

::: pf-proof

Since $X$ is irreducible,
\[
\Gamma(X,\mathcal K)=K.
\]
By step [](#s14){.pf-ref}, a section of the quotient is a finite collection of principal parts.
Step [](#s15){.pf-ref} constructs a rational function whose image in every
\[
K/\mathcal O_{X,P}
\]
is that prescribed principal part.
Hence every global section of the quotient is in the image of $K$.

:::

:::

::: {.pf-step #s17}

Therefore
\[
\boxed{
0
\longrightarrow
\Gamma(X,\mathcal O_X)
\longrightarrow
\Gamma(X,\mathcal K)
\longrightarrow
\Gamma(X,\mathcal K/\mathcal O_X)
\longrightarrow0
}
\]
is exact.

::: pf-proof

Left exactness of global sections applied to
\[
0\to\mathcal O_X\to\mathcal K\to\mathcal K/\mathcal O_X\to0
\]
gives exactness at the first two terms.
Step [](#s16){.pf-ref} gives surjectivity of the final map.

Equivalently, the kernel consists of rational functions with no pole anywhere on $\mathbb P^1$, hence the global regular functions, which are the constants $k$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove (a), steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove (b), steps [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref} prove (c), steps [](#s9){.pf-ref}, [](#s10){.pf-ref}, [](#s11){.pf-ref}, [](#s12){.pf-ref} and [](#s13){.pf-ref} prove (d), and steps [](#s14){.pf-ref}, [](#s15){.pf-ref}, [](#s16){.pf-ref} and [](#s17){.pf-ref} prove (e).

:::

:::

:::
