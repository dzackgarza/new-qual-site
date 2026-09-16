---
schema: qual/card@1
id: E-HAT-4.K-6
kind: problem
title: "Projection from $\\Delta X$ is a quasifibration"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.K, Exercise 6 and the corrected current statement of Lemma 4K.3 where relevant; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $X$ be a complex of spaces over a simplicial complex $\Gamma$, as defined in §4.G. Show that the natural projection $\Delta X \to \Gamma$ is a quasifibration if all the maps in $X$ associated to edges of $\Gamma$ are weak homotopy equivalences.
:::

::: {.solution}
Let
\[
p:\Delta X\longrightarrow\Gamma
\]
be the canonical projection. We prove that it is a quasifibration.

First restrict over a simplex
\[
\sigma=[v_0,\ldots,v_q]\subset\Gamma.
\]
By definition, \(p^{-1}(\sigma)\) is the iterated mapping cylinder of the sequence of edge maps
\[
X_{v_0}\longrightarrow X_{v_1}\longrightarrow\cdots\longrightarrow X_{v_q}.
\]
Collapse \(\sigma\) linearly to its terminal vertex \(v_q\). The corresponding deformation of the iterated mapping cylinder collapses it to \(X_{v_q}\). For a point \(b\in\sigma\), the induced map from the fiber \(p^{-1}(b)\) to the terminal fiber \(X_{v_q}\) is a composite of edge maps. By hypothesis every edge map is a weak homotopy equivalence, hence so is every such composite. Lemma 4K.3(c) therefore implies
\[
p:p^{-1}(\sigma)\to\sigma
\]
is a quasifibration. The same argument applies to every face of \(\sigma\).

Now pass from a single simplex to the whole complex. Over each finite subcomplex \(L\subset\Gamma\), glue the simplexwise quasifibrations one simplex at a time. Near the attaching boundary of a simplex use a collar, so Lemma 4K.3(a) applies; the intersections are precisely restrictions over faces, already known to be quasifibrations. Hence
\[
p:p^{-1}(L)\to L
\]
is a quasifibration for every finite subcomplex \(L\).

Finally exhaust \(\Gamma\) by its finite subcomplexes. Every compact subset of a CW complex is contained in a finite subcomplex, so the corrected form of Lemma 4K.3(b) applies. Therefore
\[
\boxed{\Delta X\longrightarrow\Gamma\text{ is a quasifibration}.}
\]
The fiber over a vertex \(v\) is the corresponding vertex space \(X_v\), and fibers over arbitrary points are weakly equivalent to these via the edge maps.
:::
