# MATH 8210, FALL 2011 LECTURE NOTES

## 1. Multivariable calculus without coordinates

The objects of study in this course are what are called “smooth manifolds.” For the time being I won’t give a precise definition of these (it will come later, or of course you can easily look it up), but for now suffice it to say that these are topological spaces which locally resemble Euclidean space and in which, in particular, it is possible to do something resembling calculus. The surface of the Earth is (to good approximation) an example of a two-dimensional smooth manifold. Of course, the Earth is not $\mathbb { R } ^ { 2 }$ but rather a closed surface (I was going to say a sphere, but then it occurred to me that if one looks closely enough there are some rock formations which cause the genus to be positive), yet locally it looks enough like $\mathbb { R } ^ { 2 }$ that it seems reasonable to speak for instance of the directional derivatives of a function (the temperature, say) defined on the Earth.

So how can we formulate calculus in such spaces? Part of the definition will be that a manifold M will have an open cover $\{ U _ { \alpha } | \alpha \in A \}$ by sets equipped with homeomorphisms (“charts”) $\phi _ { \alpha } \colon U _ { \alpha } \to V _ { \alpha }$ where $V _ { \alpha } \subset \mathbb { R } ^ { n }$ is open. So we can try to do calculus on M by, roughly speaking, doing standard multivariable calculus in the open sets $V _ { \alpha }$ and then transporting the constructions back to M by the maps $\phi _ { \alpha }$ (or their inverses). However, if $n \in M ,$ then m will typically belong to several of the sets $U _ { \alpha }$ in the open cover of M, and one needs to make sure that one’s constructions don’t depend on which of the charts one is using. To compare between the αth chart and the βth chart, one needs to look at the “transition function”

$$
\phi _ { \beta } \circ \phi _ { \alpha } ^ { - 1 } \colon \phi _ { \alpha } ( U _ { \alpha } \cap U _ { \beta } ) \to \phi _ { \beta } ( U _ { \alpha } \cap U _ { \beta } ) .
$$

This is a map between two open subsets of $\mathbb { R } ^ { n }$ , and part of the definition of a smooth manifold will ensure that the map is smooth $( i . e . , C ^ { \infty } )$ and invertible (with a smooth inverse), but there won’t be any restrictions on what $\phi _ { \beta } \circ \phi _ { \alpha } ^ { - 1 }$ other than that. So for example it doesn’t make sense to “take the partial derivative of a function on M with respect to the first coordinate,” since although we can differentiate a function on $V _ { \alpha }$ with respect to the first coordinate, or we can do the same for a function on $V _ { \beta }$ , these operations won’t be equivalent when we try to lift them up to M using the maps $\phi _ { \alpha } , \phi _ { \beta }$

So this makes it important to understand how notions of multivariable calculus behave under the action of diffeomorphisms $( i . e .$ , smooth maps with smooth inverses) φ : $U  { \tilde { U } }$ where U and $\tilde { U }$ are open subsets of Rn. You should think of the action of such a diffeomorphism as being the same as changing one’s coordinate system, e.g. from Cartesian coordinates to polar coordinates. In particular I want to first discuss various notions of what a tangent vector at a point $p \in U$ is. (And we’ll later generalize this to the notion of a tangent vector at a point in a smooth manifold.) Visually you’re supposed to think of a tangent vector at $p$ as being a little arrow whose base is at $p ,$ pointing in a possible direction of motion from $p .$ . The set of these tangent vectors will form a vector space called the tangent space to U at $p$ and denoted $T _ { p } U$ . I’ll give three characterizations, from most concrete to most abstract.

(1) The way to describe this notion that is used in undergraduate multivariable calculus courses is just to say that a tangent vector v at $p \in U$ is (or is represented by) an n-tuple of numbers $( \nu _ { 1 } , \ldots , \nu _ { n } ) \in \mathbb { R } ^ { n }$ . One can then draw the vector whose base is at $p$ and whose first coordinate is $\nu _ { 1 }$ , second coordinate is $\nu _ { 2 }$ , and so on. (In somewhat more sophisticated language, the standard Cartesian coordinates on $\mathbb { R } ^ { n }$ determine a basis $\{ e _ { 1 } , \ldots , e _ { n } \}$ of unit vectors, and one has $\begin{array} { r } { \nu = \sum \nu _ { i } e _ { i } . ) } \end{array}$

## MIKE USHER

This characterization is very good for computational purposes, but when one is interested in how tangent vectors behave under coordinate changes φ : $U  { \tilde { U } }$ it has some disadvantages. The tangent vector $\nu = ( \nu _ { 1 } , \ldots , \nu _ { n } ) \in T _ { p } U$ should correspond under the coordinate change φ to a tangent vector $\phi _ { * } \nu \ \in \ T _ { \phi ( p ) } \tilde { U }$ at $\phi ( p )$ . Perhaps you’ve learned how this correspondence works: one constructs the Jacobian matrix at p of the map $\phi$ (with (i, j) entry given by $\frac { \partial \phi _ { i } } { \partial x _ { j } }$ where $\phi _ { i }$ is the ith component of $\phi ) _ { - }$ and then the coordinates of φ∗v are obtained by multiplying the Jacobian matrix by the vector consisting of the components of v. This is a manageable computation, but it may not be very conceptually clear from this discussion what’s going on here. In particular if we then want to say what a tangent vector to a point m on a smooth manifold is we’d have to say something like “an n-tuple of numbers for each chart containing $m ,$ such that the n-tuples for different charts are related by the Jacobians of the transition functions,” which is much more opaque and less natural-sounding than it really should be.

(2) A more natural characterization of tangent vectors is the following. The idea is that the tangent space $T _ { p } U$ consists of all possible velocities of curves passing through $p . \mathrm { ~ H ~ } p \in U$ , consider all $C ^ { \infty }$ paths $\gamma \colon ( - \epsilon , \epsilon )  U$ (for some $\epsilon > 0 )$ such that $\gamma ( 0 ) = p .$ I would like to declare two of these to be equivalent if they have the same velocity, i.e., $\gamma _ { 1 } ~ \sim ~ \gamma _ { 2 }$ iff $\gamma _ { 1 } ^ { \prime } ( 0 ) = \gamma _ { 2 } ^ { \prime } ( 0 )$ (or equivalently, and maybe less circularly, $\gamma _ { 1 } ~ \sim ~ \gamma _ { 2 }$ if $\begin{array} { r } { \operatorname* { l i m } _ { t \to 0 } \frac { \gamma _ { 1 } ( t ) - \gamma _ { 2 } ( t ) } { t } = 0 ) } \end{array}$ Then simply define a “tangent vector” at $p$ to be an equivalence class $[ \gamma ]$ of $C ^ { \infty }$ arcs through $p$ (and so $T _ { p } U$ is just the set of equivalence classes). The way this behaves under coordinate changes is extremely simple, since I’m not using coordinates to define the notion: a tangent vector $\nu \in T _ { p } U$ has the form $\nu = [ \gamma ]$ for some $\gamma ,$ and the corresponding tangent vector $\phi _ { * } \nu \in T _ { \phi ( p ) } \tilde { U }$ is just $[ \phi \circ \gamma ]$ . We’ll see later that this adapts to general smooth manifolds very simply and directly—a tangent vector at a point on a smooth manifold will just be a suitable equivalence class of curves passing through that point.

The one disadvantage of this characterization is that it’s not so intuitively obvious how to do algebraic operations (like addition of tangent vectors) on equivalence classes of curves through a point (though you can make a suitable definition if you put your mind to it).

It shouldn’t be hard to construct a natural correspondence between tangent vectors in this sense and tangent vectors in the sense of Definition (1) above, but again, the advantage of thinking about it this way is that it’s less coordinate-dependent.

(3) Now for a characterization of tangent vectors that you almost certainly would not have thought of. To attempt to motivate it, note that a given tangent vector $\nu \in T _ { p } U$ gives you the ability to differentiate smooth functions $f \colon U \to \mathbb { R }$ at $p \mathrm { - }$ —namely you take the directional derivative at $p \mathrm { : }$

$$
( D _ { \nu } f ) ( p ) = \operatorname * { l i m } _ { t \to 0 } { \frac { f ( p + t \nu ) - f ( p ) } { t } } .
$$

So we will define a tangent vector at $p$ to be $\mathbf { \ddot { a } }$ way of differentiating functions defined near $p , \ ' \ i . e .$ , we will abstract some relevant properties of the operation of taking a directional derivative, and then define a tangent vector to be one of these operations.

To do this, first consider pairs $( f , V )$ where V is an open neighborhood of $p$ and $f \colon V  \mathbb { R }$ is $C ^ { \infty }$ , and declare two such pairs $( f , V )$ and $( g , W )$ to be equivalent if there is a smaller neighborhood $Z \subset V \cap W$ of $p$ such that $f | _ { Z } = g | _ { Z }$ . Let $O _ { p }$ be the set of equivalence classes. Since we can set, for instance $[ f , V ] \cdot [ g , W ] = [ f g , V \cap W ] , O _ { p }$ is easily seen to be a commutative R-algebra $( i . e .$ , it is both a commutative ring and a vector space over R, with appropriately compatible operations), called the “algebra of germs of functions at $p . \ '$ I’ll tend to denote a germ by just $f$ rather than $[ f , V ] ;$ it is to be understood that $f$ is defined not necessarily throughout U but rather on some (varying) open neighborhood of $p .$ Of course one always has a well-defined value $f ( p )$ for $f \in O _ { p }$

A tangent vector at p will then be defined to be a derivation v: $O _ { p } \to \mathbb { R } ,$ i.e. v is to satisfy

• (R-linearity) $\nu ( c f + g ) = c \nu ( f ) + \nu ( g )$ for $c \in \mathbb { R }$ and $f , g \in O _ { p }$

• (Leibniz rule) $\nu ( f g ) = f ( p ) \nu ( g ) + g ( p ) \nu ( f )$ for $f , g \in O _ { p }$

It’s standard that the directional derivative operations $D _ { \nu }$ alluded to above satisfy these properties. It’s not obvious that, conversely, any derivation on $O _ { p }$ is given by a directional derivative in some direction, but we’ll prove this shortly.

Like the characterization of tangent vectors as equivalence classes curves, this formulation is completely coordinate free, making it easy to extend the definition to manifolds when the time comes. Unlike the situation with curve characterization, though, it’s quite obvious that derivations form a vector space, which is another advantage.

To see how this notion behaves under diffeomorphisms (or indeed under more general smooth maps) $\phi \colon { \cal U }  \tilde { { \cal U } } , \mathrm { i f } \nu \in T _ { p } { \cal U } ( i . e .$ ., if v is a derivation on $O _ { p } ) .$ , we need to construct a derivation $\phi _ { * } \nu$ on $O _ { \phi ( p ) }$ Well, if $f \in O _ { \phi ( p ) }$ (really we should write $[ f , V ] ) , \operatorname { s o } f$ is a smooth function defined near $\phi ( p )$ , then $f \circ \phi$ will be a smooth function defined near p (specifically, it will be defined on the open set $\phi ^ { - 1 } ( V )$ around $p )$ , and so we can define

$$
( \phi _ { * } \nu ) ( f ) = \nu ( f \circ \phi )
$$

So as with the curve formulation, it’s quite simple to see how derivations transform under coordinate changes.

Among the three above characterizations of tangent vectors, it should be clear that (1) is equivalent to $( 2 ) .$ under the correspondence which assigns to an equivalence class of curves [γ] the vector $\gamma ^ { \prime } ( 0 )$ (expressed in coordinates using the standard basis for Rn). We now set about proving that (1) and (3) are also equivalent. Let $T _ { p } U$ denote the space of tangent vectors as given by formulation (1) (i.e., as elements of Rn) and (for the moment) $\tilde { T } _ { p } U$ that given by $( 3 ) \left( i . e . \right.$ , as derivations). Write the coordinates of $p \in U \subset \mathbb { R } ^ { n }$ as $( p _ { 1 } , \ldots , p _ { n } )$ . Now we have a linear map α: $T _ { p } U  \tilde { T } _ { p } U$ given by

$$
\alpha ( \nu _ { 1 } , \ldots , \nu _ { n } ) = \sum _ { i = 1 } ^ { n } \nu _ { i } { \frac { \partial } { \partial x _ { i } } } ,
$$

$i . e .$ , α sends a vector (in the undergraduate multivariable calculus sense) to the operation given by directional differentiation in the direction of that vector. We claim that α is bijective, justifying our proposal to regard (3) as an equivalent definition of the tangent space at $p .$ It should be clear that α is injective. Indeed, for each i we have an element $x _ { i } - p _ { i } \in O _ { p }$ , and we see that, where β : $\tilde { T } _ { p } U  T _ { p } U$ is given by

$$
\beta ( \nu ) = \left( \nu ( x _ { 1 } - p _ { 1 } ) , \dots , \nu ( x _ { n } - p _ { n } ) \right) ,
$$

we have $\begin{array} { r } { \beta \circ \alpha = 1 ( \mathrm { a s } \ \frac { \partial } { \partial x _ { i } } ( x _ { j } - p _ { j } ) = \delta _ { i j } ) } \end{array}$ . Thus α is injective, and $\beta$ surjective. To see that α is surjective, we note the following, whenever $\nu \in \tilde { T } _ { p } U \colon$

$\nu ( 1 ) = \nu ( 1 \cdot 1 ) = 1 \nu ( 1 ) + 1 \nu ( 1 ) = \nu ( 1 ) + \nu ( 1 )$ . Hence $\nu ( 1 ) = 0$ , and so by R-linearity $\nu ( c ) = 0$ for every constant function c.

• For any i and $j , \operatorname { i f } f \in O _ { p }$ we have

$$
\nu \left( ( x _ { i } - p _ { i } ) ( x _ { j } - p _ { j } ) f \right) = ( x _ { i } - p _ { i } ) | _ { p } \nu ( ( x _ { j } - p _ { j } ) f ) + ( x _ { j } - p _ { j } ) | _ { p } f ( p ) \nu ( ( x _ { i } - p _ { i } ) ) = 0 .
$$

• By the multivariable Taylor formula, any (germ of a) function $g \in O _ { p }$ can be written (on some neighborhood of $p )$

$$
g ( x ) = g ( p ) + \sum _ { i = 1 } ^ { n } \frac { \partial g } { \partial x _ { i } } ( p ) ( x _ { i } - p _ { i } ) + \sum _ { i , j = 1 } ^ { n } ( x _ { i } - p _ { i } ) ( x _ { j } - p _ { j } ) f _ { i j } ( x )
$$

for some $f _ { i j } \in O _ { p }$ . Hence by the first two items and the linearity of $\nu ,$ we get

$$
\nu ( g ) = \sum _ { i = 1 } ^ { n } \frac { \partial g } { \partial x _ { i } } ( p ) \nu ( x _ { i } - p _ { i } ) .
$$

Thus

$$
\nu = \sum \nu _ { i } \frac { \partial } { \partial x _ { i } } = \alpha ( \nu _ { 1 } , \ldots , \nu _ { n } ) ,
$$

where the numbers $\nu _ { i }$ are equal to $\nu ( x _ { i } - p _ { i } )$

In view of the above correspondence, we can drop the tilde in the notation $\tilde { T } _ { p } U$ , and always view tangent vectors as derivations on spaces of germs of functions. Even when we express a tangent vector in coordinates, we will often use notation consistent with the derivation interpretation and write the vector as

$$
\nu _ { 1 } \frac { \partial } { \partial x _ { 1 } } + \cdots + \nu _ { n } \frac { \partial } { \partial x _ { n } }
$$

rather than $( \nu _ { 1 } , \ldots , \nu _ { n } )$

Of course, another familiar notion from multivariable calculus is that of a vector field on an open set $U ,$ which can be thought of as a smooth family of tangent vectors at all of the points of $U ,$ , or as a smooth vector-valued function $X \colon ~ U \to \mathbb { R } ^ { n }$ , expressible in coordinates as $X ( m ) = ( X _ { 1 } ( m ) , \ldots , X _ { n } ( m ) )$ . There is also a coordinate-free interpretation of what a vector field is: it is a map X : $C ^ { \infty } ( U ) \to C ^ { \infty } ( U )$ which, as with tangent vectors, is a derivation, namely:

$X ( c f + g ) = c X ( f ) + X ( g )$ for all $c \in \mathbb { R } , f , g \in C ^ { \infty } ( U )$ , and

$X ( f g ) = f X ( g ) + g X ( f )$ for all $f , g \in C ^ { \infty } ( M )$

Note that while tangent vectors, when viewed as derivations, just take values in ${ \mathbb R } ,$ vector fields take values in the space of smooth functions. Just as with tangent vectors, there’s a natural one-to-one correspondence between the undergraduate versions of vector fields and the derivations on $C ^ { \infty } ( U )$ : simply assign to $( X _ { 1 } ( \cdot ) , \ldots , X _ { n } ( \cdot ) )$ the derivation

$$
f \mapsto \sum _ { i = 1 } ^ { n } X _ { i } { \frac { \partial f } { \partial x _ { i } } } .
$$

Again, the great advantage of the derivation interpretation is that it makes no direct reference to coordinates. So on a smooth manifold M, once have defined the space of smooth functions $C ^ { \infty } ( M )$ , we will effortlessly be able to define a vector field on M as a derivation X : $C ^ { \infty } ( M ) \to C ^ { \infty } ( M )$

Another nice feature of the derivation interpretation for vector fields (but not for tangent vectors) is that it points toward some additional structure on the space of vector fields that we wouldn’t have noticed if we just worked in coordinates. Namely, given that a vector field is a certain kind of function X : $C ^ { \infty } ( U ) \to C ^ { \infty } ( U )$ , it becomes natural to think about composing such functions. Now a slight hitch with this is that the composition of two derivations will not typically be a derivation. For example, $\frac { \partial } { \partial x _ { 1 } }$ is a derivation, but $\begin{array} { r } { \frac { \partial } { \partial { { x } _ { 1 } } } \circ \frac { \partial } { \partial { { x } _ { 1 } } } } \end{array}$ certainly is not: namely we have

$$
\frac { \partial } { \partial x _ { 1 } } \circ \frac { \partial } { \partial x _ { 1 } } ( x _ { 1 } x _ { 1 } ) = 2
$$

but

$$
x _ { 1 } \frac { \partial } { \partial x _ { 1 } } \circ \frac { \partial } { \partial x _ { 1 } } ( x _ { 1 } ) + x _ { 1 } \frac { \partial } { \partial x _ { 1 } } \circ \frac { \partial } { \partial x _ { 1 } } ( x _ { 1 } ) = 0 .
$$

So while we can “compose” two vector fields the result won’t be a vector field. However:

Proposition 1.1. Let A be a commutative R-algebra and let $X , Y \colon { \mathcal { A } }  { \mathcal { A } }$ be two derivations on $\mathcal { A }$ Then the commutator $[ X , Y ] : = X \circ Y - Y \circ X$ is also a derivation on A.

Proof. The linearity of [X, Y] is trivial, so we just need to check the Leibniz rule. We find, for $f , g \in { \mathcal { A } } ;$

$$
\begin{array} { r l } & { [ X , Y ] ( f g ) = X \left( Y ( f g ) \right) - Y \left( X ( f g ) \right) = X \left( f Y g + g Y f \right) - Y \left( f X g + g X f \right) } \\ & { \qquad = \left( f X Y g + ( X f ) ( Y g ) + g X Y f + ( X g ) ( Y f ) \right) - \left( f Y X g + ( Y f ) ( X g ) + g Y X f + ( Y g ) ( X f ) \right) } \\ & { \qquad = f ( X Y - Y X ) g + g ( X Y - Y X ) f = f [ X , Y ] ( g ) + g [ Y , X ] ( f ) , } \end{array}
$$

which is precisely the Leibniz rule for [X, Y].

In local coordinates, if $\begin{array} { r } { X = \sum X _ { i } \frac { \partial } { \partial x _ { i } } } \end{array}$ and $\begin{array} { r } { Y = \sum Y _ { j } \frac { \partial } { \partial x _ { i } } } \end{array}$ , then one finds

$$
\begin{array} { l } { [ X , Y ] ( f ) = \displaystyle \sum _ { i = 1 } ^ { n } X _ { i } \frac { \partial } { \partial x _ { i } } \left( \displaystyle \sum _ { j = 1 } ^ { n } Y _ { j } \frac { \partial f } { \partial x _ { j } } \right) - \displaystyle \sum _ { i = 1 } ^ { n } Y _ { i } \frac { \partial } { \partial x _ { i } } \left( \displaystyle \sum _ { j = 1 } ^ { n } X _ { j } \frac { \partial f } { \partial x _ { j } } \right) } \\ { = \displaystyle \sum _ { i , j = 1 } ^ { n } \left( X _ { i } Y _ { j } \frac { \partial ^ { 2 } f } { \partial x _ { i } \partial x _ { j } } + X _ { i } \frac { \partial Y _ { j } } { \partial x _ { i } } \frac { \partial f } { \partial x _ { j } } \right) - \displaystyle \sum _ { i , j = 1 } ^ { n } \left( Y _ { i } X _ { j } \frac { \partial ^ { 2 } f } { \partial x _ { i } \partial x _ { j } } + Y _ { i } \frac { \partial X _ { j } } { \partial x _ { i } } \frac { \partial f } { \partial x _ { j } } \right) } \\ { = \displaystyle \sum _ { j = 1 } ^ { n } \left( \displaystyle \sum _ { i = 1 } ^ { n } X _ { i } \frac { \partial Y _ { j } } { \partial x _ { i } } - Y _ { i } \frac { \partial X _ { j } } { \partial x _ { i } } \right) \frac { \partial f } { \partial x _ { j } } . } \end{array}
$$

Thus [X, Y] is the vector field $\textstyle \sum Z _ { j } { \frac { \partial } { \partial x _ { j } } }$ whose jth component is given by

$$
Z _ { j } = \sum _ { i = 1 } ^ { n } \left( X _ { i } { \frac { \partial Y _ { j } } { \partial x _ { i } } } - Y _ { i } { \frac { \partial X _ { j } } { \partial x _ { i } } } \right)\tag{1}
$$

This commutator operation on vector fields (also called the Lie bracket) turns out to be a fairly important one. Of course, if one wanted to work entirely in coordinates without taking a more abstract point of view, it would have been possible to just define the Lie bracket of two vector fields X and Y to be the vector field given by formula (1), but it’s not clear why one would be motivated to do so.

In general, the commutator operation $[ \cdot , \cdot ]$ on the space of linear maps from a vector space to itself satisfies the Jacobi identity:

$$
[ X , [ Y , Z ] ] + [ Z , [ X , Y ] ] + [ Y , [ Z , X ] ] = 0\tag{2}
$$

Indeed, the left hand side is equal to

$$
X ( Y Z - Z Y ) - ( Y Z - Z Y ) X + Z ( X Y - Y X ) - ( X Y - Y X ) Z + Y ( X Z - Z X ) - ( Z X - X Z ) Y
$$

and (using associativity of function composition) you can see that each of the six three-letter words made up of one each of the letters X,Y,Z appears above once positively and once negatively, so the sum is zero. Note that if $[ \cdot , \cdot ]$ were an associative operation we would instead have $[ X , [ Y , Z ] ] + [ Z , [ X , Y ] ] = [ X , [ Y , Z ] ] - [ [ X , Y ] , Z ] = 0 ;$ thus the Jacobi identity expresses a particular way for a binary operation to be non-associative. In general a vector space L equipped with a binary operation $[ \cdot , \cdot ] \colon A \times A \to A$ which is bilinear, which obeys $[ X , Y ] = - [ Y , X ]$ , and which satisfies the Jacobi identity is called a Lie algebra; thus we have shown that, if $U \subset \mathbb { R } ^ { n }$ is open, then the space $\chi ( U )$ of vector fields on $U$ is naturally a Lie algebra.

Exercise 1.2. a) Let $\phi \colon U \to V$ be a diffeomorphism between two open subsets of $\mathbb { R } ^ { n }$ , and let X be a vector field on $U .$ . Prove that if $\phi _ { * } X \colon C ^ { \infty } ( V ) \to C ^ { \infty } ( V )$ is defined by $( ( \phi _ { * } X ) ( f ) ) ( \phi ( p ) ) = ( X ( f \circ \phi ) ) ( p )$ , then $\phi _ { * } X$ is a vector field on V. Why did we have to assume that $\phi$ was a diffeomorphism (or at least bijective) in order to do this (unlike the situation with tangent vectors, which can be pushed forward by any smooth map)?

b) Prove that if X, Y are two vector fields on $U$ and $\operatorname { i f } \phi \colon U \to V$ is a diffeomorphism then

$$
\phi _ { * } [ X , Y ] = [ \phi _ { * } X , \phi _ { * } Y ] .
$$

Exercise 1.3. Define the following three vector fields1 on $\mathbb { R } ^ { 3 } \mathbf { i }$

