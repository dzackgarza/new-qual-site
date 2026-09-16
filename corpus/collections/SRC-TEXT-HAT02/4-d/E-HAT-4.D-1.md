---
schema: qual/card@1
id: E-HAT-4.D-1
kind: problem
title: "Cup product structure on pullbacks of $\\mathbb{CP}^3 \\to S^4$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.D, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
By Exercise 35 in §4.2 there is a bundle $S^2 \to \mathbb{CP}^3 \to S^4$.
Let $S^2 \to E_k \to S^4$ be the pullback of this bundle via a degree $k$ map $S^4 \to S^4$, $k > 1$.
Use the Leray-Hirsch theorem to show that $H^*(E_k; \mathbb{Z})$ is additively isomorphic to $H^*(\mathbb{CP}^3; \mathbb{Z})$ but has a different cup product structure in which the square of a generator of $H^2(E_k; \mathbb{Z})$ is $k$ times a generator of $H^4(E_k; \mathbb{Z})$.
:::

::: {.solution}
Let \(p:\mathbb{CP}^3\to S^4\) denote the bundle and let \(f:S^4\to S^4\) have degree \(k\). Form the pullback square
\[
\begin{array}{ccc}
E_k&\xrightarrow{F}&\mathbb{CP}^3\\
\downarrow p_k&&\downarrow p\\
S^4&\xrightarrow{f}&S^4.
\end{array}
\]
Choose \(x\in H^2(\mathbb{CP}^3;\mathbb Z)\) restricting to a generator on each fiber \(S^2\). Then \(F^*x\), which we again call \(x\), restricts to a generator on each fiber of \(E_k\). Leray--Hirsch gives
\[
H^*(E_k;\mathbb Z)\cong H^*(S^4;\mathbb Z)\{1,x\}
\]
as an \(H^*(S^4)\)-module. Thus additively there is one copy of \(\mathbb Z\) in degrees \(0,2,4,6\), exactly as for \(\mathbb{CP}^3\).

Let \(u\in H^4(S^4;\mathbb Z)\) be a generator and normalize signs so that in \(\mathbb{CP}^3\)
\[
x^2=p^*u.
\]
Put \(v=p_k^*u\in H^4(E_k)\). Naturality in the pullback square gives
\[
x^2=F^*(x^2)=F^*p^*u=p_k^*f^*u=k\,p_k^*u=kv.
\]
Hence
\[
\boxed{x^2=kv,}
\]
where \(x\) and \(v\) generate \(H^2(E_k)\) and \(H^4(E_k)\). Since \(k>1\), this ring cannot be isomorphic to \(H^*(\mathbb{CP}^3;\mathbb Z)\), although the additive groups are the same.
:::
