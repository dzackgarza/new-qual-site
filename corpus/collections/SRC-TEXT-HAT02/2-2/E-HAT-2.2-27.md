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
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the two points: a degreewise section need not commute with boundaries, so it does not take
    relative cycles to absolute cycles and does not pass to homology; the connecting map of the
    long exact sequence is the obstruction, being zero exactly when the chain sequence splits; and
    $(D^n,S^{n-1})$ has both absolute groups zero and the relative group $\ZZ$.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 27 as printed on p. 157. The answer is right - the degreewise
    sections are not a chain map - and is now pinned to the book: the degreewise splitting is the
    Splitting Lemma on pp. 147-148 with the remark that a sequence ending in a free group splits,
    which applies because C_n(X,A) is free; chain maps and their induced maps are Proposition 2.9
    and Proposition 2.12, pp. 111 and 113; the long exact sequence is Theorem 2.16 p. 117, with
    the deduction of a splitting from a retraction as on p. 148. The example (D^n,S^{n-1}) is
    correct at degree n and now cites Corollary 2.14 p. 114; p. 148 carries the same example at
    degree n-1. What is not covered: no certificate.
---

::: {.problem}
The short exact sequences $0 \to C_n(A) \to C_n(X) \to C_n(X, A) \to 0$ always split, but why does this not always yield splittings $H_n(X) \approx H_n(A) \oplus H_n(X, A)$?
:::

::: {.solution}
The issue is that a splitting of the short exact sequence
$$
0\to C_n(A)\to C_n(X)\to C_n(X,A)\to0
$$
for each individual degree $n$ need not be compatible with the boundary operators. Each of these sequences does split, by the Splitting Lemma (pp. 147–148), because $C_n(X,A)$ is free: it is the free abelian group on the relative simplices, so the remark on p. 148 that a short exact sequence ending in a free group splits applies. Splitting is therefore a statement about each degree separately, and says nothing about $\partial$.

::: pf

::: pf-step

Degreewise splittings need not assemble to a splitting of chain complexes.

::: pf-proof

A group-theoretic section
$$
s_n:C_n(X,A)\to C_n(X)
$$
only satisfies that the quotient map composed with $s_n$ is the identity. There is no reason for
$$
\partial s_n=s_{n-1}\partial.
$$
This is exactly the condition that makes the sections a chain map, and it is not implied by the degreewise identities. Without this chain-map condition, $s_n$ need not take relative cycles to absolute cycles, nor relative boundaries to absolute boundaries. Hence it does not in general induce a map on homology, which is what a splitting of $H_n(X)$ would require: chain maps and the maps they induce are the subject of Proposition 2.9 and Proposition 2.12 (pp. 111 and 113).

:::

:::

::: pf-step

The connecting homomorphism in the long exact sequence measures this failure.

::: pf-proof

The short exact sequence of chain complexes yields the long exact sequence of Theorem 2.16 (p. 117),
$$
\cdots\to H_n(A)\to H_n(X)\to H_n(X,A)
\xrightarrow{\partial}H_{n-1}(A)\to\cdots.
$$
If the chain sequence split as chain complexes, this connecting map would be zero and the homology sequence would break into split short exact sequences, giving $H_n(X)\cong H_n(A)\oplus H_n(X,A)$; this is the deduction made on p. 148 from the Splitting Lemma and a retraction. In general the connecting map can be nonzero, precisely because a degreewise section fails to commute with boundaries.

:::

:::

::: pf-step

For example, take
$$
(X,A)=(D^n,S^{n-1}),
\qquad n\ge2.
$$
Then no decomposition
$$
H_n(X)\cong H_n(A)\oplus H_n(X,A)
$$
is possible.

::: pf-proof

Here
$$
H_n(D^n)=0,
\qquad
H_n(S^{n-1})=0,
\qquad
H_n(D^n,S^{n-1})\cong\ZZ,
$$
the first two because $D^n$ is contractible and because $H_n(S^{n-1})=0$ for $n\ge2$ by Corollary 2.14 (p. 114), and the third by the pair sequence of Theorem 2.16 (p. 117), in which $D^n$ and $S^{n-1}$ have vanishing $H_n$ and $H_{n-1}(S^{n-1})=\ZZ$. Thus the proposed splitting would assert
$$
0\cong0\oplus\ZZ,
$$
a contradiction. Indeed the connecting map
$$
H_n(D^n,S^{n-1})\xrightarrow{\cong}H_{n-1}(S^{n-1})
$$
is an isomorphism; this is the example discussed on p. 148 in the form $H_{n-1}(D^n)\approx H_{n-1}(S^{n-1})\oplus H_{n-1}(D^n,S^{n-1})$.

:::

:::

:::

Therefore degreewise splittings of singular chain groups do not imply splittings on homology.
:::
