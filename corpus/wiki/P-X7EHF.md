---
schema: qual/card@1
id: P-X7EHF
kind: problem
title: "Let $R$ be a commutative ring with $1\\neq 0$."
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
Let $R$ be a commutative ring with $1\neq 0$.
Recall that $x\in R$ is *nilpotent* iff $x^n = 0$ for some positive integer $n$.

a.
Show that the collection of nilpotent elements in $R$ forms an ideal.

b.
Show that if $x$ is nilpotent, then $x$ is contained in every prime ideal of $R$.

c.
  Suppose $x\in R$ is not nilpotent and let $S = \theset{x^n \suchthat n\in \NN}$.
  There is at least on ideal of $R$ disjoint from $S$, namely $(0)$.

  By Zorn's lemma the set of ideals disjoint from $S$ has a maximal element with respect to inclusion, say $I$.
  In other words, $I$ is disjoint from $S$ and if $J$ is any ideal disjoint from $S$ with $I\subseteq J \subseteq R$ then $J=I$ or $J=R$.

  Show that $I$ is a prime ideal.