$$
I = z { \frac { \partial } { \partial y } } - y { \frac { \partial } { \partial z } }
$$

$$
J = x \frac { \partial } { \partial z } - z \frac { \partial } { \partial x }
$$

$$
K = y \frac { \partial } { \partial x } - x \frac { \partial } { \partial y }
$$

a) Compute [I, J], [I, K], and $[ J , K ]$

b) Deduce as a formal consequence of part (a) that the cross product on $\mathbb { R } ^ { 3 }$ satisfies the Jacobi identity.

## 2. Bump functions and partitions of unity in $\mathbb { R } ^ { n }$

In point-set topology one learns a result called Urysohn’s Lemma, which states that given inclusions $A \subset$ $U \subset X$ where $X$ is a normal topological space, U is open, and A is closed, there is a continuous function $\chi \colon X \to [ 0 , 1 ]$ identically equal to one on A and identically zero on X \ U. A version of this result is extremely important in differential topology (perhaps more important than in point-set topology); unfortunately, since we need our functions to be $C ^ { \infty }$ and not just continuous, we can’t just cite Urysohn’s Lemma but rather need to prove a new, smooth, version of the result (of course, this smooth version will apply in a more limited context, if only because it doesn’t make sense to speak of “smooth functions” on a general normal topological space). The good news is that the functions can be constructed in a more concrete fashion than one sees in the proof of Urysohn’s Lemma.

We begin with a result in one-variable calculus.

Lemma 2.1. Define the function f : R → R by

$$
f ( t ) = \left\{ \begin{array} { l l } { e ^ { - 1 / t } } & { t > 0 } \\ { 0 } & { t \leq 0 } \end{array} \right.
$$

Then $f \in C ^ { \infty } (  { \mathbb { R } } )$ . Indeed, for all k ∈ N there is a polynomial $P _ { k } \in \mathbb { R } [ t ]$ with the property that the kth derivative $f ^ { ( k ) }$ exists and is given by

$$
f ^ { ( k ) } ( t ) = { \left\{ \begin{array} { l l } { P _ { k } ( 1 / t ) e ^ { - 1 / t } } & { t > 0 } \\ { 0 } & { t \leq 0 } \end{array} \right. }\tag{3}
$$

Proof. First note that if (3) holds, then $f ^ { ( k ) }$ is continuous on all of R: indeed continuity is obvious everywhere except zero, and at zero we have, by repeated applications of L’Hopital’s rule, ˆ

$$
\operatorname* { l i m } _ { t \to 0 ^ { + } } P _ { k } ( 1 / t ) e ^ { - 1 / t } = \operatorname* { l i m } _ { s \to \infty } \frac { P _ { k } ( s ) } { e ^ { s } } = \operatorname* { l i m } _ { s \to \infty } \frac { c _ { k } } { e ^ { s } } = 0
$$

where $c _ { k }$ is some constant (which results from differentiating deg $P _ { k }$ -many times the polynomial $P _ { k } ) .$ , from which continuity at zero follows directly.

Thus we just need to prove (3), which we do by induction on k. So assume (3) holds for $k ;$ we prove it for $k + 1$ . For $t < 0$ the formula is trivial. For $t = 0$ we see

$$
\operatorname * { l i m } _ { t \to 0 ^ { + } } { \frac { f ^ { ( k ) } ( t ) - f ^ { ( k ) } ( 0 ) } { t } } = \operatorname * { l i m } _ { t \to 0 ^ { + } } { \frac { 1 } { t } } P _ { k } ( 1 / t ) e ^ { - 1 / t } = \operatorname * { l i m } _ { s \to \infty } { \frac { s P _ { k } ( s ) } { e ^ { s } } } = 0
$$

by L’Hopital’s rule, and so (since the left-hand limit is triviall ˆ y zero) we have $f ^ { ( k + 1 ) } ( t ) = 0$ . Finally for $t > 0$ we have, by the product and chain rules,

$$
f ^ { ( k + 1 ) } ( t ) = { \frac { d } { d t } } \left( P _ { k } ( 1 / t ) e ^ { - 1 / t } \right) = - { \frac { 1 } { t ^ { 2 } } } P _ { k } ^ { \prime } \left( { \frac { 1 } { t } } \right) e ^ { - 1 / t } + { \frac { 1 } { t ^ { 2 } } } P _ { k } \left( { \frac { 1 } { t } } \right) e ^ { - 1 / t } ,
$$

and so the formula holds with

$$
P _ { k + 1 } ( s ) = s ^ { 2 } ( P _ { k } ^ { \prime } ( s ) + P _ { k } ( s ) ) .
$$

Note that our function f is a surjection to the half-open interval [0, 1), with $f ^ { - 1 } ( \{ 0 \} ) = ( - \infty , 0 ]$ . Out of this function we can build many other useful ones. For instance:

Corollary 2.2. There is $a ~ C ^ { \infty }$ function $g \colon { \mathbb { R } }  [ 0 , 1 ]$ with the property that $g ^ { - 1 } ( \{ 1 \} ) = [ 1 , \infty )$ and $g ^ { - 1 } ( \{ 0 \} ) =$ $( - \infty , 0 ] .$

Proof. Note that the function $t \mapsto f ( 1 - t )$ is smooth and nonnegative, and equals zero precisely on the interval $[ 1 , \infty )$ . In particular $f ( t ) + f ( 1 - t )$ is positive everywhere. So we can let

$$
g ( t ) = { \frac { f ( t ) } { f ( t ) + f ( 1 - t ) } } .
$$

I leave it to you to check that this has the desired properties.

Corollary 2.3. For any real numbers $a < b$ there is a $C ^ { \infty }$ function $g _ { a , b } \colon \mathrm { \mathbb { R } } \to [ 0 , 1 ]$ such that $g _ { a , b } ^ { - 1 } ( \{ 0 \} ) = ( - \infty , a ]$ and $g _ { a , b } ^ { - 1 } ( \{ 1 \} ) = [ b , \infty )$

Proof. Let

$$
g _ { a , b } ( t ) = g \left( \frac { t - a } { b - a } \right) .
$$

Corollary 2.4. For any real numbers $a < b < c <$ d there is a smooth “bump” function h: $\mathbb { R } \to [ 0 , 1 ]$ so that $h ^ { - 1 } ( \{ 1 \} ) = [ b , c ]$ and $h ^ { - 1 } ( \{ 0 \} ) = ( - \infty , a ] \cup [ d , \infty )$ .

Proof. Let

$$
h ( t ) = g _ { a , b } ( t ) ( 1 - g _ { c , d } ( t ) ) .
$$

Corollary 2.5. For $x \in \mathbb { R } ^ { n }$ and $r > 0$ let $B _ { r } ( x ) = \{ y \in \mathbb { R } ^ { n } \| y - x \| < r \}$ denote the open ball of radius r around x. Then for any $0 < s < r$ there is a smooth function $\beta \colon \mathbb { R } ^ { n } \to [ 0 , 1 ]$ such that $\beta ^ { - 1 } ( \{ 1 \} ) = \overline { { B _ { s } ( x ) } }$ and $s u p p ( \beta ) = \overline { { B _ { r } ( x ) } }$

(Here by $s u p p ( \beta )$ we mean the support of β, i.e., the closed set $\overline { { \{ y \in \mathbb { R } ^ { n } | \beta ( y ) \neq 0 \} } } )$

Proof. Let

$$
\beta ( y ) = 1 - g _ { s ^ { 2 } , r ^ { 2 } } ( \| y - x \| ^ { 2 } ) .
$$

Our goal now is the following theorem:

Theorem 2.6. Let $U \subset \mathbb { R } ^ { n }$ be an open set, and let $\mathcal { V } = \{ V _ { \alpha } | \alpha \in A \}$ be an open cover of U. Then there are $C ^ { \infty }$ functions $\chi _ { \alpha } \colon U \to [ 0 , 1 ]$ obeying the following properties:

(i) $s u p p ( \chi _ { \alpha } ) \subset V _ { \alpha }$

(ii) $A n y \ x \in U$ has a neighborhood $W _ { x }$ with the property that $\chi _ { \alpha } | _ { W _ { x } } = 0 .$ for all but finitely many α.

(iii) For all $x \in U$ we have $\begin{array} { r } { \sum _ { \alpha } \chi _ { \alpha } ( x ) = 1 } \end{array}$

## MIKE USHER

Note that property (ii) ensures that $\textstyle \sum _ { \alpha } \chi _ { \alpha }$ is well-defined and smooth (even if there are infinitely many— perhaps uncountably many—different α), since U is then covered by open sets on each of which the sum $\textstyle \sum _ { \alpha } \chi _ { \alpha }$ is really a finite sum (all but finitely many terms are zero).

Definition 2.7. A collection of functions $\{ \chi _ { \alpha } | \alpha \in A \}$ obeying properties (i)-(iii) of Theorem 2.6 is called a partition of unity subordinate to the cover $\{ V _ { \alpha } \}$

Theorem 2.6 has an analogue for general smooth manifolds (see Theorem 3.17); to make this more general version eventually easier to reach we present the proof for open sets in $\mathbb { R } ^ { n }$ in a fairly general way (a proof more specifically adapted to $\mathbb { R } ^ { n }$ can be found in Appendix A of Madsen-Tornehave). In particular we bring in the following definition from point-set topology:

Definition 2.8. A topological space X is called second-countable if there is a countable basis for the topology of X .

In other words, there should be a collection $\{ O _ { n } | n \in \mathbb { N } \}$ of open sets with the property that if U is open and $x \in U$ then $x \in O _ { n } \subset U$ for some n. For example $\mathbb { R } ^ { n }$ has this property (take the base to consist of open balls centered at points with rational coordinates and having rational radius), as does any open subset of $\mathbb { R } ^ { n }$ (just use those rational balls that are contained in the open subset). Part of our eventual definition will require that any smooth manifold also has this property.

Lemma 2.9. Let X be a second-countable locally compact Hausdorff space. Then there is a sequence of compact sets $\{ K _ { i } \} _ { i = 1 } ^ { \infty }$ and a sequence of open sets $\{ H _ { i } \} _ { i = 1 } ^ { \infty }$ such that

$K _ { i } \subset H _ { i }$

$X = \cup _ { i = 1 } ^ { \infty } K _ { i } = \cup _ { i = 1 } ^ { \infty } H _ { i }$

• If j ≥ i + 3 then Hi ∩ H j = ∅.

Proof. First note that a second-countable, locally compact space has a countable base for its topology which consists of open sets with compact closure. Indeed, given a countable base B, by local compactness any point $x \in X$ has a neighborhood $O _ { x }$ with compact closure, and there will be some $V \in { \mathcal { B } }$ such that $x \in V \subset O _ { x } ;$ evidently $\overline { { V } }$ will be compact, and the set of all V that can be obtained in this fashion will still be a base for the topology (and will be contained in the original ${ \mathcal { B } } ,$ so will be countable).

So let $\{ U _ { i } \} _ { i = 0 } ^ { \infty }$ be a base for the topology which is countable and such that each $\overline { { U _ { i } } }$ is compact. In particular the $U _ { i }$ cover X. We claim now that there is a sequence $\{ G _ { i } \} _ { i = 0 } ^ { \infty }$ of open sets with each $\overline { { G _ { i } } }$ compact, such that ${ \overline { { G _ { i } } } } \subset G _ { i + 1 }$ and such that $\cup _ { i = 0 } ^ { \infty } G _ { i } = X$ . Specifically, the $G _ { i }$ will have the form

$$
G _ { i } = U _ { 0 } \cup \cdots \cup U _ { j _ { i } }
$$

for a certain increasing sequence of natural numbers { ji}. To construct the sequence { ji}, we let $j _ { 0 } = 0$ (so $G _ { 0 } = U _ { 0 } )$ , and assuming that we have chosen $j _ { k }$ , so that $G _ { k } = U _ { 1 } \cup \cdots \cup U _ { j _ { k } }$ , we note that $G _ { k }$ is compact since the $\overline { { U _ { i } } }$ are, and so since the $U _ { i }$ cover X there must be some $j _ { k + 1 } > j _ { k }$ so that ${ \overline { { G _ { k } } } } \subset \cup _ { i = 1 } ^ { j _ { k + 1 } } U _ { i }$ . Inductively choosing the $j _ { k }$ in this fashion results in a sequence $G _ { i }$ satisfying the required properties (the fact that the $G _ { i }$ cover X follows from the fact that the $U _ { i }$ do, and the fact that $j _ { i } $ ∞ since the $j _ { i }$ are a strictly increasing sequence of natural numbers).

To construct $K _ { i }$ and $H _ { i } ,$ let $K _ { 1 } = { \overline { { G _ { 1 } } } } , W _ { 1 } = G _ { 2 }$ , and, for $i \geq 2$ , let $K _ { i } = \overline { { G _ { i } } } \setminus G _ { i - 1 }$ and $H _ { i } = G _ { i + 1 } \setminus \overline { { G _ { i - 2 } } }$ . These are easily seen to satisfy the required properties.

Proof of Theorem 2.6. Let $K _ { i }$ and $H _ { i }$ be subsets of U as in Lemma 2.9 (applied with $X = U )$ , and fix any i. For all $x \in K _ { i }$ we may choose $\alpha _ { x } \in A$ and $\epsilon _ { x } > 0$ so that $B _ { 2 \epsilon _ { x } } ( x ) \subset V _ { \alpha _ { x } } \cap H _ { i }$ . Then the collection of open balls $\{ B _ { \epsilon _ { x } } ( x ) | x \in K _ { i } \}$ covers $K _ { i } ,$ so it has a finite subcover.

Now letting i vary and taking the union of all of these finite subcovers, we have a countable collection of balls $\left\{ B _ { k } \right\} _ { k = 1 } ^ { \infty }$ that covers $X ,$ , and such that where $\tilde { B } _ { k }$ denotes the ball with the same center as $B _ { k }$ but twice the radius, there are $\alpha _ { k }$ and $i _ { k }$ such that ${ \tilde { B } } _ { k } \subset V _ { \alpha _ { k } } \cap H _ { i _ { k } }$ . (While there may be more than one such $\alpha _ { k }$ and $i _ { k } .$ —there might even be uncountably many possible $\alpha _ { k } { \mathrm { - } } \mathrm { w e }$ specifically choose one $\alpha _ { k }$ and $i _ { k }$ for every $k .$ For convenience let us take $i _ { k }$ to be the i for which $B _ { k }$ was a member of the finite subcover of $K _ { i }$ , so that in particular for any i there are just finitely many k with $i _ { k } = i . )$

I claim that the balls $\tilde { B } _ { k }$ form a locally finite cover of $U , i . e .$ that any point $x \in U$ has a neighborhood $O _ { x }$ which meets just finitely many of the $\tilde { B } _ { k }$ . Indeed we could use for $O _ { x }$ any neighborhood of x with compact closure. For then $O _ { x }$ is contained in the union of just finitely many of the sets $H _ { i } ,$ , say $O _ { x } \subset H _ { 1 } \cup \cdots \cup H _ { r }$ . But the $H _ { i }$ have the property that $H _ { i } \cap H _ { m } = \emptyset$ whenever $m \geq i + 3$ , and so $O _ { x } \cap H _ { m } = \emptyset$ for m $\geq r + 3$ . Consequently $\tilde { B } _ { k } \cap O _ { x } = \emptyset$ unless k is one of the finitely many indices having $i _ { k } \le r + 2$

We can now construct the desired functions. First, for each $k ,$ let $\psi _ { k } \colon U \to [ 0 , 1 ]$ be a smooth function identically equal to 1 on $B _ { k }$ and such that $s u p p ( \psi _ { k } ) \subset \tilde { B } _ { k } ;$ such $\psi _ { k }$ exist by Corollary 2.5. By the previous paragraph, any point in $U$ has a neighborhood which is disjoint from the supports of all but finitely many of the $\psi _ { k } ;$ consequently

$$
\psi = \sum _ { k = 1 } ^ { \infty } \psi _ { k }
$$

is a well-defined, smooth function. Moreover $\psi > 0$ everywhere, since the (smaller) balls $B _ { k }$ cover $U .$ So for any k we have a well-defined, smooth function $\frac { \psi _ { k } } { \psi }$ , and obviously $\begin{array} { r } { \sum _ { k } \frac { \psi _ { k } } { \psi } = 1 } \end{array}$

Now define

$$
\chi _ { \alpha } = \sum _ { k : \alpha _ { k } = \alpha } \frac { \psi _ { k } } { \psi } .
$$

Since $\tilde { B } _ { k } \subset V _ { \alpha }$ whenever $\alpha ~ = ~ \alpha _ { k }$ , we have $s u p p ( \chi _ { \alpha } ) \subset V _ { \alpha }$ for all $\alpha .$ . Since any point has a neighborhood intersecting the support of $\psi _ { k }$ for only finitely many k, there will be just finitely many $\chi _ { \alpha }$ whose supports intersect this neighborhood (namely, just those α which equal $\alpha _ { k }$ for one of these k). Finally, we clearly have

$$
\sum _ { \alpha } \chi _ { \alpha } = \sum _ { \alpha } \sum _ { k : \alpha _ { k } = \alpha } \frac { \psi _ { k } } { \psi } = \sum _ { k } \frac { \psi _ { k } } { \psi } = 1 .
$$



As essentially a special case we get a direct analogue of Urysohn’s Lemma:

Corollary 2.10. $I f A \subset U \subset \mathbb { R } ^ { n }$ with A closed and U open, there is a $C ^ { \infty }$ function $f \colon  { \mathbb { R } } ^ { n } \to [ 0 , 1 ]$ with $f | _ { A } = 1$ and $s u p p ( f ) \subset U$

Proof. Let $\{ \chi _ { 1 } , \chi _ { 2 } \}$ be a partition of unity subordinate to the cover $\{ U , \mathbb { R } ^ { n } \setminus A \} \ \mathrm { o f } \ \mathbb { R } ^ { n }$ , and let $f = \chi _ { 1 }$ . I leave it to you to confirm the desired properties. 

Exercise 2.11. a) Let $U \subset \mathbb { R } ^ { n }$ be open, let $p \in U$ , and let X be a vector field on U (use the interpretation of X as a derivation from $C ^ { \infty } ( U )$ to itself). Prove that one can obtain a well-defined tangent vector (in the sense of a derivation $O _ { p } \to \mathbb { R } ) X _ { p }$ by the following prescription: If $[ f , V ] \in O _ { p } ,$ let ${ \tilde { f } } \in C ^ { \infty } ( U )$ be a function such that $[ \tilde { f } , U ] = [ f , V ]$ . Then $X \tilde { \tilde { f } } \in C ^ { \infty } ( U )$ , and we set

$$
X _ { p } ( [ f , V ] ) = ( X \tilde { f } ) ( p )
$$

(Part of the problem is showing that $\tilde { f }$ exists, and moreover that $X _ { p } ( [ f , V ] )$ is independent of the choice of such ${ \textrm { a } } { \tilde { f } } . )$

b) If in coordinates we have $\begin{array} { r } { X = \sum _ { i } f _ { i } \frac { \partial } { \partial x _ { i } } } \end{array}$ , prove that $\begin{array} { r } { X _ { p } = \sum _ { i } f _ { i } ( p ) \frac { \partial } { \partial x _ { i } } } \end{array}$

## MIKE USHER

## 3. Smooth manifolds

Definition 3.1. Let $n \in \mathbb { N } .$ An n-dimensional topological manifold (or “topological n-manifold”) is a secondcountable Hausdorff space M with the property that, for all $m \in M _ { : }$ , there is a neighborhood $U \subset M$ of m and a homeomorphism φ: $U \to V$ where $V \subset \mathbb { R } ^ { n }$ is an open subset.

Remark 3.2. Of course, by replacing V with a small open ball $B \subset V$ around $\phi ( p )$ and U with $\phi ^ { - 1 } ( B )$ , we could just as well require the image of $\phi$ is an open ball in $\mathbb { R } ^ { n }$ rather than an arbitrary open set. In turn, since any open ball in $\mathbb { R } ^ { n }$ is homeomorphic (and indeed diffeomorphic) to $\mathbb { R } ^ { n }$ , we could equally well require the images of the maps $\phi$ in Defnition 3.1 to all be $\mathbb { R } ^ { n } { \underline { { - i . e . } } }$ , a topological n-manifold is a second-countable Hausdorff space in which every point has a neighborhood homeomorphic to $\mathbb { R } ^ { n }$

Definition 3.3. Let M be a topological n-manifold, and let k be either a positive integer or ∞. A $C ^ { k }$ atlas on M is a collection $\mathcal { A } = \{ ( U _ { \alpha } , \phi _ { \alpha } ) | \alpha \in A \}$ } where

• The $U _ { \alpha }$ are open subsets of M, and $\cup _ { \alpha \in A } U _ { \alpha } = M .$

• Each $\phi _ { \alpha } \colon { \cal U } _ { \alpha } \to \mathbb { R } ^ { n }$ is a homeomorphism from $U _ { \alpha }$ to the open subset $\phi _ { \alpha } ( U _ { \alpha } ) \subset \mathbb { R } ^ { n }$ , and

$H \alpha , \beta \in A$ are such that $U _ { \alpha } \cap U _ { \beta } \neq \emptyset ,$ , then

$$
\phi _ { \beta } \circ \phi _ { \alpha } ^ { - 1 } \colon \phi _ { \alpha } ( U _ { \alpha } \cap U _ { \beta } ) \to \phi _ { \beta } ( U _ { \alpha } \cap U _ { \beta } )
$$

is of class $C ^ { k }$

The maps $\phi _ { \alpha } \colon { \cal U } _ { \alpha } \to \mathbb { R } ^ { n }$ are called coordinate charts (or sometimes “coordinate patches”) for the atlas A.

Exercise 3.4. (a) If A and B are $C ^ { k }$ atlases on a topological n-manifold, write $\mathcal { A } \sim \mathcal { B } \operatorname { i f } \mathcal { A } \cup \mathcal { B }$ is also a $C ^ { k }$ atlas. Prove that ∼ defines an equivalence relation on the set of all atlases.

(b) If ${ \mathcal { A } } = \{ ( U _ { \alpha } , \phi _ { \alpha } ) \}$ is a $C ^ { k }$ atlas for M, let $\mathcal { A } _ { m a x }$ x denote the set of all pairs $( U , \phi )$ where φ : $U \to \mathbb { R } ^ { n }$ is a homeomorphism from an open subset $U \subset M$ to an open subset $\phi ( U ) \subset \mathbb { R } ^ { n }$ , and such that whenever $U \cap U _ { \alpha } \neq \emptyset$ the map φ ◦ $\cdot \phi _ { \alpha } ^ { - 1 } \colon \phi _ { \alpha } ( U \cap U _ { \alpha } ) \to \phi ( U \cap U _ { \alpha } )$ is $C ^ { k }$ and has inverse which is $C ^ { k }$ . Prove that $\mathcal { A } _ { m a x }$ is an atlas containing A, and is maximal in the sense that it contains every other atlas that contains A. Deduce that if A ∼ B then $\mathcal { A } _ { m a x } = \mathcal { B } _ { m a x }$

Definition 3.5. A $C ^ { k }$ -differentiable structure on a topological n-manifold is a maximal atlas A on M (i.e., an atlas such that, in the notation of Exercise 3.4(b), $\mathcal { A } = \mathcal { A } _ { m a x } ) .$ . An n-dimensional $C ^ { k }$ manifold is a topological n-manifold M equipped with a $C ^ { k }$ -differentiable structure. $A C ^ { \infty }$ manifold will also be called a smooth manifold, and a $C ^ { \infty }$ -differentiable structure will also be called a smooth structure.

Remark 3.6. We will almost exclusively discuss smooth $( i . e . , C ^ { \infty } )$ manifolds in this course. This is partly justified by the fact that, for $1 \leq k < \infty$ , any $C ^ { k }$ manifold is Ck-diffeomorphic to a $C ^ { \infty }$ manifold (there is a proof in Hirsch’s book Differential Topology). On the other hand there is some real loss of generality in looking at $C ^ { \infty }$ (or even just $C ^ { 1 } )$ manifolds rather than just topological $( C ^ { 0 } )$ manifolds, as there are topological manifolds which are not homeomorphic to any $C ^ { 1 }$ manifold. Examples of such are rather complicated—Kervaire constructed a 10-dimensional one in 1960, and the lowest dimension in which any occur is 4, where there are examples due to Freedman in the early 1980s.

Remark 3.7. The definition is that a smooth manifold is a certain kind of topological space equipped with a maximal $C ^ { \infty }$ atlas. A maximal atlas is a rather unwieldy object—except in trivial cases it will consist of uncountably many coordinate charts. But in view of Exercise 3.4 it is rarely if ever necessary to really work with a maximal atlas—you just have to specify one atlas (often with a small, finite number of charts), and then this canonically determines a maximal atlas by the construction in Exercise 3.4(b). One could equally well define a smooth manifold as a topological manifold equipped with an equivalence class of atlases, where the equivalence relation is the one from Exercise 3.4(a). One advantage of a maximal atlas is that “everything that could be a coordinate patch is,” so that if you have to work in local coordinates you have a great variety of possible coordinate systems to work in and you can choose whichever works best for your purposes at the time.

