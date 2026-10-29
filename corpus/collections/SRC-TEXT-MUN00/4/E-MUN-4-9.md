---
schema: qual/card@1
id: E-MUN-4-9
kind: problem
title: Archimedean property and density of $\QQ$ in $\RR$
classification:
  areas:
  - topology
  topics:
  - Integers and Real Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 4, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

(a) Show that every nonempty subset of $\ZZ$ that is bounded above has a largest element.

(b) If $x \notin \ZZ$, show there is exactly one $n \in \ZZ$ such that $n < x < n + 1$ .

(c) If $x - y > 1$, show there is at least one $n \in \ZZ$ such that $y < n < x$ .

(d) If $y < x$, show there is a rational number $z$ such that $y < z < x$ .
:::

::: {.solution}
(a) Let \(A\subset\ZZ\) be nonempty and bounded above. By the Archimedean property choose \(N\in\ZZ_+\) larger than an upper bound for \(A\). Then
\[
B=\{N-a:a\in A\}
\]
is a nonempty subset of \(\ZZ_+\). By the well-ordering property, \(B\) has a smallest element \(b_0=N-a_0\). For every \(a\in A\),
\[
N-a_0\le N-a,
\]
so \(a\le a_0\). Thus \(a_0\) is the largest element of \(A\).

(b) Let \(x\notin\ZZ\). The set
\[
A=\{m\in\ZZ:m<x\}
\]
is nonempty and bounded above, hence has a largest element \(n\) by part (a). Then \(n<x\). If \(x\ge n+1\), equality would make \(x\) an integer, while strict inequality would put \(n+1\) in \(A\), contradicting maximality of \(n\). Hence
\[
n<x<n+1.
\]
Uniqueness follows because two distinct integers cannot both be the integer immediately below \(x\): if \(m<n\), then \(m+1\le n\), contradicting \(n<x<m+1\).

(c) Suppose \(x-y>1\). If \(y\in\ZZ\), take \(n=y+1\); then \(y<n<x\). If \(y\notin\ZZ\), part (b) gives \(m<y<m+1\). Set \(n=m+1\). Then
\[
y<n<y+1<x.
\]

(d) Let \(y<x\). Since \(x-y>0\), choose \(n\in\ZZ_+\) with
\[
n(x-y)>1.
\]
Then \(nx-ny>1\), so by part (c) there is \(m\in\ZZ\) with
\[
ny<m<nx.
\]
Dividing by the positive integer \(n\) gives
\[
y<\frac mn<x.
\]
Thus \(z=m/n\in\QQ\) lies strictly between \(y\) and \(x\).
:::
