---
title: Ringed spaces
order: 6
topics:
- Locally Ringed Spaces
- Structure Sheaf
- Morphisms Of Schemes
---

# Ringed spaces

Before there is a scheme there is a topological space carrying a sheaf of rings, and before there is a morphism of schemes there is a continuous map carrying a map of sheaves the wrong way.
The definitions are short, and everything in the rest of the chapter is an instance of them; the one clause that has to be understood rather than memorised is the one that asks the maps on stalks to be local, because that clause is what makes the algebra of a ring visible in the geometry of its spectrum.

## Ringed and locally ringed spaces

[[D-AN662]]

The structure sheaf is a sheaf of rings and not merely a sheaf of sets: the restriction maps are ring homomorphisms, so a section can be added and multiplied over an open set and the result is again a section over that set.
A morphism is therefore a pair, and the direction of $f^\sharp\colon\OO_Y\to f_*\OO_X$ is the direction that lets a function on $Y$ be pulled back along $f$ — the same direction as the pullback of a differential form, and the opposite direction of $f$ itself.

## Why locality is the extra clause

On stalks, $f^\sharp$ gives for each $p\in X$ a ring map $f_p\colon\OO_{Y,f(p)}\to\OO_{X,p}$, and $f$ is a morphism of locally ringed spaces when $f_p$ carries the maximal ideal of $\OO_{Y,f(p)}$ into that of $\OO_{X,p}$.
Dropping the clause enlarges the category past anything a ring map can produce: the card above contains a morphism $\Spec K\to\Spec R$ of ringed spaces, for a discrete valuation ring $R$ with fraction field $K$, that sends the generic point of $\Spec K$ to the closed point of $\Spec R$ and is not local.
Its map on global sections is the inclusion $R\injects K$, which is also the ring map behind the morphism of schemes $\Spec K\to\Spec R$ sending the generic point to the generic point; the two morphisms of ringed spaces agree on global sections and differ only at one point, so no condition on sections detects the difference and the stalk condition is the only one that does.
With the clause, a morphism of schemes gives for each $p$ an inclusion of residue fields $\kappa(f(p))\hookrightarrow\kappa(p)$, so a point of $X$ maps to a point of $Y$ together with a way of reading the functions at the second as functions at the first.
That is the precise sense in which the topological map is determined by the algebra, and it is the reason $\Spec$ can be an anti-equivalence of categories rather than a functor ([[T-SK599]]).

## Stalks and germs

[[D-0QSI0]]

Locality is a condition on stalks, and a section is determined by its germ at every point, so every condition on a morphism of locally ringed spaces can be read one point at a time.
The same is true of the sheaf axioms themselves: a section over an open cover glues when the germs agree, which is the statement that the structure sheaf is a subsheaf of the product of its stalks.
In a locally ringed space the maximal ideal $\mfm_p\subseteq\OO_{X,p}$ is what makes the phrase "the value of a function at $p$" mean something: a global section $s\in\OO_X(X)$ has a value $s(p)\in\kappa(p)\coloneqq\OO_{X,p}/\mfm_p$, and $s$ is a unit at $p$ exactly when that value is nonzero.

## Schemes as the local models

A scheme is then a locally ringed space covered by open subspaces each isomorphic, as a locally ringed space, to $\Spec A$ for some ring $A$; the single model object is therefore the whole content of the theory, and $\Spec A$ with its structure sheaf is a locally ringed space whose stalks are the localisations $A_\mfp$ ([[D-VKR54]]).
Two consequences of the definition are used constantly.
First, a morphism $X\to\Spec\ZZ[t]$ is the same thing as a global section of $\OO_X$, because a ring map $\ZZ[t]\to\OO_X(X)$ is determined by the image of $t$; this is the first case of the functor of points ([[PR-SCHFOP]]).
Second, being a scheme is a local property of a locally ringed space, so a space glued from affine pieces along open immersions is a scheme without any further checking ([[algebraic-geometry/schemes/proj-and-gluing|Proj and gluing]]).

## Where the chapter goes next

The structure sheaf of $\Spec A$ and the criterion for recognising an affine scheme are the subject of [[algebraic-geometry/schemes/what-is-a-scheme|what is a scheme]]; the points of a scheme, and the residue field attached to each, are the subject of [[algebraic-geometry/schemes/subschemes-and-points|subschemes and points]].
