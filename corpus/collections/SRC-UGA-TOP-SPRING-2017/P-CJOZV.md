---
schema: qual/card@1
id: P-CJOZV
kind: problem
title: Three-fold covers of $\RP^2\vee\RP^2$
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
  note: Checked the statement against problem 6 of the official UGA Spring 2017 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Replaced the incorrect direct-product fundamental group and incomplete cover list by the full monodromy classification; there are five three-sheeted covers without a connectedness convention and exactly one connected three-sheeted cover.
---

::: problem
Find all three-fold covers of the wedge of two copies of $\RP^2$. Justify your answer.
:::

::: {.solution}
Let
\[
X=A\vee B,
\qquad
A\cong B\cong\RP^2,
\]
and let $a,b$ denote the nontrivial elements of $\pi_1(A)$ and $\pi_1(B)$ respectively.

<1>1. The fundamental group of $X$ is
\[
\pi_1(X)\cong C_2*C_2
=\left\langle a,b\mid a^2=b^2=1\right\rangle.
\]
::: {.proof}
Since $X$ is the wedge of the path-connected spaces $A$ and $B$, van Kampen's theorem gives
\[
\pi_1(X)\cong\pi_1(A)*\pi_1(B).
\]
Because
\[
\pi_1(A)\cong\pi_1(B)\cong C_2,
\]
the displayed presentation follows.
:::

<1>2. Equivalence classes of three-sheeted covers of $X$ are in bijection with simultaneous-conjugacy classes of pairs
\[
(\sigma,\tau)\in S_3\times S_3
\]
satisfying
\[
\sigma^2=\tau^2=1.
\]
::: {.proof}
Choose labels $1,2,3$ on the fiber over the wedge point. Monodromy gives a homomorphism
\[
\rho:\pi_1(X)\longrightarrow S_3.
\]
By <1>1, such a homomorphism is determined by
\[
\sigma=\rho(a),
\qquad
\tau=\rho(b),
\]
and the relations force $\sigma^2=\tau^2=1$.

Conversely, any such pair defines a permutation representation of $\pi_1(X)$ and hence a three-sheeted cover. Relabeling the fiber by $g\in S_3$ replaces the pair by
\[
(g\sigma g^{-1},g\tau g^{-1}),
\]
and two covers over $X$ are equivalent exactly when their monodromy representations differ by such a relabeling.
:::

<1>3. Up to simultaneous conjugacy, there are exactly five possible monodromy pairs:
\[
\begin{aligned}
& (1,1),\\
& (1,(12)),\\
& ((12),1),\\
& ((12),(12)),\\
& ((12),(23)).
\end{aligned}
\]
::: {.proof}
The only involutions in $S_3$ are the identity and the three transpositions.

If neither entry is a transposition, the pair is $(1,1)$.
If exactly one entry is a transposition, conjugacy makes it $(12)$, giving the two ordered possibilities
\[
(1,(12)),
\qquad
((12),1).
\]
If both entries are transpositions, either they are equal, giving the class
\[
((12),(12)),
\]
or they are distinct. Every ordered pair of distinct transpositions is simultaneously conjugate to
\[
((12),(23)).
\]
These cases are mutually inequivalent because simultaneous conjugacy preserves which entries are trivial and whether the two nontrivial entries are equal.
:::

<1>4. These five monodromy classes give five three-sheeted covers if disconnected covers are allowed, and exactly one of them is connected.
::: {.proof}
A covering is connected exactly when the monodromy action on the fiber is transitive.

For the first four pairs in <1>3, the generated subgroup fixes at least one element of $\{1,2,3\}$, so the action is not transitive. For the last pair,
\[
\langle(12),(23)\rangle=S_3,
\]
which acts transitively. Hence only
\[
((12),(23))
\]
gives a connected three-sheeted cover.
:::

<1>5. The five covers can be described explicitly from the restrictions over the two projective-plane factors.
::: {.proof}
Write $v_1,v_2,v_3$ for the three points over the wedge point. A transposition for the $A$-generator joins the corresponding two fiber points inside a copy of the universal cover
\[
S^2\longrightarrow\RP^2,
\]
while a fixed fiber point contributes a copy of $A\cong\RP^2$. The same description applies to $B$.

Thus the five cases are as follows.

For $(1,1)$, all three sheets are fixed by both generators, so the cover is
\[
X\sqcup X\sqcup X.
\]

For $(1,(12))$, the orbit $\{1,2\}$ gives a connected double cover consisting of one $S^2$ over $B$ with one copy of $A$ attached at each of the two points $v_1,v_2$, while the fixed point $v_3$ gives a separate copy of $X$.

For $((12),1)$, the analogous description holds with $A$ and $B$ interchanged.

For $((12),(12))$, the orbit $\{1,2\}$ gives one copy of $S^2$ over $A$ and one copy of $S^2$ over $B$, glued to each other at the two fiber points $v_1,v_2$; the fixed point $v_3$ again gives a separate copy of $X$.

Finally, for the connected class $((12),(23))$, the inverse image of $A$ consists of an $S^2$ through $v_1,v_2$ and a copy of $\RP^2$ at $v_3$, while the inverse image of $B$ consists of an $S^2$ through $v_2,v_3$ and a copy of $\RP^2$ at $v_1$. Gluing these four pieces at the indicated fiber points gives the unique connected three-sheeted cover.
:::

<1>6. Therefore the complete answer is: five equivalence classes of three-sheeted covers in general, represented by the five pairs in <1>3; if “cover” is intended to mean connected cover, there is exactly one, represented by
\[
\boxed{((12),(23)).}
\]
::: {.proof}
This is exactly the classification established in <1>2--<1>5.
:::
:::
