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
A subset of $\PP^n$ is \dfn{closed} if it is $V(T)$ for a set $T$ of homogeneous elements of $S \da k[x_0,\ldots,x_n]$.
A \dfn{projective variety} is an irreducible closed subset of $\PP^n$; a \dfn{quasi-projective variety} is an open subset of one.
:::

::: {.remark}
Let $p\in\PP^n$ have representative $v\in k^{n+1}\sm\ts{0}$, and let $f\in S$ be homogeneous of degree $d$.
Then $f(\lambda v)=\lambda^d f(v)$ for $\lambda\in k^\times$, so the condition $f(v)=0$ does not depend on the representative $v$, although the value $f(v)$ does when $d>0$.
For $f=x_0+x_1^2$ in $k[x_0,x_1]$ and $v=(-1,1)$, $f(v)=0$ but $f(2v)=2\ne0$ when $\operatorname{char}k\ne2$.
Homogenizing with respect to a new variable $Z$ gives projective closures: $V(x^2 + y^2 - 1)$ becomes $V(X^2 + Y^2 - Z^2)$, and $V(y - x^3)$ becomes $V(YZ^2 - X^3)$.

The \dfn{irrelevant ideal} $S_+ = (x_0,\ldots,x_n)$ is homogeneous and radical, and $V(S_+) = \emptyset=V(S)$.
The projective Nullstellensatz: for a homogeneous ideal $J$, $V(J) = \emptyset$ exactly when $\sqrt{J} \supseteq S_+$, and otherwise $I(V(J)) = \sqrt{J}$.
Hence $V$ and $I$ are inclusion-reversing bijections, inverse to each other, between closed subsets of $\PP^n$ and homogeneous radical ideals of $S$ other than $S_+$ [@Har10a, Exercise I.2.4].
:::
