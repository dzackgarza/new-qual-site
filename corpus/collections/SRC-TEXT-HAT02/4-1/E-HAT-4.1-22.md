---
schema: qual/card@1
id: E-HAT-4.1-22
kind: problem
title: "Countable CW approximation for countable $\\pi_n$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 22; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

Show that a path-connected space $X$ has a CW approximation with countably many cells if $\pi_n(X)$ is countable for all $n$.

::: {.solution}
We use the standard inductive construction of a CW approximation, keeping track of cardinalities.

Start with one \(0\)-cell and attach \(1\)-cells representing a generating set for \(\pi_1(X)\). Since \(\pi_1(X)\) is countable, only countably many \(1\)-cells are needed. Attach countably many \(2\)-cells to kill the kernel of the resulting map on \(\pi_1\): the kernel is countable because the fundamental group of a countable CW complex is countable.

Inductively suppose a countable CW complex \(K_n\) and a map
\[
f_n:K_n\to X
\]
have been constructed inducing isomorphisms on \(\pi_i\) for \(i<n\) and a surjection on \(\pi_n\). The group \(\pi_n(K_n)\) is countable: every map \(S^n\to K_n\) has compact image, hence lies in a finite subcomplex, and there are only countably many finite subcomplexes and countably many homotopy classes of maps into each. Thus the kernel of
\[
(f_n)_*:\pi_n(K_n)\to\pi_n(X)
\]
is countable. Attach one \((n+1)\)-cell for each element of a countable generating set of this kernel. Then attach countably many further \((n+1)\)-cells, if necessary, to represent the countable group \(\pi_{n+1}(X)\) and make the next homotopy map surjective.

At every stage only countably many cells are added. Taking the union
\[
K=\bigcup_n K_n
\]
produces a CW complex with countably many cells and a map \(K\to X\) inducing isomorphisms on every homotopy group. Hence \(K\to X\) is a CW approximation, and
\[
\boxed{X\text{ has a CW approximation with countably many cells}.}
\]
:::
