---
schema: qual/card@1
id: D-CP2MH
kind: definition
title: Projective varieties and homogeneous ideals
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Varieties
  - Homogeneous Ideals
  - Varieties
relations:
- kind: uses
  target: PR-7OT2Z
review: draft
prompts:
- What is a projective variety?
- Why must the defining polynomials be homogeneous?
- Which homogeneous ideals correspond to which closed subsets of $\PP^n$?
- Over an infinite field, show that $f$ is homogeneous of degree $d$ if and only if $f(\lambda \mathbf{x}) = \lambda^d f(\mathbf{x})$ for all $\lambda$.
- Find the projective closures of $V(x^2 + y^2 - 1)$ and $V(y - x^3)$ in $\PP^2$.
- Describe the line at infinity in $\PP^2$, and find the intersection of the projective closures of $V(y)$ and $V(y - tx - 1)$ when $t = 0$.
- 'Show that a real conic $V(f) \subseteq \RR^2$ with infinitely many real points is a circle if and only if the projective closure of $V(f)$ passes through the circular points $[1 : \pm i : 0]$.'
- Show that conics in $\PP^2$ are parametrized by $\PP^5$, and that the conics through a fixed point form a hyperplane $H_p$.
- Show that over an infinite field the conics through $5$ fixed points form a single point or an infinite set, and that there is a unique conic through $5$ points in linear general position.
- Show that there is a unique circle through any $3$ non-collinear points of $\RR^2$.
- Describe $\PGL_{n+1}(k)$ as a quotient, and show that for two sets of $n+2$ points in linear general position in $\PP^n$ there is a unique element of $\PGL_{n+1}(k)$ carrying one to the other.
- Show that the $(k+1)$-dimensional linear subspaces of $\PP^n$ containing a fixed $k$-dimensional subspace $W$ form a $\PP^{n-k-1}$.
- For $\PP^n = \PP(V)$, show that $\PP(V\dual)$ parametrizes the hyperplanes of $\PP^n$.
- Show that there is a unique rational normal curve through $n+3$ points in linear general position in $\PP^n$.
- Show that $\dim(V_1 \cap V_2) \geq \dim V_1 + \dim V_2 - n$ for linear subspaces $V_1, V_2 \subseteq \PP^n$.
---

::: {.definition title="Projective variety"}
Let $S\coloneqq k[x_0,\ldots,x_n]$.
A subset of $\PP^n_k$ is \dfn{Zariski closed} if it is $V(T)$ for a set $T$ of homogeneous elements of $S$.
A \dfn{projective variety} is an irreducible Zariski-closed subset of $\PP^n_k$; a \dfn{quasi-projective variety} is an open subvariety of a projective variety.
:::

::: {.remark}
A homogeneous polynomial $f$ of degree $d$ satisfies
$$
f(\lambda x_0,\ldots,\lambda x_n)=\lambda^d f(x_0,\ldots,x_n),
$$
so the condition $f=0$ is invariant under rescaling homogeneous coordinates. An arbitrary inhomogeneous polynomial does not define a projective equation unless its vanishing condition is separately shown to be scaling-invariant.

Homogenizing with respect to a new variable $Z$ gives projective closures: $V(x^2+y^2-1)\subseteq\AA^2$ has closure $V(X^2+Y^2-Z^2)\subseteq\PP^2$, and $V(y-x^3)$ has closure $V(YZ^2-X^3)$.

The \dfn{irrelevant ideal} is $S_+=(x_0,\ldots,x_n)$. It is homogeneous and radical, and $V(S_+)=\emptyset$.
For a homogeneous ideal $J\subseteq S$, the projective Nullstellensatz states
$$
V(J)=\emptyset\quad\Longleftrightarrow\quad S_+\subseteq\sqrt J.
$$
If $V(J)\ne\emptyset$, then $I(V(J))=\sqrt J$.
:::
