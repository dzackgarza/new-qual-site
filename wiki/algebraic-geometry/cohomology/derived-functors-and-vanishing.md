---
title: Derived functors and vanishing
order: 3
topics:
- Derived Functors
- Flasque Sheaves
- Vanishing Theorems
---

# Derived functors and vanishing

Sheaf cohomology is the right derived functor of the global-sections functor $\Gamma(X,-)$, so $H^i(X,\mcf)=R^i\Gamma(X,-)(\mcf)$: it is computed from an injective resolution of $\mcf$, and equivalently from any resolution by $\Gamma(X,-)$-acyclic sheaves ([[D-COHDER]]).

[[D-COHDER]]

The definition needs enough injectives, and the category of sheaves of abelian groups has them: embedding each stalk in an injective group and pushing the product forward along the inclusions of the points produces an injective sheaf containing $\mcf$ ([[D-COHDER]]).
A resolution by acyclic sheaves computes the same groups, and the functors $(H^i)_{i\ge0}$ are the universal cohomological $\delta$-functor extending global sections ([[D-COHDER]]).

## Acyclic resolutions

[[D-COHFLQ]]

[[D-COHGODEMENT]]

Injective sheaves are flasque, flasque sheaves are acyclic for global sections, and every sheaf embeds in the flasque sheaf of discontinuous sections $\prod_x j^x_*\mcf_x$, so flasque resolutions exist for every sheaf ([[D-COHFLQ]]).
Iterating the construction gives the Godement resolution, which is functorial in the sheaf and involves no choice of injective resolution, so $H^i(X,\mcf)$ is the cohomology of $\globsec{X;\mathcal G^\bullet(\mcf)}$ ([[D-COHGODEMENT]]).
For a continuous map $f\colon X\to Y$, pushforwards of flasque sheaves are flasque and flasque sheaves are $f_*$-acyclic, so $R^if_*\mcf$ is computed by $f_*\mathcal G^\bullet(\mcf)$ ([[D-COHGODEMENT]]).

## Fine and soft resolutions

[[D-SHFFINE]]

On a paracompact Hausdorff space, flasque and fine sheaves are soft and soft sheaves are acyclic, so a resolution by fine sheaves also computes the cohomology ([[D-SHFFINE]]).
On a locally compact Hausdorff space the same holds for $c$-soft sheaves and compactly supported sections, $R^i\Gamma_c(X,\mcf)=0$ for $i>0$ ([[D-SHFFINE]]).

## Affine and Grothendieck vanishing

[[T-COHAFF]]

[[T-COHGROTH]]

For $A$ noetherian and $\mcf$ quasicoherent on $\Spec A$, one has $H^0(\Spec A,\mcf)=\Gamma(\Spec A,\mcf)$ and $H^i(\Spec A,\mcf)=0$ for $i>0$ ([[T-COHAFF]]).
Quasicoherence is the hypothesis that carries the theorem: on $X=\AA^1_k$ with distinct closed points $P,Q$, $U=X\setminus\{P,Q\}$, and $j\colon U\hookrightarrow X$, the sequence $0\to j_!\ZZ_U\to\ZZ_X\to\ZZ_P\oplus\ZZ_Q\to0$, with skyscraper sheaves $\ZZ_P,\ZZ_Q$, gives $H^1(X,j_!\ZZ_U)\cong\ZZ^2/\ZZ\neq0$, because $\ZZ_X$ is flasque on the irreducible space $X$ [@Har77, Exercise III.2.1].
For a noetherian topological space of dimension $n$, $H^i(X,\mcf)=0$ for every sheaf of abelian groups $\mcf$ and every $i>n$ ([[T-COHGROTH]]); the bound is sharp, since $H^n(\PP^n,\OO(-n-1))\neq0$ ([[T-COHGROTH]]).

## The long exact sequence

[[PR-COHLES]]

## The six operations

[[D-SHFSIX]]

[[T-LADICPROPER]]
