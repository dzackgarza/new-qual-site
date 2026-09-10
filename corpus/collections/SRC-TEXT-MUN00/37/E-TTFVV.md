---
schema: qual/card@1
id: E-TTFVV
kind: problem
title: The countable intersection property characterizes Lindelof spaces
classification:
  areas:
  - topology
  topics:
  - Countability
  - Compactness
relations: []
review: draft
---

::: {.exercise}

A collection $\mathcal{A}$ of subsets of $X$ has the countable intersection property if every countable intersection of elements of $\mathcal{A}$ is nonempty.
Show that $X$ is a Lindelöf space if and only if for every collection $\mathcal{A}$ of subsets of $X$ having the countable intersection property,

$$
\bigcap_{A \in \mathcal{A}} \overline{A}
$$

is nonempty.
:::

::: {.solution}
Assume first that \(X\) is Lindelöf, and let \(\mathcal A\) have the countable intersection property. Suppose
\[
\bigcap_{A\in\mathcal A}\overline A=\varnothing.
\]
Then the open sets
\[
X\setminus\overline A,\qquad A\in\mathcal A,
\]
cover \(X\). Lindelöfness gives a countable subcover
\[
X=\bigcup_{n=1}^\infty (X\setminus\overline{A_n}).
\]
Taking complements,
\[
\bigcap_{n=1}^\infty\overline{A_n}=\varnothing,
\]
so certainly \(igcap_{n=1}^\infty A_n=\varnothing\), contradicting the countable intersection property. Hence the intersection of all closures is nonempty.

Conversely, assume the stated closure-intersection property, and let
\[
\mathcal U=\{U_i:i\in I\}
\]
be an open cover of \(X\). Suppose no countable subfamily covers \(X\). Put
\[
A_i=X\setminus U_i.
\]
For every countable set of indices \(i_1,i_2,\dots\), the union \(U_{i_1}\cup U_{i_2}\cup\cdots\) is not all of \(X\), so
\[
A_{i_1}\cap A_{i_2}\cap\cdots\ne\varnothing.
\]
Thus \(\{A_i:i\in I\}\) has the countable intersection property. Each \(A_i\) is closed, so the assumed property gives
\[
\varnothing\ne\bigcap_{i\in I}\overline{A_i}
=\bigcap_{i\in I}A_i
=X\setminus\bigcup_{i\in I}U_i,
\]
contradicting that \(\mathcal U\) covers \(X\). Therefore every open cover has a countable subcover, and \(X\) is Lindelöf.
:::
