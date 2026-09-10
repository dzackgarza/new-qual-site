---
schema: qual/card@1
id: E-KIH81
kind: problem
title: Maximal collections with the finite intersection property
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Let $X$ be a space.
Let $\mathcal{D}$ be a collection of subsets of $X$ that is maximal with respect to the finite intersection property.

(a) Show that $x \in \overline{D}$ for every $D \in \mathcal{D}$ if and only if every neighborhood of $x$ belongs to $\mathcal{D}$.
Which implication uses maximality of $\mathcal{D}$?

(b) Let $D \in \mathcal{D}$.
Show that if $A \supset D$, then $A \in \mathcal{D}$.

(c) Show that if $X$ is Hausdorff, there is at most one point belonging to $\bigcap_{D \in \mathcal{D}} \overline{D}$.
:::

::: {.solution}
(a) Suppose first that
\[
x\in\overline D\qquad\text{for every }D\in\mathcal D.
\]
Let \(U\) be a neighborhood of \(x\). We claim \(\mathcal D\cup\{U\}\) still has the finite intersection property. Indeed, if \(D_1,\dots,D_n\in\mathcal D\), maximality implies the finite intersection
\[
D=D_1\cap\cdots\cap D_n
\]
itself belongs to \(\mathcal D\): adding \(D\) cannot destroy the finite intersection property. Since \(x\in\overline D\), every neighborhood of \(x\), in particular \(U\), meets \(D\). Hence
\[
U\cap D_1\cap\cdots\cap D_n\ne\varnothing.
\]
By maximality of \(\mathcal D\), \(U\in\mathcal D\).

Conversely, suppose every neighborhood of \(x\) belongs to \(\mathcal D\). If \(D\in\mathcal D\) and \(U\) is any neighborhood of \(x\), then \(U,D\in\mathcal D\), so the finite intersection property gives \(U\cap D\ne\varnothing\). Thus every neighborhood of \(x\) meets \(D\), hence \(x\in\overline D\).

Therefore the forward implication is the one using maximality.

(b) Let \(D\in\mathcal D\) and \(A\supset D\). Any finite intersection involving \(A\) and sets \(D_1,\dots,D_n\in\mathcal D\) contains
\[
D\cap D_1\cap\cdots\cap D_n,
\]
which is nonempty by the finite intersection property. Hence \(\mathcal D\cup\{A\}\) has the finite intersection property. Maximality forces \(A\in\mathcal D\).

(c) Assume \(X\) is Hausdorff and suppose distinct points \(x,y\) both belong to
\[
\bigcap_{D\in\mathcal D}\overline D.
\]
By part (a), every neighborhood of \(x\) and every neighborhood of \(y\) belongs to \(\mathcal D\). Hausdorffness gives disjoint neighborhoods \(U\ni x\) and \(V\ni y\). Then \(U,V\in\mathcal D\), contradicting the finite intersection property because \(U\cap V=\varnothing\). Hence the intersection contains at most one point.
:::
