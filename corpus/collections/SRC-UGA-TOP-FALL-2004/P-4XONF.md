---
schema: qual/card@1
id: P-4XONF
kind: problem
title: 3-fold connected covering spaces of $S^1\lor S^1$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
  - Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 5 of the official UGA Fall 2004 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Classified transitive monodromy pairs in S_3 up to simultaneous conjugacy
    and verified that exactly seven isomorphism classes of connected
    three-sheeted covers occur.
---

::: problem
Describe the 3-fold connected covering spaces of $S^1 \lor S^1$.
:::

::: {.solution}
Let
\[
B=S^1_a\vee S^1_b
\]
with wedge point $v$ and oriented loop-edges $a$ and $b$.

<1>1. A three-sheeted covering of $B$ is determined, up to relabeling its fiber over $v$, by a pair of permutations
\[
(\sigma,\tau)\in S_3\times S_3.
\]
::: {.proof}
Label the fiber over $v$ by
\[
p^{-1}(v)=\{1,2,3\}.
\]
For each $i$, lift the loop $a$ beginning at the point labeled $i$.
Its endpoint is another point of the fiber, say $\sigma(i)$.
Unique path lifting makes
\[
\sigma:\{1,2,3\}\longrightarrow\{1,2,3\}
\]
a permutation.
Likewise, lifting $b$ gives a permutation $\tau$.

Conversely, given $(\sigma,\tau)$, construct a graph with vertices $1,2,3$, one oriented $a$-edge from $i$ to $\sigma(i)$ for every $i$, and one oriented $b$-edge from $i$ to $\tau(i)$ for every $i$.
Map every $a$-edge homeomorphically to the $a$-circle and every $b$-edge homeomorphically to the $b$-circle.
At each vertex there is exactly one incoming and one outgoing lift of each oriented base edge, so this graph maps to $B$ as a three-sheeted covering.
:::

<1>2. The covering determined by $(\sigma,\tau)$ is connected exactly when the subgroup
\[
\langle\sigma,\tau\rangle\le S_3
\]
acts transitively on $\{1,2,3\}$.
::: {.proof}
A path in $B$ based at $v$ is represented by a word in $a^{\pm1}$ and $b^{\pm1}$.
Lifting such a word from a point $i$ in the fiber ends at the point obtained by applying the corresponding word in $\sigma^{\pm1}$ and $\tau^{\pm1}$.
Hence two vertices of the covering graph lie in the same path component exactly when they lie in the same orbit of $\langle\sigma,\tau\rangle$.
Thus the graph is connected exactly when there is one orbit.
:::

<1>3. Two pairs $(\sigma,\tau)$ and $(\sigma',\tau')$ determine isomorphic covering spaces over $B$ exactly when they are simultaneously conjugate:
\[
(\sigma',\tau')
=
(h\sigma h^{-1},h\tau h^{-1})
\]
for some $h\in S_3$.
::: {.proof}
Relabeling the three points of the fiber by $h$ changes each monodromy permutation by conjugation with $h$.
Every isomorphism of covering spaces over $B$ restricts to such a relabeling of the fiber over $v$, and it must intertwine the lifts of both base loops.
Thus simultaneous conjugacy is precisely the equivalence relation corresponding to isomorphism of covers over the fixed base.
:::

<1>4. Put
\[
r=(123),
\qquad
s=(12),
\qquad
t=(23).
\]
The following seven monodromy pairs give connected three-sheeted coverings:
\[
\boxed{
\begin{array}{c|c}
\sigma_a&\sigma_b\\
\hline
e&r\\
s&r\\
s&t\\
r&e\\
r&s\\
r&r\\
r&r^{-1}
\end{array}}
\]
::: {.proof}
Any pair containing the $3$-cycle $r$ generates a transitive subgroup, since $\langle r\rangle$ is already transitive.
The remaining pair $(s,t)$ consists of two distinct transpositions; they generate $S_3$, hence act transitively.
Therefore all seven displayed pairs define connected covers by <1>2.
:::

<1>5. Every connected three-sheeted covering is isomorphic to one of the seven covers in <1>4.
::: {.proof}
Let $(\sigma,\tau)$ be a transitive pair.
We classify it by the cycle type of $\sigma$.

If
\[
\sigma=e,
\]
then transitivity forces $\tau$ to be a $3$-cycle.
All $3$-cycles are conjugate, so this gives the representative
\[
(e,r).
\]

Suppose next that $\sigma$ is a transposition.
After simultaneous conjugation, take
\[
\sigma=s=(12).
\]
If $\tau=e$ or $\tau=s$, the generated subgroup fixes $3$ and is not transitive.
Thus $\tau$ must be either a $3$-cycle or a transposition distinct from $s$.
The centralizer
\[
C_{S_3}(s)=\{e,s\}
\]
interchanges the two $3$-cycles by conjugation, and it also interchanges the two transpositions different from $s$.
Hence these possibilities give exactly
\[
(s,r)
\qquad\text{and}\qquad
(s,t).
\]

Finally suppose that $\sigma$ is a $3$-cycle.
After simultaneous conjugation, take
\[
\sigma=r=(123).
\]
Its centralizer is
\[
C_{S_3}(r)=\langle r\rangle.
\]
The second permutation $\tau$ can have three possible cycle types.
If $\tau=e$, this gives $(r,e)$.
If $\tau$ is a transposition, conjugation by powers of $r$ acts transitively on the three transpositions, so there is one class represented by $(r,s)$.
If $\tau$ is a $3$-cycle, then
\[
\tau=r
\qquad\text{or}\qquad
\tau=r^{-1},
\]
giving $(r,r)$ and $(r,r^{-1})$.
These exhaust all possibilities.
:::

<1>6. The seven covers in <1>4 are pairwise nonisomorphic over $B$.
::: {.proof}
Simultaneous conjugation preserves the cycle type of each coordinate, so pairs having different cycle-type pairs cannot be equivalent.
This already separates all displayed pairs except potentially
\[
(r,r)
\qquad\text{and}\qquad
(r,r^{-1}).
\]
If these two were simultaneously conjugate while their first coordinates were both $r$, the conjugating permutation would lie in
\[
C_{S_3}(r)=\langle r\rangle.
\]
But this centralizer is abelian, so conjugation by any of its elements fixes both $r$ and $r^{-1}$; it cannot send the second coordinate $r$ to $r^{-1}$.
Thus these two covers are also nonisomorphic.
Hence there are exactly seven isomorphism classes.
:::

<1>7. Equivalently, each row of <1>4 can be drawn as a three-vertex labeled covering graph.
::: {.proof}
For a row $(\sigma_a,\sigma_b)$, take vertices $1,2,3$.
For each label $x\in\{a,b\}$ and each vertex $i$, draw one oriented $x$-edge
\[
i\longrightarrow\sigma_x(i).
\]
Thus an identity permutation gives three loops of that label, a transposition gives two oppositely directed edges between the transposed vertices together with a loop at the fixed vertex, and a $3$-cycle gives a directed triangle.
By <1>1 these seven labeled graphs are exactly the desired connected three-sheeted covering spaces.
:::
:::
