# INTRODUCTION TO ALGEBRAIC TOPOLOGY

## SI LI

ABSTRACT. To be continued. This is course note for Algebraic Topology in Spring 2018 at Tsinghua university.

Coure References:

(1) Hatcher: Algebraic Topology

(2) Bott and Tu: Differential forms in algebraic topology.

(3) May: A Concise Course in Algebraic Topology

(4) Spanier: Algebraic Topology.

## CONTENTS

1. Category and Functor mber 2   
2. Fundamental Groupoid 5   
3. Covering and fibration 7   
4. $\pi _ { 1 } ( S ^ { 1 } )$ and applications 9   
5. Classification of covering 11   
6. Seifert-van Kampen Theore 14   
7. Path space and homotopy fi 15   
8. Group object and homotopy group 19   
9. Exact Puppe sequence 21   
10. Cofibration 24   
11. CW complex 27   
12. Whitehead Theorem 29   
13. Cellular and CW approximations 32   
14. Eilenberg-MacLane Space 34   
15. Singular Homology 36   
16. Exact homology sequence 39   
17. Excision 41   
18. Homology of spheres 44   
19. Cellular homology 46   
20. Cohomology and Universal Coefficient Theorem 49   
21. Eilenberg-Zilber Theorem and Kunneth formula¨ 53   
22. Cup and Cap product 56   
23. Poincare duality ´ 60   
24. Intersection and Lefschetz Fixed Point Theorem 63   
25. Spectral sequence 65   
26. Obstruction theory 66   
27. The Theorem of Hurewicz 66   
28. Eilenberg-Steenrod Axioms 67

## 1. CATEGORY AND FUNCTOR

Category.

Definition 1.1. A category C consists of

(1) a class of objects: Obj(C)

(2) morphisms: a set Hom ${ \mathfrak { c } } ( A , B ) , \forall A , B \in \mathrm { O b j } ( { \mathcal { C } } )$ . An element $f \in { \mathrm { H o m } } ( A , B )$ will be denoted by

$$
A \ { \stackrel { f } { \to } } \ B \quad { \mathrm { o r } } \quad f : A \to B .
$$

(3) composition:

$$
\operatorname { H o m } ( A , B ) \times \operatorname { H o m } ( B , C ) \to \operatorname { H o m } ( A , C ) , \forall A , B , C \in \operatorname { O b j } ( { \mathcal { C } } )
$$

$$
f \times g \to g \circ f
$$

satisfying the following axioms

(1) associativity: h $\circ ( g \circ f ) = ( h \circ g ) \circ f$ for any $A \ { \stackrel { f } { \to } } \ B \ { \stackrel { g } { \to } } \ C \ { \stackrel { h } { \to } } \ D$

(2) identity: $\forall A \in \operatorname { O b j } ( { \mathcal { C } } ) , \exists 1 _ { A } \in \operatorname { H o m } ( A , A )$ called the identity element, such that

$$
f \circ 1 _ { A } = f = 1 _ { B } \circ f , \quad \forall A \stackrel { f } { \to } B .
$$

A category is called small if its objects form a set.

Definition 1.2. A morphism $f : A  B$ is called an equivalence/invertible if $\exists g : B  A$ such that

$$
f \circ g = 1 _ { B } , \quad g \circ f = 1 _ { A } .
$$

Two objects A, B are called equivalent if there exists an equivalence $f : A  B .$

Definition 1.3. A category where all morphisms are equivalences is called a groupoid.

Definition 1.4. A subcategory ${ \mathcal { C } } ^ { \prime } \subset { \mathcal { C } }$ is a category such that

$\operatorname { O b j } ( { \mathcal { C } } ^ { \prime } ) \subset \operatorname { O b j } ( { \mathcal { C } } )$

$\mathrm { H o m } _ { \mathscr { C } ^ { \prime } } ( A , B ) \subset \mathrm { H o m } _ { \mathscr { C } } ( A , B ) , \forall A , B \in \mathrm { O b j } ( \mathscr { C } ^ { \prime } )$

• composition coincides.

$\mathcal { C } ^ { \prime }$ is called a full subcategory of C if Hom $\mathfrak { r } ^ { \prime } ( A , B ) = \mathrm { H o m } _ { \mathscr { C } } ( A , B ) , \forall A , B \in \mathrm { O b j } ( \mathscr { C } ^ { \prime } )$

Definition 1.5. Let ∼ be an equivalence relation defined on each Hom $( A , B ) , A , B \in \mathrm { O b j } ( { \mathcal { C } } )$ satisfying

$$
f _ { 1 } \sim f _ { 2 } , g _ { 1 } \sim g _ { 2 } \Longrightarrow g _ { 1 } \circ f _ { 1 } \sim g _ { 2 } \circ f _ { 2 } .
$$

Then we define the quotient category $\mathcal { C } ^ { \prime } = \mathcal { C } / \sim \mathbf { b y }$

$\mathrm { O b j } ( { \mathcal { C } } ^ { \prime } ) = \mathrm { O b j } ( { \mathcal { C } } ^ { \prime } )$

${ \mathrm { H o m } } _ { { \mathscr { C } } ^ { \prime } } ( A , B ) = { \mathrm { H o m } } _ { { \mathscr { C } } } ( A , B ) / \sim , \forall A , B \in { \mathrm { O b j } } ( { \mathscr { C } } ^ { \prime } )$

Example 1.6. We will frequently use the following categories.

• Set: the category of set.

• Vect: the category of vector spaces.

• Group: the category of groups.

• Ab: the category of abelian groups.

• Ring: the category of rings.

Vect ⊂ Set is a subcategory, and $\underline { { \mathrm { A b } } } \subset \mathrm { G r o u p }$ is a full subcategory.

The main object of our interest is the category of topological spaces Top

• objects of Top are topological spaces.

• morphism $f : X \to Y$ is a continuous map.

Definition 1.7. Given $X , Y \in \mathrm { T o p } , f _ { 0 } , f _ { 1 } : X $ Y are said to to homotopic, denoted by $f _ { 0 } \simeq f _ { 1 } , \mathrm { i f }$

∃F : X × I → Y, such that F|X×0 = f0, F|X×1 = f1. I = [0, 1].

Homotopy defines an equivalence relation on Top. We denote its quotient category by

$$
\underline { { \mathrm { h T o p } } } = \underline { { \mathrm { T o p } } } / \simeq
$$

We also denote

$$
\operatorname { H o m } _ { \mathrm { h T o p } } ( X , Y ) = [ X , Y ] .
$$

Definition 1.8. Two topological spaces $X , Y$ are said to have the same homotopy type (or homotopy equivalent) if they are equivalent in hTop.

There is also a relative version as follows.

Definition 1.9. Let $A \subset X \in \mathrm { T o p } , f _ { 0 } , f _ { 1 } : X  Y$ such that $f _ { 0 } | _ { A } = f _ { 1 } | _ { A } : A \to Y .$ . We say $f _ { 0 }$ is homotopic to $f _ { 1 }$ relative to A, denoted by

$$
f _ { 0 } \simeq f _ { 1 } \mathrm { r e l } A
$$

if there exists $F : X \times I  Y$ such that

$$
\begin{array} { r } { F | _ { X \times 0 } = f _ { 0 } , \quad F | _ { X \times 1 } = f _ { 1 } , \quad F | _ { A \times t } = f _ { 0 } | _ { A } , \forall t \in I . } \end{array}
$$

Functor.

Definition 1.10. Let $\mathcal { C } , \mathcal { D }$ be two categories. A covariant functor (or contravariant functor) $F : { \mathcal { C } }  { \mathcal { D } }$ consists of

$$
\bullet \ F : \mathrm { O b j } ( { \mathcal { C } } ) \to \mathrm { O b j } ( { \mathcal { D } } ) , A \to F ( A )
$$

• Ho $\mathsf { n } _ { \mathcal { C } } ( A , B ) \to \mathrm { H o m } _ { \mathcal { D } } ( F ( A ) , F ( B ) ) , \forall A , B \in \mathrm { O b j } ( \mathcal { C } )$ . We denote by

$$
A \ { \stackrel { f } { \to } } \ B \Longrightarrow F ( A ) \ { \stackrel { F ( f ) } { \to } } \ F ( B )
$$

$$
{ \mathrm { ( o r ~ H o m } } _ { \mathcal { C } } ( A , B ) \to { \mathrm { H o m } } _ { \mathcal { D } } ( F ( B ) , F ( A ) ) , \forall A , B \in { \mathrm { O b j } } ( \mathcal { C } ) , { \mathrm { d e n o t e d } } { \mathrm { b y } } A \stackrel { f } { \to } B \Longrightarrow F ( B ) \stackrel { F ( f ) } { \to } F ( A ) )
$$

satisfying

$$
\begin{array} { r l } & { \bullet \ F ( g \circ f ) = F ( g ) \circ F ( f ) \ ( \mathrm { o r } \ F ( g \circ f ) = F ( f ) \circ F ( g ) ) \mathrm { f o r } \ \mathrm { a n y } \ A \stackrel { f } { \to } \ B \stackrel { g } { \to } \ C } \\ & { \bullet \ F ( 1 _ { A } ) = 1 _ { F ( A ) } , \forall A \in \mathrm { O b j } ( \mathscr { C } ) . } \end{array}
$$

F is called faithful (or full) if $\operatorname { H o m } _ { \mathcal { C } } ( A , B ) \to \operatorname { H o m } _ { \mathcal { D } } ( F ( A ) , F ( B ) )$ is injective (or surjective) $\forall A , B \in \mathrm { O b j } ( { \mathcal { C } } )$

Example 1.11. $\forall X \in \operatorname { O b j } ( { \mathcal { C } } )$

$$
\operatorname { H o m } ( X , - ) : { \mathcal { C } } \to \operatorname { S e t } , \quad A \to \operatorname { H o m } ( X , A )
$$

defines a covariant functor. Similarly $\mathrm { H o m } ( - , X )$ defines a contravariant functor. A functor $F : { \mathcal { C } } \to { \underline { { \operatorname { S e t } } } }$ of such type is called representable.

Example 1.12. Let G be an abelian group. Given X ∈ Top, we will study its n-th cohomology $\mathrm { H } ^ { n } ( X ; G )$ . It defines a functor

$$
\mathrm { H } ^ { n } ( - ; G ) : \mathrm { h T o p } \to \underline { { \mathrm { S e t } } } , \quad X \to \mathrm { H } ^ { n } ( X ; G )
$$

We will see that this functor is representable by the Eilenberg-Maclane space if we work with the subcategory of CW-complexes.

Example 1.13. We define a contravariant functor

$$
\mathrm { F u n } : \underline { { \mathrm { T o p } } } \to \underline { { \mathrm { R i n g } } } , \quad X \to \mathrm { F u n } ( X ) = \mathrm { H o m } ( X , \mathbb { R } )
$$

$\operatorname { F } ( X )$ are continuous real functions on X. A classical theorem of Gelfand-Kolmogoroff says that two compact Hausdorff spaces $X , Y$ are homeomorphic if and only i $\mathrm { \Delta } \mathrm { f } \operatorname { F u n } ( X ) , \operatorname { F u n } ( Y )$ are ring isomorphic.

Proposition 1.14. Let $F : { \mathcal { C } }  { \mathcal { D } }$ be a functor. f : $A  B$ is an equivalence. Then $F ( f ) : F ( A ) \to F ( B )$ is also an equivalence.

Natural transformation.

Definition 1.15. Let $\mathcal { C } , \mathcal { D }$ be two categories. $F , G : { \mathcal { C } } \to { \mathcal { D } }$ be two functors. A natural transformation $\tau : F  G$ consists of morphisms

$$
\tau = \{ \tau _ { A } : F ( A )  G ( A ) | \forall A \in \mathrm { O b j } ( { \mathcal { C } } ) \}
$$

such that the following diagram commutes for any $A , B \in \mathrm { O b j } ( { \mathcal { C } } )$

$$
\begin{array} { r l r } & { } & { F ( A ) \xrightarrow { F ( f ) } F ( B ) } \\ & { } & { \quad \downarrow \tau _ { A } } \\ & { } & { G ( A ) \xrightarrow { G ( f ) } G ( B ) } \end{array}
$$

τ is called natural equivalence if $\tau _ { A }$ is an equivalence for any $A \in { \mathrm { O b j } } ( { \mathcal { C } } )$ . We write $F \simeq G$

Definition 1.16. Two categories $\mathcal { C } , \mathcal { D }$ are called isomorphic if $\exists F : { \mathcal { C } }  { \mathcal { D } } , G : { \mathcal { D } }  { \mathcal { C } }$ such that $F \circ G =$ $1 _ { \mathcal { D } } , G \circ F = 1 _ { \mathcal { C } }$ . They are called equivalent if ∃F : $\mathcal { C }  \mathcal { D } , G : \mathcal { D }  \mathcal { C }$ such that $F \circ G \simeq 1 _ { \mathcal { D } } , G \circ F \simeq 1 _ { \mathcal { C } }$

Proposition 1.17. Let $F : { \mathcal { C } }  { \mathcal { D } }$ be an equivalence of categories. Then F is fully faithful.

Definition 1.18. Let C be a small category, and D be a category. We define the functor category $\mathrm { F u n } ( \mathcal { C } , \mathcal { D } )$

• objects: covariant functors from C to D

• morphism: natural transformations between two functors (which is indeed a set since C is small).

## 2. FUNDAMENTAL GROUPOID

Path connected component.

Definition 2.1. Let X ∈ Top. A map $\gamma : I  X$ is called a path from $\gamma ( 0 )$ to $\gamma ( 1 )$ . We denote $\gamma ^ { - 1 }$ be the path from γ(1) to γ(0) defined by $\gamma ^ { - 1 } ( t ) = \gamma ( 1 - t )$ . We denote $i _ { x _ { 0 } } : I \to X$ be the constant map to $x _ { 0 } \in X$

Let us introduce an equivalence relation on X by

$$
x _ { 0 } \sim x _ { 1 } \Longleftrightarrow \exists \mathrm { a } \mathrm { p a t h } \mathrm { f r o m } x _ { 0 } \mathrm { t o } x _ { 1 } .
$$

We denote the quotient space

$$
\pi _ { 0 } ( X ) = X / \sim
$$

which is the set of path connected components of X.

Proposition 2.2. $\pi _ { 0 } : \mathrm { h T o p } $ Set defines a covariant functor.

As a consequence, $\pi _ { 0 } ( X ) \cong \pi _ { 0 } ( Y )$ if $X , Y$ are homotopy equivalent.

Path category/fundamental groupoid.

Definition 2.3. Let $\gamma : I  X$ be a path. We define the path class of $\gamma$

$$
[ \gamma ] = \{ \tilde { \gamma } : I  X | \tilde { \gamma } \simeq \gamma \mathrm { r e l } \partial I = \{ 0 , 1 \} \}
$$

Definition 2.4. Let $\gamma _ { 1 } , \gamma _ { 2 } : I  X$ such that $\gamma _ { 1 } ( 1 ) = \gamma _ { 2 } ( 0 )$ . We define

$$
\gamma _ { 2 } \star \gamma _ { 1 } : I  X
$$

by

