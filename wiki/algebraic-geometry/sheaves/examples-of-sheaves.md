---
title: Examples of sheaves
order: 3
topics:
- Sheaves
- Skyscraper Sheaves
- Local Systems
---

# Examples of sheaves

The sheaf axioms are short and the examples decide what they mean.
Four families recur in this chapter and in everything after it: the constant and locally constant sheaves, which carry no information beyond the gluing data of a cover; the skyscraper sheaves, which are the simplest sheaves whose cohomology vanishes for the trivial reason; the sheaves of functions, which are why a space can be recovered from its ring of functions; and the presheaf that fails an axiom, which shows what the axioms buy by showing what is lost without them.

## Constant and locally constant sheaves

[[D-SHFLOCSYS]]

A constant sheaf records nothing about $X$: its sections over an open set are the continuous maps to a discrete group, so on a connected open set there is exactly one section per element.
A locally constant sheaf does record something, and the monodromy theorem above says exactly what — a representation of the fundamental group — which is why local systems are the geometric form of a group representation and why they appear wherever a family is locally trivial but globally twisted.
On an irreducible space, and in particular on the underlying space of an irreducible scheme, every constant sheaf is flabby, and this is the fact behind the vanishing of higher cohomology of a constant sheaf on an irreducible noetherian space.

## Skyscraper sheaves

::: {.definition title="Skyscraper sheaf"}
Let $X$ be a topological space, $p\in X$ a point, and $A$ an abelian group.
Write $i_p\colon\theset{p}\hookrightarrow X$ for the inclusion of the one-point subspace, and let $A$ also denote the constant sheaf on that point.
The \dfn{skyscraper sheaf} at $p$ with value $A$ is $(i_p)_*A$, the sheaf whose sections over an open $U$ are $A$ when $p\in U$ and $0$ otherwise.
:::

Its stalk is $A$ at $p$ and $0$ at every other point, which is the whole of its local information: a skyscraper is determined by one group at one point.
Every open cover of $X$ splits into the sets containing $p$, on which the sections are all of $A$, so the sheaf is flabby, and a flabby sheaf is acyclic for global sections ([[D-COHFLQ]]); hence $H^i(X,A_p)=0$ for $i>0$.
A point of a scheme carries no cohomology, and the skyscraper is the sheaf that says so.
On an affine scheme the skyscraper at a closed point is the quasicoherent sheaf attached to $A/\mfm$, so it is also the standard example of a quasicoherent sheaf whose support is a single point ([[D-UDIVH]]).

[[FE-SHFPONE]]

The sequence in that example is the standard way a skyscraper arises in practice: a section of a line bundle vanishes at a point, and the quotient by the subsheaf of sections vanishing there is the skyscraper at that point.

## Sheaves of functions

::: {.example title="Sheaves of functions"}
On a topological space $X$ the assignment $U\mapsto C^0(U,\RR)$ of continuous real-valued functions is a sheaf of rings.
On a smooth manifold the assignment $U\mapsto C^\infty(U)$ is a subsheaf of it, and on a complex manifold the assignment $U\mapsto\OO_X^{an}(U)$ of holomorphic functions is a subsheaf of that.
The same three assignments can be made on the open sets of a scheme with regular functions in place of smooth ones ([[D-VARREG]]).
:::

Each of these is a sheaf for the same reason: a function is continuous, smooth, or holomorphic exactly when its restriction to every member of an open cover is, and the values on overlaps determine the glued function.
The stalks of the holomorphic sheaf are rings of convergent power series, which are local rings, so a complex manifold is a locally ringed space and the maximal ideal at a point is the ideal of functions vanishing there ([[algebraic-geometry/schemes/ringed-spaces|ringed spaces]]).
The sheaf of holomorphic functions is a proper subsheaf of the sheaf of continuous functions, and the exponential shows the difference on global sections: $\exp$ is onto on stalks and not onto on $\OO_X(X)$ when $X=\CC\sm\theset{0}$ ([[FE-DNTT6]]).

## A presheaf that is not a sheaf

[[FE-AM5Z8]]

The card above separates the two failures: the constant presheaf fails to glue on a disconnected open set, the presheaf of continuous functions modulo bounded ones is not determined by its local data, and the presheaf $U\mapsto\mcf(U)\tensor\mcg(U)$ has sections on the two standard charts of $\PP^1$ that agree on the overlap and glue nowhere.
A presheaf is a sheaf exactly when both axioms hold, and sheafification repairs the gluing one ([[T-3VX80]]).

## Stalks do not determine a sheaf

[[FE-SHFISOSTALKS]]

A map of sheaves that is an isomorphism on every stalk is an isomorphism, but a family of sheaves with isomorphic stalks need not be isomorphic, and pushforward is where the difference is visible: the stalk of a pushforward is not the pushforward of the stalks.

## Constructible sheaves

[[D-SHFCONSTR]]

The examples above are the two extremes, locally constant and supported at a point, and a constructible sheaf is what a finite stratification between them produces.
They are the sheaves for which the six operations close up, which is why the proper base change and vanishing theorems are stated for constructible coefficients rather than for all sheaves ([[T-LADICPROPER]]).
