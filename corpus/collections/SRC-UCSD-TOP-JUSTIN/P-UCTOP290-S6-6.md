---
schema: qual/card@1
id: P-UCTOP290-S6-6
kind: problem
title: Retractions, sections, and splitting of an exact sequence
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Abelian Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 6, Problem 6 in its checked-in extraction and PDF page image.
---

::: {.problem}
For a short exact sequence of abelian groups
$$
0\to A\xrightarrow{i}B\xrightarrow{p}C\to0,
$$
prove that the following are equivalent:
$i$ has a retraction, $p$ has a section, and
$B\cong A\oplus C$ compatibly with $i$ and $p$.
Show that the sequence splits if $C$ is free.
:::

::: {.solution}

Suppose $r:B\to A$ satisfies $ri=1_A$.
For $c\in C$, choose $b\in B$ with $p(b)=c$
and set $s(c)=b-i(r(b))$. If $b$ changes by
$i(a)$, this expression is unchanged.
Therefore $s$ is a homomorphism, and
$ps=1_C$.

Conversely, if $s:C\to B$ satisfies
$ps=1_C$, then $b-s(p(b))$ lies in
$\ker p=\operatorname{im}i$. Since $i$ is
injective, it has a unique preimage
$r(b)\in A$. This defines a homomorphism
with $ri=1_A$.

Given $s$, the map
$$
A\oplus C\longrightarrow B,\qquad
(a,c)\longmapsto i(a)+s(c)
$$
is an isomorphism: its inverse sends
$b$ to $(r(b),p(b))$. It carries the
standard inclusion and projection to
$i$ and $p$. Such an isomorphism conversely
supplies both $r$ and $s$.

If $C$ is free, choose a basis and lift
each basis element through the surjection
$p$. Extending these lifts linearly defines
a section, so the sequence splits.
:::
