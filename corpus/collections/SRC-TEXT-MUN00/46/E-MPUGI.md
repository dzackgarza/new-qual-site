---
schema: qual/card@1
id: E-MPUGI
kind: problem
title: Products with a locally compact Hausdorff factor preserve quotient maps
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
relations: []
review: draft
---

::: {.exercise}

Here is an application of Theorem 46.11 to quotient maps.
(Compare [[E-S57IX]].)

Theorem.
If $p: A \to B$ is a quotient map and $X$ is locally compact Hausdorff, then $i_X \times p: X \times A \to X \times B$ is a quotient map.

(a) Let $Y$ be the quotient space induced by $i_X \times p$; let $q: X \times A \to Y$ be the quotient map.
Show there is a bijective continuous map $f: Y \to X \times B$ such that $f \circ q = i_X \times p$.

(b) Let $g = f^{-1}$.
Let $G: B \to \mathcal{C}(X, Y)$ and $Q: A \to \mathcal{C}(X, Y)$ be the maps induced by $g$ and $q$, respectively.
Show that $Q = G \circ p$.

(c) Show that $Q$ is continuous; conclude that $G$ is continuous, so that $g$ is continuous.
:::

::: {.solution}
Let $q:X\times A\to Y$ be the quotient induced by $i_X\times p$.

(a) The map $i_X\times p$ is constant exactly on the fibers of $q$, hence factors uniquely as
\[
X\times A\xrightarrow qY\xrightarrow fX\times B.
\]
The induced $f$ is bijective and continuous by the defining property of the quotient topology.

(b) Let $g=f^{-1}$. Under the exponential correspondence of Theorem 46.11, $g$ induces
\[
G:B\to C(X,Y),\qquad G(b)(x)=g(x,b),
\]
and $q$ induces
\[
Q:A\to C(X,Y),\qquad Q(a)(x)=q(x,a).
\]
Since $f q=i_X\times p$, equivalently $q=g(i_X\times p)$, we have
\[
Q(a)(x)=g(x,p(a))=G(p(a))(x),
\]
so $Q=G\circ p$.

(c) The map $q:X\times A\to Y$ is continuous. Since $X$ is locally compact Hausdorff, Theorem 46.11 says its adjoint $Q:A\to C(X,Y)$ is continuous. Because $p$ is quotient and $Q=G\circ p$, the quotient criterion implies $G$ is continuous. Applying Theorem 46.11 again, the adjoint $g:X\times B\to Y$ is continuous. Hence the continuous bijection $f$ has continuous inverse, so $f$ is a homeomorphism. Therefore $i_X\times p$ is the composite of the quotient map $q$ with a homeomorphism, and is quotient.
:::
