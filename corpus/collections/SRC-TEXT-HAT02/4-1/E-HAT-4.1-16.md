---
schema: qual/card@1
id: E-HAT-4.1-16
kind: problem
title: "Factoring maps through $n$-connective covers"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 16 and the cell-attachment construction preceding Proposition 4.13; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

Show that a map $f: X \to Y$ between connected CW complexes factors as a composition $X \to Z_n \to Y$ where the first map induces isomorphisms on $\pi_i$ for $i \leq n$ and the second map induces isomorphisms on $\pi_i$ for $i \geq n+1$.

::: {.solution}
Use the relative cell-attachment construction from the proof preceding Proposition 4.13. Starting with
\[
f:X\longrightarrow Y,
\]
attach cells to the source only in dimensions at least \(n+1\), extending the map over every attached cell.

Inductively, suppose a map
\[
f_k:Z_k\to Y
\]
has already been made an isomorphism on \(\pi_i\) for
\[
n+1\le i<k.
\]
Attach \(k\)-cells corresponding to generators of the relative group
\[
\pi_k(Y,Z_k)
\]
so that the resulting map is surjective on \(\pi_k\). Then attach \((k+1)\)-cells along representatives of the kernel of
\[
\pi_k(Z_k)\to\pi_k(Y)
\]
and extend them over \(Y\) by chosen nullhomotopies. The resulting map is an isomorphism on \(\pi_k\), while the already established lower homotopy groups are unchanged.

Begin this process at \(k=n+1\) and continue for all \(k\). Let \(Z_n\) be the union. Since every cell added to \(X\) has dimension at least \(n+1\), cellular approximation for the pair \((Z_n,X)\) gives
\[
\pi_i(Z_n,X)=0\qquad(i\le n),
\]
so the long exact sequence of the pair yields
\[
\pi_i(X)\xrightarrow{\cong}\pi_i(Z_n)
\qquad(i\le n).
\]
By the inductive construction, the extension
\[
g:Z_n\to Y
\]
induces isomorphisms
\[
\pi_i(Z_n)\xrightarrow{\cong}\pi_i(Y)
\qquad(i\ge n+1).
\]
The original map is the composite
\[
X\longrightarrow Z_n\xrightarrow{g}Y.
\]
Thus
\[
\boxed{f\text{ has the required factorization}.}
\]
:::
