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
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source asks for wX = |clop(X)| for every compact Hausdorff zero-dimensional X, which fails for finite X (wX = n, |clop(X)| = 2^n). Part 2 now assumes X is infinite.
---

::: {.problem}
For a space $X$, put
\[
\operatorname{clop}(X)=\{U\subseteq X:U\text{ is both closed and open}\}.
\]
Call $X$ *zero-dimensional* if $\operatorname{clop}(X)$ is a basis, and let $wX$ denote the minimum cardinality of a basis for $X$.

1. Show that $\QQ$ with its usual topology is zero-dimensional and that
   \[
   w\QQ<|\operatorname{clop}(\QQ)|.
   \]
2. Prove that if $X$ is infinite, compact Hausdorff, and zero-dimensional, then
   \[
   wX=|\operatorname{clop}(X)|.
   \]
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The usual topology on \(\QQ\) has a basis of clopen sets.


::: pf-proof

Let \(q\in\QQ\) and let \(U\) be an open neighborhood of \(q\) in \(\QQ\). Choose real numbers \(a<q<b\) with \(a,b\notin\QQ\) and
\[
(a,b)\cap\QQ\subseteq U.
\]
Then
\[
C=(a,b)\cap\QQ
\]
is open in \(\QQ\). It is also closed, because
\[
\QQ\setminus C
=
(-\infty,a)\cap\QQ
\;\cup\;
(b,\infty)\cap\QQ,
\]
where the irrationality of \(a\) and \(b\) removes any endpoint issue. Thus every neighborhood of every point contains a clopen neighborhood, so \(\operatorname{clop}(\QQ)\) is a basis and \(\QQ\) is zero-dimensional.

:::

:::

::: {.pf-step #s1-2}

The weight of \(\QQ\) is
\[
w\QQ=\aleph_0.
\]


::: pf-proof

The family
\[
\{(a,b)\cap\QQ:a,b\in\QQ,\ a<b\}
\]
is a countable basis, so \(w\QQ\le\aleph_0\).

On the other hand, \(\QQ\) is an infinite \(T_1\) space. A finite basis would generate only finitely many open sets and therefore only finitely many closed sets, whereas the distinct singletons \(\{q\}\) are all closed. Hence no finite basis exists, so \(w\QQ\ge\aleph_0\).

:::

:::

::: {.pf-step #s1-3}

The set of clopen subsets of \(\QQ\) has cardinality at least \(2^{\aleph_0}\).


::: pf-proof

For each irrational number \(a\), define
\[
C_a=(-\infty,a)\cap\QQ.
\]
The set \(C_a\) is clopen in \(\QQ\): both it and its complement
\[
(a,\infty)\cap\QQ
\]
are open in the subspace topology.

If \(a<b\) are irrational, density of \(\QQ\) in \(\RR\) gives \(q\in\QQ\) with \(a<q<b\). Then \(q\notin C_a\) but \(q\in C_b\), so \(C_a\ne C_b\). Thus
\[
\RR\setminus\QQ\longrightarrow\operatorname{clop}(\QQ),
\qquad
a\longmapsto C_a,
\]
is injective. Since \(|\RR\setminus\QQ|=2^{\aleph_0}\), the claim follows.

:::

:::

::: {.pf-step #s1-4}

Therefore
\[
\boxed{w\QQ<|\operatorname{clop}(\QQ)|.}
\]


::: pf-proof

By step [](#s1-2){.pf-ref}, \(w\QQ=\aleph_0\), while step [](#s1-3){.pf-ref} gives
\[
|\operatorname{clop}(\QQ)|\ge2^{\aleph_0}>\aleph_0
\]
by Cantor's theorem.

:::

:::

::: {.pf-step #s1-6}

If \(X\) is infinite, compact, Hausdorff, and zero-dimensional, then
\[
\boxed{wX=|\operatorname{clop}(X)|.}
\]


::: pf-proof

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

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} prove part \(1\). Step [](#s1-6){.pf-ref} proves part \(2\).

:::

:::

:::
