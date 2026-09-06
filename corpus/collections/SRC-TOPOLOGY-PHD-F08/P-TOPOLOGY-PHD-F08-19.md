---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-19
kind: problem
title: Euler characteristic of the n-sphere from a standard triangulation
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Cell Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against Part Two, question 7 of the Topology Ph.D. Qualifying Exam
    dated January 17, 2009 in assets/attachments/F08phdtop.pdf. The source says
    to triangulate S^n using an n-simplex, but the boundary of an n-simplex is
    S^{n-1}; the standard simplex triangulation of S^n is the boundary of an
    (n+1)-simplex.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Counted k-simplices in the boundary of Delta^{n+1} as C(n+2,k+1) and used
    the alternating binomial sum to obtain chi(S^n)=1+(-1)^n.
---

::: {.problem}
Compute the Euler characteristic of the $n$-sphere $S^n$ using the standard triangulation of an $n$-simplex.
:::

::: {.solution}
The simplex dimension in the source is off by one: the boundary of an $n$-simplex is $S^{n-1}$.
To triangulate $S^n$, use the boundary of an $(n+1)$-simplex.

<1>1. The boundary complex
\[
\partial\Delta^{n+1}
\]
is a triangulation of $S^n$.
::: {.proof}
The simplex $\Delta^{n+1}$ is homeomorphic to the closed ball $D^{n+1}$.
Its topological boundary is therefore homeomorphic to
\[
\partial D^{n+1}=S^n.
\]
The proper faces of $\Delta^{n+1}$ form the simplicial complex $\partial\Delta^{n+1}$, giving the standard triangulation of that boundary.
:::

<1>2. For each $0\le k\le n$, the triangulation $\partial\Delta^{n+1}$ has
\[
f_k=\binom{n+2}{k+1}
\]
$k$-simplices.
::: {.proof}
The simplex $\Delta^{n+1}$ has $n+2$ vertices.
A $k$-dimensional face is determined uniquely by choosing its $k+1$ vertices.
Hence there are
\[
\binom{n+2}{k+1}
\]
such faces.
Since $k\le n$, every $k$-face is a proper face and therefore belongs to the boundary complex.
:::

<1>3. Thus
\[
\chi(S^n)
=\sum_{k=0}^{n}(-1)^k\binom{n+2}{k+1}.
\]
::: {.proof}
For a finite simplicial complex, the Euler characteristic is the alternating sum of the numbers of simplices in each dimension.
Apply this to the simplex counts from <1>2.
:::

<1>4. The alternating sum in <1>3 equals
\[
1+(-1)^n.
\]
::: {.proof}
Set $j=k+1$.
Then
\[
\chi(S^n)
=-\sum_{j=1}^{n+1}(-1)^j\binom{n+2}{j}.
\]
The binomial theorem gives
\[
0=(1-1)^{n+2}
=\sum_{j=0}^{n+2}(-1)^j\binom{n+2}{j}.
\]
Therefore
\[
\sum_{j=1}^{n+1}(-1)^j\binom{n+2}{j}
=-1-(-1)^{n+2}
=-1-(-1)^n.
\]
Negating this identity yields
\[
\chi(S^n)=1+(-1)^n.
\]
:::

<1>5. Hence
\[
\boxed{
\chi(S^n)=
\begin{cases}
2,&n\text{ even},\\
0,&n\text{ odd}.
\end{cases}}
\]
::: {.proof}
This is the parity form of the formula in <1>4.
:::
:::