Example 3.8. As the simplest possible example, we note that $\mathbb { R } ^ { n }$ is canonically a smooth manifold: take an atlas consisting of the single pair $( 1 _ { \mathbb { R } ^ { n } } , \mathbb { R } ^ { n } )$ where $1 _ { \mathbb { R } ^ { n } }$ denotes the identity map. As noted in Remark 3.7 specifying this (very small!) atlas canonically determines a maximal atlas $( i . e .$ , a differentiable structure).

Of course we could just as well have replaced $\mathbb { R } ^ { n }$ by any open subset U of $\mathbb { R } ^ { n }$ , using the atlas $\{ ( 1 _ { U } , U ) \}$ t o make U into a smooth manifold. More generally, if M is any smooth manifold with atlas $\{ ( \phi _ { \alpha } , U _ { \alpha } ) \}$ } and if $U \subset M$ is an open subset then we naturally get an atlas on U, namely $\{ ( \phi _ { \alpha } | _ { U \cap U _ { \alpha } } , U \cap U _ { \alpha } ) \}$

I promised at the outset that a smooth manifold would be the kind of space on which it is possible to do something resembling calculus. In particular if M is a smooth m-manifold it should be possible to speak of differentiable functions from M to $\mathbb { R } ^ { n }$ , or vice versa, for any n (and, more generally, if M and N are two smooth manifolds we should be able to speak of differentiable functions from M to $N )$ . The principle is simple: one checks the differentiability of a function by using coordinate charts to turn the function into one whose domain and range are open subsets of Euclidean space, where we already have a notion of differentiability.

Definition 3.9. Let M be an m-dimensional smooth manifold, with (maximal) atlas $\{ ( \phi _ { \alpha } , U _ { \alpha } ) | \alpha \in A \}$

$\begin{array} { r } { { I f f \colon M \to \mathbb { R } ^ { n } } } \end{array}$ is a continuous function, we say f is of class $C ^ { k } { } _ { ; }$ , and write $f \in C ^ { k } ( M , \mathbb { R } ^ { n } )$ , if for every α $\in A$ the function

$$
f \circ \phi _ { \alpha } ^ { - 1 } \colon \phi _ { \alpha } ( U _ { \alpha } ) \to \mathbb { R } ^ { n }
$$

is of class $C ^ { k }$ (note that $f \circ \phi _ { \alpha } ^ { - 1 }$ is a function from an open set in $\mathbb { R } ^ { m }$ to $\mathbb { R } ^ { n }$ , so the notion of $f \circ \phi _ { \alpha } ^ { - 1 }$ being of class $C ^ { k }$ is well-defined from multivariable calculus).

$I f V \subset \mathbb { R } ^ { m }$ is an open subset and g: V → M is a continuous function we say that $g$ is of class $C ^ { k } { } _ { ; }$ , and write $C ^ { k } ( V , M )$ , if for all $\alpha \in A$ the function

$$
\phi _ { \alpha } \circ g \colon g ^ { - 1 } ( U _ { \alpha } ) \to \mathbb { R } ^ { m }
$$

is of class $C ^ { k } .$

• Suppose that N is an n-dimensional smooth manifold, with (maximal) atlas $\{ \psi _ { \beta } , V _ { \beta } ) | \beta \in B \} . \ I f f \colon M \to$ N is a continuous function, we say that f is of class $C ^ { k }$ if, for all $\alpha , \beta$ such that $f ( U _ { \alpha } ) \cap V _ { \beta } \neq \emptyset ,$ the function

$$
\psi _ { \beta } \circ f \circ \phi _ { \alpha } ^ { - 1 } \colon \phi _ { \alpha } ( U _ { \alpha } \cap f ^ { - 1 } ( V _ { \beta } ) ) \to \mathbb { R } ^ { n }
$$

is of class $C ^ { k }$ (as a function from an open subset of Rm to $\mathbb { R } ^ { n } )$

The appropriate notion of isomorphism of smooth manifolds is the following:

Definition 3.10. Let M and N be $C ^ { k }$ -manifolds. A $C ^ { k }$ -diffeomorphism from M to N is a smooth, bijective map $f \colon M \to N$ such that $f ^ { - 1 }$ is also smooth.

As mentioned earlier, we will generally just consider the $C ^ { \infty }$ case—as such a “diffeomorphism” will, unless otherwise indicated, mean a $C ^ { \infty }$ diffeomorphism.

Of course, it would be a pain to actually check that Definition 3.9 is satisfied since maximal atlases are very large. But the following exercise shows that the $C ^ { k }$ property can be checked more easily (and also implies that, viewing $\mathbb { R } ^ { n }$ as a smooth manifold, the third part of the above definition contains the first two as special cases). This exercise is intended in part to demonstrate the role of the assumption on the functions $\phi _ { \beta } \circ \phi _ { \alpha } ^ { - 1 }$ in the definition of an atlas.

Exercise 3.11. Let M and N be smooth manifolds, and let $f \colon { \cal { M } }  { \cal { N } }$ be a continuous function. Prove that $f \in C ^ { k } ( M , N )$ if and only if the following holds: For each $x \in M$ , there exists a coordinate chart φ : $U \to \mathbb { R } ^ { m }$ from the atlas for M and a coordinate chart $\psi \colon { \cal V }  \mathbb { R } ^ { n }$ from the atlas for N such that $x \in U , f ( x ) \in V$ and

$$
\psi \circ f \circ \phi ^ { - 1 } \colon \phi ( U \cap f ^ { - 1 } ( V ) ) \to \mathbb { R } ^ { n }
$$

is of class $C ^ { k }$

Thus in practice to show that a map is $C ^ { k }$ we just need to find collections of charts covering the manifolds in terms of which the map is a $C ^ { k }$ map between Euclidean spaces, rather than checking the condition on the entire maximal atlas. Another way of saying this is that the two appearances of the word “(maximal)” in Definition 3.9 are unnecessary—we can just use any atlases (possibly quite small) to check the $C ^ { k }$ condition.

Example 3.12. One can see that the n-dimensional sphere

$$
S ^ { n } = \left\{ ( x _ { 0 } , x _ { 1 } , \ldots , x _ { n } ) \in \mathbb { R } ^ { n + 1 } \left| \sum _ { i = 0 } ^ { n } x _ { i } ^ { 2 } = 1 \right. \right\}
$$

is a smooth manifold by using stereographic projections. Of course the subspace topology on $S ^ { n }$ induced by its inclusion into $\mathbb { R } ^ { n + 1 }$ makes $S ^ { n }$ into a second-countable Hausdorff space. We construct a smooth atlas on $S ^ { n }$ with two charts: define

$$
\begin{array} { l } { { U _ { - } = \{ ( x _ { 0 } , \ldots , x _ { n } ) \in S ^ { n } | x _ { 0 } \neq 1 \} } } \\ { { \ } } \\ { { U _ { + } = \{ ( x _ { 0 } , \ldots , x _ { n } ) \in S ^ { n } | x _ { 0 } \neq - 1 \} } } \end{array}
$$

In other words, $U _ { - }$ and $U _ { + }$ are the complements of the north and south poles, respectively. Clearly $S ^ { n } = U _ { - } \cup U _ { + }$ Now define $\phi _ { - } \colon { U _ { - } \to \mathbb { R } ^ { n } }$ by

$$
\phi _ { - } ( x _ { 0 } , \ldots , x _ { n } ) = \left( { \frac { x _ { 1 } } { 1 - x _ { 0 } } } , \ldots , { \frac { x _ { n } } { 1 - x _ { 0 } } } \right)
$$

and similarly define $\phi _ { + } \colon U _ { + } \to \mathbb { R } ^ { n }$ by

$$
\phi _ { + } ( x _ { 0 } , \ldots , x _ { n } ) = \left( { \frac { x _ { 1 } } { 1 + x _ { 0 } } } , \ldots , { \frac { x _ { n } } { 1 + x _ { 0 } } } \right)
$$

So $\phi _ { - }$ can be visualized as sending a point $p \in S ^ { n } \backslash$ {north pole} to the point of intersection between the hyperplane $\{ x _ { 0 } ~ = ~ 0 \}$ and the unique line through the north pole and $p .$ It is clear from the formulas that $\phi _ { - }$ and $\phi _ { + }$ are continuous. Both of them are in fact homeomorphisms to $\mathbb { R } ^ { n }$ : one finds that the inverses $\phi _ { \pm } ^ { - 1 } \mathbb { R } ^ { n } \to U _ { \ast }$ ± are given by the formula

$$
\phi _ { \pm } ^ { - 1 } ( y _ { 1 } , \ldots , y _ { n } ) = \left( \pm \frac { 1 - \sum y _ { i } ^ { 2 } } { 1 + \sum y _ { i } ^ { 2 } } , \frac { 2 y _ { 1 } } { 1 + \sum y _ { i } ^ { 2 } } , \ldots , \frac { 2 y _ { n } } { 1 + \sum y _ { i } ^ { 2 } } \right) .
$$

Since the inverses are continuous the $\phi _ { \pm }$ are indeed homeomorphisms to $\mathbb { R } ^ { n }$ . What remains is to check that the “transition function” $\phi _ { + } \circ \phi _ { - } ^ { - 1 } \colon \phi _ { - } ( U _ { + } \cap U _ { - } ) \to \phi _ { + } ( U _ { + } \cap U _ { - } ) { \mathrm { ~ i s ~ } } C ^ { \infty }$ , and likewise that $\phi _ { - } \circ \phi _ { + } ^ { - 1 }$ is $C ^ { \infty }$ (of course, the second of these is the inverse of the first). Now $U _ { + } \cap U .$ − is the complement of the two (north and south) poles of $S ^ { n }$ , i.e. $U _ { + } \cap U _ { - } = S ^ { n } \setminus \{ ( \pm 1 , 0 , \dots , 0 ) \}$ }. Now

$$
\phi _ { + } ( 1 , 0 , \ldots , 0 ) = \phi _ { - } ( - 1 , 0 , \ldots , 0 ) = ( 0 , \ldots , 0 ) ,
$$

so

$$
\phi _ { - } ( U _ { + } \cap U _ { - } ) = \phi _ { + } ( U _ { + } \cap U _ { - } ) = \mathbb { R } ^ { n } \ \backslash \ \{ ( 0 , \ldots , 0 ) \} .
$$

For any $( y _ { 1 } , \dots , y _ { n } ) \in \mathbb { R } ^ { n } \setminus \{ ( 0 , \dots , 0 ) \}$ we have

$$
\begin{array} { r l } & { \phi _ { + } \circ \phi _ { - } ^ { - 1 } ( y _ { 1 } , \dots , y _ { n } ) = \phi _ { + } \left( \frac { \sum y _ { i } ^ { 2 } - 1 } { \sum y _ { i } ^ { 2 } + 1 } , \frac { 2 y _ { 1 } } { \sum y _ { i } ^ { 2 } + 1 } , \dots , \frac { 2 y _ { n } } { \sum y _ { i } ^ { 2 } + 1 } \right) } \\ & { \qquad = \left( \left( \frac { 2 \sum y _ { i } ^ { 2 } } { \sum y _ { i } ^ { 2 } + 1 } \right) ^ { - 1 } \frac { 2 y _ { 1 } } { \sum y _ { i } ^ { 2 } + 1 } , \dots , \left( \frac { 2 \sum y _ { i } ^ { 2 } } { \sum y _ { i } ^ { 2 } + 1 } \right) ^ { - 1 } \frac { 2 y _ { n } } { \sum y _ { i } ^ { 2 } + 1 } \right) } \\ & { \qquad = \left( \frac { y _ { 1 } } { \sum y _ { i } ^ { 2 } } , \dots , \frac { y _ { n } } { \sum y _ { i } ^ { 2 } } \right) . } \end{array}
$$

Since this map is defined only on the complement of the origin, it is clearly $C ^ { \infty }$ (the components are quotients of nonvanishing $C ^ { \infty }$ functions), and its inverse (which as noted earlier is $\phi _ { - } \circ \phi _ { + } ^ { - 1 } )$ is evidently $C ^ { \infty }$ as well (actually

if you look at the formula you see that it turns out that this map is equal to its own inverse). Thus we’ve shown that the transition functions for our atlas are $C ^ { \infty }$ , completing the proof that $S ^ { n }$ is a smooth manifold.

Example 3.13. Recall that the n-dimensional real projective space $\mathbb { R } P ^ { n }$ is the space of lines through the origin in $\mathbb { R } ^ { n + 1 }$ . This is given the structure of a (second-countable, Hausdorff) topological space by identifying it as

$$
\mathbb { R } P ^ { n } = \frac { \mathbb { R } ^ { n + 1 } \setminus \{ \vec { 0 } \} } { \vec { \nu } \sim \lambda \vec { \nu } \forall \vec { \nu } \in \mathbb { R } ^ { n + 1 } \setminus \{ 0 \} , \lambda \in \mathbb { R } \setminus \{ 0 \} }
$$

and using the quotient topology. Thus a general element of $\mathbb { R } { P } ^ { n + 1 }$ can be written as an equivalence class $[ x _ { 0 } , \ldots , x _ { n } ]$ for some $x _ { i } ~ \in ~ \mathbb { R }$ with not all $x _ { i } \ = \ 0 ,$ and we have $[ x _ { 0 } \ : \ \cdot \ \cdot \ : \ x _ { n } ] \ = \ [ y _ { 0 } \ : \ \cdot \ \cdot \ : y _ { n } ]$ iff there is $\lambda \neq 0$ so that $y _ { i } = \lambda x _ { i }$ for all i. (The $x _ { i }$ are called “homogeneous coordinates.”)

We now put a differentiable structure on $\mathbb { R } P ^ { n }$ , making it a smooth n-manifold. For $i = 0 , \ldots , n$ let

$$
U _ { i } = \{ [ x _ { 0 } , \dots , x _ { n } ] \in \mathbb { R } P ^ { n } | x _ { i } \neq 0 \}
$$

(of course, the truth or falsehood of the statement that $x _ { i } ~ \neq ~ 0$ is independent of which representative of the equivalence class we choose). The $U _ { i }$ are open sets $( \mathrm { w h y 2 } )$ , and $\mathbb { Q } P ^ { n } = \cup _ { i = 0 } ^ { n } U _ { i }$ since any element of $\mathbb { R } P ^ { n }$ has at least one of its homogeneous coordinates nonzero.

It shouldn’t be too hard to convince yourself that each of the open sets $U _ { i }$ is homeomorphic to Rn: for example for $i ~ = ~ n ,$ , an element of $x \ \in \ U _ { n }$ has form $[ x _ { 0 } \ : \ \cdots \ : \ x _ { n } ]$ where $x _ { n } \ \ne \ 0 ,$ , and since $x _ { n } ~ \neq ~ 0$ we can simultaneously multiply all of the $x _ { i }$ by 1x —this doesn’t change the equivalence class, but changes the last homogeneous coordinate to 1. Thus $U _ { n }$ can be identified with the set of tuples $( x _ { 0 } , \ldots , x _ { n - 1 } , 1 )$ , which is equivalent to Rn.

To make the discussion in the previous paragraph more precise, we introduce charts $\phi _ { i } \colon U _ { i } \to \mathbb { R } ^ { n }$ . Namely, define

$$
\begin{array} { c } { \phi _ { i } \colon U _ { i } \to \mathbb { R } ^ { n } } \\ { \phi _ { i } ( [ x _ { 0 } : \cdots : x _ { n } ] ) = \left( \displaystyle \frac { x _ { 0 } } { x _ { i } } , \ldots , \displaystyle \frac { x _ { i - 1 } } { x _ { i } } , \displaystyle \frac { x _ { i + 1 } } { x _ { i } } , \ldots , \displaystyle \frac { x _ { n } } { x _ { i } } \right) . } \end{array}
$$

This map is certainly well-defined, since multiplying all entries of $( x _ { 0 } , \ldots , x _ { n } )$ by the same scalar λ does not affect the ratios $x _ { j } / x _ { i }$ . Moreover we see that $\phi _ { i }$ is bijective, with inverse given by

$$
\phi _ { i } ^ { - 1 } ( y _ { 0 } , \ldots , y _ { i - 1 } , y _ { i + 1 } , \ldots , y _ { n } ) = [ y _ { 0 } : \cdots , y _ { i - 1 } : 1 : y _ { i + 1 } : \cdots : y _ { n } ] .
$$

Both $\phi _ { i }$ and $\phi _ { i } ^ { - 1 }$ are continuous—of course to see this one has to think a little bit about the quotient topology, but it’s not hard and is left to you.

So we have a covering $\mathbb { R } P ^ { n } = \cup _ { i = 0 } ^ { n } U _ { i }$ by open sets with homeomorphisms $\phi _ { i } \colon U _ { i } \to \mathbb { R } ^ { n }$ . It remains to check that the transition functions $\phi _ { i } \circ \phi _ { i } ^ { - 1 } \colon \phi _ { j } ( U _ { i } \cap U _ { j } ) \to \phi _ { i } ( U _ { i } \cap U _ { j } )$ are smooth. This follows quickly from the formulas that we’ve already written down: assuming that $i < j$

$$
\begin{array} { r l } & { \phi _ { i } \circ \phi _ { j } ^ { - 1 } ( y _ { 0 } , \dotsc , y _ { j - 1 } , y _ { j + 1 } , \dotsc , y _ { n } ) = \phi _ { i } ( [ y _ { 0 } : \dots : y _ { j - 1 } : 1 : y _ { j + 1 } : \dots : n ] ) } \\ & { \qquad = \left( \frac { y _ { 0 } } { y _ { i } } , \dotsc , \frac { y _ { i - 1 } } { y _ { i } } , \frac { y _ { i + 1 } } { y _ { i } } , \dotsc , \frac { y _ { j - 1 } } { y _ { i } } , \frac { 1 } { y _ { i } } , \frac { y _ { j + 1 } } { y _ { i } } , \dotsc , \frac { y _ { n } } { y _ { i } } \right) . } \end{array}
$$

Of course the case that $i > j$ differs from this only in the ordering of i and j in the above formula. Now on the open subset $\phi _ { j } ( U _ { i } \cap U _ { j } ) \subset \mathbb { R } ^ { n }$ we will have $y _ { i } \neq 0 ,$ , so $\phi _ { i } \circ \phi _ { i } ^ { - 1 }$ is indeed smooth on $\phi _ { j } ( U _ { i } \cap U _ { j } )$ , as required. Thus $\{ ( \phi _ { i } , U _ { i } ) : i = 0 , \ldots , n \}$ forms a $C ^ { \infty }$ atlas for $\mathbb { Q } P ^ { n }$ , making $\check { \mathbb { R } } P ^ { n }$ into a smooth manifold.

Fairly easy modifications of this argument show that the complex projective space $\mathbb { C } P ^ { n }$ is a smooth $2 n \text{‰}$ manifold, and that the quaternionic projective space $\mathbb { H } P ^ { n }$ is a smooth 4n-manifold.

Exercise 3.14. Recall that another way of describing $\mathbb { R } P ^ { n }$ is as a quotient of $S ^ { n }$ by the equivalence relation which identifies any $x \in S ^ { n } \subset \mathbb { R } ^ { n + 1 }$ with −x. Thus we have a quotient projection $\pi \colon { \cal S } ^ { n }  \mathbb { R } P ^ { n }$ . Prove that $\pi \in C ^ { \infty } ( S ^ { n } , \mathbb { R } P ^ { n } )$ .

Exercise 3.15. (a) If M and N are smooth manifolds, construct a $C ^ { \infty }$ atlas on the product $M \times N$ (thus $M \times N$ has the structure of a smooth manifold).

(b) Let M be a Hausdorff space, and suppose that we can write $M = U \cup V$ where U and V are open sets, and both U and V are smooth manifolds. Since $U \cap V$ is an open subset of $U ,$ it inherits a differentiable structure from $U ;$ likewise $U \cap V$ inherits a differentiable structure from V. Assume that these two differentiable structures on $U \cap V$ are the same. Prove that one can then construct a smooth structure on M such that the inclusions $U \to M$ and $V  M$ are both smooth maps.

(c) Prove that for any g the compact surface of genus $g$ (and no boundary) can be given the structure of a smooth manifold (Hint: The case $g = 0$ is covered by Example 3.12, and $g = 1$ follows from Example3.12 and part (a). Now repeatedly use (b) together with the fact that an open subset of a smooth manifold is naturally a smooth manifold.)

Remark 3.16. In our examples we’ve brushed over the question of whether the smooth structures on these spaces are unique. This is an important but difficult question; a fair amount is now known, but the proofs are generally beyond the scope of this course. It’s known that in any dimension $n \leq 3$ , every topological n-manifold has a unique smooth structure; in particular the smooth structures on surfaces from the exercise above are the only possible ones. Things become more complicated beginning in (and especially in) dimension 4: in fact there are uncountably many distinct smooth structures on $\mathbb { R } ^ { 4 }$ , and there are many compact 4-manifolds with infinitely many smooth structures, and none that are currently known to have just one smooth structure (though as mentioned earlier there are some topological 4-manifolds with no smooth structures). For spheres, once $n \geq 7$ there is typically more than one smooth structure on $S ^ { n }$ ; the first “exotic” structure on $S ^ { 7 }$ was a big surprise when it was discovered by Milnor in 1956. It’s still a major open question whether there are any smooth structures on $S ^ { 4 }$ other than the standard one.

We now record a result asserting the existence of partitions of unity subordinate to covers of smooth manifolds:

Theorem 3.17. Let M be a smooth manifold and let $\{ V _ { \alpha } | \alpha \ \in \ A \}$ be a collection of open subsets of M with $\cup _ { \alpha \in A } V _ { \alpha } = M$ . Then there is a smooth partition of unity on M subordinate to the cover $\{ V _ { \alpha } \}$ , i.e., a collection $\{ \chi _ { \alpha } | \alpha \in A \}$ where

• Each $\chi _ { \alpha } \in C ^ { \infty } ( M )$ , with $0 \leq \chi _ { \alpha } ( x ) \leq 1$ for all x ∈ M

• For all $\alpha , s u p p ( \chi _ { \alpha } ) \subset V _ { a }$

• For any x ∈ M there is a neighborhood $O _ { x }$ of x such that $O _ { x } \cap s u p p ( \chi _ { \alpha } ) = \emptyset$ for all but finitely many α

$\begin{array} { r } { \sum _ { \alpha } \chi _ { \alpha } = 1 } \end{array}$

Proof. The special case in which M is an open subset of $\mathbb { R } ^ { n }$ was proven as Theorem 2.6. That proof carries over directly to the more general case now that we have the appropriate definitions. Indeed, a smooth manifold M is by definition second-countable and Hausdorff, and is certainly locally compact (any point has a neighborhood whose closure is homeomorphic to a closed ball in $\mathbb { R } ^ { n }$ and so is compact), so Lemma 2.9 applies to produce a sequence of compact sets $K _ { i }$ and open sets $H _ { i }$ . These sets can then be used just as they are used in the proof of Theorem 2.6. Basically all that needs to be changed is the first paragraph of that proof: if $x \in K _ { i }$ we can find a neighborhood of $x$ having the form $\phi ^ { - 1 } ( B _ { 2 r _ { x } } ( \phi ( x ) ) ;$ ) which is contained in $V _ { \alpha _ { \mathrm { r } } } \cap W _ { i }$ for some $\alpha _ { x } ,$ , where $\phi \colon { \cal U }  \mathbb { R } ^ { n }$ is some chart (depending on x) whose domain $U$ contains x. The sets $\phi ^ { - 1 } ( B _ { r _ { x } } ( x ) )$ then cover $K _ { i } ,$ and this cover has a finite subcover. Aggregating these finite subcovers gives a countable sequence $\{ B _ { k } \}$ of open sets covering M; the $B _ { k }$ are preimages of balls in $\mathbb { R } ^ { n }$ by local charts φ, and where $\tilde { B } _ { k }$ is the preimage of the ball with the same center and twice the radius we will have $B _ { k } \subset V _ { \alpha _ { k } } \cap W _ { i _ { k } }$ for appropriate $\alpha _ { k } , i _ { k }$ . Moreover there is a smooth function $\psi _ { k }$ supported in $\tilde { B } _ { k }$ and identically equal to one on $B _ { k }$ —just precompose an appropriate smooth function on $\mathbb { R } ^ { n }$ given by Corollary 2.5 with $\phi ^ { - 1 }$ . The proof of Theorem 2.6 then applies verbatim. 

