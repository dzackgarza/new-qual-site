# Topology Qual Prep Week 1: Point-Set

D. Zack Garza

## Table of Contents

## Contents

Table of Contents 2\
1 Topics 3\
2 Warmups 3\
3 Exercises 4\
4 Qual Questions 5

## 1 Topics

• Definitions:

– topologies,

– open/closed/clopen, bases,

– continuity,

– homeomorphisms,

– subspaces

– products,

– quotients

– closures,

– retracts

• Metric spaces

– Complete

– Bounded

• Compactness

• Connectedness

– Path-connected

– Locally path-connected

– Totally disconnected

• Separation axioms,

– Hausdorff,

– Normal,

– Regular

• The tube lemma

• Common counterexamples (sine curve)

## 2 Warmups

• State the axioms of a topology.

• What does it mean for a set to be open?
Closed?

• State the definition of the product topology, the subspace topology, and the quotient topology.

• What does it mean for a family of sets to form a basis for a topology?

• What is an interior point?
An isolated point?
A limit point?

• What is the closure of a subspace $E \subseteq X ?$

• What does it mean for a topological space to be compact?

• What does it mean for $E \subseteq X$ to be a dense subspace?

• Come up with 6 different topologies on $\mathbb { R } ^ { d }$

• What is a separable space?

• What is a nowhere dense subspace?

## 3 Exercises

• Prove Cantor’s intersection theorem.

• Determine if the following subsets of R are opened, closed, both, or neither:

$$
{ \begin{array} { r l } & { { \mathrm { ~ - ~ } } \mathbb { Q } } \\ & { { \mathrm { ~ - ~ } } \mathbb { Z } } \\ & { - \ \{ 1 \} } \\ & { { \mathrm { ~ - ~ } } \{ p \in \mathbb { Z } ^ { \geq 0 } \ | \ p { \mathrm { ~ i s ~ p r i m e } }  \} } \\ & { { \mathrm { ~ - ~ } } \{ { \frac { 1 } { n } } \ | \ n \in \mathbb { Z } ^ { \geq 0 }  \} } \\ & { { \mathrm { ~ - ~ } } \{ { \frac { 1 } { n } } \ | \ n \in \mathbb { Z } ^ { \geq 0 } \} \cup \{ 0 \} } \end{array} }
$$

• Prove that $\mathbb { R } ^ { n }$ is not homeomorphic to R for any $n \geq 2$

• Is it true that the closure of a product is the product of the closures?

– Is it true that the interior of a product is the product of the interiors?

• Find a space that is connected but not locally connected.
Can there be a space that is locally connected but not connected?

• Show that for X an arbitrary topological space, the one-point compactification $\widehat { X }$ (with its corresponding topology) is compact.

• Prove that path-connected implies connected

– Show that the topologist’s sine curve is connected but not path-connected.

• Is every product (finite or infinite) of Hausdorff spaces Hausdorff?

• Is R homeomorphic to [0, ∞)?

• Show that X is connected iff the only subsets of X which are both closed and open are ∅, X.

• Show that a closed subset A of a compact space X is compact.
Does this hold when A is instead an open subset?

• Show that if $f : X \to Y$ is continuous and X is compact then the image $f ( X ) \subseteq Y$ is compact.

• Show that every compact metric space is complete.

• Show that a compact subset of a Hausdorff space is closed.
Does the converse hold?

– What property on a space guarantees that compact sets are closed

– What property on a space guarantees that closed sets are compact?

• Show that a continuous bijection from a compact space to a Hausdorff space is necessarily a homeomorphism.

1. (May 2016) Given any topological space $Z$ and subset $D \subseteq Z$ , let $C l _ { Z } ( D )$ denote the closure of D in $Z .$ Show that if X and $Y$ are topological spaces and $A \subseteq X , B \subseteq Y$ , then $C l _ { X \times Y } ( A \times B ) =$ $C l _ { X } ( A ) \times C l _ { Y } ( B )$

2. (May 2016) Let X be a connected space and $A , B \subseteq X$ be closed subsets of X with $X = A \cup B$ and A ∩ B a connected subset of X. Show that both A and B are connected.

$$
\bullet \ T _ { 4 } \ =
$$

• Prove the following implications of separation axioms, and show that they are strict:

• Show that every compact metrizable space has a countable basis.

## 4 Qual Questions

Show that for any two topological spaces X and $Y \ , X \times Y$ is compact if and only if both X and Y are compact.

Tube lemma:

Solution:

Problem 1.1.9 (?)

If X is a topological space and $S \subset X$ , define in terms of open subsets of X what it means for S not to be connected.

Show that if S is not connected there are nonempty subsets A, $B \subset X$ such that

$$
A \cup B = S \quad { \mathrm { a n d } } \quad A \cap { \overline { { B } } } = { \overline { { A } } } \cap B = \emptyset
$$

Here A and B denote closure with respect to the topology on the ambient space X.

Problem 1.3.3 (?) Let

$$
X = \left\{ ( x , y ) \in \mathbb { R } ^ { 2 } | x > 0 , y \geq 0 , { \mathrm { ~ a n d ~ } } { \frac { y } { x } } { \mathrm { ~ i s ~ r a t i o n a l ~ } } \right\}
$$

and equip X with the subspace topology induced by the usual topology on $\mathbb { R } ^ { 2 }$ Prove or disprove that X is connected.

## Problem 1.4.3 (Spring 2009, 31)

a. Show that a continuous bijection from a compact space to a Hausdorff space is a homeomorphism.

b. Give an example that shows that the "Hausdorff" hypothesis in part (a) is necessary.

## Problem 1.4.4 (?)

Let X be a topological space and let

$$
\Delta = \left\{ ( x , y ) \in X \times X \ \middle | \ x = y \right\} .
$$

Show that X is a Hausdorff space if and only if Δ is closed in $X \times X$
