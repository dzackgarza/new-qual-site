---
schema: qual/card@1
id: E-HAT-3.F-4
kind: problem
title: "Divisible groups and vanishing Ext"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.F, Exercise 4; repaired the local statement to restore the source's “if and only if”.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
An abelian group $G$ is defined to be divisible if the map $G \xrightarrow{n} G$, $g \mapsto ng$, is surjective for all $n > 1$.
Show that a group is divisible if and only if it is a quotient of a direct sum of $\mathbb{Q}$'s. Deduce from the previous problem that if $G$ is divisible then $\operatorname{Ext}(A, G) = 0$ for all $A$.
:::

::: {.solution}
First suppose
\[
G\cong\left(\bigoplus_{i\in I}\mathbb Q\right)/K.
\]
A direct sum of copies of $\mathbb Q$ is divisible coordinatewise. If $\bar g$ is the image of $g$ in the quotient and $n>0$, choose $h$ upstairs with $nh=g$; then $n\bar h=\bar g$. Hence every quotient of a direct sum of $\mathbb Q$'s is divisible.

Conversely, let $G$ be divisible. Choose a generating set $(g_i)_{i\in I}$ for $G$ as an abelian group. For each $i$, divisibility lets us choose coherently elements
\[
g_{i,1}=g_i,
\qquad
n\,g_{i,n!}=g_{i,(n-1)!}
\]
for $n\ge2$; inductively this defines a homomorphism
\[
\phi_i:\mathbb Q\to G
\]
with $\phi_i(1)=g_i$ (equivalently, extend the map $\mathbb Z\to G$, $1\mapsto g_i$, across the inclusions $\mathbb Z\subset \frac1{2!}\mathbb Z\subset\frac1{3!}\mathbb Z\subset\cdots$ using divisibility).
Taking the direct sum gives
\[
\Phi:\bigoplus_{i\in I}\mathbb Q\to G.
\]
Its image contains every generator $g_i$, so $\Phi$ is surjective. Thus $G$ is a quotient of a direct sum of copies of $\mathbb Q$.

By Exercise 3, $\operatorname{Ext}(A,\mathbb Q)=0$ for every $A$. Ext takes direct sums in the second variable here to the corresponding direct sums for free resolutions of $A$, so
\[
\operatorname{Ext}\!\left(A,\bigoplus_I\mathbb Q\right)=0.
\]
If
\[
0\to K\to\bigoplus_I\mathbb Q\to G\to0
\]
is the quotient sequence, the six-term exact sequence for $\operatorname{Hom}(A,-)$ and $\operatorname{Ext}(A,-)$ ends with
\[
\operatorname{Ext}\!\left(A,\bigoplus_I\mathbb Q\right)
\longrightarrow \operatorname{Ext}(A,G)\longrightarrow0.
\]
The left group is zero, hence
\[
\boxed{\operatorname{Ext}(A,G)=0}
\]
for every divisible $G$.
:::
