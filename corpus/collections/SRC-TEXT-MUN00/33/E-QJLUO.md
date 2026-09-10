---
schema: qual/card@1
id: E-QJLUO
kind: problem
title: Separating compact sets from closed sets in completely regular spaces
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

Let $X$ be completely regular; let $A$ and $B$ be disjoint closed subsets of $X$.
Show that if $A$ is compact, there is a continuous function $f: X \to [0, 1]$ such that $f(A) = \ts{0}$ and $f(B) = \ts{1}$.
:::

::: {.solution}
For each \(a\in A\), complete regularity gives a continuous function
\[
u_a:X\to[0,1]
\]
with
\[
u_a(a)=1,\qquad u_a(B)=\{0\}.
\]
The open sets
\[
U_a=\{x:u_a(x)>1/2\}
\]
cover compact \(A\). Choose \(a_1,\dots,a_n\) such that \(A\subset U_{a_1}\cup\cdots\cup U_{a_n}\). Set
\[
u(x)=\max\{u_{a_1}(x),\dots,u_{a_n}(x)\}.
\]
Then \(u\) is continuous, \(u=0\) on \(B\), and \(u>1/2\) on \(A\). Finally define
\[
f(x)=\max\{0,1-2u(x)\}.
\]
Then \(f:X\to[0,1]\) is continuous, \(f=0\) on \(A\), and \(f=1\) on \(B\).
:::
