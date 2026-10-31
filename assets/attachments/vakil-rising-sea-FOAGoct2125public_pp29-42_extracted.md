universal property are bijections. In short, there is a unique bijection between $\mathsf { P } _ { 1 }$ and ${ \mathsf { P } } _ { 2 }$ preserving the “product structure” (the maps to M and N). This gives us the right to name any such product $M \times \mathsf { N } ,$ since any two such products are uniquely identified.

This definition has the advantage that it works in many circumstances, and once we define categories, we will soon see that the above argument applies verbatim in any category to show that products, if they exist, are unique up to unique isomorphism. Even if you haven’t seen the definition of category before, you can verify that this agrees with your notion of product in some category that you have seen before (such as the category of vector spaces, or the category of manifolds).

This is handy even in cases that you understand. For example, one way of defining the product of two manifolds M and N is to cut them both up into charts, then take products of charts, then glue them together. But if I cut up the manifolds M and N in one way, and you cut them up in another, how do we know our resulting product manifolds are the “same”? We could wave our hands, or make an annoying argument about refining covers, but instead, we should just show that they are “categorical products” and hence canonically the “same” (i.e., isomorphic). We will formalize this argument in §1.2.

Another set of notions we will abstract is that of categories that “behave like modules.” We will want to define kernels and cokernels for new notions, and we should make sure that these notions behave the way we expect them to. This leads us to the definition of abelian categories, first defined by Grothendieck in his Tohoku ˆ paper [Gr1].

In this chapter, we will give an informal introduction to these and related notions, in the hope of our developing just enough familiarity to comfortably use them in practice.

## 1.1 Categories and functors

The introduction of the digit 0 or the group concept was general nonsense too, and mathematics was more or less stagnating for thousands of years because nobody was around to take such childish steps.

— A. Grothendieck, [BroP, pp. 4–5]

Before functoriality, people lived in caves.

— B. Conrad

We begin with an informal definition of categories and functors.

## 1.1.1. Categories.