$$
\gamma _ { 2 } \star \gamma _ { 1 } ( t ) = { \left\{ \begin{array} { l l } { \gamma _ { 1 } ( 2 t ) } & { 0 \leq t \leq 1 / 2 } \\ { \gamma _ { 2 } ( 2 t - 1 ) } & { 1 / 2 \leq t \leq 1 . } \end{array} \right. }
$$

? is not associative for strict paths. However, ? defines an associative composition on path classes.

Theorem 2.5. Let $X \in$ Top. We define a category $\Pi _ { 1 } ( X )$ as follows:

$\operatorname { O b j } ( \Pi _ { 1 } ( X ) ) = X .$

$\mathrm { H o m } _ { \Pi _ { 1 } ( X ) } ( x _ { 0 } , x _ { 1 } )$ =path classes from $x _ { 0 }$ to $x _ { 1 }$

• $1 _ { x _ { 0 } } = i _ { x _ { 0 } } .$

Then $\Pi _ { 1 } ( X )$ defines a category which is in fact a groupoid. The inverse of [γ] is given by $[ \gamma ^ { - 1 } ] . \Pi _ { 1 } ( X )$ is called the fundamental groupoid of X.

Let C be a groupoid. Let $A \in { \mathrm { O b j } } ( { \mathcal { C } } )$ , then

$$
\operatorname { A u t } _ { \mathcal { C } } ( A ) : = \operatorname { H o m } _ { \mathcal { C } } ( A , A )
$$

forms a group. For any $f : A  B ,$ , it induces a group isomorphism

$$
A d _ { f } : \operatorname { A u t } _ { \mathcal { C } } ( A ) \to \operatorname { A u t } _ { \mathcal { C } } ( B )
$$

$$
g  f \circ g \circ f ^ { - 1 } .
$$

This naturally defines a functor

$$
{ \mathcal { C } } \to { \mathrm { G r o u p } }
$$

$$
A \to \operatorname { A u t } _ { \mathcal { C } } ( A )
$$

$$
f  A d _ { f }
$$

Specialize this to topological spaces, we find a functor

$$
{ \boxed { \Pi _ { 1 } ( X ) \to \underline { { \mathrm { G r o u p } } } } } .
$$

Definition 2.6. Let $x _ { 0 } \in X$ , the group

$$
\pi _ { 1 } ( X , x _ { 0 } ) : = \mathrm { A u t } _ { \Pi _ { 1 } ( X ) } ( x _ { 0 } )
$$

is called the fundamental group of the pointed space $( X , x _ { 0 } )$

Theorem 2.7. Let X be path connected. Then for $x _ { 0 } , x _ { 1 } \in X .$ , the have group isomorphism

$$
\pi _ { 1 } ( X , x _ { 0 } ) \cong \pi _ { 1 } ( X , x _ { 1 } ) .
$$

Let $f : X \to Y$ be a continuous map. It defines a functor

$$
\Pi _ { 1 } ( f ) : \Pi _ { 1 } ( X )  \Pi _ { 1 } ( Y )
$$

$$
x \to f ( x )
$$

$$
[ \gamma ]  [ f \circ \gamma ] .
$$

Then $\Pi _ { 1 }$ defines a functor

$$
\boxed { \Pi _ { 1 } : \underline { { \mathrm { T o p } } }  \underline { { \mathrm { G r o u p o i d } } } } , \quad X  \Pi _ { 1 } ( X )
$$

from the category Top to the category Groupoid of groupoids. Here morphisms in Groupoid are given by natural transformations.

Proposition 2.8. Let $f , g : X \to Y$ be maps which are homotopic by $F : X \times I  Y$ . Let us define path classes

$$
\tau _ { x _ { 0 } } = [ F | _ { x _ { 0 } \times I } ] \in \mathrm { H o m } _ { \Pi _ { 1 } ( Y ) } ( f ( x _ { 0 } ) , g ( x _ { 0 } ) ) .
$$

Then τ defines a natural transformation

$$
\tau : \Pi _ { 1 } ( f ) \Longrightarrow \Pi _ { 1 } ( g ) .
$$

This proposition can be pictured by the following diagram

$$
X \underbrace { \overset { f } { \underset { \left. F _ { f } \right. } { \downarrow } } } _ { g } Y \implies \Pi _ { 1 } ( X ) \underbrace { \overset { \Pi _ { 1 } ( f ) } { \underset { \left. \tau \right. } { \downarrow } } } _ { \Pi _ { 1 } ( g ) } \Pi _ { 1 } ( Y )
$$

The following theorem is a formal consequence of the above proposition

Theorem 2.9. Let $f : X \to Y$ be a homotopy equivalence. Then

$$
\Pi _ { 1 } ( f ) : \Pi _ { 1 } ( X )  \Pi _ { 1 } ( Y )
$$

is an equivalence of categories. In particular, it induces group isomorphisms

$$
\pi _ { 1 } ( X , x _ { 0 } ) \cong \pi _ { 1 } ( Y , f ( x _ { 0 } ) ) ,
$$

## 3. COVERING AND FIBRATION

Covering.

Definition 3.1. Let $p : E  B$ be continuous. A trivialization of p over an open $U \subset B$ is a homeomorphism $\varphi : p ^ { - 1 } ( U ) \to U \times F$ over U, i.e. , the following diagram commutes

<!-- image-->

p is called locally trivial if there exists an open cover U of B such that p has a trivialization over each open U ∈ U . Such p is also called a fiber bundle and F is called the fiber.

Definition 3.2. A covering is a locally trivial map $p : E  B$ with discrete fiber F.

Example 3.3. $e x : \mathbb { R } ^ { 1 } \to S ^ { 1 } , \quad t \to e ^ { 2 \pi i t }$ is a covering.

Definition 3.4. Let $p : E \to B , f : X \to B . \mathrm { A }$ lifting of f along p is a map $F : X  E$ such that $p \circ F = f$

<!-- image-->

Lemma 3.5. Let $p : E  B$ be a covering. Let

$$
D = \{ ( x , x ) \in E \times E | x \in E \}
$$

$$
Z = \{ ( x , y ) \in E \times E | p ( x ) = p ( y ) \} .
$$

Then $D \subset Z$ is open and closed.

Theorem 3.6 (Uniqueness of lifting). Let $p : E  B$ be a covering. Let $F _ { 0 } , F _ { 1 } : X \to E$ be two liftings of f .   
Suppose X is connected and $F _ { 0 } , F _ { 1 }$ agree somewhere. Then $F _ { 0 } = F _ { 1 }$ .

Proof. Consider the map $\tilde { F } = ( F _ { 0 } , F _ { 1 } ) : X \to Z . \ \tilde { F } ( X ) \cap D \neq \emptyset$ . The above lemma implies ${ \tilde { F } } ( X ) \subset D$



fibration.

Definition 3.7. A map $p : E  B$ is said to have the homotopy lifting property (HLP) with respect to X if for any maps $\tilde { f } : X \to E$ and $F : X \times I  B$ such that $p \circ \tilde { f } = F | _ { X \times 0 } ,$ , there exists a lifting F˜ of F along p such

that ${ \tilde { F } } | _ { X \times 0 } = { \tilde { f } } , { \mathrm { i . e . } }$ , the following diagram commutes

$$
\begin{array} { c } { { X \times 0 \xrightarrow [ ] { \tilde { f } } ~ } } \\ { { \mathrm { ~ } } } \\ { { \hat { V } \times \tilde { I } ~ } } \\ { { X \times \tilde { I } ~ \xrightarrow [ ] { \tilde { f } } ~ } } \end{array} \downarrow ^ { p }
$$

Definition 3.8. A map $p : E  B$ is called a fibration (or Hurewicz fibration) if $p$ has $\mathrm { H L P }$ for any space.

Theorem 3.9. A covering is a fibration .

Corollary 3.10. Let $p : E  B$ be a fibration. Then for any path γ : I → B and $e \in E$ such that $p ( e ) = \gamma ( 0 )$ , there exists a unique path $\tilde { \gamma } : I  E$ that lifts γ and $\tilde { \gamma } ( 0 ) = e$

Proof. Apply HLP to $X { \mathrm { = } } { \mathrm { p t } } .$

$$
\begin{array} { l } { 0 \xrightarrow { e } E } \\  \displaystyle \int _ { \begin{array} { c } { \gamma } \\ { \gamma } \\ { I } \end{array} } \tilde { \downarrow } \end{array} \begin{array} { l } { \left| p \right. } \\ { \left. \begin{array} { c } { \gamma } \\ { \gamma } \end{array} \right| } \end{array}
$$

Corollary 3.11. Let $p : E  B$ be a covering. Then $\Pi _ { 1 } ( E ) \to \Pi _ { 1 } ( B )$ is a faithful functor. In particular, the induced map $\pi _ { 1 } ( E , e ) \to \pi _ { 1 } ( B , p ( e ) )$ is injective.

Transport functor.

Let $p : E  B$ be a covering. Let $\gamma : I  B$ be a path in B from $b _ { 1 }$ to $b _ { 2 }$ . It defines a map

$$
\begin{array} { c } { { T _ { \gamma } : p ^ { - 1 } ( b _ { 1 } ) \to p ^ { - 1 } ( b _ { 2 } ) } } \\ { {       } } \end{array}
$$

where $\tilde { \gamma }$ is a lift of $\gamma$ with initial condition $\tilde { \gamma } ( 0 ) = e _ { 1 } .$ .

Assume $[ \gamma _ { 1 } ] = [ \gamma _ { 2 } ]$ in B. HLP implies that $T _ { \gamma _ { 1 } } = T _ { \gamma _ { 2 } }$ . We find a well-defined map

$$
\begin{array} { c } { { T : \mathrm { H o m } _ { \Pi _ { 1 } ( B ) } ( b _ { 1 } , b _ { 2 } )  \mathrm { H o m } _ { \underline { { { \mathrm { S e t } } } } } ( p ^ { - 1 } ( b _ { 1 } ) , p ^ { - 1 } ( b _ { 2 } ) ) } } \\ { { [ \gamma ]  T _ { [ \gamma ] } } } \end{array}
$$

Proposition 3.12. The following data

$$
\begin{array} { c } { { T : \Pi _ { 1 } \big ( B \big )  \underline { { { \mathrm { S e t } } } } } } \\ { { b  p ^ { - 1 } ( b ) } } \\ { { \lbrack \gamma \rbrack  T _ { [ \gamma ] } . } } \end{array}
$$

defines a functor, called the transport functor. In particular, we have a well-defined map

$$
\pi _ { 1 } ( B , b ) \to \mathrm { A u t } ( p ^ { - 1 } ( b ) ) .
$$

Proposition 3.13. Let $p : E  B$ be a covering, E path connected. Let $e \in E , b = p ( e ) \in B$ . Then the action of $\pi _ { 1 } ( B , b )$ on $p ^ { - 1 } ( b )$ is transitive, whose stabilizer at e is $\pi _ { 1 } ( E , e )$ . In other words,

$$
p ^ { - 1 } ( b ) \cong \pi _ { 1 } ( B , b ) / \pi _ { 1 } ( E , e )
$$

as a coset space.

Lifting Criterion.

Theorem 3.14 (Lifting Criterion). Let $p : E  B$ be a covering. $f : X \to B$ for X path connected and locally path connected. Let $e \in E , x _ { 0 } \in X$ such that $f ( x _ { 0 } ) = p ( e )$ . Then there exists a lift $F o f f$ with $F ( x _ { 0 } ) = e $ if and only if

$$
f _ { * } ( \pi _ { 1 } ( X , x _ { 0 } ) ) \subset p _ { * } ( \pi _ { 1 } ( E , e ) ) .
$$

Proof. If such F exists, $f _ { * } ( \pi _ { 1 } ( X , x _ { 0 } ) ) = p _ { * } F _ { * } ( \pi _ { 1 } ( X , x _ { 0 } ) ) \subset p _ { * } ( \pi _ { 1 } ( E , e ) )$ . Conversely, consider the product

<!-- image-->

Let $\tilde { e } = ( e , x _ { 0 } ) \in \tilde { E }$ . Then $\tilde { p }$ is a covering and we have a commuting diagram of functors

<!-- image-->

which induces a natural map

$$
\pi _ { 1 } ( X , x _ { 0 } ) \to \pi _ { 1 } ( B , b ) \to \operatorname { A u t } ( p ^ { - 1 } ( b ) ) .
$$

The condition $f _ { * } ( \pi _ { 1 } ( X , x _ { 0 } ) ) \subset p _ { * } ( \pi _ { 1 } ( E , e ) )$ says that $\pi _ { 1 } ( X , x _ { 0 } )$ stabilizes e˜. This implies

$$
\pi _ { 1 } ( { \tilde { E } } , { \tilde { e } } ) \cong \pi _ { 1 } ( X , x _ { 0 } ) .
$$

Since X is locally path connected, E˜ is also locally path connected. Then path connected components and connected components of E˜ coincide. Let X˜ be the (path) connected component of E˜ containing ${ \tilde { e } } ,$ then $\pi _ { 1 } ( { \tilde { E } } , { \tilde { e } } ) \cong \pi _ { 1 } ( X , x _ { 0 } )$ implies that ${ \tilde { p } } : { \tilde { X } } \to X$ is a covering with fiber a single point, hence a homeomorphism. Its inverse defines a continuous map $X  { \tilde { E } }$ whose composition with $\tilde { E }  E$ gives F. 

$$
4 . \ \pi _ { 1 } ( S ^ { 1 } ) \ \mathrm { A N D \ A P P L I C A T I O N S }
$$

G-principal covering.

Definition 4.1. Let G be a discrete group. An action $G \times X \to X$ is called properly discontinuous if $\forall x \in X , \exists$ open neighborhood U of x such that

$$
g ( U ) \cap U = \emptyset , \quad \forall g \neq 1 \in G .
$$

We define the orbit space $X / G$ by the quotient $X / \sim$ where x $\sim g ( x )$ for any $x \in X , g \in G$

Proposition 4.2. Assume G acts properly discontinuously on X, then the quotient map $X \to X / G$ is a covering.

Definition 4.3. A left (right) G-principal covering is a covering $p : E  B$ with a left (right) properly discontinuous G-action on E over B

<!-- image-->

such that the induced map $E / G \to B$ is a homeomorphism.

Example 4.4. $e x : \mathbb { R } ^ { 1 } \to S ^ { 1 }$ is a Z-principal covering for the action n : $t \to t + n , \forall n \in \mathbb { Z } .$

Example 4.5. $S ^ { n } \to \mathbb { R } P ^ { n } \cong S ^ { n } / \mathbb { Z } _ { 2 }$ is a Z2-principal covering.

Proposition 4.6. Let $p : E  B$ be a G-principal covering. Then transportation commutes with $G \mathrm { - } a c t i o n , i . e . ,$

$$
T _ { [ \gamma ] } \circ g = g \circ T _ { [ \gamma ] } , \quad \forall g \in G , \gamma a p a t h i n B .
$$

Theorem 4.7. Let $p : E  B$ be a G-principal covering, E path connected, $e \in E , b = p ( e )$ . Then we have an exact sequence of groups

$$
1 \to \pi _ { 1 } ( E , e ) \to \pi _ { 1 } ( B , b ) \to G \to 1 .
$$

In other words, $\pi _ { 1 } ( E , e )$ is a normal subgroup of $\pi _ { 1 } ( B , b )$ and $G = \pi _ { 1 } ( B , b ) / \pi _ { 1 } ( E , e )$

Proof. Let $F = p ^ { - 1 } ( b )$ . The previous proposition implies that $\pi _ { 1 } ( B , b )$ -action and G-action on F commute. It induces a $\pi _ { 1 } ( B , b ) \times G { \cdot } \mathrm { a c t i o n }$ on F. Consider its stabilizer at e and two projections

<!-- image-->

$p r _ { 1 }$ is an isomorphism and $p r _ { 2 }$ is an epimorphism with $\ker ( p r _ { 2 } ) = \mathrm { S t a b } _ { e } ( \pi _ { 1 } ( B , b ) ) = \pi _ { 1 } ( E , e )$

Apply this theorem to the covering ex : $\mathbb { R } ^ { 1 } \to S ^ { 1 } .$ , we find a group isomorphism

$$
\deg : \boxed { \pi _ { 1 } ( S ^ { 1 } ) \to \mathbb { Z } }
$$

which is called the degree map.

Applications.

Definition 4.8. i : $A \subset X$ be a subspace. A continuous map $r : X \to A$ is called a retraction if $r \circ i = 1 _ { A }$ . It is called a deformation retraction if furthermore $i \circ r \simeq 1 _ { X } .$ . We say A is a (deformation) retract of X if such a (deformation) retraction exists.

Proposition 4.9. $I f i : A \subset X$ is a retract, then $r _ { * } : \pi _ { 1 } ( A ) \to \pi _ { 1 } ( X )$ is injective.

Corollary 4.10. Let $D ^ { 2 }$ be the unit disk in $\mathbb { R } ^ { 2 }$ . Then its boundary $S ^ { 1 }$ is not a retract of $D ^ { 2 }$ .

Theorem 4.11 (Brouwer fixed point Theorem). Let $f : D ^ { 2 } \to D ^ { 2 }$ . Then there exists $x \in D ^ { 2 }$ such that $f ( x ) = x .$

Proof. Assume f has no fixed point. Let $l _ { x }$ be the ray starting from $f ( x )$ pointing toward x. Then

$$
D ^ { 2 } \to S ^ { 1 } , \quad x \to l _ { x } \cap \partial D ^ { 2 }
$$

is a retraction of $\partial D ^ { 2 } = S ^ { 1 } \subset D ^ { 2 }$ . Contradiction.

Theorem 4.12 (Fundamental Theorem of Algebra). Let $f ( x ) = x ^ { n } + c _ { 1 } x ^ { n - 1 } + \cdot \cdot \cdot + c _ { n }$ be a polynomial with $c _ { i } \in \mathbb { C } , n > 0$ . Then there exists $a \in \mathbb { C }$ such that $f ( a ) = 0 .$

Proof. Assume f has no root in C. Define a homotopy

$$
F : S ^ { 1 } \times I  S ^ { 1 } , \quad F ( e ^ { 2 \pi i \theta } , t ) = \frac { f ( \tan ( \frac { \pi t } { 2 } ) e ^ { 2 \pi i \theta } ) } { | f ( \tan ( \frac { \pi t } { 2 } ) e ^ { 2 \pi i \theta } ) | } .
$$

Then $\mathrm { d e g } ( F | _ { S ^ { 1 } \times 0 } ) = 0$ and deg $( F | _ { S ^ { 1 } \times 1 } ) = n$ . Contradiction.

Theorem 4.13 (Borsuk-Ulam). Let $f : S ^ { 2 } \to \mathbb { R } ^ { 2 }$ . Then $\exists x \in S ^ { 2 }$ such that $f ( x ) = f ( - x )$

Proof. Assume $f ( x ) \neq f ( - x ) , \forall x \in S ^ { 2 }$ . Define

$$
\rho : S ^ { 2 }  S ^ { 1 } , \quad \rho ( x ) = { \frac { f ( x ) - f ( - x ) } { | f ( x ) - f ( - x ) | } } .
$$

Let $D ^ { 2 }$ be the upper hemi-sphere of $S ^ { 2 }$ . It defines a homotopy between constant map and $\rho | _ { \partial D ^ { 2 } } : S ^ { 1 } \to S ^ { 1 } .$ , hence $\deg ( \rho | _ { \partial D ^ { 2 } } ) = 0$ . On the other hand, $\rho | _ { \partial D ^ { 2 } }$ is antipode-preserving: $\rho | _ { \partial D ^ { 2 } } ( - x ) = - \rho | _ { \partial D ^ { 2 } } ( x )$ , hence $\deg ( \rho | _ { \partial D ^ { 2 } } )$ is odd. Contradiction. 

Corollary 4.14 (Ham Sandwich Theorem). Let $A _ { 1 } , A _ { 2 }$ be two bounded regions of positive areas in $\mathbb { R } ^ { 2 }$ . Then there exists a line which cuts each $A _ { i }$ into half of equal areas.

Proof. Let $A _ { 1 } , A _ { 2 } \subset \mathbb { R } ^ { 2 } \times \{ 1 \} \subset \mathbb { R } ^ { 3 }$ . Given $u \in S ^ { 2 } .$ , let $P _ { u }$ be the plane passing the origin and perpendicular to the unit vector u. Let ${ A } _ { i } ( u ) = \{ p \in { A } _ { i } | p \cdot u \le 0 \}$ . Define the map

$$
f : S ^ { 2 } \to \mathbb { R } ^ { 2 } , \quad f _ { i } ( u ) = \operatorname { A r e a } ( A _ { i } ( u ) ) .
$$

By Borsuk-Ulam, ∃u such that $f ( u ) = f ( - u )$ . The intersection $\mathbb { R } ^ { 2 } \times \{ 1 \} \cap P _ { u }$ gives the required line.

## 5. CLASSIFICATION OF COVERING

Definition 5.1. The universal cover of B is a covering map $p : E  B$ with E simply connected.

Theorem 5.2. Assume B is path connected and locally path connected. Then universal cover of B exists if and only if B is semi-locally simply connected space.

Definition 5.3. We define the category $\operatorname { C o v } ( B )$ of coverings of B

• objects are covering maps

• a morphism between two coverings $p _ { 1 } : E _ { 1 } \to B$ and $p _ { 2 } : E _ { 2 } \to B$ is a map $f : E _ { 1 } \to E _ { 2 }$ such that the following diagram commutes

<!-- image-->

Definition 5.4. Let B be connected. We define $\operatorname { C o v } _ { 0 } ( B ) \subset \operatorname { C o v } ( B )$ to be the subcategory whose objects consist of coverings of B which are connected spaces.

Proposition 5.5. Let B be connected and locally path connected. Then any morphism in $C o v _ { 0 } ( B )$ is a covering map.

Definition 5.6. We define the orbit category ${ \mathrm { O r b } } ( G )$

• objects consist of (left) coset $G / H$ , where H is a subgroup of G

• morphisms are G-equivariant maps: $G / H _ { 1 } \to G / H _ { 2 }$

A morphism $\rho : G / H _ { 1 } \to G / H _ { 2 }$ is equivalent to an element $\gamma \in G$ such that $H _ { 1 } \subset \gamma H _ { 2 } \gamma ^ { - 1 }$ . Then

$$
\rho ( g H _ { 1 } ) = g \gamma H _ { 2 } .
$$

In particular. $G / H _ { 1 }$ and $G / H _ { 2 }$ are equivalent if and only if $H _ { 1 }$ and $H _ { 2 }$ are conjugate subgroups of G.

For convenience, we also introduce the following category

Definition 5.7. We define the category $G { \mathrm { - } } S \mathrm { e t }$

• objects consist of sets with G-action

• morphisms are G-equivariant set maps.

Given a covering $p : E \to B , b \in B$ , we find

$$
p ^ { - 1 } ( b ) \in \pi _ { 1 } ( B , b ) \ J { \cdot } \underline { { \mathrm { S e t . } } }
$$

Proposition 5.8. Assume B is path connected and locally path connected. Let $p _ { 1 } , p _ { 2 } \in C o v ( B )$ . Then

$$
\mathrm { H o m } _ { C o v ( B ) } ( p _ { 1 } , p _ { 2 } ) \cong \mathrm { H o m } _ { \pi _ { 1 } ( B , b )  } ( p _ { 1 } ^ { - 1 } ( b ) , p _ { 2 } ^ { - 1 } ( b ) )
$$

Proof. This is a consequence of Lifting Criterion and the Theorem of Uniqueness of lifting.

Definition 5.9. Let B be path connected and $p : E  B$ be a connected covering. deck transformation (or covering transformation) of p is a homeomorphism $f : E \to E$ such that $p \circ f = p .$ . Let $\operatorname { A u t } ( p )$ denote the group of deck transformation.

Note that $\operatorname { A u t } ( p )$ acts freely on E by the Uniqueness of Lifting.

Proposition 5.10. Let B be path connected and $p : E  B$ be a connected covering. Then $\operatorname { A u t } ( p )$ acts properly discontinuous on E.

We find that the universal cover E is a $\mathtt { . } \pi _ { 1 } ( B , b ) \mathtt { - p r i n c i p a l c o v e r i n g }$

Corollary 5.11. Assume B is path connected, locally path connected. Let $p : E  B$ be a connected covering, $e \in E , b = p ( e ) \in B , G = \pi _ { 1 } ( B , b ) , H = \pi _ { 1 } ( E , e )$ . Then

$$
\operatorname { A u t } ( p ) \cong N _ { G } ( H ) / H
$$

where $N _ { G } ( H )$ is the normalizer of H in G.

Proof. By the above proposition,

$$
\mathrm { A u t } ( p ) \cong \mathrm { H o m } _ { G \cdot \mathrm { S e t } } \bigl ( G / H , G / H \bigr ) = N _ { G } \bigl ( H \bigr ) / H .
$$

Theorem 5.12. Assume B is path connected, locally path connected and semi-locally simply connected. $b \in B$ . Then there exists an equivalence of categories

$$
\boxed { C o v ( B ) \simeq \pi _ { 1 } ( B , b ) { \ - } \underline { { \mathrm { S e t } } } } .
$$

Proof. Let us denote $\pi _ { 1 } = \pi _ { 1 } ( B , b )$ . Let $\tilde { p } : \tilde { B }  B$ be a fixed universal cover of B and $\tilde { b } \in \pi ^ { - 1 } ( b )$ chosen.

We define the following functors

$$
\operatorname { C o v } ( B ) \xrightarrow [ { G } ] { F } \pi _ { 1 } { \mathord { \cdot } } \underline { { \operatorname { S e t . } } }
$$

Let $p : E  B$ be a covering, we define

$$
F ( p ) = p ^ { - 1 } ( b ) .
$$

Let $S \in \pi _ { 1 }$ -Set, we define

$$
G ( S ) = \tilde { B } \times _ { \pi _ { 1 } } S = \tilde { B } \times S / \sim , \mathrm { ~ w h e r e ~ } ( e \cdot g , s ) \sim ( e , g \cdot s ) , \forall e \in \tilde { B } , s \in S , g \in \pi _ { 1 } .
$$

Here $e \cdot g$ represents the $( \mathrm { r i g h t } ) \pi _ { 1 }$ -action on ${ \tilde { B } } .$ Then we have natural equivalences

$$
F \circ G \overset { \eta } { \simeq } 1 , \quad G \circ F \overset { \tau } { \simeq } 1 .
$$

Here η is the natural equivalence

$$
\eta _ { S } \in \operatorname { H o m } _ { \pi _ { 1 } \ldots \operatorname { g e t } } ( F \circ G ( S ) , S ) , \quad \eta _ { S } ( e , s ) = g \cdot s \quad { \mathrm { i f ~ } } e = { \tilde { b } } \cdot g .
$$

τ is the natural equivalence

$$
\tau _ { E } \in \mathrm { H o m } _ { \mathsf { C o v } ( B ) } ( p ^ { \prime } , p ) \cong \mathrm { H o m } _ { \pi _ { 1 } \cdot \mathsf { S e t } } ( p ^ { - 1 } ( b ) , p ^ { - 1 } ( b ) ) , \quad p ^ { \prime } : \tilde { B } \times _ { \pi _ { 1 } } p ^ { - 1 } ( b ) \to B ,
$$

which is determined by the identity map in Hom $\mathsf { \iota } _ { \pi _ { 1 } - \mathrm { S e t } } ( p ^ { - 1 } ( b ) , p ^ { - 1 } ( b ) )$

If we restrict the above theorem to connected coverings, we find an equivalence of categories

$$
\boxed { \mathbf { C o v } _ { 0 } ( B ) \simeq \mathbf { O r b } ( \pi _ { 1 } ( B , b ) ) } .
$$

The universal cover $\tilde { B }  B$ corresponds to the orbit $\pi _ { 1 } ( B , b )$ . For the orbit $\pi _ { 1 } ( B , b ) / H ,$ it corresponds to

$$
E = \tilde { B } / H \to B .
$$

We have the following commuting diagram

<!-- image-->

A more intrinsic formulation is as follows. Given a covering $p : E \to B ,$ , we obtain a transport functor

$$
T _ { p } : \Pi _ { 1 } ( B ) \to \underline { { \mathsf { S e t } } } .
$$

Given a commuting diagram

<!-- image-->

we find a natural transformation

$$
\tau : T _ { p _ { 1 } } \Longrightarrow T _ { p _ { 2 } } , \quad \tau = \{ f : p _ { 1 } ^ { - 1 } ( b )  p _ { 2 } ^ { - 1 } ( b ) | b \in B \} .
$$

The above structure can be summerized by a functor

$$
\boxed { T : \mathrm { C o v } ( B ) \to \mathrm { F u n } ( \Pi _ { 1 } ( B ) , \underline { { \mathrm { S e t } } } ) }
$$

Theorem 5.13. Assume B is path connected, locally path connected and semi-locally simply connected. Then

$$
T : C o v ( B ) \to \operatorname { F u n } ( \Pi _ { 1 } ( B ) , \underline { { { \mathrm { S e t } } } } )
$$

is an equivalence of categories.

## 6. SEIFERT-VAN KAMPEN THEOREM

Product.

Definition 6.1. Let C be a category, $\{ A _ { \alpha } \} _ { \alpha \in I }$ be a set of objects in C. Their product is an object A in C together with $\pi _ { \alpha } : A \to A _ { \alpha }$ satisfying the following universal property: for any X in C and $f _ { \alpha } : X \to A _ { \alpha . }$ , there exists a unique morphism $f : X \to A$ such that the following diagram commutes

$$
\begin{array} { r } { X \_ - \_ - \times A } \\ { \hfill } \\ { f _ { \alpha } \backslash \_ \forall \pi } \\ { A _ { \alpha } } \end{array}
$$

The universal property implies that the product is unique up to equivalence if it exists. We denote it by

$$
\prod _ { \alpha \in I } A _ { \alpha } .
$$

Example 6.2.

• Let $S _ { \alpha } \in \underline { { \mathrm { S e t . } } } \prod S _ { \alpha } = \left\{ ( s _ { \alpha } ) | s _ { \alpha } \in S _ { \alpha } \right\}$ is the Cartesian product.

• Let $X _ { \alpha } \in \underline { { \mathrm { T o p . } } } \mathrm { \stackrel { \cdot } { I I } } X _ { \alpha }$ is the Cartesian product with induced product topology.

• Let $G _ { \alpha } \in \underbrace { \mathrm { G r o u p } } _ { \alpha } . \prod _ { \alpha } G _ { \alpha }$ is the Cartesian product with induced group structure.

Coproduct.

Definition 6.3. Let C be a category, $\{ A _ { \alpha } \} _ { \alpha \in I }$ be a set of objects in C. Their coproduct is an object A in C together with $i _ { \alpha } : A _ { \alpha } \to A$ satisfying the following universal property: for any X in C and $f _ { \alpha } : A _ { \alpha } \to X .$ , there exists a unique morphism $f : A \to X$ such that the following diagram commutes

<!-- image-->

The universal property implies that the product is unique up to equivalence if it exists. We denote it by

$$
\coprod _ { \alpha \in I } A _ { \alpha } .
$$

Example 6.4.

• Let $X _ { \alpha } \in$ Top. $\operatorname { I I } X _ { \alpha }$ is the disjoint union of topological spaces.

• Let $G _ { \alpha } \in \underline { { \mathrm { G r o u p . } } } \ \underline { { \mathrm { I } } } \ \mathrm { J } G _ { \alpha }$ is the free product of groups.

Pushout.

Definition 6.5. Let C be a category. Given $f _ { 1 } : A _ { 0 } \to A _ { 1 } , f _ { 2 } : A _ { 0 } \to A _ { 2 } .$ , their pushout is an object A together with $\pi _ { 1 } : A _ { 1 } \to A , \pi _ { 2 } : A _ { 2 } \to A$ such that

$\pi _ { 1 } \circ f _ { 1 } = \pi _ { 2 } \circ f _ { 2 }$

$p _ { i } : A _ { i } \to X$ in C such that $p _ { 1 } \circ f _ { 1 } = p _ { 2 } \circ f _ { 2 }$ , there exists a unique $F : A  X$ such that $p _ { i } = F \circ \pi _ { i }$

It can be described by the following diagram

<!-- image-->

The universal property implies that the pushout is unique up to equivalence if it exists. We denote it by

$$
A _ { 1 } \coprod _ { A _ { 0 } } A _ { 2 } .
$$

Example 6.6.

• Let $j _ { 1 } : X _ { 0 }  X _ { 1 } , j _ { 2 } : X _ { 0 }  X _ { 2 }$ in Top. Their pushout is the quotient of $X _ { 1 } \amalg X _ { 2 }$ by identifying $j _ { 1 } ( y ) \sim j _ { 2 } ( y ) , y \in X _ { 0 }$ . It glues $X _ { 1 } , X _ { 2 }$ along $X _ { 0 }$ using $j _ { 1 } , j _ { 2 }$

• Let $\rho _ { 1 } : H \to G _ { 1 } , \rho _ { 2 } : H \to G _ { 2 }$ in Group, then

$$
G _ { 1 } \coprod _ { H } G _ { 2 } = \big ( G _ { 1 } * G _ { 2 } \big ) / N
$$

where $G _ { 1 } * G _ { 2 }$ is the free product and N is the normal subgroup generated by $\rho _ { 1 } ( h ) \rho _ { 2 } ^ { - 1 } ( h ) , h \in H .$

Seifert-van Kampen Theorem.

Theorem 6.7 (Seifert-van Kampen Theorem, Groupoid version). Let $X = U \cup V$ where U, $V \subset X$ are open. Then the following diagram

$$
\begin{array} { r l } { \Pi ( U \cap V ) } & { { } \longrightarrow \Pi ( U ) } \\ { \bigcirc } & { { } \downharpoonright } & { { } } \\ { \Pi ( V ) } & { { } \xrightarrow { 7 \textsc { 9 } 1 1 } \sim \Pi ( X ) } \end{array}
$$

is a pushout in the category Groupoid.

Corollary 6.8 (Seifert-van Kampen Theorem). Let $X = U \cup V$ where $U , V \subset X$ are open and $U , V , U \cap V$ are path connected. Let $x _ { 0 } \in U \cap V .$ . Then the following diagram

$$
\begin{array} { c c } { { \pi _ { 1 } ( U \cap V , x _ { 0 } ) \longrightarrow \pi _ { 1 } ( U , x _ { 0 } ) } } \\ { { \downarrow } } \\ { { \pi ( V , x _ { 0 } ) ~ } } & { { > ~ \pi ( X , x _ { 0 } ) } } \end{array}
$$

is a pushout in the category Group.

## 7. PATH SPACE AND HOMOTOPY FIBER

Path space and loop space.

Definition 7.1. Let $X , Y \in { \mathrm { T o p } } .$ , we let $C ( X , Y ) \in$ Top denote the set of continuous maps from X to Y with the compact open topology. It is also denoted $Y ^ { X }$ . For $A \subset X , B \subset Y ,$ we denote the subspace

$$
C ( X , A ; Y , B ) = \{ f \in C ( X , Y ) | f ( A ) \subset B \} .
$$

Theorem 7.2 (Exponential Correspondence). Let Y be locally compact Hausdorff. Then the evaluation map $C ( Y , Z ) \times Y  Z$ is continuous and we have

$$
\mathrm { H o m } _ { \mathrm { T o p } } ( X \times Y , Z ) = \mathrm { H o m } _ { \mathrm { T o p } } ( X , C ( Y , Z ) ) .
$$

If furthermore X is Hausdorff, then

$$
C ( X \times Y , Z ) = C ( X , C ( Y , Z ) ) .
$$

Definition 7.3. Let $X \in \mathrm { T o p } ,$ we define

• free path space $P X = C ( I , X )$ and based path space $P _ { x } X = C ( I , 0 ; X , x ) ;$

• free loop space $\mathcal { L } X = C ( S ^ { 1 } , X )$ and based loop space $\Omega _ { x } X = C ( S ^ { 1 } , 1 ; X , x )$ or simply ΩX.

We denote the two maps

$$
\begin{array} { c } { { P X \xrightarrow { p _ { 1 } } \mathrm { ~ } } } \\ { { p _ { 0 } \Biggl \downarrow } } \\ { { X } } \end{array}
$$

where $p _ { 0 } ( \gamma ) = \gamma ( 0 )$ is the start point and $p _ { 1 } ( \gamma ) = \gamma ( 1 )$ is the end point of the path $\gamma .$ It induces

$$
p = ( p _ { 0 } , p _ { 1 } ) : P X  X \times X .
$$

Theorem 7.4. Let $X \in \mathrm { T o p }$

(1) $p : P X \to X \times X$ is a fibration.

(2) The map $p _ { 0 } : P X \to X$ is a fibration whose fiber at x is $P _ { x _ { 0 } } X .$

(3) The map $p _ { 1 } : P _ { x _ { 0 } } X \to X$ is a fibration whose fiber at $x _ { 0 } \ i s \ \Omega _ { x _ { 0 } } X .$

(4) $p _ { 0 } : P X \to X$ is homotopy equivalence. $P _ { x _ { 0 } } X$ is contractible.

Proof. (1) We need to prove the HLP of the diagram

<!-- image-->

Since I is locally compact Hausdorff, this is equivalent to the extension problem

$$
\begin{array} { c } { { Y \times \{ 0 \} \times I \cup Y \times I \times \partial I \xrightarrow [ ] { } \sum X } } \\ { { \downarrow \qquad } } \\ { { \quad Y \times I \times \bar { I } ^ { - \ddots } } } \end{array}
$$

which is easily solved by observing that $Y \times \{ 0 \} \times I \cup Y \times I \times \partial I$ is a deformation retract of $Y \times I \times I$

(2) follows from the composition of two fibrations

<!-- image-->

(3) follows from the pull-back diagram

<!-- image-->

(4) follows from retracting the path.

Definition 7.5. Let $f : X \to Y .$ . We define the mapping path space $P _ { f }$ by the pull-back diagram

<!-- image-->

An element of $P _ { f }$ is a pair $( x , \gamma )$ where $\gamma$ is a path in Y that ends at $f ( x )$

Let $\iota : X \hookrightarrow P _ { f }$ represent the constant paths and $q _ { 0 } : P _ { f } \to Y$ be the start point of the path. We have

<!-- image-->

Theorem 7.6. $\iota : X \to P _ { f }$ is strong deformation retract (hence homotopy equivalence) and $q _ { 0 } : P _ { f } \to Y$ is a fibration.   
In particular, any map $f : X \to Y$ is a composition of a homotopy equivalence with a fibration.

Proof. The pull-back diagram

<!-- image-->

implies that $P _ { f } \to Y \times X$ is a fibration. Since $Y \times X \to Y$ is also a fibration, its composition $q _ { 1 }$ is a fibration. 

This theorem says that in hTop, every map is equivalent to a fibration.

Fiber homotopy.

Definition 7.7. Let $p _ { 1 } : E _ { 1 } \to B$ and $p _ { 2 } : E _ { 2 } \to B$ be two fibrations. A fiber map from $p _ { 1 }$ to $p _ { 2 }$ is a map $f : E _ { 1 } \to E _ { 2 }$ such that $p _ { 1 } = p _ { 2 } \circ f \colon$

<!-- image-->

Two fiber maps $f _ { 0 } , f _ { 1 } : p _ { 1 } \to p _ { 2 }$ are said to be fiber homotopic

$$
f _ { 0 } \simeq _ { B } f _ { 1 }
$$

if there exists a homotopy $F : E _ { 1 } \times I \to E _ { 2 }$ from $f _ { 0 }$ to $f _ { 1 }$ such that $F ( - , t )$ is a fiber map for each $t \in I .$ $f : p _ { 1 } \to p _ { 2 }$ is a fiber homotopic equivalence if there exists $g : p _ { 2 }  p _ { 1 }$ such that both $f \circ g$ and $g \circ f$ are fiber homotopic to identity maps.

Proposition 7.8. Let $p _ { 1 } : E _ { 1 }  B$ and $p _ { 2 } : E _ { 2 }  B$ be two fibrations and $f : E _ { 1 } \to E _ { 2 }$ be a fiber map. Assume $f : E _ { 1 } \to E _ { 2 }$ is a homotopy equivalence, then $f$ is a fiber homotopy equivalence. In particular, $f : p _ { 1 } ^ { - 1 } ( b ) \to p _ { 2 } ^ { - 1 } ( b )$ is a homotopy equivalence for any $b \in B$

Proof. We only need to prove that for any fiber map $f : E _ { 1 } \to E _ { 2 }$ which is a homotopy equivalence, there is a fiber map $g : E _ { 2 }  E _ { 1 }$ such that $g \circ f \simeq _ { B }$ 1. In fact, such a $\boldsymbol { g }$ is also a homotopy equivalence and we can find h : $E _ { 1 } \to E _ { 2 }$ such that h $\circ g \simeq _ { B } 1$ . Then $f \simeq _ { B } h \circ g \circ f \simeq _ { B } h ,$ , which implies $f \circ g \simeq _ { B } .$ 1 as well.

Let $g : E _ { 2 }  E _ { 1 }$ be a homotopy inverse of $f ,$ so $g = f ^ { - 1 }$ in hTop. We first show that we can choose a homotopy class of $g$ such that $g$ is a fiber map. In fact, consider the diagram

$$
\begin{array}{c} \begin{array}{c} E _ { 2 } \underbrace { \overbrace { \underbrace { \mathcal { H } _ { 1 0 } g } _ { \begin{array} { c } { | \Psi _ { 2 } | } | } ^ { g } } \end{array} } _ { \begin{array} { c } { | \Psi _ { 2 } | } \end{array} } \underbrace { \overbrace { \mathbf { \Psi } ^ { * } | } ^ { g } } \end{array}  _ { \begin{array} { c } { | \Psi _ { 2 } | } \end{array} } \end{array}
$$

Since $g \circ p _ { 1 } = g \circ f \circ p _ { 2 }$ is homotopic to $p _ { 2 }$ and $p _ { 1 }$ is a fibration, we can lift the above homotopy to a homotopy from g to $g ^ { \prime } : E _ { 2 } \to E _ { 1 }$ which lifts $p _ { 2 }$ . Then $g ^ { \prime }$ is a fiber map as required.

We further reduce the problem to prove the following

“Claim”: Let $p : E  B$ be a fibration and $f : E  E$ is a fiber map that is homotopic to ${ 1 } _ { E } ,$ then there is a fiber map $h : E \to E$ such that h ◦ $f \simeq _ { B } 1$ .

In fact, let $f : E _ { 1 } \to E _ { 2 }$ as in the proposition, $g : E _ { 2 } \to E _ { 1 }$ be a fiber map such that $g \circ f \simeq 1$ as chosen above. The “Claim” implies that we can find a fiber map $h : E _ { 1 } \to E _ { 1 }$ such that $h \circ g \circ f \simeq _ { B } 1$ . The the fiber map $\tilde { g } = h \circ g$ has the required property that $\tilde { g } \circ f \simeq _ { B } 1$

Now we prove the “Claim”. Let F be a homotopy from $f$ to $1 _ { E }$ and $G = p \circ F$ . Since $p$ is fibration, we can construct a homotopy H that starts from $1 _ { E }$ and lifts G. Here is the picture

<!-- image-->

Combining these two homotopy we find a homotopy $\tilde { F }$ from $h \circ f$ to $1 _ { E }$ that lifts the following homotopy

$$
\tilde { G } : E \times I \to B , \quad \tilde { G } ( - , t ) = \left\{ \begin{array} { l l } { G ( - . 2 t ) } & { 0 \leq t \leq 1 / 2 } \\ { G ( - , 2 - 2 t ) } & { 1 / 2 \leq t \leq 1 } \end{array} \right.
$$

Here is the picture

$$
\begin{array} { r l } & { E \overbrace { \underbrace { \left. \tilde { F } \right. } _ { \begin{array} { l } { 1 } \\ { \frac { p } { p } } \\ { \sqrt { \tilde { \mathscr { H } } } } \end{array} } } ^ { h o f } \underbrace { F } _ { \begin{array} { l } { p } \\ { p } \end{array} } } \\ & { E \overbrace { \underbrace { \left. \tilde { G } \right. } _ { p } } ^ { H o f } \ \underbrace { \mathrm { ~ B } } _ { \begin{array} { l } { p } \end{array} } } \end{array}
$$

It is easy to see that we can construct a homotopy $K : E \times I \times I $ B such that

$$
K ( - , u , 0 ) = \tilde { G } ( - , u ) , \quad K ( - , u , 1 ) = p ( - ) = K ( - , 0 , t ) = K ( - , 1 , t ) , \quad \forall u , t \in I .
$$

Since p is a fibration, we can find a lift $\tilde { K } : E \times I \times I \to E$ of K such that

$$
\tilde { K } ( - , u , 0 ) = \tilde { F } ( - , u ) .
$$

Then we have the following fiber homotopy

$$
h \circ f = \tilde { K } ( - , 0 , 0 ) \simeq _ { B } \tilde { K } ( - , 0 , 1 ) \simeq _ { B } \tilde { K } ( - , 1 , 1 ) \simeq _ { B } \tilde { K } ( - , 1 , 0 ) = 1 _ { E } .
$$

Homotopy fiber.

Definition 7.9. Let $f : X \to Y ,$ , we define its homotopy fiber over $y \in Y$ to be the fiber of $P _ { f } \to Y$ over y.

If Y is path connected, then all homotopy fibers are homotopic equivalent since $P _ { f } \to Y$ is a fibration. In this case we will usually write the following diagram

$$
\begin{array}{c} \begin{array} { c c c } { F \longrightarrow X } \\ { } & { } & { \begin{array} { r l } { \end{array} } \\ { \bigtriangledown _ { f } } \end{array} } \end{array}
$$

where F denotes the homotopy fiber.

Proposition 7.10. $I f f : X \to Y$ is a fibration, then its homotopy fiber at y is homotopy equivalent to $f ^ { - 1 } ( y )$

Proof. We have

<!-- image-->

where ι is a homotopy equivalence. Then ι is fiber homotopy equivalence.

## 8. GROUP OBJECT AND HOMOTOPY GROUP

Definition 8.1. We define the category Top of pointed topological space where

• An object $( X , x _ { 0 } )$ is a topological space X with a based point $x _ { 0 } \in X$

• morphisms are based continuous maps that map based point to based point.

Definition 8.2. Let $X , Y \in \mathsf { T o p } .$ be two pointed spaces. A based homotopy between two based maps $f _ { 0 } , f _ { 1 } : X \to Y$ is a homotopy between $f _ { 0 } , f _ { 1 }$ relative to the base points. We denote $[ X , Y ] _ { 0 }$ to be based homotopy classes of based maps. We define the category hTop by the quotient of Top where

$$
{ \mathrm { H o m } } _ { \underline { { \mathrm { h T o p } } } _ { * } } ( X , Y ) = [ X , Y ] _ { 0 } .
$$

The loop space defines a functor

$$
\Omega : \underline { { \mathrm { T o p } } } _ { * } \to \underline { { \mathrm { T o p } } } _ { * } , \quad X \to \Omega X
$$

where ΩX is based at the constant loop to the base point of X. It is easy to see that it also defines

$$
\Omega : \underline { { \mathrm { h T o p } } } _ { * } \to \underline { { \mathrm { h T o p } } } _ { * } .
$$

Definition 8.3. Let C be a category with finite product and terminal object ?. A group object in C is an object G in C together with morphisms

$$
\mu : G \times G \to G , \quad \eta : G \to G , \quad \epsilon : \star \to G
$$

such that the following diagrams commute

(1) associativity:

<!-- image-->

(2) unit:

<!-- image-->

(3) inverse

<!-- image-->

µ is called the multiplication, η is called the inverse, e is called the unit.

Example 8.4.

• Group objects in Set are groups.

• Group objects in Top are topological groups.

• Group objects in hTop are called H-groups.

Proposition 8.5. Let C be a category with finite product and terminal object. Let G be a group object. Then

$$
{ \mathrm { H o m } } ( - , G ) : { \mathcal { C } } \to { \underline { { \mathrm { G r o u p } } } }
$$

defines a contravariant functor from C to Group.

In the category Top and hTop , product exists and is given by

$$
( X , x _ { 0 } ) \times ( Y , y _ { 0 } ) = ( X \times Y , x _ { 0 } \times y _ { 0 } ) .
$$

Initial objects and terminal objects are a single pointed space.

Theorem 8.6. Let $X \in \mathrm { T o p } _ { * }$ . Then ΩX is a group object in hTop .

Corollary 8.7. For any X, Y ∈ Top , [Y, ΩX]0 forms a group.

Definition 8.8. Let $( X , x _ { 0 } ) \in \mathrm { T o p } ,$ . We define its suspension ΣX by the quotient of $X \times I$

$$
\boxed { \Sigma X = X \times I / X \times \partial I \cup x _ { 0 } \times I } .
$$

It defines functors

$$
\Sigma : \underline { { \mathrm { T o p } } } _ { * } \to \underline { { \mathrm { T o p } } } _ { * } , \quad \underline { { \mathrm { h T o p } } } _ { * } \to \underline { { \mathrm { h T o p } } } _ { * } .
$$Example 8.9. $\Sigma S ^ { n } \cong S ^ { n + 1 }$ are homeomorphic for any $n \geq 0 .$

Definition 8.10. Let $F : { \mathcal { C } }  { \mathcal { D } }$ and $G : { \mathcal { D } }  { \mathcal { C } }$ be two functors. $( F , G )$ is called adjoint pair if there are isomorphisms

$$
\tau : \mathrm { H o m } _ { \mathcal { D } } ( F X , Y ) \cong \mathrm { H o m } _ { \mathcal { C } } ( X , G Y ) , \quad \forall X \in \mathcal { C } , Y \in \mathcal { D }
$$

which are natural for all $X , Y .$ . In other words, τ defines a natural equivalence between two functors

$$
{ \mathrm { H o m } } _ { \mathcal { D } } ( F - , - ) , { \mathrm { H o m } } _ { \mathcal { C } } ( - , G - ) : \mathcal { C } ^ { o p } \times \mathcal { D } \to \underline { { \mathrm { S e t } } } .
$$

F (G) is called the left (right) adjoint of G (F), denoted by $F  G$

Example 8.11. Let Y be locally compat Hausdorff, then $- \times Y$ is left adjoint to $C ( Y , - )$

Proposition 8.12. (Σ, Ω) is an adjoint pair in Top\* and hTop\*.

Definition 8.13. Let $( X , x _ { 0 } ) \in \mathrm { T o p } ,$ . We define the n-th homotopy group

$$
{ \sqrt { \pi _ { n } ( X , x _ { 0 } ) = [ S ^ { n } , X ] _ { 0 } \left[ \right]} }   .
$$

Sometimes we simply denote it by $\pi _ { n } ( X )$

For $n \geq 1 .$ , we know that

$$
\pi _ { n } ( X ) = [ \Sigma S ^ { n - 1 } , X ] _ { 0 } = [ S ^ { n - 1 } , \Omega X ]
$$

which is a group since ΩX is a group object.

Proposition 8.14. $\pi _ { n } ( X )$ is abelian $i f n \geq 2 .$

Proposition 8.15. Let X be path connected. There is a natural functor

$$
T : \Pi _ { 1 } ( X ) \to { \mathrm { G r o u p } }
$$

which sends $x _ { 0 }$ to $\pi _ { n } ( X , x _ { 0 } )$ . In particular, there is a natural action of $\pi _ { 1 } ( X , x _ { 0 } )$ on $\pi _ { n } ( X , x _ { 0 } )$ and all $\pi _ { n } ( X , x _ { 0 } ) ^ { \prime } s$ are isomorphic for different choices of x0.

Proposition 8.16. Let $f : X \to Y$ be homotopy equivalence. Then

$$
f _ { * } : \pi _ { n } ( X , x _ { 0 } ) \to \pi _ { n } ( Y , f ( x _ { 0 } ) )
$$

is a group isomorphism.

## 9. EXACT PUPPE SEQUENCE

Definition 9.1. A sequence of maps of sets with base points

$$
( A , a _ { 0 } ) \stackrel { f }  ( B , b _ { 0 } ) \stackrel { g }  ( C , c _ { 0 } )
$$

is said to be exact at $B \operatorname { i f } \operatorname { i m } ( f ) = \ker ( g )$ where im $( f ) = f ( A ) , \ker ( g ) = g ^ { - 1 } ( c _ { 0 } )$ . A sequence

$$
\cdot \cdot \cdot  A _ { n + 1 }  A _ { n }  A _ { n - 1 }  \cdot \cdot \cdot
$$

is called an exact sequence if it is exact at every $A _ { i }$

Definition 9.2. A sequence of maps in hTop

$$
\cdot \cdot \cdot \to X _ { n + 1 } \to X _ { n } \to X _ { n - 1 } \to \cdot \cdot \cdot
$$

is called exact if for any $Y \in \mathrm { h T o p } _ { * }$ , the following sequence of pointed sets is exact

$$
\begin{array} { r } { \cdots \to [ Y , X _ { n + 1 } ] _ { 0 } \to [ Y , X _ { n } ] _ { 0 } \to [ Y , X _ { n - 1 } ] _ { 0 } \to \cdot \cdot \cdot } \end{array}
$$

Definition 9.3. Let $f : ( X , x _ { 0 } ) \to ( Y , y _ { 0 } )$ be a map in Top . We define its homotopy fiber $F _ { f }$ in $\underline { { \mathrm { h T o p , } } }$ by the pull-back diagram

$$
\begin{array} { r l r } & { F _ { f } \longmapsto \neg P _ { y _ { 0 } } Y \qquad } & { F _ { f } = \{ ( x , \gamma ) \in X \times P Y | \gamma ( 0 ) = y _ { 0 } , \gamma ( 1 ) = f ( x ) \} } \\ & { \pi \Big \downarrow } & { \qquad \downarrow p _ { 1 } } \\ & { V \qquad f \quad \qquad e } & { } \end{array}
$$

Note that $F _ { f }$ is precisely the fiber of $P _ { f } \to Y$ over y0. We have the following commutative diagram

<!-- image-->

When f is a fibration, ι is a fiber homotopy equivalence, hence $f ^ { - 1 } ( y _ { 0 } ) \to F _ { f }$ is a homotopy equivalence.

Lemma 9.4. The sequence

$$
F _ { f } \stackrel { \pi } { \to } X \stackrel { f } { \to } Y
$$

is exact at X in hTop .

Proof. We first observe that f ◦ π factors through $P _ { y _ { 0 } } Y$ which is contractible. Therefore f ◦ π is null homotopy. Let $Z \in { \mathrm { h T o p } } ,$ . Consider

$$
[ Z , F _ { f } ] _ { 0 } \stackrel { \pi _ { * } } {  } [ Z , X ] _ { 0 } \stackrel { f _ { * } } {  } [ Z , Y ] _ { 0 } .
$$

Since $f \circ \pi$ is null homotopic, we have im $\pi _ { * } \subset$ ker f∗.

Let $g : Z \to X$ such that $[ g ] _ { 0 } \in$ ker $f _ { * }$ . Let G be a homotopy of $f \circ g$ to the trivial map. G defines a lifting

<!-- image-->

By the definition of pull-back, the pair $( G , g )$ defines a map to $F _ { f }$ such that the following diagram commutes

<!-- image-->

This implies $[ g ] _ { 0 } \in$ im $\pi _ { * }$ . Therefore ker $f _ { * } \subset \mathrm { i m } \pi _ { * }$

The fiber of $F _ { f }$ over x0 is precisely ΩY. We find the following sequence of pointed maps

$$
\Omega X \stackrel { \Omega f } { \to } \Omega Y \to F _ { f } \stackrel { \pi } { \to } X \stackrel { f } { \to } Y .
$$

Lemma 9.5. The sequence ΩX ${ \stackrel { \Omega f } { \to } } \Omega Y \to F _ { f } { \stackrel { \pi } { \to } } X { \stackrel { f } { \to } } Y$ is exact in $\mathrm { h T o p } { \mathrm { , } }$ \* •

Proof. We construct the following diagram in hTop with all vertical arrows homotopy equivalences

<!-- image-->

Since $F _ { f } { \overset { \pi } { \to } } X$ is a fibration with fiber ΩY, we have a commutative diagram

<!-- image-->

where j is a homotopy equivalence. This explains the second square above.

Similarly, the fiber of the fibration $F _ { \pi } \to F _ { f }$ is ΩX. We find the following diagram

<!-- image-->

$F _ { \pi ^ { \prime } }$ is the homotopy fiber, and j0 is homotopy equivalence as before. However, the following diagram

<!-- image-->

is NOT commutative in Top

However, it is easy to see that $j \circ \Omega f$ is homotopic to k, so this diagram is commutative in hTop . Therefore

<!-- image-->

is commutative in hTop .

The lemma follows from the above commutative diagram in hTop and that ${ \mathrm { \Sigma } } _ { j , j ^ { \prime } } \mathrm { \Sigma }$ are homotopy equivalence.

Lemma 9.6. Let $X _ { 1 }  X _ { 2 }  X _ { 3 }$ be exact in hTop , then so is $\Omega X _ { 1 }  \Omega X _ { 2 }  \Omega X _ { 3 }$

Proof. Use the fact that Ω is right adjoint to the suspension Σ.

The following Theorem is a direct consequence of the above Lemmas.

Theorem 9.7 (Exact Puppe Sequence). Let $f : X \to Y$ in Top . Then the following sequence in exact in hTop

$$
\cdot \cdot \cdot \to \Omega ^ { 2 } Y \to \Omega F _ { f } \to \Omega X \to \Omega Y \to F _ { f } \to X \to Y .
$$

Theorem 9.8. Let $\pi : E  B$ be a map in Top . Assume π is fibration whose fiber over the base point is F. Then we have the following exact sequence of homotopy groups

$$
\cdots \to \pi _ { n } ( F ) \to \pi _ { n } ( E ) \to \pi _ { n } ( B ) \to \pi _ { n - 1 } ( F ) \to \cdots \to \pi _ { 0 } ( E ) \to \pi _ { 0 } ( B )
$$

where all homotopy groups are understood to have based points on the relevant spaces.

Proof. Since π is a fibration, F is homotopy equivalent to Fπ. Apply $\left[ S ^ { 0 } , - \right]$ to the Puppe Sequence.

The following proposition gives a criterion for fibration

Theorem 9.9. Let $p : E  B$ with B paracompact Hausdorff. Assume there exists an open cover $\{ U _ { \alpha } \}$ of B such that $p ^ { - 1 } ( U _ { \alpha } ) \to U _ { \alpha }$ is a fibration. Then p is a fibration.

Corollary 9.10. Let $p : E  B$ be a fiber bundle with B paracompact Hausdorff. Then p is a fibration.

Proposition 9.11. $I f i < n ,$ , then $\pi _ { i } ( S ^ { n } ) = 0$

Example 9.12. We have the Hopf fibration $S ^ { 3 } \to S ^ { 2 }$ with fiber $S ^ { 1 }$ . Its associated exact sequence of homotopy groups implies

$$
\pi _ { 2 } ( S ^ { 2 } ) \cong \mathbb { Z } , \quad \pi _ { n } ( S ^ { 3 } ) \cong \pi _ { n } ( S ^ { 2 } ) { \mathrm { ~ f o r ~ } } n \geq 3 .
$$

10. COFIBRATION

Cofibration.

Definition 10.1. A map $i : A \to X$ is said to have the homotopy extension property (HEP) with respect to Y if for any maps $f : X \to Y$ and $F : A  Y ^ { I }$ such that $p _ { 0 } \circ F = f \circ i ,$ there exists a map $\tilde { F } : X \to Y ^ { I }$ such that the following diagram commutes

$$
\begin{array} { r }  Y \prec \overbrace { \sum _ { \begin{array} { l } { p _ { 0 } } \\ { \sum _ { \begin{array} { l } { \ell } \end{array} } \int _ { \ell } \boldsymbol { i } } \\ { Y ^ { I } \prec \overbrace { \boldsymbol { \Omega } _ { \begin{array} { l } { \ell } \end{array} } \int _ { \ell } \boldsymbol { i } } \end{array} } } ^ { f } X } \end{array}
$$

Definition 10.2. A map $i : A \to$ X is called a cofibration if it has HEP for any spaces.

The notion of cofibration is dual to that of the fibration. Fibration is defined by the HLP of the diagram

$$
\begin{array} { r } { Y \frac { \tilde { f } } { \sum \limits _ { j = \tilde { F } _ { \tilde { f } } < \tilde { f } _ { e } \atop \tilde { Y } \times I _ { \tilde { f } } } \sum _ { j = \tilde { B } _ { \tilde { f } } } E } } \\ { Y \times I \frac { \tilde { f } } { \mathrm { ~ \it ~ F ~ } } > B } \end{array}
$$

If we reverse the arrows and observe that $Y \times I$ is dual to the path space $Y ^ { I }$ via the adjointness of $( - ) \times I$ and $( - ) ^ { I } .$ , we arrive at HEP.

Definition 10.3. Let $f : A  X .$ . We define its mapping cylinder $M _ { f }$ by the push-out

<!-- image-->

The HEP of i : $A  X$ is equivalent to the property of filling the commutative diagram

<!-- image-->

It is enough to consider $Y = M _ { i }$ to check cofibration by the universal property of push-out. .

Proposition 10.4. Let $i : A \to X$ and $j : M _ { i } \to X \times I$ be the above map. Then i is a cofibration if and only there exists $r : X \times I \to M _ { i }$ such that $r \circ j = 1 _ { M _ { i } }$

Proposition 10.5. Let $i : A \to X$ be a cofibration. Then i is a homeomorphism to its image (i.e. embedding). If furthermore X is Hausdorff. Then i has closed image (i.e. closed embedding).

Proof. Use the retraction in the previous proposition

<!-- image-->

Lemma 10.6. Let A be a closed subspace of X. Then the inclusion map $i : A \subset X$ is a cofibration if and only if $X \times \{ 0 \} \cup A \times I$ is a retract of $X \times I .$

Proof. If i is closed embedding, then $M _ { i }$ is homeomorphic to the subspace $X \times \{ 0 \} \cup A \times I \mathrm { o f } X \times I .$

Remark 10.7. This lemma still holds if we only assume A is a subspace without closeness condition. It can be shown that if $X \times \{ 0 \} \cup A \times I$ is a retract of $X \times I ,$ then $M _ { i }$ is again homeomorphic to the subspace $X \times \{ 0 \} \cup A \times I \mathrm { o f } X \times I .$ This homeomorphism may fail without the assumption of the existence of retract.

Example 10.8. The inclusion $S ^ { n - 1 } \hookrightarrow D ^ { n }$ is a cofibration.

Definition 10.9. Let A be a subspace of X. We say $( X , A )$ is cofibered if the inclusion $A \subset X$ is a cofibration.

Definition 10.10. Let A be a subspace of X. A is called a neighborhood deformation retract (NDR) if there exists a continuous map $u : X \to I$ with $A = u ^ { - 1 } ( 0 )$ and a homotopy $H : X \times I  X$ such that

$$
\left\{ \begin{array} { l l } { H ( x , 0 ) = x } & { \forall x \in X } \\ { H ( a , t ) = a } & { { \mathrm { i f ~ } } ( a , t ) \in A \times I } \\ { H ( x , 1 ) \in A } & { { \mathrm { i f ~ } } u ( x ) < 1 } \end{array} \right.
$$

Note that if A is a NDR of $X ,$ then A is a strong deformation retract of the open subset $u ^ { - 1 } ( [ 0 , 1 ) )$ of X .

Theorem 10.11. Let A be a closed subspace of X. Then the following conditions are equivalent

(1) $( X , A )$ is a cofibered pair.

(2) A is a NDR of X.

(3) $X \times \{ 0 \} \cup A \times I$ is a retract of $X \times I .$

(4) $X \times \{ 0 \} \cup A \times I$ is a strong deformation retract of $X \times I .$

Proposition 10.12. Let $i : A \to X$ be a cofibration, $f : A  B$ is a map. Consider the push-out

<!-- image-->

Then j : $B  Y$ is also a cofibration.

Definition 10.13. Let $i : A \to X , j : A \to$ Y be cofibrations. A map $f : X \to Y$ is called a cofiber map if the following diagram commutes

<!-- image-->

A cofiber homotopy between two cofiber maps $f , g : X \to Y$ is a homotopy of cofiber maps between f andg. Cofiber homotopy equivalence is defined similarly.

Proposition 10.14. Let i : $A \to X , j : A \to$ Y be cofibrations. Let $f : X \to Y$ be a cofiber map. Assume $f$ is a homotopy equivalence. Then f is a cofiber homotopy equivalence.

Let $f : A \to X$ be a map. Consider the diagram of mapping cylinder

<!-- image-->

There is a natural commuting diagram

<!-- image-->

Here $i _ { 1 } ( a ) = ( a , 1 ) , r ( a , t ) = f ( a ) , r ( x , 0 ) = x$ . It is easy to see that r is a homotopy equivalence. Moreover, A is a closed subspace of $M _ { f }$ and $M _ { f } \times \{ 0 \} \cup A \times I$ is a retract of $M _ { f } \times I .$ . Therefore $i _ { 1 }$ is a cofibration.

We arrive at the dual result of fibrations: any map $f : A \to X$ can be factored as $f = r \circ i _ { 1 }$ where $i _ { 1 }$ is a cofibration and r is a homotopy equivalence. Moreover, if $f$ is a cofibration, then $r : M _ { f } \to X$ is a cofiber homotopy equivalence.

Cofiber exact sequence.

Now we work with the category Top and hTop .

Definition 10.15. Let $( X , x _ { 0 } ) \in \mathrm { T o p } .$ . We define its cone in Top by

$$
C X = X \wedge I = X \times I / X \times \{ 0 \} \cup x _ { 0 } \times I .
$$

Given $f : X \to Y$ in Top , we define its homotopy cofiber $C _ { f }$ by the push-out

<!-- image-->

where $i _ { 1 } ( x ) = ( x , 1 )$

The closed embedding $i _ { 1 }$ is a cofibration. Therefore $j : Y \to C _ { f }$ is also a cofibration. Note that the quotient of $C _ { f }$ by Y is precisely ΣX. We can extend the above maps by

$$
X \longrightarrow Y \longrightarrow C _ { f } ~ \longrightarrow ~ \Sigma X \longrightarrow \Sigma Y ~ \longrightarrow ~ \Sigma C _ { f } ~ \longrightarrow ~ \Sigma ^ { 2 } X \longrightarrow \Sigma ^ { . . . }
$$

Definition 10.16. A sequence of maps in hTop

$$
\cdot \cdot \cdot \to X _ { n + 1 } \to X _ { n } \to X _ { n - 1 } \to \cdot \cdot \cdot
$$

is called co-exact if for any $Y \in \mathrm { h T o p } ,$ , the following sequence of pointed sets is exact

$$
\cdot \cdot \cdot  [ X _ { n - 1 } , Y ] _ { 0 }  [ X _ { n } , Y ] _ { 0 }  [ X _ { n + 1 } , Y ] _ { 0 }  \cdot \cdot \cdot
$$

Theorem 10.17 (Co-exact Puppe Sequence). Let $f : X \to Y$ in Top . The following sequence is co-exact in hTop

$$
X \longrightarrow Y \longrightarrow C _ { f } ~  ~ \Sigma X \longrightarrow \Sigma Y ~  \Sigma C _ { f } ~  \Sigma ^ { 2 } X ~  \Sigma ^ { . } \times  Y ^ { . } ~ .
$$

Proposition 10.18. Let $i : A \to X$ be a cofibration. Then the natural map

$$
{ \bar { r } } : C _ { f } \to X / A
$$

is a homotopy equivalence. In other words, cofiber is homotopy equivalent to the homotopy cofiber.

Theorem 10.19. Let $i : A \to X$ be a cofibration. The following sequence is co-exact in hTop

$$
{ \cal A } \longrightarrow X \longrightarrow X / { \cal A } \longrightarrow \Sigma { \cal A } \longrightarrow \Sigma X \longrightarrow \Sigma \left( X / { \cal A } \right) \longrightarrow \Sigma ^ { 2 } { \cal A } \longrightarrow \Sigma ^ { 2 } { \cal A } \longrightarrow \Sigma ^ { 2 } { \cal A } .
$$

## 11. CW COMPLEX

$D ^ { n }$ denotes the n-disk and $e ^ { n } = D ^ { n } - \partial D ^ { n } = D ^ { n } - S ^ { n - 1 }$ denotes the open disk called n-cell.

Definition 11.1. A cell decomposition of a space X is a family $\mathcal { E } = \{ e _ { \alpha } ^ { n } | \alpha \in J _ { n } \}$ of subspaces of X such that each $e _ { \alpha } ^ { n }$ is a n-cell and we have a disjoint union of sets

$$
X = \coprod \mathrm { ~ \large { I } \ln \mathrm { { } ~ } e _ { \alpha } ^ { n } . }
$$

The n-skeleton of X is the subspace

$$
X ^ { n } = \coprod _ { \alpha \in J _ { m } , m \leq n } e _ { \alpha } ^ { m } .
$$

Definition 11.2. A CW complex is a pair (X, E ) of a Hausdorff space X with a cell decomposition such that

(1) Characteristic map: for each n-cell $e _ { \alpha } ^ { n } ,$ , there is a characteristic map $\Phi _ { e _ { \alpha } ^ { n } } : D ^ { n } \to X$ such that the restriction of $\Phi _ { e _ { n } ^ { \alpha } }$ to $D ^ { n } - S ^ { n - 1 }$ is a homeomorphism to $e _ { \alpha } ^ { n }$ and $\Phi _ { e _ { \alpha } ^ { n } } \bigl ( S ^ { n - 1 } \bigr ) \subset X ^ { n - 1 }$

(2) Closure finiteness: for any cell $e \in { \mathcal { E } }$ the closure e¯ intersects only a finite number of other cells in E.

(3) Weak topology: a subset $A \subset X$ is closed if and only if A ∩ e¯ is closed in e¯ for each $e \in { \mathcal { E } }$

We say X is n-dim CW complex if the maximal dimension of cells in E is n (n could be ∞).

Note that the Hausdorff property of X implies that $\bar { e } = \Phi _ { e } ( D ^ { n } )$ for each cell $e \in { \mathcal { E } }$ . The surjective map $\Phi _ { e } : D ^ { n } \to \bar { e }$ is a quotient since $D ^ { n }$ is compact and e¯ is Hausdorff. Let us denote the full characteristic maps

$$
\Phi : \coprod _ { e \in { \mathcal { E } } } D ^ { n } { \xrightarrow { \amalg \Phi _ { e } } } X .
$$

Then the weak topology implies that Φ is a quotient map. This implies the following proposition.

Proposition 11.3. Let $( X , \mathcal { E } )$ be a CW complex. Then $f : X \to Y$ is continuous if and only if $f \circ \Phi _ { e }$ is continuous for each $e \in { \mathcal { E } }$ .

Proposition 11.4. Let $( X , \mathcal { E } )$ be a CW complex. Then any compact subspace of X meets only finite many cells in $\mathcal { E } .$

Example 11.5. $\mathbb { R } ^ { n } , S ^ { n } , \mathbb { C } P ^ { n } , \mathbb { H } P ^ { n } , S ^ { \infty } , \mathbb { C } P ^ { \infty } , \mathbb { H } P ^ { \infty }$

Definition 11.6. A subcomplex $( X ^ { \prime } , { \mathcal { E } } ^ { \prime } )$ of the CW complex $( X , \mathcal { E } )$ is a closed subspace $X ^ { \prime } \subset X$ with a cell decomposition ${ \mathcal { E } } ^ { \prime } \subset { \mathcal { E } }$ . We will just write $X ^ { \prime } \subset X$ when the cell decomposition is clear. We will also write $X ^ { \prime } = | \mathcal { E } ^ { \prime } |$ . Equivalently, a subcomplex is described by a subset ${ \mathcal { E } } ^ { \prime } \subset { \mathcal { E } }$ such that

$$
e _ { 1 } \in { \mathcal { E } } ^ { \prime } , e _ { 2 } \in { \mathcal { E } } , { \bar { e } } _ { 1 } \cap e _ { 2 } \neq \emptyset \Longrightarrow e _ { 2 } \in { \mathcal { E } } ^ { \prime } .
$$

Example 11.7. The n-skeleton $X ^ { n }$ is a subcomplex of X of dimension $\leq n .$

Definition 11.8. Given $f : S ^ { n - 1 } \to X$ . Consider the push-out

<!-- image-->

We say $D ^ { n } \operatorname { I I } _ { f } X$ is obtained by attaching an n-cell to X. $\Phi _ { f }$ is called the characteristic map of the attached n-cell. More generally, if we have a set of maps $f _ { \alpha } : S ^ { n - 1 } \to X ,$ the push-out

$$
\begin{array} { l c r } { { \mathrm { I I } _ { \alpha } S ^ { n - 1 } \xrightarrow { f } X } } & { { f = \displaystyle \prod f _ { \alpha } } } \\ { { \mathrm { ~ \displaystyle ~ \int ~ } } } & { { \Phi _ { f } \underbrace { \vphantom { \mathrm { I I } _ { \alpha } D ^ { n - 1 } } \mathrm { I I } _ { f } X } } } \\ { { \mathrm { ~ \displaystyle ~ \operatorname ~ { I I } _ { \alpha } D ^ { n } ~ \frac { \Phi _ { f } } { \longrightarrow } ~ ( \mathrm { I I } D ^ { n } ) \operatorname { I I } _ { f } X } } } & { { } } \end{array}
$$

is called X with n-cells attached.

Proposition 11.9. Let $( X , \mathcal { E } )$ be a CW complex, and ${ \mathcal { E } } = \amalg { \mathcal { E } } ^ { n }$ where ${ \mathcal { E } } ^ { n }$ is the set of n-cells. Then the diagram

$$
\begin{array} { l c r } { { \displaystyle \prod _ { e \in \mathcal { E } ^ { n } } S ^ { n - 1 } \xrightarrow { \partial \Phi ^ { n } } \ _ { \displaystyle - \bigcup } X ^ { n - 1 } \qquad \ \Phi ^ { n } = \displaystyle \prod _ { e \in \mathcal { E } ^ { n } } \Phi _ { e } } } \\ { { \displaystyle \int _ { e \in \mathcal { E } ^ { n } } \ _ { \displaystyle - \bigoplus } \down _ { X ^ { n } } \ _ { \displaystyle - \bigstar } ^ { } } } \\ { { \displaystyle \prod _ { e \in \mathcal { E } ^ { n } } D ^ { n } \ \xrightarrow { \Phi ^ { n } } \ _ { X ^ { n } } } } \end{array}
$$

is a push-out. In particular, $X ^ { n }$ is obtained from $X ^ { n - 1 }$ by attaching n-cells in X.

Proof. This follows from the fact that $X ^ { n - 1 }$ is a closed subspace of $X ^ { n }$ and the weak topology.

The converse is also true. The next proposition can be viewed as an alternate definition of CW complex. Proposition 11.10. Suppose we have a sequence of spaces

$$
{ \oslash } = X ^ { - 1 } \subset X ^ { 0 } \subset X ^ { 1 } \subset \cdots \subset X ^ { n } \subset X ^ { n + 1 } \subset \cdots
$$

where $X ^ { n }$ is obtained from $X ^ { n - 1 }$ by attaching n-cells. Let $X = \cup _ { n \geq 0 } X ^ { n }$ be the union with the weak topology: $A \subset X$ is closed if and only $i f A \cap X ^ { n }$ is closed in $X ^ { n }$ for each n. Then X is a CW complex.

Proof. The nontrivial part is to show that X is Hausdorff.

Definition 11.11. Let A be a subspace of X. A CW decomposition of $( X , A )$ consiss of a sequence

$$
A = X ^ { - 1 } \subset X ^ { 0 } \subset X ^ { 1 } \subset \cdots \subset X
$$

such that $X ^ { n }$ is obtained from $X ^ { n - 1 }$ by attaching n-cells and X carries the weak topology with respect to the subspaces $X ^ { n }$ . The pair $( X , A )$ is called a relative CW complex.

Note that for a relative CW complex $( X , A )$ , A itself may not have any cell structures.

Proposition 11.12. Let (X, A) be a relative CW complex. Then $A \subset X$ is a cofibration.

Proof. $S ^ { n - 1 } \hookrightarrow D ^ { n }$ is a cofibration, and cofibration is preserved under push-out and compositions.

Corollary 11.13. Let X be a CW complex and X0 be a CW subcomplex. Then $X ^ { \prime }  X$ is a cofibration.

Proof. $( X , X ^ { \prime } )$ is a relative CW complex.

Proposition 11.14. Let X.Y be CW complexes. X is locally compact. Then $X \times Y$ is a CW complex

## 12. WHITEHEAD THEOREM

Relative homotopy group.

Definition 12.1. The define the category TopP of topological pairs where an object $( X , A )$ is a topological space X with a subspace $X ,$ and morphisms $\overline { { ( } } X , A )  ( Y , B )$ are continuous maps $f : X \to Y$ such that $f ( A ) \subset B .$ . A homotopy between two maps $f _ { 1 } , f _ { 2 } : ( X , A ) \to ( Y , B )$ is a homotopy $F : X \times I  Y$ between $f _ { 0 } , f _ { 1 }$ such that $F | _ { X \times t } ( A ) \subset B$ for any $t \in I .$

The quotient category of TopP by homotopy of maps is denoted by hTopP. The pointed versions are defined similarly and denoted by TopP and hTopP . Morphisms in hTopP and hTopP are denoted by

$$
[ ( X , A ) , ( Y , B ) ] , \qquad [ ( X , A ) , ( Y , B ) ] _ { 0 } .
$$

Lemma 12.2. Let $f : ( X , A ) \to ( Y , B )$ . Let ${ \bar { f } } = f | _ { A }$ . Then the sequence

$$
( X , A ) \to ( Y , B ) \to ( C _ { f } , C _ { \bar { f } } )
$$

is co-exact in $\mathrm { \ h T o p P { _ { * } } }$ . When $A = B = p o i n t ,$ , this recovers the co-exactness of homotopy cofiber.

Theorem 12.3. Let $f : ( X , A ) \to ( Y , B )$ . Let ${ \bar { f } } = f | _ { A }$ . Then the sequence

$$
( X , A ) \to ( Y , B ) \to ( C _ { f } , C _ { \bar { f } } ) \to \Sigma ( X , A ) \to \Sigma ( Y , B ) \to \Sigma ( C _ { f } , C _ { \bar { f } } ) \to \Sigma ^ { 2 } ( X , A ) \to \cdots .
$$

is co-exact in hTopP . This generalizes the co-exact Puppe sequence to the pair case.

Definition 12.4. Let $( X , A ) \in \mathrm { T o p P } ,$ . We define the relative homotopy group $\pi _ { n } ( X , A )$

$$
\pi _ { n } ( X , A ) = [ ( D ^ { n } , S ^ { n - 1 } ) , ( X , A ) ] _ { 0 } .
$$

We will also write $\pi _ { n } ( X , A ; x _ { 0 } )$ when we want to specify the base point.

Note that for $n \geq 2$

$$
( D ^ { n } , S ^ { n - 1 } ) \simeq \Sigma ^ { n - 1 } ( D ^ { 1 } , S ^ { 0 } ) ,
$$

therefore $\pi _ { n } ( X , A )$ is a group for $n \geq 2$ by the adjunct pair $\left( \Sigma , \Omega \right)$

Lemma 12.5. $f : ( D ^ { n } , S ^ { n - 1 } ) \to ( X , A )$ is zero in $\pi _ { n } ( X , A )$ if and only $i f f$ is homotopic rel $S ^ { n - 1 }$ to a map whose image lies in A.

This lemma can be summarized by the following diagram

<!-- image-->

Here g maps $D ^ { n }$ to A and $g \simeq f$ rel $S ^ { n - 1 }$

Theorem 12.6. Let $B \subset A \subset X$ in Top . Then there is a long exact sequence

$$
\cdots \to \pi _ { n } ( A , B ) \ { \overset { i _ { * } } { \to } } \ \pi _ { n } ( X , B ) \ { \overset { j _ { * } } { \to } } \ \pi _ { n } ( X , A ) \ { \overset { \partial } { \to } } \ \pi _ { n - 1 } ( A , B ) \cdots \to \pi _ { 0 } ( X )
$$

Here the boundary map ∂ sends $f \in [ ( D ^ { n } , S ^ { n - 1 } ) , ( X , A ) ] _ { 0 }$ to its restriction to $S ^ { n - 1 } = D ^ { n - 1 } / S ^ { n - 2 }$ viewed as

$$
\partial f : ( D ^ { n - 1 } , S ^ { n - 2 } ) \to ( A , B )
$$

where ∂ f sends the whole $S ^ { n - 2 }$ to the base point in B.

Proof. We prove the case for A = B = base point $x _ { 0 } \in X .$ . Consider

$$
f : ( S ^ { 0 } , \{ 0 \} )  ( S ^ { 0 } , S ^ { 0 } ) .
$$

Let ${ \bar { f } } = f | _ { \{ 0 \} } : \{ 0 \} \to S ^ { 0 }$ . It is easy to see that

$$
( C _ { f } , C _ { \bar { f } } ) \simeq ( D ^ { 1 } , S ^ { 0 } ) .
$$

Since $\Sigma ^ { n } ( S ^ { 0 } ) = S ^ { n } , \Sigma ( D ^ { n } , S ^ { n - 1 } ) = ( D ^ { n + 1 } , S ^ { n } )$ , the co-exact Puppe sequence

$$
( S ^ { 0 } , \{ 0 \} )  ( S ^ { 0 } , S ^ { 0 } )  ( D ^ { 1 } , S ^ { 0 } )  ( S ^ { 1 } , \{ 0 \} )  ( S ^ { 1 } , S ^ { 1 } )  ( D ^ { 2 } , S ^ { 1 } )  ( S ^ { 2 } , \{ 0 \} )  \cdots .
$$

implies the exact sequence

$$
\cdots \to \pi _ { n } ( A ) \ { \overset { i _ { * } } { \to } } \pi _ { n } ( X ) \ { \overset { j _ { * } } { \to } } \pi _ { n } ( X , A ) \ { \overset { \partial } { \to } } \pi _ { n - 1 } ( A ) \cdots \to \pi _ { 0 } ( X )
$$

Definition 12.7. A pair $( X , A )$ is called n-connected $( n \geq 0 ) \operatorname { i f } \pi _ { 0 } ( A ) \to \pi _ { 0 } ( X )$ is surjective and $\pi _ { k } ( X , A ; x _ { 0 } ) =$ 0 for any $1 \leq k \leq n , x _ { 0 } \in A$

From the long exact sequence

$$
\cdots \to \pi _ { n } ( A ) { \overset { i _ { * } } { \to } } \pi _ { n } ( X ) { \overset { j _ { * } } { \to } } \pi _ { n } ( X , A ) { \overset { \partial } { \to } } \pi _ { n - 1 } ( A ) \cdots \to \pi _ { 0 } ( X )
$$

we see that $( X , A )$ is n-connected if and only if for any $x _ { 0 } \in A$

$$
\left\{ \begin{array} { l l } { \pi _ { r } ( A , x _ { 0 } ) \to \pi _ { r } ( X , x _ { 0 } ) { \mathrm { ~ i s ~ b i j e c t i v e ~ f o r ~ } } r < n } \\ { \pi _ { n } ( A , x _ { 0 } ) \to \pi _ { n } ( X , x _ { 0 } ) { \mathrm { ~ i s ~ s u r j e c t i v e } } } \end{array} \right.
$$

Definition 12.8. A map $f : X \to Y$ is called an n-equivalence $( n \geq 0 )$ if for any $x _ { 0 } \in X$

$$
\left\{ \begin{array} { l l } { f _ { * } : \pi _ { r } ( X , x _ { 0 } ) \to \pi _ { r } ( Y , f ( x _ { 0 } ) ) { \mathrm { ~ i s ~ b i j e c t i v e ~ f o r ~ } } r < n } \\ { f _ { * } : \pi _ { n } ( X , x _ { 0 } ) \to \pi _ { n } ( Y , f ( x _ { 0 } ) ) { \mathrm { ~ i s ~ s u r j e c t i v e } } } \end{array} \right.
$$

f is called weak homotopy equivalence or ∞-equivalence if f is n-equivalence for any $n \geq 0$

Example 12.9. For any $n \geq 0 ,$ , the pair $( D ^ { n + 1 } , S ^ { n } )$ is n-connected.

CW complex.

Lemma 12.10. Let X be obtained from A by attaching n-cells. Let $( Y , B )$ be a pair such that $\pi _ { n } ( Y , B ; b ) = 0 , \forall b \in B$ $i f n \geq 1$ or $\pi _ { 0 } ( B ) \to \pi _ { 0 } ( Y )$ surjective $i f n = 0$ . Then any map from $( X , A ) \to ( Y , B )$ is homotopic rel A to a map from X to B.

Proof. Apply the universal property of push-out and the result for $S ^ { n - 1 } \hookrightarrow D ^ { n }$

<!-- image-->

Theorem 12.11. Let $( X , A )$ be a relative CW complex with relative dimension $\leq n .$ . Let $( Y , B )$ be n-connected $( 0 \leq n \leq \infty )$ . Then any map from $( X , A )$ to $( Y , B )$ is homotopic relative to A to a map from X to B.

<!-- image-->

Proof. Apply the previous Lemma to

$$
A \subset X ^ { 0 } \subset X ^ { 1 } \subset \cdots \subset X ^ { n } = X
$$

and observe that all embeddings are cofibrations.

Proposition 12.12. Let $f : X \to Y$ be a weak homotopy equivalence, P be a CW complex. Then

$$
f _ { * } : [ P , X ] \to [ P , Y ]
$$

is a bijection.

Proof. We can assume $f$ is an embedding and $( Y , X )$ is ∞-connected. Otherwise replace Y by $M _ { f }$

Surjectivity follows from the diagram

<!-- image-->

Injectivity follows from the diagram (observe $P \times I , P \times \partial I$ are CW complexes)

<!-- image-->

Theorem 12.13 (Whitehead Theorem). A map between CW complexes is a weak homotopy equivalence if and only if it is a homotopy equivalence.

Proof. Let $f : X \to$ Y be a weak homotopy equivalence between CW complexes. We have bijections

$$
f _ { * } : [ X , X ] _ { 0 } \to [ X , Y ] _ { 0 } , \quad f _ { * } : [ Y , X ] \to [ Y , Y ] _ { 0 } .
$$

Let $g \in [ Y , X ] _ { 0 }$ such that $f _ { * } [ g ] = 1 _ { Y }$ . Then $g \circ f \simeq 1 _ { Y }$ . On the other hand,

$$
f _ { * } [ f \circ g ] = [ f \circ g \circ f ] \simeq [ f \circ 1 ] = [ f ] = f _ { * } [ 1 _ { X } ]
$$

we find $[ f \circ g ] = 1 _ { X }$ . Therefore f is a homotopy equivalence. The reverse direction is obvious.

## 13. CELLULAR AND CW APPROXIMATIONS

Cellular Approximation.

Definition 13.1. Let $( X , Y )$ be CW complexes. A map $f : X \to Y$ is called cellular if $f ( X ^ { n } ) \subset Y ^ { n }$ for any n.   
We define the category CW whose objects are CW complexes and morphisms are cellular maps.

Definition 13.2. A cellular homotopy between two cellular maps $X  Y$ of CW complexes is a homotopy $X \times I  Y$ that is itself a cellular map. Here I is naturally a CW complex. We define the quotient category hCW of CW whose morphisms are cellular homotopy class of cellular maps.

Lemma 13.3. Let X be obtained from A by attaching n-cells $( n \geq 1 )$ , then $\left( X , A \right) i s \left( n - 1 \right)$ -connected.

Proof. Let $r < n$ . Consider a diagram

<!-- image-->

Since $D ^ { r }$ is compact, $f ( D ^ { r } )$ meets only finitely many attached n-cells on $X ,$ say $e _ { 1 } , \cdots , e _ { m }$ . Let $p _ { i }$ be the center of $e _ { i }$ . Let $e _ { i } ^ { * } = e _ { i } - \{ p _ { i } \} . \ Y = X - \{ p _ { 1 } , \cdot \cdot \cdot , p _ { m } \}$ . We subdivide $D ^ { r }$ into small disks $D ^ { r } = \cup _ { \alpha } D _ { \alpha } ^ { r }$ such that $f ( D _ { \alpha } ^ { r } ) \subset Y$ or $f ( D _ { \alpha } ^ { r } ) \subset e _ { i } ^ { * }$ . For each $D _ { \alpha } ^ { r }$ such that $f ( D _ { \alpha } ^ { r } ) \subset e _ { i }$ but not in $\boldsymbol { Y } ,$ we use the fact that

$( e _ { i } , e _ { i } ^ { * } ) \simeq ( D ^ { n } , S ^ { n - 1 } )$ is $( n - 1 )$ -connected to find a homotopy rel $\partial D _ { \alpha } ^ { r }$ to adjust mapping $D _ { \alpha } ^ { r }$ into $e _ { i } ^ { * }$ . It glues together to obtain

<!-- image-->

Then we can further find a homotopy

<!-- image-->

Corollary 13.4. Let $( X , A )$ be a relative CW complex, then for any $n \geq 0 ,$ , the pair $( X , X ^ { n } )$ is n-connected.

Theorem 13.5. Let $f : ( X , A )  ( { \tilde { X } } , { \tilde { A } } )$ between relative CW complexes which is cellular on a subcomplex $( Y , B )$ $o f \left( X , A \right)$ . Then $f$ is homotopic rel Y to a cellular map $g : ( X , A )  ( { \tilde { X } } , { \tilde { A } } )$

Proof. Assume we have constructed $f _ { n - 1 } : ( X , A ) \to ( { \tilde { X } } , { \tilde { A } } )$ which is homotopic to $f$ rel Y and cellular on the (n − 1)-skeleton $X ^ { n - 1 }$ . Let $X ^ { n }$ be obtained from $X ^ { n - 1 }$ by attaching n-cells. Consider

$$
\begin{array} { l } { { X ^ { n - 1 } \hfill \longrightarrow \tilde { X } ^ { n } } } \\ { { \hfill \iint _ { S ^ { n } } \hfill \iint _ { S ^ { n } } \hfill \iint _ { S ^ { n } } } } \\ { { X ^ { n } \hfill \hfill \longrightarrow \tilde { X } ^ { n } } } \end{array}
$$

Since $X ^ { n }$ is obtained from $X ^ { n - 1 }$ by attaching n-cells and $( \tilde { X } , \tilde { X } ^ { n } )$ is n-connected,

<!-- image-->

we can find a homotopy rel $X ^ { n - 1 }$ from $f _ { n - 1 } | _ { X ^ { n } } : X ^ { n } \to { \tilde { X } }$ to a map $X ^ { n }  { \tilde { X } } ^ { n }$ . Since $f$ is cellular on $\boldsymbol { Y } ,$ we can choose this homotopy rel Y by adjusting only those n-cells not in Y. This homotopy extends to a homotopy rel $X ^ { n - 1 } \cup Y$ from $f _ { n - 1 }$ to a map $f _ { n } : X \to { \tilde { X } }$ since $X ^ { n } \subset X$ is a cofibration. Then $f _ { \infty }$ works. 

Theorem 13.6 (Cellular Approximation Theorem). Any map between relative CW complexes is homotopic to a cellular map. If two cellular maps between relative CW complexes are homotopic, then they are cellular homotopic.

Proof. Apply the previous Theorem to $( X , \emptyset )$ and $\left( X \times I , X \times \partial I \right)$

Remark 13.7. This theorem says that hCW is a full subcategory of hTop.

CW Approximation.

Definition 13.8. A CW approximation of a topological space Y is a CW complex X with a weak homotopy equivalence $f : X \to Y$ .

Theorem 13.9. Any space has a CW approximation.

Proof. We may assume Y is path connected. We construct a CW approximation X of Y by induction on the skeleton $X ^ { n }$ . Assume we have constructed $f _ { n } : X ^ { n } \to Y$ which is an n-equivalence. We attach an $( n + 1 )$ )-cell to every generator of ker $( \pi _ { n } ( X ^ { n } ) \to \pi _ { n } ( Y ) )$ to obtain $\tilde { X } ^ { n + 1 }$ . We can extend $f _ { n }$ to a map ${ \tilde { f } } _ { n + 1 } : { \tilde { X } } ^ { n + 1 } \to Y$

<!-- image-->

Since $( \tilde { X } ^ { n + 1 } , X ^ { n } )$ is also n-connected, $\tilde { f } _ { n + 1 }$ is an n-equivalence. By construction and the surjectivity of $\pi _ { n } ( { \tilde { X } } ^ { n + 1 } ) \to \pi _ { n } ( X ^ { n } ) , { \tilde { f } } _ { n + 1 }$ defines also an isomorphism for $\pi _ { n } ( { \tilde { X } } ^ { n + 1 } ) \to \pi _ { n } ( Y )$

Now for every generator $S _ { \alpha } ^ { n + 1 }$ of coker $( \pi _ { n + 1 } ( { \tilde { X } } ^ { n + 1 } ) \to \pi _ { n + 1 } ( Y ) )$ , we take a wedge sum to obtain

$$
{ X ^ { n + 1 } } = { \tilde { X } } ^ { n + 1 } \vee ( \vee _ { \alpha } S ^ { n + 1 } ) .
$$

Then the induced map $f _ { n + 1 } : X ^ { n + 1 } \to Y$ extends $f _ { n }$ to an $( n + 1 )$ )-equivalence. Inductively we obtain a weak homotopy equivalence $f _ { \infty } : X = X ^ { \infty } \to Y .$ 

Theorem 13.10. Let $f : X \to Y .$ . Let $\Gamma X  X ,$ and $\Gamma Y  Y$ be CW approximations. Then there exists a unique map in [ΓX, ΓY] making the following diagram commutes in hTop

<!-- image-->

Proof. Weak homotopy equivalence of $\Gamma Y  Y$ implies the bijection $[ \Gamma _ { X } , \Gamma _ { Y } ]  [ \Gamma _ { X } , Y ]$

Definition 13.11. Two spaces $X _ { 1 } , X _ { 2 }$ are said to have the same weak homotopy type if there exists a space Y and weak homotopy equivalences $f _ { i } : Y \to X _ { i } , i = 1 , 2$

Proposition 13.12. Weak homotopy type is an equivalence relation.

## 14. EILENBERG-MACLANE SPACE

Graphs.

Definition 14.1. A graph is a one-dimensional CW complex. The points of the 0-skeleton are called vertices and the 1-cells are called edges.

By definition, a basis for the topology of a graph consists of the open intervals in the edges together with the path-connected neighborhoods of the vertices. A graph is compact if and only if it contains only finitely many vertices and edges.

Definition 14.2. A subgraph of a graph is a CW subcomplex. A tree is a contractible graph. By a tree in a graph X we mean a subgraph that is a tree. We call a tree in X maximal if it contains all the vertices of X.

Proposition 14.3. Every connected graph contains a maximal tree, and in fact any tree in the graph is contained in a maximal tree.

Lemma 14.4. Let $A \subset X$ be a cofibration and A is contractible, then $X \to X / A$ is a homotopy equivalence.

Theorem 14.5. For a connected graph X with maximal tree $T , \pi _ { 1 } ( X )$ is a free group with basis the classes corresponding to the edges e of $X - T$

Theorem 14.6 (Nielsen-Schreier theorem). Every subgroup of a free group is itself free.

Proof. Let F be a free group with basis indexed by I. Let $X = \bigvee _ { I \in B } S ^ { 1 }$ . Then $\pi _ { 1 } ( X ) = F .$ . Let $G \subset F$ and $\tilde { X }  X$ be the covering such that $\pi _ { 1 } ( \tilde { X } ) = G$ . Then X˜ is also a CW complex. It follows that G is free.  $\pi _ { n } ( S ^ { n } )$

We have seen that $\pi _ { k } ( S ^ { n } ) = 1$ for $k < n$ . In this subsection we compute

$$
\pi _ { n } ( S ^ { n } ) = [ S ^ { n } , S ^ { n } ] _ { 0 } \cong \mathbb { Z } .
$$

Given $f : S ^ { n } \to S ^ { n }$ , its class $[ f ] \in \mathbb { Z }$ under the above isomorphism is called the degree of $f .$

Theorem 14.7 (Homotopy Excision Theorem)). Let $( A , C ) , ( B , C )$ be relative CW complex. Let X be the push-out

<!-- image-->

$I f \left( A , C \right)$ is m-connected and (B, C) is n-connected, then

$$
\pi _ { i } ( A , C ) \to \pi _ { i } ( X , B )
$$

is an isomorphism for $i < m + n$ , and a surjection for $i = m + n$

Corollary 14.8 (Freudenthal Suspension Theorem). The suspension map

$$
\pi _ { i } ( S ^ { n } ) \to \pi _ { i + 1 } ( S ^ { n + 1 } )
$$

is an isomorphism for $i < 2 n - 1$ and a surjection for $i = 2 n - 1$

Proof. Apply Homotopy Excision to $\ b { X } = \ b { S } ^ { n + 1 } , \ b { C } = \ b { S } ^ { n }$ , A the upper half disk, B the lower half disk.

Freudenthal Suspension Theorem holds similarly replacing $S ^ { n }$ by general (n − 1)-connected space.

Proposition 14.9. $\pi _ { n } ( S ^ { n } ) \cong \mathbb Z f o r n \geq 1$

$$
S ^ { 1 } \to S ^ { 3 } \to S ^ { 2 } .
$$

Proof. Freudenthal Suspension Theorem reduces to show $\pi _ { 2 } ( S ^ { 2 } ) \cong \mathbb { Z }$ . This follows from the Hopf fibration

Eilenberg-MacLane Space.

Definition 14.10. An Eilenberg-MacLane Space is a CW complex $K ( G , n )$ such that $\pi _ { n } ( K ( G , n ) ) \cong G$ and $\pi _ { k } ( K ( G , n ) ) = 0$ for $k \neq n .$ . Here G is abelian if $n > 1$ .

Theorem 14.11. Eilenberg-MacLane Space $K ( G , n )$ exists.

Proof. We prove the case for $n \geq 2 .$ . There exists an exact sequence

$$
0  F _ { 1 }  F _ { 2 }  G  0
$$

where $F _ { 1 } , F _ { 2 }$ are free abelian groups. Let $B _ { i }$ be a basis of $F _ { i } .$ . Let

$$
A = \bigvee _ { i \in B _ { 1 } } S ^ { n } , \quad B = \bigvee _ { j \in B _ { 2 } } S ^ { n } .
$$

A, B are $( n - 1 )$ -connected and $\pi _ { n } ( A ) = F _ { 1 } , \pi _ { n } ( B ) = F _ { 2 }$ . Using the degree map, we can construct

$$
f : A  B
$$

such that $\pi _ { n } ( A ) \to \pi _ { n } ( B )$ realizes the map $F _ { 1 }  F _ { 2 }$ . Let X be obtained from B by attaching $( n + 1 )$ -cells via $f .$ Then X is $( n - 1 )$ -connected and $\pi _ { n } ( X ) = G$ . Now we proceed as the proof of CW approximation theorem to attach cells of dimension $\geq ( n + 2 )$ to kill all higher homotopy groups of X to get $K ( G , n )$ 

As we will see, $K ( G , n )$ is the representing space for cohomology functor with coefficients in G

$$
H ^ { n } ( X ; G ) \cong [ X , K ( G , n ) ] \quad { \mathrm { f o r ~ a n y ~ C W ~ c o m p l e x ~ } } X .
$$

Example 14.12. $S ^ { 1 } = K ( \mathbb { Z } , 1 )$ . Connected graphs are Eilenberg-MacLane space for free groups at $n = 1$

Example 14.13. Using the fibration $S ^ { 1 } \to S ^ { \infty } \to \mathbb { C } P ^ { \infty }$ , we find $\mathbb { C } P ^ { \infty } = K ( \mathbb { Z } , 2 )$

Example 14.14. A knot is an embedding $K : S ^ { 1 } \hookrightarrow S ^ { 3 }$ . Let $G \equiv \pi _ { 1 } ( S ^ { 3 } - K )$ . Then $S ^ { 3 } - K = K ( G , 1 )$

## 15. SINGULAR HOMOLOGY

Chain complex.

Definition 15.1. Let R be a commutative ring. A chain complex over R is sequence of R-module maps

$$
\cdots \to C _ { n + 1 } { \overset { \partial _ { n + 1 } } { \to } } C _ { n } { \overset { \partial _ { n } } { \to } } C _ { n - 1 } \to \cdots
$$

such that $\partial _ { n } \circ \partial _ { n + 1 } = 0 \forall n$ . When R is not specified, we mean chain complex of abelian groups $( \mathbf { i . e . \ : } R = \mathbb { Z } )$

Sometimes we just write the map by ∂ and the chain complex by $( C _ { \bullet } , \partial )$ . Then $\partial _ { n } = \partial | _ { C _ { n } }$ and $\partial ^ { 2 } = 0$

Definition 15.2. A chain map $f : C _ { \bullet }  C _ { \bullet } ^ { \prime }$ between two chain complexes over R is a sequence of R-module maps $f _ { n } : C _ { n } \to C _ { n } ^ { \prime }$ such that the following diagram commutes

$$
\begin{array} { r l } & { \cdots \longmapsto C _ { n + 1 } \xrightarrow { \partial _ { n + 1 } } C _ { n } \xrightarrow { \partial _ { n } } C _ { n - 1 } \longrightarrow \cdots } \\ & { \qquad f _ { n + 1 } \Bigg \downarrow \qquad \quad f _ { n } \Bigg \downarrow \qquad f _ { n - 1 } \Bigg \downarrow } \\ &  \cdots \xrightarrow { \qquad \quad \longrightarrow C _ { n + 1 } ^ { \prime } \frac { \partial _ { n + 1 } } { \partial _ { n + 1 } ^ { \prime } } \xrightarrow { \qquad \quad  C _ { n } ^ { \prime } \xrightarrow { \qquad \quad  C _ { n - 1 } ^ { \prime } \longrightarrow \cdots } } \cdots } \end{array}
$$

We simply write it as

$$
\boxed { f \circ \partial = \partial ^ { \prime } \circ f }
$$

Chain complexes over R together with chain maps form the category $\mathrm { C h } _ { \bullet } ( \mathrm { R } )$ of chain complexes over $R ,$ or simply Ch• when $R = \mathbb { Z }$

Definition 15.3. Given a chain complex $( C _ { \bullet } , \partial )$ , its n-cycles $Z _ { n }$ and n-boundaries $B _ { n }$ are

$$
Z _ { n } = \mathrm { K e r } ( \partial : C _ { n } \to C _ { n - 1 } ) , \quad B _ { n } = \mathrm { I m } ( \partial : C _ { n + 1 } \to C _ { n } ) .
$$

$\partial ^ { 2 } = 0$ implies $B _ { n } \subset Z _ { n }$ . We define the n-th homology group by

$$
{ \bigg | } H _ { n } ( C _ { \bullet } , \partial ) : = { \frac { Z _ { n } } { B _ { n } } } = { \frac { \ker ( \partial _ { n } ) } { \mathrm { i m } ( \partial _ { n + 1 } ) } } { \bigg | } .
$$

A chain complex $C _ { \bullet }$ is called acyclic or exact if $H _ { n } ( C _ { \bullet } ) = 0 , \forall n$

Proposition 15.4. n-th homology group defines a functor

$$
H _ { n } : \underline { { \mathbf { C h } } } _ { \bullet }  \underline { { \mathbf { A b } } }
$$

Definition 15.5. A chain homotopy $f \ { \overset { s } { \simeq } } \ g$ between two chain maps $f , g : C \bullet  C _ { \bullet } ^ { \prime }$ is a sequence of homomorphisms $s _ { n } : C _ { n } \to C _ { n + 1 } ^ { \prime }$ such that $f _ { n } - g _ { n } = s _ { n - 1 } \circ \partial _ { n } + \partial _ { n + 1 } ^ { \prime } \circ s _ { n } ,$ or simply

$$
\boxed { f - g = s \circ \partial + \partial ^ { \prime } \circ s } .
$$

Two complexes $C _ { \bullet } , C _ { \bullet } ^ { \prime }$ are called chain homotopy equivalent if there exists chain maps $f : C _ { \bullet }  C _ { \bullet } ^ { \prime }$ and $h : C _ { \bullet } ^ { \prime } \to C _ { \bullet }$ such that $f \circ g \simeq 1$ and $g \circ f \simeq 1$ 1.

Proposition 15.6. Chain homotopy defines an equivalence relation on chain maps and compatible with compositions.

In other word, chain homotopy defines an equivalence relation on $\mathrm { C h } _ { \bullet }$ . We define the quotient category

$$
\mathrm { { h C h } } _ { \bullet } = \mathrm { { C h } } _ { \bullet } / \simeq .
$$

Chain homotopy equivalence becomes an equivalence in hCh•.

Proposition 15.7. Let $f , g$ be chain homotopic chain maps. Then they induce identical map on homology groups

$$
H _ { n } ( f ) = H _ { n } ( g ) : H _ { n } ( C _ { \bullet } )  H _ { n } ( C _ { \bullet } ^ { \prime } ) .
$$

In other words, the functor $H _ { n }$ factor through

$$
H _ { n } : \underline { { \mathbf { C h } } } _ { \bullet }  \underline { { \mathbf { h C h } } } _ { \bullet }  \underline { { \mathbf { A b } } } .
$$

Singular homology.

Definition 15.8. We define the standard n-simplex

$$
\Delta ^ { n } = \{ ( t _ { 0 } , \cdots , t _ { n } ) \in \mathbb { R } ^ { n + 1 } | \sum _ { i = 0 } ^ { n } t _ { i } = 1 , t _ { i } \geq 0 \}
$$

We let $\{ v _ { 0 } , \cdots , v _ { n } \}$ denote its vertices. Here $v _ { i } = ( 0 , \cdot \cdot \cdot , 0 , 1 , 0 , \cdot \cdot \cdot , 0 )$ where 1 sits at the i-th position.

Definition 15.9. Let X be a topological space. A singular n-simplex in X is a continuous map $\sigma : \Delta ^ { n } \to X$ For each $n \geq 0$ , we define $S _ { n } ( X )$ as the free abelian group with basis all singular n-simplexes in X

$$
S _ { n } ( X ) = \bigoplus _ { \sigma \in \mathrm { H o m } ( \Delta ^ { n } , X ) } \mathbb { Z } \sigma .
$$

The elements of $S _ { n } ( X )$ are called singular n-chains in X.

A singular n-chain is given by a finite formal sum

γ = ∑ mσσ, mσ ∈ Z and only finitely many $m _ { \sigma } { ' } s$ are nonzero. σ∈Hom(∆n,X)

The abelian group structure is: $\begin{array} { r } { - \gamma : = \sum _ { \sigma } ( - m _ { \sigma } ) \sigma } \end{array}$ and

$$
( \sum _ { \sigma } m _ { \sigma } \sigma ) + ( \sum _ { \sigma } m _ { \sigma } ^ { \prime } \sigma ) = \sum _ { \sigma } ( m _ { \sigma } + m _ { \sigma } ^ { \prime } ) \sigma .
$$

Definition 15.10. Given a n-simplex $\sigma : \Delta ^ { n } \to X$ and $0 \leq i \leq n ,$ , we define

$$
\partial ^ { ( i ) } \sigma : \Delta ^ { n - 1 }  X
$$

to be the $\left( n - 1 \right)$ -simplex by restricting σ to the i-th face of $\Delta ^ { n }$ whose vertices are given by $\{ v _ { 0 } , v _ { 1 } , \cdot \cdot \cdot , \hat { v } _ { i } , \cdot \cdot \cdot , v _ { n } \}$ We define the boundary map

$$
\partial : S _ { n } ( X ) \to S _ { n - 1 } ( X )
$$

by the abelian group homomorphism generated by

$$
{ \boxed { \partial \sigma : = \sum _ { i = 0 } ^ { n } ( - 1 ) ^ { i } \partial ^ { ( i ) } \sigma } } .
$$

Proposition 15.11. $( S _ { \bullet } ( X ) , \partial )$ defines a chain complex, $i . e . , \partial ^ { 2 } = \partial \circ \partial = 0 .$

Definition 15.12. For each $n \geq 0 .$ , we define n-th singular homology group of X by

$$
{ \boxed { H _ { n } ( X ) : = H _ { n } ( S _ { \bullet } ( X ) , \partial ) } } .
$$

Let $f : X \to Y$ be a continuous map, it defines a chain map

$$
S _ { \bullet } ( f ) : S _ { \bullet } ( X )  S _ { \bullet } ( Y ) .
$$

This defines the functor of singular chain complex

$$
S _ { \bullet } : \underline { { \mathrm { T o p } } }  \underline { { \mathrm { C h } } } _ { \bullet } .
$$

Singular homology group can be viewed as the composition of functors

$$
\underline { { \mathrm { T o p } } } \to \underline { { \mathrm { C h } } } _ { \bullet } \overset { H _ { n } } { \to } \underline { { \mathrm { A b } } } .
$$

Proposition 15.13. Let $f , g : X \to Y$ be homotopic maps. Then $S _ { \bullet } ( f ) , S _ { \bullet } ( g ) \ : \ S _ { \bullet } ( X ) \ \to \ S _ { \bullet } ( Y )$ are chain homotopic. In particular, they induce identical map $H _ { n } ( f ) = H _ { n } ( g ) : H _ { n } ( X ) \to H _ { n } ( Y )$

Proof. We only need to prove that for $i _ { 0 } , i _ { 1 } : X \to X \times I ,$ the induced map

$$
S _ { \bullet } ( i _ { 0 } ) , S _ { \bullet } ( i _ { 1 } ) : S _ { \bullet } ( X )  S _ { \bullet } ( X \times I )
$$

are chain homotopic. Then their composition with the homotopy $X \times I  Y$ gives the proposition.

Let us define a homotopy

$$
s : S _ { n } ( X ) \to S _ { n + 1 } ( X \times I ) .
$$

For $\sigma : \Delta ^ { n }  X .$ , we define (topologically)

$$
s ( \sigma ) : \Delta ^ { n } \times I \stackrel { \sigma \times 1 } {  } X \times I
$$

Here we treat $\Delta ^ { n } \times I$ as a collection of $( n + 1 )$ -simplexes as follows: let $\{ v _ { 0 } , \cdots , v _ { n } \}$ denote the vertices of $\Delta ^ { n }$ , then the vertices of $\Delta ^ { n } \times I$ contain two copies $\{ v _ { 0 } , \cdots , v _ { n } \}$ and $\{ w _ { 0 } , \cdot \cdot \cdot , w _ { n } \}$ . Then

$$
\Delta ^ { n } \times I = \sum _ { i = 0 } ^ { n } ( - 1 ) ^ { n } [ v _ { 0 } , v _ { 1 } , \cdot \cdot \cdot v _ { i } , w _ { i } , w _ { i + 1 } , \cdot \cdot \cdot , w _ { n } ]
$$

cuts $\Delta ^ { n } \times I$ into (n + 1)-simplexes. Its sum defines $s ( \sigma ) \in S _ { n + 1 } ( X \times I )$ . The intuitive formula holds

$$
\partial ( \Delta ^ { n } \times I ) = \Delta \times \partial I - ( \partial \Delta ^ { n } ) \times I
$$

as an equation for singular chains, leading to

$$
\begin{array} { r } { S _ { \bullet } ( i _ { 1 } ) - S _ { \bullet } ( i _ { 0 } ) = \partial \circ s + s \circ \partial . } \end{array}
$$

Theorem 15.14. Singular homologies are homotopy invariants. They factor through

$$
H _ { n } : \mathrm { h T o p }  \underline { { \mathrm { h C h } } } _ { \bullet }  \underline { { \mathrm { A b } } } .
$$

## 16. EXACT HOMOLOGY SEQUENCE

Exact homology sequence.

Definition 16.1. Chain maps $0 \to C _ { \bullet } ^ { \prime } { \overset { i } { \to } } C _ { \bullet } { \overset { p } { \to } } C _ { \bullet } ^ { \prime \prime } \to 0$ is called an short exact sequence if for each n

$$
0 \to C _ { n } ^ { \prime } \stackrel { i } { \to } C _ { n } \stackrel { p } { \to } C _ { n } ^ { \prime \prime } \to 0
$$

is an exact sequence of abelian groups.

We have the following commuting diagram

<!-- image-->

Lemma/Definition 16.2. Let $0 \to C _ { \bullet } ^ { \prime } { \overset { i } { \to } } C _ { \bullet } { \overset { p } { \to } } C _ { \bullet } ^ { \prime \prime } \to 0$ be a short exact sequence. There is a natural homomorphism

$$
\delta : H _ { n } ( C _ { \bullet } ^ { \prime \prime } )  H _ { n - 1 } ( C _ { \bullet } ^ { \prime } )
$$

called the connecting map. It induces a long exact sequence of abelian groups

$$
\begin{array} { r } { \cdot \cdot \cdot  H _ { n } ( C _ { \bullet } ^ { \prime } ) \stackrel { i * } {  } H _ { n } ( C _ { \bullet } ) \stackrel { p _ { \ast } } {  } H _ { n } ( C _ { \bullet } ^ { \prime \prime } ) \stackrel { \delta } {  } H _ { n - 1 } ( C _ { \bullet } ^ { \prime } ) \stackrel { i * } {  } H _ { n - 1 } ( C _ { \bullet } ) \stackrel { p _ { \ast } } {  } H _ { n - 1 } ( C _ { \bullet } ^ { \prime \prime } )  \cdot \cdot \cdot } \end{array}
$$

The connecting map δ is natural in the sense that a commutative diagram of complexes with exact rows

<!-- image-->

induces a commutative diagram of abelian groups with exact rows

$$
\begin{array} { r l } & { \cdots \longrightarrow H _ { n } ( C _ { \bullet } ^ { \prime \prime } ) \longrightarrow H _ { n } ( C _ { \bullet } ) \longrightarrow H _ { n } ( C _ { \bullet } ^ { \prime \prime } ) \longrightarrow H _ { n } ( C _ { \bullet } ^ { \prime \prime } ) \xrightarrow { \delta } H _ { n - 1 } ( C _ { \bullet } ^ { \prime } ) \longrightarrow \cdots } \\ & { \qquad \downarrow } \\ & { \cdots \longrightarrow H _ { n } ( D _ { \bullet } ^ { \prime \prime } ) \longrightarrow H _ { n } ( D _ { \bullet } ) \longrightarrow H _ { n } ( D _ { \bullet } ^ { \prime \prime } ) \xrightarrow { \delta } H _ { n - 1 } ( D _ { \bullet } ^ { \prime } ) \longrightarrow \cdots } \end{array}
$$

Relative homology.

Definition 16.3. Let $A \subset X$ be a subspace. It indues a natural injective chain map $S _ { \bullet } ( A ) \hookrightarrow S _ { \bullet } ( X )$ . We define the singular chain complex of X relative to A to be

$$
S _ { n } ( X , A ) : = S _ { n } ( X ) / S _ { n } ( A )
$$

with the induced differential. Its homology $\mathrm { H } _ { n } ( X , A ) : = \mathrm { H } _ { n } ( S _ { \bullet } ( X , A ) )$ is called the n-th relative homology.

Proposition 16.4. For $A \subset X ,$ there is a long exact sequence of abelian groups

$$
\cdots \to \operatorname { H } _ { n } ( A ) \to \operatorname { H } _ { n } ( X ) \to \operatorname { H } _ { n } ( X , A ) { \overset { \delta } { \to } } \operatorname { H } _ { n - 1 } ( A ) \to \cdots
$$

Proof. This follows from the short exact sequence of complexes

$$
0 \to S _ { \bullet } ( A ) \to S _ { \bullet } ( X ) \to S _ { \bullet } ( X , A ) \to 0 .
$$

Let us define relative n-cycles $Z _ { n } ( X , A )$ and relative n-boundaries $B _ { n } ( X , A )$ to be

$$
\begin{array} { r l } & { Z _ { n } ( X , A ) = \{ \gamma \in S _ { n } ( X ) : \partial \gamma \in S _ { n - 1 } ( A ) \} } \\ & { B _ { n } ( X , A ) = B _ { n } ( X ) + S _ { n } ( A ) \subset S _ { n } ( X ) . } \end{array}
$$

Then it is easy to check that $S _ { n } ( A ) \subset B _ { n } ( X , A ) \subset Z _ { n } ( X , A ) \subset S _ { n } ( X )$ and

$$
\mathrm { H } _ { n } ( X , A ) = Z _ { n } ( X , A ) / B _ { n } ( X , A )
$$

Two relative n-cycles $\gamma _ { 1 } , \gamma _ { 2 }$ defines the same class $[ \gamma _ { 1 } ] = [ \gamma _ { 2 } ] \mathrm { i n } \mathrm { H } _ { n } ( X , A )$ if and only if $\gamma _ { 1 } - \gamma _ { 2 }$ is homologous to a chain in A. The connecting map

$$
\delta : \mathrm { H } _ { n } ( X , A )  \mathrm { H } _ { n - 1 } ( A )
$$

can be understood as follows: a n-cycle in $\mathrm { H } _ { n } ( X , A )$ is represented by a n-chain $\gamma \in S _ { n } ( X )$ such that its boundary $\partial ( \gamma )$ lies in A. Viewing $\partial ( \gamma )$ as a (n − 1)-cycle in A, then

$$
\delta [ \gamma ] = [ \partial ( \gamma ) ] .
$$

Let $f : ( X , A ) \to ( Y , B )$ be a map of pairs. It naturally induces a commutative diagram

$$
\begin{array} { l c c c } { { 0 \longrightarrow S _ { \bullet } ( A ) \longrightarrow S _ { \bullet } ( X ) \longrightarrow S _ { \bullet } ( X , A ) \longrightarrow 0 } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { \downarrow } } \\ { { 0 \longrightarrow S _ { \bullet } ( B ) \longrightarrow S _ { \bullet } ( Y ) \longrightarrow S _ { \bullet } ( Y , B ) \longrightarrow 0 } } & { { } } & { { } } \end{array}
$$

which further induces compatible maps on various homology groups.

Proposition 16.5. Let $\{ X _ { \alpha } \}$ be path connected components of X, then

$$
\mathrm { H } _ { n } ( X ) = \bigoplus _ { \alpha } \mathrm { H } _ { n } ( X _ { \alpha } ) .
$$Proposition 16.6. Let X be path connected. Then $\mathrm { H } _ { 0 } ( X ) \cong \mathbb { Z } .$

In general, we have a surjective map

$$
\epsilon : \mathrm { H } _ { 0 } ( X )  \mathbb { Z } , \quad \sum _ { p \in X } m _ { p } p  \sum _ { p } m _ { p } .
$$

Definition 16.7. We define the reduced homology group by

$$
{ \tilde { \mathrm { H } } } _ { n } ( X ) = { \left\{ \begin{array} { l l } { \mathrm { H } _ { n } ( X ) } & { n > 0 } \\ { \ker ( \mathrm { H } _ { 0 } ( X ) \to \mathbb { Z } ) } & { n = 0 } \end{array} \right. }
$$

The long exact sequence still holds for the reduced case

$$
\therefore \cdot \cdot  \tilde { \mathrm { H } } _ { n } ( A )  \tilde { \mathrm { H } } _ { n } ( X )  \mathrm { H } _ { n } ( X , A ) \stackrel { \delta } {  } \tilde { \mathrm { H } } _ { n - 1 } ( A )  \cdot \cdot \cdot
$$

Example 16.8. If X is contractible, then ${ \tilde { H } } _ { n } ( X ) = 0$ for all n.

Example 16.9. Let $x _ { 0 } \in X$ be a point. Using the long exact sequence for $A = \{ x _ { 0 } \} \subset X .$ , we find

$$
\mathrm { H } _ { n } ( X , x _ { 0 } ) = \tilde { \mathrm { H } } _ { n } ( X ) .
$$

## 17. EXCISION

The fundamental property of homology which makes it computable is excision.

Barycentric Subdivision.

Definition 17.1. Let $\Delta ^ { n }$ be the standard n-simplex with vertices $v _ { 0 } , \cdots , v _ { n }$ . We define its barycenter to be

$$
c ( \Delta ^ { n } ) = \frac { 1 } { n + 1 } \sum _ { i = 0 } ^ { n } v _ { i } \in \Delta ^ { n } .
$$

Definition 17.2. We define the barycentric subdivision ${ \mathcal { B } } \Delta ^ { n }$ of a n-simplex $\Delta ^ { n }$ as follows:

(1) $\mathcal { B } \Delta ^ { 0 } = \Delta ^ { 0 }$

(2) Let $F _ { 0 } , \cdots , F _ { n }$ be the n-simplexes of faces of $\Delta ^ { n + 1 }$ . c be the barycenter of $\Delta ^ { n + 1 }$ . Then $\mathcal { B } \Delta ^ { n + 1 }$ consists of $( n + 1 )$ -simplexes with ordered vertices $\left[ c , w _ { 0 } , \cdots , w _ { n } \right]$ where $\left[ w _ { 0 } , \cdots , w _ { n } \right]$ is a n-simplexes in $\mathcal { B } \boldsymbol { F } _ { 0 } , \cdots , \mathcal { B } \boldsymbol { F } _ { n } .$

Equivalently, a simplex in ${ \mathcal { B } } \Delta ^ { n }$ is indexed by a sequence $\left\{ S _ { 0 } \subset S _ { 1 } \cdot \cdot \cdot \subset S _ { n } = \Delta ^ { n } \right\}$ where $S _ { i }$ is a face of $S _ { i + 1 }$ . Then its vertices are $\left[ c ( S _ { n } ) , c ( S _ { n - 1 } ) , \cdot \cdot \cdot , c ( S _ { 0 } ) \right]$ . It is seen that $\Delta ^ { n }$ is the union of simplexes in ${ \mathcal { B } } \Delta ^ { n }$

Definition 17.3. We define the n-chain of barycentric subdivision ${ \mathcal { B } } _ { n }$ by

$$
\boxed { \mathcal { B } _ { n } = \sum _ { \alpha } \pm \sigma _ { \alpha } \in S _ { n } \big ( \Delta ^ { n } \big ) }
$$

where the summation is over all sequence $\alpha = \{ S _ { 0 } \subset S _ { 1 } \colon \colon \subset S _ { n } = \Delta ^ { n } \}$ $\sigma _ { \alpha }$ is the simplex with ordered vertices $\left[ c ( S _ { n } ) , c ( S _ { n - 1 } ) , \cdot \cdot \cdot , c ( S _ { 0 } ) \right]$ , viewed as a singular n-chain in $\Delta ^ { n }$ . The sign ± is about orientation: if the orientation of $\left[ c ( S _ { n } ) , c ( S _ { n - 1 } ) , \cdot \cdot \cdot , c ( S _ { 0 } ) \right]$ coincides with that of $\Delta ^ { n } ,$ we take +; otherwise we take −.

Definition 17.4. We define the composition map denoted by

$$
S _ { k } ( \Delta ^ { m } ) \times S _ { n } ( \Delta ^ { k } )  S _ { n } ( \Delta ^ { m } ) , \quad \sigma \times \eta  \sigma \circ \eta .
$$

This is defined on generators via the composition $\Delta ^ { n }  \Delta ^ { k }  \Delta ^ { m }$ and extended linearly on singular chains.

Similarly, there is a natural map denoted by

$$
S _ { n } ( \Delta ^ { m } ) : S _ { m } ( X ) \to S _ { n } ( X ) , \quad \eta : \sigma \to \eta ^ { * } ( \sigma ) = \sigma \circ \eta
$$

where $\eta ^ { \ast } ( \sigma ) = \sigma \circ \eta$ is the composition of σ with η.

Example 17.5. Let $\tilde { \partial } _ { n } \in S _ { n - 1 } ( \Delta ^ { n } )$ be the faces. Then $\sqrt { \tilde { \partial } _ { n } \circ \tilde { \partial } _ { n - 1 } = 0 }$ and

$$
\boxed { \partial _ { n } = \tilde { \partial } _ { n } ^ { * } } : S _ { n } ( X )  S _ { n - 1 } ( x )
$$

defines the boundary map in singular chains.

Lemma 17.6.

$$
\boxed { \mathcal { B } _ { n } \circ \tilde { \partial } _ { n } = \tilde { \partial } _ { n } \circ \mathcal { B } _ { n - 1 } }
$$

Proof. The choice of ordering and orientation guarantees that

$$
\partial \mathcal { B } _ { n } = \mathcal { B } ( \partial \Delta ^ { n } )
$$

where $\mathcal { B } ( \partial \Delta ^ { n } )$ is the barycentric subdivision of faces ∂∆n of $\Delta ^ { n } ,$ , viewed as a (n − 1)-chain in $\Delta ^ { n }$

Definition 17.7. We define the barycentric subdivision on singular chain complex by

$$
{ \mathcal { B } } ^ { * } : S _ { \bullet } ( X ) \to S _ { \bullet } ( X )
$$

where $\mathcal { B } ^ { \ast } = \mathcal { B } _ { n } ^ { \ast }$ on $S _ { n } ( X )$

Lemma 17.8. ${ \mathcal { B } } : S _ { \bullet } ( X )  S _ { \bullet } ( X )$ is a chain map. Moreover, it is chain homotopic to the identity map.

Proof. The previous lemma implies

$$
\begin{array} { r } { \partial _ { n } \circ \mathcal { B } _ { n } ^ { * } = \tilde { \partial } _ { n } ^ { * } \circ \mathcal { B } _ { n } ^ { * } = ( \mathcal { B } _ { n } \circ \tilde { \partial } _ { n } ) ^ { * } = ( \tilde { \partial } _ { n } \circ \mathcal { B } _ { n - 1 } ) ^ { * } = \mathcal { B } _ { n - 1 } ^ { * } \circ \partial _ { n } . } \end{array}
$$

This show that ${ \mathcal { B } } ^ { * }$ is a chain map.

To show the chain homotopy, it is enough to construct $T _ { n + 1 } \in S _ { n + 1 } \big ( \Delta ^ { n } \big )$ such that

$$
\mathcal { B } _ { n } - 1 _ { \Delta ^ { n } } = T _ { n + 1 } \circ \tilde { \partial } _ { n + 1 } + \tilde { \partial } _ { n } \circ T _ { n } .
$$

Here $1 _ { \Delta ^ { n } } : \Delta ^ { n } \to \Delta ^ { n }$ is the identity map, viewed as a n-chain. Then $T _ { n + 1 } ^ { * }$ gives the required homotopy. T is constructed inductively in n as follows. $T _ { 1 } = 0 .$ . Suppose we have constructed $T _ { n }$ . We need to find $T _ { n + 1 }$ such that

$$
\partial ( T _ { n + 1 } ) = \mathcal { B } _ { n } - 1 _ { \Delta ^ { n } } - \tilde { \partial } _ { n } \circ T _ { n } .
$$

Observe

$$
\begin{array} { r } { \partial \left( \mathcal { B } _ { n } - 1 _ { \Delta ^ { n } } - \tilde { \partial } _ { n } \circ T _ { n } \right) = \left( \mathcal { B } _ { n } - 1 _ { \Delta ^ { n } } - \tilde { \partial } _ { n } \circ T _ { n } \right) \circ \tilde { \partial } _ { n } = \tilde { \partial } _ { n } \circ \left( \mathcal { B } _ { n - 1 } - 1 _ { \Delta ^ { n - 1 } } - T _ { n } \circ \tilde { \partial } _ { n } \right) = \tilde { \partial } _ { n } \circ \tilde { \partial } _ { n - 1 } \circ T _ { n - 1 } = 0 . } \end{array}
$$

Therefore $\mathcal { B } _ { n } - 1 _ { \Delta ^ { n } } - \tilde { \partial } _ { n } \circ T _ { n }$ is a n-cycle. However $\mathrm { H } _ { n } ( \Delta ^ { n } ) = 0 { \mathrm { ~ f o r ~ } } n \geq 1$ . It follows that $T _ { n + 1 }$ can be constructed.

Corollary 17.9. The barycentric subdivision map ${ \mathcal { B } } ^ { * } : S _ { \bullet } ( X ) \to S _ { \bullet } ( X )$ is a quasi-isomorphism.

Excision.

Theorem 17.10 (Excision). Let $U \subset A \subset X$ be subspaces such that ${ \bar { U } } \subset A ^ { \circ }$ (the interior of A). Then the inclusion $i : ( X - U , A - U ) \hookrightarrow ( X , A )$ induces isomorphisms

$$
i _ { * } : \mathrm { H } _ { n } ( X - U , A - U ) \cong \mathrm { H } _ { n } ( X , A ) , \quad \forall n .
$$

Proof. Let us call $\sigma : \Delta ^ { n } \to X$ small if

$$
\sigma ( \Delta ^ { n } ) \subset A \quad { \mathrm { o r } } \quad \sigma ( \Delta ^ { n } ) \subset X - U .
$$

Let $S _ { \bullet } ^ { \prime } ( X ) \subset S _ { \bullet } ( X )$ denote the subcomplex generated by small simplexes, and $S _ { \bullet } ^ { \prime } ( X , A )$ defined by the exact sequence

$$
0 \to S _ { \bullet } ( A ) \to S ^ { \prime } ( X ) \to S ^ { \prime } ( X , A ) \to 0 .
$$

It is easy to see that

$$
S _ { \bullet } ^ { \prime } ( X , A ) \cong S _ { \bullet } ( X - U , A - U ) .
$$

There is a natural commutative diagram of chain maps

$$
\begin{array} { r l r } { 0 \longrightarrow S _ { \bullet } ( A ) \longrightarrow S _ { \bullet } ^ { \prime } ( X ) \longrightarrow S _ { \bullet } ^ { \prime } ( X , A ) \longrightarrow 0 } \\ & { \downarrow } & { \downarrow } \\ { 0 \longrightarrow S _ { \bullet } ( A ) \longrightarrow S _ { \bullet } ( X ) \longrightarrow S _ { \bullet } ( X , A ) \longrightarrow 0 } \end{array}
$$

By the Five Lemma, it is enough to show that

$$
S _ { \bullet } ^ { \prime } ( X )  S _ { \bullet } ( X )
$$

is a quasi-isomorphism.

(1) Injectivity of $\operatorname { H } ( S _ { \bullet } ^ { \prime } ( X ) ) \to \operatorname { H } ( S _ { \bullet } ( X ) ) \colon$

Let α be a cycle in $S _ { \bullet } ^ { \prime } ( X )$ and $\alpha = \partial \beta$ for $\beta \in S _ { \bullet } ( X )$ . Take k big enough that $( { \mathcal { B } } ^ { \ast } ) ^ { k } ( { \boldsymbol { \beta } } ) \in S ^ { \prime } ( X )$ . Then

$$
\begin{array} { r } { ( \mathcal { B } ^ { * } ) ^ { k } ( \alpha ) = \partial ( \mathcal { B } ^ { * } ) ^ { k } ( \beta ) . } \end{array}
$$

Hence $( \mathcal { B } ^ { \ast } ) ^ { k } ( \alpha )$ is zero in $\mathrm { H } ( S _ { \bullet } ^ { \prime } ( X ) )$ , so is α which is homologous to $( \mathcal { B } ^ { \ast } ) ^ { k } ( \alpha )$

(2) Surjectivity of $\mathrm { H } ( S _ { \bullet } ^ { \prime } ( X ) )  \mathrm { H } ( S _ { \bullet } ( X ) )$

Let α be a cycle in $S _ { \bullet } ( X )$ . Take k big enough that $( \mathcal { B } ^ { \ast } ) ^ { k } ( \alpha ) \in S _ { \bullet } ^ { \prime } ( X )$ . Then $( \mathcal { B } ^ { \ast } ) ^ { k } ( \alpha )$ is a small cycle which is homologous to α. 

Theorem 17.11. Let $X _ { 1 } , X _ { 2 }$ be subspaces of X and $X = X _ { 1 } ^ { \circ } \cup X _ { 2 } ^ { \circ }$ . Then

$$
\mathrm { H } _ { \bullet } ( X _ { 1 } , X _ { 1 } \cap X _ { 2 } ) \to \mathrm { H } _ { \bullet } ( X , X _ { 2 } )
$$

is an isomorphism for all n.

Proof. Apply Excision to $U = X - X _ { 1 } , A = X _ { 2 }$

Theorem 17.12 (Mayer-Vietoris). Let $X _ { 1 } , X _ { 2 }$ be subspaces of X and $X = X _ { 1 } ^ { \circ } \cup X _ { 2 } ^ { \circ }$ . Then there is an exact sequence

$$
\begin{array} { r } { \cdot \cdot \cdot  \mathrm { H } _ { n } ( X _ { 1 } \cap X _ { 2 } ) \overset { ( i _ { 1 } , . . , i _ { 2 } ) } {  } \mathrm { H } _ { n } ( X _ { 1 } ) \oplus \mathrm { H } _ { n } ( X _ { 2 } ) \overset { j _ { 1 } , . . - j _ { 2 } } {  } \mathrm { H } _ { n } ( X ) \overset { \delta } {  } \mathrm { H } _ { n - 1 } ( X _ { 1 } \cap X _ { 2 } )  \cdot \cdot \cdot } \end{array}
$$

It is also true for the reduced homology.

Proof. Let $S _ { \bullet } ( X _ { 1 } ) + S _ { \bullet } ( X _ { 2 } ) \subset S _ { \bullet } ( X )$ be the subspace spanned by $S _ { \bullet } ( X _ { 1 } )$ and $S _ { \bullet } ( X _ { 2 } )$ . We have a short exact sequence

$$
0 \to S _ { \bullet } ( X _ { 1 } \cap X _ { 2 } ) \stackrel { ( i _ { 1 } , i _ { 2 } ) } { \to } S _ { \bullet } ( X _ { 1 } ) \oplus S _ { \bullet } ( X _ { 2 } ) \stackrel { j _ { 1 } - j _ { 2 } } { \to } S _ { \bullet } ( X _ { 1 } ) + S _ { \bullet } ( X _ { 2 } ) \to 0 .
$$

Similar to the proof of Excision via barycentric subdivision, the embedding $S _ { \bullet } ( X _ { 1 } ) + S _ { \bullet } ( X _ { 2 } ) \subset S _ { \bullet } ( X )$ is a quasi-isomorphism. Mayer-Vietoris sequence follows. 

Theorem 17.13. Let $A \subset X$ be a closed subspace. Assume A is a strong deformation retract of a neighborhood in X. Then the map $( X , A ) \to ( X / A , A / A )$ induces an isomorphism

$$
\mathrm { H } _ { \bullet } ( X , A ) \cong \tilde { \mathrm { H } } _ { \bullet } ( X / A ) .
$$

Proof. Let U be an open neighborhood of A that deformation retracts to A. Then $\mathrm { H } _ { \bullet } ( A ) \cong \mathrm { H } _ { \bullet } ( U )$ , hence

$$
\mathrm { H } _ { \bullet } ( X , A ) \cong \mathrm { H } _ { \bullet } ( X , U )
$$

by Five Lemma. Since A is closed and U is open, we can apply Excision to find

$$
\mathrm { H } _ { \bullet } ( X , A ) \cong \mathrm { H } _ { \bullet } ( X , U ) \cong \mathrm { H } _ { \bullet } ( X - A , U - A ) .
$$

The same consideration applied to $\left( X / A , A / A \right)$ and $U / A$ gives

$$
\mathrm { H } _ { \bullet } \big ( X / A , A / A \big ) \cong \mathrm { H } _ { \bullet } \big ( X / A - A / A , U / A - A / A \big ) = \mathrm { H } _ { \bullet } \big ( X - A , U - A \big ) .
$$

This Theorem in particular applies to cofibrations.

## 18. HOMOLOGY OF SPHERES

Theorem 18.1. The reduced homology of the sphere Sn is given by

$$
{ \tilde { \mathrm { H } } } _ { k } ( S ^ { n } ) = { \left\{ \begin{array} { l l } { \mathbb { Z } } & { k = n } \\ { 0 } & { k \neq n } \end{array} \right. }
$$

Proof. Let $S ^ { n } = D _ { + } ^ { n } \cup D _ { - } ^ { n }$ , where $D _ { + } ^ { n } ~ ( D _ { - } ^ { n } )$ is the upper (lower) hemi-sphere and we choose a bit bigger ones to satisfy excision. $D _ { + } ^ { n } \cap D _ { - } ^ { n } = S ^ { n - 1 } \times I \simeq S ^ { n - 1 }$ . Apply Mayer-Vietoris sequence we find

$$
\begin{array} { r } { \tilde { \mathrm { H } } _ { k } \mathopen { } \mathclose \bgroup \left( S ^ { n } \aftergroup \egroup \right) = \tilde { \mathrm { H } } _ { k - 1 } \mathopen { } \mathclose \bgroup \left( S ^ { n - 1 } \aftergroup \egroup \right) . } \end{array}
$$

The theorem follows.

Corollary 18.2. If m $\neq n$ , then $\mathbb { R } ^ { m }$ and $\mathbb { R } ^ { n }$ are not homeomorphic.

Definition 18.3. A continous map $f : S ^ { n }  S ^ { n } \ : ( n \geq 0 )$ has degree d, denoted by $\deg ( f ) = d ,$ if

$$
f _ { * } : \tilde { \mathrm { H } } _ { n } ( S ^ { n } ) = \mathbb { Z } \to \tilde { \mathrm { H } } _ { n } ( S ^ { n } ) = \mathbb { Z }
$$

is multiplication by d.

Lemma 18.4. Let $f , g : S ^ { n } \to S ^ { n }$ be continuous maps.

(1) $\deg ( f \circ g ) = \deg ( f ) \deg ( g )$

(2) $I f f \simeq g$ are homotopic, then $\deg ( f ) = \deg ( g )$

(3) $_ { I f f }$ is a homotopy equivalence, then $\deg ( f ) = \pm 1$

Proposition 18.5. Let $r : S ^ { n } \to S ^ { n } , ( x _ { 0 } , \cdot \cdot \cdot , x _ { n } ) \to ( - x _ { 0 } , x _ { 1 } , \cdot \cdot \cdot , x _ { n } )$ be the reflection. Then

$$
\deg ( r ) = - 1 .
$$

Proof. Prove by induction on n. This is true for $n = 0 .$ . The induction follows from the commutative diagram

$$
\begin{array} { r l r } & { } & { \tilde { \mathrm { H } } _ { n } ( S ^ { n } ) \xrightarrow { \delta } \tilde { \mathrm { H } } _ { n - 1 } ( S ^ { n - 1 } ) } \\ & { } & { \qquad \downarrow } \\ & { } & { \qquad \forall } \\ & { } & { \tilde { \mathrm { H } } _ { n } ( S ^ { n } ) \xrightarrow { \delta } \tilde { \mathrm { H } } _ { n - 1 } ( S ^ { n - 1 } ) } \end{array}
$$

Corollary 18.6. Let $\sigma : S ^ { n }  S ^ { n } , ( x _ { 0 } , \cdot \cdot \cdot , x _ { n } )  ( - x _ { 0 } , \cdot \cdot \cdot , - x _ { n } )$ be the antipodal map. Then

$$
\deg ( \sigma ) = ( - 1 ) ^ { n + 1 } .
$$

Proof. σ is a composition of $n + 1$ reflections.

Theorem 18.7 (Hairy Ball Theorem). $S ^ { n }$ has a nowhere vanishing tangent vector field if and only if n is odd.

Proof. If n is odd, we construct

$$
v ( x _ { 0 } , \cdot \cdot \cdot , x _ { n } ) = ( - x _ { 1 } , x _ { 0 } , - x _ { 3 } , x _ { 2 } , \cdot \cdot \cdot ) .
$$

Conversely, assume v is no-where vanishing vector field. Let

$$
f : S ^ { n } \to S ^ { n } , \quad x \to { \frac { v ( x ) } { | v ( x ) | } } .
$$

The map

$$
F : S ^ { n } \times I  S ^ { n } , \quad F ( x , t ) = \cos ( \pi t ) x + \sin ( \pi t ) f ( x )
$$

defines a homotopy between the identity map 1 and the antipodal map σ. It follows that

$$
\deg ( \sigma ) = 1 \Longrightarrow n = \mathrm { o d d } .
$$

Theorem 18.8 (Brower’s Fixed Point Theorem). Any continuous map $f : D ^ { n } \to D ^ { n }$ has a fixed point.

Proof. Assume f has no fixed point. Define

$$
r : D ^ { n } \to S ^ { n - 1 }
$$

where $r ( p )$ is the intersection of $\partial D ^ { n }$ with the ray starting from $f ( p )$ pointing toward $p .$ Then r defines a retract of $S ^ { n - 1 } \hookrightarrow D ^ { n }$ . This implies ${ \mathrm { H } } _ { \bullet } ( D ^ { n } ) = { \mathrm { H } } _ { \bullet } ( S ^ { n - 1 } ) \oplus { \mathrm { H } } _ { \bullet } ( D ^ { n } , S ^ { n - 1 } )$ , a contradiction.

We give a geometric interpretation of the degree of $f : S ^ { n } \to S ^ { n }$ . Let $V \subset S ^ { n }$ be a small open ball such that $f ^ { - 1 } ( V ) \to V$ is a disjoint union of open balls

$$
f ^ { - 1 } ( V ) = U _ { 1 } \cup \cdot \cdot \cdot \cup U _ { d } .
$$

Let $f _ { i } : { \bar { U } } _ { i } / \partial { \bar { U } } _ { i } \cong S ^ { n }  { \bar { V } } / \partial { \bar { V } } \cong S ^ { n }$ . We have the commutative diagram

$$
\begin{array}{c} \begin{array} { l l } { { \mathrm { H } _ { n } ( S ^ { n } ) \longrightarrow \mathrm { H } _ { n } ( S ^ { n } / S ^ { n } - \cup _ { i } U _ { i } ) \cong \oplus _ { i } H _ { n } ( S ^ { n } ) } } \\ { { \Bigg \downarrow _ { * } } } \\ { { \mathrm { H } _ { n } ( S ^ { n } ) \longrightarrow \mathrm { H } _ { n } ( S ^ { n } / S ^ { n } - V ) \cong H _ { n } ( S ^ { n } ) } } \end{array} \downarrow \oplus _ { i } ( f _ { i } ) _ { * }  \end{array}
$$

It is easy to see that first row is $k  ( k , k , \cdots , k )$ and the second row is $k  k .$ It follows that

$$
\deg ( f ) = \sum _ { i = 1 } ^ { d } \deg ( f _ { i } ) .
$$

Note that when $f ^ { - 1 } ( V ) \to V$ is a covering map, then $f : U _ { i } \to V$ is a homeomorphism. We have $\deg ( f _ { i } ) = \pm 1$ and $\deg ( f )$ is given by a counting with signs.

Example 18.9. Identify $S ^ { 2 } = \mathbb { C } \cup \{ \infty \}$ . Consider the map $f : S ^ { 2 } \to S ^ { 2 } , z \to z ^ { k }$ . Then $\deg ( f ) = k .$

## 19. CELLULAR HOMOLOGY

Cellular homology.

Definition 19.1. Let $( X , A )$ be a relative CW complex with skeletons: $A = X ^ { - 1 } \subset X ^ { 0 } \subset \cdots \subset X ^ { n } \subset \cdot \cdot \cdot$ We define the relative cellular chain complex $( C _ { \bullet } ^ { c e l l } ( X , A ) , \partial )$

$$
\cdot \cdot \cdot \to C _ { n } ^ { c e l l } ( X , A ) \stackrel { \partial } { \to } C _ { n - 1 } ^ { c e l l } ( X , A ) \stackrel { \partial } { \to } \cdot \cdot \cdot \to C _ { 0 } ^ { c e l l } ( X , A ) \to 0
$$

where $\boxed { C _ { n } ^ { c e l l } ( X , A ) : = \mathrm { H } _ { n } \bigl ( X ^ { n } , X ^ { n - 1 } \bigr ) }$ and the boundary map ∂ is defined by the commutative diagram

$$
{ \mathrm { H } } _ { n } ( X ^ { n } , X ^ { n - 1 } ) \xrightarrow { \qquad \quad > \quad \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Sigma } \qquad \quad > \mathrm { H } _ { n - 1 } ( X ^ { n - 1 } , X ^ { n - 2 } ) }
$$

Here $\delta$ is the connecting map of relative homology for $A \subset X ^ { n - 1 } \subset X ^ { n }$ and $j$ is the natural map.

Assume $X ^ { n }$ is obtained from $X ^ { n - 1 }$ by attaching n-cells indexed by $J _ { n }$

$$
\begin{array} { r l r } & { \underset { \alpha \in J _ { n } } { \mathrm { I I } } S ^ { n - 1 } \xrightarrow { f } X ^ { n - 1 } } & \\ & { \underset { \alpha \in J _ { n } } { \mathrm { \widehat { I } } } \overset { \biggr \Updownarrow } { \underset { \alpha \in J _ { n } } { \mathrm { \widehat { I } } } } \overset { \biggr \Updownarrow } { \underset { \alpha } { \mathrm { \widehat { I } } } } } & \end{array}
$$

Since $X ^ { n - 1 } \hookrightarrow X ^ { n }$ is a cofibration,

$$
C _ { n } ^ { c e l l } ( X , A ) \cong \tilde { \mathrm { H } } _ { n } ( X ^ { n } / X ^ { n - 1 } ) \cong \bigoplus _ { J _ { n } } \tilde { \mathrm { H } } _ { n } ( S ^ { n } ) \cong \bigoplus _ { J _ { n } } \mathbb { Z }
$$

is the free abelian group generated by each attached $\mathrm { H } _ { n } ( D ^ { n } , S ^ { n - 1 } )$ . Using the diagram

<!-- image-->

and $\delta _ { n - 1 } \circ j _ { n } = 0 ,$ , we see that

$$
\partial _ { n - 1 } \circ \partial _ { n } = j _ { n - 1 } \circ \delta _ { n - 1 } \circ j _ { n } \circ \delta _ { n } = 0 .
$$

Therefore $( C _ { \bullet } ^ { c e l l } ( X , A ) , \partial )$ indeed defines a chain complex.

Definition 19.2. Let $( X , A )$ be a relative CW complex. We define its n-th relative cellular homology by

$$
{ \boxed { \mathbf { H } _ { n } ^ { c e l l } ( X , A ) : = \mathbf { H } _ { n } ( C _ { \bullet } ^ { c e l l } ( X , A ) , \partial ) } } .
$$

When $A = \emptyset$ , we simply denote it by $\operatorname { H } _ { n } ^ { c e l l } ( X )$ called the n-th cellular homology.

Lemma 19.3. Let $( X , A )$ be a relative CW complex. Let $0 \leq q < p \leq \infty$ . Then

$$
{ \mathrm { H } } _ { n } ( X ^ { p } , X ^ { q } ) = 0 , \quad n \leq q \quad o r \quad n > p .
$$

Theorem 19.4. Let $( X , A )$ be a relative CW complex. Then cellular homology coincides with singular homology

$$
\boxed { \mathrm { H } _ { n } ^ { c e l l } ( X , A ) \cong \mathrm { H } _ { n } ( X , A ) } .
$$

Proof. Consider the following commutative diagram

$$
\begin{array}{c} \mathbf { H } _ { n + 1 } ( X ^ { n + 1 } , X ^ { n } ) \quad \quad \quad \quad \quad \quad \quad \mathbf { H } _ { n + 1 } ( X ^ { n + 1 } , X ^ { n } ) \quad \quad \quad \quad \quad \quad \quad \quad \mathbf { a } _ { n + 1 } \quad \quad \quad \quad \quad \quad \quad \quad \mathbf { H } _ { n } ( X ^ { n - 2 } , A ) ( = 0 )  \\ { \mathbf { H } _ { n } ( X ^ { n - 1 } , A ) ( = 0 ) \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \mathbf { V } _ { n } ( X ^ { n } , A ) \quad \quad \quad \quad \quad \quad \quad \quad \mathbf { H } _ { n } ( X ^ { n } , X ^ { n - 1 } ) \underbrace { \quad \quad \quad \quad \quad \quad \quad } _ { \mathrm { H } _ { n - 1 } ( X ^ { n - 1 } , A ) } } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \mathbf { H } _ { n } ( X ^ { n + 1 } , A ) \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \mathbf { H } _ { n - 1 } ( X ^ { n - 1 } , X ^ { n - 2 } ) \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \mathbf { H } _ { n } ( X ^ { n + 1 } , X ^ { n } ) ( = 0 ) \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \mathbf { H } _ { n - 1 } ( X ^ { n - 2 } , A ) ( = 0 ) } \end{array}
$$

Diagram chasing implies $\mathrm { H } _ { n } \bigl ( X ^ { n + 1 } , A \bigr ) \cong \mathrm { H } _ { n } ^ { c e l l } ( X , A )$ . Theorem follows from the exact sequence

$$
{ \mathrm { H } } _ { n + 1 } ( X , X ^ { n + 1 } ) ( = 0 ) \to { \mathrm { H } } _ { n } ( X ^ { n + 1 } , A ) \to { \mathrm { H } } _ { n } ( X , A ) \to { \mathrm { H } } _ { n } ( X , X ^ { n + 1 } ) ( = 0 )
$$

Let $f : ( X , A ) \to ( Y , B )$ ) be a cellular map. It induces a map on cellular homology

$$
f _ { * } : { \mathrm { H } } _ { \bullet } ^ { c e l l } ( X , A ) \to { \mathrm { H } } _ { \bullet } ^ { c e l l } ( Y , B ) .
$$

Therefore in the category of CW complexes, we can work entirely with cellular homology which is combinatorially easier to compute by the next formula.

Cellular Boundary Formula.

Let us now analyze cellular differential

$$
\partial _ { n } : \mathrm { H } _ { n } ( X ^ { n } , X ^ { n - 1 } ) \to \mathrm { H } _ { n - 1 } ( X ^ { n - 1 } , X ^ { n - 2 } ) .
$$

For each n-cell $e _ { \alpha } ^ { n } ,$ we have the gluing map

$$
f _ { e _ { \alpha } ^ { n } } : S ^ { n - 1 } \to X ^ { n - 1 } .
$$

This defines a map

$$
{ \bar { f } } _ { e _ { \alpha } ^ { n } } : S ^ { n - 1 } \to X ^ { n - 1 } / X ^ { n - 2 } = \bigvee _ { J _ { n - 1 } } S ^ { n - 1 }
$$

which induces a degree map

$$
( \bar { f } _ { e _ { \alpha } ^ { n } } ) _ { * } : \tilde { \mathrm { H } } _ { n - 1 } ( S ^ { n - 1 } ) \cong \mathbb { Z } \to \bigoplus _ { J _ { n - 1 } } \tilde { \mathrm { H } } _ { n - 1 } ( S ^ { n - 1 } ) \cong \bigoplus _ { J _ { n - 1 } } \mathbb { Z } .
$$

Collecting all n-cells, this generates the degree map

$$
d _ { n } : \bigoplus _ { J _ { n } } \mathbb { Z } \to \bigoplus _ { J _ { n - 1 } } \mathbb { Z } .
$$

Theorem 19.5. Under the identification $C _ { n } ^ { c e l l } ( X ^ { n } , X ^ { n - 1 } ) \cong \bigoplus _ { J _ { n } } \mathbb { Z } ,$ cellular differential coincides with the degree map

$$
{ \sqrt { \partial _ { n } \cong d _ { n } } } ~ .
$$

Example 19.6. $\mathbb { C } P ^ { n }$ has a CW structure with a single 2m-cell for each m $\leq n .$ Since there is no odd dim cells, the degree map $d = 0$ . We find

$$
\mathrm { H } _ { k } ( \mathbb { C } P ^ { n } ) = { \left\{ \begin{array} { l l } { \mathbb { Z } } & { k = 0 , 2 , \cdots , 2 n } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

Example 19.7. A closed oriented surface $\Sigma _ { g }$ of genus g has a CW structure with a 0-cell, 2g 1-cells, and a 2-cell. It is easy to see that the degree map is zero. We find

$$
\mathrm { H } _ { k } ( \Sigma _ { g } ) = \left\{ \begin{array} { l l } { \mathbb { Z } } & { k = 0 } \\ { \mathbb { Z } ^ { 2 g } } & { k = 1 } \\ { \mathbb { Z } } & { k = 2 } \\ { 0 } & { k > 2 . } \end{array} \right.
$$

Example 19.8. $\mathbb { R } P ^ { n }$ has a CW structure with a k-cell for each $0 \leq k \leq n$ . The degree map is $d _ { k } = 1 + ( - 1 ) ^ { k }$

$$
\mathbf { H } _ { k } ( \mathbb { R } P ^ { n } ) = { \left\{ \begin{array} { l l } { \mathbb { Z } } & { k = 0 } \\ { \mathbb { Z } / 2 \mathbb { Z } } & { 0 < k < n , k { \mathrm { ~ o d d } } } \\ { \mathbb { Z } } & { k = n = { \mathrm { o d d } } } \\ { 0 } & { k = n = { \mathrm { e v e n } } } \\ { 0 } & { k > n } \end{array} \right. }
$$

Euler characteristic.

Definition 19.9. Let X be a finite CW complex of dimension n and denote by $c _ { i }$ the number of i-cells of X. The Euler characteristic of X is defined as:

$$
\chi ( X ) : = \sum _ { i } ( - 1 ) ^ { i } c _ { i } .
$$

Recall that any finitely generaed abelian group G is decomposed into a free part and a torsion part

$$
G \cong \mathbb { Z } ^ { r } \oplus \mathbb { Z } / m _ { 1 } \mathbb { Z } \oplus \cdot \cdot \cdot \oplus \mathbb { Z } / m _ { k } \mathbb { Z } .
$$

The integer $r : = r k ( G )$ is called the rank of G.

Theorem 19.10. Let X be a finite CW complex. Then

$$
\boxed { \chi ( X ) = \sum _ { i } ( - 1 ) ^ { i } b _ { i } ( X ) }
$$

where $b _ { i } ( X ) : = r k ( \mathrm { H } _ { i } ( X ) )$ is called the i-th Betti number of X In particular, $\chi ( X )$ is independent of the chosen CW structure on X and only depend on the cellular homotopy class of X.

## 20. COHOMOLOGY AND UNIVERSAL COEFFICIENT THEOREM

Cohomology.

Definition 20.1. Let R be a commutative ring. A cochain complex over R is sequence of R-module maps

$$
\cdots \to C ^ { n - 1 } { \overset { d _ { n } } { \to } } 1 C ^ { n } { \overset { d _ { n } } { \to } } C ^ { n - 1 } \to \cdots
$$

such that $d _ { n } \circ d _ { n - 1 } = 0 \forall n$ . When R is not specified, we mean cochain complex of abelian groups (i.e. $R = \mathbb { Z } )$

Sometimes we just write the map by d and the cochain complex by $( C ^ { \bullet } , d )$ . Then $d _ { n } = d | _ { C _ { n } }$ and $d ^ { 2 } = 0$

Definition 20.2. Given a cochain complex $( C ^ { \bullet } , d )$ , its n-cocycles $Z ^ { n }$ and n-coboundaries $B ^ { n }$ are

$$
Z ^ { n } = \mathrm { K e r } ( d : C ^ { n } \to C ^ { n + 1 } ) , \quad B ^ { n } = \mathrm { I m } ( d : C ^ { n - 1 } \to C ^ { n } ) .
$$

$d ^ { 2 } = 0$ implies $B ^ { n } \subset Z ^ { n }$ . We define the n-th cohomology group by

$$
{ \boxed { \mathrm { H } ^ { n } ( C ^ { \bullet } , d ) : = { \frac { Z ^ { n } } { B ^ { n } } } = { \frac { \ker ( d _ { n } ) } { \operatorname { i m } ( d _ { n - 1 } ) } } } } .
$$

A cochain complex $C ^ { \bullet }$ is called acyclic or exact if $\mathrm { H } ^ { n } ( C ^ { \bullet } ) = 0 , \forall n$

We are interested in the following relation between cochain and chain complex.

Definition 20.3. Let $( C _ { \bullet } , \partial )$ be a chain complex over $R ,$ and G be a R-module. We define its dual cochain complex $( C ^ { \bullet } , d ) = \operatorname { H o m } _ { R } ( C _ { \bullet } , G )$ by

$$
\cdot \cdot \cdot \mathrm { H o m } _ { R } ( C _ { n - 1 } , G ) \to \mathrm { H o m } _ { R } ( C _ { n } , G ) \to \mathrm { H o m } _ { R } ( C _ { n + 1 } , G ) \to \cdot \cdot \cdot
$$

Here given $f \in { \mathrm { H o m } } _ { R } ( C _ { n } , G )$ , we define $d _ { n } f \in { \mathrm { H o m } } _ { R } ( C _ { n + 1 } , G )$ by

$$
d _ { n } f ( c ) : = f ( \partial _ { n + 1 } ( c ) ) , \quad \forall c \in C _ { n + 1 } .
$$

Definition 20.4. Let G be an abelian group and X be a topological space. For $n \geq 0 ,$ we define the group of singular n-cochains in X with coefficient in G to be

$$
S ^ { n } ( X ; G ) : = \operatorname { H o m } ( S _ { n } ( X ) , G ) .
$$

The dual cochain complex $S ^ { \bullet } ( X ; G ) = \operatorname { H o m } ( S _ { \bullet } ( X ) , G )$ is called the singular cochain complex with coefficient in G. Its cohomology is called the singular cohomology with coefficient in $G ,$ denoted by

$$
\mathrm { H } ^ { n } ( X ; G ) : = \mathrm { H } ^ { n } ( S ^ { \bullet } ( X ; G ) ) .
$$

When $G = \mathbb { Z } ,$ we simply write it as $\mathrm { H } ^ { n } ( X )$

Theorem 20.5. $\mathrm { H } ^ { n } ( - ; G )$ defines a contra-variant functor

$$
\mathrm { H } ^ { n } ( - ; G ) : \underline { { { \mathrm { h T o p } } } } \to \underline { { { \mathrm { A b } } } } .
$$

Example 20.6 (Dimension Axiom). Let X be a point. Then

$$
\begin{array} { r } { \mathrm { H } ^ { n } ( X ; G ) = \left\{ \begin{array} { l l } { G } & { k = 0 } \\ { 0 } & { k > 0 } \end{array} \right. } \end{array}
$$

Lemma 20.7. Let G be a R-module. $I f 0 \to A _ { 1 } \to A _ { 2 } \to A _ { 3 } \to 0$ is an exact sequence of R-modules, then applying Hom $\iota _ { R } ( - , G )$ gives an exact sequence

$$
0 \to \operatorname { H o m } _ { R } ( A _ { 3 } , G ) \to \operatorname { H o m } _ { R } ( A _ { 2 } , G ) \to \operatorname { H o m } _ { R } ( A _ { 1 } , G ) .
$$

$I f A _ { 3 }$ is a free R-module (or more generally projective R-module), then the last morphism is also surjective.

Definition 20.8. Let G be an abelian group. Let $A \subset X$ be a subspace. We define the relative singular cochain complex with coefficient in G by

$$
\begin{array} { r } { S ^ { \bullet } ( X , A ; G ) : = \operatorname { H o m } ( S _ { \bullet } ( X ) / S _ { \bullet } ( A ) , G ) . } \end{array}
$$

Its cohomology is called the relative singular cohomology, denoted by $\mathrm { H } ^ { \bullet } ( X , A ; G )$

Since $S _ { \bullet } ( X ) / S _ { \bullet } ( A )$ is a free abelian group, we have a short exact sequence of cochain complex

$$
0 \to S ^ { \bullet } ( X , A ; G ) \to S ^ { \bullet } ( X ; G ) \to S ^ { \bullet } ( A ; G ) \to 0
$$

which induces a long exact sequence of cohomology groups

$$
0 \to \mathrm { H } ^ { 0 } ( X , A ; G ) \to \mathrm { H } ^ { 0 } ( X ; G ) \to \mathrm { H } ^ { 0 } ( A ; G ) \to \mathrm { H } ^ { 1 } ( X , A ; G ) \to \cdots .
$$

Moreover, the connecting maps

$$
\delta : \mathrm { H } ^ { n } ( A , G )  \mathrm { H } ^ { n + 1 } ( X , A ; G )
$$

is natural in the same sense as homology case.

Theorem 20.9 (Excision). Let $U \subset A \subset X$ be subspaces such that ${ \bar { U } } \subset A ^ { \circ }$ (the interior of A). Then the inclusion $i : ( X - U , A - U ) \hookrightarrow ( X , A )$ induces isomorphisms

$$
i ^ { * } : \mathrm { H } ^ { n } ( X , A ; G ) \cong \mathrm { H } ^ { n } ( X - U , A - U ; G ) , \quad \forall n .
$$

Universal Coefficient Theorem for Cohomology.

Definition 20.10. Let M, N be two R-modules. Let $P _ { \bullet }  M$ be a free R-module resolution of M:

$$
\cdot \cdot \cdot P _ { n }  P _ { n - 1 }  \cdot \cdot \cdot P _ { 1 }  P _ { 0 }  M  0
$$

is an exact sequence of R-modules and $P ^ { i } { ^ , } _ { \mathrm { { s } } }$ are free. We define the Ext group

$$
\mathrm { E x t } _ { R } ^ { k } ( M , N ) = \mathrm { H } ^ { k } ( \mathrm { H o m } ( P _ { \bullet } , N ) )
$$

and the Tor group

$$
\operatorname { T o r } _ { k } ^ { R } ( M , N ) = \mathrm { H } _ { k } ( P _ { \bullet } \otimes _ { R } N ) .
$$

Note that

$$
\operatorname { E x t } _ { R } ^ { 0 } ( M , N ) = \operatorname { H o m } _ { R } ( M , N ) , \quad \operatorname { T o r } _ { 0 } ^ { R } ( M , N ) = M \otimes _ { R } N .
$$

Ext and Tor are called the derived functors of Hom and ⊗. It is a classical result in homological algebra that $\mathrm { E x t } _ { R } ^ { k } ( M , N )$ and $\mathrm { T o r } _ { k } ^ { R } ( M , N )$ don’t depend on the choice of resolution of M. They are functorial with respect to both variables and $\mathrm { T o r } _ { k } ^ { R }$ is symmetric in two variables

$$
\mathrm { T o r } _ { k } ^ { R } ( M , N ) = \mathrm { T o r } _ { k } ^ { R } ( N , M ) .
$$

Moreover, for any short exact sequence of R-modules

$$
0  M _ { 1 }  M _ { 2 }  M _ { 3 }  0
$$

there associate long exact sequences

$$
{ \begin{array} { r l } & { 0 \to \operatorname { H o m } _ { R } ( M _ { 3 } , N ) \to \operatorname { H o m } _ { R } ( M _ { 2 } , N ) \to \operatorname { H o m } _ { R } ( M _ { 1 } , N ) } \\ & { \quad \to \operatorname { E x t } _ { R } ^ { 1 } ( M _ { 3 } , N ) \to \operatorname { E x t } _ { R } ^ { 1 } ( M _ { 2 } , N ) \to \operatorname { E x t } _ { R } ^ { 1 } ( M _ { 1 } , N ) } \\ & { \quad \to \operatorname { E x t } _ { R } ^ { 2 } ( M _ { 3 } , N ) ) \to \operatorname { E x t } _ { R } ^ { 2 } ( M _ { 2 } , N ) \to \operatorname { E x t } _ { R } ^ { 2 } ( M _ { 1 } , N ) \to \cdots } \end{array} }
$$

and

$$
\begin{array} { r l } & { 0 \to \mathrm { H o m } _ { R } ( N , M _ { 1 } ) \to \mathrm { H o m } _ { R } ( N , M _ { 2 } ) \to \mathrm { H o m } _ { R } ( N , M _ { 3 } ) } \\ & { \quad \to \mathrm { E x t } _ { R } ^ { 1 } ( N , M _ { 1 } ) \to \mathrm { E x t } _ { R } ^ { 1 } ( N , M _ { 2 } ) \to \mathrm { E x t } _ { R } ^ { 1 } ( N , M _ { 3 } ) } \\ & { \quad \to \mathrm { E x t } _ { R } ^ { 2 } ( N , M _ { 1 } ) ) \to \mathrm { E x t } _ { R } ^ { 2 } ( N , M _ { 2 } ) \to \mathrm { E x t } _ { R } ^ { 2 } ( N , M _ { 3 } ) \to \cdots } \end{array}
$$

and

$$
\begin{array} { r l } & { \cdot \cdot \cdot  \operatorname { T o r } _ { 2 } ^ { R } ( M _ { 1 } , N )  \operatorname { T o r } _ { 2 } ^ { R } ( M _ { 2 } , N )  \operatorname { T o r } _ { 3 } ^ { R } ( M _ { 3 } , N ) } \\ & { \quad  \operatorname { T o r } _ { 1 } ^ { R } ( M _ { 1 } , N )  \operatorname { T o r } _ { 1 } ^ { R } ( M _ { 2 } , N )  \operatorname { T o r } _ { 1 } ^ { R } ( M _ { 3 } , N ) } \\ & { \quad  M _ { 1 } \otimes _ { R } N  M _ { 2 } \otimes _ { R } N  M _ { 3 } \otimes _ { R } N  0 } \end{array}
$$

Now we focus on the case of abelian groups $R = \mathbb { Z }$ . For any abelian group M, let $P _ { 0 }$ be a free abelian group such that $P _ { 0 } \to M$ is surjective. Let $P _ { 1 }$ be its kernel. Then $P _ { 1 }$ is also free and

$$
0 \to P _ { 1 } \to P _ { 0 } \to M \to 0
$$

defines a free resolution of abelian groups. This implies that

$$
\operatorname { E x t } ^ { k } ( M , N ) = 0 , \quad \operatorname { T o r } _ { k } ( M , N ) = 0 \quad { \mathrm { f o r } } \quad k \geq 2 .
$$

In the case of abelian groups we will simply denote

$$
{ \Big | } \operatorname { E x t } ( M , N ) : = \operatorname { E x t } _ { \mathbb { Z } } ^ { 1 } ( M . N ) , \quad \operatorname { T o r } ( M , N ) : = \operatorname { T o r } _ { 1 } ^ { \mathbb { Z } } ( M , N ) { \Big | } .
$$

Lemma 20.11. If either M is free or N is divisible, then $\operatorname { E x t } ( M , N ) = 0$

Proposition 20.12. Let $( C _ { \bullet } , \partial )$ be a chain complex of free abelian groups, then

$$
\mathrm { H } ^ { n } ( \mathrm { H o m } ( C _ { \bullet } , G ) ) \cong \mathrm { H o m } ( \mathrm { H } _ { n } ( C _ { \bullet } ) , G ) \oplus \mathrm { E x t } ( \mathrm { H } _ { n - 1 } ( C _ { \bullet } ) , G )
$$

Proof. Let $B _ { n }$ be n-boundaries and $Z _ { n }$ be n-cycles, which are both free. We have exact sequences

$$
0  B _ { n }  Z _ { n }  \mathrm { H } _ { n }  0 , \quad 0  Z _ { n }  C _ { n }  B _ { n - 1 }  0 .
$$

This implies exact sequences

$$
0 \to \operatorname { H o m } ( \mathrm { H } _ { n } , G ) \to \operatorname { H o m } ( Z _ { n } , G ) \to \operatorname { H o m } ( B _ { n } , G ) \to \operatorname { E x t } ( \mathrm { H } _ { n } , G ) \to 0
$$

and the split exact sequence

$$
0 \to \operatorname { H o m } ( B _ { n - 1 } , G ) \to \operatorname { H o m } ( C _ { n } , G ) \to \operatorname { H o m } ( Z _ { n } , G ) \to 0 .
$$

Consider the commutative diagram with exact columns

<!-- image-->

This implies a short exact sequence

$$
0 \to \operatorname { E x t } ( \mathrm { H } _ { n - 1 } , G ) \to \mathrm { H } ^ { n } ( \operatorname { H o m } ( C _ { \bullet } , G ) ) \to \operatorname { H o m } ( \mathrm { H } _ { n } , G ) \to 0
$$

which is also split due to the split of the middle column in the above diagram.

Theorem 20.13 (Universal Coefficient Theorem for Cohomology). Let G be an abelian group and X be a topological space. Then for any $n \geq 0$ , there exists a split exact sequence

$$
0 \to \operatorname { E x t } ( \operatorname { H } _ { n - 1 } ( X ) , G ) \to \operatorname { H } ^ { n } ( X ; G ) \to \operatorname { H o m } ( \operatorname { H } _ { n } ( X ) , G ) \to 0
$$

which induces isomorphisms

$$
\mathrm { H } ^ { n } ( X ; G ) \cong \mathrm { H o m } ( \mathrm { H } _ { n } ( X ) , G ) \oplus \mathrm { E x t } ( \mathrm { H } _ { n - 1 } ( X ) , G ) .
$$

Proof. Apply the previous Lemma to $C _ { \bullet } = S _ { \bullet } ( X )$

Universal Coefficient Theorem for Homology.

Definition 20.14. Let G be an abelian group. Let $A \subset X$ be a subspace. We define the relative singular chain complex with coefficient in G by

$$
S _ { \bullet } ( X , A ; G ) : = S _ { \bullet } ( X , A ) \otimes _ { \mathbb { Z } } G
$$

Its cohomology is called the relative singular homology with coefficient in $G ,$ denoted by $\mathrm { H } _ { \bullet } ( X , A ; G )$ When $A = \emptyset$ , we simply get the singular homology H•(X; G).

Similar long exact sequence for relative singular homologies follows from the exact sequence

$$
0 \to S _ { \bullet } ( A ; G ) \to S _ { \bullet } ( X ; G ) \to S _ { \bullet } ( X , A ; G ) \to 0 .
$$

Theorem 20.15 (Universal Coefficient Theorem for homology). Let G be an abelian group and X be a topological space. Then for any $n \geq 0 ,$ , there exists a split exact sequence

$$
0 \to \mathrm { H } _ { n } ( X ) \otimes G \to \mathrm { H } _ { n } ( X ; G ) \to \operatorname { T o r } ( \mathrm { H } _ { n - 1 } ( X ) , G ) \to 0
$$

which induces isomorphisms

$$
\mathrm { H } _ { n } ( X ; G ) \cong \mathrm { H } _ { n } ( X ) \otimes G \oplus \mathrm { T o r } ( \mathrm { H } _ { n - 1 } ( X ) , G ) .
$$

The proof is similar to the cohomology case.

## 21. EILENBERG-ZILBER THEOREM AND KUNNETH FORMULA¨

Eilenberg-Zilber Theorem.

Definition 21.1. Let $( C _ { \bullet } , \partial _ { C } )$ and $( D _ { \bullet } , \partial _ { D } )$ be two chain complexes. We define their tensor product $C _ { \bullet } \otimes D _ { \bullet }$ as the chain complex E

$$
\boxed { ( C _ { \bullet } \otimes D _ { \bullet } ) _ { k } : = \sum _ { p + q = k } C _ { p } \otimes D _ { q } }
$$

with the boundary map

$$
\partial ( c _ { p } \otimes d _ { q } ) : = \partial _ { C } ( c _ { p } ) \otimes d _ { q } + ( - 1 ) ^ { p } c _ { p } \otimes \partial _ { D } ( d _ { q } ) , \quad c _ { p } \in C _ { p } , d _ { q } \in D _ { q } .
$$

Proposition 21.2. Assume $C _ { \bullet }$ is chain homotopy equivalent to $C _ { \bullet } ^ { \prime }$ . Then $C _ { \bullet } \otimes D _ { \bullet }$ is chain homotopy equivalent to $C _ { \bullet } ^ { \prime } \otimes D _ { \bullet }$ .

We would like to compare two functors from Top $\times \mathrm { T o p }  \underline { { \mathrm { C h } } } .$

$$
S _ { \bullet } ( X \times Y ) , \quad S _ { \bullet } ( X ) \otimes S _ { \bullet } ( Y ) .
$$

We first observe that there exists a canonical isomorphism

$$
\mathrm { H } _ { 0 } ( X \times Y ) \cong \mathrm { H } _ { 0 } ( X ) \otimes \mathrm { H } _ { 0 } ( Y ) .
$$

The following theorem of Eilenberg-Zilber says that such initial condition determines a natural homotopy equivalent between the above two functors which is unique up to chain homotopy.

Theorem 21.3 (Eilenberg-Zilber). Let X, Y be two topological spaces. Then there exists a chain equivalence

$$
S _ { \bullet } ( X \times Y ) \xrightarrow [ { { \mathfrak { s } } \atop { \mathfrak { s } } } ] { \longrightarrow } S _ { \bullet } ( X ) \otimes S _ { \bullet } ( Y )
$$

which is natural with respect to $X , Y$ and induce the canonical isomorphism $\mathrm { H } _ { 0 } ( X \times Y ) \cong \mathrm { H } _ { 0 } ( X ) \otimes \mathrm { H } _ { 0 } ( Y )$ . Such chain equivalence is unique up to chain homotopy. In particular, there are canonical isomorphisms

$$
\mathrm { H } _ { n } ( X \times Y ) = \mathrm { H } _ { n } ( S _ { \bullet } ( X ) \otimes S _ { \bullet } ( Y ) ) , \quad \forall n \geq 0 .
$$

$F , G$ will be called Eilenberg-Zilber maps.

Proof. Observe that any map $\Delta ^ { p } \stackrel { ( \sigma _ { x } , \sigma _ { y } ) } {  } X \times Y$ factors through

$$
\Delta ^ { p } \stackrel { \delta _ { p } } {  } \Delta ^ { p } \times \Delta ^ { p } \stackrel { \sigma _ { x } \times \sigma _ { y } } {  } X \times Y
$$

where $\Delta ^ { p } \stackrel { \delta _ { p } } {  } \Delta ^ { p } \times \Delta ^ { p }$ is the diagonal map. This implies that a natural transformation of the functor $S _ { \bullet } ( - , - )$ is determined by its value on $\{ \delta _ { p } \} _ { p \ge 0 }$ . For example,

$$
F ( ( \sigma _ { x } , \sigma _ { y } ) ) = ( \sigma _ { x } \otimes \sigma _ { y } ) _ { * } F ( \delta _ { p } ) .
$$

Similarly, a natural transformation of the functor $S _ { \bullet } ( - ) \otimes S _ { \bullet } ( - )$ is determined by its value on $1 _ { p } \otimes 1 _ { q }$ where $1 _ { p } : \Delta ^ { p } \to \Delta ^ { p }$ is the identity map. For example, for any $\sigma _ { x } : \Delta ^ { p }  X , \sigma _ { y } : \Delta ^ { q }  Y ,$ we have

$$
G ( \sigma _ { x } \otimes \sigma _ { y } ) = ( \sigma _ { x } \times \sigma _ { y } ) _ { * } G ( 1 _ { p } \otimes 1 _ { q } ) .
$$

Therefore F and G are completely determined by

$$
f _ { n } : = F ( \delta _ { n } ) \in \bigoplus _ { p + q = n } S _ { p } ( \Delta ^ { n } ) \otimes S _ { q } ( \Delta ^ { n } ) , \quad g _ { n } : = \bigoplus _ { p + q = n } G ( 1 _ { p } \otimes 1 _ { q } ) \in \bigoplus _ { p + q = n } S _ { n } ( \Delta ^ { p } \times \Delta ^ { q } ) .
$$

We will use the same notations as in the discussion of Barycentric decomposition. Then

$$
f _ { n } \circ g _ { n } \simeq \delta _ { n } \in S _ { n } ( \Delta ^ { n } \times \Delta ^ { n } ) , \quad g _ { n } \circ f _ { n } \in \bigoplus _ { p + q = n } ( S _ { \bullet } ( \Delta ^ { p } ) \otimes S _ { \bullet } ( \Delta ^ { q } ) ) _ { n } .
$$

Let us denote the following complexes

$$
C _ { n } = \prod _ { k \geq 0 } ( S _ { \bullet } ( \Delta ^ { k } ) \otimes S _ { \bullet } ( \Delta ^ { k } ) ) _ { n + k } , \quad D _ { n } = \prod _ { m \geq 0 } \left( \bigoplus _ { p + q = m } S _ { n + p + q } ( \Delta ^ { p } \times \Delta ^ { q } ) \right)
$$

with boundary map

$$
\partial + \tilde { \partial } : C _ { n }  C _ { n - 1 } , \quad \partial + \tilde { \partial } : D _ { n }  D _ { n - 1 }
$$

as follows. ∂ is the usual boundary map of singular chain complexes

$$
\begin{array} { r } { \partial : ( S _ { \bullet } ( \Delta ^ { k } ) \otimes S _ { \bullet } ( \Delta ^ { k } ) ) _ { n } \to ( S _ { \bullet } ( \Delta ^ { k } ) \otimes S _ { \bullet } ( \Delta ^ { k } ) ) _ { n - 1 } , \quad \partial : \quad S _ { n } ( \Delta ^ { p } \times \Delta ^ { q } ) \to S _ { n - 1 } ( \Delta ^ { p } \times \Delta ^ { q } ) . } \end{array}
$$

$\tilde { \partial }$ is the map induced by composing with the face singular chain $\tilde { \partial } \in \oplus _ { k } S _ { k - 1 } ( \Delta ^ { k } )$

$$
\tilde { \partial } : S _ { p } ( \Delta ^ { k - 1 } ) \otimes S _ { q } ( \Delta ^ { k - 1 } )  S _ { p } ( \Delta ^ { k } ) \otimes S _ { q } ( \Delta ^ { k } ) , \quad \sigma _ { p } \otimes \sigma _ { q }  \tilde { \partial } \circ \sigma _ { p } \otimes \tilde { \partial } \circ \sigma _ { q }
$$

and

$$
\bar { \partial } : S _ { n } ( \Delta ^ { p } \times \Delta ^ { q } )  S _ { n } ( \Delta ^ { p + 1 } \times \Delta ^ { q } ) \oplus S _ { n } ( \Delta ^ { p } \times \Delta ^ { q + 1 } ) , \quad \sigma _ { p } \times \sigma _ { q }  ( \tilde { \partial } \circ \sigma _ { p } ) \times \sigma _ { q } + ( - 1 ) ^ { n - p } \sigma _ { p } \times ( \tilde { \partial } \circ \sigma _ { q } ) .
$$

Then $f = ( f _ { n } ) \in C _ { 0 }$ and $g = \left( g _ { n } \right) \in D _ { 0 }$

$$
F , G \mathrm { ~ a r e ~ c h a i n ~ m a p s } \longleftrightarrow f , g \mathrm { ~ a r e ~ } 0 \mathrm { - c y c l e s ~ i n ~ } C _ { \bullet } , D _ { \bullet }
$$

and natural chain homotopy of $F , G$ are given by 0-boundaries. We claim that

$$
\mathrm { H } _ { n } ( C _ { \bullet } ) = \{ { \begin{array} { l l } { \mathbb { Z } } & { n = 0 } \\ { 0 } & { n \neq 0 } \end{array} } , \quad \mathrm { H } _ { n } ( D _ { \bullet } ) = \{ { \begin{array} { l l } { \mathbb { Z } } & { n = 0 } \\ { 0 } & { n \neq 0 } \end{array} }  .
$$

This follows from a spectral sequence computation by first computing ∂-homology and then computing ˜∂-homology. For example the first page $( \mathrm { H } _ { \bullet } ( C _ { \bullet } , \partial ) , \tilde { \partial } )$ is

$$
0 \to \mathbb { Z } { \stackrel { 0 } { \to } } \mathbb { Z } { \stackrel { 1 } { \to } } \mathbb { Z } { \stackrel { 0 } { \to } } \mathbb { Z } { \stackrel { 1 } { \to } } \cdots
$$

whose $\widetilde { \partial } \cdot$ -homology is now $\mathbb { Z }$ at degree 0. The case of D is similar. This implies that the initial condition completely determines chain maps F, G up to chain homotopy.

Let us now analyze the composition $F \circ G$ and $G \circ F .$ . We similarly form the chain complexes

$$
C _ { n } ^ { \prime } = \prod _ { k \geq 0 } S _ { n + k } ( \Delta ^ { k } \times \Delta ^ { k } ) , \quad D _ { n } ^ { \prime } : = \prod _ { m \geq 0 } \bigoplus _ { p + q = m } ( S _ { \bullet } ( \Delta ^ { p } ) \otimes S _ { \bullet } ( \Delta ^ { q } ) ) _ { n + p + q }
$$

with boundary map $\partial + \tilde { \partial }$ defined similarly. Homology of $C _ { \bullet } ^ { \prime }$ controls natural chain maps of $S _ { \bullet } ( X \times Y )$ to itself up to chain homotopy, and similarly for $D _ { \bullet } ^ { \prime }$ . We still have

$$
\mathrm { H } _ { n } ( C _ { \bullet } ^ { \prime } ) = \{ \begin{array} { l l } { \mathbb { Z } } & { n = 0 } \\ { 0 } & { n \neq 0 } \end{array} , \quad \mathrm { H } _ { n } ( D _ { \bullet } ^ { \prime } ) = \{ \begin{array} { l l } { \mathbb { Z } } & { n = 0 } \\ { 0 } & { n \neq 0 } \end{array}  .
$$

It follows that $F \circ G$ and $G \circ F$ are both naturally chain homotopic to the identity map. The theorem follows.

An explicit construction of G can be described as follows: given $\sigma _ { p } : \Delta ^ { p }  X , \sigma _ { q } : \Delta ^ { q }  Y ,$

$$
G ( \sigma _ { p } \otimes \sigma _ { q } ) : \Delta ^ { p } \times \Delta ^ { q } \to X \times Y
$$

where we have to chop $\Delta ^ { p } \times \Delta ^ { q }$ into $p + q { \mathrm { - s i m p l e x e s } }$ . This is the shuffle product.

An explicit construction of F can be given by Alexander-Whitney map described as follows.

Definition 21.4. Given a singular n-simplex $\sigma : \Delta ^ { n } \to X$ and $0 \leq p , q \leq n ,$ , we define

• the front p-face of σ to be the singular p-simplex

$$
_ { p } \sigma : \Delta ^ { p }  X , \quad _ { p } \sigma ( t _ { 0 } , \cdot \cdot \cdot , t _ { p } ) : = \sigma ( t _ { 0 } , \cdot \cdot \cdot , t _ { p } , 0 , \cdot \cdot \cdot , 0 ) 
$$

• the back q-face of σ to be the singular q-simplex

$$
\sigma _ { q } : \Delta ^ { q }  X , \quad \sigma _ { q } ( t _ { 0 } , \cdot \cdot \cdot , t _ { q } ) : = \sigma ( 0 , \cdot \cdot \cdot , 0 , t _ { 0 } , \cdot \cdot \cdot , t _ { q } ) .
$$

Definition 21.5. Let $X , Y$ be topological spaces. Let $\pi _ { X } : X \times Y \to X , \pi _ { Y } : X \times Y \to Y$ be the projections. We define the Alexander-Whitney map

$$
A W : S _ { \bullet } ( X \times Y ) \to S _ { \bullet } ( X ) \otimes S _ { \bullet } ( Y )
$$

by the natural transformation given by the formula

$$
\boxed { A W ( \sigma ) : = \sum _ { p + q = n } p ( \pi _ { X } \circ \sigma ) \otimes ( \pi _ { Y } \circ \sigma ) _ { q } } .
$$

Theorem 21.6. The Alexander-Whitney map is a chain homotopy equivalence.

Proof. It is easy to see that AW is a natural chain map which induces the canonical isomorphism

$$
\mathrm { H } _ { 0 } ( X \times Y ) \to \mathrm { H } _ { 0 } ( X ) \otimes \mathrm { H } _ { 0 } ( Y ) .
$$

Therefore AW is a chain homotopy equivalence by Eilenberg-Zilber Theorem.

K ¨unneth formula.

Theorem 21.7 (Algebraic Kunneth formula) ¨ . Let $C _ { \bullet }$ and $D _ { \bullet }$ be chain complex of free abelian groups. Then there is a split exact sequence

$$
0 \to ( \mathbf { H _ { \bullet } } ( C ) \otimes \mathbf { H _ { \bullet } } ( D ) ) _ { n } \to \mathbf { H } _ { n } ( C _ { \bullet } \otimes D _ { \bullet } ) \to \operatorname { T o r } ( \mathbf { H _ { \bullet } } ( C ) , \mathbf { H _ { \bullet } } ( D ) ) _ { n - 1 } \to 0 .
$$

Here To $\mathbf { \partial } \cdot ( \mathrm { H } _ { \bullet } ( C ) , \mathrm { H } _ { \bullet } ( D ) ) _ { k } = \bigoplus _ { p + q = k } T o r ( \mathrm { H } _ { p } ( C ) , \mathrm { H } _ { q } ( D ) ) .$

Proof. Using the freeness of $C _ { \bullet }$ we can show that

$$
\mathrm { H } _ { \bullet } ( C _ { \bullet } \otimes D _ { \bullet } ) = \mathrm { H } _ { \bullet } ( C _ { \bullet } \otimes \mathrm { H } _ { \bullet } ( D ) ) .
$$

Applying Universal Coefficient Theorem for Homology, we find

$$
0 \to { \mathrm { H } } _ { p } ( C ) \otimes { \mathrm { H } } _ { q } ( D ) \to { \mathrm { H } } _ { p + q } ( C _ { \bullet - q } \otimes { \mathrm { H } } _ { q } ( D ) ) \to { \mathrm { T o r } } ( { \mathrm { H } } _ { p - 1 } ( C ) , { \mathrm { H } } _ { q } ( D ) ) \to 0 .
$$

Summing over $p , q$ gives the theorem.

Theorem 21.8 (Kunneth formula) ¨ . For any topological spaces $X , Y$ and $n \geq 0 ,$ there is a split exact sequence

$$
{ \Bigg | } 0 \to \bigoplus _ { p + q = n } H _ { p } ( X ) \otimes H _ { q } ( X ) \to \mathrm { H } _ { n } ( X \times Y ) \to \bigoplus _ { p + q = n - 1 } { \mathrm { T o r } } ( \mathrm { H } _ { p } ( X ) , \mathrm { H } _ { q } ( Y ) ) \to 0 { \Bigg | } 0 
$$

Proof. This follows from Eilenberg-Zilber Theorem and algebraic Kunneth formula. ¨

## 22. CUP AND CAP PRODUCT

Let R be a commutative ring with unit. We have natural cochain maps

$$
S ^ { \bullet } ( X ; R ) \otimes _ { R } S ^ { \bullet } ( Y ; R )  \mathrm { H o m } ( S ^ { \bullet } ( X ) \otimes S ^ { \bullet } ( Y ) , R )  S ^ { \bullet } ( X \times Y ; R )
$$

where the first map maps $\varphi _ { p } \in S ^ { p } ( X ; R ) , \eta _ { q } \in S ^ { q } ( X ; R )$ to $\varphi _ { p } \otimes \eta _ { q }$ where

$$
\varphi _ { p } \otimes \eta _ { q } : \sigma _ { p } \otimes \sigma _ { q } \to \varphi _ { p } ( \sigma _ { p } ) \cdot \eta _ { q } ( \sigma _ { q } ) , \quad \sigma _ { p } \in S _ { p } ( X ) , \quad \sigma _ { q } \in S _ { q } ( X ) .
$$

Here · is the product in R. This leads to a cochain map

$$
\boxed { S ^ { \bullet } ( X ; R ) \otimes _ { R } S ^ { \bullet } ( Y ; R ) \to S ^ { \bullet } ( X \times Y ; R ) }
$$

which further induces

$$
{ \boxplus } ^ { \bullet } ( X ; R ) \otimes _ { R } { \mathrm H } ^ { \bullet } ( Y ; R ) \to { \mathrm H } ^ { \bullet } ( X \times Y ; R )
$$

Cup product.

Definition 22.1. Let R be a commutative ring with unit. We define the cup product on cohomology groups

$$
\boxed { \mathsf { U } : \mathrm { H } ^ { p } ( X ; R ) \otimes _ { R } \mathrm { H } ^ { q } ( X ; R ) \to \mathrm { H } ^ { p + q } ( X ; R ) }
$$

by the composition

$$
\begin{array} { r } { \mathrm { H } ^ { \bullet } ( X ; R ) \otimes _ { R } \mathrm { H } ^ { \bullet } ( X ; R ) \longrightarrow \mathrm { H } ^ { \bullet } ( X \times X ; R ) } \\ { \cup \qquad \downarrow \qquad } \\ { \qquad \quad } \\ { \mathrm { H } ^ { \bullet } ( X ; R ) } \end{array}
$$

Here $\Delta : X \to X \times X$ is the diagonal map.

Alexander-Whitney map gives a specific product formula

$$
\Big | ( \alpha \cup \beta ) ( \sigma ) = \alpha ( _ { p } \sigma ) \cdot \beta ( \sigma _ { q } ) \Big | , \quad \alpha \in S ^ { p } ( X ; R ) , \beta \in S ^ { q } ( X ; R ) , \sigma : \Delta ^ { p + q }  X .
$$

Theorem 22.2. $\mathrm { H } ^ { \bullet } ( X ; R )$ is a graded commutative ring with uint:

(1) Unit: let $1 \in \mathrm { H } ^ { 0 } ( X ; R )$ be represented by the cocyle which takes every singular 0-simplex to $1 \in R$ . Then

$$
1 \cup \alpha = \alpha \cup 1 = \alpha , \quad \forall \alpha \in \mathrm { H } ^ { \bullet } ( X ; R ) .
$$

(2) Associativity:

$$
( \alpha \cup \beta ) \cup \gamma = \alpha \cup ( \beta \cup \gamma ) .
$$

(3) Graded commutativity:

$$
\alpha \cup \beta = ( - 1 ) ^ { p q } \beta \cup \alpha , \quad \forall \alpha \in \mathrm { H } ^ { p } ( X ; R ) , \beta \in \mathrm { H } ^ { q } ( X ; R ) .
$$

Proof. Unit of 1 is checked easily. Observe that the following two compositions of Eilenberg-Zilber maps are chain homotopic (similar to Eilenberg-Zilber Theorem)

$$
\begin{array} { r l } & { S _ { \bullet } ( X \times Y \times Z ) \to S _ { \bullet } ( X \times Y ) \otimes S _ { \bullet } ( Z ) \to S _ { \bullet } ( X ) \otimes S _ { \bullet } ( Y ) \otimes S _ { \bullet } ( Z ) } \\ & { S _ { \bullet } ( X \times Y \times Z ) \to S _ { \bullet } ( X ) \otimes S _ { \bullet } ( Y \times Z ) \to S _ { \bullet } ( X ) \otimes S _ { \bullet } ( Y ) \otimes S _ { \bullet } ( Z ) . } \end{array}
$$

Associativity follows from the commutative diagram (R is hidden for simplicity)

$$
\begin{array} { r l } & { \mathbf { H } ^ { \bullet } ( X ) \otimes \mathbf { H } ^ { \bullet } ( X ) \otimes \mathbf { H } ^ { \bullet } ( X ) \longleftrightarrow \mathbf { H } ^ { \bullet } ( X \times X ) \otimes \mathbf { H } ^ { \bullet } ( X ) \overset { ( \Delta \times 1 ) ^ { * } } { \longrightarrow } \mathbf { H } ^ { \bullet } ( X ) \otimes \mathbf { H } ^ { \bullet } ( X ) } \\ & { \qquad \downarrow } \\ & { \mathbf { H } ^ { \bullet } ( X ) \otimes \mathbf { H } ^ { \bullet } ( X \times X ) \xrightarrow [ ] { \qquad } \mathbf { H } ^ { \bullet } ( X \times X \times X ) \xrightarrow [ ] { \bullet } \mathbf { H } ^ { \bullet } ( X \times X ) } \\ & { \qquad \downarrow ( 1 \times \Delta ) ^ { * } \qquad \quad ( 1 \times \Delta ) ^ { * } , } \\ & { \qquad \quad \mathbf { H } ^ { \bullet } ( X ) \otimes \mathbf { H } ^ { \bullet } ( X ) } \end{array}
$$

Graded commutativity follows from the fact that the interchange map of tensor product of chain complexes

$$
\begin{array} { c } { { T : C _ { \bullet } \otimes D _ { \bullet } \to D _ { \bullet } \otimes C _ { \bullet } } } \\ { { { } } } \\ { { c _ { p } \otimes d _ { q } \to ( - 1 ) ^ { p q } d _ { q } \otimes c _ { p } } } \end{array}
$$

is a chain isomorphism. Therefore the two chain maps

$$
\begin{array} { r l } & { S _ { \bullet } ( X \times Y )  S _ { \bullet } ( Y \times X )  S _ { \bullet } ( Y ) \otimes S _ { \bullet } ( X ) } \\ & { S _ { \bullet } ( X \times Y )  S _ { \bullet } ( X ) \times S _ { \bullet } ( Y ) \stackrel { T } {  } S _ { \bullet } ( Y ) \otimes S _ { \bullet } ( X ) } \end{array}
$$

are chain homotopic, again by the uniqueness in Eilenberg-Zilber Theorem.

Set $Y = X$ we find the following commutative diagram

$$
\begin{array} { r l } { \mathrm { H } ^ { \bullet } ( X ) \otimes \mathrm { H } ^ { \bullet } ( X ) \longrightarrow \mathrm { H } ^ { \bullet } ( X \times X ) } \\ { \downarrow ^ { T } } \\ { \mathrm { H } ^ { \bullet } ( X ) \otimes \mathrm { H } ^ { \bullet } ( X ) \longrightarrow \mathrm { H } ^ { \bullet } ( X \times X ) . } \end{array}
$$

which gives graded commutativity.

Alternately, all the above can be checked explicitly using Alexander-Whitney map

Theorem 22.3. Let $f : X \to Y$ be a continuous map. Then

$$
f ^ { * } : \mathrm { H } ^ { \bullet } ( Y ; R )  \mathrm { H } ^ { \bullet } ( X ; R )
$$

is a morphism of graded commutative rings, i.e. $f ^ { * } ( \alpha \cup \beta ) = f ^ { * } \alpha \cup f ^ { * } \beta ,$ . In other words, $\mathrm { H } ^ { \bullet } ( - )$ defines a functor from the category of topological spaces to the category of graded commutative rings.

Proof. The theorem follows from the commutative diagram

<!-- image-->

Theorem 22.4 (Kunneth formula) ¨ . Assumem R is a PID, and $\operatorname { H } _ { i } ( X ; R )$ are finitely generated R-module, then there exists a split exact sequence of R-modules

$$
0 \to \bigoplus _ { p + q = n } \mathrm { H } ^ { p } ( X ; R ) \otimes \mathrm { H } ^ { q } ( Y ; R ) \to \mathrm { H } ^ { n } ( X \times Y ; R ) \to \bigoplus _ { p + q = n + 1 } { \mathrm { T o r } } _ { 1 } ^ { R } ( \mathrm { H } ^ { p } ( X ; R ) , \mathrm { H } ^ { q } ( Y ; R ) ) .
$$

In particular, $i f \mathrm { H } ^ { \bullet } ( X ; R ) o r \mathrm { H } ^ { \bullet } ( Y ; R )$ are free R-modules, we have an isomorphism of graded commutative rings

$$
\mathrm { H } ^ { \bullet } ( X \times Y ; R ) \cong \mathrm { H } ^ { \bullet } ( X ; R ) \otimes _ { R } \mathrm { H } ^ { \bullet } ( Y ; R ) .
$$

Example 22.5. $\mathrm { H } ^ { \bullet } ( S ^ { n } ) = \mathbb { Z } [ \eta ] / \eta ^ { 2 }$ where $\eta \in \mathrm { H } ^ { n } ( S ^ { n } )$ is a generator.

Example 22.6. Let $T ^ { n } = S ^ { 1 } \times \cdot \cdot \cdot \times S ^ { 1 }$ be the n-torus. Then

$$
\mathrm { H } ^ { \bullet } ( T ^ { n } ) \cong \mathbb { Z } [ \eta _ { 1 } , \cdot \cdot \cdot , \eta _ { n } ] , \quad \eta _ { i } \eta _ { - } - \eta _ { j } \eta _ { i }
$$

is the exterior algebra with n generators. Each ηi corresponds a generator of $\mathrm { H } ^ { 1 } ( S ^ { 1 } )$

Proposition 22.7. $\mathrm { H } ^ { \bullet } ( \mathbb { C } P ^ { n } ) = \mathbb { Z } [ x ] / x ^ { n + 1 }$ , where $x \in \mathrm { H } ^ { 2 } ( \mathbb { C } P ^ { n } )$ is a generator.

Proof. We prove by induction n. We know that

$$
\mathrm { H } ^ { k } ( \mathbb { C } P ^ { n } ) = { \left\{ \begin{array} { l l } { \mathbb { Z } } & { k = 2 m \leq 2 n } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

Let x be a generator of $\mathrm { H } ^ { 2 } ( \mathbb { C } P ^ { n } )$ . We only need to show that $x ^ { k }$ is a generator of $\operatorname { H } ^ { 2 k } ( \mathbb { C } P ^ { n } )$ for each $k \leq n$ Using cellular chain complex, we know that for $k < n$

$$
\mathrm { H } ^ { 2 k } ( \mathbb { C } P ^ { n } ) \to \mathrm { H } ^ { 2 k } ( \mathbb { C } P ^ { k } )
$$

is an isomorphism. By induction, this implies that $x ^ { k }$ is a generator of $\operatorname { H } ^ { 2 k } ( \mathbb { C } P ^ { n } )$ for $k < n$ . Poincare duality theorem (which will be proved in the next section) implies that

$$
\mathrm { H } ^ { 2 } ( \mathbb { C } P ^ { n } ) \otimes \mathrm { H } ^ { 2 n - 2 } ( \mathbb { C } P ^ { n } ) \stackrel { \cup } {  } \mathrm { H } ^ { 2 n } ( \mathbb { C } P ^ { n } )
$$

is an isomorphism. This says that $x ^ { n }$ is a generator of $\operatorname { H } ^ { 2 n } ( \mathbb { C } P ^ { n } )$ . This proves the proposition.

Cap product.

Definition 22.8. We define the evaluation map

$$
\langle - , - \rangle : S ^ { \bullet } ( X ; R ) \times _ { R } S _ { \bullet } ( X ; R ) \to R
$$

as follows: for $\alpha \in S ^ { p } ( X ; R ) , \sigma \in S _ { p } ( X ) , r \in R ,$

$$
\langle \alpha , \sigma \otimes r \rangle : = \alpha ( \sigma ) \cdot r .
$$

The evaluation map is compatible with boundary map and induces an evaluation map

$$
\langle - , - \rangle : { \mathrm { H } } ^ { p } ( X ; R ) \otimes _ { R } { \mathrm { H } } _ { p } ( X ; R ) \to R .
$$

This generalized to

$$
S ^ { \bullet } ( X ; R ) \otimes _ { R } S _ { \bullet } ( X \times Y ; R ) \to S ^ { \bullet } ( X ; R ) \otimes _ { R } S _ { \bullet } ( X ; R ) \otimes _ { R } S _ { \bullet } ( Y ; R ) \overset { \langle - , - \rangle \otimes 1 } { \longrightarrow } S _ { \bullet } ( Y ; R )
$$

which induces

$$
\begin{array} { r } { \mathrm { H } ^ { p } ( X ; R ) \otimes _ { R } \mathrm { H } _ { p + q } ( X \times Y ; R ) \to \mathrm { H } _ { q } ( Y ; R ) . } \end{array}
$$

Definition 22.9. We define the cap product

$$
{ \big | } \cap : \mathrm { H } ^ { p } ( X ; R ) \otimes \mathrm { H } _ { p + q } ( X ; R ) \to \mathrm { H } _ { q } ( X ; R )
$$

by the composition

$$
\begin{array} { r l } & { \mathbf { H } ^ { p } ( X ; R ) \otimes \mathbf { H } _ { p + q } ( X ; R ) \xrightarrow { \quad \log \Delta } \mathbf { H } ^ { p } ( X ; R ) \otimes \mathbf { H } _ { p + q } ( X \times X ; R ) } \\ & { \qquad \quad \overset { \quad \sharp } { = } \quad \overset { \quad \cap } { = } \quad \overset { \quad } { \quad } } \\ & { \qquad \overset { \quad \sharp } { = } \quad \overset { \quad } { \quad } \mathbf { H } _ { q } ( X ; R ) } \end{array}
$$

Theorem 22.10. The cap product gives $\operatorname { H } _ { \bullet } ( X ; R )$ a structure of $\mathrm { H } ^ { \bullet } ( X ; R )$ -module.

Theorem 22.11. The cap product extends naturally to the relative case: for any pair $A \subset X$

$$
\begin{array} { r l } & { \cap : \mathrm { H } ^ { p } ( X , A ) \otimes \mathrm { H } _ { p + q } ( X , A ) \to \mathrm { H } _ { q } ( X ) } \\ & { \cap : \mathrm { H } ^ { p } ( X ) \otimes \mathrm { H } _ { p + q } ( X , A ) \to \mathrm { H } _ { q } ( X , A ) } \end{array}
$$

Proof. Since $S ^ { \bullet } ( X , A ) \subset S ^ { \bullet } ( X )$ , we have

$$
\cap : S ^ { \bullet } ( X , A ) \times S _ { \bullet } ( X ) \to S _ { \bullet } ( X ) .
$$

We model the cap product on chains via the Alexander-Whitney map. Then

$$
\cap : S ^ { \bullet } ( X , A ) \times S _ { \bullet } ( A )  0 .
$$

Therefore ∩ factors through

$$
\cap : S ^ { \bullet } ( X , A ) \times { \frac { S _ { \bullet } ( X ) } { S _ { \bullet } ( A ) } } \to S _ { \bullet } ( X ) .
$$

Passing to homology (cohomology) we find the first cap product. The second one is proved similarly using

$$
\cap : S ^ { \bullet } ( X ) \times { \frac { S _ { \bullet } ( X ) } { S _ { \bullet } ( A ) } } \to { \frac { S _ { \bullet } ( X ) } { S _ { \bullet } ( A ) } } .
$$

## 23. POINCARE DUALITY ´

Definition 23.1. A topological manifold of dimension n , or a topological n-manifold, is a Hausdorff space in which each point has an open neighborhood homeomorphic to $\mathbb { R } ^ { n }$

In this section, a manifold always means a topological manifold. For any point $x \in X ,$ there exists an open neighborhood U and a homeomorphism $\phi : U \to \mathbb { R } ^ { n } . \ ( U , \phi )$ is called a chart around x.

Orientation.

Definition 23.2. Let X be a n-manifold. $x \in X$ be a point. A generator of

$$
\mathrm { H } _ { n } ( X , X - x ) \cong \mathrm { H } _ { n } ( \mathbb { R } ^ { n } , \mathbb { R } ^ { n } - 0 ) \cong \mathbb { Z }
$$

is called a local orientation of X at x.

For any $x \in X ,$ , there are two choices of local orientation at x. We obtain a two-sheet cover

π : X˜ → X, where $\tilde { X } = \{ ( x , \mu _ { x } ) | \mu _ { x }$ is a local orientation of $X \mathrm { a t } x \}$

Here π is the natural projection $( x , \mu _ { x } ) \to x . \ \tilde { X }$ is topologized as follows. Let U be a small open ball in X. Then for any $x \in U$ , we have an isomorphism

$$
\mathrm { H } _ { n } ( X , X - U ) \cong \mathrm { H } _ { n } ( X , X - x )
$$

which induces a set theoretical identification

$$
\pi ^ { - 1 } ( U ) \cong U \times \mathbb { Z } _ { 2 } .
$$

Then we give a topology on $\tilde { X }$ by requiring all such identifications being homeomorphisms. In particular, $\pi : \tilde { X } \to X$ is a $\mathbb { Z } _ { 2 } .$ -covering map.

Definition 23.3. A (global) orientation of X is a section of $\pi : \tilde { X } \to X , \mathrm { i . e . , }$ a continuous map $s : X \to { \tilde { X } }$ such that π $\circ s = 1 _ { X }$ . If an orientation exists, we say X is orientable.

Theorem 23.4. Let X be a connected manifold. Then X is orientable if and only if X has two connected components. ˜ In particular, a connected orientable manifold has precisely two orientations.

Example 23.5. A simply connected manifold is orientable.

Example 23.6. Let X be connected non-orientable manifold. Then $\tilde { X }$ is connected orientable.

Lemma 23.7. Let $U \subset \mathbb { R } ^ { n }$ be open. Then the natural map

$$
{ \mathrm { H } } _ { n } ( \mathbb { R } ^ { n } , U ) \to \prod _ { x \in \mathbb { R } ^ { n } - U } { \mathrm { H } } _ { n } ( \mathbb { R } ^ { n } , \mathbb { R } ^ { n } - x )
$$

is injective.

Proof. This is equivalent to the injectivity of

$$
{ \tilde { \mathrm { H } } } _ { n - 1 } ( U ) \to \prod _ { x \in \mathbb { R } ^ { n } - U } { \mathrm { H } } _ { n - 1 } ( \mathbb { R } ^ { n } - x ) .
$$

Let α be a singular $( n - 1 )$ -chain representing a class $[ \alpha ] _ { U }$ in ${ \tilde { \mathrm { H } } } _ { n - 1 } ( U )$ . We can choose a big ball B containing U and finite small cubes $D _ { 1 } , \cdots , D _ { N }$ such that $D _ { i }$ is not a subset of U but

$$
\mathsf { S u p p } ( \alpha ) \subset B - D _ { 1 } \cup \dots \cup D _ { N } \subset U .
$$Then α represents a class in $\tilde { \mathrm { H } } _ { n - 1 } \big ( D _ { 1 } \cup \cdot \cdot \cdot \cup D _ { N } \big ) \cong \mathrm { H } _ { n } \big ( B , B - D _ { 1 } \cup \cdot \cdot \cdot \cup D _ { N } \big )$ which maps to zero in each $\mathrm { H } _ { n } \big ( B , B - D _ { i } \big ) \cong \mathrm { H } _ { n } \big ( B , B - x _ { i } \big )$ where $x _ { i } \in D _ { i } - U$ . It follows via Mayer-Vietoris argument that α is the zero class in $\tilde { \mathrm { H } } _ { n - 1 } \big ( D _ { 1 } \cup \dots \cup D _ { N } \big )$ , hence zero in ${ \tilde { \mathrm { H } } } _ { n - 1 } ( U )$ 

Fundamental class.

Theorem 23.8. Let X be a connected n-manifold. For any abelian group $G ,$ we have the following vanishing statement

$$
\left\{ \begin{array} { l l } { \mathrm { H } _ { i } ( X ; G ) = 0 } & { i > n } \\ { \mathrm { H } _ { n } ( X ; G ) = 0 } & { i f X i s n o n c o m p a c t . } \end{array} \right.
$$

Proof. We prove the case for $G = \mathbb { Z }$ . General G is similar. We assume X is connected.

Step 1: $X = U \subset \mathbb { R } ^ { n }$ is an open subset.

Let $\alpha \in S _ { i } ( U )$ represent an element of $[ \alpha ] \in \mathrm { H } _ { i } ( U )$ . Let $K \subset U$ be a compact subset such that $\operatorname { S u p p } ( \alpha ) \in$ K. Equip $\mathbb { R } ^ { n }$ with a CW structure in terms of small enough cubes such that

$$
K \subset L \subset U
$$

where L is a finite CW subcomplex. We have a commutative diagram

$$
\begin{array}{c} \begin{array} { r l } { \mathrm { H } _ { i + 1 } ( \mathbb { R } ^ { n } , L ) \longrightarrow \mathrm { H } _ { i + 1 } ( \mathbb { R } ^ { n } , U ) } \\ { \Big | _ { \begin{array} { l } { \ell \mathrm { ~  ~ } } \\ { \ell \mathrm { ~  ~ } } \end{array} } - \begin{array} { l } { \mathrm { \Delta } } \\ { \mathrm { \Delta } } \end{array} } \end{array} \}  \end{array}
$$

By construction, $[ \alpha ] \in \mathrm { H } _ { i } ( U )$ lies in the image of $\mathrm { H } _ { i } ( L )$ . But $\mathrm { H } _ { i + 1 } ( \mathbb { R } ^ { n } , L ) \cong \mathrm { H } _ { i + 1 } ^ { c e l l } ( \mathbb { R } ^ { n } , L ) = 0 { \mathrm { ~ f o r ~ } } i \geq n .$

Step 2: $X = U \cup V$ where U open is homeomorphic to Rn and V open satisfies the vanishing condition.

Consider the Mayer-Vietoris sequence

$$
\tilde { \mathrm { H } } _ { i } ( U ) \oplus \tilde { \mathrm { H } } _ { i } ( V ) \to \tilde { \mathrm { H } } _ { i } ( U \cup V ) { \to } \tilde { \mathrm { H } } _ { i - 1 } ( U \cap V ) \to \tilde { \mathrm { H } } _ { i - 1 } ( U ) \oplus \tilde { \mathrm { H } } _ { i - 1 } ( V )
$$

For $i > n ,$ , we find $\mathrm { H } _ { i } ( U \cup V ) = 0$ by Step 1. Assume that $X = U \cup V$ is not compact. We need to prove

$$
\tilde { \mathrm { H } } _ { n - 1 } ( U \cap V ) \to \tilde { \mathrm { H } } _ { n - 1 } ( V )
$$

is injective. The noncompactness and connectedness of X implies that

$$
\mathrm { H } _ { n } ( U \cup V )  \mathrm { H } _ { n } ( U \cup V , U \cup V - x )
$$

is zero map for any $x \in X$ . Consider the commutative diagram, where $x \in U - U \cap V$

$$
\begin{array} { r } { \begin{array} { c c c c c c c } { { \mathrm { H } _ { n } ( U \cup V ) } } \\ { \bigg \downarrow } \\ { \mathrm { ~ H } _ { n } ( U \cup V , U \cup V - x ) } \\ { \mathrm { H } _ { n } ( U \cup V , U \cup V ) } \\ { \bigg \downarrow \simeq } \\ { { \mathrm { H } _ { n } ( U , U - x ) }  \qquad } & { { \mathrm { H } _ { n } ( U , U \cap V ) } \xrightarrow [ ] { \qquad \mathrm { H } _ { n - 1 } ( U \cap V ) } \longrightarrow 0 } \\ { { \mathrm { H } _ { n } ( U , U - x ) }  \qquad } & { { \mathrm { H } _ { n } ( U \cap V ) } \end{array} } } & { \qquad { \mathrm { H } _ { n } ( V , U \cap V ) } } \\ { { \mathrm { H } _ { n - 1 } ( V ) } } & { \longrightarrow 0 } \end{array}
$$

Let $\alpha \in \mathrm { H } _ { n } ( U , U \cap V )$ maps to ker $\cdot ( \tilde { \mathrm { H } } _ { n - 1 } ( U \cap V ) \to \tilde { \mathrm { H } } _ { n - 1 } ( V ) )$ . Diagram chasing implies that α maps to $\mathrm { H } _ { n } ( U , U - x )$ for any $x \in U - U \cap V$ . Since x is arbitrary, this implies $\alpha = 0$ by the previous lemma.

Step 3: General case. Let $\alpha \in S _ { i } ( X )$ representing a class in $\mathrm { H } _ { i } ( X )$ . We can choose finite coordinate charts $U _ { 1 } , \cdots , U _ { N }$ such that Supp $( \alpha ) \subset U _ { 1 } \cup \cdot \cdot \cdot \cup U _ { N }$ . Then the class of α lies in the image of the map

$$
\mathrm { H } _ { i } ( U _ { 1 } \cup \cdot \cdot \cdot \cup U _ { N } )  \mathrm { H } _ { i } ( X ) .
$$

We only need to prove the theorem for $U _ { 1 } \cup \cdots \cup U _ { N }$ . This follows from Step 2 and induction on N.

Definition 23.9. Let X be an n-manifold. A fundamental class of X at a subspace $A \subset X$ is an element $s \in \mathrm { H } _ { n } ( X , X - A )$ whose image

$$
\mathrm { H } _ { n } ( X , X - A ) \to \mathrm { H } _ { n } ( X , X - x )
$$

defines a local orientation for each $x \in A$ . When $A = X , s \in \mathrm { H } _ { n } ( X )$ is called a fundamental clas of X.

Theorem 23.10. Let X be an oriented n-manifold, $K \subset X$ be compact subspace. Then

(1) $\mathrm { H } _ { i } ( X , X - K ) = 0 f o r a n y i > n .$

(2) The orientation of X defines a unique fundamental class of X at K.

In particular, if X is compact, then there exists a unique fundamental class of X associated to the orientation.

Proof.

Step 1: K is a compact subset inside a cooridinate chart $U \cong \mathbb { R } ^ { n }$ . Then

$$
\mathrm { H } _ { i } ( X , X - K ) \cong \mathrm { H } _ { i } ( U , U - K ) \cong \tilde { \mathrm { H } } _ { i - 1 } ( U - K ) = 0 \quad i > n .
$$

Take a big enough ball B such that $K \subset B \subset U$ . The orientation of X at the local chart U determines an element of $\mathrm { H } _ { n } ( X , X - U )$ which maps to the required fundamental class of X at K.

Step 2: $K = K _ { 1 } \cup K _ { 2 }$ where $K _ { 1 } , K _ { 2 } , K _ { 1 } \cap K _ { 2 }$ satisfy (1)(2). Using Mayer-Vietoris sequence

$$
\cdots \cdot \mathrm { H } _ { i + 1 } ( X , X - K _ { 1 } \cap K _ { 2 } ) \to \mathrm { H } _ { i } ( X , X - K _ { 1 } \cup K _ { 2 } ) \to \mathrm { H } _ { i } ( X , X - K _ { 1 } ) \not \equiv \mathrm { H } _ { i } ( X , X - K _ { 2 } ) \to \mathrm { H } _ { i } ( X , X - K _ { 1 } \cap K _ { 2 } ) \to \cdots
$$

we see K satisfies (1). The unique fundamental classes at $K _ { 1 }$ and $K _ { 2 }$ map to the unique fundamental class at $K _ { 1 } \cap K _ { 2 }$ , giving rise to a unique fundamental class at $K _ { 1 } \cup K _ { 2 }$ by the exact sequence

$$
0 \to { \mathrm { H } } _ { n } ( X , X - K _ { 1 } \cup K _ { 2 } ) \to { \mathrm { H } } _ { n } ( X , X - K _ { 1 } ) \oplus { \mathrm { H } } _ { n } ( X , X - K _ { 2 } ) \to { \mathrm { H } } _ { n } ( X , X - K _ { 1 } \cap K _ { 2 } )
$$

Step 3: For arbitrary K, it is covered by a finite number of coordinates charts $\{ U _ { i } \} _ { 1 \le i \le N }$ . Let $K _ { i } = K \cap U _ { i }$ Then $K = K _ { 1 } \cup \cdot \cdot \cdot \cup K _ { N }$ . The theorem holds for K by induction on N and Step 1, 2.

Poincar´e duality.

Definition 23.11. Let K denote the set of compact subspaces of X. We define compactly supported cohomology of X by

$$
\mathrm { H } _ { c } ^ { k } ( X ) : = \operatorname* { c o l i m } _ { K \in { \mathcal K } } \mathrm { H } ^ { k } ( X , X - K )
$$

where the colimit is taken with respect to the homomorphisms

$$
\mathrm { H } ^ { k } ( X , X - K _ { 1 } ) \to \mathrm { H } ^ { k } ( X , X - K _ { 2 } )
$$

for $K _ { 1 } \subset K _ { 2 }$ compact. In particular, if X is compact, then $\mathrm { H } _ { c } ^ { k } ( X ) = \mathrm { H } ^ { k } ( X )$

The functorial structure is with respect to the proper maps: let $f : X \to Y$ be proper, then

$$
f ^ { * } : \mathrm { H } _ { c } ^ { k } ( Y )  \mathrm { H } _ { c } ^ { k } ( X ) .
$$

Example 23.12. Let $X = \mathbb { R } ^ { n }$ . Consider the sequence of compact subspaces $B _ { 1 } \subset B _ { 2 } \subset B _ { 3 } \subset \cdots$ , where $B _ { k }$ is the closed ball of radius k. Any compact subspace is contained in some ball. Therefore

$$
\begin{array} { r } { \mathrm { H } _ { c } ^ { i } ( \mathbb { R } ^ { n } ) = \displaystyle \mathrm { c o l i m } _ { k } \mathrm { H } ^ { i } ( \mathbb { R } ^ { n } , \mathbb { R } ^ { n } - B _ { k } ) = \tilde { \\mathrm { H } } ^ { i } ( S ^ { n - 1 } ) = \left\{ \mathbb { Z } \begin{array} { l l } { \displaystyle { d } } & { \displaystyle { i = n } } \\ { \displaystyle { 0 } } & { \displaystyle { i \ne n } } \end{array} . \right. } \end{array}
$$

Theorem 23.13. Let $X = U \cup V$ where U, V open. Then we have the Mayer-Vietoris exact sequence

$$
\begin{array} { r } { \cdots \to \mathbf { H } _ { c } ^ { k } ( U \cap V ) \to \mathbf { H } _ { c } ^ { k } ( U ) \oplus \mathbf { H } _ { c } ^ { k } ( V ) \to \mathbf { H } _ { c } ^ { k } ( X ) \to \mathbf { H } _ { c } ^ { k + 1 } ( U \cap V ) \to \cdots . } \end{array}
$$

Let X be an oriented n-manifold. For each compact $K ,$ let $\xi _ { K } \in \mathrm { H } _ { n } ( X , X - K )$ be the fundamental class determined by the orientation. Taking the cap product we find

$$
D _ { K } : { \mathrm { H } } ^ { p } ( X , X - K ) \ { \overset { \cap { \xi _ { K } } } { \to } } \mathrm { H } _ { n - p } ( X ) .
$$

This passes to the colimit and induces a map

$$
\boxed { D : \mathrm { H } _ { c } ^ { p } ( X ) \to \mathrm { H } _ { n - p } ( X ) . }
$$

Theorem 23.14 (Poincare Duality) ´ . Let X be an oriented n-manifold. Then for any $p ,$

$$
D : \operatorname { H } _ { c } ^ { p } ( X ) \to \operatorname { H } _ { n - p } ( X )
$$

is an isomorphism. In particular, if X is compact then $\mathrm { H } ^ { p } ( X ) \cong \mathrm { H } _ { n - p } ( X )$

Proof. We prove the theorem for all open subset U of X.

Step 1: If the theorem holds for open $U , V$ and U ∩ V, then the theorem holds for $U \cup V$

This follows from Mayer-Vietoris sequence and the commutative diagram

$$
\begin{array} { r l } &  \begin{array} { l l l l l l l } & { \longrightarrow \mathrm { H } _ { c } ^ { k } ( U \cap V ) } & { \longrightarrow \mathrm { H } _ { c } ^ { k } ( U ) \oplus \mathrm { H } _ { c } ^ { k } ( V ) \underbrace { \quad \quad } } & { \longrightarrow \mathrm { H } _ { c } ^ { k } ( U \cup V ) \longrightarrow \mathrm { H } _ { c } ^ { k + 1 } ( U \cap V ) \quad \longrightarrow \quad \cdots } \\ & { \Bigm \downarrow _ { D } } & { \qquad \Bigm \downarrow _ { D \oplus D \quad \quad \quad \quad \quad \sqrt { \mathrm { \scriptsize ~ \beta ~ } \cap \ 1 1 ^ { \circ } } } \end{array} \Bigm \} \begin{array} { l } { \mathrm { \smallskip ~ \psi ~ } } \\ { \displaystyle \qquad \psi } \end{array} } \\ & { \longrightarrow \mathrm { H } _ { n - k } ( U \cap V ) \longrightarrow \mathrm { H } _ { n - k } ( U ) \oplus \mathrm { H } _ { n - k } ( V ) \longrightarrow \mathrm { H } _ { n - k } ( U \cup V ) \longrightarrow \mathrm { H } _ { n - k - 1 } ( U \cap V ) \longrightarrow \cdots } \end{array} ,
$$

Step 2: Let $U _ { 1 } \subset U _ { 2 } \subset \cdots$ and $U = \cup _ { i } U _ { i }$ . Assume the theorem holds for $U _ { i } ,$ then it holds for U.

This follows from the isomorphism

$$
\mathrm { H } _ { c } ^ { k } ( U ) = \displaystyle { \mathrm { c o l i m } } \mathrm { H } _ { c } ^ { k } ( U _ { i } ) , \quad \mathrm { H } _ { n - k } ( U ) = \displaystyle { \mathrm { c o l i m } } \mathrm { H } _ { n - k } ( U _ { i } ) .
$$

Step 3: The theorem holds for an open U contained in a coordinate chart.

This follows by expressing U as a countable union of convex subsets of $\mathbb { R } ^ { n }$

Step 4: For any open U.

By Step 2, 3 and Zorn’s lemma, there is a maximal open subset U of X for which the theorem is true. By Step 1, U must be the same as X. 

## 24. INTERSECTION AND LEFSCHETZ FIXED POINT THEOREM

In this section X will be an oriented connected closed n-dim manifold. [X] its fundamental class.

Intersection form. Poincare duality gives an isomorphism ´

$$
\mathrm { H } ^ { i } ( X ) \stackrel { \cap [ X ] } { \cong } \mathrm { H } _ { n - i } ( X ) .
$$

The cup product on cohomology has a geometric meaning under Poincare duality as follows. Let ´ $Y , Z$ be two oriented closed submanifold of X. Assume dim $( Y ) = i , \dim ( Z ) = j ,$ , and Y intersects Z transversely so that their intersection $Y \cap Z$ is manifold of dimension $i + j - n$ . Y ∩ Z has an induced orientation. Let $[ Y ] ^ { * } \in \mathrm { H } ^ { n - i } ( X )$ be the Poincare dual of the fundamental class ´ $[ Y ] \in \mathrm { H } _ { i } ( X )$ . Then

$$
\boxed { \left[ Y \right] ^ { * } \cup \left[ Z \right] ^ { * } = \left[ Y \cap Z \right] ^ { * } } .
$$

Therefore the cup product is interpreted as intersection under Poincare duality. ´

An important case is when Y and Z have complementary dimension, i.e. $i + j = n$ so that $Y \cap Z$ is a finite set of points, whose signed sum gives the intersection number of Y and Z.

Definition 24.1. We define the intersection pairing

$$
\langle - , - \rangle : \mathrm { H } _ { i } ( X ) \times \mathrm { H } _ { n - i } ( X ) \to \mathrm { H } _ { 0 } ( X ) \cong \mathbb { Z } .
$$

Equivalently, we have the pairing on cohomology

$$
\langle - , - \rangle : \mathrm { H } ^ { i } ( X ) \times \mathrm { H } ^ { n - i } ( X ) \to \mathrm { H } ^ { n } ( X ) \stackrel { [ X ] } { \cong } \mathbb { Z } .
$$

The intersection pairing is non-degenerate when torsion elements are factored out. In particular

$$
\mathrm { H } ^ { i } ( X ; \mathbb { Q } ) \times \mathrm { H } ^ { n - i } ( X ; \mathbb { Q } ) \to \mathbb { Q }
$$

is a non-degenerate pairing.

Example 24.2. $T ^ { 2 } = S ^ { 1 } \times S ^ { 1 } . \ Y _ { 1 } = S ^ { 1 } \times \{ 1 \} , Y _ { 2 } = \{ 1 \} \times S ^ { 1 }$ $Y _ { 1 } \cap Y _ { 2 }$ is a point. This is dual to the ring structure $\mathrm { H } ^ { \bullet } ( T ^ { 2 } ) = \mathbb { Z } [ \eta _ { 1 } , \eta _ { 2 } ]$ , where $\eta _ { i }$ is dual to $Y _ { i }$

Example 24.3. Let $f : \Sigma _ { g } \to \Sigma _ { h }$

Lefschetz Fixed Point Theorem. Let us consider the diagonal $\Delta \subset X \times X$ . Let $\left\{ \boldsymbol { e } _ { i } \right\}$ be a basis of $\operatorname { H } _ { \bullet } ( X ; \mathbb { R } )$ consisting of elements of pure degree. Let $e ^ { i }$ be its dual basis of $\operatorname { H } _ { \bullet } ( X ; \mathbb { Q } )$ such that

$$
\left. e ^ { j } , e _ { i } \right. = \delta _ { i } ^ { j } .
$$

First we observe that

$$
[ \Delta ] \in \mathrm { H } _ { n } ( X \times X ; \mathbb { Q } ) \cong \oplus _ { p } \mathrm { H } _ { p } ( X ; \mathbb { Q } ) \otimes \mathrm { H } _ { n - p } ( X ; \mathbb { Q } )
$$

is given by

$$
[ \Delta ] = \sum _ { i } e _ { i } \otimes e ^ { i } .
$$

This can be checked by intersecting with a basis of $\mathrm { H } _ { \bullet } ( X \times X ; \mathbb { Q } )$

Let $f : X \to X$ be a smooth map. Let

$$
\Gamma _ { f } : = \{ ( x , f ( x ) ) | x \in X \} \subset X \times X
$$

be the graph of $f .$ Let $\alpha \in \mathrm { H } _ { p } ( X ) , \beta \in \mathrm { H } _ { n - p } ( X )$ . From the geometry of graph, we find

$$
\left[ \Gamma _ { f } \right] \cdot \alpha \times \beta = ( - 1 ) ^ { p } f _ { * } \alpha \cdot \beta .
$$

Applying this to [∆], we find

$$
[ \Gamma _ { f } ] \cdot [ \Delta ] = \sum _ { i } ( - 1 ) ^ { | e _ { i } | } f _ { * } e _ { i } \cdot e ^ { i } = \sum _ { p } ( - 1 ) ^ { p } \operatorname { T r } ( f _ { * } : \mathrm { H } _ { p } ( X ; \mathbb { Q } ) \to \mathrm { H } _ { p } ( X ; \mathbb { Q } ) ) .
$$

Definition 24.4. We define the Lefschetz number of f by

$$
{ \Big \vert } L ( f ) : = \sum _ { p } ( - 1 ) ^ { p } \operatorname { T r } ( f _ { * } : \operatorname { H } _ { p } ( X ; \mathbb { Q } ) \to \operatorname { H } _ { p } ( X ; \mathbb { Q } ) ) { \Big \vert } .
$$

When $\Gamma _ { f }$ and ∆ intersects transversely,

$$
\sharp \mathrm { F i x } ( f ) = [ \Gamma _ { f } ] \cdot [ \Delta ]
$$

gives a signed count of fixed points of the map $f .$ This gives the Lefschetz Fixed Point Theorem

$$
\boxed { \sharp \mathrm { F i x } ( f ) = L ( f ) } .
$$

In particular, if the right hand side is not zero, there must exist a fixed point of $f .$

Example 24.5. Let n be even. Then any map $f : \mathbb { C } P ^ { n } \to \mathbb { C } P ^ { n }$ has a fixed point. In fact,

$$
f ^ { * } : { \mathrm { H } } ^ { \bullet } ( \mathbb { C } P ^ { n } ; \mathbb { Q } ) \to { \mathrm { H } } ^ { \bullet } ( \mathbb { C } P ^ { n } ; \mathbb { Q } )
$$

is a ring map. Let $x \in \mathrm { H } ^ { 2 } ( \mathbb { C } P ^ { n } )$ be a generator, let $f ^ { * } ( x ) = k x$ for some $k \in \mathbb { Z }$ . Then

$$
\sum _ { p } ( - 1 ) ^ { p } \operatorname { T r } ( f _ { * } | _ { \mathrm { H } _ { p } ( \mathbb { C } P ^ { n } ; \mathbb { Q } ) } ) = \sum _ { i = 0 } ^ { n } k ^ { n }
$$

is an odd number, hence not zero. By Lefschetz Fixed Point Theorem, f must have a fixed point.

Example 24.6. The Lefschetz number of the identity map id : $X  X$ is precisely the Euler characteristic

$$
L ( \operatorname { i d } ) = \chi ( X ) .
$$

Consider the sphere $S ^ { 2 }$ , and the map

$$
f : S ^ { 2 }  S ^ { 2 } , \quad x  \frac { x + v } { \vert x + v \vert } , \quad v = ( 0 , 0 , 1 / 2 ) .
$$

f has two fixed points: north and south pole, and f is homotopy to the identify. We find

$$
\chi ( S ^ { 2 } ) = { \cal L } ( \mathrm { i d } ) = { \cal L } ( f ) = 2 .
$$

For another example, consider a compact connected Lie group G. Let $g \in G$ which is not identity but close to identity. Then multiplication by g has no fixed point, and it is hompotopic to the identity map. We find

$$
\chi ( G ) = 0 .
$$

## 25. SPECTRAL SEQUENCE

Spectral sequences usually arise in two situations

(1) A Z-filtration of a chain complex: a sequence of subcomplexes $\ \cdots \subset F _ { p } \subset F _ { p + 1 } \subset \cdots$

(2) A Z-filtration of a topological space: a family of subspaces $\cdots \subset X _ { p } \subset X _ { p + 1 } \subset \cdots$

Definition 25.1. A filtered R-module is an R-module A with an increasing sequence of submodules

$$
\cdots \subset F _ { p } A \subset F _ { p + 1 } A \subset \cdots
$$

indexed by $p \in \mathbb { Z } .$ . We always assume that it is exhaustive and Hausdorff

$$
\bigcup _ { p } F _ { p } A = A \quad ( { \mathrm { e x h a u s t i v e } } ) , \quad \bigcap _ { p } F _ { p } A = 0 \quad ( { \mathrm { H a u s d o r f f } } ) .
$$

The filtration is bounded if $F _ { p } A = 0$ for p sufficiently small and $F _ { p } A$ for p sufficiently large. The associated graded module $G _ { \bullet } ^ { F } A$ is defined by

$$
G _ { \bullet } ^ { F } ( { \cal A } ) : = \bigoplus _ { p \in { \mathbb Z } } G _ { p } ^ { F } { \cal A } , \quad G _ { p } ^ { F } { \cal A } : = F _ { p } { \cal A } / F _ { p - 1 } { \cal A } .
$$

A filtered chain complex is a chain complex $( C _ { \bullet } , \partial )$ together with a filtration $F _ { p } C _ { i }$ of each $C _ { i }$ such that the differential preserves the filtration

$$
\partial ( F _ { p } C _ { i } ) \subset F _ { p } C _ { i - 1 } .
$$

In other words, we have an increasing sequence of subcomplexes $F _ { p } C _ { \bullet }$ of $C _ { \bullet }$ .

A filtered chain complex induces a filtration on its homology

$$
F _ { p } \operatorname { H } _ { i } ( C _ { \bullet } ) = \operatorname { I m } ( \operatorname { H } _ { i } ( F _ { p } C _ { \bullet } ) \to \operatorname { H } _ { i } ( C _ { \bullet } ) ) .
$$

In other words, an element $[ \alpha ] \in \mathrm { H } _ { i } ( C _ { \bullet } )$ lies in $F _ { p } \mathrm { H } _ { i } ( C _ { \bullet } )$ if and only if there exists a representative $x \in F _ { P } C _ { i }$ such that $[ \alpha ] = [ x ]$ . Its graded piece is given by

$$
G _ { p } ^ { F } \mathrm { H } _ { i } ( C _ { \bullet } ) = \frac { \mathrm { K e r } ( \partial : F _ { p } C _ { i } \to F _ { p } C _ { i - 1 } ) } { F _ { p - 1 } C _ { i } + \partial C _ { i + 1 } } .
$$

Notation 25.2. In this section, our notation of quotient means the quotient of the numerator by its intersection with the denominator, i.e., $\textstyle { \frac { A } { B } } : = { \frac { A } { A \cap B } }$

Given a filtered R-module A, we define its Rees module as a submodule of $A [ z , z ^ { - 1 } ]$ defined by

$$
A _ { F } : = \bigoplus _ { p \in \mathbb { Z } } F _ { p } A z ^ { p } \subset A [ z , z ^ { - 1 } ] .
$$

Our conditions for the filtration can be interpreted as follows

(1) increasing fitration: $A _ { F }$ is a $R [ z ]$ -submodule of $A [ z , z ^ { - 1 } ]$ and $z : A _ { F }  A _ { F }$ is injective.

(2) exhaustive: $A _ { F } [ z ^ { - 1 } ] : = A _ { F } \otimes _ { R [ z ] } R [ z , z ^ { - 1 } ]$ equals $A [ z , z ^ { - 1 } ]$

(3) Hausdorff: $\bigcap _ { . . . . } z ^ { - p } A _ { F } = 0$ in $A [ z , z ^ { - 1 } ] ,$

We have

$$
G _ { \bullet } ^ { F } ( A ) : = A _ { F } / z A _ { F } .
$$

## 26. OBSTRUCTION THEORY

## 27. THE THEOREM OF HUREWICZ

Definition 27.1. We define the Hurewicz map $\rho : \pi _ { n } ( X , A )  \operatorname { H } _ { n } ( X , A )$ by

$$
\rho ( [ f ] ) : = f _ { \ast } ( \eta )
$$

where $f : ( D ^ { n } , S ^ { n - 1 } ) \to ( X , A )$ represents an element of $\pi _ { n } ( X , A )$ and η is a generator of $\mathrm { H } _ { n } ( D ^ { n } , S ^ { n - 1 } )$ .

The following diagram commutes

$$
{ \begin{array} { r l } { } & { \cdots { \xrightarrow { } } \pi _ { n } ( A ) { \xrightarrow { } } \pi _ { n } ( X ) { \xrightarrow { } } \pi _ { n } ( X , A ) { \xrightarrow { } } \pi _ { n - 1 } ( A ) { \xrightarrow { } } \cdots } \\ { \downarrow } & { { \Bigg \downarrow } } \\ { } & { \cdots { \xrightarrow { } } \mathrm { H } _ { n } ( A ) { \xrightarrow { } } \mathrm { H } _ { n } ( X ) { \xrightarrow { } } \mathrm { H } _ { n } ( X , A ) { \xrightarrow { } } \mathrm { H } _ { n - 1 } ( A ) { \xrightarrow { } } \cdots } \end{array} }
$$

Theorem 27.2 (Hurewicz).

(1) If a space X is (n − 1)−connected, $n \geq 2 ,$ then $\mathrm { H } _ { i } ( X ) = 0 f o r i < n$ and $\pi _ { n } ( X ) \cong \operatorname { H } _ { n } ( X )$

(2) $I f a p a i r \left( X , A \right) i s \left( n - 1 \right) - c o n n e c t e d , n \geq 2 ,$ with A simply- connected and nonempty, then $\mathrm { H } _ { i } ( X , A ) = 0$ for i < n and $\pi _ { n } ( X , A ) \cong \operatorname { H } _ { n } ( X , A )$

## 28. EILENBERG-STEENROD AXIOMS

In this section we discuss Eilenberg-Steenrod’s axiomatic approach to homology theory.

Eilenberg-Steenrod Axioms.

Definition 28.1. A homology theory consists of a sequence of functors $\mathrm { H } _ { n } \left( n \in \mathbb { Z } \right)$ from the category of pairs $( X , A )$ of topological spaces to the category of abelian groups, together with a natural transformation

$$
\partial : \mathrm { H } _ { i } ( X , A ) \to \mathrm { H } _ { i - 1 } ( A ) \quad ( : = \mathrm { H } _ { i - 1 } ( A , \emptyset ) )
$$

called the connecting map. They satisfy the following properties

(1) Exactness. For any pair $( X , A )$ with inclusions i : $A \subset X , j : ( X , \emptyset ) \subset ( X , A )$ , there is an exact sequence

$$
\cdot \cdot \cdot  \mathrm { H } _ { q } ( A ) \stackrel { \mathrm { H } _ { q } ( i ) } {  } \mathrm { H } _ { q } ( X ) \stackrel { \mathrm { H } _ { q } ( j ) } {  } \mathrm { H } _ { q } ( X , A ) \stackrel { \partial } {  } \mathrm { H } _ { q - 1 } ( A ) 
$$

(2) Homotopy. $\operatorname { I f } f _ { 0 } , f _ { 1 } : ( X , A ) \to ( Y , B )$ are homotopic, then

$$
\mathrm { H } ( f _ { 0 } ) = \mathrm { H } ( f _ { 1 } ) : \mathrm { H } _ { \bullet } ( X , A )  \mathrm { H } _ { \bullet } ( Y , B ) .
$$

(3) Excision. For any pair $( X , A ) ,$ if U is a subset of X such that the closure of U is contained in the interior of A, then the inclusion $j : ( X - U , A - U ) \subset ( X , A )$ induces isomorphisms

$$
\mathrm { H } ( j ) : \mathrm { H } _ { \bullet } ( X - U , A - U ) \cong \mathrm { H } _ { \bullet } ( X , A ) .
$$

(4) Dimension. If ? is a point, then $\mathrm { H } _ { i } ( \star ) = 0 \mathrm { f o r a n y } i \neq 0 .$

We also add two additional axioms

(5) Additivity. If $\textstyle X = \coprod _ { \alpha } X _ { \alpha }$ is a disjoint union, then

$$
\mathrm { H } _ { \bullet } ( X ) = \bigoplus _ { \alpha } \mathrm { H } _ { \bullet } ( X _ { \alpha } ) .
$$

(6) Weak equivalence. $\operatorname { I f } f : ( X , A ) \to ( Y , B )$ is a weak equivalence, then $\operatorname { H } _ { \bullet } ( f )$ are isomorphism.

For a homology theory, $\operatorname { H } _ { 0 } ( \star ) = G$ is called the coefficient group of the theory.

Remark 28.2. The weak equivalence axiom ensures that a homology theory is uniquely determined by the subcategory of CW complexes.

Definition 28.3. Let $\mathrm { H } , \mathrm { H } ^ { \prime }$ be two homology theories. A natural transformation $\Phi : \mathrm { H }  \mathrm { H } ^ { \prime }$ is a sequence of natural transformations $\Phi _ { i } : \mathrm { H } _ { i } \to \mathrm { H } _ { i } ^ { \prime }$ such that the following diagram commutes for any pair $( X , A )$

$$
\begin{array} { r l r } & { } & { \mathrm { H } _ { i } ( X , A ) \xrightarrow { \partial } \mathrm { H } _ { i - 1 } ( A ) } \\ & { } & { \Phi _ { i } \Bigg \downarrow \qquad } \\ & { } & { \mathrm { H } ^ { \prime } ( X , A ) \xrightarrow { \partial ^ { \prime } } \mathrm { H } _ { i - 1 } ^ { \prime } ( A ) } \end{array}
$$

If $\Phi _ { i }$ is a natural isomorphism for each i, then we say $\mathrm { H } , \mathrm { H } ^ { \prime }$ are naturally isomorphic.

Example 28.4. Singularity homology $\operatorname { H } ( X , A ; G )$ is a homology theory with coefficient G.

Given a homology theory, we can similarly define its reduced homology by

$$
\begin{array} { r } { \tilde { \mathbf { H } } _ { i } ( X , A ) = \left\{ \begin{array} { l l } { \ker ( \mathrm { H } _ { 0 } ( X ) \to \mathrm { H } _ { 0 } ( \star ) ) } & { i = 0 , A = \emptyset } \\ { \mathrm { H } _ { i } ( X , A ) } & { \mathrm { o t h e r w i s e } } \end{array} \right. } \end{array}
$$

The reduced homology sequence is also exact.

Proposition 28.5. Let H be a homology theory with coefficient G, Then

$$
{ \tilde { \mathrm { H } } } _ { i } ( S ^ { n } ) = { \left\{ \begin{array} { l l } { G } & { i = n } \\ { 0 } & { i \neq n } \end{array} \right. }
$$

Hurewicz Theorem gives a natural isomorphism

$$
\mathrm { H } _ { n } ( X ; \mathbb { Z } ) \to \mathrm { H } _ { n } ( X )
$$

from the singular homology to our given homology theory, for (n − 1)-connected space X. This is the key to prove the following uniqueness theorem.

Theorem 28.6. Any homology theory is naturally isomorphic to the singular homology.

Proof. We only need to prove for CW complex. We can use the axioms to construct the cellular chain complex $C _ { n } ( X ) \ = \ \mathrm { H } _ { n } { \big ( } X ^ { ( n ) } / X ^ { ( n - 1 ) } { \big ) }$ for any homology theory, and show by the same method that the homology of

$$
\cdots \to C _ { n } ( X ) \ { \overset { d } { \to } } \ C _ { n - 1 } ( X ) \to \cdots
$$

is isomorphic to H•(X) of our given homolog theory. Hurewicz Theorem will imply that this chain complex is isomorphic to the cellular chain complex associated to the singular homology. This proves the theorem.

Generalized homology theory.

Definition 28.7. A (co)-homology functor H that satisfies Eilenberg-Steenrod Axioms except the Dimension axiom is called a generalized (co)-homology theory

Example 28.8 (K-theory).

Example 28.9 (Bordism).