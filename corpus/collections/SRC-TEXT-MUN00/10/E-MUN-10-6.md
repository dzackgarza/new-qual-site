---
schema: qual/card@1
id: E-MUN-10-6
kind: problem
title: Properties of the minimal uncountable well-ordered set $S_{\Omega}$
classification:
  areas:
  - topology
  topics:
  - Well-Ordered Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 10, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $S_{\Omega}$ be the minimal uncountable well-ordered set.

(a) Show that $S_{\Omega}$ has no largest element.

(b) Show that for every $\alpha \in S_{\Omega}$, the subset $\{x \mid \alpha < x\}$ is uncountable.

(c) Let $X_0$ be the subset of $S_{\Omega}$ consisting of all elements $x$ such that $x$ has no immediate predecessor.
Show that $X_0$ is uncountable.
:::

::: {.solution}
Recall that \(S_{\Omega}\) is uncountable and every section \(S_\alpha\) with \(\alpha\in S_\Omega\) is countable.

(a) If \(S_\Omega\) had a largest element \(\alpha\), then
\[
S_\Omega=S_\alpha\cup\{\alpha\}
\]
would be countable, contradiction. Hence \(S_\Omega\) has no largest element.

(b) Fix \(\alpha\in S_\Omega\). The section \(S_\alpha\) is countable. If the tail
\[
T_\alpha=\{x\in S_\Omega:\alpha<x\}
\]
were also countable, then
\[
S_\Omega=S_\alpha\cup\{\alpha\}\cup T_\alpha
\]
would be countable. Hence \(T_\alpha\) is uncountable.

(c) Let \(X_0\) be the set of points having no immediate predecessor. Suppose \(X_0\) were countable. By Theorem 10.3 it would have an upper bound \(a\in S_\Omega\).

Starting at \(a\), form the successor sequence
\[
a=a_0<a_1<a_2<\cdots,
\]
where \(a_{n+1}\) is the immediate successor of \(a_n\); this is possible by part (a) and Exercise 2. The countable set \(\{a_n:n\ge0\}\) has an upper bound in \(S_\Omega\), hence, by Exercise 1, a least upper bound \(\beta\in S_\Omega\).

The point \(\beta\) is not one of the \(a_n\), since \(a_{n+1}>a_n\) for every \(n\). We claim \(\beta\) has no immediate predecessor. If \(\gamma\) were an immediate predecessor of \(\beta\), then \(\gamma\) could not be an upper bound of the sequence, so \(a_n>\gamma\) for some \(n\). Then
\[
\gamma<a_n<a_{n+1}<\beta,
\]
contradicting immediacy. Thus \(\beta\in X_0\). But \(\beta>a=a_0\), contradicting that \(a\) is an upper bound for \(X_0\). Therefore \(X_0\) is uncountable.
:::
