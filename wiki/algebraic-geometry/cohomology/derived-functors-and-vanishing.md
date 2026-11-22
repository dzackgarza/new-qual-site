---
title: Derived functors and vanishing
order: 3
topics:
- Derived Functors
- Flasque Sheaves
- Vanishing Theorems
---

# Derived functors and vanishing

Sheaf cohomology is the right derived functor of the global-sections functor, so $H^i(X,\mcf)=R^i\Gamma(X,-)(\mcf)$ is computed from an injective resolution of $\mcf$ and, equally, from any resolution by sheaves on which $\Gamma(X,-)$ is acyclic ([[D-COHDER]]).
Two things have to be supplied before that definition is usable: the category of sheaves of abelian groups must have enough injectives, and there must be a supply of acyclic sheaves with which a resolution can be written down without appealing to the axiom of choice on injectives.
The flasque sheaves are that supply, and they produce the basic vanishing theorems: on an affine scheme quasicoherent sheaves have no higher cohomology, and on a noetherian space of dimension $n$ every sheaf has vanishing cohomology above degree $n$.

## Sheaf cohomology as a derived functor

[[D-COHDER]]

The global-section functor is left exact, so it has right derived functors as soon as injectives exist, and they exist: embedding each stalk $\mcf_x$ in an injective abelian group and taking the product of the pushforwards along $\theset{x}\injects X$ produces an injective sheaf containing $\mcf$ ([[D-COHDER]]).
The result does not depend on the injective resolution chosen, and more is true: a resolution $\mcf\to\mca^\bullet$ by $\Gamma(X,-)$-acyclic sheaves computes the same groups, $H^i(X,\mcf)\cong H^i\bigl(\Gamma(X,\mca^\bullet)\bigr)$ [@Har77, Proposition III.1.2A] ([[D-COHDER]]).
The functors $(H^i)_{i\ge0}$ are the universal cohomological $\delta$-functor extending $\Gamma(X,-)$ [@Har77, Corollary III.1.4], which is what makes the long exact sequence of a short exact sequence of sheaves automatic rather than a separate theorem.

## Flasque sheaves

[[D-COHFLQ]]

Flasqueness is the combinatorial condition that every restriction map $\mcf(U)\to\mcf(V)$ is surjective; an injective $\OO_X$-module is flasque [@Har77, Lemma III.2.4], and a flasque sheaf is acyclic for global sections, $H^i(X,\mcf)=0$ for every $i>0$ [@Har77, Proposition III.2.5] ([[D-COHFLQ]]).
The second implication is proved by dimension shifting: for a flasque $\mcf$ embedded in an injective $\mci$, the quotient $\mcg=\mci/\mcf$ is again flasque [@Har77, Exercise II.1.16], the sequence of global sections stays exact because the left term is flasque, and the long exact sequence identifies $H^i(X,\mcf)$ with $H^{i-1}(X,\mcg)$ so induction applies.
Every sheaf embeds in the flasque sheaf of discontinuous sections $\prod_x j^x_*\mcf_x$ [@Har77, Exercise II.1.16], so flasque resolutions always exist and may replace injective ones in the definition of $H^i$ [@Har77, Remark III.2.5.1] ([[D-COHFLQ]]).

## The Godement resolution

[[D-COHGODEMENT]]

Iterating the discontinuous-sections construction gives a resolution $\mcf\to\mathcal G^\bullet(\mcf)$ whose every term is flasque, which is functorial in $\mcf$ and carries short exact sequences of sheaves to short exact sequences of complexes ([[D-COHGODEMENT]]).
So $H^i(X,\mcf)=H^i\bigl(\Gamma(X,\mathcal G^\bullet(\mcf))\bigr)$ with no choice made anywhere, and for a continuous map $f\colon X\to Y$ the same argument with $f_*$ in place of $\Gamma(X,-)$ computes the higher direct images: flasque sheaves are $f_*$-acyclic because pushforward preserves flasqueness, so $R^if_*\mcf\cong\mathcal H^i\bigl(f_*\mathcal G^\bullet(\mcf)\bigr)$ [@Har77, Exercise II.1.16] ([[D-COHGODEMENT]]).
The functoriality is the point: a comparison of two constructions of a sheaf gives a comparison of their cohomology, with no resolutions to choose and no zig-zag to check.

## Soft and fine sheaves

[[D-SHFFINE]]

On a paracompact Hausdorff space the analytic argument replaces flasqueness by a partition of unity: a fine sheaf admits endomorphisms $\eta_i$ with supports in the members of a locally finite cover and $\sum_i\eta_i=\id$, and gluing $\eta_i(t_i)$ for local lifts $t_i$ produces a global section extending a given section of a closed subset, so a fine sheaf is soft ([[D-SHFFINE]]).
Soft sheaves are acyclic for global sections, so any resolution by fine sheaves computes the cohomology; on a locally compact Hausdorff space the same holds for $c$-soft sheaves and compactly supported sections, $R^i\Gamma_c(X,\mcf)=0$ for $i>0$ ([[D-SHFFINE]]).
This is the mechanism by which the de Rham and Dolbeault complexes of a manifold compute its cohomology, and it is where the difference between the algebraic and the analytic settings sits: Zariski opens are not paracompact in the relevant sense, so the algebraic theory has no partitions of unity and uses flasque sheaves instead.

