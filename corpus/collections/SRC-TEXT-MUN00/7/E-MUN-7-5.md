---
schema: qual/card@1
id: E-MUN-7-5
kind: problem
title: Countability of function spaces and subsets of $\mathbb{Z}_+$
classification:
  areas:
  - topology
  topics:
  - Countable and Uncountable Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 7, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Determine, for each of the following sets, whether or not it is countable.
Justify your answers.

(a) The set $A$ of all functions $f:\{0,1\} \to \mathbb{Z}_{+}$ .

(b) The set $B_{n}$ of all functions $f:\{1,\ldots ,n\} \to \mathbb{Z}_{+}$ .

(c) The set $C = \bigcup_{n\in \mathbf{Z}_{+}}B_{n}$ .

(d) The set $D$ of all functions $f: \mathbb{Z}_{+} \to \mathbb{Z}_{+}$ .

(e) The set E of all functions $f : Z_{+} \to \{0, 1\}$ .

(f) The set $F$ of all functions $f: \mathbb{Z}_{+} \to \{0,1\}$ that are "eventually zero."
[We say that $f$ is eventually zero if there is a positive integer $N$ such that $f(n) = 0$ for all $n \geq N$ .]

(g) The set $G$ of all functions $f: \mathbb{Z}_{+} \to \mathbb{Z}_{+}$ that are eventually 1.

(h) The set $H$ of all functions $f: \mathbb{Z}_{+} \to \mathbb{Z}_{+}$ that are eventually constant.

(i) The set $I$ of all two-element subsets of $\mathbb{Z}_{+}$ .

(j) The set $J$ of all finite subsets of $\mathbb{Z}_{+}$ .
:::

::: {.solution}
(a) \(A\) is countable: a function \(\{0,1\}\to\mathbb Z_+\) is determined by the pair \((f(0),f(1))\in\mathbb Z_+^2\), and \(\mathbb Z_+^2\) is countable.

(b) Each \(B_n\) is countable because
\[
B_n\cong(\mathbb Z_+)^n,
\]
a finite product of countable sets.

(c) \(C=\bigcup_{n\ge1}B_n\) is countable as a countable union of countable sets.

(d) \(D=(\mathbb Z_+)^\omega\) is uncountable. Indeed, the map
\[
E=\{0,1\}^\omega\hookrightarrow D,
\qquad
(x_n)\mapsto(x_n+1)
\]
is injective, and \(E\) is uncountable by the diagonal theorem.

(e) \(E=\{0,1\}^\omega\) is uncountable by Theorem 7.7.

(f) \(F\) is countable. Let \(F_N\) consist of functions that vanish for all \(n\ge N\). Such a function is determined by its first \(N-1\) binary values, so \(F_N\) is finite. Since
\[
F=\bigcup_{N\ge1}F_N,
\]
\(F\) is countable.

(g) \(G\) is countable. Let \(G_N\) consist of functions with \(f(n)=1\) for all \(n\ge N\). The first \(N-1\) values are arbitrary positive integers, so
\[
G_N\cong(\mathbb Z_+)^{N-1}
\]
is countable. Hence \(G=\bigcup_NG_N\) is countable.

(h) \(H\) is countable. For \(N,c\in\mathbb Z_+\), let \(H_{N,c}\) consist of functions with \(f(n)=c\) for all \(n\ge N\). Each \(H_{N,c}\cong(\mathbb Z_+)^{N-1}\) is countable, and
\[
H=\bigcup_{N,c\in\mathbb Z_+}H_{N,c}
\]
is a countable union of countable sets.

(i) \(I\) is countable. The map
\[
\{(m,n)\in\mathbb Z_+^2:m<n\}\to I,
\qquad
(m,n)\mapsto\{m,n\}
\]
is bijective, and the domain is a subset of the countable set \(\mathbb Z_+^2\).

(j) \(J\) is countable. Let \(J_n\) denote the family of subsets having at most \(n\) elements. The map
\[
(\mathbb Z_+)^n\to J_n,
\qquad
(a_1,\ldots,a_n)\mapsto\{a_1,\ldots,a_n\}
\]
is surjective after allowing repetitions (with the empty set handled separately), so \(J_n\) is countable. Since
\[
J=\{\varnothing\}\cup\bigcup_{n\ge1}J_n,
\]
\(J\) is countable.
:::