Partitions of unity are very useful in the study of smooth manifolds. For a brief indication of why, consider the case in which the cover $\{ V _ { \alpha } \}$ consists of the domains of coordinate charts $\phi _ { \alpha } \colon \ : V _ { \alpha } \to \mathbb { R } ^ { n }$ (of course, by definition, any smooth manifold admits such a cover). If ${ \bf \Sigma } ^ { \prime } \in C ^ { \infty } ( M )$ , then we can write

$$
f = \left( \sum _ { \alpha } \chi _ { \alpha } \right) f = \sum _ { \alpha } ( \chi _ { \alpha } f ) .
$$

Now for any α the function $\chi _ { \alpha f }$ is supported in the set $V _ { \alpha }$ , which is identified by $\phi _ { \alpha }$ with an open subset in $\mathbb { R } ^ { n }$ So we can hope to analyze f by decomposing it as a sum of smooth functions $\chi _ { \alpha } f .$ , where each of these smooth functions can (at least individually) be treated as though it were just a compactly supported smooth function on $\mathbb { R } ^ { n }$ . To get slightly ahead of myself, the same applies when f is, instead of a smooth function, a differential form.

3.1. Tangent spaces. If M is a smooth manifold and $m \in M$ , we will define a vector space $T _ { m } M$ called the tangent space to M at m. As suggested at the start of these notes, there are various ways of trying to do this, any of which can be considered to be inspired by the special case in which M is an open subset of $\mathbb { R } ^ { n }$ . For instance we could define a tangent vector v at m to be an equivalence class [γ] where $\gamma \colon ( - \epsilon , \epsilon ) \to M$ is a $C ^ { \infty }$ map from an open interval around 0 to M with $\gamma ( 0 ) = m$ , with two curves $\gamma _ { 1 } , \gamma _ { 2 }$ considered to be equivalent if $\begin{array} { r } { \frac { d } { d t } ( \phi _ { \alpha } \circ \gamma _ { 1 } ) ( 0 ) = \frac { d } { d t } ( \phi _ { \alpha } \circ \gamma _ { 1 } ) ( 0 ) } \end{array}$ (as vectors in $\mathbb { R } ^ { n } )$ for one (and hence every—why?) chart $\phi _ { \alpha } \colon { \cal U } _ { \alpha } \to \mathbb { R } ^ { n }$ whose domain contains m. However, for definiteness we will adopt the third interpretation from the start of the notes: a tangent vector at m will be, by definition, a derivation from the algebra of germs of smooth functions defined near m to R.

So just as earlier we consider pairs $( f , V )$ where V is an open neighborhood of m in M and $f \colon \ : V \to \mathbb { R } \mathrm { i s } \ : C ^ { \infty }$ (this notion is well-defined since $V ,$ being an open set in a smooth manifold, is itself a smooth manifold, and we have defined the space of $C ^ { \infty }$ functions on a smooth manifold). Say that $( f _ { 1 } , V _ { 1 } ) \sim ( f _ { 2 } , V _ { 2 } )$ if and only if there is an open set W with m $\in W \subset V _ { 1 } \cap V _ { 2 }$ and $f _ { 1 } | _ { W } = f _ { 2 } | _ { W }$ . Let $O _ { m }$ denote the set of equivalence classes; this inherits addition, multiplication, and scalar multiplication from $C ^ { \infty } ( M )$ (for example, $[ f , V ] [ g , W ] = [ f g , V \cap W ] )$ .

Definition 3.18. $T _ { m } M$ is defined as the space of derivations v: $O _ { m } \to \mathbb { R } ,$ i.e., maps v such that

• v(c f + g) = cv( f ) + v(g) if c ∈ R and f , g ∈ Op

$$
\bullet \ \nu ( f g ) = f ( m ) \nu ( g ) + g ( m ) \nu ( f ) \ i f f , g \in O _ { m }
$$

As indicated in the above definition we will often abuse notation slightly by just writing f for $[ f , V ]$ . Compatibly with this abuse of notation, if φ : $M \to N$ is a smooth map where N is another smooth manifold and m ∈ $M ,$ if we write $f$ for an element $[ f , V ] \in O _ { \phi ( m ) }$ (thus f is a function defined on a neighborhood of $f ( m )$ in $N ) .$ , then we will write f ◦ φ for the element $[ f \circ \phi , \phi ^ { - 1 } ( V ) ] \in O _ { m }$ . These sorts of abuse of notation are justified by the fact that replacing the open set V by a different neighborhood of φ(m) will not change either the element [ f, V] (denoted $f )$ or the element $[ f \circ \phi , \phi ^ { - 1 } ( V ) ]$ (denoted $f \circ \phi )$ .

We record here the fact that, if $U \subset M$ is an open subset and m $\in U$ , there is a canonical identification of $T _ { m } U$ with $T _ { m } M$ (convince yourself of this if it’s not obvious). Also, in case U is an open subset of $\mathbb { R } ^ { n }$ , our definition coincides with the one from the start of these notes.

Definition 3.19. If φ : M → N is a smooth map between smooth manifolds and if $m \in M ,$ , the derivative of $\phi$ at m (sometimes called the linearization of φ at m is the map

$$
\phi _ { * } \colon T _ { m } M \to T _ { \phi ( m ) } N
$$

defined by

$$
( \phi _ { * } ( \nu ) ) ( f ) = \nu ( f \circ \phi )
$$

whenever $f \in O _ { \phi ( m ) }$ and $\nu \in T _ { m } M .$

Sometimes it’s helpful to indicate m within the notation for $\phi _ { * }$ , in which case we’ll write $( \phi _ { * } ) _ { m }$ . One also sees the notation dφ or $d _ { m } \phi$ used to denote what we have called $\phi _ { * }$ .

Proposition 3.20. Where $1 _ { M }$ is the identity map then for all m $\in M , ( 1 _ { M } ) _ { * } \colon T _ { m } M \to T _ { m } M$ is the identity map. Also, $i f \phi \colon M \to N$ and ψ : $N  P$ are smooth maps then

$$
( \psi \circ \phi ) _ { * } = \psi _ { * } \circ \phi _ { * }
$$

Proof. The first statement (about the identity) is obvious from the definition. For the second, we have, if $f \in$ $O _ { \psi \circ \phi ( m ) }$ ,

$$
\begin{array} { r } { ( ( \psi \circ \phi ) _ { \ast } \nu ) ( f ) = \nu ( f \circ ( \psi \circ \phi ) ) = \nu ( ( f \circ \psi ) \circ \phi ) = ( \phi _ { \ast } \nu ) ( f \circ \psi ) = ( \psi _ { \ast } \phi _ { \ast } \nu ) ( f ) . } \end{array}
$$

Corollary 3.21. If m ∈ M where M is a smooth n-manifold, then dim $T _ { m } M = n .$

Proof. We can choose a coordinate chart φ : $U \to \phi ( U )$ where U is an open neighborhood of m. As noted earlier we have $T _ { m } M = T _ { m } U .$ . By Proposition $3 . 2 0 , ( \phi ^ { - 1 } ) _ { * } \circ \phi _ { * } = ( \phi ^ { - 1 } \circ \phi )$ ∗ is the identity map from $T _ { m } U = T _ { m } M$ to itself, and $\phi _ { * } \circ ( \phi ^ { - 1 } ) _ { * } = ( \phi \circ \phi ^ { - 1 } )$ ∗ is the identity map from $T _ { \phi ( m ) } \phi ( U )$ to itself. Thus $\phi _ { * }$ is an isomorphism of vector spaces from $T _ { m } M$ to $T _ { \phi ( m ) } \phi ( U )$ , with inverse $( \phi ^ { - 1 } ) _ { * }$ . We showed in Section 1 that, since $\phi ( U )$ is an open subset of $\mathbb { R } ^ { n }$ , dim $T _ { \phi ( m ) } \phi ( U ) = n .$ , so the conclusion follows. 

Expanding a bit on the above proof, recall that we showed that $T _ { \phi ( m ) } \phi ( U )$ consists precisely of maps $O _ { \phi ( m ) } \to \mathbb { R }$ taking the form $\begin{array} { r } { g \mapsto \sum _ { i = 1 } ^ { n } \nu _ { i } \frac { \partial g } { \partial x _ { i } } \big | _ { \phi ( m ) } } \end{array}$ . So since $( \phi ^ { - 1 } )$ ∗ is an isomorphism, we conclude that, in the presence of a chosen coordinate chart φ : $U \overset { \cdot } { \to } \mathbb { R } ^ { n }$ around $m ,$ a general element $\nu \in T _ { m } M$ will be given by the formula

$$
\nu ( f ) = \sum _ { i = 1 } ^ { n } \nu _ { i } \frac { \partial } { \partial x _ { i } } ( f \circ \phi ^ { - 1 } ) | _ { \phi ( m ) } .
$$

When this is the case, we will say something along the lines of, $^ { 6 6 } \nu$ is given in the coordinate chart $\phi$ by $\textstyle \nu = \sum \nu _ { i } { \frac { \partial } { \partial x _ { i } } } . ^ { \prime \prime } \operatorname { O f }$ course, the coefficients $\nu _ { i }$ will depend on the coordinate chart, not just on the tangent vector v.

Exercise 3.22. Let $\phi , \psi \colon { U } \to \mathbb { R } ^ { n }$ be two coordinate charts where U is an open subset of a smooth manifold $M ,$ and let $m \in U$ . If v is given in the coordinate chart $\phi$ by $\begin{array} { r } { \nu = \sum \nu _ { i } \frac { \partial } { \partial x _ { i } } } \end{array}$ , and is given in the coordinate chart ψ by $\begin{array} { r } { \nu = \sum w _ { i } \frac { \partial } { \partial y _ { i } } } \end{array}$ , find, with proof, an expression for the $w _ { i }$ in terms of the vi and the maps $\phi \circ \psi ^ { - 1 }$ and/or $\psi \circ \phi ^ { - 1 }$

So if M is a smooth n-manifold, we have associated to every point $m \in M$ an n-dimensional vector space $T _ { m } M$ . A diffeomorphism $\phi \colon M \to M ^ { \prime }$ induces an isomorphism of vector spaces $\phi _ { * } \colon T _ { m } M \to T _ { \phi ( m ) } M ^ { \prime }$ . However there is (in general) no canonical way of identifying $T _ { m _ { 1 } } M$ with $T _ { m _ { 2 } } M$ for distinct point $m _ { 1 } , m _ { 2 } \in M$ (of course, since the two vector spaces have the same dimension, they are isomorphic as vector spaces, just not canonically so).

Relatedly, while choosing the point $m \in M$ canonically determines the n-dimensional vector space $T _ { m } M ,$ it does not canonically determine a basis for this vector space. One way of choosing a basis for $T _ { m } M$ is suggested above: choose a local coordinate chart φ : $U \to \mathbb { R } ^ { n }$ around $U ;$ then a basis is given by the derivations $\textstyle f \mapsto { \frac { \partial } { \partial x _ { i } } } ( f \circ$ $\phi ^ { - 1 } ) ( p )$ for $i = 1 , \ldots , n$ (the members of this basis are typically denoted by $\frac { \partial } { \partial x _ { i } }$ . Different choices of coordinate chart of course give rise to different bases; the relationship between the bases is determined by Exercise 3.22.

The tangent bundle of a smooth manifold is, as a set, defined to be the union

$$
T M = \cup _ { m \in M } \{ m \} \times M .
$$

For any subset $S \in M$ (typically S will be open or closed) we define the “restriction of the tangent bundle to $S ^ { \prime \prime }$ as

$$
T M | _ { S } = \cup _ { m \in S } \{ m \} \times T _ { m } M .
$$

Given a coordinate chart $\phi \colon { \cal U }  \mathbb { R } ^ { n }$ where $U \subset M$ is open, we have a bijection Φ: $T M \vert _ { U }  \phi ( U ) \times \mathbb { R } ^ { n }$ given by

$$
\Phi \left( m , \sum \nu _ { i } \frac { \partial } { \partial x _ { i } } \right) = ( \phi ( m ) , \nu _ { 1 } , \ldots , \nu _ { n } ) .
$$

We can then define a topology on $^ { T M }$ by requiring that each of these bijections be homeomorphisms—more precisely, we take as a base for this topology the collection of subsets of the form Φ $^ { - 1 } ( V )$ where Φ : $T M \vert _ { U } $ $\phi ( U ) \times \mathbb { R } ^ { n }$ is a map as above constructed from a coordinate chart $\phi$ and $V \subset \phi ( U ) \times \mathbb { R } ^ { n }$ is open.

The various homeomorphisms Φ: $T M \vert _ { U }  \phi ( U ) \times \mathbb { R } ^ { n }$ associated to coordinate charts $\phi \colon { U } \to \phi ( { U } )$ in fact form a $C ^ { \infty }$ atlas for T M. Indeed the domains $T M | _ { U }$ certainly cover T M (since M is covered by coordinate charts) and so we just need to check that the transition functions are smooth. This latter fact follows from Exercise 3.22. Indeed, if $\phi _ { \alpha } \colon { U } _ { \alpha } \to \mathbb { R } ^ { n }$ and $\phi _ { \beta } \colon { U } _ { \beta } \colon { U } _ { \beta } \to { \mathbb { R } } ^ { n }$ are two coordinate charts, then it should follow from your computation in Exercise 3.22 that the transition function

$$
\Phi _ { \beta } \circ \Phi _ { \alpha } ^ { - 1 } \colon \phi _ { \alpha } ( U _ { \alpha } \cap U _ { \beta } ) \times { \mathbb { R } } ^ { n } \to \phi _ { \beta } ( U _ { \alpha } \cap U _ { \beta } ) \times { \mathbb { R } } ^ { n }
$$

is given by

$$
\Phi _ { \beta } \circ \Phi _ { \alpha } ^ { - 1 } ( x , \vec { \nu } ) = ( \phi _ { \beta } \circ \phi _ { \alpha } ^ { - 1 } ( x ) , g _ { \alpha \beta } ( x ) \vec { \nu } )\tag{4}
$$

where $g _ { \alpha \beta }$ is a certain smooth function which takes values in the group of invertible $n \times n$ matrices. Thus the transition functions are smooth, and so determine a smooth manifold structure on $T M$

Of course, we have a projection π : $T M  M$ which sends $( m , \nu )$ to m. In terms of the local coordinate charts Φ on T M and φ on M, π just acts by the projection of $\phi ( U ) \times \mathbb { R } ^ { n }$ onto its first factor; thus π is a smooth map.

Summing up, out of an n-dimensional smooth manifold M we have constructed a 2n-dimensional smooth manifold T M, equipped with a projection π : $T M  M$ . The “fibers” $\pi ^ { - 1 } ( \{ m \} )$ of π are canonically identified with the tangent spaces $T _ { m } M ,$ and thus are n-dimensional vector spaces. Moreover there is an atlas on T M such that the transition functions respect the vector space structures on the fibers in the sense that they are given by a formula of the shape (4) where each $g _ { \alpha \beta } ( x )$ is a linear map. T M is thus an example of what is called a vector bundle; we will see more examples of vector bundles as the course proceeds.

## 3.2. Vector fields. Consistently with what was done in Section 1, we make the following definition:

Definition 3.23. Let M be a smooth manifold and $U \subset M$ an open subset. A vector field on U is a derivation $X \colon C ^ { \infty } ( U ) \to C ^ { \infty } ( U ) ( { \mathrm { i . e . , } }$ X obeys $X ( c f + g ) = c X f + X g$ and $X ( f g ) = f X g + g X f i f f , g \in C ^ { \infty } ( U ) , c \in \mathbb { R } )$ . We denote the space of vector fields on U by $\chi ( U )$

Just as in Section 1, we can scalar multiply, add, and take the commutators of derivations from $C ^ { \infty } ( U )$ to itself, so $\chi ( U )$ naturally has the structure of a Lie algebra.

A vector field on U should have another interpretation as a “smoothly-varying” choice of tangent vector at m for each $m \in M$ . We now lay out how this works. For $U \subset M$ we have a (restricted) tangent bundle π : $T M \vert _ { U }  U$

Definition 3.24. A smooth section of T M over U is a smooth map s : $U  T M | _ { U }$ such that π ◦ s is the identity.   
We write Γ(U, T M) for the space of smooth sections of T M over U.

In other words, $s ( m ) \in T _ { m } U$ for all $p \in U ;$ the notion that the tangent vectors should vary smoothly is encoded in the requirement that s should be a smooth map. Since $T _ { m } U$ is a vector space, we get vector space operations on $\Gamma ( U , T M )$ defined by $( c s ) ( m ) = c ( s ( m ) )$ and $( s _ { 1 } + s _ { 2 } ) ( m ) = s _ { 1 } ( m ) + s _ { 2 } ( m )$ (there’s something to show here, namely that for instance the sum of two smooth sections is still smooth, but it’s not hard to check this). One important example of a section of T M (or more generally of any vector bundle) is the zero section, defined by $s ( m ) = 0 \in T _ { m } M$ for all $p .$ (To see that this is smooth, just note that in the local coordinates $\phi ( U ) \times \mathbb { R } ^ { n } \subset \mathbb { R } ^ { 2 n }$ described earlier the map is given by $x \mapsto ( x , 0 )$ which is obviously a smooth map from $\mathbb { R } ^ { n }$ to R2n).

Recall Exercise 2.11, to which the following gives a solution:

Proposition 3.25. Let M be a smooth manifold, $U \subset M$ open, $m \in U ,$ and $X \in { \mathcal { X } } ( U )$ . Then the following prescription uniquely specifies an element $X _ { m } \in  { T _ { m } } M$ . For any $[ f , V ] \in O _ { m } ,$ choose a ${ \tilde { f } } \in C ^ { \infty } ( U )$ such that $[ \tilde { f } , U ] = [ f , V ] ,$ , and define $X _ { m } ( [ f , V ] ) = ( X \tilde { f } ) ( m )$

Proof. First of all we need to show that for any $[ f , V ] \in O _ { m }$ (in other words, V is an open set around m and f is a smooth function on V) there is a smooth function $\tilde { f }$ defined throughout U and coinciding on with $f$ on some neighborhood G of m. To see this, note that we can find a coordinate chart $\phi \colon ~ W \to ~ \mathbb { R } ^ { n }$ around m and $r > 0$ so that $\overline { { \phi ^ { - 1 } ( B _ { 2 r } ( \phi ( m ) ) ) } } \subset V .$ Take a partition of unity $\{ \chi _ { 1 } , \chi _ { 2 } \}$ subordinate to the open cover $\{ \phi ^ { - 1 } ( B _ { 2 r } ( \phi ( m ) ) ) , M \setminus \overline { { \phi ^ { - 1 } ( B _ { r } ( \phi ( m ) ) ) } } \}$ of M. Then let ${ \tilde { f } } = \chi _ { 1 } f ;$ initially this function is only defined on $V ,$ but since it has support contained in a compact subset of V we may extend it by zero to obtain a smooth function on all of M. Since $\chi _ { 1 } + \chi _ { 2 } = 1$ and $\chi _ { 2 }$ vanishes on $\phi ^ { - 1 } ( B _ { r } ( \phi ( m ) ) ) , \tilde { f }$ coincides with $f$ on $\phi ^ { - 1 } ( B _ { r } ( \phi ( m ) ) )$ , as desired.

We now show that the value $( X { \tilde { f } } ) ( m )$ is independent of the choice of $\tilde { f }$ with $[ \tilde { f } , U ] = [ f , V ]$ . If $\tilde { g }$ is another such choice, there is a neighborhood W of m such that $\tilde { f } | _ { W } = \tilde { g } | _ { W }$ . Let $o$ be a neighborhood of m such that $m \in \overline { { O } } \subset W$ (for instance take $o$ to be the preimage of a small ball in a coordinate chart, as in the previous paragraph). Just as in the previous paragraph we can find a smooth function χ: $M \to \mathbb { R }$ such that $\chi | _ { \cal O } = 1$ and $s u p p ( \chi ) \subset W$ . Let $\beta = 1 - \chi$ , so $\beta$ vanishes identically on the neighborhood $o$ of m and is equal to 1 outside $W$ Hence

$$
( 1 - \beta ^ { 2 } ) \tilde { f } = ( 1 - \beta ^ { 2 } ) \tilde { g }
$$

(both sides are zero everywhere that $\tilde { f } \neq \tilde { g } )$ . On the other hand

$$
\left( X ( \beta ^ { 2 } \tilde { f } ) \right) ( m ) = \beta ( m ) \left( X ( \beta \tilde { f } ) \right) ( m ) + \beta ( m ) \tilde { f } ( m ) \left( X \beta \right) ( m ) = 0
$$

and similarly

$$
\left( X ( \beta ^ { 2 } \tilde { g } ) \right) ( m ) = 0 .
$$

Hence

$$
\begin{array} { r l } & { ( X \tilde { f } ) ( m ) = \left( X ( \beta ^ { 2 } \tilde { f } ) \right) ( m ) + \left( X ( ( 1 - \beta ^ { 2 } ) \tilde { f } ) \right) ( m ) } \\ & { \qquad = \left( X ( ( 1 - \beta ^ { 2 } ) \tilde { f } ) \right) ( m ) = \left( X ( ( 1 - \beta ^ { 2 } ) \tilde { g } ) \right) ( m ) } \\ & { \qquad = \left( X ( \beta ^ { 2 } \tilde { g } ) \right) ( m ) + \left( X ( ( 1 - \beta ^ { 2 } ) \tilde { g } ) \right) ( m ) = ( X \tilde { g } ) ( m ) . } \end{array}
$$

This confirms that the prescription of the proposition gives a well-defined map $X _ { m } \colon O _ { m } \to \mathbb { R }$ . It remains to check that $X _ { m }$ is a derivation. But this follows easily from the derivation property for X. Given $[ f , V ] , [ g , W ] \in$ $O _ { m } .$ , if we use ${ \tilde { f } } \in C ^ { \infty } ( U )$ to compute $X _ { m } [ f , V ] = ( X \tilde { f } ) ( m )$ and ${ \tilde { g } } \in C ^ { \infty } ( U )$ to compute $X _ { m } [ g , V ] = ( X \tilde { g } ) ( m )$ then we can use $\widetilde { f g } = \widetilde { f } \widetilde { g }$ to compute $X _ { m } ( [ f , V ] [ g , W ] )$ (of course we could make other choices for $f g ,$ , but the start of the proof ensures that this would result in the same value for $X _ { m } ( [ f , V ] [ g , W ] ) )$ ). Then the derivation property for X shows

$$
\begin{array} { c l l } { { X _ { m } ( [ f , V ] [ g , W ] ) = \left( X ( \widetilde { f g } ) \right) ( m ) = f ( m ) ( X \tilde { g } ) ( m ) + g ( m ) ( X \tilde { f } ) ( m ) } } \\ { { { } } } & { { { } } } \\ { { { } = f ( m ) X _ { m } [ g , W ] + g ( m ) X _ { m } [ f , V ] . } } \end{array}
$$

R-linearity is proved in essentially the same way, completing the proof that $X _ { m } \in T _ { m } M .$

We now show that giving a vector field (in the sense of a derivation on the space of smooth functions) is exactly the same as giving a smooth section of the tangent bundle.

Theorem 3.26. Let U be an open subset of the smooth manifold M. A bijection $\mathcal { F } \colon X ( U )  \Gamma ( U , T M )$ may be defined as follows. For $X \in { \mathcal { X } } ( U )$ , set ${ \mathcal { F } } ( X )$ equal to the map $s _ { X } \colon { \cal M } \to T M$ defined by $s _ { X } ( m ) = X _ { m }$ (where $X _ { m }$ is given by Proposition 3.25).

Proof. First we need to show that $\mathcal { F }$ is well-defined—we certainly have a well-defined function $s _ { X } \colon { \cal M } \to T M$ for any $X \in { \mathcal { X } } ( U )$ , and $s _ { X }$ is a section in the sense that $\pi \circ s _ { X } = 1 _ { M }$ , but we also need to check that $s _ { X }$ is smooth in order for $\mathcal { F }$ to take values in the space $\Gamma ( U , T M )$ of smooth sections.

To see this, note first of all that a function $f$ between two smooth manifolds is smooth if and only if the domain can be covered by open sets to each of which f restricts as a smooth function. If m $\in M ,$ let $\phi \colon { \cal V }  \mathbb { R } ^ { n }$ be a coordinate chart with $m \in V \subset U$ , and for $r > 0$ small enough that $B _ { 2 r } ( \phi ( m ) ) \subset \phi ( V )$ let $W _ { m } = \phi ^ { - 1 } ( B _ { r } ( \phi ( m ) ) )$ . We will show that $s _ { X } | _ { W _ { m } }$ is smooth, which suffices since any point in M has a neighborhood of the form $W _ { m } .$

In this direction, let $\chi \colon M \to \mathbb { R }$ be a smooth function with $\chi | _ { \overline { { W _ { m } } } } = 1$ and $s u p p ( \chi ) \subset V$ . For any $q \in W _ { m }$ and $f \in O _ { q }$ we have

$$
( s _ { X } ( q ) ) ( f ) = X _ { q } ( f ) = X _ { q } ( \chi f )
$$

since $f$ and $\chi f$ coincide on a neighborhood (namely $W _ { m } )$ of $q .$

Now for each $j = 1 , \dotsc , n$ write $g _ { j } = ( x _ { j } \circ \psi ) \cdot \chi \in C ^ { \infty } ( M )$ . Then on $W _ { m } , g$ coincides with the jth coordinate of the chart $\psi | _ { W _ { m } } \colon W _ { m } \to \mathbb { R } ^ { n }$ . We know that, for each $q \in W _ { m } .$ , since $X _ { q } \in T _ { q } M$ we can express $X _ { q }$ in the coordinate chart $\psi$ as $\begin{array} { r } { X _ { q } = \sum _ { i } \nu _ { i } ( q ) \frac { \partial } { \partial x _ { i } } | _ { q } } \end{array}$ for some $\nu _ { i } ( q ) \in \mathbb { R }$ . Evaluating on the functions $g _ { j }$ we see that, for each $j ,$

$$
\nu _ { j } ( q ) = ( X g _ { j } ) ( q ) .
$$

Thus the functions $\nu _ { j } \colon W _ { m } \to \mathbb { R }$ are each smooth. Now in terms of the local coordinates for the tangent bundle described at the end of the previous subsection, the map $s _ { X }$ is given within $W _ { m }$ by the formula (where $x \in$ $\psi ( W _ { m } ) \subset \mathbb { R } ^ { n } )$

$$
x \mapsto \left( x , \nu _ { 1 } ( \psi ^ { - 1 } ( x ) ) , \ldots , \nu _ { n } ( \psi ^ { - 1 } ( x ) ) \right) .
$$

This map is smooth since the $\nu _ { j }$ are smooth. Thus $s _ { X } | _ { W _ { m } }$ is smooth, and so $s _ { X }$ is smooth since U can be covered by open sets of the form $W _ { m } .$

Now that we have shown the map $\mathcal { F } \colon \chi ( U )  \Gamma ( U , T M )$ to be well-defined, we show that it is bijective. Suppose that $X , Y \in { \mathcal { X } } ( U )$ are two distinct vector fields on U. Then there is $f \in C ^ { \infty } ( U )$ and $m \in U$ such that $( X f ) ( m ) \neq ( Y f ) ( m )$ . But then $[ f , U ]$ is a well-defined element of $O _ { m }$ with $X _ { m } ( [ f , U ] ) \neq Y _ { m } ( [ f , U ] )$ , and thus $X _ { m } \neq Y _ { m } , i . e . s _ { X } ( m ) \neq s _ { Y } ( m )$ . Thus F is injective.

Finally suppose that $s \in \Gamma ( U , T M )$ ; we must find $X \in { \mathcal { X } } ( U )$ so that $s _ { X } = s . \ \mathrm { I f } \ f \in C ^ { \infty } ( U )$ then for all m we have an element $[ f , U ] \in O _ { m }$ and so a real number $( s ( m ) ) ( [ f , U ] )$ . This determines a function $X f \colon U  \mathbb { R }$ by the formula $( X f ) ( m ) = ( s ( m ) ) ( [ f , U ] )$ . The derivation properties $X ( c f + g ) = c X f + X g$ and $X ( f g ) = f X g + g X f$ follow directly from the fact that each s(m) is a derivation from $O _ { m }$ to R; however we still need to check that $X f \in C ^ { \infty } ( U )$ ) for any $f \in C ^ { \infty } ( U )$ . In a local coordinate chart $\psi \colon \textit { V } \to \mathbb { R } ^ { n }$ , the tangent vectors s(m) for $m \in V$ are represented as $\begin{array} { r } { s ( m ) = \sum \nu _ { i } ( m ) \frac { \partial } { \partial x _ { i } } } \end{array}$ , where the functions $\nu _ { i }$ are $C ^ { \infty }$ by the fact that s is a smooth map. But then $\begin{array} { r } { X f | _ { V } = \sum \nu _ { i } \frac { \partial f } { \partial x _ { i } } } \end{array}$ , which is a smooth function. Thus $X f$ restricts to each coordinate chart as a smooth function, and so is smooth. It is clear from the definition that $s _ { X } = s ,$ 

