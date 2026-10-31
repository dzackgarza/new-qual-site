## ALGEBRAIC TOPOLOGY I: FALL 2008

## TIM PERUTZ

## Contents

I. The fundamental group 3   
1. Introduction 3   
1.1. Homotopy equivalence 3   
1.2. The fundamental groupoid 4   
2. The fundamental group of the circle 6   
2.1. Trivial loops 6   
2.2. Computing π1(S1) 6   
2.3. Applications 7   
3. Van Kampen in theory 9   
3.1. Group presentations 9   
3.2. Push-outs 9   
3.3. Van Kampen’s theorem 11   
4. Van Kampen in practice 13   
4.1. Fundamental groups of spheres 13   
4.2. A useful lemma 13   
4.3. Fundamental groups of compact surfaces 13   
4.4. The complement of a trefoil knot 15   
5. Covering spaces 17   
5.1. Deck transformations 18   
5.2. Examples 18   
5.3. Unique path lifting 19   
6. Classifying covering spaces 21   
6.1. An equivalence of categories 21   
6.2. Existence of a simply connected covering space 23   
II. Singular homology theory 25   
7. Singular homology 25   
7.1. The definition 25   
7.2. The zeroth homology group 26   
7.3. The first homology group 26   
8. Simplicial complexes and singular homology 28   
8.1. ∆-complexes 28   
8.2. The Hurewicz map revisited 29   
9. Homological algebra 30   
9.1. Exact sequences 30   
9.2. Chain complexes 31   
10. Homotopy invariance of singular homology 34   
11. The locality property of singular chains 37   
12. Mayer–Vietoris and the homology of spheres 39

## TIM PERUTZ

12.1. The Mayer–Vietoris sequence 39   
12.2. Degree 41   
13. Relative homology and excision 42   
13.1. Relative homology 42   
13.2. Suspension 43   
13.3. Summary of the properties of relative homology 44   
14. Vanishing theorems for homology of manifolds 45   
14.1. Local homology 46   
14.2. Homology in dimension n 46   
15. Orientations and fundamental classes 49   
15.1. Homology with coefficients 49   
15.2. What it’s good for 49   
15.3. The local homology cover 49   
15.4. Orientations 50   
15.5. Fundamental classes 50   
16. Universal coefficients 53   
16.1. Homology with coefficients 53   
16.2. Tor 53   
16.3. Universal coefficients 55   
III. Cellular homology 57   
17. CW complexes 57   
17.1. Compact generation 59   
17.2. Degree matrices 59   
17.3. Cellular approximation 59   
18. Cellular homology 61   
19. Cellular homology calculations 64   
19.1. Calculations 64   
20. The Eilenberg–Steenrod axioms 67   
IV. Product structures 70   
21. Cohomology 70   
21.1. Ext 71   
22. Product structures, formally 74   
22.1. The evaluation pairing 74   
22.2. The cup product 74   
22.3. The cap product 75   
23. Formal computations in cohomology 77   
23.1. The K¨unneth formula 78   
23.2. An algebraic application of cup product 78   
24. Cup products defined 80   
24.1. The basic mechanism 80   
24.2. Cup products in cellular cohomology 80   
24.3. Cup products in singular cohomology 81   
25. Non-commutativity 83   
26. Poincar´e duality 84

## I. The fundamental group

## 1. Introduction

We explain that algebraic topology aims to distinguish homotopy types. We introduce the fundamental groupoid and the fundamental group.

## 1.1. Homotopy equivalence.

1.1.1. A topological space is a set X equipped with a distinguished collection of subsets, called ‘open’. The collection must be closed under finite intersections and arbitrary unions. In particular, it includes the empty union ∅, and the empty intersection X.

A map $X \  \ Y$ between topological spaces is continuous if the preimage of every open set in Y is open in X. A homeomorphism is a continuous map with a continuous two-sided inverse.

Convention: In this course, ‘map’ will mean ‘continuous map’.

1.1.2. Elementary properties of spaces that are preserved by homeomorphism $\left( \mathrm { e . g . } \right.$ the Hausdorff property, compactness, connectedness, path-connectedness) allow us to distinguish some spaces. For instance, the interval [0, 1] is not homeomorphic to the circle $S ^ { 1 } = \mathbb { R } / \mathbb { Z }$ because $[ 0 , 1 ] \setminus \{ 1 / 2 \}$ is disconnected, whilst $S ^ { 1 } \setminus \{ x \}$ is connected for any $x \in S ^ { 1 }$ . The spaces $\textstyle { \dot { X _ { n } } } = { \dot { \mathsf { V } } } _ { i = 1 } ^ { n } S ^ { 1 }$ (the wedge product, or onepoint union, of n copies of $S ^ { 1 } )$ are all distinct, because it is possible to delete $n ,$ but not $n + 1$ , distinct points of $X _ { n }$ without disconnecting it.

However, if we thickened the circles in $X _ { n }$ to ribbons, making a space $Y _ { n }$ , the argument would fail. In algebraic topology, one looks for invariants of spaces which are insensitive to such thickenings, so that if they distinguish the $X _ { n }$ they also distinguish the $Y _ { n }$

Definition 1.1. If $f _ { 0 } , f _ { 1 } \colon X \to Y$ are maps, a homotopy from $X  Y$ is a map $F \colon [ 0 , 1 ] \times X \to Y$ such that $F \circ i _ { t } = f _ { t }$ for $t \in \{ 0 , 1 \}$ , where $i _ { t } ( x ) = ( t , x ) \in [ 0 , 1 ] \times X$ We often think of F as a path $\{ f _ { t } \} _ { t \in [ 0 , 1 ] }$ of maps $f _ { t } \colon X \to Y$

Homotopy defines an equivalence relation on the set of maps $f \colon X \to Y$ , which we denote by the symbol '.

Definition 1.2. A homotopy equivalence is a map $f \colon X \to Y$ such that there exists $g \colon Y \to X$ which is an inverse up to homotopy. That is, $f \circ g \simeq \operatorname { i d } _ { Y }$ and $g \circ f \simeq \operatorname { i d } _ { X }$

Exercise 1.1: Homotopy equivalence defines an equivalence relation on spaces.

The equivalence classes are called homotopy types. Algebraic topology provides a collection of invariants of homotopy types. The principal invariants are the fundamental group and the homology groups, and the homomorphisms between these groups associated with maps between spaces.

Exercise 1.2: The following equivalent conditions define what is means for a non-empty space X to be contractible. Check their equivalence.

• X is homotopy equivalent to a one-point space.

• For every $x \in X$ , the inclusion $\{ x \} \to X$ is a homotopy equivalence.

• For some $x \in X$ , the inclusion $\{ x \} \to X$ is a homotopy equivalence.

• For some $x \in X$ , the constant map $c _ { x } \colon X \to X$ at x is homotopic to idX .

Exercise 1.3: Any convex subset of $\mathbb { R } ^ { n }$ is contractible.

Convex subsets of $\mathbb { R } ^ { n }$ are contractible for a particular reason: their points are deformation retracts. In general, if X is a space and $i \colon A \to X$ the inclusion of a subspace, we say that A is a deformation retract of X if there is a map $r \colon X \to A$ such that $r \circ i = \operatorname { i d } _ { A }$ and $i \circ r \simeq \operatorname { i d } _ { X }$ by a homotopy $\left\{ h _ { t } \right\}$ so that (in addition to $h _ { 0 } = i \circ r$ and $h _ { 1 } = \operatorname { i d } _ { X } \quad$ one has $h _ { t } ( a ) = a$ for all t and $a \in A$ . Such a map r, called a deformation retraction, is obviously a homotopy equivalence.

Exercise 1.4: Show carefully that the letter A, considered as a union of closed line segments in $\mathbb { R } ^ { 2 }$ , is homotopy equivalent but not homeomorphic to the letter O. Show briefly that all but one of the capital letters of the alphabet is either contractible or deformation-retracts to a subspace homeomorphic to O. Show that the letters fall into exactly three homotopy types. How many homeomorphism types are there? (View a letter as a finite union of the images of paths $[ 0 , 1 ] \to \mathbb { R } ^ { 2 }$ . Choose a typeface!)

Exercise 1.5: Let $\{ X _ { \alpha } \} _ { \alpha \in A }$ be a collection of spaces indexed by a set A. Let $x _ { \alpha } \in X _ { \alpha }$ be basepoints. Define the wedge sum (or 1-point union) $\vee _ { \alpha \in A } X _ { \alpha }$ as the quotient space of the disjoint union $\operatorname { I I } _ { \alpha } X _ { \alpha }$ by the equivalence relation $x _ { \alpha } \sim x _ { \beta }$ for all $\alpha , ~ \beta \in { \cal A }$ Show carefully that, for $n \geq 1$ , the complement of p distinct points in $\mathbb { R } ^ { n }$ is homotopyequivalent to the wedge sum of p copies of the sphere $S ^ { n - 1 } = \{ x \in \mathbb { R } ^ { n } : | x | = 1 \}$

Remark. Let’s look ahead. Theorems of Hurewicz and J. H. C. Whitehead imply that, among all spaces which are cell complexes, the sphere $S ^ { n } = \{ x \in \mathbb { R } ^ { n + 1 }$ : $| x | = 1 \}$ , with $n > 1$ , is characterized up to homotopy equivalence by its homology groups ${ \bf \zeta } ^ { H _ { 0 } ( S ^ { n } ) } \cong H _ { n } ( S ^ { n } ) \cong \mathbb { Z } , H _ { i } ( S ^ { n } ) = 0$ for $i \notin \{ 0 , 1 \}$ and its trivial fundamental group. In general, distinct homotopy types can have trivial fundamental groups and isomorphic homology groups (e.g. $S ^ { \dot { 2 } } \times S ^ { 2 } , \mathbb { C } P ^ { 2 } \# \mathbb { C } P ^ { 2 } )$ . Another invariant, the cohomology ring, distinguishes these two examples. When it fails to distinguish spaces, one localizes the problem and works over $\mathbb { Q }$ and mod primes $p .$ . Over $\mathbb { Q } .$ , a certain commutative differential graded algebra gives a new invariant [D. Sullivan, Infinitesimal computations in topology, Publ. Math. I.H.E.S. (1977)]. Mod $p ,$ one considers the Steenrod operations on cohomology. There is an algebraic structure which captures all this at once, and gives a complete invariant for the homotopy type of cell complexes with trivial fundamental group [M. Mandell, Cochains and homotopy type, Publ. Math. I.H.E.S. (2006)].

## 1.2. The fundamental groupoid.

1.2.1. Our first invariants of homotopy type are the fundamental groupoid and the isomorphism class of the fundamental group.

A path in a space X is a map $f \colon I \to X$ , where $I = [ 0 , 1 ]$ . Two paths $f _ { 0 }$ and $f _ { 1 }$ are homotopic rel endpoints if there is a homotopy $\{ f _ { t } \} _ { t \in [ 0 , 1 ] }$ between them such that $f _ { t } ( 0 )$ and $f _ { t } ( 1 )$ are both independent of t. Write ∼ for the equivalence relation of homotopy rel endpoints.

Two paths f and g are composable if $f ( 1 ) = g ( 0 )$ . In this case, their composite $f \cdot g$ is the result of traversing first $f ,$ then g, both at double speed: $( f \cdot g ) ( t ) = f ( 2 t )$ for $t \in [ 0 , 1 / 2 ]$ and $( f \cdot g ) ( t ) = g ( 2 t - 1 )$ for $t \in [ 1 / 2 , 1 ]$

The composition operation is not associative: $( f \cdot g ) \cdot h \neq f \cdot ( g \cdot h )$ . What is true, however, is that $( f \cdot g ) \cdot h \sim f \cdot ( g \cdot h )$ . (Proof by picture.)

If f is a path, let $f ^ { - 1 }$ denote the reversed path: $f ^ { - 1 } ( t ) = f ( 1 - t )$ . One has $f \cdot f ^ { - 1 } \sim c _ { f ( 0 ) }$ and $f ^ { - 1 } \cdot f \sim c _ { f ( 1 ) }$ , where $c _ { x }$ denotes the constant path at x. (Picture.) Moreover, $c _ { f ( 0 ) } \cdot f \simeq f$ and $f \cdot c _ { f ( 1 ) } \simeq f$

We now define a category $\Pi _ { 1 } ( X )$ , the fundamental groupoid of X. A category consists of a collection (for instance, a set) of objects, and for any pair of objects $( x , y )$ , a set $\operatorname { M o r } ( x , y )$ of ‘morphisms’ $( \mathrm { o r } \ \cdot \mathrm { m a p s } ^ { \prime } )$ from x to $y .$ Also given is an associative composition rule

$$
\operatorname { M o r } ( x , y ) \times \operatorname { M o r } ( y , z ) \to \operatorname { M o r } ( x , z ) .
$$

Each set $\operatorname { M o r } ( x , x )$ must contain an identity $e _ { x }$ (meaning that composition with $e _ { x }$ on the left or right does nothing).

The objects of the category $\Pi _ { 1 } ( X )$ are the points of $X$ . Define $\Pi _ { 1 } ( x , y )$ as the set of equivalence classes of paths from x to $y$ under the relation of homotopy rel endpoints. $\Pi _ { 1 } ( x , y )$ will be the morphism set $\operatorname { M o r } ( x , y )$ in the category. One has well-defined composition maps $\Pi _ { 1 } ( x , y ) \times \Pi _ { 1 } ( y , z ) \to \Pi _ { 1 } ( x , z )$ , which are associative by our discussion. The class $\left[ c _ { x } \right]$ of the constant path at x defines an identity element $e _ { x }$ for $\Pi _ { 1 } ( x , x )$ . This shows that $\Pi _ { 1 } ( X )$ is a category.

A category in which every morphism has a 2-sided inverse is called a groupoid. Every morphism $[ f ] \in \Pi _ { 1 } ( x , y )$ has a 2-sided inverse $[ f ^ { - 1 } ] \in \Pi _ { 1 } ( y , x )$

1.2.2. Groupoids are too complicated to be really useful as invariants. However, as with any groupoid, the sets $\Pi _ { 1 } ( x , x )$ form groups under composition, and we can use this to extract a practical invariant. When a basepoint $x \in X$ is fixed, $\pi _ { 1 } ( X , x ) : = \Pi _ { 1 } ( x , x )$ is called the fundamental group. It is the group of based homotopy classes of loops based at x.

• If X is path connected, the fundamental groups for different basepoints are all isomorphic. Indeed, if $f$ is a path from x to y then the map

$$
\pi _ { 1 } ( X , x ) \to \pi _ { 1 } ( Y , y ) , \quad [ \gamma ] \mapsto [ f ] \cdot [ \gamma ] \cdot [ f ^ { - 1 } ]
$$

is an isomorphism.

• If $F \colon X \to Y$ is a map, there is an induced homomorphism

$$
F _ { * } \colon \pi _ { 1 } ( X , x ) \to \pi _ { 1 } ( Y , F ( x ) ) , \quad [ f ] \mapsto [ F \circ f ] .
$$

If $G \colon Y  Z$ is another map, one clearly has $G _ { * } F _ { * } = ( G \circ F ) ,$ ∗.

• Maps $F _ { 0 }$ and $F _ { 1 }$ which are based homotopic (i.e. homotopic through maps $F _ { t }$ with $F _ { t } ( x )$ constant for all t) give the same homomorphism $\pi _ { 1 } ( X , x ) \to$ $\pi _ { 1 } ( Y , F _ { 0 } ( x ) )$

Exercise 1.6: (a) If $f _ { 0 }$ and $f _ { 1 }$ are loops $( I , \partial I )  ( X , x )$ , we say they are homotopic through loops if they are joined by a homotopy $f _ { t }$ with $f _ { t } ( 0 )$ equal to $f _ { t } ( 1 )$ but not necessarily to x. Show that $f _ { 0 }$ is homotopic to $f _ { 1 }$ through loops iff $[ f _ { 0 } ]$ is conjugate to $[ f _ { 1 } ]$ in $\pi _ { 1 } ( X , x )$

(b) Show that a homotopy equivalence between path connected space induces an isomorphism on $\pi _ { 1 }$ , regardless of the choices of basepoints.

A point ∗ clearly has trivial $\pi _ { 1 }$ (there’s only one map $I \to * )$ . By (b) from the exercise, $\pi _ { 1 } ( X , x ) = \{ 1 \}$ for any contractible space X and any $x \in X$

A space is called simply connected if it is path-connected and has trivial $\pi _ { 1 }$ . We have just seen that contractible spaces are simply connected.

Exercise 1.7: (\*) Prove directly that the 2-sphere $S ^ { 2 } = \{ x \in \mathbb { R } ^ { 3 } : | x | = 1 \}$ is simply connected.

## 2. The fundamental group of the circle

Our first calculation of a non-trivial fundamental group has already has remarkable consequences.

2.1. Trivial loops. We begin by interpreting what it means for a loop to be trivial in the fundamental group. It is convenient to regard a loop not as a map $f \colon I \to X$ with $f ( 1 ) = f ( 0 )$ but as a map from the unit circle $S ^ { 1 } = \partial D ^ { 2 } \subset \mathbb { C }$ into X.

Proposition 2.1. A loop $f \colon S ^ { 1 } \to X$ represents the identity element $e \in \pi _ { 1 } ( X , f ( 1 ) )$ $i f$ and only if it extends to a map from the closed unit disc $D ^ { 2 }$ into X .

Thus a simply connected space is a path-connected space in which every loop bounds a disc.

Proof. If $[ f ] = 1 \in \pi _ { 1 } ( X , f ( 1 ) )$ , let $\{ f _ { t } \} _ { t \in [ 0 , 1 ] }$ be a homotopy rel endpoints from the constant map $c _ { f ( 1 ) }$ to $f = f _ { 1 }$ . Define a continuous extension $F \colon D ^ { 2 } \to X$ of f by setting $F ( z ) = \dot { f } _ { | z | } \dot { ( z / | z | ) }$ if $z \neq 0$ and $F ( 0 ) = f ( 1 )$

Conversely, if f extends to $F \colon D ^ { 2 } \to X$ , define a map $I \times S ^ { 1 }  X , ( t , z ) \mapsto F ( t z )$ Then F is a homotopy from the constant map $c _ { F ( 0 ) }$ to $f .$ The latter is in turn is homotopic through constant maps to $c _ { f ( 1 ) }$ . Hence f is homotopic through loops to $c _ { f ( 1 ) }$ . By (a) from Exercise 1.6, [f] is conjugate to $\left[ c _ { f ( 1 ) } \right]$ . But $[ c _ { f ( 1 ) } ] = e _ { : }$ hence $[ f ] = e$ 

## 2.2. Computing $\pi _ { 1 } ( S ^ { 1 } )$

Theorem 2.2. The fundamental group of $S ^ { 1 }$ is infinite cyclic: there is $a \ ( u n i q u e )$ homomorphism deg: $\pi _ { 1 } ( S ^ { 1 } ) \cong \mathbb { Z }$ such that $\deg ( \mathrm { i d } _ { S ^ { 1 } } ) = 1$

We think of $S ^ { 1 }$ as $\mathbb { R } / \mathbb { Z }$ , and take [0] as basepoint. Note that two maps $S ^ { 1 } \to S ^ { 1 }$ taking [0] to [0] are homotopic through loops iff they represent conjugate elements in $\pi _ { 1 } ( \dot { S } ^ { 1 } , [ 0 ] )$ . By the theorem, $\pi _ { 1 }$ is abelian, so conjugate elements are actually equal. Hence deg is actually an invariant of homotopy through loops, indeed a complete invariant.

The key idea of the proof is to look at the quotient map $p \colon \mathbb { R } \to \mathbb { R } / \mathbb { Z } = S ^ { 1 }$ . This map is the prototypical example of a covering map.

Lemma 2.3. Every map $f \colon ( I , \partial I )  ( S ^ { 1 } , [ 0 ] )$ lifts uniquely to a map $\tilde { f } \colon I   { \mathbb { R } }$ such that (i) $\tilde { f } ( 0 ) = 0$ , and $( i i ) p \circ \tilde { f } = f$

Proof. Let T be the set of $t \in I$ such that ˜f exists and is unique on $[ 0 , t ]$ . For any $[ x ] = p ( x ) \in S ^ { 1 }$ , the open set $U _ { [ x ] } = p ( x - 1 / 4 , x + 1 / 4 ) \subset S ^ { 1 }$ contains [x] and has the following property: the preimage $p ^ { - 1 } ( U )$ is the disjoint union of open sets $V _ { x } ^ { n } : = ( n + x - 1 / 4 , n + x - 1 / 4 ) , n \in \mathbb { Z }$ . Moreover, p maps each $V _ { x } ^ { n }$ homeomorphically onto U.

If ˜f has been defined on $[ 0 , t ]$ , with $t < 1$ , there exists $\delta > 0$ so that $f ( t - \delta , t + \delta ) \subset$ $U _ { f ( t ) }$ . Since $\tilde { f } ( t ) \in V _ { \tilde { f } ( t ) } ^ { 0 }$ , we are forced to define $\tilde { f }$ on $[ t , t + \delta )$ as the composite

$$
[ t + \delta ) ~ { \xrightarrow { \ f \ } } ~ U _ { f ( t ) } ~ { \xrightarrow { \ p ^ { - 1 } \ } } ~ V _ { f ( t ) } ^ { 0 } .
$$

This does indeed define an extension of $\tilde { f }$ to $[ 0 , t + \delta )$ . So T is an open set.

Now suppose $\tilde { f }$ exists and is unique on [0, t). Since $f ( s ) \to f ( t )$ as $s \ \to \ t ,$ when $0 < t - s \ll 1$ the lifts $\tilde { f } ( s )$ must lie in one of the open sets V projecting homeomorphically to $U _ { f ( t ) }$ , independent of s. Thus we can define $\tilde { f } ( t )$ to be the preimage of $f ( t )$ that lies in $V ,$ and this defines the unique continuous lift of $f$ on $[ 0 , t ]$ . Hence T is closed. Since I is connected and $T$ non-empty, we have $T = I$ 

Proof of the theorem. Given $f \colon ( I , \partial I )  ( S ^ { 1 } , [ 0 ] )$ , construct $\tilde { f }$ as in the lemma. Since $p \circ \tilde { f } ( 1 ) = [ 0 ] , \tilde { f } ( 1 )$ is an integer. Define the degree $\deg ( f )$ to be this integer. Since $\tilde { f }$ was uniquely determined by $f , \deg ( f )$ is well-defined. We now observe that if $\{ f _ { t } \} _ { t \in [ 0 , 1 ] }$ is a based homotopy then $\deg ( f _ { 0 } ) = \deg ( f _ { 1 } )$ . Indeed, we can lift each $f _ { t }$ to a unique map $\tilde { f } _ { t } \colon I   { \mathbb { R } } , p ( \tilde { f } _ { t } ( 0 ) ) = [ 0 ]$ , and $p \circ \tilde { f } _ { t } = f _ { t }$ . It is easy to check that the $\tilde { f } _ { t }$ vary continuously in t, hence define a homotopy $\{ \tilde { f } _ { t } \}$ from $\tilde { f } _ { 0 }$ to $\tilde { f } _ { 1 }$ Thus deg $( f _ { t } ) = \tilde { f } _ { t } ( 1 )$ is a continuous Z-valued function, hence constant.

Thus deg defines a map $\pi _ { 1 } ( S ^ { 1 } ) \to \mathbb { Z } .$ . It is a homomorphism because $\widetilde { f \cdot g }$ is given on $[ 0 , 1 / 2 ]$ by the unique lift of $t \mapsto f ( 2 t )$ which begins at 0 (this ends at $\deg ( f ) )$ , and on $[ 1 / 2 , 1 ]$ by the unique lift of $t \mapsto f ( 2 t - 1 )$ which begins at $\deg ( f )$ (this ends at $\deg ( g ) + \deg ( f ) )$

The degree homomorphism is surjective because $\mathrm { d e g } ( \mathrm { i d } _ { S ^ { 1 } } ) = 1$ . To see that it is injective, suppose deg $f = 0$ . Then $\tilde { f }$ is a loop in R, based at 0. Since R is simply connected, $\tilde { f }$ is based-homotopic to the constant map, and applying $p$ to this homotopy we see that the same is true of $f .$ 

## 2.3. Applications.

Corollary 2.4 (The fundamental theorem of algebra). Every non-constant polynomial $p ( z ) \in \mathbb { C } [ z ]$ has a complex root.

Proof. We may assume p is monic. If $p ( z ) = z ^ { n } + c _ { n - 1 } z ^ { n - 1 } + \cdot \cdot \cdot + c _ { 0 }$ has no root, $p ( z ) / | p ( z ) |$ is a well-defined function $\mathbb { C } \to S ^ { 1 } \subset \mathbb { C }$ . Let f denote its restriction to the circle $\{ | z | = 1 \}$ . Now, $f$ extends to a map from the unit disc to $S ^ { 1 }$ , whence $f$ is null-homotopic (cf. the last lecture) so $\deg ( f ) = 0$ by the homotopy-invariance of degree.

Now define $f _ { t } \colon S ^ { 1 } \to S ^ { 1 }$ for $t > 1$ by $f _ { t } ( z ) = p ( t z ) / | p ( t z ) |$ . The $f _ { t }$ are all homotopic, and $f _ { 1 } = f ,$ , so deg $( f _ { t } ) = 0$ for all t. But for $| z | \gg 0 , | c _ { n - 1 } z ^ { n - 1 } + \cdot \cdot \cdot +$ $c _ { 0 } | < | z ^ { n } |$ , and hence $p _ { s } ( z ) : = z ^ { n } + s ( c _ { n - 1 } z ^ { n } + \cdot \cdot \cdot + c _ { 0 } )$ has no root for $0 \leq s \leq 1$ Thus, for some fixed $t \gg 0$ , we can define $g _ { s } \colon S ^ { 1 } \to S ^ { 1 }$ by $g _ { s } ( z ) = p _ { s } ( t z ) / | p _ { s } ( t z ) |$ and this defines a homotopy from $f _ { t } = g _ { 1 } \mathrm { t o } g _ { 0 }$ . But $g _ { 0 } ( z ) = z ^ { n } / | z ^ { n } |$ , and so deg $g _ { 0 } = n$ (check this!). Hence $n = 0$ 

Remark. Some proofs of FTA invoke Cauchy’s theorem from complex analysis. To make the link with our approach, note that $\operatorname { i f } \gamma \colon S ^ { 1 } \to \mathbb { C } ^ { * }$ is a loop then, by the residue theorem (a consequence of Cauchy’s theorem) the complex number

$$
d ( \gamma ) = \frac { 1 } { 2 \pi i } \int _ { \gamma } z ^ { - 1 } d z
$$

is actually an integer depending on γ only through its homotopy class in $\mathbb { C } ^ { * }$ . When $\gamma$ is a based loop $S ^ { 1 } \to S ^ { 1 } \subset \overline { { \mathbb { C } } } ^ { * } , d ( \gamma ) = \deg ( \bar { \gamma } )$ (this follows from our theorem, bearing in mind that d defines a homomorphism $d \colon \pi _ { 1 } ( S ^ { 1 } ) \to \mathbb { Z }$ and that $d ( \mathrm { i d } _ { S ^ { 1 } } ) =$ 1).

Another corollary is the Brouwer fixed point theorem.

Corollary 2.5. Every continuous map g : $D ^ { 2 } \to D ^ { 2 }$ has a fixed point.

(Here $D ^ { 2 }$ denotes the closed unit disc.)

Proof. Suppose g has no fixed point. Then, for any $x \in D ^ { 2 }$ , there is a unique line passing through x and $g ( x )$ . Define $r ( x ) \in S ^ { 1 }$ to be the point where this line hits $\bar { S } ^ { 1 } = \bar { \partial } D ^ { 2 }$ when one starts at $g ( x )$ and moves along the line towards x. Thus $r ( x ) = x$ when $x \in \partial D ^ { 2 }$ . Writing $r ( x ) = x + t ( g ( x ) - x )$ , one calculates from the requirements that $| r ( x ) | = 1$ and $t \leq 0$ that

$$
t = { \frac { \langle x , x - g ( x ) \rangle - { \sqrt { \langle x , x - g ( x ) \rangle ^ { 2 } - ( | x | ^ { 2 } - 1 ) | x - g ( x ) | ^ { 2 } } } } { | x - g ( x ) | ^ { 2 } } } .
$$

Thus r is continuous.

On the other hand, there can be no continuous r : $D ^ { 2 }  \partial D ^ { 2 }$ with $r | _ { \partial D ^ { 2 } } = \mathrm { i d }$ 7 for if such an r existed, the degree of its restriction $r ^ { \prime }$ to the boundary would be 1 (because $r ^ { \prime } = \mathrm { i d } )$ but also 0 (because $r ^ { \prime }$ extends over $D ^ { 2 } )$ . Hence there must be a fixed point. 

Remark. The Brouwer fixed point theorem holds in higher dimensions too: every continuous map $g \colon D ^ { n } \to D ^ { n }$ has a fixed point. One can attempt to prove it using the same argument. For this to work, what one needs is a homotopy-invariant, integer-valued degree for maps $S ^ { n - 1 } \to S ^ { n - 1 }$ . The identity map should have degree 1 and the constant map degree 0. With such a function in place, the same argument will run.

There are many ways of defining a degree function (actually, the same degree function): one can use homology theory, homotopy theory, differential topology or complex analysis.

Exercise 2.1: Show that every matrix $A \in S L _ { 2 } ( \mathbb { R } )$ can be written uniquely as a product KL with $K \in S O ( 2 )$ and L lower-triangular with positive diagonal entries. Use this to write down (i) a deformation-retraction of $S L _ { 2 } ( \mathbb { R } )$ (topologized as a subspace of $\mathbb { R } ^ { 4 } )$ onto its subspace $S O ( 2 )$ ; and (ii) a homeomorphism $S ^ { 1 } \times ( 0 , \infty ) \times \mathbb { R } \to S L _ { 2 } ( \mathbb { R } )$ Deduce that $S L _ { 2 } ( \mathbb { R } )$ is path-connected and that $\pi _ { 1 } ( S L _ { 2 } ( \mathbb { R } ) ) \cong \mathbb { Z } .$

Exercise 2.2: The polar decomposition. It is known that every matrix $A \in S L _ { 2 } ( \mathbb { C } )$ can be written uniquely as a product $U P$ with $U \in S U ( 2 )$ and P positive-definite hermitian. Assuming this, deduce a homeomorphism $S ^ { 3 } \times ( 0 , \infty ) \times \mathbb { C } \to S L _ { 2 } ( \mathbb { C } )$ . (We will soon see that this implies $\pi _ { 1 } S L _ { 2 } ( \mathbb { C } ) = \{ 1 \} . )$ 0

## 3. Van Kampen in theory

There are two basic methods for computing fundamental groups. $O n e ,$ the method of covering spaces, generalises our proof that $\pi _ { 1 } ( S ^ { 1 } ) = \mathbb { Z }$ . The other, which we shall discuss today, is to cut the space into simpler pieces and use a ‘locality’ property of $\pi _ { 1 }$ called van Kampen’s theorem (a.k.a. the Seifert–van Kampen theorem).

## 3.1. Group presentations.

Definition 3.1. A free group on a set $S$ is a group $F _ { S }$ equipped with a map $i \colon S \to F _ { S }$ enjoying a ‘universal proper $\mathrm { { ; y } } ^ { \prime } \mathrm { { ; } }$ : for any map f from $S$ to a group $G$ there is a unique homomorphism ${ \tilde { f } } \colon F _ { S } \to G$ with ${ \tilde { f } } \circ i = f$

If $F _ { S }$ and $F _ { S } ^ { \prime }$ are both free groups on $S ,$ and $i \colon S \ \to \ F _ { S }$ and $i ^ { \prime } \colon S \ \to \ F _ { S } ^ { \prime }$ the defining maps, then there are unique homomorphisms $h \colon F _ { S } \to F _ { S } ^ { \prime }$ such that $h \circ i = i ^ { \prime }$ and $h ^ { \prime } \colon F _ { S } ^ { \prime } \to F _ { S }$ such that h $\circ i ^ { \prime } = i .$ . Thus $h ^ { \prime } \circ h \circ i = i$ . It follows that $h ^ { \prime } \circ h = \operatorname { i d }$ , since both sides are homomorphisms $F _ { S }  F _ { S }$ extending i. Hence h and $h ^ { \prime }$ are inverse isomorphisms.

The free group $\mathbb { F } _ { n } : = F _ { \{ 1 , \ldots , n \} }$ can be realised as the group of all ‘words’ made up of ‘letters’ $a _ { 1 } , \ldots , a _ { n }$ and their formal inverses $a _ { 1 } ^ { - 1 } , \dots , a _ { n } ^ { - 1 } , \mathrm { e . g . } a _ { 4 } a _ { 3 } ^ { - 1 } a _ { 4 } ^ { 2 } a _ { 1 } ^ { - 7 }$ Expressions $a _ { i } a _ { i } ^ { - 1 }$ and $a _ { i } ^ { - 1 } a _ { i }$ can be deleted or inserted. The group operation is concatenation of words, $\begin{array} { r } { \mathrm { e . g . } ( a _ { 4 } a _ { 3 } ^ { - 1 } ) \cdot ( a _ { 3 } a _ { 2 } ^ { 3 } ) = a _ { 4 } a _ { 3 } ^ { - 1 } a _ { 3 } a _ { 2 } ^ { 3 } = a _ { 4 } a _ { 2 } ^ { 3 } } \end{array}$ . The identity element is the empty word. The map i sends m to $a _ { m } ,$ and given an $f \colon \{ 1 , \ldots , n \} $ $G$ we extend it to $\tilde { f }$ by sending, for example, $a _ { 2 } a _ { 1 } ^ { - 1 } a _ { 3 } ^ { 2 }$ to $f ( a _ { 2 } ) f ( a _ { 1 } ) ^ { - 1 } f ( a _ { 3 } ) ^ { 2 }$

We often write this group as $\langle a _ { 1 } , \ldots , a _ { n } \rangle$ . For example, $\mathbb { F } _ { 1 } = \left. a \right. \cong \mathbb { Z }$

## Lemma 3.2. The groups Fn, for different n, are all distinct.

Proof. The abelianization $( \mathbb { F } _ { n } ) ^ { a b } : = \mathbb { F } _ { n } / [ \mathbb { F } _ { n } , \mathbb { F } _ { n } ]$ is isomorphic to $\mathbb { Z } ^ { n }$ , and $\mathbb { Z } ^ { n } / 2 \mathbb { Z } ^ { n }$ has $2 ^ { n }$ elements.

Now suppose that $r _ { 1 } , \ldots , r _ { m }$ are elements of $\langle a _ { 1 } , \ldots , a _ { n } \rangle$ . Let R be the smallest normal subgroup containing the ri (R is thought of as a group of ‘relations’). Define

$$
\langle a _ { 1 } , \dots , a _ { n } \mid r _ { 1 } , \dots , r _ { m } \rangle = \langle a _ { 1 } , \dots , a _ { r } \rangle / R .
$$

If G is a group, and $g _ { 1 } , \dotsc , g _ { n } \in G$ group elements, there’s a unique homomorphism $f \colon  a _ { 1 } , \ldots , a _ { n }   G$ sending each $a _ { i }$ to $g _ { i }$ . It is surjective iff $g _ { 1 } , \ldots , g _ { n }$ generate $G .$ In this case, $G \cong \langle a _ { 1 } , \ldots , a _ { n } \rangle /$ ker f . Thus, if $g _ { 1 } , \ldots g _ { n }$ generate $G ,$ and $r _ { 1 } , \ldots , r _ { m }$ are elements of $\langle a _ { 1 } , \ldots , a _ { n } \rangle$ which generate ker $f$ as a normal subgroup, then $f$ induces an isomorphism

$$
\langle a _ { 1 } , \ldots , a _ { n } \mid r _ { 1 } , \ldots , r _ { m } \rangle  G .
$$

Such an isomorphism is called a (finite) presentation for G. As examples, we have(!)

$$
\mathbb { Z } / ( n ) \cong \langle a \mid a ^ { n } \rangle , \quad D _ { 2 n } \cong \langle a , b \mid a ^ { n } , b ^ { 2 } , ( b a ) ^ { 2 } \rangle , \quad \mathbb { Z } ^ { 2 } \cong \langle a , b \mid a b a ^ { - 1 } b ^ { - 1 } \rangle .
$$

## 3.2. Push-outs.

Definition 3.3. Consider three groups, $G _ { 1 } , \ G _ { 2 }$ and H, and a pair of homomorphisms

$$
G _ { 1 } \xleftarrow { f _ { 1 } } H \xrightarrow { f _ { 2 } } G _ { 2 } .
$$

A push-out for $( f _ { 1 } , f _ { 2 } )$ is another group P and a pair of homomorphisms $p _ { 1 } \colon G _ { 1 } \to$ P and $g _ { 2 } \colon G _ { 2 } \to P$ forming a commutative square

$$
\begin{array}{c} \begin{array} { r c c l } { { } } & { { } } & { { { \cal H } } } & { { \longrightarrow } } & { { { \cal G } _ { 1 } } } \\ { { } } & { { } } & { { } } & { { } } \\ { { f _ { 2 } \rule { 0 ex } { 5 ex } } } & { { } } & { { \rule { 0 ex } { 5 ex } } } & { { \rule { 0 ex } { 5 ex } } } \\ { { } } & { { } } & { { } } & { { \rule { 0 ex } { 5 ex } } } \\ { { } } & { { } } & { { { p _ { 2 } } } } & { { \rule { 0 ex } { 5 ex } } } \end{array} \begin{array} { l } { { } } \\ { { } } \\ { { } } \end{array}   \end{array}
$$

and satisfying a universal property: given any other such square (a group K and homomorphisms $k _ { 1 } \colon G _ { 1 } \to K$ and $k _ { 2 } \colon G _ { 2 } \to K$ such that $k _ { 1 } \circ f _ { 1 } = k _ { 2 } \circ f _ { 2 } )$ , there is a unique homomorphism $h \colon P \to K$ such that $k _ { 1 } = h \circ p _ { 1 }$ and $k _ { 2 } = h \circ p _ { 2 }$

Exercise 3.1: Prove that the universal property determines P up to isomorphism. In what sense is the isomorphism unique?

We can understand push-outs concretely using group presentations. Suppose $\boldsymbol { G } _ { 1 } = \langle a _ { 1 } , \dots , a _ { n } \mid r _ { 1 } , \dots r _ { m } \rangle$ and that $G _ { 2 } = \langle b _ { 1 } , \dots , b _ { p } \mid s _ { 1 } , \dots , s _ { q } \rangle$ . Also suppose that H has generators $h _ { 1 } , \ldots , h _ { o }$ . In the push-out square above, the group $P$ is then a group called the free product of $G _ { 1 }$ and $G _ { 2 }$ amalgamated along H and notated $G _ { 1 } * _ { H } G _ { 2 }$ . It has the presentation

$$
G _ { 1 } * _ { H } G _ { 2 } = \langle a _ { 1 } , \ldots , a _ { n } , b _ { 1 } , \ldots , b _ { p } \mid r _ { 1 } , \ldots r _ { m } , s _ { 1 } , \ldots , s _ { q } , c _ { 1 } , \ldots , c _ { o } \rangle ,
$$

where $c _ { i } = f _ { 1 } ( h _ { i } ) f _ { 2 } ( h _ { i } ) ^ { - 1 }$

Exercise 3.2: Check that $K = G _ { 1 } * _ { H } G _ { 2 }$ fits into a push-out square for $f _ { 1 }$ and $f _ { 2 }$

Note that there was no need for our group presentations to be finite, except for notational convenience: we can allow infinite sets of generators and relations.

Exercise 3.3: The free product $G _ { 1 } * G _ { 2 }$ of groups $G _ { 1 }$ and $G _ { 2 }$ is the push-out of the diagram $G _ { 1 } \left. \{ 1 \} \right. G _ { 2 }$ . Define $D _ { \infty }$ as the subgroup of the group of affine transformations R → R generated by $x \mapsto - x$ and $x \mapsto x + 1$ . Prove that $D _ { \infty } \cong ( \mathbb { Z } / 2 ) * ( \mathbb { Z } / 2 )$

Exercise 3.4: In this exercise we show that the modular group, $P S L _ { 2 } ( \mathbb { Z } ) = S L _ { 2 } ( \mathbb { Z } ) / \{ \pm I \}$ is the free product $( \mathbb { Z } / 2 ) * ( \mathbb { Z } / 3 )$ . Define three elements of $S L _ { 2 } ( \mathbb { Z } )$

$$
S = \left[ \begin{array} { r r } { 0 } & { 1 } \\ { - 1 } & { 0 } \end{array} \right] , T = \left[ \begin{array} { r r } { 1 } & { - 1 } \\ { 0 } & { 1 } \end{array} \right] , U = S T = \left[ \begin{array} { r r } { 0 } & { 1 } \\ { - 1 } & { 1 } \end{array} \right] .
$$

(a) Verify that $S ^ { 2 } = U ^ { 3 } = - I .$

(b) Show that, for any $A \ \in \ S L _ { 2 } ( \mathbb { Z } )$ , there is an $n \in \mathbb { Z }$ such that the matrix $\left[ \begin{array} { c c } { { a } } & { { b } } \\ { { c } } & { { d } } \end{array} \right] = A T ^ { n }$ has $c = 0 ~ \mathsf { o r } ~ | d | \leq | c | / 2$

(c) Explain how to find an integer $l \geq 0$ and a sequence of integers $n _ { 1 } , \ldots , n _ { l }$ such that either $A T ^ { n _ { 1 } } S T ^ { n _ { 2 } } S \dots S T ^ { l }$ or $A T ^ { n _ { 1 } } { S T ^ { n _ { 2 } } } { S } \dots { S T ^ { l } } { \bar { S } }$ has 0 as its lower-left entry.

(d) Show that S and T generate $S L _ { 2 } ( \mathbb { Z } )$

(e)\* Define $\theta \colon \langle a , b \mid a ^ { 2 } , b ^ { 3 } \rangle \ = \ ( \mathbb { Z } / 2 ) * ( \mathbb { Z } / 3 ) \ \to \ P S L _ { 2 } ( \mathbb { Z } )$ to be the unique homomorphism such that $\theta ( a ) \ = \ \pm S$ and $\theta ( b ) \ = \ \pm U$ Remind yourself how $P S L _ { 2 } ( \mathbb { R } )$ acts on the upper half-plane H $\subset \mathbb { C }$ by M¨obius maps. Take $1 \neq w \in ( \mathbb { Z } / 2 ) * ( \mathbb { Z } / 3 )$ . Prove that the M¨obius map $\mu _ { w }$ corresponding to $\theta ( w ) \in P S L _ { 2 } ( \mathbb { R } )$ has the property that $\mu _ { w } ( D ) \cap D = \emptyset$ , where

$$
D = \{ z \in \mathbb { H } : 0 < \mathrm { R e } z < 1 / 2 , | z - 1 | > 1 \} .
$$

[Hint: consider $A : = \{ z \in \mathbb { H } : \mathrm { R e } z > 0 \}$ and $B : = \{ z \in \mathbb { H } : | z - 1 | >$ $\operatorname* { m a x } ( 1 , | z | ) \} . ]$ Deduce that θ is an isomorphism.

## 3.3. Van Kampen’s theorem.

Theorem 3.4. Suppose that X is the union of two path-connected open subsets U and V with path-connected intersection $U \cap V$ . Take $x \in U \cap V$ . Then the commutative diagram

<!-- image-->

of maps induced by the inclusions is a push-out square.

Example 3.5. Let $C _ { n }$ be the complement of n points in the plane. Observe that $C _ { n }$ deformation-retracts to the wedge sum $\textstyle \bigvee _ { i = 1 } ^ { n } S ^ { 1 }$ . We have $\pi _ { 1 } ( C _ { n } ) \cong \mathbb { F } _ { n }$ . Indeed, when $n > 0 , \vee _ { i = 1 } ^ { n } S ^ { 1 }$ is the union of a subspace U which deformation-retracts to $\textstyle \bigvee _ { i = 1 } ^ { n - 1 } S ^ { 1 }$ , and a subspace V which deformation-retracts to $S ^ { 1 }$ , where the subspace U ∩ V is contractible. By induction, $\pi _ { 1 } ( U ) \cong \mathbb { F } _ { n - 1 }$ . We know $\pi _ { 1 } ( V ) \cong \mathbb { Z } = \mathbb { F } _ { 1 }$ The push-out of $\mathbb { F } _ { n - 1 }$ and Z along the trivial group H is $\mathbb { F } _ { n - 1 } * \mathbb { F } _ { 1 } \cong \mathbb { F } _ { n }$ . Thus the result follows from van Kampen’s theorem.

Lemma 3.6. For any loop $\gamma \colon ( I , \partial I ) \to ( X , x )$ , there exists a finite, strictly increasing sequence $0 = s _ { 0 } < s _ { 1 } < s _ { 2 } < \dots < s _ { n } = 1$ such that $\gamma$ maps each interval $[ s _ { i } , s _ { i + 1 } ]$ into U or into V .

Proof. Every $x \in I$ has a connected open neighbourhood whose closure maps to U or to V . Since I is compact, finitely many of these intervals cover I. The endpoints of the intervals in the finite cover form a finite subset of I, which we may enumerate in ascending order as $\left( s _ { 0 } , \ldots , s _ { n } \right)$ 

Let us call the sequence (si) a subdivison for γ.

Lemma 3.7. Suppose $\Gamma = \{ \gamma _ { t } \} _ { t \in [ 0 , 1 ] }$ is a homotopy of paths $( I , \partial I )  ( X , x )$ Then there are increasing sequences $\quad 0 ^ { \cdot } = t _ { 0 } < t _ { 1 } < \cdots < t _ { m } = 1$ , and $0 = s _ { 0 } <$ $\cdots < s _ { n } = 1$ , such that Γ maps each rectangle $[ t _ { i } , t _ { i + 1 } ] \times [ s _ { j } , s _ { j + 1 } ]$ into U or into V . Moreover, we can take the sequence $\left( { { s } _ { i } } \right)$ to refine given subdivisions of γ0 and γ1.

## Exercise 3.5: Prove the lemma.

Proof of Van Kampen’s theorem. Suppose we are given a group G and homomorphisms $f \colon \pi _ { 1 } ( U )  G , g \colon \pi _ { 1 } ( V )  G$ which agree on the images of $\pi _ { 1 } ( U \cap V )$ . We construct a map $\alpha \colon \pi _ { 1 } ( X ) \to G$ so that $f = \alpha \circ ( i _ { U } )$ ∗ and $g = \alpha \circ ( i _ { V } ) ,$ ∗, where $i _ { U } \colon U \to X$ and $i _ { V } \colon V \to X$ are the inclusions.

Take $\gamma \colon ( I , \partial I ) \to ( X , x )$ , and choose a subdivision $s _ { 0 } < \cdots < s _ { n }$ . Label the intervals $\left[ s _ { i } , s _ { i + 1 } \right]$ as red or blue, in such a way that γ maps red intervals to U and blue intervals to V . For $0 < i < n$ , connect $\gamma ( s _ { i } )$ to x by a path $\delta _ { i }$ inside U (if both adjacent intervals $[ s _ { i - 1 } , s _ { i } ]$ and $[ s _ { i } , s _ { i + 1 } ]$ are red), inside V (if both adjacent intervals are blue), or inside U ∩ V (if the adjacent intervals are different colours). Then $\beta _ { i } : = \delta _ { i } ^ { - 1 } * \gamma | _ { [ s _ { i } , s _ { i + 1 } ] } * \delta _ { i }$ is a loop in either U or V . Define $\alpha [ \gamma ] =$ $\alpha _ { 1 } [ \beta _ { 0 } ] \cdot \cdot \cdot \cdot \cdot \alpha _ { n - 1 } [ \beta _ { n - 1 } ]$ , where $\alpha _ { i }$ is either f or g according to whether $[ s _ { i } , s _ { i + 1 } ]$ is red or blue.

We need to see that α is well-defined, and does not depend on the choices of path, subdivision and colouring. Observe that for a fixed γ and fixed subdivision, changing the colouring does not affect $\alpha _ { \mathrm { { ; } } }$ , because f and $g$ agree on the image of $\pi _ { 1 } ( U \cap V )$ . Moreover, refining a subdivision for given γ does not affect the definition of α. Nor does changing the choice of a path $\delta _ { i }$ (instead of trying to replace $\delta _ { i }$ by a rival path $\delta _ { i } ^ { \prime } .$ , insert an extra point into the subdivision, and use both paths $\delta _ { i }$ and $\delta _ { i } ^ { \prime } )$

Hence we are left with considering homotopic paths $\gamma _ { 0 }$ and $\gamma _ { 1 }$ with a common subdivision $s _ { 0 } < \cdots < s _ { n }$

Given a homotopy $\Gamma = \{ \gamma _ { t } \}$ , we can subdivide $[ 0 , 1 ] \times [ 0 , 1 ]$ into rectangles $R _ { i j } = \left[ t _ { i } , t _ { i + 1 } \right] \times \left[ s _ { j } , s _ { j + 1 } \right]$ and color the $R _ { i j }$ as red or blue in such a way so that Γ maps the red rectangles to $U$ and the blue ones to V . It will suffice to show that $\gamma _ { 0 }$ and $\gamma _ { t _ { 1 } } ~ \mathrm { g i v e }$ the same definition for α.

This last part of the argument requires pictures, which I will draw in class. (Consult Hatcher if you need to.) The idea is this: rather than going along the bottom edge of $R _ { 0 j }$ we can go around the other three sides. We have $\gamma _ { 0 } \simeq \beta _ { 0 } * \cdot \cdot * \beta _ { n } .$ but by going round these three sides we can replace $\beta _ { i }$ by a new loop $\beta _ { i } ^ { \prime }$ , and this will not affect α. By eliminating backtracking we can get from $\beta _ { 0 } * \cdots * \beta _ { n }$ to $\gamma _ { t _ { 1 } }$ 2 again without affecting α.

Knowing it is well-defined, one can check that α is a homomorphism making the two triangles commute (do so!). Note also that it is the unique such homomorphism: since $\gamma$ is homotopic to the composite of the $\delta _ { i } * \gamma | _ { [ s _ { i } , s _ { i + 1 } ] } * \delta _ { i } ^ { - 1 }$ , we have no choice but to define α this way. This concludes the proof. 

## 4. Van Kampen in practice

We compute some fundamental groups using van Kampen’s theorem.

4.1. Fundamental groups of spheres. A first use of van Kampen’s theorem is to show that spaces that should be simply connected are simply connected.

Proposition 4.1. Let $S ^ { n } = \{ x \in \mathbb { R } ^ { n + 1 } : | x | = 1 \}$ be the n-sphere. When $n \geq 2 .$ $\pi _ { 1 } ( S ^ { n } )$ is trivial.

Proof. Notice that the subspace $U = \{ x = ( x _ { 0 } , \ldots , x _ { n } ) \in S ^ { n } : x _ { 0 } \neq 1 \}$ is homeomorphic to $\mathbb { R } ^ { n }$ . Similarly, $V : = \{ x = ( x _ { 0 } , \ldots , x _ { n } ) \in S ^ { n } : x _ { 0 } \neq - 1 \}$ is homeomorphic to $\mathbb { R } ^ { n }$ . Thus $U$ and V are contractible open sets, and their intersection is path connected: it deformation-retracts to the equator $\{ x _ { 0 } = 0 \} \cong S ^ { n - 1 }$ , which is path connected when $n - 1 > 0$ . By van Kampen, $\pi _ { 1 } ( S ^ { n } )$ is the push-out of two homomorphisms to the trivial group; it is therefore trivial. 

## 4.2. A useful lemma.

Lemma 4.2. Suppose

<!-- image-->

is a pushout square. Then $p$ is surjective, and its kernel is the normalizer of im $f$

Proof. Put $P ^ { \prime } = G / N$ , where N is the normalizer of im $f ,$ and define $p ^ { \prime } \colon G \to P ^ { \prime }$ to be the quotient map. It is easy to check that $P ^ { \prime }$ and $p ^ { \prime }$ fit into a push-out square for the homomorphisms $f \colon H \to G$ and $H  \{ 1 \}$ . Thus $P$ is isomorphic to $P ^ { \prime }$ so that $p$ is identified with $p ^ { \prime }$ 

In conjunction with van Kampen’s theorem, this lemma has the following consequence.

Proposition 4.3. Suppose that X is the union of a path-connected open set U and a simply connected open set $V ,$ with $U \cap V$ path-connected. Let $x \in U \cap V$ . Then $\pi _ { 1 } ( X , x )$ is generated by loops in $U . \ A$ based loop in U becomes trivial in $\pi _ { 1 } ( X ) ~ i f f$ it lies in the normal subgroup $o f \pi _ { 1 } ( U , x )$ generated by loops in $U \cap V$

## 4.3. Fundamental groups of compact surfaces.

Proposition 4.4. Let $T ^ { 2 }$ be the 2-torus, $\mathbb { R } P ^ { 2 }$ the real projective plane, $K ^ { 2 }$ the Klein bottle. Then

$$
\pi _ { 1 } ( T ^ { 2 } ) \cong \mathbb { Z } ^ { 2 } ; \quad \pi _ { 1 } ( \mathbb { R } P ^ { 2 } ) \cong \mathbb { Z } / 2 ; \quad \pi _ { 1 } ( K ^ { 2 } ) \cong \langle a , b \mid a b a ^ { - 1 } b \rangle .
$$

No two of these spaces are homotopy-equivalent.

Proof. These spaces X are all quotient spaces q : $I ^ { 2 }  X$ of the square $I ^ { 2 } \subset \mathbb { R } ^ { 2 }$ obtained by gluing together its sides in pairs. Take p in $\operatorname { i n t } ( I ^ { 2 } )$

Let $U = q ( I ^ { 2 } \setminus \{ p \} )$ , and $V = q ( D )$ with D a small open disc containing $p .$ Thus U ∩ V deformation-retracts to a circle and V is simply connected. By the last proposition, $\pi _ { 1 } ( X )$ is generated by loops in the subspace $U .$ , which deformationretracts to $q ( \partial I ^ { 2 } )$

Going anticlockwise round $\partial I ^ { 2 }$ , we label the sides as $s _ { 1 } , s _ { 2 } , s _ { 3 } , s _ { 4 }$ (as directed paths).

In $T ^ { 2 } , q ( s _ { 1 } ) = q ( s _ { 3 } ^ { - 1 } )$ and $q ( s _ { 2 } ) = q ( s _ { 4 } ^ { - 1 } )$ Thus $U$ deformation-retracts to a wedge of two circles $a = q ( s _ { 1 } )$ and $b = q ( s _ { 2 } )$ , and $\partial U \simeq s _ { 1 } \cdot s _ { 2 } \cdot s _ { 3 } \cdot s _ { 4 }$ ' $a \cdot b \cdot a ^ { \bar { - 1 } } \cdot b ^ { - 1 }$ . To apply van Kampen, note that $\pi _ { 1 } ( U \cap V ) = \mathbb { Z }$ and $\pi _ { 1 } ( U ) = \langle a , b \rangle$ . The homomorphism $\mathbb { Z } \to F _ { 2 }$ induced by $U \cap V \hookrightarrow U$ sends 1 to $a b a ^ { - 1 } b ^ { - 1 }$ . Thus, by the last proposition,

$$
\pi _ { 1 } ( T ^ { 2 } ) \cong \langle a , b \mid a b a ^ { - 1 } b ^ { - 1 } \rangle \cong \mathbb { Z } ^ { 2 } .
$$

In $K ^ { 2 } , q ( s _ { 1 } ) = q ( s _ { 3 } )$ and $q ( s _ { 2 } ) = q ( s _ { 4 } ^ { - 1 } )$ . The argument is just the same as for the torus, except that now the homomorphism $\mathbb { Z } \to F _ { 2 }$ sends 1 to $a b a ^ { - 1 } b$ . Thus

$$
\pi _ { 1 } ( K ^ { 2 } ) \cong \langle a , b \mid a b a ^ { - 1 } b \rangle .
$$

In $\mathbb { R } P ^ { 2 } , q ( s _ { 1 } ) = q ( s _ { 3 } )$ and $q ( s _ { 2 } ) = q ( s _ { 4 } )$ . Thus $q ( \partial I ^ { 2 } )$ is a single circle, and the map $q \colon \partial I ^ { 2 }  { 1 } ( \partial I ^ { 2 } )$ has degree 2. So $\pi _ { 1 } ( U ) = \mathbb { Z }$ and $\pi _ { 1 } ( U \cap V ) = \mathbb { Z }$ . The map $\pi _ { 1 } ( U \cap V ) \to \pi _ { 1 } ( U )$ corresponds to $x \mapsto 2 x$ as a map $\mathbb { Z } \to \mathbb { Z }$ . Hence

$$
\pi _ { 1 } ( \mathbb { R } P ^ { 2 } ) \cong \mathbb { Z } / 2 .
$$

It follows easily that these three spaces are homotopically inequivalent: the abelianized fundamental groups (in which everything commutes) are $\pi _ { 1 } ( T ^ { 2 } ) ^ { a b } \ \cong \ \mathbb { Z } ^ { 2 }$ 7 $\pi _ { 1 } ( \mathbb { R } P ^ { 2 } ) ^ { a b } \cong \mathbb { Z } / 2$ and $\bar { \pi } _ { 1 } ( \dot { K } ^ { 2 } ) ^ { a b } \cong \mathbb { Z } / 2 \oplus \bar { \mathbb { Z } }$ 

As part of the last proposition, we showed $\pi _ { 1 } ( T ^ { 2 } ) = \mathbb { Z } ^ { 2 }$ . We now compute $\pi _ { 1 }$ for a torus with n punctures.

Lemma 4.5. Let $p _ { 1 } , \ldots , p _ { n }$ be distinct points of $\cdot _ { T ^ { 2 } }$ . There are isomorphisms

$$
\theta _ { n } \colon \pi _ { 1 } ( T ^ { 2 } \setminus \{ p _ { 1 } , \ldots , p _ { n } \} ) \to G _ { n } : = \langle \gamma _ { 1 } , \ldots , \gamma _ { n } , a , b \mid a b a ^ { - 1 } b ^ { - 1 } ( \gamma _ { 1 } \cdot \cdot \cdot \gamma _ { n } ) ^ { - 1 } \rangle
$$

so that filling in $p _ { n }$ induces the following commutative diagram:

$$
\begin{array} { c c c } { { \pi _ { 1 } ( T ^ { 2 } \setminus \{ p _ { 1 } , \dots , p _ { n } \} ) \xrightarrow { } { } \longrightarrow \pi _ { 1 } ( T ^ { 2 } \setminus \{ p _ { 1 } , \dots , p _ { n - 1 } \} ) } } & { { } } & { { } } \\ { { \theta _ { n } \Big \downarrow } } & { { } } & { { } } \\ { { { } \cal { G } _ { n } } } & { { \xrightarrow [ { g _ { n } } ] { } } } & { { { } \cal { G } _ { n - 1 } , } } \end{array}
$$

where $g _ { n } ( \gamma _ { n } ) = 1 , g _ { n } ( \gamma _ { i } ) = \gamma _ { i } f o r i < n , g _ { n } ( a ) = a a n d g _ { n } ( b ) = b .$

Proof. Apply van Kampen to a decomposition of $T ^ { 2 } \setminus \{ p _ { 1 } , . . . , p _ { n } \}$ into a oncepunctured torus U and an $( n + 1 )$ )-punctured 2-sphere. 

Proposition 4.6. Let $\Sigma _ { g }$ be the closed orientable surface of genus g. Then

$$
\pi _ { 1 } ( \Sigma _ { g } ) \cong \langle a _ { 1 } , b _ { 1 } , \ldots , a _ { g } , b _ { g } \ | \ [ a _ { 1 } , b _ { 1 } ] \cdot \cdot \cdot [ a _ { g } , b _ { g } ] \rangle ,
$$

where $[ a , b ] : = a b a ^ { - 1 } b ^ { - 1 } . \ I f p _ { 1 } , . . . , p _ { n }$ are distinct points in $\Sigma _ { g }$ then

$$
\pi _ { 1 } ( \Sigma _ { g } \setminus \{ p _ { 1 } , \dots , p _ { n } \} ) \cong \langle a _ { 1 } , b _ { 1 } , \dots , a _ { g } , b _ { g } , \gamma _ { 1 } , \dots , \gamma _ { n } \mid [ a _ { 1 } , b _ { 1 } ] \cdot \cdot \cdot [ a _ { g } , b _ { g } ] = \gamma _ { 1 } \cdot \cdot \cdot \gamma _ { n } \rangle .
$$

Proof. By induction on g. We have already proved it for $g = 0$ and for $g = 1$ Decompose $\Sigma _ { g } \setminus \{ p _ { 1 } , . . . , p _ { n } \}$ as the union of $U \simeq \Sigma _ { g } \setminus \{ p _ { 1 } , . . . , p _ { n } , q \}$ and $V \simeq$ $T ^ { 2 } \setminus \{ \bar { q ^ { \prime } } \}$ along an annulus $U \cap V$ (wrapping round q in $U$ and around $q ^ { \prime }$ in V ). By induction on $^ { g , }$ , van Kampen, and the last lemma, we find that $\pi _ { 1 } ( \Sigma _ { g } \setminus \{ p _ { 1 } , . . . , p _ { n } \} )$ has generators

$$
a _ { 1 } , b _ { 1 } , \dotsc , a _ { g - 1 } , b _ { g - 1 } , \gamma _ { 1 } , \dotsc , \gamma _ { n } , \delta
$$

coming from $U ;$

$$
a _ { g } , b _ { g } , \gamma _ { n + 1 } , \delta ^ { \prime }
$$

coming from $V ;$ a relation $\delta = \delta ^ { \prime }$ from $U \cap V ;$ and relations

$$
[ a _ { 1 } , b _ { 1 } ] \cdot \cdot \cdot [ a _ { g - 1 } , b _ { g - 1 } ] = \gamma _ { 1 } \cdot \cdot \cdot \gamma _ { n } \delta , \quad [ a _ { g } , b _ { g } ] = \delta ^ { \prime - 1 } \gamma _ { n + 1 }
$$

from $U$ and V . It is easy to check that this system of generators and relations are equivalent to those given. 

Another standard way to prove this is to think of $\Sigma _ { g }$ as an identification-space of the 4g-gon.

4.4. The complement of a trefoil knot. The left-handed trefoil knot K is the image of the embedding $f \colon S ^ { 1 } \to S ^ { 3 } = \{ ( z , w ) \in \mathbb { C } ^ { 2 } : | z | ^ { 2 } + | w | ^ { 2 } = 1 \}$ given by

$$
f ( e ^ { 2 \pi i t } ) = ( \frac { 1 } { \sqrt { 2 } } e ^ { 4 \pi i t } , \frac { 1 } { \sqrt { 2 } } e ^ { 6 \pi i t } ) .
$$

Proposition 4.7. $\pi _ { 1 } ( S ^ { 3 } \setminus K ) \cong \langle a , b \mid a ^ { 2 } b ^ { - 3 } \rangle$

Proof. We decompose $S ^ { 3 }$ as the union of two subspaces $Y = \{ ( z , w ) : | z | \geq | w | \}$ and $Z = \{ ( z , w ) : | z | \leq w \}$ . Both are solid tori $\bar { S } ^ { 1 } \times D ^ { 2 }$ , and $Y \cap Z$ is a torus $S ^ { 1 } \times S ^ { 1 }$ . There results a decomposition $S ^ { 3 } \setminus K = ( Y \setminus K ) \cup ( Z \setminus K )$ . Though the sets in this decomposition are not open, van Kampen is applicable because we can thicken up K to a ‘rope’ R, and then take thin open neighbourhoods of $Y \setminus R$ and $Z \backslash R$ which deformation-retract onto them. Now, $Y \setminus K$ deformation-retracts to the ‘core’ circle $| w | = 0$ , and $Z \backslash K$ to the core circle $| z | = 0$ , while $( Y \backslash K ) \cap ( Z \backslash K )$ deformation retracts to a circle $K ^ { \prime }$ parallel to K inside the torus $Y \cap Z .$ . Now $K ^ { \prime }$ wraps twice around the core circle in $Y \backslash K$ , three times around that in $Z \backslash K$ . Van Kampen shows that $\pi _ { 1 } ( S ^ { 3 } \setminus K )$ is a push-out of the diagram

$$
\mathbb { Z } \longleftarrow \mathbb { Z } \xrightarrow { 3 } \mathbb { Z } ,
$$

and this gives the presentation claimed.

Exercise 4.1: An n-dimensional manifold is a Hausdorff space X covered by open sets homeomorphic to $\mathbb { R } ^ { n }$ Let $X _ { 1 }$ and $X _ { 2 }$ be connected n-dimensional manifolds. A connected sum $X _ { 1 } \# X \cal { X } _ { 2 }$ is constructed by choosing embeddings $i _ { 1 } \colon D ^ { n } \to X _ { 1 }$ and $i _ { 2 } \colon D ^ { n } \to X _ { 2 }$ of the closed n-disc $D ^ { n }$ , and letting

$$
X _ { 1 } \# X _ { 2 } = ( X _ { 1 } \setminus i _ { 1 } ( \operatorname { i n t } D ^ { \prime } ) ) \operatorname { I I } { \big ( } X _ { 2 } \setminus i _ { 2 } ( \operatorname { i n t } D ^ { \prime } ) { \big ) } / \sim ,
$$

$D ^ { \prime } = { \textstyle { \frac { 1 } { 2 } } } D ^ { n } \subset D ^ { n }$ , where ∼ identifies $i _ { 1 } ( x )$ with $i _ { 2 } ( x )$ for all $x \in S ^ { n - 1 } = \partial D ^ { \prime }$

(a) Prove that if $n > 2$ then $\pi _ { 1 } ( X _ { 1 } \# X _ { 2 } ) \cong \pi _ { 1 } ( X _ { 1 } ) * \pi _ { 1 } ( X _ { 2 } )$

(b) Let X be an iterated connected sum of r copies of $S ^ { 1 } \times S ^ { n - 1 }$ , where $n \geq 3$ Compute $\pi _ { 1 } ( X )$ .

(c)\* Given a finitely presented group $\boldsymbol { G } = \langle g _ { 1 } , \dots , g _ { k } \mid r _ { 1 } , \dots , r _ { l } \rangle$ , find a connected, compact, 4-dimensional manifold M with $\pi _ { 1 } ( M ) \cong G$ . [Hint: Start with the case of no relations. Use the fact that $\partial ( S ^ { 1 } \times D ^ { \dot { 3 } } ) = S ^ { 1 } \dot { \times } S ^ { 2 } = \partial ( D ^ { 2 } \times S ^ { 2 } ) . ]$

Exercise 4.2: Let K be the trefoil knot. We’ve seen that $\pi _ { 1 } ( S ^ { 3 } \setminus K ) = \langle a , b \mid a ^ { 2 } = b ^ { 3 } \rangle$ How do you find a word representing a given loop in $S ^ { 3 } \setminus K ?$ Find words representing a meridian for $K \ ( \mathsf { i . e . }$ , the boundary of a small normal disc) and a longitude (parallel to the knot; not unique!). Let $Z$ be the the kernel of the homomorphism $\pi _ { 1 } ( S ^ { 3 } \setminus K ) \to$ $\langle a , b \mid a ^ { 2 } , b ^ { 3 } \rangle$ which sends a to a and b to b. Show that $Z \cong \mathbb { Z } ,$ generated by a longitude, and that $Z$ is contained in the center of $\pi _ { 1 } ( S ^ { 3 } \setminus K )$ . [Interestingly, by an earlier exercise we have $\langle a , b \mid a ^ { 2 } , b ^ { 3 } \rangle \cong P S L _ { 2 } ( \mathbb { Z } ) . ]$

Exercise 4.3: The braid group on 3 strings. In this extended exercise (based on one in Serre’s book Trees) we’ll see that the following five groups are isomorphic:

$\pi _ { 1 } ( S ^ { 3 } \setminus K )$ , where K is a (left-handed) trefoil knot.

• The group $\langle a , b \mid a ^ { 2 } = b ^ { 3 } \rangle$

• The algebraic braid group on 3 strings, $\langle s , t \mid s t s = t s t \rangle$

• The geometric braid group on 3 strings $B _ { 3 }$ , defined as the fundamental group of the configuration space ${ \mathcal { C } } _ { 3 }$ of 3-element subsets of $\mathbb { C }$

$\pi _ { 1 } ( \mathbb { C } ^ { 2 } \setminus C )$ , where $C \subset \mathbb { C } ^ { 2 }$ is the cuspidal cubic $\{ ( X , Y ) : X ^ { 2 } = Y ^ { 3 } \}$

(a) We already know that $\pi _ { 1 } ( S ^ { 3 } \setminus K ) \cong \langle a , b \mid a ^ { 2 } = b ^ { 3 } \rangle$ . Show that $a \mapsto s t s$ $b \mapsto t s$ defines an isomorphism

$$
\langle a , b \mid a ^ { 2 } = b ^ { 3 } \rangle  \langle s , t \mid s t s = t s t \rangle .
$$

(b) Take as basepoint $\{ - 2 , 0 , 2 \} \ \in \mathcal { C } _ { 3 }$ Define loops σ and τ in $X _ { 3 } , \ \sigma ( t ) \ =$ $\{ - 1 - e ^ { \pi i t } , - 1 + e ^ { \pi i t } , 2 \}$ 2} and $\tau ( t ) = \{ - 2 , 1 - e ^ { \pi i t } , 1 + e ^ { \pi i t } \}$ for $t \in [ 0 , 1 ]$ Let $s = [ \sigma ]$ and $t = [ \tau ]$ in $B _ { 3 }$ . Check that $s t s \ = \ t s t$ , so that one has a homomorphism $\langle s , t \mid s t s = t s t \rangle  B _ { 3 }$

(b) ${ \mathcal { C } } _ { 3 }$ is the subspace of $\mathrm { S y m ^ { 3 } } ( \mathbb { C } )$ (the quotient of $\mathbb { C } ^ { 3 }$ by the action of the symmetric group $S _ { 3 }$ permuting coordinates) where the three points are distinct. Let $\mathrm { S y m } _ { 0 } ^ { 3 } ( \mathbb { C } ) = \{ \{ a , b , c \} \in \mathrm { S y m } ^ { 3 } ( \mathbb { C } ) : a + b + c = 0 \}$ . Show that $\mathrm { S y m } ^ { 3 } ( \mathbb { C } ) \cong \mathbb { C } \times \mathrm { S y m } _ { 0 } ^ { 3 } ( \mathbb { C } )$ . Define a homeomorphism $h \colon \mathrm { S y m } _ { 0 } ^ { 3 } ( \mathbb { C } ) \to \mathbb { C } ^ { 2 }$ by sending $\{ a , b , c \}$ to the point $( x , y )$ such that

$$
( t - a ) ( t - b ) ( t - c ) \equiv t ^ { 3 } + x t + y .
$$

Verify that the points $a , b$ and c are distinct iff $4 x ^ { 3 } + 2 7 y ^ { 2 } \neq 0$ . Deduce that $\mathcal { C } _ { 3 } \cong \mathbb { C } \times ( \mathbb { C } ^ { 2 } \setminus C )$ , hence that $B _ { 3 } \cong \pi _ { 1 } ( \mathbb { C } ^ { 2 } \setminus C )$

(d) Show that $\mathbb { C } ^ { 2 } \setminus C$ is homotopy-equivalent to $S ^ { 3 } \setminus K$ , whence $\pi _ { 1 } ( \mathbb { C } ^ { 2 } \setminus C ) \cong$ $\pi _ { 1 } ( S ^ { 3 } \setminus K )$

(e)\* Show that going round the full circle of homomorphisms, the resulting homomorphism $\pi _ { 1 } ( S ^ { 3 } \setminus K ) \to \pi _ { 1 } ( S ^ { 3 } \setminus K )$ is an isomorphism.

## 5. Covering spaces

Another basic method of computing fundamental groups is to identify the space X as the quotient $\tilde { X } / G$ of a simply connected space X˜ by a discrete group G acting freely on it by homeomorphisms. Under certain additional conditions, one then has $\pi _ { 1 } ( X ) \cong G$ (just as $\pi _ { 1 } ( S ^ { 1 } ) = \pi _ { 1 } ( \mathbb { R } / \mathbb { Z } ) = \mathbb { Z } )$ . In this lecture we will explore how covering spaces arise in practice. We also see how a covering map gives rise to two groups: (i) its group of deck transformations, and $( i i )$ the image of π1 of the covering space in π1 of the base.

Definition 5.1. A covering map is a surjective map $p \colon \tilde { X }  X$ such that X has a cover by open sets U with the property that $p ^ { - 1 } ( U )$ is the disjoint union of open sets, each of which is mapped by p homeomorphically onto U. The domain X˜ of a covering map is called a covering space of X.

The fibre $F = p ^ { - 1 } ( x )$ is a discrete space. For an open set U as in the definition, and $x \in U$ , there is a homeomorphism t: $p ^ { - 1 } ( U ) \to F \times U$ such that $\mathsf { p r } _ { 2 } \circ t = p$ as maps $p ^ { - 1 } ( U ) \to U$ (t is called a trivialisation for p over U). Thus the fibres over points of U are all homeomorphic, and hence, if X is path-connected, all the fibres of p are homeomorphic. The covering map is trivial if there exists a trivialisation over X.

Remark. In the theory of covering spaces it’s a useful safety precaution to assume that all spaces are locally path connected (i.e., for any point x and any neighbourhood of x there is a smaller neighbourhood which is path connected).

Exercise 5.1: The following are covering maps:

(1) The quotient map $\mathbb { R } \to \mathbb { R } / \mathbb { Z } .$

(2) The map $S ^ { 1 } \to S ^ { 1 } , e ^ { i t } \mapsto e ^ { i n t }$

(3) The product of covering maps $( \ e . \ g . \ \mathbb { R } ^ { n } \to ( \mathbb { R } / \mathbb { Z } ) ^ { n } = \mathbb { R } ^ { n } / \mathbb { Z } ^ { n } )$

(4) The quotient map $S ^ { n } \to \mathbb { R } P ^ { n }$

Example 5.2. Let $( X , x )$ be a based space. A covering space Y for $S ^ { 1 } \vee X$ can be obtained by taking a family $( X _ { n } ) _ { n \in \mathbb { Z } }$ of identical copies of X, then letting $Y$ be the result of attaching $X _ { n }$ to R by identifying $x \in X _ { n } = X$ to $n \in \mathbb { Z }$ . The covering map p: $Y  X$ is given on R by the quotient map $\mathbb { R } \to \mathbb { R } / \mathbb { Z } = S ^ { 1 } \subset S ^ { 1 } \vee X$ and on $X _ { n }$ by the identification $X _ { n } = X$

Graphs. A graph is a topological space Γ obtained by the following procedure. One takes a discrete space V (the vertices), a set E (the edges) and for each $e \in E$ a map $a _ { e } \colon \{ 0 , 1 \} \to V$ One forms the identification space of V q $\mathrm { { I I } } _ { e \in E } \left[ 0 , 1 \right]$ in which $0 \in [ 0 , 1 ] _ { \epsilon }$ is identified with its image $a _ { e } ( 0 ) \in V$ , and $1 \in [ 0 , 1 ] _ { \epsilon }$ is identified with $a _ { e } \in V$

Example 5.3. A covering space of a graph is again a graph. For example $S ^ { 1 } \vee S ^ { 1 }$ is a graph with one vertex and 2 edges. The vertex has valency 4 (i.e., 4 intervals emanate from it). Any covering space Γ of $S ^ { 1 } \vee S ^ { 1 }$ is a graph in which each vertex has valency 4. The edges of $\Gamma$ can be coloured red and blue so that each vertex has two red and two blue intervals emanating from it. Moreover, Γ can be oriented (i.e., each edge given a direction) so that at each vertex, exactly one red interval is outgoing and exactly one blue interval is outgoing. Conversely any oriented, coloured graph Γ with these properties defines a covering of $S ^ { 1 } \vee S ^ { 1 }$

## 5.1. Deck transformations.

Definition 5.4. Fix covering maps $p _ { 1 } \colon Y _ { 1 } \to X$ and $p _ { 2 } \colon Y _ { 2 } \to X$ . A map of covering spaces from $( Y _ { 1 } , p _ { 1 } )$ to $( Y _ { 2 } , p _ { 2 } )$ is a map $f \colon Y _ { 1 } \to Y _ { 2 }$ such that $p _ { 1 } \circ f = p _ { 2 } $ A deck transformation for a covering space $p \colon Y \to X$ is a map of covering spaces h from $( Y , p )$ to itself which is also a homeomorphism.

The inverse of a deck transformation is another deck transformation. Hence the deck transformations form a group $\operatorname { A u t } ( Y / X )$

Example 5.5. In Example 5.2, the covering space $p \colon Y \to S ^ { 1 } \vee X$ has Z as its group of deck transformations. The generator is the ‘shift’ homeomorphism, acting on R by $t \mapsto t + 1$ and sending $X _ { n }$ identically to $X _ { n + 1 }$

Coverings arise ‘in nature’ via group actions. Suppose given a continuous action $G \times Y \to Y$ of the discrete group G on the space Y .

Proposition 5.6. The quotient map $q \colon Y \to Y / G$ is a covering map provided the action is a ‘covering action’: Y is covered by open sets V such that $g V \cap V = \emptyset$ for all $g \in G \backslash \{ e \}$ $I f Y$ is path connected, the group of deck tranformations is G.

Proof. Given $x \in Y$ , take a neighbourhood V of x as in the statement. We may assume V is connected. Let $U = q ( V )$ Then $q ^ { - 1 } ( U )$ is the disjoint union of the open sets $g V$ for $g \in G$ . Each is mapped bijectively to $U ;$ the map is open by definition of the quotient topology, hence a homeomorphism. This shows that q is a covering map.

Any $g \in G$ determines a deck transformation $x \mapsto g \cdot x ,$ and these give a homomorphism $G  G ^ { \prime }$ , where $G ^ { \prime }$ is the group of deck transformations. Since the action is free, the kernel of this homomorphism is trivial. To see that it is surjective, suppose f is a deck transformation. Pick a point $y \in Y$ , choose $g \in G$ such that $f ( y ) = h _ { g } \cdot y . $ , where $h _ { g }$ is the action of g. Then $h _ { g ^ { - 1 } } \circ f$ fixes y. By the last theorem, $G ^ { \prime }$ acts freely, hence $h _ { g ^ { - 1 } } \circ f = \operatorname { i d }$ , i.e. $f = h _ { g } .$ 

## 5.2. Examples.

• The action of $\mathbb { Z } ^ { n }$ on $\mathbb { R } ^ { n }$ by translations is a covering action (take the cover to be by balls of radius $1 / 3 )$

• The action of the cyclic group $\mathbb { Z } / p$ on $S ^ { 2 n - 1 } = \{ z \in \mathbb { C } ^ { n } : | z | = 1 \}$ , where the generator acts by scalar multiplication by $e ^ { 2 \pi i / p }$ , is a covering action. Indeed, a non-trivial group element moves every point by a distance $\geq d$ (for the Euclidean metric in $\mathbb { C } ^ { n } )$ , where $\begin{array} { r } { d = \operatorname* { m i n } _ { k \in \{ 1 , \dots , p - 1 \} } | 1 - e ^ { 2 \pi i k / p } | } \end{array}$ hence the open sets $S ^ { 2 n - 1 } \cap B ( z ; d / 2 )$ (with $| z | = 1 )$ provide a suitable cover. The quotient $L _ { 2 n - 1 } ( p ) = S ^ { 2 n - 1 } / ( \mathbb { Z } / p )$ is called a lens space.

• The last example generalises: if Y is compact and simply connected, and a finite group $G$ acts freely on $Y _ { ; }$ , then $\pi _ { 1 } ( Y / G ) \cong G$

• If G is a compact, simply connected topological group, and $Z \subset G$ a finite subgroup, then the action of Z on G is a covering action. An interesting example is $G = { \mathrm { S U } } ( 2 )$ and $Z = \{ \pm I \} \subset G$ . The quotient $P U ( 2 ) : = \mathrm { { S U } } ( 2 ) / Z$ is isomorphic to $\mathrm { S O ( 3 ) }$ . Indeed, $\mathrm { P U } ( 2 )$ is the group of conformal symmetries of $\mathbb { C } \cup \{ \infty \}$ , while $\mathrm { S O ( 3 ) }$ the group of orientation-preserving isometries of $S ^ { 2 }$ . These symmetries coincide under the standard homeomorphism $\mathbb { C } \cup \{ \infty \} = S ^ { 2 }$ . Moreover, there is a homeomorphism

$$
\operatorname { S U } ( 2 ) \to S ^ { 3 } = \{ ( \alpha , \beta ) \in \mathbb { C } ^ { 2 } : | \alpha | ^ { 2 } + | \beta | ^ { 2 } = 1 \} , \quad ( \alpha , \beta ) \mapsto { \left[ \begin{array} { l l } { \alpha } & { \beta } \\ { - { \bar { \beta } } } & { { \bar { \alpha } } } \end{array} \right] } .
$$

The involution $A  - A$ on ${ \mathrm { S U } } ( 2 )$ corresponds to the antipodal map on $S ^ { 3 }$ hence $\mathrm { P U } ( 2 ) \cong \mathbb { R } P ^ { 3 }$

Exercise 5.2: Do this exercise if you know the basic facts about smooth manifolds. Suppose Y and X are smooth n-manifolds, and $p \colon Y  X$ a smooth, proper map whose derivative $D p \colon T _ { x } Y  T _ { p ( x ) } X$ is an isomorphism for all $x \in Y$ Then $p$ is a (finite-sheeted) covering map.

Exercise 5.3: Show that $T ^ { 2 } \ \backslash$ {4 points} is a 2-sheeted covering of $S ^ { 2 } \backslash$ {4 points}. Some possible approaches are (a) a direct topological argument; (b) the Weierstrass ℘-function from complex analysis; (c) a pencil of divisors of degree 2 on an elliptic curve.

## 5.3. Unique path lifting.

Lemma 5.7. Let $p \colon \tilde { X } \  \ X$ be a covering map. Fix basepoints $x \in X$ and $\tilde { x } \in p ^ { - 1 } ( x )$

(1) $I f \gamma \colon I \to X$ a path, and $\gamma ( 0 ) = x$ , then there is a unique path $\tilde { \gamma } \colon I  \tilde { X }$ such that $\tilde { \gamma } ( 0 ) = x$ which $l i f t s \gamma$ in the sense that $p \circ \tilde { \gamma } = \gamma$

(2) A homotopy $\Gamma \colon I ^ { 2 } \to X$ lifts uniquely to a map $\tilde { \Gamma } \colon I ^ { 2 } \to \tilde { X }$ once we specify $\tilde { \Gamma } ( 0 , 0 )$

(3) The map $p _ { * } \colon \pi _ { 1 } ( \tilde { X } , \tilde { x } ) \to \pi _ { 1 } ( X , x )$ is injective.

(4) $H \tilde { x } ^ { \prime }$ also lies in $p ^ { - 1 } ( x )$ then $p _ { * } ( \pi _ { 1 } ( \tilde { X } , \tilde { x } ^ { \prime } ) )$ and $p _ { * } ( \pi _ { 1 } ( \tilde { X } , \tilde { x } ) )$ are conjugate subgroups of $\pi _ { 1 } ( X , x )$

(5) All conjugates $o f p _ { * } ( \pi _ { 1 } ( \tilde { X } , \tilde { x } ) )$ ) arise in this way.

Proof. (1) The proof is exactly the same as the proof of unique path lifting for $\mathbb { R } \to S ^ { 1 }$ that we gave in our proof that $\pi _ { 1 } ( S ^ { 1 } ) = \mathbb { Z }$ . Similarly (2).

(3) If $p _ { * } ( \gamma _ { 0 } )$ and $p _ { * } ( \gamma _ { 1 } )$ are homotopic rel endpoints then the unique lift of the homotopy to X˜ defines a homotopy rel endpoints between $\gamma _ { 0 }$ and $\gamma _ { 1 }$

(4) Choose a path γ in $\tilde { X }$ joining $\tilde { x } ^ { \prime }$ to ˜x. Then we have

$$
p _ { * } ( \pi _ { 1 } ( \tilde { X } , \tilde { x } ^ { \prime } ) ) = ( p _ { * } \gamma ) \cdot p _ { * } ( \pi _ { 1 } ( \tilde { X } , \tilde { x } ) ) \cdot ( p _ { * } \gamma ) ^ { - 1 } .
$$

(5) Follows from (1).

Exercise 5.4: Write out the missing details.

Exercise 5.5: A surjective map $p \colon Y  X$ which has unique path-lifting need not be a covering map. (You may choose Y not to be locally path connected. For a harder exercise, find an example where Y is locally path connected.)

Let us summarise where we have got to. A covering space $p \colon \tilde { X }  X$ gives rise (a) to a group of deck transformations $\operatorname { A u t } ( \tilde { X } / X )$ ; and $( b )$ to a conjugacy class of subgroups of $\pi _ { 1 } ( X , x )$ , the images of $\pi _ { 1 } ( { \tilde { X } } , { \tilde { x } } )$ , for basepoints $\tilde { x } \in p ^ { - 1 } ( x )$

Example 5.8. If ${ \tilde { X } } = X = S ^ { 1 }$ , and p is the covering $e ^ { i t } \mapsto e ^ { i n t }$ , then $\operatorname { A u t } ( { \tilde { X } } / X ) =$ $\mathbb { Z } / n$ (the generator being multiplication by $e ^ { 2 \pi i / n } )$ , while the image of $\pi _ { 1 } ( { \tilde { X } } )$ in $\pi _ { 1 } ( X )$ is $n \mathbb { Z } \subset \mathbb { Z }$ . We see in this example that the image of $\pi _ { 1 } ( { \tilde { X } } )$ in $\pi _ { 1 } ( X )$ is a subgroup whose index is equal to the number of sheets of the covering. It is a normal subgroup, and the quotient group is isomorphic to $\operatorname { A u t } ( { \tilde { X } } / X )$ . If we take $\tilde { X } \ = \ \mathbb { R }$ R, with $p \colon  { \mathbb { R } } \to  { \mathbb { R } } /  { \mathbb { Z } } = S ^ { 1 }$ the quotient map, then $\operatorname { A u t } ( { \tilde { X } } / { X } ) = \mathbb { Z }$ and $\pi _ { 1 } ( \mathbb { R } ) = \{ 1 \}$ , so again $\operatorname { A u t } ( \tilde { X } / X ) = \pi _ { 1 } ( X ) / p _ { * } \pi _ { 1 } ( \tilde { X } )$ .

In the next lecture we will see that these observations generalise (except that the image of $\pi _ { 1 } ( { \tilde { X } } )$ is not always normal). In particular, if X˜ is simply connected then $\operatorname { A u t } ( \tilde { X } / X ) \cong \pi _ { 1 } ( X )$## 6. Classifying covering spaces

In the previous lecture we introduced covering spaces. Today we classify the covering spaces of a given space $X$

The following theorem could be called the fundamental lemma of covering space theory.

Theorem 6.1 (lifting criterion). Let $p \colon \tilde { X }  X$ be a covering map, with $\tilde { X } \ p a t h .$ connected, and $f \colon B \to X ~ .$ a map from a path-connected and locally path-connected space $B .$ Choose $b \in B$ and $\tilde { x } \in \tilde { X }$ such that $p ( \tilde { x } ) = f ( b )$ . Then f lifts to a map $\tilde { f } \colon B \to \tilde { X }$ with $p \circ \tilde { f } = f$ and $\tilde { f } ( b ) = \tilde { x }$ if and only if

$$
f _ { * } ( \pi _ { 1 } ( B , b ) ) \subset p _ { * } ( \pi _ { 1 } ( \tilde { X } , \tilde { x } ) )
$$

in $\pi _ { 1 } ( X , f ( b ) )$ . When it exists, the lift is unique.

Proof. If the lift exists then $p _ { * } \circ \tilde { f } _ { * } = f _ { * }$ , hence im $f _ { * } \subset \mathrm { i m } p _ { * }$ . Uniqueness follows from the uniqueness of lifts of paths. We now consider existence. Take $y \in B$ and a path $\gamma$ from b to $y .$ We attempt to define $\tilde { f } ( y ) = \delta ( 1 )$ , where $\delta \colon B \to { \tilde { X } }$ is the unique lift of $f \circ \gamma$ with $\delta ( 0 ) = \tilde { x }$ . If this make sense and is continuous then it will certainly fulfil the requirements. We need to prove that $\delta ( 1 )$ is independent of the choice of $\gamma$ . If $\gamma ^ { \prime }$ is another such path then $\gamma$ followed by $( \gamma ^ { \prime } ) ^ { - 1 }$ is a loop l in $B .$ But if $f _ { * } ( \pi _ { 1 } ( Y , y ) ) \subset p _ { * } ( \pi _ { 1 } ( \tilde { X } , \tilde { x } ) )$ then l is homotopic rel endpoints to the image of a loop ζ in $\tilde { X }$ . Lifting the homotopy gives a homotopy rel endpoints between $\zeta$ and the lift of $\gamma * ( \gamma ^ { \prime } ) ^ { - \smile }$ , which shows that the lift $\delta ^ { \prime }$ of $f \circ \gamma ^ { \prime }$ ends at the same point as does $f \circ \gamma$ . Continuity of $f$ follows from local path-connectedness of B (cf. Hatcher). 

From now on, the base spaces of our covering maps will be assumed pathconnected and locally path-connected.

Corollary 6.2. If $p _ { 1 } \colon Y _ { 1 } \to X$ and $p _ { 2 } \colon Y _ { 2 } \to X$ are covering maps, and $p ( y _ { 1 } ) =$ $x = p _ { 2 } ( y _ { 2 } )$ , then there exists a homeomorphism $h \colon Y _ { 1 } \to Y _ { 2 }$ with $p _ { 2 } \circ h = p _ { 1 }$ and $h ( y _ { 1 } ) = y _ { 2 } i f$ and only $i f p _ { 1 * } \pi _ { 1 } ( Y _ { 1 } , y _ { 1 } ) = p _ { 2 * } \pi _ { 1 } ( Y _ { 2 } , y _ { 2 } )$ in $\pi _ { 1 } ( X , x )$ Hence two coverings of X are isomorphic iff they define conjugate subgroups of $\pi _ { 1 } ( X , x )$

Corollary 6.3. Any two simply connected covering spaces of X are isomorphic.

Because of this result, we shall refer to a simply connected covering space of X as a universal cover of X.

Corollary 6.4. $I f p \colon \tilde { X } \to X$ is a universal cover, Aut $( \tilde { X } / X )$ acts freely and transitively on any fibre $p ^ { - 1 } ( x )$ . We obtain an isomorphism $I _ { \tilde { x } } \colon \pi _ { 1 } ( X , x ) \to \operatorname { A u t } ( \tilde { X } / X )$ by fixing a base-point $\tilde { x } \in p ^ { - 1 } ( x )$ , then mapping [γ] to the unique deck transformation which sends x˜ to γ˜(1), γ˜ being the unique lift of γ with $\tilde { \gamma } ( 0 ) = \tilde { x }$

Proof. According to the lifting criterion, maps $h \colon { \tilde { X } } \to { \tilde { X } }$ intertwining p are necessarily homeomorphisms, and they are in natural bijection with the fibre $p ^ { - 1 } ( x )$

6.1. An equivalence of categories. We now formulate the classification theorem for coverings of X. In a nutshell, this says that isomorphism classes of path connected covering spaces correspond to conjugacy classes of subgroups of $\pi _ { 1 } ( X , x )$ We give a sharper statement, which classifies not only the coverings, but also the maps between them.

We shall define two categories and prove their equivalence. An equivalence of categories $\mathcal { F } \colon \mathcal { C } \to \mathcal { C } ^ { \prime }$ is a functor such that there exists a functor $\mathcal { G } \colon \mathcal { C } ^ { \prime } \to \mathcal { C }$ so that ${ \mathcal { F } } \circ { \mathcal { G } }$ and $\mathcal G \circ \mathcal F$ are naturally isomorphic to the identity functors on $\scriptstyle { \mathcal { C } } ^ { \prime }$ and C respectively. A standard result in category theory says that $\mathcal { F }$ is an equivalence provided that $\left( \mathrm { i } \right) \mathcal { F } _ { \ast }$ : ${ \mathrm { H o m } } ( X , Y ) \to { \mathrm { H o m } } ( { \mathcal { F } } ( X ) , { \mathcal { F } } ( Y ) )$ is bijective for all objects X and Y , and (ii) every object of $\scriptstyle { \mathcal { C } } ^ { \prime }$ is isomorphic to some $\mathcal C ( X )$

Definition 6.5. Let G be a group. Its orbit category ${ \mathcal { O } } ( G )$ is the category whose objects are the subgroups $H \leq G$ . For any H, the set $G / H$ of left cosets of H is a transitive $G { \mathrm { s e t } }$ . We define the morphisms $H  K$ to be maps of G-sets $G / H \to G / K$

Definition 6.6. If X is a path-connected space, we define a category $\operatorname { C o v } ( X )$ whose objects are path-connected covering spaces $p \colon Y \to X$ and whose morphisms are maps of covering spaces.

Theorem 6.7. Suppose that $( X , x )$ is a based space. Fixing a universal cover $p \colon \tilde { X }  X$ and a basepoint ${ \tilde { x } } \in p ^ { - 1 } ( X )$ determines an equivalence of categories

$$
{ \mathcal { G } } \colon { \mathcal { O } } ( \pi _ { 1 } ( X , x ) ) \to \operatorname { C o v } ( X ) .
$$

Proof. We define a functor ${ \mathcal G } \colon { \mathcal O } ( \pi _ { 1 } ( X , x ) ) \to \operatorname { C o v } ( X )$ Thus let $\tilde { X }  X$ be a simply-connected covering space, and fix a basepoint ˜x over $x \in X$ . Path-lifting starting at ˜x defines an isomorphism $I _ { \tilde { x } } \colon G \to \operatorname { A u t } ( \tilde { X } / X )$ where $G = \pi _ { 1 } ( X , x )$ • Take $H \subset \pi _ { 1 } ( X , x )$ , and define $\mathcal { G } ( H ) = \tilde { X } / I _ { \tilde { x } } ( H )$ . It comes with a projection map $\mathcal { G } ( H )  X$ , induced by $p \colon \tilde { X }  X$ , and this is certainly a covering. Its fibre over x is canonically identified with $G / H _ { \mathrm { { i } } }$ and $\pi _ { 1 } ( \mathcal { G } ( X ) , [ \tilde { x } ] )$ maps to H under the covering map.

Every path-connected covering $Y ~  ~ X$ is isomorphic to $\mathcal { G } ( H )$ for some H. Indeed, we take H to be the image of $\pi _ { 1 } ( Y , y )$ in $\pi _ { 1 } ( X , x )$ for some y lying over x, cf. Corollary 6.2.

If K is another subgroup, and $f \colon G / H \to G / K$ a map of G-sets, let $f ( H ) = \gamma K$ Then, for all $g \in G .$ , we have $f ( g H ) = g \gamma K$ . Notice that if $h \in H$ then $f ( h H ) =$ $h \gamma K = \gamma K$ , hence $\gamma ^ { - 1 } H \gamma \subset K$ ; conversely, an element $\gamma$ such that $\gamma ^ { - 1 } H \gamma \subset K$ defines a map of G-sets.

We shall define $\mathcal G ( f )$ via the lifting criterion. We are looking for a map $\tilde { X } / I _ { \tilde { x } } ( H ) $ $\tilde { X } / I _ { \tilde { x } } ( K )$ covering the identity on X. Such a map will be unique once we specify its effect on a point. For existence, take a basepoint $z \in \tilde { X } / I _ { \tilde { x } } ( H )$ such that the image of $\pi _ { 1 } ( \tilde { X } / I _ { \tilde { x } } ( H ) , z )$ in G is $\gamma ^ { - 1 } H \gamma$ (cf. Lemma $5 . 7 , ~ ( 5 ) )$ . By the lifting criterion, there is a unique map of covering spaces $\tilde { X } / I _ { \tilde { x } } ( H ) \to \tilde { X } / I _ { \tilde { x } } ( K )$ which sends z to [˜x]. This is $\mathcal { G } ( f )$ . It’s straightforward to check this gives a functor.

It remains to see that $\mathcal { G }$ gives a bijection between morphism sets. This is another application of the lifting criterion, but we omit the details. 

Let us spell out some aspects of this correspondence.

• $\mathrm { A t }$ one extreme, we can consider the trivial subgroup $\{ 1 \} \subset G$ , which corresponds to the universal cover. At the other extreme, $G \subset G$ gives the trivial cover $X  X$

• In general, the fibre of the covering $\mathcal { G } ( H )$ corresponding to $H \leq G$ is $G / H$ Thus finite index subgroups correspond to coverings with finite fibres.

• We can recover the conjugacy class of $H \leq G$ from $\mathcal { G } ( H )$ as the image of $\pi _ { 1 } ( \mathcal { G } ( H ) )$ in $\pi _ { 1 } ( X , x )$ . (To recover H on the nose, we have to remember the basepoint [˜x] coming from $\tilde { x } \in \tilde { X } . )$

• The normal (or regular, or Galois) coverings of X are those coverings $q \colon Y \to X$ for which $q _ { * } \pi _ { 1 } ( Y )$ is a normal subgroup of G. Equivalently, $\operatorname { A u t } ( Y / X )$ acts transitively on the fibre. A normal covering determines an actual subgroup, not just a conjugacy class of subgroups.

The similarity of the classification theorem with the fundamental theorem of Galois theory is not coincidental; the theory of ´etale maps in algebraic geometry unites them. In particular, finite extensions of the function field $K ( X )$ of a variety X correspond to finite (´etale) coverings of X.

6.2. Existence of a simply connected covering space. Under very mild hypotheses, a simply connected covering exists. Assume X locally path connected.

Proposition 6.8. Suppose that X admits a covering map $p \colon \tilde { X }  X$ from a simply connected space $\tilde { X }$ . Then X is semi-locally simply connected, meaning that each $x \in X$ has a path-connected neighbourhood U such that im ${ \mathfrak { c } } ( \pi _ { 1 } ( U ) \to \pi _ { 1 } ( X ) )$ is trivial.

Proof. Let U be a neighbourhood over which $p$ is trivial. Then any loop $\gamma$ in U lifts to a loop in $\tilde { X }$ , which is nullhomotopic (rel ∂I). Projecting the nullhomotopy to X, we see that γ is nullhomotopic in $X$ 

Exercise 6.1: Find a path connected, locally path connected space which is not semilocally simply connected.

Now fix a basepoint $x \in X$ . Define $\tilde { X }$ as the set of homotopy classes $[ \gamma ] ,$ , where $\gamma \colon I  X$ with $\gamma ( 0 ) = x$ and [γ] its homotopy class rel ∂I. Define $p \colon \tilde { X }  X$ to be the evaluation map $[ \gamma ] \mapsto \gamma ( 1 )$ . The topology on $\tilde { X }$ ought to be generated by the ‘path components’ of the sets $p ^ { - 1 } ( V )$ with $V \subset X$ open. Path components do not make sense a priori, but we can make sense of them, via path-lifting, when V is path connected and im $( \pi _ { 1 } ( V ) \to \pi _ { 1 } ( X ) )$ is trivial.

Proposition 6.9. If X is path-connected, locally path-connected and semi-locally simply connected then $p \colon \tilde { X }  X$ is a covering map and $\tilde { X }$ is simply connected. Thus X admits a simply connected covering space.

Exercise 6.2: Make the topology on $\tilde { X }$ more precise, then prove the proposition.

Exercise 6.3: (From May’s book.) Identify all index 2 subgroups of the free group $\mathbb { F } _ { 2 }$ Show that they are all free groups and identify generators for them.

Exercise $6 . 4 \colon ( \mathsf { a } )$ The universal cover of the torus $T ^ { 2 } : \mathbb { R } ^ { 2 }$ Identify all the deck transformations and hence determine (once again) the fundamental group. Which surfaces can cover $T ^ { 2 } ? \ ( \mathsf { b } )$ Show that the Klein bottle is also covered by $\mathbb { R } ^ { 2 }$ ; identify the deck transformations and hence the fundamental group.

Exercise 6.5: Let p : $Y  X$ be a covering (with Y path connected and X locally path connected) such that $p _ { * } \pi _ { 1 } ( Y , y ) = H \subset G = \pi _ { 1 } ( X , p ( y ) )$ . Show that $\operatorname { A u t } ( { \tilde { X } } / X ) \cong$ $( N _ { G } H ) / H$ , where $N _ { G } H = \{ g \in G : g H g ^ { - 1 } = H \}$

For the next exercise, you may use the following fact: the quotient $\mathrm { S U } ( 2 ) / \{ \pm I \}$ is isomorphic, as a topological group, to SO(3).

Exercise 6.6: Define a regular tetrahedron as a set of four distinct, unordered, equidistant points on $S ^ { 2 } \subset \mathbb { R } ^ { 3 }$ . Let $\tau$ be the space of regular tetrahedra. (a) Show that $\pi _ { 1 } ( \mathcal { T } )$ has a central subgroup $Z \cong \mathbb { Z } / 2$ such that $\pi _ { 1 } ( T ) / Z \cong A _ { 4 } .$ (b) Identify several (at least 5) pairwise non-isomorphic, path connected covering spaces of $\tau$ , describing them geometrically. (c) Show that the fundamental group of the space $\mathcal { P }$ of regular icosahedra (unordered collections of 20 distinct points on $S ^ { 2 }$ forming the vertices of a regular icosahedron) has order 120, but that the abelianization $\pi _ { 1 } ( \mathcal { P } ) ^ { a b }$ has order at most 2. (In fact it is trivial.) [Recall that the icosahedral group $A _ { 5 }$ is simple.]

Exercise 6.7: Rotation about a fixed axis, by angles increasing from 0 up to 2π, determines a loop $\gamma$ in SO(3). Show that $\gamma * \gamma$ is nullhomotopic.

## II. Singular homology theory

## 7. Singular homology

We explain a fundamental construction of algebraic topology—singular homology. We compute the 0th homology groups in terms of the path components of the space, and show that $\pi _ { 1 }$ maps onto the first homology group.

Precursors of homology theory go back to the 18th Century and Euler’s formula $v - e + f = 2$ for the numbers of vertices, edges and faces of a convex polyhedron. Its systematic development began with Poincar´e in the 1890s. The definition of singular homology we shall give is due to Eilenberg (1944), but it rests on fifty years of exploration and refinement by many mathematicians. Every aspect of it is the result of a gradual process of experiment and abstraction. It is perfectly simple and, at first, perfectly mysterious.

7.1. The definition. The geometric n-simplex is

$$
\Delta ^ { n } = \{ ( x _ { 0 } , \ldots , x _ { n } ) \in [ 0 , 1 ] ^ { n + 1 } : \sum x _ { i } = 1 \} .
$$

It is the convex hull $[ v _ { 0 } , \ldots , v _ { n } ]$ of the points $v _ { i } = ( 0 , \ldots , 0 , 1 _ { i } , 0 , \ldots , 0 )$

Define the ith face map

$$
\delta _ { i } \colon \Delta ^ { n - 1 } \to \Delta ^ { n } , \quad ( x _ { 0 } , \ldots , x _ { n - 1 } ) \mapsto ( x _ { 0 } , \ldots x _ { i - 1 } , 0 , x _ { i } , \ldots , x _ { n - 1 } ) .
$$

It is homeomorphism onto the face $[ v _ { 0 } , \ldots , \hat { v } _ { i } , \ldots , v _ { n } ] .$

An n-simplex in the space X is a continuous map $\sigma \colon \Delta ^ { n } \to X$ . Let $\Sigma _ { n } ( X )$ be the set of all n-simplices. Define the nth singular chain group $S _ { n } ( X )$ as

$$
S _ { n } ( X ) = \mathbb { Z } ^ { \Sigma _ { n } ( X ) } ,
$$

the free abelian group generated by $\Sigma _ { n } ( X )$ . It is the group of finite formal sums $\sum _ { i } n _ { i } \sigma _ { i }$ with $n _ { i } \in \mathbb { Z }$ and $\sigma _ { i } \in \Sigma _ { n } ( X )$ ). For $n > 0$ , define $\partial _ { n } \colon S _ { n } \to S _ { n - 1 }$ as the Z-linear map such that

$$
\partial _ { n } \sigma = \sum _ { i = 0 } ^ { n } ( - 1 ) ^ { i } ( \sigma \circ \delta _ { i } ) , \quad \sigma \in \Sigma _ { n } ( X ) .
$$

In alternative notation, $\begin{array} { r } { \partial _ { n } \sigma = \sum _ { i = 0 } ^ { n } { ( - 1 ) ^ { i } } ( \sigma | _ { [ v _ { 0 } , \dots , \hat { v } _ { i } , \dots , v _ { n } ] } ) } \end{array}$

Lemma 7.1. $\partial _ { n } \circ \partial _ { n + 1 } = 0$

Proof. This is a consequence of the following relations among the face maps:

$$
\delta _ { i } \circ \delta _ { j } = \delta _ { j } \circ \delta _ { i - 1 } , \quad j < i .
$$

For any n + 1-simplex $\sigma ,$ we have

$$
\begin{array} { r l } { \displaystyle \partial _ { n } \circ \partial _ { n + 1 } \sigma = \sum _ { 0 \leq j \leq n } \sum _ { 0 \leq i \leq n + 1 } \ ( - 1 ) ^ { i + j } \sigma \circ \delta _ { i } \circ \delta _ { j } } & { } \\ { \displaystyle = \sum _ { 0 \leq j < i \leq n + 1 } ( - 1 ) ^ { i + j } \sigma \circ \delta _ { i } \circ \delta _ { j } + \sum _ { 0 \leq i \leq j \leq n } ( - 1 ) ^ { i + j } \sigma \circ \delta _ { i } \circ \delta _ { j } } & { } \\ { \displaystyle = \sum _ { 0 \leq j < i \leq n + 1 } ( - 1 ) ^ { i + j } \sigma \circ \delta _ { j } \circ \delta _ { i - 1 } + \sum _ { 0 \leq i \leq j \leq n } ( - 1 ) ^ { i + j } \sigma \circ \delta _ { i } \circ \delta _ { j } } & { } \\ { \displaystyle = \sum _ { 0 \leq j < i \leq n + 1 } ( - 1 ) ^ { k + l + 1 } \sigma \circ \delta _ { k } \circ \delta _ { l } + \sum _ { 0 \leq i \leq j \leq n } ( - 1 ) ^ { i + j } \sigma \circ \delta _ { i } \circ \delta _ { j } } & { } \\ { \displaystyle = \sum _ { 0 \leq k \leq l \leq n } ( - 1 ) ^ { k + l + 1 } \sigma \circ \delta _ { k } \circ \delta _ { l } + \sum _ { 0 \leq i \leq j \leq n } ( - 1 ) ^ { i + j } \sigma \circ \delta _ { i } \circ \delta _ { j } } & { } \\ { \displaystyle = 0 . } \end{array}
$$

Since simplices generate $S _ { n + 1 } ( X )$ , the result follows.

It is convenient to let $\partial _ { 0 } \colon S _ { 0 } ( X ) \to 0$ be the zero-map. The nth singular homology of X is the abelian group

$$
H _ { n } ( X ) : = \ker \partial _ { n } / \operatorname { i m } \partial _ { n + 1 } .
$$

Elements of ker $\partial _ { n }$ are called n-cycles; elements of im $\partial _ { n + 1 }$ are n-boundaries. By the lemma, an n-boundary is an n-cycle, and the nth homology is the group of n-cycles modulo n-boundaries.

In future lectures we will develop these groups systematically. Today we will look only at the zeroth and first homology groups.

## 7.2. The zeroth homology group.

Proposition 7.2. The map $\begin{array} { r } { \varepsilon \colon S _ { 0 } ( X ) \to \mathbb Z , \varepsilon ( \sum n _ { i } \sigma _ { i } ) = \sum n _ { i } } \end{array}$ induces a surjection $H _ { 0 } ( X ) \to \mathbb { Z }$ provided only that X is non-empty. When X is path-connected, this map is an isomorphism.

Proof. We have to show that ε descends to $H _ { 0 } ( X ) = S _ { 0 } ( X ) / \operatorname { i m } \partial _ { 1 } . \mathrm { ~ I f ~ } \tau$ is a 1- simplex then $\partial \tau = \tau \circ \delta _ { 0 } - \tau \circ \delta _ { 1 }$ . Thus $\varepsilon ( \partial \tau ) = 1 - 1 = 0$ . Hence $\varepsilon ( \mathrm { i m } \delta _ { 1 } ) = 0$ 7 and ε descends to $H _ { 0 } ( X )$ . For any 0-simplex $\sigma , \varepsilon ( n \sigma ) = n$ , so ε is surjective. If X is path-connected, take $s = \sum n _ { i } \sigma _ { i } \in$ ker ε. We may assume $n _ { i } = \pm 1$ for all i. The number of + and − signs is equal, so we may partition the 0-simplices into pairs $( \sigma _ { i } , \sigma _ { j } )$ with $n _ { i } = 1$ and $n _ { j } = - 1$ . But $\sigma _ { i } - \sigma _ { j }$ is the boundary of a 1-simplex $( \mathrm { i . e . , }$ of a path), since X is path-connected. Hence $s \in$ im $\partial _ { 1 }$

Exercise 7.1: Show that, in general, $H _ { n } ( X ) = \bigoplus _ { Y \in \pi _ { 0 } ( X ) } H _ { n } ( Y )$ , where $\pi _ { 0 } ( X )$ is the set of path-components of X. Thus $H _ { 0 } ( X ) \cong \mathbb { Z } ^ { \pi _ { 0 } ( X ) }$

So, whilst $S _ { 0 } ( X )$ is typically very large (often uncountably generated), $H _ { 0 } ( X )$ is finitely generated for all compact spaces.

7.3. The first homology group. There’s a homeomorphism $I  \Delta _ { 1 }$ given by $t \mapsto t v _ { 1 } + ( 1 - t ) v _ { 0 }$ . Thus a path $\gamma \colon I  X$ defines a 1-simplex $\hat { \gamma }$ . When $\gamma ( 0 ) = \gamma ( 1 )$ , γˆ is a 1-cycle.

Lemma 7.3. Fix a basepoint $x \in X$ . The map $\gamma \mapsto \hat { \gamma }$ induces a homomorphism

$$
h \colon \pi _ { 1 } ( X , x ) \to H _ { 1 } ( X ) .
$$

Proof. A constant loop is the boundary of a constant 2-simplex. Loops which are homotopic rel endpoints give homologous 1-simplices (by subdividing a square into two triangles and using the fact that constant loops are boundaries). Thus h is well-defined. If f and g are composable paths, the composition f ∗ g maps under h to ${ \hat { f } } + { \hat { h } } \colon$ define a 2-simplex $\sigma = ( f * g ) \circ p \colon \Delta ^ { 2 } \to X$ , where p is the projection $[ v _ { 0 } , v _ { 1 } , v _ { 2 } ]  [ v _ { 0 } , v _ { 2 } ] , t _ { 0 } v _ { 0 } + t _ { 1 } v _ { 1 } + t _ { 2 } v _ { 2 } \mapsto t _ { 1 } v _ { 1 } + t _ { 2 } v _ { 2 }$ . We have $\partial \sigma = { \hat { g } } - { \widehat { f * g } } + { \hat { f } } .$

The map h is sometimes called the Hurewicz map.

Proposition 7.4. The kernel of the Hurewicz map $h \colon \pi = \pi _ { 1 } ( X , x ) \to H _ { 1 } ( X )$ contains the commutator subgroup $[ \pi , \pi ]$ , and hence h induces a homomorphism

$$
\pi ^ { a b } : = \pi / [ \pi , \pi ] \to H _ { 1 } ( X ) .
$$

When X is path-connected, h is surjective.

Proof. Since h is a homomorphism, $h ( f \cdot g \cdot f ^ { - 1 } \cdot g ^ { - 1 } ) = h ( f ) + h ( g ) - h ( f ) - h ( g ) = 0 ,$ Thus $[ \pi , \pi ] \subset$ ker h. To obtain surjectivity in the path-connected case, note that the group of 1-cycles is generated by loops, where a loop is a 1-cycle $\pm \sum _ { i \in \mathbb { Z } / N } \sigma _ { i }$ with $\delta _ { 1 } \sigma _ { i } + \delta _ { 0 } \sigma _ { i + 1 } = 0$ for all $i \in \mathbb { Z } / N$ . Thus it suffices to show that any loop lies in the image of h. But any loop is homologous to a loop based at x (insert a path γ from x to $\sigma _ { 0 } ( 0 )$ , and $\gamma ^ { - 1 }$ from $\sigma _ { N - 1 } ( 1 ) \ \mathrm { t o } \ x )$ . The composition of all the paths making up the based loop is homologous to their sum, and it lies in im(h). 

## Example 7.5. Any simply connected space X has $H _ { 1 } ( X ) = 0$

Remark. By analogy, one can look at the group $H _ { 2 } ( X ) / s ( X )$ , where $s ( X ) \subset H _ { 2 } ( X )$ is the subgroup generated by the ‘spherical cycles’: those represented by a map from a tetrahedron (built from four 2-simplices) into X. This group is zero when X is simply connected. A theorem of Hopf [Comment. Math. Helv. 14, (1942), 257–309] says that, for a general path-connected X, $H _ { 2 } ( X ) / s ( X )$ depends only on $\pi _ { 1 } ( X )$ It is naturally isomorphic to a group which is now understood as $H _ { 2 } ( \pi _ { 1 } ( X ) )$ , the second group homology of $\pi _ { 1 } ( X )$ . Indeed, group homology was developed partly in response to Hopf’s theorem. See, e.g., Brown, Cohomology of groups (GTM 87).

## 8. Simplicial complexes and singular homology

We show that a singular n-cycle can be represented by a map from an n-dimensional ∆-complex. We complete our calculation of $H _ { 1 }$ in terms of $\pi _ { 1 }$

## 8.1. ∆-complexes.

Definition 8.1. A ∆-complex (or semi-simplicial complex) is a space X equipped with sets $\mathcal { S } _ { n }$ , empty for $n \gg 0 .$ , and for each n and each $\alpha \in \mathcal S _ { n }$ a continuous maps $\sigma _ { \alpha } ^ { n } \colon \Delta ^ { n } \to X$ . We require that (i) $\sigma _ { \alpha } ^ { n }$ is injective on int $( \Delta ^ { n } )$ , and X (as a set) is the disjoint union over n and α of the images $\sigma _ { \alpha } ^ { n } ( \mathrm { i n t } ( \Delta ^ { n } )$ ; (ii) when $n > 0$ , the restriction to a face, $\sigma _ { \alpha } ^ { n } \circ \delta _ { i } .$ , is equal to $\sigma _ { \beta } ^ { n - 1 }$ for some $\beta \in \mathcal S _ { n - 1 } ;$ and (iii), a set $U \subset X$ is open iff $( \sigma _ { \alpha } ^ { n } ) ^ { - 1 } ( U )$ is open for all n and all $\alpha .$

There are a number of connections between ∆-complexes and singular homology. If a space is given the structure of a ∆-complex, there is a distinguished sub-space $S _ { n } ^ { s i m p } ( X ) \subset S _ { n } ( X )$ , spanned by the n-simplices $\sigma _ { \alpha } ^ { n }$ One has $\partial ( S _ { n } ^ { s i m p } ) ( X ) \subset$ $S _ { n - 1 } ^ { s i m p } ( X )$ , so it makes sense to form the simplicial homology group

$$
H _ { n } ^ { s i m p } ( X ) = \frac { \ker ( \partial _ { n } \colon S _ { n } ^ { s i m p } ( X ) \to S _ { n - 1 } ^ { s i m p } ( X ) ) } { \operatorname { i m } ( \partial _ { n + 1 } \colon S _ { n + 1 } ^ { s i m p } ( X ) \subset S _ { n } ^ { s i m p } ( X ) } .
$$

This comes with a natural homomorphism $H _ { n } ^ { s i m p } ( X ) \to H _ { n } ( X )$ , induced by the inclusion $S _ { n } ^ { s i m p } ( X ) \to S _ { n } ( X )$

Exercise 8.1: Think of $S ^ { 2 }$ as a tetrahedron, i.e., a ∆-complex with four 2-simplices, six 1-simplices and four 0-simplices. Show that for this structure

$$
H _ { 0 } ^ { s i m p } ( S ^ { 2 } ) = \mathbb { Z } , \quad H _ { 1 } ^ { s i m p } ( S ^ { 2 } ) = 0 , \quad H _ { 2 } ^ { s i m p } ( S ^ { 2 } ) = \mathbb { Z } , \quad H _ { > 2 } ^ { s i m p } ( S ^ { 2 } ) = 0 .
$$

Exercise 8.2: Compute $H _ { * } ^ { s i m p }$ for the spaces $T ^ { 2 } , \mathbb { R } P ^ { 2 }$ and $K ^ { 2 }$ , each thought of as a ∆-complex with two 2-simplices (and some 1- and 0-simplices).

Remark. You may like to keep in mind the following fact, even though it’s not part of the logical development of this course: the map $H _ { n } ^ { s i m p } ( X ) \to H _ { n } ( X )$ an isomorphism. So, for example, the homology of a ∆-complex is finitely generated.

The following simple observation gives some geometric insight into singular homology.

Lemma 8.2. Let z be a singular n-cycle in X, so $\partial _ { n } z \ : = \ : 0$ Write it as $z =$ $\sum _ { i = 1 } ^ { N } \epsilon _ { i } \sigma _ { i }$ with $\epsilon _ { i } ~ = ~ \pm 1$ Then there is an ∆-complex Z, with precisely N nsimplices $\left( \tau _ { 1 } , \dots , \tau _ { N } \right)$ and no higher-dimensional simplices, and a map $f \colon Z \to X$ , such that $( i ) \sum \epsilon _ { i } \tau _ { i }$ represents a simplicial n-cycle for $Z ,$ and (ii) $\sigma _ { i } = f \circ \tau _ { i }$ for each i.

Proof. Since $\partial _ { n } z \ = \ 0$ , each face $\sigma _ { i } \circ \delta _ { j }$ must cancel with another face $\sigma _ { i } ^ { \prime } \circ \delta _ { j ^ { \prime } }$ Thus, we can partition the set of faces of all $\sigma _ { i }$ into pairs. We define a ∆-complex Z by gluing N n-simplices together along their faces, paired up in the way just determined. This has the right properties. 

More generally, if $\partial _ { n } z = y$ , we can build a ∆-complex and a map from it into X so that the summed boundary of the n-simplices in the complex maps to X as the cycle y.

8.2. The Hurewicz map revisited. Last lecture, we introduced the ‘Hurewicz map’ $h \colon \pi _ { 1 } ( X ) ^ { a b } \ \longrightarrow \ H _ { 1 } ( X )$ and proved its surjectivity (assuming X path connected). We did not analyse its kernel. We now finish the job.

Theorem 8.3. When X is path-connected, the Hurewicz map $h \colon \pi _ { 1 } ( X ) ^ { a b }  H _ { 1 } ( X )$ is an isomorphism.

Example 8.4. • Recall that $\pi _ { 1 } ( S ^ { 1 } ) \cong \mathbb { Z }$ . Since this group is already abelian, $H _ { 1 } ( S ^ { 1 } ) \cong \mathbb { Z }$ also.

• Recall that $\pi _ { 1 } ( T ^ { 2 } ) = \pi _ { 1 } ( T ^ { 2 } ) ^ { a b } \cong \mathbb { Z } ^ { 2 } , \pi _ { 1 } ( K ^ { 2 } ) ^ { a b } \cong \mathbb { Z } \oplus \mathbb { Z } / 2$ and $\pi _ { 1 } ( \mathbb { R } P ^ { 2 } ) =$ $\pi _ { 1 } ( \mathbb { R } P ^ { 2 } ) ^ { a b } \cong \mathbb { Z } / 2$ , where $T ^ { 2 }$ is the 2-torus, $K ^ { 2 }$ the Klein bottle, and $\mathbb { R } P ^ { 2 }$ the real projective plane.

• Recall that the closed, oriented surface $\Sigma _ { g }$ of genus g has

$$
\pi _ { 1 } ( \Sigma _ { g } ) \cong \langle a _ { 1 } , \ldots , a _ { g } ; b _ { 1 } , \ldots , b _ { g } \mid [ a _ { 1 } , b _ { 1 } ] \cdot \cdot \cdot [ a _ { g } , b _ { g } ] \rangle .
$$

Thus $H _ { 1 } ( \Sigma _ { g } ) \cong \mathbb { Z } ^ { 2 g }$ , generated by the classes of $a _ { 1 } , \dots , a _ { g }$ and $b _ { 1 } , \dots , b _ { g }$

Proof of the theorem. Take a loop $\gamma \in$ ker h: say $\gamma = \partial _ { 2 } \beta$ . We will show that $[ \gamma ]$ is a product of commutators in $\pi ,$ hence lies in $[ \pi , \pi ]$ . We have already proved that h is onto, so this will complete the proof. But we can build from the 2-chain $\beta$ a 2-dimensional $\Delta \cdot$ -complex $K _ { \colon }$ , and a map $f \colon K \to X$ , with the following properties: if z is the sum of the 2-simplices, then $\partial _ { 2 } z = \sigma$ for a 1-simplex σ such that $f \circ \sigma = \gamma$ Moreover, the image of $\sigma$ in $K$ is a loop $\partial K$ . It suffices, then, to show that $\partial K$ is in the commutator subgroup of $\pi _ { 1 } ( K , b )$ (for the obvious basepoint $b \in \partial K )$ , for then the corresponding result will hold in X just by applying $f .$ . Thus we deduce the theorem from the following lemma. 

Lemma 8.5. Let K be a compact, connected, 2-dimensional ∆-complex. Suppose z is the sum of the 2-simplices, and that $\begin{array} { r } { \partial _ { 2 } z = \sum _ { i = 1 } ^ { N } \sigma _ { i } } \end{array}$ for some 1-simplices $\sigma _ { i }$ such that $\sigma _ { i } ( 1 ) = \sigma _ { i + 1 } ( 0 ) , i \in \mathbb { Z } / N$ . Fix a basepoint b; take it to be a vertex lying on ∂K. Then $\partial _ { 2 } z$ represents an element of $\pi = \pi _ { 1 } ( K , b )$ ). This element lies in the normal subgroup $[ \pi , \pi ]$ generated by commutators.

Proof. First observe (exercise!) that in general, if we have a free homotopy through loops $\gamma _ { t } \colon S ^ { 1 } \to X$ , then we have two fundamental groups $\pi = \pi _ { 1 } ( X , \gamma _ { 0 } ( 1 ) )$ and $\pi ^ { \prime } = \pi _ { 1 } ( X , \gamma _ { 1 } ( 1 ) )$ ; and $\left[ \gamma _ { 0 } \right] \in \left[ \pi , \pi \right] \subset \pi { \mathrm { ~ i f f ~ } } [ \gamma _ { 1 } ] \in [ \pi ^ { \prime } , \pi ^ { \prime } ] \subset \pi ^ { \prime }$

We now proceed by induction on the number of 2-simplices. The lemma is obvious when there is only one 2-simplex. When there is more than one, remove a 2-simplex σ adjacent to the boundary which has the basepoint as one of its vertices, so as to create a new $\Delta \cdot$ -complex $K ^ { \prime }$ which again satisfies the hypotheses(!). Pick a new basepoint $b ^ { \prime }$ on $\partial K ^ { \prime }$ which was one of the vertices of $\sigma .$ . By induction, $\partial K ^ { \prime }$ is a product of commutators in $\pi _ { 1 } ( K ^ { \prime } , b ^ { \prime } )$ , hence in $\pi _ { 1 } ( K , b ^ { \prime } )$ . But ∂K is homotopic through loops to $\partial K ^ { \prime }$ , so the result follows from our observation. 

Remark. The lemma is connected with the geometric interpretation of the algebraic notion of ‘commutator length’. In general, for a group π, the commutator length $c l ( \gamma ) \ \mathrm { o f } \ \gamma \in [ \pi , \pi ]$ is the least integer g such that $\gamma$ is the product of g commutators in π. If $\pi = \pi _ { 1 } ( X , x )$ , then one can show that $c l ( \gamma )$ is the minimal genus g of a compact oriented surface $K$ bounding γ. Here by a compact oriented surface I mean a ∆-complex K, equipped with a map $f \colon K \to X$ , which satisfies the conditions of the lemma and which is locally homeomorphic to $\mathbb { R } ^ { 2 }$ . The genus of K is half the rank of $H _ { 1 } ^ { s i m p } ( K )$ .

## 9. Homological algebra

Having introduced singular homology, we now need an adequate algebraic language to describe it.

9.1. Exact sequences. We shall work with modules over a base ring R, which we will assume to be commutative and unital. We write 0 for the zero-module. A sequence of R-modules and linear maps

$$
A { \overset { a } { \to } } B { \overset { b } { \to } } C
$$

is exact if ker $b =$ im a. A longer sequence of maps is called exact if it is exact at each stage.

$0 \to B { \overset { b } { \to } } C$ is exact iff b is injective.

$A \stackrel { a } {  } B  0$ is exact iff a is surjective.

$0 \to A { \overset { a } { \to } } B \to 0$ is exact iff a is bijective, i.e., iff a is an isomorphism.

• Exact sequences of the form

$$
0  A \ { \stackrel { a } {  } } \ B \ { \stackrel { b } {  } } \ C  0 ,
$$

are called short exact sequences. In such a sequence, coker $a = B /$ im $a =$ B/ ker b. But b induces an isomorphism $B /$ ker $B $ im $b = C$ . Thus a is injective with cokernel C, while b is surjective with kernel A.

• A short exact sequence is called split if it satisfies any of the following equivalent conditions: (i) there is a homomorphism $s \colon C \to B$ with bs = $\mathrm { i d } _ { C } ; ( \mathrm { i i } )$ there is a homomorphism t: $B  A$ with $t \circ a = \mathrm { i d } _ { A } ; \mathrm { o r ~ ( \mathrm { i i i ) } }$ there is an isomorphism $f \colon B \to A \oplus C$ so that $a ( x ) = f ( x , 0 )$ and $b ( f ^ { - 1 } ( x , y ) ) = y$

• If the six-term sequence

$$
0 \to A { \overset { a } { \to } } B { \overset { b } { \to } } C { \overset { c } { \to } } D \to 0
$$

is exact then a induces an isomorphism A ∼= ker b while c induces an isomorphism $D \cong$ coker b.

Exact sequences are useful because if one has partial information about the groups and maps in a sequence (in particular, the ranks of the groups) then exactness helps fill the gaps.

Example 9.1. Suppose one has an exact sequence of Z-modules

$$
0 \to \mathbb { Z } { \stackrel { i } { \to } } A { \stackrel { p } { \to } } \mathbb { Z } / 2 \to 0 .
$$

What can one say about A (and about the maps)? Choose $x \in A$ with $p ( x ) \neq 0$ Then $2 x \in \ker p = \operatorname { i m } i$ . There are two possibilities:

(i) $2 x \ : = \ : i ( 2 k )$ for some k. Let $x ^ { \prime } = x - i ( k )$ Then $2 x ^ { \prime } = 0$ . We can then define a homomorphism $s \colon \mathbb { Z } / 2 \to A$ with $p \circ s = \operatorname { i d }$ by sending 1 to x. Thus the sequence splits, and so may be identified with the ‘trivial’ short exact sequence $0 \to \mathbb { Z } \to \mathbb { Z } / 2 \oplus \mathbb { Z } \to \mathbb { Z } / 2 \to 0 .$

$( \mathrm { i i } ) ~ 2 x ~ = ~ i ( 2 k + 1 )$ for some k. Let $x ^ { \prime } = x - i ( k )$ Then $2 x ^ { \prime } = i ( 1 )$ and $p ( x ^ { \prime } ) \ = \ p ( x ) \neq 0$ Given $y \in A .$ , either $y \ = \ i ( m )$ for some m, in which case $y = 2 m x ^ { \prime }$ , or else $y - x ^ { \prime } = i ( m )$ for some m, in which case $y = ( 2 m + 1 ) x ^ { \prime }$ . Thus $A = \mathbb { Z } x ^ { \prime }$ . Moreover, $x ^ { \prime }$ has infinite order (since $\mathbb { Z } x ^ { \prime }$ contains im i). So the sequence may be identified with the sequence $0 \to \mathbb { Z } \to \mathbb { Z } \to \mathbb { Z } / 2 \to 0 .$ in which the map $\mathbb { Z } \to \mathbb { Z }$ is multiplication by 2 and $\mathbb { Z } \to \mathbb { Z } / 2$ is the quotient map.

9.2. Chain complexes. A chain complex over R is a collection $\{ C _ { p } \} _ { p \in \mathbb { Z } }$ of $R -$ modules, together with linear maps $d _ { p } \colon C _ { p } \to C _ { p - 1 }$ , called differentials, satisfying $d _ { p - 1 } \circ d _ { p } = 0$ We write $C _ { * }$ for the sum $\bigoplus _ { p } C _ { p } ,$ which is a graded module, and $d = \oplus d _ { p } \colon C _ { * } \to C _ { * }$ (an endomorphism map which lowers degree by 1, satisfying $d ^ { 2 } = 0 )$ . We define the homology

$$
H ( C _ { * } ) = \ker d / \operatorname { i m } d .
$$

Notice that ker $d = \oplus _ { \tau }$ ker $d _ { p }$ and im $d = \oplus \operatorname { i m } d _ { p }$ , so $\begin{array} { r } { H ( C _ { * } ) = \bigoplus _ { p } H _ { p } ( C _ { * } ) } \end{array}$ , where $H _ { p } ( C _ { * } ) = \ker d _ { p } / \operatorname { i m } d _ { p + 1 } ^ { \cdot }$

Elements of $Z _ { p } ( C ) : = \ker d _ { p }$ are called p-cycles; elements of $B _ { p } ( C ) : = \mathrm { i m } d _ { p + 1 }$ p-boundaries. If $H ( C _ { * } ) = 0$ , we say that C is acyclic.

A chain map from $( C _ { * } , d _ { C } )$ to $( D _ { * } , d _ { D } )$ is a linear map $f \colon C _ { * } \ \to \ D ,$ ∗ such that $f ( C _ { p } ) \subset D _ { p }$ and $d _ { D } \circ f = f \circ d _ { C } . \mathrm { ~ A ~ }$ chain map induces homomorphisms $H _ { p } ( f ) \colon \dot { H } _ { p } ( C _ { * } ) \dot {  } H _ { p } ( D _ { * } )$ . A chain map which induces an isomorphism on homology is called a quasi-isomorphism.

9.2.1. Chain homotopies. We need a criterion for two chain maps f and $g \colon C _ { * } \to$ $D _ { * }$ to induce the same map on homology. For this we introduce the notion of chain homotopy. A chain homotopy from $g$ to f is a collection of linear maps $h _ { p } \colon C _ { p } \to D _ { p + 1 }$ such that

$$
d _ { D } \circ h _ { p } + h _ { p - 1 } \circ d _ { C } = f - g .
$$

If $x \in Z _ { p } ( C )$ then $f ( x ) = g ( x ) + d _ { D } ( h _ { p } x )$ , hence $[ f ( x ) ] = [ g ( x ) ] \in H ( D _ { * } )$ . If, for example, there is a chain homotopy from $f \colon C _ { * } \to C _ { * }$ to the identity map $\mathrm { i d } _ { C }$ , then f is a quasi-isomorphism. If there is a null-homotopy, i.e., a chain homotopy from $f$ to the zero-map, then $f$ induces the zero-map on homology. If both possibilities occur then $C _ { * }$ must be acyclic, $\mathrm { i . e . , ~ } H _ { \ast } ( C ) = 0$

9.2.2. Short and long exact sequences. We study the effect of passing to homology on a short exact sequence

$$
0 \to A _ { * } \ { \overset { a } { \to } } \ B _ { * } \ { \overset { b } { \to } } \ C _ { * } \to 0
$$

of chain complexes and chain maps.

Lemma 9.2. (i) The sequence $H _ { p } ( A ) \stackrel { H _ { p } ( a ) } { \longrightarrow } H _ { p } ( B ) \stackrel { H _ { p } ( b ) } { \longrightarrow } H _ { p } ( C )$ is exact.

(ii) Take $x \in A _ { p }$ with $d _ { A } x = 0$ . Then $[ x ] \in$ ker $H _ { p } ( a )$ iff there exists $y \in B _ { p + 1 }$ such that $a ( x ) = d _ { B } y$

(iii) Take $z \in C _ { p }$ with $d _ { C } z = 0$ . Then $[ z ] \in$ im $H _ { p } ( b )$ iff there exists $y \in B _ { p - 1 }$ such that $b ( y ) = z$ and $d _ { B } y = 0$

Proof. (i) Take $y \in B _ { p }$ with $d _ { B } y = 0$ and $b ( y ) = d _ { C } z$ for some $z \in C _ { p + 1 }$ . Then $z = b ( y ^ { \prime } )$ ), say, and $b ( y - d _ { B } y ^ { \prime } ) = d _ { C } ( z - b ( y ^ { \prime } ) ) = 0 ,$ , so $y - d _ { B } y ^ { \prime } = a ( x )$ for some $x \in A _ { p } , { \mathrm { i . e . ~ } } y \in$ im a + im $d _ { B }$ , as required.

(ii) is obvious, and (iii) almost so.

Points (ii) and (iii) can be pushed considerably further. Define the connecting homomorphism

$$
\delta \colon Z _ { p } ( C ) \to H _ { p - 1 } ( A )
$$

as follows:

$$
\delta ( z ) = [ x ] { \mathrm { ~ w h e n ~ t h e r e ~ e x i s t s ~ } } y \in B _ { p } { \mathrm { ~ w i t h ~ } } b ( y ) = z { \mathrm { ~ a n d ~ } } a ( x ) = d _ { B } y .
$$

Lemma 9.3. δ is a well-defined map.

Proof. Note first that, since b is onto, there is some y with $b ( y ) = z ;$ and $b ( d _ { B } y ) =$ $d _ { C } ( b y ) = d _ { C } z = 0$ , hence $d _ { B } y \in$ ker $b = \operatorname { i m } a$ Thus suitable y and x exist. Moreover, x is determined by y, because of the injectivity of a. If $b ( y ) = b ( y ^ { \prime } ) = z$ then $y - y ^ { \prime } \in$ ker b = im a, so $y = y ^ { \prime } + a ( x ^ { \prime } )$ for some $x ^ { \prime }$ , and $d _ { B } y = d _ { B } y ^ { \prime } + d _ { B } a ( x ^ { \prime } ) =$ $d _ { B } y ^ { \prime } + a ( d _ { A } x ^ { \prime } )$ . Thus replacing y by $y ^ { \prime }$ has the effect of replacing x by $x + d _ { A } x ^ { \prime } ,$ so the homology class [x] is well-defined.

Linearity of δ is clear. Note that δ maps $B _ { p } ( C )$ to 0, and hence descends to a map on homology,

$$
\delta \colon H _ { p } ( C ) \to H _ { p - 1 } ( A ) .
$$

Theorem 9.4. The short exact sequence of chain complexes

$$
0 \to A _ { * } \ { \overset { a } { \to } } \ B _ { * } \ { \overset { b } { \to } } \ C _ { * } \to 0
$$

induces an exact sequence

$$
\cdots \to H _ { p } ( A ) \xrightarrow { H a } H _ { p } ( B ) \xrightarrow { H b } H _ { p } ( C ) \xrightarrow { \delta } H _ { p - 1 } ( A ) \xrightarrow { H a } H _ { p - 1 } ( B ) \xrightarrow { H b } H _ { p - 1 } ( C ) \to \cdots .
$$

Proof. We have already established exactness at $H _ { p } ( C )$ and well-definedness of the connecting map δ.

Exactness at $H _ { p } ( C )$ : Say $[ z ] \in$ ker δ. This means that $z = b ( y )$ and $a ( d _ { A } x ^ { \prime } ) =$ $d _ { B } y$ for some $x ^ { \prime } \in A _ { p } .$ . Then $d _ { B } ( y - a x ^ { \prime } ) = 0$ , and $b ( y - a x ^ { \prime } ) = z , \mathrm { s o } z \in$ im b.

Exactness at $H _ { p - 1 } ( A )$ : Let $x \in Z _ { p - 1 } ( A )$ , and suppose that $a x = d _ { B } y$ . Then $[ x ] = \delta ( b ( y ) )$ 

Exercise 9.1: We consider chain complexes $( C _ { * } , \delta )$ over a field k such that dim $_ { \cdot k } H _ { * } ( C ) <$ ∞. The Euler characteristic of $C _ { * }$ is then defined as the alternating sum

$$
\chi ( C _ { * } ) = \sum _ { p } ( - 1 ) ^ { p } \dim _ { k } H _ { p } ( C ) .
$$

(i) Show that when $\sum _ { p }$ dimk $C _ { p } < \infty$ , one has $\begin{array} { r } { \chi ( C _ { * } ) = \sum _ { p } ( - 1 ) ^ { p } } \end{array}$ dimk $C _ { p } .$

(ii) Show that if

$$
\cdot \cdot \cdot \longrightarrow C _ { p }  C _ { p - 1 }  C _ { p - 2 }  . . .
$$

is an exact sequence, and $\sum _ { p }$ dim $C _ { p } < \infty$ , then $\sum { ( - 1 ) ^ { p } }$ dim $C _ { p } = 0$

Exercise 9.2: A collection C of Z-modules is called a Serre class if for every short exact sequence $0  A  B  C  0$ such that two out of the three Z-modules A, B, C are in C, the third is in C also. Fix a prime $p \in \mathbb Z$ . Identify which of the following properties of Z-modules M define Serre classes: (a) M is torsion; (b) M is torsion-free; (c) M is torsion but has no p-torsion; (d) every element of M has p-power order; (e); every element of M is divisible by $p ; ( { \mathsf { f } } )$ every M is finitely generated. (\*) What if we replace M by an arbitrary commutative ring R (and p by a prime of R?).

Exercise 9.3: Prove or give a counterexample: given two path connected open sets U and V whose union is X and whose intersection $U \cap V$ is path connected, there exists a short exact sequence of abelian groups

$$
0 \to H _ { 1 } ( U \cap V ) \to H _ { 1 } ( U ) \oplus H _ { 1 } ( V ) \to H _ { 1 } ( X ) \to 0 .
$$

Exercise 9.4: If $a \colon A _ { * } \to B _ { * }$ is a chain map its mapping cone, denoted cone(a)∗, is the complex

$$
{ \mathsf { c o n e } } ( a ) _ { n } = A _ { n - 1 } \oplus B _ { n }
$$

with differential $d _ { \mathsf { c o n e } ( a ) } ( x , y ) = - d _ { A } x + a ( x ) + d _ { B } y$ (check that this squares to zero). The point of this construction is to convert questions about chain maps to questions about chain complexes.

(i) Show that the induced map on homology, $a _ { * } = H ( a ) \colon H _ { * } ( A ) \to H _ { * } ( B )$ , is an isomorphism iff $H ( \mathsf { c o n e } ( a ) _ { * } ) = 0$

(ii) Construct a short exact sequence

$$
0  B _ { * }  \mathsf { c o n e } ( a ) _ { * }  A _ { * - 1 }  0 ,
$$

and identify the connecting map in the resulting long exact sequence.

(iii) Show that to give a map of complexes $f = ( h , b ) \colon \mathsf { c o n e } ( a ) _ { * } \to C _ { * }$ is to give a chain map $b \colon B _ { * } \to C _ { * }$ and a chain-homotopy h from b ◦ a to the zero map.

(iv) Show that if the map f from (iii) induces an isomorphism on homology then there is a long exact sequence

$$
\cdots \to H _ { n } ( A ) \ { \overset { a * } { \to } } \ H _ { n } ( B ) \ { \overset { b * } { \to } } \ H _ { n } ( C ) \to H _ { n - 1 } ( A ) \ { \overset { a * } { \to } } \ H _ { n - 1 } ( B ) \ { \overset { b * } { \to } } \ H _ { n - 1 } \to \dots . . .
$$

Exercise $9 . 5 ; ( ^ { * } )$ If $a \colon A _ { * } \ \to \ B _ { * }$ and $b _ { * } \colon B _ { * } \to C ,$ are chain maps, what can we say about $\mathsf { c o n e } ( b \circ a ) ?$ Show how to arrange the six groups $H _ { * } ( A ) , H _ { * } ( B ) , H _ { * } ( C )$ $H _ { * } ( \mathsf { c o n e } ( a ) ) , H _ { * } ( \mathsf { c o n e } ( b ) )$ and $\scriptstyle H _ { * } ( \mathsf { c o n e } ( b a ) )$ as the vertices of an octahedral diagram of maps. Four of the faces should be commuting triangles, the other four exact triangles (i.e., long exact sequences visualised as triangles). The last of these triangles is a long exact sequence

$$
\cdots \to H _ { p } ( \mathsf { c o n e } ( a ) ) \to H _ { p } ( \mathsf { c o n e } ( b a ) ) \to H _ { p - 1 } ( \mathsf { c o n e } ( b ) ) \to \dots . . .
$$

The hard part of the exercise is constructing this triangle and proving its exactness. [Hint: define $f \colon \mathsf { c o n e } ( a )  \mathsf { c o n e } ( b a )$ by $f ( x , y ) = ( x , b y )$ . There is a natural inclusion $i \colon \mathsf { c o n e } ( b ) \to \mathsf { c o n e } ( f )$ . Show that i is a chain-homotopy equivalence.]

This exercise shows shows that the derived category of the abelian category of chain complexes satisfies Verdier’s ‘octahedral axiom’ for triangulated categories.

## 10. Homotopy invariance of singular homology

We prove that singular homology is an invariant of homotopy type. We thereby we compute the homology of contractible spaces.

Proposition 10.1. Let ∗ denote a one-point space. Then $H _ { i } ( * ) = 0$ for all $i > 0$

Proof. There is exactly one simplex $\sigma _ { i }$ in each dimension. Thus the singular complex is

$$
\begin{array} { r } { \cdot \cdot \cdot \longrightarrow \mathbb { Z } \sigma _ { 2 } \longrightarrow \mathbb { Z } \sigma _ { 1 } \longrightarrow \mathbb { Z } \sigma _ { 0 } \longrightarrow 0 . } \end{array}
$$

Since $\sigma _ { n } \circ \delta _ { i } = \sigma _ { n - 1 }$ , the boundary operator is given by

$$
\partial _ { n } \sigma _ { n } = \sum _ { i = 0 } ^ { n } ( - 1 ) ^ { i } \sigma _ { n - 1 } = \frac { 1 } { 2 } [ 1 + ( - 1 ) ^ { n } ] \sigma _ { n - 1 } .
$$

Thus the complex is

$$
\cdots \to \mathbb { Z } \sigma _ { 3 } \overset { 0 } { \to } \mathbb { Z } \sigma _ { 2 } \overset { 1 } { \to } \mathbb { Z } \sigma _ { 1 } \overset { 0 } { \to } \mathbb { Z } \sigma _ { 0 } \to 0 .
$$

So ker $\partial _ { i } = 0$ when i is even and positive; and when i is odd, $\partial _ { i + 1 }$ is onto. Thus $H _ { i } ( * ) = 0$ when $i > 0$ . As expected, we find $H _ { 0 } ( * ) \cong \mathbb { Z }$ 

Maps between spaces introduce homomorphisms between homology groups. Given $f \colon X \to Y$ , define $f _ { \# } \colon S _ { n } ( X ) \to S _ { n } ( Y )$ by

$$
f _ { \# } ( \sigma ) = f \circ \sigma .
$$

It is clear that this is a chain map: $\partial _ { n } f _ { \# } = f _ { \# } \partial _ { n }$ . Thus there is an induced map

$$
f _ { * } = H _ { n } ( f ) \colon H _ { n } ( X ) \to H _ { n } ( Y ) .
$$

Notice that if $g \colon Y \ \to \ Z$ is another map then $( g \circ f ) _ { \# } = g _ { \# } \circ f _ { \# }$ , and hence $( g \circ f ) _ { * } = g _ { * } \circ f _ { * }$

Remark. In categorical language, we can express this by saying that $H _ { n }$ defines a functor from the category Top of topological space and continuous maps to the category Ab of abelian groups and homomorphisms. That is, $H _ { n }$ associates with each space X an abelian group $H _ { n } ( X )$ ; with each map $f \colon X \to Y$ a homomorphism $H _ { n } ( f ) \colon H _ { n } ( X ) \to H _ { n } ( Y )$ ; and the homomorphism $H _ { n } ( g \circ f )$ associated with a composite is the composite $H _ { n } ( g ) \circ H _ { n } ( f )$ . Moreover, identity maps go to identity maps.

Theorem 10.2. Suppose that F is a homotopy from $f _ { 0 } \colon X \to Y$ to $f _ { 1 } \colon X \to Y$ The homotopy then gives rise to a chain homotopy $P ^ { F } \colon S _ { * } ( X ) \to S _ { * + 1 } ( Y )$ from $\left( f _ { 0 } \right) _ { \# } t o \left( f _ { 1 } \right) _ { \# }$ , that is, a sequence of maps $P _ { n } ^ { F } \colon \bar { S _ { n } } ( X ) \to \dot { S _ { n + 1 } } \bar { ( Y ) }$ such that

$$
\partial _ { n + 1 } \circ P _ { n } ^ { F } + P _ { n - 1 } ^ { F } \circ \partial _ { n } = ( f _ { 1 } ) _ { \# } - ( f _ { 0 } ) _ { \# } .
$$

Hence $H _ { n } ( f _ { 0 } ) = H _ { n } ( f _ { 1 } )$

Corollary 10.3. $I f f \colon X \to Y$ is a homotopy equivalence then $H _ { n } ( f )$ is an isomorphism for all n.

Corollary 10.4. A contractible space X has $H _ { i } ( X ) = 0$ for all $i > 0$

Remark. We can express the theorem in categorical language. Define a category hTop whose objects are topological spaces, and whose morphisms are homotopy classes of continuous maps. Then singular homology defines a sequence of functors $H _ { n } \colon \mathbf { h T o p } \to \mathbf { A b }$

To prove the theorem, we begin with low-dimensional cases, because there the geometry is transparent.

Proof of the theorem when n is 0 or 1. First, given a 0-simplex $\rho \colon \Delta ^ { 0 } \to X$ , note that we have a 1-simplex $P _ { 0 } ^ { F } ( \rho ) : = F \circ \rho \colon I = \bar { \Delta } ^ { 1 } \to Y$ , and $\partial _ { 1 } ( P _ { 0 } ^ { F } ( \rho ) ) = f _ { 1 } \circ \rho -$ $f _ { 0 } \circ \rho .$

Next, consider some 1-simplex $\sigma \colon \Delta ^ { 1 } \to X$ . We want to examine $f _ { 1 } \circ \sigma - f _ { 0 } \circ \sigma$ Since $\Delta ^ { 1 } = I$ , our homotopy $F$ defines a map on from the square $\Delta ^ { 1 } \times I \ \mathrm { t o } \ Y$

$$
F \circ ( \sigma \times \operatorname { i d } _ { I } ) \colon \Delta ^ { 1 } \times I .
$$

But the square is a union of two 2-simplices along a common diagonal. To notate this, let the bottom edge be $\Delta ^ { 1 } \times \{ 0 \} = \bar { [ } v _ { 0 } , v _ { 1 } ]$ , and the top edge $\Delta ^ { 1 } \times \{ 1 \} = [ w _ { 0 } , w _ { 1 } ]$ Thus the square is the convex hull $[ v _ { 0 } , v _ { 1 } , w _ { 0 } , w _ { 1 } ]$ of its four vertices. It is the union of the two triangles $[ v _ { 0 } , v _ { 1 } , w _ { 1 } ]$ and $[ v _ { 0 } , w _ { 0 } , w _ { 1 } ]$ along the common edge $[ v _ { 0 } , w _ { 1 } ]$ . Note that by expressing these triangles as convex hulls, we implicitly identify them with the geometric 2-simplex $\Delta ^ { 2 } { \mathrm { ; } }$ : for the first of them, say, the point $t _ { 0 } v _ { 0 } + t _ { 1 } v _ { 1 } + t _ { 2 } w _ { 1 }$ corresponds to the $( t _ { 0 } , t _ { 1 } , t _ { 2 } ) \in \Delta ^ { 2 }$

Now define a 2-chain $P _ { 1 } ^ { F } ( \sigma )$ by applying F to each of these two simplices:

$$
\begin{array} { r } { P _ { 1 } ^ { F } ( \sigma ) = F \circ ( \sigma \times \mathrm { i d } _ { I } ) | _ { [ v _ { 0 } , w _ { 0 } , w _ { 1 } ] } - F \circ ( \sigma \times \mathrm { i d } _ { I } ) | _ { [ v _ { 0 } , v _ { 1 } , w _ { 1 } ] } } \end{array}
$$

We have

$$
\partial _ { 2 } P _ { 1 } ^ { F } ( \sigma ) = f _ { 1 } \circ \sigma - f _ { 0 } \circ \sigma + P _ { 0 } ^ { F } ( \partial _ { 1 } \sigma ) :
$$

the first terms come fom the top of the square, the second term from the bottom, and the third from the two other sides. Thus, defining $P _ { 1 } ^ { F } \colon S _ { 1 } ( X ) \to S _ { 0 } ( Y )$ and $P _ { 2 } ^ { F } \colon S _ { 2 } ( X ) \to S _ { 1 } ( Y )$ by linearly extending the definitions from simplices to singular chains, we have that

$$
\partial _ { 2 } P _ { 2 } ^ { F } + P _ { 1 } ^ { F } \partial _ { 1 } = ( f _ { 1 } ) _ { \# } - ( f _ { 0 } ) _ { \# } .
$$

Proof of the theorem in arbitrary dimensions. We proceed in the same way. For an n-simplex $\sigma \colon \Delta ^ { n } \to X$ , we have a map

$$
F \circ ( \sigma \times \operatorname { i d } _ { I } ) \colon \Delta ^ { n } \times I \to Y
$$

defined on the ‘prism’ $\Delta ^ { n } \times I .$ and we want to express this as a sum of n+1-simplices. To do this, we think of the prism as the convex hull $\left[ v _ { 0 } , \ldots , v _ { n } , w _ { 0 } , \ldots , w _ { n } \right]$ , where $v _ { i }$ is the ith vertex of $\Delta \times \{ 0 \} = \Delta$ , and $w _ { i }$ the ith vertex of $\Delta \times \{ 1 \} = \Delta$ . Then one can check (as Hatcher does) that

$$
\Delta \times I = \bigcup _ { i = 0 } ^ { n } [ v _ { 0 } , \ldots , v _ { i } , w _ { i } , w _ { i + 1 } , \ldots , w _ { n } ] ,
$$

that each $\left[ v _ { 0 } , \ldots , v _ { i } , w _ { i } , w _ { i + 1 } , \ldots , w _ { n } \right]$ is an n + 1-simplex, and that these simplices intersect along common faces. This gives $\Delta \times I$ the structure of a ∆-complex.

We now define

$$
P _ { n } ^ { F } ( \sigma ) = \sum _ { i = 0 } ^ { n } { ( - 1 ) ^ { i } F \circ ( \sigma \times \mathrm { i d } _ { I } ) | _ { [ v _ { 0 } , \dots , v _ { i } , w _ { i } , w _ { i + 1 } , \dots , w _ { n } ] } } ,
$$

extending by linearity to get a map $P _ { n } ^ { F } \colon S _ { n } ( X ) \to S _ { n + 1 } ( Y )$ . The boundary of $P _ { n } ( \sigma )$ should then consist (geometrically and hence algebraically) of $f _ { 1 } \circ \sigma , f _ { 0 } \circ \sigma$ and $P _ { n - 1 } ( \partial \sigma )$ . Since we did not actually verify that we had a ∆-complex, let us instead verify algebraically that $P ^ { F }$ defines a chain homotopy.

We have

$$
\begin{array} { l } { { \displaystyle \partial _ { n + 1 } { \cal P } _ { n } ^ { F } ( \sigma ) = \sum _ { j \leq i } ( - 1 ) ^ { i + j } { \cal F } \circ ( \sigma \times \mathrm { i d } _ { I } ) \vert _ { [ v _ { 0 } , \dots , \hat { v } _ { j } \dots , v _ { i } , w _ { i } , \dots , w _ { n } ] } } } \\ { { \displaystyle \qquad + \sum _ { l > k } ( - 1 ) ^ { k + l } { \cal F } \circ ( \sigma \times \mathrm { i d } _ { I } ) \vert _ { [ v _ { 0 } , \dots , v _ { k } , w _ { k } , \dots , \hat { w } _ { l - 1 } \dots , w _ { n } ] } . } } \end{array}
$$

The term with $j = i = 0$ in the first sum is

$$
F \circ ( \sigma \times \mathrm { i d } _ { I } ) | _ { [ w _ { 0 } , \ldots , w _ { n } ] } = f _ { 1 } \circ \sigma .
$$

The term with $l = k + 1 = n$ in the second sum is

$$
- F \circ ( \sigma \times \mathrm { i d } _ { I } ) | _ { [ v _ { 0 } , \ldots , v _ { n } ] } = - f _ { 0 } \circ \sigma .
$$

Next we look for the cancelling pairs of faces which we expect geometrically. These appear as the equality of $\bigl [ v _ { 0 } , \ldots , \hat { v } _ { i } , w _ { i } , \ldots , w _ { n } \bigr ] = \bigl [ v _ { 0 } , \ldots , v _ { i - 1 } , \hat { w } _ { i - 1 } , \ldots , w _ { n } \bigr ]$ . Apart from the exceptional cases $i = j = 0$ and $l = k + 1 = n .$ , the $j = i$ term in the first sum cancels with the $l = k + 1$ term in the second sum where $k = i - 1$ . So, at this point we have

$$
\begin{array} { l } { { \displaystyle \partial _ { n + 1 } P _ { n } ^ { F } ( \sigma ) = f _ { 1 } \circ \sigma - f _ { 0 } \circ \sigma } } \\ { { \displaystyle \qquad + \sum _ { j < i } ( - 1 ) ^ { i + j } F \circ ( \sigma \times \mathrm { i d } _ { I } ) \vert _ { [ v _ { 0 } , \dots \hat { v } _ { j } \dots , v _ { i } , w _ { i } , \dots , w _ { n } ] } } } \\ { { \displaystyle \qquad + \sum _ { l > k } ( - 1 ) ^ { k + l + 1 } F \circ ( \sigma \times \mathrm { i d } _ { I } ) \vert _ { [ v _ { 0 } , \dots , v _ { k } , w _ { k } , \dots \hat { w } _ { l } \dots , w _ { n } ] } . } } \end{array}
$$

We want the two sums here to total $- P _ { n } ^ { F } ( \partial _ { n } \sigma )$ . But if $j < i ,$ , then

$$
P _ { n } ^ { F } ( \sigma \circ \delta _ { i } ) = \sum _ { j } { ( - 1 ) ^ { j + i - 1 } ( \sigma \times \mathrm { i d } _ { I } ) | _ { [ v _ { 0 } , \dots \hat { v } _ { j } \dots v _ { i } , w _ { i } , \dots , w _ { n } ] } } .
$$

If $j \geq i$ then instead

$$
P _ { n } ^ { F } ( \sigma \circ \delta _ { i } ) = \sum _ { j } { ( - 1 ) ^ { j + i } ( \sigma \times \mathrm { i d } _ { I } ) | _ { [ v _ { 0 } , \dots \dots , v _ { i } , w _ { i } , \dots \hat { w } _ { j - 1 } \dots , w _ { n } ] } } .
$$

So the desired equality does indeed hold.

Exercise 10.1: Suppose that X is a subspace of $\mathbb { R } ^ { n }$ such that there is a map $r \colon \mathbb { R } ^ { n } \to X$ with $r | _ { X } = \operatorname { i d } _ { X }$ . Show that X has the homology of a point.

Exercise 10.2: Compute the first homology group $H _ { 1 }$ of the n-torus $T ^ { n } = ( S ^ { 1 } ) ^ { n }$ . Use this to construct a surjective homomorphism $G \to G L _ { n } ( \mathbb { Z } )$ , where G is the group of homotopy equivalences $T ^ { n } \to T ^ { n }$ . Show that when $n = 1$ its kernel consists of maps homotopic to the identity.

Exercise 10.3: (\*) The model Dehn twist on the annulus $A = [ - 1 , 1 ] \times ( \mathbb { R } / \mathbb { Z } )$ is the homeomorphism $t \colon A \to A$ of form $( s , t ) \mapsto ( s , t + ( s + 1 ) / 2 )$ . A Dehn twist along an embedded circle C in a surface S is a homeomorphism $S  S$ obtained by identifying a neighbourhood of C with $A ,$ and ‘transplanting’ a model Dehn twist into S. (I am being careless about right/left-handed twists.)

Let Σ be a genus 2 surface, and $C \subset \Sigma :$ a circle dividing it into two 1-holed tori. Show that if $f$ is a Dehn twist along C then $f _ { * }$ acts on $H _ { 1 } ( \Sigma )$ as the identity, but f is not homotopic to the identity map.

## 11. The locality property of singular chains

There is a ‘locality’ theorem for singular chains, reminiscent of the proof of van Kampen’s theorem on $\pi _ { 1 }$ . This may be regarded as the technical core of singular homology theory. We do not give a complete proof, but we reduce it to a lemma concerning the geometric p-simplex $\Delta ^ { p }$

Definition 11.1. An excisive triad is a triple $( X ; A , B )$ with X a space and A, B subspaces of X such that $X = \operatorname { i n t } ( A ) \cup \operatorname { i n t } ( B )$

Theorem 11.2 (locality for singular chains). Suppose $( X ; A , B )$ is an excisive triad. Let $S _ { n } ( A + B )$ denote the subgroup of $S _ { n } ( X )$ generated by the images of $\Sigma _ { n } ( A )$ and $\Sigma _ { n } ( B )$ . Notice that it is a subcomplex. Then the inclusion map

$$
i \colon S _ { * } ( A + B ) \to S _ { * } ( X )
$$

is a quasi-isomorphism.

(Hatcher proves that i is a chain-homotopy equivalence, but this is more than we need.)

Setting up the proof. Form the quotient complex $Q _ { * } ~ = ~ S _ { * } ( X ) / \operatorname { i m } ( i )$ . Then we have a short exact sequence

$$
0 \to S _ { * } ( A + B ) { \overset { i } { \to } } S _ { * } ( X ) \to Q _ { * } \to 0
$$

and hence a long exact sequence of homology groups

$$
\cdots \to H _ { p + 1 } ( Q _ { * } ) \to H _ { p } ( S _ { * } ( A + B ) ) \ { \overset { i * } { \to } } \ H _ { p } ( X ) \to H _ { p } ( Q _ { * } ) \to \dots .
$$

The theorem asserts that $i _ { * }$ is an isomorphism. From the long exact sequence, we see that this is equivalent to the assertion that $Q _ { * }$ is acyclic, i.e., that

$$
H _ { p } ( Q _ { * } ) = 0 \quad { \mathrm { f o r ~ a l l ~ } } p \in \mathbb { Z } .
$$

Thus we have to show that if q is a singular p-chain representing a cycle in $q ,$ so

$$
\partial q = r + s
$$

with $r \in S _ { p - 1 } ( A )$ and $s \in S _ { p - 1 } ( B )$ , then there are p-chains $a \in S _ { p } ( A )$ and $b \in$ $S _ { p } ( B )$ , and a $( p + 1 )$ -chain $c \in S _ { p + 1 } ( X )$ , such that

$$
q = a + b + \partial c .
$$

Clearly it suffices to do this when q is a simplex. ${ \mathrm { S o } } ,$ in words: we must show that any σ : $\Delta ^ { p }  X$ is homologous to the sum of a p-chain in A and a p-chain in B. 

We could hope to find such a homology by breaking up the simplex σ as a union of sub-simplices making $\Delta ^ { p }$ into a ∆-complex. If the p-simplices in this decomposition are sufficiently small then they will map either to A or to B under $\sigma .$ When σ is a 1-simplex, i.e., a path $I  X$ , it is clear how we could do this: we write $I = [ 0 , 1 / 2 ] \cup [ 1 / 2 , 1 ]$ . Then $\sigma$ is homologous to $\sigma | _ { [ 0 , 1 / 2 ] } + \sigma | _ { [ 1 / 2 , 1 ] }$ . Iterating this subdivision k times, we break up the unit interval into sub-intervals of length $2 ^ { - k } { \mathrm { ; } }$ ; when $k \gg 0 .$ , each sub-interval will map into $\operatorname { i n t } ( A )$ or $\operatorname { i n t } ( B )$

The proof in higher dimensions uses a generalization of this subdivision of $\Delta ^ { 1 }$

Lemma 11.3 (Subdivision lemma). The geometric p-simplex $\Delta ^ { p }$ can be decomposed as a p-dimensional ∆-complex in such a way that all the p-simplices $\tau _ { 1 } , \ldots , \tau _ { N }$ in this decomposition have diameter < 1, and such that in the singular chain complex $S _ { * } ( \Delta ^ { p } )$ , one has

$$
\mathrm { i d } _ { \Delta ^ { p } } - \sum _ { i } \tau _ { i } \in \mathrm { i m } \partial _ { p + 1 } .
$$

Here we regard $\mathrm { i d } _ { \Delta ^ { p } }$ as a p-simplex in $\Delta ^ { p }$ . (In fact, one can take $N = p !$ and the diameters to be $\leq { \frac { p } { p + 1 } } . )$

The particular subdivision we have in mind here is called barycentric subdivision. For the proof of the lemma we refer to Hatcher (it can be extracted from Steps 1 and 2 of the proof of the Excision Theorem). We will at least say what the barycentric subdivision is. The barycenter b of a p-simplex $[ v _ { 0 } , \ldots , v _ { p } ]$ is the point

$$
b = { \frac { 1 } { p + 1 } } ( v _ { 0 } + \cdot \cdot \cdot + v _ { p } ) .
$$

We now define the barycentric subdivision by induction on $p .$ . When $p = 0$ , the subdivision of $\Delta ^ { 0 } = [ v _ { 0 } ]$ has just one simplex: [v0] itself. When $p > 0 .$ , the $p \mathrm { - }$ simplices of the barycentric subdivision of $[ v _ { 0 } , \ldots , v _ { p } ]$ are of form $[ b , w _ { 0 } , \dotsc , w _ { p - 1 } ]$ where $[ w _ { 0 } , \dotsc , w _ { p - 1 } ]$ is a $( p - 1 )$ -simplex in the barycentric subdivision of some face $[ v _ { 0 } , \ldots , \hat { v } _ { i } , \ldots , v _ { p } ]$ of $[ v _ { 0 } , \ldots , v _ { p } ]$

The subdivision lemma is a little fiddly to prove. Since we are omitting the proof, let us emphasize that this is an entirely combinatorial lemma concerning convex geometry in Euclidean spaces; the target space X does not appear at all.

Proof of locality, granting the subdivision lemma. Write $\begin{array} { r } { \beta = \sum _ { i } \tau _ { i } \in S _ { p } ( \Delta ^ { p } ) } \end{array}$ . Now, each $\tau _ { i }$ is a map $\Delta ^ { p }  \Delta ^ { p }$ (actually an embedding), so we can iterate the subdivision process, considering the composed maps $\tau _ { j } \circ \tau _ { i } \colon \Delta ^ { p } \ :  \ : \Delta ^ { p }$ . Let’s write $\begin{array} { r } { \beta ^ { 2 } = \sum _ { i , j } \tau _ { j } \circ \tau _ { i } } \end{array}$ , and more generally

$$
\beta ^ { n } = \sum _ { i _ { 1 } , . . . , i _ { n } } \tau _ { i _ { n } } \circ \cdot \cdot \cdot \circ \tau _ { i _ { 1 } } .
$$

By induction on $n ,$ we have that $\mathrm { i d } _ { \Delta ^ { p } } - \beta ^ { n } \in \mathrm { i m } \partial _ { p + 1 }$

Let $1 - \epsilon$ be the maximum diameter of one of the $\tau _ { i }$ . Any $x \in \Delta ^ { p }$ has an open neighbourhood $N _ { x }$ such that $\sigma ( N )$ is contained in int(A) or in int(B), since these are open sets that cover X. But the image of $\tau _ { i _ { n } } \circ \cdots \circ \tau _ { i _ { 1 } }$ has diameter $\leq ( 1 - \epsilon ) ^ { n }$ so for large enough n, Nx is contained is the image of such a simplex. Thus $\Delta ^ { p }$ is covered by subdivided simplices $\tau _ { i _ { n } } \circ \cdots \circ \tau _ { i _ { 1 } }$ which map either to $\operatorname { i n t } ( A )$ or to int(B). A priori, the number n depends on x, but because $\Delta ^ { p }$ is compact we can use the same $n = n _ { 0 }$ for all these subdivided simplices.

We know that $\mathrm { i d } _ { \Delta ^ { p } } - \beta ^ { n _ { 0 } } \in B _ { p } ( \Delta ^ { p } )$ (recall that $B _ { p }$ denotes im $\partial _ { p + 1 } )$ ), and applying σ we find that

$$
\sigma - \sigma _ { \# } \circ \beta ^ { n _ { 0 } } \in B _ { p } ( X ) .
$$

But $\sigma _ { \# } \circ \beta ^ { n _ { 0 } }$ is the sum of simplices $\sigma \circ \tau _ { i _ { n _ { 0 } } } \circ \cdot \cdot \cdot \circ \tau _ { i _ { 1 } }$ that map either to $\operatorname { i n t } ( A )$ or to int(B). This proves the theorem.

## 12. Mayer–Vietoris and the homology of spheres

The locality theorem from the previous lecture has an important consequence: the exact Mayer–Vietoris sequence. Using this sequence, we can at last carry out interesting calculations in singular homology. We show that the homotopy type of $S ^ { n }$ , and hence the homeomorphism type of $\mathbb { R } ^ { n }$ , detects the dimension n.

12.1. The Mayer–Vietoris sequence. We extract from the locality theorem an extremely useful computational tool in singular homology.

Theorem 12.1. Suppose $( X ; A , B )$ is an excisive triad. Let a : $A \to X , b \colon B \to X$ , $\alpha \colon A \cap B \to A$ and $\beta \colon A \cap B \to B$ be the inclusion maps. Then there is a canonical long exact sequence

$$
\begin{array} { r } { \cdots \to H _ { p } ( A \cap B ) { \overset { \alpha _ { * } \to \beta _ { * } } { \longrightarrow } } H _ { p } ( A ) \oplus H _ { p } ( B ) { \overset { ( a _ { * } , b _ { * } ) } { \longrightarrow } } H _ { p } ( X ) { \overset { \delta } { \longrightarrow } } H _ { p - 1 } ( A \cap B ) \to \dots . . . } \end{array}
$$

Remark. Since $H _ { - 1 } ( A \cap B ) = 0$ , the sequence ends with $\cdot \cdot \cdot  H _ { 0 } ( A ) \oplus H _ { 0 } ( B ) $ $H _ { 0 } ( X ) \to 0$

Proof. There’s a short exact sequence of chain complexes

$$
0 \to S _ { * } ( A \cap B ) { \overset { \alpha - \beta } { \to } } S _ { * } ( A ) \oplus S _ { * } ( B ) { \overset { a + b } { \to } } S _ { * } ( A + B ) \to 0 ,
$$

simply because $S _ { * } ( A \cap B ) = S _ { * } ( A ) \cap S _ { * } ( B )$ . This results in a long exact sequence of homology groups. But $H _ { n } ( S _ { * } ( A + B ) ) = H _ { n } ( X )$ by the locality theorem, and hence the long exact sequence has the form claimed. 

Exercise 12.1: Show that the connecting map δ can be understood as follows. Take a p-cycle $z \in S _ { p } ( X )$ . By locality, there is a homologous p-cycle $z ^ { \prime } = x + y$ with x a chain in A and y a chain in B. Then $\partial x = - \partial y$ , hence ∂x is a cycle in $A \cap B$ . We have $\delta [ z ] = [ \partial x ]$

Exercise 12.2: Show that the Mayer–Vietoris sequence is not merely canonical, but also natural in the following sense. Given an another excisive triad $( X ^ { \prime } ; A ^ { \prime } , B ^ { \prime } )$ and a map $f \colon X \to X ^ { \prime }$ such that $f ( A ) \subset A ^ { \prime }$ and $f ( B ) \subset B ^ { \prime }$ , the two long exact sequences and the maps between them induced by f form a commutative diagram.

Example 12.2. As a first example of the Mayer–Vietoris sequence, let us prove that

$$
H _ { * } ( S ^ { 1 } ) = \mathbb { Z } \oplus \mathbb { Z }
$$

where the first Z is in degree 0, the second Z in degree 1. We have $S ^ { 1 } = A \cup B$ where $A = S ^ { 1 } \setminus \{ ( 1 , 0 ) \}$ and $B = S ^ { 1 } \setminus \{ ( - 1 , 0 ) \}$ . Then $A \cap B \simeq S ^ { 0 }$ . Since A and B are contractible, and A ∩ B the disjoint union of two contractible components, the exactness of the Mayer–Vietoris sequence

$$
H _ { p } ( A ) \oplus H _ { p } ( B ) \to H _ { p } ( S ^ { 1 } ) \to H _ { p - 1 } ( A \cap B ) ,
$$

tells us that $H _ { p } ( S ^ { 1 } ) = 0$ for all $p > 1$ . We already know $H _ { 1 } ( S ^ { 1 } ) = \mathbb { Z } = H _ { 0 } ( S ^ { 1 } )$ (via $\pi _ { 1 }$ and path-connectedness), but let’s see that we can recover this by the present method. The sequence ends with the 6-term sequence

$$
0 \to H _ { 1 } ( S ^ { 1 } ) \to \mathbb { Z } ^ { 2 } \to \mathbb { Z } ^ { 2 } \to H _ { 0 } ( S ^ { 1 } ) \to 0 ,
$$

where the map $\mathbb { Z } ^ { 2 } = H _ { 0 } ( A \cap B )  H _ { 0 } ( A ) \oplus H _ { 0 } ( B ) = \mathbb { Z } ^ { 2 }$ is given by $( m , n ) \mapsto$ $( m - n , m - n )$ Thus $H _ { 1 } ( S ^ { 1 } )$ is isomorphic to the kernel of this map, which is $\mathbb { Z } ( 1 , 1 )$ 1), and $H _ { 0 } ( S ^ { 1 } )$ to its cokernel, which is also $\mathbb { Z }$

Proposition 12.3. We have

$$
H _ { * } ( S ^ { n } ) \cong \mathbb { Z } \oplus \mathbb { Z } , \quad n \geq 0 ,
$$

where the first Z is in degree 0, the second $\mathbb { Z }$ in degree n.

Proof. By induction on n. Since $S ^ { 0 }$ is a 2-point space, it’s true for that case. We’ve just proved it for $n = 1$ , so we’ll start the induction there.

So now assume $n > 1$ . We have $S ^ { n } = A \cup B$ where $A = S ^ { n } \setminus \{ N \}$ and $B =$ $S ^ { n } \setminus \{ S \}$ , N and S being the north and south poles. Then $A \cap B \simeq S ^ { n - 1 }$ . Since A and B are contractible, Mayer–Vietoris tells us that $H _ { p } ( A ) \oplus H _ { p } ( B ) = 0$ for $p > 0$ Thus, from the exactness of

$$
H _ { p } ( A ) \oplus H _ { p } ( B ) \to H _ { p } ( S ^ { n } ) \to H _ { p - 1 } ( A \cap B ) \to H _ { p - 1 } ( A ) \oplus H _ { p - 1 } ( B ) ,
$$

we see that $H _ { p } ( S ^ { n } ) \cong H _ { p - 1 } ( S ^ { n - 1 } )$ for all $p > 1$ . We also have an exact sequence

$$
0 \to H _ { 1 } ( S ^ { 1 } ) \to \mathbb { Z } \to \mathbb { Z } ^ { 2 } ,
$$

where the map $\mathbb { Z } = H _ { 0 } ( A \cap B )  H _ { 0 } ( A ) \oplus H _ { 0 } ( B ) = \mathbb { Z } ^ { 2 }$ is $n \mapsto ( n , - n )$ , and so is injective. Hence $H _ { 1 } ( S ^ { n } ) = 0$ (which we knew anyway, $S ^ { n }$ being simply connected.) 

Remark. The argument can be made slicker using reduced homology.

Note that, in all dimensions (even n = 1) the connecting map $\delta _ { n } \colon H _ { n } ( S ^ { n } ) \to$ $H _ { n - 1 } ( S ^ { n } )$ is an isomorphism.

Exercise 12.3: Describe an n-cycle $c _ { n } \in S _ { n } ( S ^ { n } )$ that generates $H _ { n } ( S ^ { n } )$ . (Prove that your cycle generates by induction, looking at the explicit form of the connecting map.)

We now take a break from the formal development of the theory and harvest some applications.

Theorem 12.4. $I f \mathbb { R } ^ { n }$ is homeomorphic to $\mathbb { R } ^ { m }$ then $m = n$

Proof. We may assume that m and n are positive. If $\mathbb { R } ^ { m } \cong \mathbb { R } ^ { n }$ then $\mathbb { R } ^ { m } \setminus \left\{ 0 \right\} \cong$ $\mathbb { R } ^ { n } \setminus \left\{ { \mathrm { p t . } } \right\} \cong \mathbb { R } ^ { n } \setminus \left\{ 0 \right\}$ , hence $S ^ { n - 1 }$ is homotopy equivalent to $S ^ { m - 1 }$ . But $S ^ { n - 1 }$ and $S ^ { m - 1 }$ have different homology in degree $n - 1$ , unless $m = n .$ 

Theorem 12.5 (Brouwer fixed point theorem). Let $D ^ { n }$ denote the closed n-ball in $\mathbb { R } ^ { n } , n \geq 1$ . Then every continuous map $D ^ { n } \to D ^ { n }$ fixes a point.

Proof. Recall that we already proved this using $\pi _ { 1 } ,$ when $n = 2 .$ . By the same argument that we gave there, it suffices to show there is no retraction $r \colon D ^ { n } \to$ $\partial D ^ { n } = S ^ { n - 1 }$ , i.e. no r such that $r \circ i = \operatorname { i d } _ { S ^ { n - 1 } }$ , where $i \colon S ^ { n - 1 } \to D ^ { n }$ denotes the inclusion map. If such an r existed, we would have

$$
\operatorname { i d } _ { H _ { n - 1 } ( X ) } = H _ { n - 1 } ( r ) \circ H _ { n - 1 } ( i ) .
$$

But $H _ { n - 1 } ( S ^ { n - 1 } ) \neq 0$ , whereas $H _ { n - 1 } ( D ^ { n } )$ (the target of $H _ { n - 1 } ( i ) )$ is zero, assuming $n > 1$ . This proves the theorem (except when $n = 1 ;$ but in that case it follows from the intermediate value theorem). ## 12.2. Degree. Define the degree deg(f) of a map $f \colon S ^ { n } \to S ^ { n }$ by the equation

$$
H _ { n } ( f ) ( m ) = \deg ( f ) m , \quad m \in H _ { n } ( S ^ { n } ) \cong \mathbb { Z } .
$$

The following properties of degree follow from the definition and the basic properties of homology:

(1) Homotopic maps have the same degree.

(2) $\deg ( \operatorname { i d } _ { S ^ { n } } ) = 1 .$

(3) deg $f = 0$ when f extends to a map $D ^ { n + 1 } \to S ^ { n }$

(4) $\deg ( f g ) = \deg ( f ) \deg ( g )$

You will find solutions to the following exercise in Hatcher, but I recommend trying to work it out for yourself.

Exercise 12.4: Degree has the following further properties:

(i) When $n = 1$ , the homological degree defined here coincides with the degree as we defined it earlier via $\pi _ { 1 } ( S ^ { 1 } )$

(ii) deg $s = - 1$ when s is the restriction to $S ^ { n }$ of a reflection in $\mathbb { R } ^ { n + 1 }$

(iii) deg $a = ( - 1 ) ^ { n + 1 }$ when a is the antipodal map $x \mapsto - x$

(iv) deg $f = ( - 1 ) ^ { n + 1 }$ when f has no fixed points.

Use the last point to show (a) that no group of order $> 2$ can act freely on $S ^ { 2 m }$ , and (b) that $S ^ { 2 m }$ possesses no nowhere-vanishing vector field.

Exercise 12.5: Complex projective n-space $\mathbb { C } P ^ { n }$ is defined as $( \mathbb { C } ^ { n + 1 } \setminus \{ 0 \} ) / \mathbb { C } ^ { * }$ , where $\mathbb { C } ^ { * }$ acts by scalar multiplication. Use Mayer–Vietoris to show that

$$
H _ { p } ( \mathbb { C } P ^ { n } ) \cong \left\{ { \begin{array} { l l } { \mathbb { Z } , } & { { \mathsf { i f } } \ p \ { \mathsf { i s \ e v e n \ a n d \ 0 } } \leq p \leq 2 n , } \\ { 0 , } & { { \mathsf { e l s e } } . } \end{array} } \right.
$$

Show, moreover, that the inclusion of $\mathbb { C } P ^ { n }$ in $\mathbb { C } P ^ { n + 1 }$ , induced by the inclusion of $\mathbb { C } ^ { n + 1 }$ as a linear subspace of $\mathbb { C } ^ { n + 2 }$ , induces an isomorphism on homology up to degree 2n.

Exercise 12.6: Use Mayer–Vietoris to compute $H _ { * } ( T ^ { 2 } ) , \ H _ { * } ( \mathbb { R } P ^ { 2 } )$ and $H _ { * } ( K ^ { 2 } )$ . In each case, find an explicit (minimal) collection of cycles that span the homology.

Exercise 12.7: Use Mayer–Vietoris to compute $H _ { * } ( \Sigma _ { g } )$ where $\Sigma _ { g }$ is a 2-sphere with g handles attached.

## 13. Relative homology and excision

13.1. Relative homology. Suppose $i \colon A \to X$ is the inclusion of a subspace. There is a short exact sequence of chain complexes

$$
0 \to S _ { * } ( A ) { \overset { i _ { \# } } { \to } } S _ { * } ( X ) \to S _ { * } ( X , A ) \to 0 ,
$$

where $S _ { * } ( X , A ) \ = \ S _ { * } ( X ) / i _ { \# } S _ { * } ( A )$ We denote by $H _ { * } ( X , A )$ the homology of $S _ { * } ( X , A )$ Thus a chain in X defines a cycle in $S _ { * } ( X , A )$ if its boundary is a sum of simplices in A. A map of pairs $f \colon ( X , A ) \to ( Y , B )$ induces $f _ { * } \colon H _ { * } ( X , A ) \to$ $H _ { * } ( Y , B )$

The short exact sequence for the pair (X, A) induces the long exact sequence of the pair

$$
\cdots \to H _ { p } ( A ) \ { \overset { i _ { * } } { \to } } \ H _ { p } ( X ) \to H _ { p } ( X , A ) \ { \overset { \delta } { \to } } \ H _ { p - 1 } ( A ) \to \dots . . .
$$

We can understand the connecting map δ as follows. If $c \in S _ { p } ( X , A )$ is a cycle, δ[c] is defined by lifting c to a chain ˜c in $S _ { p } ( X )$ , and putting $\delta [ \dot { c } ] = [ i _ { * } ( \partial _ { p } c ) ]$ . In other words, δ[c] is the boundary of a chain representing c, considered as a cycle in A.

Exercise 13.1: Show that if $B \subset A \subset X$ , one has a long exact sequence of the triple

$$
\cdots \to H _ { i } ( A , B ) \to H _ { i } ( X , B ) \to H _ { i } ( X , A ) \to H _ { i - 1 } ( A , B ) \to \dots ,
$$

and describe the maps in this sequence.

We now state the excision theorem. It has essentially the same content as the Mayer–Vietoris sequence.

Theorem 13.1 (Excision). Suppose $( X ; A , B )$ is an excisive triad. Then the map

$$
H _ { * } ( A , A \cap B ) \to H _ { * } ( X , B )
$$

induced by the inclusion $( A , A \cap B ) \to ( X , B )$ is an isomorphism.

Proof. We invoke the locality theorem for chains. Note that $H _ { * } ( A , A \cap B )$ is the homology of the complex $S _ { * } ( A ) / S _ { * } ( A \cap B ) = S _ { * } ( A ) / ( S _ { * } ( A ) \cap S _ { * } ( B ) )$ (where we think of $S _ { * } ( A )$ and $S _ { * } ( B )$ as subcomplexes of $S _ { * } ( X ) )$ . By a general property of abelian groups, the inclusion of $S _ { * } ( A )$ in $S _ { * } ( A ) + S _ { * } ( B )$ induces an isomorphism

$$
S _ { * } ( A ) / ( S _ { * } ( A ) \cap S _ { * } ( B ) ) \cong ( S _ { * } ( A ) + S _ { * } ( B ) ) / S _ { * } ( B ) .
$$

But $S _ { * } ( A ) + S _ { * } ( B ) = S _ { * } ( A + B )$ by definition of the latter, and the map $S _ { * } ( A { + } B ) $ $S _ { * } ( X )$ is a quasi-isomorphism. Let $I _ { n } = H _ { n } ( S _ { * } ( A + B ) / S _ { * } ( B ) )$ . Then we have a commutative diagram with exact rows

$$
{ \begin{array} { c c c c c c c c c c } { H _ { n } ( B ) } & { \longrightarrow } & { H _ { n } ( S _ { * } ( A + B ) ) } & { \longrightarrow } & { I _ { n } } & { \longrightarrow } & { H _ { n - 1 } ( B ) } & { \longrightarrow } & { H _ { n - 1 } ( S _ { * } ( A + B ) ) } \\ { = { \Big \downarrow } } & { \cong { \Big \downarrow } } & { \bigcup } & { \qquad } & { = { \Big \downarrow } } & { \cong { \Big \downarrow } } \\ { H _ { n } ( B ) } & { \longrightarrow } & { H _ { n } ( X ) } & { \longrightarrow } & { H _ { n } ( X , B ) } & { \longrightarrow } & { H _ { n - 1 } ( B ) } & { \longrightarrow } & { H _ { n - 1 } ( X ) } \end{array} }
$$

All the vertical arrows but the middle one are isomorphisms, and hence so is the middle one (this is the 5-lemma). Putting things together, we find that $S _ { * } ( A ) / S _ { * } ( A \cap B ) \to S _ { * } ( X ) / S _ { * } ( B )$ is a quasi-isomorphism, which is the result we want. 

Exercise 13.2: Re-derive $H _ { * } ( S ^ { n } ) \cong \mathbb { Z } _ { ( 0 ) } \oplus \mathbb { Z } _ { ( n ) }$ using excision.

Example 13.2. When working with spaces X equipped with basepoints $x ,$ it’s often useful to work with reduced homology $\tilde { H } _ { * }$ . We put

$$
{ \tilde { H } } _ { n } ( X ) = H _ { n } ( X , \{ x \} ) .
$$

Then, by the exact sequence of the pair, the natural map

$$
H _ { n } ( X ) \to { \tilde { H } } _ { n } ( X )
$$

is an isomorphism for all $n > 0$ . The end of the sequence looks like this:

$$
H _ { 1 } ( X , \{ x \} )  H _ { 0 } ( \{ x \} )  H _ { 0 } ( X )  H _ { 0 } ( X , \{ x \} )  0 .
$$

The map $H _ { 0 } ( \{ x \} ) \to H _ { 0 } ( X )$ is injective (which explains why $\tilde { H } _ { 1 } ( X ) = H _ { 1 } ( X ) )$ , so $\tilde { H } _ { 0 } ( X ) = H _ { 0 } ( X ) / H _ { 0 } ( \{ x \} )$ . Thus, when X is path connected, we have

$$
{ \tilde { H } } _ { n } ( X ) = { \left\{ \begin{array} { l l } { 0 , } & { n = 0 } \\ { H _ { n } ( X ) , } & { n > 0 . } \end{array} \right. }
$$

This justifies the omission of x from the notation (when X is not path connected, x is important).

$$
H _ { * } ( X , A )  H _ { * } ( X / A , A / A ) = \tilde { H } _ { * } ( X / A )
$$

Exercise 13.4: Show that if $( X ; A , B )$ is an excisive triad, and $b \in A \cap B \mathsf { a }$ basepoint, there is an exact Mayer–Vietoris sequence in reduced homology (formally the same as the usual one, but with H˜∗ instead of $H _ { * } )$

13.2. Suspension. We now set up the suspension isomorphisms. The (unreduced) suspension SX of X is the space $( X \times [ - 1 , 1 ] ) / \sim$ where $( x , t ) \sim ( x ^ { \prime } , t ^ { \prime } ) { \mathrm { ~ i f ~ } } t = t ^ { \prime } = 1$ or $t = t ^ { \prime } = - 1$ . For example, $S ( S ^ { n } ) \cong { \bf \bar { \Phi } } S ^ { n + 1 }$

Proposition 13.3. Fix a basepoint $x \in X$ . There are natural isomorphisms

$$
s _ { n } \colon \tilde { H } _ { n + 1 } ( S X ) \to \tilde { H } _ { n } ( X ) , \quad n \geq 0 .
$$

Proof. We have $S X = C _ { + } \cup C _ { - }$ , where

$$
C _ { + } = ( X \times [ - \frac 1 2 , 1 ] ) / ( X \times \{ 1 \} ) , \quad C _ { - } = ( X \times [ - 1 , \frac 1 2 ] ) / ( X \times \{ - 1 \} ) .
$$

Both $C _ { + }$ and $C _ { - }$ are cones on $X ;$ they deformation retract to their respective cone points $c _ { \pm } = ( X \times \{ \pm 1 \} ) / ( X \times \{ \pm 1 \} )$ . Thus

$$
H _ { n } ( S X , C _ { + } ) = H _ { n } ( S X , \{ c _ { + } \} ) = { \tilde { H } } _ { n } ( S X ) .
$$

On the other hand $( X ; C _ { + } , C _ { - } )$ is an excisive triad, so

$$
H _ { n } ( S X , C _ { + } ) \cong H _ { n } ( C _ { - } , C _ { + } \cap C _ { - } ) .
$$

Since $C _ { - }$ is contractible, the long exact sequence of the pair tells us that

$$
H _ { n } ( C _ { - } , C _ { + } \cap C _ { - } ) \to H _ { n - 1 } ( C _ { + } \cap C _ { - } ) = H _ { n - 1 } ( X )
$$

is an isomorphism when $n > 1$ , and that $H _ { 1 } ( C _ { - } , C _ { + } \cap C _ { - } ) = \tilde { H } _ { 0 } ( X )$ . Putting this together, we get isomorphisms

$$
\tilde { H } _ { n } ( S X ) \cong H _ { n } ( S X , C _ { + } ) \cong H _ { n } ( C _ { - } , C _ { + } \cap C _ { - } ) \cong \tilde { H } _ { n - 1 } ( X ) .
$$

Exercise 13.5: Show that the two spaces $S ^ { 2 } \vee S ^ { 4 }$ and $\mathbb { C } P ^ { 2 }$ have isomorphic homology groups. Likewise the two spaces $S ^ { 3 } \vee S ^ { 5 }$ and $S ( \mathbb { C } P ^ { 2 } )$

Remark. We will see later that the homotopy types of $S ^ { 2 } \vee S ^ { 4 }$ and $\mathbb { C } P ^ { 2 }$ can be distinguished by their cohomology rings, but that $\bar { S ^ { 3 } } \vee S ^ { 5 }$ and $S ( \mathbb { C } P ^ { 2 } )$ have isomorphic cohomology rings.

13.3. Summary of the properties of relative homology.

• To each pair of spaces $( X , A )$ , and each integer n, it assigns an abelian group $H _ { n } ( X , A )$ (and we write $H _ { n } ( X )$ for $H _ { n } ( X , \varnothing ) )$

• To each map $f \colon ( X , A ) \to ( X ^ { \prime } , A ^ { \prime } )$ and each $n \in \mathbb { Z }$ it assigns a homomorphism $H _ { n } ( f ) \colon H _ { n } ( X , A ) \to H _ { n } ( X ^ { \prime } , A ^ { \prime } )$ . One has $H _ { n } ( f \circ g ) = H _ { n } ( f ) \circ H _ { n } ( g )$ and $H _ { n } ( \operatorname { i d } _ { ( X , A ) } ) = \operatorname { i d } _ { H _ { n } ( X , A ) }$ . If f0 is homotopic to $f _ { 1 }$ via a homotopy $\{ f _ { t } \}$ such that $f _ { t } | _ { A } = f _ { 0 } | _ { A }$ , then $\prime H _ { n } ( f _ { 1 } ) = H _ { n } ( f _ { 0 } )$

• To each pair of spaces $( X , A )$ , and each integer $n ,$ it assigns a homomorphism

$$
\delta _ { n } \colon H _ { n } ( X , A ) \to H _ { n - 1 } ( A ) .
$$

These maps are natural transformations. That is, given $f \colon ( X , A ) \ $ $( X ^ { \prime } , A ^ { \prime } )$ , one has

$$
\delta _ { n } \circ H _ { n } ( f ) = H _ { n - 1 } ( f ) \circ \delta _ { n }
$$

as homomorphisms $H _ { n } ( X , A ) \to H _ { n - 1 } ( A ^ { \prime } )$

Besides these basic properties, the following also hold:

• DIMENSION: If ∗ denotes a 1-point space then $H _ { n } ( * ) = 0$ for $n \neq 0 ,$ , while $H _ { 0 } ( * ) = \mathbb { Z } .$

• EXACTNESS: The sequence

$$
\begin{array} { r } { \cdots \to H _ { n } ( A ) \to H _ { n } ( X ) \to H _ { n } ( X , A ) { \overset { \delta _ { n } } { \to } } H _ { n - 1 } ( A ) \to H _ { n - 1 } ( A ) \to \dots } \end{array}
$$

is exact, where the unlabelled maps are induced by the inclusions $( A , \varnothing ) \to$ $( X , \varnothing )$ and $( X , \emptyset ) \to ( X , A )$

• EXCISION: if $( X ; A , B )$ is an excisive triad then the map

$$
H _ { n } ( A , A \cap B ) \to H _ { n } ( X , B )
$$

induced by the inclusion $( A , A \cap B ) \to ( X , B )$ is an isomorphism.

• ADDITIVITY: If $\left( X _ { \alpha } , A _ { \alpha } \right)$ is a family of pairs, then one has an isomorphism

$$
\bigoplus _ { \alpha } H _ { n } ( X _ { \alpha } , A _ { \alpha } ) \to H _ { n } ( \prod _ { \alpha } X _ { \alpha } , \prod _ { \alpha } A _ { \alpha } )
$$

given by the sum of the maps induced by the inclusions into the disjoint union.

(Additivity is easy to check; for finite families, it follows from excision and exactness.)

Remark. As stated, these axioms do not uniquely characterise relative homology. However, they do characterise it if one restricts the pairs $( X , A )$ to be CW pairs. Alternatively, if we include one more axiom, that ‘weak equivalences’ induce isomorphisms on homology, then the axioms uniquely characterise the theory for arbitrary pairs, because every pair is weakly equivalent to a CW pair. If one omits the dimension axiom, there are many different homology theories on CW pairs, including stable homotopy, real or complex K-theory, and oriented, unoriented or complex bordism.

## 14. Vanishing theorems for homology of manifolds

Theorem 14.1. Let M be an n-manifold, i.e., a space locally homeomorphic to $\mathbb { R } ^ { n }$ . Then $H _ { p } ( M ) = 0$ for $p > n$

The proof will use Mayer–Vietoris sequences to increase the generality incrementally, starting from a very banal statement. So as to avoid low-dimensional exceptions, we use Mayer–Vietoris for reduced homology. However, we can and shall assume throughout that $n > 0$

Proof. Step $\textstyle 1 \colon I f n \geq 1$ and X is the union of strictly less than 2n of the faces of the n-cube $I ^ { n } { } _ { ; }$ , then $\tilde { H } _ { p } ( X ) = 0 f o r p \geq n - 1$

This we prove by induction on n; the $n = 1$ case is clear. The induction step is done by a further induction, on the number of faces of X. When X is empty it it trivial. Otherwise, choose a face F of $I ^ { n }$ which is contained in X, and let $X ^ { \prime } = X \setminus \operatorname { i n t } ( F )$ . Choose $F$ so that not all its neighbours are in X. Mayer–Vietoris (and a few deformation retractions of open neighbourhoods) then gives an exact seqence

$$
\tilde { H } _ { p } ( F ) \oplus \tilde { H } _ { p } ( X ^ { \prime } ) \to \tilde { H } _ { p } ( X ) \to \tilde { H } _ { p - 1 } ( F \cap X ^ { \prime } ) .
$$

But $F \cap X ^ { \prime }$ is a union of strictly less than $2 ( n - 1 )$ of the faces of the $( n - 1 )$ -cube $F _ { ; }$ so inductively $\tilde { H } _ { p - 1 } ( F \cap X ^ { \prime } ) = 0$ . Trivially $\tilde { H } _ { p } ( F ) = 0$ , and by induction on the number of faces, $\tilde { H } _ { p } ( X ^ { \prime } ) = 0$ . This completes the induction.

Step 2: $I f C _ { 1 } , \ldots , C _ { q }$ are integer cubes in $\mathbb { R } ^ { n }$ then $H _ { p } ( \bigcup _ { i } C _ { i } ) = 0 ~ f o r ~ p \ge n$

Here an integer cube C in $\mathbb { R } ^ { n }$ means a translate by some $( m _ { 1 } , \ldots , m _ { n } ) \in \mathbb { Z } ^ { n }$ of $I ^ { n }$ . We prove this by induction on the number of cubes q. A single cube is contractible. For the induction step, observe that one of the cubes, which we may take to be $C _ { q } .$ , has maximal x1-coordinate. It then intersects less than 2n of its neighbours. Write $D _ { q } = C _ { 1 } \cup \cdots \cup C _ { q }$ . We then have a Mayer–Vietoris sequence

$$
H _ { p } ( C _ { q } ) \oplus H _ { p } ( D _ { q - 1 } ) \to H _ { p } ( D _ { q } ) \to \tilde { H } _ { p - 1 } ( D _ { q - 1 } \cap C _ { q } ) .
$$

By induction, the left-hand term is zero for $p \geq n$ , so it suffices to show that $H _ { p - 1 } ( D _ { q - 1 } \cap C _ { q } ) = 0$ also. But this follows from Step 1.

Step 3: Let $U \subset \mathbb { R } ^ { n }$ be an open set. Then $H _ { p } ( U ) = 0 ~ f o r ~ p \ge n$

Let $z = \sum a _ { i } \sigma _ { i }$ be a p-cycle, and let K denote the union S im $\sigma _ { i }$ . Note that K is compact. Thus we can find $\epsilon > 0$ and a finite collection of integer cubes $C _ { j }$ such that the interiors of the small cubes $\epsilon C _ { j }$ cover K, but the union L of the $\epsilon C _ { j }$ is contained in $U .$ . Then z represents a p-cycle in L. But $H _ { p } ( L ) = 0$ by Step 2; so z is a boundary in $L ,$ and hence in $U .$

Step 4: For an n-manifold M, we have $H _ { p } ( M ) = 0$ when $p > n$

Let $z = \sum a _ { i } \sigma _ { i }$ be a p-cycle in M, and let $K = \bigcup \operatorname { i m } \sigma _ { i } . \mathrm { A g a i n }$ it is compact, and hence covered by finitely many open sets homeomorphic to $\mathbb { R } ^ { n }$ . We prove by induction on N that a p-cycle z contained in N open sets $V _ { 1 } , \dots , V _ { N }$ homeomorphic to $\mathbb { R } ^ { n }$ is a boundary in $\cup V _ { i }$ (hence in M). The case $N = 1$ was Step 3. For the induction step, assume $N > 1$ and let $U = V _ { 1 } \cup \dots \cup V _ { N - 1 }$ . Mayer–Vietoris gives an exact sequence

$$
H _ { p } ( U ) \oplus H _ { p } ( V _ { N } ) \to H _ { p } ( U \cup V _ { N } ) \to H _ { p - 1 } ( U \cap V _ { N } ) .
$$

By induction, the left term vanishes. The term on the right vanishes by Step 3. Hence the middle term also vanishes. 

14.1. Local homology. The local homology of a space M at $x \in M$ is defined as $H _ { * } ( M , M \setminus \{ x \} )$

Lemma 14.2. When M is an n-manifold, one has $H _ { * } ( M , M \setminus \{ x \} ) \cong \mathbb { Z } _ { ( n ) }$

Proof. Choose a neighbourhood D of x homeomorphic to a closed n-ball. By excision, $H _ { * } ( M , M \setminus \{ x \} ) \cong H _ { * } ( D , D \setminus \{ x \} )$ . One finds from the long exact sequence of the pair that $H _ { p } ( D , D \setminus \{ x \} ) \cong \tilde { H } _ { p - 1 } ( D - \{ x \} )$ for all $p .$ But $D \setminus \{ x \}$ deformationretracts to $S ^ { n - \bar { 1 } }$ , and $H _ { * } ( S ^ { n - 1 } ) \cong \mathbb { Z } _ { ( p - 1 ) }$ , whence the result. 

We can form a natural covering space p: $H _ { M } \ \to \ M$ whose fiber over x is $H _ { n } ( M , M \setminus \{ x \} )$ . Thus a point in $H _ { M }$ is a pair $( x , h _ { x } )$ where $x \in M$ and $h _ { x } \in$ $H _ { n } ( M , M \setminus \{ x \} )$ , and $p ( x , h _ { x } ) = x$ The topology is defined as follows. Let U be an open set in X homeomorphic to $\mathbb { R } ^ { n }$ , and let $B \subset U$ be a closed neighbourhood homeomorphic to the closed disc $D ^ { n }$ . Then one has isomorphisms

$$
H _ { n } ( M , M \setminus \{ y \} ) \left. H _ { n } ( M , M \setminus B ) \right. H _ { n } ( M , M \setminus \{ x \} ) .
$$

Define a ‘component’ of $p ^ { - 1 } ( U )$ to be an equivalence class of pairs $( x , h _ { x } ) \in p ^ { - 1 } ( U )$ , where $( x , h _ { x } )$ is equivalent to $( y , h _ { y } )$ if there is a ball B containing both x and y and an element $z \in H _ { n } ( M , M \setminus B )$ mapped by the above isomorphisms to $h _ { x }$ and $h _ { y }$ The components of $p ^ { - 1 } ( U )$ , as U varies over open neighbourhoods homeomorphic to $\mathbb { R } ^ { n }$ , form a basis for a topology making p a covering map.

## 14.2. Homology in dimension n.

Theorem 14.3. $H _ { n } ( M ) = 0$ when M is a connected but non-compact n-manifold.

We have already established a special case of this, the case where M is an open set in $\mathbb { R } ^ { n }$ . The principle of the proof is standard, but the details here are from May’s book. The proof is more technical than one would ideally like, but there is only really new idea:

An n-dimensional homology class z determines a section $s _ { z }$ of p : $H _ { M } \to M$ , and $z = 0 \ i f s _ { z } ( x ) = 0$ for some x.

Lemma 14.4. Let $U \subset \mathbb { R } ^ { n }$ be open. Then the natural homomorphism

$$
H _ { n } ( \mathbb { R } ^ { n } , U ) \to \prod _ { x \in \mathbb { R } ^ { n } \setminus U } H _ { n } ( \mathbb { R } ^ { n } , \mathbb { R } ^ { n } \setminus \{ x \} )
$$

is injective. Equivalently, the product of maps induced by inclusions,

$$
\tilde { H } _ { n - 1 } ( U ) \to \prod _ { x \in \mathbb { R } ^ { n } \setminus U } \tilde { H } _ { n - 1 } ( \mathbb { R } ^ { n } \setminus \{ x \} ) ,
$$

is injective.

The equivalence of the two assertions follows from the long exact sequences of the pairs $( \mathbb { R } ^ { n } , U )$ and $( \mathbb { R } ^ { n } , \mathbb { R } ^ { n } \backslash \{ x \} )$ . Informally, the second assertion says that any non-trivial (n − 1)-cycle in U must wrap around some point outside U. We prove the second assertion.

Proof. Suppose $s \in \tilde { H } _ { n - 1 } ( U )$ maps to zero in ${ \tilde { H } } _ { n } ( \mathbb { R } ^ { n } \backslash \{ x \} )$ for all $x \notin U$ . We will show that $s = 0$ . The notation will be rather heavy: we fix a chain of subspaces

$$
K \subset V \subset { \bar { V } } \subset U
$$

where K is compact, V open, V¯ compact, and s is the image of some $r \in \tilde { H } _ { n - 1 } ( K )$ Let T be a cube $( - d , d ) ^ { n }$ large enough that $\bar { V } \subset T$ . We discard everything outside T : we shall show that r maps to zero in ${ \tilde { H } } _ { n - 1 } ( T \cap U )$ , hence also in ${ \tilde { H } } _ { n - 1 } ( U )$ . We know that r maps to zero in ${ \tilde { H } } _ { n - 1 } ( T \backslash \{ x \} )$ for all $x \in T \setminus U$ . Our method will be to ‘eat away’ more and more of $T \backslash U .$ , showing that r maps to zero in ${ \tilde { H } } _ { n - 1 } ( T \backslash S )$ for progressively larger subsets $E \subset T \setminus U$ , starting at $E = \{ x \}$ and ending at $E = T \setminus U$ itself. Since $T \setminus \left( T \setminus U \right) = T \cap U$ , this will do the job.

Now, $T \backslash U$ is covered by a grid of small compact cubes in $\mathbb { R } ^ { n }$ , whose diameter is chosen small enough that none of them hits V . Let $C _ { 1 } , \ldots , C _ { q }$ be the intersections of these small cubes with T . We claim that r maps to zero in $\tilde { H } _ { n - 1 } ( T \backslash E _ { p } )$ for $p \leq q$ where $E _ { p } = C _ { 1 } \cup \cdots \cup C _ { p } ,$ . Indeed, the case $p = 0$ is trivial, and for $p > 0$ we have $T \backslash E _ { p } = { \dot { ( T \setminus E _ { p - 1 } ) } } \cap ( \mathbb { R } ^ { n } { \dot { \setminus } } E _ { p } )$ . On the other hand, $( T \backslash E _ { p - 1 } ) \cup ( \mathbb { R } ^ { n } \backslash E _ { p } ) = \mathbb { R } ^ { n } \backslash E _ { p }$ Mayer–Vietoris gives

$$
H _ { n } ( \mathbb { R } ^ { n } \setminus E _ { p } ) = 0 \to \tilde { H } _ { n - 1 } ( T \setminus E _ { p } ) \to \tilde { H } _ { n - 1 } ( T \setminus E _ { p - 1 } ) \oplus \tilde { H } _ { n - 1 } ( \mathbb { R } ^ { n } \setminus E _ { p } ) .
$$

Here the group on the left is zero by Step 3 in the proof of the earlier theorem. Since r maps to zero in $\tilde { H } _ { n - 1 } ( T \setminus E _ { p - 1 } ) \oplus \tilde { H } _ { n - 1 } ( \mathbb { R } ^ { n } \setminus E _ { p } )$ , it must then map to zero in $\tilde { H } _ { n - 1 } ( T \setminus E _ { p } )$ 

Proof of the theorem. Any $z \in H _ { n } ( M )$ defines a continuous section $s _ { z } \colon M \to H _ { M }$ If M is connected (hence path-connected), it follows from unique path-lifting that any continuous section is determined by its value at a point. But z is represented by a cycle that maps to a compact subset $Z \subset M$ . If M is connected but non-compact, we can choosing $x \in M \setminus Z$ . Then $s _ { z } ( x ) = 0$ , and hence $s _ { z } = 0$

Thus we take a class $z \in H _ { n } ( M )$ that maps to zero in some $H _ { n } ( M , M \setminus \{ x \} )$ We must show that $z = 0$

There is some compact set $Z \subset M$ such that z is in the image of $H _ { n } ( Z )$ ). Now, Z is contained in a finite union $U _ { 1 } \cup \cdots \cup U _ { q }$ of coordinate neighbourhoods $U _ { i } .$ and it suffices to show $[ z ] = 0$ in $H _ { n } ( U _ { 1 } \cup \cdots \cup \bar { U } _ { q } )$ We have already proved that $H _ { n } ( U _ { 1 } ) = 0$ Now take $q > 1$ , and inductively suppose that we’ve shown that $H _ { n } ( U _ { 1 } \cup \cdot \cdot \cdot \cup U _ { q - 1 } ) = 0$ . Mayer–Vietoris gives an exact sequence

$$
H _ { n } ( U ) \oplus H _ { n } ( V ) \to H _ { n } ( U _ { 1 } \cup \cdot \cdot \cdot \cup U _ { q } ) \to \tilde { H } _ { n - 1 } ( U \cap V ) \to \tilde { H } _ { n - 1 } ( U ) \oplus \tilde { H } _ { n - 1 } ( V ) ,
$$

where $V = U _ { 1 } \cup \cdots \cup U _ { q - 1 }$ and $U = U _ { q }$ . This reduces to

$$
0  H _ { n } ( U _ { 1 } \cup \cdots \cup U _ { q } )  \tilde { H } _ { n - 1 } ( U \cap V )  \tilde { H } _ { n - 1 } ( V ) ,
$$

and so the task is to show that the map $j _ { * } \colon \tilde { H } _ { n - 1 } ( U \cap V ) \to \tilde { H } _ { n - 1 } ( V )$ induced by inclusion is injective. This step is a little tricky. Take $r \in \ker j _ { * }$ . From the long exact sequence of the pair $( V , U \cap V )$ ,

$$
0 \to H _ { n } ( V , U \cap V ) \to \tilde { H } _ { n - 1 } ( U \cap V ) \to \tilde { H } _ { n - 1 } ( V ) ,
$$

we find a (unique) $t \in H _ { n } ( V , U \cap V )$ such that $\delta t = r$ . From the long exact sequence of the pair $( U , U \cap V )$

$$
0 \to H _ { n } ( U , U \cap V ) \to \tilde { H } _ { n - 1 } ( U \cap V ) \to 0 ,
$$

we find a (unique) $s \in H _ { n } ( U , U \cap V )$ with $\delta s \ = \ r$ . Now, s and t have images $s ^ { \prime }$ and t0 in a common group $H _ { n } ( U \cup V , U \cap V )$ , and $s ^ { \prime } - t ^ { \prime }$ lies in the kernel of $\delta \colon H _ { n } ( U \cup V , U \cap V ) \to \tilde { H } _ { n - 1 } ( V )$ , hence in the image of $H _ { n } ( U \cup V )$ : say $s ^ { \prime } - t ^ { \prime }$ comes from $w \in H _ { n } ( U \cup V )$ . Since $U \cup V$ is non-compact, the composite $H _ { n } ( U \cup V ) $ $H _ { n } ( M )  H _ { n } ( M , M \setminus \{ x \} )$ maps w to zero (by the argument at the beginning of this proof). Take x outside $U \cup V$ . Then we have a map $H _ { n } ( U \cup V , U \cap V ) $ $H _ { n } ( M , M \setminus \{ x \} )$ factoring $H _ { n } ( U \cup V )  H _ { n } ( M , M \setminus \{ x \} )$ which therefore carries $t ^ { \prime } - s ^ { \prime }$ to zero. Moreover, t0 maps to zero in $H _ { n } ( M , M \backslash \{ x \} )$ , because it comes from $t \in H _ { n } ( V , U \cup V )$ , and the map $H _ { n } ( V , U \cup V )  H _ { n } ( M , M \setminus \{ x \} )$ factors through $H _ { n } ( M \setminus \{ x \} , M \setminus \{ x \} ) = 0$ . Hence s0 maps to zero in $H _ { n } ( M , M \setminus \{ x \} )$ ). It follows that s maps to zero in $H _ { n } ( U , U \setminus \{ c \} ) \cong H _ { n } ( M , M \setminus \{ c \} )$ .

Since $U \cong \mathbb { R } ^ { n }$ , we have $s \in H _ { n } ( \mathbb { R } ^ { n } , \mathbb { R } ^ { n } \backslash V )$ and s maps to zero in $H _ { n } ( \mathbb { R } ^ { n } , \mathbb { R } ^ { n } \backslash \{ y \} )$ for every y lying outside V . We wish to show that s is zero (so that $r = \delta s = 0 )$ But that is what we proved in the last lemma.

Exercise 14.1: (a) Let X be a path connected space. Show how 2-sheeted covering spaces of X, up to isomorphism, correspond to homomorphisms $\pi _ { 1 } ( X , x ) \to \mathbb { Z } / 2$

(b) Let $\tilde { M } \subset H _ { M }$ be the subspace consisting of pairs $( x , h _ { x } )$ with $h _ { x }$ a generator for $H _ { n } ( M , M \setminus \{ x \} ) \cong \mathbb { Z }$ Thus $p \colon \tilde { M }  M$ is a 2-sheeted covering space. The corresponding homomorphism $\pi _ { 1 } ( M ) \to \mathbb { Z } / 2$ is called the orientation character or first Stiefel–Whitney class $w _ { 1 } ( M )$ of M . Compute it for X the Klein bottle and for $\mathbb { R } P ^ { 2 }$

## 15. Orientations and fundamental classes

15.1. Homology with coefficients. Homology with coefficients is a simple generalisation of singular homology.

Let R be a commutative unital ring. The case we have been considering up to this point is $R = \mathbb { Z } ,$ but we could also take, for example, a field such as $\mathbb { F } _ { p } = \mathbb { Z } / p$ (where p is prime) or Q.

Define a chain complex of R-modules $S _ { * } ( X ; R )$ by defining $S _ { n } ( X ; R )$ as the free R-module generated by the n-simplices in X:

$$
S _ { n } ( X ; R ) = R ^ { \Sigma _ { n } ( X ) } \cong S _ { n } ( X ) \otimes _ { \mathbb { Z } } R .
$$

Define the differential ∂ on simplices by the familiar formula, and in general by R-linearity. Let $H _ { n } ( X ; R ) = H _ { n } ( S _ { * } ( X ; R ) )$ , as an R-module.

If $A \subset X$ is a subspace then one has an injective chain map $S _ { * } ( A ; R ) \to S _ { * } ( X ; R )$ Put

$$
S _ { * } ( X , A ; R ) = S _ { * } ( X ; R ) / S _ { * } ( A ; R ) , \quad H _ { n } ( X , A ; R ) = H _ { n } ( S _ { * } ( X , A ; R ) ) .
$$

Then one has a long exact sequence of the pair. Locality, Mayer–Vietoris and excision hold just as before, as does homotopy invariance. One has $H _ { 0 } ( X ; R ) =$ $R ^ { \pi _ { 0 } ( X ) }$ . The homology of a point, $H _ { i } ( * ; R )$ , vanishes for $i > 0$ . For an n-manifold $M ,$ one has $H _ { i } ( M ; R ) = 0$ for all $i > n$ and, in the non-compact case, for $i = n$ . All these assertions follow from routine generalisations of the proofs we have given.

Slightly trickier is the assertion that, for X path connected, one has

$$
H _ { 1 } ( X ; R ) \cong \pi _ { 1 } ( X ) ^ { a b } \otimes _ { \mathbb { Z } } R .
$$

The proof we gave for the case $R = \mathbb { Z }$ uses the integer coefficients in a significant way, but the general case follows from it and the universal coefficients theorem, to be given in the next lecture. (If you have a simpler proof, tell me!)

15.2. What it’s good for. Homology with coefficients contains no more information than ordinary homology, but is useful for the following reasons.

• When R is a field, algebraic properties of homology simplify. For instance, over a field, passing to homology commutes with the tensor product and dualisation operations on chain complexes.

• For many spaces, the Z-homology is more complicated than the homology over the prime fields $\mathbb { Z } / p \mathrm { o r } \mathrm { o v e r } \mathbb { Q } .$ Moreover, considering these collectively, one does not lose information. Good examples are $\mathbb { R } P ^ { n }$ and various Lie groups, notably $S O ( n )$

• When working with manifolds, in Z-homology one must distinguish the orientable and non-orientable cases, but in Z/2-homology this is unnecessary.

15.3. The local homology cover. Recall from the last lecture that the local homology of an n-manifold (now with R-coefficients) is given by

$$
H _ { * } ( M , M \setminus \{ x \} ; R ) \cong R _ { ( n ) } .
$$

Collectively, these form a covering space $H _ { M , R } \to M$ with fibres $H _ { n } ( M , M \backslash \{ x \} ; R )$ (Here one gives $H _ { n } ( M , M \setminus \{ x \} ; R )$ the discrete topology.) The sections $\Gamma _ { M , R }$ of this covering space form an R-module. A class $z \in H _ { n } ( M ; R )$ gives classes $z _ { x } \in$ $H _ { n } ( M , M \setminus \{ x \} ; R )$ for all $x ,$ , and this determines a homomorphism $H _ { n } ( M ; R ) \to$ $\Gamma _ { M , R }$

Theorem 15.1. The the natural homomorphism $H _ { n } ( M ; R ) \to \Gamma _ { M , R }$ is injective.

Proof. We may assume M is connected. Fix $x \in M$ , and observe that by our vanishing theorem for homology of non-compact manifolds, $H _ { n } ( M \setminus \{ x \} ) = 0$ . The long exact sequence of the pair therefore reads

$$
0  H _ { n } ( M )  H _ { n } ( M , M \setminus \{ x \} ) .
$$

That is, the homomorphism $H _ { n } ( M )  H _ { n } ( M , M \backslash \{ x \} )$ is injective. Our vanishing theorem was proved for Z coefficients, but the proof applies to an arbitrary coefficient ring. Since it injects into $H _ { n } ( M , M \setminus \{ x \} )$ , a fortiori $H _ { n } ( M ; R )$ injects into $\Gamma _ { M , R }$ 

15.4. Orientations. Depending on the ground ring R, there may be more than one isomorphism of R-modules $H _ { n } ( M , M \backslash \{ x \} ; R ) \cong R \mathrm { . }$ : for instance, when $R = \mathbb { Z } .$ , there are exactly two isomorphisms (the one you first thought of, and its composition with $n \mapsto - n )$ . However, when $R = \mathbb { Z } / 2$ , there is a unique isomorphism.

Definition 15.2. An R-orientation for the n-manifold M at x is an isomorphism of R-modules

$$
\eta \colon H _ { n } ( M , M \setminus \{ x \} ; R ) \to R .
$$

If R is not specified, we understand $R = \mathbb { Z }$

Define the R-orientation cover

$$
\tilde { M } _ { R } = \{ ( x , \eta _ { x } ) : x \in M \mathrm { ~ a n d ~ } \eta \mathrm { ~ i s ~ a n ~ } R \mathrm { - o r i e n t a t i o n ~ f o r ~ } M \mathrm { ~ a t ~ } x \} ,
$$

and let $p _ { R } \colon \tilde { M } \to M$ be the projection $( x , \eta _ { x } ) \mapsto x$ . The topology is constructed in much the same way as that of $H _ { M }$ (work this through!). Notice that $\tilde { M } _ { R }$ is itself an n-manifold. When $R = \mathbb { Z }$ , it is a 2-sheeted covering of M. Assuming M is connected, $\tilde { M _ { \mathbb { Z } } }$ is either connected, hence a non-trivial covering, or disconnected, hence(!) trivial.

Definition 15.3. An R-orientation for M is a section of p, i.e., a map $s \colon M \to { \tilde { M } }$ such that $p _ { R } \circ s = \operatorname { i d } _ { M }$ . If an orientation exists, M is called R-orientable. Again, if no ring is specified we understand $R = \mathbb { Z }$

Thus an R-orientation for M is a coherent choice of orientations for all points. Observe that there is automatically a unique $\left( \mathbb { Z } / 2 \right)$ -orientation.

The orientation cover is closely related to the local homology cover $H _ { M , R } \to M$ We illustrate this with the case $R = \mathbb { Z }$ . If $a \in \mathbb { Z }$ then the subset

$$
\tilde { M } ( a ) : = \{ ( x , h _ { x } ) \in H _ { M , R } : \eta _ { x } ( h _ { x } ) = a \mathrm { ~ f o r ~ s o m e ~ o r i e n t a t i o n ~ } \eta _ { x } \}
$$

then $\tilde { M } ( a ) = \tilde { M } ( - a )$ . If $a \ne 0$ then the covering $\tilde { M } ( a )  M$ is isomorphic to $\tilde { M } _ { \mathbb { Z } } \to M$ , while if $a = 0$ it is a trivial covering $M \to M$

## 15.5. Fundamental classes.

Definition 15.4. (i) If M is an n-manifold, an R-fundamental class for M is a class $z \in H _ { n } ( M ; R )$ whose image in $H _ { n } ( M , M \setminus \{ x \} ; R )$ is a generator, for every $x \in M$

(ii) More generally, if $K \subset M$ is a subspace, an R-fundamental class for M at K is a class $z \in H _ { n } ( M , M \setminus K ; R )$ whose image in $H _ { n } ( M , M \setminus \{ x \} ; R )$ is a generator, for every $x \in K$

Theorem 15.5. An R-orientation for M determines an R-fundamental class $z _ { K }$ at K, for every compact subspace $K \subset M$ . The orientation maps $z _ { K } ( x ) \in H _ { n } ( M , M \backslash$ {x}) to $1 \in R$

Proof. We drop the coefficients from the notation. It is technically easier to prove, alongside the theorem, that $H _ { p } ( M , M \setminus K ) = 0$ for $p > n .$

Start by supposing $K \subset U$ , with $U \cong \mathbb { R } ^ { n }$ . Notice that by excision and a deformation retraction, $H _ { n } ( M , M \setminus U ) \cong H _ { n } ( \mathbb { R } ^ { n } , \mathbb { R } ^ { n } \setminus \{ 0 \} )$ . Thus an orientation determines a fundamental class for M at U, and hence at K. Also, in this case $H _ { p } ( M , M \setminus K ) = 0$ for $p > n$ by the long exact sequence of the pair and our vanishing theorem from last time.

A general compact subset $K \subset M$ , is the union of finitely many compact subsets $K _ { i } ,$ each contained in a neighbourhood $U _ { i } \cong \mathbb { R } ^ { n }$ . So, by induction, it suffices to show that if the theorem (including the statement about $p > n )$ holds for K, L and $K \cap L$ then it holds for $K \cup L$

To prove this, we need a relative form of Mayer–Vietoris. If $Y \subset X$ X, and $( Y ; A , B )$ is an excisive triad, then one has a long exact sequence

$$
\begin{array} { r } { \cdots \to H _ { p } ( X , X \setminus ( A \cup B ) ) \to H _ { p } ( X , X \setminus A ) \oplus H _ { p } ( X , X \setminus B ) \to H _ { p } ( X , A \cap B ) \to \dots . } \end{array}
$$

In our case we get

$$
H _ { n + 1 } ( M , M \setminus ( K \cap L ) ) \to H _ { n } ( M , M \setminus ( K \cup L ) ) \to H _ { n } ( M , M \setminus K ) \oplus H _ { n } ( M , M \setminus L ) .
$$

By hypothesis, the module on the left is zero, but we have fundamental classes $z _ { K } \in H _ { n } ( M , M \setminus ( K \cup L ) )$ and $z _ { L } \in H _ { n } ( M , M \setminus ( K \cup L ) )$ determined by the orientation. Their difference, in $H _ { n } ( M , M \setminus ( K \cap L )$ , is zero, and hence $z _ { K } + z _ { L }$ comes from a class $z _ { K \cup L } \in H _ { n } ( M , M \setminus ( K \cup L ) )$ which is clearly a fundamental class. 

Exercise 15.1: Use the locality theorem for chains to derive this relative Mayer–Vietoris sequence.

Corollary 15.6. If M is compact, connected and R-oriented then $H _ { n } ( M ; R ) = R$ Hence any compact, connected n-manifold M has $H _ { n } ( M ; \mathbb { Z } / 2 ) \cong \mathbb { Z } / 2$ . If it is also orientable then $H _ { n } ( M ) \cong \mathbb { Z }$

Proof. We know by the last theorem that a fundamental class exists, so the homomorphism

$$
H _ { n } ( M ; R ) \to \Gamma _ { M , R }
$$

is onto. We observed earlier that it is injective. Hence it is an isomorphism. But $\Gamma _ { M , R } \cong R$ , and an orientation specifies such an isomorphism. 

Corollary 15.7. If M is connected but not orientable then $H _ { n } ( M ) = 0$

Proof. The natural map $H _ { n } ( M ) \to \Gamma _ { M }$ is injective. If it had non-trivial image, the image would contain a section of one of the covers $\tilde { M } ( a )  M$ with $a \neq 0$ . But these covers are copies of $\tilde { M }  M$ , and so have no sections by hypothesis. 

Exercise 15.2: Convince yourself that the definition of an orientation at x is not crazy. More specifically, take $R = \mathbb { Z }$ and M to be an n-dimensional vector space V . An orientation for V in a more familiar sense would be an isomorphism $V \to \mathbb { R } ^ { n }$ , where two isomorphisms $\theta _ { 1 }$ and $\theta _ { 2 }$ are considered equivalent if det $( \theta \circ \theta _ { 2 } ^ { - 1 } ) > 0$ . Show how an orientation for the vector space V determines an orientation for V as a manifold, at any chosen point x.

Exercise 15.3: If M is given a smooth structure then it is orientable iff there is a smooth atlas whose transition functions $\tau _ { i j }$ have positive Jacobian determinants det $D _ { x } \tau _ { i j }$

Exercise 15.4: A manifold M is orientable if it is simply connected, or more generally, if $\pi _ { 1 } ( M )$ is finite and has odd order.

Exercise 15.5: If $p$ is odd then a Z/p-orientation determines, and is determined by, a Z-orientation.

Exercise 15.6: Show that if a group G acts freely on $M = S ^ { n }$ , then the orientation character $\pi _ { 1 } ( M / G ) = G \to \mathbb { Z } / 2$ of the quotient manifold is given by $G \ni g \mapsto$ $\deg ( g ) \in \{ \pm 1 \} = \mathbb { Z } / 2$ . For which n is R $P ^ { n }$ orientable?

Exercise 15.7: (i) Show that there is no homeomorphism $\mathbb { H } ^ { n } \cong \mathbb { R } ^ { n }$ , where $\mathbb { H } ^ { n } =$ $\{ ( x _ { 1 } , \ldots , x _ { n } ) \in \mathbb { R } ^ { n } : x _ { 1 } \geq 0 \}$

(ii) Let M be a space, and N the subspace of points $x \in M$ which have a neighbourhood U such that there is a homeomorphism $U \to \mathbb { H } ^ { n }$ sending x to 0. Say M is an n-manifold with boundary if M \ N is an n-manifold. In that case write ∂M for the boundary N. Check that that ∂M is an $( n - 1 )$ )-manifold.

Exercise 15.8: Suppose M is a compact, connected n-manifold with non-empty boundary ∂M . It is a fact (see Hatcher) that there is a neighbourhood U of ∂M and a homeomorphism $U \to \partial M \times [ 0 , 1 )$ sending any $x \in \partial M$ to (x, 0).

(a) Show that $H _ { p } ( M ) = 0$ for $p \geq n$ and $H _ { p } ( M , \partial M ) = 0$ for $p > n$

(b) Show that if M \ ∂M is orientable then $H _ { n } ( M , \partial M ) \cong \mathbb { Z } .$

(c) Let X be a space. Suppose $h \in H _ { n - 1 } ( X )$ is a homology class that is representable by a manifold, in that there is a compact oriented n − 1-manifold N with fundamental class $z _ { N }$ and a map $f \colon N \to X$ with $f _ { * } z _ { N } = h$ . Show that $h = 0$ if $N = \partial M$ for a compact oriented n-manifold with $\partial M = N$ such that $f$ extends to $F \colon M \to X$

Exercise 15.9: Let $h \colon S ^ { 3 } \to S ^ { 2 }$ denote the Hopf map, given by

$$
h ( z _ { 1 } , z _ { 2 } ) \mapsto z _ { 1 } / z _ { 2 } .
$$

Here we think of $S ^ { 3 }$ as the unit sphere in $\mathbb { C } ^ { 2 }$ and of $S ^ { 2 }$ as the Riemann sphere $\mathbb { C } \cup \{ \infty \}$ Let ω be a generator for $H _ { 3 } ( S ^ { 3 } ) = \mathbb { Z }$ . Then $h _ { * } \omega = 0$ , since $H _ { 3 } ( S ^ { 2 } ) = 0$ . Can you find a direct explanation for why the particular class $h _ { * } \omega$ should be zero? In other words, can you find a 4-chain bounding a 3-cycle representing $h _ { * } \omega ?$

## 16. Universal coefficients

In this lecture, we address the following question. Let $C _ { * }$ be a chain complex over R, and Q an R-module. How does one compute $H ( C _ { * } \otimes _ { R } Q )$ in terms of $H ( C _ { * } ) \ell$ We obtain a solution when R is a principal ideal domain (PID) and $C _ { * }$ is a free R-module.

16.1. Homology with coefficients. Last time, we introduced homology $H _ { * } ( X ; k )$ with coefficients in a ring k. This was defined as the homology of the complex of k-modules

$$
k ^ { \Sigma _ { * } ( X ) } = S _ { * } ( X ) \otimes _ { \mathbb { Z } } k .
$$

What is its relation to $H _ { * } ( X ) ?$ The answer is supplied by the universal coefficients theorem:

Theorem 16.1 (Universal coefficients: homology version). There are short exact sequences of k-modules,

$$
0 \to H _ { n } ( X ) \otimes k \to H _ { n } ( X ; k ) \to \operatorname { T o r } _ { \mathbb { Z } } ( H _ { n - 1 } ( X ) , k ) \to 0 ,
$$

natural in X. These sequence split, so $H _ { n } ( X ; k ) \cong H _ { n } ( X )$ ⊕ $\mathrm { T o r _ { \mathbb { Z } } } ( H _ { n - 1 } ( X ) , k )$ but the splitting cannot be chosen naturally in X.

A first task will be to explain what Tor is.

16.2. Tor. Fix a commutative ring R (for instance Z) and an R-module Q. We investigate the effect on exact sequences of the functor $\cdot \otimes Q$ from R-modules to R-modules. (Later we may suppose that Q is actually an R-algebra, and think of $\cdot \otimes Q$ as a functor from R-modules to Q-modules.)

Lemma 16.2. Let $0 \to M _ { 1 } \ { \overset { i } { \to } } \ M _ { 2 } \ { \overset { p } { \to } } \ M _ { 3 } \to 0$ be a short exact sequence of Rmodules. Let Q be another R-module. Then the induced sequence

$$
M _ { 1 } \otimes Q \to M _ { 2 } \otimes Q \to M _ { 3 } \otimes Q \to 0
$$

is also exact. If the short exact sequence splits $( f o r$ instance, $i f M _ { 3 }$ is a free module) then $M _ { 1 } \otimes Q \to M _ { 2 } \otimes Q$ is injective.

Proof. Take $m _ { 3 } \otimes q \in M _ { 3 } \otimes Q$ . Say $q = p ( m _ { 2 } )$ . Then $( p \otimes \mathrm { i d } ) ( m _ { 2 } \otimes q ) = m _ { 3 } \otimes q .$ Hence p ⊗ id is onto.

Now, $( p \otimes \mathrm { i d } ) \circ ( i \otimes \mathrm { i d } ) = ( p \circ i ) \otimes \mathrm { i d } = 0$ , and hence there is an induced map [p $\mathrm { ~ \vartheta ~ } \otimes \mathrm { i d } ] \colon ( M _ { 2 } \otimes Q ) / \mathrm { i m } ( i \otimes \mathrm { i d } ) \to M _ { 3 } \otimes Q$ Exactness of the sequence at $M _ { 2 } \otimes Q$ is equivalent to the assertion that $[ p \otimes \mathrm { i d } ]$ is injective. But im $( i \otimes \mathrm { i d } ) =$ im $i \otimes Q = \ker p \otimes Q$ , and hence we can define $s \colon \dot { M } _ { 3 } \otimes Q  ( M _ { 2 } \otimes Q ) / \mathrm { i m } ( i \otimes \mathrm { i d } )$ by $s ( m \otimes q ) = [ p ^ { - 1 } m \otimes q ]$ . We have s ◦ $[ p \otimes \mathrm { i d } ] = \mathrm { i d }$ d, so $[ p \otimes \mathrm { i d } ]$ is indeed injective.

Now suppose the sequence splits. Then there is a homomorphism $l \colon M _ { 2 } \to M _ { 2 }$ with $l \circ i = \mathrm { i d }$ . Thus l ⊗ id: $M _ { 2 } \otimes Q \longrightarrow M _ { 1 } \otimes Q$ satisfies $( l \otimes \mathrm { i d } ) \circ ( i \otimes \mathrm { i d } ) = \mathrm { i d } \otimes \mathrm { i d } .$ hence $i \otimes$ id is injective.

In general, i ⊗ id is not injective, but its kernel can be measured by the introduction of the ‘torsion products’. For simplicity, we assume R is Z, a field, or more generally a principal ideal domain (PID). A PID is a commutative ring R such that $( \mathrm { i } ) \ x y = 0$ implies $x = 0$ or $y = 0$ , and (ii) every ideal is of form $( x ) = \{ a x : a \in R \}$ The simplification in the present context because if R is a PID then every submodule of a free R-module is $f r e e ,$ i.e., has a basis. For the proof see, $\mathrm { e . g . }$ , Lang’s Algebra,

Appendix 2 (in the general case, not restricted to finite rank free modules, this uses $\mathrm { Z o r n } { \mathrm { : } } _ { \mathrm { s } }$ lemma).

This has the following consequence: any R-module M has a two-step free resolution, i.e. an exact sequence

$$
0 \to F _ { 1 } { \overset { f _ { 1 } } { \to } } F _ { 0 } { \overset { f _ { 0 } } { \to } } M \to 0
$$

with $F _ { 0 }$ and $F _ { 1 }$ free. Just take any generating set S for $M .$ , let $F _ { 0 }$ be free on $S ,$ and let $F _ { 1 }$ be the kernel of the natural map $F _ { 0 } \to M$

Applying $\cdot \otimes Q$ to this sequence, we obtain a complex

$$
0 \to F _ { 1 } \otimes Q { \overset { f _ { 1 } \otimes \mathrm { i d } } { \to } } F _ { 0 } \otimes Q { \overset { f _ { 0 } \otimes \mathrm { i d } } { \to } } M \otimes Q \to 0
$$

which is exact at $M \otimes Q$ and at $F _ { 0 } \otimes Q$ . We prefer to truncate this to the complex

$$
0 \to F _ { 1 } \otimes Q { \overset { f _ { 1 } \otimes \mathrm { i d } } { \longrightarrow } } F _ { 0 } \otimes Q \to 0 .
$$

By the lemma, its homology at $F _ { 0 } \otimes Q \ ( \mathrm { i . e . }$ , the cokernel of $f _ { 1 } \otimes \mathrm { i d } )$ is naturally isomorphic to $M \otimes Q$ . We define $\mathrm { T o r } ( M , Q )$ to be its homology at $F _ { 1 } \otimes Q$ :

$$
\operatorname { T o r } ( M , Q ) = \ker f _ { 1 } \otimes \operatorname { i d } .
$$

In brief: to define Tor, we took a free resolution of $M .$ , tensored it with $Q { \mathrm { . } }$ , and measured its failure to be exact by taking homology.

The next point is that Tor $( M , Q )$ is independent of the choice of free resolution. It is convenient to think of $0  F _ { 1 }  F _ { 0 }$ as a chain complex $F _ { * }$ , and of $f _ { 0 }$ as an ‘augmentation’ $( F _ { * } \to M )$ of the complex.

Lemma 16.3. Take two free resolutions $( F _ { * } \stackrel { f _ { 0 } } { \longrightarrow } M )$ and $( G _ { * } \stackrel { g _ { 0 } } {  } M )$ . Then there is a chain map α: $F _ { * } \to G _ { * }$ such that $g _ { 0 } \circ \alpha = f _ { 0 }$ . Moreover, α is unique up to chain homotopy.

The proof is left as an exercise.

Proposition 16.4. $\mathrm { T o r } ( M , Q )$ is independent of the choice of two-step free resolution $F _ { * } \longrightarrow M \longrightarrow 0$

Proof. In the notation of the last lemma, we have to compare the homologies of the complexes $F _ { * } \otimes Q$ and $G _ { * } \otimes Q$ . But the lemma supplies us with an augmentationpreserving chain maps $\alpha \colon F _ { * } \to G ,$ ∗ and $\beta \colon G _ { * } \to F _ { * }$ Moreover, the uniqueness clause tells us that $\beta \alpha$ is chain homotopic to the identity; likewise $\alpha \beta .$ . Thus $\alpha \otimes \mathrm { i d }$ and β ⊗ id give chain-homotopy equivalences between $F _ { * } \otimes Q$ and $G _ { * } \otimes Q$ , showing that they have canonically isomorphic homologies. 

Example 16.5. • When R is a field we may take $F _ { 0 } = M$ and $F _ { 1 } = 0$ . Thus Tor $( M , Q ) = 0$ , consistent with our first lemma.

• If M is torsion-free over the PID $R ,$ we may take $F _ { 0 } = M$ have Tor $( M , Q ) =$ 0 for any $Q$ and $F _ { 1 } = 0$ . Hence Tor $( M , Q ) = 0$ for all Q.

• The R-module $M = R / ( x )$ has the free resolution $0 \to R { \overset { x } { \to } } R \to R / ( x ) \to$ 0. Thus

$$
\operatorname { T o r } ( R / ( x ) , Q ) = \ker ( x \otimes \mathrm { i d } \colon R \otimes Q \to R \otimes Q ) = \ker ( x \colon Q \to Q ) ,
$$

i.e., $\mathrm { T o r } ( R / ( x ) , Q )$ is the x-torsion in $Q .$ . For instance, if $p$ is prime then Tor $( R / ( p ^ { n } ) , R / ( p ) ) = R / ( p )$

## 16.3. Universal coefficients.

Theorem 16.6 (Universal coefficients). Let C∗ be a chain complex of free Rmodules over a PID R. Then, for any R-module Q, one has short exact sequences

$$
0 \to H _ { p } ( C _ { * } ) \otimes Q \stackrel { j } { \to } H _ { p } ( C _ { * } \otimes Q ) \stackrel { p } { \to } \mathrm { T o r } ( H _ { p - 1 } ( C _ { * } ) , Q ) \to 0 ,
$$

where the map j is induced by the inclusion ker $d _ { p } \otimes Q \to \ker ( d _ { p } \otimes \mathrm { i d } _ { Q } )$ . These sequences are functorial in $C _ { * }$ . They always split, but not in a natural way.

Proof of universal coefficients. We let $i _ { p } \colon B _ { p } \ \to \ Z _ { p }$ be the inclusion of the $p \mathrm { - }$ boundaries into the p-cycles. From the free resolution

$$
0 \to B _ { p } { \overset { i _ { p } } { \to } } Z _ { p } \to H _ { p } ( C _ { * } ) \to 0
$$

for the homology $H _ { p } ( C _ { * } )$ , we see that

$$
\mathrm { c o k e r } ( i _ { p } \otimes \mathrm { i d } ) = H _ { p } ( C _ { * } ) \otimes Q , \quad \mathrm { k e r } ( i _ { p - 1 } \otimes \mathrm { i d } ) = \mathrm { T o r } ( H _ { p - 1 } ( C _ { * } ) , Q ) .
$$

Now consider the short exact sequence

$$
0 \to Z _ { p } \to C _ { p } { \overset { d _ { p } } { \to } } B _ { p - 1 } \to 0 .
$$

Since the terms are free modules, the sequence splits, and so the sequence

$$
0 \to Z _ { p } \otimes Q { \overset { j _ { p } \otimes \mathrm { i d } } { \to } } C _ { p } \otimes Q { \overset { d _ { p } \otimes \mathrm { i d } } { \to } } B _ { p - 1 } \otimes Q \to 0
$$

is also exact. It is, moreover, a short exact sequence of chain complexes, so it induces a long exact sequence of homology groups. With a little thought one identifies the connecting maps; the long exact sequence reads

$$
\cdots \to H _ { p + 1 } ( C _ { * } \otimes Q ) \to B _ { p } \otimes Q { \overset { i _ { p } \otimes \mathrm { i d } } { \to } } Z _ { p } \otimes Q \to H _ { p } ( C _ { * } \otimes Q ) \to \dots ,
$$

with $i _ { p } \colon B _ { p } \to Z _ { p }$ the inclusion. Its exactness tells us that there are short exact sequences

$$
0 \to \operatorname { c o k e r } ( i _ { p } \otimes \operatorname { i d } ) \to H _ { p } ( C _ { * } \otimes Q ) \to \ker ( i _ { p - 1 } \otimes \operatorname { i d } ) \to 0 ,
$$

i.e.,

$$
0 \to H _ { p } ( C _ { * } ) \otimes Q \to H _ { p } ( C _ { * } \otimes Q ) \to \operatorname { T o r } ( H _ { p - 1 } ( C _ { * } ) , Q ) \to 0 .
$$

It is left as an exercise to think through why the map on the left is j. A splitting arises from a chosen splitting of $0  Z _ { p }  C _ { p } \stackrel { d _ { p } } {  } B _ { p - 1 }  0 ;$ again, this is left as an exercise.

It is also left as an exercise to see that the whole sequence is functorial in $C _ { * }$ The non-naturality of the splittings will follow from a topological example in one of the exercises below. 

Notice that if $Q$ is a commutative R-algebra, then $H _ { p } ( C _ { * } ) \otimes Q$ and Tor $( H _ { p - 1 } ( C _ { * } ) , Q )$ are naturally Q-modules. And, rather obviously, the universal coefficients theorem is valid as a statement about $Q -$ -modules. In particular taking $R = \mathbb { Z }$ and $Q = k .$ we obtain the topological universal coefficients theorem stated at the outset.

Exercise 16.1: Compute $H _ { * } ( K )$ , where K is the Klein bottle. Now compute $H _ { * } ( K ; \mathbb { Z } / 2 ^ { n } )$ (i) by a direct argument, and (ii) using universal coefficients.

Exercise 16.2: Prove that the splittings of the universal coefficient theorem cannot be chosen naturally in X by means of the following example. Take an embedding $i \colon  { \mathbb { R } } ^ { 2 } \ \to \  { \mathbb { R } } P ^ { 2 }$ , let $D = i ( \{ z \in \mathbb { R } ^ { 2 } : | z | < 1 \} )$ , and let $q$ be the quotient map $\mathbb { R } P ^ { 2 }  \mathbb { R } P ^ { 2 } / ( \mathbb { R } P ^ { 2 } \backslash D ) \cong S ^ { 2 }$ . Show that the $k = \mathbb { Z } / 2$ universal coefficients sequences for R $P ^ { 2 }$ and $S ^ { 2 }$ cannot be split compatibly with q.

Exercise 16.3: This exercise develops an alternative approach to a special case of universal coefficients. Let $C _ { * }$ be a chain complex of free abelian groups. Show that tensoring by the short exact sequence $0 \to \mathbb { Z } \to \mathbb { Z } \to \mathbb { Z } / n \to 0$ gives rise to a short exact sequence of chain complexes $0 \to C _ { * } \to C _ { * } \to C _ { * } \otimes \mathbb { Z } / n \to 0$ . By analyzing the resulting long exact sequence of homology groups, deduce a short exact sequence

$$
0 \to H _ { p } ( C _ { * } ) \otimes _ { \mathbb { Z } } { \mathbb { Z } } / n \to H _ { p } ( C _ { * } \otimes { \mathbb { Z } } / n ) \to \{ x \in H _ { p - 1 } ( C _ { * } ) : n x = 0 \} \to 0 .
$$

## III. Cellular homology

## 17. CW complexes

We introduce a manageable category of spaces and maps, the category of CW complexes and cellular maps.

CW complexes are a particularly convenient and useful class of spaces to work with, for a number of reasons.

• There is an efficient and geometrically clear way of computing the homology groups of a CW complex.

• Maps between CW complexes behave far better than maps between general spaces: a weak homotopy equivalence between CW complexes is a homotopy equivalence. A weak equivalence $f \colon X \to Y$ is a map which induces bijections $\mathbf { h T o p } ( S ^ { n } , X ) \to \mathbf { h T o p } ( S ^ { n } , Y ) , h \mapsto f \circ h$ for all n (here $\mathbf { h } \mathbf { T o p } ( S ^ { n } , X )$ denotes the set of homotopy class of maps).

• One can localise the category hTop, artificially inverting the weak equivalences to form the topological derived category. Simplistically, performing this localisation is equivalent to working with CW complexes. The precise statement is that the topological derived category is equivalent to the homotopy category of CW spectra, see C. Weibel, Introduction to homological algebra, Chapter 10.

• On a smooth compact manifold M, a Morse function gives rise to a cell structure making M a CW complex.

Definition 17.1. The n-cell $e _ { n }$ is the closed unit disc $D ^ { n } \subset \mathbb { R } ^ { n }$ . For $n > 0 ,$ , its boundary is $\partial e _ { n } = S ^ { n - 1 }$ . We put $\partial e _ { 0 } = \emptyset$ . If A is a space, and $f \colon S ^ { n - 1 } \to A$ a map, we can build a space

$$
C f = e _ { n } \cup _ { f } A = ( A \operatorname { I I } e _ { n } ) / \sim \quad { \mathrm { w h e r e ~ } } f ( x ) \sim x { \mathrm { ~ f o r ~ } } x \in \partial e _ { n } .
$$

We say that $A \cup _ { f } e _ { n }$ results from attaching an n-cell to A via the attaching map $f .$

The notation Cf refers to the general notion of the ‘homotopy cofiber’ $C f =$ $C X \cup _ { f } Y$ of a map $f \colon X \to Y$ , where $C X = X \times I / X \times \{ 1 \}$ is the cone on X.

Example 17.2. Let $c \colon S ^ { n - 1 } \to e _ { 0 }$ be the constant map. Then $S ^ { n } \cong C c = e _ { n } \cup _ { c } e _ { 0 }$

Two crucial observations are:

• that $C f$ contains A as a closed subspace; and

• that the quotient $C f / A$ is homeomorphic to $e ^ { n } / \partial e ^ { n }$ , hence to $S ^ { n }$

More generally, given an indexing set I and a map $\begin{array} { r } { f = \coprod _ { i \in I } f _ { i } \colon \coprod _ { i \in I } \partial e _ { n } \longrightarrow A _ { : } } \end{array}$ we can build a space

$$
C f = ( A \operatorname { I I } \prod _ { i } e _ { n } ) / \sim \ \mathrm { \ w h e r e } \ f _ { i } ( x ) \sim x \ \mathrm { f o r } \ x \in \partial e _ { n } .
$$

The images of the $f _ { i }$ need not be disjoint. We say Cf is obtained by attaching n-cells to A.

Note that $C f / A \cong \vee _ { i \in I } S ^ { n }$

Definition 17.3. A cell complex of dimension $\leq d$ is a space X together with a sequence of closed subspaces

$$
\varnothing = X ^ { - 1 } \subset X ^ { 0 } \subset X ^ { 1 } \subset \cdots \subset X ^ { d } = X
$$

such that each $X ^ { k + 1 }$ is obtained from $X ^ { k }$ by attaching a (possibly empty) collection of n-cells. We call $X ^ { k }$ the k-skeleton of X. A cell complex is a space X together with a sequence of closed subspaces

$$
\varnothing = X ^ { - 1 } \subset X ^ { 0 } \subset X ^ { 1 } \subset X ^ { 2 } \subset \ldots
$$

such that $\textstyle X = \bigcup _ { k } X ^ { k }$ . A cell complex is a CW complex if X has the weak topology, ${ \mathrm { i . e . ~ } } U \subset X$ is open iff $U \cap X ^ { k }$ is open in $X ^ { k }$ for each k.

(I’m not sure how standard my usage of the term ‘cell complex’ is here. However, the term ‘CW complex’ is certainly standard.)

Mostly we shall work with cell complexes with finitely many cells, which are automatically CW complexes.

Remark. It is perhaps a pity that J. H. C. Whitehead’s term ‘CW complex’, which refers to certain technical properties, has not been replaced by something more descriptive. $^ { \circ } \mathrm { W } ^ { \prime }$ is for ‘weak topology’; $\mathbf { \nabla } ^ { \left. \mathbf { { C } } \right. }$ for ‘closure finiteness’, the property that the image of each closed cell intersects the interiors of only finitely many cells of lower dimension. In this as in other aspects of algebraic topology, there were many possible variants of the definition—the ones that we use lead to a streamlined theory, and most of the others do not, but this is far from obvious.

Example 17.4. A graph is just a CW complex of dimension $\leq 1$

Example 17.5. The ‘Hawaiian earring’, i.e. the union $\textstyle \bigcup _ { n > 1 } C _ { n }$ of circles $C _ { n }$ in $\mathbb { R } ^ { 2 }$ of radius $n ^ { - 1 }$ centered at $n ^ { - 1 }$ , is naturally a cell complex, but the topology inherited from $\mathbb { R } ^ { 2 }$ does not make it a CW complex $\left( \bigcup C _ { 2 n } \setminus \{ 0 \} \right.$ is open in the weak topology but not the subspace topology).

Example 17.6. The 2-torus $T ^ { 2 }$ has the structure of a CW complex with one 0- cell, one 1-cell (so the 1-skeleton is $S ^ { 1 } )$ and one 2-cell. The same goes for the Klein bottle $K ^ { 2 }$ . The real projective plane $\mathbb { R } P ^ { 2 }$ has the structure of a CW complex with two 0-cells, one 1-cell and one 2-cell.

Example 17.7. Complex projective space $\mathbb { C } P ^ { n } = ( \mathbb { C } ^ { n + 1 } \backslash \{ 0 \} ) / \mathbb { C } ^ { * }$ is a cell complex $e _ { 2 n } \cup e _ { 2 n - 2 } \cup \cdot \cdot \cdot \cup e _ { 0 }$ . To see this, define

$$
X ^ { 2 k } = \{ [ z _ { 0 } , \dots , z _ { n } ] \in \mathbb { C } P ^ { n } : z _ { j } = 0 { \mathrm { ~ f o r ~ a l l ~ } } j > k \} .
$$

Thus $X ^ { 0 } \subset X ^ { 2 } \subset \cdots \subset X ^ { 2 n } = \mathbb { C } P ^ { n }$ , and $X ^ { 2 k } \cong \mathbb { C } P ^ { k } . \mathrm { W e }$ will exhibit $X ^ { 2 k }$ as the 2k-skeleton of a cell decomposition. If $[ z ] \in X ^ { 2 k } \setminus X ^ { 2 ( k - 1 ) } \subset \mathbb { C } P ^ { n }$ then $z _ { k + 1 } = \dots = z _ { n } = 0$ but $z _ { k } \neq 0 .$ , so $[ z ] = [ w _ { 1 } , \dots , w _ { k - 1 } , 1 , 0 \dots , 0 ]$ for a unique $( w _ { 0 } , \dots , w _ { k - 1 } ) \in \mathbb { C } ^ { k }$ . Thus $X ^ { \overset { . } { 2 k } } \setminus X ^ { 2 ( \overset { . } { k - 1 } ) } \cong \overset { . } { \mathbb { C } } ^ { k }$ . Thus $\mathbb { C } P ^ { n }$ is a disjoint union of open cells, one of each even dimension up to 2n. To see that they are attached in the proper way, think of $e _ { 2 k }$ as $\{ w = ( w _ { 0 } , \dots , w _ { k - 1 } ) \in \mathbb { C } ^ { k } : | w | \le 1 \}$ and define i2k : $\stackrel { - } { e } _ { 2 k } \stackrel { - } {  } X ^ { 2 \bar { k } - 2 }$ as follows:

$$
i _ { k } ( w ) = ( w _ { 0 } , \ldots , w _ { k - 1 } , ( 1 - | w | ^ { 2 } ) ^ { 1 / 2 } , 0 , \ldots , 0 ) .
$$

This map extends to a homeomorphism $e ^ { 2 k } \cup _ { f _ { k } } X ^ { 2 k - 2 }  X ^ { k }$ which restricts to the inclusion on $X ^ { 2 k - 2 }$ , where $f _ { k } \colon S ^ { 2 k - 1 } \to { \ddot { X } } ^ { 2 k - 2 }$ is given by $f _ { k } ( \zeta _ { 0 } , \ldots , \zeta _ { k } ) =$ $[ \zeta _ { 0 } , \ldots , \zeta _ { k } , 0 , \ldots , 0 ]$

Example 17.8. Let C[t] be the C-vector space of polynomials in t. Denote by $\mathbb { C } P ^ { \infty }$ its projective space $( \mathbb { C } [ t ] \setminus \{ 0 \} ) / \mathbb { C } ^ { * }$ . Then $\mathbb { C } P ^ { \infty }$ is a CW complex with 2k-skeleton (and $2 k + 1 { \mathrm { - s k e l e t o n } } ) \ \mathbb { C } P ^ { k }$

17.1. Compact generation. CW complexes are examples of compactly generated spaces. A space X is compactly generated if (i) it is ‘weak Hausdorff’, meaning that any compact Hausdorff subspace is closed, and (ii) every ‘compactly closed’ subspace is closed. Here a subspace $A \subset X$ is compactly closed if $g ^ { - 1 } ( A )$ is closed in K for every compact Hausdorff space K and every map $g \colon K \to X$

There’s a functor k from weak Hausdorff spaces to compactly generated spaces (the closed sets of kX are the compactly closed sets of X). Algebraic topologists like to work in the category of compactly generated spaces because compact generation is a more intrinsic notion than that of a (space homotopy equivalent to a) CW complex, and because this category has excellent properties. The quotient of a compactly generated space by a closed equivalence relation is compactly generated. The direct limit of compactly generated spaces is compactly generated. Define a product $X \times Y$ in this category to be $k ( X \times Y )$ (k applied to the usual product); and define $Y ^ { X }$ as $k \mathrm { M a p } ( X , Y )$ where $\operatorname { M a p } ( X , Y )$ has its compact–open topology. Then the canonical bijection $\mathring { Z } ^ { X \times Y } \cong ( Z ^ { \hat { Y } } ) ^ { X }$ is a homeomorphism. For instance, a homotopy $I \times X \to Y$ is the same thing as a map $X \to Y ^ { I }$

17.2. Degree matrices. A good deal of information about how a CW complex $\textstyle X = \bigcup _ { k } X ^ { k }$ is built is encoded in its ‘degree matrices’ $D _ { n }$

Suppose that for each n, one has a labelling of the n-cells as $e _ { 1 } , \ldots , e _ { N ( n ) }$ . Define an ${ \cal N } ( n - 1 ) \times { \cal N } ( n )$ matrix $D _ { n }$ with integer entries as follows: the matrix entry $D _ { n } ^ { i j }$ is equal to the degree of the map

$$
\pi _ { j } \circ q _ { n - 1 } \circ f _ { i } \colon S ^ { n - 1 } \to S ^ { n - 1 } ,
$$

where $f _ { i } \colon S ^ { n - 1 } \to X ^ { n - 1 }$ is the attaching map for $e _ { i } ; q _ { n - 1 } \colon X ^ { n - 1 } \to X ^ { n - 1 } / X ^ { n - 2 }$ the quotient map; and $\pi _ { j } \colon X ^ { n - 1 } / X ^ { n - 2 } = \bar { \bigvee } _ { j } S ^ { n - 1 } \ \xrightarrow { \textstyle { , } } \ S ^ { n - 1 }$ the map which collapses all the spheres in the wedge except the jth.

Exercise 17.1: Compute degree matrices for the above-mentioned CW structures on $T ^ { 2 } , \mathbb { R } P ^ { 2 }$ and $K ^ { 2 }$

Remark. The degree matrix has a geometric interpretation in Morse theory. Fix a smooth Riemannian manifold $( M , g )$ . If f is a Morse function on M then the union of the unstable manifolds (with respect to $g )$ of the critical points is a subspace $M ^ { \prime }$ such that $M ^ { \prime }  M$ is a homotopy equivalence. $M ^ { \prime }$ has a canonical cell decomposition in which the p-cells are the unstable manifolds of the index $p$ critical points $c _ { p } ^ { i } .$ . If now $c _ { p - 1 } ^ { j }$ is an index $p - 1$ critical point then the matrix entry $D _ { i j } ^ { p }$ for the cell decomposition is the signed count $o f$ downward gradient flow lines from $c _ { p } ^ { i }$ to $c _ { p - 1 } ^ { j }$ . (To make this count finite and meaningful, we perturb the pair $( f , g )$ so that it satisfies the ‘Morse–Smale’ transversality condition.)

17.3. Cellular approximation. The following theorem is not especially difficult to prove, but we shall nonetheless omit the proof.

Theorem 17.9 (Cellular approximation of maps). Let $f \colon X \to Y$ be a map between CW complexes. Then $f$ is homotopic to a cellular map, i.e. a map g such that $g ( X ^ { k } ) \subset Y ^ { k }$ for all k.

The next theorem is best proved using a little homotopy theory. Again we shall omit the proof.

Theorem 17.10 (CW approximation of spaces). There is a procedure which assigns to any space X a CW complex $\Gamma ( X )$ and a weak homotopy equivalence $\Gamma X  X$

Moreover, the procedure can be made functorial, in the sense that if $f \colon X \to Y$ is a map then there is a map $\Gamma f \colon \Gamma X \to \Gamma Y$ so that the obvious square commutes up to homotopy.

This theorem has an important consequence. If one wants to prove a theorem about the homology of general spaces, it suffices to prove it for CW complexes; by cellular approximation of maps, one can also take the maps to be cellular.## 18. Cellular homology

We compute the singular homology of cell complexes in terms of the cells and the degree matrix obtained from their attaching maps.

Let X be a CW complex, and $X ^ { k }$ its k-skeleton; thus

$$
\emptyset = X ^ { - 1 } \subset X _ { 0 } \subset X _ { 1 } \subset X _ { 2 } \subset \cdots \subset \bigcup _ { k \geq 0 } X ^ { k } = X .
$$

We wish to compute $H _ { * } ( X )$ in terms of the cells and their attaching maps.

One of the convenient properties of CW complexes is that the subspace $X ^ { n - 1 }$ of $X ^ { n }$ has an open neighbourhood U which deformation-retracts to $X ^ { n - 1 }$ . Also $X ^ { n - 1 }$ is closed in $X ^ { n }$ . Hence (this was an exercise using the excision theorem), one has $H _ { * } ( X ^ { n } , X ^ { n - 1 } ) = \tilde { H } _ { * } ( X ^ { n } / X ^ { n - 1 } )$ when $X ^ { n - 1 } \neq \varnothing$

Now, the idea of our calculation is to exploit the fact that $X ^ { n } / X ^ { n - 1 }$ is a very simple space:

$$
X ^ { n } / X ^ { n - 1 } \cong \bigvee _ { n \mathrm { - c e l l s } } D ^ { n + 1 } / \partial D ^ { n + 1 } = \bigvee _ { n \mathrm { - c e l l s } } S ^ { n } .
$$

Thus $H _ { n } ( X ^ { n } , X ^ { n - 1 } ) = \mathbb { Z } ^ { \{ n - \mathrm { c e l l s } \} }$

Define $\delta _ { n + 1 }$ as the connecting homomorphism

$$
H _ { n + 1 } ( X ^ { n + 1 } , X ^ { n } ) \stackrel { \delta _ { n + 1 } } { \longrightarrow } H _ { n } ( X ^ { n } )
$$

from the exact sequence of the pair $( X ^ { n + 1 } , X ^ { n } )$ . Define $q _ { n }$ as the natural map

$$
H _ { n } ( X ^ { n } ) \stackrel { q _ { n } } { \longrightarrow } H _ { n } ( X ^ { n } , X ^ { n - 1 } ) .
$$

Theorem 18.1. Let $C _ { n } \ = \ H _ { n } ( X ^ { n } , X ^ { n - 1 } ) \ = \ \mathbb { Z } ^ { \{ n - c e l l s \} }$ . Define $d _ { n } ~ = ~ q _ { n - 1 } ~ \circ$ $\delta _ { n } \colon C _ { n } \to C _ { n - 1 }$ . Then one has $d _ { n } \circ d _ { n + 1 } \ : = \ : 0$ . The homology $H _ { n } ( C _ { * } )$ of the chain complex

$$
\cdots \to C _ { n + 1 } \stackrel { d _ { n + 1 } } { \to } C _ { n } \stackrel { d _ { n } } { \to } C _ { n - 1 } \to \ldots
$$

is canonically isomorphic to the singular homology $H _ { n } ( X )$

This theorem is very useful as a computational tool, as we will see next time. For now, we record two simple corollaries.

Corollary 18.2. If X is a d-dimensional CW complex then $H _ { n } ( X ) = 0$ for all $n > d$ . If X is a CW complex with a finite number l of n-cells then the rank of $H _ { n } ( X )$ is finite and $\leq l .$

Corollary 18.3. If X is a CW with only even-dimensional cells then $H _ { n } ( X ) =$ $\mathbb { Z } ^ { \{ n - c e l l s \} } ~ f o r$ all n. In particular, $H _ { * } ( \mathbb { C } P ^ { n } ) = \mathbb { Z } _ { ( 0 ) } \oplus \mathbb { Z } _ { ( 2 ) } \oplus \cdots \oplus \mathbb { Z } _ { ( 2 n ) }$ , where the subscripts denote degrees of the Z-summands.

Proof of the theorem. We will simplify by assuming that X is finite-dimensional, $\mathrm { i . e . }$ , that $X = X ^ { d }$ for some $d \geq 0$ . We also assume that $X \neq \emptyset$ , which forces $X ^ { 0 } \neq \varnothing$

Step 1. We have already mentioned this step. By excision (which applies because $X ^ { n - 1 }$ is a deformation retract of an open neighbourhood in $X ^ { n } )$ one has, for $n > 0$

$$
H _ { k } ( X ^ { n } , X ^ { n - 1 } ) \cong H _ { k } ( \bigvee _ { n \mathrm { - c e l l s } } S ^ { n } , * ) = \tilde { H } _ { k } ( \bigvee _ { n \mathrm { - c e l l s } } S ^ { n } ) \cong \bigoplus _ { n \mathrm { - c e l l s } } \tilde { H } _ { k } ( S ^ { n } ) .
$$

Thus one has

$$
H _ { n } ( X ^ { n } , X ^ { n - 1 } ) \cong \mathbb { Z } ^ { \{ n - \mathrm { c e l l s } \} } ,
$$

and this is valid even when $n = 0$

Step 2. From the long exact sequence of the pair $( X ^ { n } , X ^ { n - 1 } )$ , one sees that, for $k > n \geq 0 , H _ { k } ( X ^ { n } ) = H _ { k } ( X ^ { n - 1 } )$ , and thus iteratively $H _ { k } ( X ^ { n } ) = H _ { k } ( X ^ { 0 } ) = 0$ . So, when $X = X ^ { d } , X$ has homology only up to dimension d.

Step 3. From the long exact sequence of the pair $( X ^ { n + 1 } , X ^ { n } )$ , one sees that, for $k < n + 1 , H _ { k } ( X ^ { n } ) = H _ { k } ( X ^ { n + 1 } )$ . Thus, iteratively, $H _ { k } ( X ^ { n } ) = H _ { k } ( X ^ { n + p } ) = H _ { k } ( X )$ since $X ^ { n + p } = X$ for all $n + p \geq d .$ So to compute nth homology we can get away with considering the n + 1-skeleton of X:

$$
H _ { n } ( X ) = H _ { n } ( X ^ { n + 1 } )
$$

Step 4. Part of the long exact sequence of the pair $( X ^ { n + 1 } , X ^ { n } )$ reads

$$
H _ { n + 1 } ( X ^ { n + 1 } , X ^ { n } ) \stackrel { \delta _ { n + 1 } } {  } H _ { n } ( X ^ { n } )  H _ { n } ( X ^ { n + 1 } )  0 .
$$

Thus $H _ { n } ( X ) = H _ { n } ( X ^ { n + 1 } )$ is isomorphic to coker $\delta _ { n + 1 }$ . This represents progress, since the domain of $\delta _ { n + 1 }$ is a known group $\mathbb { Z } ^ { \{ ( n + 1 ) - \mathrm { c e l l s } \} }$

Step 5. The target of $\delta _ { n + 1 } , H _ { n } ( X ^ { n } )$ , sits in another exact sequence

$$
0 \to H _ { n } ( X ^ { n } ) { \overset { q _ { n } } { \to } } H _ { n } ( X ^ { n } , X ^ { n - 1 } ) \to H _ { n - 1 } ( X ^ { n - 1 } )
$$

(the zero on the left comes from Step 3). ${ \mathrm { S o } } ,$ crucially, the map $q _ { n }$ is injective. Let $d _ { n + 1 } = q _ { n } \circ \delta _ { n + 1 }$ . Here’s the tricky step: one has

$$
H _ { n } ( X ) \cong H _ { n } ( X ^ { n } ) / \operatorname { i m } \delta _ { n + 1 } \cong \operatorname { i m } q _ { n } / \operatorname { i m } d _ { n + 1 } ,
$$

since $q _ { n }$ carries $H _ { n } ( X ^ { n } )$ isomorphically to im $q _ { n }$ and im $\delta _ { n + 1 }$ isomorphically to im $d _ { n + 1 } .$

Step 6. One has

$$
\begin{array} { r l } & { \mathrm { i m } q _ { n } = \ker \left( \delta _ { n } \colon H _ { n } ( X ^ { n } , X ^ { n - 1 } ) \to H _ { n - 1 } ( X ^ { n - 1 } ) \right) } \\ & { \qquad = \ker \left( d _ { n - 1 } \colon H _ { n } ( X ^ { n } , X ^ { n - 1 } ) \to H _ { n } ( X ^ { n - 1 } , X ^ { n - 2 } ) \right) . } \end{array}
$$

Thus

$$
H _ { n } ( X ) \cong H _ { n } ( X ^ { n } ) / \operatorname * { i m } \delta \cong \ker d _ { n } / \operatorname * { i m } d _ { n + 1 } .
$$

Note that $d _ { n } \circ d _ { n + 1 } = 0$ because $\delta _ { n } \circ q _ { n } = 0$

Remark. Let us make a note of what we have used in the proof. We needed excision and the long exact sequence of the pair. We also needed the fact that the reduced homology of a wedge is the direct sum of the reduced homologies. We needed to know that $\tilde { H } _ { * } ( S ^ { n } ) \ : = \ : \mathbb { Z } _ { ( n ) }$ Recall that this was proved using excision (and homotopy invariance of singular homology) by an inductive argument beginning with $\tilde { H } _ { k } ( S ^ { 0 } ) = \mathbb { Z }$

We have $C _ { n } = \mathbb { Z } ^ { \{ n - \mathrm { c e l l s } \} }$ and $C _ { n - 1 } = \mathbb { Z } ^ { \{ ( n - 1 ) - \mathrm { c e l l s } \} }$ , so $d _ { n }$ is represented by an integer-valued matrix $( D _ { n } ^ { i j } )$ :

$$
D _ { n } \langle i \rangle = \sum _ { j } D _ { n } ^ { i j } \langle j \rangle ,
$$

where hii represents an n-cell and the sum is over $( n - 1 ) – \mathrm { c e l l s \ } j$

Theorem 18.4. For any $n > 1$ , the matrix $D _ { n }$ representing the differential $d _ { n }$ is equal to the degree matrix for the cellular attachments. The differential $d _ { 1 }$ is characterized by $d \langle i \rangle = \langle f _ { i } ( 1 ) \rangle - \langle f _ { i } ( 0 ) \rangle$ .

Proof. We can think of the closure of the cell $e _ { k }$ as an k-simplex (since it is homeomorphic to $\Delta ^ { k }$ . Thus the ith Z-summand in $H _ { n } ( X ^ { n } , X ^ { n - 1 } )$ is represented by the cell $e _ { n } ^ { i } ,$ considered as a singular chain (notice that it is a relative n-cycle, since its boundary lies in $X ^ { n } )$

Under $\delta _ { n } .$ , the singular chain $e _ { n } ^ { i }$ is mapped to its boundary, which is the image of the fundamental class $[ S ^ { n } ] \in H _ { n } ( S ^ { n } )$ under the cellular attaching map $f _ { i } { \mathrm { : } }$ that is, $\delta _ { n } e _ { n } ^ { i } = ( f _ { i } ) _ { * } [ S ^ { n - 1 } ]$ . Next we have to apply the quotient map $q _ { n } \colon X ^ { n - 1 } \ \to$ $X ^ { n - 1 } / X ^ { n - 2 }$ , since $d _ { n } ( e _ { n } ^ { i } ) = ( q _ { n - 1 } ) _ { * } ( f _ { i } ) _ { * } [ S ^ { n - 1 } ] \in H _ { n } ( X ^ { n - 1 } / X ^ { n - 2 } )$

The projection $H _ { n } ( X ^ { n - 1 } / X ^ { n - 2 } ) \to \mathbb { Z }$ to the jth Z-summand is induced by the collapsing map

$$
\pi _ { j } \colon X ^ { n - 1 } / X ^ { n - 2 } = \bigvee _ { ( n - 1 ) - \mathrm { c e l l s } } S ^ { n - 1 } \to S ^ { n - 1 }
$$

which acts as the identity on jth copy of $S ^ { n - 1 }$ and sends everything else to the wedge point. Thus the jth component of $\delta _ { n } e _ { n } ^ { i }$ is

$$
( \pi _ { j } ) _ { * } ( q _ { n - 1 } ) _ { * } ( f _ { i } ) _ { * } [ S ^ { n - 1 } ] = ( \pi _ { j } \circ q _ { n - 1 } \circ f _ { i } ) _ { * } [ S ^ { n - 1 } ] \in H _ { n - 1 } ( S ^ { n - 1 } ) .
$$

But this is exactly the definition of the degree matrix $D _ { n }$

## 19. Cellular homology calculations

We compute some examples of cellular homology, and observe the uniqueness of homology theories.

We begin by repeating the theorem from last time:

Theorem 19.1. If X is a CW complex then the homology of the cellular complex $( C _ { * } , d )$ is canonically isomorphic to $H _ { * } ( X )$ . Here $C _ { n } \ = \ \mathbb { Z } ^ { \{ n \} }$ n-cells} and $C _ { n - 1 } =$ $\dot { \mathbb Z } ^ { \{ ( n - 1 ) - c e l l s \} }$ , so the cellular differential $d _ { n }$ is represented by an integer-valued matrix $( D _ { n } ^ { i j } )$

$$
D _ { n } \langle i \rangle = \sum _ { j } D _ { n } ^ { i j } \langle j \rangle ,
$$

where hii represents an n-cell and the sum is over $( n - 1 ) – c e l l s \ j$

When $n > 1$ , the matrix entry $D _ { n } ^ { i j }$ is the degree of $\pi _ { j } \circ Q _ { n - 1 } \circ f _ { i } \colon S ^ { n - 1 } \ \longrightarrow$ $S ^ { n - 1 }$ , where $f _ { i }$ is the attaching map of the ith n-cell, $Q _ { n } \colon { \dot { X } } ^ { n - 1 } \to X ^ { n - 1 } / X ^ { n - 2 } =$ $\mathsf { V } _ { ( n - 1 ) - \mathrm { c e l l s } } S ^ { n - 1 }$ the quotient map, and $\pi _ { j } \colon X ^ { n - 1 } / X ^ { n - 2 } \to S ^ { n - 1 }$ the collapsing map on the $j t h$ wedge-summand. The differential $d _ { 1 }$ is characterized by $d _ { 1 } \langle i \rangle =$ $\left. f _ { i } ( 1 ) \right. - \left. f _ { i } ( 0 ) \right.$

19.1. Calculations. Let us use this theorem to compute the homology of $T ^ { 2 } , \mathbb { R } P ^ { 2 }$ and $K ^ { 2 }$ . The homology vanishes in degrees $> 2$ , because these are 2-dimensional cell complexes, but the interesting thing is to compute $H _ { 1 }$ and $H _ { 2 }$

• $X = T ^ { 2 }$ has an obvious cell decomposition with one 0-cell, two 1-cells and one 2-cell. These cells give bases $v _ { 0 }$ for $C _ { 0 } , ( v _ { 1 } ^ { a } , v _ { 1 } ^ { b } )$ for $C _ { 1 }$ , and $v _ { 2 }$ for $C _ { 2 }$ One has $d _ { 1 } v _ { 1 } ^ { a } = v _ { 0 } - v _ { 0 } = 0 = d _ { 1 } v _ { 1 } ^ { b }$ . The attaching map for the 2-cell is a map $S ^ { 1 } \to S _ { a } ^ { 1 } \lor S _ { b } ^ { 1 }$ . For $T ^ { 2 }$ it is $a b a ^ { - 1 } b ^ { - 1 }$ , so after collapsing $S _ { b } ^ { 1 }$ we get a map homotopic to $a \cdot a ^ { - 1 } \colon S ^ { 1 } \to S _ { a } ^ { 1 }$ (which has degree 0), and after collapsing $S _ { b } ^ { 1 }$ we get a map homotopic to $\widehat { b } \cdot \widehat { b } ^ { - 1 } \colon S ^ { 1 } \to S _ { b } ^ { \bar { 1 } }$ (alslo degree 0). Hence $d _ { 2 } v _ { 2 } = 0$ . So $H _ { 2 } ( T ^ { 2 } ) = \mathbb { Z }$ and $H _ { 1 } ( T ^ { 2 } ) = \mathbb { Z } ^ { 2 }$

$X = K ^ { 2 }$ has a cell decomposition with $\dot { X } ^ { 0 } = e _ { 0 } , X ^ { 1 } = e _ { 1 } ^ { a } \cup e _ { 1 } ^ { b } \cup X ^ { 0 }$ , and $X = X ^ { 2 } = e ^ { 2 } \cup X ^ { 1 }$ . These cells give bases $v _ { 0 }$ for $C _ { 0 } , ( v _ { 1 } ^ { a } , v _ { 1 } ^ { b } )$ for $C _ { 1 }$ , and $v _ { 2 }$ for $C _ { 2 }$ . As for $T ^ { 2 }$ , one has $d _ { 1 } = 0$ . The attaching map for $e _ { 2 }$ is $a b a ^ { - 1 } b$ 7 so $d _ { 2 } v _ { 2 } = 2 v _ { 1 } ^ { b }$ . Hence $H _ { 2 } ( K ^ { 2 } ) = 0$ and $H _ { 1 } ( K ^ { 2 } ) = \mathbb { Z } \oplus ( \mathbb { Z } / 2 )$

$X = \mathbb { R } P ^ { 2 }$ has a cell decomposition with two 0-cells, two 1-cells, and one 2-cell. These cells give bases $( v _ { 0 } , v _ { 0 } ^ { \prime } )$ for $C _ { 0 } , ( v _ { 1 } ^ { a } , v _ { 1 } ^ { b } )$ for $C _ { 1 } .$ and $v _ { 2 }$ for $C _ { 2 }$ Our conventions are such that $d _ { 1 } ( v _ { 1 } ^ { a } ) = v _ { 0 } ^ { \prime } - v _ { 0 } = - d _ { 1 } ( v _ { 1 } ^ { b } )$ ; thus ker $d _ { 1 } =$ $\mathbb { Z } ( v _ { 1 } ^ { a } + v _ { 1 } ^ { b } )$ . The attaching map for $e _ { 2 }$ is then abab, so $d _ { 2 } v _ { 2 } = 2 v _ { 1 } ^ { a } + 2 v _ { 1 } ^ { b }$ Hence $H _ { 2 } ( K ^ { 2 } ) = 0$ and $H _ { 1 } ( K ^ { 2 } ) = \mathbb { Z } / 2$

Happily, these calculations are consistent with our earlier results concerning $\pi _ { 1 }$

Example 19.2. Real projective space R $P ^ { n } = ( \mathbb { R } ^ { n + 1 } \backslash \{ 0 \} ) / \mathbb { R } ^ { * }$ is a cell complex with one k-cell of each dimension $k \in \{ 0 , 1 , \ldots , n \}$ . To see this, define

$$
X ^ { k } = \{ [ x _ { 0 } : \dots : x _ { n } ] \in \mathbb { R } P ^ { n } : x _ { j } = 0 { \mathrm { ~ f o r ~ a l l ~ } } j > k \} .
$$

Thus $X ^ { 0 } \subset X ^ { 1 } \subset \cdots \subset X ^ { n } = \mathbb { R } P ^ { n }$ , and $X ^ { k } \cong \mathbb { R } P ^ { k }$ . We will exhibit $X ^ { k }$ as the $k -$ skeleton of a cell decomposition. If $\operatorname { \dot { \operatorname { x } } } 1 \in X ^ { k } \setminus X ^ { k - 1 } \subset \mathbb { R } P ^ { n }$ then $x _ { k + 1 } = \cdot \cdot \cdot = x _ { n } =$ 0 but $x _ { k } \neq 0 , \operatorname { s o } \left[ x \right] = \left[ y _ { 0 } : \ldots , y _ { k - 1 } : 1 : 0 \cdots : 0 \right]$ for a unique $( y _ { 0 } , \dotsc , y _ { k - 1 } ) \in \mathbb { R } ^ { k }$ Thus $X ^ { k } \setminus X ^ { k - 1 } \cong \mathbb { R } ^ { \bar { k } }$ . Thus $\mathbb { R } P ^ { n }$ is a disjoint union of open cells, one of each dimension up to n. To see that they are attached in the proper way, think of $e _ { k }$ as $\{ y = ( y _ { 0 } , \cdot \cdot \cdot : y _ { k - 1 } ) \in \mathbb { R } ^ { k } : | y | \leq 1 \}$ and define $i _ { k } \colon e _ { k } \to X ^ { k }$ as follows:

$$
i _ { k } ( y ) = ( y _ { 0 } : \cdot \cdot \cdot : y _ { k - 1 } : ( 1 - | y | ^ { 2 } ) ^ { 1 / 2 } : 0 : \cdot \cdot \cdot : : 0 ) .
$$

Then $i _ { k }$ is injective on the interior of $e _ { k }$ , but restricts to $\partial e _ { k } = S ^ { k - 1 }$ as the map $f _ { k } ( \zeta _ { 0 } , \dots , \zeta _ { k - 1 } ) = [ \zeta _ { 0 } : \dots , \zeta _ { k - 1 } : 0 : \dots : 0 ]$ which is the quotient map $S ^ { k - 1 } $ $X ^ { k - 1 } = \mathbb { R } P ^ { k - 1 }$ . Notice that $i _ { k }$ extends to a homeomorphism $e ^ { k } \cup _ { f _ { k } } X ^ { \hat { k } - 1 }  X ^ { k }$ which restricts to the inclusion on $X ^ { k - 1 }$

To compute the cellular chain complex, we need to look at the composite $Q _ { k - 1 } \circ$ $f _ { k } ,$ where $\mathrm { \large { ~ \cal { Q } } } _ { k - 1 } \colon X ^ { k - 1 } \to X ^ { k - 1 } / X ^ { k - 2 } = S ^ { k - 1 }$ is the collapsing map. Well, when $| y | = 1$ , we have $f _ { k } ( y _ { 0 } , \dots , y _ { k - 1 } ) = [ y _ { 0 } : \dots : y _ { k - 1 } : 0 : \dots 0 ]$ . Thus ${ \bf { \bar { \it f } } } _ { k } ( y ) \in X ^ { k - 2 }$ precisely when $y _ { k - 1 } = 0 . { \mathrm { ~ C u t ~ } } S ^ { k - 1 }$ into two hemispheres $D _ { \pm } ^ { k - 1 } = \{ ( y _ { 0 } , \dots , y _ { k - 1 } )$ $| y | = 1 , \pm y _ { k - 1 } \geq 0 \}$ . Then, if $y \in \mathrm { i n t } ( D _ { + } ^ { k - 1 } )$ , we have

$$
\begin{array} { l } { { i _ { k - 1 } ^ { - 1 } \circ f _ { k } ( y ) = i _ { k - 1 } ^ { - 1 } \circ i _ { k } ( y ) } } \\ { { \qquad = i _ { k - 1 } ^ { - 1 } ( y _ { 0 } : \cdot \cdot \cdot : y _ { k - 1 } : 0 : \cdot \cdot \cdot : : 0 ) } } \\ { { \qquad = ( y _ { 0 } , \ldots \cdot \cdot , y _ { k - 2 } ) } } \end{array}
$$

(check the last line for yourself!). If $y \in \mathrm { i n t } ( D _ { + } ^ { k - 1 } )$ , then we have instead

$$
i _ { k - 1 } ^ { - 1 } \circ f _ { k } ( y ) = ( - y _ { 0 } , \ldots , - y _ { k - 2 } ) .
$$

We now see that the cellular differential $d _ { k }$ is given by $d _ { k } \langle e _ { k } \rangle \to \lambda \langle e _ { k - 1 } \rangle$ , where λ is the degree of the composite map

$$
S ^ { k - 1 } { \overset { p } { \to } } S ^ { k - 1 } \vee S ^ { k - 1 } { \overset { \mathrm { i d } \vee a } { \longrightarrow } } S ^ { k - 1 } .
$$

Here $p$ is the ‘pinching map’ that collapses the equator to the wedge point. The second map acts as the identity on the first wedge summand $S _ { + } ^ { k - 1 }$ and as the antipodal map a on the second wedge summand $S _ { - } ^ { k - \bar { 1 } }$ . Now, on fundamental classes we have $p _ { * } [ S ^ { k - 1 } ] = [ S ^ { k - 1 } ] _ { + } + [ S ^ { k - 1 } ] _ { - }$ , whilst $( \mathrm { i d } \lor a )$ ∗ maps $[ S ^ { k - 1 } ] + + [ S ^ { k - 1 } ] .$ − to $( 1 + \mathrm { d e g } ( a ) ) [ S ^ { k - 1 } ] \stackrel {  } { = } ( 1 + \bar { ( - 1 ) ) } [ S ^ { k - 1 } ]$ . Thus $\lambda = 1 + ( - 1 ) ^ { k }$

Hence the cellular complex reads

$$
\cdot \cdot \cdot \longrightarrow \mathbb { Z } \stackrel { 0 } { \to } \mathbb { Z } \stackrel { 2 } { \to } \mathbb { Z } \stackrel { 0 } { \to } \mathbb { Z } \longrightarrow 0 .
$$

So we find the following: if n is even then

$$
H _ { k } ( \mathbb { R } P ^ { n } ) = { \left\{ \begin{array} { l l } { \mathbb { Z } , } & { k = 0 , } \\ { \mathbb { Z } / 2 , } & { k < n { \mathrm { ~ o d d } } } \\ { 0 , } & { k < n { \mathrm { ~ e v e n } } } \\ { 0 , } & { p \geq n . } \end{array} \right. }
$$

If n is odd then

$$
H _ { k } ( \mathbb { R } P ^ { n } ) = { \left\{ \begin{array} { l l } { \mathbb { Z } , \ } & { k = 0 , } \\ { \mathbb { Z } / 2 , } & { k < n { \mathrm { ~ o d d } } } \\ { 0 , } & { k < n { \mathrm { ~ e v e n } } } \\ { \mathbb { Z } , \ } & { k = n , } \\ { 0 , } & { p > n . } \end{array} \right. }
$$

Taking the last example further, let’s now calculate $H _ { * } ( \mathbb { R } P ^ { n } ; \mathbb { Z } / 2 )$ . We can do this in two ways. One way is to use the cellular chain complex reduced mod $2 ,$ which reads

$$
0 \to \mathbb { Z } / 2 \to \mathbb { Z } / 2 \to \cdots \to \mathbb { Z } / 2 \to 0
$$

with $\mathrm { ~ a ~ } \mathbb { Z } / 2$ in each degree between 0 and n. The maps are all zero. Hence $H _ { i } ( \mathbb { R } P ^ { n } ; \mathbb { Z } / 2 ) = \mathbb { Z } / 2 { \mathrm { ~ i f ~ } } 0 \leq i \leq n ,$ , and it is zero otherwise.

The other method is to use our calculation for Z-coefficients in conjunction with universal coefficients. For n even, say, the Z/2-module $H _ { k } ( \mathbb { R } P ^ { n } ) \otimes _ { \mathbb { Z } / 2 }$ is $\mathbb { Z } / 2$ for $k = 0 \mathrm { ~ o r ~ } 0 < k < n$ odd, and 0 otherwise. However, $\operatorname { T o r } ( H _ { k - 1 } ( \mathbb { R } P ^ { n } ) , \mathbb { Z } / 2 )$ is $\mathbb { Z } / 2$ if $k - 1 > 0$ with k even, and is zero otherwise. Thus for any k between 0 and $n ,$ the flanking terms in the universal coefficients exact sequence

$$
0 \to H _ { k } ( \mathbb { R } P ^ { n } ; \mathbb { Z } ) \otimes _ { \mathbb { Z } } \mathbb { Z } / 2 \to H _ { k } ( \mathbb { R } P ^ { n } ; \mathbb { Z } / 2 ) \to \operatorname { T o r } ( H _ { k - 1 } ( \mathbb { R } P ^ { n } ) , \mathbb { Z } / 2 ) \to 0
$$

always consist of $\mathbb { Z } / 2$ and 0 (in some order), hence $H _ { k } ( \mathbb { R } P ^ { n } ; \mathbb { Z } / 2 ) = \mathbb { Z } / 2$

Exercise 19.1: Compute $H _ { * } ( \mathbb { R } P ^ { n } ; \mathbb { Z } / 4 )$ . Do it in two ways: via the $\mathbb { Z } / 4$ cellular chain complex; and via the homology over Z and universal coefficients.

Exercise 19.2: Use cellular homology to compute $H _ { * } ( \Sigma _ { g } )$ , where $\Sigma _ { g }$ is a standard closed, orientable surface of genus g (defined, for instance, as a quotient of the $4 g -$ gon). Also, compute $H _ { * } ( \Sigma _ { g } \# \mathbb { R } P ^ { 2 } )$ , the connected sum of $\Sigma _ { g }$ and $\mathbb { R } P ^ { 2 }$ .

Exercise 19.3: Describe how the product $X \times Y$ of finite CW complexes X and Y inherits a structure of CW complex.

(1) Compute the Euler characteristic $\chi ( X \times Y )$ in terms of $\chi ( X )$ and $\chi ( Y )$

(2) Show that $C _ { * } ^ { c e l l } ( X \times Y ) = C _ { * } ^ { c e l l } ( X ) \otimes C _ { * } ^ { c e l l } ( Y )$ as a graded abelian group. (You are not asked to compute the differential.)

(3) Compute $H _ { * } ( S ^ { n } \times S ^ { n } )$

(4) Let $X = ( S ^ { 3 } ) ^ { \times n } = S ^ { 3 } \times \cdot \cdot \times S ^ { 3 }$ . Show that $H _ { 3 p } ( X )$ is isomorphic to the exterior power $\Lambda ^ { p } \mathbb { Z } ^ { n }$ , and that $H _ { q } ( X ) = 0 { \mathrm { ~ i f ~ } } q$ is not a multiple of 3.

## 20. The Eilenberg–Steenrod axioms

We show that the Eilenberg–Steenrod axioms uniquely characterize a homology theory for CW pairs.

A CW pair $( X , A )$ is a CW complex X and a subspace A which is a subcomplex, i.e. it is a union of cells of X which form a CW complex.

Definition 20.1. An Eilenberg–Steenrod homology theory E∗ on CW pairs assigns:

• To each CW pair $( X , A )$ , and each integer n, an abelian group $E _ { n } ( X , A )$ (and we write $E _ { n } ( X )$ for $E _ { n } ( X , \varnothing ) )$

• To each map $f \colon ( X , A ) \to ( X ^ { \prime } , A ^ { \prime } )$ and each $n \in \mathbb { Z }$ it assigns a homomorphism $E _ { n } ( f ) \colon E _ { n } ( X , A ) \to H _ { n } ( X ^ { \prime } , A ^ { \prime } )$ . One has $E _ { n } ( f \circ g ) = E _ { n } ( f ) \circ E _ { n } ( g )$ and $E _ { n } { \left( \mathrm { i d } _ { \left( X , A \right) } \right) } = \mathrm { i d } _ { E _ { n } \left( X , A \right) }$ . If f0 is homotopic to $f _ { 1 }$ via a homotopy $\{ f _ { t } \}$ such that $f _ { t } | _ { A } = f _ { 0 } | _ { A } ,$ then $E _ { n } ( f _ { 1 } ) = E _ { n } ( f _ { 0 } )$ .

• To each pair of spaces $( X , A )$ , and each integer n, it assigns a homomorphism

$$
\delta _ { n } \colon E _ { n } ( X , A ) \to E _ { n - 1 } ( A ) .
$$

These maps are natural transformations. That is, given $f \colon ( X , A ) \ $ $( X ^ { \prime } , A ^ { \prime } )$ , one has

$$
\delta _ { n } \circ E _ { n } ( f ) = E _ { n - 1 } ( f ) \circ \delta _ { n }
$$

as homomorphisms $E _ { n } ( X , A ) \to E _ { n - 1 } ( A ^ { \prime } )$

Besides these basic properties, the following axioms are required to hold:

• DIMENSION: If ∗ denotes a 1-point space then $E _ { n } ( * ) = 0$ for $n \neq 0$ , while $E _ { 0 } ( * ) = \mathbb { Z }$

• EXACTNESS: The sequence

$$
\cdots \to E _ { n } ( A ) \to E _ { n } ( X ) \to E _ { n } ( X , A ) { \overset { \delta _ { n } } { \to } } E _ { n - 1 } ( A ) \to H _ { n - 1 } ( A ) \to \dots .
$$

is exact, where the unlabelled maps are induced by the inclusions $( A , \varnothing ) \to$ $( X , \varnothing )$ and $( X , \emptyset ) \to ( X , A )$

• EXCISION: if $( X ; A , B )$ is an excisive triad then the map

$$
E _ { n } ( A , A \cap B ) \to E _ { n } ( X , B )
$$

induced by the inclusion $( A , A \cap B ) \to ( X , B )$ is an isomorphism.

• ADDITIVITY: $\operatorname { I f } \left( X _ { \alpha } , A _ { \alpha } \right)$ is a family of pairs, then one has an isomorphism

$$
\bigoplus _ { \alpha } E _ { n } ( X _ { \alpha } , A _ { \alpha } ) \to E _ { n } ( \prod _ { \alpha } X _ { \alpha } , \prod _ { \alpha } A _ { \alpha } )
$$

$\mathrm { \ g i v e n }$ by the sum of the maps induced by the inclusions into the disjoint union.

Theorem 20.2 (Eilenberg–Steenrod). Take any homology theory $E _ { * }$ on CW pairs. Then for any CW complex X, one has $E _ { n } ( X , A ) \cong H _ { n } ( X , A )$ . In fact, there is a unique natural transformation $E _ { * } \to H _ { * }$ extending a given isomorphism $E _ { * } ( * ) \to$ $H _ { * } ( * )$ , and this natural transformation is a natural isomorphism.

Remark. The Eilenberg–Steenrod theorem is one of two general organising principles for (co)homology theories. The other is sheaf cohomology: the idea that one can use different resolutions of the same sheaf to compute its cohomology. This leads to a proof that singular cohomology is isomorphic to Cech cohomology, and ˇ that the real cohomology $H ^ { * } ( M ; \mathbb { R } )$ of a smooth manifold is isomorphic to its de Rham cohomology $H _ { d R } ^ { * } ( M )$

We will not give a complete proof of the theorem: for a start, we will restrict our attention, for simplicity’s sake, to finite-dimensional CW complexes. We will prove the existence of the natural isomorphism, but not its uniqueness. We will also not prove that the natural transformations $\delta _ { n }$ are uniquely determined.

Proof. We have already proved the heart of this theorem in showing that $H _ { * } ( X ) \cong$ $H _ { * } ^ { c e l l } ( X )$ , for our proof only used properties of singular homology derivable from the axioms.

To flesh this out, it is more convenient to work with reduced homology theories. Let’s put $\tilde { E } _ { n } ( X ) = E _ { n } ( X , \{ b \} )$ , where the basepoint $b \in X$ is one of the 0-simplices. Then ${ \tilde { E } } _ { n }$ defines a ‘reduced homology theory’ on based CW complexes, satisfying analogues of the axioms above. To state them, we need the notion of the reduced suspension ΣX of X: $\Sigma X = ( X \times [ - 1 , 1 ] ) / \sim _ { ! }$ , where $( x , 1 ) \sim ( y , 1 ) , ( x , - 1 ) \sim ( y , - 1 )$ and (unlike the unreduced suspension) $( b , s ) \sim ( b , t )$ , where b is the basepoint. It is made a CW complex by thinking of it as the ‘smash product’

$$
S ^ { 1 } \wedge X = ( S ^ { 1 } \times X ) / ( S ^ { 1 } \vee X )
$$

(think this through). In general, the reduced suspension differs from the unreduced suspension. However, one still has $\Sigma S ^ { n } \cong S ^ { n + 1 }$ . A map $f \colon X \to Y$ preserving basepoints induces $\Sigma f \colon \Sigma X \to \Sigma Y$ in a functorial manner.

The new axioms are as follows.

• DIMENSION: $\tilde { E } _ { * } ( S ^ { 0 } ) = \mathbb { Z }$

• EXACTNESS: if A is a CW subcomplex containing b then the sequence

$$
\tilde { E } _ { * } ( A ) \to \tilde { E } _ { * } ( X ) \to \tilde { E } _ { * } ( X / A )
$$

is exact.

• SUSPENSION: There is a natural (in X) isomorphism

$$
\Sigma \colon \tilde { E } _ { * } ( X ) \to \tilde { E } _ { * + 1 } ( \Sigma X ) .
$$

• ADDITIVITY: The natural map $\oplus _ { i } \tilde { E } _ { * } ( X _ { i } ) \to \tilde { E } _ { * } ( \vee _ { i } X _ { i } )$ is an isomorphism. Here the $X _ { i }$ are based CW complexes, and $\vee _ { i } X _ { i }$ their wedge sum along the basepoints.

Exercise 20.1: Show that if E∗ is a homology theory then $\tilde { E } _ { * }$ is a reduced homology theory.

Let $C _ { * } ^ { E } ( X )$ be the cellular chain complex defined via $\tilde { E } _ { * }$

$$
C _ { * } ^ { E } ( X ) = \tilde { E } _ { * } ( X ^ { n } / X ^ { n - 1 } ) .
$$

We can run our proof from two lectures ago to show that $\tilde { E } _ { n } ( X ) \cong H _ { n } ( \tilde { C } _ { * } ^ { E } ( X ) )$ , where $\tilde { C } _ { * } ^ { E } ( X )$ is the reduced cellular chain complex $C _ { * } ^ { E } ( X ) / C _ { * } ^ { E } ( b )$ . (This necessitates some slight adjustments in degree $0 ;$ otherwise the argument is identical.) To be precise, the argument shows that we can obtain an isomorphism

$$
\alpha \colon \tilde { E } _ { n } ( X ) \to H _ { n } ( \tilde { C } _ { * } ^ { E } ( X ) )
$$

as follows: $x \in \tilde { E } _ { n } ( X )$ lifts to some $\hat { x } \in \tilde { E } _ { n } ( X ^ { n } )$ . We define $\alpha ( x )$ as the image of ˆx in ${ \tilde { E } } _ { n } ( X ^ { n } / X ^ { n - 1 } )$

The dimension and suspension axioms tell us that $\tilde { E } _ { * } ( S ^ { n } ) \cong \mathbb { Z } _ { ( n ) }$ , and hence that $\tilde { E } _ { n } ( X ^ { n } / X ^ { n - 1 } ) = \mathbb { Z } ^ { \{ n - \mathrm { c e l l s } \} }$ . As before, the cellular differential may be identified with a degree matrix, but at this point we hit a snag. The degree matrix is computed using $\tilde { E } _ { * }$ ∗ rather than ordinary homology. Do these degrees agree?

Let $f \colon S ^ { n } \to S ^ { n }$ be a map preserving a basepoint. It has a homology degree and an E˜∗-degree, and we would like to prove that they are the same. This is easy to check for $S ^ { 0 }$ , and quite easy also for $S ^ { 1 }$ , where we know that every map $f$ is homotopic rel basepoint to $z \mapsto z ^ { d }$ for some $d \in \mathbb { Z }$ . We can try to prove it in general by induction on $n _ { \mathrm { : } }$ , using naturality of the suspension isomorphism, but this will only work for maps $f$ homotopic to $\Sigma g$ for some $g \colon S ^ { n - 1 } \to S ^ { n - 1 }$ . Does this exhaust all possible maps $S ^ { n } \to S ^ { n } ?$ Yes. This can be seen as a special case of the Hurewicz theorem, one of the basic principles of homotopy theory. Alternatively, it can be proved using a little differential topology (see Milnor, Topology from the differentiable viewpoint).

The upshot is that the cellular chain complexes as defined via $\tilde { E } _ { * }$ and $\tilde { H } _ { * }$ coincide. We deduce an isomorphism

$$
{ \tilde { E } } _ { * } ( X ) \to { \tilde { H } } _ { * } ( X ) .
$$

One now checks that this isomorphism is natural with respect to cellular maps (those that send k-skeleta to k-skeleta) and so, by cellular approximation, with respect to arbitrary based maps. We have now succeeded in rebuilding $\tilde { E } _ { * }$ (and hence $E _ { * } )$ from the cellular homology of X.

We now recover $E _ { * }$ from its reduced theory $\tilde { E } _ { * }$ . Indeed, it follows from excision that the quotient map $X  X / A$ induces an isomorphism $E _ { * } ( X , A ) \cong \tilde { E } _ { * } ( X / A )$ when $A \neq \varnothing ;$ and one has $E _ { * } ( X ) = \tilde { E } _ { * } ( X \amalg * )$

One can also recover the natural transformation $\delta _ { n }$ , though this is trickier, and I will omit it (see May chapters 14 and 8).

## IV. Product structures

## 21. Cohomology

A cochain complex over R is a sequence of R-modules and maps

$$
\cdots { \xrightarrow { } } C ^ { p - 1 } { \overset { d ^ { p - 1 } } { \longrightarrow } } C ^ { p } { \overset { d ^ { p } } { \longrightarrow } } C ^ { p + 1 } \to \dots , \quad p \in \mathbb { Z } ,
$$

such that $d ^ { p } \circ d ^ { p - 1 } = 0$ for all p. It’s just the same as a chain complex, except that the indexing runs the other way. We use superscripts for cochain complexes, subscripts for chain complexes. We write $C ^ { * } = \oplus _ { p } C ^ { p }$ The pth cohomology module is then

$$
H ^ { p } ( C ^ { * } ) = \ker d ^ { p } / \operatorname { i m } d ^ { p - 1 } ,
$$

and we put $H ^ { * } ( C ^ { * } ) = \oplus H ^ { p } ( C ^ { * } )$

If $( D _ { * } , \partial )$ is a chain complex then one obtains a cochain complex by dualisation, putting $C ^ { p } = \operatorname { H o m } _ { R } ( D _ { p } , R )$ and $( d ^ { p } f ) ( x ) = f ( \partial _ { p + 1 } x )$

Remark. It is not true that $C ^ { * } = \mathrm { H o m } _ { R } ( D _ { * } , R )$ , unless $C _ { p } = 0$ for $| p | \gg 0 :$ one has Hom $\begin{array} { r } { { \bf \nabla } _ { R } ( D _ { * } , R ) = \prod _ { p } C ^ { p } } \end{array}$ , which is usually bigger than $\oplus _ { p } C ^ { p }$

If X is a space, one defines the singular cochains $S ^ { * } ( X ; R )$ by

$$
S ^ { p } ( X ; R ) = \operatorname { H o m } _ { \mathbb { Z } } ( S _ { p } ( X ) , R ) ,
$$

with the differentials $d ^ { p }$ defined by dualising ∂:

$$
( d ^ { p } c ) ( \sigma ) = c ( \partial \sigma ) = \sum _ { i } { ( - 1 ) ^ { i } c ( \sigma \circ \delta _ { i } ) } .
$$

One then puts $H ^ { p } ( X ; R ) = H ^ { p } ( S ^ { * } ( X ; R ) )$ . Note that singular cochains, and hence singular cohomology, are contravariantly functorial: a map $f \colon X \ \to \ Y$ induces $f ^ { * } \colon H ^ { * } ( Y ; R ) \to H ^ { * } ( X ; R )$ , and one has $( f \circ g ) ^ { * } = g ^ { * } \circ f ^ { * }$

Relative cohomology $H ^ { p } ( X , A ; R )$ for a subspace $i \colon A \to X$ is defined as the cohomology of ker $\cdot ( i ^ { * } \colon S ^ { * } ( X ; R ) \to S ^ { * } ( A ; R ) )$ ).

All the familiar properties of homology (long exact sequences of the pair, homotopy invariance, excision, Mayer–Vietoris, etc.) have dual versions in cohomology, with essentially identical proofs. Note that the connecting maps in long exact sequences go up not down in degree.

Exercise 21.1: Formulate these properties of cohomology, and think through how you would prove them.

Theorem 21.1 (Dual universal coefficients). If X is a space, and R any commutative unital ring, there are natural $( i n \ X )$ , non-naturally split short exact sequences

$$
0 \to \operatorname { E x t } ( H _ { p - 1 } ( X ) , R ) \to H ^ { p } ( X ; R ) \overset { q } \to \operatorname { H o m } _ { \mathbb { Z } } ( H _ { p } ( X ) , R ) \to 0 .
$$

In particular, there are non-canonical isomorphisms

$$
H ^ { n } ( X ) \cong \operatorname { H o m } ( H _ { n } ( X ) , \mathbb { Z } ) \oplus H _ { n - 1 } ( X ) _ { \mathrm { t o r s } } .
$$

where the $A _ { \mathrm { t o r s } }$ denotes the torsion subgroup of A.

This is a direct consequence of an algebraic theorem given below.

Exercise 21.2: Show that $H ^ { 1 } ( X ; R ) \cong \operatorname { H o m } _ { \mathbb { Z } } ( \pi _ { 1 } ( X ) , R )$ for path connected X. Deduce that $H ^ { 1 } ( X ) = H ^ { 1 } ( X ; \mathbb { Z } )$ is a torsion-free abelian group for X locally path connected X.

21.1. Ext. Fix a commutative ring R and an R-module P . We investigate the effect on exact sequences of the functor Hom $( \cdot , P )$ from R-modules to R-modules. This problem is dual to the one we considered earlier involving tensor product, because of the adjunction

$$
{ \mathrm { H o m } } ( M \otimes Q , P ) \cong { \mathrm { H o m } } ( Q , { \mathrm { H o m } } ( M , P ) ) .
$$

The arguments closely parallel those in the proof of homology universal coefficients, and we shall mostly leave the verifications to the reader to work through.

Lemma 21.2. Let $0 \to M _ { 1 } \ { \overset { i } { \to } } \ M _ { 2 } \ { \overset { p } { \to } } \ M _ { 3 } \to 0$ be a short exact sequence of $R \mathrm { - }$ modules. Let P be another R-module. Then the induced sequence

$$
0 \longrightarrow \mathrm { H o m } ( M _ { 3 } , P ) \stackrel { p ^ { * } } \longrightarrow \mathrm { H o m } ( M _ { 2 } , P ) \stackrel { i ^ { * } } \longrightarrow \mathrm { H o m } ( M _ { 1 } , P )
$$

is also exact. If the short exact sequence splits (for instance, if $M _ { 3 }$ is a free module) then $\mathrm { H o m } ( M _ { 2 } , P )  \mathrm { H o m } ( M _ { 1 } , P )$ is surjective.

In general, i∗ is not surjective but its cokernel is measured by ‘Ext’. We assume R is a PID, so (as discussed in the context of homology universal coefficients) any R-module M has a two-step free resolution

$$
0 \to F _ { 1 } { \overset { f _ { 1 } } { \to } } F _ { 0 } { \overset { f _ { 0 } } { \to } } M \to 0 .
$$

Applying Hom(·, P ) to this sequence, we obtain a complex

$$
0 \to { \mathrm { H o m } } ( M , P ) { \overset { f _ { 0 } ^ { * } } { \to } } { \mathrm { H o m } } ( F _ { 0 } , P ) { \overset { f _ { 1 } ^ { * } } { \to } } { \mathrm { H o m } } ( F _ { 1 } , P ) \to 0
$$

which is exact at ${ \mathrm { H o m } } ( M , P )$ and at Hom $( F _ { 0 } , P )$ . We prefer to truncate this to the (non-exact) sequence

$$
0 \to \operatorname { H o m } ( F _ { 0 } , P ) { \overset { f _ { 1 } ^ { * } } { \to } } \operatorname { H o m } ( F _ { 1 } , P ) \to 0 .
$$

which we think of as a cochain complex. By the lemma, its cohomology at Hom $( F _ { 0 } , P )$ (i.e., ker $f _ { 1 } ^ { * } )$ is naturally isomorphic to Hom $( M , P )$ . We define Ext $( M , P )$ to be its cohomology at Hom $( F _ { 1 } , P )$ :

$$
\operatorname { E x t } ( M , P ) = \operatorname { c o k e r } f _ { 1 } ^ { * } .
$$

We showed in our treatment of Tor that given two free resolutions $( F _ { * } ~ { \stackrel { f _ { 0 } } { \to } } ~ M )$ and $( G _ { * } \ { \stackrel { g _ { 0 } } { \to } } \ M )$ , there is a chain map $\alpha \colon F _ { * } \to G _ { * }$ , unique up to chain homotopy, such that $g _ { 0 } \circ \alpha = f _ { 0 }$ . This shows that $\operatorname { E x t } ( M , P )$ is independent of the choice of free resolution, up to canonical isomorphism.

Remark. Those who have studied Ext in other contexts should note that one can compute $\operatorname { E x t } ( M , P )$ from a projective resolution of M or an injective resolution of P . We have opted for a special case of the former.

Example 21.3. • When R is a field we may take $F _ { 0 } = M$ and $F _ { 1 } = 0$ . Thus Ext $( M , P ) = 0$ for all P .

• If M is a free module over the PID R, we may take $F _ { 0 } = M$ and $F _ { 1 } = 0$ Hence $\operatorname { E x t } ( M , P ) = 0$ for all $P .$

• The R-module $M = R / ( x )$ has free resolution $0 \to R { \overset { x } { \to } } R \to R / ( x ) \to 0$ Thus

$$
\begin{array} { l } { \operatorname { E x t } ( R / ( x ) , P ) = \operatorname { c o k e r } ( x ^ { * } \colon \operatorname { H o m } ( R , P ) \to \operatorname { H o m } ( R , P ) ) } \\ { \qquad = \operatorname { c o k e r } ( x \colon P \to P ) } \\ { \qquad = P / x P . } \end{array}
$$

For instance, $\operatorname { E x t } ( R / ( x ) , R ) = R / ( x )$ . Since Ext commutes with direct sum (on either factor), one deduces that for a finitely-generated R-module M one has $\operatorname { E x t } ( M , R ) = M _ { t o r s }$ , the torsion submodule of M.

Theorem 21.4 (Dual universal coefficients). Let $C _ { * }$ be a chain complex of free $R \mathrm { - }$ modules over a PID R. Then, for any R-module P , one has short exact sequences

$$
0 \to \operatorname { E x t } ( H _ { p - 1 } ( C _ { * } ) , P ) \to H ^ { p } ( \operatorname { H o m } ( C _ { * } , P ) ) { \overset { q } { \to } } \operatorname { H o m } ( H _ { p } ( C _ { * } ) , P ) \to 0 .
$$

These sequences split, but there is no preferred splitting. In particular, taking $P =$ $R ,$ we get short exact sequences

$$
0 \to H _ { p - 1 } ( C _ { * } ) _ { t o r s } \stackrel { j } \to H ^ { p } ( C _ { * } ^ { \vee } ) \stackrel { q } \to H _ { p } ( C _ { * } ) ^ { \vee } \to 0 ,
$$

where $f o r$ any R-module M, $M ^ { \vee }$ denotes Hom $( M , R )$

Proof. The proof is similar to that of the universal coefficient theorem for tensor products. We take for our free resolution of the homology groups

$$
0 \to B _ { p } { \overset { i _ { p } } { \to } } Z _ { p } \to H _ { p } ( C _ { * } ) \to 0
$$

$( B _ { p }$ and $Z _ { p }$ are free because $B _ { p } \subset Z _ { p } \subset C _ { p } )$ . Thus we have

$$
\operatorname { E x t } ( H _ { p - 1 } ( C _ { * } ) , R ) = \operatorname { c o k e r } [ i _ { p - 1 } ^ { * } \colon \operatorname { H o m } ( Z _ { p - 1 } , R ) \to \operatorname { H o m } ( B _ { p - 1 } , R ) ] .
$$

As in the tensor product argument, we have short exact sequences

$$
0 \to Z _ { p } \to C _ { p } { \overset { \partial _ { p } } { \to } } B _ { p - 1 } \to 0
$$

which split and therefore induce short exact sequences

$$
0 \to { \mathrm { H o m } } ( B _ { p - 1 } , R ) { \overset { d ^ { p } } { \to } } \operatorname { H o m } ( C _ { p } , R ) \to \operatorname { H o m } ( Z _ { p } , R ) \to 0 .
$$

These constitute a short exact sequence of cochain complexes, and the resulting long exact sequence on cohomology reads(!)

$$
\begin{array} { r } { \mathrm { H o m } ( Z _ { p - 1 } , R ) \overset { i _ { p - 1 } ^ { * } }  \mathrm { H o m } ( B _ { p - 1 } , R ) \overset { d ^ { p } }  H ^ { p } ( \mathrm { H o m } ( C _ { * } , R ) )  \mathrm { H o m } ( Z _ { p } , R ) \overset { i _ { p } ^ { * } }  \mathrm { H o m } ( B _ { p } , R ) . } \end{array}
$$

We deduce from this short exact sequences

$$
0 \to \operatorname { c o k e r } ( i _ { p - 1 } ^ { * } ) \to H ^ { p } ( \operatorname { H o m } ( C _ { * } , R ) ) \to \ker ( i _ { p } ^ { * } ) \to 0 .
$$

But ker $i _ { p } ^ { * } = \operatorname { H o m } ( H _ { p } ( C _ { * } ) , R )$ and coker $( i _ { p - 1 } ^ { * } ) = \operatorname { E x t } ( H _ { p - 1 } ( C _ { * } ) , R )$ . These short exact sequences split because Hom $( H _ { p } ( C _ { * } ) , R )$ is a free R-module. 

Remark. The universal coefficients theorems show that $H _ { * } ( X )$ determines $H _ { * } ( X ; R )$ and $H ^ { * } ( X ; R )$ up to isomorphism, but not functorially. It is arguably better to think of the singular chains as defining functors $S _ { n } \colon \mathbf { h T o p } \to \mathbf { h C h }$ , where the category on the right is the category of chain complexes and chain homotopy classes of chain maps. These functors can then be followed by algebraic functors $\cdot \otimes R$ and Hom(·, R).

Exercise 21.3: Work over $\mathbb { Z }$ and fix distinct primes $p$ and $q .$ Compute (i) Ext $( \mathbb { Z } , \mathbb { Z } / p ^ { n } )$ (ii) Ext $( \mathbb { Z } / p ^ { n } , \mathbb { Z } )$ ; (iii) Ext $( \mathbb { Z } / p ^ { n } , \mathbb { Z } / q ^ { m } )$ ; (iv) Ext $: ( \mathbb { Z } / p ^ { n } , \mathbb { Z } / p ^ { m } )$ .

Exercise 21.4: Working over $\mathbb { Z } ,$ compute Ext $( A , \mathbb { Q } / \mathbb { Z } )$ for an arbitrary finitely generated abelian group A.

Exercise 21.5: For any simply connected space $X ,$ , one has $H ^ { 2 } ( X ) \cong$ Hom $( H _ { 2 } ( X ) , \mathbb { Z } )$

Exercise 21.6: Verify a case of the theorem by computing $H ^ { * } ( \mathbb { R } P ^ { 2 } ; \mathbb { Z } )$ in two ways. Do the same for $H ^ { * } ( \mathbb { R } P ^ { 2 } ; \mathbb { Z } / 2 )$

Exercise 21.7: What is the relation between $H ^ { * } ( X ; R )$ and $H ^ { * } ( X ) ?$

## 22. Product structures, formally

We explain the formal structure of the cup and cap products and state the Poincar´e duality theorem.

Homology and cohomology are much more powerful invariants when one takes account of their multiplicative structures. The cohomology $H ^ { * } ( X )$ is a graded ring under the cup product. Homology $H _ { * } ( X )$ is not a ring, but it is a graded module over the graded ring $H ^ { * } ( X )$ . This is expressed by the cap product.

22.1. The evaluation pairing. The most basic product structure is the ‘evaluation’ pairing

$$
H ^ { p } ( X ) \times H _ { p } ( X ) , \quad ( c , h ) \mapsto \langle c , h \rangle .
$$

In singular theory, this is induced by the evaluation

$$
S ^ { p } ( X ) \times S _ { p } ( X ) = \operatorname { H o m } ( S _ { p } ( X ) , \mathbb { Z } ) \times S _ { p } ( X ) \to \mathbb { Z } ;
$$

similarly in cellular theory. One extends the evaluation pairing to a linear map

$$
H ^ { * } ( X ) \otimes H _ { * } ( X ) \to \mathbb { Z }
$$

which is zero on $H ^ { p } \otimes H _ { q }$ when $p \neq q$

Remark. It might be interesting to axiomatise this pairing in an arbitrary Eilenberg– Steenrod theory. Over a field k, $H ^ { n } ( \cdot ; k )$ is dual to $H _ { n } ( \cdot ; k )$ in a functorial manner. Over Z this is not so, but there are specialisation maps $H ^ { n } ( \cdot ) \to H ^ { n } ( \cdot ; \mathbb { Z } / p )$ and $H _ { n } ( \cdot ) \to H _ { n } ( \cdot ; \mathbb { Z } / p )$ , so one could ask that an evaluation pairing should be naural, and should specialise to the dual pairing between mod $p$ homology and cohomology for all primes p.

22.2. The cup product. The cup product is an associative bilinear product

$$
H ^ { * } ( X ) \times H ^ { * } ( X ) \to H ^ { * } ( X ) , \quad ( a , b ) \mapsto a \smile b .
$$

Its fundamental properties are as follows:

• One has $H ^ { p } ( X ) \smile H ^ { q } ( X ) \subset H ^ { p + q } ( X )$ . Thus ^ makes $H ^ { * } ( X )$ into a graded ring.

• The ring has a unit element $1 \in H ^ { 0 } ( X )$ : it is characterised by $\langle 1 , h \rangle = 1$ when $h \in H _ { 0 } ( X )$ is the class of a point.

• The cup product is commutative in the graded sense:

$$
a \smile b = ( - 1 ) ^ { | a | | b | } b \smile a .
$$

• The cup product is functorial: if $f \colon X \to Y$ is a map then

$$
f ^ { * } ( a \smile b ) = f ^ { * } a \smile f ^ { * } b .
$$

hence $f ^ { * }$ is a homomorphism of unital graded rings. In particular, the cohomology ring is an invariant of homotopy type.

• The natural isomorphism $\begin{array} { r } { H ^ { * } ( \coprod _ { i \in I } X _ { i } ) \cong \prod _ { i \in I } H ^ { * } ( X _ { i } ) } \end{array}$ is an isomorphism of rings.

So, for example, the ‘pinching’ map $\begin{array} { r } { \prod _ { i \in I } X _ { i } \to \bigvee _ { i \in I } X _ { i } } \end{array}$ induces a ring homomorphism

$$
H ^ { n } ( \bigvee _ { i \in I } X _ { i } ) \to \prod _ { i \in I } H ^ { n } ( X _ { i } ) ,
$$

which is an isomorphism in degrees $n > 0$ . Since this isomorphism is induced by a map between the spaces, it respects the cup product.

22.3. The cap product. The cap product is a bilinear product

$$
H ^ { * } ( X ) \times H _ { * } ( X ) \to H _ { * } ( X ) , \quad ( c , h ) \mapsto c \frown h .
$$

Its fundamental properties are as follows:

• One has $( a \smile b ) \frown h = a \frown ( b \frown h )$

• One has $1 \frown h = h$

• One has $H ^ { p } ( X ) \frown H _ { n } ( X ) \subset H _ { n - p } ( X )$ . Thus _ makes $H _ { * } ( X )$ into a graded unital module (with suitable grading conventions...) over the ring $H ^ { * } ( X )$

• One has

$$
\langle a \smile b , h \rangle = \langle a , b \frown h \rangle .
$$

• If $f \colon X \to Y$ is a map then

$$
f _ { * } ( f ^ { * } c \frown h ) = c \frown f _ { * } h
$$

for $h \in H _ { * } ( X )$ and $c \in H ^ { * } ( Y )$ This shows that homology, as a graded module over cohomology, is an invariant of homotopy type.

• The natural isomorphism $\begin{array} { r } { H _ { * } ( \coprod _ { i \in I } X _ { i } ) \cong \bigoplus _ { i \in I } H _ { * } ( X _ { i } ) } \end{array}$ is an isomorphism of modules.

I don’t know whether the axioms for the cap and cup products that I have listed, when considered together, characterise both of them uniquely. However, the relation between cup, cap and evaluation products does force them to be non-trivial (e.g. one can’t define the cup product of positive-degree cohomology classes to be identically zero).

Most interesting computations of cohomology rings and homology modules invoke the Poincar´e duality theorem.

Theorem 22.1 (Poincar´e duality). Suppose M is a compact, connected, oriented n-manifold with fundamental class $[ M ] \in H _ { n } ( M )$ . Then the ‘duality map’

$$
D \colon H ^ { p } ( M ) \to H _ { n - p } ( M ) , \quad D ( c ) = c \frown [ M ] ,
$$

is an isomorphism for all $p \in \mathbb Z$

The proof of this theorem mostly uses the naturality properties of cap and cup products, though at one point it becomes necessary to look more closely at the definition.

In practice, one works with a corollary. Next time we’ll use this to compute the cohomology ring of projective space.

Corollary 22.2 (Poincar´e duality: cup product version). Let M be a compact, connected, oriented n-manifold, and $[ M ] \in H _ { n } ( M )$ the fundamental class. Then for any $p \in \mathbb Z$ the Poincar´e pairing

$$
H ^ { p } ( M ) / T ^ { p } \times H ^ { n - p } ( M ) / T ^ { n - p } \to \mathbb { Z } , \quad ( a , b ) \mapsto \langle a \smile b , [ M ] \rangle ,
$$

is non-degenerate. Here $T ^ { k } \subset H ^ { k } ( M )$ denotes the submodule of torsion classes, so $H ^ { k } ( M ) / { \bar { T } } ^ { k }$ is torsion-free and hence free.

Remark. Note that the ‘hence’ here uses a fact that we have not proved, that the (co)homology of a compact manifold is finitely generated (a finitely generated torsion-free abelian group is free). In fact, any compact manifold is homotopyequivalent to a finite CW complex. In the smooth case, this follows easily from Morse theory; in general, it is a hard theorem.

Remark. Non-degeneracy means that the adjoint map

$$
H ^ { p } ( M ) / T ^ { p } \to \mathrm { H o m } ( H ^ { n - p } ( M ) / T ^ { n - p } , \mathbb { Z } ) , \quad a \mapsto ( b \mapsto \langle a \smile b , [ M ] \rangle )
$$

is an isomorphism. If one fixes bases for the free abelian groups $H ^ { k } ( M ) / T ^ { k }$ , it is the assertion that the matrix of the pairing is square and its determinant is ±1.

Proof of the corollary. Recall a corollary of universal coefficients (which used finite generation): $H ^ { p } ( M ) \ : = \ : \mathrm { H o m } ( H _ { p } ( M ) , \mathbb { Z } ) \oplus H _ { p - 1 } ( M ) _ { t o r s } .$ Thus $H ^ { p } ( M ; R ) / T ^ { p } \cong$ Hom $( H _ { p } ( M ) , \mathbb { Z } )$ . The adjoint map α: $H ^ { p } ( \dot { M } ) $ Hom $( H ^ { n - p } ( M ) , \mathbb { Z } )$ sends a to the map $b \mapsto \langle a \smile b , [ M ] \rangle = \pm \langle b \smile a , [ M ] \rangle = \pm \langle b , a \frown [ M ] \rangle$ . If b is non-zero (mod torsion) then it evaluates non-trivially on some homology class, and by the Poincar´e duality theorem, we may take that class to be of form $b \frown [ M ]$ . Hence ker $\alpha = T ^ { p }$ . And α is also surjective, because given any homomorphism $f \in H ^ { n - p } ( M ) \to \mathbb { Z }$ , we can represent it as evaluation on some homology class $h = D ( c )$ , and then $f = \alpha ( c )$

## 23. Formal computations in cohomology

We show that Poincar´e duality leads to computations of cup product structures. We explain an algebraic application.

Last time, we noted a corollary of Poincar´e duality, that on a compact oriented manifold, the cup-product pairing on cohomology mod torsion is non-degenerate. We now apply this to complex projective space. Take a polynomial ring $\mathbb { Z } [ u ]$ , and make it a graded ring by declaring u to have degree 2. Truncate it to the graded ring $\mathbb { Z } [ u ] / ( u ^ { n + 1 } )$ . As a graded abelian group, we have

$$
H ^ { * } ( \mathbb { C } P ^ { n } ) \cong \mathbb { Z } [ u ] / ( u ^ { n + 1 } ) .
$$

Theorem 23.1. There is an isomorphism of graded rings,

$$
H ^ { * } ( \mathbb { C } P ^ { n } ) \cong \mathbb { Z } [ u ] / ( u ^ { n + 1 } ) , \quad \deg u = 2 .
$$

Proof. Induction on n. The space $\mathbb { C } P ^ { 0 }$ is a point, and the result is trivially true in this case. It is also trivially true when $n = 1$ , and we will start the induction there. If $n > 1$ , observe that we have an inclusion $i \colon \mathbb { C } P ^ { n - 1 } \to \mathbb { C } P ^ { n }$ , induced by a linear inclusion $\mathbb { C } ^ { n + 1 } \to \mathbb { C } ^ { n + 2 }$ . By induction, $H ^ { * } ( \mathbb { C } P ^ { n - 1 } ) \cong \mathbb { Z } [ t ] / t ^ { n }$ where deg $t \ = \ 2 .$ . Now, $i ^ { * }$ is additively an isomorphism up to degree $2 ( n - 1 )$ . Let $u \in H ^ { 2 } ( \mathbb { C } P ^ { n } )$ be defined by $i ^ { * } u = t .$ . Since $t ^ { n }$ generates $\bar { H ^ { 2 ( n - 1 ) } } ( \mathbb { C } P ^ { n - 1 } )$ 1 ), $u ^ { n }$ generates $H ^ { 2 ( n - 1 ) } ( \mathbb { C } P ^ { n } )$ $\mathrm { B y }$ Poincar´e duality, the pairing

$$
H ^ { 2 ( n - 1 ) } ( \mathbb { C } P ^ { n } ) \times H ^ { 2 } ( \mathbb { C } P ^ { n } ) \to \mathbb { Z }
$$

is non-degenerate over $\mathbb { Z } .$ . It follows that the generators of the two groups pair to give ±1, i.e.,

$$
\langle u ^ { n - 1 } \cup u , [ \mathbb { C } P ^ { n } ] \rangle = \langle u ^ { n } , [ \mathbb { C } P ^ { n } ] \rangle = \pm 1 .
$$

Hence $u ^ { n }$ generates $H ^ { 2 n } ( \mathbb { C } P ^ { n } )$ , and the result follows.

Exercise 23.1: Specify a suitable cohomology class u. Describe $u ^ { k }$ for all k. (Part of the exercise is to work out what format the answer should sensibly take.)

Remark. A precisely similar argument, using the mod 2 version of Poincar´e duality, shows that

$$
H ^ { * } ( \mathbb { R } P ^ { n } ; \mathbb { Z } / 2 ) \cong ( \mathbb { Z } / 2 ) [ t ] / t ^ { n + 1 } , \quad \mathrm { d e g } t = 1 .
$$

The result for projective spaces shows that the cup product makes cohomology a more powerful invariant.

Example 23.2. $\mathbb { C } P ^ { 2 }$ is not homotopy equivalent to $S ^ { 2 } \lor S ^ { 4 }$ . Indeed, $H ^ { * } ( \mathbb { C } P ^ { 2 } )$ contains a degree 2 class u such that $u \smile u$ is non-tivial, whereas the cup-square of a degree 2 class in $H ^ { * } ( S ^ { 2 } \vee S ^ { 4 } )$ is always zero.

Example 23.3. Any homeomorphism $h \colon \mathbb { C } P ^ { 2 } \to \mathbb { C } P ^ { 2 }$ preserves orientation. For it suffices to show that $h _ { * } [ \mathbb { C } P ^ { 2 } ] = [ \mathbb { C } P ^ { 2 } ]$ (where $\left[ \mathbb { C } P ^ { 2 } \right]$ is the fundamental class), i.e., that h has degree 1 rather than −1. But $h ^ { \ast } u = \pm u$ , since these are the two generators for $H ^ { 2 } .$ . So $h ^ { * } ( u \smile u ) = h ^ { * } u \smile h ^ { * } u = u \smile u$ , hence $h ^ { * }$ is the identity on $H ^ { 4 }$ . Hence the dual map h∗ on $H _ { 4 }$ is also the identity.

The argument also extends to $\mathbb { C } P ^ { 2 n }$ , but not to $\mathbb { C } P ^ { 2 n + 1 }$ (indeed, it is false for $\mathbb { C } P ^ { 1 } )$

However, it still has limitations:

Example 23.4. $S ^ { 3 } \backslash S ^ { 5 }$ and $S ( \mathbb { C } P ^ { 2 } )$ have isomorphic cohomology rings: additively, both are $\mathbb { Z } _ { ( 0 ) } \oplus \mathbb { Z } _ { ( 3 ) } \oplus \mathbb { Z } _ { ( 5 ) }$ where the subscripts denote degree. The product of two classes of positive degree has to be zero, for reasons of degree.

Exercise 23.2: (a) Suppose that X and Y are compact, connected, orientable nmanifolds. Describe the cohomology ring of their connected sum $X \# Y$ . (b) Prove that $\mathbb { C } P ^ { 2 } \# \mathbb { C } P ^ { 2 }$ and $\mathbb { C } P ^ { 2 } \# \overline { { \mathbb { C } P ^ { 2 } } }$ are not homotopy-equivalent. Here $\mathbb { C } P ^ { 2 }$ is the complex projective plane with one orientation, and $\overline { { \mathbb { C } P ^ { 2 } } }$ the same space with the opposite orientation.

23.1. The K¨unneth formula. There is one other general result which is very useful in computing cup products. To state it I need to work with cohomology with coefficients in a ring k. Cohomology with coefficients in k also carries a cup product, which is linear over k and so makes $H ^ { * } ( X ; k )$ a k-algebra.

The result is the K¨unneth formula. In general, if A and B are graded k-algebras then their tensor product $A \otimes B$ is also a graded k-algebra, with ith graded part $\oplus _ { j } A _ { j } \otimes B _ { i - j }$ , and product given on homogeneous monomials by

$$
( x \otimes y ) \cdot ( x ^ { \prime } \otimes y ^ { \prime } ) = ( - 1 ) ^ { | y | | x ^ { \prime } | } ( x \smile x ^ { \prime } ) \otimes ( y \smile y ^ { \prime } ) .
$$

Theorem 23.5 (K¨unneth formula). Let X and Y be spaces. Define the ‘cross product’ map

$$
H ^ { * } ( X ; k ) \otimes _ { k } H ^ { * } ( Y ; k ) \to H ^ { * } ( X \times Y ; k ) , \quad ( x , y ) \mapsto x \times y : = { \mathsf { p r } } _ { X } ^ { * } x \smile { \mathsf { p r } } _ { Y } ^ { * } y ,
$$

where $\mathsf { p r } _ { X }$ and $\mathsf { p r } _ { Y }$ the two projection maps from $X \times Y$ . One checks that it is a map of graded k-algebras. When $X$ and Y are CW complexes, and $H ^ { * } ( Y )$ is a finitely generated free k-module $( e . g .$ when k is a field), this map is an isomorphism.

Without the assumption that $H ^ { * } ( Y )$ is a free module, there is still a K¨unneth theorem; it says that the cross product map is injective, and expresses its cokernel using Tor.

Example 23.6.

$$
H ^ { * } ( \mathbb { C } P ^ { n } \times \mathbb { C } P ^ { m } ) \cong \mathbb { Z } [ t , u ] / ( t ^ { n + 1 } , u ^ { m + 1 } )
$$

with $| t | = | u | = 2$ , and

$$
H ^ { * } ( \mathbb { R } P ^ { n } \times \mathbb { R } P ^ { m } ; \mathbb { Z } / 2 ) \cong ( \mathbb { Z } / 2 ) [ x , y ] / ( x ^ { n + 1 } , y ^ { m + 1 } )
$$

with $| x | = | y | = 1$ (the signs become irrelevant when $k = \mathbb { Z } / 2 )$

23.2. An algebraic application of cup product. A division algebra over a field F is an F -vector space A equipped with a bilinear map m: $A \times A \to A .$ , such that for each $x \in A \setminus \{ 0 \}$ the linear maps $m ( x , \cdot ) \colon A \to A$ and $m ( \cdot , x ) \colon A \to A$ are isomorphisms.

Theorem 23.7 (Hopf). The dimension of a finite-dimensional division algebra over R is a power of 2.

Proof. Let A be an n-dimensional real division algebra, with multiplication

$$
m \colon A \times A \to A .
$$

Bilinearity of $m ,$ and the fact that $m ( x , y ) = 0$ implies $x = 0$ or $y = 0 ,$ , tell us that there is an induced map

$$
M = \mathbb { P } m \colon \mathbb { P } A \times \mathbb { P } A \longrightarrow \mathbb { P } A .
$$

Let k be the field $\mathbb { Z } / 2$ . On mod 2 cohomology, M gives us a map

$$
M ^ { * } \colon H ^ { * } ( \mathbb { P } A \times \mathbb { P } A ; k ) \to H ^ { * } ( \mathbb { P } A ; k ) .
$$

We have $H ^ { * } ( \mathbb { P } A ; k ) = k [ x ] / ( x ^ { n } )$ where deg $x = 1$ , and by the K¨unneth formula, $H ^ { * } ( \mathbb { P } A \times \mathbb { P } A ; \mathbb { Z } / 2 ) = k [ y , z ] / ( y ^ { n } , z ^ { n } )$ . Thus we have a map of graded rings

$$
M ^ { * } \colon k [ x ] / ( x ^ { n } ) \to k [ y , z ] / ( y ^ { n } , z ^ { n } ) .
$$

We claim that $M ^ { * } ( x ) = y + z$ . Indeed, we know that for some (or indeed, any) $\mu \in \mathbb { P } A$ , the composite $\mathbb { P } A \to \mathbb { P } A \times \mathbb { P } A \to \mathbb { P } A , \lambda \mapsto ( \lambda , \mu ) \mapsto M ( \lambda , \mu )$ is a homeomorphism, hence that $M ^ { * } x = y$ mod $z ,$ and similarly that $M ^ { * } x = z$ mod $y .$ This proves the claim.

Hence $( y + z ) ^ { n } \in k [ y , z ]$ lies in the ideal generated by $y ^ { n }$ and $z ^ { n }$ . This implies that the coefficient of $y ^ { k } z ^ { n - j }$ for $1 \leq j < n$ , namely $\textstyle { \binom { n } { j } }$ , must be zero in $k ,$ and hence that the equation

$$
( 1 + t ) ^ { n } = 1 + t ^ { n }
$$

holds in $k [ t ]$ . Now, $( 1 + t ) ^ { 2 } = 1 + t ^ { 2 }$ in $k [ t ]$ . Thus $( 1 + t ) ^ { 4 } = ( 1 + t ^ { 2 } ) ^ { 2 } = 1 + t ^ { 4 }$ , and more generally, $( 1 + t ) ^ { 2 ^ { m } } = ( 1 + t ^ { 2 ^ { m } } )$ . But if we write n in binary form, putting

$$
n = 2 ^ { m _ { 1 } } + 2 ^ { m _ { 2 } } + \cdot \cdot \cdot + 2 ^ { m _ { a } } , \quad m _ { 1 } < m _ { 2 } < \cdot \cdot \cdot < m _ { a } ,
$$

then $\ l ( 1 + t ) ^ { n } = \prod { ( 1 + t ) ^ { 2 ^ { m } i } } = \prod { ( 1 + t ^ { 2 ^ { m } i } ) }$ . But this expression is $1 + t ^ { 2 ^ { m _ { 1 } } }$ plus higher order terms. So the equation $( 1 + t ) ^ { n } = 1 + t ^ { n }$ holds only if $a = 1$ , i.e. n is a power of 2. 

Remark. The proof applies to a slightly more general kind of algebra: we can assume that there exist some x and y in A so that $m ( x , \cdot )$ and $m ( \cdot , y )$ are isomorphisms.

Exercise 23.3: Prove that the cohomology groups of a compact, simply connected, oriented 4-manifold M are completely determined by the second Betti number

$$
b _ { 2 } ( M ) = \dim _ { \mathbb { Q } } H ^ { 2 } ( M ; \mathbb { Q } ) .
$$

Prove that the cohomology ring is determined by the cup-product pairing $H ^ { 2 } \times H ^ { 2 } \to \mathbb { Z }$ Exercise 23.4: A special case of the Lefschetz fixed point theorem states that if $X$ is a finite CW complex, and $g \colon X \to X$ a map without fixed points, then

$$
\sum _ { p \geq 0 } ( - 1 ) ^ { p } \operatorname { t r } H ^ { p } ( g ) = 0 .
$$

Here $H ^ { p } ( g )$ is the induced map on $H ^ { * } ( X ; \mathbb { Q } )$ . What restrictions does this entail for groups acting freely on $\mathbb { C } P ^ { n } ?$

## 24. Cup products defined

We define the cup product of cochains.

24.1. The basic mechanism. The definition of cup products combines two ideas:

(1) There is a chain map

$$
D ^ { * } \colon C ^ { * } ( X \times X ) \to C ^ { * } ( X )
$$

induced by the diagonal map $D \colon X \to X \times X , x \mapsto ( x , x )$

(2) There is a natural chain map (actually, a quasi-isomorphism)

$$
\zeta \colon C ^ { * } ( X ) \otimes C ^ { * } ( X ) \to C ^ { * } ( X \times X ) .
$$

Here by $C ^ { * }$ denotes cochains, but they could be singular or cellular. Given these elements, one defines a chain map

$$
\smile \colon C ^ { p } ( X ) \otimes C ^ { q } ( X ) \to C ^ { p + q } ( X ) , \quad a \smile b = D ^ { \# } \circ \zeta ( a \otimes b ) .
$$

24.2. Cup products in cellular cohomology. Suppose, for instance, we work with cellular cohomology.

Proposition 24.1. Suppose X has a CW decomposition with p-cells $e _ { p } ^ { \alpha } .$ , and Y a CW decomposition with q-cell $f _ { q } ^ { \beta }$ . Then $X \times Y$ has a cell decomposition with (p + q)-cells $e _ { p } ^ { \alpha } \times e _ { q } ^ { \beta }$ . The cellular chain complex of the product is given by

$$
C _ { * } ^ { c e l l } ( X \times Y ) = C _ { * } ^ { c e l l } ( X ) \otimes C _ { * } ^ { c e l l } ( Y ) ,
$$

with the cellular boundary $d ^ { X \times Y } ( e \otimes f ) = d ^ { X } e \otimes f + ( - 1 ) ^ { \deg e } e \otimes d ^ { Y } f .$

I won’t give the proof (see Hatcher p. 268 or May p.99), but the basic point is that the product of a p-cell and a q-cell is a $p + q \mathrm { - c e l l }$

Let’s apply this to $X \times X$ . It has a cell decomposition with cells $e _ { p } ^ { \alpha } \otimes e _ { q } ^ { \beta }$ , and one has an isomorphism of chain complexes

$$
C _ { * } ^ { c e l l } ( X \times X ) \to C _ { * } ^ { c e l l } ( X ) \otimes C _ { * } ^ { c e l l } ( X ) ,
$$

where the differential on the right-hand side is given on the summand $C _ { p } ^ { c e l l } ( X )$ ⊗ $C _ { q } ^ { c e l l } ( X )$ by

$$
d _ { p } \otimes \mathrm { i d } + ( - 1 ) ^ { p } \mathrm { i d } \otimes d _ { q } .
$$

The cellular cochain complex $C _ { c e l l } ^ { * } ( X )$ is defined as the dual cochain complex to $( C _ { * } ( X ) , d )$ . Thus by duality one has an isomorphism of cochain complexes

$$
\zeta \colon C _ { c e l l } ^ { * } ( X ) \otimes C _ { c e l l } ^ { * } ( X ) \to C _ { c e l l } ^ { * } ( X \times X ) .
$$

Now, D is not a cellular map, but we have the cellular approximation theorem:

Theorem 24.2. Every map between CW complexes is homotopic to a cellular map, $i . e .$ , one which maps the k-skeleton to the k-skeleton for all k.

So D is homotopic to a cellular map $D ^ { \prime } \colon X \to X \times X$

Example 24.3. Make $S ^ { 1 } \mathrm { ~ a ~ }$ CW complex with exactly two cells. Then one can see from a picture how the diagonal $S ^ { 1 } \stackrel { - } {  } S ^ { 1 } \times S ^ { 1 }$ is homotopic to a cellular map.

Exercise 24.1: Find a cellular approximation to the diagonal $S ^ { n } \to S ^ { n } \times S ^ { n }$Define the cup product on the cellular cochain complex by

$$
a \smile b = D ^ { \prime \# } \circ \zeta ( a \otimes b ) .
$$

This is a perfectly reasonable (and correct) definition; for instance, it satisfies

$$
d ( a \smile b ) = d a \smile b + ( - 1 ) ^ { \vert a \vert } a \smile d b .
$$

Its only deficiency is that it is non-explicit, because of the cellular approximation to $D$

In some cases, one can write down an explicit cellular approximation and use it compute the cup product:

Example 24.4. Use a cellular approximation to the diagonal $S ^ { 1 } \to S ^ { 1 } \times S ^ { 1 }$ to construct another such approximation $S ^ { 1 } \times S ^ { 1 }  S ^ { 1 } \times S ^ { 1 } \times \bar { S } ^ { 1 } \times S ^ { 1 }$ . Hence compute the cup-product structure of $H ^ { * } ( S ^ { 1 } \times S ^ { 1 } )$

24.3. Cup products in singular cohomology. We have a canonically-defined chain map $D ^ { \# } \colon S ^ { * } ( X \times X ) \to S ^ { * } X$ . Explicitly, for $c \in S ^ { p } ( X \times X )$ and $\tau \in \Sigma _ { p } ( X )$ 7 one has

$$
\langle D ^ { \# } ( c ) , \tau \rangle = \langle c , \tau \times \tau \rangle .
$$

We want to define

$$
a \smile b = D ^ { \# } \zeta ( a \otimes b ) .
$$

We need to set up a suitable chain map ζ, which should be natural in X. There is an explicit formula for such a $\zeta ,$ called the Alexander–Whitney map:

Proposition 24.5 (Alexander–Whitney). Define a linear map

$$
\zeta = \zeta _ { X } \colon S ^ { p } ( X ) \otimes S ^ { q } ( X ) \to S ^ { p + q } ( X \times X )
$$

by

$$
\langle \zeta ( a \otimes b ) , \sigma \rangle = \langle a , ( { \mathsf { p r } } _ { 1 } \circ \sigma ) | _ { [ v _ { 0 } , \ldots , v _ { p } ] } ) \rangle \langle b , ( { \mathsf { p r } } _ { 2 } \circ \sigma ) | _ { [ v _ { p } , \ldots , v _ { p + q } ] } ) \rangle
$$

for $a \in S ^ { p } ( X ) , b \in S ^ { q } ( X )$ , and $\sigma \in \Sigma _ { p + q } ( X \times X )$ . Then $\zeta$ is a chain map. $I t$ is natural in X in that

$$
( f \times f ) ^ { * } \circ \zeta _ { Y } = \zeta _ { X } \circ f ^ { * }
$$

for $f \colon X \to Y$ . One has

$$
\zeta ( 1 _ { X } \otimes 1 _ { X } ) = 1 _ { X \times X } ,
$$

where $1 _ { X } \in S ^ { 0 } ( X )$ evaluates as 1 on any simplex (similarly 1X×X).

Exercise 24.2: Check the proposition.

We can use the Alexander–Whitney map to define the cup product as $D ^ { \# } \circ \zeta \colon$

Definition 24.6. The cup product of cochains a and b is defined by

$$
\langle a \smile b , \sigma \rangle = \langle a , \sigma | _ { [ v _ { 0 } , . . . , v _ { p } ] } ) \rangle \langle b , \sigma | _ { [ v _ { p } , . . . , v _ { p + q } ] } ) \rangle .
$$

Remark. It is a theorem of Eilenberg–Zilber that ζ is a chain-homotopy equivalence. Moreover, any other chain map $\zeta ^ { \prime }$ that is natural in X and satisfies $\zeta ^ { \prime } ( 1 _ { X } \otimes 1 _ { X } ) =$ $1 _ { X \times X }$ is naturally chain-homotopic to $\zeta .$ . Thus one could define cup product via $\zeta ^ { \prime }$ but on cohomology the definition would give the same product.

Lemma 24.7. One has

$$
\begin{array} { r } { d ( a \smile b ) = d a \smile b + ( - 1 ) ^ { | a | } a \smile d b ; } \\ { a \smile ( b \smile c ) = ( a \smile b ) \smile c ; } \\ { a \smile 1 _ { X } = a = 1 _ { X } \smile a . } \end{array}
$$

Thus $S ^ { * } ( X )$ is a differential graded algebra $( D G A )$ . For a map $f ,$ one has $f ^ { * } ( a \smile$ $b ) = f ^ { * } a \smile f ^ { * } b _ { \mathrm { \scriptscriptstyle 3 } }$ , so this DGA is natural in X.

Thus ^ descends to give a unital ring structure on cohomology $H ^ { * } ( X )$ bilinear product on cohomology, natural in X.

Exercise 24.3: Use singular cohomology to compute $H ^ { * } ( S ^ { 1 } \times S ^ { 1 } )$ as a ring. [You may find it helpful to think of $S ^ { 1 } \times S ^ { 1 }$ as $\mathsf { a \_ { \Delta \Delta \Delta \Delta \Delta \Delta \mathrm { c o m p l e x . } } } ]$

The cap product is defined by a similar procedure:

$$
S ^ { p } ( X ) \otimes S _ { n } ( X ) \overset { ^ { 1 \otimes D } \# } \longrightarrow ^ { 1 } S ^ { p } ( X ) \otimes S _ { n } ( X \times X ) ) \overset { ^ { 1 \otimes \zeta ^ { \vee } } } \longrightarrow S ^ { p } ( X ) \otimes [ S _ { * } ( X ) \otimes S _ { * } ( X ) ] _ { n } \longrightarrow S _ { n - p } ( X ) .
$$

Here the last map is

$$
c \otimes y \otimes z \mapsto \langle c , y \rangle z .
$$

Exercise 24.4: Check that the cap product has the properties I claimed two lectures back.

## 25. Non-commutativity

We sketch a definition of the simplest interesting Steenrod operation,

$$
S q ^ { n - 1 } \colon H ^ { n } ( X ; \mathbb { Z } / 2 ) \to H ^ { 2 n - 1 } ( X ; \mathbb { Z } / 2 )
$$

and use it to distinguish two homotopy types.

In the de Rham cohomology theory of smooth manifolds M, which is naturally isomorphic to $M \mapsto H ^ { * } ( M ; \mathbb { R } )$ , the wedge product of differential forms is commutative (in the graded sense). However, the cup product of cochains is not commuative.

Lemma 25.1. The cochain-level cup product of singular cochains is not commutative. However, there exist natural maps κ : $S ^ { p } ( X ) \otimes S ^ { q } ( X )  S ^ { p + q - 1 } ( X )$ satisfying the chain homotopy identity

$$
a \smile b - ( - 1 ) ^ { \vert a \vert \vert b \vert } b \smile a = d \kappa ( a \otimes b ) + \kappa ( d a \otimes b + ( - 1 ) ^ { \vert a \vert } a \otimes d b ) .
$$

Hence the cohomology cup product is commutative (in the graded sense).

I will not prove this lemma.

Suppose we work with cochains over $\mathbb { Z } / 2$ . Construct the natural map κ as in the lemma. For $[ c ] \in H ^ { n } ( X ; \mathbb { Z } / 2 )$ , define $S q ^ { n } ( [ c ] ) = [ c \smile c ] \in H ^ { 2 n } ( X ; \mathbb { Z } / 2 )$ ), and

$$
S q ^ { n - 1 } ( [ c ] ) = [ \kappa ( c \otimes c ) ] \in H ^ { 2 n - 1 } ( X ; \mathbb { Z } / 2 ) .
$$

This makes sense because the identity satisfied by κ implies that, working mod 2, we have that $d \kappa ( c \otimes c ) = 0$ when $d c = 0$ , and also that $\kappa ( ( c + d b ) \otimes ( c + d b ) ) - \kappa ( c \otimes c )$ is exact.

It is eminently plausible—and moreover true—that if $( X ; A , B )$ is an excisive triad then the Mayer–Vietoris connecting maps $\delta _ { p } \colon H ^ { p } ( A \cap B ) \to H ^ { p + 1 } ( X )$ satisfy

$$
S q ^ { n - 1 } ( \delta _ { n } c ) = \delta _ { 2 n - 1 } ( S q ^ { n - 1 } c ) , \quad c \in H ^ { n - 1 } ( A \cap B ) .
$$

(Here the $S q ^ { n - 1 }$ on the right is the cup-square, that on the left the one defined using κ.) It follows that one has (for $n > 0 )$ )

$$
S q ^ { n - 1 } ( \Sigma c ) = \Sigma ( S q ^ { n - 1 } c ) = \Sigma ( c \smile c ) , \quad c \in H ^ { n - 1 } ( X ) ,
$$

where $\Sigma \colon \tilde { H } ^ { \ast } ( X ) \to H ^ { \ast + 1 } ( S X )$ is the suspension isomorphism.

Example 25.2. For instance, if $0 \neq u \in H ^ { 2 } ( \mathbb { C } P ^ { 2 } ; \mathbb { Z } / 2 )$ then in $H ^ { 5 } ( S \mathbb { C } P ^ { 2 } ; \mathbb { Z } / 2 )$ one has

$$
S q ^ { 2 } ( \Sigma u ) = \Sigma ( u ^ { 2 } ) \neq 0 .
$$

So $S q ^ { 2 }$ is non-zero. On the other hand, in $S ^ { 5 } \vee S ^ { 3 }$ , which has the same cohomology ring as $S ( \mathbb { C } P ^ { 2 } )$ , one has $S q ^ { 2 } ( H ^ { 3 } ) = 0 . \mathrm { ~ S o }$ , once the operation $S q ^ { 2 } \colon H ^ { 3 } \to H ^ { 5 }$ has been put on a sound footing, we will have a proof that $S ^ { 5 } \vee S ^ { 3 } \not \cong S ( \mathbb { C } P ^ { 2 } )$

We have omitted several details in this discussion, but the basic points are these.

• There is no commutative cochain-level cup product on mod 2 cochains which is natural in X.

• This non-commutativity has a manifestation in an operation on mod 2 cohomology which is sometimes non-trivial. This can be used to distinguish homotopy types (such as $S ^ { 5 } \vee S ^ { 3 }$ versus $S ( \mathbb { C } P ^ { 2 } ) )$ .

## 26. Poincare duality´

We provide most but not all of the details of the proof of Poincar´e duality.

Poincar´e duality is primarily a statement about compact manifolds. Let us recall the statement in that case.

Theorem 26.1 (Poincar´e duality: compact case). Suppose M is a compact, connected, R-oriented n-manifold with fundamental class $[ M ] \in H _ { n } ( M ; R )$ . Then the ‘duality map’

$$
D \colon H ^ { p } ( M ; R ) \to H _ { n - p } ( M ; R ) , \quad D ( c ) = c \frown [ M ] ,
$$

is an isomorphism for all $p \in \mathbb Z$

We shall prove the Poincar´e duality theorem using Mayer–Vietoris sequences, starting from simple cases and gradually expanding the generality. However, most of the manifolds one encounter along the way are non-compact, and it is therefore useful to have a formulation valid in the non-compact case. This involves the compactly supported cohomology and relative cap products.

The compactly supported cohomology $H _ { c } ^ { * } ( M ; R )$ is is the cohomology of a complex built from singular cochains c for which there is some compact subset K so that c annihilates all chains in $X \setminus K . ^ { 1 }$ More precisely, we define

$$
H _ { c } ^ { p } ( M ; R ) = \varinjlim _ { K } H ^ { p } ( X , X \setminus K ; R )
$$

where the direct limit is over compact subsets $K \subset X$ . To explain this, note that the compact subsets of X form a direct system under inclusion. This means that one has inclusion maps $i \colon K _ { 1 } \to K _ { 2 }$ , and the composite of inclusion maps is again an inclusion map. The identity map on X is then a map of pairs

$$
( X , X \setminus K _ { 2 } ) \to ( X , X \setminus K _ { 1 } ) ,
$$

and hence induces a homomorphism

$$
H ^ { p } ( X , X \setminus K _ { 2 } ; R ) \to H ^ { p } ( X , X \setminus K _ { 1 } ; R ) .
$$

In this way, the modules $H ^ { p } ( X , X \setminus K )$ become a direct system as $K$ ranges over compact subsets. We defined $H _ { c } ^ { p } ( M ; R )$ as the direct limit of this system. Thus one has a canonical map

$$
H ^ { p } ( X , X \setminus K ; R ) \to H _ { c } ^ { p } ( X ; R )
$$

for each compact $K ,$ , and these commute with the maps in the inverse system.   
Indeed, $H _ { c } ^ { p } ( X ; R )$ is universal with respect to this property.

In practice, one computes $H _ { c } ^ { p } ( X )$ as the direct limit of $H ^ { p } ( X , X \setminus K )$ as K ranges over some compact exhaustion, i.e., a family of compact subspaces $K _ { i }$ such that every compact subspace is contained in some $K _ { i }$ . This is valid by abstract nonsense about cofinal families.

Example 26.2. Let us compute $H _ { c } ^ { p } ( \mathbb { R } ^ { n } )$ . A compact exhaustion is given by the discs $D ^ { n } ( m )$ centred at 0 and of radius $m = 1 , 2 , \ldots$ One has $H ^ { \ast } ( \mathbb { R } ^ { n } , \mathbb { R } ^ { n } \mid$ $D ^ { n } ( m ) ) \cong \mathbb { Z } _ { ( n ) }$ The inclusion of $D ( m )$ in $D ( m + 1 )$ obviously induces an isomorphism on the relative cohomology groups. Hence $H _ { c } ^ { * } ( \mathbb { R } ^ { n } ) \cong \mathbb { Z } _ { ( n ) }$

Remark. Taking direct limits of (co)chain complexes is an exact functor, i.e. it commutes with passing to (co)homology. This is not true of inverse limits; the failure of exactness is measured by the derived functor $\varprojlim ^ { 1 }$ of the inverse limit.

The cap product $\frown \colon H ^ { p } ( X ) \times H _ { q } ( X ) \to H _ { q - p } ( X )$ generalizes to a relative cap product

$$
H ^ { p } ( X , A ) \times H _ { q } ( X , A ) \to H _ { q - p } ( X ) ,
$$

defined at (co)chain level by the same formula as the original cap product. Indeed, one has $\partial ( \phi \frown a ) = d \phi \frown a \pm \phi \frown \partial c$ . If φ represents a cocycle rel A, and a a cycle rel A, then both terms vanish. When $p = q$ , the cap product is essentially just the evaluation pairing. More precisely,

$$
\langle 1 , \phi \frown a \rangle = \langle \phi , a \rangle .
$$

Theorem 26.3 (Poincar´e duality: general case). If M is an R-oriented n-manifold then the duality map

$$
D \colon H _ { c } ^ { p } ( M ; R ) \to H _ { n - p } ( M ; R ) ,
$$

is an isomorphism. Here D is defined as the direct limit of the maps

$$
D _ { K } \colon H ^ { p } ( M , M \setminus K ; R ) \to H _ { n - p } ( M ; R ) , \quad c \mapsto c \frown [ M _ { K } ] ,
$$

where $[ M _ { K } ] \in H _ { n } ( M , M \setminus K )$ is the fundamental class of M relative to K, and _ the relative cap product.

In the proof we shall need the observation that the inclusion $i \colon U \ \to \ M$ of an open subspace U induces a covariant homomorphism $i _ { * * } \colon H _ { c } ^ { p } ( U ) \to H _ { c } ^ { p } ( M )$ Indeed, if $K \subset U$ with K compact then excision gives an isomorphism

$$
H ^ { p } ( U , U \setminus K ) \cong H ^ { p } ( M , M \setminus K ) ,
$$

and these isomorphisms commute with the maps in the direct system. We define $i _ { * * }$ as the composite

$$
H _ { c } ^ { p } ( U ) = \operatorname* { l i m } _ { K \subset U } H ^ { p } ( U , U \setminus K ) \cong \operatorname* { l i m } _ { K \subset U } H ^ { p } ( M , M \setminus K )  H _ { c } ^ { p } ( M ) .
$$

Proof of the theorem. We drop the coefficients R from the notation. We shall prove that $D \colon H _ { c } ^ { p } ( U ) \ \to \ H _ { n - p } ( U )$ is an isomorphism for each open subset $D \subset M$ (including, eventually, M itself).

Step 1. The result holds when $U = \mathbb { R } ^ { n }$

Indeed, we saw above that $H _ { c } ^ { * } ( \mathbb { R } ^ { n } ) \cong R _ { ( n ) } \cong H _ { n - * } ( \mathbb { R } ^ { n } )$ . For any compact subset K, the cap product of a generator for $H ^ { \mathit { \hat { n } } } ( \mathbb { R } ^ { n } , \mathbb { R } ^ { n } \setminus K )$ by the fundamental class $\left[ \mathbb { R } _ { K } ^ { n } \right] \in H _ { n } ( \mathbb { R } ^ { n } , \mathbb { R } ^ { n } \setminus K )$ is (up to a sign) the point class in $H _ { 0 } ( \mathbb { R } ^ { n } )$ , because of the relation between relative cap product and the evaluation pairing. Passing to the direct limit, we find that D is an isomorphism in this case.

Step 2: If the result holds for U , V and $U \cap V$ then it holds for U ∪ V .

I claim that there is a covariant Mayer–Vietoris sequence in compactly supported cohomology, and that one has a commutative diagram with exact rows of which one portion reads

$$
\begin{array} { c c c c c c c } { { } } & { { } } & { { \begin{array} { c c c c c c } { { } } & { { } } & { { H _ { c } ^ { p } ( U ) \oplus H _ { c } ^ { p } ( V ) } } & { { \longrightarrow } } & { { H _ { c } ^ { p } ( U \cup V ) } } & { { \longrightarrow } } & { { H _ { c } ^ { p + 1 } ( U \cap V ) } } & { { \longrightarrow } } & { { } } \\ { { } } & { { } } & { { D \Big \downarrow } } & { { \qquad } } & { { \ D \Big \downarrow } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { \longmapsto H _ { n - p } ( U ) \oplus H _ { n - p } ( V ) } } & { { \longrightarrow } } & { { H _ { n - p } ( U \cup V ) } } & { { \longrightarrow } } & { { \large H _ { n - p - 1 } ( U \cap V ) } } & { { \longrightarrow } } \end{array} } } \end{array}
$$

Once this is verified, the 5-lemma assures us that D : $H _ { c } ^ { p } ( U \cup V )  H _ { n - p } ( U \cup V )$ is an isomorphism. The proof of this claim involves locality for chains (unsurprising since that underlies Mayer–Vietoris) and a good deal of checking, for which I refer to Hatcher.

Step 3: If the result holds for each $U _ { i }$ in a nested sequence $U _ { 1 } \subset U _ { 2 } \subset U _ { 3 } \subset o f$ open subspaces, then it holds for $V = \cup U _ { i }$

Any compact subset $K \subset V$ is contained in some $U _ { i }$ . The algebraic properties of direct limits give

$$
H _ { c } ^ { p } ( V ) = \varinjlim _ { i } \varinjlim _ { K \subset U _ { i } } H ^ { p } ( U _ { i } , U _ { i } \backslash K ) = \varinjlim _ { i } H _ { c } ^ { p } ( U _ { i } ) .
$$

But

$$
H _ { n - p } ( V ) = H _ { n - p } ( \bigcup U _ { i } ) = \varinjlim _ { i } H _ { n - p } ( U _ { i } ) ,
$$

because the singular chain complex of an expanding union is the direct limit of the singular chain complexes, and taking homology commutes with direct limits. Now D : $H _ { c } ^ { p } ( U _ { i } ) \to H _ { n - p } ( U _ { i } )$ is an isomorphism, and it commutes with the maps induced by inclusion of $U _ { i }$ in $U _ { i + 1 } ;$ hence $D = \underline { { { \operatorname* { l i m } } } } _ { i } ( D \colon H _ { c } ^ { p } ( V ) \to H _ { n - p } ( M ) )$ is an isomorphism.

Step 4: The result holds for open subsets $o f \mathbb { R } ^ { n }$

Every open set $U \subset \mathbb { R } ^ { n }$ is the union of a countable set of open balls. Hence U is the union of a nested family $U _ { 1 } \subset U _ { 2 } \subset U _ { 3 } \subset \ldots$ , where $U _ { 1 }$ is an open ball, and $U _ { i + 1 }$ is the union of $U _ { i }$ and a convex open set C homeomorphic to $\mathbb { R } ^ { n }$ . Note that $C \cap U _ { i }$ is convex, open, and has compact closure, and hence is homeomorphic to a ball. Thus the result holds for $U _ { i + 1 }$ by induction and steps 1 and 2.

Step 5: The result holds for M .

By Steps 1 and 4, and Zorn’s lemma, there is a non-empty, maximal open set O for which the result holds. If this weren’t all of M, we could take the union of O and a coordinate neighbourhood $U \cong \mathbb { R } ^ { n }$ , disjoint from $O ;$ the result would then hold for $O \cup U$ by steps 1 and 2. This contradicts maximality of $O$ 

Remark. There is an almost trivial proof of duality for compact smooth manifolds M in the context of Morse theory. The cellular chain complex can be understood in terms of critical points and gradient flows for a Morse function $f .$ . Replacing $f$ by −f does not change the homology (which is just $H _ { * } ( M ) )$ but it has the effect of dualizing the chain complex and changing degree ∗ to degree $n - *$ . Thus $H _ { * } ( M )$ is isomorphic to the cellular cohomology of M in degree $n - *$

Exercise 26.1: Let M be a compact, connected, oriented 3-manifold. Determine the graded ring $H ^ { * } ( M )$ when $( \mathfrak { i } ) \ \pi _ { 1 } ( M )$ is finite; (ii) $H _ { 1 } ( M ) \cong \mathbb { Z }$ ; (iii) $H _ { 1 } ( M ) \cong \mathbb { Z } ^ { 2 }$ Exhibit two such 3-manifolds with non-isomorphic cohomology rings, both of which have $H _ { 1 } \cong \mathbb { Z } ^ { 3 }$ .

Exercise 26.2: Show that the Euler characteristic of a compact, orientable, odd-dimensional manifold is zero.

Exercise 26.3: For which even dimensions 2n is it true that the Euler characteristic of a compact, connected, orientable 2n-manifold is necessarily even?

Exercise 26.4: Show that for every map $f \colon S ^ { 2 n } \to \mathbb { C } P ^ { n }$ , the induced map $\tilde { f } _ { * }$ on reduced homology is zero.