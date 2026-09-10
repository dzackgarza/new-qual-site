---
schema: qual/card@1
id: E-MUN-2-5
kind: problem
title: Left inverses, right inverses, and bijectivity
classification:
  areas:
  - topology
  topics:
  - Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 2, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

In general, let us denote the identity function for a set $C$ by $i_C$ . That is, define $i_C: C \to C$ to be the function given by the rule $i_C(x) = x$ for all $x \in C$ . Given $f: A \to B$, we say that a function $g: B \to A$ is a left inverse for $f$ if $g \circ f = i_A$ ; and we say that $h: B \to A$ is a right inverse for $f$ if $f \circ h = i_B$ .

(a) Show that if $f$ has a left inverse, $f$ is injective; and if $f$ has a right inverse, $f$ is surjective.

(b) Give an example of a function that has a left inverse but no right inverse.

(c) Give an example of a function that has a right inverse but no left inverse.

(d) Can a function have more than one left inverse?
More than one right inverse?

(e) Show that if $f$ has both a left inverse $g$ and a right inverse $h$, then $f$ is bijective and $g = h = f^{-1}$ .
:::

::: {.solution}
(a) Suppose \(g\circ f=i_A\). If \(f(a_1)=f(a_2)\), then
\[
a_1=g(f(a_1))=g(f(a_2))=a_2,
\]
so \(f\) is injective. If \(f\circ h=i_B\), then every \(b\in B\) has the form \(b=f(h(b))\), so \(f\) is surjective.

(b) Let
\[
f:\{0\}\hookrightarrow\{0,1\}
\]
be inclusion. The map \(g:\{0,1\}\to\{0\}\) is a left inverse, but no right inverse exists because \(f\) is not surjective.

(c) Let
\[
f:\{0,1\}\to\{0\}
\]
be the constant map. Choosing \(h(0)=0\) gives a right inverse, but no left inverse exists because \(f\) is not injective.

(d) Yes in both cases. For the inclusion
\[
f:\{0,1\}\hookrightarrow\{0,1,2\},
\]
a left inverse must fix \(0,1\) but may send \(2\) to either \(0\) or \(1\), giving two left inverses. For the constant surjection
\[
f:\{0,1\}\to\{0\},
\]
either choice \(h(0)=0\) or \(h(0)=1\) is a right inverse.

(e) Suppose \(g\circ f=i_A\) and \(f\circ h=i_B\). Part (a) shows that \(f\) is both injective and surjective, hence bijective. Moreover,
\[
g=g\circ i_B=g\circ(f\circ h)=(g\circ f)\circ h=i_A\circ h=h.
\]
Thus the common map \(g=h\) is the unique inverse \(f^{-1}\).
:::
