---
title: Ringed spaces
order: 6
topics:
- Locally Ringed Spaces
- Structure Sheaf
- Morphisms Of Schemes
---

# Ringed spaces

[[D-AN662]]

## Local morphisms

A morphism $(f,f^\sharp)$ of ringed spaces is a morphism of locally ringed spaces when for each $p\in X$ the induced map $f^\sharp_p\colon\OO_{Y,f(p)}\to\OO_{X,p}$ is a local homomorphism: $(f^\sharp_p)^{-1}(\mfm_p)=\mfm_{f(p)}$ [@Har77, Section II.2].
Without that condition the category is larger than the one $\Spec$ maps into: for a discrete valuation ring $R$ with fraction field $K$ there is a morphism of ringed spaces $\Spec K\to\Spec R$ carrying the generic point to the closed point whose stalk map is $R\into K$, and its inverse image of $\mfm_K=0$ is $0\neq\mfm_R$ ([[D-AN662]]).
With the condition a morphism of schemes induces $\kappa(f(p))\hookrightarrow\kappa(p)$ for every $p$, and $\Spec$ is an anti-equivalence between rings and affine schemes ([[T-SK599]]).

## Stalks and germs

[[D-0QSI0]]

For a sheaf $\mcf$ on $X$ the map $\mcf(U)\to\prod_{p\in U}\mcf_p$, $s\mapsto(s_p)$, is injective: a section whose germ vanishes at every point of $U$ is zero, which is axiom (3) of a sheaf [@Har77, Section II.1].
Injectivity is not the gluing axiom. A family $s_i\in\mcf(U_i)$ over an open cover with $s_i=s_j$ on $U_i\cap U_j$ must come from a section of $\mcf(U)$ [@Har77, Section II.1], and the product of the stalks imposes no compatibility between its coordinates, so an element of the product need not be a section.
For the structure sheaf, a global section $s$ has a value $s(p)\in\kappa(p)=\OO_{X,p}/\mfm_p$, and $s$ is a unit at $p$ exactly when $s(p)\neq0$ ([[D-0QSI0]]).

## Schemes

A scheme is a locally ringed space covered by open subspaces isomorphic, as locally ringed spaces, to $\Spec A$ with its structure sheaf ([[D-VKR54]]).
A morphism $X\to\Spec\ZZ[t]$ is the same thing as a global section of $\OO_X$, since a ring map $\ZZ[t]\to\OO_X(X)$ is determined by the image of $t$ ([[PR-SCHFOP]]).
Being a scheme is a local property of a locally ringed space, so a space glued from affine pieces along open immersions is a scheme ([[algebraic-geometry/schemes/proj-and-gluing|Proj and gluing]]).
