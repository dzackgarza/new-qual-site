---
schema: qual/card@1
id: P-AGH238NORMALIZATION
kind: problem
title: Normalization of an integral scheme and its universal property
classification:
  areas:
  - algebraic-geometry
  topics:
  - Integral Schemes
  - Normalization
  - Integral Closure
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.8 statement and the standard normalization universal property.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
A scheme is **normal** if all of its local rings are integrally closed domains.
Let $X$ be an integral scheme.
For each open affine subset $U = \Spec A$ of $X$, let $\tilde{A}$ be the integral closure of $A$ in its quotient field, and let $\tilde{U} = \Spec \tilde{A}$.

Show that one can glue the schemes $\tilde{U}$ to obtain a normal integral scheme $\tilde{X}$, called the **normalization** of $X$.

Show also that there is a morphism $\tilde{X} \to X$ with the following universal property: for every normal integral scheme $Z$ and every dominant morphism $f: Z \to X$, the morphism $f$ factors uniquely through $\tilde{X}$.
If $X$ is of finite type over a field $k$, then the morphism $\tilde{X} \to X$ is a finite morphism.
:::

::: {.solution}
Let
\[
K=K(X)
\]
be the function field of the integral scheme $X$.

<1>1. If $A\subseteq K$ is a domain and $S\subseteq A$ is multiplicatively closed, then the integral closure of $S^{-1}A$ in $K$ is
\[
S^{-1}\widetilde A,
\]
where $\widetilde A$ is the integral closure of $A$ in $K$.
::: {.proof}
Every element of $S^{-1}\widetilde A$ is integral over $S^{-1}A$, because integrality is preserved by localization.

Conversely, let
\[
x\in K
\]
be integral over $S^{-1}A$.  It satisfies a monic equation
\[
x^n+\frac{a_{n-1}}{s_{n-1}}x^{n-1}+\cdots+\frac{a_0}{s_0}=0.
\]
Let
\[
s=s_0s_1\cdots s_{n-1}\in S.
\]
Multiplying the equation by $s^n$ shows that $sx$ satisfies a monic polynomial with coefficients in $A$.  Hence
\[
sx\in\widetilde A,
\]
so
\[
x\in S^{-1}\widetilde A.
\]
:::

<1>2. Let
\[
U=\Spec A,
\qquad
V=\Spec B
\]
be affine open subsets of $X$.  The normalizations
\[
\widetilde U=\Spec\widetilde A,
\qquad
\widetilde V=\Spec\widetilde B
\]
have canonically isomorphic open subschemes lying over $U\cap V$.
::: {.proof}
The intersection $U\cap V$ is covered by open subsets which are distinguished in both $U$ and $V$.  Indeed, for a point of the intersection, choose a distinguished neighborhood inside $U\cap V$ in $U$, then shrink once more to a distinguished open in $V$; the same denominator-clearing argument used in Hartshorne II.3.3 makes the final open distinguished in both charts.

Thus it is enough to compare over an open
\[
W=D_A(f)=D_B(g)\subseteq U\cap V.
\]
Since $X$ is integral, II.3.6 identifies
\[
\operatorname{Frac}(A)=K=\operatorname{Frac}(B).
\]
By <1>1, the integral closure of $A_f$ in $K$ is $(\widetilde A)_f$, and the integral closure of $B_g$ in $K$ is $(\widetilde B)_g$.

But
\[
A_f\cong\Gamma(W,\mathcal O_X)\cong B_g
\]
as subrings of $K$.  Their integral closures in $K$ are therefore the same ring.  Hence
\[
D_{\widetilde U}(f)
\cong
\Spec(\widetilde A)_f
\cong
\Spec(\widetilde B)_g
\cong
D_{\widetilde V}(g).
\]
These isomorphisms are canonical because they are induced by equality inside the common field $K$.
:::

<1>3. The isomorphisms from <1>2 satisfy the cocycle condition, so the affine schemes $\widetilde U$ glue to a scheme $\widetilde X$.
::: {.proof}
On every common distinguished open, the transition isomorphism is induced by the identity map on the same subring of $K$.  Therefore on a triple overlap the composite of two transition maps is again the identity on that subring, hence equals the direct transition map.

Hartshorne II.2.12, the gluing theorem for schemes along open subschemes, therefore produces a scheme $\widetilde X$ covered by the affine schemes $\widetilde U$.
:::

<1>4. The scheme $\widetilde X$ is integral and normal.
::: {.proof}
Each $\widetilde A$ is a subring of the field $K$, hence a domain.  Thus every affine chart $\Spec\widetilde A$ is integral.

Each $\widetilde A$ is integrally closed in its fraction field $K$ by definition.  Localizations of integrally closed domains are integrally closed, so every local ring of every affine chart is integrally closed.  Hence $\widetilde X$ is normal.

The affine charts have nonempty common intersections above the generic point of $X$, because the generic point belongs to every nonempty affine open of $X$ and the localization of every $\widetilde A$ at $(0)$ is $K$.  Consequently the glued scheme is irreducible.  Being covered by spectra of domains, it is also reduced.  Thus it is integral.
:::

