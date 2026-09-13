---
schema: qual/card@1
id: P-AGH348COHDIM
kind: problem
title: Cohomological dimension of a noetherian separated scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cech Cohomology
  - Cohomological Dimension
  - Complete Intersections
relations: []
review: draft
---

::: problem
Let $X$ be a noetherian separated scheme.
We define the **cohomological dimension** of $X$, denoted $\operatorname{cd}(X)$, to be the least integer $n$ such that $H^i(X, \mcf)=0$ for all quasi-coherent sheaves $\mcf$ and all $i>n$.

Thus for example, Serre's theorem (3.7) says that $\operatorname{cd}(X)=0$ if and only if $X$ is affine.
Grothendieck's theorem (2.7) implies that $\operatorname{cd}(X) \leq \dim X$.

a. In the definition of $\operatorname{cd}(X)$, show that it is sufficient to consider only coherent sheaves on $X$.
Use (II, Ex.
5.15) and (2.9).

b. If $X$ is quasi-projective over a field $k$, then it is even sufficient to consider only locally free coherent sheaves on $X$.
Use (II, 5.18).

c. Suppose $X$ has a covering by $r+1$ open affine subsets.
Use Čech cohomology to show that $\operatorname{cd}(X) \leq r$.

d. If $X$ is a quasi-projective scheme of dimension $r$ over a field $k$, then $X$ can be covered by $r+1$ open affine subsets.
Conclude (independently of (2.7)) that $\operatorname{cd}(X) \leq \dim X$.

e. Let $Y$ be a set-theoretic complete intersection (I, Ex.
2.17) of codimension $r$ in $X=\PP_k^n$.
Show that $\operatorname{cd}(X-Y) \leq r-1$.
:::
