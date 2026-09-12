---
schema: qual/card@1
id: E-X4TVL
kind: problem
title: Rational and irrational anti-diagonals in the Sorgenfrey plane
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
---

::: {.exercise}

Let $A$ be the set of all points of $\mathbb{R}_\ell^2$ of the form $x \times (-x)$, for $x$ rational; let $B$ be the set of all points of this form for $x$ irrational.
If $V$ is an open set of $\mathbb{R}_\ell^2$ containing $B$, show there exists no open set $U$ containing $A$ that is disjoint from $V$, as follows:

(a) Let $K_n$ consist of all irrational numbers $x$ in $[0, 1]$ such that $[x, x + 1/n) \times [-x, -x + 1/n)$ is contained in $V$.
Show that $[0, 1]$ is the union of the sets $K_n$ and countably many one-point sets.

(b) Use Exercise 5 of §27 to show that some set $\overline{K}_n$ contains an open interval $(a, b)$ of $\mathbb{R}$.

(c) Show that $V$ contains the open parallelogram consisting of all points of the form $x \times (-x + \epsilon)$ for which $a < x < b$ and $0 < \epsilon < 1/n$.

(d) Conclude that if $q$ is a rational number with $a < q < b$, then the point $q \times (-q)$ of $\mathbb{R}_\ell^2$ is a limit point of $V$.
:::

::: {.solution}
(a) For each irrational \(x\in[0,1]\), the point \((x,-x)\) lies in the open set \(V\). Hence there is \(\varepsilon_x>0\) such that
\[
[x,x+\varepsilon_x)\times[-x,-x+\varepsilon_x)\subset V.
\]
Choose \(n\) with \(1/n<\varepsilon_x\). Then \(x\in K_n\). Thus every irrational point of \([0,1]\) lies in some \(K_n\), while the rational points form a countable union of one-point sets. Therefore
\[
[0,1]=\bigcup_{n\ge1}K_n\ \cup\ \bigcup_{q\in\mathbb Q\cap[0,1]}\{q\}.
\]

(b) If every \(\overline{K_n}\) had empty interior, then the compact Hausdorff space \([0,1]\) would be a countable union of closed sets with empty interior, together with countably many singleton closed sets, also of empty interior. This contradicts the Baire-category exercise of §27. Hence some \(\overline{K_n}\) contains a nonempty open interval \((a,b)\).

(c) Since \((a,b)\subset\overline{K_n}\), the set \(K_n\) is dense in \((a,b)\). Fix
\[
a<x<b,\qquad 0<\epsilon<1/n.
\]
Choose
\[
t\in K_n\cap(\max\{a,x-\epsilon\},x).
\]
Then \(t<x<t+1/n\), and \(t>x-\epsilon\) implies
\[
-t<-x+\epsilon.
\]
Also \(t<x<x-\epsilon+1/n\), so
\[
-x+\epsilon<-t+1/n.
\]
Therefore
\[
(x,-x+\epsilon)\in[t,t+1/n)\times[-t,-t+1/n)\subset V.
\]
Thus \(V\) contains the stated open parallelogram.

(d) Let \(q\in(a,b)\cap\mathbb Q\). Every basic neighborhood of \((q,-q)\) in the Sorgenfrey plane contains a point
\[
(q,-q+\epsilon)
\]
with \(0<\epsilon<1/n\) sufficiently small. By (c) this point lies in \(V\), and it differs from \((q,-q)\). Hence \((q,-q)\) is a limit point of \(V\).

Now if \(U\) were an open set containing \(A\) and disjoint from \(V\), then \(U\) would contain \((q,-q)\), but every neighborhood of this point meets \(V\), contradiction. Therefore no open neighborhood of \(A\) is disjoint from \(V\).
:::
