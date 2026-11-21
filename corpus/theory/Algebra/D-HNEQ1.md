---
schema: qual/card@1
id: D-HNEQ1
kind: definition
title: Localization of a ring at a multiplicative subset
classification:
  areas:
  - algebra
  topics:
  - Localization
  - Commutative Algebra
relations: []
review: draft
---

::: {.definition}
Let $A$ be a commutative [[D-GURUB|ring]] and let $S\subseteq A$ be a subset with $1\in S$ that is closed under multiplication.
On $A\times S$ put $(x,s)\sim(y,t)$ when $(xt-ys)u=0$ for some $u\in S$, and write $a/s$ for the class of $(a,s)$.
The \dfn{localization of $A$ at $S$}, written $A\localize{S}$, is the ring $(A\times S)/{\sim}$, and $a\mapsto a/1$ is a ring map $A\to A\localize{S}$ [Stacks, Tag 00CN; Stacks, Tag 00CO].
:::

::: {.proposition}
Let $A$ and $B$ be commutative rings, let $S\subseteq A$ be a subset with $1\in S$ that is closed under multiplication, and let $f\colon A\to B$ be a ring map that sends every element of $S$ to a unit of $B$.
Then there is exactly one ring map $g\colon A\localize{S}\to B$ with $g(a/1)=f(a)$ for every $a\in A$ [Stacks, Tag 00CP].
:::
