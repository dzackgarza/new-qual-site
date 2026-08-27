# Algebraic Geometry FS 15: Exam Guidelines and Problems

12. August 2015

## 1 Exam Guidelines

Some of the questions will draw from the homework problems and the new problems listed below. The exam is not intended to be computationally intensive but instead to demonstrate some understanding of how to apply the basic definitions and results to concrete problems. In some cases we will ask about simpler special cases of some of those problems. For instance, Problem 2.1 on Sheet 3 asks one to verify that with $X : = \mathbb { A } ^ { 2 }$ and $U : = \mathbb { A } ^ { 2 } - O$ , the restriction map $A ( X ) = \mathcal { O } ( X ) \to \mathcal { O } ( U )$ is an isomorphism. We might just ask: “give an example of a proper open subset U of $X : = \mathbb { A } ^ { 2 }$ for which the restriction map $A ( X ) \longrightarrow { \mathcal { O } } ( U )$ is an isomorphism.” You will also be expected to know the basic definitions, concepts and results from the course, including but not limited to Zariski topology, affine varieties, projective varieties, regular functions, morphisms, affine/projective coordinate rings, dimension, connectedness/irreducibility, rational functions/rational maps, birational equivalence, function field, localization, images of morphisms, blow-ups, nonsingularity, products of projective varieties and the Segre embedding, differential forms, ramification indices.

The two lectures of the final week will not be covered in the exam.

During the exam you might be asked to state precise definitions of basic concepts and main results. Here is an example of a sequence of questions illustrating the intended exam format. Note that the answer to several of these questions is contained in the lectures and exercises.

Describe $\mathbb { P } ^ { 2 }$ and the standard embedding $\mathbb { A } ^ { 2 } \hookrightarrow \mathbb { P } ^ { 2 }$ . Let $Z : = V ( y ^ { 2 } - x ^ { 3 } )$ What is $A ( Z ) \stackrel { \mathcal { Q } } { : } I s Z$ irreducible? What is the projective closure Z of Z? What is $\overline { { Z } } - Z \ell$ Can you depict this result with a picture? Does the morphism $f : Z - \{ 0 \} \ \to \mathbb { P } ^ { 1 }$ given by $f ( \alpha , \beta ) = [ \alpha , \beta ]$ extend to a morphism $Z \to \mathbb { P } ^ { 1 } \mathcal { Z }$ Is f bijective? Is it an isomorphism? Is f a birational equivalence? What is the function field of Z? Can you compute the blow-up of Z at $\{ 0 \} \ell$ Where is Z nonsingular? What is the integral closure of $A ( Z ) \ell$ What is the normalization of Z?

## 2 Problems from the exercise sheets

Sheet 1: Problems 1, 3a and 3b, 6   
Sheet 2: Problems 1, 2, 3, 6   
Sheet 3: Problems 1, 2   
Sheet 4: Problems 1, 2 without 2e, 3, 5, 6   
Sheet 5: Problems 1 (in 1a not the full calculation will be asked), 2, 3, 5, 6   
Sheet 6: Problems 4, 5   
Sheet 7: Problems 3, 5a   
Sheet 8: Problems 1 (results from sheet 7 may be freely used), 3, 4a, 5   
Sheet 9: Problems 1, 2a and 2b, 3 (correction in 3a: X is in addition assumed irreducible)   
Sheet 10: 1, 3, 5   
Sheet 11: 1

## 3 New problems

Unless stated otherwise we work over an algebraically closed field k. Any material from the lectures and the exercise sheets may be freely used.

1. (Gathmann lecture notes Exercise 2.31) Let X be the set of all $2 \times 3$ -matrices over k that have rank at most one, considered as a subset of $\mathrm { M a t _ { 2 , 3 } } ( k ) = \mathbb { A } ^ { 6 }$ . Show that X is an affine variety. Is it irreducible? What is its dimension?

Hint: You may use the Segre embedding.

2. (Gathmann lecture notes Exercise 4.14) Let $f : X \to Y$ be a morphism of affine varieties and $f ^ { \sharp } : A ( Y ) \to A ( X )$ the corresponding homomorphism of coordinate rings. Are the following statements true or false?

a) f is surjective if and only if $f ^ { \sharp }$ is injective.

b) f is injective if and only if $f ^ { \sharp }$ is surjective.

c) If $f : \mathbb { A } ^ { 1 } \longrightarrow \mathbb { A } ^ { 1 }$ is an isomorphism, then f is affine linear, i.e. of the form $f ( x ) =$ $a x + b$ for some $a , b \in k$

d) If $f : \mathbb { A } ^ { 2 } \longrightarrow \mathbb { A } ^ { 2 }$ is an isomorphism, then f is affine linear, i.e. of the form $f ( x ) =$ $A x + b$ for some $A \in \mathrm { M a t } _ { 2 , 2 } ( k )$ and $b \in k$

3. Let S be a finite set of points of a quasi-projective variety X. Show that $S$ is contained in an affine open subset of X.

4. We consider $f \in k [ z , z ^ { - 1 } ]$ as a morphism $f : \mathbb { A } ^ { 1 } \backslash \{ 0 \}  \mathbb { A } ^ { 1 }$

a) Show that f extends uniquely to a morphism $\overline { { f } } : \mathbb { P } ^ { 1 } \to \mathbb { P } ^ { 1 }$

b) For which f is f an automorphism?

c) For which f is $\overline { { f } } ^ { * } : \Omega _ { \mathbb { P } ^ { 1 } } \to \Omega _ { \mathbb { P } ^ { 1 } }$ 1 an isomorphism? Here $\Omega _ { \mathbb { P } ^ { 1 } }$ is the $k ( \mathbb { P } ^ { 1 } )$ -vector space of rational differentials on $\mathbb { P } ^ { 1 }$

5. Let char $k = 0$ . Consider the curve C given by $y ^ { 2 } = ( x - e _ { 1 } ) ( x - e _ { 2 } ) ( x - e _ { 3 } )$ in $\mathbb { A } ^ { 2 }$ with $e _ { j } \in k$ pairwise distinct. Let $P _ { j } = ( e _ { j } , 0 ) \in C$ and $P _ { \infty }$ be the point at infinity, lying in $\overline { { C } } \subseteq \mathbb { P } ^ { 2 }$ . Solve the exercise from the lecture stating

$$
\mathrm { d i v } ( \mathrm { d } x ) = [ P _ { 1 } ] + [ P _ { 2 } ] + [ P _ { 3 } ] - 3 [ P _ { \infty } ]
$$

$$
\mathrm { d i v } ( y ) = [ P _ { 1 } ] + [ P _ { 2 } ] + [ P _ { 3 } ] - 3 [ P _ { \infty } ]
$$

and div $\begin{array} { r } { \left( \frac { \mathrm { d } x } { y } \right) = 0 } \end{array}$ , i.e. $\frac { \mathrm { d } x } { y }$ is a regular nowhere vanishing differential on $\overline { C }$