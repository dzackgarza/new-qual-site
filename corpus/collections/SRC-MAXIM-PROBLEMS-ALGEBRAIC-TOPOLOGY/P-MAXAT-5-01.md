---
schema: qual/card@1
id: P-MAXAT-5-01
kind: problem
title: Maxim algebraic topology 5.1
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 5, problem 1 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Classify the $S ^ { 1 } \mathbf { \Phi } .$ -bundles over $S ^ { 2 } .$
:::

::: {.solution}
Interpret the statement as asking for principal $S^1$-bundles over $S^2$. Their isomorphism classes are indexed by an integer, the first Chern number.

<1>1. Principal $S^1$-bundles over a paracompact space $X$ are classified by homotopy classes of maps
\[
[X,BS^1].
\]

::: {.proof}
The universal principal circle bundle
\[
S^1\longrightarrow ES^1\longrightarrow BS^1
\]
has contractible total space. Pullback along a map $X\to BS^1$ produces a principal $S^1$-bundle over $X$, and the classifying-space theorem identifies homotopic maps exactly with isomorphic bundles.
:::

<1>2. Since
\[
BS^1\simeq\mathbb{CP}^{\infty}=K(\mathbb Z,2),
\]
one has
\[
[S^2,BS^1]
\cong H^2(S^2;\mathbb Z)
\cong\mathbb Z.
\]

::: {.proof}
The infinite complex projective space is the classifying space of $S^1=U(1)$ and is an Eilenberg--MacLane space $K(\mathbb Z,2)$. Maps into $K(\mathbb Z,2)$ represent degree-$2$ integral cohomology. The fundamental class identifies $H^2(S^2;\mathbb Z)$ with $\mathbb Z$.
:::

<1>3. The integer classifying a bundle
\[
S^1\to E\xrightarrow{p}S^2
\]
is
\[
k=\langle c_1(E),[S^2]\rangle\in\mathbb Z.
\]

::: {.proof}
Under the identification in step <1>2, the universal generator of $H^2(BS^1;\mathbb Z)$ pulls back to the first Chern class of the associated complex line bundle. Evaluating this class on the fundamental class of $S^2$ gives the corresponding integer.
:::

<1>4. Equivalently, the classification can be obtained by clutching along the equator:
\[
S^2=D^2_+\cup_{S^1}D^2_-.
\]
The clutching function is a map
\[
g:S^1\to S^1,
\]
and its degree $k$ is the complete invariant.

::: {.proof}
Every bundle is trivial over each hemisphere because each disk is contractible. The two trivializations differ on the equator by a transition function $g:S^1\to S^1$. Changing trivializations changes $g$ by homotopy, and homotopy classes
\[
[S^1,S^1]\cong\pi_1(S^1)\cong\mathbb Z
\]
are classified by degree. This integer agrees with the Chern number in step <1>3.
:::

<1>5. A representative of class $k$ is obtained by gluing
\[
D^2_+\times S^1
\quad\text{and}\quad
D^2_-\times S^1
\]
along their boundary by
\[
(z,u)_+\sim(z,z^ku)_-.
\]

::: {.proof}
The map $z\mapsto z^k$ has degree $k$, so this is exactly the clutching construction from step <1>4 for the class $k$.
:::

<1>6. For $k=0$ the total space is
\[
S^2\times S^1.
\]
For $k=\pm1$ the total space is $S^3$ with the Hopf fibration, up to orientation of the circle action. For $|k|>1$ the total space is the lens space
\[
L(|k|,1)
\]
up to orientation convention.

::: {.proof}
Degree zero gives the constant clutching map and hence the product bundle. The Hopf bundle has Chern number $1$, and reversing the $S^1$ action changes the sign. Quotienting the Hopf $S^1$ action on $S^3$ by its subgroup of $|k|$th roots of unity gives the circle bundle of Chern number $k$; its total space is the standard lens space $L(|k|,1)$.
:::

<1>7. Therefore
\[
\boxed{
\{\text{principal }S^1\text{-bundles over }S^2\}/\cong
\;\cong\;\mathbb Z,}
\]
classified by $c_1$ or, equivalently, the degree of the clutching map.

::: {.proof}
Steps <1>1--<1>4 identify the set of isomorphism classes with $\mathbb Z$, and step <1>5 gives an explicit representative of every integer class.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the requested classification.
:::
:::
