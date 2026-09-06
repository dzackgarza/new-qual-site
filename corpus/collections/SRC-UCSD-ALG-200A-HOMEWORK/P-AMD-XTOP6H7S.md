---
schema: qual/card@1
id: P-AMD-XTOP6H7S
kind: problem
title: 'A finite group covered by three subgroups: one is all of $G$ or all have index $2$'
classification:
  areas:
  - algebra
  topics:
  - Subgroups
  - Cosets and Lagrange
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 2, Exercise 2(ii).
    Restored the source's omitted final request to find the smallest group in
    which the three-proper-subgroup alternative occurs.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    When all three subgroups are proper, first showed their pairwise
    intersections equal the common intersection K. Inclusion-exclusion and
    |H_i H_j| = |H_i||H_j|/|K| then force [H_i:K] = 2 for every i, hence
    [G:H_i] = 2. The Klein four group realizes the alternative and no smaller
    group can do so.
---

::: {.problem}
Let $H_1,H_2,H_3$ be subgroups of a finite group $G$ and suppose
\[
G=H_1\cup H_2\cup H_3.
\]

Show that either $G=H_i$ for some $i$, or
\[
[G:H_i]=2
\qquad\text{for }i=1,2,3.
\]
Find the smallest group for which the second possibility occurs.
:::

::: {.solution}
If one of the $H_i$ equals $G$, the first alternative holds.
Assume henceforth that all three subgroups are proper, and set
\[
K=H_1\cap H_2\cap H_3.
\]

<1>1. The pairwise intersections are all equal to $K$.
::: {.proof}
It suffices by symmetry to prove $H_1\cap H_2=K$.

Because $H_1$ and $H_2$ are both proper, they cannot cover $G$: a group that is the union of two subgroups must equal one of them.
Hence choose
\[
z\in G\setminus(H_1\cup H_2).
\]
Since $G=H_1\cup H_2\cup H_3$, we have $z\in H_3$.

Let $x\in H_1\cap H_2$.
If $x\notin H_3$, then $xz\notin H_1$; otherwise $z=x^{-1}(xz)\in H_1$.
Similarly $xz\notin H_2$.
Therefore the three-subgroup cover forces $xz\in H_3$.
Since also $z\in H_3$,
\[
x=(xz)z^{-1}\in H_3,
\]
a contradiction.
Thus every $x\in H_1\cap H_2$ lies in $H_3$, so
\[
H_1\cap H_2=K.
\]
The same argument applies to the other two pairs.
:::

<1>2. Put $a_i=[H_i:K]$.
Then each $a_i\ge 2$ and
\[
[G:K]=a_1+a_2+a_3-2.
\]
::: {.proof}
If $a_i=1$, then $H_i=K$ is contained in each of the other two subgroups.
The three-subgroup cover would then reduce to a cover of $G$ by two proper subgroups, which is impossible.
Hence $a_i\ge2$.

By <1>1 and inclusion-exclusion,
\[
\begin{aligned}
|G|
 &=|H_1|+|H_2|+|H_3|
   -|H_1\cap H_2|-|H_1\cap H_3|-|H_2\cap H_3|
   +|K|\\
 &=|K|(a_1+a_2+a_3-2).
\end{aligned}
\]
Dividing by $|K|$ gives the asserted formula.
:::

<1>3. For distinct $i,j$,
\[
a_i a_j\le [G:K].
\]
::: {.proof}
For finite subgroups $A,B\le G$, the multiplication map
\[
A\times B\longrightarrow AB,
\qquad
(a,b)\longmapsto ab,
\]
has every fiber of cardinality $|A\cap B|$: if $ab=a'b'$, then $a'^{-1}a=b'b^{-1}\in A\cap B$, and every element of $A\cap B$ gives one such representation.
Consequently
\[
|AB|=\frac{|A||B|}{|A\cap B|}.
\]
Applying this with $A=H_i$ and $B=H_j$ and using <1>1 gives
\[
|H_iH_j|=|K|a_i a_j.
\]
Since $H_iH_j\subseteq G$,
\[
|K|a_i a_j\le |G|,
\]
and division by $|K|$ proves the claim.
:::

<1>4. We have $a_1=a_2=a_3=2$.
::: {.proof}
Relabel the subgroups so that
\[
2\le a_1\le a_2\le a_3.
\]
By <1>2 and <1>3,
\[
a_2a_3\le a_1+a_2+a_3-2.
\]
Rearranging,
\[
(a_2-1)(a_3-1)\le a_1-1\le a_2-1.
\]
Since $a_2-1>0$, division gives $a_3-1\le1$, so $a_3\le2$.
Together with $2\le a_1\le a_2\le a_3$, this yields
\[
a_1=a_2=a_3=2.
\]
:::

<1>5. Each $H_i$ has index $2$ in $G$.
::: {.proof}
By <1>2 and <1>4,
\[
[G:K]=2+2+2-2=4.
\]
Therefore, for each $i$,
\[
[G:H_i]=\frac{[G:K]}{[H_i:K]}=\frac42=2.
\]
This proves the second alternative.
:::

<1>6. The smallest group realizing the second alternative is the Klein four group $C_2\times C_2$.
::: {.proof}
In
\[
C_2\times C_2=\{(0,0),(1,0),(0,1),(1,1)\},
\]
the three subgroups generated respectively by $(1,0)$, $(0,1)$, and $(1,1)$ all have order $2$, hence index $2$, and their union is the whole group.

No smaller group can realize the second alternative.
Such a cover cannot use the same proper subgroup twice, since then two proper subgroups would cover $G$.
Thus it requires three distinct proper subgroups.
Groups of orders $1$, $2$, and $3$ do not have three distinct proper subgroups.
Hence order $4$ is minimal, and $C_2\times C_2$ provides an example of that order.
:::
:::
