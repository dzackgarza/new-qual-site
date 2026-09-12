---
schema: qual/card@1
id: E-Y4MFU
kind: problem
title: Perfect maps transfer separation and countability properties
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Let $p: X \to Y$ be a closed continuous surjective map such that $p^{-1}(\ts{y})$ is compact for each $y \in Y$.
(Such a map is called a perfect map.)

(a) Show that if $X$ is Hausdorff, then so is $Y$.

(b) Show that if $X$ is regular, then so is $Y$.

(c) Show that if $X$ is locally compact, then so is $Y$.

(d) Show that if $X$ is second-countable, then so is $Y$.
[Hint: Let $\mathcal{B}$ be a countable basis for $X$. For each finite subset $J$ of $\mathcal{B}$, let $U_J$ be the union of all sets of the form $p^{-1}(W)$, for $W$ open in $Y$, that are contained in the union of the elements of $J$.]
:::

::: {.solution}
We repeatedly use the following consequence of closedness of \(p\): if \(U\subset X\) is open and contains the fiber \(p^{-1}(y)\), then
\[
W=Y\setminus p(X\setminus U)
\]
is an open neighborhood of \(y\) and \(p^{-1}(W)\subset U\).

(a) Let \(y_1\ne y_2\). The compact fibers \(F_i=p^{-1}(y_i)\) are disjoint compact subsets of Hausdorff \(X\), so they have disjoint open neighborhoods \(U_1,U_2\). Applying the lemma gives neighborhoods \(W_i\ni y_i\) with \(p^{-1}(W_i)\subset U_i\). Then \(W_1\cap W_2=\varnothing\). Hence \(Y\) is Hausdorff.

(b) Let \(C\subset Y\) be closed and \(y\notin C\). The compact fiber \(F=p^{-1}(y)\) is disjoint from the closed set \(A=p^{-1}(C)\). Since \(X\) is regular, each point of \(F\) has an open neighborhood disjoint from an open neighborhood of \(A\); compactness of \(F\) and a finite intersection argument give disjoint open sets \(U,V\subset X\) with \(F\subset U\) and \(A\subset V\). The lemma gives an open \(W\ni y\) with \(p^{-1}(W)\subset U\). For each \(c\in C\), apply the lemma to the fiber \(p^{-1}(c)\subset V\), and take the union of the resulting neighborhoods to obtain an open \(O\supset C\) with \(p^{-1}(O)\subset V\). Then \(W\cap O=\varnothing\). Thus \(Y\) is regular.

(c) Let \(y\in Y\). Compactness of \(F=p^{-1}(y)\) and local compactness of \(X\) give finitely many neighborhoods \(U_1,\dots,U_n\) of points of \(F\), each contained in a compact subspace \(K_i\subset X\), with \(F\subset U=\bigcup_iU_i\). Then \(K=K_1\cup\cdots\cup K_n\) is compact and contains \(U\). By the lemma there is a neighborhood \(W\ni y\) with \(p^{-1}(W)\subset U\subset K\). Hence
\[
W\subset p(K),
\]
and \(p(K)\) is compact. Thus \(Y\) is locally compact.

(d) Let \(\mathcal B\) be a countable basis for \(X\). For each finite \(J\subset\mathcal B\), let
\[
U_J=\bigcup\{p^{-1}(W): W\subset Y\text{ open and }p^{-1}(W)\subset\bigcup J\}.
\]
Then \(U_J\) is open and saturated, so \(p(U_J)\) is open in \(Y\). There are only countably many finite \(J\), hence only countably many sets \(p(U_J)\).

We show they form a basis. Let \(y\in W\) with \(W\subset Y\) open. The compact fiber \(F=p^{-1}(y)\) is contained in the open set \(p^{-1}(W)\). Choose finitely many basis elements \(B_1,\dots,B_n\in\mathcal B\) such that
\[
F\subset B_1\cup\cdots\cup B_n\subset p^{-1}(W).
\]
Let \(J=\{B_1,\dots,B_n\}\). By the closed-map lemma there is an open neighborhood \(W'\ni y\) with
\[
p^{-1}(W')\subset\bigcup J.
\]
Hence \(y\in p(U_J)\). Also by definition \(U_J\subset p^{-1}(W)\), since every saturated open subset counted in \(U_J\) lies in \(\bigcup J\subset p^{-1}(W)\). Thus
\[
y\in p(U_J)\subset W.
\]
Therefore \(Y\) is second countable.
:::
