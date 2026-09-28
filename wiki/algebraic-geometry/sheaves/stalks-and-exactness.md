---
title: Stalks and exactness
order: 2
topics:
- Stalks
- Exact Sequences
- Cohomology
---

# Stalks and exactness

Sheaves of abelian groups on $X$ form an abelian category, and a sequence of them is exact exactly when it is exact on every stalk.

[[PR-C9ZEK]]

A surjection of sheaves need not be surjective on global sections.

[[FE-Y12XB]]

[[FE-DNTT6]]

[[FE-SHFISOSTALKS]]

[[PR-SHFPUSHEX]]

## The obstruction to a global lift

Lifting a global section of $\mch$ is possible over each member of some open cover, by the definition of surjectivity.
The lifts differ on overlaps by sections of $\mcf$, and those differences form a Čech $1$-cocycle.
The section lifts globally exactly when that cocycle is a coboundary, so the obstruction lives in $H^1(X, \mcf)$ and the long exact sequence
\[
0 \to \mcf(X) \to \mcg(X) \to \mch(X) \to H^1(X, \mcf) \to \cdots
\]
records it; see [[algebraic-geometry/cohomology/index|cohomology]].

## Locally constant and constructible sheaves

[[D-SHFLOCSYS]]

[[D-SHFCONSTR]]

## Support

[[D-UDIVH]]

The support of a sheaf need not be closed: for an open immersion $j\colon U\hookrightarrow X$, extension by zero gives $\supp(j_!\ZZ_U)=U$.
For a coherent sheaf on a noetherian scheme, the support is closed.
