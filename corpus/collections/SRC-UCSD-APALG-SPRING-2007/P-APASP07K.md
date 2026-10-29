---
schema: qual/card@1
id: P-APASP07K
kind: problem
title: "Equivalent representations yield the same Hilbert series of invariant rings"
classification:
  areas:
  - applied-algebra
  topics:
  - Commutative Algebra
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
(a) Show the following: Let $G$ be a finite group, and let $g \mapsto A_g \in \operatorname{GL}(\CC^n)$ and $g \mapsto B_g \in \operatorname{GL}(\CC^n)$ be two equivalent representations of $G$.
Show that the rings of invariants $\CC[x_1, x_2, \ldots, x_n]^G$ defined by these two actions have the same Hilbert series.

(b) Give two examples of an action of a group $G$ on a two-dimensional vector space which lead to two different Hilbert series of the corresponding rings $\CC[x,y]^G$.
:::

::: {.solution}
For part (a), equivalence of the two representations means that there is some $P\in\operatorname{GL}_n(\CC)$ such that
\[
B_g=PA_gP^{-1}
\qquad(g\in G).
\]
Let $V=\CC^n$. The linear isomorphism $P:V\to V$ induces a graded algebra isomorphism on polynomial functions,
\[
P^*:\CC[V]\longrightarrow\CC[V],
\qquad
(P^*f)(v)=f(Pv).
\]
Because $P$ intertwines the two $G$-actions, $P^*$ intertwines the corresponding actions on polynomial functions. Hence
\[
f\in \CC[V]^{G,A}
\quad\Longleftrightarrow\quad
P^*f\in \CC[V]^{G,B}.
\]
Therefore $P^*$ restricts to a graded algebra isomorphism
\[
\CC[x_1,\ldots,x_n]^{G,A}
\cong
\CC[x_1,\ldots,x_n]^{G,B}.
\]
A graded isomorphism preserves the dimension of every homogeneous piece, so the two invariant rings have the same Hilbert series.

For part (b), take $G=C_2=\{1,s\}$.

First let
\[
s\mapsto
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix}.
\]
Then a monomial $x^a y^b$ is invariant exactly when $a$ is even, so
\[
\CC[x,y]^G=\CC[x^2,y].
\]
Hence
\[
H_1(t)=\frac1{(1-t^2)(1-t)}.
\]

Now let
\[
s\mapsto -I_2.
\]
Then $x^a y^b$ is invariant exactly when $a+b$ is even. The degree-$2m$ invariant piece is the whole degree-$2m$ piece of $\CC[x,y]$, of dimension $2m+1$, while every odd-degree invariant piece is zero. Thus
\[
H_2(t)
=
\sum_{m\ge0}(2m+1)t^{2m}.
\]
Putting $u=t^2$ and using
\[
\sum_{m\ge0}(2m+1)u^m=\frac{1+u}{(1-u)^2},
\]
we obtain
\[
H_2(t)=\frac{1+t^2}{(1-t^2)^2}.
\]
Since
\[
\frac1{(1-t)(1-t^2)}
\ne
\frac{1+t^2}{(1-t^2)^2},
\]
these two actions of the same group on a two-dimensional vector space have different invariant-ring Hilbert series.
:::
