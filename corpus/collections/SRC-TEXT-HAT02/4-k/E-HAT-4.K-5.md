---
schema: qual/card@1
id: E-HAT-4.K-5
kind: problem
title: "Quasifibrations"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.K, Exercise 5 and the corrected current statement of Lemma 4K.3 where relevant; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

A map $p: E \to B$ with $B$ not necessarily path-connected is defined to be a quasifibration if the following equivalent conditions are satisfied:

(i) For all $b \in B$ and $x_0 \in p^{-1}(b)$, the map $p_*: \pi_i(E, p^{-1}(b), x_0) \to \pi_i(B, b)$ is an isomorphism for $i > 0$ and $\pi_0(p^{-1}(b), x_0) \to \pi_0(E, x_0) \to \pi_0(B, b)$ is exact.

(ii) The inclusion of the fiber $p^{-1}(b)$ into the homotopy fiber $F_b$ of $p$ over $b$ is a weak homotopy equivalence for all $b \in B$.

(iii) The restriction of $p$ over each path-component of $B$ is a quasifibration according to the definition in this section.

Show these three conditions are equivalent, and prove Lemma 4K.3 for quasifibrations over non-path-connected base spaces.

::: {.solution}
Fix \(b\in B\) and \(x_0\in p^{-1}(b)\). Let \(F_b\) denote the homotopy fiber of \(p\) over \(b\). There is a natural inclusion
\[
j:p^{-1}(b)\hookrightarrow F_b
\]
obtained by using the constant path at \(b\).

The homotopy fiber fits into the fibration sequence
\[
F_b\longrightarrow E\longrightarrow B,
\]
whose long exact homotopy sequence identifies, for \(i>0\),
\[
\pi_i(F_b,p^{-1}(b),x_0)
\cong
\ker\!\left[\pi_i(E,p^{-1}(b),x_0)\to\pi_i(B,b)\right]
\]
together with the corresponding cokernel one degree higher. Comparing the long exact sequence of the pair \((E,p^{-1}(b))\) with that of the homotopy-fiber fibration and applying the five-lemma shows:
\[
j:p^{-1}(b)\to F_b\text{ is a weak equivalence}
\]
if and only if
\[
p_*:\pi_i(E,p^{-1}(b),x_0)\xrightarrow{\cong}\pi_i(B,b)
\qquad(i>0),
\]
with the stated exactness condition on \(\pi_0\). Hence **(i) and (ii) are equivalent**.

Next, all homotopy groups based at \(b\), and all relative homotopy classes appearing in (i), are contained in the path component \(B_b\) of \(b\) and its inverse image. The same is true for the homotopy fiber. Thus condition (i), equivalently (ii), holds for every \(b\in B\) exactly when it holds after restricting \(p\) to each path component of \(B\). This is condition (iii). Hence
\[
\boxed{(i)\Longleftrightarrow(ii)\Longleftrightarrow(iii).}
\]

We now extend Lemma 4K.3 to non-path-connected bases. Each proof in the lemma is based at a chosen point \(b\), so after the preceding equivalence it suffices to work in the path component containing \(b\).

- In **(a)**, intersect the two open sets with this path component. The five-lemma proof with the triples used in Hatcher then applies verbatim. The \(\pi_0\)-tail is handled by the exactness clause in (i).
- In **(b)**, use the corrected current hypothesis that every compact subset of \(B\) is contained in some \(B_n\). A representative sphere or disk has compact image, so each relative homotopy class occurs in some stage. Consequently
  \[
  \pi_i(E,p^{-1}(b))\cong\varinjlim_n
  \pi_i(p^{-1}(B_n),p^{-1}(b)),
  \]
  and similarly for \(B\). The stagewise isomorphisms therefore pass to the colimit. The same compactness argument gives the required statement on components.
- In **(c)**, the path \(t\mapsto\bar F_t(b)\) stays in the path component of \(b\). The proof of Hatcher's lemma therefore takes place entirely in this component. Since
  \[
  F_1:p^{-1}(b)\to p^{-1}(\bar F_1(b))
  \]
  is a weak equivalence, the same diagram chase proves the relative homotopy isomorphisms and the \(\pi_0\)-exactness.

Thus all three sufficient criteria of Lemma 4K.3 remain valid for arbitrary, possibly disconnected bases.
:::
