---
schema: qual/card@1
id: P-HOIQ3
kind: problem
title: The one-point compactification and the missing Hausdorff hypothesis in uniqueness
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Point-Set Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Checked all three parts against problem 1 of the official UGA Fall 2004
    topology exam. The printed uniqueness claim in part (b) assumes only that
    Y is compact; under the standard convention that compact need not mean
    Hausdorff, this omits a necessary hypothesis.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Verified the topology, compactness, density, and Hausdorffness of the
    construction; exhibited a counterexample to the printed part (b); proved
    the intended compact-Hausdorff uniqueness theorem; and identified the two
    requested compactifications.
---

::: {.problem}
Let $X$ be a noncompact locally compact Hausdorff space, with topology $\mct$.
Let $\widehat X=X\cup\theset{\infty}$ ($X$ with one point adjoined), and consider the family $\mcb$ of subsets of $\widehat X$ defined by
\[
\mcb
=
\mct
\cup
\theset{S\cup\theset{\infty}\mid S\subset X,\ X\backslash S\text{ is compact}}.
\]

(a) Prove that $\mcb$ is a topology on $\widehat X$, that the resulting space is compact, and that $X$ is dense in $\widehat X$.

(b) Prove that if $Y\supset X$ is a compact space such that $X$ is dense in $Y$ and $Y\backslash X$ is a singleton, then $Y$ is homeomorphic to $\widehat X$.

> The space $\widehat X$ is called the **one-point compactification** of $X$.

(c) Find familiar spaces that are homeomorphic to the one-point compactifications of

(i) $X=(0,1)$ and

(ii) $X=\RR^2$.
:::

::: {.solution}
<1>1. The sets in $\mcb$ that contain $\infty$ are exactly the complements in $\widehat X$ of compact subsets of $X$.
::: {.proof}
Since $X$ is Hausdorff, every compact subset of $X$ is closed.
Thus, if $K\subseteq X$ is compact, then
\[
S=X\setminus K
\]
is open in $X$ and
\[
S\cup\{\infty\}=\widehat X\setminus K.
\]
Conversely, a set in the second family defining $\mcb$ has this form with
\[
K=X\setminus S
\]
compact.
Hence
\[
\mcb
=
\mct
\cup
\{\widehat X\setminus K:K\subseteq X\text{ compact}\}.
\]
In particular, the intersection with $X$ of every member of $\mcb$ is open in $X$.
:::

<1>2. The family $\mcb$ contains $\emptyset$ and $\widehat X$.
::: {.proof}
We have
\[
\emptyset\in\mct\subseteq\mcb.
\]
Also the empty set is compact, so <1>1 gives
\[
\widehat X=\widehat X\setminus\emptyset\in\mcb.
\]
:::

<1>3. The family $\mcb$ is closed under arbitrary unions.
::: {.proof}
Let
\[
U=\bigcup_{i\in I}U_i,
\qquad
U_i\in\mcb.
\]
If $\infty\notin U$, then every $U_i$ lies in $X$ and is open there, so
\[
U\in\mct\subseteq\mcb.
\]

Suppose instead that $\infty\in U$.
Choose $j\in I$ with $\infty\in U_j$.
By <1>1,
\[
K_j=\widehat X\setminus U_j
\]
is a compact subset of $X$.
Set
\[
K=\widehat X\setminus U.
\]
Then $K\subseteq K_j$.
Moreover,
\[
K
=
K_j\cap\bigcap_{i\in I}\bigl(X\setminus(U_i\cap X)\bigr).
\]
Each $U_i\cap X$ is open in $X$ by <1>1, so every set in the intersection on the right is closed in $X$.
Thus $K$ is closed in the compact space $K_j$, hence compact.
Therefore
\[
U=\widehat X\setminus K\in\mcb.
\]
:::

<1>4. The family $\mcb$ is closed under finite intersections.
::: {.proof}
It is enough to consider two members $U,V\in\mcb$.
If at least one of them does not contain $\infty$, then
\[
U\cap V\subseteq X.
\]
By <1>1, both $U\cap X$ and $V\cap X$ are open in $X$, so
\[
U\cap V\in\mct\subseteq\mcb.
\]

If both contain $\infty$, write
\[
U=\widehat X\setminus K,
\qquad
V=\widehat X\setminus L
\]
with $K,L\subseteq X$ compact.
Then
\[
U\cap V
=
\widehat X\setminus(K\cup L),
\]
and $K\cup L$ is compact.
Hence $U\cap V\in\mcb$.
Together with <1>2 and <1>3, this proves that $\mcb$ is a topology on $\widehat X$.
:::

<1>5. The space $\widehat X$ is compact.
::: {.proof}
Let $\mathcal U$ be an open cover of $\widehat X$.
Choose
\[
U_\infty\in\mathcal U
\]
with $\infty\in U_\infty$.
By <1>1,
\[
K=\widehat X\setminus U_\infty
\]
is compact in $X$.