<1>5. The inclusions
\[
A\hookrightarrow\widetilde A
\]
on affine opens glue to a dominant morphism
\[
\boxed{\nu:\widetilde X\longrightarrow X.}
\]
::: {.proof}
Each inclusion $A\hookrightarrow\widetilde A$ induces a morphism
\[
\Spec\widetilde A\longrightarrow\Spec A.
\]
On an overlap, both morphisms are induced by the same inclusion of the common localized coordinate ring into its integral closure in $K$.  Hence the local morphisms agree on overlaps and glue.

The generic point of $\Spec\widetilde A$ is $(0)$ and contracts to $(0)$ in $A$, so the generic point of $\widetilde X$ maps to the generic point of $X$.  Therefore $\nu$ is dominant.
:::

<1>6. Let $Z$ be a normal integral scheme and let
\[
f:Z\longrightarrow X
\]
be dominant.  Then the induced map of function fields is an inclusion
\[
K(X)\hookrightarrow K(Z).
\]
::: {.proof}
The generic point of $Z$ maps to the generic point of $X$ because $f$ is dominant.  The induced local homomorphism
\[
\mathcal O_{X,\eta_X}=K(X)
\longrightarrow
\mathcal O_{Z,\eta_Z}=K(Z)
\]
is a local homomorphism between fields, hence injective.
:::

<1>7. For every affine open $U=\Spec A\subseteq X$, the restricted morphism
\[
f^{-1}(U)\longrightarrow U
\]
factors uniquely through
\[
\Spec\widetilde A\longrightarrow\Spec A.
\]
::: {.proof}
Let $W=\Spec C\subseteq f^{-1}(U)$ be an affine open.  The morphism gives an injective map
\[
A\longrightarrow C\subseteq K(Z).
\]
Take $x\in\widetilde A$.  It is integral over $A$, hence its image in $K(Z)$ is integral over $C$ as well, because the same monic polynomial has coefficients in the image of $A\subseteq C$.

The normality of $Z$ means that the domain $C$ is integrally closed in $K(Z)$.  Therefore the image of $x$ lies in $C$.  Thus the field inclusion of <1>6 restricts to a ring homomorphism
\[
\widetilde A\longrightarrow C
\]
extending $A\to C$.

These homomorphisms are compatible on smaller affine opens because all are restrictions of the same inclusion
\[
K(X)\hookrightarrow K(Z).
\]
Hence they glue on $f^{-1}(U)$ to the required factorization.

Uniqueness holds because any factorization must induce the same map on function fields and therefore the same homomorphism $\widetilde A\to C$ on every affine open $W$.
:::

<1>8. The local factorizations in <1>7 glue uniquely to a morphism
\[
\boxed{\widetilde f:Z\longrightarrow\widetilde X}
\]
such that
\[
f=\nu\circ\widetilde f.
\]
::: {.proof}
On overlaps of affine opens of $X$, the factorizations from <1>7 are all induced by the same map of function fields and the same canonical transition isomorphisms of <1>2.  They therefore agree and glue to a morphism $\widetilde f$.

The composite $\nu\circ\widetilde f$ agrees with $f$ over every affine open of $X$, hence globally.  If another morphism had the same property, its restriction over every affine open would equal the unique local factorization from <1>7, so it would equal $\widetilde f$.
:::

<1>9. Thus $\nu:\widetilde X\to X$ has the universal property of normalization:
\[
\boxed{
\begin{array}{c}
Z\text{ normal integral},\quad f:Z\to X\text{ dominant}
\\[2mm]
\Longrightarrow
\exists!\,\widetilde f:Z\to\widetilde X
\text{ with }f=\nu\circ\widetilde f.
\end{array}}
\]
::: {.proof}
This is exactly <1>8.
:::

<1>10. Assume now that $X$ is of finite type over a field $k$.  For every affine open
\[
U=\Spec A\subseteq X,
\]
the integral closure $\widetilde A$ of $A$ in $K(X)$ is a finite $A$-module.
::: {.proof}
The ring $A$ is a finitely generated integral $k$-algebra.  The standard finiteness theorem for normalization of affine varieties says that the integral closure of such a domain in a finite extension of its fraction field is finite as an $A$-module.  Apply it to the trivial finite extension
\[
K(X)/\operatorname{Frac}(A)=K(X)/K(X).
\]
Thus $\widetilde A$ is finite over $A$.
:::

<1>11. If $X$ is of finite type over $k$, then
\[
\boxed{\nu:\widetilde X\to X\text{ is finite}.}
\]
::: {.proof}
On every affine open $U=\Spec A\subseteq X$, the inverse image under $\nu$ is by construction
\[
\nu^{-1}(U)=\Spec\widetilde A,
\]
and <1>10 shows that $\widetilde A$ is finite as an $A$-module.  This is the affine-local criterion for a finite morphism proved in Hartshorne II.3.4.
:::

<1>12. Q.E.D.
::: {.proof}
Steps <1>1--<1>5 construct the normal integral scheme $\widetilde X$ and its morphism to $X$; steps <1>6--<1>9 prove the universal property; steps <1>10--<1>11 prove finiteness over a field.
:::
:::
