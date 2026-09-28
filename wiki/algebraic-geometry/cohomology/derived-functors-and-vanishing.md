---
title: Derived functors and vanishing
order: 3
topics:
- Derived Functors
- Flasque Sheaves
- Vanishing Theorems
---

# Derived functors and vanishing

[[D-COHDER]]

Any resolution of $\mcf$ by $\globsec{X;\wait}$-acyclic sheaves computes $H^*(X,\mcf)$.

[[D-COHFLQ]]

Since flasque sheaves are $\globsec{X;\wait}$-acyclic, a flasque resolution, such as the Godement resolution, computes sheaf cohomology.

[[D-SHFFINE]]

[[D-COHGODEMENT]]

## Affine and Grothendieck vanishing

[[T-COHAFF]]

[[T-COHGROTH]]

For a quasicoherent sheaf $\mcf$ on a noetherian separated scheme $X$ with a finite affine open cover $\mathfrak U$, every finite intersection of members of $\mathfrak U$ is affine, affine vanishing makes $\mcf$ acyclic on each of them, and so the Čech complex of $\mathfrak U$ computes $H^*(X,\mcf)$ ([[D-PTIW0]]).
Grothendieck vanishing holds for every sheaf of abelian groups on a noetherian topological space, with bound $\dim X$.
Affine vanishing fails for sheaves that are not quasicoherent: on $X=\AA^1_k$ with distinct closed points $P,Q$, $U=X\setminus\{P,Q\}$, and $j\colon U\hookrightarrow X$, the sequence $0\to j_!\ZZ_U\to\ZZ_X\to\ZZ_P\oplus\ZZ_Q\to0$, with skyscraper sheaves $\ZZ_P,\ZZ_Q$, gives $H^1(X,j_!\ZZ_U)\cong\ZZ^2/\ZZ\neq0$, because $\ZZ_X$ is flasque on the irreducible space $X$ [@Har10a, Exercise III.2.1].

## The long exact sequence

[[PR-COHLES]]

For a closed subscheme $Y\subseteq\PP^n$ with ideal sheaf $\mci_Y$, the twisted ideal sequence $0\to\mci_Y(d)\to\OO_{\PP^n}(d)\to\OO_Y(d)\to0$ and $H^i(\PP^n,\OO(d))=0$ for $0<i<n$ give $H^i(Y,\OO_Y(d))\cong H^{i+1}(\PP^n,\mci_Y(d))$ for $1\le i\le n-2$.
For a $k$-rational point $p$ on a curve over $k$, the skyscraper sequence $0\to\OO(D-p)\to\OO(D)\to k(p)\to0$ gives $\ell(D)-1\le\ell(D-p)\le\ell(D)$.

## The six operations

[[D-SHFSIX]]

[[T-LADICPROPER]]
