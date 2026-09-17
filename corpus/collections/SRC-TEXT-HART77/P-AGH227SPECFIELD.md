---
schema: qual/card@1
id: P-AGH227SPECFIELD
kind: problem
title: Morphisms from the spectrum of a field are points with residue field inclusions
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Residue Fields
  - Points
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.2.7 statement and source-order placement after II.2.6.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a scheme.
For any $x \in X$, let $\OO_x$ be the local ring at $x$ and $\mfm_x$ its maximal ideal.
Define the residue field of $x$ on $X$ to be the field $k(x) = \OO_x / \mfm_x$.

Now let $K$ be any field.
Show that to give a morphism $\Spec K \to X$ is equivalent to giving a point $x \in X$ together with an inclusion map $k(x) \to K$.
:::

::: {.solution}
Let
\[
S=\operatorname{Spec}K.
\]
Since $K$ is a field, $S$ has a single point, which we denote by $\eta$, and
\[
\mathcal O_{S,\eta}=K
\]
with maximal ideal $(0)$.

<1>1. A morphism
\[
f:S\longrightarrow X
\]
determines a point
\[
x=f(\eta)\in X
\]
and a local ring homomorphism
\[
f_\eta^\sharp:
\mathcal O_{X,x}
\longrightarrow K.
\]
::: {.proof}
The underlying continuous map sends the unique point $\eta$ to a point $x\in X$.  Since a morphism of schemes is a morphism of locally ringed spaces, its induced map on stalks at $\eta$ is
\[
\mathcal O_{X,f(\eta)}
\longrightarrow
\mathcal O_{S,\eta}=K,
\]
and this homomorphism is local by definition.
:::

<1>2. The kernel of the local homomorphism in <1>1 is exactly
\[
\mathfrak m_x.
\]
::: {.proof}
For a local ring homomorphism
\[
\phi:(A,\mathfrak m_A)
\longrightarrow
(B,\mathfrak m_B),
\]
one has
\[
\phi^{-1}(\mathfrak m_B)=\mathfrak m_A.
\]
Here the target is the field $K$, whose maximal ideal is
\[
\mathfrak m_K=(0).
\]
Thus
\[
\ker f_\eta^\sharp
=(f_\eta^\sharp)^{-1}(0)
=\mathfrak m_x.
\]
:::

<1>3. Hence $f$ determines an injective field homomorphism
\[
\boxed{
\kappa(x)
=\mathcal O_{X,x}/\mathfrak m_x
\hookrightarrow K.
}
\]
::: {.proof}
By <1>2, the stalk map factors through the quotient by its kernel:
\[
\mathcal O_{X,x}
\longrightarrow
\mathcal O_{X,x}/\mathfrak m_x
\longrightarrow
K.
\]
The second map has zero kernel, again by <1>2, and is therefore injective.  Both source and target are fields.
:::

<1>4. Conversely, suppose we are given a point $x\in X$ and an injective field homomorphism
\[
\iota:\kappa(x)\hookrightarrow K.
\]
Define a continuous map
\[
f:S\longrightarrow X
\]
by
\[
f(\eta)=x.
\]
::: {.proof}
The only nonempty subset of the one-point space $S$ is $S$ itself.  For an open set $U\subseteq X$,
\[
f^{-1}(U)
=
\begin{cases}
S,&x\in U,\\
\varnothing,&x\notin U.
\end{cases}
\]
Both subsets are open, so $f$ is continuous.
:::

<1>5. Define a sheaf morphism
\[
f^\sharp:\mathcal O_X\longrightarrow f_*\mathcal O_S
\]
as follows.  For an open $U\subseteq X$ containing $x$, put
\[
f_U^\sharp:
\mathcal O_X(U)
\longrightarrow
\mathcal O_{X,x}
\longrightarrow
\kappa(x)
\xrightarrow{\iota}
K
=(f_*\mathcal O_S)(U),
\]
where the first map takes a section to its germ at $x$.  If $x\notin U$, use the unique map
\[
\mathcal O_X(U)\longrightarrow0
=(f_*\mathcal O_S)(U).
\]
::: {.proof}
If
\[
V\subseteq U
\]
and both contain $x$, taking the germ at $x$ after restriction gives the same element of $\mathcal O_{X,x}$ as taking the germ directly.  Thus the displayed maps commute with restrictions.

If $x\notin V$, the target over $V$ is the zero ring, so compatibility is automatic.  Hence the maps $f_U^\sharp$ define a morphism of sheaves of rings.
:::

<1>6. The pair $(f,f^\sharp)$ from <1>4--<1>5 is a morphism of schemes.
::: {.proof}
The only stalk map to check is at the point $\eta\in S$.  It is
\[
\mathcal O_{X,x}
\longrightarrow
\kappa(x)
\xrightarrow{\iota}
K.
\]
Its kernel is
\[
\mathfrak m_x,
\]
because the quotient map has that kernel and $\iota$ is injective.  Since the maximal ideal of $K$ is zero,
\[
(f_\eta^\sharp)^{-1}(0)
=\mathfrak m_x.
\]
Thus the stalk map is local, so $(f,f^\sharp)$ is a morphism of locally ringed spaces and hence a morphism of schemes.
:::

<1>7. Starting with a morphism $f:S\to X$, extracting the pair
\[
(x,\kappa(x)\hookrightarrow K)
\]
and applying the construction of <1>4--<1>6 recovers the original morphism.
::: {.proof}
The underlying point is clearly the same point
\[
x=f(\eta).
\]
For every open $U$ containing $x$, the original sheaf map
\[
\mathcal O_X(U)\to K
\]
factors through the stalk map
\[
\mathcal O_{X,x}\to K,
\]
because the stalk map is induced from the sheaf morphism.  By <1>2--<1>3 this stalk map is exactly the quotient
\[
\mathcal O_{X,x}\to\kappa(x)
\]
followed by the extracted embedding into $K$.  This is precisely the formula in <1>5.  On opens not containing $x$, both maps land in the zero ring.  Hence the entire morphism is recovered.
:::

<1>8. Starting with a pair
\[
(x,\iota:\kappa(x)\hookrightarrow K),
\]
constructing a morphism and then extracting its residue-field map recovers the same pair.
::: {.proof}
The constructed continuous map sends the unique point of $S$ to $x$.  Its stalk map is
\[
\mathcal O_{X,x}
\to\kappa(x)
\xrightarrow{\iota}K.
\]
Passing to the quotient by the maximal ideal therefore gives exactly the original embedding $\iota$.
:::

<1>9. Therefore there is a natural bijection
\[
\boxed{
\operatorname{Hom}_{\mathrm{Sch}}(\operatorname{Spec}K,X)
\cong
\left\{
(x,\iota):
x\in X,
\ \iota:\kappa(x)\hookrightarrow K
\right\}.
}
\]
::: {.proof}
Steps <1>7 and <1>8 show that the two constructions are inverse.
:::

<1>10. Q.E.D.
::: {.proof}
Step <1>9 is the equivalence requested in the exercise.
:::
:::
