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

(a) Let $Y$ be a closed subset of $X$.
For each open set $U \subseteq X$, let $\mci_Y(U)$ be the ideal in the ring $\OO_X(U)$ consisting of those regular functions which vanish at all points of $Y \intersect U$.
Show that the presheaf $U \mapsto \mci_Y(U)$ is a sheaf.
It is called the \dfn{sheaf of ideals} $\mci_Y$ of $Y$, and it is a subsheaf of the sheaf of rings $\OO_X$.

(b) If $Y$ is a subvariety, show that the quotient sheaf $\OO_X / \mci_Y$ is isomorphic to $i_* \OO_Y$, where $i: Y \to X$ is the inclusion and $\OO_Y$ is the sheaf of regular functions on $Y$.

(c) Now let $X = \PP^1$ and let $Y$ be the union of two distinct points $P, Q \in X$.
Then with $\mcf = i_* \OO_P \oplus i_* \OO_Q$ there is an exact sequence of sheaves on $X$
$$
0 \to \mci_Y \to \OO_X \to \mcf \to 0.
$$
Show however that the induced map on global sections $\Gamma(X, \OO_X) \to \Gamma(X, \mcf)$ is not surjective.
This shows that the global section functor $\Gamma(X, \wait)$ is not exact.

(d) Again let $X = \PP^1$ and let $\OO$ be the sheaf of regular functions.
Let $\mck$ be the constant sheaf on $X$ associated to the function field $K$ of $X$.
Show that there is a natural injection $\OO \to \mck$.
Show that the quotient sheaf $\mck / \OO$ is isomorphic to the direct sum of sheaves $\bigoplus_{P \in X} i_P(I_P)$, where $I_P$ is the group $K/\OO_P$ and $i_P(I_P)$ denotes the skyscraper sheaf given by $I_P$ at the point $P$.

(e) Finally, show that in the case of (d) the sequence
$$
0 \to \Gamma(X, \OO) \to \Gamma(X, \mck) \to \Gamma(X, \mck/\OO) \to 0
$$
is exact.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For a closed subset $Y\subseteq X$, the assignment
$$
\mci_Y(U)
=
\{f\in\OO_X(U) \st f\restrict_{Y\cap U}=0\text{ pointwise}\}
$$
is a subpresheaf of rings of $\OO_X$.

::: pf-proof

If $V\subseteq U$ and
$$
f\in\mci_Y(U),
$$
then for every
$$
P\in Y\cap V
\subseteq
Y\cap U
$$
one has
$$
(f\restrict_V)(P)=f(P)=0.
$$
Thus
$$
f\restrict_V\in\mci_Y(V).
$$
The set $\mci_Y(U)$ is clearly an ideal of $\OO_X(U)$, since sums of functions vanishing on $Y\cap U$ vanish there and multiplying by an arbitrary regular function preserves vanishing.

:::

:::

