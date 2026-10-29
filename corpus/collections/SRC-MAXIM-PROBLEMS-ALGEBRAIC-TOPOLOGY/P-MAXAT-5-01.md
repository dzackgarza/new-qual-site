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

::: pf

::: {.pf-step #s1-1}

Principal $S^1$-bundles over a paracompact space $X$ are classified by homotopy classes of maps
\[
[X,BS^1].
\]


::: pf-proof

The universal principal circle bundle
\[
S^1\longrightarrow ES^1\longrightarrow BS^1
\]
has contractible total space. Pullback along a map $X\to BS^1$ produces a principal $S^1$-bundle over $X$, and the classifying-space theorem identifies homotopic maps exactly with isomorphic bundles.

:::

:::

::: {.pf-step #s1-2}

Since
\[
BS^1\simeq\CP^{\infty}=K(\ZZ,2),
\]
one has
\[
[S^2,BS^1]
\cong H^2(S^2;\ZZ)
\cong\ZZ.
\]


::: pf-proof

The infinite complex projective space is the classifying space of $S^1=U(1)$ and is an Eilenberg--MacLane space $K(\ZZ,2)$. Maps into $K(\ZZ,2)$ represent degree-$2$ integral cohomology. The fundamental class identifies $H^2(S^2;\ZZ)$ with $\ZZ$.

:::

:::

::: {.pf-step #s1-3}

The integer classifying a bundle
\[
S^1\to E\xrightarrow{p}S^2
\]
is
\[
k=\langle c_1(E),[S^2]\rangle\in\ZZ.
\]


::: pf-proof

Under the identification in step [](#s1-2){.pf-ref}, the universal generator of $H^2(BS^1;\ZZ)$ pulls back to the first Chern class of the associated complex line bundle. Evaluating this class on the fundamental class of $S^2$ gives the corresponding integer.

:::

:::

::: {.pf-step #s1-4}

Equivalently, the classification can be obtained by clutching along the equator:
\[
S^2=D^2_+\cup_{S^1}D^2_-.
\]
The clutching function is a map
\[
g:S^1\to S^1,
\]
and its degree $k$ is the complete invariant.


::: pf-proof

Every bundle is trivial over each hemisphere because each disk is contractible. The two trivializations differ on the equator by a transition function $g:S^1\to S^1$. Changing trivializations changes $g$ by homotopy, and homotopy classes
\[
[S^1,S^1]\cong\pi_1(S^1)\cong\ZZ
\]
are classified by degree. This integer agrees with the Chern number in step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

A representative of class $k$ is obtained by gluing
\[
D^2_+\times S^1
\quad\text{and}\quad
D^2_-\times S^1
\]
along their boundary by
\[
(z,u)_+\sim(z,z^ku)_-.
\]


::: pf-proof

The map $z\mapsto z^k$ has degree $k$, so this is exactly the clutching construction from step [](#s1-4){.pf-ref} for the class $k$.

:::

:::

::: pf-step

For $k=0$ the total space is
\[
S^2\times S^1.
\]
For $k=\pm1$ the total space is $S^3$ with the Hopf fibration, up to orientation of the circle action. For $|k|>1$ the total space is the lens space
\[
L(|k|,1)
\]
up to orientation convention.


::: pf-proof

Degree zero gives the constant clutching map and hence the product bundle. The Hopf bundle has Chern number $1$, and reversing the $S^1$ action changes the sign. Quotienting the Hopf $S^1$ action on $S^3$ by its subgroup of $|k|$th roots of unity gives the circle bundle of Chern number $k$; its total space is the standard lens space $L(|k|,1)$.

:::

:::

::: {.pf-step #s1-7}

Therefore
\[
\boxed{
\{\text{principal }S^1\text{-bundles over }S^2\}/\cong
\;\cong\;\ZZ,}
\]
classified by $c_1$ or, equivalently, the degree of the clutching map.


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} identify the set of isomorphism classes with $\ZZ$, and step [](#s1-5){.pf-ref} gives an explicit representative of every integer class.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the requested classification.

:::

:::

:::
