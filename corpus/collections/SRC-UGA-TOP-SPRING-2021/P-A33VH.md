---
schema: qual/card@1
id: P-A33VH
kind: problem
title: Setwise distance of compact sets is attained, and vanishes only on a nonempty
  intersection
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked all three parts and the hint against problem 3 of the official UGA Spring 2021 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified compact attainment on A x B, the closed-set limit argument when the infimum is zero, and the suggested nonattainment example in the subspace {0} union (1,2].
---

:::{.problem}
For nonempty subsets $A, B$ of a metric space $(X, d)$, define the **setwise distance** as 
\[
d(A, B) \da \inf \ts{ d(a, b) \st a\in A,\, b\in B } 
.\]

a. 
Suppose that $A$ and $B$ are compact.
Show that there is an $a\in A$ and $b\in B$ such that $d(A, B) = d(a, b)$.

b.
Suppose that $A$ is closed and $B$ is compact.
Show that if $d(A, B) = 0$ then $A \intersect B \neq \emptyset$.

c. 
Give an example in which $A$ is closed, $B$ is compact, and $d(a, b) > d(A, B)$ for all $a\in A$ and $b\in B$.

> Hint: take $X = \ts{ 0 } \union (1, 2] \subset \RR$.
> Throughout this problem, you may use without proof that the map $d:X\cross X\to \RR$ is continuous.

:::

::: {.solution}
<1>1. If $A$ and $B$ are compact, then the setwise distance $d(A,B)$ is attained.
::: {.proof}
The product $A\times B$ is compact.
By the allowed continuity of the metric map,
\[
d|_{A\times B}:A\times B\longrightarrow\RR,
\qquad
(a,b)\longmapsto d(a,b),
\]
is continuous.
Therefore it attains a minimum at some pair
\[
(a_0,b_0)\in A\times B.
\]
Thus
\[
d(a_0,b_0)
=\min\{d(a,b):a\in A,\ b\in B\}
=\inf\{d(a,b):a\in A,\ b\in B\}
=d(A,B).
\]
This proves part (a).
:::

<1>2. Suppose $A$ is closed, $B$ is compact, and $d(A,B)=0$.
::: {.proof}
For each positive integer $n$, the definition of infimum gives points
\[
a_n\in A,
\qquad
b_n\in B
\]
such that
\[
d(a_n,b_n)<\frac1n.
\]
Since $B$ is compact and metric, the sequence $(b_n)$ has a convergent subsequence
\[
b_{n_k}\longrightarrow b
\qquad\text{for some }b\in B.
\]
By the triangle inequality,
\[
d(a_{n_k},b)
\le d(a_{n_k},b_{n_k})+d(b_{n_k},b)
\longrightarrow0.
\]
Hence
\[
a_{n_k}\longrightarrow b.
\]
Every $a_{n_k}$ lies in the closed set $A$, so $b\in A$.
Since also $b\in B$,
\[
b\in A\cap B.
\]
Therefore $A\cap B\ne\emptyset$, proving part (b).
:::

<1>3. The conclusion of part (a) can fail when only $B$ is compact.
::: {.proof}
Use the suggested metric subspace
\[
X=\{0\}\cup(1,2]\subset\RR
\]
with the Euclidean metric, and set
\[
A=(1,2],
\qquad
B=\{0\}.
\]
The set $B$ is finite, hence compact.
Also
\[
X\setminus A=\{0\}=X\cap(-1,1),
\]
so $\{0\}$ is open in $X$ and therefore $A$ is closed in $X$.

For $a\in A$ and the unique $b=0\in B$,
\[
d(a,b)=a>1.
\]
On the other hand, values of $a\in(1,2]$ can be arbitrarily close to $1$, so
\[
d(A,B)=\inf_{a\in(1,2]}a=1.
\]
Consequently
\[
d(a,b)>d(A,B)
\]
for every $a\in A$ and $b\in B$.
This proves part (c).
:::
:::