## Vanishing on an affine scheme

[[T-COHAFF]]

For $X=\Spec A$ noetherian and $\mcf$ quasicoherent, $H^i(X,\mcf)=0$ for every $i>0$ [@Har77, Theorem III.3.5] ([[T-COHAFF]]).
The hypothesis on the sheaf is not removable, and the failure is not a technicality of the proof.
On $X=\AA^1_k$ over an infinite field, with distinct closed points $P,Q$ and $U=X\sm\theset{P,Q}$, the extension by zero $j_!\ZZ_U$ sits in
$$
0\to j_!\ZZ_U\to\ZZ_X\to\ZZ_P\oplus\ZZ_Q\to0 ,
$$
and $H^0(\ZZ_X)=\ZZ$ while $H^0(\ZZ_P\oplus\ZZ_Q)=\ZZ^2$; since $\ZZ_X$ is flasque on the irreducible space $X$, $H^1(X,\ZZ_X)=0$, so $H^1(X,j_!\ZZ_U)\cong\ZZ^2/\ZZ\neq0$ [@Har77, Exercise III.2.1].
The sheaf $j_!\ZZ_U$ is a sheaf of abelian groups that is not quasicoherent, so this is consistent with affine vanishing; and since the constant sheaf $\ZZ_U$ on the irreducible $U$ is itself flasque [@Har77, Exercise II.1.16], the example also shows that $j_!$, although exact, does not carry acyclic sheaves to acyclic sheaves.

## Grothendieck vanishing

[[T-COHGROTH]]

If $X$ is a noetherian topological space of dimension $n$, then $H^i(X,\mcf)=0$ for all $i>n$ and every sheaf of abelian groups $\mcf$ on $X$ [@Har77, Theorem III.2.7] ([[T-COHGROTH]]).
No quasicoherence is needed, because the bound comes from the length of a chain of closed subsets rather than from the sheaf: the proof reduces to the constant sheaf on an irreducible space by noetherian induction.
The bound is sharp, and the same example shows it: on $\AA^1_k$ the sheaf $j_!\ZZ_U$ has $H^1\neq0$ although $\dim X=1$, so vanishing in degree $n$ cannot hold in general [@Har77, Exercise III.2.1].
On $\PP^n$ the bound is attained: $H^i(\PP^n,\OO(d))=0$ for $i>n$ and for $0<i<n$, so only degree $0$ and degree $n$ carry cohomology ([[T-IJW1K]]).

## The long exact sequence and Čech computation

[[PR-COHLES]]

Every short exact sequence of sheaves of abelian groups gives a long exact sequence, natural in morphisms of short exact sequences, and the connecting map $\delta$ is what classifies obstructions: a section of $\mcf''$ lifts to $\mcf$ exactly when its image under $\delta$ vanishes ([[PR-COHLES]]).
For quasicoherent sheaves on a noetherian separated scheme the Čech complex of a finite affine open cover computes the same groups, $\check H^p(\mcu,\mcf)\cong H^p(X,\mcf)$, which is what makes cohomology computable in practice [@Har77, Theorem III.4.5] ([[D-PTIW0]]).
The computation on $\PP^n$ and its consequences are on [[algebraic-geometry/cohomology/computing-cohomology|computing cohomology]] ([[T-IJW1K]]).

## Dévissage

[[D-COHDEVISSAGE]]

A coherent sheaf on a noetherian scheme has a finite filtration whose successive quotients are pushforwards of ideal sheaves on integral closed subschemes, so a property of coherent sheaves that passes to extensions along such a filtration may be checked on those quotients alone ([[D-COHDEVISSAGE]]).
Vanishing and finiteness statements are of this kind, which is why they are usually proved for an ideal sheaf on an integral subscheme and then transported.

## The six operations

[[D-SHFSIX]]

For a morphism of locally compact Hausdorff spaces the four functors $f^{-1}\dashv Rf_*$ and $Rf_!\dashv f^!$, together with the derived tensor and sheaf Hom adjunction, satisfy base change and the projection formula, and $Rf_!=Rf_*$ when $f$ is proper ([[D-SHFSIX]]).
The proper-support pushforward is the topological shadow of compactly supported cohomology, and in the algebraic setting it is what makes a constructible sheaf's higher direct images constructible: for $f$ separated of finite type between schemes of finite type over a field, $R^if_!\mcf$ is constructible $\ell$-adic for $\mcf$ constructible, and for $f$ proper the same holds for $R^if_*$ ([[T-LADICPROPER]]).
