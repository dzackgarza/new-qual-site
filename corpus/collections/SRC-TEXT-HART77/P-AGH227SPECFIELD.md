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
$$
S=\Spec K.
$$
Since $K$ is a field, $S$ has a single point, which we denote by $\eta$, and
$$
\OO_{S,\eta}=K
$$
with maximal ideal $(0)$.

::: pf

::: {.pf-step #f-determines-point-and-local-hom}
A morphism
$$
f:S\longrightarrow X
$$
determines a point
$$
x=f(\eta)\in X
$$
and a local ring homomorphism
$$
f_\eta^\sharp:
\OO_{X,x}
\longrightarrow K.
$$

::: pf-proof
The underlying continuous map sends the unique point $\eta$ to a point $x\in X$.  Since a morphism of schemes is a morphism of locally ringed spaces, its induced map on stalks at $\eta$ is
$$
\OO_{X,f(\eta)}
\longrightarrow
\OO_{S,\eta}=K,
$$
and this homomorphism is local by definition.
:::

:::

::: {.pf-step #kernel-is-mx}
The kernel of the local homomorphism in step [](#f-determines-point-and-local-hom){.pf-ref} is exactly
$$
\mfm_x.
$$

::: pf-proof
For a local ring homomorphism
$$
\phi:(A,\mfm_A)
\longrightarrow
(B,\mfm_B),
$$
one has
$$
\phi^{-1}(\mfm_B)=\mfm_A.
$$
Here the target is the field $K$, whose maximal ideal is
$$
\mfm_K=(0).
$$
Thus
$$
\ker f_\eta^\sharp
=(f_\eta^\sharp)^{-1}(0)
=\mfm_x.
$$
:::

:::

::: {.pf-step #residue-field-embeds-in-k}
Hence $f$ determines an injective field homomorphism
$$
\boxed{
\kappa(x)
=\OO_{X,x}/\mfm_x
\hookrightarrow K.
}
$$

::: pf-proof
By step [](#kernel-is-mx){.pf-ref}, the stalk map factors through the quotient by its kernel:
$$
\OO_{X,x}
\longrightarrow
\OO_{X,x}/\mfm_x
\longrightarrow
K.
$$
The second map has zero kernel, again by step [](#kernel-is-mx){.pf-ref}, and is therefore injective.  Both source and target are fields.
:::

:::

::: {.pf-step #f-continuous-map-construction}
Conversely, suppose we are given a point $x\in X$ and an injective field homomorphism
$$
\iota:\kappa(x)\hookrightarrow K.
$$
Define a continuous map
$$
f:S\longrightarrow X
$$
by
$$
f(\eta)=x.
$$

::: pf-proof
The only nonempty subset of the one-point space $S$ is $S$ itself.  For an open set $U\subseteq X$,
$$
f^{-1}(U)
=
\begin{cases}
S,&x\in U,\\
\varnothing,&x\notin U.
\end{cases}
$$
Both subsets are open, so $f$ is continuous.
:::

:::

::: {.pf-step #fsharp-sheaf-morphism-construction}
Define a sheaf morphism
$$
f^\sharp:\OO_X\longrightarrow f_*\OO_S
$$
as follows.  For an open $U\subseteq X$ containing $x$, put
$$
f_U^\sharp:
\OO_X(U)
\longrightarrow
\OO_{X,x}
\longrightarrow
\kappa(x)
\xrightarrow{\iota}
K
=(f_*\OO_S)(U),
$$
where the first map takes a section to its germ at $x$.  If $x\notin U$, use the unique map
$$
\OO_X(U)\longrightarrow0
=(f_*\OO_S)(U).
$$

::: pf-proof
If
$$
V\subseteq U
$$
and both contain $x$, taking the germ at $x$ after restriction gives the same element of $\OO_{X,x}$ as taking the germ directly.  Thus the displayed maps commute with restrictions.

If $x\notin V$, the target over $V$ is the zero ring, so compatibility is automatic.  Hence the maps $f_U^\sharp$ define a morphism of sheaves of rings.
:::

:::

::: {.pf-step #pair-is-scheme-morphism}
The pair $(f,f^\sharp)$ from steps [](#f-continuous-map-construction){.pf-ref} and [](#fsharp-sheaf-morphism-construction){.pf-ref} is a morphism of schemes.

::: pf-proof
The only stalk map to check is at the point $\eta\in S$.  It is
$$
\OO_{X,x}
\longrightarrow
\kappa(x)
\xrightarrow{\iota}
K.
$$
Its kernel is
$$
\mfm_x,
$$
because the quotient map has that kernel and $\iota$ is injective.  Since the maximal ideal of $K$ is zero,
$$
(f_\eta^\sharp)^{-1}(0)
=\mfm_x.
$$
Thus the stalk map is local, so $(f,f^\sharp)$ is a morphism of locally ringed spaces and hence a morphism of schemes.
:::

:::

::: {.pf-step #morphism-to-pair-recovers-morphism}
Starting with a morphism $f:S\to X$, extracting the pair
$$
(x,\kappa(x)\hookrightarrow K)
$$
and applying the construction of steps [](#f-continuous-map-construction){.pf-ref}, [](#fsharp-sheaf-morphism-construction){.pf-ref} and [](#pair-is-scheme-morphism){.pf-ref} recovers the original morphism.

::: pf-proof
The underlying point is clearly the same point
$$
x=f(\eta).
$$
For every open $U$ containing $x$, the original sheaf map
$$
\OO_X(U)\to K
$$
factors through the stalk map
$$
\OO_{X,x}\to K,
$$
because the stalk map is induced from the sheaf morphism.  By steps [](#kernel-is-mx){.pf-ref} and [](#residue-field-embeds-in-k){.pf-ref} this stalk map is exactly the quotient
$$
\OO_{X,x}\to\kappa(x)
$$
followed by the extracted embedding into $K$.  This is precisely the formula in step [](#fsharp-sheaf-morphism-construction){.pf-ref}.  On opens not containing $x$, both maps land in the zero ring.  Hence the entire morphism is recovered.
:::

:::

::: {.pf-step #pair-to-morphism-recovers-pair}
Starting with a pair
$$
(x,\iota:\kappa(x)\hookrightarrow K),
$$
constructing a morphism and then extracting its residue-field map recovers the same pair.

::: pf-proof
The constructed continuous map sends the unique point of $S$ to $x$.  Its stalk map is
$$
\OO_{X,x}
\to\kappa(x)
\xrightarrow{\iota}K.
$$
Passing to the quotient by the maximal ideal therefore gives exactly the original embedding $\iota$.
:::

:::

::: {.pf-step #hom-speck-x-bijection}
Therefore there is a natural bijection
$$
\boxed{
\Hom_{\Sch}(\Spec K,X)
\cong
\left\{
(x,\iota) \st
x\in X,
\ \iota:\kappa(x)\hookrightarrow K
\right\}.
}
$$

::: pf-proof
Steps [](#morphism-to-pair-recovers-morphism){.pf-ref} and [](#pair-to-morphism-recovers-pair){.pf-ref} show that the two constructions are inverse.
:::

:::

::: pf-qed
Step [](#hom-speck-x-bijection){.pf-ref} is the equivalence requested in the exercise.
:::

:::

:::
