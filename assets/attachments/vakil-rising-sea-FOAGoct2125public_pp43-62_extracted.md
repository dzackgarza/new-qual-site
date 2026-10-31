show that there is a unique morphism g: $A  A ^ { \prime }$ such that for all $C \in { \mathcal { C } } ,$ iC is $\mathfrak { u } \mapsto \mathfrak { g } \circ \mathfrak { u } .$

(b) If furthermore the $\mathrm { i } _ { \mathrm { C } }$ are all bijections, show that the resulting g is an isomorphism. (Hint for both: This is much easier than it looks. This statement is so general that there are really only a couple of things that you could possibly try. For example, if you’re hoping to find a morphism $\bar { A _ { \mathbf { \lambda } } } \to \bar { A _ { \mathbf { \lambda } } } ^ { \prime } .$ , where will you find it? Well, you are looking for an element $\operatorname { M o r } ( \mathsf { A } , \mathsf { A } ^ { \prime } )$ . So just plug $\mathsf C = A$ into (1.2.11.2), and see where the identity goes.)

There is an analogous statement with the arrows reversed, where instead of maps into $\mathsf { A } ,$ you think of maps from A. The role of the contravariant functor $\mathsf { h } _ { \mathsf { A } }$ of Example 1.1.20 is played by the covariant functor $\mathrm { h } ^ { A }$ of Example 1.1.14. Because the proof is the same (with the arrows reversed), you needn’t think it through.

The phrase “Yoneda’s Lemma” properly refers to a more general statement. Although it looks more complicated, it is no harder to prove.

## 1.2.Z. ⋆ EXERCISE.

(a) Suppose A and B are objects in a category $\mathcal { C } .$ . Give a bijection between the natural transformations $\mathrm { \bf h } ^ { \tt A }  \mathrm { \bf h } ^ { \tt B }$ of covariant functors $\mathcal { C } \to S e t s$ (see Example 1.1.14 for the definition) and the morphisms $\mathrm { B }  A$

(b) State and prove the corresponding fact for contravariant functors $\mathsf { h } _ { \mathsf { A } }$ (see Example 1.1.20). Remark: A contravariant functor F from $\mathcal { C }$ to Sets is said to be representable if there is a natural isomorphism

$$
\xi \colon \mathsf { F } \longrightarrow \mathsf { h } _ { A } .
$$

Thus the representing object A is determined up to unique isomorphism by the pair (F, ξ). There is a similar definition for covariant functors. (We will revisit this in $\ S 7 . 6 ,$ and this problem will appear again as Exercise $7 . 6 . C$ . The element $\xi ^ { - 1 } ( \mathop { \bf i d } _ { A } ) \in \mathsf { F } ( A )$ is often called the “universal object”; do you see why?)

(c) Yoneda’s Lemma. Suppose F is a covariant functor $\mathcal { C }  S e t s ,$ , and $\lambda \in \mathcal { C }$ Give a bijection between the natural transformations $\mathfrak { h } ^ { A } \ \to \ \mathsf { F }$ and $\mathsf { F } ( A )$ . (The corresponding fact for contravariant functors is essentially Exercise 10.1.B.)

In fancy terms, Yoneda’s lemma states the following. Given a category $\mathcal { C } _ { \iota }$ , we can produce a new category, called the functor category of $\mathcal { C } ,$ where the objects are contravariant functors $\mathcal { C } \to S e t s ,$ and the morphisms are natural transformations of such functors. We have a functor (which we can usefully call h) from $\mathcal { C }$ to its functor category, which sends A to $\mathsf { h } _ { \mathsf { A } }$ . Yoneda’s Lemma states that this is a fully faithful functor, called the Yoneda embedding. (Fully faithful functors were defined in §1.1.15.)

1.2.12. Joke. The Yoda embedding, contravariant it is.

## 1.3 Limits and colimits

Two important definitions, those of limits and colimits, are determined by universal properties. They generalize a number of familiar constructions. I will give the definitions first, and then show you why they are familiar. For example, fractions will be motivating examples of colimits (Exercise 1.3.D(a)), and the p-adic integers (Example 1.3.4) will be motivating examples of limits.

1.3.1. Limits. We say that a category is a small category if the objects form a set and the morphisms form a set. (This is a technical condition intended only for experts.) Suppose $\mathcal { I }$ is any small category, and $\mathcal { C }$ is any category. Then a functor F : ${ \mathcal { I } }  { \mathcal { C } } ~ ( { \mathrm { i . e . } }$ , with an object $\boldsymbol { A } _ { \mathrm { i } } \in \mathcal { C }$ for each element ${ \mathfrak { i } } \in { \mathcal { I } } ,$ and appropriate commuting morphisms dictated by $\mathcal { I } )$ is said to be a diagram indexed by $\bar { \mathcal { S } }$ . We call $\mathcal { I }$ an index category. Our index categories will usually be partially ordered sets (Example 1.1.8), in which, in particular, there is at most one morphism between any two objects. (But other examples are sometimes useful.) For example, if □ is the category

<!-- image-->

and $\mathcal { A }$ is a category, then a functor $\square  \mathcal { A }$ is precisely the data of a commuting square in $\mathcal { A } .$

Then the limit of the diagram is an object lim $A _ { \mathrm { i } }$ (or lim− $\boldsymbol { \mathsf { A } } _ { \mathrm { i } } )$ of $\mathcal { C }$ along with morphisms $\mathsf { f } _ { \mathrm { j } }$ : lim $\lambda _ { \mathrm { i } } \to \lambda _ { \mathrm { j } }$ for each $\mathrm { j } \in { \mathcal { I } } ,$ , such that if m : $\stackrel { \mathcal { S } } { \mathrm { j } } $ k is a morphism in I ${ \mathcal { I } } ,$ then

(1.3.1.1)

<!-- image-->

commutes, and the object and the maps to each $A _ { \mathrm { i } }$ are universal (final) with respect to this property. More precisely, given any other object W along with maps $g _ { \mathrm { i } } \colon W \to \bar { \mathsf { A } } _ { \mathrm { i } }$ commuting with the F(m) (if m : j  k is a morphism in $\mathcal { \bar { I } } _ { \mathbf { \Phi } }$ , then ${ \mathfrak { g } } _ { \mathbf { k } } = { \mathsf { F } } ( { \mathfrak { m } } ) \circ { \mathfrak { g } } _ { \mathbf { j } } )$ , there is a unique map

$$
{ \mathfrak { g } } \colon W \to \operatorname* { l i m } _ { \mathcal { I } } { A _ { \mathrm { i } } }
$$

so that ${ \mathfrak { g } } _ { \mathrm { i } } = { \mathfrak { f } } _ { \mathrm { i } } \circ { \mathfrak { g } }$ for all i. (In some cases, the limit is sometimes called the inverse limit or projective limit. We won’t use this language.) By the usual universal property argument, if the limit exists, it is unique up to unique isomorphism.

1.3.2. Examples: Products. For example, if I is the partially ordered set

<!-- image-->

we obtain the fibered product.

If $\mathcal { I }$ is

we obtain the product.

If I is a set $( \mathrm { i . e . }$ , its only morphisms are the identity maps), then the limit is called the product of the $\lambda _ { \mathrm { i } } ,$ , and is denoted $\textstyle \prod _ { \mathrm { i } } A _ { \mathrm { i } }$ . The special case where $\mathcal { I }$ has two elements is the example of the previous paragraph.

1.3.A. EXERCISE (REALITY CHECK). Suppose that the partially ordered set $\mathcal { I }$ has an initial object e. Show that the limit of any diagram indexed by $\mathcal { I }$ exists.

1.3.B. EXERCISE: THE DIAGONAL-BASE-CHANGE DIAGRAM, AGAIN. Solve 1.2.S again by identifying both $X _ { 1 } \times _ { \mathsf { Y } } X _ { 2 }$ and $\mathsf { Y } \times _ { ( \mathsf { Y } \times z \mathsf { Y } ) } \left( \mathsf { X } _ { 1 } \times _ { Z } \mathsf { X } _ { 2 } \right)$ as the limit of the diagram

<!-- image-->

1.3.3. Example: Formal power series. For a ring A, the (formal) power series, $\mathsf { A } [ [ \boldsymbol { x } ] ]$ are often described informally (and somewhat unnaturally) as being the ring

$$
\pmb { \mathrm { A } } [ [ \pmb { x } ] ] = \{ \mathbf { a } _ { 0 } + \mathbf { a } _ { 1 } \pmb { x } + \mathbf { a } _ { 2 } \pmb { x } ^ { 2 } + \cdots \}
$$

(where ${ \mathfrak { a } } _ { \mathrm { i } } \in A _ { \cdot }$ , and the ring operations are the “obvious” ones). It is an example of a limit in the category of rings:

<!-- image-->

The universal property of limits yields a natural ring morphism $A [ x ]  A [ [ x ] ]$ ]. If A = R or C, this map factors through the ring of convergent power series.

1.3.4. Example: The p-adic integers. For a prime number p, the p-adic integers (or more informally, p-adics), $\mathbb { Z } _ { \mathfrak { p } } ,$ are often described informally (and somewhat unnaturally) as being of the form

$$
{ \bf a } _ { 0 } + { \bf a } _ { 1 } { \bf p } + { \bf a } _ { 2 } { \bf p } ^ { 2 } + \cdot \cdot \cdot
$$

(where $0 \leq \mathtt { a } _ { \mathrm { i } } < \mathtt { p } )$ ). They are an example of a limit in the category of rings:

<!-- image-->

(Warning: $\mathbb { Z } _ { \mathtt { p } }$ is sometimes used to denote the integers modulo p, but $\mathbb { Z } / ( { \mathfrak { p } } )$ or $\mathbb { Z } / { \mathsf { p } } \mathbb { Z }$ is better to use for this, to avoid confusion. Worse: by $\ S 1 . 2 . 3 , \mathbb { Z } _ { \mathfrak { p } }$ also denotes those rationals whose denominators are a power of p. Hopefully the meaning of $\mathbb { Z } _ { \mathfrak { p } }$ will be clear from the context.)

The similarity of Examples 1.3.3 and 1.3.4 is no coincidence. Formal power series and the p-adic integers are examples of completions, the topic of Chapter 28.

Limits do not always exist for any index category ${ \mathcal { I } } .$ However, you can often easily check that limits exist if the objects of your category can be interpreted as sets with additional structure, and arbitrary products exist (respecting the set-like structure).

