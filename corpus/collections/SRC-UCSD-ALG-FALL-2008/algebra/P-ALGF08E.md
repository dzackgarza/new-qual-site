---
schema: qual/card@1
id: P-ALGF08E
kind: problem
title: "Every K-monomorphism of an algebraic extension to itself is surjective"
classification:
  areas:
  - algebra
  topics:
  - Field Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 5 of the official UCSD Algebra Qualifying Examination, Fall 2008; the statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified surjectivity without assuming finite degree by showing that the iterates of each algebraic element under the K-embedding lie among finitely many roots of its minimal polynomial.
---

::: {.problem}
If $L$ is a field algebraic over the subfield $K$, show that any $K$-monomorphism of $L$ to $L$ is onto.
:::

::: {.solution}
Let
\[
\sigma:L\longrightarrow L
\]
be a \(K\)-monomorphism.
Thus \(\sigma\) fixes every element of \(K\) and is injective.

<1>1. For every \(a\in L\), all iterates
\[
a,\sigma(a),\sigma^2(a),\ldots
\]
are roots of the same polynomial over \(K\).
::: {.proof}
Because \(L/K\) is algebraic, \(a\) has a minimal polynomial
\[
m_a(T)\in K[T].
\]
Since
\[
m_a(a)=0
\]
and \(\sigma\) fixes the coefficients of \(m_a\), applying \(\sigma\) gives
\[
m_a(\sigma(a))=0.
\]
Repeating the argument shows
\[
m_a(\sigma^n(a))=0
\]
for every \(n\ge0\).
Thus every iterate is a root of \(m_a\).
:::

<1>2. Every element \(a\in L\) lies in the image of \(\sigma\).
::: {.proof}
The polynomial \(m_a\) has only finitely many roots in the field \(L\).
By <1>1, the infinite sequence
\[
a,\sigma(a),\sigma^2(a),\ldots
\]
takes values in this finite set.
Hence there exist integers
\[
r>s\ge0
\]
such that
\[
\sigma^r(a)=\sigma^s(a).
\]
Because \(\sigma^s\) is injective, cancellation gives
\[
\sigma^{r-s}(a)=a.
\]
Set
\[
b:=\sigma^{r-s-1}(a)\in L.
\]
Since \(r-s\ge1\), this is defined, and
\[
\sigma(b)=a.
\]
Thus \(a\in\operatorname{im}\sigma\).
:::

<1>3. Therefore \(\sigma\) is onto.
::: {.proof}
By <1>2, every \(a\in L\) has a preimage under \(\sigma\).
Hence
\[
\operatorname{im}\sigma=L,
\]
so every \(K\)-monomorphism \(L\to L\) is surjective.
:::
:::
