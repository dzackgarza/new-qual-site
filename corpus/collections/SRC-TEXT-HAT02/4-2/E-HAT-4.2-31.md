---
schema: qual/card@1
id: E-HAT-4.2-31
kind: problem
title: "Split sequences from nullhomotopic fiber inclusions"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 31; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
For a fiber bundle $F \to E \to B$ such that the inclusion $F \hookrightarrow E$ is homotopic to a constant map, show that the long exact sequence of homotopy groups breaks up into split short exact sequences giving isomorphisms $\pi_n(B) \approx \pi_n(E) \oplus \pi_{n-1}(F)$.
In particular, for the Hopf bundles $S^1 \to S^3 \to S^2$, $S^3 \to S^7 \to S^4$, and $S^7 \to S^{15} \to S^8$ this yields isomorphisms $\pi_n(S^2) \approx \pi_n(S^3) \oplus \pi_{n-1}(S^1)$, $\pi_n(S^4) \approx \pi_n(S^7) \oplus \pi_{n-1}(S^3)$, and $\pi_n(S^8) \approx \pi_n(S^{15}) \oplus \pi_{n-1}(S^7)$.
Thus $\pi_3(S^2)$, $\pi_7(S^4)$, and $\pi_{15}(S^8)$ contain $\mathbb{Z}$ summands.
:::

::: {.solution}
Let
\[
F\xrightarrow{i}E\xrightarrow{p}B
\]
be the bundle, and suppose \(i\) is nullhomotopic. Then \(i_*\) is zero on every homotopy group. The long exact sequence therefore breaks into short exact sequences
\[
0\longrightarrow\pi_n(E)
\xrightarrow{p_*}\pi_n(B)
\xrightarrow{\partial}\pi_{n-1}(F)
\longrightarrow0.
\]

To split this sequence, represent \(\alpha\in\pi_{n-1}(F)\) by
\[
a:S^{n-1}\to F.
\]
Since \(i\) is nullhomotopic, \(ia\) extends to a map
\[
A:D^n\to E.
\]
Then \(pA\) sends \(\partial D^n\) to the basepoint of \(B\), so it defines a class
\[
s(\alpha)=[pA]\in\pi_n(B).
\]
Different choices of representative and extension change \(pA\) by a based homotopy, so \(s\) is well-defined; juxtaposing extensions shows that \(s\) is a homomorphism. By the definition of the connecting homomorphism, lifting \(pA\) by \(A\) gives
\[
\partial s(\alpha)=\alpha.
\]
Thus \(s\) is a section of \(\partial\), and
\[
\boxed{\pi_n(B)\cong\pi_n(E)\oplus\pi_{n-1}(F).}
\]

For the Hopf bundles the fiber inclusions are nullhomotopic because the total space sphere has no homotopy in the fiber dimension. Hence
\[
\pi_n(S^2)\cong\pi_n(S^3)\oplus\pi_{n-1}(S^1),
\]
\[
\pi_n(S^4)\cong\pi_n(S^7)\oplus\pi_{n-1}(S^3),
\]
and
\[
\pi_n(S^8)\cong\pi_n(S^{15})\oplus\pi_{n-1}(S^7).
\]
In particular the second summands give copies of \(\mathbb Z\) in \(\pi_3(S^2)\), \(\pi_7(S^4)\), and \(\pi_{15}(S^8)\).
:::
