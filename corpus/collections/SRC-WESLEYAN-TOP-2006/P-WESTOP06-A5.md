---
schema: qual/card@1
id: P-WESTOP06-A5
kind: problem
title: Clopen bases and the weight of zero-dimensional compact Hausdorff spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
For a space $X$, put
\[
\operatorname{clop}(X)=\{U\subseteq X:U\text{ is both closed and open}\}.
\]
Call $X$ *zero-dimensional* if $\operatorname{clop}(X)$ is a basis, and let $wX$ denote the minimum cardinality of a basis for $X$.

1. Show that $\mathbb Q$ with its usual topology is zero-dimensional and that
   \[
   w\mathbb Q<|\operatorname{clop}(\mathbb Q)|.
   \]
2. Prove that if $X$ is compact Hausdorff and zero-dimensional, then
   \[
   wX=|\operatorname{clop}(X)|.
   \]
:::

::: {.solution}
<1>1. The usual topology on \(\mathbb Q\) has a basis of clopen sets.

::: {.proof}
Let \(q\in\mathbb Q\) and let \(U\) be an open neighborhood of \(q\) in \(\mathbb Q\). Choose real numbers \(a<q<b\) with \(a,b\notin\mathbb Q\) and
\[
(a,b)\cap\mathbb Q\subseteq U.
\]
Then
\[
C=(a,b)\cap\mathbb Q
\]
is open in \(\mathbb Q\). It is also closed, because
\[
\mathbb Q\setminus C
=
(-\infty,a)\cap\mathbb Q
\;\cup\;
(b,\infty)\cap\mathbb Q,
\]
where the irrationality of \(a\) and \(b\) removes any endpoint issue. Thus every neighborhood of every point contains a clopen neighborhood, so \(\operatorname{clop}(\mathbb Q)\) is a basis and \(\mathbb Q\) is zero-dimensional.
:::

<1>2. The weight of \(\mathbb Q\) is
\[
w\mathbb Q=\aleph_0.
\]

::: {.proof}
The family
\[
\{(a,b)\cap\mathbb Q:a,b\in\mathbb Q,\ a<b\}
\]
is a countable basis, so \(w\mathbb Q\le\aleph_0\).

On the other hand, \(\mathbb Q\) is an infinite \(T_1\) space. A finite basis would generate only finitely many open sets and therefore only finitely many closed sets, whereas the distinct singletons \(\{q\}\) are all closed. Hence no finite basis exists, so \(w\mathbb Q\ge\aleph_0\).
:::

<1>3. The set of clopen subsets of \(\mathbb Q\) has cardinality at least \(2^{\aleph_0}\).

::: {.proof}
For each irrational number \(a\), define
\[
C_a=(-\infty,a)\cap\mathbb Q.
\]
The set \(C_a\) is clopen in \(\mathbb Q\): both it and its complement
\[
(a,\infty)\cap\mathbb Q
\]
are open in the subspace topology.

If \(a<b\) are irrational, density of \(\mathbb Q\) in \(\mathbb R\) gives \(q\in\mathbb Q\) with \(a<q<b\). Then \(q\notin C_a\) but \(q\in C_b\), so \(C_a\ne C_b\). Thus
\[
\mathbb R\setminus\mathbb Q\longrightarrow\operatorname{clop}(\mathbb Q),
\qquad
a\longmapsto C_a,
\]
is injective. Since \(|\mathbb R\setminus\mathbb Q|=2^{\aleph_0}\), the claim follows.
:::

<1>4. Therefore
\[
\boxed{w\mathbb Q<|\operatorname{clop}(\mathbb Q)|.}
\]

::: {.proof}
By step <1>2, \(w\mathbb Q=\aleph_0\), while step <1>3 gives
\[
|\operatorname{clop}(\mathbb Q)|\ge2^{\aleph_0}>\aleph_0
\]
by Cantor's theorem.
:::

<1>5. Part \(2\) is false as printed for finite compact Hausdorff zero-dimensional spaces.

::: {.proof}
Let \(X\) be a discrete space with \(n\ge1\) points. It is compact, Hausdorff, and zero-dimensional. Every subset is clopen, so
\[
|\operatorname{clop}(X)|=2^n.
\]
Moreover \(wX=n\): the singleton subsets form a basis, and every basis must contain every singleton because each singleton is open. Hence
\[
wX=n\ne2^n=|\operatorname{clop}(X)|.
\]
In particular, the one-point space already contradicts the literal statement.
:::

<1>6. If \(X\) is infinite, compact, Hausdorff, and zero-dimensional, then
\[
\boxed{wX=|\operatorname{clop}(X)|.}
\]

::: {.proof}
Because \(X\) is zero-dimensional, \(\operatorname{clop}(X)\) itself is a basis. Therefore
\[
wX\le|\operatorname{clop}(X)|.
\]

Let \(\mathcal B\) be a basis of cardinality
\[
|\mathcal B|=wX=\kappa.
\]
Since \(X\) is infinite Hausdorff, \(\kappa\) is infinite. Let \(C\in\operatorname{clop}(X)\). For each \(x\in C\), choose \(B_x\in\mathcal B\) with
\[
x\in B_x\subseteq C.
\]
The set \(C\) is compact because it is closed in the compact space \(X\). Hence finitely many of these basis elements cover \(C\):
\[
C=B_{x_1}\cup\cdots\cup B_{x_m}.
\]
Thus every clopen set is a finite union of members of \(\mathcal B\).

An infinite set of cardinality \(\kappa\) has only \(\kappa\) finite subsets, so there are at most \(\kappa\) finite unions of members of \(\mathcal B\). Consequently
\[
|\operatorname{clop}(X)|\le\kappa=wX.
\]
Combining the two inequalities gives the claimed equality.
:::

<1>7. The exact corrected form of part \(2\) is: the asserted equality holds for every infinite compact Hausdorff zero-dimensional space, while an \(n\)-point compact Hausdorff space satisfies
\[
wX=n,
\qquad
|\operatorname{clop}(X)|=2^n.
\]

::: {.proof}
The infinite case is step <1>6. A finite Hausdorff space is discrete, so the finite computation is exactly the one in step <1>5.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1 through <1>4 prove part \(1\). Steps <1>5 through <1>7 show that part \(2\) is false as printed and prove the intended infinite-space statement together with the exact finite exception.
:::
:::