So we have two equivalent characterizations of vector fields on M: as derivations $C ^ { \infty } \to \mathbb { C } ^ { \infty }$ , and as smooth sections $M \to T M$ (which in coordinate charts can be locally expressed in the form $\textstyle \sum \nu _ { i } { \frac { \partial } { \partial x _ { i } } }$ for suitable smooth functions vi). Both characterizations are often useful.

## 4. Differential forms

As the title of the course textbook suggests, a very important role will be played in the rest of the course by what are called the differential forms on a smooth manifold. If M is a smooth n-manifold, we will develop the notion of $\mathbf { a } \ { } ^ {  } p { \mathrm { - } } \mathrm { f o r m } ^ { \prime \prime }$ on M for $p = 0 , 1 , \ldots , n$ (and also for $p > n ,$ , but for algebraic reasons it turns out that the only $p \mathrm { - }$ -forms with $p > n$ will be zero). These p-forms will form a vector space $\Omega ^ { p } ( M )$ , and we will have a very important map d, called the exterior derivative, which maps the space of all differential forms to itself and restricts for each p to a map d : $\Omega ^ { p } ( M ) \to \Omega ^ { p + 1 } ( M )$

To ease into this, let’s start with $p = 0$ and $p = 1$

Definition 4.1. A 0-form on M is a smooth function $f \colon M \to \mathbb { R } .$ In other words $\Omega ^ { 0 } ( M ) = C ^ { \infty } ( M )$

The case of 1-forms is a bit more interesting. First we introduce the notion of the cotangent space:

Definition 4.2. • If M is a smooth manifold and m $\in M ,$ , the cotangent space at m, denoted by $T _ { m } ^ { * } M ,$ , is the dual space to the tangent space $T _ { m } M .$

• The cotangent bundle of M is

$$
T ^ { * } M = \cup _ { m \in M } \{ m \} \times T _ { m } ^ { * } M .
$$

In other words, $T _ { m } ^ { * } M$ consists of linear functionals $\alpha \colon T _ { m } M \to \mathbb { R } .$ . Since a vector space and its dual have the same dimension, if M is an n-manifold then dim $T _ { \upsilon } ^ { * } M = n$ for all $m \in M$

Definition 4.2 identifies the cotangent bundle ${ \dot { T } } ^ { * } M$ as a set. One can equip it with a topology and then with a smooth manifold structure, in such a way that the projection π : $T ^ { * } M \to M$ (sending $( m , \alpha )$ to m if α $\in T _ { m } ^ { * } M )$

makes $T ^ { * } M$ into a vector bundle, just like the situation with the tangent bundle. At least for now we won’t really need to use this fact, but note that we have (at least at a set-theoretic level) the notion of a section s : $M \to T ^ { * } M$ , i.e. a function $s \colon M \to T ^ { * } M$ such that π ◦ $s = 1 _ { M } .$ . A section s : $M \to T ^ { * } M$ associates to each $m \in M$ an element $s _ { m } \in T _ { p } ^ { * } M$

Definition 4.3. A differential 1-form on a smooth manifold M is a section α: $M \to T ^ { * } M$ which satisfies the following smoothness property: Whenever $X \in { \mathcal { X } } ( M )$ is a vector field on M, the function

$$
\alpha ( X ) \colon m \mapsto \alpha _ { m } ( X _ { m } )
$$

is a $C ^ { \infty }$ function on M. We denote by $\Omega ^ { 1 } ( M )$ the vector space of differential 1-forms.

To unpack the above, note that the section α of the cotangent bundle determines covectors $\alpha _ { m } \in T _ { m } ^ { * } M$ for all $m ,$ while the vector field X (which by Theorem 3.26) is equivalent to a section of the tangent bundle, determines for each m a tangent vector $X _ { m } \in T _ { m } M$ . Hence we can evaluate $\alpha _ { m } ( { \cal X } _ { m } )$ , and the smoothness requirement on α is that (as long as X is smooth) the result of this evaluation varies smoothly with m. If we had gone ahead and put a smooth manifold structure on $T ^ { * } M$ it turns out that this would be equivalent to requiring $\alpha \colon M \to T ^ { * } M$ to be a smooth map.

As mentioned earlier, for all $p$ we will define a map d : $\Omega ^ { p } ( M )  \Omega ^ { p + 1 } ( M )$ . I can now fulfill this promise for $p = 0$ . Actually if one thinks of tangent vectors as derivations the definition may seem strangely simple:

To any $f \in \Omega ^ { 0 } ( M ) , i . e .$ , any smooth function $f ,$ , we are to associate a section $d f \colon M \to T ^ { * } M$ . In other words for each m we should obtain $( d f ) _ { m } \colon T _ { m } M \to \mathbb { R }$ . Well, bearing in mind that an element of $T _ { m } M$ is a derivation from functions defined near m to R, we use the formula

$$
( d f ) _ { m } ( \nu ) = \nu ( f ) \quad \mathrm { i f } \ \nu \in T _ { m } M .\tag{5}
$$

Suppose now that φ: $U \to \mathbb { R } ^ { n }$ is a coordinate chart, where $U \subset M$ is open. Now U is a smooth manifold in its own right, so we can consider $\Omega ^ { 1 } ( U )$ . The coordinate chart $\phi$ distinguishes some special smooth functions on $U ,$ namely the coordinate functions $x _ { 1 } , \ldots , x _ { n }$ (perhaps we should really write $x _ { 1 } \circ \phi , \ldots , x _ { n } \circ \phi$ , or we could just agree that the decomposition of φ into coordinates is given by $\phi ( m ) = ( x _ { 1 } ( m ) , \ldots , x _ { n } ( m ) ) )$ . Since the $x _ { i }$ are smooth functions (i.e., 0-forms) on $U ,$ , we obtain 1-forms $d x _ { 1 } , \ldots , d x _ { n } \in \Omega ^ { 1 } ( U )$ . So for each $m \in U$ we have covectors $( d x _ { i } ) _ { m } \in T _ { m } ^ { * } U = T _ { m } ^ { * } M$

On the other hand, recall that the tangent space $T _ { m } M$ at m has basis given by $\frac { \partial } { \partial x _ { 1 } } | _ { m } , \ldots , \frac { \partial } { \partial x _ { n } } | ,$ m. We have

$$
( d x _ { i } ) _ { m } \left( \frac { \partial } { \partial x _ { j } } | _ { m } \right) = \frac { \partial } { \partial x _ { j } } ( x _ { i } ) = \delta _ { i j } .
$$

Thus the $( d x _ { i } ) _ { m }$ form a dual basis to the cotangent space $T _ { m } ^ { * } M$ with respect to the basis $\left\{ \frac { \partial \mathbf { \Phi } } { \partial x _ { i } } | _ { m } \right\}$ for $T _ { p } M$ Since the $( d x _ { i } ) _ { m }$ form a basis for $T _ { m } ^ { * } M$ at all $m ,$ it follows that any 1-form $\alpha \in \Omega ^ { 1 } ( U )$ can be written as

$$
\alpha = \sum _ { i = 1 } ^ { n } \alpha _ { i } d x _ { i }
$$

for some functions $\alpha _ { i } \in C ^ { \infty } ( U )$ (which may be recovered by evaluating α on $\textstyle { \frac { \partial } { \partial x _ { i } } } )$

Exercise 4.4. Suppose that we have two different coordinate charts

$$
\phi \colon \ m \mapsto ( x _ { 1 } ( m ) , \ldots , x _ { n } ( m ) ) \quad { \mathrm { a n d } } \quad \psi \colon \ m \mapsto ( y _ { 1 } ( m ) , \ldots , y _ { n } ( m ) )
$$

each with domain given by some open subset U of a smooth manifold. If $\alpha \in \Omega ^ { 1 } ( U )$ can be written as

$$
\alpha = \sum _ { i = 1 } ^ { n } \alpha _ { i } d x _ { i } = \sum _ { i = 1 } ^ { n } \beta _ { i } d y _ { i }
$$

find a general formula (in terms of the derivatives of $\phi \circ \psi ^ { - 1 }$ and/or $\psi \circ \phi ^ { - 1 } )$ for the relationship between the coefficients $\alpha _ { i }$ and $\beta _ { i }$The above exercise is designed to be compared to Exercise 3.22. A single coordinate chart around m produces distinguished bases $\left\{ \frac { \partial \phantom { x _ { i } } } { \partial x _ { i } } | _ { m } \right\}$ for $T _ { m } M$ and $\{ ( d x _ { i } ) _ { m } \}$ for $T _ { m } ^ { * } M$ , allowing one to parametrize $T _ { m } M$ or $T _ { m } ^ { * } M$ by $\mathbb { R } ^ { n }$ Changing the coordinate chart changes the appropriate parametrization for either $T _ { m } M$ or $T _ { m } ^ { * } M ,$ , and you should have found that the way in which the parametrization transforms under a coordinate change is different for $T _ { m } M$ than it is for $T _ { m } ^ { * } M$ . This reflects the fact that vector fields and 1-forms really are fundamentally different kinds of objects.

If $( x _ { 1 } , . . . , x _ { n } ) \colon U \to \mathbb { R } ^ { n }$ is a coordinate patch and $m \in U ,$ , we see that

$$
d f _ { m } \left( \frac { \partial } { \partial x _ { i } } \right) = \frac { \partial f } { \partial x _ { i } } ( m ) = \left( \sum _ { j = 1 } ^ { n } \frac { \partial f } { \partial x _ { j } } ( d x _ { j } ) _ { m } \right) \left( \frac { \partial } { \partial x _ { i } } \right) ,
$$

and thus, throughout the coordinate chart U, we have

$$
d f = \sum _ { j = 1 } ^ { n } { \frac { \partial f } { \partial x _ { j } } } d x _ { j } .\tag{6}
$$

In principle we could also have defined d : $\Omega ^ { 0 } ( M )  \Omega ^ { 1 } ( M )$ by saying that if $f \in \Omega ^ { 0 } ( M )$ has support in a coordinate chart then $d f$ is given by formula (6), and requiring that d be linear over R—this would determine $d f$ for any f (not necessarily supported in a coordinate chart) since by using a partition of unity we can write an arbitrary function as a sum of functions each of which is supported in a coordinate chart. (Of course, with this approach one would need to make sure that $d f$ didn’t depend on the way in which $f$ is decomposed as such a sum—our more natural and coordinate-free definition of d evades this issue).

Having defined the map d : $\Omega ^ { 0 } ( M ) \to \Omega ^ { 1 } ( M )$ , one could ask whether it is surjective. A little thought should convince you that the answer must be no (if dim $M \ \geq \ 2 )$ —indeed this may be familiar from multivariable calculus. Consider just a 1-form α which is supported in a coordinate chart $U ,$ so in coordinates $\alpha | _ { U } = \textstyle \sum _ { i }$ αidxi for some smooth functions $\alpha _ { i }$ supported in $U ,$ and α vanishes elsewhere. Evidently if $\alpha = d f$ then, on $U ,$ we would have $\begin{array} { r } { \alpha _ { i } = \frac { \partial f } { \partial x _ { i } } } \end{array}$ . Since $f$ is assumed $C ^ { \infty }$ , its mixed partials are equal and so if we had $\alpha = d f$ we would need $\begin{array} { r } { \frac { \partial \alpha _ { i } } { \partial x _ { j } } = \frac { \partial \alpha _ { j } } { \partial x _ { i } } } \end{array}$ for all $i , j ,$ and of course these equations have no reason to hold for a general collection of smooth functions $\alpha _ { i }$ supported in $U .$

Thus we obtain an obstruction to a 1-form α being in the image of d, which in local coordinates can be seen as coming from the partial derivatives of the various components of α. If α is in the image of d it is called exact. Once we define the space of 2-forms $\Omega ^ { 2 } ( M )$ and the exterior derivative d : $\Omega ^ { 1 } ( M )  \Omega ^ { 2 } ( M )$ , we will see that the above obstruction vanishes in the sense that the relevant partial derivatives coincide if and only if $d \alpha = 0$ Indeed, $d \circ d \colon \Omega ^ { 0 } ( M ) \to \Omega ^ { 2 } ( M )$ is zero (as, more generally, is d ◦ d : $\Omega ^ { p } ( M )  \Omega ^ { p + 2 } ( M ) )$ . One can then ask whether every α for which the obstruction vanishes $( d \alpha = 0 )$ is indeed exact. We’ll see that the answer to this question depends on the topology of M (as measured by the de Rham cohomology groups). )

## 4.1. The alternating algebra.

Definition 4.5. Let V be a vector space over R, and let p be a positive integer. An alternating p-form on V is a function η : $V ^ { p } \to \mathbb { R }$ with the following properties:

• η is p-linear: For any i, $i f c \in \mathbb { R }$ and $\nu _ { 1 } , \dots , \nu _ { p } \in V$ and $w _ { i } \in V$ then

$$
\begin{array} { r } { \eta ( \nu _ { 1 } , \dots , \nu _ { i - 1 } , c \nu _ { i } + w _ { i } , \dots , \nu _ { p } ) = c \eta ( \nu _ { 1 } , \dots , \nu _ { i - 1 } , \nu _ { i } , \dots , \nu _ { p } ) + \eta ( \nu _ { 1 } , \dots , \nu _ { i - 1 } , w _ { i } , \dots , \nu _ { p } ) . } \end{array}
$$

• V is antisymmetric: $i f \nu , w \in V$ then, for any $i < j$ and any $u _ { 1 } , \dots , u _ { i - 1 } , u _ { i + 1 } , \dots , u _ { j - 1 } , u _ { j + 1 } , \dots , u _ { p } \in V$

$$
\eta ( u _ { 1 } , \dots , u _ { i - 1 } , \nu , u _ { i + 1 } , \dots , u _ { j - 1 } , w , u _ { j + 1 } , \dots , u _ { p } ) = - \eta ( u _ { 1 } , \dots , u _ { i - 1 } , w , u _ { i + 1 } , \dots , u _ { j - 1 } , \nu , u _ { j + 1 } , \dots , u _ { p } ) .
$$

We will denote the vector space of alternating p-forms on V by $\Lambda ^ { p } V ^ { * }$ . We extend the notation $\Lambda ^ { p } V ^ { * }$ to $p = 0$ by setting $\Lambda ^ { 0 } V ^ { * } = \mathbb { R }$

Implicit in the above is that the alternating p-forms do indeed form a vector space, which should be clear. Our notation $\Lambda ^ { p } V ^ { * }$ reflects a number of algebraic facts, not all of which we will need or use: for any vector space V there is a certain standard vector space $\Lambda ^ { p } V$ (“the pth graded part of the exterior algebra”), and (at least assuming that V is finite-dimensional) what we denote by $\Lambda ^ { p } V ^ { * }$ can be canonically identified both with $( \Lambda ^ { p } V ) ^ { * }$ and with $\Lambda ^ { p } ( V ^ { * } )$ (so our lack of parentheses is in writing $\Lambda ^ { p } V ^ { * }$ is deliberate). There is an obvious identification of $\Lambda ^ { 1 } V ^ { * }$ with $V ^ { * }$

With this definition, there is for all $p , q \ge 0$ a map

$$
\begin{array} { r } { \wedge \colon \Lambda ^ { p } V ^ { * } \times \Lambda ^ { q } V ^ { * } \to \Lambda ^ { p + q } V ^ { * } } \\ { ( \alpha , \beta ) \mapsto \alpha \wedge \beta } \end{array}
$$

called the wedge product, which satisfies various important properties. Let us give the definition gradually. The first interesting case is when $p = q = 1$ : in this case we define the wedge product by, for $\alpha , \beta \in \Lambda ^ { 1 } V ^ { * }$ , and $\nu , w \in V ,$

$$
( \alpha \wedge \beta ) ( \nu , w ) = \alpha ( \nu ) \beta ( w ) - \alpha ( w ) \beta ( \nu ) .
$$

It is not hard to see that, with this definition, $\alpha \wedge \beta$ does indeed belong to $\Lambda ^ { 2 } V ^ { * }$ (the minus sign ensures that the antisymmetry condition holds). We then extend this to the case that $p = 1$ but q is arbitrary by, for $\alpha \in \Lambda ^ { 1 } V ^ { * } , \beta \in$ $\Lambda ^ { q } V ^ { * }$

$$
\begin{array} { l } { ( \alpha \wedge \beta ) ( \nu _ { 1 } , \nu _ { 2 } , \dots , \nu _ { q + 1 } ) = \alpha ( \nu _ { 1 } ) \beta ( \nu _ { 2 } , \dots , \nu _ { q + 1 } ) - \alpha ( \nu _ { 2 } ) \beta ( \nu _ { 1 } , \nu _ { 3 } , \dots , \nu _ { q + 1 } ) } \\ { + \alpha ( \nu _ { 3 } ) \beta ( \nu _ { 1 } , \nu _ { 2 } , \nu _ { 4 } , \dots , \nu _ { q + 1 } ) + \dots + ( - 1 ) ^ { l } \alpha ( \nu _ { q + 1 } ) \beta ( \nu _ { 1 } , \dots , \nu _ { q } ) } \\ { = \displaystyle \sum _ { j = 1 } ^ { q + 1 } ( - 1 ) ^ { j - 1 } \alpha ( \nu _ { j } ) \beta ( \nu _ { 1 } , \dots , \nu _ { j - 1 } , \nu _ { j + 1 } , \dots , \nu _ { q + 1 } ) } \end{array}
$$

We introduce a notation for $\mathrm { \cdots } \mathrm { o m i t t i n g ^ { \prime } }$ inputs into k-forms as we often need to do: instead of writing $\beta ( \nu _ { 1 } , \ldots , \nu _ { j - 1 } , \nu _ { j + 1 } , \ldots , \nu _ { q + 1 } )$ we will write $\beta ( \nu _ { 1 } , \ldots , \hat { \nu _ { j } } , \ldots , \nu _ { q + 1 } ) ;$ ; thus the hat signifies that the $j \mathrm { t h }$ term has been omitted.

We should check that $\alpha \wedge \beta$ as defined above is actually an element of $\Lambda ^ { q + 1 } V ^ { * }$ ∗. It’s fairly obvious from this definition that α ∧ β is $( q + 1 )$ -linear. As for antisymmetry, if we switch $\nu _ { k }$ and $\nu _ { l }$ with $k < l$ then the antisymmetry of $\beta$ shows that all terms in the sum change sign except for those with $j = k , l .$ Meanwhile the kth term changes from $( - 1 ) ^ { k - 1 } \alpha ( \nu _ { k } ) \beta ( \nu _ { 1 } , \dots , \hat { \nu _ { k } } , \dots , \nu _ { l } , \dots , \nu _ { q + 1 } ) \mathrm { ~ t o ~ } ( - 1 ) ^ { k - 1 } \alpha ( \nu _ { l } ) \beta ( \nu _ { 1 } , \dots , \hat { \nu _ { l } } , \dots , \nu _ { k } , \dots , \nu _ { q + 1 } )$ , and the lth term changes from $( - 1 ) ^ { l - 1 } \alpha ( \nu _ { l } ) \beta ( \nu _ { 1 } , \dots , \nu _ { k } , \dots , \hat { \nu } _ { l } , \dots , \nu _ { q + 1 } ) \mathrm { t o } ( - 1 ) ^ { l - 1 } \alpha ( \nu _ { k } ) \beta ( \nu _ { 1 } , \dots , \nu _ { l } , \dots , \hat { \nu _ { k } } , \dots , \nu _ { q + 1 } )$ . I claim that the new lth term is the negative of the old kth term, and vice versa. Indeed to convert the new lth term to something that looks like the old kth term we can “move the vl past $\nu _ { k + 1 } , \ldots , { \nu _ { l - 1 } } ^ { \prime \prime } .$ —in other words we should switch $\nu _ { l }$ with $\nu _ { k + 1 } ,$ then switch $\nu _ { l }$ with $\nu _ { k + 2 }$ , and so on, until we switch vl with $\nu _ { l - 1 }$ . Since $\beta$ is antisymmetric each of these switches produces a factor of −1, and so since there are a total of $l - k - 1$ numbers from $k + 1 \mathrm { t o } l - 1$ the whole procedure produces a factor of $( - 1 ) ^ { l - k - 1 }$ . So the new lth term is equal to $( - 1 ) ^ { l - 1 } ( - 1 ) ^ { l - k - 1 } \alpha ( \nu _ { k } ) \beta ( \nu _ { 1 } , \dots , \hat { \nu _ { k } } , \dots , \nu _ { q + 1 } )$ , which is indeed equal to the negative of the old kth term. Similarly, the new kth term can be equated with the negative of the old lth term by “moving $\nu _ { k } l - k - 1$ slots to the left.” Summing up, switching $\nu _ { k }$ with $\nu _ { l }$ causes all the terms with $j \notin \{ k , l \}$ to change signs, and also causes the sum of the kth and lth terms to change sign. This proves that α $\wedge \beta$ is alternating, so our map $\Lambda ^ { 1 } V ^ { * } \times \Lambda ^ { q } V ^ { * } \to \Lambda ^ { q + 1 } V ^ { * }$ is well-defined.

