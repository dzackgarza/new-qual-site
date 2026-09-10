---
schema: qual/card@1
id: E-HAT-4.2-39
kind: problem
title: "Indeterminacy of Toda brackets"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 39; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that the indeterminacy of a Toda bracket $\langle f, g, h \rangle$ with $f \in \pi_i^s$, $g \in \pi_j^s$, $h \in \pi_k^s$ is the subgroup $f \cdot \pi_{j+k+1}^s + h \cdot \pi_{i+j+1}^s$ of $\pi_{i+j+k+1}^s$.

::: {.solution}
A representative of the stable Toda bracket
\[
\langle f,g,h\rangle
\]
is obtained by choosing nullhomotopies of
\[
gf\simeq0,
\qquad
hg\simeq0
\]
and gluing the resulting extensions across the two cones in the standard Toda construction.

Change the chosen nullhomotopy of \(hg\). The difference between two such nullhomotopies is an arbitrary stable class
\[
\alpha\in\pi_{j+k+1}^s.
\]
After composing with \(f\), the resulting Toda representative changes by
\[
f\alpha\in f\cdot\pi_{j+k+1}^s.
\]
Similarly, changing the nullhomotopy of \(gf\) by
\[
\beta\in\pi_{i+j+1}^s
\]
changes the bracket representative by
\[
\beta h.
\]
In the stable homotopy ring this generates the same subgroup, up to the usual graded sign, as
\[
h\cdot\pi_{i+j+1}^s.
\]
The two choices are independent, and these are the only choices entering the construction. Therefore the set of possible bracket values is a coset modulo
\[
\boxed{f\cdot\pi_{j+k+1}^s+h\cdot\pi_{i+j+1}^s}
\subseteq\pi_{i+j+k+1}^s.
\]
This is exactly the indeterminacy of \(\langle f,g,h\rangle\).
:::
