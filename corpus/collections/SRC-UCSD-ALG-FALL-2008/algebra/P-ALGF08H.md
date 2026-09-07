---
schema: qual/card@1
id: P-ALGF08H
kind: problem
title: "Maximal ideal in polynomial ring over a field intersects each variable polynomial ring (Nullstellensatz)"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 8 of the official UCSD Algebra Qualifying Examination, Fall 2008; the statement and Nullstellensatz hint agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the application of Zariski's lemma to the residue field and the resulting nonzero polynomial in each single variable lying in the maximal ideal.
---

::: {.problem}
Let $R$ be the polynomial ring in $n$ variables over the field $k$.
Show that any maximal ideal in $R$ intersects the polynomial ring in each of the variables.

Hint: Nullstellensatz.
:::

::: {.solution}
Write
\[
R=k[x_1,\ldots,x_n]
\]
and let
\[
\mathfrak m\subset R
\]
be maximal.
For each \(i\), we will prove
\[
\mathfrak m\cap k[x_i]\neq(0).
\]

<1>1. The residue field \(L:=R/\mathfrak m\) is a finite algebraic extension of \(k\).
::: {.proof}
Because \(\mathfrak m\) is maximal,
\[
L=R/\mathfrak m
\]
is a field.
If \(\alpha_i\) denotes the image of \(x_i\) in \(L\), then
\[
L=k[\alpha_1,\ldots,\alpha_n].
\]
Thus \(L\) is a field finitely generated as a \(k\)-algebra.

By Zariski's lemma, equivalently the algebraic form of the weak Nullstellensatz, every field that is finitely generated as an algebra over a field \(k\) is a finite algebraic extension of \(k\).
Therefore
\[
[L:k]<\infty,
\]
and in particular every \(\alpha_i\) is algebraic over \(k\).
:::

<1>2. For every \(i\), the maximal ideal \(\mathfrak m\) contains a nonzero polynomial involving only \(x_i\).
::: {.proof}
Fix \(i\).
By <1>1, \(\alpha_i\) is algebraic over \(k\).
Let
\[
f_i(T)\in k[T]
\]
be its monic minimal polynomial.
Then \(f_i\neq0\) and
\[
f_i(\alpha_i)=0
\]
in \(L=R/\mathfrak m\).
Equivalently,
\[
f_i(x_i)\in\mathfrak m.
\]
Since the substitution map
\[
k[T]\longrightarrow k[x_i],
\qquad
T\longmapsto x_i
\]
is an isomorphism of polynomial rings, \(f_i(x_i)\neq0\).
Hence
\[
0\neq f_i(x_i)\in\mathfrak m\cap k[x_i].
\]
Therefore
\[
\mathfrak m\cap k[x_i]\neq(0).
\]
:::

<1>3. The conclusion holds for every variable.
::: {.proof}
The argument in <1>2 applies independently to each
\[
i=1,\ldots,n.
\]
Thus a maximal ideal of \(k[x_1,\ldots,x_n]\) has nonzero intersection with each one-variable subring \(k[x_i]\).
:::
:::
