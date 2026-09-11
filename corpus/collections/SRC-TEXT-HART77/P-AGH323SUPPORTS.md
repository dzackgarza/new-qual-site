---
schema: qual/card@1
id: P-AGH323SUPPORTS
kind: problem
title: Cohomology with supports in a closed subset
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Local Cohomology
  - Flasque Sheaves
  - Excision
relations: []
review: draft
---

::: problem
Let $X$ be a topological space, let $Y$ be a closed subset, and let $\mcf$ be a sheaf of abelian groups. Let $\Gamma_Y(X, \mcf)$ denote the group of sections of $\mcf$ with support in $Y$ (II, Ex. 1.20).

a. Show that $\Gamma_Y(X, \wait)$ is a left exact functor from $\Ab(X)$ to $\Ab$. We denote the right derived functors of $\Gamma_Y(X, \wait)$ by $H_Y^i(X, \wait)$. They are the cohomology groups of $X$ with supports in $Y$, and coefficients in a given sheaf.

b. If $0 \to \mcf' \to \mcf \to \mcf'' \to 0$ is an exact sequence of sheaves, with $\mcf'$ flasque, show that
\[
0 \to \Gamma_Y(X, \mcf') \to \Gamma_Y(X, \mcf) \to \Gamma_Y(X, \mcf'') \to 0
\]
is exact.

c. Show that if $\mcf$ is flasque, then $H_Y^i(X, \mcf)=0$ for all $i>0$.

d. If $\mcf$ is flasque, show that the sequence
\[
0 \to \Gamma_Y(X, \mcf) \to \Gamma(X, \mcf) \to \Gamma(X-Y, \mcf) \to 0
\]
is exact.

e. Let $U=X-Y$. Show that for any $\mcf$, there is a long exact sequence of cohomology groups
\[
\begin{aligned}
0 &\to H_Y^0(X, \mcf) \to H^0(X, \mcf) \to H^0(U, \ro{\mcf}{U}) \to \\
&\to H_Y^1(X, \mcf) \to H^1(X, \mcf) \to H^1(U, \ro{\mcf}{U}) \to \\
&\to H_Y^2(X, \mcf) \to \cdots
\end{aligned}
\]

f. *Excision.* Let $V$ be an open subset of $X$ containing $Y$. Then there are natural functorial isomorphisms, for all $i$ and $\mcf$,
\[
H_Y^i(X, \mcf) \cong H_Y^i(V, \ro{\mcf}{V}).
\]
:::
