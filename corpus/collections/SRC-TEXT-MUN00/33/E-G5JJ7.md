---
schema: qual/card@1
id: E-G5JJ7
kind: problem
title: Strong form of the Urysohn lemma
classification:
  areas:
  - topology
  topics:
  - Urysohn Lemma
relations: []
review: draft
---

::: {.exercise}

Prove the following.

Theorem (Strong form of the Urysohn lemma).
Let $X$ be a normal space.
There is a continuous function $f: X \to [0, 1]$ such that $f(x) = 0$ for $x \in A$, and $f(x) = 1$ for $x \in B$, and $0 < f(x) < 1$ otherwise, if and only if $A$ and $B$ are disjoint closed $G_\delta$ sets in $X$.
:::

::: {.solution}
Suppose first that such a function \(f:X\to[0,1]\) exists. Then
\[
A=f^{-1}(\{0\}),\qquad B=f^{-1}(\{1\})
\]
are closed. Also
\[
A=\bigcap_{n\ge1} f^{-1}([0,1/n)),
\qquad
B=\bigcap_{n\ge1} f^{-1}((1-1/n,1]),
\]
so both are \(G_\delta\) sets. They are disjoint because \(f\) cannot be both \(0\) and \(1\).

Conversely, let \(A,B\) be disjoint closed \(G_\delta\) sets. Write
\[
A=\bigcap_{n\ge1}U_n,\qquad B=\bigcap_{n\ge1}V_n
\]
with \(U_n,V_n\) open. By normality and Urysohn's lemma, for each \(n\) there is a continuous function
\[
a_n:X\to[0,2^{-n}]
\]
that is \(0\) on \(A\) and \(2^{-n}\) on \(X\setminus U_n\). The uniformly convergent series
\[
a=\sum_{n\ge1}a_n
\]
defines a continuous function with
\[
a^{-1}(0)=A.
\]
Indeed, outside \(A\) some \(U_n\) is missed, forcing \(a_n>0\). Similarly there is a continuous \(b:X\to[0,1]\) with
\[
b^{-1}(0)=B.
\]
Since \(A\cap B=\varnothing\), \(a+b>0\) everywhere. Define
\[
f=\frac{a}{a+b}.
\]
Then \(f=0\) exactly on \(A\), \(f=1\) exactly on \(B\), and \(0<f<1\) elsewhere. This is the required strong Urysohn function.
:::
