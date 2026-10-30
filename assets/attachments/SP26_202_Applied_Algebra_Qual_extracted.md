# Spring 2026 Applied Algebra Qualifying Exam Math 202 A/B/C

## Name:

## Instructions.

1. There are ten problems on this exam.

2. Give complete proofs and justify all assertions.

3. Throughout this exam, the term Hilbert space refers to a finite-dimensional complex vector space V equipped with a scalar product.

4. The term algebra refers to a finite-dimensional complex vector space A equipped with an associative, bilinear, unital multiplication and an antilinear, antimultiplicative, involutive conjugation.

5. All algebra homomorphisms respect multiplication, conjugation, and units.

## Problem 1.

Let V and W be Hilbert spaces, each of dimension at least two. Prove that the operator norm on Hom(V, W ) is not induced by any scalar product on Hom(V, W ).

## Problem 2.

Let A be an $m \times n$ matrix whose columns are one-hot binary vectors: each column contains exactly one entry equal to 1 and all other entries are equal to 0. Let $r _ { i }$ denote the sum of the entries in row i of A. Determine the nonzero singular values of A, and give explicit orthonormal bases for each of the corresponding left and right singular spaces.

## Problem 3.

Let $( V , \varphi )$ and $( W , \psi )$ be finite-dimensional unitary representations of a group G. Let $A \in \operatorname { H o m } _ { G } ( V , W )$ be a G-equivariant linear map with operator norm $\sigma _ { 1 } > 0$ . Prove that

$$
V _ { 1 } = \{ v \in V : \| A v \| = \sigma _ { 1 } \| v \| \}
$$

is a subrepresentation of $( V , \varphi )$

## Problem 4.

Let A be an algebra. Prove that A is commutative if and only if all its elements are normal.

## Problem 5.

Let A be an algebra which admits a faithful state σ : $A \to \mathbb { C }$ . Prove that A admits a faithful tracial state $\tau \colon A  \mathbb { C }$

## Problem 6.

Let B be a commutative subalgebra of an algebra A. Prove that B is a maximal commutative subalgebra of A if and only if it is equal to its own centralizer. Using this result, or otherwise, classify the maximal commutative subalgebras of End(V ), where V is a Hilbert space.

## Problem 7.

Let $G = ( S , T )$ be the graph whose vertex set S consists of all bitstrings of length 3, with $\{ s _ { 1 } , s _ { 2 } \} \in T$ an edge if and only if $s _ { 1 }$ and $s _ { 2 }$ differ by a single bit. Let $A \in$ End $\mathcal { F } ( S )$ be the adjacency operator of G. Find the eigenvalues of A, and give an orthonormal basis for each eigenspace.

## Problem 8.

Let G be a nontrivial finite group of odd order. Show that the convolution algebra C(G) contains a subalgebra B not isomorphic to $\mathcal { C } ( H )$ for any subgroup $H \leq G$

## Problem 9.

Let $n \geq 2$ . Let $S _ { n } = \operatorname { A u t } \{ 1 , \dots , n \}$ be the symmetric group, and consider the unitary representation $( V , \varphi )$ of $S _ { n }$ in which

$$
V = \bigoplus _ { i = 1 } ^ { n } \mathbb { C } | i \rangle , \qquad \varphi ( \pi ) | i \rangle = | \pi ( i ) \rangle .
$$

Decompose $( V , \varphi )$ into irreducible unitary representations of $S _ { n } ,$ with proof. Write out the character table of $S _ { 3 }$

## Problem 10.

Let G be a finite group and let H be a subgroup of G. Let $\Lambda ( G )$ be a set parameterizing irreducible unitary representations $V ^ { \lambda }$ of G, and let $\Lambda ( H )$ be a set parameterizing irreducible unitary representations $W ^ { \mu }$ of H. For $\lambda \in \Lambda ( G )$ and $\mu \in \Lambda ( H )$ , let $m _ { \lambda \mu }$ be the multiplicity of $W ^ { \mu }$ in the restriction of $V ^ { \lambda }$ to H. Omitting terms with $m _ { \lambda \mu } = 0$ , show that the centralizer of $\mathcal { C } ( H )$ in ${ \mathcal { C } } ( G )$ is isomorphic to

$$
\bigoplus _ { \lambda \in \Lambda ( G ) } \bigoplus _ { \mu \in \Lambda ( H ) } { \mathrm { E n d } } { \left( \mathbb { C } ^ { m _ { \lambda \mu } } \right) } .
$$