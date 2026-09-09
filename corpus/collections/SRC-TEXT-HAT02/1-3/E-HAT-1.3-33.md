---
schema: qual/card@1
id: E-HAT-1.3-33
kind: problem
title: "Quotient graphs and freeness of subgroups"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 33; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Computed K-orbits of the Bass-Serre tree from the translation homomorphism and used Euler characteristic of the finite quotient graph.
---

In Example 1.44 let $d$ be the greatest common divisor of $m$ and $n$, and let $m' = m/d$ and $n' = n/d$.
Show that the graph $T_{m,n}/K$ consists of $m'$ vertices labeled $a$, $n'$ vertices labeled $b$, together with $d$ edges joining each $a$ vertex to each $b$ vertex.
Deduce that the subgroup $K \subset G_{m,n}$ is free on $dm'n' - m' - n' + 1$ generators.


::: {.solution}
Recall from Example 1.44 that
\[
G_{m,n}=\langle a,b\mid a^m=b^n\rangle
\]
acts on the tree $T_{m,n}$, and that
\[
K=\ker\chi,
\]
where after scaling the translation action to have image $\mathbb Z$ one may take
\[
\chi(a)=n',
\qquad
\chi(b)=m',
\]
with
\[
m=dm',\qquad n=dn',\qquad \gcd(m',n')=1.
\]

<1>1. The quotient graph $T_{m,n}/K$ has $m'$ vertices of the type labeled $a$ and $n'$ vertices of the type labeled $b$.
::: {.proof}
In the Bass--Serre tree, the vertices labeled $a$ are the cosets of the subgroup $\langle b\rangle$, while the vertices labeled $b$ are the cosets of $\langle a\rangle$.
Passing to $K$-orbits and using
\[
G_{m,n}/K\cong\mathbb Z
\]
gives
\[
K\backslash G_{m,n}/\langle b\rangle
\cong
\mathbb Z/\chi(\langle b\rangle)
\cong
\mathbb Z/m'\mathbb Z,
\]
so there are $m'$ $a$-vertices.
Similarly,
\[
K\backslash G_{m,n}/\langle a\rangle
\cong
\mathbb Z/n'\mathbb Z,
\]
so there are $n'$ $b$-vertices.
:::

<1>2. The quotient graph has
\[
dm'n'
\]
edges.
::: {.proof}
The stabilizer of an edge in $T_{m,n}$ is the central subgroup
\[
Z=\langle a^m\rangle=\langle b^n\rangle.
\]
Since
\[
\chi(a^m)=mn'=dm'n',
\]
we have
\[
\chi(Z)=dm'n'\mathbb Z.
\]
Therefore
\[
K\backslash G_{m,n}/Z
\cong
\mathbb Z/(dm'n')\mathbb Z,
\]
so there are $dm'n'$ edge orbits.
:::

<1>3. Each $a$-vertex is joined to each $b$-vertex by exactly $d$ edges.
::: {.proof}
The quotient action of $G_{m,n}/K\cong\mathbb Z$ is transitive on the vertices of each fixed type modulo the respective stabilizers, so the number of edges joining a given pair of vertex orbits is constant.
There are
\[
m'n'
\]
pairs consisting of one $a$-vertex and one $b$-vertex, while <1>2 gives $dm'n'$ edges total.
Hence each pair is joined by exactly
\[
\frac{dm'n'}{m'n'}=d
\]
edges.
Thus $T_{m,n}/K$ has exactly the asserted form.
:::

<1>4. The action of $K$ on $T_{m,n}$ is free, so
\[
K\cong\pi_1(T_{m,n}/K).
\]
::: {.proof}
The kernel of the $G_{m,n}$-action on the tree is the central subgroup
\[
Z=\langle a^m\rangle.
\]
But
\[
K\cap Z=1
\]
because $\chi(a^m)=dm'n'\ne0$.
Vertex stabilizers are conjugates of the cyclic vertex groups, and their intersection with $K$ is likewise trivial since $\chi(a)$ and $\chi(b)$ are nonzero.
Hence $K$ acts freely on the tree.
A group acting freely on a tree is naturally the fundamental group of its quotient graph.
:::

<1>5. Therefore $K$ is free of rank
\[
\boxed{dm'n'-m'-n'+1.}
\]
::: {.proof}
The quotient graph is connected and finite, with
\[
E=dm'n',
\qquad
V=m'+n'.
\]
The fundamental group of a connected finite graph is free of rank
\[
E-V+1.
\]
Using <1>4 gives
\[
\operatorname{rank}K
=dm'n'-m'-n'+1.
\]
:::
:::