Finally we extend the definition of the wedge product to general values of $p$ and $q .$ One way of characterizing this extension is that, given our definition for the case $p = 1$ , there turns out to be a unique way of extending the definition to general $p$ so that the operation ∧ will be bilinear and associative (for instance, if $\alpha , \beta \in \Lambda ^ { 1 } V ^ { * }$ , so that α $\wedge \beta \in \Lambda ^ { 2 } V ^ { * }$ , we take the wedge product with $\alpha \wedge \beta$ (on the left) by insisting that $( \alpha \wedge \beta ) \wedge \gamma = \alpha \wedge ( \beta \wedge \gamma )$ for $\gamma \in \mathsf { \Lambda } \Lambda ^ { q } V ^ { * } -$ since we’ve already decided how to take wedge product with 1-forms the right-hand side is well-defined).

Instead of showing that this indirect argument gives a well-defined prescription, we give a formula. Given nonnegative integers $p$ and $q ,$ let $S _ { p , q }$ denote the collection of p-element subsets of $\{ 1 , \ldots , p + q \}$ . Then for

$S \in S _ { p , q }$ let the positive integers $i _ { 1 } ^ { S } < i _ { 2 } ^ { S } < \cdots < i _ { p } ^ { S }$ be the elements of S , and let the positive integers $j _ { 1 } ^ { S } < \ldots < j _ { q } ^ { S }$ be the elements of $\{ 1 , . . . , p + q \} \setminus S$ . Define $\rho _ { S } : \{ 1 , \dotsc , p + q \}  \{ 1 , \dotsc , p + q \}$ by, for $1 \le k \le p , \rho _ { S } ( k ) = i _ { k } ^ { S }$ and for $p + 1 \leq k \leq p + q , \rho _ { S } ( k ) = j _ { k - p } ^ { S }$ . In other words $\rho _ { S }$ is the permutation of $\{ 1 , \ldots , p + q \}$ gotten by writing all the elements of $S$ in increasing order, and then all the elements of $\{ 1 , \ldots , p + q \} \setminus S$ in increasing order. Let $( - ) ^ { S }$ be 1 if the permutation $\rho _ { S }$ is even and −1 if $\rho _ { S }$ is odd. The general formula for the wedge product is then

$$
( \alpha \wedge \beta ) ( \nu _ { 1 } , \dots , \nu _ { p + q } ) = \sum _ { S \in S _ { p , q } } ( - ) ^ { S } \alpha ( \nu _ { i _ { 1 } ^ { S } } , \dots , \nu _ { i _ { p } ^ { S } } ) \beta ( \nu _ { j _ { 1 } ^ { S } } , \dots , \nu _ { j _ { q } ^ { S } } )\tag{7}
$$

In other words, (α $\wedge \beta ) ( \nu _ { 1 } , \ldots , \nu _ { p + q } )$ is gotten by looking at all the different products gotten by plugging in $p$ of the $\nu _ { i }$ into α and q of them into ${ } ^ { \cdot \beta , }$ and summing these up with a naturally associated sign. It’s not hard to see that this coincides with our previous definition in case $p = 1$

To help verify some other properties of the wedge product (in particular the fact that the wedge product of alternating forms is alternating) we rewrite (7) as a sum over all permutations on $p + q$ letters. Let ${ \mathfrak { S } } _ { p + q }$ denote the group of permutations on $p + q$ letters. Identify $\mathfrak { S } _ { p } \times \mathfrak { S } _ { q }$ with a subgroup of ${ \mathfrak { S } } _ { p + q }$ by associating to $( \sigma , \tau ) \in \mathfrak { S } _ { p } \times \mathfrak { S } _ { q }$ with the permutation on $p + q$ letters (still denoted $( \sigma , \tau ) )$ such that $( \sigma , \tau ) ( i ) = \sigma ( i )$ for $1 \leq i \leq p$ and $( \sigma , \tau ) ( p + j ) = p + \tau ( j )$ for $1 \leq j \leq q$ (in other words, σ acts on the first $p$ letters and τ acts on the last $q )$ . Any permutation in $\eta \in \mathfrak { S } _ { p + q }$ can be written uniquely in the form $\eta = \rho _ { S } \circ ( \sigma , \tau )$ where $\rho _ { S }$ is one of the permutations from the previous paragraph: namely, let $S = \{ \eta ( 1 ) , \dots , \eta ( p ) \}$ ; let σ send j to r if $\eta ( j )$ is the rth largest element of S ; and let τ send j to s if $\eta ( p + j )$ is the sth largest element of $S \setminus \{ \eta ( 1 ) , \dots , \eta ( p ) \} . \mathrm { I f } \eta = \rho _ { S } \circ ( \sigma , \tau )$ we see that

$$
\alpha ( \nu _ { \eta ( 1 ) } , \dots , \nu _ { \eta ( p ) } ) = s g n ( \sigma ) \alpha ( \nu _ { \eta ( \sigma ^ { - 1 } ( 1 ) ) } , \dots , \nu _ { \eta ( \sigma ^ { - 1 } ( p ) ) } ) = s g n ( \sigma ) \alpha ( \nu _ { i _ { 1 } ^ { s } } , \dots , \nu _ { i _ { p } ^ { s } } )
$$

where sgn(σ) is one if σ is even and −1 if $\sigma$ is odd, and similarly

$$
\beta ( \nu _ { \eta ( p + 1 ) } , \dots , \nu _ { \eta ( p + q ) } ) = s g n ( \tau ) \beta ( \nu _ { j _ { 1 } ^ { s } } , \dots , \nu _ { j _ { q } ^ { s } } ) .
$$

Now evidently if $\eta = \rho _ { S } \circ ( \sigma , \tau )$ then $s g n ( \eta ) = ( - ) ^ { S } s g n ( \sigma ) s g n ( \tau )$ , and so we deduce

$$
s g n ( \eta ) \alpha ( \nu _ { \eta ( 1 ) } , \dots , \nu _ { \eta ( p ) } ) \beta ( \nu _ { \eta ( p + 1 ) } , \dots , \nu _ { \eta ( p + q ) } ) = ( - ) ^ { S } \alpha ( \nu _ { \iota _ { 1 } ^ { s } } , \dots , \nu _ { \iota _ { p } ^ { s } } ) \beta ( \nu _ { j _ { 1 } ^ { s } } , \dots , \nu _ { j _ { q } ^ { s } } ) \quad { \mathrm { i f ~ } } \eta = \rho _ { S } \circ ( \sigma , \tau ) .
$$

Now as mentioned earlier any $\eta \in \mathfrak { S } _ { p + q }$ can be expressed uniquely as $\rho _ { S } \circ ( \sigma , \tau )$ for some $S , \sigma , \tau ,$ , and so since the pair $( \sigma , \tau )$ varies through the group $\mathfrak { S } _ { p } \times \mathfrak { S } _ { q }$ which has order $p ! q ! .$ , we deduce the following (more symmetric and redundant) version of (7):

$$
( \alpha \wedge \beta ) ( \nu _ { 1 } , \dots , \nu _ { p + q } ) = { \frac { 1 } { p ! q ! } } \sum _ { \eta \in { \mathfrak { S } } _ { p + q } } s g n ( \eta ) \alpha ( \nu _ { \eta ( 1 ) } , \dots , \nu _ { \eta ( p ) } ) \beta ( \nu _ { \eta ( p + 1 ) } , \dots , \nu _ { \eta ( p + q ) } )\tag{8}
$$

From (8) it is not difficult to see that α $\wedge \beta$ (which is obviously $( p + q ) { \mathrm { - l i n e a r } } )$ is antisymmetric and hence is an alternating $( p + q )$ -form: indeed, let $\tau _ { k , l }$ be the transposition which switches letters k and $l ;$ of course any permutation can be written uniquely in the form $\eta \circ \tau _ { k , l } .$ , and so we have

$$
\begin{array}{c} ( \alpha \wedge \beta ) ( \nu _ { 1 } , \dots , \nu _ { p + d } ) = { \frac { 1 } { p ! q ! } } \sum _ { \eta \in { \overline { { z } } } _ { p + q } } s g n ( \eta \circ \tau _ { k , i } ) \alpha ( \nu _ { \eta \circ \tau _ { j , 1 } } ( 1 ) , \dots , \nu _ { \eta \circ \tau _ { k } ( p ) } ) \beta ( \nu _ { \eta \circ \tau _ { i } ( p + 1 ) } , \dots , \nu _ { \eta \circ \tau _ { k } ( p + q ) } )  \\ { = { \frac { 1 } { p ! q ! } } \sum _ { \eta \in { \overline { { z } } } _ { p + q } } ( - 1 ) s g n ( \eta ) \alpha ( \nu _ { \eta ( 1 ) } , \dots , \nu _ { \eta ( p ) } ) \beta ( \nu _ { \eta ( p + 1 ) } , \dots , \nu _ { \eta ( p + q ) } ) { \mathrm { ~ b u t ~ w i t h ~ t h e ~ p l a c e s ~ o f ~ } } \eta ( k ) { \mathrm { ~ a n d ~ } } \eta ( l ) { \mathrm { ~ s w i t c h e d ~ } } } \\ { = - ( \alpha \wedge \beta ) ( \nu _ { 1 } , \dots , \nu _ { k - 1 } , \nu _ { i } , \nu _ { k + 1 } , \dots , \nu _ { i - 1 } , \nu _ { k } , \nu _ { i + 1 } , \dots , \nu _ { p + q } ) . \qquad } \end{array}
$$

This proves that the map $\wedge \colon \Lambda ^ { p } V ^ { * } \times \Lambda ^ { q } V ^ { * } \to \Lambda ^ { p + q } V ^ { * }$ defined by the equivalent formulas (7,8) is well-defined. The definition is still valid when p and/or q is zero (recalling that $\Lambda ^ { 0 } V ^ { * } = \mathbb { R }$ by definition): wedge product with a 0-form is just multiplication by the corresponding number.

We define the algebra of alternating forms on V as the direct sum

$$
\Lambda ^ { * } V ^ { * } = \oplus _ { p = 0 } ^ { \infty } \Lambda ^ { p } V ^ { * } .
$$

This is equipped with the obvious vector space structure, and also with a multiplication operation ∧ induced by extending bilinearly from the above-defined operations $\wedge \colon \Lambda ^ { p } V ^ { * } \times \Lambda ^ { q } V ^ { * } \to \Lambda ^ { p + q } V ^ { * }$

Proposition 4.6. The wedge product obeys:

(a) For α $\ d S ^ { \prime } \in \Lambda ^ { p } V ^ { * } , \beta \in \Lambda ^ { q } V ^ { * } ,$

$$
\beta \wedge \alpha = ( - 1 ) ^ { p q } \alpha \wedge \beta .
$$

(b) For all $\alpha , \beta , \gamma \in \Lambda ^ { * } V ^ { * } ;$

$$
\alpha \wedge ( \beta \wedge \gamma ) = ( \alpha \wedge \beta ) \wedge \gamma .
$$

Proof. (a) Let $\eta _ { p , q } ~ \in ~ \mathfrak { S } _ { p + q }$ be the permutation given by $\eta ( i ) ~ = ~ q + i$ for $1 \ \leq \ i \ \leq \ p$ and $\eta ( j ) = j - p$ for $p + 1 \leq j \leq p + q .$ . Note that $s g n ( \eta _ { p , q } ) = ( - 1 ) ^ { p q } ~ \mathrm { ( w h y ? ) }$ . Any permutation in $\mathfrak { S } _ { p + q }$ can be written uniquely in the form $\eta \circ \eta _ { p , q } .$ , so we have

$$
\alpha \wedge \beta ( \nu _ { 1 } , \dots , \nu _ { p + q } ) = \frac { 1 } { p ! q ! } \sum _ { \eta \in \mathfrak { S } _ { p + q } } s g n ( \eta \circ \eta _ { p , q } ) \alpha ( \nu _ { \eta \circ \eta _ { p , q } ( 1 ) } , \dots , \nu _ { \eta \circ \eta _ { p , q } ( p ) } ) \beta ( \nu _ { \eta \circ \eta _ { p , q } ( p + 1 ) } , \dots , \nu _ { \eta \circ \eta _ { p , q } ( p + q ) } )
$$

proving (a).

(b) Using the bilinearity of ∧ we may assume that, for some $p , q , r ,$ we have $\alpha \in \Lambda ^ { p } V ^ { * } , \beta \in \Lambda ^ { q } V ^ { * }$ , and $\gamma \in \Lambda ^ { r } V ^ { * }$ . Consider ways of writing $\{ 1 , \ldots , p + q + r \}$ as a disjoint union $\{ 1 , . . . , p + q + r \} = S _ { 1 } \coprod S _ { 2 } \coprod S _ { 3 }$ where $\# S _ { 1 } = p , \# S _ { 2 } = q , \# S _ { 3 } = r .$ For any such decomposition, write the elements of $S _ { 1 }$ in increasing order as $a _ { 1 } < \cdots < a _ { p }$ , those of $S _ { 2 }$ as $b _ { 1 } < \dots < b _ { q }$ , and those of $S _ { 3 }$ as $c _ { 1 } < \cdots < c _ { r } .$ . Also let $( - ) ^ { S _ { 1 } S _ { 2 } S _ { 3 } }$ for the sign of the permutation obtained by sending i to ai for $1 \leq i \leq p ,$ to $b _ { i - p }$ for $p + 1 \leq i \leq p + q ,$ and to $c _ { i - p - q }$ for $p + q + 1 \leq i \leq p + q + r .$ Then after repeatedly applying our original formula (7) and unraveling the notation it is easy to check that both

$$
( \alpha \wedge ( \beta \wedge \gamma ) ) ( \nu _ { 1 } , \ldots , \nu _ { p + q + r } ) \quad { \mathrm { a n d } } \quad ( ( \alpha \wedge \beta ) \wedge \gamma ) ( \nu _ { 1 } , \ldots , \nu _ { p + q + r } )
$$

are equal to

$$
\sum _ { S _ { 1 } , S _ { 2 } , S _ { 3 } } ( - ) ^ { S _ { 1 } S _ { 2 } S _ { 3 } } \alpha ( \nu _ { a _ { 1 } } , \ldots , \nu _ { a _ { p } } ) \beta ( \nu _ { b _ { 1 } } , \ldots , \nu _ { b _ { q } } ) \gamma ( \nu _ { c _ { 1 } } , \ldots , \nu _ { c _ { r } } ) .
$$

Of course, one consequence of associativity is that if $\alpha _ { 1 } , \ldots , \alpha _ { m } \in \Lambda ^ { * } V ^ { * }$ we can unambiguously write $\alpha _ { 1 } \wedge \cdot \cdot \cdot \wedge$ $\alpha _ { m }$ . The results of Proposition 4.6 can be summarized as sayingthat $\Lambda ^ { * } V ^ { * }$ is an associative, graded commutative algebra.

We now observe that the exterior algebra behaves nicely under linear maps. Suppose that we have two real vector spaces V, W and a linear map $A \colon V \to W$ . For any $p ,$ we obtain a linear map $A ^ { * } \colon \Lambda ^ { p } W ^ { * } \to \Lambda ^ { p } V ^ { * }$ (called the pullback of A) by setting

$$
( A ^ { * } \alpha ) ( \nu _ { 1 } , \ldots , \nu _ { p } ) = \alpha ( A \nu _ { 1 } , \ldots , A \nu _ { p } ) .
$$

Note that since we don’t assume A to be invertible it is necessary for $A ^ { * } ~ { \mathrm { t o } } ~ { \mathrm { ^ { * } g o } }$ in the opposite direction” to get a well-defined map. Extending by linearity produces a linear map $A ^ { * } \colon \Lambda ^ { * } W ^ { * } \to \Lambda ^ { * } V ^ { * }$ defined on the whole alternating algebra.

Proposition 4.7. $I f A \colon V \to W$ is a linear map and α $\mathcal { B } \in \Lambda ^ { * } W ^ { * }$ then

$$
A ^ { * } ( \alpha \wedge \beta ) = ( A ^ { * } \alpha ) \wedge ( A ^ { * } \beta ) .
$$

Proof. This is an immediate consequence of our formula (7) for the wedge product.

In other words, a linear map A: V → W induces not just a linear map but in fact an algebra homomorphism $\Lambda ^ { * } W ^ { * } \to \Lambda ^ { * } V ^ { * }$ . Looking at how compositions behave, one sees easily that the alternating algebra construction $V \mapsto \Lambda ^ { * } V ^ { * }$ defines a contravariant functor from the category of real vector spaces to the category of real associative graded commutative algebras. (Given what we’ve proven, one just needs to check that $1 _ { V } ^ { * } = 1 _ { \Lambda ^ { * } V ^ { * } }$ and that $( A \circ B ) ^ { * } = B ^ { * } \circ A ^ { * } . )$

In the discussion of alternating forms so far, we have avoided choosing a basis for the vector space V (and we haven’t even assumed that V is finite-dimensional). This has been deliberate, as we intend to apply this with V equal to the tangent space $T _ { m } M$ at a point on a smooth manifold, and as mentioned before although we can impose a basis on $T _ { m } M$ by choosing a coordinate chart around $m ,$ different coordinate charts yield different bases and so there is no canonical choice. However to actually do any computations on a specific vector space one typically does eventually have to choose a basis, and so we now turn to discussing how a basis for V allows one to do calculations in $\Lambda ^ { * } V ^ { * }$

So let V be a real vector space with finite dimension n and basis $\{ e _ { 1 } , \ldots , e _ { n } \}$ . Let $\{ e ^ { 1 } , \ldots , e ^ { n } \}$ denote the dual basis for $V ^ { * } \left( \ s _ { 0 } \ e ^ { i } ( e _ { j } ) = \delta _ { i j } \right)$ , and recall that $V ^ { * }$ is equal to $\Lambda ^ { 1 } V ^ { * }$ , so that the $e ^ { i }$ can be viewed as elements of the alternating algebra $\Lambda ^ { * } V ^ { * }$

Proposition 4.8. Let $\eta \in \Lambda ^ { p } V ^ { * }$ and suppose that for all p-tuples of integers $( i _ { 1 } , \ldots , i _ { p } )$ with $1 \leq i _ { 1 } < \cdots < i _ { p } \leq n$ we have

$$
\eta ( e _ { i _ { 1 } } , \ldots , e _ { i _ { p } } ) = 0 .
$$

Then η = 0.

Proof. Suppose to the contrary that $\eta \ne 0$ . Then we can choose some $\nu _ { 1 } , \dotsc , \nu _ { p } \ \in \ V$ with $\eta ( \nu _ { 1 } , \ldots , \nu _ { p } )$ , 0. Now the $\nu _ { i }$ can be written in the form $\nu \ : = \ : \sum _ { i } \nu _ { j i } e _ { j }$ for some real numbers $\nu _ { j i }$ . Repeatedly using the $p \mathrm { - }$ linearity of η we then find that the nonzero number $\eta ( \nu _ { 1 } , \ldots , \nu _ { p } )$ can be written as a linear combination of the real numbers $\eta ( e _ { j _ { 1 } } , \ldots , e _ { j _ { p } } )$ for various k-tuples $( j _ { 1 } , \ldots , j _ { p } )$ . So the fact that $\eta ( \nu _ { 1 } , \ldots , \nu _ { p } ) \neq 0$ implies that some $\eta ( e _ { j _ { 1 } } , \ldots , e _ { j _ { p } } ) \neq 0$ where $j _ { 1 } , \dotsc , j _ { p } \in \{ 1 , \dotsc , n \}$ . Now if two of the numbers $j _ { i }$ are equal to each other then it follows directly from the antisymmetry property of η that $\eta ( e _ { j _ { 1 } } , \ldots , e _ { j _ { p } } )$ would be zero, so the numbers $j _ { 1 } , \ldots , j _ { p }$ making $\eta ( e _ { j _ { 1 } } , \ldots , e _ { j _ { p } } ) \neq 0$ must all be distinct. But again using the antisymmetry property, any reordering of the numbers $j _ { 1 } , \ldots , j _ { p }$ causes $\eta ( e _ { j _ { 1 } } , \ldots , e _ { j _ { p } } )$ to change only by multiplication by ±1. So if we choose $i _ { 1 } < \cdots < i _ { p }$ to be the result of writing $j _ { 1 } , \ldots , j _ { p }$ (which we know to be distinct) in strictly increasing order it will hold that $\eta ( e _ { i _ { 1 } } , \ldots , e _ { i _ { p } } ) \neq 0$ . This proves (the contrapositive of) the proposition. 

Proposition 4.9. Suppose that $1 \leq p \leq n$ and that $1 \leq i _ { 1 } < \cdots < i _ { p } \leq n$ and $1 \leq j _ { 1 } < \cdots < j _ { p } \leq n$ are two strictly increasing sequences of integers from 1 to n. Then

$$
( e ^ { i _ { 1 } } \wedge \cdot \cdot \cdot \wedge e ^ { i _ { p } } ) ( e _ { j _ { 1 } } , \ldots , e _ { j _ { p } } ) = \left\{ \begin{array} { l l } { { 1 } } & { { \ i f i _ { l } = j _ { l } f o r a l l \ : l } } \\ { { 0 } } & { { \ o t h e r w i s e } } \end{array} \right.
$$

Proof. We can use induction on $p .$ . For $p = 1$ this is just the definition of the dual basis, so assume the result holds for $p$ and consider increasing sequences $i _ { 1 } < \cdots < i _ { p + 1 }$ and $j _ { 1 } < \cdots < j _ { p + 1 }$ . If these sequences are not identical to each other, then there is some r such that $j _ { r } \notin \{ i _ { 1 } , \ldots , i _ { p + 1 } \}$ . We have (usingˆto signify omission)

$$
( e ^ { i _ { 1 } } \wedge \cdot \cdot \cdot \wedge e ^ { i _ { p + 1 } } ) ( e _ { j _ { 1 } } , \dots , e _ { j _ { p + 1 } } ) = \sum _ { s = 1 } ^ { p + 1 } ( - 1 ) ^ { s - 1 } e ^ { i _ { 1 } } ( e _ { j _ { s } } ) ( e ^ { i _ { 2 } } \wedge \cdot \cdot \cdot \wedge e ^ { i _ { p + 1 } } ) ( e _ { j _ { 1 } } , \dots , \widehat { e _ { j _ { s } } } , \dots , e _ { j _ { p + 1 } } ) .\tag{9}
$$

The rth term vanishes because $j _ { r } \neq i _ { 1 }$ , and all of the other terms vanish by the inductive hypothesis because $j _ { r } \notin \{ i _ { 2 } , \ldots , i _ { k + 1 } \}$ . This proves the “otherwise” part of the proposition.

On the other hand if each il coincides with $j _ { l } ,$ then since the il form an increasing sequence it follows from the inductive hypothesis that, in (9), the first term (i.e. the one with $s = 1 )$ equals 1 and all others equal zero. 

Corollary 4.10. $I f I = ( i _ { 1 } , \ldots , i _ { p } )$ is a p-tuple of integers with $1 \leq i _ { 1 } < \cdots < i _ { p } \leq n = \dim V ,$ , and if we write

$$
e ^ { I } = e ^ { i _ { 1 } } \wedge \cdot \cdot \cdot \wedge e ^ { i _ { p } } ,
$$

then the various eI form a basis for $\Lambda ^ { p } V ^ { * }$ . In particular dim $\begin{array} { r } { \Lambda ^ { p } V ^ { * } = { \binom { n } { p } } = \frac { n ! } { p ! ( n - p ) ! } } \end{array}$

Proof. The various $e ^ { I }$ are linearly independent: if some linear combination $\begin{array} { r } { \sum _ { I } c _ { I } e ^ { I } ~ = ~ 0 } \end{array}$ then, for any $J \ =$ $( j _ { 1 } , \ldots , j _ { p } )$ , evaluating both sides on the tuple $( e _ { j _ { 1 } } , \ldots , e _ { j _ { p } } )$ shows that $c _ { J } = 0$ by Proposition 4.9.

To see that the $e ^ { I }$ span $\Lambda ^ { p } V ^ { * }$ , if $\eta \in \Lambda ^ { k } V ^ { * }$ and $I = ( i _ { 1 } , \ldots , i _ { p } )$ is an increasing sequence, let $\eta _ { I } = \eta ( e _ { i _ { 1 } } , \ldots , e _ { i _ { p } } )$ Then by Proposition 4.9 we have

$$
\left( \eta - \sum _ { I } \eta _ { I } e ^ { I } \right) ( e _ { j _ { 1 } } , \dots , e _ { j _ { p } } ) = 0
$$

for all increasing sequences $j _ { 1 } < \cdots < j _ { p }$ . So by Proposition 4.8 it follows that $\begin{array} { r } { \eta = \sum _ { I } \eta _ { I } e ^ { I } } \end{array}$

The statement about dim $\Lambda ^ { p } V ^ { * }$ just follows from counting the number of increasing sequences of p-tuples I drawn from the set $\{ 1 , \ldots , n \}$ , which is evidently the same as the number of p-element subsets of $\{ 1 , \ldots , n \}$ ; which of course is $\binom { n } { p }$

Of course, the formula dim $\Lambda ^ { p } V ^ { * } = { \binom { \dim V } { p } }$ continues to hold for $p = 0$ for trivial reasons. We note in particular that, if dim $V = n , \Lambda ^ { p } V ^ { * }$ is trivial for $p > n ,$ and one-dimensional for $p = n$ . Evidently a generator for the onedimensional vector space $\Lambda ^ { n } V ^ { * }$ is given by $e ^ { 1 } \wedge \ldots \wedge e ^ { n }$ where the $e ^ { i }$ form a dual basis to a basis $\left\{ \boldsymbol { e } _ { i } \right\}$ for v. For some other basis $\{ f _ { i } \}$ the element $f ^ { 1 } \wedge \cdots \wedge f ^ { n }$ will then be a multiple of $e ^ { 1 } \wedge \dots \wedge e ^ { n }$ ; this multiple is given by the determinant of a certain basis change matrix, as you may be able to see from the following exercise:

Exercise 4.11. Let A : $V  V$ be a linear map, where V is an n-dimensional real vector space. We then have an induced map $A ^ { * } \colon \Lambda ^ { n } V ^ { * } \to \Lambda ^ { n } V ^ { * }$ , which is a linear map from a one-dimensional vector space to itself and hence is given by the formula $A ^ { * } x = c _ { A } x$ for all x where $c _ { A }$ is some number depending on A. Prove that $c _ { A } = \operatorname* { d e t } A$ (Hint: Choose a basis in terms of which A has Jordan normal form)

Exercise 4.12. Let V be a finite-dimensional real vector space and let $\alpha \in \Lambda ^ { p } V ^ { * }$ , with $2 \leq p \leq$ dim V. Let us say that α is decomposable if there are $\alpha _ { 1 } , \dotsc , \alpha _ { p } \in \Lambda ^ { 1 } V ^ { * }$ p so that $\alpha = \alpha _ { 1 } \wedge \cdot \cdot \cdot \wedge \alpha _ { p }$

(a) Prove that if α is decomposable then α $\wedge \alpha = 0$

(b) Prove that if dim $V = 2$ or 3 then (for $2 \leq p \leq$ dim V) every $\alpha \in \Lambda ^ { p } V ^ { * }$ is decomposable.

(c) If dim $V \ \geq \ 4$ , construct (with proof, giving an explicit formula) some $\alpha \in \Lambda ^ { 2 } V ^ { * }$ such that α is not decomposable. (Hint: By (a) it is enough to arrange that α $\land \alpha \neq 0 . )$ )

