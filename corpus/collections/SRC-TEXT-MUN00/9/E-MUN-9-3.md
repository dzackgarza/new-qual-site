---
schema: qual/card@1
id: E-MUN-9-3
kind: problem
title: Infinite sets from sequences of injections
classification:
  areas:
  - topology
  topics:
  - Infinite Sets and the Axiom of Choice
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 9, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Suppose that $A$ is a set and $\{f_n\}_{n \in \mathbf{Z}_+}$ is a given indexed family of injective functions

$$
f _ {n}: \{1, \dots , n \} \longrightarrow A.
$$

Show that $A$ is infinite.
Can you define an injective function $f: \mathbb{Z}_+ \to A$ without using the choice axiom?
:::

::: {.solution}
For each \(n\), the injection
\[
f_n:\{1,\ldots,n\}\to A
\]
has an image containing exactly \(n\) distinct elements. If \(A\) were finite, say \(|A|=N\), then \(f_{N+1}\) would inject an \((N+1)\)-element set into an \(N\)-element set, impossible. Thus \(A\) is infinite.

Moreover, an injection \(\mathbb Z_+\to A\) can be defined without the choice axiom because the entire indexed family \(\{f_n\}\) is already given.

Fix once and for all an explicit enumeration
\[
(n_1,k_1),(n_2,k_2),\ldots
\]
of all pairs with \(1\le k\le n\); for instance enumerate by increasing \(n+k\), breaking ties lexicographically. Put
\[
a_j=f_{n_j}(k_j).
\]
The set \(S=\{a_j:j\ge1\}\) is infinite, since it contains the image of every \(f_n\), and those images have arbitrarily large finite cardinality.

Define integers \(r_m\) recursively. Let \(r_1=1\). Having chosen \(r_1<\cdots<r_m\) so that \(a_{r_1},\ldots,a_{r_m}\) are distinct, let
\[
r_{m+1}=\min\{j>r_m:a_j\notin\{a_{r_1},\ldots,a_{r_m}\}\}.
\]
The set on the right is nonempty because \(S\) is infinite. Then
\[
F(m)=a_{r_m}
\]
defines an injection \(F:\mathbb Z_+\to A\). Every selection was made by taking a least positive integer, so no choice axiom is used.
:::
