---
schema: qual/card@1
id: E-HAT-2.2-27
kind: problem
title: Splitting of chain short exact sequences does not give splitting of homology
classification:
  areas:
  - topology
  topics:
  - Homology
  - Exact Sequences
  - Chain Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 27; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof checked.
---

::: {.problem}
The short exact sequences $0 \to C_n(A) \to C_n(X) \to C_n(X, A) \to 0$ always split, but why does this not always yield splittings $H_n(X) \approx H_n(A) \oplus H_n(X, A)$?
:::

::: {.solution}
The issue is that a splitting of the short exact sequence
\[
0\to C_n(A)\to C_n(X)\to C_n(X,A)\to0
\]
for each individual degree $n$ need not be compatible with the boundary operators.

<1>1. Degreewise splittings need not assemble to a splitting of chain complexes.
::: {.proof}
A group-theoretic section
\[
s_n:C_n(X,A)\to C_n(X)
\]
only satisfies that the quotient map composed with $s_n$ is the identity. There is no reason for
\[
\partial s_n=s_{n-1}\partial.
\]
Without this chain-map condition, $s_n$ need not take relative cycles to absolute cycles, nor relative boundaries to absolute boundaries. Hence it does not in general induce a map on homology.
:::

<1>2. The connecting homomorphism in the long exact sequence measures this failure.
::: {.proof}
The short exact sequence of chain complexes yields
\[
\cdots\to H_n(A)\to H_n(X)\to H_n(X,A)
\xrightarrow{\partial}H_{n-1}(A)\to\cdots.
\]
If the chain sequence split as chain complexes, this connecting map would be zero and the homology sequence would split. In general the connecting map can be nonzero, precisely because a degreewise section fails to commute with boundaries.
:::

<1>3. For example, take
\[
(X,A)=(D^n,S^{n-1}),
\qquad n\ge2.
\]
Then no decomposition
\[
H_n(X)\cong H_n(A)\oplus H_n(X,A)
\]
is possible.
::: {.proof}
Here
\[
H_n(D^n)=0,
\qquad
H_n(S^{n-1})=0,
\qquad
H_n(D^n,S^{n-1})\cong\mathbb Z.
\]
Thus the proposed splitting would assert
\[
0\cong0\oplus\mathbb Z,
\]
a contradiction. Indeed the connecting map
\[
H_n(D^n,S^{n-1})\xrightarrow{\cong}H_{n-1}(S^{n-1})
\]
is an isomorphism.
:::

Therefore degreewise splittings of singular chain groups do not imply splittings on homology.
:::
