---
schema: qual/card@1
id: E-HAT-4.1-21
kind: problem
title: "Postnikov towers and covering spaces commute"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 21; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

For this problem it is convenient to use the notations $X^n$ for the $n$th stage in a Postnikov tower for $X$ and $X_m$ for an $(m-1)$-connected covering of $X$, where $X$ is a connected CW complex.
Show that $(X^n)_m \simeq (X_m)^n$, so the notation $X_m^n$ is unambiguous.
Thus $\pi_i(X_m^n) \approx \pi_i(X)$ for $m \leq i \leq n$ and all other homotopy groups of $X_m^n$ are zero.

::: {.solution}
Let \(X^n\) be the \(n\)-th Postnikov stage of \(X\), and \(X_m\) an \((m-1)\)-connected covering of \(X\). The two constructions affect disjoint ranges of homotopy groups:

- passing to \(X^n\) preserves \(\pi_i\) for \(i\le n\) and kills \(\pi_i\) for \(i>n\);
- passing to \(X_m\) kills \(\pi_i\) for \(i<m\) and preserves \(\pi_i\) for \(i\ge m\).

Therefore both iterated constructions \((X^n)_m\) and \((X_m)^n\) have homotopy groups
\[
\pi_i\cong
\begin{cases}
\pi_i(X),&m\le i\le n,\\
0,&i<m\text{ or }i>n.
\end{cases}
\]
The natural maps in the two constructions give a comparison map
\[
(X^n)_m\longrightarrow (X_m)^n
\]
compatible with the maps to the corresponding Postnikov stages of \(X\). On every homotopy group this comparison is an isomorphism by the displayed calculation. Both spaces have CW type, so Whitehead's theorem gives
\[
\boxed{(X^n)_m\simeq (X_m)^n.}
\]
Thus the notation \(X_m^n\) is unambiguous up to homotopy, and it has exactly the stated nonzero homotopy groups.
:::
