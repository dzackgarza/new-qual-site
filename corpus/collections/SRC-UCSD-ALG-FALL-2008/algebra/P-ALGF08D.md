---
schema: qual/card@1
id: P-ALGF08D
kind: problem
title: "Intermediate extensions of abelian Galois extensions are Galois"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 4 of the official UCSD Algebra Qualifying Examination, Fall 2008; the statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the normal-subgroup criterion in the finite Galois correspondence and the resulting quotient description of the intermediate Galois group.
---

::: {.problem}
Let $E$ be a finite Galois extension of $F$ with an abelian Galois group.
Show that any intermediate extension is also Galois over $F$.
:::

::: {.solution}
Let
\[
F\subseteq K\subseteq E
\]
be an intermediate field, and set
\[
G:=\operatorname{Gal}(E/F),
\qquad
H:=\operatorname{Gal}(E/K).
\]

<1>1. The subgroup \(H\) is normal in \(G\).
::: {.proof}
By hypothesis, \(G\) is abelian.
Every subgroup of an abelian group is normal, so
\[
H\triangleleft G.
\]
:::

<1>2. The extension \(K/F\) is Galois.
::: {.proof}
The fundamental theorem of Galois theory for the finite Galois extension \(E/F\) states that an intermediate field \(K\) is Galois over \(F\) if and only if its corresponding subgroup
\[
H=\operatorname{Gal}(E/K)
\]
is normal in
\[
G=\operatorname{Gal}(E/F).
\]
By <1>1, \(H\) is normal.
Therefore
\[
K/F
\]
is Galois.
Moreover, the restriction map induces the canonical isomorphism
\[
\operatorname{Gal}(K/F)\cong G/H.
\]
Since \(K\) was arbitrary, every intermediate extension of \(E/F\) is Galois over \(F\).
:::
:::