::: {.pf-step #s2}

The presheaf $\mci_Y$ is a sheaf, hence a sheaf of ideals in $\OO_X$.

::: pf-proof

Let
$$
U=\bigcup_iU_i
$$
and suppose compatible sections
$$
f_i\in\mci_Y(U_i)
$$
are given.
Since $\OO_X$ is a sheaf, the $f_i$ glue uniquely to
$$
f\in\OO_X(U).
$$

For any point
$$
P\in Y\cap U,
$$
choose $i$ with $P\in U_i$.
Then
$$
f(P)=f_i(P)=0.
$$
Thus
$$
f\in\mci_Y(U).
$$
Uniqueness is inherited from $\OO_X$.
Hence $\mci_Y$ is a sheaf.

:::

:::

::: {.pf-step #s3}

If $Y$ is a subvariety and
$$
i:Y\hookrightarrow X
$$
is the inclusion, restriction of regular functions gives a sheaf morphism
$$
\rho:\OO_X\longrightarrow i_*\OO_Y
$$
whose kernel is $\mci_Y$.

::: pf-proof

For every open $U\subseteq X$, restriction gives
$$
\rho_U:\OO_X(U)
\longrightarrow
\OO_Y(U\cap Y).
$$
These maps commute with further restrictions, so they define a sheaf morphism.

By definition,
$$
f\in\ker\rho_U
$$
exactly when $f$ vanishes as a regular function on $U\cap Y$, equivalently when it vanishes at every point of $U\cap Y$.
This is precisely
$$
f\in\mci_Y(U).
$$
Thus
$$
\ker\rho=\mci_Y.
$$

:::

:::

::: {.pf-step #s4}

The morphism $\rho$ is surjective as a morphism of sheaves.

::: pf-proof

It suffices to check surjectivity on stalks.

If $P\notin Y$, then
$$
(i_*\OO_Y)_P=0,
$$
so surjectivity is automatic.

Let $P\in Y$.
Choose an affine open neighborhood $V$ of $P$, with affine coordinate ring $A$.
Then $Y\cap V$ is a closed subvariety of $V$ whose affine coordinate ring is $A/I$, where $I$ is the ideal of $Y\cap V$ in $A$.
If $\mfm \subseteq A$ is the maximal ideal of $P$, the map on stalks is
$$
A_{\mfm }
\longrightarrow
(A/I)_{\mfm /I},
$$
which is surjective.
Hence $\rho$ is surjective at every stalk.

:::

:::

::: {.pf-step #s5}

Therefore
$$
\boxed{
\OO_X/\mci_Y
\cong
i_*\OO_Y.
}
$$

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} give an exact sequence
$$
0\longrightarrow\mci_Y
\longrightarrow\OO_X
\xrightarrow{\rho}i_*\OO_Y
\longrightarrow0.
$$
The sheaf first-isomorphism theorem gives the displayed quotient isomorphism.

:::

:::

::: {.pf-step #s6}

Let now
$$
X=\PP^1_k,
\qquad
Y=\{P,Q\}
$$
for distinct $k$-points $P,Q$, and let
$$
\mcf=i_{P*}\OO_P\oplus i_{Q*}\OO_Q.
$$
Then
$$
0\longrightarrow\mci_Y
\longrightarrow\OO_X
\longrightarrow\mcf
\longrightarrow0
$$
is exact.

::: pf-proof

The reduced subvariety $Y$ is the disjoint union of the two points $P$ and $Q$, so
$$
\OO_Y
\cong
\OO_P\oplus\OO_Q
$$
as a sheaf on $Y$.
Therefore
$$
i_*\OO_Y
\cong
i_{P*}\OO_P\oplus i_{Q*}\OO_Q
=\mcf.
$$
Apply the exact sequence from step [](#s5){.pf-ref}.

:::

:::

::: {.pf-step #s7}

The induced map on global sections
$$
\Gamma(X,\OO_X)
\longrightarrow
\Gamma(X,\mcf)
$$
is not surjective.

::: pf-proof

Every global regular function on the projective integral curve $\PP^1_k$ is constant, so
$$
\Gamma(X,\OO_X)=k.
$$
On the other hand,
$$
\Gamma(X,\mcf)
\cong
k\oplus k.
$$
The restriction map sends
$$
c\longmapsto(c,c).
$$
Its image is the diagonal subspace of $k\oplus k$, which does not contain, for example,
$$
(1,0).
$$
Hence the map is not surjective.

:::

:::

::: {.pf-step #s8}

Thus the global-section functor is left exact but not exact.

::: pf-proof

Applying global sections to the short exact sequence of step [](#s6){.pf-ref} gives
$$
0\to
\Gamma(X,\mci_Y)
\to
\Gamma(X,\OO_X)
\to
\Gamma(X,\mcf),
$$
which is exact at the first two terms because $\Gamma$ is left exact.
Step [](#s7){.pf-ref} shows that the last map need not be surjective, so $\Gamma$ is not right exact and hence not exact.

:::

:::

::: {.pf-step #s9}

Continue with $X=\PP^1_k$.
Let
$$
K=k(X)
$$
be its function field and let $\mck$ be the constant sheaf associated to the abelian group $K$.
There is a natural injection
$$
\boxed{\OO_X\hookrightarrow\mck.}
$$

::: pf-proof

Every nonempty open subset of the irreducible variety $X$ is irreducible, so the constant sheaf $\mck$ has
$$
\mck(U)=K
$$
for every nonempty open $U$.

A regular function on a nonempty open $U$ is, by definition, a rational function regular at every point of $U$.
Thus there is a natural injective map
$$
\OO_X(U)\hookrightarrow K=\mck(U).
$$
These inclusions commute with restriction, giving the sheaf morphism.
It is injective on every open set, hence a monomorphism.

:::

:::

::: {.pf-step #s10}

For every point $P\in X$, the stalk of the quotient sheaf is
$$
\boxed{
(\mck/\OO_X)_P
\cong
K/\OO_{X,P}
=:I_P.
}
$$

::: pf-proof

Sheaf stalks are exact.
Taking the stalk at $P$ of
$$
0\longrightarrow\OO_X
\longrightarrow\mck
\longrightarrow\mck/\OO_X
\longrightarrow0
$$
gives
$$
0\longrightarrow\OO_{X,P}
\longrightarrow\mck_P
\longrightarrow
(\mck/\OO_X)_P
\longrightarrow0.
$$
Since $X$ is irreducible,
$$
\mck_P=K,
$$
so the quotient stalk is $K/\OO_{X,P}$.

:::

:::

::: {.pf-step #s11}

A section of $\mck/\OO_X$ over an open set $U$ has nonzero germ at only finitely many points of $U$.

::: pf-proof

The support of any section of a sheaf is closed in $U$.
We show more directly that it is finite.

Every point of $U$ has a neighborhood on which the section is represented by a section of $\mck$, hence by one rational function in $K$.
Since $X=\PP^1_k$ is noetherian, the open set $U$ is quasicompact, so finitely many such neighborhoods cover $U$.

A rational function on the nonsingular projective curve $\PP^1$ has only finitely many poles.
On a neighborhood where the quotient section is represented by a rational function $f$, its germ is zero at every point where $f$ is regular.
Thus the support on that neighborhood is contained in the finite pole set of $f$.

Taking the finite union over a finite cover shows that the support of the original section is finite.

:::

:::

::: {.pf-step #s12}

Sending a section to its germs defines a sheaf morphism
$$
\Phi:
\mck/\OO_X
\longrightarrow
\bigoplus_{P\in X}i_P(I_P).
$$

::: pf-proof

By Hartshorne II.1.11, direct sums of sheaves on the noetherian space $X$ are computed sectionwise as filtered direct limits of finite direct sums.
Hence
$$
\left(\bigoplus_{P\in X}i_P(I_P)\right)(U)
\cong
\bigoplus_{P\in U}I_P,
$$
the group of finite-support tuples.

Given
$$
s\in(\mck/\OO_X)(U),
$$
define
$$
\Phi_U(s)=(s_P)_{P\in U}.
$$
By step [](#s11){.pf-ref} this tuple has finite support, so it belongs to the direct sum.
Taking germs is compatible with restriction, so the maps $\Phi_U$ form a sheaf morphism.

:::

:::

::: {.pf-step #s13}

The morphism $\Phi$ is an isomorphism:
$$
\boxed{
\mck/\OO_X
\cong
\bigoplus_{P\in X}i_P(I_P).
}
$$

::: pf-proof

It suffices to check the map on stalks.

At a point $Q\in X$, step [](#s10){.pf-ref} gives
$$
(\mck/\OO_X)_Q=I_Q.
$$
On the right, the stalk of the $Q$th skyscraper is $I_Q$, while every skyscraper supported at a different closed point has zero stalk at $Q$.
Thus
$$
\left(\bigoplus_{P\in X}i_P(I_P)\right)_Q
\cong I_Q.
$$
Under these identifications, $\Phi_Q$ is the identity map on $I_Q$.
Therefore $\Phi$ is an isomorphism at every stalk, hence an isomorphism of sheaves.

:::

:::

::: {.pf-step #s14}

Consequently,
$$
\Gamma(X,\mck/\OO_X)
\cong
\bigoplus_{P\in X}K/\OO_{X,P}.
$$

::: pf-proof

Take global sections of the isomorphism in step [](#s13){.pf-ref}. As noted in step [](#s12){.pf-ref}, the direct sum is computed sectionwise on the noetherian space $X$, so its global sections are the direct sum of the skyscraper groups.

:::

:::

::: {.pf-step #s15}

Every finite collection of principal parts on $\PP^1$ is the collection of principal parts of a single rational function.

::: pf-proof

Choose the affine coordinate
$$
x
$$
on
$$
\AA^1=\PP^1\setminus\{\infty\}.
$$
Let a finite tuple
$$
(\xi_P)_P
\in
\bigoplus_{P\in X}K/\OO_{X,P}
$$
be given.

At a finite point
$$
P=a\in k,
$$
the local parameter is
$$
x-a.
$$
Every class
$$
\xi_a\in K/\OO_{X,a}
$$
has a unique representative consisting of its finite polar part
$$
p_a(x)
=
\sum_{m=1}^{N_a}
\frac{c_{a,m}}{(x-a)^m}.
$$

At infinity, take the local parameter
$$
t=1/x.
$$
Every class
$$
\xi_\infty\in K/\OO_{X,\infty}
$$
has a unique finite polar representative
$$
p_\infty(t)
=
\sum_{m=1}^{N_\infty}d_mt^{-m}
=
\sum_{m=1}^{N_\infty}d_mx^m.
$$

Now define
$$
f(x)
=
p_\infty(1/x)
+
\sum_{a\in k}p_a(x),
$$
where only the finitely many $a$ in the support of the given tuple occur.

For a fixed finite point $a$, every summand $p_b$ with $b\ne a$ is regular at $a$, and the polynomial $p_\infty(1/x)$ is also regular there.
Thus the principal part of $f$ at $a$ is exactly $p_a$.

At infinity, every term
$$
\frac{1}{(x-a)^m}
$$
tends to zero in the parameter $t=1/x$ and is regular there, while the polynomial part has precisely the prescribed principal part $p_\infty$.
Hence $f$ realizes every prescribed component $\xi_P$.

:::

:::

::: {.pf-step #s16}

The map on global sections
$$
\Gamma(X,\mck)
\longrightarrow
\Gamma(X,\mck/\OO_X)
$$
is surjective.

::: pf-proof

Since $X$ is irreducible,
$$
\Gamma(X,\mck)=K.
$$
By step [](#s14){.pf-ref}, a section of the quotient is a finite collection of principal parts.
Step [](#s15){.pf-ref} constructs a rational function whose image in every
$$
K/\OO_{X,P}
$$
is that prescribed principal part.
Hence every global section of the quotient is in the image of $K$.

:::

:::

::: {.pf-step #s17}

Therefore
$$
\boxed{
0
\longrightarrow
\Gamma(X,\OO_X)
\longrightarrow
\Gamma(X,\mck)
\longrightarrow
\Gamma(X,\mck/\OO_X)
\longrightarrow0
}
$$
is exact.

::: pf-proof

Left exactness of global sections applied to
$$
0\to\OO_X\to\mck\to\mck/\OO_X\to0
$$
gives exactness at the first two terms.
Step [](#s16){.pf-ref} gives surjectivity of the final map.

Equivalently, the kernel consists of rational functions with no pole anywhere on $\PP^1$, hence the global regular functions, which are the constants $k$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove (a), steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove (b), steps [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref} prove (c), steps [](#s9){.pf-ref}, [](#s10){.pf-ref}, [](#s11){.pf-ref}, [](#s12){.pf-ref} and [](#s13){.pf-ref} prove (d), and steps [](#s14){.pf-ref}, [](#s15){.pf-ref}, [](#s16){.pf-ref} and [](#s17){.pf-ref} prove (e).

:::

:::

:::

::: {.remark}
Part (e) is an analogue of the first Cousin problem in several complex variables; see Gunning and Rossi.
:::
