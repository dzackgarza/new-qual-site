---
schema: qual/card@1
id: P-AGH245VALCENTER
kind: problem
title: Centers of valuations on separated and proper schemes
classification:
  areas:
  - algebraic-geometry
  topics:
  - Valuative Criteria
  - Valuation Rings
  - Proper Morphisms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against Hartshorne II.4.5 and the refined Noetherian valuative criteria for separatedness and properness.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: problem
Let $X$ be an integral scheme of finite type over a field $k$, having function field $K$.
We say that a valuation of $K/k$ has **center** $x$ on $X$ if its valuation ring $R$ dominates the local ring $\OO_{x, X}$.

a. If $X$ is separated over $k$, then the center of any valuation of $K/k$ on $X$, if it exists, is unique.

b. If $X$ is proper over $k$, then every valuation of $K/k$ has a unique center on $X$.
   Note: if $X$ is a variety over $k$, the criterion of (b) is sometimes taken as the definition of a complete variety.

c. Prove the converses of (a) and (b). *Hint:* while (a) and (b) follow easily from (4.3) and (4.7), their converses require some comparison of valuations in different fields.

d. If $X$ is proper over $k$, and if $k$ is algebraically closed, show that $\Gamma(X, \OO_X) = k$.
   This result generalizes (I, 3.4a). *Hint:* let $a \in \Gamma(X, \OO_X)$ with $a \not\in k$.
   Show that there is a valuation ring $R$ of $K/k$ with $\inverseof{a} \in \mfm_R$, then use (b) to get a contradiction.
:::

::: {.solution}
Let
\[
\eta\in X
\]
be the generic point, so
\[
\kappa(\eta)=K(X)=K.
\]

<1>1. Let $R\subseteq K$ be a valuation ring containing $k$.
Giving a center $x\in X$ of $R$ is equivalent to giving a $k$-morphism
\[
\widetilde\eta:\Spec R\longrightarrow X
\]
whose restriction to the generic point
\[
\Spec K\subseteq\Spec R
\]
is the canonical morphism
\[
\Spec K\longrightarrow X
\]
with image $\eta$.
::: {.proof}
Suppose first that $x$ is a center.
By definition,
\[
\mathcal O_{X,x}\subseteq R
\]
and
\[
\mathfrak m_x
=
\mathcal O_{X,x}\cap\mathfrak m_R.
\]
Thus the inclusion
\[
\mathcal O_{X,x}\longrightarrow R
\]
is a local homomorphism.
A local homomorphism from the local ring at $x$ to a local ring defines a unique morphism
\[
\Spec R\longrightarrow X
\]
sending the closed point to $x$.
On fraction fields this is the identity map
\[
K(X)=K\longrightarrow K,
\]
so the generic point maps canonically to $\eta$.

Conversely, let such a morphism $\widetilde\eta$ be given and let $x$ be the image of the closed point of $\Spec R$.
The induced homomorphism
\[
\mathcal O_{X,x}\longrightarrow R
\]
is local because morphisms of schemes are morphisms of locally ringed spaces.
Its restriction on the generic point is the identity on $K$, hence it identifies $\mathcal O_{X,x}$ with a subring of $R$.
Therefore $R$ dominates $\mathcal O_{X,x}$, so $x$ is a center.
:::

<1>2. If $X$ is separated over $k$, every valuation of $K/k$ has at most one center on $X$.
::: {.proof}
Let $R$ be a valuation ring of $K/k$.
Two centers would, by <1>1, give two morphisms
\[
\Spec R\rightrightarrows X
\]
whose restrictions to
\[
\Spec K
\]
are both the canonical generic-point morphism.

The valuative criterion for separatedness says that a separated morphism has at most one such lift.  Therefore the two morphisms, and hence their closed-point images, coincide.
:::

<1>3. If $X$ is proper over $k$, every valuation of $K/k$ has a unique center on $X$.
::: {.proof}
Let $R$ be a valuation ring of $K/k$.  Consider the diagram
\[
\begin{array}{ccc}
\Spec K&\longrightarrow&X\\
\downarrow&&\downarrow\\
\Spec R&\longrightarrow&\Spec k.
\end{array}
\]
The valuative criterion for properness gives a unique dotted lift
\[
\Spec R\longrightarrow X.
\]
By <1>1 this lift is exactly a unique center of $R$ on $X$.
:::

<1>4. We use the refined Noetherian valuative criterion in the converse direction.
For a finite-type morphism
\[
T\longrightarrow S
\]
with $S$ locally noetherian, separatedness and properness may be tested using only discrete valuation rings whose fraction field is the residue field of the generic point of an irreducible component of $T$, with the generic point mapping canonically to that component.
::: {.proof}
This is the refined Noetherian valuative criterion; see the Stacks Project, Lemmas 32.15.2 and 32.15.3.