The sets
\[
U\cap X,
\qquad
U\in\mathcal U,
\]
form an open cover of $K$ in $X$.
Compactness of $K$ gives finitely many
\[
U_1,\ldots,U_r\in\mathcal U
\]
whose intersections with $X$ cover $K$.
Then
\[
U_\infty,U_1,\ldots,U_r
\]
cover all of $\widehat X$.
Thus $\widehat X$ is compact.
:::

<1>6. The subspace $X$ is dense in $\widehat X$.
::: {.proof}
Every point of $X$ already lies in $X$, so it remains only to show
\[
\infty\in\overline X.
\]
Let $U$ be any open neighborhood of $\infty$.
By <1>1,
\[
U=\widehat X\setminus K
\]
for some compact $K\subseteq X$.
If $U\cap X$ were empty, then $K=X$, contradicting the assumption that $X$ is noncompact.
Hence every neighborhood of $\infty$ meets $X$, and therefore
\[
\overline X=\widehat X.
\]
This completes the assertions requested in part (a).
:::

<1>7. In fact, $\widehat X$ is Hausdorff.
::: {.proof}
Two distinct points of $X$ have disjoint open neighborhoods because $X$ is Hausdorff; these neighborhoods are also open in $\widehat X$.

Now let $x\in X$.
By local compactness, there is a compact neighborhood $K\subseteq X$ of $x$.
Choose an open set $V\subseteq X$ with
\[
x\in V\subseteq K.
\]
Then $V$ and
\[
\widehat X\setminus K
\]
are disjoint open neighborhoods of $x$ and $\infty$, respectively.
Thus $\widehat X$ is Hausdorff.
:::

<1>8. Under the usual convention that compact spaces need not be Hausdorff, part (b) is false as printed.
::: {.proof}
Let $p\notin X$ and set
\[
Y=X\cup\{p\}.
\]
Give $Y$ the topology
\[
\mathcal T_Y=\mct\cup\{Y\}.
\]
This is a topology, and its restriction to $X$ is the original topology $\mct$.

The only open neighborhood of $p$ is $Y$ itself.
Consequently every open cover of $Y$ contains $Y$, so $Y$ is compact.
Also every neighborhood of $p$ meets $X$, hence $X$ is dense in $Y$, and plainly
\[
Y\setminus X=\{p\}.
\]
However $Y$ is not Hausdorff: $p$ cannot be separated from any point of $X$ by disjoint neighborhoods.
By <1>7, $\widehat X$ is Hausdorff.
Therefore
\[
Y\not\cong\widehat X.
\]
So the hypotheses printed in part (b) do not imply its conclusion.
:::

<1>9. The intended uniqueness statement is true if $Y$ is assumed compact Hausdorff.
::: {.proof}
Assume now that $Y$ is compact Hausdorff, that $X\subseteq Y$ is dense, and that
\[
Y\setminus X=\{p\}.
\]
Define the bijection
\[
h:Y\longrightarrow\widehat X,
\qquad
h(x)=x\quad(x\in X),
\qquad
h(p)=\infty.
\]
We prove that $h$ is continuous.

First let $U\subseteq\widehat X$ be open with $\infty\notin U$.
Then $U$ is open in $X$.
Since $Y$ is Hausdorff, $\{p\}$ is closed, so
\[
X=Y\setminus\{p\}
\]
is open in $Y$.
Hence every set open in the subspace $X$ is open in $Y$, and therefore
\[
h^{-1}(U)=U
\]
is open in $Y$.

Next let $U$ contain $\infty$.
By <1>1,
\[
U=\widehat X\setminus K
\]
for some compact $K\subseteq X$.
The inclusion $X\hookrightarrow Y$ is continuous, so $K$ is compact in $Y$.
Since $Y$ is Hausdorff, $K$ is closed in $Y$.
Thus
\[
h^{-1}(U)=Y\setminus K
\]
is open.

Hence $h$ is a continuous bijection from the compact space $Y$ to the Hausdorff space $\widehat X$.
It follows that $h$ is a homeomorphism.
Thus part (b) is correct after adding the missing Hausdorff hypothesis on $Y$.
:::

<1>10. The one-point compactification of $(0,1)$ is homeomorphic to $S^1$.
::: {.proof}
The interval $(0,1)$ is homeomorphic to $\RR$, for example by
\[
t\longmapsto \tan\bigl(\pi(t-\tfrac12)\bigr).
\]
Stereographic projection identifies
\[
S^1\setminus\{N\}\cong\RR
\]
for any chosen point $N\in S^1$.
Thus, after identifying $(0,1)$ with $S^1\setminus\{N\}$, the circle $S^1$ is a compact Hausdorff space containing $(0,1)$ densely with one-point complement.
By <1>9, its one-point compactification is therefore
\[
\boxed{S^1}.
\]
:::

<1>11. The one-point compactification of $\RR^2$ is homeomorphic to $S^2$.
::: {.proof}
Stereographic projection gives a homeomorphism
\[
S^2\setminus\{N\}\cong\RR^2.
\]
The sphere $S^2$ is compact Hausdorff, and $S^2\setminus\{N\}$ is dense with singleton complement.
Applying <1>9 gives
\[
\boxed{\widehat{\RR^2}\cong S^2}.
\]
This proves part (c).
:::
:::
