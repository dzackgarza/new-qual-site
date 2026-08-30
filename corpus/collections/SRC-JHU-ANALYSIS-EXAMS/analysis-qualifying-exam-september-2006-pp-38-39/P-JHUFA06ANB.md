---
schema: qual/card@1
id: P-JHUFA06ANB
kind: problem
title: "Hurwitz theorem for uniformly convergent holomorphic sequences with one zero"
classification:
  areas:
  - complex-analysis
  topics:
  - Hurwitz's Theorem
  - Normal Families
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

2. Let $f _ { n } : D \to \mathbb { C } , n = 1 , 2 , 3 , . . . ,$ be a sequence of holomorphic functions on the unit disk D such that $f _ { n } ^ { - 1 } ( 0 ) = \{ c _ { n } \}$ , where $c _ { n } \in D$ . Suppose that $f _ { n }  f _ { 0 }$ uniformly, where $f _ { 0 }$ is not constant.

a) Prove that $f _ { 0 }$ has at most one zero in $D$

b) Can $f _ { 0 }$ have no zeros?
If so, give a necessary and sufficient condition on the $c _ { n }$ for this to happen.

::: {.solution}
**(a).**

<1>1. $f_n\to f_0$ uniformly on compacta, $f_0$ nonconstant, $f_n$ has exactly one zero $c_n$.
Proof: hypothesis.

<1>2. By Hurwitz, any zero $c$ of $f_0$ is limit of zeros $c_n$; since each $f_n$ has one zero, $f_0$ has at most one zero (counting multiplicity).
Proof: Hurwitz theorem.

**(b).**

<1>1. $f_0$ can be zero-free.
Proof: example $f_n(z)=z- (1-1/n)$ has zero $c_n=1-1/n\to1\notin D$, limit $f_0(z)=z-1$ zero-free in $D$.

<1>2. $f_0$ zero-free iff $|c_n|\to1$.
Proof: if $c_n\to c\in D$ then $f_0(c)=0$; if $|c_n|\to1$ then zeros escape to boundary and limit has no zero in $D$.

<1>3. Q.E.D.
Proof: <1>2 and <1>2(b).
:::