A category consists of a collection of objects, and for each pair of objects, a set of morphisms (or arrows) between them. (For experts: technically, this is the definition of a locally small category. In the correct definition, the morphisms need only form a class, not necessarily a set, but see Caution 0.3.1.) Morphisms are often informally called maps. The collection of objects of a category $\mathcal { C }$ is often denoted by obj(C ), but we will usually denote the collection also by C . If $A , \mathrm { B } \in \mathcal { C }$ , then the set of morphisms from A to B is denoted by Mor(A, B). A morphism is often written $\mathsf { f } \colon \lambda  \mathsf { B } ,$ and A is said to be the source of ${ \mathfrak { f } } ,$ and B the target of f. (Of course, Mor(A, B) is taken to be disjoint from $\mathrm { M o r } ( \mathcal { A } ^ { \prime } , \mathbb { B } ^ { \prime } )$ unless $\lambda = \lambda ^ { \prime }$ and $\boldsymbol { \mathrm { B } } = \boldsymbol { \mathrm { B } } ^ { \prime } \boldsymbol { \cdot } \boldsymbol { \mathrm { J } }$

Morphisms compose as expected: there is a composition Mor $( \mathsf { B } , \mathsf { C } ) { \times } \mathbf { M o r } ( \mathsf { A } , \mathsf { B } ) \to$ $\operatorname { M o r } ( A , C )$ , and if $\mathsf { f } \in \operatorname { M o r } ( \mathsf { A } , \mathsf { B } )$ and ${ \mathfrak { g } } \in \operatorname { M o r } ( { \mathfrak { B } } , { \mathsf { C } } )$ , then their composition is denoted by g ◦ f. Composition is associative: if $\mathsf { f } \in \mathrm { M o r } ( \mathsf { A } , \mathsf { B } ) , \mathsf { g } \in \bar { \mathrm { M o r } } ( \mathsf { B } , \mathsf { C } )$ , and $\mathsf { h } \in \mathbf { M o } \bar { \mathbf { r } } ( \mathsf { C } , \mathsf { D } )$ , then $\mathtt { h } \circ ( { \mathfrak { g } } \circ { \mathfrak { f } } ) = ( { \mathfrak { h } } \circ { \mathfrak { g } } ) \circ { \mathfrak { f } } .$ For each object ${ \boldsymbol { A } } \in { \mathcal { C } } .$ , there is always an identity morphism id $\ A : A \to A$ , such that when you (left- or right-)compose a morphism with the identity, you get the same morphism. More precisely, for any morphisms $\mathsf { f } \colon \mathsf { A }  \mathsf { B }$ and ${ \mathfrak { g } } \colon { \mathsf { B } } \to { \mathsf { C } } , { \mathsf { i d } } _ { \mathsf { B } } \circ { \mathsf { f } } = { \mathsf { f } }$ and ${ \mathfrak { g o i d } } _ { \mathrm { B } } = { \mathfrak { g } }$ . (If you wish, you may check that “identity morphisms are unique”: there is only one morphism deserving the name $\mathrm { i d } _ { A \cdot } )$ This ends the definition of a category.

We have a notion of isomorphism between two objects of a category (a morphism $\mathsf { f } \colon \mathsf { A }  \mathsf { B }$ such that there exists some — necessarily unique — morphism ${ \mathfrak { g } } \colon { \mathrm { B } } \to A$ , where f ◦ g and ${ \mathfrak { g } } \circ { \mathfrak { f } }$ are the identities on B and A respectively).

1.1.2. Example. The prototypical example to keep in mind is the category of sets, denoted by Sets. The objects are sets, and the morphisms are maps of sets. (Because Russell’s paradox shows that there is no set of all sets, we did not say earlier that there is a set of all objects. But as stated in §0.3, we are deliberately omitting all set-theoretic issues.)

1.1.3. Example. Another good example is the category $V e c _ { \boldsymbol { \mathrm { k } } }$ of vector spaces over a given field k. The objects are k-vector spaces, and the morphisms are linear transformations. (What are the isomorphisms?)

1.1.A. UNIMPORTANT EXERCISE. A category in which each morphism is an isomorphism is called a groupoid. (This notion is not important in what we will discuss. The point of this exercise is to give you some practice with categories, by relating them to an object you know well.)

(a) A perverse definition of a group is: a groupoid with one object. Make sense of this. (Similarly, in case you care, a perverse definition of a monoid is: a category with one object.)

(b) Describe a groupoid that is not a group.

1.1.B. EXERCISE. If A is an object in a category $\mathcal { C } ,$ show that the invertible elements of Mor(A, A) form a group (called the automorphism group of $\mathsf { A } ,$ , denoted by $\operatorname { A u t } ( A ) )$ . What are the automorphism groups of the objects in Examples 1.1.2 and 1.1.3? Show that two isomorphic objects have isomorphic automorphism groups. (For readers with a topological background: if X is a topological space, then the fundamental groupoid is the category where the objects are points of ${ \bar { \boldsymbol { x } } } ,$ and the morphisms $x \to$ y are paths from x to y, up to homotopy. Then the automorphism group of $\boldsymbol { \mathrm { { x } } } _ { 0 }$ is the (pointed) fundamental group $\pi _ { 1 } ( \boldsymbol { X } , \boldsymbol { x } _ { 0 } )$ . In the case where X is connected, and $\pi _ { 1 } ( X )$ is not abelian, this illustrates the fact that for a connected groupoid — whose definition you can guess — the automorphism groups of the objects are all isomorphic, but not canonically isomorphic.)

1.1.4. Example: Abelian groups. The abelian groups, along with group homomorphisms, form a category Ab.

1.1.5. Important Example: Modules over a ring. If A is a ring, then the A-modules form a category $M o d _ { A }$ . (This category has additional structure; it will be the prototypical example of an abelian category; see §1.5.) Taking $\mathsf { A } = \mathsf { k }$ , we obtain Example 1.1.3; taking $\begin{array} { r } { \mathsf { A } = \mathbb { Z } , } \end{array}$ we obtain Example 1.1.4.

1.1.6. Example: Rings. There is a category Rings, where the objects are rings, and the morphisms are maps of rings in the usual sense (maps of sets that respect addition and multiplication, and that send 1 to 1 by our conventions; see §0.3).

1.1.7. Example: Topological spaces. The topological spaces, along with continuous maps, form a category Top. The isomorphisms are homeomorphisms.

In all of the above examples, the objects of the categories were in obvious ways sets with additional structure (a concrete category, although we won’t use this terminology). This needn’t be the case, as the next example shows.

1.1.8. Example: Partially ordered sets. A partially ordered set (or poset) is a set S along with a binary relation ≥ on S satisfying:

(i) $\begin{array} { r } { x \ge x ( \mathrm { r e f l e x i v i t y } ) , } \end{array}$

(ii) $x \geq y$ and y ≥ z imply $x \ge z$ (transitivity), and

(iii) if $x \geq y$ and $y \geq x$ then ${ x = 9 }$ (antisymmetry).

A partially ordered set $( S , \geq )$ can be interpreted as a category whose objects are the elements of S, and with a single morphism from x to y if and only i $\dot { \cdot } \ x \geq \ y$ (and no morphism otherwise).

A trivial example is $( S , \geq )$ where $x \geq y$ if and only if ${ \mathfrak { x } } = { \mathfrak { y } }$ . Another example is

(1.1.8.1)

<!-- image-->

Here there are three objects. The identity morphisms are omitted for convenience, and the two non-identity morphisms are depicted. A third example is

(1.1.8.2)

<!-- image-->

Here the “obvious” morphisms are again omitted: the identity morphisms, and the morphism from the upper left to the lower right. Similarly,

<!-- image-->

depicts a partially ordered set, where, again, only the “generating morphisms” are depicted.

1.1.9. Example: The category of subsets of a set, and the category of open subsets of a topological space. If X is a set, then the subsets form a partially ordered set, where arrows are given by inclusion. (Be careful: you may be expecting the arrows to go the other way, because of Example 1.1.8.) Informally, if ${ \hat { \mathsf { u } } } \subset { \check { \mathsf { V } } } ,$ then we have exactly one morphism $\mathsf { U } \to \mathsf { V }$ in the category (and otherwise none). Similarly, if

X is a topological space, then the open sets form a partially ordered set, where the maps are given by inclusions.

1.1.10. Definition. A subcategory A of a category B has as its objects some of the objects of B, and some of the morphisms of ${ \mathcal { B } } ,$ such that the objects of $\mathcal { A }$ include the sources and targets of the morphisms of $\mathcal { A } ,$ and the morphisms of $\mathcal { A }$ include the identity morphisms of the objects of ${ \mathcal { A } } ,$ and are preserved by composition. (For example, (1.1.8.1) is in an obvious way a subcategory of (1.1.8.2). Also, we have an obvious “inclusion” i : ${ \mathcal { A } } \to { \mathcal { B } } ,$ which will soon be an example of a functor.)

## 1.1.11. Functors.

A covariant functor F from a category A to a category ${ \mathcal { B } } ,$ denoted by F: $\mathcal { A } $ ${ \mathcal { B } } ,$ is the following data. It is a map of objects F : ob $\dot { \mathbf { \eta } } ( \mathcal { A } )  \mathrm { o b j } ( \mathcal { B } )$ , and for each $\mathsf { A } _ { 1 } , \mathsf { A } _ { 2 } \in \mathcal { A } ,$ and morphism m: $\lambda _ { 1 }  \lambda _ { 2 } ,$ a morphism $\mathsf { F } ( \mathsf { m } ) \colon \mathsf { F } (  { \mathbf { A } } _ { 1 } ) \to \mathsf { F } (  { \mathbf { A } } _ { 2 } )$ in B. We require that F preserve identity morphisms (for $\mathsf { A } \in \mathcal { A } , \mathsf { F } ( \mathrm { i d } _ { \mathsf { A } } ) = \mathrm { i d } _ { \mathsf { F } ( \mathsf { A } ) } )$ and that F preserve composition $( \mathsf { F } ( \mathsf { m } _ { 2 } \circ \mathsf { m } _ { 1 } ) = \mathsf { F } ( \mathsf { m } _ { 2 } ) \circ \mathsf { F } ( \mathsf { m } _ { 1 } ) )$ . (You may wish to verify that covariant functors send isomorphisms to isomorphisms.) A trivial example is the identity functor id : $\mathcal { A }  \mathcal { A }$ , whose definition you can guess. Here are some less trivial examples.

1.1.12. Example: A forgetful functor. Consider the functor from the category of vector spaces (over a field k) $V e c _ { \boldsymbol { \mathrm { k } } }$ to Sets that associates to each vector space its underlying set. The functor sends a linear transformation to its underlying map of sets. This is an example of a forgetful functor, where some additional structure is forgotten. Another example of a forgetful functor is $M o d _ { \mathrm { A } }  A b$ from A-modules to abelian groups, which remembers only the abelian group structure of the A-module.

1.1.13. Topological examples. Examples of covariant functors include the fundamental group functor π1, which sends a topological space X with choice of a point $x _ { 0 } \in X$ to a group π1(X, x0) (what are the objects and morphisms of the source category?), and the ith homology functor $T o p  A b$ , which sends a topological space X to its ith homology group $\mathsf { H } _ { \mathrm { i } } ( \mathsf { X } , \mathbb { Z } )$ . The covariance corresponds to the fact that a (continuous) morphism of pointed topological spaces $\Phi \colon X \to \mathsf { Y }$ with $\Phi ( \boldsymbol { x } _ { 0 } ) = \boldsymbol { y } _ { 0 }$ induces a map of fundamental groups $\pi _ { 1 } \bar { ( } X , x _ { 0 } \bar { ) }  \pi _ { 1 } ( Y , y _ { 0 } )$ , and similarly for homology groups.

1.1.14. Example. Suppose A is an object in a category $\mathcal { C } .$ . Then there is a functor $\mathfrak { h } ^ { \sf A } : \mathcal { C } \mathrm { ~  ~ }$ Sets sending $\textit { \textbf { B } } \in \textit { \textbf { \textit { 6 } } }$ to $\operatorname { M o r } ( A , { \mathrm { B } } )$ and sending $\mathsf { f } \colon \mathsf { B } _ { 1 } \  \ \mathsf { B } _ { 2 }$ to $\operatorname { M o r } ( \mathtt { A } , \mathtt { B } _ { 1 } ) \to \operatorname { M o r } ( \mathtt { A } , \mathtt { B } _ { 2 } )$ , described by

$$
[ 9 \colon A \to \mathsf { B } _ { 1 } ] \longmapsto [ \mathsf { f o } ~ \mathsf { g } \colon A \to \mathsf { B } _ { 1 } \to \mathsf { B } _ { 2 } ] .
$$

This seemingly silly functor ends up surprisingly being an important concept.

1.1.15. Definitions. If F: $\mathcal { A }  \mathcal { B }$ and $\mathsf { G } \colon \mathcal { B } \to \mathcal { C }$ are covariant functors, then we define a functor ${ \mathsf { G } } \circ { \mathsf { F } } \colon { \mathcal { A } }  { \mathcal { C } }$ (the composition of G and F) in the obvious way. Composition of functors is associative in an evident sense.

A covariant functor $\mathsf { F } \colon \mathcal { A } \ \to \ \mathcal { B }$ is faithful if for all $A , A ^ { \prime } \in \mathcal { A } ,$ the map Mor ${ \mathcal { A } } ( \mathsf { A } , \mathsf { A } ^ { \prime } ) \to \operatorname { M o r } _ { \mathcal { B } } ( \mathsf { F } ( \mathsf { A } ) , \mathsf { F } ( \mathsf { A } ^ { \prime } ) )$ is injective, and full if it is surjective. A functor that is full and faithful is fully faithful. (For various philosophical reasons, the notion of $" \mathrm { f u l l } ^ { \prime \prime }$ functor on its own is unimportant; “fully faithful” is the useful notion.) A subcategory i : $\mathcal { A }  \mathcal { B }$ is a full subcategory if i is full. (Inclusions are always faithful, so there is no need for the phrase “faithful subcategory.”) Thus a subcategory A ′ ${ \mathcal { A } } ^ { \prime }$ of $\mathcal { A }$ is full if and only if for all $\mathsf { A } , \mathsf { B } \in \mathrm { o b j } ( \mathcal { A } ^ { \prime } )$ $\begin{array} { r l } {  { \operatorname { M o r } _ { \mathcal { A } ^ { \prime } } ( A , B ) = } } \end{array}$ $\mathsf { M o r } _ { \mathcal { A } } ( A , \mathsf { B } )$ . For example, the forgetful functor $V e c _ { \bf k }  S e t s$ is faithful, but not full; and if A is a ring, the category of finitely generated A-modules is a full subcategory of the category $M o d _ { A }$ of A-modules.

1.1.16. Definition. A contravariant functor is defined in the same way as a covariant functor, except the arrows switch directions: in the above language, $\mathsf { F } ( { \cal A } _ { 1 } \to { \cal A } _ { 2 } )$ is now an arrow from $\mathsf { F } ( A _ { 2 } )$ to $\mathsf { F } ( A _ { 1 } )$ . (Thus $\mathsf { F } ( \mathsf { m } _ { 2 } \circ \mathsf { m } _ { 1 } ) = \mathsf { F } ( \mathsf { m } _ { 1 } ) \circ$ $\mathsf { F } ( \mathsf { m } _ { 2 } )$ , not $\mathsf { F } ( \mathfrak { m } _ { 2 } ) \circ \mathsf { F } ( \mathfrak { m } _ { 1 } ) . )$

It is wise to state whether a functor is covariant or contravariant, unless the context makes it very clear. If it is not stated (and the context does not make it clear), the functor is often assumed to be covariant.

Sometimes people describe a contravariant functor $\mathcal { C } \to \mathcal { D }$ as a covariant functor $\mathcal { C } ^ { \mathrm { o p p } }  \mathcal { D } ,$ , where $\mathcal { C } ^ { \mathrm { o p p } }$ is the same category as C except that the arrows go in the opposite direction. Here $\mathcal { C } ^ { \mathrm { o p p } }$ is said to be the opposite category to $\mathcal { C }$

One can define fullness, etc. for contravariant functors, and you should do so.

1.1.17. Linear algebra example. If $V e c _ { \boldsymbol { \mathrm { k } } }$ is the category of k-vector spaces (introduced in Example 1.1.3), then taking duals gives a contravariant functor $\hat { ( \cdot ) } ^ { \vee } \colon V e c _ { \bf k }  V e c _ { \bf k }$ Indeed, to each linear transformation $\mathsf { f } \colon \mathsf { V } \to \mathsf { W } ,$ we have a dual transformation $\mathsf { f } ^ { \vee } \colon W ^ { \vee }  \mathsf { V } ^ { \vee }$ , and $( \mathbf { f } \circ \mathbf { g } ) ^ { \vee } = \mathbf { g } ^ { \vee } \circ \mathbf { f } ^ { \vee }$

1.1.18. Topological example (cf. Example 1.1.13) for those who have seen cohomology. The ith cohomology functor $\mathsf { H } ^ { i } ( \cdot , \mathbb { Z } ) \colon T o p  A b$ is a contravariant functor.

1.1.19. Example. There is a contravariant functor Top  Rings taking a topological space X to the ring of real-valued continuous functions on X. A morphism of topological spaces $x \to \Upsilon$ (a continuous map) induces the pullback map from functions on $\dot { \gamma }$ to functions on X.

1.1.20. Example (the functor of points; cf. Example 1.1.14). Suppose A is an object of a category $\mathcal { C } .$ Then there is a contravariant functor $\mathrm { h } _ { \mathrm { A } } \colon \mathcal { C } \ \to$ Sets sending $\boldsymbol { \mathrm { ~ B ~ } } \in \mathcal { C }$ to $\operatorname { M o r } ( \mathtt { B } , \lambda )$ , and sending the morphism $\mathsf { f } \colon \mathsf { B } _ { 1 } \  \ \mathsf { B } _ { 2 }$ to the morphism $\operatorname { M o r } ( \mathtt { B } _ { 2 } , \mathtt { A } ) \to \operatorname { M o r } ( \mathtt { B } _ { 1 } , \mathtt { A } )$ via

$$
[ { \mathfrak { g } } \colon { \mathrm { B } } _ { 2 } \to { \mathrm { A } } ] \longmapsto [ { \mathfrak { g } } \circ { \mathfrak { f } } \colon { \mathrm { B } } _ { 1 } \to { \mathrm { B } } _ { 2 } \to { \mathrm { A } } ] .
$$

This example initially looks weird and different, but Examples 1.1.17 and 1.1.19 may be interpreted as special cases; do you see how? What is A in each case? This functor might reasonably be called the functor of maps (to $A ) ,$ , but is actually known as the functor of points. We will meet this functor again in §1.2.11 and (in the category of schemes) in Definition 7.3.10.

## 1.1.21. ⋆ Natural transformations (and natural isomorphisms) of covariant functors, and equivalences of categories.

(This notion won’t come up in an essential way until at least Chapter 7, so you shouldn’t read this section until then.) Suppose F and G are two covariant functors from $\mathcal { A }$ to B. A natural transformation of covariant functors $\mathsf { F } \to \mathsf { G }$ is the data of a morphism $\mathfrak { m } _ { A } \colon \mathsf { F } ( A )  \mathsf { G } ( A )$ for each $\boldsymbol { A } \in \mathcal { A }$ such that for each f : $A  A ^ { \prime }$ in $\mathcal { A } ,$

the diagram

<!-- image-->

commutes. A natural isomorphism of functors is a natural transformation such that each $\mathsf { m } _ { A }$ is an isomorphism. (We make analogous definitions when F and G are both contravariant.)

The data of functors F: ${ \mathcal { A } }  { \mathcal { B } }$ and $\mathsf { F } ^ { \prime } \colon \mathcal { B }  \mathcal { A }$ such that $\mathsf { F } \circ \mathsf { F } ^ { \prime }$ is naturally isomorphic to the identity functor idB on B and $\mathsf { F } ^ { \prime } \circ \mathsf { F }$ is naturally isomorphic to $\mathrm { i d } _ { \mathcal { A } }$ is said to be an equivalence of categories. The right notion of when two categories are “essentially the same” is not isomorphism (a functor giving bijections of objects and morphisms) but equivalence. Exercises 1.1.C and 1.1.D might give you some vague sense of this. Later exercises (for example, to show that “rings” and “affine schemes” are essentially the same once arrows are reversed, Exercise 7.3.E) may help, too.

Two examples might make this strange concept more comprehensible. The double dual of a finite-dimensional vector space V is not V, but we learn early to say that it is canonically isomorphic to V. We can make that precise as follows. Let $f . d . V e c _ { \mathrm { k } }$ be the category of finite-dimensional vector spaces over k. Note that this category contains oodles of vector spaces of each dimension.

1.1.C. EXERCISE. Let $( \cdot ) ^ { \vee \vee } : f . d . V e c _ { \bf k }  f . d . V e c _ { \bf k }$ be the double dual functor from the category of finite-dimensional vector spaces over k to itself. Show that $( \cdot ) ^ { \vee \vee }$ is naturally isomorphic to the identity functor on $f . d . W e c _ { \mathrm { k } } .$ (Without the finitedimensionality hypothesis, we only get a natural transformation of functors from id to $( \cdot ) ^ { \vee \vee } . )$

Let $\mathcal { V }$ be the category whose objects are the k-vector spaces ${ \boldsymbol { \mathrm { k } } } ^ { \mathrm { n } }$ for each $\mathfrak { n } \geq 0$ (there is one vector space for each n), and whose morphisms are linear transformations. The objects of $\mathcal { V }$ can be thought of as vector spaces with bases, and the morphisms as matrices. There is an obvious functor $\mathcal { V }  f . d . V e c _ { \mathrm { k } } ^ { } .$ , as each ${ \boldsymbol { \mathrm { k } } } ^ { \mathrm { n } }$ is a finite-dimensional vector space.

1.1.D. EXERCISE. Show that $\mathcal { V }  f . d . V e c _ { \bf k }$ gives an equivalence of categories, by describing an “inverse” functor. (Recall that we are being cavalier about settheoretic assumptions — see Caution 0.3.1 — so feel free to simultaneously choose bases for each vector space in $f . d . V e c _ { \mathrm { k } }$ . To make this precise, you will need to use Godel-Bernays set theory or else replace¨ $f . d . V e c _ { \mathrm { k } }$ with a very similar small category, but we won’t worry about this.)

1.1.22. ⋆⋆ Aside for experts. Your argument for Exercise 1.1.D will show that (modulo set-theoretic issues) this definition of equivalence of categories is the same as another one commonly given: a covariant functor F: ${ \mathcal { A } }  { \mathcal { B } }$ is an equivalence of categories if it is fully faithful and every object of B is isomorphic to an object of the form $\mathsf { F } ( A )$ for some $\boldsymbol { A } \in \mathcal { A }$ (F is essentially surjective, a term we will not need).

## 1.2 Universal properties determine an object up to unique isomorphism

Given some category that we come up with, we often will have ways of producing new objects from old. In good circumstances, definitions will usefully be made using the notion of a universal property. Informally, we wish that there were an object with some property. We first show that if it exists, then it is essentially unique, or more precisely, is unique up to unique isomorphism. Then we go about constructing an example of such an object to show existence.

Explicit constructions are sometimes easier to work with than universal properties, but with a little practice, universal properties are useful in proving things quickly and slickly. Indeed, when learning the subject, people often find explicit constructions more appealing, and use them more often in proofs, but as they become more experienced, they find universal property arguments more elegant and insightful.

1.2.1. Products were defined by a universal property. We have seen one important example of a universal property argument already in §1.0.1: products. You should go back and verify that our discussion there gives a notion of product in any category, and shows that products, if they exist, are unique up to unique isomorphism.

1.2.2. Initial, final, and zero objects. Here are some simple but useful concepts that will give you practice with universal property arguments. An object of a category C is an initial object if it has precisely one map to every object. It is a final object if it has precisely one map from every object. It is a zero object if it is both an initial object and a final object.

1.2.A. EXERCISE. Show that any two initial objects are uniquely isomorphic. Show that any two final objects are uniquely isomorphic.

In other words, if an initial object exists, it is unique up to unique isomorphism, and similarly for final objects. This (partially) justifies the phrase “the initial object” rather than “an initial object,” and similarly for “the final object” and “the zero object.” (Convention: We often say “the,” not ${ \bf \mathit { \Omega } } ^ { \prime \prime } { \bf { \hat { a } } , \omega } ^ { \prime \prime }$ for anything defined up to unique isomorphism.)

1.2.B. EXERCISE. What are the initial and final objects in Sets, Rings, and Top (if they exist)? How about in the two examples of §1.1.9?

1.2.3. Localization of rings and modules. Another important example of a definition by universal property is the notion of localization of a ring. We first review a constructive definition, and then reinterpret the notion in terms of universal property. A multiplicative subset S of a ring A is a subset closed under multiplication containing 1. We define a ring $S ^ { - 1 } A$ . The elements of $S ^ { - 1 } A$ are of the form $\alpha / s$ where ${ \mathfrak { a } } \in A$ and $s \in S _ { \varepsilon }$ , and where ${ \bf a } _ { 1 } / s _ { 1 } = { \bf a } _ { 2 } / s _ { 2 }$ if (and only if) for some $s \in \mathrm { S } , s ( s _ { 2 } \mathbf { a } _ { 1 } - s _ { 1 } \mathbf { a } _ { 2 } ) = 0$ . We define $( { \bf a } _ { 1 } / s _ { 1 } ) + ( { \bf a } _ { 2 } / s _ { 2 } ) = ( s _ { 2 } { \bf a } _ { 1 } + s _ { 1 } { \bf a } _ { 2 } ) / ( s _ { 1 } s _ { 2 } ) ,$ and $( { \bf a } _ { 1 } / s _ { 1 } ) \times ( { \bf a } _ { 2 } / s _ { 2 } ) = ( { \bf a } _ { 1 } { \bf a } _ { 2 } ) / ( s _ { 1 } s _ { 2 } )$ . (If you wish, you may check that this equality of fractions really is an equivalence relation and the two binary operations on fractions are well-defined on equivalence classes and make $S ^ { - 1 } A$ into a ring.)

We have a canonical ring map

$$
A { \longrightarrow } S ^ { - 1 } A\tag{1.2.3.1}
$$

given by $\mathfrak { a } \mapsto \mathfrak { a } / 1$ . Note that if $0 \in { \mathsf { S } } , { \mathsf { S } } ^ { - 1 } { \boldsymbol { A } }$ is the 0-ring.

There are two particularly important flavors of multiplicative subsets. The first is $\{ 1 , 1 , 1 ^ { 2 } , 1 \cdots \} ,$ where ${ \mathsf { f } } \in A$ . This localization is denoted $\mathsf { A } _ { \mathsf { f } } .$ . (Can you describe an isomorphism $\bar { \mathsf { A } } _ { \mathrm { f } } \longleftrightarrow \bar { \mathsf { A } } [ \mathbf { t } ] / ( \mathbf { t } \mathbf { f } - 1 ) ? )$ The second is ${ \mathsf { A } } \setminus { \mathfrak { p } } ,$ where p is a prime ideal. This localization $S ^ { - 1 } A$ is denoted $\mathsf { A } _ { \mathsf { p } } .$ . (Notational warning: If p is a prime ideal, then $\mathsf { A } _ { \mathfrak { p } }$ means you’re allowed to divide by elements not in p. However, if ${ \mathrm { : } } \mathsf { f } \in \mathsf { A } _ { \iota }$ $\boldsymbol { A } _ { \mathrm { f } }$ means you’re allowed to divide by f. This can be confusing. For example, if (f) is a prime ideal, then $\lambda _ { \mathrm { f } } \neq \lambda _ { \mathrm { ( f ) } } . )$

Warning: Sometimes localization is first introduced in the special case where A is an integral domain and $0 \not \in S .$ . In that case, $A \hookrightarrow S ^ { - 1 } A$ , but this isn’t always true, as shown by the following exercise. (But we will see that noninjective localizations needn’t be pathological, and we can sometimes understand them geometrically; see Exercise 3.2.L.)

1.2.C. EXERCISE. Show that $A \to S ^ { - 1 } A$ is injective if and only if S contains no zerodivisors. (A zerodivisor of a ring A is an element a such that there is a nonzero element b with ${ \mathrm { a b } } = 0$ . The other elements of A are called non-zerodivisors. For example, an invertible element is never a zerodivisor. Counterintuitively, 0 is a zerodivisor in every ring but the 0-ring. More generally, if M is an A-module, then ${ \mathfrak { a } } \in A$ is a zerodivisor for M if there is a nonzero $\mathfrak { m } \in M$ with ${ \mathrm { a m } } = 0 .$ . The other elements of A are called non-zerodivisors for M. Equivalently, and very usefully, ${ \mathfrak { a } } \in A$ is a non-zerodivisor for M if and only $\mathbf { i f } \times \mathbf { a } : M \to M$ is an injection, or equivalently in the language of §1.5, if

$$
 { \boldsymbol { 0 } } \longrightarrow  { \boldsymbol { M } } \xrightarrow { \times  { \mathbf { a } } }  { \boldsymbol { \mathrm { M } } }
$$

is exact.)

If A is an integral domain and $S = A \setminus \{ 0 \}$ , then $S ^ { - 1 } A$ is called the fraction field of A, which we denote by $\mathsf { K } ( A )$ . The previous exercise shows that A is a subring of its fraction field ${ \mathsf { K } } ( \bar { A _ { \mathbf { \lambda } } } )$ . We now return to the case where A is a general (commutative) ring.

1.2.D. EXERCISE. Verify that $A \to S ^ { - 1 } A$ satisfies the following universal property: $S ^ { - 1 } A$ is initial among A-algebras B where every element of S is sent to an invertible element in B. (Recall: The data of “an A-algebra $\mathrm { B } ^ { \prime \prime }$ and $\mathbf { \check { a } }$ ring map $A  \mathrm { B } ^ { \prime \prime }$ are the same.) Translation: Any map $\lambda  1$ B where every element of S is sent to an invertible element factors uniquely through $ { \lambda } \to  { \varsigma } ^ { - 1 }  { \lambda }$ . Another translation: a ring map out of $S ^ { - 1 } A$ is the same thing as a ring map from A that sends every element of S to an invertible element. Furthermore, an S−1A-module is the same thing as an A-module for which $\mathfrak { s } \times \because M \to M$ is an A-module isomorphism for all $s \in S .$

In fact, it is cleaner to define $A \to S ^ { - 1 } A$ by the universal property, and to show that it exists, and to use the universal property to check various properties $S ^ { - 1 } A$ has. Let’s get some practice with this by defining localizations of modules by the universal property. Suppose M is an A-module. We define the A-module map $\Phi \colon M \to S ^ { \bar { - } 1 }$ M as being initial among A-module maps $M  \Nu$ such that elements of S are invertible in N $( s \times \because N $ N is an isomorphism for all $s \in S )$ . More precisely, any such map α : $M  \Nu$ factors uniquely through ϕ:

<!-- image-->

(Translation: $M \to S ^ { - 1 } M$ is universal (initial) among A-module maps from M to modules that are actually $S ^ { - 1 } A$ -modules. Can you make this precise by defining clearly the objects and morphisms in this category?)

Notice: (i) This determines $\Phi \colon M \to S ^ { - 1 } M$ up to unique isomorphism (you should think through what this means); (ii) we are defining not only $S ^ { - 1 } M$ , but also the map ϕ at the same time; and (iii) essentially by definition the A-module structure on $S ^ { - 1 } M$ extends to an $S ^ { - 1 } A$ -module structure.

1.2.E. EXERCISE. Show that ϕ: $M  S ^ { - 1 } M$ exists, by constructing something satisfying the universal property. Hint: Define elements of $S ^ { - 1 } M$ to be of the form $\mathfrak { m } / s$ where $\mathfrak { m } \in { M }$ and $s \in S ,$ , and $\mathfrak { m } _ { 1 } / s _ { 1 } = \mathfrak { m } _ { 2 } / s _ { 2 }$ if and only if for some $s \in { \mathsf { S } } , s ( s _ { 2 } \mathsf { m } _ { 1 } - s _ { 1 } \mathsf { m } _ { 2 } ) = 0$ . Define the additive structure by $\begin{array} { r } { ( \mathfrak { m } _ { 1 } / s _ { 1 } ) + ( \mathfrak { m } _ { 2 } / s _ { 2 } ) = } \end{array}$ $( s _ { 2 } \mathsf { m } _ { 1 } + s _ { 1 } \mathsf { m } _ { 2 } ) / ( s _ { 1 } s _ { 2 } )$ , and the $S ^ { - 1 } .$ A-module structure (and hence the A-module structure) as given by $( \mathbf { a } _ { 1 } / s _ { 1 } ) \cdot ( \mathbf { m } _ { 2 } / s _ { 2 } ) = ( \mathbf { a } _ { 1 } \mathbf { m } _ { 2 } ) / ( s _ { 1 } s _ { 2 } )$

## 1.2.F. EXERCISE.

(a) Show that localization commutes with finite products, or equivalently, with finite direct sums. In other words, if $M _ { 1 } , . . . , M _ { \mathrm { n } }$ are A-modules, describe an isomorphism (of A-modules, and of $S ^ { - 1 } A$ -modules) $S ^ { - 1 } ( M _ { 1 } \times \cdot \cdot \cdot \times M _ { \mathrm { n } } ) $ $\mathsf { S } ^ { - 1 } \mathsf { M } _ { 1 } \bar { \times } \cdots \times \mathsf { S } ^ { - 1 } \mathsf { M } _ { \mathrm { n } }$ .

(b) Show that localization commutes with arbitrary direct sums.

(c) Show that “localization does not necessarily commute with infinite products”: the obvious map $\begin{array} { r } { { \mathsf { S } } ^ { - 1 } ( \prod _ { \mathrm { i } } { M _ { \mathrm { i } } } ) \to \prod _ { \mathrm { i } } { S ^ { - 1 } M _ { \mathrm { i } } } } \end{array}$ induced by the universal property of localization is not always an isomorphism. (Hint: $( 1 , 1 \dot { / } 2 , 1 / 3 , 1 / 4 , . . . \dot { ) } \in \boldsymbol { \hat { \mathbb { Q } } } \times \boldsymbol { \bar { \mathbb { Q } } } \times$ $\cdots . . . )$

1.2.4. Remark. Localization does not always commute with Hom; see Example 1.5.10. But Exercise 1.5.H will show that in good situations (if the first argument of Hom is finitely presented), localization does commute with Hom.

1.2.5. Tensor products. Another important example of a universal property construction is the notion of a tensor product of A-modules:

$$
\otimes _ { A } : \qquad { \mathrm { o b j } } ( M o d _ { A } ) \times { \mathrm { o b j } } ( M o d _ { A } ) \qquad \to { \mathrm { o b j } } ( M o d _ { A } )
$$

$$
( M , \mathsf { N } ) \longmapsto M \otimes _ { A } \mathsf { N }
$$

The subscript A is often suppressed when it is clear from context. The tensor product is often defined as follows. Suppose you have two A-modules M and N. Then elements of the tensor product $M \otimes _ { A }$ N are finite A-linear combinations of symbols m⊗n $( \mathsf { m } \in M , \mathsf { n } \in \mathsf { N } )$ , subject to relations $( \mathfrak { m } _ { 1 } + \mathfrak { m } _ { 2 } ) \otimes \mathfrak { n } = \mathfrak { m } _ { 1 } \otimes \mathfrak { n } + \mathfrak { m } _ { 2 } \otimes \mathfrak { n } ,$ $\begin{array} { r } { \mathfrak { m } \otimes ( \mathfrak { n } _ { 1 } + \mathfrak { n } _ { 2 } ) = \mathfrak { m } \otimes \mathfrak { n } _ { 1 } + \mathfrak { m } \otimes \mathfrak { n } _ { 2 } , \mathfrak { a } ( \mathfrak { m } \otimes \mathfrak { n } ) = ( \mathfrak { a } \mathfrak { m } ) \otimes \mathfrak { n } = \mathfrak { m } \otimes ( \mathfrak { a } \mathfrak { n } ) ( \mathrm { w h e r e ~ } \mathfrak { a } \in \mathcal { A } _ { \mathrm { \Gamma } } ) . } \end{array}$ $\mathfrak { m } _ { 1 } , \mathfrak { m } _ { 2 } \in \mathbf { M } , \mathfrak { n } _ { 1 } , \mathfrak { n } _ { 2 } \in \mathsf { N } )$ . More formally, $M \otimes _ { A }$ N is the free A-module generated by ${ \cal M } \times { \sf N } ,$ , quotiented by the submodule generated by $( \mathfrak { m } _ { 1 } + \mathfrak { m } _ { 2 } , \mathfrak { n } ) - ( \mathfrak { m } _ { 1 } , \mathfrak { n } ) -$ $( \mathbf { \tilde { m } } _ { 2 } , \mathbf { n } ) , ( \mathbf { m } , \mathbf { \tilde { n } } _ { 1 } + \mathbf { n } _ { 2 } ) - ( \mathbf { \tilde { m } } , \mathbf { n } _ { 1 } ) - ( \mathbf { m } , \mathbf { n } _ { 2 } ) , \mathbf { a } ( \mathbf { m } , \mathbf { n } ) - ( \mathbf { a } \mathbf { \tilde { m } } , \mathbf { n } ) , \mathrm { a n d ~ } \mathbf { a } ( \mathbf { m } , \mathbf { n } ) - ( \mathbf { m } , \mathbf { a } \mathbf { n } ) - ( \mathbf { a } \mathbf { n } _ { 1 } ) , \mathbf { a } ( \mathbf { m } , \mathbf { n } ) - ( \mathbf { a } \mathbf { n } _ { 2 } ) , \mathbf { a } ( \mathbf { m } , \mathbf { n } ) - \mathbf { b } ( \mathbf { n } _ { 1 } ) .$ for $\mathbf { a } \in \mathsf { A } , \mathsf { m } , \mathsf { m } _ { 1 } , \mathsf { m } _ { 2 } \in \mathsf { M } , \mathsf { n } , \mathsf { n } _ { 1 } , \mathsf { n } _ { 2 } \in \mathsf { N }$ . The image of $( \mathfrak { m } , \mathfrak { n } )$ in this quotient is m ⊗ n.

If A is a field k, we recover the tensor product of vector spaces.

1.2.G. EXERCISE (IF YOU HAVEN’T SEEN TENSOR PRODUCTS BEFORE). Show that $\mathbb { Z } / ( 1 0 ) \otimes _ { \mathbb { Z } } \mathbb { Z } / ( 1 2 ) \cong \mathbb { Z } / ( 2 )$ . (This exercise is intended to give some hands-on practice with tensor products.)

1.2.H. IMPORTANT EXERCISE: RIGHT-EXACTNESS OF $( \cdot ) \otimes _ { A }$ N. Show that $( \cdot ) \otimes _ { { \cal A } } \mathsf { N }$ gives a covariant functor $M o d _ { \mathrm { A } }  M o d _ { \mathrm { A } }$ . Show that $( \cdot ) \otimes _ { A }$ N is a right-exact functor, i.e., if

$$
M ^ { \prime }  M  M ^ { \prime \prime }  0
$$

is an exact sequence of A-modules (which means f : $M  M ^ { \prime \prime }$ is surjective, and $M ^ { \prime }$ surjects onto the kernel of ${ \mathfrak { f } } ;$ see §1.5), then the induced sequence

$$
\mathbf { M } ^ { \prime } \otimes _ { A } \mathbf { N } \to \mathbf { M } \otimes _ { A } \mathbf { N } \to \mathbf { M } ^ { \prime \prime } \otimes _ { A } \mathbf { N } \to 0
$$

is also exact. This exercise is repeated in Exercise 1.5.G, but you may get a lot out of doing it now. (You will be reminded of the definition of right-exactness in §1.5.6.)

In contrast, you can quickly check that the tensor product is not left-exact: tensor the exact sequence of Z-modules

$$
0 \xrightarrow [ ] { } \mathbb { Z } \xrightarrow { \times 2 } \mathbb { Z } \xrightarrow [ ] { } \mathbb { Z } / ( 2 ) \xrightarrow [ ] { } 0
$$

with $\mathbb { Z } / ( 2 )$

The constructive definition of ⊗ is a weird definition, and really the “wrong” definition. To motivate a better one: notice that there is a natural A-bilinear map ${ \cal M } \times { \sf N } \to { \cal M } \otimes _ { { \cal A } }$ N. (If $M , \mathsf { N } , \mathsf { P } \in M o d _ { \mathsf { A } } .$ , a map f : $M \times \Nu \to \mathsf { P }$ is A-bilinear if $\mathsf { f } \big ( \mathsf { m } _ { 1 } + \mathsf { m } _ { 2 } , \mathsf { n } \big ) = \mathsf { f } \big ( \mathsf { m } _ { 1 } , \mathsf { n } \big ) + \mathsf { f } \big ( \mathsf { m } _ { 2 } , \mathsf { n } \big ) , \mathsf { f } \big ( \mathsf { m } , \mathsf { n } _ { 1 } + \mathsf { n } _ { 2 } \big ) = \mathsf { f } \big ( \mathsf { m } , \mathsf { n } _ { 1 } \big ) + \mathsf { f } \big ( \mathsf { m } , \mathsf { n } _ { 2 } \big )$ , and $\mathsf { f } ( \mathtt { a m } , \mathtt { n } ) = \mathsf { f } ( \mathtt { m } , \mathtt { a n } ) = \mathtt { a f } ( \mathtt { m } , \mathtt { n } ) . \mathtt { . } )$ Any A-bilinear map $M \times \mathsf { N } \to \mathsf { P }$ factors through the tensor product uniquely: $M \times \mathsf { N } \to M \otimes _ { \mathsf { A } } \mathsf { N } \to \mathsf { P }$ . (Think this through!)

We can take this as the definition of the tensor product as follows. It is an A-module T along with an A-bilinear map t : $M \times \bar { \mathsf { N } } \to \mathsf { T } .$ , such that given any A-bilinear map $\mathrm { t } ^ { \prime } \colon \boldsymbol { M } \times \mathsf { N }  \mathsf { T } ^ { \prime }$ , there is a unique A-linear map $\mathsf { f } \colon \mathsf { T } \stackrel { \cdot } {  } \mathsf { T } ^ { \prime }$ such that $\mathrm { t } ^ { \prime } = \mathrm { f } \circ \mathrm { t }$

<!-- image-->

1.2.I. EXERCISE. Show that $( \mathsf { T } , \mathsf { t } \colon M \times \mathsf { N } \to \mathsf { T } )$ is unique up to unique isomorphism. Hint: First figure out what “unique up to unique isomorphism” means for such pairs, using a category of pairs (T, t). Then follow the analogous argument for the product.

In short, given M and $\Nu ,$ there is an A-bilinear map t : $M \times \mathsf { N } \to M \otimes _ { \mathsf { A } } \mathsf { N } _ { \mathsf { A } }$ unique up to unique isomorphism, defined by the following universal property: for any A-bilinear map $\mathbf { t } ^ { \prime } \colon M \times \mathsf { N }  \mathsf { T } ^ { \prime }$ there is a unique A-linear map f : $M \otimes _ { \mathsf { A } } \mathsf { N } \to \mathsf { T } ^ { \prime }$ such that $\mathbf { t } ^ { \prime } = \mathbf { f } \circ \bar { \mathbf { t } }$

As with all universal property arguments, this argument shows uniqueness assuming existence. To show existence, we need an explicit construction.

1.2.J. EXERCISE. Show that the construction of §1.2.5 satisfies the universal property of tensor product.

The three exercises below are useful facts about tensor products with which you should be familiar.

## 1.2.K. IMPORTANT EXERCISE.

(a) If M is an A-module and $A  \mathrm { ~ B ~ }$ is a morphism of rings, give $\textsf { B } \otimes _ { A }$ M the structure of a B-module (this is part of the exercise). Show that this describes a functor $M o d _ { \mathrm { A } }  M o d _ { \mathrm { B } }$ .

(b) (tensor product of rings) If further $\lambda  { \cal C }$ is another morphism of rings, show that B ⊗A C has a natural structure of a ring. Hint: Multiplication will be given by $(  { \mathbf { b } } _ { 1 } \otimes  { \mathbf { c } } _ { 1 } ) (  { \mathbf { b } } _ { 2 } \otimes  { \mathbf { c } } _ { 2 } ) = (  { \mathbf { b } } _ { 1 }  { \mathbf { b } } _ { 2 } ) \otimes (  { \mathbf { c } } _ { 1 }  { \mathbf { c } } _ { 2 } )$ . (Exercise 1.2.U will interpret this construction as a fibered coproduct.)

1.2.L. IMPORTANT EXERCISE. If S is a multiplicative subset of A and M is an A-module, describe a natural isomorphism $( S ^ { - 1 } A ) \otimes _ { A } M \ { \stackrel { \sim } { \longrightarrow } } \ S ^ { - 1 } M \ ( { \mathrm { a s } } \ S ^ { - 1 } A -$ modules and as A-modules).

1.2.M. EXERCISE (⊗ COMMUTES WITH ⊕). Show that tensor products commute with arbitrary direct sums: if M and $\{ { \mathsf { N } } _ { \mathrm { i } } \} _ { \mathrm { i } \in \mathrm { I } }$ are all A-modules, describe an isomorphism

$$
\mathsf { M } \otimes \left( \oplus _ { \mathsf { i } \in \mathsf { I } } \mathsf { N } _ { \mathrm { i } } \right) \xrightarrow [ ] { \sim } \oplus _ { \mathsf { i } \in \mathsf { I } } \left( \mathsf { M } \otimes \mathsf { N } _ { \mathrm { i } } \right) .
$$

1.2.6. Essential Example: Fibered products. Suppose we have morphisms $\alpha \colon X \to$ Z and $\beta \colon \Upsilon  Z$ (in any category). Then the fibered product (or fibred product) is an object $X \times _ { Z } Y$ along with morphisms $\operatorname { p r } x \colon X \times _ { Z } \Upsilon \to X$ and prY : ${ \sf X } \times _ { Z } { \sf Y } \to { \sf Y } ,$ where the two compositions $\alpha \circ { \sf p r } _ { \sf X } , \beta \circ { \sf p r } _ { \sf Y } \colon X \times _ { Z } \sf Y \to Z$ agree, such that given any object W with maps to X and Y (whose compositions to Z agree), these maps factor through some unique $W \to X \times _ { Z } \ Y ;$

<!-- image-->

(Warning: The definition of the fibered product depends on α and $\beta ,$ , even though they are omitted from the notation $X \times _ { Z } Y . )$

By the usual universal property argument, if it exists, it is unique up to unique isomorphism. (You should think this through until it is clear to you.) Thus the use of the phrase “the fibered product” (rather than $\mathbf { \bar { \rho } } _ { \mathbf { \hat { d } } }$ fibered product”) is reasonable, and we should reasonably be allowed to give it the name ${ \boldsymbol { \mathrm { X } } } \times { \boldsymbol { \mathrm { \Sigma } } } = { \boldsymbol { \mathrm { Y } } } .$ We know what maps to it are: they are precisely maps to X and maps to Y that agree as maps to Z.

1.2.7. Definition. As an example, if π : $\Chi \to \Upsilon$ is a morphism, and the fibered product $\dot { x } \times \dot { y } X$ exists, then this determines a diagonal morphism $\delta _ { \pi } \colon X \to X \times _ { Y } X$ The diagonal morphism will turn out to be a very useful notion.

Depending on your religion, the diagram

<!-- image-->

is called a fibered/pullback/Cartesian diagram/square (six possibilities — and even more are possible if you prefer “fibred” to “fibered”).

The right way to interpret the notion of fibered product is first to think about what it means in the category of sets.

1.2.N. EXERCISE (FIBERED PRODUCTS OF SETS). Show that in Sets,

$$
X \times _ { Z } { \mathsf { Y } } = \{ ( { \mathsf { x } } , { \mathsf { y } } ) \in X \times { \mathsf { Y } } \ : \ \alpha ( { \mathsf { x } } ) = \beta ( { \mathsf { y } } ) \} .
$$

More precisely, show that the right side, equipped with its evident maps to X and $\Upsilon ,$ satisfies the universal property of the fibered product. (This will help you build intuition for fibered products.)

1.2.O. EXERCISE. If X is a topological space, show that fibered products always exist in the category of open sets of $\Sigma ,$ by describing what a fibered product is. (Hint: It has a one-word description.)

1.2.P. EXERCISE. If Z is the final object in a category $\mathcal { C } ,$ and $\qquad X , \Upsilon \in { \mathcal { C } } ,$ show that ${ } ^ { \prime \prime } X \times _ { Z } Y = X \times Y ^ { \prime \prime } ;$ : “the” fibered product over Z is uniquely isomorphic to $\mathrm { \Delta ^ { \prime \prime } t h e ^ { \prime \prime } }$ product. Assume all relevant (fibered) products exist. (This is an exercise about unwinding the definition.)

1.2.Q. USEFUL EXERCISE: TOWERS OF CARTESIAN DIAGRAMS ARE CARTESIAN DIAGRAMS. If the two squares in the following commutative diagram are Cartesian diagrams, show that the “outside rectang $\mathrm { l e } ^ { \prime \prime }$ (involving U, ${ \mathsf { V } } , { \mathsf { Y } } ,$ and $\boldsymbol { Z } )$ is also a Cartesian diagram.

<!-- image-->

1.2.R. EXERCISE. Given morphisms ${ \cal X } _ { 1 }  \Upsilon , { \cal X } _ { 2 }  \Upsilon ,$ and $\Upsilon  Z ,$ show that there is a natural morphism ${ \sf X } _ { 1 } \times _ { Y } { \sf X } _ { 2 }  { \sf X } _ { 1 } \times _ { Z } { \sf X } _ { 2 }$ , assuming that both fibered products exist. (This is trivial once you figure out what it is saying. The point of this exercise is to see why it is trivial.)

1.2.S. IMPORTANT EXERCISE: THE DIAGONAL-BASE-CHANGE DIAGRAM. Suppose we are given morphisms $\Chi _ { 1 } , \qquad \to \mathsf { Y }$ and $\Upsilon  Z .$ Show that the following diagram is a Cartesian square.

<!-- image-->

Assume all relevant (fibered) products exist. (If this exercise is too hard now, you can try it again in Exercise 1.3.B.) You will appreciate how useful this diagram is when you repeatedly use the diagonal morphism in proofs and constructions.

If you liked this problem, you may enjoy Exercise 11.1.C.

1.2.8. Coproducts. Define coproduct in a category by reversing all the arrows in the definition of product. Define fibered coproduct in a category by reversing all the arrows in the definition of fibered product. Coproduct is denoted by \`.

1.2.T. EXERCISE. Show that coproduct for Sets is disjoint union. This is why we use the notation \` for disjoint union.

1.2.U. EXERCISE. Suppose $\lambda  \mathtt { B }$ and $A  C$ are two ring morphisms, so in particular B and C are A-modules. Recall (Exercise 1.2.K) that $\mathbb { B } \otimes _ { A } \mathbb { C }$ has a ring structure. Show that there is a natural morphism $\mathsf { B } \to \mathsf { B } \otimes _ { \mathsf { A } } \mathsf { C }$ given by b $\mapsto \boldsymbol { \mathsf { b } } \otimes \boldsymbol { \mathsf { l } }$ (This is not necessarily an inclusion; see Exercise 1.2.G.) Similarly, there is a natural morphism $\mathsf { C } \to \mathsf { B } \otimes _ { \mathsf { A } } \mathsf { \bar { C } } .$ . Show that this gives a fibered coproduct on rings, i.e., that

<!-- image-->

satisfies the universal property of fibered coproduct.

## 1.2.9. Monomorphisms and epimorphisms.

1.2.10. Definition. A morphism $\pi \colon X  \Upsilon$ is a monomorphism if any two morphisms $\mu _ { 1 } : Z  X$ and $\mu _ { 2 } \colon Z  X$ such that $\pi \circ \mu _ { 1 } = \pi \circ \mu _ { 2 }$ must satisfy $\mu _ { 1 } = \mu _ { 2 }$ . In other words, there is at most one way of filling in the dotted arrow so that the diagram

<!-- image-->

commutes — for any object $Z ,$ the natural map Mor $( Z , X ) \ \to \ \operatorname { M o r } ( Z , \Upsilon )$ is an injection. Intuitively, it is the categorical version of an injective map, and indeed this notion generalizes the familiar notion of injective maps of sets. (The reason we don’t use the word “injective” is that in some contexts, “injective” will have an intuitive meaning that may not agree with “monomorphism.” One example: in the category of divisible groups, the map $\mathbb { Q } \to \mathbb { Q } / \mathbb { Z }$ is a monomorphism but not injective. This is also the case with “epimorphism” — to be defined shortly — in contrast with “surjective.”)

1.2.V. EXERCISE. Show that the composition of two monomorphisms is a monomorphism.

1.2.W. EXERCISE. Prove that a morphism π: $X  \Upsilon$ is a monomorphism if and only if the fibered product $\boldsymbol { \mathrm { \Sigma } } \times \boldsymbol { \mathrm { \Sigma } } \times \boldsymbol { \mathrm { \Sigma } }$ exists, and the induced diagonal morphism $\delta _ { \pi } \colon X \to X \times _ { Y } X$ (Definition 1.2.7) is an isomorphism. We may then take this as the definition of monomorphism. (Monomorphisms aren’t central to future discussions, although they will come up again. This exercise is just good practice.)

1.2.X. EASY EXERCISE. We use the notation of Exercise 1.2.R. Show that if $\Upsilon  Z$ is a monomorphism, then the morphism ${ \sf X } _ { 1 } \times _ { \sf Y } { \sf X } _ { 2 }  { \sf X } _ { 1 } \times _ { Z } { \sf X } _ { 2 }$ you described in Exercise 1.2.R is an isomorphism. (Hint: For any object V, give a natural bijection between maps from V to the first and maps from V to the second. It is also possible to use the Diagonal-Base-Change diagram, Exercise 1.2.S.)

The notion of epimorphism is “dual” to the definition of monomorphism, where all the arrows are reversed. This concept will not be central for us, although it turns up in the definition of an abelian category. Intuitively, it is the categorical version of a surjective map. (But be careful when working with categories of objects that are sets with additional structure, as epimorphisms need not be surjective. Example: In the category Rings, $\mathbb { Z } \to \mathbb { Q }$ is an epimorphism, but obviously not surjective.)

1.2.11. Representable functors and Yoneda’s Lemma. Much of our discussion about universal properties can be cleanly expressed in terms of representable functors, under the rubric of “Yoneda’s Lemma.” Yoneda’s lemma is an easy fact stated in a complicated way. Informally speaking, you can essentially recover an object in a category by knowing the maps into it. For example, we have seen that the data of maps to $\boldsymbol { x } \times \boldsymbol { Y }$ are naturally (canonically) the data of maps to X and to Y. Indeed, we have now taken this as the definition of $\boldsymbol { x } \times \boldsymbol { Y }$

Recall Example 1.1.20. Suppose A is an object of category $\mathcal { C } .$ . For any object $\ b { \mathrm { C } } \in \mathcal { C }$ , we have a set of morphisms Mor $( \mathsf C , \mathsf A )$ . If we have a morphism $\mathsf { f } \colon \mathsf { B }  \mathsf { C } ,$ we get a map of sets

$$
\operatorname { M o r } ( \mathbb { C } , \mathbb { A } ) \longrightarrow \operatorname { M o r } ( \mathbb { B } , \mathbb { A } )\tag{1.2.11.1}
$$

by composition: given a map from C to A, we get a map from B to A by precomposing with $\mathsf { f } \colon \mathsf { B }  \mathsf { C }$ . Hence this gives a contravariant functor $\mathrm { h } _ { \mathrm { A } } \colon \mathcal { C } \to$ Sets. Yoneda’s Lemma states that the functor $\mathsf { h } _ { \mathsf { A } }$ determines A up to unique isomorphism. More precisely:

1.2.Y. IMPORTANT EXERCISE THAT YOU SHOULD DO ONCE IN YOUR LIFE (YONEDA’SLEMMA).

(a) Suppose you have two objects A and $A ^ { \prime }$ in a category ${ \mathcal { C } } ,$ and maps

$$
\mathrm { i } _ { \mathrm { C } } \colon \mathrm { M o r } ( \mathsf { C } , \mathsf { A } ) \longrightarrow \mathrm { M o r } ( \mathsf { C } , \mathsf { A } ^ { \prime } )\tag{1.2.11.2}
$$

that commute with the maps (1.2.11.1). Show that the $\mathrm { i } _ { \mathrm { C } }$ (as C ranges over the objects of C ) are induced from a unique morphism g: $A  A ^ { \prime }$ . More precisely,