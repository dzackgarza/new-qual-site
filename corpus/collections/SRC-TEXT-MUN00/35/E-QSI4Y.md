---
schema: qual/card@1
id: E-QSI4Y
kind: problem
title: The Tietze extension theorem implies the Urysohn lemma
classification:
  areas:
  - topology
  topics:
  - Urysohn Lemma
relations: []
review: draft
---

::: {.exercise}

Show that the Tietze extension theorem implies the Urysohn lemma.
:::

::: {.solution}
Let \(A,B\subset X\) be disjoint closed subsets of a normal space \(X\). The union \(A\cup B\) is closed. Define
\[
f:A\cup B\to[-1,1]
\]
by \(f=0\) on \(A\) and \(f=1\) on \(B\). This is continuous because \(A\) and \(B\) are disjoint closed-and-open subsets of the subspace \(A\cup B\).

By the Tietze extension theorem, \(f\) extends to a continuous
\[
F:X\to[-1,1].
\]
Composing with the continuous truncation
\[
t(s)=\min\{1,\max\{0,s\}\}
\]
gives \(u=t\circ F:X\to[0,1]\), with \(u(A)=0\) and \(u(B)=1\). This is exactly the Urysohn lemma.
:::
