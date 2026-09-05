---
schema: qual/card@1
id: P-R7EFJ
kind: problem
title: Whether three tangent circles cover $S^1\vee S^1$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 4 of the official UGA Spring 2019 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Replaced the image-only answer with an explicit two-sheeted graph covering and verified the local covering condition at both tangency vertices.
---

::: problem
Is there a covering map from
\[
X_3
=
\{x^2+y^2=1\}
\cup
\{(x-2)^2+y^2=1\}
\cup
\{(x+2)^2+y^2=1\}
\subset\RR^2
\]
to $S^1\vee S^1$?
If there is, give an example; if not, give a proof.
:::

::: {.solution}
Yes. In fact, $X_3$ is a connected two-sheeted covering of $S^1\vee S^1$.

Let
\[
v_0=(-1,0),
\qquad
v_1=(1,0)
\]
be the two tangency points.
Regard the target rose
\[
R=S^1\vee S^1
\]
as a graph with one vertex $*$ and two oriented loop-edges $a$ and $b$.

<1>1. Regard $X_3$ as a graph with vertices $v_0,v_1$ and four edges:

- the left circle, a loop $L$ based at $v_0$;
- the right circle, a loop $R'$ based at $v_1$;
- the upper semicircle $U$ of the middle circle, joining $v_0$ to $v_1$;
- the lower semicircle $D$ of the middle circle, joining $v_1$ to $v_0$.

::: {.proof}
The left and middle circles meet only at $v_0$, the middle and right circles meet only at $v_1$, and the two outer circles are disjoint.
Removing $v_0$ and $v_1$ therefore leaves exactly the four open edge pieces listed above.
:::

<1>2. Define
\[
p:X_3\longrightarrow R
\]
by sending both $v_0$ and $v_1$ to $*$, mapping each of the loops $L$ and $R'$ homeomorphically onto the $a$-petal, and mapping each of $U$ and $D$ homeomorphically and orientation-preservingly onto the $b$-petal.
::: {.proof}
Choose the orientation of $U$ from $v_0$ to $v_1$ and the orientation of $D$ from $v_1$ to $v_0$.
Then the endpoint identifications agree with the common vertex $*$ of the target loops, so the four edge maps fit together to a continuous graph map $p$.
Restricted to the middle circle, this map is the standard two-sheeted covering of the $b$-circle: going once around the middle circle traverses the $b$-petal twice.
:::

<1>3. Every point in the interior of either target petal has exactly two evenly covered preimages.
::: {.proof}
An interior point of the $a$-petal has one preimage on $L$ and one on $R'$, and both edge restrictions are homeomorphisms.
An interior point of the $b$-petal has one preimage on $U$ and one on $D$, again with both restrictions homeomorphisms.
Small interval neighborhoods are therefore evenly covered.
:::

<1>4. A sufficiently small neighborhood of the wedge point $*$ is evenly covered by neighborhoods of $v_0$ and $v_1$.
::: {.proof}
Choose a small graph neighborhood $W$ of $*$ consisting of short initial and terminal arcs of each oriented petal $a$ and $b$.
At each $v_i$, exactly four half-edges meet.
Under $p$, these four half-edges map bijectively to the four arms of $W$:

- the two half-edges of the outer loop at $v_i$ map to the two arms of the $a$-petal;
- one incident middle-circle half-edge maps to the initial arm of the $b$-petal and the other to its terminal arm.

Hence there are disjoint neighborhoods $W_0$ of $v_0$ and $W_1$ of $v_1$ such that
\[
p^{-1}(W)=W_0\amalg W_1
\]
and
\[
p|_{W_i}:W_i\longrightarrow W
\]
is a homeomorphism for $i=0,1$.
:::

<1>5. Therefore $p:X_3\to S^1\vee S^1$ is a two-sheeted covering map.
::: {.proof}
By <1>3 every nonvertex point has an evenly covered neighborhood, and by <1>4 the wedge point does as well.
Thus $p$ is a covering map.
Every point of the target has exactly two preimages, so it is two-sheeted.
:::
:::
