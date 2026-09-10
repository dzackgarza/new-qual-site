---
schema: qual/card@1
id: E-LRAPM
kind: problem
title: Compact closed intervals imply the least upper bound property
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Prove that if $X$ is an ordered set in which every closed interval is compact, then $X$ has the least upper bound property.
:::

::: {.solution}
Let \(A\subset X\) be nonempty and bounded above. Choose \(a_0\in A\) and an upper bound \(b\) of \(A\). For each \(a\in A\), consider the closed subset
\[
F_a=[a,b]\subset[a_0,b].
\]
The family \(\{F_a:a\in A\}\) has the finite intersection property: for finitely many \(a_1,\dots,a_n\in A\), one of them is largest, say \(a_j\), and then
\[
F_{a_1}\cap\cdots\cap F_{a_n}=[a_j,b]\ne\varnothing.
\]
Since the closed interval \([a_0,b]\) is compact by hypothesis,
\[
F=\bigcap_{a\in A}F_a\ne\varnothing.
\]
The set \(F\) is exactly the set of upper bounds of \(A\) that lie in \([a_0,b]\).

It remains to show that the nonempty compact ordered subspace \(F\) has a least element. Suppose it had none. For each \(x\in F\), choose \(y_x\in F\) with \(y_x<x\). Then the sets
\[
(y_x,\infty)\cap F
\]
form an open cover of \(F\): given \(z\in F\), choose \(x\in F\) with \(x<z\), and then \(z\in(y_x,\infty)\cap F\) since \(y_x<x<z\). By compactness, finitely many suffice. Let \(y\) be the least of the finitely many left endpoints \(y_{x_1},\dots,y_{x_n}\). Then \(y\in F\), but \(y\) belongs to none of the sets \((y_{x_i},\infty)\cap F\), contradiction. Thus \(F\) has a least element.

That least element is the least upper bound of \(A\). Therefore \(X\) has the least upper bound property.
:::
