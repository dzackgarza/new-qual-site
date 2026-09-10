---
schema: qual/card@1
id: E-QOXG5
kind: problem
title: Countable compactness equals limit point compactness for T1 spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}

A space $X$ is said to be countably compact if every countable open covering of $X$ contains a finite subcollection that covers $X$.
Show that for a $T_1$ space $X$, countable compactness is equivalent to limit point compactness.
[Hint: If no finite subcollection of $U_n$ covers $X$, choose $x_n \notin U_1 \cup \dots \cup U_n$, for each $n$.]
:::

::: {.solution}
Assume first that \(X\) is countably compact, and let \(A\subset X\) be infinite. Suppose \(A\) had no limit point. Choose a countably infinite subset
\[
\{a_1,a_2,\dots\}\subset A.
\]
Since \(X\) is \(T_1\) and none of the \(a_n\) is a limit point of this subset, for each \(n\) there is an open set \(V_n\ni a_n\) with
\[
V_n\cap\{a_1,a_2,\dots\}=\{a_n\}.
\]
The countable subset \(B=\{a_n:n\ge1\}\) has no limit point, hence is closed in a \(T_1\) space: if \(x\notin B\) lay in \(\overline B\), every neighborhood of \(x\) would meet \(B\), making \(x\) a limit point of \(B\). Therefore
\[
X\setminus B,\ V_1,V_2,\dots
\]
is a countable open cover of \(X\). No finite subfamily covers \(B\). This contradicts countable compactness. Hence every infinite subset has a limit point, so \(X\) is limit point compact.

Conversely, suppose \(X\) is limit point compact and let
\[
U_1,U_2,\dots
\]
be a countable open cover with no finite subcover. For each \(n\), choose
\[
x_n\notin U_1\cup\cdots\cup U_n.
\]
The set \(A=\{x_n:n\ge1\}\) is infinite. Indeed, if it were finite, each of its points would belong to some \(U_j\); for sufficiently large \(N\), all points of \(A\) would then lie in \(U_1\cup\cdots\cup U_N\), contradicting \(x_N\notin U_1\cup\cdots\cup U_N\).

We show \(A\) has no limit point. Fix \(x\in X\), and choose \(m\) with \(x\in U_m\). For every \(n\ge m\),
\[
x_n\notin U_m,
\]
so \(U_m\cap A\) is finite. Since \(X\) is \(T_1\), deleting the finitely many points of \((U_m\cap A)\setminus\{x\}\) leaves an open neighborhood of \(x\) meeting \(A\) in at most \(x\). Hence \(x\) is not a limit point of \(A\). This contradicts limit point compactness. Therefore every countable open cover has a finite subcover.

Thus, for \(T_1\) spaces,
\[
\boxed{\text{countably compact}\iff\text{limit point compact}.}
\]
:::