4.2. Higher-degree differential forms. If M is a smooth manifold and $m \in M$ we let $\Lambda ^ { p } T _ { m } ^ { * } M$ denote the space of alternating p-forms on the tangent space $T _ { m } M$ (strictly speaking in the notation of the previous subsection we should instead write $\Lambda ^ { p } T _ { m } M ^ { * }$ , but we do not), and let

$$
\Lambda ^ { p } T ^ { * } M = \cup _ { m \in M } \{ m \} \times \Lambda ^ { p } T _ { m } ^ { * } M .
$$

Thus projection onto the first factor gives a function $\pi \colon \Lambda ^ { p } T ^ { * } M  M$ , and so we can consider the notion of a section $s \colon M \to \Lambda ^ { p } T ^ { * } M ,$ , i.e. a map s obeying $\pi \circ s = 1 _ { M }$ and thus associating to each $m \in M$ an alternating p-form $s _ { m }$ on the tangent space $T _ { m } M$

Definition 4.13. A differential p-form on M is a section η : $M \to \Lambda ^ { p } T ^ { * } M$ obeying the following smoothness property: $I f X _ { 1 } , \ldots , X _ { p }$ are any smooth vector fields on M, then the function

$$
m \mapsto \eta _ { m } \left( ( X _ { 1 } ) _ { m } , \ldots , ( X _ { p } ) _ { m } \right)
$$

is of class $C ^ { \infty }$ . We denote the vector space of differential p-forms on M by $\Omega ^ { p } ( M )$

Note that this coincides with the previous definition for $p = 1$ , recalling the general fact that $\Lambda ^ { 1 } V ^ { * } = V ^ { * }$ . We also earlier defined $\Omega ^ { 0 } ( M )$ to be the space of smooth functions from M to R; since $\Lambda ^ { 0 } V ^ { * } = \mathbb { R }$ this new definition is equivalent (albeit slightly notationally different, but this shouldn’t cause a problem) to the previous one.

Assume that dim $M = n$ Choose a coordinate chart $( x _ { 1 } , . . . , x _ { n } ) \colon U \to \mathbb { R } ^ { n }$ with $m \in U$ . Recall that, for each m $\in \ { M } ,$ , the covectors $( d x _ { 1 } ) _ { m } , \ldots , ( d x _ { n } ) _ { m }$ form a basis for $T _ { m } ^ { * } M ,$ dual to the basis $\left\{ \frac { \partial } { \partial x _ { i } } | _ { m } \right\}$ for $T _ { m } M$ . For $I = ( i _ { 1 } , \ldots , i _ { p } ) \in \{ 1 , \ldots , n \} ^ { p }$ with $i _ { 1 } < \ldots < i _ { p } ,$ write

$$
d x _ { m } ^ { I } = ( d x _ { 1 } ) _ { m } \wedge \cdot \cdot \cdot \wedge ( d x _ { n } ) _ { m } .
$$

According to Corollary 4.10, the various $d x _ { m } ^ { I }$ form a basis for $\Lambda ^ { p } T _ { m } ^ { * } M .$ . Consequently, for any $\eta \in \Omega ^ { p } ( M )$ , for each q in the coordinate patch U we can write

$$
\eta _ { q } = \sum _ { I } f _ { I } ( q ) d x _ { q } ^ { I }
$$

for some functions $f _ { I } \colon \ { U } \to \mathbb { R }$ . Moreover, by evaluating η on tuples of vector fields whose restrictions to U coincide with some of the $\textstyle { \frac { \partial } { \partial x _ { i } } }$ , we see that the functions $f _ { I }$ are smooth. Thus, a differential p-form restricts to a coordinate chart $( U , x _ { 1 } , \ldots , { \dot { x _ { n } } } )$ as an object of the form

$$
\eta | _ { U } = \sum _ { I } f _ { I } d x ^ { I } \mathrm { w h e r e } f _ { I } \in C ^ { \infty } ( U ) .
$$

In less abbreviated notation, we could write

$$
\eta | _ { U } = \sum _ { i _ { 1 } < \cdots < i _ { p } } f _ { i _ { 1 } \cdots i _ { p } } d x _ { i _ { 1 } } \wedge \cdots \wedge d x _ { i _ { p } } .
$$

Having defined the spaces of p-forms $\Omega ^ { p } ( M )$ , we can let $\Omega ^ { * } ( M ) = \oplus _ { p = 0 } ^ { \infty } \Omega ^ { p } ( M )$ ; a differential form on M is then simply an element of $\Omega ^ { * } ( M )$ .

For each $m \in M$ and $p , q \ge 0$ we have a wedge product operation $\wedge \Lambda ^ { p } T _ { m } ^ { * } M \times \Lambda ^ { q } T _ { m } ^ { * } M \to \Lambda ^ { p + q } T _ { m } ^ { * } M .$ . This then induces a wedge product $\Omega ^ { p } ( M ) \times \Omega ^ { q } ( M )  \Omega ^ { p + q } ( M )$ in an obvious way, setting (α $\wedge \beta ) _ { m } = \alpha _ { m } \wedge \beta _ { m }$ . So, extending bilinearly, we get a wedge product $\wedge \colon \Omega ^ { * } ( M ) \times \Omega ^ { * } ( M )  \Omega ^ { * } ( M )$ . In view of Proposition 4.6, the wedge product on differential forms is associative and graded commutative.

We now complete the definition of the exterior derivative d : $\Omega ^ { * } ( M ) \to \Omega ^ { * } ( M )$

Theorem 4.14. There is a unique R-linear map d : $\Omega ^ { * } ( M ) \to \Omega ^ { * } ( M )$ obeying the following properties:

(i) For all p, the restriction $d | _ { \Omega ^ { p } ( M ) }$ has image contained in $\Omega ^ { p + 1 } ( M )$

(ii) $d \vert _ { \Omega ^ { 0 } ( M ) }$ coincides with the map d : $\Omega ^ { 0 } ( M ) \to \Omega ^ { 1 } ( M )$ defined in (5).

(iii) $H \omega \in \Omega ^ { p } ( M )$ and $\phi \in \Omega ^ { q } ( M )$ we have

$$
d ( \omega \wedge \phi ) = ( d \omega ) \wedge \phi + ( - 1 ) ^ { p } \phi \wedge d \omega .
$$

(iv) $d \circ d = 0 .$

For any coordinate chart $\begin{array} { r } { ( x _ { 1 } , \ldots , x _ { n } ) \colon U \to \mathbb { R } ^ { n } , i f \omega | _ { U } = \sum _ { I } f _ { I } d x ^ { I } } \end{array}$ , then

$$
d \omega | _ { U } = \sum _ { j = 1 } ^ { n } \sum _ { I } { \frac { \partial f _ { I } } { \partial x _ { j } } } d x _ { j } \wedge d x ^ { I } .\tag{10}
$$

Proof. We start with the following lemma. Of course, the support supp(η) of a $p \mathrm { . }$ -form η is by definition the closure of the set of $m \in M$ for which $\eta _ { m } \in \Lambda ^ { p } T _ { m } ^ { * } M$ is nonzero.

Lemma 4.15. Assume that the linear map d : $\Omega ^ { * } ( M )  \Omega ^ { * } ( M )$ satisfies properties (i)-(iv) and suppose that $\omega \in \Omega ^ { p } ( M )$ has supp(η) equal to a closed subset of M which is contained in the domain U of a coordinate chart $( x _ { 1 } , \dots , x _ { n } ) \colon U \to \mathbb { R } ^ { n } . \ I f \omega | _ { U } = \sum _ { I } f _ { I } d x ^ { I }$ , then dω has support contained in U and $\begin{array} { r } { d \omega | _ { U } = \sum _ { j = 1 } ^ { n } \sum _ { I } \frac { \partial f _ { I } } { \partial x _ { i } } d x _ { j } \wedge d x ^ { I } . } \end{array}$ The same conclusion continues to hold if we only assume that conditions $( i ) – ( i \nu )$ hold for d when d is restricted to forms whose supports are contained in U.

Proof. Let $\beta \colon M \to \mathbb { R }$ be a smooth function such that $\beta | _ { s u p p ( \omega ) } = 1$ and $s u p p ( \beta ) \subset U$ . Note then that for each i the smooth function $\beta x _ { i } \colon { U }  \mathbb { R } ^ { n }$ has closed support within $U ,$ and therefore extends to a smooth function on all of M by setting it equal to zero outside of $U .$ Also the functions $f _ { I }$ each have support contained in the support of ω (on which $\beta = 1 )$ , so the $f _ { I }$ also extend by zero to smooth functions on all of M, and moreover if $I = ( i _ { 1 } , \ldots , i _ { p } )$ we have (at least on U, where both sides are defined)

$$
f _ { I } d x ^ { I } = f _ { I } d ( \beta x _ { i _ { 1 } } ) \wedge \dots \wedge d ( \beta x _ { i _ { p } } ) .
$$

Thus

$$
\omega = \sum _ { I = ( i _ { 1 } , . . . , i _ { p } ) } f _ { I } d ( \beta x _ { i _ { 1 } } ) \wedge \cdot \cdot \cdot \wedge d ( \beta x _ { i _ { p } } )
$$

(the two sides coincide on $U ,$ and are both zero outside of U).

Now by induction on the integer r it is easy to see from conditions (iii) and (iv) that, for any smooth functions $g _ { 1 } , \ldots , g _ { r }$ we have

$$
d ( d g _ { 1 } \wedge d g _ { 2 } \wedge \cdot \cdot \cdot \wedge d g _ { r } ) = 0 .
$$

Applying this fact together with (iii) again (and the linearity of d) shows that

$$
d \omega = \sum _ { I } d f _ { I } \wedge d ( \beta x _ { i _ { 1 } } ) \wedge \cdot \cdot \cdot \wedge d ( \beta x _ { i _ { p } } ) .
$$

Since $\beta$ is identically 1 on the union of the supports of the $f _ { I }$ (which is contained in U), and since $\begin{array} { r } { d f _ { I } = \sum _ { j } \frac { \partial f _ { I } } { \partial x _ { j } } d x _ { j } } \end{array}$ on $U ,$ the result follows. 

Motivated by this lemma, choose once and for all a cover $\{ U _ { \alpha } \}$ by domains of coordinate charts $( x _ { 1 } ^ { \alpha } , . . . , x _ { n } ^ { \alpha } ) \colon U _ { \alpha } \to$ R, and let $\{ \chi _ { \alpha } \}$ be a partition of unity subordinate to the cover $\{ U _ { \alpha } \}$ . For $I = ( i _ { 1 } , \ldots , i _ { p } )$ let $d x _ { \alpha } ^ { I } = d x _ { i _ { 1 } } ^ { \alpha } \wedge \cdot \cdot \cdot \wedge d x _ { i _ { p } } ^ { \alpha }$

Lemma 4.16. For any α let $\Omega _ { \alpha } ^ { * } ( M )$ denote the space of differential forms on M whose support is contained in α. Define $d _ { \alpha } \colon \Omega _ { \alpha } ^ { * } ( M ) \to \Omega _ { \alpha } ^ { * } ( M )$ by setting, if ω ∈ Ω∗α(M) with $\begin{array} { r } { \omega | _ { U _ { \alpha } } = \sum _ { I } f _ { I } d x _ { \alpha } ^ { I } } \end{array}$

$$
d _ { \alpha } \omega | _ { U _ { \alpha } } = \sum _ { I } d f _ { I } \wedge d x _ { \alpha } ^ { I }
$$

(and $d _ { \alpha } \omega = 0$ outside $U _ { \alpha } ) .$ . Then $d _ { \alpha } \colon \Omega _ { \alpha } ^ { * } ( M ) \to \Omega _ { \alpha } ^ { * } ( M )$ satisfies $( i ) – ( i \nu )$ of Theorem 4.14 when restricted to $\Omega _ { \alpha } ^ { * } ( M )$ , and is the unique such map with these properties.

Proof. Uniqueness is already proven in (the last sentence of) Lemma 4.15, so we just need to check that $( \mathrm { i } ) { - } ( \mathrm { i } \mathrm { v } )$ are satisfied. (i) is obvious, and (ii) is given by Equation 6. The fact that (iii) holds outside of $U _ { \alpha }$ is trivial (both sides are zero); inside of $U _ { \alpha }$ let us write $\begin{array} { r } { \omega | _ { U _ { \alpha } } = \sum _ { I } f _ { I } d x _ { \alpha } ^ { I } } \end{array}$ and $\begin{array} { r } { \phi | _ { U \alpha } = \sum _ { J } g _ { J } d x _ { \alpha } ^ { J } } \end{array}$ (where the multi-indices I have length $p$ and the multi-indices J have length $q )$ . We then have, on $U _ { \alpha }$

$$
\begin{array} { l } { { \displaystyle d _ { \alpha } ( \omega \wedge \phi ) = d _ { \alpha } \left( \sum _ { I , J } f _ { I } g _ { J } d x _ { \alpha } ^ { I } \wedge d x _ { \alpha } ^ { J } \right) = \sum _ { k , I , J } \frac { \partial ( f _ { I } g _ { J } ) } { \partial x _ { k } ^ { \alpha } } d x _ { k } ^ { \alpha } \wedge d x _ { \alpha } ^ { I } \wedge d x _ { \alpha } ^ { J } } } \\ { { \displaystyle ~ = \sum _ { k , I , J } \left( \frac { \partial f _ { I } } { \partial x _ { k } ^ { \alpha } } g _ { J } + f _ { I } \frac { \partial g _ { J } } { \partial x _ { k } ^ { \alpha } } \right) d x _ { k } ^ { \alpha } \wedge d x _ { \alpha } ^ { I } \wedge d x _ { \alpha } ^ { J } } } \\ { { \displaystyle ~ = \sum _ { k , I , J } \left( \frac { \partial f _ { I } } { \partial x _ { k } ^ { \alpha } } d x _ { k } ^ { \alpha } \wedge d x _ { \alpha } ^ { J } \right) \wedge ( g _ { J } d x _ { \alpha } ^ { J } ) + \sum _ { k , I , J } ( - 1 ) ^ { p } ( f _ { I } d x _ { \alpha } ^ { I } ) \wedge \left( \frac { \partial g _ { J } } { \partial x _ { k } ^ { \alpha } } \right) d x _ { k } ^ { \alpha } \wedge d x _ { \alpha } ^ { J } } }  \\ { { \displaystyle ~ = ( d _ { \alpha } \omega ) \wedge \phi + ( - 1 ) ^ { p } \omega \wedge d _ { \alpha } \phi } }  \end{array}
$$

where the $( - 1 ) ^ { p }$ comes from applying Proposition 4.6 (a) to the wedge product $d x _ { k } ^ { \alpha } \wedge d x _ { \alpha } ^ { I }$ . This proves that $d _ { \alpha }$ satisfies (iii). As for (iv), if $\begin{array} { r } { \omega | _ { U _ { \alpha } } = \sum _ { I } f _ { I } d x _ { \alpha } ^ { I } } \end{array}$ , then clearly $d _ { \alpha } ( d _ { \alpha } \omega )$ vanishes outside $U _ { \alpha } ,$ , and on $U _ { \alpha }$ we have

$$
\begin{array} { l } { \displaystyle d _ { \alpha } ( d _ { \alpha } \omega ) = d _ { \alpha } \left( \displaystyle \sum _ { k = 1 } ^ { n } \displaystyle \sum _ { I } \frac { \partial f _ { I } } { \partial x _ { k } ^ { \alpha } } d x _ { k } ^ { \alpha } \wedge d x _ { \alpha } ^ { I } \right) } \\ { = \displaystyle \sum _ { I } \left( \displaystyle \sum _ { l = 1 } ^ { n } \displaystyle \sum _ { k = 1 } ^ { n } \frac { \partial ^ { 2 } f _ { I } } { \partial x _ { l } ^ { \alpha } \partial x _ { k } ^ { \alpha } } d x _ { l } ^ { \alpha } \wedge d x _ { k } ^ { \alpha } \right) \wedge d x _ { \alpha } ^ { I } } \\ { = \displaystyle \sum _ { I } \left( \displaystyle \sum _ { l = 1 } ^ { n } \displaystyle \sum _ { k < l } \left( \frac { \partial ^ { 2 } f _ { I } } { \partial x _ { l } ^ { \alpha } \partial x _ { k } ^ { \alpha } } - \frac { \partial ^ { 2 } f _ { I } } { \partial x _ { k } ^ { \alpha } \partial x _ { l } ^ { \alpha } } \right) d x _ { l } ^ { \alpha } \wedge d x _ { k } ^ { \alpha } \right) \wedge d x _ { \alpha } ^ { I } = 0 } \end{array}
$$

since the mixed partials of the smooth function $f _ { I }$ are equal (of course in the second-to-last equation we’ve switched the indices k and l in the terms that initially had $k > l$ and used the fact that $d x _ { k } ^ { \alpha } \wedge d x _ { l } ^ { \alpha } = - d x _ { l } ^ { \alpha } \wedge d x _ { k } ^ { \alpha } )$ This proves (iv) and so completes the proof of the lemma. 

We now move from these local considerations to prove the global Theorem 4.14. We have fixed a (locally finite) partition of unity $\{ \chi _ { \alpha } \}$ subordinate to a cover $U _ { \alpha }$ . Then if $\omega \in \Omega ^ { * } ( M )$ we have

$$
\omega = \sum _ { \alpha } ( \chi _ { \alpha } \omega ) \quad { \mathrm { ~ w h e r e ~ e a c h ~ } } \quad \chi _ { \alpha } \omega \in \Omega _ { \alpha } ^ { * } ( M ) .
$$

So for each α we have a well-defined differential form $d _ { \alpha } ( \chi _ { \alpha } \omega )$ , whose support is contained in the support of $\chi _ { \alpha }$ (in particular any point in M has a neighborhood meeting the supports of only finitely many of the $d _ { \alpha } ( \chi _ { \alpha } \omega )$ , so the sum $\textstyle \sum _ { \alpha } d _ { \alpha } ( \chi _ { \alpha } \omega )$ is a well-defined differential form). So define

$$
d \omega = \sum _ { \alpha } d _ { \alpha } ( \chi _ { \alpha } \omega ) .
$$

This is clearly R-linear since each of the $d _ { \alpha }$ are, and conditions ${ ( \mathrm { i } ) , ( \mathrm { i i } ) }$ , and (iv) are each also manifestly inherited from the corresponding facts for $d _ { \alpha }$ (together, in the case of (ii), with the fact that the map d : $\Omega ^ { 0 } ( M ) \to \Omega ^ { 1 } ( M )$ defined earlier in (5) is also R-linear). Condition (iii) (the form version of the Leibniz rule) takes just a little more work. For each α let $\psi _ { \alpha }$ be a smooth function which is equal to one on $s u p p ( \chi _ { \alpha } )$ but such that we still have $s u p p ( \psi _ { \alpha } ) \subset U _ { a }$ . If $\omega \in \Omega ^ { p } ( M )$ and $\phi \in \Omega ^ { q } ( M )$ , we have by definition

$$
d ( \omega \wedge \phi ) = \sum _ { \alpha } d _ { \alpha } ( \chi _ { \alpha } ( \omega \wedge \phi ) ) .
$$

Note that $\chi _ { \alpha } ( \omega \wedge \phi ) = ( \chi _ { \alpha } \omega ) \wedge ( \psi _ { \alpha } \phi )$ (both factors of which have support in $U _ { \alpha } )$ , so

$$
d _ { \alpha } ( \chi _ { \alpha } ( \omega \wedge \phi ) ) = d _ { \alpha } ( \chi _ { \alpha } \omega ) \wedge ( \psi _ { \alpha } \phi ) + ( - 1 ) ^ { p } \chi _ { \alpha } \omega \wedge d _ { \alpha } ( \psi _ { \alpha } \phi )
$$

and so (freely using associativity and distributivity of the wedge product, as well as the fact that $\psi _ { \alpha } \phi = \phi$ wherever $d ( \chi _ { \alpha } \omega ) \neq 0 )$

$$
\begin{array} { l } { { d ( \omega \wedge \phi ) = \displaystyle \sum _ { \alpha } d _ { \alpha } ( \chi _ { \alpha } \omega ) \wedge \phi + ( - 1 ) ^ { p } \omega \wedge \left( \displaystyle \sum _ { \alpha } \chi _ { \alpha } d _ { \alpha } ( \psi _ { \alpha } \phi ) \right) } } \\ { { ~ = ( d \omega ) \wedge \phi + ( - 1 ) ^ { p } \omega \wedge \left( \displaystyle \sum _ { \alpha } \chi _ { \alpha } d _ { \alpha } ( \psi _ { \alpha } \phi ) \right) } } \end{array}
$$

So evidently it remains only to show that

$$
\sum _ { \alpha } \chi _ { \alpha } d _ { \alpha } ( \psi _ { \alpha } \phi ) = ^ { ? } d \phi .\tag{11}
$$

Note also that $\chi _ { \alpha } \psi _ { \alpha } = \chi _ { \alpha }$ and $\psi _ { \alpha } d \chi _ { \alpha } = d \chi _ { \alpha } ,$ , so

$$
\begin{array} { l } { { d _ { \alpha } ( \chi _ { \alpha } \phi ) = d _ { \alpha } ( \chi _ { \alpha } \psi _ { \alpha } \phi ) } } \\ { { \qquad = \chi _ { \alpha } d _ { \alpha } ( \psi _ { \alpha } \phi ) + d \chi _ { \alpha } \wedge ( \psi _ { \alpha } \phi ) = \chi _ { \alpha } d _ { \alpha } ( \psi _ { \alpha } \phi ) + d \chi _ { \alpha } \wedge \phi , } } \end{array}
$$

i.e.