The comparison of valuations in different fields mentioned in Hartshorne's hint is the content of the reduction to these generic-component valuation rings.  Since the present $X$ is integral, it has only one irreducible component and its generic residue field is exactly $K(X)=K$.
:::

<1>5. Conversely, suppose every valuation of $K/k$ has at most one center on $X$.
Then $X$ is separated over $k$.
::: {.proof}
Let
\[
R\subseteq K
\]
be any discrete valuation ring containing $k$ with fraction field $K$.
By hypothesis, $R$ has at most one center on $X$.
By <1>1, the diagram
\[
\begin{array}{ccc}
\Spec K&\longrightarrow&X\\
\downarrow&&\downarrow\\
\Spec R&\longrightarrow&\Spec k
\end{array}
\]
has at most one lift.

Thus the generic-component uniqueness condition of the refined valuative criterion <1>4 holds.  Since $X$ is of finite type over the field $k$, that criterion implies
\[
X\longrightarrow\Spec k
\]
is separated.
:::

<1>6. Conversely, suppose every valuation of $K/k$ has a unique center on $X$.
Then $X$ is proper over $k$.
::: {.proof}
For every discrete valuation ring
\[
R\subseteq K
\]
containing $k$ and having fraction field $K$, the hypothesis and <1>1 say that the generic-point valuative diagram has exactly one lift
\[
\Spec R\longrightarrow X.
\]

The existence-and-uniqueness condition in the refined valuative criterion <1>4 therefore holds.  Since $X$ is of finite type over the noetherian scheme $\Spec k$, the criterion implies that
\[
X\longrightarrow\Spec k
\]
is proper.
:::

<1>7. Parts (a)--(c) therefore give the equivalences
\[
\boxed{
X\text{ separated over }k
\iff
\text{every valuation of }K/k\text{ has at most one center on }X,
}
\]
and
\[
\boxed{
X\text{ proper over }k
\iff
\text{every valuation of }K/k\text{ has exactly one center on }X.
}
\]
::: {.proof}
The forward implications are <1>2--<1>3, and the converses are <1>5--<1>6.
:::

<1>8. Assume now that $X$ is proper over an algebraically closed field $k$, and let
\[
a\in\Gamma(X,\mathcal O_X).
\]
If $a\notin k$, then $a$ is transcendental over $k$.
::: {.proof}
Because $X$ is integral, restriction to the generic point gives an injection
\[
\Gamma(X,\mathcal O_X)\hookrightarrow K(X)=K.
\]

If $a$ were algebraic over the algebraically closed field $k$, then $a\in k$.  Thus $a\notin k$ forces $a$ to be transcendental.
:::

<1>9. Under the assumption $a\notin k$, there is a valuation ring
\[
R\subseteq K
\]
of $K/k$ such that
\[
a^{-1}\in\mathfrak m_R.
\]
::: {.proof}
Since $a$ is transcendental over $k$, the subfield
\[
k(a)\subseteq K
\]
is a rational function field.
Consider the discrete valuation ring at infinity
\[
A_0
=
k[a^{-1}]_{(a^{-1})}
\subseteq k(a)\subseteq K.
\]
Its maximal ideal is generated by $a^{-1}$.

By the valuation-ring existence theorem, any local subring of a field is dominated by a valuation ring of that field.
Thus there is a valuation ring
\[
R\subseteq K
\]
with fraction field $K$ which dominates $A_0$; see the Stacks Project, Lemma 10.50.2.

Because $k\subseteq A_0\subseteq R$, this is a valuation of $K/k$.  Domination gives
\[
a^{-1}\in\mathfrak m_{A_0}
\subseteq
\mathfrak m_R.
\]
:::

<1>10. The valuation ring from <1>9 cannot have a center on $X$.
::: {.proof}
Suppose it had center $x$.
Then
\[
\mathcal O_{X,x}\subseteq R.
\]
The global regular function $a$ has a germ
\[
a_x\in\mathcal O_{X,x},
\]
so
\[
a\in R.
\]

But <1>9 also gives
\[
a^{-1}\in\mathfrak m_R.
\]
Since $a\in R$ is the inverse of $a^{-1}$, the element $a^{-1}$ is a unit of $R$, contradicting membership in the maximal ideal.
:::

<1>11. Therefore every global regular function on $X$ lies in $k$:
\[
\boxed{\Gamma(X,\mathcal O_X)=k.}
\]
::: {.proof}
If some $a\in\Gamma(X,\mathcal O_X)$ lay outside $k$, <1>9--<1>10 would produce a valuation of $K/k$ with no center on $X$.
This contradicts properness and part (b), proved in <1>3.

The reverse inclusion
\[
k\subseteq\Gamma(X,\mathcal O_X)
\]
is the structure map of the $k$-scheme $X$.  Hence equality holds.
:::

<1>12. Q.E.D.
::: {.proof}
Steps <1>2, <1>3, <1>5--<1>7, and <1>11 prove parts (a), (b), (c), and (d), respectively.
:::
:::