## 1.3.C. IMPORTANT EXERCISE. Show that in the category Sets,

$$
\left\{ ( \mathbf { a } _ { \mathrm { i } } ) _ { \mathrm { i } \in \mathcal { I } } \in \prod _ { \mathrm { i } } \mathsf { A } _ { \mathrm { i } } : \mathsf { F } ( \mathsf { m } ) ( \mathbf { a } _ { \mathrm { j } } ) = \mathbf { a } _ { \mathrm { k } } \mathrm { ~ f o r ~ a l l ~ } \mathsf { m } \in \mathbf { M o r } _ { \mathcal { I } } ( \mathsf { j } , \mathsf { k } ) \subset \mathbf { M o r } ( \mathcal { I } ) \right\} ,
$$

along with the obvious projection maps to each $\mathsf { A } _ { \mathrm { i } }$ , is the limit lim $A _ { \mathrm { i } }$ I

This clearly also works in the category ModA of A-modules (in particular, $V e c _ { \mathrm { k } }$ and Ab), as well as Rings.

From this point of view, $2 + 3 \mathfrak { p } + 2 \mathfrak { p } ^ { 2 } + \cdot \cdot \cdot \in \mathbb { Z } \mathfrak { p }$ can be understood as the sequence $( 2 , 2 \bar { + } 3 \mathsf p , 2 + 3 \mathsf p + 2 \mathsf p ^ { 2 } , \ldots )$

1.3.5. Colimits. More immediately relevant for us will be the dual (arrow-reversed version) of the notion of limit (or inverse limit). We just flip the arrows $\mathsf { f } _ { \mathrm { i } }$ in (1.3.1.1), and get the notion of a colimit, which is denoted colim $\mathcal { I } \hat { A } _ { \mathrm { i } }$ (or $\underline { { \operatorname* { l i m } } } _ { \mathcal { I } } A _ { \mathrm { i } } )$ (You →should draw the corresponding diagram.) Again, if it exists, it is unique up to unique isomorphism. (In some cases, the colimit is sometimes called the direct limit, inductive limit, or injective limit. We won’t use this language. I prefer using limit/colimit in analogy with kernel/cokernel and product/coproduct. This is more than analogy, as kernels and products may be interpreted as limits, and similarly with cokernels and coproducts. Also, I remember that kernels “map $\mathrm { t o } , \prime \prime$ and cokernels are “mapped $\mathrm { t o } , ^ { \prime \prime }$ which reminds me that a limit maps to all the objects in the big commutative diagram indexed by ${ \mathcal { I } } ;$ and a colimit has a map from all the objects.)

## 1.3.6. Joke. A comathematician is a device for turning cotheorems into ffee.

Even though we have just flipped the arrows, colimits behave quite differently from limits.

1.3.7. Example. The abelian group $5 ^ { - \infty } \mathbb { Z }$ of rational numbers whose denominators are powers of 5 is a colimit colim $\mathfrak { i } \in \mathbb { Z } ^ { + } ^ { 5 ^ { - 1 } \mathbb { Z } }$ . More precisely, $5 ^ { - \infty } \mathbb { Z }$ is the colimit of the diagram

$$
\mathbb { Z } \longrightarrow 5 ^ { - 1 } \mathbb { Z } \longrightarrow 5 ^ { - 2 } \mathbb { Z } \longrightarrow \cdots
$$

in the category of abelian groups.

The colimit over an index set I is called the coproduct, denoted $\operatorname { I I } _ { \mathrm { i } } \boldsymbol { A } _ { \mathrm { i } }$ , and is the dual (arrow-reversed) notion to the product.

## 1.3.D. EXERCISE.

(a) Interpret the statement $\begin{array} { r } { { \mathrm { \Omega } } ^ { \prime \prime } \mathbb { Q } = \operatorname { c o l i m } { \frac { 1 } { \mathrm { n } } } \mathbb { Z } . { \mathrm { \Omega } } ^ { \prime \prime } } \end{array}$ (b) Interpret the union of some subsets of a given set as a colimit. (Dually, the intersection can be interpreted as a limit.) The objects of the category in question are the subsets of the given set.

Colimits do not always exist, but there are two useful large classes of examples for which they do.

1.3.8. Definition. A nonempty partially ordered set $( S , \geq )$ is filtered (or is said to be a filtered set) if for each $x , y \in S .$ , there is a z such that $x \ge z$ and $y \geq z .$ . More generally (see Figure 1.1), a nonempty category $\mathcal { I }$ is filtered if:

(i) for each $x , y \in { \mathcal { I } } ,$ there is ${ \sf a } z \in \mathcal { I }$ and arrows x  z and y  z, and

(ii) for every two arrows u : x  y and $\nu \colon x  y$ , there is an arrow w : $y  z$ such that w $\circ \mathrm { u } = \boldsymbol { w } \circ \boldsymbol { \nu } .$

(Other terminologies are also commonly used, such as “directed partially ordered $\operatorname { s e t } ^ { \prime \prime }$ and “filtered index category,” respectively.)

<!-- image-->

<!-- image-->  
FIGURE 1.1. A filtered category (pictorial definition).

