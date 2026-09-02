# Topology Qualifying Exam Review

D. Zack Garza

## Table of Contents

## Contents

Table of Contents 2   
1 Preface 5   
1.1 Notation 5   
1.2 Background Algebra 6   
2 Summary and Topics: Point-Set Topology 7   
3 Definitions 7   
3.1 Point-Set Topology 7   
3.2 Algebraic Topology 13   
3.3 Homotopy 28   
4 Examples 29   
4.1 Point-Set 29   
4.1.1 Common Spaces and Operations 29   
4.1.2 Alternative Topologies 32   
4.1.3 Connectedness 33   
5 “Analysis”-esque Results in Topology 33   
6 Theorems 33   
6.1 Metric Spaces and Analysis 34   
6.2 Compactness 35   
6.3 Separability 36   
6.4 Maps and Homeomorphism 36   
6.5 The Tube Lemma . 37   
7 Summary of Standard Topics 39   
8 Examples: Algebraic Topology 40   
8.1 Standard Spaces and Modifications 40   
8.2 Modifying Known Spaces 44   
9 Low Dimensional Homology Examples 44   
10 Table of Homotopy and Homology Structures 44   
11 Theorems: Algebraic Topology 46   
11.1 General Homotopies 46   
11.2 Fundamental Group 47   
11.2.1 Definition 47   
11.2.2 Conjugacy in π1: 48   
11.2.3 Calculating π1 48   
11.2.4 Facts . 51   
11.3 General Homotopy Theory 52   
12 Covering Spaces 53   
12.1 Useful Facts 56   
12.2 Universal Covers 56   
12.2.1 Examples 58   
12.2.2 Applications 61   
13 CW and Simplicial Complexes 63   
13.1 Degrees 63   
13.2 Examples of CW Complexes/Structures 64   
13.3 Examples of Simplicial Complexes 65   
13.4 Cellular Homology 67   
13.5 Constructing a CW Complex with Prescribed Homology 68   
14 Homology 69   
14.1 Useful Facts 69   
14.2 Known Homology . 70   
14.3 Mayer-Vietoris 70   
14.4 More Exact Sequences 72   
14.5 Relative Homology 73   
15 Fixed Points and Degree Theory 74   
16 Surfaces and Manifolds 74   
16.1 Classification of Surfaces 75   
16.2 Manifolds 79   
16.2.1 3-Manifolds, and Knot Complements 80   
17 Extra Problems: Algebraic Topology 81   
17.1 Homotopy 101 81   
17.2 π1 . . 82   
17.3 Surfaces 82   
18 Fall 2014 82   
18.1 1 82   
18.2 2 82   
18.3 3 82   
18.4 4 83   
18.5 5 84   
19 Summer 2003 84   
19.1 1 84   
19.2 2 85   
19.3 3 8686   
19.4 4   
19.5 5   
19.6 6 89   
19.7 7 92   
19.8 8 92   
19.9 9 93   
20 Fall 2017 Final 95   
20.1 1 95   
20.2 2 95   
20.3 3 95   
20.4 4 96   
20.5 5 96   
20.6 6 97   
21 Appendix: Homological Algebra 97   
21.1 Exact Sequences 97   
21.2 Five Lemma . 98   
21.3 Free Resolutions 98   
21.4 Properties of Tensor Products 99   
21.5 Properties of Hom 99   
21.6 Properties of Tor 99   
21.7 Properties of Ext 99   
21.8 Computing Tor 99   
21.9 Computing Ext 100   
21.10Hom/Ext/Tor Tables . 100   
22 Appendix: Unsorted Stuff 101   
22.1 Cap and Cup Products . 101   
22.2 The Long Exact Sequence of a Pair 103   
22.3 Tables 104   
22.4 Homotopy Groups of Lie Groups 105   
22.5 Higher Homotopy . 106   
22.6 Higher Homotopy Groups of the Sphere 106   
22.7 Misc . 107   
22.8 Building a Moore Space 107   
Bibliography 107

## 1 Preface

References:

• Munkres [2]

• Hatcher [1]

Some fun resources:

• The Line with Two Origins

## 1.1 Notation

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $X \times Y , \prod X _ { j } , X ^ { \times n }$   $j \in J$ </td><td>Direct Products</td></tr><tr><td> $X \oplus Y , \bigoplus X _ { j } , X ^ { \oplus n }$   $j \in J$ </td><td>Direct sums</td></tr><tr><td> ${ X \otimes Y , \bigotimes X _ { j } , X ^ { \otimes n } }$   $j \in J$ </td><td>Tensor products</td></tr><tr><td> $X * Y , * _ { j \in J } X _ { j } , X ^ { * n }$ </td><td>Free products</td></tr><tr><td> $\mathbb { Z } ^ { n }$ </td><td>The free abelian group of rank n</td></tr><tr><td> $F _ { n } , \mathbb { Z } ^ { * n }$ </td><td>The free group on n generators</td></tr><tr><td> $\pi _ { 0 } ( X )$ </td><td>The set of path components of X</td></tr><tr><td> $G = 1$ </td><td>The trivial abelian group</td></tr><tr><td> $G = 0$ </td><td>The trivial nonabelian group</td></tr></table>

Remark 1.1.1: I use $e _ { G }$ or $1 _ { G } , 0 _ { G }$ to denote identity elements in a group G.

Remark 1.1.2(on direct sums vs direct products): $A \times B$ denotes the direct product of modules. A ⊕ B denotes a direct sum: the subset of $A \times B$ where only finitely many terms are nonzero. Both the product and direct sum have coordinate-wise operations. For finite index sets $| J | < \infty ,$ , the direct sum and product coincide, but in general there is only an injection $\bigoplus X _ { i } { \dot { \hookrightarrow } } \prod X _ { j }$ . In the direct sum $\bigoplus X _ { j }$ have only finitely many nonzero entries, while the j j j

product allows infinitely many nonzero entries. So in general, I always use the product notation.

Remark 1.1.3(on notation for free groups and free products): The free group on n generators is the free product of n free abelian groups, but is not generally abelian! So we use multiplicative notation, and elements

$$
x \in \mathbb { Z } ^ { * n } = \langle a _ { 1 } , \ldots , a _ { n } \rangle
$$

are finite words in the noncommuting symbols $a _ { i } ^ { k }$ for $k \in \mathbb { Z }$ . E.g. an element may look like

$$
x = a _ { 1 } ^ { 2 } a _ { 2 } ^ { 4 } a _ { 1 } a _ { 2 } ^ { - 2 } .
$$

Remark 1.1.4(on notation for free abelian groups): The free abelian group of rank n is the abelianization of $\mathbb { Z } ^ { \ast n }$ , and its elements are characterized by

$$
x \in \mathbb { Z } ^ { * n } = \langle a _ { 1 } , \cdots , a _ { n } \rangle \implies x = \sum _ { n } { c _ { i } a _ { i } { \mathrm { ~ f o r ~ s o m e ~ } } c _ { i } \in \mathbb { Z } }
$$

where the $a _ { i }$ are some generating set of n elements and we used additive notation since the group is abelian. E.g. such an element may look like

$$
x = 2 a _ { 1 } + 4 a _ { 2 } + a _ { 1 } - a _ { 2 } = 3 a _ { 1 } + 3 a _ { 2 } .
$$

Remark 1.1.5(on indexing conventions and list notation): Spaces are assumed to be connected and path connected, so $\pi _ { 0 } ( X ) = H _ { 0 } ( X ) = \mathbb { Z }$ . So I virtually never consider anything occurring at index zero in these notes.

Graded objects such as $\pi _ { * } , H _ { * } , H ^ { * }$ are sometimes represented as lists, which always start indexing at 1. Examples:

$$
\begin{array} { l } { { \pi _ { * } ( X ) = [ \pi _ { 1 } ( X ) , \pi _ { 2 } ( X ) , \pi _ { 3 } ( X ) , \cdots ] } } \\ { { { \cal H } _ { * } ( X ) = [ H _ { 1 } ( X ) , H _ { 2 } ( X ) , H _ { 3 } ( X ) , \cdots ] . } } \end{array}
$$

## 1.2 Background Algebra

Fact 1.2.1

An injective group morphism $f : X \hookrightarrow Y$ where X is trivial forces $Y$ to be trivial.

Proposition 1.2.2(Morphisms between groups finite and infinite groups). There are no nontrivial homomorphisms from finite groups into free groups. In particular, any group morphism $f : \mathbb { Z } _ { n } \to \mathbb { Z }$ is trivial.

Proof (?).

Let $f : G \to H$ , then $f ( 1 _ { G } ) = 1 _ { H }$ . Supposing $g \in G$ is torsion of order n, we have

$$
1 _ { H } = f ( 1 _ { G } ) = f ( g ^ { n } ) = f ( g ) ^ { n } ,
$$

so $f ( g )$ is torsion of order dividing n. But a free group is torsionfree.

Remark 1.2.3(How to use this fact): This is especially useful if you have some $f : A  B$ and you look at the induced homomorphism $f _ { * } : \pi _ { 1 } ( A ) \to \pi _ { 1 } ( B )$ . If the former is finite and the latter contains a copy of Z, then $f _ { * }$ has to be the trivial map $f _ { * } ( [ \alpha ] ) = e \in \pi _ { 1 } ( B )$ for every $[ \alpha ] \in \pi _ { 1 } ( A )$ You can play a similar game when you take homology or cohomology.

## 2 Summary and Topics: Point-Set Topology

Some key high-level topics:

• Connectedness

• Compactness

• Metric spaces

• Hausdorff spaces

## 3 Definitions

## 3.1 Point-Set Topology

Remark 3.1.1(on the term ’locally’): The prefix “locally blah” almost always means that for every $x \in X$ , there exists some neighborhood $N _ { x } \ni x$ which has property “blah”.

Definition 3.1.2 (Basis for a topology)   
A set B is a basis for a topology iff

• B is closed under intersections,

• Every $x \in X$ is in some basic set,

• If x is in the intersection of two basis sets $B _ { 1 } \cap B _ { 2 }$ , there is a third basic open $B _ { 3 } \ni x$ with $B _ { 3 } \subset B _ { 1 } \cap B _ { 2 }$

The topology generated by B is the following: $U \subseteq X$ is open iff for each $x \in U$ there is a basic open B with $x \in B \subset U$ . Equivalently, every open set is a union of basic open sets.

A set S in a metric space $( X , d )$ is bounded iff there exists an $m \in \mathbb { R }$ such that $d ( x , y ) < m$ for every $x , y \in S .$

Definition 3.1.4 (Comparability of topologies)   
Given two topologies τ1, τ2,   
• $\tau _ { 1 }$ is finer than τ2 iff $\tau _ { 1 } \supseteq \tau _ { 2 }$   
$\tau _ { 1 }$ is coarser than τ2 iff $\tau _ { 1 } \supseteq \tau _ { 2 }$   
Two topologies are comparable if either $\tau _ { 1 } < \tau _ { 2 }$ or $\tau _ { 2 } < \tau _ { 1 }$   
Note: more open sets is like having a “finer” reso  
lution.

## Is this actually a poset relation? Fails reflexivity.

## Definition 3.1.5 (Connected)

A space X is connected iff there does not exist a disconnection $X = A \mathbf { J } [ B$ with A, B nonempty open sets. I.e. X can not be written as the disjoint union of two proper nonempty open sets. Equivalently, X contains no proper nonempty clopen sets.

Note that there is an additional condition for a subspace $Y \subset X$ to be connected:

$$
\operatorname { c l } _ { Y } ( A ) \cap V = A \cap \operatorname { c l } _ { Y } ( B ) = \emptyset .
$$

Definition 3.1.6 (Connected Components)   
Set $x \sim y$ iff there exists a connected set $U \ni x , y$ and take equivalence classes. These classes   
are the connected components of X.

## Definition 3.1.7 (Closed Sets)

• A set is closed if and only if its complement is open.

• A set is closed iff it contains all of its limit points.

• A closed set in a subspace: $Y \subset X \implies \mathrm { c l } _ { Y } ( A ) : = \mathrm { c l } _ { X } ( A ) \cap Y .$

```latex
Definition 3.1.9 (Closure of a set)
For $U \subseteq X$ the closure of U in X is given by $\operatorname { C l } _ { X } ( U ) = \cap _ { B \supseteq U } B$ the intersection of all
closed sets in X containing U . For $Y \subseteq X$ a subspace containing U, the closure of U in closed $Y$ is
$\operatorname { C l } _ { Y } ( U ) = \operatorname { C l } _ { X } ( U ) \cap Y . ^ { a }$ In general, we write ${ \overline { { U } } } : = \operatorname { c l } _ { X } ( U )$
An equivalent condition: $x \in { \overline { { U } } }$ ⇐⇒ every neighborhood of x intersects $\boldsymbol { U } . ^ { b }$
aThis is theorem 17.4 in Munkres
bMunkres 17.5
Definition 3.1.10 (Compact)
A topological space $( X , \tau )$ is compact iff every open cover has a finite subcover. That is, if
$\{ U _ { j } \} _ { j \in J } \subseteq \tau$ is a collection of open sets such that $X = \bigcup U _ { j }$ then there exists a finite subset
j∈J
$J ^ { \prime } \subset J$ such that $X \subseteq \bigcup U _ { j }$
j∈J 0
Definition 3.1.11 (Continuous Map)
A map $f : X \to Y$ between topological spaces is continuous if and only if whenever $U \subseteq Y$ is
open, $f ^ { - 1 } ( U ) \subseteq X$ is open.
Definition 3.1.12 (Cover)
A collection of subsets $\{ U _ { \alpha } \}$ of X is said to cover X iff $X = \cup _ { \alpha } U _ { \alpha }$ If $A \subseteq X$ is a subspace,
then this collection covers A iff $A \subseteq \cup _ { \alpha } U _ { \alpha }$
```

## Definition 3.1.13 (Dense)

A subspace $Q \subset X$ is dense iff every neighborhood of every point in x intersects Q. Equivalently, $\operatorname { c l } _ { X } ( Q ) = Q$

## Definition 3.1.14 (First Countable)

A space is first-countable iff every point admits a countable neighborhood basis.

## Definition 3.1.15 (Hausdorff)

A topological space X is Hausdorff iff points can be separated by disjoint neighborhoods: for every $p \neq q \in X$ there exist disjoint open sets $U \ni p$ and $V \ni q$

## Definition 3.1.16 (Injection)

A map $\iota : A  B$ with a left inverse $f : B  A$ satisfying $f \circ \iota = \operatorname { i d } _ { A }$ . Note that this is equivalent to $f ( x ) = f ( y ) \implies x = y .$

## Definition 3.1.17 (Lebesgue Number)

For $( X , d )$ a compact metric space and $\{ U _ { \alpha } \} \ni X$ , there exists a Lebesgue number $\delta _ { L } > 0$ which satisfies

$$
A \subset X , \ \mathrm { d i a m } ( A ) < \delta _ { L } \implies A \subseteq U _ { \alpha } { \mathrm { ~ f o r ~ s o m e ~ } } \alpha .
$$

## Definition 3.1.18 (Limit Point)

For $A \subset X$ , x is a limit point of A if every punctured neighborhood $P _ { x }$ of x intersects A. I.e., every neighborhood of x intersects A at a point other than x. Equivalently, $x \in \operatorname { c l } _ { X } ( A \setminus \{ x \} )$

## Definition 3.1.19 (Locally Connected)

A space is locally connected iff every neighborhood of every point admits a smaller connected neighborhood. I.e. for all $x \in X$ , for all $N _ { x } \ni x$ there exists a connected set $U \subset X$ with $x \in U$

## Definition 3.1.20 (Locally Compact)

A space X is locally compact iff every $x \in X$ has a neighborhood contained in a compact subset of X.

Note: authors such as Hartshorne often also require that X is Hausdorff, and refer to the above definition as quasicompactness.

## Definition 3.1.21 (Locally Finite)

A collection of subsets S of X is locally finite iff each point of M has a neighborhood that intersects at most finitely many elements of S.

## Definition 3.1.22 (Locally Path-Connected)

A space X is locally path-connected iff every point in X admits some path-connected neighborhood. Equivalently, X admits a basis of path-connected open subsets.

Definition 3.1.23 (Neighborhood)   
A neighborhood of a point x is any open set containing x.

Definition 3.1.24 (Normal)   
A space is normal if any two disjoint closed subsets can be separated by neighborhoods.

$$
p \in X
$$

$$
p ,
$$

$$
N _ { p } \supseteq B
$$

$$
B _ { p }
$$

$$
\boldsymbol { B } \in \boldsymbol { B } _ { p }
$$

$$
p
$$

$$
N _ { p }
$$

Definition 3.1.26 (Open and Closed Maps)   
A map $f : X \to Y$ is an open map (respectively a closed map) if and only if whenever   
$U \subseteq X$ is open (resp. closed), f (U ) is again open (resp. closed)>

Definition 3.1.27 (Paracompact)   
A topological space X is paracompact iff every open cover of X admits an open locally finite   
refinement.

Definition 3.1.28 (Quotient Map)   
A map q : X → Y is a quotient map if and only if   
1. q is surjective, and   
2. $U \subseteq Y$ is open if and only if $q ^ { - 1 } ( U )$ is open.

Definition 3.1.29 (Path Connected)   
A space X is path connected if and only if for every pair of points x $\neq y$ there exists a   
continuous map $f : I \to X$ such that $f ( 0 ) = x$ and $f ( 1 ) = y$

Definition 3.1.30 (Path Components)   
Set $x \sim y$ iff there exists a path-connected set $U \ni x , y$ and take equivalence classes.

$$
A \subseteq X
$$

$$
x ( A )
$$

Definition 3.1.32 (Product topology)   
$( X , \tau _ { X } )$ $( Y , \tau _ { Y } )$ topological spaces, defining   
$\tau _ { X \times Y } : = \left\{ U \times V ~ \middle | ~ U \in \tau _ { X } , V \in \tau _ { Y } \right\}$   
yields the product topology on $X \times Y$

Definition 3.1.33 (Quasicompact)   
A topological space X (possible non-Hausdorff) is quasi-compact iff every open cover admits   
a finite subcover. If X is additionally Hausdorff, X is said to be compact.   
Note: this is a distinction coming from algebraic   
geometry, and Hartshorne in particular.

## Definition 3.1.34 (Refinement)

A cover $\nu \Longrightarrow X$ is a refinement of $u \stackrel { } { \to } X$ iff for each $V \in \mathcal V$ there exists a $U \in \mathcal { U }$ such that $V \subseteq U .$

## Definition 3.1.35 (Regular)

A space X is regular if whenever $x \in X$ and $F \nsupseteq$ x is closed, F and x are separated by neighborhoods.

## Definition 3.1.36 (Retract)

A map r in $A \underset {   \ l _ { r } }  ^ { \iota } B$ satisfying

$$
r \circ \iota = \operatorname { i d } _ { A } .
$$

A retract of B onto a subspace A is a map $r : B  A$ that is a left-inverse for the inclusion $f : A \hookrightarrow B ,$ so $r \circ f = \operatorname { i d } _ { A } { \mathrm { : } }$

$$
\operatorname { i d } _ { A } \operatorname { \longrightarrow } A { \xrightarrow { \operatorname { z ^ { \operatorname { z ^ { -- } } } } { \overset { \operatorname { r } } { \operatorname { f } } } \cdots \operatorname { \mu } } } B
$$

## Link to (partial) Diagram

Equivalently, a continuous map $r : B  A$ with $r | _ { A } = \operatorname { i d } _ { A }$ restricting to the identity on A, i.e. fixing A pointwise. Note that r is necessarily a surjection.

Alt: Let X be a topological space and $A \subset X$ be a subspace, then a retraction of X onto A is a map $r : X \to X$ such that the image of X is A and r restricted to A is the identity.

Remark 3.1.37: If X retracts onto A with $\iota : A \hookrightarrow X$ , then i∗ is injective. Any nonempty space retracts to a point via a constant map.

## Definition 3.1.38 (Saturated)

A subset $U \subseteq X$ is saturated with respect to a surjective map $p : X \to Y$ if and only if whenever $U \cap p ^ { - 1 } ( y ) = V \neq \emptyset$ , we have $V \subseteq U .$ , i.e. U contains every set $p ^ { - 1 } ( y )$ that it intersects. Equivalently, U is the complete inverse image of a subset of Y .

## Definition 3.1.39 (Separable spaces)

A space X is separable iff X contains a countable dense subset.

## Definition 3.1.40 (Second Countable)

A space is second-countable iff it admits a countable basis.

## Definition 3.1.41 (The subspace topology)

For $( X , \tau )$ a topological space and $U \subseteq X$ an arbitrary subset, the space $( U , \tau _ { U } )$ is a topological space with a subspace topology defined by

$$
\tau _ { U } : = \left\{ Y \cap U \ \middle | \ U \in \tau \right\} .
$$

Definition 3.1.42 (Surjection)

A map π with a right inverse f satisfying

$$
\pi \circ f = \operatorname { i d }
$$

Definition 3.1.43 $( T _ { n }$ Spaces (Separation Axioms))

$T _ { 0 } { \mathrm { : } }$ Points are distinguishable. For any 2 points $x _ { 1 } \neq x _ { 2 }$ , at least one $x _ { i } \ ( \operatorname { s a y } x _ { 1 } )$ admits a neighborhood not containing x2.

$T _ { 1 } { \mathrm { : } }$ For any 2 points, both admit neighborhoods not containing the other. Equivalently, points are closed.

• $T _ { 2 } { \mathrm { : } }$ For any 2 points, both admit disjoint separating neighborhoods.

• $T _ { 2 . 5 }  \} :$ For any 2 points, both admit disjoint closed separating neighborhoods.

$T _ { 3 } \colon \ T _ { 0 }$ & regular. Given any point x and any closed $F \nsupseteq x$ , there are neighborhoods separating F and x.

$T _ { 3 . 5 } \colon \ { T } _ { 0 }$ & completely regular. Any point x and closed F 63 x can be separated by a continuous function.

$T _ { 4 } \colon T _ { 1 }$ & normal. Any two disjoint closed subsets can be separated by neighborhoods.

## Example 3.1.44(Counterexamples for separation axioms):

• Not $T _ { 0 } { \mathrm { : } }$ the space $\left\{ f : \mathbb { R } \to \mathbb { C } \ \Big | \ \int _ { \mathbb { R } } | f | ^ { 2 } < \infty \right\}$ , since two a.e. equal functions aren’t distinguishable (they have precisely the same set of neighborhoods).

$T _ { 1 }$ but not $T _ { 0 } { \mathrm { : } }$ Spec R for R ∈ CRing with the Zariski topology. There are points that aren’t closed: Spec R \ mSpec R.

Definition 3.1.45 (Topology)

• Using open sets: closed under arbitrary unions and finite intersections.

• Using closed sets: closed under arbitrary intersections and finite unions.

## Remark 3.1.46: A mnemonic: in R, $\cap _ { n \in \mathbb { N } } ( - 1 / n , 1 / n ) = \{ 0 \}$ which is closed in R.

Definition 3.1.47 (Topological Embedding)

A topological embedding is a continuous map $f : X \to Y$ which is a homeomorphism onto its image, i.e. $X \cong _ { \mathsf { T o p } } f ( X )$

Definition 3.1.48 (Uniform Continuity)

For $f : ( X , d _ { x } )  ( Y , d _ { Y } )$ metric spaces,

$$
\forall \varepsilon > 0 , \ \exists \delta > 0 \ \mathrm { s u c h \ t h a t } \quad d _ { X } ( x _ { 1 } , x _ { 2 } ) < \delta \implies d _ { Y } ( f ( x _ { 1 } ) , f ( x _ { 2 } ) ) < \varepsilon .
$$

## 3.2 Algebraic Topology

Definition 3.2.1 (Acyclic)

Definitions

Definition 3.2.2 (Alexander duality)

Definitions

Definition 3.2.3 (Basis of a module)

For an R-module M, a basis B is a linearly independent generating set.

Definition 3.2.4 (Boundary)

Definitions

Definition 3.2.5 (Boundary of a manifold)

Points $x \in M ^ { n }$ defined by

$$
\partial M = \{ x \in M : H _ { n } ( M , M - \{ x \} ; \mathbb { Z } ) = 0 \}
$$

Definition 3.2.6 (Cap Product)

Denoting $\Delta ^ { p } \overset { \sigma } {  } X \in C _ { p } ( X ; G )$ , a map that sends pairs (p-chains, q-cochains) to $( p - q )$ -chains $\Delta ^ { p - q }  X$ by

$$
\begin{array} { r l r } & { } & { H _ { p } ( X ; R ) \times H ^ { q } ( X ; R ) \widehat { \longrightarrow } H _ { p - q } ( X ; R ) } \\ & { } & { \sigma \frown \psi = \psi ( F _ { 0 } ^ { q } ( \sigma ) ) F _ { q } ^ { p } ( \sigma ) } \end{array}
$$

where $F _ { i } ^ { j }$ is the face operator, which acts on a simplicial map σ by restriction to the face spanned by $[ v _ { i } \dots v _ { j } ] , \mathrm { i . e . \ } F _ { i } ^ { j } ( \sigma ) = \sigma | _ { [ v _ { i } \dots v _ { j } ] } .$

Definition 3.2.7 (Cellular Homology)

Definitions

Definition 3.2.8 (Cellular Map)

A map $X ~ { \stackrel { f } { \to } } ~ Y$ is said to be cellular if $f ( X ^ { ( n ) } ) \subseteq Y ^ { ( n ) }$ where $X ^ { ( n ) }$ denotes the n- skeleton.

Definition 3.2.9 (Chain)

An element $c \in C _ { p } ( X ; R )$ can be represented as the singular p simplex $\Delta ^ { p }  X$

## Definition 3.2.10 (Chain Homotopy)

Given two maps between chain complexes $\left( C _ { * } , \partial _ { C } \right) \xrightarrow { f , g } \left( D _ { * } , \partial _ { D } \right)$ , a chain homotopy is a family $h _ { i } : C _ { i }  B _ { i + 1 }$ satisfying

$$
f _ { i } - g _ { i } = \partial _ { B , i - 1 } \circ h _ { n } + h _ { i + 1 } \circ \partial _ { A , i }
$$

Definition 3.2.11 (Chain Map)

A map between chain complexes $( C _ { * } , \partial _ { C } ) \ \stackrel { f } { \to } \ ( D _ { * } , \partial _ { D } )$ is a chain map iff each component $C _ { i } \xrightarrow { f _ { i } } D _ { i }$ satisfies

$$
f _ { i - 1 } \circ \partial _ { C , i } = \partial _ { D , i } \circ f _ { i }
$$

(i.e this forms a commuting ladder)

Definition 3.2.12 (Closed manifold)

A manifold that is compact, with or without boundary.

Definition 3.2.13 (Coboundary)

## Definitions

Definition 3.2.14 (Cochain)

An cochain $c \in C ^ { p } ( X ; R )$ is a map $c \in \hom ( C _ { p } ( X ; R ) , R )$ on chains.

Definition 3.2.15 (Cocycle)

## Definitions

