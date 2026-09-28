---
title: Quasicoherence and twisting
order: 1
topics:
- Quasicoherent Sheaves
- Line Bundles
- Twisting Sheaves
---

# Quasicoherence and twisting

[[D-QNTZY]]

A sheaf of $\OO_X$-modules $\mcf$ is quasicoherent exactly when every point has an open neighbourhood $U$ with an exact sequence $\OO_U^{(J)}\to\OO_U^{(I)}\to\mcf|_U\to0$.
For a morphism $X\to S$ and affine opens $\Spec B\subseteq X$ and $\Spec A\subseteq S$ with $\Spec B$ mapping into $\Spec A$, $\Omega_{X/S}|_{\Spec B}\cong\widetilde{\Omega_{B/A}}$.

## The twists

[[D-CB9XS]]

[[FE-SHFPONE]]

For $S=k[x_0,\ldots,x_n]$, $H^0(\PP^n_k,\OO(d))=S_d$ for $d\ge0$.
For a closed subscheme $X=V(I)\subseteq\PP^n_k$, the Hilbert polynomial of $S/I$ from [[algebraic-geometry/varieties/dimension-and-degree|dimension and degree]] equals $h^0(X,\OO_X(d))$ for $d\gg0$.

Every coherent sheaf on $\PP^n_A$ is a quotient of a finite sum of twists $\OO(-d_i)$.
By descending induction on $i$, starting above $n$ where $H^i$ vanishes, finiteness of $H^i(\PP^n_A,\mcf)$ for coherent $\mcf$ and noetherian $A$ follows from finiteness of $H^i(\PP^n_A,\OO(d))$.
