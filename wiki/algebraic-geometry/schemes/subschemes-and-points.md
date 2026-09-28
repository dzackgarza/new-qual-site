---
title: Subschemes and points
order: 5
topics:
- Subschemes
- Generic Points
- Dimension
---

# Subschemes and points

A closed subset of a scheme carries many closed subscheme structures and an open subset carries one open subscheme structure.

[[D-SCHSUB]]

A closed subscheme is determined by its quasicoherent ideal sheaf: $V(x)$ and $V(x^2)$ in $\AA^1$ have the same underlying point and are different closed subschemes.

[[D-SCHRED]]

[[D-SCHIMG]]

The scheme-theoretic image is the smallest closed subscheme through which the morphism factors.
For $\Spec k[\varepsilon]/(\varepsilon^2)\to\AA^1_k$, $x\mapsto\varepsilon$, it is $V(x^2)$.
By Chevalley's theorem, the set-theoretic image of a morphism of finite type of noetherian schemes is constructible; the image of $\AA^2_k\to\AA^2_k$, $(x,y)\mapsto(x,xy)$, is $\{x\neq0\}\cup\{(0,0)\}$, which is neither open nor closed.

[[PR-SCHINT]]

## Points, and dimension

[[D-SCHPTS]]

The value of $f\in\OO_X(U)$ at $x\in U$ is its image $f(x)\in\kappa(x)$.
On $\Spec\ZZ$, $15$ has value $0$ in $\FF_3$ and in $\FF_5$, value $1$ in $\FF_7$, and value $15$ in $\QQ$ at the generic point.
Specialization, $x\rightsquigarrow y$ when $y\in\overline{\{x\}}$, is a partial order on the points of $X$; for a variety over an algebraically closed field, the closed points are the points of the classical variety.
Generic points and their use in "generically" are in [[algebraic-geometry/schemes/properties-from-the-ring|properties from the ring]].

[[D-SCHDIM]]