## Definition 3.2.16 (Constant Map)

A constant map $f : X \to Y { \mathrm { ~ i f f ~ } } f ( X ) = y _ { 0 }$ for some $y _ { 0 } \in Y$ , i.e. for every $x \in X$ the output value $f ( x ) = y _ { 0 }$ is the same.

## Definition 3.2.17 (Colimit)

For a directed system $( X _ { i } , f _ { i j }$ , the colimit is an object X with a sequence of projections $\pi _ { i } : X  X _ { i }$ such that for any Y mapping into the system, the following diagram commutes:

<!-- image-->

Example 3.2.18(of colimits):

• Products

• Pullbacks

• Inverse / projective limits

• The p-adic integers $\mathbb { Z } _ { p }$

## Definition 3.2.19 (Contractible)

A space X is contractible if $\operatorname { i d } _ { X }$ is nullhomotopic. i.e. the identity is homotopic to a constant map $c ( x ) = x _ { 0 }$

Equivalently, X is contractible if $X \simeq \{ x _ { 0 } \}$ is homotopy equivalent to a point. This means that there exists a mutually inverse pair of maps $f : X  \{ x _ { 0 } \}$ and $g : \{ x _ { 0 } \} \to X$ such that $f \circ g \simeq \operatorname { i d } _ { \{ x _ { 0 } \} }$ and $g \circ f \simeq \operatorname { i d } _ { X }$ a

aThis is a useful property because it supplies you with a homotopy.

Definition 3.2.20 (Coproduct)

## Definitions

## Definition 3.2.21 (Covering Space)

A covering space of X is the data $p : \tilde { X } \to X$ such that

1. Each $x \in X$ admits a neighborhood U such that $p ^ { - 1 } ( U )$ is a union of disjoint open sets in ${ \tilde { V } } _ { i } \subseteq X$ (the sheets of X˜ over U),

2. $p | _ { V _ { i } } : V _ { i }  U$ is a homeomorphism for each sheet.

An isomorphism of covering spaces ${ \tilde { X } } _ { 1 } \cong { \tilde { X } } _ { 2 }$ is a commutative diagram

<!-- image-->  
Link to diagram

Definition 3.2.22 (Cup Product)   
A map taking pairs (p-cocycles, q-cocycles) to $( p + q )$ -cocyles by   
Hp(X; R) × Hq(X; R) ^−→ Hp+q(X; R)   
(a ∪ b)(σ) = a(σ ◦ Ip0 ) b(σ ◦ Ip+qp )   
where $\Delta ^ { p + q } \stackrel { \sigma } {  } X$ is a singular $p + q$ simplex and   
I ji : [i, · · · , j] ,→ ∆p+q .   
is an embedding of the (j − i)-simplex into a $( p + q )$ -simplex.

Example 3.2.23(Applications of the cup product): On a manifold, the cup product is Poincaré dual to the intersection of submanifolds. Also used to show $T ^ { 2 } \not \simeq S ^ { 2 } \vee S ^ { 1 } \vee S ^ { \bar { 1 } }$

Definition 3.2.24 (CW Complex)

Definition 3.2.25 (CW Cell)   
An n-cell of X, say $e ^ { n }$ , is the image of a map $\Phi : B ^ { n } \to X$ . That is, $e ^ { n } = \Phi ( B ^ { n } )$ . Attaching   
an n-cell to X is equivalent to forming the space $B ^ { n } \coprod X$ where $f : \partial B ^ { n } \to X$   
• A 0-cell is a point.   
• A 1-cell is an interval $[ - 1 , 1 ] \ = \ B ^ { 1 } \ \subset \ \mathbb { R } ^ { 1 }$ Attaching requires a map from $S ^ { 0 } =$   
$\{ - 1 , + 1 \} \to X$   
• A 2-cell is a solid disk $B ^ { 2 } \subset \mathbb { R } ^ { 2 }$ in the plane. Attaching requires a map $S ^ { 1 } \to X$   
• A 3-cell is a solid ball $B ^ { 3 } \subset \mathbb { R } ^ { 3 }$ Attaching requires a map from the sphere $S ^ { 2 } \to X$

Definition 3.2.26 (Cycle)

## Definitions

Definition 3.2.27 (Deck transformation)

For a covering space $\tilde { X } \ { \stackrel { p } { \to } } \ X$ , self-isomorphisms $f : { \tilde { X } }  { \tilde { X } }$ of covering spaces are referred to as deck transformations.

Definition 3.2.28 (Deformation)

## Definitions

Definition 3.2.29 (Deformation Retract)

A map r in $A \underset {  - \ l _ { r } } {  } { } $ X that is a retraction (so $r \circ \iota = \operatorname { i d } _ { A } )$ that also satisfies $\iota \circ r \simeq \operatorname { i d } _ { X }$

Note that this is equality in one direction, but only homotopy equivalence in the other.

Equivalently, a map $F : I \times X \to X$ such that

$$
F _ { 0 } ( x ) = \operatorname { i d } _ { X } F _ { t } ( x ) \mid _ { A }
$$

$$
= \operatorname { i d } _ { A } F _ { 1 } ( X ) = A .
$$

Alt:

A deformation retract is a homotopy $H : X \times I  X$ from $\operatorname { i d } _ { X }$ to $\operatorname { i d } _ { A }$ where $H | _ { A } = \operatorname { i d } _ { A }$ fixes A at all times.

$$
H : X \times I  X
$$

$$
H ( x , 0 ) = \operatorname { i d } _ { X }
$$

$$
H ( x , 1 ) = \operatorname { i d } _ { A }
$$

$$
x \in A \implies H ( x , t ) \in A \quad \forall t
$$

Remark 3.2.30: A deformation retract between a space and a subspace is a homotopy equivalence, and further $X \simeq Y$ iff there is a Z such that both X and Y are deformation retracts of Z. Moreover, if A and B both have deformation retracts onto a common space $X ,$ , then $A \simeq B$

## Definition 3.2.31 (Degree of a Map of Spheres)

Given any $f : S ^ { n } \to S ^ { n }$ , there are induced maps on homotopy and homology groups. Taking $f ^ { * } : H ^ { n } ( S ^ { n } )  H ^ { n } ( S ^ { n } )$ and identifying $H ^ { n } ( S ^ { n } ) \cong \mathbb { Z }$ we have $f ^ { * } : \mathbb { Z } \to \mathbb { Z }$ But homomorphisms of free groups are entirely determined by their action on generators. So if $f ^ { * } ( 1 ) = n$ define n to be the degree of $f .$

Definition 3.2.32 (Derived Functor)

For a functor T and an R-module A, a left derived functor $\left( L _ { n T } \right)$ is defined as $h _ { n } ( T P _ { A } )$ , where $P _ { A }$ is a projective resolution of A.

Definition 3.2.33 (Dimension of a manifold)

For $x \in M ,$ the only nonvanishing homology group $H _ { i } ( M , M - \{ x \} ; \mathbb { Z } )$

Definition 3.2.34 (Direct Limit)

Definitions

Definition 3.2.35 (Direct Product)

Definitions

Definition 3.2.36 (Direct Sum)

Definitions

## Definition 3.2.37 (Euler Characteristic)

## Definitions

## Definition 3.2.38 (Exact Functor)

A functor T is right exact if a short exact sequence

$$
0  A  B  C  0
$$

yields an exact sequence

$$
\dots T A \to T B \to T C \to 0
$$

and is left exact if it yields

$$
0 \to T A \to T B \to T C \to . . .
$$

Thus a functor is exact iff it is both left and right exact, yielding

$$
0  T A  T B  T C  0 .
$$

Example 3.2.39(of an exact functor): − $\mathbf { \nabla } - \otimes _ { R } -$ is a right exact bifunctor.

Definition 3.2.40 (Exact Sequence)

Definitions

Definition 3.2.41 (Excision)

Definitions

Definition 3.2.42 (Ext Group)

Definitions

## Definition 3.2.43 (Flat)

An R-module is flat if $A \otimes _ { R } -$ is an exact functor.

## Definition 3.2.44 (Free and Properly Discontinuous)

An action $G \cap X$ is properly discontinuous if each $x \in X$ has a neighborhood U such that all of the images $g ( U )$ for $g \in G$ are disjoint, i.e. $g _ { 1 } ( U ) \cap g _ { 2 } ( U ) \neq \emptyset \implies g _ { 1 } = g _ { 2 }$ . The action

is free if there are no fixed points.

Sometimes a slightly weaker condition is used: every point $x \in X$ has a neighborhood U such that $U \cap G ( U ) \neq \emptyset$ for only finitely many G.

Definitions

Definition 3.2.45 (Free module)

A -module M with a basis $S = \{ s _ { i } \}$ of generating elements. Every such module is the image of a unique map ${ \mathcal { F } } ( S ) = R ^ { S } \twoheadrightarrow M$ , and if $M =  S | \mathcal { R } $ for some set of relations R, then $M \cong R ^ { S } / \mathcal { R }$

Definition 3.2.46 (Free Product)

Definitions

Definition 3.2.47 (Free product with amalgamation)

Definitions

Definition 3.2.48 (Fundamental Class)

For a connected, closed, orientable manifold, [M] is a generator of $H _ { n } ( M ; \mathbb { Z } ) = \mathbb { Z } .$

Definition 3.2.49 (Fundamental Group)

Definitions

Definition 3.2.50 (Generating Set)

$S = \{ s _ { i } \}$ is a generating set for an R- module M iff

$$
x \in M \implies x = \sum r _ { i } s _ { i }
$$

for some coefficients $r _ { i } \in R$ (where this sum may be infinite).

Definition 3.2.51 (Gluing Along a Map)

Definitions

Definition 3.2.52 (Group Ring)

Definitions

Definition 3.2.53 (Homologous)

Definition 3.2.54 (Homotopic)

Definitions

Definition 3.2.55 (Homotopy)   
Let X, Y be topological spaces and $f , g : X \to Y$ continuous maps. Then a homotopy from   
f to g is a continuous function   
F : X × I → Y   
such that   
F (x, 0) = f (x) and F (x, 1) = g(x)   
for all x ∈ X. If such a homotopy exists, we write f ' g. This is an equivalence relation on   
Hom(X, Y ), and the set of such classes is denoted $[ X , Y ] : = \hom ( X , Y ) / \simeq$

Definition 3.2.56 (Homotopy Class)

Definition 3.2.57 (Homotopy Equivalence)   
Let f : X → Y be a continuous map, then f is said to be a homotopy equivalence if there   
exists a continuous map g : X → Y such that   
f ◦ g ' idY and g ◦ f ' idX .   
Such a map g is called a homotopy inverse of f, the pair of maps is a homotopy equivalence.   
If such an f exists, we write X ' Y and say X and Y have the same homotopy type, or that   
they are homotopy equivalent.   
Note that homotopy equivalence is strictly weaker   
than homeomorphic equivalence, i.e., X ∼= Y im  
plies X ' Y but not necessarily the converse.

Definition 3.2.58 (Homotopy Extension Property)

Definitions

Definition 3.2.59 (Homotopy Groups)

Definitions

Definition 3.2.60 (Homotopy Lifting Property)

Definitions

## Definition 3.2.61 (Intersection Pairing)

For a manifold M, a map on homology defined by

$$
{ \cal H } _ { \widehat i } { \cal M } \otimes { \cal H } _ { \widehat j } { \cal M } \to { \cal H } _ { \widehat { i + j } } X
$$

$$
\alpha \otimes \beta \mapsto \langle \alpha , \beta \rangle
$$

obtained by conjugating the cup product with Poincaré Duality, i.e.

$$
\langle \alpha , \beta \rangle = [ M ] \frown ( [ \alpha ] ^ { \check { \mathbf { \alpha } } } \smile [ \beta ] ) .
$$

Then, if [A], [B] are transversely intersecting submanifolds representing $\alpha , \beta ,$ , then

$$
\langle \alpha , \beta \rangle = [ A \cap B ]
$$

$\operatorname { I f } { \widehat { i } } = j$ then $\left. \alpha , \beta \right. \in H _ { 0 } M = \mathbb { Z }$ is the signed number of intersection points.

Alt: The pairing obtained from dualizing Poincare Duality to obtain

$$
\operatorname { F } ( H _ { i } M ) \otimes \operatorname { F } ( H _ { n - i } M ) \to \mathbb { Z }
$$

Computed as an oriented intersection number between two homology classes (perturbed to be transverse).

## Definition 3.2.62 (Inverse Limit)

## Definitions

## Definition 3.2.63 (Intersection Form)

The nondegenerate bilinear form cohomology induced by the Kronecker Pairing:

$$
I : H ^ { k } ( M _ { n } ) \times H ^ { n - k } ( M ^ { n } ) \to \mathbb { Z }
$$

where $n = 2 k$ .

• When k is odd, I is skew-symmetric and thus a symplectic form.

• When k is even (and thus $n \equiv 0$ (mod 4)) this is a symmetric form.

• Satisfies $I ( x , y ) = ( - 1 ) ^ { k ( n - k ) } I ( y , x )$

## Definition 3.2.64 (Kronecker Pairing)

A map pairing a chain with a cochain, given by

$$
{ \begin{array} { r } { H ^ { n } ( X ; R ) \times H _ { n } ( X ; R ) \to R } \\ { ( [ \psi , \alpha ] ) \mapsto \psi ( \alpha ) } \end{array} }
$$

which is a nondegenerate bilinear form.

Definition 3.2.65 (Kronecker Product)

Definitions

Definition 3.2.66 (Lefschetz duality)

Definitions

Definition 3.2.67 (Lefschetz Number)

Definitions

Definition 3.2.68 (Lens Space)

Definitions

Definition 3.2.69 (Local Degree)

At a point $x \in V \subset M$ , a generator of $H _ { n } ( V , V - \{ x \} )$ . The degree of a map $S ^ { n } \to S ^ { n }$ is the sum of its local degrees.

Definition 3.2.70 (Local Orientation)

Definitions

Definition 3.2.71 (Limit)

Definitions

## Definition 3.2.72 (Linear Independence)

A generating S for a module M is linearly independent if $\sum { r _ { i } s _ { i } } = 0 _ { M } \implies \forall i , \ r _ { i } = 0$ where $s _ { i } \in S , r _ { i } \in R .$

Definition 3.2.73 (Local homology)

$H _ { n } ( X , X - A ; \mathbb { Z } )$ is the local homology at A, also denoted $H _ { n } ( X \mid A )$

Definition 3.2.74 (Local orientation of a manifold)

At a point $x \in M ^ { n }$ , a choice of a generator $\mu _ { x }$ of $H _ { n } ( M , M - \{ x \} ) = \mathbb { Z } .$

Definition 3.2.75 (Long exact sequence)

Definitions

## Definition 3.2.76 (Manifold)

An n-manifold is a Hausdorff space in which each neighborhood has an open neighborhood homeomorphic to $\mathbb { R } ^ { n }$

## Definition 3.2.77 (Manifold with boundary)

A manifold in which open neighborhoods may be isomorphic to either $\mathbb { R } ^ { n }$ or a half-space   
$\left\{ \mathbf { x } \in \mathbb { R } ^ { n } \mid x _ { i } > 0 \right\}$

Definition 3.2.78 (Mayer-Vietoris Sequence)

Definitions

Definition 3.2.79 (Monodromy)

Definitions

Definition 3.2.80 (N-cell)

Definitions

Definition 3.2.81 (N-connected)

Definitions

## Definition 3.2.82 (Normal covering space (a.k.a. ’regular’))

A covering space is normal if and only if for every $x \in X$ and every pair of lifts ${ \tilde { x } } _ { 1 } , { \tilde { x } } _ { 2 }$ , there is a deck transformation f such that $f ( \tilde { x } _ { 1 } ) = \tilde { x } _ { 2 }$

## Definition 3.2.83 (Nullhomotopic)

A map $X ~ { \stackrel { f } { \to } } ~ Y$ is nullhomotopic if it is homotopic to a constant map $X \ { \overset { g } { \to } } \ \{ y _ { 0 } \}$ ; that is, there   
exists a homotopy

$$
F : X \times I  Y
$$

$$
\begin{array} { r } { F | _ { X \times \{ 0 \} } = f \quad F ( x , 0 ) = f ( x ) } \end{array}
$$

$$
\begin{array} { r } { F | _ { X \times \{ 1 \} } = g \quad F ( x , 1 ) = g ( x ) = y _ { 0 } } \end{array}
$$

If f is homotopic to a constant map, say $f : x \mapsto y _ { 0 }$ for some fixed $y _ { 0 } \in Y$ , then f is said to be nullhomotopic. In other words, if $f : X \to Y$ is nullhomotopic, then there exists a homotopy $H : X \times I  Y$ such that $H ( x , 0 ) = f ( x )$ and $H ( x , 1 ) = y _ { 0 }$ Note that constant maps (or anything homotopic) induce zero homomorphisms.

Definition 3.2.84 (Orbit space)   
For a group action $G \cap X$ , the orbit space $X / G$ is defined as $X /$ ∼ where ∀x, $y \in X , x \sim$   
$y \iff \exists g \in G \ | \ g . x = y .$

Definition 3.2.85 (Orientable manifold)   
A manifold for which an orientation exists, see “Orientation of a Manifold”.

Definition 3.2.86 (Orientation cover)   
For any manifold M, a two sheeted orientable covering space $\tilde { M } _ { o }$ M is orientable iff $\tilde { M }$ is   
disconnected. Constructed as   
$\tilde { M } = \coprod _ { x \in M } \left\{ \mu _ { x } \big | \mu _ { x } \right.$ is a local orientation $\Bigg \}$

Definition 3.2.87 (Orientation of a manifold)   
A family of $\{ \mu _ { x } \} _ { x \in M }$ with local consistency: if $x , y \in U$ then $\mu _ { x } , \mu _ { y }$ are related via a propaga  
tion.   
Formally, a function   
$M ^ { n } \to \coprod _ { x \in M } H ( X \mid \{ x \} )$   
$x \mapsto \mu _ { x }$   
such that $\forall x \exists N _ { x }$ in which $\forall y \in N _ { x } ,$ the preimage of each $\mu _ { y }$ under the map $H _ { n } ( M \mid N _ { x } ) $   
$H _ { n } ( M \mid y )$ is a single generator $\mu N _ { x }$   
TFAE:   
• M is orientable.   
The map $W : ( M , x ) \to \mathbb { Z } _ { 2 }$ is trivial.   
$\tilde { M } _ { o } = M \coprod \coprod \mathbb { Z } _ { 2 }$ (two sheets).   
$\tilde { M } _ { o }$ is disconnected   
• The projection $\tilde { M } _ { o }  M$ admits a section.

Definition 3.2.88 (Oriented manifold)

Definitions

Definition 3.2.89 (Path)

Definitions

Definition 3.2.90 (Path Lifting Property)

Definitions

Definition 3.2.91 (Perfect Pairing)

A pairing alone is an R-bilinear module map, or equivalently a map out of a tensor product since $p : M \otimes _ { R } N \to L$ can be partially applied to yield $\varphi : M \to L ^ { N } = \hom _ { R } ( N , L )$ . A pairing is perfect when $\varphi$ is an isomorphism.

Definition 3.2.92 (Poincaré Duality)

For a closed, orientable n-manifold, following map $[ M ] \frown -$ is an isomorphism:

$$
D : H ^ { k } ( M ; R ) \to H _ { n - k } ( M ; R )
$$

$$
D ( \alpha ) = [ M ] \frown \alpha
$$

Definition 3.2.93 (Projective Resolution)

Definitions

Definition 3.2.94 (Properly Discontinuous)

Definitions

Definition 3.2.95 (Pullback)

Definitions

Definition 3.2.96 (Pushout)

Definitions

Definition 3.2.97 (Quasi-isomorphism)

Definitions

Definition 3.2.98 (R-orientability)

Definitions

Definition 3.2.99 (Relative boundaries)

Definitions

Definition 3.2.100 (Relative cycles)

Definition 3.2.101 (Relative homotopy groups)

Definition 3.2.102 (Semilocally Simply Connected)   
A space X is semilocally simply connected if every x $\in X$ has a neighborhood U such that   
U ,→ X induces the trivial map $\pi _ { 1 } ( U ; x ) \to \pi _ { 1 } ( X , x )$

```latex
Definition 3.2.104 (Simplicial Complex)
Given a simplex $\sigma = [ v _ { 1 } \cdot \cdot \cdot v _ { n } ]$ define the face map
$\partial _ { i } : \Delta ^ { n } \to \Delta ^ { n - 1 }$
$\sigma \mapsto \left[ v _ { 1 } \cdot \cdot \cdot \widehat { v } _ { i } \cdot \cdot \cdot v _ { n } \right]$
A simplicial complex is a set K satisfying
1. $\sigma \in K \implies \partial _ { i } \sigma \in K .$
2. $\sigma , \tau \in { \cal K } \Longrightarrow \sigma \cap \tau = \emptyset , \ \partial _ { i } \sigma ,$ or $\partial _ { i } \tau .$
This amounts to saying that any collection of $( n { - } 1 )$ -simplices uniquely determines an n-simplex
(or its lack thereof), or that that map $\Delta ^ { k }  X$ is a continuous injection from the standard
simplex in $\mathbb { R } ^ { n }$
3. $| K \cap B _ { \varepsilon } ( \sigma ) | < \infty$ for every $\sigma \in K ,$ , identifying $\sigma \subseteq \mathbb { R } ^ { n }$
Definition 3.2.105 (Simplicial Map)
For a map
$K { \stackrel { f } { \to } } L$
between simplicial complexes, $f$ is a simplicial map if for any set of vertices $\{ v _ { i } \}$ spanning a
simplex in $K ,$ the set $\{ f ( v _ { i } ) \}$ are the vertices of a simplex in $L .$
Definition 3.2.106 (Simply Connected)
A space X is simply connected if and only if X is path-connected and every loop $\gamma : S ^ { 1 } \to X$
can be contracted to a point.
Equivalently, there exists a lift ${ \widehat { \gamma } } : D ^ { 2 } \to X$ such that $\widehat \gamma | _ { \partial D ^ { 2 } } = \gamma .$
Equivalently, for any two paths $p _ { 1 } , p _ { 2 } : I \to X$ bsuch that $p _ { 1 } ( 0 ) = p _ { 2 } ( 0 )$ and $p _ { 1 } ( 1 ) = p _ { 2 } ( 1 )$ there
exists a homotopy $F : I ^ { 2 } \to X$ such that $\left. F \right| _ { 0 } = p _ { 1 } , \left. F \right| _ { 0 } = p _ { 2 } .$
```

Equivalently, $\pi _ { 1 } X = 1$ is trivial.

Definition 3.2.107 (Singular Chain)

$$
x \in C _ { n } ( x ) \implies X = \sum _ { i } n _ { i } \sigma _ { i } = \sum _ { i } n _ { i } \bigl ( \Delta ^ { n } \xrightarrow { \sigma _ { i } } X \bigr ) .
$$

Definition 3.2.108 (Singular Cochain)

$$
x \in C ^ { n } ( x ) \implies X = \sum _ { i } n _ { i } \psi _ { i } = \sum _ { i } n _ { i } ( \sigma _ { i } \xrightarrow { \psi _ { i } } X ) .
$$

Definition 3.2.109 (Singular Homology)

Definitions

Definition 3.2.110 (Tor Group)

For an R-module

$$
\operatorname { T o r } _ { R } ^ { n } ( - , B ) = L _ { n } ( - \otimes _ { R } B ) ,
$$

where $L _ { n }$ denotes the nth left derived functor.

Definition 3.2.111 (Universal Cover)

Definitions

Definition 3.2.112 (Weak Homotopy Equivalence)

Definitions

Definition 3.2.113 (Weak Topology)

Definitions

Definition 3.2.114 (Wedge Product)

Definitions

## 3.3 Homotopy

## Definition 3.3.1 (Cone)

For a space X, defined as

$$
C X = \frac { X \times I } { X \times \{ 0 \} } .
$$

Example: The cone on the circle $C S ^ { 1 }$

Note that the cone embeds X in a contractible space CX.

## Definition 3.3.2 (Suspension)

Compact represented as $\Sigma { \cal { X } } = { \cal { C } } { \cal { X } } \prod _ { \mathrm { i d } _ { \cal { X } } } { \cal { C } } { \cal { X } } .$ , two cones on X glued along X. Explicitly given by

$$
\Sigma X = \frac { X \times I } { ( X \times \{ 0 \} ) \cup ( X \times \{ 1 \} ) \cup ( \{ x _ { 0 } \} \times I ) } .
$$

Definition 3.3.3 (Smash Product)

Definitions

Definition 3.3.4 (Moore Space)

Definitions

Definition 3.3.5 (Mapping Cone)

Definitions

Definition 3.3.6 (Mapping Cylinder)

Definitions

Definition 3.3.7 (Mapping Path Space)

Definitions

Definition 3.3.8 (Loop Space)

Definitions

Definition 3.3.9 (Eilenberg-MacLane Space)

Definitions

## Examples

## 4.1 Point-Set

## 4.1.1 Common Spaces and Operations

Example 4.1.1(Nice spaces): The following are some standard “nice” spaces:

$$
S ^ { n } , \mathbb { D } ^ { n } , T ^ { n } , \mathbb { R P } ^ { n } , \mathbb { C P } ^ { n } , \mathbb { M } , \mathbb { K } , \Sigma _ { g } , \mathbb { R P } ^ { \infty } , \mathbb { C P } ^ { \infty } .
$$

Example 4.1.2(A bank of counterexamples): The following are useful spaces to keep in mind to furnish counterexamples:

• Finite discrete sets with the discrete topology.

• Subspaces of R: $( a , b ) , ( a , b ] , ( a , \infty )$ , etc.

– Sets given by real sequences, such as $\{ 0 \} \cup \left\{ { \frac { 1 } { n } } \mid n \in \mathbb { Z } ^ { \geq 1 } \right\}$

Q

• The topologist’s sine curve

• One-point compactifications

$\mathbb { R } ^ { \omega }$ for ω the least uncountable ordinal (?)

• The Hawaiian earring

• The Cantor set

Examples of some more exotic spaces that show up less frequently:

$\mathrm { H P } ^ { n }$ , quaternionic projective space

• The Dunce Cap

• The Alexander Horned sphere

Break these into separate examples and explain properties.

Example 4.1.3(Non-Hausdorff spaces): The following spaces are non-Hausdorff:

• The cofinite topology on any infinite set.

$\mathbb { R } / \mathbb { Q }$

• The line with two origins.

• Any variety $V ( J ) \subseteq \mathbb { A } _ { / k } ^ { n }$ for k a field and $J \triangleleft k [ x _ { 1 } , \cdot \cdot \cdot , x _ { n } ]$

Example 4.1.4(Constructed spaces): The following are some examples of ways to construct specific spaces for examples or counterexamples:

• Knot complements in $S ^ { 3 }$

• Covering spaces (hyperbolic geometry)

• Lens spaces

• Matrix groups

• Prism spaces

• Pair of pants

• Seifert surfaces

• Surgery

• Simplicial Complexes

– Nice minimal example:

<!-- image-->  
Fact 4.1.5 (Operations)

Some common operations that combine spaces:

• Cartesian product $A \times B$

• Wedge product $A \lor B$

• Connect Sum A#B

• Quotienting $A / B$

• Puncturing $A \setminus \{ a _ { i } \}$

• Smash product

• Join

• Cones

• Suspension

• Loop space

• Identifying a finite number of points

## 4.1.2 Alternative Topologies

Example 4.1.6(Nonstandard topologies): The following are some nice examples of topologies to put on familiar spaces to produce counterexamples:

• Discrete

• Cofinite

• Discrete and Indiscrete

• Uniform

Example 4.1.7(The cofinite topology): The cofinite topology on any space X is always

• Non-Hausdorff

• Compact

Proposition 4.1.8(Topology is discrete if and only if points are open).   
A topology (X, τ ) is the discrete topology iff points x ∈ X are open.

Proof (?).

If {x}i is open for each $x _ { i } \in X$ , then

• Any set U can be written as $U = \cup _ { i \in I } x _ { I }$ (for some I depending on U), and

• Unions of open sets are open.

Thus U is open.

Example 4.1.9(The discrete topology): Some facts about the discrete topology:

• Definition: every subset is open.

• Always Hausdorff

• Compact iff finite

• Totally disconnected

• If X is discrete, every map $f : X \to Y$ for any Y is continuous (obvious!)

Example 4.1.10(The indiscrete topology): Some facts about the indiscrete topology:

• Definition: the only open sets are $\varnothing , X$

• Never Hausdorff

• If Y is indiscrete, every map $f : X \to Y$ is continuous (obvious!)

• Always compact

## 4.1.3 Connectedness

<table><tr><td>Space</td><td></td><td>Connected Locally Connected</td></tr><tr><td>R</td><td>✓</td><td>✓</td></tr><tr><td>[0, 1] U [2, 3]</td><td></td><td>✓</td></tr><tr><td>Sine Curve</td><td>✓</td><td></td></tr><tr><td>Q</td><td></td><td></td></tr></table>

## 5 “Analysis”-esque Results in Topology

Proposition 5.0.1(The rationals are neither open nor closed).   
$\mathbb { Q } \subset \mathbb { R }$ is not open and not closed.

This follows because every neighborhood of $q \in \mathbb { Q }$ contains an irrational and every neighborhood of $q ^ { \prime } \in \mathbb { R } \setminus \mathbb { Q }$ contains a rational.

## 6 Theorems

Proposition 6.0.1(The continuous image of $\mathbf { \delta } _ { a \ldots } )$

The following properties are “pushed forward” through continuous maps, in the sense that if property P holds for X and $f : X \to Y$ , then f (X) also satisfies P :

• Compactness

• Separability

• If f is surjective:

– Connectedness

Density

The following are not preserved:

• Openness

• Closedness

See more here.

## 6.1 Metric Spaces and Analysis

Theorem 6.1.1(Cantor’s Intersection Theorem).   
A bounded collection of nested closed sets $C _ { 1 } \supset C _ { 2 } \supset \cdots$ in a metric space X is nonempty   
⇐⇒ X is complete.

```latex
Theorem 6.1.2(Cantor’s Nested Intervals Theorem).
If $\left\{ \left[ a _ { n } , b _ { n } \right] \ \left| \ n \in \mathbb { Z } ^ { \geq 0 } \right. \right\}$ is a nested sequence of compact intervals in a topological space X, then
their intersection is nonempty.
If X is a complete metric space and the diameters diam $( [ a _ { n } , b _ { n } ] ) \stackrel { n \to \infty } { \longrightarrow } 0$ , then their intersection
contains exactly one point.
```

Proposition 6.1.3(Continuous on compact =⇒ uniformly continuous).   
A continuous function on a compact set is uniformly continuous.

Proof (?).

$$
\left\{ B _ { \frac { \varepsilon } { 2 } } ( y ) \ \middle | \ y \in Y \right\} \preceq Y
$$

$$
x ^ { \prime } \in B _ { \delta _ { L } } ( x ) \implies f ( x ) , f ( x ^ { \prime } ) \in B _ { \frac { \varepsilon } { 2 } } ( y )
$$

$$
\delta _ { L } > 0 .
$$

Lipschitz continuity implies uniform continuity (take $\delta = \varepsilon / C )$

Remark 6.1.5: Counterexample to the converse: $f ( x ) = { \sqrt { x } }$ on [0, 1] has unbounded derivative.

Theorem 6.1.6(Extreme Value Theorem).   
For $f : X \to Y$ continuous with X compact and Y ordered in the order topology, there exist   
points c, d ∈ X such that $f ( x ) \in [ f ( c ) , f ( d ) ]$ for every x.

Theorem 6.1.7(Sequentially compact if and only if complete and totally bounded).   
A metric space X is sequentially compact iff it is complete and totally bounded. Theorem 6.1.8(Totally bounded if and only if Cauchy subsequences exist).   
A metric space is totally bounded iff every sequence has a Cauchy subsequence. Theorem 6.1.9(Compact if and only if complete and totally bounded).   
A metric space is compact iff it is complete and totally bounded.

If X is a complete metric space, X is a Baire space: the intersection of countably many dense open sets in X is again dense in X.

## 6.2 Compactness

Theorem 6.2.1(Closed if and only if compact in Hausdorff spaces).   
$U \subset X$ a Hausdorff spaces is closed ⇐⇒ it is compact. Theorem 6.2.3(Continuous image of compact is compact).   
The continuous image of a compact set is compact.

Theorem 6.2.2(Closed subset of compact is compact).   
A closed subset A of a compact set B is compact.

• Let $\{ A _ { i } \} \ni A$ be a covering of A by sets open in A.

• Each $A _ { i } = B _ { i } \cap$ A for some $B _ { i }$ open in B (definition of subspace topology)

• Define $V = \{ B _ { i } \}$ , then $V  A$ is an open cover.

• Since A is closed, $W : = B \setminus A$ is open

• Then V ∪ W is an open cover of B, and has a finite subcover {Vi}

Let $f : X \to f ( X )$ be continuous. Take an open covering $\mathcal { U } \supseteq f ( \boldsymbol { X } )$ , then $f ^ { - 1 } ( \mathcal { U } ) \overset { } { \underset { } {  } } X$ , which is cover by opens since f is continuous. Take a finite subcover by compactness of X, then they push forward to a finite subcover of f (X).

Theorem 6.2.4(Closed in Hausdorff =⇒ compact).

A closed subset of a Hausdorff space is compact.

## 6.3 Separability

Proposition 6.3.1(Properties preserved under retracts).   
A retract of a Hausdorff/connected/compact space is closed/connected/compact respectively.

Proposition 6.3.2(?).   
Points are closed in T1 spaces.

## 6.4 Maps and Homeomorphism

Theorem 6.4.1(Continuous bijections from compact to Hausdorff are homeomor  
phisms).   
A continuous bijection f : X → Y with X is compact and Y is Hausdorff is a homeomorphism.

Proof (?).   
Show that f −1 is continuous by showing f is a closed map. If $A \subseteq X$ is closed in a compact   
space, A is compact. The continuous image of a compact set is compact, so f(A) is compact.   
A compact set in a Hausdorff space is closed, so f (A) is closed in Y .

Remark 6.4.2(On retractions): Every space has at least one retraction - for example, the constant map $r : X  \{ x _ { 0 } \}$ for any $x \_ 0 \in X$

Theorem 6.4.3(When open maps are homeomorphisms).   
A continuous bijective open map is a homeomorphism.

Theorem 6.4.4(Characterizations of continuous maps, Munkres 18.1).   
For f : X → Y , TFAE:   
f is continuous   
$A \subset X \implies f ( \mathrm { c l } _ { X } ( A ) ) \subset \mathrm { c l } _ { X } ( f ( A ) )$   
B closed in Y =⇒ f −1(B) closed in X.   
• For each x ∈ X and each neighborhood V 3 f(x), there is a neighborhood U 3 x such   
that $f ( U ) \subset V$

Proof (?).   
See Munkres page 104.

Theorem 6.4.5(Maps from compact to Hausdorff spaces, Lee A.52). If f : X → Y is continuous where X is compact and Y is Hausdorff, then

• f is a closed map.

• If f is surjective, f is a quotient map.

• If f is injective, f is a topological embedding.

• If f is bijective, it is a homeomorphism.

## 6.5 The Tube Lemma

## Theorem 6.5.1(The Tube Lemma).

Let X, Y be spaces with Y compact, and let $x _ { 0 } \in X$ . Let $N \subseteq X \times Y$ be an open set containing the slice $x _ { 0 } \times Y$ , then there is a neighborhood $W \ni x$ in X such that $N \supset W \times Y ;$

<!-- image-->  
Figure 1: image_2021-05-21-00-28-13

Remark 6.5.2: Compactness in one factor is a necessary condition. For a counterexample, $\mathbb { R } ^ { 2 }$ and let N be the set contained between a Gaussian and its reflection across the x-axis. Then no tube about $y = 0$ is entirely contained within N :

<!-- image-->  
Figure 2: image_2021-05-21-01-39-26

Proof (Sketch).

• For each $y \in Y$ choose neighborhoods $A _ { y } , B _ { y } \subseteq Y$ such that

$$
( x , y ) \in A _ { y } \times B _ { y } \subseteq U .
$$

• By compactness of $Y _ { i }$ , reduce this to finitely many $B _ { y } \Longrightarrow Y \operatorname { s o } Y = \bigcup _ { j = 1 } ^ { n } B _ { y _ { j } }$

• Set $O : = \cap _ { j = 1 } ^ { n } B _ { y _ { j } }$ ; this works.

## Proof (Detailed proof of the Tube Lemma).

## Check this proof!

• Let $\Big \{ U _ { j } \times V _ { j } \ \Big | \ j \in J \Big \} \Longrightarrow X \times Y .$

• Fix a point $x _ { 0 } \in X$ , then $\{ x _ { 0 } \} \times Y \subset N$ for some open set $N .$

• $\mathrm { B y }$ the tube lemma, there is a $U ^ { x } \subset X$ such that the tube $U ^ { x } \times Y \subset N .$

• Since $\{ x _ { 0 } \} \times Y \cong Y$ which is compact, there is a finite subcover $\left\{ U _ { j } \times V _ { j } ~ \Big | ~ j \leq n \right\} \preceq$ $\{ x _ { 0 } \} \times Y$

• “Integrate the $X ^ { \dag }$ : write

$$
\begin{array} { r } { W = \cap _ { j = 1 } ^ { n } U _ { j } , } \end{array}
$$

then $x _ { 0 } \in W$ and $W$ is a finite intersection of open sets and thus open.

• Claim: $\left\{ U _ { j } \times V _ { j } \ \middle | \ j \leq n \right\} \Rightarrow W \times Y$

– Let $( x , y ) \in W \times Y ;$ ; want to show $( x , y ) \in U _ { j } \times V _ { j }$ for some $j \leq n$

– Then $( x _ { 0 } , y ) \in \{ x _ { 0 } \} \times Y$ is on the same horizontal line

$( x _ { 0 } , y ) \in U _ { j } \times V _ { j }$ for some j by construction

So $y \in V _ { j }$ for this j

– Since $x \in W , x \in U _ { j }$ for every j, thus $x \in U _ { j }$

So $( x , y ) \in U _ { j } \times V _ { j }$

## 7 Summary of Standard Topics

• Algebraic topology topics:

– Classification of compact surfaces

– Euler characteristic

– Connect sum

– Homology and cohomology groups

– Fundamental group

– Singular/cellular/simplicial homology

– Mayer-Vietoris long exact sequences for homology and cohomology

– Diagram chasing

– Degree of maps from $S ^ { n } \to S ^ { n }$

– Orientability, compactness

– Top-level homology and cohomology

– Reduced homology and cohomology

– Relative homology

– Homotopy and homotopy invariance

– Deformation retract

– Retract

– Excision

– Kunneth formula

– Factoring maps

– Fundamental theorem of algebra

• Algebraic topology theorems:

– Brouwer fixed point theorem

– Poincaré lemma

– Poincaré duality

– de Rham theorem

– Seifert-van Kampen theorem

• Covering space theory topics:

– Covering maps

– Free actions

– Properly discontinuous action

– Universal cover

– Correspondence between covering spaces and subgroups of the fundamental group of the base.

– Lifting paths

– Homotopy lifting property

– Deck transformations

– The action of the fundamental group

– Normal/regular cover

## Examples: Algebraic Topology

## 8.1 Standard Spaces and Modifications

Example 8.1.1(Spheres and Balls):

$$
\mathbb { D } ^ { n } = \mathbb { B } ^ { n } : = \left\{ \mathbf { x } \in \mathbb { R } ^ { n } \middle | \Vert \mathbf { x } \Vert \leq 1 \right\} \mathbb { S } ^ { n }
$$

$$
: = \left\{ \mathbf { x } \in \mathbb { R } ^ { n + 1 } ~ \middle | ~ \left\| \mathbf { x } \right\| = 1 \right\} = \partial \mathbb { D } ^ { n }
$$

Note: I’ll immediately drop the blackboard notation, this is just to emphasize that they’re “canonical” objects.

The sphere can be constructed in several equivalent ways:

$S ^ { n } \cong D ^ { n } / \partial D ^ { n }$ : collapsing the boundary of a disc is homeomorphic to a sphere.

$S ^ { n } \cong D ^ { n } \coprod _ { \partial D ^ { n } } D ^ { n }$ : gluing two discs along their boundary.

Note the subtle differences in dimension: $S ^ { n }$ is a manifold of dimension n embedded in a space of dimension n + 1.

<!-- image-->  
Figure 3: Low Dimensional Discs/Balls vs Spheres

Example 8.1.2(Real Projective Space): Constructed in one of several equivalent ways:

$S ^ { n } /$ ∼ where $\mathbf { x } \sim - \mathbf { x } ,$ i.e. antipodal points are identified.

• The space of lines in $\mathbb { R } ^ { n + 1 }$

One can also define $\mathbb { R P } ^ { \infty } : = \varinjlim _ { n } \mathbb { R P } ^ { n }$ . Fits into a fiber bundle of the form

<!-- image-->

Example 8.1.3(Complex Projective Space): Defined in a similar ways,

• Taking the unit sphere in $\mathbb { C } ^ { n }$ and identifying $\mathbf { z } \sim - \mathbf { z } .$

• The space of lines in $\mathbb { C } ^ { n + 1 }$

Can similarly define $\mathbb { C P } ^ { \infty } : = \varinjlim _ { n } \mathbb { C P } ^ { n }$ . Fits into a fiber bundle of the form

<!-- image-->

Example 8.1.4(Torii): The n-torus, defined as

$$
T ^ { n } : = \prod _ { j = 1 } ^ { n } S ^ { 1 } = S ^ { 1 } \times S ^ { 1 } \times \cdots .
$$

Example 8.1.5(Grassmannians): The real Grassmannian, $\operatorname { G r } ( n , k ) _ { / \mathbb { R } }$ , i.e. the set of k dimensional subspaces of Rn. One can similar define $\mathrm { G r } ( \boldsymbol { n } , \boldsymbol { k } ) _ { \mathbb { C } }$ for complex subspaces. Note that $\mathbb { R P } ^ { n } = \operatorname { G r } ( n , 1 ) _ { \mathbb { R } }$ and $\mathbb { C P } ^ { n } = \mathrm { G r } ( n , 1 ) _ { / \mathbb { C } }$

Example 8.1.6(Stiefel Manifolds): The Stiefel manifold $V _ { n } ( k ) _ { \mathbb { R } }$ , the space of orthonormal k-frames in $\mathbb { R } ^ { n } ?$

Example 8.1.7(Lie Groups): Lie Groups:

• The general linear group, ${ \mathrm { G L } } _ { n } ( \mathbb { R } )$

– The special linear group $S L _ { n } ( \mathbb { R } )$

• The orthogonal group, $O _ { n } ( \mathbb { R } )$

– The special orthogonal group, $S O _ { n } ( \mathbb { R } )$

• The real unitary group, $U _ { n } ( \mathbb { C } )$

– The special unitary group, $S U _ { n } ( \mathbb { R } )$

• The symplectic group $S p ( 2 n )$

Example 8.1.8(More random geometric examples): Some other spaces that show $\mathrm { u p } .$ , but don’t usually have great algebraic topological properties:

• Affine n-space over a field $\mathbb { A } ^ { n } ( k ) = k ^ { n } \rtimes G L _ { n } ( k )$

• The projective space $\mathbb { P } ^ { n } ( k )$

• The projective linear group over a ring $R , P G L _ { n } ( R )$

• The projective special linear group over a ring $R , P S L _ { n } ( R )$

• The modular groups $P S L _ { n } ( \mathbb { Z } )$

– Specifically $P S L _ { 2 } ( \mathbb { Z } )$

Example 8.1.9(Eilenberg-MacLane Spaces): $K ( G , n )$ is an Eilenberg-MacLane space, the homotopy-unique space satisfying

$$
\pi _ { k } ( K ( G , n ) ) = { \left\{ \begin{array} { l l } { G } & { k = n , } \\ { 0 } & { { \mathrm { e l s e } } } \end{array} \right. }
$$

Some known examples:

$K ( \mathbb { Z } , 1 ) = S ^ { 1 }$

$K ( \mathbb { Z } , 2 ) = \mathbb { C P } ^ { \infty }$

$K ( \mathbb { Z } / 2 \mathbb { Z } , 1 ) = \mathbb { R P } ^ { \infty }$

Example 8.1.10(Moore Spaces): $M ( G , n )$ is a Moore space, the homotopy-unique space satisfying

$$
H _ { k } ( M ( G , n ) ; G ) = { \left\{ \begin{array} { l l } { G } & { k = n , } \\ { 0 } & { k \neq n . } \end{array} \right. }
$$

Some known examples:

$M ( \mathbb { Z } , n ) = S ^ { n }$

$M ( \mathbb { Z } / 2 \mathbb { Z } , 1 ) = \mathbb { R P } ^ { 2 }$

$M ( \mathbb { Z } / p \mathbb { Z } , n )$ is made by attaching $e ^ { n + 1 }$ to $S ^ { n }$ via a degree p map.

Fact 8.1.11 (about standard low-dimensional spaces)

$\mathcal { M } \simeq S ^ { 1 }$ where M is the Mobius band.

$\mathbb { C P } ^ { n } = \mathbb { C } ^ { n } \coprod \mathbb { C P } ^ { n - 1 } = \coprod \bar { \big | } ^ { \circ } \mathbb { C } ^ { i }$

$\mathbb { C P } ^ { n } = S ^ { 2 n + 1 } / S ^ { n }$

$S ^ { n } / S ^ { k } \simeq S ^ { n } \vee \Sigma S ^ { k } .$

Remark 8.1.12(Accidental isomorphisms): In low dimensions, there are some “accidental” homeomorphisms:

$\mathbb { R } \mathbb { P } ^ { 1 } \cong S ^ { 1 }$

$\mathbb { C P } ^ { 1 } \cong S ^ { 2 }$

$\mathrm { S O } ( 3 ) \cong \mathbb { R P } ^ { 2 } ?$

## 8.2 Modifying Known Spaces

Example 8.2.1(Deleting points): Write $D ( k , X )$ for the space X with $k \in \mathbb N$ distinct points deleted, i.e. the punctured space $X - \{ x _ { 1 } , x _ { 2 } , . . . x _ { k } \}$ where each $x _ { i } \in X$ .

Example 8.2.2(Bouquets of Spheres): The “generalized uniform bouquet”? $B ^ { n } ( m ) = \bigvee _ { i = 1 } ^ { n } S ^ { m }$ There’s no standard name for this, but it’s an interesting enough object to consider!

Example 8.2.3(Other ways to modify a known space): Possible modifications to a space X:

• Remove a line segment

• Remove an entire line/axis

• Remove a hole

• Quotient by a group action (e.g. antipodal map, or rotation)

• Remove a knot

• Take complement in ambient space

## 9 Low Dimensional Homology Examples

Fact 9.0.1 (Table of low-dimensional homology)

$$
\begin{array} { r l } { S ^ { 1 } } &  { } =  \mathrm  ~ [ ~ \begin{array} { l l l l l l l } { Z , } & { \mathbb { Z } , } & { 0 , } & { 0 , } & { 0 , } & { 0 \to } \\ { \mathbb { M } } &  = { \mathrm { ~ [ ~ \begin{array} { l l l l l l } { Z , } & { \mathbb { Z } , } & { 0 , } & { 0 , } & { 0 , } & { 0 \to } \\ { 0 } & { \mathbb { Z } , } & { \mathbb { Z } , } & { 0 , } & { 0 , } & { 0 , } & { 0 \to } \end{array} ] } } \\ { \mathbb { R } \mathbb { P } ^ { 1 } } &  { } = { \mathrm { ~ [ ~ \begin{array} { l l l l l l l } { Z , } & { \mathbb { Z } , } & { 0 , } & { 0 , } & { 0 , } & { 0 , } & { 0 \to } \\ { \mathbb { Z } , } & { \mathbb { Z } , } & { 0 , } & { 0 , } & { 0 , } & { 0 , } & { 0 \to } \end{array} ] } } \\ { \mathbb { R } \mathbb { P } ^ { 2 } } &  { } = { \mathrm { ~ [ ~ \begin{array} { l l l l l l l } { \mathbb { Z } , } & { \mathbb { Z } , } & { 0 , } & { 0 , } & { 0 , } & { 0 , } & { 0 \to } \\ { \mathbb { Z } , } & { \mathbb { Z } , } & { 0 , } & { \mathbb { Z } , } & { 0 , } & { 0 , } & { 0 \to } \end{array} ] } } \\ { \mathbb { R } \mathbb { P } ^ { 4 } } &  { } = { \mathrm { ~ [ ~ \begin{array} { l l l l l l l } { \mathbb { Z } , } & { \mathbb { Z } , } & { 0 , } & { \mathbb { Z } , } & { \mathbb { Z } , } & { 0 , } & { 0 \to } \\ { \mathbb { Z } , } & { 0 , } & { \mathbb { Z } , } & { 0 , } & { 0 , } & { 0 \to } \end{array} ] } } \\ { S ^ { 2 } } &  { } =  \mathrm  ~ [ ~ \begin{array} { l l l l l l }  \ \end{array} \end{array} \end{array}
$$

# 10 Table of Homotopy and HomologyStructures

Remark 10.0.1: The following is a giant list of known homology/homotopy.

<table><tr><td>X</td><td> $\pi _ { * } ( X )$ </td><td> $H _ { * } ( X )$ </td><td>CW Structure</td><td> $H ^ { * } ( X )$ </td></tr><tr><td> $\mathbb { R } ^ { 1 }$ </td><td>0</td><td>0</td><td> $\mathbb { Z } \cdot 1 + \mathbb { Z } \cdot x$ </td><td>0</td></tr><tr><td> $\mathbb { R } ^ { n }$ </td><td>0</td><td>0</td><td> $( \mathbb { Z } \cdot 1 + \mathbb { Z } \cdot x ) ^ { n }$ </td><td>0</td></tr><tr><td> $D ( k , \mathbb { R } ^ { n } )$ </td><td> $\pi _ { * } \bigvee ^ { k } S ^ { 1 }$ </td><td> $\bigoplus \ H _ { * } M ( \mathbb { Z } , 1 )$ </td><td> $1 + k x$ </td><td>?</td></tr><tr><td> $B ^ { n }$ </td><td> $\pi _ { * } ( \mathbb { R } ^ { n } )$ </td><td>k  $\overset { \underset { \mathrm { \tiny ~ \ " ~ } } { } } { H _ { \ast } } ( \mathbb { R } ^ { n } )$ </td><td> $1 + x ^ { n } + x ^ { n + 1 }$ </td><td>0</td></tr><tr><td> $S ^ { n }$ </td><td> $[ 0 \ldots , \mathbb { Z } , ? \ldots ]$ </td><td> $H _ { * } M ( \mathbb { Z } , n )$ </td><td> $1 + x ^ { n } \ { \mathrm { o r } } \sum _ { i = 0 } ^ { n } 2 x ^ { i }$ </td><td> $\mathbb { Z } [ _ { n } x ] / ( x ^ { 2 } )$ </td></tr><tr><td> $D ( k , S ^ { n } )$ </td><td> $\pi _ { * } \big \langle \bigvee ^ { k - 1 } S ^ { 1 }$ </td><td> $\bigoplus \ H _ { * } M ( \mathbb { Z } , 1 )$ </td><td> $1 + ( k - 1 ) x ^ { 1 }$ </td><td>?</td></tr><tr><td> $T ^ { 2 }$ </td><td> $\pi _ { * } S ^ { 1 } \times \pi _ { * } S ^ { 1 }$ </td><td>k−1  $\stackrel {  } { ( } H _ { * } M ( \mathbb { Z } , 1 ) ) ^ { 2 } \times H _ { * } M ( \mathbb { Z } , 2 )$ </td><td> $1 + 2 x + x ^ { 2 }$ </td><td> $\Lambda ( _ { 1 } x _ { 1 } , _ { 1 } x _ { 2 } )$ </td></tr><tr><td> $T ^ { n }$ </td><td>n  $\prod \pi _ { * } S ^ { 1 }$ </td><td>n  $\prod ^ { n } ( H _ { * } M ( \mathbb { Z } , i ) ) ^ { \binom { n } { i } }$ </td><td> $( 1 + x ) ^ { n }$ </td><td> $\Lambda ( \ b _ { 1 } x _ { 1 } , \ b _ { 1 } x _ { 2 } , \ b _ { \cdot \cdot \cdot } \ b _ { 1 } x _ { n } )$ </td></tr><tr><td> $D ( k , T ^ { n } )$ </td><td></td><td> $\begin{array} { l } { i = 1 } \\ { \left[ 0 , 0 , 0 , 0 , \ldots \right] ? } \end{array}$ </td><td></td><td></td></tr><tr><td> $S ^ { 1 } \dot { \ V } S ^ { 1 } \dot { \ }$ </td><td> $[ 0 , 0 , 0 , 0 , \ldots ] ?$   $\pi _ { * } S ^ { 1 } * \pi _ { * } S ^ { 1 }$ </td><td> $\mathsf { \bar { ( } } H _ { * } M ( \mathbb { Z } , 1 ) \mathsf { ) ^ { 2 } }$ </td><td> $\begin{array} { l } { 1 + x } \\ { 1 + 2 x } \end{array}$ </td><td>? ?</td></tr><tr><td> $\ddot { \bigvee } { s ^ { 1 } }$ </td><td> $* ^ { n } \pi _ { * } S ^ { 1 }$ </td><td> $\prod \scriptscriptstyle H _ { * } M ( \mathbb { Z } , 1 )$ </td><td> $1 + x$ </td><td>?</td></tr><tr><td> $\mathbb { R } \mathbb { P } ^ { 1 }$ </td><td> $\pi _ { * } S ^ { 1 }$ </td><td> $H _ { * } M ( \mathbb { Z } , 1 )$ </td><td></td><td> $\phantom { + } 0 \mathbb { Z } \times \phantom { + } 1 \mathbb { Z }$ </td></tr><tr><td> $\mathbb { R } \mathbb { P } ^ { 2 }$ </td><td> $\pi _ { * } K ( \mathbb { Z } / 2 \mathbb { Z } , 1 ) +$ </td><td> $H _ { * } M ( \mathbb { Z } / 2 \mathbb { Z } , 1 )$ </td><td> $\begin{array} { l } { 1 + x } \\ { 1 + x + x ^ { 2 } } \end{array}$ </td><td> $\phantom { + } 0 \mathbb { Z } \times \phantom { + } _ { 2 } \mathbb { Z } / 2 \mathbb { Z }$ </td></tr><tr><td> $\mathbb { R } \mathbb { P } ^ { 3 }$ </td><td> $\pi _ { * } S ^ { 2 }$   $\pi _ { * } K ( \mathbb { Z } / 2 \mathbb { Z } , 1 ) +$ </td><td> $H _ { * } M ( \mathbb { Z } / 2 \mathbb { Z } , 1 ) + H _ { * } M ( \mathbb { Z } , 3 )$ </td><td> $1 + x + x ^ { 2 } + x ^ { 3 }$ </td><td> $\phantom { + } 0 \mathbb { Z } \times \phantom { + } 2 \mathbb { Z } / 2 \mathbb { Z } \times \phantom { + } _ { 3 } \mathbb { Z }$ </td></tr><tr><td> $\mathbb { R } \mathbb { P } ^ { 4 }$ </td><td> $\pi _ { * } S ^ { 3 }$   $\pi _ { * } K ( \mathbb { Z } / 2 \mathbb { Z } , 1 ) +$   $\pi _ { * } S ^ { 4 }$ </td><td> $H _ { * } M ( \mathbb { Z } / 2 \mathbb { Z } , 1 ) +$   $H _ { * } M ( \mathbb { Z } / 2 \mathbb { Z } , 3 )$ </td><td> $1 + x + x ^ { 2 } + x ^ { 3 } + x ^ { 4 }$ </td><td> $\phantom { + } 0 \mathbb { Z } \times ( 2 \mathbb { Z } / 2 \mathbb { Z } ) ^ { 2 }$ </td></tr><tr><td> $\mathbb { R P } ^ { n } , n \geq 4$ </td><td> $\pi _ { * } K ( \mathbb { Z } / 2 \mathbb { Z } , 1 ) +$ </td><td> $\prod \mathrm { \Sigma } \ H _ { * } M ( \mathbb { Z } / 2 \mathbb { Z } , i )$ </td><td> $\sum _ { i = 1 } ^ { n } x ^ { i }$ </td><td></td></tr><tr><td>even</td><td> $\pi _ { * } S ^ { n }$ </td><td> $\mathbf { o d d } \ i < n$ </td><td></td><td> $\mathfrak { o } \mathbb { Z } \times \prod _ { i = 1 } ^ { n / 2 } \mathfrak { z } / 2 \mathbb { Z }$ </td></tr><tr><td> $\mathbb { R P } ^ { n } , n \geq 4$ </td><td> $\pi _ { * } K ( \mathbb { Z } / 2 \mathbb { Z } , 1 ) +$ </td><td> $\begin{array} { r l } { \prod } & { { } H _ { * } M ( \mathbb { Z } / 2 \mathbb { Z } , i ) \times } \end{array}$ </td><td> $\sum _ { i = 1 } ^ { \cdot \setminus } x ^ { i }$ </td><td> $H ^ { * } ( \mathbb { R P } ^ { n - 1 } ) \times { _ { n } \mathbb { Z } }$ </td></tr><tr><td>odd</td><td> $\pi _ { * } S ^ { n }$ </td><td> $\mathbf { o d d } \ i \leq n - 2$ </td><td></td><td></td></tr><tr><td> $\mathbb { C P } ^ { 1 }$ </td><td> $\pi _ { * } K ( \mathbb { Z } , 2 ) + \pi _ { * } S ^ { 3 }$ </td><td> $H _ { * } S ^ { n }$   $H _ { * } S ^ { 2 }$ </td><td> $x ^ { 0 } + x ^ { 2 }$ </td><td> $\mathbb { Z } [ _ { 2 } x ] / ( _ { 2 } x ^ { 2 } )$ </td></tr><tr><td> $\mathbb { C P } ^ { 2 }$ </td><td> $\pi _ { * } K ( \mathbb { Z } , 2 ) + \pi _ { * } S ^ { 5 }$ </td><td> $H _ { * } S ^ { 2 } \times H _ { * } S ^ { 4 }$  n</td><td> $x ^ { 0 } + x ^ { 2 } + x ^ { 4 }$ </td><td> $\mathbb { Z } [ 2 x ] / ( 2 x ^ { 3 } )$ </td></tr><tr><td> $\mathbb { C P } ^ { n } , n \geq 2$ </td><td> $\pi _ { * } K ( \mathbb { Z } , 2 ) +$ </td><td> $\prod { H _ { * } S ^ { 2 i } }$ </td><td> $\sum _ { . } ^ { n } x ^ { 2 i }$ </td><td> $\mathbb { Z } [ { _ { 2 } } x ] / ( { _ { 2 } } x ^ { n + 1 } )$ </td></tr><tr><td></td><td>π*S2n+1</td><td>i=1</td><td>i=1</td><td></td></tr><tr><td>Mobius Band Klein Bottle</td><td> $\pi * S ^ { 1 }$   $K ( \mathbb { Z } \rtimes _ { - 1 } \mathbb { Z } , 1 )$ </td><td> $H _ { * } S ^ { 1 }$   $H _ { \ast } S ^ { 1 } \times H _ { \ast } \mathbb { R P } ^ { \infty }$ </td><td>1+x  $1 + 2 x + x ^ { 2 }$ </td><td>? ?</td></tr></table>

## Fact 10.0.2 (used to fill out the above table)

$\mathbb { R } ^ { n }$ is a contractible space, and so $[ S ^ { m } , \mathbb { R } ^ { n } ] = 0$ for all $n ,$ m which makes its homotopy groups all zero.

$D ( k , \mathbb { R } ^ { n } ) = \mathbb { R } ^ { n } - \{ x _ { 1 } \ldots x _ { k } \} \simeq \bigvee _ { i = 1 } ^ { k } S ^ { 1 }$ by a deformation retract.

$S ^ { n } \cong B ^ { n } / \partial B ^ { n }$ and employs an attaching map

$$
\begin{array} { c } { { \varphi : ( D ^ { n } , \partial D ^ { n } )  S ^ { n } } } \\ { { ( D ^ { n } , \partial D ^ { n } ) \mapsto ( e ^ { n } , e ^ { 0 } ) . } } \end{array}
$$

$B ^ { n } \simeq \mathbb { R } ^ { n }$ by normalizing vectors.

• Use the inclusion $S ^ { n } \hookrightarrow B ^ { n + 1 }$ as the attaching map.

$\mathbb { C P } ^ { 1 } \cong S ^ { 2 }$

$\mathbb { R } \mathbb { P } ^ { 1 } \cong S ^ { 1 }$

• Use $\left[ \pi _ { 1 } , \prod \right] = 0$ and the universal cover $\mathbb { R } ^ { 1 } \twoheadrightarrow S ^ { 1 }$ to yield the cover $\mathbb { R } ^ { n } \twoheadrightarrow T ^ { n }$

• Take the universal double cover $S ^ { n } \to ^ { \times 2 } \mathbb { R P } ^ { n }$ to get equality in $\pi _ { i \geq 2 }$

• Use $\mathbb { C P } ^ { n } = S ^ { 2 n + 1 } / S ^ { 1 }$

• Alternatively, the fundamental group is $\mathbb { Z } * \mathbb { Z } / b a b ^ { - 1 } a$ . Use the fact the $\tilde { K } = \mathbb { R } ^ { 2 }$

$M \simeq S ^ { 1 }$ by deformation-retracting onto the center circle.

$D ( 1 , S ^ { n } ) \cong \mathbb { R } ^ { n }$ and thus $D ( k , S ^ { n } ) \cong D ( k - 1 , \mathbb { R } ^ { n } ) \cong \bigvee S ^ { 1 }$

## 11 Theorems: Algebraic Topology

<!-- image-->

## 11.1 General Homotopies

<!-- image-->

Fact 11.1.1 (Contracting Spaces in Products)

$$
X \times \mathbb { R } ^ { n } \simeq X \times \mathrm { p t } \cong X .
$$

Fact 11.1.2 $( \pi _ { 0 } , H _ { 0 }$ detect path components)

The ranks of $\pi _ { 0 }$ and $H _ { 0 }$ are the number of path components.

Theorem 11.1.3(Convex sets admit homotopies).

Any two continuous functions into a convex set are homotopic.

Proof (?).

The linear homotopy. Supposing X is convex, for any two points $x , y \in X$ , the line $t x + ( 1 - t ) y$ is contained in X for every $t \in [ 0 , 1 ]$ . So let $f , g : Z \to X$ be any continuous functions into X.

Then define H : $Z \times I $ X by $H ( z , t ) = t f ( z ) + ( 1 - t ) g ( z )$ , the linear homotopy between $f , g .$ By convexity, the image is contained in X for every $t , z ,$ so this is a homotopy between $f , g .$

## 11.2 Fundamental Group

## 11.2.1 Definition

## Definition 11.2.1 (The Fundamental Group)

Given a pointed space $( X , x _ { 0 } )$ , we define the fundamental group $\pi _ { 1 } ( X )$ as follows:

• Take the set

$$
L : = \{ \alpha : S ^ { 1 }  X \ \middle | \ \alpha ( 0 ) = \alpha ( 1 ) = x _ { 0 } \} .
$$

• Define an equivalence relation $\alpha \sim \beta$ iff $\alpha \simeq \beta$ in $X$ , so there exists a homotopy

$$
H : S ^ { 1 } \times I \to X
$$

$$
\left\{ { \begin{array} { l } { H ( s , 0 ) = \alpha ( s ) } \\ { H ( s , 1 ) = \beta ( s ) , } \end{array} } \right.
$$

- Check that this relation is

• Symmetric: Follows from considering $H ( s , 1 - t )$

• Reflexive: Take $H ( s , t ) = \alpha ( s )$ for all t.

• Transitive: Follows from reparameterizing.

• Define $L / \sim ,$ which contains elements like [α] and $[ \mathrm { i d } _ { x _ { 0 } } ]$ , the equivalence classes of loops after quotienting by this relation.

• Define a product structure: for $[ \alpha ] , [ \beta ] \in L / \sim$ , define $[ \alpha ] [ \beta ] = [ \alpha \cdot \beta ]$ , where we just need to define a product structure on actual loops. Do this by reparameterizing:

$$
( \alpha \cdot \beta ) ( s ) : = \left\{ \begin{array} { l l } { \alpha ( 2 s ) } & { s \in [ 0 , 1 / 2 ] } \\ { \beta ( 2 s - 1 ) } & { s \in [ 1 / 2 , 1 ] . } \end{array} \right.
$$

• Check that this map is:

– Continuous: by the pasting lemma and assumed continuity of $f , g .$

– Well-defined: ?

• Check that this is actually a group

– Identity element: The constant loop $\operatorname { i d } _ { x _ { 0 } } : I \to X$ where $\mathrm { i d } _ { x _ { 0 } } ( t ) = x _ { 0 }$ for all t.   
Inverses: The reverse loop $\bar { \alpha } ( t ) : = \alpha ( 1 - t )$   
Closure: Follows from the fact that start/end points match after composing loops,   
and reparameterizing.   
Associativity: Follows from reparameterizing.

Remark 11.2.2(a summary): Elements of the fundamental group are homotopy classes of loops, and every continuous map between spaces induces a homomorphism on fundamental groups.

## 11.2.2 Conjugacy in $\pi _ { 1 } \cdot$

• See Hatcher 1.19, p.28

• See Hatcher’s proof that $\pi _ { 1 }$ is a group

• See change of basepoint map

## 11.2.3 Calculating $\pi _ { 1 }$

Proposition 11.2.3(Using universal covers).   
If X˜ → X the universal cover of X and G y X˜ with ${ \tilde { X } } / G = X$ then $\pi _ { 1 } ( X ) = G .$

```perl
Proposition 11.2.4(Killing homotopy).
$\pi _ { 1 } X$ for X a CW-complex only depends on the 2-skeleton $X ^ { 2 }$ , and in general $\pi _ { k } ( X )$ only
depends on the k + 2-skeleton. Thus attaching $k + 2$ or higher cells does not change $\pi _ { k }$
```

Theorem 11.2.5(Seifert-van Kampen).   
Suppose $X = U _ { 1 } \cup U _ { 2 }$ where $U _ { 1 } , U _ { 2 } ,$ and $U : = U _ { 1 } \cap U _ { 2 } \neq \emptyset$ are open and path-connected a   
, and let $x _ { 0 } \in U .$   
Then the inclusion maps $i _ { 1 } : U _ { 1 } \hookrightarrow X$ and $i _ { 2 } : U _ { 2 } \hookrightarrow X$ induce the following group homomor  
phisms:   
$i _ { 1 } ^ { * } : \pi _ { 1 } ( U _ { 1 } , x _ { 0 } ) \to \pi _ { 1 } ( X , x _ { 0 } )$   
$i _ { 2 } ^ { * } : \pi _ { 1 } ( U _ { 2 } , x _ { 0 } )  \pi _ { 1 } ( X , x _ { 0 } )$   
There is a natural isomorphism   
$\pi _ { 1 } ( X ) \cong \pi _ { 1 } U * _ { \pi _ { 1 } ( U \cap V ) } \pi _ { 1 } V ,$   
where the amalgamated product can be computed as follows: A pushout is the colimit of the   
following diagram

<!-- image-->

<!-- image-->  
Figure 4: Example of a pushout of spaces

For groups, the pushout is realized by the amalgamated free product: if

$$
\left\{ \begin{array} { l l } { { \pi _ { 1 } U _ { 1 } = A = \left. \boldsymbol { G } _ { A } \mid \boldsymbol { R } _ { A } \right. } } & { { } } \\ { { \pi _ { 1 } U _ { 2 } = B = \left. \boldsymbol { G } _ { B } \mid \boldsymbol { R } _ { B } \right. } } & { { } } \end{array} \right. \Longrightarrow \ A * _ { Z } B : = \left. \boldsymbol { G } _ { A } , \boldsymbol { G } _ { B } \ \middle | \ \boldsymbol { R } _ { A } , \boldsymbol { R } _ { B } , \boldsymbol { T } \right.
$$

where $T$ is a set of relations given by

$$
T = \left\{ \iota _ { 1 } ^ { \ast } ( z ) \iota _ { 2 } ^ { \ast } ( z ) ^ { - 1 } ~ \Big | ~ z \in \pi _ { 1 } ( U _ { 1 } \cap U _ { 2 } ) \right\} ,
$$

where $\iota _ { 2 } ^ { * } ( z ) ^ { - 1 }$ denotes the inverse group element. If we have presentations

$$
\pi _ { 1 } ( U , x _ { 0 } ) = \left. u _ { 1 } , \cdot \cdot \cdot , u _ { k } \ \middle | \ \alpha _ { 1 } , \cdot \cdot \cdot , \alpha _ { l } \right.
$$

$$
\pi _ { 1 } ( V , w ) = \left. v _ { 1 } , \cdot \cdot \cdot , v _ { m } \ \middle | \ \beta _ { 1 } , \cdot \cdot \cdot , \beta _ { n } \right.
$$

$$
\pi _ { 1 } ( U \cap V , x _ { 0 } ) = \left. w _ { 1 } , \cdot \cdot \cdot , w _ { p } \ \middle | \ \gamma _ { 1 } , \cdot \cdot \cdot , \gamma _ { q } \right.
$$

then

$$
\pi _ { 1 } ( X , w ) =  u _ { 1 } , \cdots , u _ { k } , v _ { 1 } , \cdots , v _ { m } | \{ \begin{array} { l } { \alpha _ { 1 } , \cdots , \alpha _ { l } } \\ { \beta _ { 1 } , \cdots , \beta _ { n } } \\ { I ( w _ { 1 } ) J ( w _ { 1 } ) ^ { - 1 } , \cdots , I ( w _ { p } ) J ( w _ { p } ) ^ { - 1 } } \end{array}  
$$

$$
= \frac { \pi _ { 1 } ( U _ { 1 } ) * \pi _ { 1 } ( U _ { 2 } ) } { \left. \left\{ \iota _ { 1 } ^ { * } ( w _ { i } ) \iota _ { 2 } ^ { * } ( w _ { i } ) ^ { - 1 } \ \middle | \ 1 \leq i \leq p \right\} \right. }
$$

aNote that the hypothesis that $U _ { 1 } \cap U _ { 2 }$ is path-connected is necessary: take $S ^ { 1 }$ with U, V neighborhoods of the poles, whose intersection is two disjoint components.

Proof (Sketch).

• Construct a map going backwards

• Show it is surjective

– “There and back” paths

• Show it is injective

– Divide $I \times I$ into a grid

Example 11.2.6(Pushing out with van Kampen): $A \ = \ \mathbb { Z } / 4 \mathbb { Z } \ = \ \left. x \ \middle | \ x ^ { 4 } \right. , B \ = \ \mathbb { Z } / 6 \mathbb { Z }$ $\left. y \mid x ^ { 6 } \right. , Z = \mathbb { Z } / 2 \mathbb { Z } = \left. z \mid z ^ { 2 } \right.$ . Then we can identify Z as a subgroup of A, B using $\iota _ { A } ( z ) = x ^ { 2 }$ and $\iota _ { B } ( z ) = y ^ { 3 }$ . So

$$
A * _ { Z } B = \left. x , y \mid x ^ { 4 } , y ^ { 6 } , x ^ { 2 } y ^ { - 3 } \right.
$$

Proposition 11. $\mathbf { . 2 . 7 } ( \pi _ { 1 }$ of a wedge).

$$
\pi _ { 1 } ( X \vee Y ) = \pi _ { 1 } ( X ) * \pi _ { 1 } ( Y ) .
$$

Proof (?).

By van Kampen, this is equivalent to the amalgamated product over $\pi _ { 1 } ( x _ { 0 } ) = 1$ , which is just a free product.

## 11.2.4 Facts

Fact 11.2.8

$H _ { 1 }$ is the abelianization of $\pi _ { 1 }$

Proposition 11.2.9(π1 of a product, Hatcher 1.12). If X, Y are path-connected, then

$$
\pi _ { 1 } ( X \times Y ) = \pi _ { 1 } ( X ) \times \pi _ { 2 } ( Y ) .
$$

Proof (sketch).

• A loop in $X \times Y$ is a continuous map $\gamma : I  X \times Y$ given by $\gamma ( t ) = ( f ( t ) , g ( t )$ in components.

• γ being continuous in the product topology is equivalent to $f , g$ being continuous maps to X, Y respectively.

• Similarly a homotopy $F : I ^ { 2 } \to X \times Y$ is equivalent to a pair of homotopies $f _ { t } , g _ { t }$ of the corresponding loops.

• So the map $[ \gamma ] \mapsto ( [ f ] , [ g ] )$ is the desired bijection.

Proposition 11.2.10 $( \pi _ { 1 }$ detects simply-connectedness).   
$\pi _ { 1 } ( X ) = 1$ iff X is simply connected.

Proof (?).

⇒: Suppose X is simply connected. Then every loop in X contracts to a point, so if α is a loop in $X , [ \alpha ] = [ \mathrm { i d } _ { x _ { 0 } } ]$ , the identity element of $\pi _ { 1 } ( X )$ . But then there is only one element in in this group.

⇐: Suppose $\pi _ { 1 } ( X ) = 0$ . Then there is just one element in the fundamental group, the identity element, so if α is a loop in X then $[ \alpha ] = [ \mathrm { i d } _ { x _ { 0 } } ]$ . So there is a homotopy taking α to the constant map, which is a contraction of α to a point.

:::{.fact “Unsorted facts”}

• For a graph G, we always have $\pi _ { 1 } ( G ) \cong \mathbb { Z } ^ { n }$ where $n = | E ( G - T ) |$ , the complement of the set n of edges in any maximal tree. Equivalently, $n = 1 - \chi ( G )$ . Moreover, $X \simeq \dot { \bigvee } S ^ { 1 }$ in this case.

## 11.3 General Homotopy Theory

A map $X ~ { \stackrel { f } { \to } } ~ Y$ on CW complexes that is a weak homotopy equivalence (inducing isomorphisms in homotopy) is in fact a homotopy equivalence.

## 4! Warning 11.3.2

Individual maps may not work: take $S ^ { 2 } \times \mathbb { R P } ^ { 3 }$ and $S ^ { 3 } \times \mathbb { R } \mathbb { P } ^ { 2 }$ which have isomorphic homotopy but not homology.

Theorem 11.3.3(Hurewicz).   
The Hurewicz map on an n − 1-connected space X is an isomorphism $\pi _ { k \leq n } X \to H _ { k \leq n } X .$   
I.e. for the minimal i ≥ 2 for which $\pi _ { i X } \neq 0$ but   
$\pi _ { \leq i - 1 } X = 0 , \pi _ { i X } \cong H _ { i X }$

Theorem 11.3.4(Cellular Approximation).

Any continuous map between CW complexes is homotopy equivalent to a cellular map.

Example 11.3.5(Applications of cellular approximation):

$\pi _ { k \leq n } S ^ { n } = 0$

$\pi _ { n } ( X ) \cong \pi _ { n } ( X ^ { ( n ) } )$

Theorem 11.3.6(Freudenthal Suspension).

:::{.fact title="Unsorted facts about higher homotopy groups}

$\pi _ { i \geq 2 } ( X )$ is always abelian.

– X simply connected $\implies \pi _ { k } ( X ) \cong H _ { k } ( X )$ up to and including the first nonvanishing $H _ { k }$

$\pi _ { k } \vee X \ne \prod \pi _ { k } X$ (counterexample: $S ^ { 1 } \vee S ^ { 2 } )$

– Nice case: $\pi _ { 1 } \bigvee X = * \pi _ { 1 } X$ by Van Kampen.

$\pi _ { i } ( { \widehat { X } } ) \cong \pi _ { i } ( X )$ for $i \geq 2$ whenever ${ \widehat { X } } \twoheadrightarrow X$ is a universal cover.

$\pi _ { i } ( S ^ { n } ) = 0$ for $i < n , \pi _ { n } ( S ^ { n } ) = \mathbb { Z }$

– Not necessarily true that $\pi _ { i } ( S ^ { n } ) = 0$ when $i > n ! ! !$

$\diamondsuit \ \mathrm { E . g . } \ \pi _ { 3 } ( S ^ { 2 } ) = \mathbb { Z }$ by Hopf fibration

$S ^ { n } / S ^ { k } \simeq S ^ { n } \vee \Sigma S ^ { k }$

$$
- \ \Sigma S ^ { n } = S ^ { n + 1 }
$$

• General mantra: homotopy plays nicely with products, homology with wedge products.1

$\pi _ { k } \prod X = \prod \pi _ { k } X$ by $\mathrm { L E S . ^ { 2 } }$

• In general, homotopy groups behave nicely under homotopy pull-backs (e.g., fibrations and products), but not homotopy push-outs (e.g., cofibrations and wedges). Homology is the opposite.

• Constructing a $K ( \pi , 1 )$ : since $\pi = \left. S \mid R \right. = F ( S ) / R .$ , take $\stackrel { | S | } { \vee } S ^ { 1 } \cup _ { | R | } e ^ { 2 }$ . In English, wedge a circle for each generator and attach spheres for relations.

## 12 Covering Spaces

Some pictures to keep in mind when it comes to covers and path lifting:

<!-- image-->  
Figure 5: Picture to keep in mind

<!-- image-->  
Figure 6: A more complicated situation

## 12.1 Useful Facts

Remark 12.1.1: When covering spaces are involved in any way, try computing Euler characteristics - this sometimes yields nice numerical constraints.

Fact 12.1.2 (Euler characteristics are multiplicative on covering spaces)

For $p : A  B$ an n-fold cover,

$$
\chi ( A ) = n \chi ( B ) .
$$

## Fact 12.1.3

Covering spaces of orientable manifolds are orientable.

## Fact 12.1.4

The preimage of a boundary point under a covering map must also be a boundary point

## Fact 12.1.5

Normal subgroups correspond to normal/regular coverings, where automorphisms act freely/transitively. These are “maximally symmetric”.

## 12.2 Universal Covers

## Proposition 12.2.1(Existence of universal covers).

• Connected,

• Locally path-connected, and

• Semilocally simply connected,

then X admits a universal cover: if $C \stackrel { q } { \to } X$ is a covering map with C connected, then there exists a covering map ${ \tilde { p } } : { \tilde { X } }  C$ making the following diagram commute:

<!-- image-->  
Link to diagram

That is, any other cover C of X is itself covered by $\tilde { X }$ . Note that by this universal property, X˜ is unique up to homeomorphism when it exists.

Theorem 12.2.2(Homotopy lifting property for covers, Hatcher 1.30). Let $p : \tilde { X } \to X$ be any covering space, $F : Y \times I  X$ be any homotopy, and ${ \tilde { F } } _ { 0 } : Y \to { \tilde { X } }$ be any lift of $F _ { 0 }$ . Then there exists a unique homotopy ${ \tilde { F } } : Y  { \tilde { X } }$ of $\tilde { F } _ { 0 }$ that lifts F :

<!-- image-->

If $f : Y \to X$ with Y path-connected and locally path-connected, then there exists a unique lift ${ \tilde { f } } : Y \to { \tilde { X } }$ if and only if $f _ { * } ( \pi _ { 1 } ( Y ) ) \subset \pi _ { * } ( \pi _ { 1 } ( { \tilde { X } } ) )$

<!-- image-->

Moreover, lifts are unique if they agree at a single point.

Remark 12.2.4(Automatic lifts): Note that if $Y$ is simply connected, then $\pi _ { 1 } ( Y ) = 0$ and this holds automatically!

Proposition 12.2.5(Covering spaces induce injections on $\pi _ { 1 }$ , Hatcher 1.31). Given a covering space $\tilde { X } \stackrel { p } { \to } X$ , the induced map $p ^ { * } : \pi _ { 1 } ( { \tilde { X } } ) \to \pi _ { 1 } ( X )$ is injective. The image consists of classes [γ] whose lifts to $\tilde { X }$ are again loops.

Theorem 12.2.6(Fundamental theorem of covering spaces, Hatcher 1.39).

For $\tilde { X } \ { \stackrel { p } { \to } } \ X$ a covering space with

$\tilde { X }$ path-connected,

• X path-connected and locally path-connected,

letting H be the image of $\pi _ { 1 } ( \tilde { X } )$ in $\pi _ { 1 } ( X )$ , we have

1. $\tilde { X }$ is normal if and only if $H \leq \pi _ { 1 } ( X )$

2. $G ( \tilde { X } ) \cong \mathrm { A u t } _ { \mathrm { C o v } ( \tilde { X } ) } N _ { \pi _ { 1 } ( X ) } ( H )$ , the normalizer of H in $\pi _ { 1 } ( X )$

In particular, if $\tilde { X }$ is normal, $\operatorname { A u t } ( { \tilde { X } } ) \cong \pi _ { 1 } ( X ) / H$ , and if $\tilde { X }$ is the universal cover, $\operatorname { A u t } ( { \tilde { X } } ) =$ $\pi _ { 1 } ( X )$

## Fact 12.2.7

There is a contravariant bijective correspondence

$$
\{ \begin{array} { c } { { \mathrm { C o n n e c t e d ~ c o v e r i n g ~ s p a c e s } } } \\ { { p { ; } \tilde { X } {  } X } } \end{array} \} _ { / \sim } \{ \begin{array} { c } { { \mathrm { C o n j u g a c y ~ c l a s s e s ~ o f ~ s u b g r o u p s } } } \\ { { \mathrm { o f } \ \pi _ { 1 } ( X ) } } \end{array} \} .
$$

If one fixes $\tilde { x } _ { 0 }$ as a basepoint for $\pi _ { 1 } ( { \tilde { X } } )$ , this yields

$$
\left\{ \begin{array} { l } { { \mathrm { C o n n e c t e d ~ c o v e r i n g ~ s p a c e s } } } \\ { { p ; \tilde { X } \longrightarrow X } } \end{array} \right\} _ { / \sim } \equiv \left\{ \mathrm { S u b g r o u p s ~ o f ~ } \pi _ { 1 } ( X ) \right\} .
$$

## Proposition 12.2.8(Number of sheets in a covering space, Hatcher 1.32).

For $X , { \tilde { X } }$ both path-connected, the number of sheets of a covering space is equal to the index

$$
[ p ^ { * } ( \pi _ { 1 } ( { \tilde { X } } ) ) : \pi _ { 1 } ( X ) ] .
$$

Note that the number of sheets is always equal to the cardinality of $p ^ { - 1 } ( x _ { 0 } )$

## 12.2.1 Examples

Example 12.2.9(The circle $S ^ { 1 } )$ : Identify $S ^ { 1 } \subset \mathbb { C }$ , then every map $p _ { n } : S ^ { 1 } \to S ^ { 1 }$ given by $z \mapsto z ^ { n }$ a yields a covering space ${ \tilde { X } } _ { n }$ . The induced map can be described on generators as

$$
\begin{array} { c } { p _ { n } ^ { * } : \pi _ { 1 } ( S ^ { 1 } ) \to \pi _ { 1 } ( S ^ { 1 } ) } \\ { [ \omega _ { 1 } ] \mapsto [ \omega _ { n } ] = n [ \omega _ { 1 } ] } \end{array}
$$

and so the image is isomorphic to nZ and thus

$$
p _ { n } ^ { * } ( \pi _ { 1 } ( S ^ { 1 } ) ) = \operatorname { A u t } _ { \operatorname { C o v } } ( \tilde { X } _ { n } ) = \mathbb { Z } / n \mathbb { Z } .
$$

where the deck transformations are rotations of the circle by $2 \pi / n$ . The universal cover of $S ^ { 1 }$ is R ;   
this is an infinitely sheeted cover, and the fiber above $x _ { 0 }$ has cardinality |Z|.

Example 12.2.10(Projective n-space $\mathbb { R } \mathbb { P } ^ { n } )$ : The universal cover of $\mathbb { R P } ^ { n }$ is $S ^ { n }$ ; this is a twosheeted cover. The fiber above $x _ { 0 }$ contains the two antipodal points.

Example 12.2.11(The torus): The universal cover of $T = S ^ { 1 } \times S ^ { 1 }$ is $\tilde { X } = \mathbb { R } \times \mathbb { R }$ . The fiber above the base point contains every point on the integer lattice $\mathbb { Z } \times \mathbb { Z } = \pi _ { 1 } ( T ) = \operatorname { A u t } ( { \tilde { X } } )$

## Fact 12.2.12

For a wedge product $X = \bigvee _ { i } ^ { n } { \tilde { X } } _ { i }$ , the covering space $\tilde { X }$ is constructed as a infinite tree with n-colored vertices:

• Each vertex corresponds to one of the universal covers ${ \tilde { X } } _ { i } .$

• The color corresponds to which summand ${ \tilde { X } } _ { i }$ appears,

• T The neighborhood of each colored vertex has edges corresponding (not bijectively) to generators of $\pi _ { 1 } ( X _ { i } )$ .

Example 12.2.13(Covering spaces of wedges of spheres): The fundamental group of $S ^ { 1 } \vee S ^ { 1 }$ is $\mathbb { Z } \ast \mathbb { Z } ,$ , and the universal cover is the following 4-valent Cayley graph:

<!-- image-->  
Figure 7: The universal cover of $\ S ^ { 1 } \vee S ^ { 1 }$

See Hatcher p.58 for other covers.

Corollary 12.2.14(Every subgroup of a free group is free). k   
Idea for a particular case: use the fact that $\pi _ { 1 } ( \bigvee S ^ { 1 } ) = \mathbb { Z } ^ { * k }$ , so if $G \leq \mathbb { Z } ^ { * k }$ then there is a   
covering space $X \twoheadrightarrow \bigvee S ^ { 1 }$ such that $\pi _ { 1 } ( X ) = G$ . Since X can be explicitly constructed as a   
graph, i.e. a CW complex with only a 1-skeleton, $\pi _ { 1 } ( X )$ is free on its maximal tree. 

Example 12.2.15(of a universal covering space): The fundamental group of $\mathbb { R P } ^ { 2 } \vee \mathbb { R P } ^ { 2 }$ is $\mathbb { Z } _ { 2 } * \mathbb { Z } _ { 2 }$ , corresponding to an infinite string of copies of 2-valent $S ^ { 2 } \mathrm { s }$ :

<!-- image-->  
Figure 8: Another universal cover.

Example 12.2.16(of a universal covering space): The fundamental group of $\mathbb { R P } ^ { 2 } \vee T ^ { 2 }$ is $\mathbb { Z } _ { 2 } * \mathbb { Z }$ and the universal cover is shown in the following image. Each red vertex corresponds to a copy of $S ^ { 2 }$ covering $\mathbb { R } \mathbb { P } ^ { 2 }$ (having exactly 2 neighbors each), and each blue vertex corresponds to $\mathbb { R } ^ { 2 }$ cover $\mathbb { T } ^ { 2 }$ , with $\left| \mathbb { Z } ^ { 2 } \right|$ many vertices as neighbors.

<!-- image-->  
Figure 9: Universal cover of T2 ∨ RP2

## 12.2.2 Applications

Theorem 12.2.17(Maps into contractible spaces are always nullhomotopic).   
If X is contractible, every map $f : Y \to X$ is nullhomotopic.

Proof (?).

If X is contractible, there is a homotopy $H : X \times I \to X$ between $\operatorname { i d } _ { X }$ and a constant map $c : x \mapsto x _ { 0 }$ . So construct

$$
H ^ { \prime } : Y \times I \to X
$$

$$
H ^ { \prime } ( y , t ) : = { \left\{ \begin{array} { l l } { H ( f ( y ) , 0 ) = ( { \mathrm { i d } } _ { X } \circ f ) ( y ) = f ( y ) } & { t = 0 } \\ { H ( f ( y ) , 1 ) = ( c \circ f ) ( y ) = c ( y ) = x _ { 0 } } & { t = 1 } \\ { H ( f ( y ) , t ) } & { { \mathrm { e l s e } } . } \end{array} \right. }
$$

Then $H ^ { \prime }$ is a homotopy between $f$ and a constant map, and $f$ is nullhomotopic.

Corollary 12.2.18(Factoring through a contractible space implies nullhomotopic).   
Any map $f : X \to Y$ that factors through a contractible space $Z$ is nullhomotopic.

Proof (?).

We have the following situation where $f = p \circ { \tilde { f } } \colon$

<!-- image-->  
Link to diagram

Since every map into a contractible space is nullhomotopic, there is a homotopy ${ \tilde { H } } : Y \times I \to Z$ from $\tilde { f }$ to a constant map $c : Y  Z ,$ say $c ( y ) = z _ { 0 }$ for all $y .$ But then p ◦ ${ \tilde { H } } : X \times I \to Y$ is also a homotopy from $f$ to the map $p \circ c ,$ which satisfies $( p \circ c ) ( y ) = p ( z _ { 0 } ) = x _ { 0 }$ for some $x _ { 0 } \in X$ , and is in particular a constant map.

Proposition 12.2.19(Application: showing one space can not cover another). There is no covering map $p : \mathbb { R P } ^ { 2 }  \mathbb { T } ^ { 2 }$

Proof (?).

• Use the fact that $\pi _ { 1 } ( \mathbb { T } ^ { 2 } ) \cong \mathbb { Z } ^ { 2 }$ and $\pi _ { 1 } ( { \mathbb R } { \mathbb P } ^ { 2 } ) = \mathbb Z / 2 \mathbb Z$ are known.

• The universal cover of $ { \mathbb { T } } ^ { 2 }$ is $\mathbb { R } ^ { 2 }$ , which is contractible.

• Using the following two facts, $p _ { * }$ is the trivial map:

– By the previous results, $p$ is thus nullhomotopic.

– Since $p$ is a covering map, $p _ { * } : \mathbb { Z } / 2 \mathbb { Z } \hookrightarrow \mathbb { Z } ^ { 2 }$ is injective.

• Since p was supposed a cover, this can be used to imply that $\mathrm { i d _ { \mathbb { T } ^ { 2 } } }$ is nullhomotopic.

• Covering maps induce injections on $\pi _ { 1 } .$ , and the only way the trivial map can be injective is if $\pi _ { 1 } ( T ^ { 2 } ) = 0$ , a contradiction.

Theorem 12.2.20(When actions yield covering maps onto their quotients, Hatcher 1.40).

If G y X is a free and properly discontinuous action, then

1. The quotient map $p : X \to X / G$ given by $p ( y ) = G y$ is a normal covering space,

2. If X is path-connected, then $G = \mathrm { A u t } _ { \mathrm { C o v } } ( X )$ is the group of deck transformations for the cover $p ,$

3. If X is path-connected and locally path-connected, then $G \cong \pi _ { 1 } ( X / G ) / p _ { * } ( \pi _ { 1 } ( X ) )$

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

given by the n-valent Cayley graph covering a wedge of circles.

$T ^ { 2 } \xrightarrow { \times 2 } \mathbb { K }$

$\mathbb { Z } / q \mathbb { Z } \to L _ { p / q } { \overset { \pi } { \to } } S ^ { 3 }$

$\mathbb { Z } / n \mathbb { Z } \to \mathbb { C } ^ { * } { \overset { z ^ { n } } { \longrightarrow } } \mathbb { C }$

## 13 CW and Simplicial Complexes

Missing a lot on CW complexes

<!-- image-->

## 13.1 Degrees

<!-- image-->

Fact 13.1.1 (Useful properties of the degree of a map between spheres)

• deg $\operatorname { i d } _ { S ^ { n } } = 1$

• d $\deg ( f \circ g ) = \deg f \cdot \deg g$

• deg r = −1 where r is any rotation about a hyperplane, i.e. $r ( [ x _ { 1 } \cdots x _ { i } \cdot \cdot \cdot x _ { n } ] ) = [ x _ { 1 } \cdot \cdot \cdot - x _ { i } \cdot \cdot \cdot x _ { n } ]$

• The antipodal map on $S ^ { n } \subset \mathbb { R } ^ { n + 1 }$ is the composition of $n + 1$ reflections, so deg $\alpha = ( - 1 ) ^ { n + 1 }$

## 13.2 Examples of CW Complexes/Structures

Example 13.2.1(Spheres): $S ^ { n } = e ^ { 0 } \cup e ^ { n }$ : a point and an n-cell.

Example 13.2.2(Real Projective Space): $\mathbb { R P } ^ { n } = e ^ { 1 } \cup e ^ { 2 } \cup \cdot \cdot \cdot \cup e ^ { n }$ : one cell in each dimension.

Example 13.2.3(Complex Projective Space): $\mathbb { C P } ^ { n } = e ^ { 2 } \cup e ^ { 4 } \cup \cdot \cdot \cdot e ^ { 2 n }$

Examples 4.17. The common surfaces $\mathbb { S } ^ { 2 } , \mathbb { T } ^ { 2 }$ $\mathbb { P } ^ { 2 }$ all have presentations:

(1) The sphere: $\langle a \mid a a ^ { - 1 } \rangle$ or $\langle a , b \mid a b b ^ { - 1 } a ^ { - 1 } \rangle$

The torus: $\langle a , b \mid a b a ^ { - 1 } b ^ { - 1 } \rangle$

(3) The projective plane: $\langle a \mid a a \rangle$ or $\langle a , b \mid a b a b \rangle$

The Klein Bottle: $\langle a , b \mid a b a b ^ { - 1 } \rangle$

<!-- image-->  
FIGURE 14. Polygonal presentation of $\mathbb { S } ^ { 2 } , \mathbb { T } ^ { 2 } , \mathbb { P } ^ { 2 }$ , and K.

Figure 10: Fundamental domains

Example 13.2.4(Surfaces):

## 13.3 Examples of Simplicial Complexes

Remark 13.3.1: To write down a simplicial complex, label the vertices with increasing integers.   
Then each n-cell will correspond to a set of n + 1 of these integers - throw them in a list.

<!-- image-->  
Figure 11: Torus  
Example 13.3.2(Torus):

<!-- image-->

<!-- image-->  
Figure 12: Klein Bottle and $\mathbb { R } \mathbb { P } ^ { 2 }$

Example 13.3.3(Klein Bottle and $\mathbb { R P } ^ { 2 } )$ :

Example 13.3.4(Non-example): For counterexamples, note that this fails to be a triangulation of T :

<!-- image-->  
Figure 13: Not a Torus

This fails - for example, the specification of a simplex [1, 2, 1] does not uniquely determine a triangle in the this picture.

## 13.4 Cellular Homology

$S ^ { n }$ has the CW complex structure of 2 k-cells for each $0 \leq k \leq n$

How to compute:

1. Write cellular complex

$$
0 \to C ^ { n } \to C ^ { n - 1 } \to \cdots C ^ { 2 } \to C ^ { 1 } \to C ^ { 0 } \to 0
$$

2. Compute differentials $\partial _ { i } : C ^ { i } \to C ^ { i - 1 }$

3. Note: $i f C ^ { 0 }$ is a point, $\partial _ { 1 }$ is the zero map.

4. Note: $H _ { n } X = 0 \iff C ^ { n } = \emptyset$

5. Compute degrees: Use $\partial _ { n } ( e _ { i } ^ { n } ) = \sum _ { i } d _ { i } e _ { i } ^ { n - 1 }$ where

$$
d _ { i } = \deg ( \operatorname { A t t a c h } e _ { i } ^ { n } \to \operatorname { C o l l a p s e } X ^ { n - 1 } \mathrm { - s k e l e t o n } ) ,
$$

which is a map $S ^ { n - 1 } \to S ^ { n - 1 }$

Alternatively, choose orientations for both spheres. Then pick a point in the target, and look at points in the fiber. Sum them up with a weight of +1 if the orientations match and -1 otherwise.

6. Note that $\mathbb { Z } ^ { m } \stackrel { f } { \to } \mathbb { Z } ^ { n }$ has an $n \times m$ matrix

7. Row reduce, image is span of rows with pivots. Kernel can be easily found by taking RREF, padding with zeros so matrix is square and has all diagonals, then reading down diagonal - if a zero is encountered on nth element, take that column vector as a basis element with −1 substituted in for the nth entry.

For example:

$$
\begin{array} { r l r } { 1 } & { 2 } & { 0 \quad 2 \quad 1 \quad 2 \quad 0 \quad 2 \quad 1 \quad 2 \quad 0 \quad 2 \ 1 \quad 2 \quad 0 \quad 2 \quad 2 \ 0 \quad 2 } \\ & { 1 } & { 2 \quad 0 \quad 1 \quad - 1  0 \quad 0 \quad 0 \quad 0 \quad 0 \quad 0 \quad 0 \quad 0 \quad 0 \quad 0 } \\ & { 0 \quad 0 \quad 0 \quad 0 \quad 0 \quad 0 \quad 1 \quad - 1 0 \quad 0 \quad 1 \quad - 1 } \\ & { 0 \quad 0 \quad 0 \quad 0 \quad 0 \quad 0 \quad 0 \quad 0 \quad 0 \quad 0 \quad 0 \quad 0 } \\ & { } & { 2 \quad 3 \quad } \\ & { } & { \mathrm { k e r } = \quad 1 \quad 0 \quad } \\ & { } & { 0 \quad - 1 \quad } \\ & { } & { 0 \quad - 1 \quad } \\ & { } & { \mathrm { i m } = \langle a + 2 b + 2 d , c - d \rangle . } \end{array}
$$

6. Or look at elementary divisors, say $n _ { i }$ , then the image is isomorphic to $\bigoplus { n _ { i } \mathbb { Z } }$

## 13.5 Constructing a CW Complex with Prescribed Homology

Given $G = \bigoplus G _ { i }$ , and want a space such that $H _ { i } X \ = \ G ?$ Construct $X \ = \ \backslash X _ { i }$ and then $H _ { i } ( \bigvee X _ { i } ) = \bigoplus H _ { i } X _ { i }$ . Reduces problem to: given a group H, find a space Y such that $H _ { n } ( Y ) = G$ By the structure theorem of finitely generated abelian groups, it suffices to know how to do this for Z and $\mathbb { Z } / n \mathbb { Z }$ , since their powers are just obtained by wedging (previous remark). Recipe:

1. Attach an $e ^ { n }$ to a point to get $H _ { n } = \mathbb { Z }$

2. Attach an $e ^ { n + 1 }$ with attaching map of degree d to get $H _ { n } = \mathbb { Z } _ { d }$

## 14 Homology

## 14.1 Useful Facts

Fact 14.1.1

$H _ { 0 } ( X )$ is a free abelian group on the set of path components of X. Thus if X is path connected, $H _ { 0 } ( X ) \cong \mathbb { Z }$ . In general, $\bar { \cal H } _ { 0 } ( \bar { X } ) \cong \mathbb { Z } ^ { | \pi _ { 0 } ( X ) | }$ , where $| \pi _ { 0 } ( X ) |$ is the number of path components of X.

Proposition 14.1.2(Homology commutes with wedge products).

$$
\tilde { H } _ { * } ( A \vee B ) \cong H _ { * } ( A ) \times H _ { * } ( B )
$$

$$
H _ { n } \left( \bigvee _ { \alpha } X _ { \alpha } \right) \cong \prod _ { \alpha } H _ { n } X _ { \alpha }
$$

See footnote for categorical interpretation.a

a_ is the coproduct in the category $\mathbf { T o p } _ { 0 }$ of pointed topological spaces, and alternatively, X ∨ Y is the pushout in Top of $X \left. \mathrm { p t } \right. Y$

May need some good pair condition?

Example 14.1.3(Application):

$$
H _ { n } ( \bigvee _ { k } S ^ { n } ) = \mathbb { Z } ^ { k } .
$$

Proof (?).

Mayer-Vietoris.

## 4! Warning 14.1.4

$H _ { k } \left( \prod _ { \alpha } X _ { \alpha } \right)$ is not generally equal to $\prod _ { \alpha } \left( H _ { k } X _ { \alpha } \right)$ . The obstruction is due to torsion – if all groups α   
are torsionfree, then the Kunneth theorem3 yields

$$
H _ { k } ( A \times B ) = \prod _ { i + j = k } H _ { i } A \otimes H _ { j } B
$$

3The generalization of Kunneth is as follows: write $\mathcal { P } ( \boldsymbol { n } , \boldsymbol { k } )$ be the set of partitions of n into k parts, i.e. ${ \textbf { x } } \in$

Theorem 14.1.5(Excision).Todo

Excision.

:::{.fact title="Assorted facts}

$H _ { n } ( X ) = 0 \iff X$ has no n-cells.

$C ^ { 0 } X = \mathrm { p t } \implies d _ { 1 } : C ^ { 1 } \to C ^ { 0 }$ is the zero map. :::

<!-- image-->

## 14.2 Known Homology

Example 14.2.1(Spheres):

$$
H _ { i } ( S ^ { n } ) = { \left\{ \begin{array} { l l } { \mathbb { Z } } & { i = 0 , n } \\ { 0 } & { { \mathrm { e l s e } } . } \end{array} \right. }
$$

Example 14.2.2(Real Projective Spaces):

Example 14.2.3(Complex Projective Spaces):

Example 14.2.4(Surfaces):

Homology examples.

<!-- image-->

## 14.3 Mayer-Vietoris

Fact 14.3.1 (Useful algebra fact)

Since Z is free and thus projective, any exact sequence of the form $0 \to \mathbb { Z } ^ { n } \to A \to \mathbb { Z } ^ { m } \to 0$ splits and $A \cong \mathbb { Z } ^ { n } \times \mathbb { Z } ^ { m }$ .

Theorem 14.3.2(Mayer-Vietoris).

Mnemonic: $X = A \cup B  ( \cap , \oplus , \cup )$

Let $X = A ^ { \circ } \cup B ^ { \circ }$ ; then there is a SES of chain complexes

$$
0 \to C _ { n } ( A \cap B ) { \xrightarrow { x \mapsto ( x , - x ) } } C _ { n } ( A ) \oplus C _ { n } ( B ) { \xrightarrow { ( x , y ) \mapsto x + y } } C _ { n } ( A + B ) \to 0
$$

where $C _ { n } ( A + B )$ denotes the chains that are sums of chains in A and chains in B. This yields

${ \mathcal { P } } ( n , k ) \implies \mathbf { x } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { k } ) { \mathrm { ~ w h e r e ~ } } \sum x _ { i } = n .$ . Then

$$
H _ { n } \left( \prod _ { j = 1 } ^ { k } X _ { j } \right) = \bigoplus _ { \mathbf { x } \in \mathcal { P } ( n , k ) } \bigotimes _ { i = 1 } ^ { k } H _ { x _ { i } } ( X _ { i } ) .
$$

a LES in homology:

$$
\begin{array} { r } { \cdot \cdot \cdot H _ { n } ( A \cap B ) \xrightarrow { ( i ^ { * } , j ^ { * } ) } H _ { n } ( A ) \oplus H _ { n } ( B ) \xrightarrow { l ^ { * } - r ^ { * } } H _ { n } ( X ) \xrightarrow { \delta } H _ { n - 1 } ( A \cap B ) \cdot \cdot . . } \end{array}
$$

where

$i : A \cap B \hookrightarrow A$ induces $i ^ { * } : H _ { * } ( A \cap B ) \to H _ { * } ( A )$

$j : A \cap B \hookrightarrow B$ induces $j ^ { * } : H _ { * } ( A \cap B ) \to H _ { * } ( B )$

$l : A \hookrightarrow A \cup B$ induces $l ^ { * } : H _ { * } ( A ) \to H _ { * } ( X )$

$r : B \hookrightarrow A \cup B$ induces $r ^ { * } : H _ { * } ( B ) \to H _ { * } ( X )$

More explicitly,

$$
\begin{array} { r l } & { \qquad \mathrm { L } _ { 2 } = - \mathrm { . . . . } = - \mathrm { . . . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { s i n } _ { 2 } ^ { ( - 1 ) } \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { L } _ { 2 } ^ { \mathrm { e q . } } \mathrm { . } \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { L } _ { 1 } ^ { \mathrm { e q . } } \mathrm { . } \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ & { \qquad \mathrm { . } } \\ &  \qquad \ \end{array}
$$

The connecting homomorphisms $\delta _ { n } : H _ { n } ( X ) \to H _ { n - 1 } ( X )$ are defined by taking a class $[ \alpha ] \in$ $H _ { n } ( X )$ , writing it as an n-cycle z, then decomposing $z = \sum c _ { i }$ where each $c _ { i }$ is an $x + y$ chain. Then $\partial ( c _ { i } ) = \partial ( x + y ) = 0$ , since the boundary of a cycle is zero, so $\partial ( x ) = - \partial ( y )$ . So then just define $\delta ( [ \alpha ] ) = [ \partial x ] = [ - \partial y ]$

Handy mnemonic diagram:

$$
\begin{array} { c c c c } { { } } & { { } } & { { { \stackrel { A \cap B } { } } } } & { { } } & { { } } \\ { { } } & { { \diagup } } & { { \longleftarrow } } & { { \searrow } } & { { \nonumber } } \\ { { } } & { { } } & { { \longleftarrow } } & { { } } & { { A \oplus B } } \end{array} .
$$

Example 14.3.3(Application: computing the homology of a connect sum): $H _ { * } ( A \# B )$ Use the fact that $A \# B = A \cup _ { S ^ { n } }$ B to apply Mayer-Vietoris.

Proposition 14.3.4(Application: isomorphisms in the homology of spheres).

$$
H ^ { i } ( S ^ { n } ) \cong H ^ { i - 1 } ( S ^ { n - 1 } ) .
$$

## Proof .

Write $X = A \cup B ,$ the northern and southern hemispheres, so that $A \cap B = S ^ { n - 1 }$ , the equator. In the LES, we have:

$$
H ^ { i + 1 } ( S ^ { n } )  H ^ { i } ( S ^ { n - 1 } )  H ^ { i } A \oplus H ^ { i } B  H ^ { i } S ^ { n }  H ^ { i - 1 } ( S ^ { n - 1 } )  H ^ { i - 1 } A \oplus H ^ { i - 1 } B .
$$

But A, B are contractible, so $H ^ { i } A = H ^ { i } B = 0 .$ , so we have

$$
H ^ { i + 1 } ( S ^ { n } ) \to H ^ { i } ( S ^ { n - 1 } ) \to 0 \oplus 0 \to H ^ { i } ( S ^ { n } ) \to H ^ { i - 1 } ( S ^ { n - 1 } ) \to 0 .
$$

In particular, we have the shape $0  A  B  0$ in an exact sequence, which is always an isomorphism.

## 14.4 More Exact Sequences

## Theorem 14.4.1(Kunneth).

There exists a short exact sequence

$$
0 \to \prod _ { i + j = k } H _ { j } ( X ; R ) \otimes _ { R } H _ { i } ( Y ; R ) \to H _ { k } ( X \times Y ; R ) \to \prod _ { i + j = k - 1 } \mathrm { T o r } _ { R } ^ { 1 } ( H _ { i } ( X ; R ) , H _ { j } ( Y ; R ) ) .
$$

If R is a free R-module, a PID, or a field, then there is a (non-canonical) splitting given by

$$
H _ { k } ( X \times Y ) \cong \left( \prod _ { i + j = k } H _ { i } X \oplus H _ { j } Y \right) \times \prod _ { i + j = k - 1 } \mathrm { T o r } ( H _ { i } X , H _ { j } Y )
$$

## Theorem 14.4.2(UCT for Change of Group).

For changing coefficients from Z to G an arbitrary group, there are short exact sequences

$$
0 \to H _ { i } X \otimes G \to H _ { i } ( X ; G ) \to \operatorname { T o r } _ { \mathbb { Z } } ^ { 1 } ( H _ { i - 1 } X , G ) \to 0
$$

and

$$
\begin{array} { r } { 0 \to \mathrm { E x t } _ { \mathbb { Z } } ^ { 1 } ( H _ { i - 1 } ( X ; \mathbb { Z } ) , A ) \to H ^ { i } ( X ; A ) \to \mathrm { E x t } _ { \mathbb { Z } } ^ { 0 } ( H _ { i } ( X ; \mathbb { Z } ) , A ) \to 0 } \\ { \Downarrow \Downarrow \qquad \Downarrow \qquad } \end{array}
$$

$$
0 \to \operatorname { E x t } ( H _ { i - 1 } X , G ) \to H ^ { i } ( X ; G ) \to \operatorname { h o m } ( H _ { i } X , G ) \to 0 .
$$

These split unnaturally:

$$
\begin{array} { r l } & { H _ { i } ( X ; G ) = ( H _ { i X } \otimes G ) \oplus \mathrm { T o r } ( H _ { i - 1 } X ; G ) } \\ & { H ^ { i } ( X ; G ) = \mathrm { h o m } ( H _ { i } X , G ) \oplus \mathrm { E x t } ( H _ { i - 1 } X ; G ) } \end{array}
$$

When all of the $H _ { i } X$ are all finitely generated (e.g. if G is a field), writing $H _ { i } ( X ; \mathbb { Z } ) = \mathbb { Z } ^ { \beta _ { i } } \oplus T _ { i }$ as the sum of a free and a torsionfree module, we have

$$
\begin{array} { r l } & { H ^ { i } ( X ; \mathbb { Z } ) \cong \mathbb { Z } ^ { \beta _ { i } } \times T _ { i - 1 } } \\ & { H ^ { i } ( X ; A ) \cong ( H _ { i } ( X ; G ) ) ^ { \vee } : = \hom _ { \mathbb { Z } } ( H _ { i } ( X ; G ) , G ) . } \end{array}
$$

In other words, letting F (−) be the free part and $T ( - )$ be the torsion part, we have

$$
\begin{array} { r l } & { H ^ { i } ( X ; \mathbb { Z } ) = F ( H _ { i } ( X ; \mathbb { Z } ) ) \times T ( H _ { i - 1 } ( X ; \mathbb { Z } ) ) } \\ & { H _ { i } ( X ; \mathbb { Z } ) = F ( H ^ { i } ( X ; \mathbb { Z } ) ) \times T ( H ^ { i + 1 } ( X ; \mathbb { Z } ) ) } \end{array}
$$

Might need assumptions: finite CW complex?

## 14.5 Relative Homology

Fact 14.5.1 (Some assorted facts)

$H _ { n } ( X / A ) \cong { \tilde { H } } _ { n } ( X , A )$ when $A \subset X$ has a neighborhood that deformation retracts onto it.

• LES of a pair

$$
- \ ( A \hookrightarrow X ) \mapsto ( A , X , X / A )
$$

• For CW complexes $X = \left\{ X ^ { ( i ) } \right\}$ , we have

$$
H _ { n } ( X ^ { ( k ) } , X ^ { ( k - 1 ) } ) \cong \left\{ { \begin{array} { l l } { { \mathbb { Z } } [ \{ e ^ { n } \} ] } & { k = n , } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} } \right. \qquad { \mathrm { s i n c e ~ } } X ^ { k } / X ^ { k - 1 } \cong \big \lor S ^ { k }
$$

• Hn(X, A) ∼=? Hn(X/A, pt)

## 15 Fixed Points and Degree Theory

Theorem 15.0.1(Lefschetz Fixed Point). For f : X → X, define the trace of f to be

$$
\Lambda _ { f } : = \sum _ { k \geq 0 } ( - 1 ) ^ { k } \operatorname { T r } ( f _ { * } \mid H _ { k } ( X ; \mathbb { Q } ) )
$$

where $f _ { * } : H _ { k } ( X ; \mathbb { Q } ) \to H _ { k } ( X ; \mathbb { Q } )$ is the induced map on homology. If $\Lambda _ { f } \neq 0$ then f has a fixed point.

Theorem 15.0.2(?).   
Every $f : B ^ { n } \to B ^ { n }$ has a fixed point.

Proof (?).

Proof

Theorem 15.0.3(Hairy Ball).

There is no non-vanishing tangent vector field on even dimensional spheres $S ^ { 2 n }$

Theorem 15.0.4(Borsuk-Ulam).

For every $S ^ { n } \stackrel { f } { \to } \mathbb { R } ^ { n } \exists x \in S ^ { n }$ such that $f ( x ) = f ( - x )$

## 16 Surfaces and Manifolds

Remark 16.0.1: The most common spaces appearing in this theory:

$\mathbb { S } ^ { 2 } .$

$\mathbb { T } ^ { 2 } : = S ^ { 1 } \times S ^ { 1 } .$

$\mathbb { R } \mathbb { P } ^ { 2 }$

• K the Klein bottle

• M the Möbius Strip

$\Sigma _ { n } : = \# _ { i = 1 } ^ { n } \mathbb { T } ^ { 2 } .$

The first 4 can be obtained from the following pasting diagrams:

# Instructions for making common surfaces

<!-- image-->  
Figure 14: Pasting Diagrams for Surfaces

## 16.1 Classification of Surfaces

## Theorem 16.1.1(Classification of Surfaces).

The set of surfaces under connect sum forms a monoid with the presentation

$$
\left. \mathbb { S } ^ { 2 } , \mathbb { R } \mathbb { P } ^ { 2 } , \mathbb { T } \ \middle | \ \mathbb { S } ^ { 2 } = 0 , 3 \mathbb { R } \mathbb { P } ^ { 2 } = \mathbb { R } \mathbb { P } ^ { 2 } + \mathbb { T } ^ { 2 } \right. = \left\{ \Sigma _ { g , n } \ \middle | \ g , n \in \mathbb { Z } ^ { \geq 0 } \right\} .
$$

where $\Sigma _ { g , n }$ is a surface of genus $g$ with n discs removed to form boundary components. Surfaces are classified up to homeomorphism by orientability and $\chi ,$ , or equivalently “genus”

• In orientable case, actual genus, g equals the number of copies of $\mathbb { T } ^ { 2 }$

• In nonorientable case, k equals the number of copies of $\mathbb { R } \mathbb { P } ^ { 2 }$

In each case, there is a formula

$$
\chi ( X ) = { \left\{ \begin{array} { l l } { 2 - 2 g - b } & { { \mathrm { o r i e n t a b l e } } } \\ { 2 - k } & { { \mathrm { n o n - o r i e n t a b l e } } . } \end{array} \right. }
$$

Proposition 16.1.2(Polygon Models for Surfaces).

Every surface can be obtained as the identification space of a polygon labeled with sides $\alpha _ { i } , \beta _ { i } , \rho _ { i }$

<!-- image-->

<!-- image-->

<!-- image-->

Examples, general procedure?

<table><tr><td>Orientable?</td><td>−4</td><td>−3</td><td>-2</td><td>−1</td><td>0</td><td>1</td><td>2</td></tr><tr><td>Yes</td><td> $\Sigma _ { 3 }$ </td><td>Q</td><td> $\Sigma _ { 2 }$ </td><td>O</td><td> $ { \mathbb { T } } ^ { 2 } , S ^ { 1 } \times I$ </td><td> $\mathbb { D } ^ { 2 }$ </td><td> $\mathbb { S } ^ { 2 }$ </td></tr><tr><td>No</td><td>.</td><td>?</td><td>.</td><td>?</td><td>K,M</td><td> $\mathbb { R } \mathbb { P } ^ { 2 }$ </td><td>Q</td></tr></table>

Fact 16.1.3

Proposition 16.1.4(Inclusion-Exclusion).

$$
X = U \cup V \implies \chi ( X ) = \chi ( U ) + \chi ( V ) - \chi ( U \cap V ) .
$$

Proof . Todo

Corollary 16.1.5(Euler for Connect Sums).

$$
\chi ( A \# B ) = \chi ( A ) + \chi ( B ) - 2 .
$$

Proof .

Set $U = A , B = V .$ , then by definition of the connect sum, $A \cap B = \mathbb { S } ^ { 2 } { \mathrm { ~ w h e r e ~ } } \chi ( \mathbb { S } ^ { 2 } ) = 2$

Proposition 16.1.6(Decomposing $\mathbb { R } \mathbb { P } ^ { 2 } )$

$$
\begin{array} { r } { \mathbb { R P } ^ { 2 } = \mathbb { M } \mathbf { \prod } _ { \mathrm { i d } _ { \partial \mathbb { M } } } \mathbb { M } . } \end{array}
$$

Proposition 16.1.7(Decomposing a Klein Bottle).

$$
\mathbb { K } \cong \mathbb { R P } ^ { 2 } \# \mathbb { R P } ^ { 2 } .
$$

Proof . Todo

Proposition 16.1.8(Rewriting a Klein Bottle).

$$
\mathbb { R P } ^ { 2 } \# \mathbb { K } \cong \mathbb { R P } ^ { 2 } \# \mathbb { T } ^ { 2 } .
$$

Proof . Todo

16.2 Manifolds

Remark 16.2.1: To show something is not a manifold, try looking at local homology. Can use point-set style techniques like removing points, i.e. $H _ { 1 } ( X , X - \mathrm { p t } )$ ; this should essentially always yield Z by excision arguments.

Proposition 16.2.2(Dimension vanishing for homology of manifolds). If $M ^ { n }$ is a closed and connected n-manifold, then $H ^ { \geq n } X = 0 .$

Proposition 16.2.3(Top homology for manifolds).   
If $M ^ { n }$ is a closed connected manifold, then $H _ { n } = \mathbb { Z }$ and Tor $\left( H _ { n - 1 } \right) = 0$ . More generally,   
$\left\{ \begin{array} { l l } { { \mathbb Z } } & { M ^ { n } } \\ { 0 } & { \mathrm { e l s e } . } \end{array} \right.$ is orientable

Proposition 16.2.4(Poincaré Duality for manifolds).

For $M ^ { n }$ a closed orientable manifold without boundary and F a field,

$$
H _ { k } ( M ^ { n } ; \mathbb { F } ) \cong H ^ { n - k } ( M ^ { n } ; \mathbb { F } ) \iff M ^ { n }
$$

Proposition 16.2.5(Relative Poincaré Duality for manifolds). If $M ^ { n }$ is a closed orientable manifold with boundary then

$$
H _ { k } ( M ^ { n } ; \mathbb { Z } ) \cong H ^ { n - k } ( M ^ { n } , \partial M ^ { n } ; \mathbb { Z } ) .
$$

Proposition 16.2.6(Known Euler characteristics). If $M ^ { n }$ is closed and n is odd, then $\chi ( M ^ { n } ) = 0$

Proof (?).   
Todo. Uses Poincaré duality?

Proof!

Proposition 16.2.7(Nondegenerate intersection pairings).   
For $M ^ { n }$ closed and orientable, the intersection pairing is nondegenerate modulo torsion.

Proposition 16.2.8(Orientation covers).

For any manifold X there exists a covering space $p : \tilde { X } _ { o } \to X$ , the orientation cover, where any map Y → X factors through $\tilde { X } _ { o }$ . If X is nonorientable, then p is a double cover.

Theorem 16.2.9(Lefschetz Duality). Todo

Statement of Lefschetz duality.

## 16.2.1 3-Manifolds, and Knot Complements

Fact 16.2.10

Every C-manifold is canonically orientable.

Proposition 16.2.11(Homology of 3-manifolds). Let ${ \bar { M } } ^ { 3 }$ be a 3-manifold, then its homology is given by the following (by cases):

• Orientable: $H _ { * } = ( \mathbb { Z } , \mathbb { Z } ^ { r } , \mathbb { Z } ^ { r } , \mathbb { Z } )$

• Nonorientable: $H _ { * } = ( \mathbb { Z } , \mathbb { Z } ^ { r } , \mathbb { Z } ^ { r - 1 } \oplus \mathbb { Z } _ { 2 } , \mathbb { Z } )$

Proposition 16.2.12(Homotopy type of knot complements).

For K a knot, $S ^ { 3 } \backslash K$ is a $K ( \pi , 1 )$ , and $\mathbb { R } ^ { 3 } \backslash K \simeq S ^ { 2 } \vee \left( S ^ { 3 } \backslash K \right)$ . Moreover, if K is nullhomologous and X is any 3-manifold,

$$
H _ { 1 } \left( X \setminus \nu ( K ) \right) \cong H _ { 1 } X \times \mathbb { Z }
$$

where $\nu ( K )$ is a tubular neighborhood of K.

Proof (?). Todo

todo

Proposition 16.2.13(Homology of knot complements in $S ^ { 3 } )$ For K a knot,

$$
H _ { * } ( S ^ { 3 } \setminus K ) = [ \mathbb { Z } , \mathbb { Z } , 0 , 0 , \cdots ] .
$$

Proof .

Apply Mayer-Vietoris, taking $S ^ { 3 } = n ( K ) \cup ( S ^ { 3 } - K )$ , where $n ( K ) \simeq S ^ { 1 }$ and $S ^ { 3 } { - } K \cap n ( K ) \simeq T ^ { 2 }$ Use the fact that $S ^ { 3 } - K$ is a connected, open 3-manifold, so $H ^ { 3 } ( S ^ { 3 } - K ) = 0$

## 17 Extra Problems: Algebraic Topology

## 17.1 Homotopy 101

• Show that if $X { \xrightarrow { f } } X ^ { n }$ is not surjective, then $f$ is nullhomotopic.

• Compute $\pi _ { 1 } ( S ^ { 1 } \vee S ^ { 1 } )$

• Compute $\pi _ { 1 } ( S ^ { 1 } \times S ^ { 1 } )$

## 17.3 Surfaces

• Show that if M orientable ${ \xrightarrow { \pi _ { k } } } M$ non-orientable is a k-fold cover, then k is even or ∞.

• Show that M is orientable if $\pi _ { 1 } ( M )$ has no subgroup of index 2.

## 18 F all 2014

<table><tr><td>18.1 1</td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>

Let $X = \mathbb { R } ^ { 3 } - \Delta ^ { ( 1 ) }$ , the complement of the skeleton of regular tetrahedron, and compute $\pi _ { 1 } ( X )$ and $H _ { * } ( X )$

Lay the graph out flat in the plane, then take a maximal tree - these leaves 3 edges, and so $\pi _ { 1 } ( X ) = \mathbb { Z } ^ { * 3 }$

Moreover $X \simeq S ^ { 1 } \vee S ^ { 1 } \vee S ^ { 1 }$ which has only a 1-skeleton, thus $H _ { * } ( X ) = [ \mathbb { Z } , \mathbb { Z } ^ { 3 } , 0  ]$

Let $X = S ^ { 1 } \times B ^ { 2 } - L$ where L is two linked solid torii inside a larger solid torus. Compute $H _ { * } ( X )$

Solution

Let L be a 3-manifold with homology $[ \mathbb { Z } , \mathbb { Z } _ { 3 } , 0 , \mathbb { Z } , \dots ]$ and let X = $L { \times } \Sigma L$ . Compute $H _ { * } ( X ) , H ^ { * } ( X )$

## Solution:

Useful facts:

$$
\begin{array} { r l } { \bullet } & { H _ { k } ( X \times Y ) \cong \bigoplus _ { i + j = k } H _ { i } ( X ) \otimes H _ { j } ( Y ) \bigoplus _ { i + j = k - 1 } \mathrm { T o r } ( H _ { i } ( X ) , H _ { j } ( Y ) ) } \\ { \bullet } & { \tilde { H } _ { i } ( \Sigma X ) = \tilde { H } _ { i - 1 } ( X ) } \end{array}
$$

We will use the fact that $H _ { * } ( \Sigma L ) = [ \mathbb { Z } , \mathbb { Z } , \mathbb { Z } _ { 3 } , 0 , \mathbb { Z } ] .$

Represent $H _ { * } ( L )$ by $p ( x , y ) = 1 + y x + x ^ { 3 }$ and $H _ { * } ( \Sigma L )$ by $q ( x , y ) = 1 + x + y x ^ { 2 } + x ^ { 4 }$ , we can extract the free part of $H _ { * } ( X )$ by multiplying

$$
p ( x , y ) q ( x , y ) = 1 + ( 1 + y ) x + 2 y x ^ { 2 } + ( y ^ { 2 } + 1 ) x ^ { 3 } + 2 x ^ { 4 } + 2 y x ^ { 5 } + x ^ { 7 }
$$

where multiplication corresponds to the tensor product, addition to the direct sum/product. So the free portion is

$$
\begin{array} { r } { H _ { * } ( X ) = [ \mathbb { Z } , \mathbb { Z } \oplus \mathbb { Z } _ { 3 } , \mathbb { Z } _ { 3 } \otimes \mathbb { Z } _ { 3 } , \mathbb { Z } \oplus \mathbb { Z } _ { 3 } \otimes \mathbb { Z } _ { 3 } , \mathbb { Z } ^ { 2 } , \mathbb { Z } _ { 3 } ^ { 2 } , 0 , \mathbb { Z } ] } \\ { = [ \mathbb { Z } , \mathbb { Z } \oplus \mathbb { Z } _ { 3 } , \mathbb { Z } _ { 3 } , \mathbb { Z } \oplus \mathbb { Z } _ { 3 } , \mathbb { Z } ^ { 2 } , \mathbb { Z } _ { 3 } ^ { 2 } , 0 , \mathbb { Z } ] } \end{array}
$$

We can add in the correction from torsion by noting that only terms of the form Tor $\left( \mathbb { Z } _ { 3 } , \mathbb { Z } _ { 3 } \right) =$ $\mathbb { Z } _ { 3 }$ survive. These come from the terms $i = 1 , j = 2 , \ s o \ i + j = k - 1 \implies k = 1 + 2 + 1 = 4$ and there is thus an additional torsion term appearing in dimension 4. So we have

$$
H _ { * } ( X ) = [ \mathbb { Z } , \mathbb { Z } \times \mathbb { Z } _ { 3 } , \mathbb { Z } _ { 3 } , \mathbb { Z } \times \mathbb { Z } _ { 3 } , \mathbb { Z } ^ { 2 } \times \mathbb { Z } _ { 3 } , \mathbb { Z } _ { 3 } ^ { 2 } , 0 , \mathbb { Z } ]
$$

$$
= [ \mathbb { Z } , \mathbb { Z } , 0 , \mathbb { Z } , \mathbb { Z } ^ { 2 } , 0 , 0 , \mathbb { Z } ] \times [ 0 , \mathbb { Z } _ { 3 } , \mathbb { Z } _ { 3 } , \mathbb { Z } _ { 3 } , \mathbb { Z } _ { 3 } , \mathbb { Z } _ { 3 } ^ { 2 } , 0 , 0 ]
$$

and

$$
\begin{array} { r } { H ^ { * } ( X ) = [ \mathbb { Z } , \mathbb { Z } , 0 , \mathbb { Z } , \mathbb { Z } ^ { 2 } , 0 , 0 , \mathbb { Z } ] \times [ 0 , 0 , \mathbb { Z } _ { 3 } , \mathbb { Z } _ { 3 } , \mathbb { Z } _ { 3 } , \mathbb { Z } _ { 3 } , \mathbb { Z } _ { 3 } ^ { 2 } , 0 ] } \\ { = [ \mathbb { Z } , \mathbb { Z } , \mathbb { Z } _ { 3 } , \mathbb { Z } \times \mathbb { Z } _ { 3 } , \mathbb { Z } ^ { 2 } \times \mathbb { Z } _ { 3 } , \mathbb { Z } _ { 3 } , \mathbb { Z } _ { 3 } ^ { 2 } , \mathbb { Z } ] . } \end{array}
$$

## 18.4 4

Let M be a closed, connected, oriented 4-manifold such that $H _ { 2 } ( M ; \mathbb { Z } )$ has rank 1. Show that there is not a free $\mathbb { Z } _ { 2 }$ action on M .

Solution:

Useful facts:

$X \to \ast _ { \times p } Y$ induces $\chi ( X ) = p \chi ( Y )$

• Moral: always try a simple Euler characteristic argument first!

We know that $H _ { * } ( M ) = [ \mathbb { Z } , A , \mathbb { Z } \times G , A , \mathbb { Z } ]$ for some group A and some torsion group G.

Letting $n = \mathrm { r a n k } ( A )$ and taking the Euler characteristic, we have $\chi ( M ) = ( 1 ) 1 + ( - 1 ) n +$ $( 1 ) 1 + ( - 1 ) n + ( 1 ) 1 = 3 - 2 n$ . Note that this is odd for any n. However, a free action of $\mathbb { Z } _ { 2 } \cap M$ would produce a double covering $M \ \to _ { \times 2 } \ M / \mathbb { Z } _ { 2 } .$ , and multiplicativity of Euler characteristics would force $\chi ( M ) = 2 \chi ( M / \mathbb { Z } _ { 2 } )$ and thus $3 - 2 n = 2 k$ for some integer k. This would require 3 − 2n to be even, so we have a contradiction.

## 18.5 5

Let X be $T ^ { 2 }$ with a 2-cell attached to the interior along a longitude. Compute $\pi _ { 2 } ( X )$

Solution:   
Useful facts:   
$T ^ { 2 } = e ^ { 0 } + e _ { 1 } ^ { 1 } + e _ { 2 } ^ { 1 } + e ^ { 2 }$ as a CW complex.   
$S ^ { 2 } / ( x _ { 0 } \sim x _ { 1 } ) \simeq ^ { - } S ^ { 2 } \wedge S ^ { 1 }$ when $x _ { 0 } , x _ { 1 }$ are two distinct points. (Picture: sphere with a   
string handle connecting north/south poles.)   
$\pi _ { \geq 2 } ( \tilde { X } ) \cong \pi _ { \geq 2 } ( X )$ for ${ \bar { \tilde { X } } }  X$ the universal cover.   
Write $T ^ { 2 } = e ^ { 0 } + e _ { 1 } ^ { 1 } + e _ { 2 } ^ { 1 } + e ^ { 2 } .$ where the first and second 1-cells denote the longitude and   
meridian respectively. By symmetry, we could have equivalently attached a disk to the meridian   
instead of the longitude, filling the center hole in the torus. Contract this disk to a point,   
then pull it vertically in both directions to obtain $S ^ { 2 }$ with two points identified, which is   
homotopy-equivalent to $S ^ { 2 } \vee S _ { 1 }$   
Take the universal cover, which is $\mathbb { R } ^ { 1 } \cup _ { \mathbb { Z } } S ^ { 2 }$ and has the same $\pi _ { 2 }$ . This is homotopy-equivalent   
to $\bigvee S ^ { 2 }$ and so $\pi _ { 2 } ( X ) = \prod \mathbb { Z }$ generated by each distinct copy of $S ^ { 2 }$ . (Alternatively written   
i∈Z i∈Z   
as $\mathbb { Z } [ t , t ^ { - 1 } ] )$

## 19 Summer 2003

## 19.1 1

Describe all possible covering maps between $S ^ { 2 } , T ^ { 2 } , K$

Solution:

## Concepts Used:

1. $\tilde { X }  X$ induces $\pi _ { 1 } ( { \tilde { X } } ) \hookrightarrow \pi _ { 1 } ( X )$

2. $\chi ( \tilde { X } ) = n \chi ( X )$

3. $\pi _ { n } ( X ) = [ S ^ { n } , X ]$

4. $Y  X$ with $\pi _ { 1 } ( Y ) = 0$ and $\tilde { X } \simeq \mathrm { p t } \implies \mathrm { e v e r y } \ Y \stackrel { f } {  } X$ is nullhomotopic.

5. $\pi _ { * } ( T ^ { 2 } ) = [ \mathbb { Z } * \mathbb { Z } , 0 \to ]$

6. $\pi _ { * } ( K ) = [ \mathbb { Z } \rtimes _ { \mathbb { Z } _ { 2 } } \mathbb { Z } , 0 \to ]$

7. Universal covers are homeomorphic.

8. $\pi _ { \geq 2 } ( { \tilde { X } } ) \cong \pi _ { \geq 2 } ( X )$

Spaces

$S ^ { 2 } \twoheadrightarrow T ^ { 2 }$

$S ^ { 2 } \twoheadrightarrow K$

$K \twoheadrightarrow S ^ { 2 }$

$T ^ { 2 } \twoheadrightarrow S ^ { 2 }$

– All covered by the fact that

$$
\mathbb { Z } = \pi _ { 2 } ( S ^ { 2 } ) \neq \pi _ { 2 } ( X ) = 0
$$

for $X = T ^ { 2 } , K .$

$K \twoheadrightarrow T ^ { 2 }$

– Doesn’t cover, would induce $\pi _ { 1 } ( K ) \hookrightarrow \pi _ { 1 } ( T ^ { 2 } ) \implies \mathbb { Z } \times \mathbb { Z } \hookrightarrow \mathbb { Z } ^ { 2 }$ but this would be a non-abelian subgroup of an abelian group.

$T ^ { 2 } \twoheadrightarrow K$

## 19.2 2

Show that $\mathbb { Z } ^ { * 2 }$ has subgroups isomorphic to $\mathbb { Z } ^ { \ast n }$ for every n.

## Solution:

```latex
Concepts Used:
k
1. $\pi _ { 1 } ( \bigvee S ^ { 1 } ) = \mathbb { Z } ^ { * k }$
2. ${ \tilde { X } } \to X \implies \pi _ { 1 } ( { \tilde { X } } ) \hookrightarrow \pi _ { 1 } ( X )$
3. Every subgroup $G \leq \pi _ { 1 } ( X )$ corresponds to a covering space $X _ { G } \twoheadrightarrow X$
4. $A \subseteq B \implies F ( A ) \leq F ( B )$ for free groups.
```

It is easier to prove the stronger claim that $\mathbb { Z } ^ { \mathbb { N } } \leq \mathbb { Z } ^ { * 2 }$ (i.e. the free group on countably many generators) and use fact 4 above. Just take the covering space $\tilde { X } \twoheadrightarrow \mathsf { \bar { \it S } } ^ { 1 } \vee { \cal S } ^ { 1 }$ defined via the gluing map R $\cup _ { \mathbb { Z } } S ^ { 1 }$ which attaches a circle to each integer point, taking 0 as the base point. Then let a denote a translation and b denote traversing a circle, so we have $\pi _ { 1 } ( { \tilde { X } } ) = \left. \cup _ { n \in \mathbb { Z } } a ^ { n } b a ^ { - n } \right.$ which is a free group on countably many generators. Since $\tilde { X }$ is a covering space, $\pi _ { 1 } ( { \tilde { X } } ) \stackrel { \cdot } { \hookrightarrow } \pi _ { 1 } ( S ^ { 1 } \vee S ^ { 1 } ) = { \bar { \mathbb Z } } ^ { * 2 }$ . By 4, we can restrict this to n generators for any n to get a subgroup, and $A \leq B \leq C \implies A \leq C$ as groups.

## 19.3 3

Construct a space having $H _ { * } ( X ) = [ \mathbb { Z } , 0 , 0 , 0 , 0 , \mathbb { Z } _ { 4 } , 0 , \cdot \cdot \cdot ]$

Solution:   
Concepts Used:   
• Construction of Moore Spaces   
• ${ \tilde { H } } _ { n } ( \Sigma X ) = { \tilde { H } } _ { n - 1 } ( X )$ , using $\Sigma X = C _ { X } \cup _ { X } C _ { X }$ and Mayer-Vietoris.   
Take $X = e ^ { 0 } \cup _ { \Phi _ { 1 } } e ^ { 5 } \cup _ { \Phi _ { 2 } } e ^ { 6 }$ , where   
Φ1 : ∂B5 = S4 z 7→z0−−−−→ e0   
Φ2 : ∂B6 = S5 z 7→z4−−−−→ e5.   
where deg $\Phi _ { 2 } = 4 .$

## 19.4 4

Compute H∗ of the complement of a knotted solid torus in $S ^ { 3 }$

## Solution:

## Concepts Used:

$H _ { * } ( T ^ { 2 } ) = [ \mathbb { Z } , \mathbb { Z } ^ { 2 } , \mathbb { Z } , 0  ]$

$$
N ^ { ( 1 ) } \simeq S ^ { 1 } , \mathrm { s o } ~ H _ { > 2 } ( N ) \bar { = } 0 .
$$

$\mathrm { ~ A ~ S E S ~ 0 \to ~ } A \to B \to F \to 0$ with F free splits.

$0 \to A \to B \ { \stackrel { \cong } { \to } } \ C \to D \to 0$ implies $A = D = 0 .$

Let N be the knotted solid torus, so that $\partial N = T ^ { 2 }$ , and let $X = S ^ { 3 } - N$ . Then

$S ^ { 3 } = N \cup _ { T ^ { 2 } } X$

$N \cap X = T ^ { 2 }$

and we apply Mayer-Vietoris to the reduced homology of $S ^ { 3 }$ :

$$
H _ { 4 } ( T ^ { 2 } ) \xrightarrow { } H _ { 4 } ( N ) \oplus H _ { 4 } ( X ) \xrightarrow { } H _ { 4 } ( S ^ { 3 } ) \implies
$$

$$
\widetilde { \longrightarrow H _ { 3 } ( T ^ { 2 } ) } \longrightarrow H _ { 3 } ( N ) \oplus H _ { 3 } ( X ) { { } \longrightarrow } H _ { 3 } ( S ^ { 3 } ) \longrightarrow
$$

$$
\begin{array}{c} \widetilde { \longrightarrow H _ { 2 } ( T ^ { 2 } ) } \longrightarrow H _ { 2 } ( N ) \oplus H _ { 2 } ( X ) { { { \longrightarrow } \atop { { { \longrightarrow } \atop { { \longrightarrow } \atop { { \longrightarrow } \atop { { \longrightarrow } \atop { { \longrightarrow } \atop { { \longrightarrow } \atop { { \longrightarrow } \atop { { \longrightarrow } \atop { \longrightarrow } \atop { { \longrightarrow } \atop { \longrightarrow } \atop { { \longrightarrow } \atop { \longrightarrow } \atop { \longrightarrow } \atop { { \longrightarrow } \atop { \longrightarrow } \atop { \longrightarrow } \atop { { \longrightarrow } \atop { \longrightarrow } \atop { \longrightarrow \atop { \longrightarrow } \atop { \longrightarrow \atop { \longrightarrow } \atop { \longrightarrow \atop { \longrightarrow } \atop { \longrightarrow \atop { \longrightarrow } \atop { \longrightarrow \atop { \longrightarrow } \atop { \longrightarrow \atop { \longrightarrow } \atop { \longrightarrow \atop { \longrightarrow } \atop { \longrightarrow \atop { \longrightarrow } \atop { \longrightarrow \atop \langle { \ Z ^ { 3 } } \atop { \ Z ^ { 3 } } \atop { \longrightarrow \ddots \big } } } } } } } } } } } } } } } } } } } } } } } } } \end{array} 
$$

$$
\textcircled { < } \tilde { H _ { 1 } ( S ^ { 3 } ) } \xrightarrow { } H _ { 1 } ( N ) \oplus H _ { 1 } ( X ) \xrightarrow { } H _ { 1 } ( S ^ { 3 } )
$$

We can plug in known information and deduce some maps:

<!-- image-->

We then deduce:

$H _ { 0 } ( X ) = \mathbb { Z } \colon ?$ (Appeal to some path-connectedness argument?)

$H _ { 1 } ( X ) = \mathbb { Z }$ using the SES appearing on the first row:

$$
0 \to \mathbb { Z } ^ { \oplus 2 } \to \mathbb { Z } \oplus H _ { 1 } ( X ) \to 0
$$

which is thus an isomorphism.

$H _ { 2 } ( X ) = H _ { 3 } ( X ) = 0$ by examining the SES spanning lines 3 and 2:

$$
0 \hookrightarrow H _ { 3 } ( X ) \hookrightarrow \mathbb { Z } \stackrel { \cong _ { \partial _ { 3 } } } { \longrightarrow } \mathbb { Z } \twoheadrightarrow H _ { 2 } ( X ) \twoheadrightarrow 0
$$

Claim: $\partial _ { 3 }$ must be an isomorphism. If this is true, $H _ { 3 } ( X ) \cong \ker \partial _ { 3 } = 0$ and $H _ { 2 } ( X ) \cong$ coker $( \partial _ { 3 } ) : = \mathbb { Z } / \operatorname { i m } ( \partial _ { 3 } ) \cong \mathbb { Z } / \mathbb { Z } = 0$

Why is this true?

## 19.5 5

Compute the homology and cohomology of a closed, connected, oriented 3-manifold M with $\pi _ { 1 } ( M ) =$ $\mathbb { Z } ^ { * 2 }$

## Solution:

Facts used:

• M closed, connected, oriented $\implies H _ { i } ( M ) \cong H ^ { n - i } ( M )$

$H _ { 1 } ( X ) = \mathsf { A b } ( \pi _ { 1 } ( X ) ) .$

• For orientable manifolds $H _ { n } ( M ^ { n } ) = \mathbb { Z }$

## Homology

• Since M is connected, $H _ { 0 } = \mathbb { Z }$

• Since $\pi _ { 1 } ( M ) = \mathbb { Z } ^ { * 2 }$ , H1 is the abelianization and $H _ { 1 } ( X ) = \mathbb { Z } ^ { 2 }$

• Since M is closed/connected/oriented, Poincaré Duality holds and $H _ { 2 } = H ^ { 3 - 2 } = H ^ { 1 }$ $\mathbf { F } H _ { 1 } + \mathbf { T } H _ { 0 }$ by UCT. Since $H _ { 0 } = \mathbb { Z }$ is torsion-free, we have $H _ { 2 } ( M ) = H _ { 1 } ( M ) = \mathbb { Z } ^ { 2 }$

• Since M is an orientable manifold, $H _ { 3 } ( M ) = \mathbb { Z }$

• So $H _ { * } ( M ) = [ \mathbb { Z } , \mathbb { Z } ^ { 2 } , \mathbb { Z } ^ { 2 } , \mathbb { Z } , 0  ]$

## Cohomology

• By Poincaré Duality, $H ^ { * } ( M ) = \widehat { H _ { * } ( M ) } = [ \mathbb { Z } , \mathbb { Z } ^ { 2 } , \mathbb { Z } ^ { 2 } , \mathbb { Z } , 0 , \cdot \cdot \cdot ]$ . (Where the hat denotes reversing the list.)

## 19.6 6

Compute Ext(Z ⊕ Z/2 ⊕ Z/3, Z ⊕ Z/4 ⊕ Z/5).

Solution:

## Concepts Used:

Facts Used:a

• Since Z is a free Z-module,

$$
\operatorname { E x t } ( \mathbb { Z } , \mathbb { Z } / m ) = 0
$$

• Using the usual projective resolution $0 \to \mathbb { Z } \to \mathbb { Z } \to \mathbb { Z } / n \to 0 ,$

$$
\operatorname { E x t } ( \mathbb { Z } / n , \mathbb { Z } ) = \mathbb { Z } / n .
$$

$$
\operatorname { E x t } ( \mathbb { Z } / n , \mathbb { Z } / m ) = ( \mathbb { Z } / m ) / ( n \cdot \mathbb { Z } / m ) \cong ( \mathbb { Z } / m ) / ( d \cdot \mathbb { Z } / m ) \quad { \mathrm { w h e r e ~ } } d : = \operatorname* { g c d } ( m , n ) .
$$

General principle: $\operatorname { E x t } ( \mathbb { Z } / n , G ) = G / n G$

By applying $\mathrm { H o m } ( - , G )$ to the above resolution:

<!-- image-->

which can be identified with:

## Link to Diagram

<!-- image-->

## Link to Diagram

3. Contravariant Hom takes coproducts to products:

$$
\operatorname { E x t } ( \bigoplus _ { i \in I } A _ { i } , \prod _ { k \in K } B _ { k } ) = \prod _ { i \in I } \prod _ { k \in K } \operatorname { E x t } ( A _ { i } , B _ { k } ) .
$$

aThanks to Oskar Henriksson for some fixes/clarifications and further explanations here!

Write

$$
\begin{array} { r l } & { A _ { - } : = A _ { 1 } \oplus A _ { 2 } \oplus A _ { 3 } : = \mathbb { Z } \oplus \mathbb { Z } / 2 \oplus \mathbb { Z } / 3 } \\ & { B _ { - } : = B _ { 1 } \oplus B _ { 2 } \oplus B _ { 3 } : = \mathbb { Z } \oplus \mathbb { Z } / 4 \oplus \mathbb { Z } / 5 . } \end{array}
$$

We can then define the bicomplex

$$
C _ { - , - } : = \operatorname { E x t } ( A _ { - } , B _ { - } ) = \bigoplus _ { 0 \leq i , k \leq 3 } \operatorname { E x t } ( A _ { i } , B _ { k } ) ,
$$

i.e. $C _ { i , k } : = \mathrm { E x t } ( A _ { i } , B _ { k } )$ , which can be organized into the following diagram where we take the Ext at each position and sum them all together:

$$
\operatorname { E x t } ( A _ { 1 } , B _ { 1 } )
$$

$$
\operatorname { E x t } ( A _ { 1 } , B _ { 2 } )
$$

$$
\operatorname { E x t } ( A _ { 1 } , B _ { 3 } )
$$

$$
\operatorname { E x t } ( A _ { 2 } , B _ { 1 } )
$$

$$
\operatorname { E x t } ( A _ { 2 } , B _ { 2 } )
$$

$$
\operatorname { E x t } ( A _ { 2 } , B _ { 3 } )
$$

$$
\operatorname { E x t } ( A _ { 3 } , B _ { 1 } )
$$

$$
\operatorname { E x t } ( A _ { 3 } , B _ { 2 } )
$$

$$
\operatorname { E x t } ( A _ { 3 } , B _ { 3 } )
$$

Link to Diagram

This equals the following:

$$
\operatorname { E x t } ( \mathbb { Z } , \mathbb { Z } / 4 )\tag{Ext(Z, Z}
$$

$$
\operatorname { E x t } ( \mathbb { Z } , \mathbb { Z } / 5 )
$$

$$
\operatorname { E x t } ( \mathbb { Z } / 2 , \mathbb { Z } )
$$

$$
\operatorname { E x t } ( \mathbb { Z } / 2 , \mathbb { Z } / 4 )
$$

$$
\operatorname { E x t } ( \mathbb { Z } / 2 , \mathbb { Z } / 5 )
$$

$$
\operatorname { E x t } ( \mathbb { Z } / 3 , \mathbb { Z } )
$$

$$
\operatorname { E x t } ( \mathbb { Z } / 3 , \mathbb { Z } / 4 )
$$

$$
\operatorname { E x t } ( \mathbb { Z } / 3 , \mathbb { Z } / 5 )
$$

Which simplifies to:

## Link to Diagram

So the answer is Z/2 ⊕ $\mathbb { Z } / 2 \oplus \mathbb { Z } / 3 \cong \mathbb { Z } / 2 \oplus \mathbb { Z } / 6 .$

## 19.7 7

Show there is no homeomorphism $\mathbb { C P } ^ { 2 } \ \underline { { f } } _ { \mathrm { \tiny \textnormal { \tiny { C P } } ^ { 2 } } }$ such that $f ( \mathbb { C P } ^ { 1 } )$ is disjoint from $\mathbb { C P } _ { 1 } \subset \mathbb { C P } _ { 2 }$

## Solution:

## Concepts Used:

1. Every homeomorphism induces isomorphisms on homotopy/homology/cohomology.   
2. $H ^ { * } ( \bar { \mathbb { C P } } ^ { 2 } ) = \mathbb { Z } [ \alpha ] \bar { / } ( \alpha ^ { 2 } )$ where deg $\alpha = 2 .$

3. $[ f ( X ) ] = f _ { * } ( [ X ] )$

$$
a \frown b = 0 \implies a = 0
$$

$$
b = 0
$$

Supposing such a homeomorphism exists, we would have $[ \mathbb { C P } ^ { 1 } ] \ \frown \ [ f ( \mathbb { C P } ^ { 1 } ) ] \ = \ 0$ by the definition of these submanifolds being disjoint. But $[ \mathbb { C P } ^ { 1 } ] \stackrel { \cdot } { \frown } [ f ( \bar { \mathbb { C P } } ^ { 1 } ) ] \stackrel { \cdot } { = } [ \mathbb { C P } ^ { 1 } ] \frown f _ { * } ( [ \mathbb { C P } ^ { 1 } ] )$ where

$$
f _ { * } : H ^ { * } ( \mathbb { C P } ^ { 2 } ) \to H ^ { * } ( \mathbb { C P } ^ { 2 } )
$$

is the induced map on cohomology. Since the intersection pairing is nondegenerate, either $[ \mathbb { C } ^ { \mathbb { P } ^ { 1 } } ] = 0$ or $f _ { * } ( [ \mathbb { C P } ^ { 1 } ] ) = 0$ . We know that $H ^ { * } ( \mathbb { C P } ^ { 2 } ) = \mathbb { Z } [ \alpha ] / \alpha ^ { 2 }$ where $\alpha = [ \mathbb { C P } ^ { 1 } ]$ , however, so this forces $f _ { * } ( [ \mathbb { C P } ^ { 1 } ] ) = 0$ . But since this was a generator of $H ^ { * }$ , we have $f _ { * } \big ( H ^ { * } ( \mathbb { C P } ^ { 2 } ) \big ) = 0$ , so f is not an isomorphism on cohomology.

## 19.8 8

Describe the universal cover of $X = ( S ^ { 1 } \times S ^ { 1 } ) \vee S ^ { 2 }$ and compute $\pi _ { 2 } ( X )$

## Solution:

## Concepts Used:

$\pi _ { \geq 2 } ( { \overline { { X } } } ) \cong \pi _ { \geq 2 } ( X )$ for X the universal cover of X

• Structure of the universal cover of a wedges

$\overline { { T ^ { 2 } } } = \mathbb { R } ^ { 2 }$ and $\overline { { S ^ { 2 } } } = S ^ { 2 }$

• By Mayer-Vietoris, $H _ { n } ( \bigvee X _ { i } ) = \bigoplus H _ { n } ( X _ { i } ) .$

The universal cover can be identified as

$$
{ \overline { { X } } } = \mathbb { R } ^ { 2 } \bigvee _ { i , j \in \mathbb { Z } ^ { 2 } } S ^ { 2 } ,
$$

i.e. the plane with a sphere wedged onto every integer lattice point. We can then check

$$
\begin{array} { l } { \pi _ { 1 } ( X ) \cong \pi _ { 1 } ( X ) } \\ { \quad \quad = \pi _ { 1 } ( \mathbb { R } ^ { 2 } \setminus \bigvee S ^ { 2 } ) } \\ { \quad \quad \quad _ { i , j \in \mathbb { Z } ^ { 2 } } } \\ { \quad \quad = \pi _ { 1 } ( \mathbb { R } ^ { 2 } \setminus \bigvee S ^ { 2 } ) } \\ { \quad \quad = \displaystyle \prod _ { i , j \in \mathbb { Z } ^ { 2 } } \pi _ { 1 } ( \mathbb { R } ^ { 2 } ) \times \pi _ { 1 } ( S ^ { 2 } ) } \\ { \quad \quad \quad = \displaystyle 0 , } \end{array}
$$

using that $\pi _ { 1 } ( S ^ { 2 } ) = 0$ . Then by Hurewicz, $\pi _ { 2 } ( X ) \cong H _ { 2 } ( X )$ , so we can compute

$$
\begin{array} { l } { { \displaystyle H _ { 2 } ( X ) = H _ { 2 } ( { \mathbb R } ^ { 2 } \vee { S } ^ { 2 } ) } } \\ { ~ } \\ { { \displaystyle ~ = ~ \bigoplus _ { i , j \in { \mathbb Z } ^ { 2 } } H _ { 2 } ( { \mathbb R } ^ { 2 } ) \oplus H _ { 2 } ( S ^ { 2 } ) } } \\ { ~ } \\ { { \displaystyle ~ = ~ \bigoplus _ { i , j \in { \mathbb Z } ^ { 2 } } \mathbb Z . } } \end{array}
$$

## 19.9 9

Let $S ^ { 3 }  E  S ^ { 5 }$ be a fiber bundle and compute $H _ { 3 } ( E )$

## Solution (Using the LES in Homotopy):

## Concepts Used:

• Homotopy LES: $F \to E \to B \to \pi _ { * } F ( \ u ) \to \pi _ { * } ( E ) \to \pi _ { * } ( B )$

• Hurewicz: $\pi _ { \leq n } ( X ) = 0 , \pi _ { n } ( X ) \neq 0 \implies \pi _ { n } ( X ) \cong H _ { n } ( X ) .$

• 0 $ A  B  0$ exact iff $A \cong B$

From the LES in homotopy we have

<!-- image-->

and plugging in known information yields

<!-- image-->

• Rows 3 and 4 force $\pi _ { 3 } ( E ) \cong \mathbb { Z } ,$

• Rows 0 and 1 force $\pi _ { 0 } ( E ) = \mathbb { Z }$ (todo: not clear if this is true. . . is it even needed here?)

• The remaining rows force $\pi _ { 1 } ( E ) = \pi _ { 2 } ( E ) = 0$

By Hurewicz, we thus have $H _ { 3 } ( E ) = \pi _ { 3 } ( E ) = \mathbb { Z } .$

Solution (Using the Serre spectral sequence):

Four-corner spectral sequences, only homology in degrees 1,3,5,8. No differentials hit anything!

## 20 Fall 2017 Final

## 20.1 1

Let X be the subspace of the unit cube $I ^ { 3 }$ consisting of the union of the 6 faces and the 4 internal diagonals. Compute $\pi _ { 1 } ( X )$

## 20.2 2

Let X be an arbitrary topological space, and compute $\pi _ { 1 } ( \Sigma X )$

Solution:   
Write $\Sigma X = U \cup V$ where $U = \Sigma X - ( X \times [ 0 , 1 / 2 ] )$ and $U = \Sigma X - X \times [ 1 / 2 , 1 ] )$ . Then   
$U \cap V = X \times \{ 1 / 2 \} \cong X , \operatorname { s o } \pi _ { 1 } ( U \cap V ) = \pi _ { 1 } ( X ) .$   
But both U and V can be identified by the cone on X, given by $C X = \frac { X \times I } { X \times 1 }$ , by just rescaling   
the interval with the maps:   
$i _ { U } : U \to C X$ where $( x , s ) \mapsto ( x , 2 s - 1 )$ (The second component just maps $[ 1 / 2 , 1 ]  [ 0 , 1 ] . ~ )$   
$i _ { V } : V \to C X$ where $( x , s ) \mapsto ( x , 2 s )$ . (The second component just maps $[ 0 , 1 / 2 ]  [ 0 , 1 ] )$   
But CX is contractible by the homotopy $H : C X \times I \to C X$ where $H ( ( c , s ) , t ) = ( c , s ( 1 - t ) )$   
$\operatorname { S o } \pi _ { 1 } ( U ) = \pi _ { 1 } ( V ) = 0$   
By Van Kampen, we have $\pi _ { 1 } ( X ) = 0 * _ { \pi _ { 1 } ( X ) } 0 = 0 .$

## 20.3 3

Let $\ b X = \ b S ^ { 1 } \times \ b S ^ { 1 }$ and $A \subset X$ be a subspace with $A \cong S ^ { 1 } \vee S ^ { 1 }$ . Show that there is no retraction from X to A.

## Solution:

We have $\pi _ { 1 } ( S ^ { 1 } \times S ^ { 1 } ) = \pi _ { 1 } ( S ^ { 1 } ) \times \pi _ { 1 } ( S ^ { 1 } )$ since $S ^ { 1 }$ is path-connected (by a lemma from the problem sets), and this equals $\mathbb { Z } \times \mathbb { Z }$

We also have $\pi _ { 1 } ( S ^ { 1 } \vee S ^ { 1 } ) = \pi _ { 1 } ( S ^ { 1 } ) * _ { \{ p t \} } \pi _ { 1 } ( S ^ { 1 } )$ , which by Van-Kampen is $\mathbb { Z } \ast \mathbb { Z } .$

Suppose X retracts onto A, we can then look at the inclusion $\iota : A \hookrightarrow X$ The induced homomorphism $\iota _ { * } : \pi _ { 1 } ( A ) \hookrightarrow \pi _ { 1 } ( X )$ is then also injective, so we’ve produced an injection from $f : \mathbb { Z } * \mathbb { Z } \hookrightarrow \mathbb { Z } \times \mathbb { Z } .$

This is a contradiction, because no such injection can exists. In particular, the commutator $[ a , b ]$ is nontrivial in the source. But $f ( a b { a } ^ { - 1 } \bar { b } ^ { - 1 } ) = f ( a ) f ( b ) f ( a ) \bar { ^ { - 1 } } f ( b ) ^ { - 1 }$ since f is a homomorphism, but since the target is a commutative group, this has to equal $f ( a ) f ( a ) ^ { - 1 } f ( b ) f ( b ) ^ { - 1 } = e$ So there is a non-trivial element in the kernel of $f ,$ and $f$ can not be injective - a contradiction.

## 20.4 4

```latex
Show that for every map $f : S ^ { 2 } \to S ^ { 1 }$ , there is a point $x \in S ^ { 2 }$ such that $f ( x ) = f ( - x )$
Solution:
Suppose towards a contradiction that f does not possess this property, so there is no $x \in S ^ { 2 }$
such that $f ( x ) = f ( - x )$
Then define $g : S ^ { 2 } \to S ^ { 1 }$ by $g ( x ) = f ( x ) - f ( - x )$ ; by assumption, this is a nontrivial map,
i.e. $g ( x ) \neq 0$ for any $x \in S ^ { 2 }$
In particular, $- g ( - x ) = - ( f ( - x ) - f ( x ) ) = f _ { \scriptscriptstyle ( } x ) - f ( - x ) = g ( x ) , \mathrm { ~ s o ~ } - g ( x ) = g ( - x )$ and
thus g commutes with the antipodal map $\alpha : S ^ { 2 } \to S ^ { 2 } .$
This means $g$ is constant on the fibers of the quotient map $p : S ^ { 2 } \to \mathbb { R P 2 }$ , and thus descends
to a well defined map $\tilde { g } : \mathbb { R P 2 } \to S ^ { 1 }$ , and since $S ^ { 1 } \cong \mathbb { R P 1 }$ , we can identify this with a map
$\tilde { g } : \mathbb { R P 2 }  \mathbb { R P 1 }$ which thus induces a homomorphism $\tilde { g } _ { * } : \pi _ { 1 } ( \mathbb { R P 2 } ) \to \pi _ { 1 } ( \mathbb { R P 1 } )$
Since g was nontrivial, g˜ is nontrivial, and by functoriality of $\pi _ { 1 } , \tilde { g } _ { * }$ is nontrivial.
But $\pi _ { 1 } ( \mathbb { R P 2 } ) = \mathbb { Z } _ { 2 }$ and $\pi _ { 1 } ( \mathbb { R P 1 } ) = \mathbb { Z } .$ , and $\tilde { g } _ { * } : \mathbb { Z } ^ { 2 } \to \mathbb { Z }$ can only be the trivial homomorphism
- a contradiction.
```

## Remark 20.4.1: Alternate Solution Use covering space $\mathbb { R } \twoheadrightarrow S ^ { 1 } ?$

## 20.5 5

How many path-connected 2-fold covering spaces does $S ^ { 1 } \vee$ RP2 have? What are the total spaces?

First note that $\pi _ { 1 } ( X ) = \pi _ { 1 } ( S ^ { 1 } ) * _ { \mathrm { p t } } \pi _ { 1 } ( \mathbb { R P 2 } )$ by Van-Kampen, and this is equal to $\mathbb { Z } * \mathbb { Z } _ { 2 }$

Let $G = < a , b >$ and $H \leq G$ where H =< aba−1b−1, a2ba−2b−1, a−1bab−1, aba− $^ { - 2 } b ^ { - 1 } a >$ . To what well-known group is H isomorphic?

## 21 Appendix: Homological Algebra

## 21.1 Exact Sequences

Proposition 21.1.1(?).   
The sequence $A \xrightarrow { f _ { 1 } } B \xrightarrow { f _ { 2 } } C$ is exact if and only if im fi = ker $f _ { i + 1 }$ and thus $f _ { 2 } \circ f _ { 1 } = 0 .$

Fact 21.1.2

Some useful results:

$0 \to A \hookrightarrow _ { f } B$ is exact iff f is injective

$B \twoheadrightarrow _ { f } C  0$ is exact iff f is surjective

$0  A  B  0$ is exact iff $A \cong B .$

$A \hookrightarrow B \to C \to D \to E { \mathrm { ~ i f f ~ } } C = 0$

$$
0 \to A \to B { \stackrel { \cong } { \to } } C \to D \to 0 { \mathrm { ~ i f f ~ } } A = D = 0 .
$$

– Todo: Proof

$0  A  B  C  0$ splits iff C is free.

• Can think of $C \cong \frac { B } { \operatorname { i m } f _ { 1 } } .$

Definition 21.1.3 (Splitting an exact sequence)   
The sequences splits when a morphism $f _ { 2 } ^ { - 1 } : C \stackrel { \cdot } {  } B$ exists. In Ab, this means $B \cong A \oplus C .$ in   
Grp it’s $B \cong A \rtimes _ { \varphi } C .$

Example 21.1.4(of exact sequences):

$0 \to \mathbb { Z } { \xrightarrow { \times 2 } } \mathbb { Z } { \xrightarrow { \mathrm { m o d ~ 2 } } } { \frac { \mathbb { Z } } { 2 \mathbb { Z } } } \to 0$

$1 \to N \ { \overset { \iota } { \to } } \ G \ { \overset { p } { \to } } \ { \frac { G } { N } } \to 1$

– Groups and normal subgroups

$1 \to { \frac { \mathbb { Z } } { n \mathbb { Z } } } \ { \overset { \iota } { \to } } \ D _ { 2 n } \ { \overset { ? } { \to } } \ { \frac { \mathbb { Z } } { 2 \mathbb { Z } } } \to 1$

– Dihedral group and cyclic groups

$$
\bullet \ 0 \to I \cap J \ { \xrightarrow { \Delta : x \mapsto ( x , x ) } } \ I \oplus J \ { \xrightarrow { f : ( x , y ) \mapsto x - y } } \ I + J \to 0
$$

– R-Modules

$$
\bullet \ : \ : 0  \frac { R } { I \cap J } \xrightarrow { \Delta : x \mapsto ( x , x ) } \frac { R } { I } \oplus \frac { R } { J } \xrightarrow { f : ( x , y ) \mapsto x - y } \frac { R } { I + J } \to 0
$$

$$
\bullet \ 0 \to \mathbb { H } _ { 1 } \overset { \nabla } { \longrightarrow } \mathbb { H } _ { \mathrm { c u r l } } \overset { \nabla \times } { \longrightarrow } \mathbb { H } _ { \mathrm { d i v } } \overset { \nabla \cdot } { \longrightarrow } \mathbb { L } _ { 2 } \to 0
$$

– Since $\nabla \times \nabla F = \nabla \cdot \nabla \times { \bar { v } } = 0$ in Hilbert spaces

Remark 21.1.5: Is $f _ { 1 } \circ f _ { 2 } = 0$ equivalent to exactness..? Answer: yes, every exact sequence is a chain complex with trivial homology. Therefore homology measures the failure of exactness.

Alternatively stated: Exact sequences are chain complexes with no cycles.

Remark 21.1.6: Any LES $A _ { 1 } \to \cdots \to A _ { 6 }$ decomposes into a twisted collection of $\mathrm { S E S } { \mathrm { s } } ;$ define $C _ { k } = \ker ( A _ { k } \to A _ { k + 1 } ) \cong \operatorname { i m } ( A _ { k - 1 } \to A _ { k } ) ) \cong \operatorname { c o k e r } ( A _ { k - 2 } \to A _ { k - 1 } )$ , then all diagonals here are exact:

## 21.2 Five Lemma

## Theorem 21.2.1(?).

If m, p are isomorphisms, l is an surjection, and q is an injection, then n is an isomorphism.   
Proof: diagram chase two “four lemmas”, one on each side. Full proof here.

## 21.3 Free Resolutions

Example 21.3.1(?): The canonical example:

$$
0 \to \mathbb { Z } { \xrightarrow { \times m } } \mathbb { Z } { \xrightarrow { { \pmod { m } } } } \mathbb { Z } _ { m } \to 0
$$

Or more generally for a finitely generated group $G = \langle g _ { 1 } , g _ { 2 } , \cdots , g _ { n } \rangle$

$$
\cdots \to \ker ( f ) \to F [ g _ { 1 } , g _ { 2 } , \cdot \cdot \cdot , g _ { n } ] \stackrel { f } { \to } G \to 0
$$

where F denotes taking the free group.

Every abelian groups has a resolution of this form and length 2.

<!-- image-->

## 21.4 Properties of Tensor Products

<!-- image-->

$A \otimes B \cong B \otimes A$

$( - ) \otimes _ { R } R ^ { n } = \operatorname { i d }$

$\bigoplus A _ { i } \otimes \bigoplus B _ { j } = \bigoplus \bigoplus ( A _ { i } \otimes B _ { j } )$

$\mathbb { Z } _ { m } \otimes \mathbb { Z } _ { n } \overset { J } { = } \mathbb { Z } _ { d }$

$\mathbb { Z } _ { n } \otimes A = A / n A$

<!-- image-->

## 21.5 Properties of Hom

<!-- image-->

$\hom _ { R } ( \bigoplus _ { i } A _ { i } , \prod B _ { j } ) = \bigoplus _ { i } \prod _ { i } \hom ( A _ { i } , B _ { j } )$

• Contravariant in first slot, covariant in second

• Exact over vector spaces

<!-- image-->

## 21.6 Properties of Tor

<!-- image-->

$\operatorname { T o r } _ { R } ^ { 0 } ( A , B ) = A \otimes _ { R } B$

• Tor(M Ai, M B) = M M Tor $( \mathbf { T } A _ { i } , \mathbf { T } B _ { j } )$ where TG is the torsion component of G.

• Tor(Zn, G) = ker(g 7→ ng) = ng ∈ G  ng = 0o

$\operatorname { T o r } ( A , B ) = \operatorname { T o r } ( B , A )$

<!-- image-->

## 21.7 Properties of Ext

<!-- image-->

$\operatorname { E x t } _ { R } ^ { 0 } ( A , B ) = \operatorname { h o m } _ { R } ( A , B )$

• Ext(M Ai, Y Bj ) = M Y Ext(TAi, Bj )

$\operatorname { E x t } ( F , G ) = 0 { \mathrm { ~ i f ~ } } F { \mathrm { ~ i s ~ f r e e } }$

$\operatorname { E x t } ( \mathbb { Z } _ { n } , G ) \cong G / n G$

<!-- image-->

## 21.8 Computing Tor

<!-- image-->

$$
\operatorname { T o r } ( A , B ) = h [ \cdot \cdot \cdot  A _ { n } \otimes B  A _ { n - 1 } \otimes B  \cdot \cdot \cdot A _ { 1 } \otimes B  0 ]
$$

where $A _ { * }$ is any free resolution of A.

Shorthand/mnemonic:

$$
\operatorname { T o r } : { \mathcal { F } } ( A ) \to ( - \otimes B ) \to H _ { * }
$$

<!-- image-->

## 21.9 Computing Ext

$$
\operatorname { E x t } ( A , B ) = h [ \cdot \cdot \cdot \operatorname { h o m } ( A , B _ { n } ) \to \operatorname { h o m } ( A , B _ { n - 1 } ) \to \cdot \cdot \cdot \to \operatorname { h o m } ( A , B _ { 1 } ) \to 0 ]
$$

where $B _ { * }$ is a any free resolution of B.

Shorthand/mnemonic:

$$
\operatorname { E x t } : { \mathcal { F } } ( B ) \to \operatorname { h o m } ( A , - ) \to H _ { * }
$$

<table><tr><td></td><td>21.10 Hom/Ext/Tor Tables</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>hom</td><td> $\mathbb { Z } _ { m }$  Z</td><td>Q</td><td></td></tr><tr><td></td><td></td><td> $\mathbb { Z } _ { d }$  0</td><td>0</td><td></td></tr><tr><td></td><td>0</td><td> $\mathbb { Z } _ { m }$  Z</td><td>Q</td><td></td></tr><tr><td>Q</td><td></td><td>0</td><td>Q</td><td></td></tr><tr><td></td><td>Tor</td><td></td><td></td><td></td></tr><tr><td> $\mathbb { Z } _ { n }$ </td><td> $\mathbb { Z } _ { d }$ </td><td> $\mathbb { Z } _ { m }$ </td><td>Z Q</td><td></td></tr><tr><td>Z</td><td>0</td><td>0 0</td><td>0 0</td><td></td></tr><tr><td>Q</td><td></td><td>0</td><td>0</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ext</td><td></td><td> $\mathbb { Z } _ { m }$  Z</td><td></td><td>Q</td></tr><tr><td> $\mathbb { Z } _ { n }$ </td><td> $\mathbb { Z } _ { d }$ </td><td> $\mathbb { Z } _ { n }$ </td><td></td><td>0</td></tr><tr><td>Z</td><td>0</td><td>0</td><td></td><td></td></tr><tr><td>Q</td><td>0</td><td>Ay/Q</td><td></td><td></td></tr></table>

Where $d = \operatorname* { g c d } ( m , n )$ and $\mathbb { Z } _ { 0 } : = 0$

Things that behave like “the zero functor”:

$\operatorname { E x t } ( \mathbb { Z } , - )$

$\operatorname { T o r } ( - , \mathbb { Z } ) , \operatorname { T o r } ( \mathbb { Z } , - )$

$\operatorname { T o r } ( - , \mathbb { Q } ) , \operatorname { T o r } ( \mathbb { Q } , - )$

Thins that behave like “the identity functor”:

$\mathrm { h o m } ( \mathbb { Z } , - )$

• − ⊗Z Z and $\mathbb { Z } \otimes _ { \mathbb { Z } } -$

For description of $\mathbf { \mathcal { A } _ { \varphi } } ,$ see here. This is a certain ring of adeles.

## 22 Appendix: Unsorted Stuff

• Assorted info about other Lie Groups:

$O _ { n } , U _ { n } , S O _ { n } , S U _ { n } , S p _ { n }$

$\pi _ { k } ( U _ { n } ) = \mathbb { Z } \cdot \mathbb { 1 } \left[ k { \mathrm { ~ o d d } } \right]$

$$
- \ \pi _ { 1 } ( U _ { n } ) = 1
$$

$\pi _ { k } ( S U _ { n } ) = \mathbb { Z } \cdot \mathbb { 1 } \left[ k { \mathrm { ~ o d d } } \right]$

$$
- \ \pi _ { 1 } ( S U _ { n } ) = 0
$$

• πk(Un) = Z/2Z · 1 [k = 0, 1 (mod 8)] + Z · 1 [k = 3, 7 (mod 8)]

• πk(SPn) = Z/2Z · 1 [k = 4, 5 (mod 8)] + Z · 1 [k = 3, 7 (mod 8)]

• Groups and Group Actions

– π0(G) = G for G a discrete topological group.

$$
- \pi _ { k } ( G / H ) = \pi _ { k } ( G ) { \mathrm { ~ i f ~ } } \pi _ { k } ( H ) = \pi _ { k - 1 } ( H ) = 0 .
$$

$- \ \pi _ { 1 } ( X / G ) = \pi _ { 0 } ( G )$ when G acts freely/transitively on X.

## 22.1 Cap and Cup Products

$$
\cup : H ^ { p } \times H ^ { q }  H ^ { p + q } ; ( a ^ { p } \cup b ^ { q } ) ( \sigma ) = a ^ { p } ( \sigma \circ F _ { p } ) b ^ { q } ( \sigma \circ B _ { q } )
$$

where $F _ { p } , B _ { q }$ is embedding into a $p + q$ simplex.

For f continuous, $f ^ { * } ( a \cup b ) = f ^ { * } a \cup f ^ { * } b$

It satisfies the Leibniz rule

$$
\partial ( a ^ { p } \cup b ^ { q } ) = \partial a ^ { p } \cup b ^ { q } + ( - 1 ) ^ { p } ( a ^ { p } \cup \partial b ^ { q } )
$$

$$
\cap : H _ { p } \times H ^ { q } \to H _ { p - q } ; \sigma \cap \psi = \psi ( F \circ \sigma ) ( B \circ \sigma )
$$

where $F , B$ are the front/back face maps.

Given $\psi \in C ^ { q } , \varphi \in C ^ { p } , \sigma : \Delta ^ { p + q }  X$ , we have

$$
\begin{array} { r } { \psi ( \sigma \cap \varphi ) = ( \varphi \cup \psi ) ( \sigma ) } \\ { \langle \varphi \cup \psi , \ \sigma \rangle = \langle \psi , \ \sigma \cap \varphi \rangle } \end{array}
$$

Let $M ^ { n }$ be a closed oriented smooth manifold, and $A ^ { \widehat { i } } , B ^ { \widehat { j } } \subseteq X$ be submanifolds of codimension i and j respectively that intersect transversely (so $\forall p \in A \cap B$ , the inclusion-induced map $T _ { p } A \times T _ { p } B $ $T _ { p } X$ is surjective.)

Then $A \cap B$ is a submanifold of codimension $i + j$ and there is a short exact sequence

$$
0 \to T _ { p } ( A \cap B ) \to T _ { p } A \times T _ { p } B \to T _ { p } X \to 0
$$

which determines an orientation on $A \cap B$

Then the images under inclusion define homology classes

$[ A ] \in H _ { \widehat { i } } X$

$[ B ] \in H _ { \widehat { i } } X$

$[ A \cap B ] { \stackrel { \cdot } { \in } } H _ { \widehat { i + j } } X .$

Denoting their Poincare duals by

$[ A ] \in H ^ { i } X$

$\left[ B \right] ^ { \check { } } \in H ^ { j } X$

$\bar { [ } A \bar { \cap } B \bar { ] } \in H ^ { i + j } X$

We then have

$$
[ A ] ^ { \smile } - [ B ] ^ { \smile } = [ A \cap B ] ^ { \smile } \in H ^ { i + j } X
$$

Example: in $\mathbb { C P } ^ { n }$ , each even-dimensional cohomology $H ^ { 2 i } \mathbb { C P } ^ { n }$ has a generator $\alpha _ { i }$ with is Poincare dual to an bi plane. A generic $\widehat { i }$ plane intersects a $\widehat { j }$ plane in a $\overline { { i + j } }$ plane, yielding $\alpha _ { i } \smile \alpha _ { j } = \alpha _ { i + j }$ for $i + j \le n .$

Example: For $T ^ { 2 }$ , we have - $H _ { 1 } T ^ { 2 } = \mathbb { Z } ^ { 2 }$ generated by $[ A ] , [ B ]$ , the longitudinal and meridian circles.   
$H _ { 0 } T ^ { 2 } = \mathbb { Z }$ generated by $[ p ]$ , the class of a point.

Then $A \cap B = \pm [ p ]$ , and so

$$
[ A ] ^ { \check { } } \smile [ B ] ^ { \check { } } = [ p ] ^ { \check { } }
$$

$$
[ B ] ^ { \smile } \smile [ A ] ^ { \smile } = - [ p ]
$$

<!-- image-->

## 22.2 The Long Exact Sequence of a Pair

<!-- image-->

LES of pair $( A , B ) \implies \cdots H _ { n } ( B ) \to H _ { n } ( A ) \to H _ { n } ( A , B ) \to H _ { n - 1 } ( B ) \cdots$

$$
{ \mathit { \Omega } } _ { ( A , B ) } \subset { \mathit { \Omega } } _ { \longleftarrow } ^ { B } \setminus { \mathit { \Omega } } _ { A }
$$

3.1.3 Example. The cases n = 1,2 and part of the case n = 3 are shown in the figure below.

<!-- image-->  
Figure 3.1: Barycentric subdivision [10].  
Figure 15: Barycentric Subdivision

22.3 Tables
<table><tr><td colspan="17">Homotopy groups of reaprojective spaces</td></tr><tr><td></td><td></td><td> $\pi _ { 1 }$ </td><td> $\pi _ { 2 }$ </td><td> $\pi _ { 3 }$ </td><td> $\pi _ { 4 }$ </td><td> $\pi _ { 5 }$ </td><td> $\pi _ { 6 }$ </td><td> $\pi _ { 7 }$ </td><td> $\pi _ { 8 }$ </td><td> $\pi _ { 9 }$ </td><td> $\pi _ { 1 0 }$ </td><td> $\pi _ { 1 1 }$ </td><td> $\pi _ { 1 2 }$ </td></tr><tr><td> $R P ^ { 1 }$ </td><td>Z</td><td></td><td></td><td></td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td><td>0</td></tr><tr><td> $R P ^ { 2 }$ </td><td> $Z _ { 2 }$ </td><td></td><td>Z 2</td><td></td><td> $Z _ { 2 }$   $Z _ { 2 }$ </td><td> $Z _ { 1 2 }$ </td><td> $Z _ { 2 }$ </td><td></td><td> $Z _ { 2 }$ </td><td> $Z _ { 3 }$ </td><td> $Z _ { 1 5 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 } \times Z _ { 2 }$ </td></tr><tr><td> $R P ^ { 3 }$ </td><td> $Z _ { 2 }$ </td><td>0</td><td>Z</td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 1 2 }$ </td><td> $Z _ { 2 }$ </td><td></td><td> $Z _ { 2 }$ </td><td> $Z _ { 3 }$ </td><td> $Z _ { 1 5 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 } \times Z _ { 2 }$ </td></tr><tr><td> $R P ^ { 4 }$ </td><td> $Z _ { 2 }$ </td><td>0</td><td></td><td>0 Z</td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z \times Z _ { 1 2 }$ </td><td></td><td> $Z _ { 2 } \times Z _ { 2 }$ </td><td> $Z _ { 2 } \times Z _ { 2 }$ </td><td> $Z _ { 2 4 } \times Z _ { 3 }$ </td><td> $Z _ { 1 5 }$ </td><td> $Z _ { 2 }$ </td></tr></table>

Figure 16: Higher homotopy groups of $\mathbb { R P } ^ { n }$
<table><tr><td colspan="10">Homotopy groups of complex projective spaces</td></tr><tr><td></td><td> $\pi _ { 1 }$ </td><td> $\pi _ { 2 }$   $\pi _ { 3 }$ </td><td> $\pi _ { 4 }$ </td><td> $\pi _ { 5 }$ </td><td> $\pi _ { 6 }$ </td><td> $\pi _ { 7 }$ </td><td> $\pi _ { 8 }$ </td><td> $\pi _ { 9 }$ </td><td> $\pi _ { 1 0 }$ </td><td> $\pi _ { 1 1 }$ </td><td> $\pi _ { 1 2 }$ </td></tr><tr><td> $C P ^ { 1 }$ </td><td>0</td><td>Z</td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 1 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 3 }$ </td><td> $Z _ { 1 5 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 } \times Z _ { 2 }$ </td></tr><tr><td> $C P ^ { 2 }$ </td><td>0</td><td>Z 0</td><td>0</td><td>Z</td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 4 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 3 0 }$ </td></tr><tr><td> $C P ^ { 3 }$ </td><td>0</td><td>Z 0</td><td></td><td></td><td>0</td><td>Z</td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 4 }$ </td><td>0</td><td>0</td></tr><tr><td> $C P ^ { 4 }$ </td><td>0</td><td></td><td>Z 0 0 0</td><td></td><td>0</td><td>0</td><td>0</td><td>Z</td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 4 }$ </td></tr></table>

Figure 17: Higher homotopy groups of $\mathbb { C P } ^ { n }$

<table><tr><td colspan="12">Homotopy groups of spheres</td></tr><tr><td></td><td> $\pi _ { 1 }$   $\pi _ { 2 }$ </td><td> $\pi _ { 3 }$ </td><td> $\pi _ { 4 }$ </td><td> $\pi _ { 5 }$ </td><td> $\pi _ { 6 }$ </td><td> $\pi _ { 7 }$ </td><td> $\pi _ { 8 }$ </td><td> $\pi _ { 9 }$ </td><td> $\pi _ { 1 0 }$ </td><td> $\pi _ { 1 1 }$ </td><td> $\pi _ { 1 2 }$ </td></tr><tr><td> $S ^ { 1 }$ </td><td>Z</td><td></td><td></td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $S ^ { 2 }$ </td><td>0</td><td>Z Z</td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 1 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 3 }$ </td><td> $Z _ { 1 5 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 } \times Z _ { 2 }$ </td></tr><tr><td> $S ^ { 3 }$ </td><td>0</td><td>0</td><td>Z  $\boxed { Z _ { 2 } }$ </td><td>My  $Z _ { 2 }$ </td><td> $Z _ { 1 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 3 }$ </td><td> $Z _ { 1 5 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 } \times Z _ { 2 }$ </td></tr><tr><td> $S ^ { 4 }$ </td><td>0</td><td></td><td>0 Z</td><td> $Z _ { 2 }$ </td><td> $\boxed { Z _ { 2 } }$ </td><td> $Z \times Z _ { 1 2 }$ </td><td> $Z _ { 2 } \times Z _ { 2 }$ </td><td> $Z _ { 2 } \times Z _ { 2 }$ </td><td> $Z _ { 2 4 } \times Z _ { 3 }$ </td><td> $Z _ { 1 5 }$ </td><td> $Z _ { 2 }$ </td></tr><tr><td> $S ^ { 5 }$ </td><td>0</td><td>0 0</td><td>0</td><td>Z</td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $\boxed { Z _ { 2 4 } }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 3 0 }$ </td></tr><tr><td> $S ^ { 6 }$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>Z</td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 4 }$ </td><td>D</td><td>Z</td><td> $Z _ { 2 }$ </td></tr><tr><td> $S ^ { 7 }$ </td><td>0 0 0 0 0</td><td></td><td></td><td></td><td>0</td><td>Z</td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 4 }$ </td><td>0</td><td>D</td></tr><tr><td> $S ^ { 8 }$ </td><td>0 0 0 0 0</td><td></td><td></td><td></td><td>0</td><td>0</td><td>Z</td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 4 }$ </td><td>0</td></tr></table>

Figure 18: Homotopy groups of spheres.

A1.1.3.4 Exceptional groups
<table><tr><td colspan="10">Homotopy groups of exceptional groups</td></tr><tr><td></td><td> $\pi _ { 1 }$ </td><td> $\pi _ { 2 }$ </td><td> $\pi _ { 3 }$   $\pi _ { 4 }$ </td><td> $\pi _ { 5 }$ </td><td> $\pi _ { 6 }$ </td><td> $\pi _ { 7 }$ </td><td> $\pi _ { 8 }$   $\pi _ { 9 }$ </td><td> $\pi _ { 1 0 }$ </td><td> $\pi _ { 1 1 }$ </td><td> $\pi _ { 1 2 }$ </td></tr><tr><td> $G _ { 2 }$ </td><td></td><td></td><td></td><td>0 0 Z 0 0</td><td> $Z _ { 3 }$ </td><td>0  $Z _ { 2 }$ </td><td> $Z _ { 6 }$ </td><td>0</td><td> $Z \times Z _ { 2 }$ </td><td>0</td></tr><tr><td> $F _ { 4 }$ </td><td></td><td></td><td></td><td></td><td>0 0 Z 0 0 0 0</td><td> $Z _ { 2 }$ </td><td> $Z _ { 2 }$ </td><td>0</td><td> $Z \times Z _ { 2 }$ </td><td>0</td></tr><tr><td> $E _ { 6 }$ </td><td></td><td></td><td></td><td></td><td>0 0 Z 0 0 0 0</td><td></td><td>0 Z 0</td><td></td><td>Z</td><td> $Z _ { 1 2 }$ </td></tr><tr><td> $E _ { 7 }$ </td><td></td><td></td><td></td><td></td><td>0 0 Z 0 0 0</td><td>0</td><td>0 0</td><td>0</td><td>Z</td><td> $Z _ { 2 }$ </td></tr><tr><td> $E _ { 8 }$ </td><td></td><td></td><td></td><td></td><td>0 0 Z 0 0 0 0 0 0</td><td></td><td></td><td>0</td><td>0</td><td>0</td></tr></table>

Figure 19: Homotopy groups of exceptional groups

## 22.4 Homotopy Groups of Lie Groups

$$
\bullet \ O ( n ) \colon \pi _ { k } O _ { n } = ?
$$

$U ( n ) : \pi _ { k } U _ { n }$ is Z in odd degrees and $\pi _ { 1 } U _ { n } = 1$

$S U ( n ) : \pi _ { k } U _ { n }$ is Z in odd degrees and $\pi _ { 1 } U _ { n } = 0$

$U _ { n } : \pi _ { k } ( U _ { n } )$ is $\mathbb { Z } / 2 \mathbb { Z }$ in degrees?

## 22.5 Higher Homotopy

$n \geq 2 \implies \pi _ { n } ( X ) \in \mathbf { A b }$

$\Sigma S ^ { n } = S ^ { n + 1 }$

$[ \Sigma ^ { n } X , Y ] \cong [ X , \Omega ^ { n } Y ]$

$\pi * n ( \Omega X ) = \pi * n + 1 ( X )$

$$
- \ \pi _ { n } ( X ) \cong \pi _ { 0 } ( \Omega ^ { n } X )
$$

• n ≥ 2 =⇒ πn(S1) = 0

$k < n \implies \pi _ { k } ( S ^ { n } ) = 0$

$\pi _ { n } ( X )$ is the obstruction to $f : S ^ { n } \to X$ being lifted to ${ \widehat { f } } : D ^ { n + 1 }$ → X

$\pi _ { n } ( X ) \cong H _ { n } ( X )$ for the first n such that $\pi _ { n } ( X ) \neq 0 ; \forall k < n , ~ H _ { k } ( X ) = 0 ,$

$$
k + 2 \leq 2 n \implies \pi _ { k } ( S ^ { n } ) \cong \pi _ { k + 1 } ( S ^ { n + 1 } )
$$

$\pi _ { k } ( S ^ { n } ) = \pi _ { k + 1 } S ^ { n + 1 } = \cdots = \pi _ { k + i } S ^ { n + i }$

$F  E  B$ a fibration yields $\cdots \pi _ { n } ( F ) \to \pi _ { n } ( E ) \to \pi _ { n } ( B ) \to \pi * n - 1 ( F ) \cdot \cdot \cdot$

• Freundenthal suspension, stable homotopy groups

## 22.6 Higher Homotopy Groups of the Sphere

$\pi _ { n } ( S ^ { n } ) = \mathbb { Z }$

$\pi _ { n + 1 } S ^ { n } = \mathbb { Z } _ { 2 }$ for $n \geq 4$

$\pi _ { n + 2 } ( S ^ { n } ) \cong \mathbb { Z } _ { 2 }$

$\pi _ { n + 3 } S ^ { n } = \mathbb { Z } _ { 8 }$ for $n \geq 5$

$\pi _ { 5 } S ^ { 2 } = \mathbb { Z } _ { 2 }$

$\pi _ { 6 } S ^ { 3 } = \mathbb { Z } _ { 4 }$

$\pi _ { 7 } S ^ { 4 } = \mathbb { Z } \oplus \mathbb { Z } _ { 4 }$

$\pi _ { k } S ^ { 2 } \cong \pi _ { k } S ^ { 3 }$

$\pi _ { 3 } S ^ { 2 } \cong \mathbb { Z }$

$\pi _ { 4 } S ^ { 2 } \cong \mathbb { Z } _ { 2 }$

<!-- image-->

## 22.7 Misc

<!-- image-->

$\Omega ( - )$ is an exact functor.

<!-- image-->

## 22.8 Building a Moore Space

<!-- image-->

• To build a Moore space $M ( n , \mathbb { Z } _ { p } )$ , take $X = S ^ { n }$ and attach $e ^ { n + 1 }$ via a map $\Phi : S ^ { n } = \partial B ^ { n + 1 } $ $X ^ { ( n ) } = S ^ { n }$ of degree p.

– To obtain $M ( n , \prod G _ { i } )$ take the corresponding $\vee X _ { i }$

– Can also use Mayer Vietoris to conclude $H _ { n + 1 } ( \dot { \Sigma } X ) = H _ { n } ( X )$ , and just suspend spaces with known homology.

## Bibliography

[1] Allen Hatcher. Algebraic Topology. Cambridge University Press, 2002.

[2] James Raymond Munkres. Topology. Pearson, 2018.