1.3.E. EXERCISE. Suppose $\mathcal { I }$ is filtered. (We will almost exclusively use the case where $\mathcal { I }$ is a filtered set.) Recall the symbol \` for disjoint union of sets. Show that any diagram in Sets indexed by $\mathcal { I }$ has the following, with the obvious maps to it, as a colimit:

$\left\{ ( \mathbf { a } _ { \mathrm { i } } , \mathrm { i } ) \in \prod _ { \mathrm { i } \in \mathcal { I } } \mathsf { A } _ { \mathrm { i } } \right\} \Biggl / \binom { ( \mathbf { a } _ { \mathrm { i } } , \mathrm { i } ) \sim ( \mathbf { a } _ { \mathrm { j } } , \mathrm { j } ) } { 9 \colon \mathsf { A } _ { \mathrm { j } } \to \mathsf { A } _ { \mathrm { k } } \mathrm { i n t } }$ if and only if there are f : $\lambda _ { \mathrm { i } } \to \lambda _ { \mathrm { k } }$ and  he diagram for which $\mathsf { f } ( \mathbf { a } _ { \mathrm { i } } ) = \mathsf { g } ( \mathbf { a } _ { \mathrm { j } } ) \mathrm { i n } \mathsf { A } _ { \mathrm { k } }  \rule { 0.3 cm } { 0 cm } / \ln \mathsf { A } _ { \mathrm { k } } \rule { 0 ex } { 0 ex } \bigg /$

(You will see that the “filtered” hypothesis is there is to ensure that ∼ is an equivalence relation.)

For example, in Example 1.3.7, each element of the colimit is an element of something upstairs, but you can’t say in advance what it is an element of. For instance, 17/125 is an element of $5 ^ { - 3 } \overline { { \mathbb { Z } } } ( \mathrm { o r } 5 ^ { - 4 } \mathbb { Z } ,$ or later ones), but not $5 ^ { - 2 } \mathbb { Z }$

This idea applies to many categories whose objects can be interpreted as sets with additional structure (such as abelian groups, A-modules, groups, etc.). For example, the colimit colim $M _ { \mathrm { i } }$ in the category of A-modules $M o d _ { A }$ can be described as follows. The set underlying colim $M _ { \mathrm { i } }$ is defined as in Exercise 1.3.E. To add the elements $\mathfrak { m } _ { \mathrm { i } } \ \in \ M _ { \mathrm { i } }$ and $\mathbf { m } _ { \mathrm { j } } \in M _ { \mathrm { j } } ,$ , choose an $\ell \in \mathcal { I }$ with arrows u : $i  \ell$ and $\nu \colon \mathrm { j } \to \ell ,$ and then define the sum of $\mathfrak { m } _ { \mathrm { i } }$ and $\mathfrak { m } _ { \mathrm { j } }$ to be $\mathsf { F } ( \mathfrak { u } ) ( \mathfrak { m } _ { \mathrm { i } } ) + \mathsf { F } ( \nu ) ( \mathfrak { m } _ { \mathrm { j } } ) \in$

$M _ { \ell }$ . The element $\mathfrak { m } _ { \mathrm { i } } \in M _ { \mathrm { i } }$ is 0 if and only if there is some arrow u : $i $ k for which $\mathsf { F } ( \mathrm { u } ) ( \mathsf { m } _ { \mathrm { i } } ) = 0 ,$ i.e., if and only if it becomes 0 “later in the diagram.” Last, multiplication by an element of A is defined in the obvious way.

1.3.F. EXERCISE. Verify that the A-module described above is indeed the colimit. (Make sure you verify that addition is well-defined, i.e., is independent of the choice of representatives $\mathrm { \ m _ { i } }$ and ${ \mathrm { m } } _ { \mathrm { j } } ,$ the choice of $\ell ,$ and the choice of arrows u and v. Similarly, make sure that scalar multiplication is well-defined.)

1.3.G. USEFUL EXERCISE (LOCALIZATION AS A COLIMIT). Generalize Exercise 1.3.D(a) to interpret localization of an integral domain as a colimit over a filtered set: suppose S is a multiplicative set of A, and interpret $S ^ { - 1 } A =$ colim $\textstyle { \frac { 1 } { s } } A$ where the colimit is over $s \in S$ , and in the category of A-modules. (Aside: Can you make some version of this work even if A isn’t an integral domain, $\mathrm { e . g . , } S ^ { - 1 } A = \mathrm { c o l i m } A _ { s } ?$ This will work in the category of A-algebras.)

A variant of this construction works without the filtered condition if you have another means of “connecting elements in different objects of your diagram.” For example:

1.3.H. EXERCISE: COLIMITS OF A-MODULES WITHOUT THE FILTERED CONDITION. Suppose you are given a diagram of A-modules indexed by ${ \mathcal { S } } \colon { \mathsf { F } } \colon { \mathcal { S } } \to M o d _ { \mathsf { A } }$ , where we let $M _ { \mathrm { i } } : = \mathsf { F } ( \mathrm { i } )$ . Show that the colimit is $\oplus _ { \mathrm { i } \in \mathcal { I } } M _ { \mathrm { i } }$ modulo the relations $\mathsf { m } _ { \mathrm { i } } - \mathsf { F } ( \mathsf { n } ) ( \mathsf { m } _ { \mathrm { i } } )$ for every n : i  j in $\mathcal { I } \left( \mathrm { i . e . } \right)$ , for every arrow in the diagram). (Somewhat more precisely: “modulo” means “quotiented by the submodule generated by.”)

1.3.9. Summary. One useful thing to informally keep in mind is the following. In a category where the objects are “set-like,” an element of a limit can be thought of as a family of elements of each object in the diagram that are “compatible” (Exercise 1.3.C). And an element of a colimit can be thought of as (“has a representative that is”) an element of a single object in the diagram (Exercise 1.3.E). Even though the definitions of limit and colimit are the same, just with arrows reversed, these interpretations are quite different.

1.3.10. Small remark. In fact, colimits exist in the category of sets for all reasonable (“small”) index categories (see for example [E, Thm. A6.1]), but that won’t matter to us.

1.3.11. Joke. What do you call someone who reads a paper on category theory? Answer: A coauthor.

## 1.4 Adjoints

We next come to a very useful notion closely related to universal properties. Just as a universal property “essentially” (up to unique isomorphism) determines an object in a category (assuming such an object exists), “adjoints” essentially determine a functor (again, assuming it exists). Two covariant functors F : ${ \mathcal { A } } \to { \mathcal { B } }$ and $\mathsf { G } \colon \mathcal { B }  \mathcal { A }$ are adjoint if there is a natural bijection for all $\boldsymbol { A } \in \mathcal { A }$ and $\mathrm { B } \in { \mathcal { B } } ,$

$$
\tau _ { A \mathrm { B } } \colon \mathrm { M o r } _ { \mathscr { B } } ( \mathsf { F } ( A ) , \mathsf { B } )  \mathrm { M o r } _ { \mathscr { A } } ( A , \mathsf { G } ( \mathsf { B } ) ) .\tag{1.4.0.1}
$$

We say that (F, G) form an adjoint pair, and that F is left-adjoint to G (and G is right-adjoint to F). We say F is a left adjoint (and G is a right adjoint). By “natural” we mean the following. For all $\mathsf { f } \colon \lambda \to \bar { A } ^ { \prime }$ in $\mathcal { A }$ , we require

$$
\begin{array} { r l } & { \mathrm { M o r } _ { \mathcal { B } } ( \mathsf { F } ( A ^ { \prime } ) , \mathsf { B } ) \xrightarrow { \mathsf { F f } ^ { * } } \succ \mathrm { M o r } _ { \mathcal { B } } ( \mathsf { F } ( A ) , \mathsf { B } ) } \\ & { \qquad \sqrt { \tau _ { A ^ { \prime } \mathrm { B } } } } \\ & { \mathrm { M o r } _ { \mathcal { A } } ( A ^ { \prime } , \mathsf { G } ( \mathsf { B } ) ) \xrightarrow { \mathsf { f } ^ { * } } \succ \mathrm { M o r } _ { \mathcal { A } } ( A , \mathsf { G } ( \mathsf { B } ) ) } \end{array}\tag{1.4.0.2}
$$

to commute, and for all $g \colon \mathrm { B }  \mathrm { B } ^ { \prime }$ in $\mathcal { B }$ we want a similar commutative diagram to commute. (Here f∗ is the map induced by $\mathsf { f } \colon \lambda \to \mathsf { A } ^ { \prime } .$ , and $\mathsf { F f } ^ { * }$ is the map induced by $\mathsf { F f } \colon \mathsf { F } ( \mathsf { A } )  \mathsf { F } ( \mathsf { A } ^ { \prime } ) . \big )$ )

1.4.A. EXERCISE. Write down what this diagram should be.

1.4.B. EXERCISE. Show that the map $\tau _ { \mathrm { A B } } \ ( 1 . 4 . 0 . 1 )$ has the following properties. For each A there is a map $\boldsymbol \eta _ { \mathsf { A } } \colon \mathsf { A } \ \to \ \mathsf { G F } ( \boldsymbol { A } )$ so that for any ${ \mathfrak { g } } \colon { \mathsf { F } } ( A ) ~  ~ \mathsf { B }$ , the corresponding $\tau _ { A \mathrm { B } } ( { \mathfrak { g } } ) \colon { \mathsf { A } } \to { \mathsf { G } } ( { \mathsf { B } } )$ is given by the composition

$$
\begin{array} { r } { A \xrightarrow { \ \eta _ { A } } \mathsf { G F } ( A ) \xrightarrow { \mathsf { G g } } \mathsf { G } ( \mathsf { B } ) . } \end{array}
$$

Similarly, there is a map $\epsilon _ { \mathrm { B } } \colon \mathsf { F G } ( \mathsf { B } ) \to \mathsf { B }$ for each B so that for any f : $A \to { \mathsf { G } } ( { \mathsf { B } } )$ the corresponding map $\tau _ { \mathrm { A B } } ^ { - 1 } ( \mathsf { f } ) \colon \mathsf { F } ( A )  \mathsf { I }$ B is given by the composition

$$
\begin{array} { r } { \mathsf { F } ( \mathsf { A } ) \xrightarrow { \mathsf { F f } } \mathsf { F G } ( \mathsf { B } ) \xrightarrow { \mathsf { \epsilon } _ { \mathsf { B } } } \mathsf { B } . } \end{array}
$$

Here is a key example of an adjoint pair.

1.4.C. EXERCISE. Suppose M, N, and P are A-modules (where A is a ring). Describe a bijection Hom $\mathfrak { l } _ { A } ( \bar { \mathsf { M } } \bar { \otimes } _ { A } \mathsf { N } , \mathsf { P } ) \longleftrightarrow \mathrm { H o m } _ { A } ( \mathsf { M } , \mathrm { H o m } _ { A } ( \mathsf { N } , \mathsf { P } ) )$ . (Hint: Try to use the universal property of ⊗.)

1.4.D. EXERCISE (TENSOR-HOM ADJUNCTION). Show that $( \cdot ) \otimes _ { A } \mathsf { N }$ and $\mathrm { H o m } _ { A } ( \mathsf { N } , \cdot )$ are adjoint functors.

1.4.E. EXERCISE. Suppose $\mathrm { B }  A$ is a morphism of rings. If M is an A-module, you can create a B-module $M _ { \mathrm { B } }$ by considering it as a B-module. This gives a functor $\cdot _ { \mathrm { B } } \colon M o d _ { \mathrm { A } }  M o d _ { \mathrm { B } }$ . Show that this functor is right-adjoint to $\otimes _ { \mathsf { B } } { \mathsf { A } }$ . In other words, describe a bijection

$$
\operatorname { H o m } _ { A } ( \mathsf { N } \otimes _ { \mathsf { B } } A , \mathsf { M } ) \cong \operatorname { H o m } _ { \mathsf { B } } ( \mathsf { N } , \mathsf { M } _ { \mathsf { B } } )
$$

functorial in both arguments. (This adjoint pair is very important.)

1.4.1. ⋆ Fancier remarks we won’t use. You can check that the left adjoint determines the right adjoint up to natural isomorphism, and vice versa. The maps ηA and $\epsilon _ { \tt B }$ of Exercise 1.4.B are called the unit and counit of the adjunction. This leads to a different characterization of adjunction. Suppose functors F: ${ \mathcal { A } }  { \mathcal { B } }$ and $\mathsf { G } \colon \mathcal { B }  \mathcal { A }$ are given, along with natural transformations $\eta \colon \mathrm { i d } _ { \mathcal { A } }  \mathsf { G F }$ and $\epsilon \colon \mathsf { F G }  \mathrm { i d } _ { \mathcal { B } }$ with the property that Gϵ $\circ \boldsymbol { \eta } \mathsf { G } = \mathsf { i d } _ { \mathsf { G } }$ (for each $\boldsymbol { \mathrm { B } } \in \mathcal { B } ,$ , the composition of $\boldsymbol { \eta } _ { \mathsf { G } ( \mathsf { B } ) } \colon \mathsf { G } ( \mathsf { B } ) $

GFG(B) and $\mathsf { G } ( \epsilon _ { \mathsf { B } } ) \colon \mathsf { G F G } ( \mathsf { B } ) \to \mathsf { G } ( \mathsf { B } )$ is the identity) and ϵF ◦ $\mathsf { F } \mathsf { \eta } = \mathsf { i d } _ { \mathsf { J } }$ F. Then you can check that F is left-adjoint to G. These facts aren’t hard to check, so if you want to use them, you should verify everything for yourself.

1.4.2. Examples from other fields. For those familiar with representation theory: Frobenius reciprocity may be understood in terms of adjoints. Suppose V is a finite-dimensional representation of a finite group $\mathsf { G } ,$ and $\boldsymbol { w }$ is a representation of a subgroup ${ \mathsf { H } } < { \mathsf { G } }$ . Then induction and restriction are an adjoint pair $( \mathrm { I n d } _ { \mathsf { H } } ^ { \mathsf { G } } , \mathrm { R e s } _ { \mathsf { H } } ^ { \mathsf { G } } )$ between the category of G-modules and the category of H-modules.

Topologists’ favorite adjoint pair may be the suspension functor and the loop space functor.

1.4.3. Example: Groupification of abelian semigroups. Here is another motivating example: getting an abelian group from an abelian semigroup. (An abelian semigroup is just like an abelian group, except we don’t require an identity or an inverse. Morphisms of abelian semigroups are maps of sets preserving the binary operation. One example is the nonnegative integers $\mathbb { Z } ^ { \geq 0 } = \{ \stackrel { \bullet } { 0 } , 1 , 2 , \ldots \}$ under addition. Another is the positive integers $\mathbb { Z } ^ { + } = \left\{ 1 , 2 , 3 , \ldots \right\}$ under addition. Yet another is the positive integers $\mathbb { Z } ^ { + }$ under multiplication. You may enjoy groupifying all three.) From an abelian semigroup, you can create an abelian group. In our examples, from the nonnegative integers under addition $( \mathbb { Z } ^ { \geq 0 } , + )$ , we create the integers $\left( \mathbb { Z } , + \right)$ and from the positive integers under multiplication $( \mathbb { Z } ^ { + } , \times )$ , we create the positive rationals $( \mathbb { Q } ^ { + } , \times )$ . Here is a formalization of that notion. A groupification of an abelian semigroup S is a map of abelian semigroups π: $S  { \sf G }$ such that G is an abelian group, and any map of abelian semigroups from S to an abelian group $\mathsf { G } ^ { \prime }$ factors uniquely through G:

<!-- image-->

(Perhaps “abelian groupification” would be more precise than “groupification.”)

1.4.F. EXERCISE (AN ABELIAN GROUP IS GROUPIFIED BY ITSELF). Show that if an abelian semigroup is already a group then the identity morphism is the groupification. (More correct: the identity morphism is a groupification.) Note that you don’t need to construct groupification (or even know that it exists in general) to solve this exercise.

1.4.G. EXERCISE. Construct the “groupification functor” H from the category of nonempty abelian semigroups to the category of abelian groups. (One possible construction: given an abelian semigroup S, the elements of its groupification H(S) are ordered pairs $( { \mathbf { a } } , { \mathbf { b } } ) \in { \mathsf { S } } \times { \mathsf { S } } ,$ which you may think of as ${ \mathfrak { a } } - { \mathfrak { b } } _ { i }$ , with the equivalence that $( { \bf a } , { \bf b } ) \sim ( { \bf c } , { \bf d } )$ if ${ \bf a } + { \bf d } + e = { \bf b } + { \bf c } + e$ for some $e \in S$ . Describe addition in this group, and show that it satisfies the properties of an abelian group. Describe the abelian semigroup map $S \to \mathsf { H } ( S ) . )$ Let F be the forgetful functor from the category of abelian groups Ab to the category of abelian semigroups. Show that H is left-adjoint to F.

(Here is the general idea for experts: We have a full subcategory of a category. We want to “project” from the category to the subcategory. We have

$$
\mathrm { M o r } _ { \mathrm { c a t e g o r y } } ( \mathsf { S } , \mathsf { H } ) = \mathrm { M o r } _ { \mathrm { s u b c a t e g o r y } } ( \mathsf { G } , \mathsf { H } )
$$

automatically; thus we are describing the left adjoint to the forgetful functor. How the argument worked: we constructed something which was in the smaller category, which automatically satisfies the universal property.)

1.4.H. EXERCISE (CF. EXERCISE 1.4.E). The purpose of this exercise is to give you more practice with “left adjoints of forgetful functors,” the means by which we get abelian groups from abelian semigroups, and sheaves from presheaves. Suppose A is a ring, and S is a multiplicative subset. Then $S ^ { - 1 } A$ -modules are a full subcategory (§1.1.15) of the category of A-modules (via the obvious inclusion $M o d _ { S ^ { - 1 } A } \overset { \cdot } { \longrightarrow } M o d _ { A } )$ . Then $M o d _ { \cal A }  \mathrm { \bar { \it M o d } } _ { S ^ { - 1 } A }$ can be interpreted as an adjoint to the forgetful functor $M o d _ { S ^ { - 1 } A }  M o d _ { A }$ . State and prove the correct statements.

(Here is the larger story. Every $S ^ { - 1 } A$ -module is an A-module, and this is an injective map, so we have a forgetful functor F: $M o d _ { S ^ { - 1 } A }  M o d _ { A }$ . In fact this is a fully faithful functor: it is injective on objects, and the morphisms between any two $S ^ { - 1 } A$ -modules as A-modules are just the same when they are considered as $\mathsf { \bar { S } } ^ { - 1 } A$ -modules. Then there is a functor ${ \sf G } \colon M o d _ { \sf A } \  \ M o d _ { { \sf S } ^ { - 1 } { \sf A } } .$ , which might reasonably be called “localization with respect to $S , \prime \prime$ which is left-adjoint to the forgetful functor. Translation: If M is an A-module, and N is an $S ^ { - 1 }$ A-module, then Mor(GM, N) (morphisms as $S ^ { - 1 } A$ -modules, which are the same as morphisms as A-modules) are in natural bijection with Mor(M, FN) (morphisms as A-modules).)

Table 1 gives most of the adjoints that will come up for us. Other examples will also come up, such as the adjoint pair $( \sim , \Gamma _ { \bullet } )$ between graded modules over a graded ring, and quasicoherent sheaves on the corresponding projective scheme (§15.7).

1.4.4. Last comments only for people who have seen adjoints before. If (F, G) is an adjoint pair of functors, then F commutes with colimits, and G commutes with limits. Also, limits commute with limits and colimits commute with colimits. We will prove these facts (and a little more) in §1.5.14.

## 1.5 An introduction to abelian categories

Ton papier sur l’Alg\`ebre homologique a ´et´e lu soigneusement, et a converti tout le monde (mˆeme Dieudonn´e, qui semble compl\`etement fonctoris´e!) \`a ton point de vue.

Your paper on homological algebra was read carefully and converted everyone (even Dieudonn´e, who seems to be completely functorised!) to your point of view.

— J.-P. Serre, letter to A. Grothendieck, July 13, 1955 [GrS, pp. 17–18]

Since learning linear algebra, you have been familiar with the notions and behaviors of kernels, cokernels, etc. Later in your life you saw them in the category of abelian groups, and later still in the category of A-modules.

We will soon define some new categories (certain sheaves) that will have familiar-looking behavior, reminiscent of that of modules over a ring. The notions of kernels, cokernels, images, and more will make sense, and they will behave “the way we expect” from our experience with modules. This can be made precise through the notion of an abelian category. Abelian categories are the right general setting in which one can do “homological algebra,” in which notions of kernel, cokernel, and so on are used, and one can work with complexes and exact sequences.

Pre-publication version (2025-10-21) of The Rising Sea: Foundations of Algebraic Geometry
<table><tr><td rowspan=1 colspan=1>situation</td><td rowspan=1 colspan=1>category $\mathcal { A }$ </td><td rowspan=1 colspan=1>categoryB</td><td rowspan=1 colspan=1>left adjoint $\mathsf { F } \colon \mathcal { A } \stackrel { \cdot } {  } \mathcal { B }$ </td><td rowspan=1 colspan=1>right adjoint $\check { \mathsf { G } } \colon \mathcal { B } \stackrel { \cdot } { \to } \mathcal { A }$ </td></tr><tr><td rowspan=1 colspan=1>A-modules (Ex. 1.4.D)</td><td rowspan=1 colspan=1>ModA</td><td rowspan=1 colspan=1> $\overline { { M o d _ { A } } }$ </td><td rowspan=1 colspan=1>(·) AN</td><td rowspan=1 colspan=1> $\overline { { \mathrm { H o m } _ { A } ( \mathsf { N } , \cdot ) } }$ </td></tr><tr><td rowspan=1 colspan=1>ring mapsB → A (Ex. 1.4.E)</td><td rowspan=1 colspan=1> $M o d _ { \mathrm { B } }$ </td><td rowspan=1 colspan=1> $M o d _ { A }$ </td><td rowspan=1 colspan=1> $\overline { { ( \cdot ) \otimes _ { \mathrm { B } } A } }$ (extensionof scalars)</td><td rowspan=1 colspan=1> $\overline { { { \cal { M } } \mapsto { \cal { M } } _ { \mathrm { { B } } } } }$ (restrictionof scalars)</td></tr><tr><td rowspan=1 colspan=1>(pre)sheaves on atopological spaceX (Ex. 2.4.K)</td><td rowspan=1 colspan=1>presheaveson X</td><td rowspan=1 colspan=1>sheaveson X</td><td rowspan=1 colspan=1>sheafification</td><td rowspan=1 colspan=1>forgetful</td></tr><tr><td rowspan=1 colspan=1>(semi)groups (§1.4.3)</td><td rowspan=1 colspan=1>semigroups</td><td rowspan=1 colspan=1>groups</td><td rowspan=1 colspan=1>groupification</td><td rowspan=1 colspan=1>forgetful</td></tr><tr><td rowspan=1 colspan=1>sheaves,π: X → Y (Ex. 2.7.B)</td><td rowspan=1 colspan=1>sheaveson Y</td><td rowspan=1 colspan=1>sheaveson X</td><td rowspan=1 colspan=1> $\overline { { \pi ^ { - 1 } } }$ </td><td rowspan=1 colspan=1> $\pi _ { * }$ </td></tr><tr><td rowspan=1 colspan=1>sheaves of abeliangroups or O-modules,open embeddingsπ: U → Y (Ex. 23.4.G)</td><td rowspan=1 colspan=1>sheaveson U</td><td rowspan=1 colspan=1>sheaveson Y</td><td rowspan=1 colspan=1>π!</td><td rowspan=1 colspan=1> $\pi ^ { - 1 }$ </td></tr><tr><td rowspan=1 colspan=1>quasicoherent sheaves,π: X → Y (Prop. 14.5.7)</td><td rowspan=1 colspan=1> $\overline { { Q C o h _ { \Upsilon } } }$ </td><td rowspan=1 colspan=1> $\overline { { Q C o h _ { X } } }$ </td><td rowspan=1 colspan=1> $\pi ^ { * }$ </td><td rowspan=1 colspan=1> $\pi _ { * }$ </td></tr><tr><td rowspan=1 colspan=1>ring mapsB → A (Ex. 17.1.J)</td><td rowspan=1 colspan=1> $M o d _ { A }$ </td><td rowspan=1 colspan=1> $M o d _ { \mathrm { B } }$ </td><td rowspan=1 colspan=1> $M \mapsto M _ { \mathrm { B } }$ (restrictionof scalars)</td><td rowspan=1 colspan=1> $\overline { { \mathsf { N } \mapsto } }$  $\mathrm { H o m } _ { \mathrm { B } } ( \boldsymbol { A } , \mathsf { N } )$ </td></tr><tr><td rowspan=1 colspan=1>quasicoherent sheaves,affine π: X → Y(Ex. 17.1.K(b))</td><td rowspan=1 colspan=1> $Q C o h _ { X }$ </td><td rowspan=1 colspan=1> $Q C o h _ { \mathsf { Y } }$ </td><td rowspan=1 colspan=1> $\pi _ { * }$ </td><td rowspan=1 colspan=1> $\pi ^ { ! ? }$ </td></tr></table>

TABLE 1. Some important adjoint pairs.

We will see enough to motivate the definitions that we will see in general: monomorphism (and subobject), epimorphism, kernel, cokernel, and image. But in this book we will avoid showing that they behave “the way we expect” in a general abelian category because the examples we will see are directly interpretable in terms of modules over rings. In particular, it is not worth memorizing the definition of abelian category.

Two central examples of an abelian category are the category Ab of abelian groups, and the category $M o d _ { A }$ of A-modules. The first is a special case of the second (just take $A = \mathbb { Z } )$ . As we give the definitions, you should verify that $M o d _ { A }$ is an abelian category.

We first define the notion of additive category. We will use it only as a stepping stone to the notion of an abelian category. Two examples you can keep in mind while reading the definition: the category of free A-modules (where A is a ring), and real (or complex) Banach spaces.

1.5.1. Definition. A category C is said to be additive if it satisfies the following properties.

Ad1. For each $\mathsf { A } , \mathsf { B } \in \mathcal { C } , \mathsf { M o r } ( \mathsf { A } , \mathsf { B } )$ is an abelian group, such that composition of morphisms distributes over addition. (You should think about what this means — it translates to two distinct statements.)

Ad2. C has a zero object, denoted 0. (This is an object that is simultaneously an initial object and a final object, Definition 1.2.2.)

$\operatorname { A d } 3 .$ It has products of two objects (a product A × B for any pair of objects), and hence, by induction, products of any finite number of objects.

In an additive category, the morphisms are often called homomorphisms, and Mor is denoted by Hom. In fact, the notation Hom is a good indication that you’re working in an additive category. A functor between additive categories preserving the additive structure of Hom is called an additive functor.

1.5.2. Remarks. It is a consequence of the definition of additive category that finite products are also finite coproducts $( \mathrm { i . e . , s u m s } )$ — the details don’t matter to us. The symbol ⊕ is used for this notion. ${ \mathrm { A l s o } } ,$ it is quick to show that additive functors send zero objects to zero objects (show that Z is a 0-object if and only if $\mathrm { i d } _ { Z } = 0 _ { Z } ;$ additive functors preserve both id and 0), and preserve products.

One motivation for the name 0-object is that the 0-morphism in the abelian group Hom(A, B) is the composition $A  0  \mathbb { B }$ . (We also remark that the notion of 0-morphism thus makes sense in any category with a 0-object.)

(A cleaner axiomatization of additive categories that makes clear that the abelian group structure of $\operatorname { M o r } ( A , { \mathrm { B } } )$ is intrinsic to the category itself is the following [Lur, pp. 21–22]. A0. C has a zero object. A1. C has products of any two objects, and coproducts of any two objects. By the universal property of product and coproduct, we have natural morphisms $\Phi _ { \mathrm { A B } } : A \coprod \mathrm { B } \ \hat { \longrightarrow } \ \hat { A ^ { * } } \times \hat { \mathrm { B } } . \ A \hat { 2 } . \ \Phi _ { \mathrm { A B } }$ is an isomorphism. This allows us to define a binary operation on $\operatorname { M o r } ( A , { \mathrm { B } } )$ , with $\mathsf { f } + \mathsf { g }$ (for $\mathsf { f } , \mathsf { g } \in M \mathrm { o r } ( \mathsf { A } , \mathsf { B } ) ;$ ) defined by the composition

$$
\begin{array} { r } { \boldsymbol { A } \xrightarrow { ( \boldsymbol { \mathsf { f } } , \boldsymbol { \mathsf { g } } ) } \boldsymbol { \mathsf { B } } \times \boldsymbol { \mathsf { B } } \xrightarrow { \boldsymbol { \Phi } _ { \mathtt { B B } } ^ { - 1 } } \boldsymbol { \mathsf { B } } \coprod \boldsymbol { \mathsf { I } } \boldsymbol { \mathsf { B } } \xrightarrow { \boldsymbol { \mathsf { B } } } \boldsymbol { \mathsf { B } } , } \end{array}
$$

where the last map is the “codiagonal” defined by the universal property of coproduct. A little work shows that this endows $\dot { \bf M o r } ( A , { \tt B } )$ with the structure of a commutative monoid, i.e., an abelian semigroup with identity. The identity is the composition $A \to 0 \to \mathbb { B } . \ A 3$ . This commutative monoid $\mathbf { M o r } ( \mathbf { \bar { A } } , \mathbf { B } )$ is an abelian $g r o u p . )$

1.5.3. The category of A-modules $M o d _ { A }$ is clearly an additive category, but it has even more structure. We now formalize some essential aspects of this structure in the notion of abelian category.

1.5.4. Definition. Let C be a category with a 0-object (and thus 0-morphisms). A kernel of a morphism $\mathsf { f } \colon \mathsf { B }  \mathsf { C }$ is defined to be a map i : $\lambda  \mathtt { B }$ such that ${ \mathsf { f } } \circ { \mathsf { i } } = 0 ,$ and that is universal with respect to this property. Diagramatically:

(1.5.4.1)

<!-- image-->

(Note that the kernel is not just an object; it is a morphism of an object to B. In practice, the term is often applied to just the object, and the intended interpretation is clear from the context.) Hence it is unique up to unique isomorphism by universal property nonsense. The kernel is written ker f  B. A cokernel (denoted coker f) is defined dually by reversing the arrows — do this yourself. The kernel of f : $\mathrm { B } \to \mathrm { C }$ is the limit (§1.3) of the diagram

(1.5.4.2)

<!-- image-->

and similarly the cokernel is a colimit (see (2.6.0.1)).

If i : A  B is a monomorphism, then we say that A is a subobject of B, where the map i is implicit. There is also the notion of quotient object, defined dually to subobject.

An abelian category is an additive category satisfying three additional properties.

(1) Every map has a kernel and cokernel.

(2) Every monomorphism is the kernel of its cokernel.

(3) Every epimorphism is the cokernel of its kernel.

It is a nonobvious (and imprecisely stated) fact that every property you want to be true about kernels, cokernels, etc. follows from these three. (Warning: In part of the literature, additional hypotheses are imposed as part of the definition.)

The image of a morphism f : A  B is defined as im(f) = ker(coker f) whenever it exists (e.g., in every abelian category). The morphism f : A  B factors uniquely through im f  B whenever im f exists, and A  im f is an epimorphism and a cokernel of ker f  A in every abelian category. The reader may want to verify this as a (hard!) exercise.

The cokernel of a monomorphism is called the quotient. The quotient of a monomorphism A  B is often denoted B/A (with the map from B implicit).

→We will leave the foundations of abelian categories untouched. The key thing to remember is that if you understand kernels, cokernels, images and so on in the category of modules over a given ring, you can manipulate objects in any abelian category. This is made precise by the Freyd-Mitchell Embedding Theorem (Remark 1.5.5).

However, the abelian categories we will come across will obviously be related to modules, and our intuition will clearly carry over, so we needn’t invoke a theorem whose proof we haven’t read. For example, we will show that sheaves of abelian groups on a topological space X form an abelian category (§2.6), and the interpretation in terms of “compatible germs” will connect notions of kernels, cokernels etc. of sheaves of abelian groups to the corresponding notions of abelian groups.

1.5.5. Small remark on chasing diagrams. It is useful to prove facts (and solve exercises) about abelian categories by chasing elements. Unfortunately, some commonly used abelian categories, such as the category of complexes (to be defined in Exercise $1 . 5 . C ) $ , do not have “elements” — they are not naturally “sets with additional structure” in any obvious way. Nonetheless, proof by element-chasing can be justified by the Freyd-Mitchell Embedding Theorem: $\operatorname { i f } \mathcal { C }$ is an abelian category whose objects form a set, then there is a ring A and an exact, fully faithful functor from $\mathcal { C }$ into $M o d _ { A }$ , which embeds $\mathcal { C }$ as a full subcategory. (Unfortunately, the ring A need not be commutative.) A proof is sketched in [Weib, §1.6], and references to a complete proof are given there. A proof is also given in [KS2, §9.6]. The upshot is that to prove something about a diagram in some abelian category, we may assume that it is a diagram of modules over some ring, and we may then “diagram-chase” elements. Moreover, any fact about kernels, cokernels, and so on that holds in $M o d _ { A }$ holds in any abelian category.

If invoking a theorem whose proof you haven’t read bothers you, a short alternative is Mac Lane’s “elementary rules for chasing diagrams,” [Mac, Thm. 3, p. 204]; [Mac, Lem. $4 , \mathsf { p }$ . 205] gives a proof of the Five Lemma (Exercise 1.6.6) as an example.

But in any case, do what you need to do to put your mind at ease, so you can move forward. Do as little as your conscience will allow.

## 1.5.6. Complexes, exactness, and homology.

(In this entire discussion, we assume we are working in an abelian category.) We say a sequence

$$
\cdots { \xrightarrow { } } \lambda { \xrightarrow { \quad \ f \ } } \mathrm { B } { \xrightarrow { \quad \ g \ } } \mathrm { C } { \xrightarrow { \quad \ f \ } } \cdots\tag{1.5.6.1}
$$

is a complex at B if ${ \mathfrak { g o f } } = 0 ,$ , and is exact at B if ker ${ \mathfrak { g } } = { \mathrm { i m } } { \mathfrak { f } } $ . (More specifically, g has a kernel that is an image of f. Exactness at B implies being a complex at $\mathrm { B } - \mathrm { d o }$ you see why?) A sequence is a complex (resp., exact) if it is a complex (resp., exact) at each (internal) term. A short exact sequence is an exact sequence with five terms, the first and last of which are zeros — in other words, an exact sequence of the form

$$
0 \longrightarrow \mathsf { A } \longrightarrow \mathsf { B } \longrightarrow \mathsf { C } \longrightarrow 0 .
$$

For example, $0 \longrightarrow \mathsf { A } \longrightarrow 0$ is exact if and only if $A = 0 ;$

$$
0 \longrightarrow \mathsf { A } \longrightarrow \mathsf { B }
$$

is exact if and only if f is a monomorphism (with a similar statement for $\mathsf { A } \longrightarrow \mathsf { B } \longrightarrow 0 \mathsf { \Gamma } )$

$$
0 \xrightarrow [ ] { } \mathrm { \left/ \left( \frac { } { } \right) \right. } \mathrm { \left/ \left( \frac { } { } \right) \right. } \mathrm { \left/ \left( \frac { } { } \right) \right. } \mathrm { \left/ \left( \frac { } { } \right) \right. } \mathrm { \left/ \left( \frac { } { } \right) \right. } \mathrm { \left/ \left( \frac { } { } \right) \right. } \mathrm { \left/ \left( \frac { } { } \right) \right. } \mathrm { \left/ \left( \frac { } { } \right) \right. } \mathrm { \left/ \left( \frac { } { } \right) \right. } \mathrm { \left/ \left( \frac { } { } \right) \right. } \mathrm { \left/ \left( \frac { } { } \right) \right. } \mathrm { \left/ \left( \frac { } { } \right) \right. } \mathrm { \left/ \left( \frac { } { } \right) \right. } \mathrm { \left/ \left( \frac { } { } \right) \right. }
$$

is exact if and only if f is an isomorphism; and

$$
0 \xrightarrow { } \mathrm { A } \frac { \mathrm { ~ \# ~ } } { \mathrm { ~ \# ~ } } > \mathrm { B } \frac { \mathrm { ~ \# ~ } } { \mathrm { ~ \# ~ } } > \mathrm { C }
$$

is exact if and only if f is a kernel of g (with a similar statement for $\mathsf { A } \xrightarrow { \mathrm { ~ \tiny ~ { ~ f ~ } ~ } } \mathsf { B } \xrightarrow { \mathrm { ~ \tiny ~ { ~ g ~ } ~ } } \mathsf { C } \xrightarrow { \mathrm { ~ \tiny ~ { ~ \chi ~ } ~ } } \mathsf { 0 } \mathrm { ~ \tiny ~ { ~ \chi ~ } ~ }$ To show some of these facts it may be helpful to prove that (1.5.6.1) is exact at B if and only if the cokernel of f is a cokernel of the kernel of g.

If you would like practice in playing with these notions before thinking about homology, you can prove the Snake Lemma (stated in Example 1.6.5, with a stronger version in Exercise 1.6.B), or the Five Lemma (stated in Example 1.6.6, with a stronger version in Exercise 1.6.C). (I would do this in the category of A-modules, but see [KS2, Lem. 12.1.1, Lem. 8.3.13] for proofs in general.)

If (1.5.6.1) is a complex at B, then its homology at B (often denoted by H) is ker g / im f. (More precisely, there is some monomorphism im f , ker g, and H is the cokernel of this monomorphism.) Therefore, (1.5.6.1) is exact at B if and only if its homology at B is 0. We say that elements of ker g (assuming the objects of the category are sets with some additional structure) are the cycles, and elements of im f are the boundaries (so homology is “cycles mod boundaries”). If the complex is indexed in decreasing order, the indices are often written as subscripts, and $\mathsf { H } _ { \mathrm { i } }$ is the homology at $\mathrm { A } _ { \mathrm { i } + 1 } \  \ \mathrm { A } _ { \mathrm { i } } \  \ \mathrm { A } _ { \mathrm { i } - 1 }$ . If the complex is indexed in increasing order, the indices are often written as superscripts, and the homology Hi at $\mathsf { A } ^ { \mathsf { i } - \mathsf { \Pi } } \to \mathsf { A } ^ { \mathsf { i } } \to \mathsf { A } ^ { \mathsf { i } + 1 }$ is often called cohomology.

An exact sequence

$$
( 1 . 5 . 6 . 2 ) \qquad \lambda ^ { \bullet } { : }
$$

$$
\cdots { \xrightarrow { } } A ^ { \operatorname { i - 1 } } \ { \xrightarrow { \operatorname { f } ^ { \operatorname { i - 1 } } } } A ^ { \operatorname { i } } \ { \xrightarrow { \operatorname { f } ^ { \operatorname { i } } } } \ A ^ { \operatorname { i + 1 } } \ { \xrightarrow { \operatorname { f } ^ { \operatorname { i + 1 } } } } \cdots A ^ { \operatorname { i } } \quad { \xrightarrow { \operatorname { f } ^ { \operatorname { i + 1 } } } } \cdots A ^ { \operatorname { i } }
$$

can be “factored” into short exact sequences

$$
0 \longrightarrow \mathrm { k e r f } ^ { \mathrm { i } } \longrightarrow \mathrm { A } ^ { \mathrm { i } } \longrightarrow \mathrm { k e r f } ^ { \mathrm { i } + 1 } \longrightarrow 0 ,
$$

which is helpful in proving facts about long exact sequences by reducing them to facts about short exact sequences.

More generally, if (1.5.6.2) is assumed only to be a complex, then it can be “factored” into short exact sequences.

$$
0 \longrightarrow \mathrm { k e r f } ^ { \mathrm { i } } \longrightarrow \mathrm { A } ^ { \mathrm { i } } \longrightarrow \mathrm { i m } \mathrm { f } ^ { \mathrm { i } } \longrightarrow 0 ,\tag{1.5.6.3}
$$

$$
0 \longrightarrow \mathrm { i m } \mathrm { f } ^ { \mathrm { i } - 1 } \longrightarrow \mathrm { k e r f } ^ { \mathrm { i } } \longrightarrow \mathsf { H } ^ { \mathrm { i } } ( \pmb { A } ^ { \bullet } ) \longrightarrow 0
$$

1.5.A. EXERCISE. Describe exact sequences

$$
0 \longrightarrow \mathrm { i m ~ f ^ { i } ~ { \longrightarrow } ~ } \lambda ^ { \left\downarrow + 1 \right. } \xrightarrow { } \mathrm { c o k e r ~ f ^ { i } ~ { \longrightarrow } ~ } 0 ,\tag{1.5.6.4}
$$

$$
0 \longrightarrow { \sf H } ^ { \mathrm { i } } ( A ^ { \bullet } ) \longrightarrow \mathrm { c o k e r f } ^ { \mathrm { i } - 1 } \longrightarrow \mathrm { i m } \mathrm { f } ^ { \mathrm { i } } \longrightarrow 0 \mathrm { i } \mathrm { d } \mathrm { f } ^ { \mathrm { i } } .
$$

(These are somehow dual to (1.5.6.3). In fact, in some mirror universe this might have been given as the standard definition of homology.) Assume the category is that of modules over a fixed ring for convenience, but be aware that the result is true for any abelian category.

1.5.B. EXERCISE AND IMPORTANT DEFINITION. Suppose

$$
0 \xrightarrow [ ] { \mathrm { { \scriptsize ~ d ^ { 0 } ~ } } } \mathrm { \sim } \mathrm { \AA } ^ { 1 } \xrightarrow [ ] { \mathrm { { \scriptsize ~ d ^ { 1 } ~ } } } \mathrm { \sim \cdots } \xrightarrow [ ] { \mathrm { { \scriptsize ~ d ^ { n - 1 } ~ } } } \mathrm { \times } \mathrm { \AA } ^ { \mathrm { n } } \xrightarrow [ ] { \mathrm { { \scriptsize ~ d ^ { n } ~ } } } \mathrm { \sim 0 }
$$

is a complex of finite-dimensional k-vector spaces (often called $A ^ { \bullet }$ for short). Define $\mathrm { { h } } ^ { \mathrm { i } } ( A ^ { \bullet } ) \dot { : = } \mathrm { { d i m } \mathrm { { H } } ^ { \mathrm { i } } ( A ^ { \bullet } ) }$ . Show that $\sum ( - 1 ) ^ { \mathrm { i } }$ dim $\begin{array} { r } { \mathsf { A } ^ { \mathrm { i } } = \sum ( - 1 ) ^ { \mathrm { i } } \mathsf { h } ^ { \mathrm { i } } ( \mathsf { A } ^ { \bullet } ) } \end{array}$ . In particular, if $\mathsf { A } ^ { \bullet }$ is exact, then $\sum ( - 1 ) ^ { \mathfrak { i } }$ dim $\lambda ^ { \mathrm { i } } = 0$ . (If you haven’t dealt much with cohomology, this will give you some practice.)

1.5.C. IMPORTANT EXERCISE. Suppose $\mathcal { C }$ is an abelian category. Define the category $C o m _ { \mathscr { C } }$ of complexes) as follows. The objects are infinite complexes

$$
A ^ { \bullet } \colon
$$

$$
\cdots { \xrightarrow { } } A ^ { \operatorname { i - 1 } } \ { \xrightarrow { \operatorname { f } ^ { \operatorname { i - 1 } } } } A ^ { \operatorname { i } } \ { \xrightarrow { \operatorname { f } ^ { \operatorname { i } } } } \ A ^ { \operatorname { i + 1 } } \ { \xrightarrow { \operatorname { f } ^ { \operatorname { i + 1 } } } } \cdots A ^ { \operatorname { i } } \quad { \xrightarrow { \operatorname { f } ^ { \operatorname { i } } } } \cdots A ^ { \operatorname { i } }
$$

in $\mathcal { C } ,$ and the morphisms $A ^ { \bullet }  \mathtt { B } ^ { \bullet }$ are commuting diagrams

$$
\begin{array} { r l } & { \cdots \xrightarrow { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \mathrm { \ l } ^ { \mathrm { i - 1 } } \xrightarrow { \mathrm { f } ^ { \mathrm { i - 1 } } } { \mathrm { A } } ^ { \mathrm { i } } \xrightarrow { \quad \mathrm { f } ^ { \mathrm { i } } \quad \quad \mathrm { f } ^ { \mathrm { i } } \quad \quad \mathrm { f } ^ { \mathrm { i + 1 } } } { \mathrm { A } } ^ { \mathrm { i + 1 } } \xrightarrow { \mathrm { f } ^ { \mathrm { i + 1 } } } \cdots } \\ & { \qquad \quad \quad \quad \quad \quad \quad \downarrow } \\ & { \cdots \xrightarrow { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \mathrm { B } ^ { \mathrm { i } } \xrightarrow { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \mathrm { b } ^ { \mathrm { i } } } \\ & { \cdots \xrightarrow { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } } \end{array}\tag{1.5.6.5}
$$

Show that ComC is an abelian category.

Feel free to deal with the special case of modules over a fixed ring. (Remark for experts: Essentially the same argument shows that $\mathcal { C } ^ { \mathcal { I } }$ is an abelian category for any small category $\mathcal { I }$ and any abelian category $\mathcal { C } .$ . This immediately implies that the category of presheaves on a topological space X with values in an abelian category $\mathcal { C }$ is automatically an abelian category; cf. §2.3.5.)

1.5.D. IMPORTANT EXERCISE. Show that (1.5.6.5) induces a map of homology $\mathsf { H } ^ { \mathrm { i } } ( \mathsf { A } ^ { \bullet } ) \longrightarrow \mathsf { H } ^ { \mathrm { i } } ( \mathsf { B } ^ { \bullet } )$ . Show furthermore that Hi is a covariant functor $C o m _ { \mathscr { C } }  \mathscr { C }$ (Again, feel free to deal with the special case $M o d _ { A } . )$ )

1.5.7. Homotopic maps induce the same maps on homology. We say two maps of complexes $\mathsf { f } \colon \mathrm { \dot { C } ^ { \bullet }  \dot { D } ^ { \bullet } }$ and ${ \mathfrak { g } } \colon { \mathsf { C } } ^ { \bullet }  { \mathsf { D } } ^ { \bullet }$ are homotopic if there is a sequence of maps w: $\mathrm { C } ^ { \mathrm { i } } \to \mathsf { D } ^ { \mathrm { i } - 1 }$ such that $\mathbf { f } - \mathbf { g } = \mathrm { d } w + w \mathrm { d }$

1.5.E. EXERCISE. Show that two homotopic maps give the same map on homology.

1.5.8. Theorem (long exact sequences). — A short exact sequence of complexes

<!-- image-->

induces a long exact sequence in cohomology

$$
\cdots { \longrightarrow } { \mathrm { H } } ^ { \mathrm { i } - 1 } ( { \bf C } ^ { \bullet } ) \longrightarrow
$$

$$
{ \mathsf { H } } ^ { \mathsf { i } } ( A ^ { \bullet } ) \longrightarrow { \mathsf { H } } ^ { \mathsf { i } } ( { \mathsf { B } } ^ { \bullet } ) \longrightarrow { \mathsf { H } } ^ { \mathsf { i } } ( C ^ { \bullet } ) \longrightarrow
$$

$$
{ \cal H } ^ { \mathrm { i } + 1 } ( { \cal A } ^ { \bullet } ) \longrightarrow \cdots
$$

(This requires a definition of the connecting homomorphism ${ \mathsf { H } } ^ { \mathrm { i } - 1 } ( { \mathsf { C } } ^ { \bullet } ) $ ${ \mathsf { H } } ^ { \mathbf { i } } ( A ^ { \bullet } ) .$ , which is “natural” in an appropriate sense.) In the category of modules over a ring, Theorem 1.5.8 will come out of our discussion of spectral sequences — see Exercise 1.6.F — but this is a somewhat perverse way of proving it. For a proof in general, see [KS2, Theorem 12.3.3]. You may want to prove it yourself, by first proving a weaker version of the Snake Lemma (Example 1.6.5), where in the hypotheses (1.6.5.1), the 0’s in the bottom left and top right are removed, and in the conclusion (1.6.5.2), the first and last 0’s are removed.

1.5.9. Exactness of functors. If F : $\mathcal { A }  \mathcal { B }$ is an additive covariant functor from one abelian category to another, we say that F is right-exact if the exactness of

$$
\left. \begin{array} { l l l } { { A ^ { \prime } \longrightarrow A \longrightarrow A ^ { \prime \prime } \longrightarrow 0 } } \end{array} \right. \longrightarrow 0
$$

in A implies that

$$
\mathsf { F } ( \mathsf { A } ^ { \prime } ) \longrightarrow \mathsf { F } ( \mathsf { A } ) \longrightarrow \mathsf { F } ( \mathsf { A } ^ { \prime \prime } ) \longrightarrow 0
$$

is also exact. Dually, we say that F is left-exact if the exactness of

$$
0 \longrightarrow A ^ { \prime } \longrightarrow A \longrightarrow A ^ { \prime \prime }
$$

implies

$$
0 \longrightarrow \mathsf { F } ( \mathsf { A } ^ { \prime } ) \longrightarrow \mathsf { F } ( \mathsf { A } ) \longrightarrow \mathsf { F } ( \mathsf { A } ^ { \prime \prime } )
$$

is exact.

An additive contravariant functor is left-exact if the exactness of

$$
 A ^ { \prime } \xrightarrow { } A \xrightarrow { } B ^ { \prime \prime } ]  A ^ { \prime \prime } \xrightarrow { } 0
$$

implies

$$
0 \longrightarrow \mathsf { F } ( \mathsf { A } ^ { \prime \prime } ) \longrightarrow \mathsf { F } ( \mathsf { A } ) \longrightarrow \mathsf { F } ( \mathsf { A } ^ { \prime } )
$$

is exact.

The reader should be able to deduce what it means for a contravariant functor to be right-exact.

An additive covariant or contravariant functor is exact if it is both left-exact and right-exact.

1.5.F. EXERCISE. Suppose F is an exact functor. Show that applying F to an exact sequence preserves exactness. For example, if F is covariant, and $A ^ { \prime }  A  A ^ { \prime \prime }$ is exact, then $\mathsf { F } \mathsf { A } ^ { \prime } \to \mathsf { F } \mathsf { A } \to \mathsf { F } \mathsf { A } ^ { \prime \prime }$ is exact. (This will be generalized in Exercise 1.5.I(c).)

1.5.G. EXERCISE. Suppose A is a ring, ${ \mathsf { S } } \subset A$ is a multiplicative subset, and M is an A-module.

(a) Show that localization of A-modules $M o d _ { \cal A }  M o d _ { \cal S ^ { - 1 } \cal A }$ is an exact covariant functor.

(b) Show that $( \cdot ) \otimes _ { A }$ M is a right-exact covariant functor Mod $_ { \cdot A }  M o d _ { A }$ . (This is a repeat of Exercise 1.2.H.)

(c) Show that Hom(M, ·) is a left-exact covariant functor $M o d _ { \mathrm { A } }  M o d _ { \mathrm { A } }$ . If $\mathcal { C }$ is any abelian category, and ${ \mathrm { ~ C ~ } } \in { \mathcal { C } }$ , show that Hom(C, ·) is a left-exact covariant functor $\mathcal { C }  A b$

(d) Show that Hom(·, M) is a left-exact contravariant functor $M o d _ { \mathrm { A } }  M o d _ { \mathrm { A } }$ . If C is any abelian category, and ${ \mathrm { C } } \in { \mathcal { C } } .$ , show that Hom $( \cdot , C )$ is a left-exact contravariant functor $\mathcal { C }  A b$

1.5.H. EXERCISE. Suppose M is a finitely presented A-module: M has a finite number of generators, and with these generators it has a finite number of relations; or, equivalently, and usefully, fits in an exact sequence

$$
\begin{array} { c c c c } { { \pmb { \mathcal { A } } ^ { \oplus } { \bf q } } } & { { \longrightarrow } } & { { \pmb { \mathcal { A } } ^ { \oplus } { \bf p } } } & { { \longrightarrow } { \bf M } } & { { \longrightarrow } 0 . } \end{array}\tag{1.5.9.1}
$$

Use (1.5.9.1) and the left-exactness of Hom to describe an isomorphism

$$
S ^ { - 1 } \operatorname { H o m } _ { A } ( M , \mathsf { N } ) \xrightarrow { \sim } \operatorname { H o m } _ { S ^ { - 1 } A } ( S ^ { - 1 } M , S ^ { - 1 } \mathsf { N } ) .
$$

(You might be able to interpret this in light of a variant of Exercise 1.5.I below, for left-exact contravariant functors rather than right-exact covariant functors.)

1.5.10. Example: Hom doesn’t always commute with localization. In the language of Exercise 1.5.H, take $\mathsf { A } = \mathsf { N } = \mathbb { Z } , \mathsf { M } = \mathbb { Q }$ , and $S = \mathbb { Z } \setminus \{ 0 \}$

## 1.5.11. ⋆ Two useful facts in homological algebra.

We now come to two (sets of) facts I wish I had learned as a child, as they would have saved me lots of grief. They encapsulate what is best and worst of abstract nonsense. The statements are so general as to be nonintuitive. The proofs are very short. They generalize some specific behavior that is easy to prove on an ad hoc basis. Once they are second nature to you, many subtle facts will become obvious to you as special cases. And you will see that they will get used (implicitly or explicitly) repeatedly.

## 1.5.12. ⋆ Interaction of homology and (right/left-)exact functors.

You might wait to prove this until you learn about cohomology in Chapter 18, when it will first be used in a serious way.

1.5.I. IMPORTANT EXERCISE (THE FHHF THEOREM). This result can take you far, and perhaps for that reason it has sometimes been called the Fernbahnhof (FernbaHnHoF) Theorem, notably in [Vak1, Exer. 1.5.I]. Suppose F: ${ \mathcal { A } }  { \mathcal { B } }$ is a covariant functor of abelian categories, and $\subset ^ { \bullet }$ is a complex in $\mathcal { A }$

(a) (F right-exact yields $\mathsf { F H } ^ { \bullet } \longrightarrow \mathsf { H } ^ { \bullet } \mathsf { F } \ )$ If F is right-exact, describe a natural morphism $\mathsf { F H } ^ { \bullet }  \mathsf { H } ^ { \bullet } \mathsf { F }$ . (More precisely, for each i, the left side is F applied to the cohomology at piece i of $C ^ { \bullet }$ , while the right side is the cohomology at piece i of FC•.)

(b) (F left-exact yields $\mathbf { \bar { \rho } } \mathbf { H ^ { \bullet } } \mathbf { < } \mathbf { \bar { \rho } } \mathbf { H ^ { \bullet } F } \mathbf { \Phi } )$ If F is left-exact, describe a natural morphism $\mathsf { H } ^ { \bullet } \mathsf { F }  \mathsf { F } \mathsf { H } ^ { \bullet }$

(c) (F exact yields $\mathsf { F H } ^ { \bullet } \xrightarrow { \sim } \mathsf { H } ^ { \bullet } \mathsf { F } )$ If F is exact, show that the morphisms of (a) and (b) are inverses and thus isomorphisms.

Hint for (a): Use $\mathrm { C ^ { i } } \xrightarrow { \mathrm { ~ \ d ^ { i } ~ } } \mathrm { C ^ { i + 1 } } \xrightarrow { } \mathrm { c o k e r d ^ { i } } \xrightarrow { } 0$ to give an isomorphism F coker $\mathrm { d } ^ { \mathrm { i } } \longleftrightarrow$ coker $\mathsf { F d } ^ { \mathrm { i } }$ . Then use the first line of (1.5.6.4) to give an epimorphism ←→F im di ↠ im Fdi. Then use the second line of (1.5.6.4) to give the desired map $\mathsf { F H } ^ { \mathrm { i } } \mathsf { C } ^ { \bullet } \to \mathsf { H } ^ { \mathrm { i } } \mathsf { F C } ^ { \bullet }$ . While you are at it, you may as well describe a map for the fourth member of the quartet {coker, im, H, ker}: F ker $\mathrm { d } ^ { \mathrm { i } }  \mathrm { k e r } \mathsf { F } \mathrm { d } ^ { \mathrm { i } }$

1.5.13. If this makes your head spin, you may prefer to think of it in the following specific case, where both $\mathcal { A }$ and $\bar { \mathcal { B } }$ are the category of A-modules, and F is $( \cdot ) \otimes _ { A }$ N for some fixed A-module N. Your argument in this case will translate without change to yield a solution to Exercise 1.5.I(a) and (c) in general. If $\otimes \mathsf { N }$ is exact, then N is called a flat A-module. (The notion of flatness will turn out to be very important, and is discussed in detail in Chapter 24.)

For example, localization is exact (Exercise $1 . 5 . { \cal G } ( \mathsf { a } ) )$ , so $S ^ { - 1 } A$ is a flat A-algebra for all multiplicative sets S. Thus taking cohomology of a complex of A-modules commutes with localization — something you could verify directly.

1.5.14. Interaction of adjoints, (co)limits, and (left- and right-) exactness.

A surprising number of arguments boil down to the following statement:

Limits commute with limits and right adjoints. In particular, in an abelian category, because kernels are limits, both limits and right adjoints are left-exact.

And to its dual:

Colimits commute with colimits and left adjoints. In particular, because cokernels are colimits, both colimits and left adjoints are right-exact.

These statements were promised in §1.4.4, and will be proved below. The latter has a useful extension:

In ModA, colimits over filtered index categories are exact. “Filtered” was defined in §1.3.8.

1.5.15. ⋆⋆ Caution. It is not true that in abelian categories in general, colimits over filtered index categories are exact. (Grothendieck realized the desirability of such colimits being exact, and formalized this as his $" \mathrm { A B } 5 ^ { \prime \prime }$ axiom; see, for example, [Stacks, tag $0 7 9 \mathrm { A l } . )$ Here is a counterexample. Because the axioms of abelian categories are self-dual, it suffices to give an example in which a cofiltered limit fails to be exact (where cofiltered has the obvious dual definition to filtered), and we do this. Fix a prime p. In the category Ab of abelian groups, for each positive integer n, we have an exact sequence $\mathbb { Z } \to \mathbb { Z } / ( { \mathfrak { p } } ^ { \mathfrak { n } } ) \to 0 .$ . Taking the limit over all n in the obvious way, we obtain $\mathbb { Z } \to \mathbb { Z } _ { \mathfrak { p } } \to 0 ,$ , which is certainly not exact.)

Unimportant Remark 1.5.18 will dash another hope you may have.

1.5.16. If you want to use these statements (for example, later in this book), you will have to prove them. Let’s now make them precise.

1.5.J. EXERCISE (KERNELS COMMUTE WITH LIMITS). Suppose $\mathcal { C }$ is an abelian category, and a: $\mathcal { I }  \mathcal { C }$ and b: $\mathcal { I }  \mathcal { C }$ are two diagrams in $\mathcal { C }$ indexed by $\mathcal { I }$ For convenience, let $\lambda _ { \mathrm { i } } = \mathbf { a } ( \mathrm { i } )$ and $\mathtt { B } _ { \mathrm { i } } = \mathtt { b } ( \mathrm { i } )$ be the objects in those two diagrams. Let $\mathtt { h } _ { \mathrm { i } } \colon \lambda _ { \mathrm { i } } \to \mathtt { B } _ { \mathrm { i } }$ be maps commuting with the maps in the diagrams. (Translation: h is a natural transformation of functors $\mathrm { ~ a ~ }  \hat { \mathrm { ~ b } } ;$ see §1.1.21.) Then the ker $\mathsf { h } _ { \mathrm { i } }$ form another diagram in $\mathcal { C }$ indexed by ${ \mathcal { I } } .$ . Describe a canonical isomorphism lim ker $\mathrm { { h } _ { i } } \stackrel { \sim } { \longleftrightarrow } \mathrm { { k e r } ( l i m { A } _ { i }  l i m { B } _ { i } ) }$ , assuming the limits exist.

Implicit in the previous exercise is the idea that limits should somehow be understood as functors.

1.5.K. EXERCISE. Make sense of the statement that “limits commute with limits” in a general category, and prove it. (Hint: Recall that kernels are limits. The previous exercise should be a corollary of this one.)

1.5.17. Proposition (right adjoints commute with limits). — Suppose $( \mathsf { F } \colon { \mathcal { C } } \to$ $\mathcal { D } , { \sf G } \colon \mathcal { D }  \mathcal { C } )$ is a pair of adjoint functors. $I f A = \operatorname* { l i m } A _ { \mathrm { i } }$ is a limit in $\mathcal { D }$ of a diagram indexed by $\mathcal { I } _ { \mathbf { \Phi } }$ , then $\mathsf { G } \mathsf { A } = \operatorname* { l i m } \mathsf { G } \mathsf { A } _ { \mathrm { i } }$ (with the corresponding maps $\mathsf { G } \mathsf { A } \to \mathsf { G } \mathsf { A } _ { \mathrm { i } } )$ is a limit in $\mathcal { C }$

Proof. We must show that $\mathsf { G A } \to \mathsf { G A } _ { \mathrm { i } }$ satisfies the universal property of limits. Suppose we have maps $W \to { \mathsf { G } } \lambda _ { \mathrm { i } }$ commuting with the maps of $\bar { \mathcal { S } }$ . We wish to show that there exists a unique $W \to \mathsf { G } A$ extending the $W \to \mathsf { G } A _ { \mathrm { i } }$ . By adjointness of F and $\mathsf { G } ,$ we can restate this as: Suppose we have maps $\mathsf { F W } \to \lambda _ { \mathrm { i } }$ commuting with the maps of $\mathcal { I }$ . We wish to show that there exists a unique $\mathsf { F W } \to \bar { A }$ extending the $\mathsf { F W } \to \bar { \mathsf { A } } _ { \mathrm { i } }$ . But this is precisely the universal property of the limit. □

Of course, the dual statements to Exercise 1.5.K and Proposition 1.5.17 hold by the dual arguments.

If F and G are additive functors between abelian categories, and $( \mathsf { F } , \mathsf { G } )$ is an adjoint pair, then (as kernels are limits and cokernels are colimits) G is left-exact and F is right-exact.

1.5.L. EXERCISE. Show that in $M o d _ { A }$ , colimits over filtered index categories are exact. (Your argument will apply without change to any abelian category whose objects can be interpreted as “sets with additional structure.”) Right-exactness follows from the above discussion, so the issue is left-exactness. (Possible hint: After you show that localization is exact, Exercise $1 . 5 . \mathrm { G } ( \mathsf { a } )$ , or stalkification is exact, Exercise 2.6.E, in a hands-on way, you will be easily able to prove this. Conversely, if you do this exercise, those two will be easy.)

1.5.M. EXERCISE. Show that filtered colimits commute with homology in $M o d _ { A }$ Hint: Use the FHHF Theorem (Exercise 1.5.I), and the previous exercise.

In light of Exercise 1.5.M, you may want to think about how limits (and colimits) commute with homology in general, and which way maps go. The statement of the FHHF Theorem should suggest the answer. (Are limits analogous to left-exact functors, or right-exact functors?) We won’t directly use this insight, but see §18.1 (vii) for an example.

Just as colimits are exact (not just right-exact) in especially good circumstances, limits are exact (not just left-exact), too. The following will be used twice in Chapter 28.

1.5.N. EXERCISE. Suppose

<!-- image-->

is an inverse system of exact sequences of modules over a ring, such that the maps $A _ { \mathfrak { n } + 1 } \  \ A _ { \mathfrak { n } }$ are surjective. (We say: “transition maps of the left term are surjective.”) Show that the limit

$$
0 \xrightarrow [ ] { } \sin A _ { \mathrm { n } } \xrightarrow [ ] { } \sin B _ { \mathrm { n } } \xrightarrow [ ] { } \sin C _ { \mathrm { n } } \xrightarrow [ ] { } 0\tag{1.5.17.1}
$$

is also exact. (You will need to define the maps in (1.5.17.1).)

1.5.18. Unimportant remark. Based on these ideas, you may suspect that right-exact functors always commute with colimits. The fact that the tensor product commutes with infinite direct sums (Exercise 1.2.M) may reinforce this idea. Unfortunately, it is not true — “double dua $\begin{array} { r } { \cdots \lor \lor : V e c _ { \mathrm { k } }  \mathbf { \dot { V } } e c _ { \mathrm { k } } } \end{array}$ is covariant and right exact (in fact, exact), but does not commute with infinite direct sums, as $\Phi _ { \mathrm { i } = 1 } ^ { \infty } ( \bf k ^ { \vee \vee } )$ is not isomorphic to $( \mathbb { \oplus } _ { \mathrm { i = 1 } } ^ { \infty } \mathbb { k } ) ^ { \vee \vee }$

1.5.19. ⋆ Dreaming of derived functors. When you see a left-exact functor, you should always dream that you are seeing the end of a long exact sequence. If

$$
0 \longrightarrow { \sf M ^ { \prime } } \longrightarrow { \sf M } \longrightarrow { \sf M ^ { \prime \prime } } \longrightarrow { \sf 0 }
$$

is an exact sequence in abelian category ${ \mathcal { A } } ,$ and F : $\mathcal { A }  \mathcal { B }$ is a left-exact functor, then

$$
0 \longrightarrow \mathsf { F M ^ { \prime } } \longrightarrow \mathsf { F M } \longrightarrow \mathsf { F M ^ { \prime \prime } }
$$

is exact, and you should always dream that it continues in some natural way. For example, the next term should depend only on $M ^ { \prime } -$ call it $\mathsf { R } ^ { 1 } \mathsf { F } M ^ { \prime } -$ and if it is zero, then $\mathsf { F } M \to \mathsf { F } M ^ { \prime \prime }$ is an epimorphism. This remark holds true for left-exact and contravariant functors too. In good cases, such a continuation exists, and is incredibly useful. We will discuss this in Chapter 23.

## 1.6 ⋆ Spectral sequences