$$
\chi _ { \alpha } d _ { \alpha } ( \psi _ { \alpha } \phi ) = d _ { \alpha } ( \chi _ { \alpha } \phi ) - d \chi _ { \alpha } \wedge \phi .
$$

Thus

$$
\begin{array} { r } { \displaystyle \sum _ { \alpha } \chi _ { \alpha } d _ { \alpha } ( \psi _ { \alpha } \phi ) = \sum _ { \alpha } d _ { \alpha } ( \chi _ { \alpha } \phi ) - \sum _ { \alpha } d \chi _ { \alpha } \wedge \phi } \\ { = d \phi - d \displaystyle \left( \sum _ { \alpha } \chi _ { \alpha } \right) \wedge \phi = d \phi } \end{array}
$$

since $\begin{array} { r } { \sum _ { \alpha } d \chi _ { \alpha } = 1 } \end{array}$ and so d $\begin{array} { r } { \left( \sum _ { \alpha } \chi _ { \alpha } \right) = 0 } \end{array}$

This completes the proof that $d ,$ as we have defined it, satisfies the desired properties. The formula (10) given at the end of the theorem for the behavior of $d$ on an arbitrary coordinate chart then follows from Lemma 4.15: If m ∈ U choose a cutoff function $\beta \colon { \cal M }  \mathbb { R }$ equal to 1 on a neighborhood of m and with compact support contained in U; then $\omega = \beta \omega + ( 1 - \beta ) \omega$ and we have $( d ( ( 1 - \beta ) \omega ) ) _ { m } = 0$ while Lemma 4.15 ensures that $( d ( \beta \omega ) ) _ { m }$ is given by evaluating the right-hand side of (10) at m. 

It is not initially obvious that the formula for d given in the proof, namely dω $\begin{array} { r } { = \sum _ { \alpha } d _ { \alpha } ( \chi _ { \alpha } \omega ) } \end{array}$ , would give an answer which is independent of the partition of unity $\{ \chi _ { \alpha } \}$ or of the open cover $\{ U _ { \alpha } \}$ , but the uniqueness part of the theorem implies that this independence property holds.

In practice, one does not calculate dω by choosing a partition of unity; rather one covers the manifold by coordinate charts $U$ and uses the formula (10) to express dω in each of these coordinate charts. Again, it is not initially obvious that, if V is another coordinate chart with $U \cap V = \emptyset$ , the forms obtained by using (10) with reference to the two different coordinate charts would give both give the same answer when restricted to $U \cap V .$ However, the theorem ensures that this is in fact the case (one can also verify this somewhat tediously by a direct computation).

Since $d \circ d = 0$ , we can make the following definition:

Definition 4.17. Let M be a smooth manifold, and p a nonnegative integer. The pth de Rham cohomology of M is the real vector space

$$
H _ { d R } ^ { p } ( M ) = \frac { \ker ( d \colon \Omega ^ { p } ( M ) \to \Omega ^ { p + 1 } ( M ) ) } { I m ( d \colon \Omega ^ { p - 1 } ( M ) \to \Omega ^ { p } ( M ) ) } .
$$

(For the case $p = 0 ,$ , we regard $\Omega ^ { - 1 } ( M )$ as the trivial vector space, so that $H _ { d R } ^ { 0 } ( M ) = \ker ( d \colon \Omega ^ { 0 } ( M )  \Omega ^ { 1 } ( M ) ) . )$

Remark 4.18. A form ω such that $d \omega = 0$ is called closed, and a form ω such that $\omega = d \phi$ for some $\phi$ is called exact. Thus the fact that d $\mathbf { \nabla } ) d = 0$ expresses that every exact form is closed, and the pth de Rham cohomology group measures the extent to which it fails to be true that, conversely, every closed p-form is exact.

I would also like to record a fact which we will make use of shortly, and which basically was proven in the proof of Theorem 4.14:

Proposition 4.19. Let $\omega \in \Omega ^ { p } ( M )$ . Then we can write ω as a locally finite sum ω $\begin{array} { r } { = \sum _ { \gamma } \omega _ { \gamma } \mathrm { ~ ( i . e . ~ } } \end{array}$ ., any point has an open set intersecting only finitely many of the supp(ωγ)) such that each $\omega _ { \gamma }$ is given by

$$
\omega _ { \gamma } = f _ { \gamma } d g _ { 1 , \gamma } \wedge \cdot \cdot \cdot \wedge d g _ { p , \gamma }
$$

for some functions $f _ { \gamma } , g _ { 1 , \gamma } , \dotsc , g _ { p , \gamma } \in C ^ { \infty } ( M )$

Proof. Let $\{ U _ { \alpha } \}$ be an open cover of M by domains of coordinate charts $( x _ { 1 } ^ { \alpha } , \ldots , x _ { n } ^ { \alpha } )$ and $\{ \chi _ { \alpha } \}$ a (locally finite) partition of unity subordinate to $\{ U _ { \alpha } \}$ . We can then write $\begin{array} { r } { \omega = \sum _ { \alpha } ( \chi _ { \alpha } \omega ) } \end{array}$ where each $\chi _ { \alpha } \omega$ is supported in $U _ { \alpha } .$ In turn, it was shown in the proof of Lemma 4.15 that each $\chi _ { \alpha } \omega$ can be written as a finite sum of forms of the desired type $f _ { \alpha , I } d g _ { 1 , \alpha , I } \wedge \cdot \cdot \cdot \wedge d g _ { p , \alpha , I }$ (as I varies over multi-indices $I = ( i _ { 1 } , \ldots , i _ { p } ) )$ , namely one sets $g _ { j , \alpha , I } = \beta x _ { i _ { j } } ^ { \alpha }$ where $\beta$ is a smooth function supported in $U _ { \alpha }$ and equal to 1 on $s u p p ( \chi _ { \alpha } )$ . So by having the index γ vary over pairs $( \alpha , I )$ the result follows.

To get a sense of what the exterior derivative d is measuring, it is instructive to consider the special cases where the smooth manifold is an open subset U of $\mathbb { R } ^ { 2 } \ o r \mathbb { R } ^ { 3 }$ . As mentioned earlier, for any open subset of Rn the degree-zero part of d acts by $\begin{array} { r } { d f = \sum _ { i = 1 } ^ { n } { \frac { \partial f } { \partial x _ { i } } } d x _ { i } } \end{array}$ . So if we use the standard basis of $\mathbb { R } ^ { n }$ to identify vector fields with $\mathrm { 1 - f o r m s } ^ { 2 } .$ , the exterior derivative of a function is essentially its gradient in the sense of multivariable calculus.

For open subsets $U \subset \mathbb { R } ^ { 2 }$ , the only remaining interesting part of d is that acting on 1-forms. A general 1-form on U has the shape

$$
\omega = P ( x , y ) d x + Q ( x , y ) d y
$$

for functions $P , Q \in C ^ { \infty } ( U )$ , and we see that

$$
{ \begin{array} { r l } & { d \omega = { \frac { \partial P } { \partial x } } d x \wedge d x + { \frac { \partial P } { \partial y } } d y \wedge d x + { \frac { \partial Q } { \partial x } } d x \wedge d y + { \frac { \partial Q } { \partial y } } d y \wedge d y } \\ & { \qquad = \left( { \frac { \partial Q } { \partial x } } - { \frac { \partial P } { \partial y } } \right) d x \wedge d y . } \end{array} }
$$

So if we consider ω as corresponding to the vector field with components P, Q, then dω is obtained by multiplying the standard 2-form $d x \wedge d y$ by what is sometimes called the scalar curl of this vector field, $\begin{array} { r } { \frac { \partial Q } { \partial x } - \frac { \partial P } { \partial y } . } \end{array}$ , a function which is probably familiar from Green’s theorem in multivariable calculus.

Moving up a dimension to open subsets $U \subset \mathbb { R } ^ { 3 }$ , a general 1-form on U has the form

$$
\omega = P d x + Q d y + R d z ,
$$

and we find that in this case

$$
d \omega = \left( { \frac { \partial R } { \partial y } } - { \frac { \partial Q } { \partial z } } \right) d y \wedge d z + \left( { \frac { \partial P } { \partial z } } - { \frac { \partial R } { \partial x } } \right) d z \wedge d x + \left( { \frac { \partial Q } { \partial x } } - { \frac { \partial P } { \partial y } } \right) d x \wedge d y .
$$

We see that the three coefficients above are the components of the curl of the vector field $\langle P , Q , R \rangle$

Meanwhile, a general 2-form on $U$ can be written $\eta = P d y \wedge d z + Q d z \wedge d x + R d x \wedge d y$ and so (because we are working in $\mathbb { R } ^ { 3 } )$ also corresponds to a vector field $\langle P , Q , R \rangle$ . We see that

$$
d \eta = \left( { \frac { \partial P } { \partial x } } + { \frac { \partial Q } { \partial y } } + { \frac { \partial R } { \partial z } } \right) d x \wedge d y \wedge d z ,
$$

and recognize the coefficient from multivariable calculus as the divergence of the vector field $\langle P , Q , R \rangle$

Thus in dimension 3 the maps d : $\Omega ^ { 0 } ( U ) \to \Omega ^ { 1 } ( U ) , d \colon \Omega ^ { 1 } ( U ) \to \Omega ^ { 2 } ( U )$ , and d : $\Omega ^ { 2 } ( U ) \to \Omega ^ { 3 } ( U )$ correspond respectively to the gradient, curl, and divergence operators from multivariable calculus. The fact that $d \circ d = 0$ expresses the facts that the curl of a gradient is always zero, and that the divergence of a curl is always zero.

Again for open subsets $U \subset \mathbb { R } ^ { 3 }$ , the first de Rham cohomology group $H _ { d R } ^ { 1 } ( U )$ will be zero if and only if, conversely, every vector field whose curl is equal to zero is in fact the gradient of a function. You probably learned

in multivariable calculus that if U is all of $\mathbb { R } ^ { 3 }$ then this statement holds. However if U is more topologically interesting it may not hold: for example there is the (misleadingly labeled) $\mathbf { \dot { \Omega } } ^ { 6 6 } d \theta ^ { \prime }$ form, given by

$$
d \theta = { \frac { x d y - y d x } { x ^ { 2 } + y ^ { 2 } } }
$$

defined on $U = \{ ( x , y , z ) \in \mathbb { R } ^ { 3 } | x ^ { 2 } + y ^ { 2 } \neq 0 \}$ , which you can verify to be closed, but which (despite the notation) is not exact since it has nonzero integral around closed curves which enclose the z-axis (dθ wants to be the exterior derivative of the polar coordinate θ, but θ is not a well-defined smooth function on U).

Similarly, the second de Rham cohomology group of an open subset $U \subset \mathbb { R } ^ { 3 }$ vanishes if and only if every vector field on U which has divergence equal to zero is in fact the curl of some other vector field. If $U = \mathbb { R } ^ { 3 }$ then this is true (we’ll prove a much more general statement not too long from now), but this statement is false for $U = \mathbb { R } ^ { 3 } \setminus \{ ( 0 , 0 , 0 ) \}$ }. A standard example illustrating this is the form

$$
\eta = { \frac { x d y \wedge d z + y d z \wedge d x + z d x \wedge d y } { ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ) ^ { 3 / 2 } } }
$$

Physically, η corresponds to the electric field on $\mathbb { R } ^ { 3 } \setminus \{ ( 0 , 0 , 0 ) \}$ generated by a point charge located at the origin. The statement that this vector field is not the curl of another vector field can be shown using Stokes’ theorem, by taking the flux integral of the vector field over a sphere around the origin. Later we’ll develop language for this that generalizes such arguments substantially and stays within the realm of differential forms rather than vector fields.

Exercise 4.20. (A coordinate-free formula for d): Let M be a smooth manifold, $\omega \in \Omega ^ { p } ( M )$ , and let $X ^ { ( 0 ) } , \ldots , X ^ { ( p ) }$ be vector fields on M. Prove that

$$
( d \omega ) ( X ^ { ( 0 ) } , \ldots , X ^ { ( p ) } ) = \sum _ { i = 0 } ^ { p } ( - 1 ) ^ { i } X ^ { ( i ) } \left( \omega ( X ^ { ( 0 ) } , \ldots , \widehat { X ^ { ( i ) } } , \ldots , X ^ { ( p ) } ) + \sum _ { i < j } ( - 1 ) ^ { i + j } \omega \left( [ X ^ { ( i ) } , X ^ { ( j ) } ] , X ^ { ( 0 ) } , \ldots , \widehat { X ^ { ( i ) } } , \ldots , \widehat { X ^ { ( j ) } } , \ldots , X ^ { ( p ) } \right) + \ldots \right)
$$

(To clarify the notation, if we have a differential q-form α and vector fields $Y ^ { ( 1 ) } , \ldots , Y ^ { ( q ) }$ , the function

$$
m \mapsto \alpha _ { m } ( Y _ { m } ^ { ( 1 ) } , \ldots , Y _ { m } ^ { ( q ) } )
$$

is a smooth function, which we denote by $\alpha ( Y ^ { ( 1 ) } , \ldots , Y ^ { ( q ) } )$ . In particular since vector fields are derivations on the space of smooth functions, if Z is another vector field we get another smooth function given by $Z \left( \alpha ( Y ^ { ( 1 ) } , \dots , Y ^ { ( q ) } ) \right)$ To do this problem, I would suggest first showing that the value of the function on the right-hand side at a point m is unchanged if some (or all) $\boldsymbol { X } ^ { ( i ) }$ are replaced by another vector field $\bar { X } ^ { ( i ) }$ such that ${ X _ { m } ^ { ( i ) } = \bar { X } _ { m } ^ { ( i ) } }$ , and then proving the result when the $\boldsymbol { X } ^ { ( i ) }$ are (at least on a neighborhood of a given point) equal to standard coordinate vector fields.)

4.3. Pullbacks of differential forms and the naturality of d. Let $\phi \colon { \cal { M } }  N$ be a smooth map between two smooth manifolds. Recall then that for each m ∈ M we have a derivative map $\phi _ { * } \colon T _ { m } M \to T _ { \phi ( m ) } N$ , defined in terms of the derivation formalism by the simple formula

$$
( \phi _ { * } \nu ) ( f ) = \nu ( f \circ \phi )
$$

whenever $f$ is a germ of a $C ^ { \infty }$ function defined near $\phi ( m ) \in N .$ As described just before Proposition 4.7, this induces for all $m \in N$ a pullback operation

$$
\phi ^ { * } \colon \Lambda ^ { p } T _ { \phi ( m ) } ^ { * } N \to \Lambda ^ { p } T _ { m } ^ { * } M
$$

by setting, for $\alpha \in \Lambda ^ { p } T _ { \phi ( m ) } ^ { * } N$ and $\nu _ { 1 } , \ldots , \nu _ { p } \in T _ { m } M$

$$
( \phi ^ { * } \alpha ) ( \nu _ { 1 } , \ldots , \nu _ { p } ) = \alpha ( \phi _ { * } \nu _ { 1 } , \ldots , \phi _ { * } \nu _ { p } ) .
$$

In particular, when $p = 1$ , so that $\Lambda ^ { p } T _ { p } ^ { * } M$ is just the cotangent space $T _ { p } ^ { * } M , \phi ^ { * }$ coincides with the adjoint map to φ∗ from linear algebra.

Theorem 4.21. Let $\phi \colon { \cal M }  N$ be a smooth map and let $\omega \in \Omega ^ { p } ( M )$ be a differential form. Define a section φ∗ω of $\Lambda ^ { p } T ^ { * }$ ∗ M by

$$
( \phi ^ { * } \omega ) _ { m } = \phi ^ { * } ( \omega _ { \phi ( m ) } ) .
$$

Then φ∗ω is a differential form on M, and

$$
d ( \phi ^ { * } \omega ) = \phi ^ { * } ( d \omega ) .\tag{12}
$$

The fact that $\phi ^ { * } \omega$ is a differential form requires proof, since there is a smoothness condition to check. In case $p = 0$ (so that $\omega \in C ^ { \infty } ( M ) ,$ ) the definition above should be read as saying that

$$
\phi ^ { * } \omega : = \omega \circ \phi \quad ( \mathrm { i f } \omega \in \Omega ^ { 0 } ( M ) ) .
$$

Proof. Step 1: We prove the theorem when $p = 0 .$ . Let $h \in \Omega ^ { 0 } ( M ) = C ^ { \infty } ( N )$ be a 0-form. By definition $\phi ^ { * } h = h \circ \phi$ which is certainly a smooth function (i.e. a 0-form) on M since compositions of smooth functions are smooth. For all $\nu \in T _ { m } M$ we have, by the definition of d on 0-forms:

$$
( d ( \phi ^ { * } h ) ) _ { m } ( \nu ) = \nu ( \phi ^ { * } h ) = \nu ( h \circ \phi ) = ( \phi _ { * } \nu ) ( h ) = ( d h ) _ { \phi ( m ) } ( \phi _ { * } \nu ) = ( \phi ^ { * } d h ) _ { m } ( \nu ) .
$$

This confirms that $d ( \phi ^ { * } h ) = \phi ^ { * } d h$ (It also confirms that $\phi ^ { * } d h$ satisfies the smoothness condition required of a 1-form, since $d ( \phi ^ { * } h )$ certainly does so.)

Step 2: We prove the theorem in case $\omega = f d g _ { 1 } \wedge \cdot \cdot \cdot \wedge d g _ { p }$ for some $f , g _ { 1 } , \ldots , g _ { p } \in C ^ { \infty } ( N )$ . In this case, if m $\in M ,$ , we have (using Proposition 4.7 and Step 1)

$$
\begin{array} { r l } & { ( \phi ^ { * } \omega ) _ { m } = f ( \phi ( m ) ) \phi ^ { * } \left( ( d g _ { 1 } ) _ { \phi ( m ) } \wedge \cdot \cdot \cdot \wedge ( d g _ { p } ) _ { \phi ( m ) } \right) } \\ & { \qquad = ( f \circ \phi ) ( m ) \left( ( \phi ^ { * } d g _ { 1 } ) _ { m } \wedge \cdot \cdot \cdot \wedge ( \phi ^ { * } d g _ { p } ) _ { m } \right) } \\ & { \qquad = ( f \circ \phi ) ( m ) \left( d ( g _ { 1 } \circ \phi ) _ { m } \wedge \cdot \cdot \cdot \wedge d ( g _ { p } \circ \phi ) _ { m } \right) , } \end{array}
$$

i.e.

$$
\phi ^ { * } \omega = ( f \circ \phi ) d ( g _ { 1 } \circ \phi ) \wedge \cdots \wedge d ( g _ { p } \circ \phi ) .
$$

Now the space of differential forms is closed under wedge product (as the smoothness condition is easily seen to be preserved), and the zero-form f ◦ φ and the 1-forms $d ( g _ { i } \circ \phi )$ are all differential forms by what we have already done, so this proves that $\phi ^ { * } \omega$ is a differential form. Using the Leibniz rule and the fact that $d ^ { 2 } = 0$ we see that

$$
\begin{array} { r l } & { d ( \phi ^ { * } \omega ) = d \big ( ( f \circ \phi ) d ( g _ { 1 } \circ \phi ) \wedge \dots \wedge d ( g _ { p } \circ \phi ) \big ) } \\ & { \qquad = d ( f \circ \phi ) \wedge d ( g _ { 1 } \circ \phi ) \wedge \dots \wedge d ( g _ { p } \circ \phi ) } \\ & { \qquad = ( \phi ^ { * } d f ) \wedge ( \phi ^ { * } d g _ { 1 } ) \wedge \dots \wedge \phi ^ { * } ( d g _ { p } ) } \\ & { \qquad = \phi ^ { * } \big ( d f \wedge d g _ { 1 } \wedge \dots \wedge d g _ { p } \big ) } \\ & { \qquad = d \big ( f d g _ { 1 } \wedge \dots \wedge d g _ { p } \big ) = d \omega . } \end{array}
$$

Step 3: We prove the result in general. By Proposition 4.19, any differential form $\omega \in \Omega ^ { p } ( N )$ can be written as a locally finite sum of forms of the type considered in Step 2. Now the smoothness condition required of a differential form is preserved under locally finite sums (since the smoothness of a function can be checked by looking at its restriction to each member of an open cover, we can reduce to the case of genuinely finite sums), so using the linearity of $\phi ^ { * }$ it follows that $\phi ^ { * } \omega$ is a differential form. Similarly the R-linearity of d, together with Step 2, implies that $d \phi ^ { * } \omega = \phi ^ { * } d \omega$ 

Corollary 4.22. A smooth map φ : M → N between two smooth manifolds induces by the pullback operation a map $\phi ^ { * } \colon \Omega ^ { * } ( N ) \to \Omega ^ { * } ( M )$ . If ω $\in \Omega ^ { * } ( N )$ is closed, then $\phi ^ { * } \omega \in \Omega ^ { * } ( M )$ is closed, and $i f \omega \in \Omega ^ { * } ( N )$ is exact, then $\phi ^ { * } \omega \in \Omega ^ { * } ( M )$ is exact

Proof. The first sentence has already been proven. If ω is closed, i.e. $d \omega = 0 ,$ then $d ( \phi ^ { * } \omega ) = \phi ^ { * } d \omega = \phi ^ { * } 0 = 0$ . If ω is exact, i.e. $\omega = d \eta$ for some $\eta \in \Omega ^ { * } ( N )$ , then $\phi ^ { * } \omega = \phi ^ { * } d \eta = d ( \phi ^ { * } \eta )$ 

Recall that we have defined the pth de Rham cohomology of a smooth manifold M as the quotient vector space

$$
H _ { d R } ^ { p } ( M ) = \frac { \{ \mathrm { c l o s e d } p \mathrm { - f o r m s } \} } { \{ \mathrm { e x a c t } p \mathrm { - f o r m s } \} } .
$$

If we write $H _ { d R } ^ { * } ( M ) = \oplus _ { p = 0 } ^ { \infty } H _ { d R } ^ { p } ( M )$ , the wedge-product induces a ring structure on $H _ { d R } ^ { * } ( M ) \colon$ if $a \in H _ { d R } ^ { p } ( M )$ and $b \in H _ { d R } ^ { q } ( M )$ , then we can find closed forms $\omega \in \Omega ^ { p } ( M ) , \eta \in \Omega ^ { q } ( M )$ , representing the classes a and b. Then $d ( \omega \wedge \eta ) = ( d \omega ) \wedge \eta + ( - 1 ) ^ { p } \omega \wedge ( d \eta ) = 0 ,$ , so ω ∧ η represents some cohomology class (denoted a ∪ b) in $H _ { d R } ^ { p + q } ( M )$ Moreover this cohomology class is independent of our particular choice of representatives ω and η—for example if we replaced ω by some other form ${ \bar { \omega } } = \omega + d \alpha$ , then

$$
{ \bar { \omega } } \wedge \eta = ( \omega + d \alpha ) \wedge \eta = \omega \wedge \eta + ( d \alpha ) \wedge \eta = \omega \wedge \eta + d ( \alpha \wedge \eta )
$$

(we’ve used that $d \eta = 0 )$ , i.e. the de Rham cohomology class of $\bar { \omega } \wedge \eta$ is the same as that of ω ∧ η (they differ by an exact form).

Using Proposition 4.6, one easily checks that this multiplication on $H _ { d R } ^ { * } ( M )$ (called the cup product) gives $H _ { d R } ^ { * } ( M )$ the structure of an associative, graded commutative R-algebra.

Corollary 4.23. If M and N are smooth manifolds and φ : $M \to N$ is a smooth map, we obtain a homomorphism of graded R-algebras (in particular a ring homomorphism) $\phi ^ { * } \colon H _ { d R } ^ { * } ( N ) \to H _ { d R } ^ { * } ( M )$ by setting $\phi ^ { * } [ \omega ] = [ \phi ^ { * } \omega ] f o r$ any closed form ω on N. If φ is a diffeomorphism then $\phi ^ { * }$ is an isomorphism.

Proof. The first sentence follows directly from various things that we have already done (check this for yourself if it’s not clear). For the second, note that $\phi ^ { * }$ (acting either on forms or on cohomology) satisfies the functoriality conditions $( I d ) ^ { * } = ( I d )$ and $( \phi \circ \psi ) ^ { * } = \psi ^ { * } \circ \phi ^ { * }$ (note the order on the right hand side, reflecting that $\phi ^ { * }$ “goes in the opposite direction” to φ). From this it follows immediately that if $\phi$ is a diffeomorphism then $\phi ^ { * }$ is an isomorphism with inverse $( \phi ^ { - 1 } ) ^ { * }$ 

Exercise 4.24. If M is a smooth manifold, give an explicit formula, in terms of the point-set topology of $M ,$ for the degree-zero de Rham cohomology $H _ { d R } ^ { 0 } ( M )$ . (As a point of convention, since there is no such thing as a (−1)-form, we regard the exact 0-forms on M to consist only of 0.)