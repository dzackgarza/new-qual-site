---
schema: qual/card@1
id: P-AGH364UNIVERSALDELTA
kind: problem
title: Sheaf Ext as a universal delta-functor
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ext Sheaves
  - Delta Functors
  - Locally Free Sheaves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the contravariant universal delta-functor assertion and coeffaceability hint with the retained Hartshorne III.6.4 transcription. Applied Theorem III.1.3A on the opposite coherent category; the required vanishing is for sheaf Ext from finite-rank locally free sheaves, not for global Ext.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a noetherian scheme, and suppose that every coherent sheaf on $X$ is a quotient of a locally free sheaf of finite rank.
In this case we say $\Coh(X)$ has enough locally frees.
Then for any $\mcg \in \Mod(X)$, show that the $\delta$-functor $(\mathcal{E}xt^i(\wait, \mcg))$, from $\Coh(X)$ to $\Mod(X)$ is a contravariant universal $\delta$-functor.
:::

::: {.hint}
Show $\mathcal{E}xt^i(\wait, \mcg)$ is coeffaceable for $i>0$.
:::

::: {.solution}
Fix $\mcg$ and put $T^i(F)=\mathcal{E}xt_X^i(F,\mcg)$ for $F\in\Coh(X)$.
Regard this contravariant functor as a covariant functor on the abelian category $\Coh(X)^{\mathrm{op}}$.

<1>1. The functors $T^i$ form a cohomological $\delta$-functor on $\Coh(X)^{\mathrm{op}}$, with $T^0(F)=\sheafhom_X(F,\mcg)$.

::: {.proof}
The category of coherent sheaves on a noetherian scheme is abelian, and its inclusion into $\Mod(X)$ is exact [@Har10a, Proposition II.5.7].
The long exact sheaf-Ext sequence in the first variable therefore applies to every short exact sequence in $\Coh(X)$ [@Har10a, Proposition III.6.4].
Reversing that short exact sequence gives a short exact sequence in the opposite category, with the variance required for a covariant cohomological $\delta$-functor.
The degree-zero identification is the definition of sheaf Ext as the right derived functors of [[D-MODOX|sheaf Hom]] in the second variable.
The boundary maps are natural by that same long exact sequence construction.
:::

<1>2. If $E$ is locally free of finite rank, then $\mathcal{E}xt_X^i(E,\mcg)=0$ for every $i>0$.

::: {.proof}
The functor $\sheafhom_X(E,-)$ is isomorphic to $E^\vee\otimes_{\OO_X}-$.
In a local frame it is a finite direct sum of copies of the identity functor, and hence is exact.
Applying it to an injective resolution of $\mcg$ consequently leaves an exact augmented complex.
Its positive-degree cohomology sheaves, which define $\mathcal{E}xt_X^i(E,\mcg)$, vanish.
This is also the locally free special case of [@Har10a, Proposition III.6.5].
:::

<1>3. Each $T^i$ for $i>0$ is coeffaceable on $\Coh(X)$, and hence effaceable on its opposite category.

::: {.proof}
For any coherent $F$, the hypothesis supplies an epimorphism $E\twoheadrightarrow F$ with $E$ locally free of finite rank.
Such $E$ is coherent, so this is an epimorphism in $\Coh(X)$.
Contravariance gives
$$
T^i(F)\longrightarrow T^i(E)=0
\qquad(i>0)
$$
by step <1>2.
Thus the induced map is zero, which is exactly coeffaceability.
In $\Coh(X)^{\mathrm{op}}$, the same arrow is a monomorphism $F\to E$, and it effaces $T^i(F)$ in the covariant sense.
The same epimorphism works for every positive degree.
:::

<1>4. Q.E.D.

::: {.proof}
By the effaceability criterion [@Har10a, Theorem III.1.3A], a cohomological $\delta$-functor whose positive-degree terms are effaceable is universal.
Apply it to the functor on $\Coh(X)^{\mathrm{op}}$ in step <1>1, using step <1>3.
Consequently every natural transformation from $T^0$ to the degree-zero part of another contravariant $\delta$-functor extends uniquely to a morphism of $\delta$-functors.
This is the requested contravariant universality.
:::
:::
