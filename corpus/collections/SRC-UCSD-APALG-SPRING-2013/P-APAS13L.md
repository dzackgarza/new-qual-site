---
schema: qual/card@1
id: P-APAS13L
kind: problem
title: Comaximal ideals, Nullstellensatz, and ideal intersection via an auxiliary variable
classification:
  areas:
  - applied-algebra
  topics:
  - Gröbner Bases
  - Ideals
  - Commutative Algebra
relations: []
review: draft
---

::: {.problem}
Let $k$ be an algebraically closed field.

Two ideals $I$ and $J$ of $k[x_1,\ldots,x_n]$ are said to be comaximal if and only if $I+J=k[x_1,\ldots,x_n]$.

(a) State the Weak Nullstellensatz and Hilbert's Nullstellensatz Theorem.

(b) Show that two ideals $I$ and $J$ are comaximal if and only if $V(I)\cap V(J)=\emptyset$.

(c) Show that if $I$ and $J$ are ideals in $k[x_1,\ldots,x_n]$, then
\[
I\cap J=(tI+(1-t)J)\cap k[x_1,\ldots,x_n].
\]

(d) Show that if $I=\langle f\rangle$ and $J=\langle g\rangle$, then $I\cap J=\langle h\rangle$ where $h$ is a least common multiple of $f$ and $g$.
:::

::: {.solution}
Let
\[
R=k[x_1,\ldots,x_n].
\]

For part (a), the **Weak Nullstellensatz** says that every maximal ideal of \(R\) has the form
\[
(x_1-a_1,\ldots,x_n-a_n)
\]
for a unique point \(a=(a_1,\ldots,a_n)\in k^n\).

Hilbert's **Nullstellensatz** says that for every ideal \(I\subseteq R\),
\[
I(V(I))=\sqrt I,
\]
where
\[
V(I)=\{a\in k^n:f(a)=0\text{ for all }f\in I\}
\]
and
\[
I(X)=\{f\in R:f(a)=0\text{ for all }a\in X\}.
\]

For part (b), note that
\[
V(I+J)=V(I)\cap V(J).
\]
If \(I+J=R\), then \(1\in I+J\), so \(V(I+J)=\varnothing\), hence
\[
V(I)\cap V(J)=\varnothing.
\]

Conversely, suppose
\[
V(I)\cap V(J)=\varnothing.
\]
Then \(V(I+J)=\varnothing\). By the Nullstellensatz,
\[
\sqrt{I+J}=I(V(I+J))=I(\varnothing)=R.
\]
Hence \(1\in\sqrt{I+J}\), so \(1^m=1\in I+J\) for some \(m\), and therefore \(I+J=R\). Thus \(I\) and \(J\) are comaximal.

For part (c), work in the polynomial ring
\[
R[t]=k[x_1,\ldots,x_n,t].
\]
Set
\[
K=tI+(1-t)J.
\]
We prove
\[
I\cap J=K\cap R.
\]

If \(f\in I\cap J\), then
\[
f=tf+(1-t)f\in tI+(1-t)J=K,
\]
and of course \(f\in R\). Hence
\[
I\cap J\subseteq K\cap R.
\]

Conversely, let \(f\in K\cap R\). Then
\[
f=t a+(1-t)b
\]
for some \(a\in I R[t]\) and \(b\in J R[t]\). Since \(f\) is independent of \(t\), specializing at \(t=1\) gives
\[
f=a|_{t=1}\in I,
\]
while specializing at \(t=0\) gives
\[
f=b|_{t=0}\in J.
\]
Thus \(f\in I\cap J\), proving
\[
\boxed{I\cap J=(tI+(1-t)J)\cap R.}
\]

For part (d), let
\[
I=(f),\qquad J=(g).
\]
Because \(R=k[x_1,\ldots,x_n]\) is a UFD, a least common multiple \(h=\operatorname{lcm}(f,g)\) exists, unique up to multiplication by a unit.

Since \(f\mid h\) and \(g\mid h\),
\[
h\in(f)\cap(g),
\]
so
\[
(h)\subseteq(f)\cap(g).
\]
Conversely, if \(q\in(f)\cap(g)\), then both \(f\mid q\) and \(g\mid q\). By the defining divisibility property of the least common multiple,
\[
h\mid q.
\]
Hence \(q\in(h)\). Therefore
\[
\boxed{(f)\cap(g)=(\operatorname{lcm}(f,g)).}
\]
:::
