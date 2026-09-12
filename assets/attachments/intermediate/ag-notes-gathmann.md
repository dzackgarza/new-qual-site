## Algebraic Geometry Problems

## D. Zack Garza

## Contents

1 Problem Set 1 2   
2 Problem Set 2 7   
3 Problem Set 3 11   
4 Problem Set 4 (Tuesday, October 06) 14   
5 Problem Set 5 (Monday, October 26) 15

Source: Section 1 of Gathmann

## 1 Problem Set 1

Exercise 1.0.1(Gathmann 1.19): Prove that every affine variety $X \subset \mathbb { A } ^ { n } / k$ consisting of only finitely many points can be written as the zero locus of n polynomials.

Hint: Use interpolation. It is useful to assume at first that all points in X have different   
x1-coordinates.   
Solution:   
Let $X = \{ \mathbf { p } _ { 1 } , \cdot \cdot \cdot , \mathbf { p } _ { d } \} = \{ \mathbf { p } _ { j } \} _ { j = 1 } ^ { d }$ , where each $\mathbf { p } _ { j } \in \mathbb { A } ^ { n }$ can be written in coordinates   
$\mathbf { p } _ { j } : = \left[ p _ { j } ^ { 1 } , p _ { j } ^ { 2 } , \cdots , p _ { j } ^ { n } \right] .$   
Remark 1.0.2: Proof idea: for some fixed k with $2 \leq k \leq n$ , consider the pairs $( p _ { j } ^ { 1 } , p _ { j } ^ { k } ) \in \mathbb { A } ^ { 2 }$   
Letting $j$ range over $1 \le j \le$ d yields d points of the form $( x , y ) \in \mathbb { A } ^ { 2 }$ , so construct an   
interpolating polynomial such that $f ( x ) = y$ for each tuple. Then $f ( x ) - y$ vanishes at every   
such tuple.   
Doing this for each k (keeping the first coordinate always of the form $p _ { j } ^ { 1 }$ and letting the second   
coordinate vary) yields $n - 1$ polynomials in $k [ x _ { 1 } , x _ { k } ] \subseteq k [ x _ { 1 } , \cdot \cdot \cdot , \overset { \cdot } { x _ { n } } ]$ , then adding in the   
polynomial $p ( x ) = \prod _ { j } ( x - p _ { j } ^ { 1 } )$ yields a system the vanishes precisely on $\{ \mathbf { p } _ { j } \}$ .   
Claim: Without loss of generality, we can assume all of the first components $\left\{ p _ { j } ^ { 1 } \right\} _ { j = 1 } ^ { d }$ are   
distinct.   
Todo: follows from "rotation of axes"?   
We will use the following fact:   
Theorem 1.0.3(Lagrange).   
Given a set of d points $\{ ( \stackrel { - } { x } _ { i } , y _ { i } ) \} _ { i = 1 } ^ { d }$ with all $x _ { i }$ distinct, there exists a unique polynomial   
of degree d in $f \in k [ x ]$ such that $\tilde { f } ( x _ { i } ) = y _ { i }$ for every i.   
This can be explicitly given by   
$\tilde { f } ( x ) = \sum _ { i = 1 } ^ { d } y _ { i } \left( \prod _ { 0 \leq m \leq d } \left( \frac { x - x _ { m } } { x _ { i } - x _ { m } } \right) \right) .$   
Equivalently, there is a polynomial $f$ defined by $f ( x _ { i } ) = { \tilde { f } } ( x _ { i } ) - y _ { i }$ of degree d whose   
roots are precisely the $x _ { i }$   
Using this theorem, we define a system of n polynomials in the following way:

• Define $f _ { 1 } \in k [ x _ { 1 } ] \subseteq k [ x _ { 1 } , \cdot \cdot \cdot , x _ { n } ]$ by

$$
f _ { 1 } ( x ) = \prod _ { i = 1 } ^ { d } \left( x - p _ { i } ^ { 1 } \right) .
$$

Then the roots of $f _ { 1 }$ are precisely the first components of the points $p .$

• Define $f _ { 2 } \in k [ x _ { 1 } , x _ { 2 } ] \subseteq k [ x _ { 1 } , \cdot \cdot \cdot , x _ { n } ]$ by considering the ordered pairs

$$
\left\{ ( x _ { 1 } , x _ { 2 } ) = ( p _ { j } ^ { 1 } , p _ { j } ^ { 2 } ) \right\} ,
$$

then taking the unique Lagrange interpolating polynomial $\tilde { f } _ { 2 }$ satisfying $\tilde { f } _ { 2 } ( p _ { j } ^ { 1 } ) = p _ { j } ^ { 2 }$ for all $1 \leq j \leq d .$ Then set $f _ { 2 } : = \tilde { f } _ { 2 } ( x _ { 1 } ) - x _ { 2 } \in k [ x _ { 1 } , x _ { 2 } ]$

• Define $f _ { 3 } \in k [ x _ { 1 } , x _ { 3 } ] \subseteq k [ x _ { 1 } , \cdot \cdot \cdot , x _ { n } ]$ by considering the ordered pairs

$$
\left\{ ( x _ { 1 } , x _ { 3 } ) = ( p _ { j } ^ { 1 } , p _ { j } ^ { 3 } ) \right\} ,
$$

then taking the unique Lagrange interpolating polynomial ${ \tilde { f } } _ { 3 }$ satisfying $\tilde { f } _ { 2 } ( p _ { j } ^ { 1 } ) = p _ { j } ^ { 3 }$ for all $1 \leq j \leq d .$ Then set $f _ { 3 } : = \tilde { f } _ { 3 } ( x _ { 1 } ) - x _ { 3 } \in k [ x _ { 1 } , x _ { 3 } ]$

Continuing in this way up to $f _ { n } \in k [ x _ { 1 } , x _ { n } ]$ yields a system of n polynomials.

Proposition 1.0.4.   
V (f1, · · · , fn) = X .

## Proof .

Claim: $X \subseteq V ( f _ { i } )$

This is essentially by construction. Letting $p _ { j } \in X$ be arbitrary, we find that

$$
f _ { 1 } ( p _ { j } ) = \prod _ { i = 1 } ^ { d } \left( p _ { j } ^ { 1 } - p _ { i } ^ { 1 } \right) = ( p _ { j } ^ { 1 } - p _ { j } ^ { 1 } ) \prod _ { \stackrel { i \leq d } { i \geq j } } \left( p _ { j } ^ { 1 } - p _ { i } ^ { 1 } \right) = 0 .
$$

Similarly, for $2 \leq k \leq n$

$$
f _ { k } ( p _ { j } ) = \tilde { f } _ { k } ( p _ { j } ^ { 1 } ) - p _ { j } ^ { k } = 0 ,
$$

which follows from the fact that $\tilde { f } _ { k } ( p _ { j } ^ { 1 } ) = p _ { j } ^ { k }$ for every k and every $j$ by the construction of $\tilde { f } _ { k } .$

Claim: $X ^ { c } \subseteq V ( f _ { i } ) ^ { c } { \mathrm { : } }$

This follows from the fact the polynomials f given by Lagrange interpolation are unique, and thus the roots of $\tilde { f }$ are unique. But if some other point was in $V ( f _ { i } )$ , then one of its coordinates would be another root of some ${ \tilde { f } } .$

## Exercise 1.0.5(Gathmann 1.21): Determine $\sqrt { I }$ for

$$
I : = \Big \langle x _ { 1 } ^ { 3 } - x _ { 2 } ^ { 6 } , x _ { 1 } x _ { 2 } - x _ { 2 } ^ { 3 } \Big \rangle \ \stackrel { \triangledown } { = } \ \mathbb { C } [ x _ { 1 } , x _ { 2 } ] .
$$

## Solution:

For notational purposes, let $\mathcal { T } , \mathcal { V }$ denote the maps in Hilbert’s Nullstellensatz, we then have

$$
( { \mathcal { T } } \circ { \mathcal { V } } ) ( I ) = { \sqrt { I } } .
$$

So we consider $\mathcal { V } ( I ) \subseteq \mathbb { A } ^ { 2 } / \mathbb { C } .$ the vanishing locus of these two polynomials, which yields the system

$$
\left\{ \begin{array} { l l } { x ^ { 3 } - y ^ { 6 } } & { = 0 } \\ { x y - y ^ { 3 } } & { = 0 . } \end{array} \right.
$$

In the second equation, we have $( x - y ^ { 2 } ) y = 0$ , and since $\mathbb { C } [ x , y ]$ is an integral domain, one term must be zero.

1. If $y = 0 ,$ , then $x ^ { 3 } = 0 \implies x = 0$ , and thus $( 0 , 0 ) \in \mathcal { V } ( I )$ , i.e. the origin is contained in this vanishing locus.

2. Otherwise, if $x - y ^ { 2 } = 0$ , then $x = y ^ { 2 }$ , with no further conditions coming from the first equation.

Combining these conditions,

$$
P : = \left\{ ( t ^ { 2 } , t ) \ \Big | \ t \in \mathbb { C } \right\} \subset \mathcal { V } ( I ) .
$$

where $I = \left. x ^ { 3 } - y ^ { 6 } , x y - y ^ { 3 } \right.$

We have $P \overset { \cdot } { = } \mathcal { V } ( I )$ , and so taking the ideal generated by P yields

$$
\left( \mathbb { Z } \circ \mathcal { V } \right) \left( I \right) = \mathbb { Z } ( P ) = \left. y - x ^ { 2 } \right. \in \mathbb { C } [ x , y ]
$$

and thus ${ \sqrt { I } } = \left. y - x ^ { 2 } \right.$

Exercise 1.0.6(Gathmann 1.22): Let $\boldsymbol { X } \subset \mathbb { A } ^ { 3 } / k$ be the union of the three coordinate axes. Compute generators for the ideal I(X) and show that it can not be generated by fewer than 3 elements.

Solution:

Claim:

$$
I ( X ) = \left. x _ { 2 } x _ { 3 } , x _ { 1 } x _ { 3 } , x _ { 1 } x _ { 2 } \right. .
$$

We can write $X = X _ { 1 } \cup X _ { 2 } \cup X _ { 3 }$ , where

• The $x _ { \mathrm { 1 - a x i s } }$ is given by $X _ { 1 } : = V ( x _ { 2 } x _ { 3 } ) \implies I ( X _ { 1 } ) = \langle x _ { 2 } x _ { 3 } \rangle { \mathrm { . } }$

• The x2-axis is given by $X _ { 2 } : = V ( x _ { 1 } x _ { 3 } ) \implies I ( X _ { 2 } ) = \langle x _ { 1 } x _ { 3 } \rangle$

• The x3-axis is given by $X _ { 3 } : = V ( x _ { 1 } x _ { 2 } ) \implies I ( X _ { 3 } ) = \langle x _ { 1 } x _ { 2 } \rangle$

Here we’ve used, for example, that

$$
I ( V ( x _ { 2 } x _ { 3 } ) ) = \sqrt { \langle x _ { 2 } x _ { 3 } \rangle } = \langle x _ { 2 } x _ { 3 } \rangle
$$

by applying the Nullstellensatz and noting that hx2x3i is radical since it is generated by a squarefree monomial.

We then have

$$
\begin{array} { r l } & { I ( X ) = I ( X _ { 1 } \cup X _ { 2 } \cup X _ { 3 } ) } \\ & { \qquad = I ( X _ { 1 } ) \cap I ( X _ { 2 } ) \cap I ( X _ { 3 } ) } \\ & { \qquad = \sqrt { I ( X _ { 1 } ) + I ( X _ { 2 } ) + I ( X _ { 3 } ) } } \\ & { \qquad = \sqrt { \langle x _ { 2 } , x _ { 3 } \rangle + \langle x _ { 1 } x _ { 3 } \rangle + \langle x _ { 1 } x _ { 2 } \rangle } } \\ & { \qquad = \sqrt { \langle x _ { 2 } x _ { 3 } , x _ { 1 } x _ { 3 } , x _ { 1 } x _ { 2 } \rangle } } \\ & { \qquad = \langle x _ { 2 } x _ { 3 } , x _ { 1 } x _ { 3 } , x _ { 1 } x _ { 2 } \rangle , } \end{array}
$$

where in the last equality we’ve again used the fact that an ideal generated by squarefree monomials is radical.

Claim: I(X) can not be generated by 2 or fewer elements.

Let $J : = I ( X )$ and $R : = k [ x _ { 1 } , x _ { 2 } , x _ { 3 } ]$ , and toward a contradiction, suppose $J = \langle r , s \rangle$ . Define $\mathfrak { m } : = \langle x , y , z \rangle$ and a quotient map

$$
\pi : J \to J / { \mathfrak { m } } J
$$

and consider the images $\pi ( r ) , \pi ( s )$

Note that $J / { \mathfrak { m } } J$ is an R/m-module, and since $R / { \mathfrak { m } } \cong k$ , J/mJ is in fact a k-vector space. Since $\pi ( r ) , \pi ( s )$ generate $J / { \mathfrak { m } } J$ as a k-module,

$$
\dim _ { k } J / { \mathfrak { m } } J \leq 2 .
$$

But this is a contradiction, since we can produce 3 k-linearly independent elements in $J / { \mathfrak { m } } J ;$ namely $\pi ( x _ { 1 } x _ { 2 } ) , \pi ( x _ { 1 } x _ { 3 } ) , \pi ( x _ { 2 } x _ { 3 } )$ . Suppose there exist $\alpha _ { i }$ such that

$$
\alpha _ { 1 } \pi ( x _ { 1 } x _ { 2 } ) + \alpha _ { 2 } \pi ( x _ { 1 } x _ { 3 } ) + \alpha _ { 3 } \pi ( x _ { 2 } x _ { 3 } ) = 0 \in J / { \mathfrak { m } } J \iff \alpha _ { 1 } x _ { 1 } x _ { 2 } + \alpha _ { 2 } x _ { 1 } x _ { 3 } + \alpha _ { 3 } x _ { 2 } x _ { 3 } \in { \mathfrak { m } } J ,
$$

But we can then note that

$$
{ \mathfrak { m } } J = \left. x _ { 1 } , x _ { 2 } . x _ { 3 } \right. \left. x _ { 1 } x _ { 2 } , x _ { 1 } x _ { 3 } , x _ { 2 } x _ { 3 } \right. = \left. x _ { 1 } ^ { 2 } x _ { 2 } , x _ { 1 } ^ { 2 } x _ { 3 } , x _ { 1 } x _ { 2 } x _ { 3 } , \cdot \cdot \cdot \right. .
$$

can’t contain any nonzero elements of degree d $< 3 .$ , so no such $\alpha _ { i }$ can exist and these elements are k-linearly independent.

Exercise 1.0.7(Gathmann 1.23: Relative Nullstellensatz): Let $Y \subset \mathbb { A } ^ { n } / k$ be an affine variety and define $A ( Y )$ by the quotient

$$
\pi : k [ x _ { 1 } , \cdots , x _ { n } ]  A ( Y ) : = k [ x _ { 1 } , \cdots , x _ { n } ] / I ( Y ) .
$$

a. Show that $V _ { Y } ( J ) = V ( \pi ^ { - 1 } ( J ) )$ ) for every $J \le A ( Y )$

b. Show that $\pi ^ { - 1 } ( I _ { Y } ( X ) ) = I ( X )$ for every affine subvariety $X \subseteq Y$

c. Using the fact that $I ( V ( J ) ) \subset { \sqrt { J } }$ for every $J \triangleleft k [ x _ { 1 } , \cdot \cdot \cdot , x _ { n } ]$ , deduce that $I _ { Y } ( V _ { Y } ( J ) ) \subset \sqrt { J }$ for every $J \le A ( Y )$

Conclude that there is an inclusion-reversing bijection

$$
\left\{ \begin{array} { c } { { \mathrm { A f f i n e ~ s u b v a r i e t i e s } } smallskip } \\ { { \mathrm { o f } Y } } \end{array} \right\} \longleftrightarrow \ \left\{ \begin{array} { c } { { \mathrm { R a d i c a l ~ i d e a l s } } } \\ { { \mathrm { i n } A ( Y ) } } \end{array} \right\} .
$$

Exercise 1.0.8√ (Extra): Let $J \triangleleft k [ x _ { 1 } , \cdot \cdot \cdot , x _ { n } ]$ be an ideal, and find a counterexample to $I ( V ( J ) ) =$ $\sqrt { J }$ when k is not algebraically closed. when k is not algebraically closed.

```latex
Solution:
Take $J = \left. x ^ { 2 } + 1 \right. \ \triangleleft \mathbb { R } [ x ]$ , noting that J is nontrivial and proper but R is not algebraically
closed. Then $V ( \dot { J } ) \subseteq \mathbb { R }$ is empty, and thus $I ( V ( J ) ) = I ( \emptyset )$
Claim: $I ( V ( J ) ) = \mathbb { R } [ x ] .$
Checking definitions, for any set $X \subset \mathbb { A } ^ { n } / k$ we have
I (X ) = nf ∈ R[x]  ∀x ∈ X, f (x) = 0o
and so we vacuously have
I(∅) = nf ∈ R[x]  ∀x ∈ ∅, f (x) = 0o = {f ∈ R[x]} = R[x].
Claim: $\sqrt { J } \neq \mathbb { R } [ x ]$
This follows from the fact that maximal ideals are radical, and $\mathbb { R } [ x ] / J \cong \mathbb { C }$ being a field implies
that J is maximal. In this case $\sqrt { J } = J \neq \mathbb { R } [ x ]$
That maximal ideals are radical follows from the fact that if $J \le R$ is maximal, we have
$J \subset { \sqrt { J } } \subset R$ which forces ${ \sqrt { J } } = J { \mathrm { ~ o r ~ } } { \sqrt { J } } = R .$
But if ${ \sqrt { J } } = R ,$ , then
1 ∈ J =⇒ 1n ∈ J for some n =⇒ 1 ∈ J =⇒ J = R,
contradicting the assumption that J is maximal and thus proper by definition.
```

## 2 Problem Set 2

Exercise 2.0.1(Gathmann 2.17): Find the irreducible components of

$$
X = V ( x - y z , x z - y ^ { 2 } ) \subset \mathbb { A } ^ { 3 } / \mathbb { C } .
$$

Solution:

Since $x = y z$ for all points in X, we have

$$
\begin{array} { r l } & { X = V ( x - y z , y z ^ { 2 } - y ^ { 2 } ) } \\ & { \quad = V \left( x - y z , y ( z ^ { 2 } - y ) \right) } \\ & { \quad = V ( x - y z , y ) \cup V ( x - y z , z ^ { 2 } - y ) } \\ & { \quad : = X _ { 1 } \cup X _ { 2 } . } \end{array}
$$

Claim: These two subvarieties are irreducible.

It suffices to show that the $A ( X _ { i } )$ are integral domains. We have

$$
A ( X _ { 1 } ) : = \mathbb { C } [ x , y , z ] / \left. x - y z , y \right. \cong \mathbb { C } [ y , z ] / \left. y \right. \cong \mathbb { C } [ z ] ,
$$

which is an integral domain since C is a field and thus an integral domain, and

$$
A ( X _ { 2 } ) : = \mathbb { C } [ x , y , z ] / \left. x - y z , z ^ { 2 } - y \right. \cong \mathbb { C } [ y , z ] / \left. z ^ { 2 } - y \right. \cong \mathbb { C } [ y ] ,
$$

which is an integral domain for the same reason.

Exercise 2.0.2(Gathmann 2.18): Let $X \subset \mathbb { A } ^ { n }$ be an arbitrary subset and show that

$$
V ( I ( X ) ) = { \overline { { X } } } .
$$

Solution:   
${ \overline { { X } } } \subseteq V ( I ( X ) ) { \mathrm { : } }$   
We have $X \ \subseteq \ V ( I ( X ) )$ and since $V ( J )$ is closed in the Zariski topology for any ideal   
$J \triangleleft k [ x _ { 1 } , \cdot \cdot \cdot , x _ { n } ]$ by definition, $V ( I ( X ) )$ is closed. Thus   
$X \subseteq V ( I ( X ) ) { \mathrm { ~ a n d ~ } } V ( I ( X ) ) { \mathrm { ~ c l o s e d ~ } } \implies { \overline { { X } } } \subseteq V ( I ( X ) ) ,$   
since $\overline { { X } }$ is the intersection of all closed sets containing $X .$   
$V ( I ( X ) ) \subseteq { \overline { { X } } } { \mathrm { : } }$   
Noting that $V ( \cdot ) , I ( \cdot )$ are individually order-reversing, we find that $V ( I ( \cdot ) )$ is order-preserving   
and thus   
$X \subseteq { \overline { { X } } } \implies V ( I ( X ) ) \subseteq V ( I ( { \overline { { X } } } ) ) = { \overline { { X } } } ,$   
where in the last equality we’ve used part (i) of the Nullstellensatz: if X is an affine variety,   
then $V ( I ( X ) ) = X$ . This applies here because $\overline { { X } }$ is always closed, and the closed sets in the   
Zariski topology are precisely the affine varieties.

Exercise 2.0.3(Gathmann 2.21): Let $\{ U _ { i } \} _ { i \in I }  X$ be an open cover of a topological space with $U _ { i } \cap U _ { j } \neq \emptyset$ for every $i , j$

a. Show that if $U _ { i }$ is connected for every i then X is connected.

b. Show that if $U _ { i }$ is irreducible for every i then X is irreducible.

Solution $( a )$ :   
Suppose toward a contradiction that $X = { X _ { 1 } } \coprod \boldsymbol { X } 2$ with $X _ { i }$ proper, disjoint, and open. Since $\{ U _ { i } \} \ni X$ , for each $j \in I$ this would force one of $U _ { j } \subseteq X _ { 1 }$ or $U _ { j } \subseteq X _ { 2 }$ , since otherwise $U _ { j } \cap X _ { 1 } \cap X _ { 2 }$ would be nonempty.

So without loss of generality (relabeling if necessary), assume $U _ { j } \in X _ { 1 }$ for some fixed j. But then for every $i \neq j ,$ we have $U _ { i } \cap U _ { j }$ nonempty by assumption, and so in fact $U _ { i } \subseteq X _ { 1 }$ for every $i \in I$ . But then $\cup _ { i \in I } U _ { i } \subseteq X _ { 1 }$ , and since $\{ U _ { i } \}$ was a cover, this forces $X \subseteq X _ { 1 }$ and thus $X _ { 2 } = \varnothing$ .

```latex
Solution(b):
Claim: X is irreducible ⇐⇒ any two open subsets intersect.
This follows because otherwise, if $U , V \subset X$ are open and disjoint then $X \setminus U , X \setminus V$ are
proper and closed. But then we can write $X = ( X \setminus U ) \coprod ( X \setminus V )$ as a union of proper closed
subsets, forcing X to not be irreducible.
So it suffices to show that if $U , V \subset X$ then $U \cap V$ is nonempty. Since $\{ U _ { i } \} \ni X$ , we can find
a pair $i , j$ such that there is at least one point in $U \cap U _ { i }$ and one point in $V \cap U _ { j }$
But by assumption $U _ { i } \cap U _ { j }$ is nonempty, so both $U \cap U _ { i }$ and $U _ { j } \cap U _ { i }$ are open nonempty subsets
of $U _ { i }$ . Since $U _ { i }$ was assumed irreducible, they must intersect, so there exists a point
x0 ∈ (U ∩ Ui) ∩ (Uj ∩ Ui) = U ∩ (Ui ∩ Uj) := U . ˜
We can now similarly note that $\tilde { U } \cap V$ and $U _ { j } \cap V$ are nonempty open subsets of $V ,$ and thus
intersect. So there is a point
x˜0 ∈ U˜ ∩ V  ∩ (Uj ∩ V ) = U˜ ∩ V = U ∩ V ∩ (Ui ∩ Uj ) ,
and in particular ${ \tilde { x } } _ { 0 } \in U \cap V$ as desired.
```

## Exercise 2.0.4(Gathmann 2.22): Let $f : X \to Y$ be a continuous map of topological spaces.

a. Show that if X is connected then f(X) is connected.

b. Show that if X is irreducible then f (X) is irreducible.

Solution(a):

Toward a contradiction, if $f ( X ) = Y _ { 1 } \coprod Y _ { 2 }$ with $Y _ { 1 } , Y _ { 2 }$ nonempty and open in $Y ,$ , then

$$
f ^ { - 1 } ( f ( X ) ) \subseteq X
$$

on one hand, and

$$
f ^ { - 1 } ( f ( X ) ) = f ^ { - 1 } ( Y _ { 1 } ) { \big [ } { \big ] } f ^ { - 1 } ( Y _ { 2 } )
$$

on the other. If f is continuous, the preimages $f ^ { - 1 } ( Y _ { i } )$ are open (and nonempty), so X contains a disconnected subset. However, every subset of a connected set must be connected, so this contradicts the connectedness of X.

$$
( b )
$$

Suppose $f ( X ) = Y _ { 1 } \cup Y _ { 2 }$ with $Y _ { i }$ proper closed subsets of $Y .$ . Then $f ^ { - 1 } ( Y _ { 1 } ) \cup f ^ { - 1 } ( Y ^ { 2 } ) =$ $( f ^ { - 1 } \circ f ) ( X ) \subseteq X$ are closed in X, since $f$ is continuous. Since X is irreducible, without loss of generality (by relabeling), this forces $X _ { 1 } = \varnothing$ . But then $f ( X _ { 1 } ) = \varnothing$ , forcing $f ( X ) = Y _ { 2 } $ .

Definition 2.0.5 (Ideal Quotient)

For two ideals $J _ { 1 } , J _ { 2 } \le R$ , the ideal quotient is defined by

$$
J _ { 1 } : J _ { 2 } : = \left\{ f \in R \Big | f J _ { 2 } \subset J _ { 1 } \right\} .
$$

Exercise 2.0.6(Gathmann 2.23): Let X be an affine variety.

a. Show that if $Y _ { 1 } , Y _ { 2 } \subset X$ are subvarieties then

$$
I ( \overline { { Y _ { 1 } \setminus Y _ { 2 } } } ) = I ( Y _ { 1 } ) : I ( Y _ { 2 } ) .
$$

b. If $J _ { 1 } , J _ { 2 } \triangleleft A ( X )$ are radical, then

$$
{ \overline { { V ( J _ { 1 } ) \setminus V ( J _ { 2 } ) } } } = V ( J _ { 1 } : J _ { 2 } ) .
$$

Solution: ?

Exercise 2.0.7(Gathmann $\it { 2 . 2 4 } )$ : Let $\boldsymbol { X } \subset \mathbb { A } ^ { n } , \boldsymbol { Y } \subset \mathbb { A } ^ { m }$ be irreducible affine varieties, and show that $X \times Y \subset \mathbb { A } ^ { n + m }$ is irreducible.

That $X \times Y$ is again an affine variety follows from writing $X = V ( I ) , Y = V ( J )$ , then $X \times Y = V ( I + J )$ where $I + J \triangleleft k [ x _ { 1 } , \cdot \cdot \cdot , x _ { n } , y _ { 1 } , \cdot \cdot \cdot , y _ { m } ]$ . So let

$$
X \times Y = U \cup V
$$

with $U , V$ proper and closed, and let $\pi _ { \boldsymbol { X } } , \pi _ { \boldsymbol { Y } }$ be the projections onto the factors.

Claim: For each $x \in X , \pi ^ { - 1 } ( x ) \cong Y$ is contained in only one of U or $V .$

Note that if this is true, we can write $X = G _ { U } \cup G _ { V }$ where

$$
G _ { U } : = \left\{ x \in X \mid \pi _ { X } ^ { - 1 } ( x ) \subseteq U \right\}
$$

are the points for which the entire fiber lies in $U ,$ and similarly $G _ { V }$ are those for which the fiber lies in V . If we can then show that $G _ { U } , G _ { V }$ are closed, by irreducibility of X this will force (wlog) $G _ { V } = \emptyset$ and $X = G _ { U }$ . But then

$$
\pi _ { X } ^ { - 1 } ( X ) = X \times Y { \mathrm { ~ a n d ~ } } \pi _ { X } ^ { - 1 } ( G _ { U } ) = U \implies X \times Y = U .
$$

which shows that $X \times Y$ is irreducible.

Proof (Every fiber is contained in one irreducible component).   
For any fixed x, we can write   
$\pi _ { X } ^ { - 1 } ( x ) = \left( \pi _ { X } ^ { - 1 } ( x ) \cap U \right) \cup \left( \pi _ { X } ^ { - 1 } ( x ) \cap V \right) .$   
Since points are closed in the Zariski topology and $\pi _ { X }$ is continuous, each $\pi _ { X } ^ { - 1 } ( x )$ is closed.   
and thus $\pi _ { X } ^ { - 1 } ( x ) \cap U$ is closed (and similarly for $V )$ . Noting that $\pi _ { X } ^ { - 1 } ( x ) \cong \{ x \} \times Y \cong Y$ •   
where we’ve assumed $Y$ to be irreducible, we can conclude wlog that $\pi _ { X } ^ { - 1 } ( x ) \cap V = \varnothing$   
Proof $( G _ { U } , G _ { V }$ are closed).   
Wlog consider $G _ { U } \subseteq X$ . Fixing any point $y _ { 0 } \in Y ,$ we have   
$X \cong X _ { y _ { 0 } } : = X \times \{ y _ { 0 } \} \subseteq X \times Y ,$   
so we can identify $G _ { U } \subset X$ with $G _ { U } \subset X _ { y _ { 0 } }$ inside a Y -fiber the product. But then   
$G _ { U } = X _ { y _ { 0 } } \cap U \subseteq X \times Y ,$   
where $U$ is closed in $X \times Y$ and thus closed in $X _ { y _ { 0 } }$ , and $X _ { y _ { 0 } }$ is trivially closed in itself.   
This exhibits $G _ { U }$ as the intersection of two sets that are closed in $X _ { y _ { 0 } } \cong X$

## 3 Problem Set 3

Exercise 3.0.1(Gathmann 2.33): Define

$$
X : = \Big \{ M \in \mathrm { M a t } ( 2 \times 3 , k ) \ \Big | \ \mathrm { r a n k } M \leq 1 \Big \} \subseteq \mathbb { A } ^ { 6 } / k .
$$

Show that X is an irreducible variety, and find its dimension.

Solution:   
We’ll use the following fact from linear algebra:   
Definition(Matrix Minor)   
For an $m \times n$ matrix, a minor of order \` is the determinant of a $\ell \times \ell$ submatrix obtained   
by deleting any $m - \ell$ rows and any $n - \ell$ columns.   
Theorem 3.0.3(Rank is a Function of Minors).   
If $A \in \mathrm { M a t } ( m \times n , k )$ is a matrix, then the rank of A is equal to the order of largest   
nonzero minor.   
Thus   
$M _ { i j } = 0$ for all \` × \` minors Mij ⇐⇒ rank(M ) < \`,

following from the fact that if one takes $\ell = \operatorname* { m i n } ( m , n )$ and all $\ell \times \ell$ minors vanish, then the largest nonzero minor must be of size $j \times j$ for $j \le \ell - 1$ . But det $M _ { i j }$ is a polynomial $f _ { i j }$ in its entries, which means that X can be written as

$$
X = V \left( \{ f _ { i j } \} \right) ,
$$

which exhibits X as a variety. Thus

$$
M = { \left[ \begin{array} { l l l } { x } & { y } & { z } \\ { a } & { b } & { c } \end{array} \right] } \implies X = V \left( \langle x b - y a , y c - z b , x c - z a \rangle \right) \subset { \mathbb { A } } ^ { 6 } .
$$

Claim: The ideal above is prime, and so the coordinate ring $A ( X )$ is a domain and thus X is irreducible.

$$
( X ) = 4 .
$$

Heuristic: there are three degrees of freedom in choosing the first row $x , y , z .$ To enforce the rank 1 condition, the second row must be a scalar multiple of the first, yielding one degree of freedom for the scalar.

Note: I looked at this for a couple of hours, but I don’t know how to prove either of these statements with the tools we have so far!

## Exercise 3.0.4(Gathmann $\it { 2 . 3 4 ) }$ : Let X be a topological space, and show

a. If $\{ U _ { i } \} _ { i \in I }  X$ , then dim X = sup dim $U _ { i }$ i∈I

b. If X is an irreducible affine variety and $U \subset X$ is a nonempty subset, then dim $X = \dim U$ Does this hold for any irreducible topological space?

## Solution:

Strictly for notational convenience, we’ll treat $\{ U _ { i } \}$ is if it were a countable open cover. Part a: We first note that if $U \subseteq V$ , then dim $U \leq$ dim V . If this were not the case, one could find a chain $\{ I _ { j } \}$ of closed irreducible subsets of V of length $n \textgreater$ dim U . But then $I _ { j } ^ { \prime } : = I _ { j } \cap U$ would again be a closed irreducible set, yielding a chain of length n in U. Thus dim $X \geq$ dim $U _ { i }$ , and it remains true that dim X ≥ sup dim $U _ { i }$ , so it suffices to show that dim $X \leq$ sup dim $U _ { i }$

Set $s : =$ sup dim $U _ { i }$ and $n : = \dim X$ , we want to show that $s \geq n .$ Let $\left\{ I _ { j } \right\} _ { j \leq n }$ be a maximal chain of length n of closed irreducible subsets of X, so we have

$$
\emptyset \subsetneq I _ { 0 } \subsetneq I _ { 1 } \subsetneq \cdots \subsetneq I _ { n } \subsetneq X .
$$

Since $I _ { 0 } \subset X$ and $\{ U _ { i } \}$ covers X, we can find some $U _ { 0 } \in \{ U _ { i } \}$ such that $I _ { 0 } \cap U _ { 0 }$ is nonempty, since otherwise there would be a point in $I _ { 0 } \cap ( X \setminus \cup _ { i \in J } U _ { i } ) = \emptyset$ . We can do this for every $I _ { j } { \mathrm { . } }$ so define $A _ { j } : = I _ { j } \cap U _ { 0 }$

Each $A _ { j }$ is now closed in $U _ { 0 }$ , and must remain irreducible, since any decomposition of $A _ { j }$ would lift to a decomposition of $I _ { 0 }$ . To see that $A _ { 0 } \subsetneq A _ { 1 }$ , i.e. that the inclusions are still

proper, we can just note that

$$
x \in A _ { i + 1 } \setminus A _ { i } \iff x \in ( I _ { i + 1 } \cap U _ { 0 } ) \setminus ( I _ { i } \cap U _ { 0 } ) = ( I _ { 1 } \setminus I _ { 2 } ) \cap U _ { 0 } = \emptyset .
$$

But this exhibits a length n chain in $U _ { 0 } ,$ , so dim $U _ { 0 } \geq n$ . Taking suprema, we have

$$
n \leq \dim U _ { 0 } \leq \operatorname* { s u p } _ { i \in J } \dim U _ { i } = s .
$$

Part b: The answer is no: we can produce a space X with some dim X and a subset U satisfying dim $U <$ dim X .

Define a space and a topology by

$$
X : = \{ a , b \} \qquad \tau : = \{ \emptyset , X , \{ 1 \} \} ,
$$

Here {b} is the only proper and closed subset, since its complement is open, so X must be irreducible. We can find an maximal ascending chain of length 1,

$$
\emptyset \subsetneq \{ b \} \subsetneq X ,
$$

and so dim X = 1. However, for $U : = \{ a \}$ , there is only one possible maximal chain:

$$
\emptyset \subsetneq \{ a \} = X ,
$$

so dim $U = 0 ,$

## Exercise 3.0.5(Gathmann 2.36): Prove the following:

a. Every noetherian topological space is compact. In particular, every open subset of an affine variety is compact in the Zariski topology.

b. A complex affine variety of dimension at least 1 is never compact in the classical topology.

Exercise 3.0.6(Gathmann $\it { 2 . 4 0 } )$ : Let

$$
R = k [ x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } ] / \left. x _ { 1 } x _ { 4 } - x _ { 2 } x _ { 3 } \right.
$$

and show the following:

a. R is an integral domain of dimension 3.

b. $x _ { 1 } , \cdots , x _ { 4 }$ are irreducible but not prime in R, and thus R is not a UFD.

c. $x _ { 1 } x _ { 4 }$ and x2x3 are two decompositions of the same element in R which are nonassociate.

d. $\langle x _ { 1 } , x _ { 2 } \rangle$ is a prime ideal of codimension 1 in R that is not principal.

Exercise 3.0.7(Problem 5): Consider a set U in the complement of $( 0 , 0 ) \in \mathbb { A } ^ { 2 }$ . Prove that any regular function on U extends to a regular function on all of $\mathbb { A } ^ { 2 }$

## 4 Problem Set 4 (Tuesday, October 06)

Problem. (Gathmann 3.20)   
Let $X \subset \mathbb { A } ^ { n }$ be an affine variety and $a \in X$ . Show that   
OX,a = OAn,a/I(X)OAn,a,   
where $I ( X ) { \mathcal { O } } _ { { \mathbb { A } } ^ { n } , a }$ denotes the ideal in $\mathcal { O } _ { \mathbb { A } ^ { n } , a }$ generated by all quotients $f / 1$ for $f \in I ( X )$

Problem. (Gathmann 3.21)   
Let $a \in \mathbb { R }$ , and consider sheaves $\mathcal { F }$ on R with the standard topology:   
1. F := the sheaf of continuous functions   
2. F := the sheaf of locally polynomial functions.   
For which is the stalk ${ \mathcal { F } } _ { a }$ a local ring?   
Recall that a local ring has precisely one maximal ideal.

Problem. (Gathmann 3.22)   
Let $\varphi , \psi \in { \mathcal { F } } ( U )$ be two sections of some sheaf $\mathcal { F }$ on an open $U \subseteq X$ and show that   
a. If $\varphi , \psi$ agree on all stalks, so $\overline { { ( U , \varphi ) } } = \overline { { ( U , \psi ) } } \in \mathcal { F } _ { a }$ for all $a \in U .$ , then $\varphi$ and $\psi$ are equal.   
b. If $\mathcal { F } : = \mathcal { O } _ { X }$ is the sheaf of regular functions on some irreducible affine variety $X$ , then if   
$\psi = \varphi$ on one stalk ${ \mathcal { F } } _ { a } .$ , then $\varphi = \psi$ everywhere.   
c. For a general sheaf $\mathcal { F }$ on X , (b) is false.

## Definition 4.0.1 (Stalk at a subspace)

Let $Y \subset X$ be a nonempty and irreducible subspace of X a topological space with a sheaf F on X. Then the stalk of $\mathcal { F }$ at $Y$ is defined by the pairs $( U , \varphi )$ such that $U \subset X$ $U \cap Y$ is nonempty, and $\varphi \in { \mathcal { F } } ( U )$ , where we identify $( U , \varphi ) \sim ( U ^ { \prime } , \varphi ^ { \prime } )$ iff there is a small enough open set such that the restrictions agree.

## Problem. (Gathmann 3.23: Geometry of a Certain Localization)

Let $Y \subset X$ be a nonempty and irreducible subvariety of an affine variety $X ,$ , and show that the stalk ${ \mathcal { O } } _ { X , Y }$ of ${ \mathcal { O } } _ { X }$ at $Y$ is a k-algebra which is isomorphic to the localization $A ( X ) _ { I ( Y ) }$

## Problem. (Gathmann 3.24) Problem. (Gathmann 3.24)

Let $\mathcal { F }$ be a sheaf on X a topological space and $a \in X$ . Show that the stalk ${ \mathcal { F } } _ { a }$ is a local object, i.e. if $U \subset X$ is an open neighborhood of $^ { a , }$ then ${ \mathcal { F } } _ { a }$ is isomorphic to the stalk of $\mathcal { F } | _ { U }$ at a on U viewed as a topological space.

## 5 Problem Set 5 (Monday, October 26)

Problem. (Gathmann 4.13)   
Let $f : X \to Y$ be a morphism of affine varieties and $f ^ { * } : A ( Y )  A ( X )$ the induced map on   
coordinate rings. Determine if the following statements are true or false:   
a. f is surjective $\iff f ^ { * }$ is injective.   
b. f is injective $\iff f ^ { * }$ is surjective.   
c. If $f : \mathbb { A } ^ { 1 } \to \mathbb { A } ^ { 1 }$ is an isomorphism, then f is affine linear, i.e. $f ( x ) = a x + b$ for some   
$a , b \in k .$   
d. If $f : \mathbb { A } ^ { 2 } \to \mathbb { A } ^ { 2 }$ is an isomorphism, then f is affine linear, i.e. $f ( x ) = A x + b$ for some   
$a \in \mathrm { M a t } ( 2 \times 2 , k )$ and $b \in k ^ { 2 } .$

## Solution:

a. True. This follows because if $p , q \in A ( Y )$ , then

$$
\begin{array} { r l } { f * p = f ^ { * } q } \\ { } & { { } \implies ( p \circ f ) = ( q \circ f ) } \\ { } & { { } \implies p = q , } \end{array}
$$

by definition

where in the last implication we’ve used the fact that f is surjective iff f admits a right-inverse.

## Problem. (Gathmann $\not { A } . { \cal { I } } ^ { g } )$

Which of the following are isomorphic as ringed spaces over C?

(a) $\mathbb { A } ^ { 1 } \backslash \{ 1 \}$

(b) $V \left( x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } \right) \subset \mathbb { A } ^ { 2 }$

(c) $V \left( x _ { 2 } - x _ { 1 } ^ { 2 } , x _ { 3 } - x _ { 1 } ^ { 3 } \right) \backslash \{ 0 \} \subset \mathbb { A } ^ { 3 }$

(d) $V \left( x _ { 1 } x _ { 2 } \right) \subset \mathbb { A } ^ { 2 }$

(e) $V \left( x _ { 2 } ^ { 2 } - x _ { 1 } ^ { 3 } - x _ { 1 } ^ { 2 } \right) \subset \mathbb { A } ^ { 2 }$

(f) $V \left( x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } - 1 \right) \subset \mathbb { A } ^ { 2 }$

Problem. (Gathmann 5.7)   
Show that   
a. Every morphism $f : \mathbb { A } ^ { 1 } \setminus \{ 0 \} \to \mathbb { P } ^ { 1 }$ can be extended to a morphism $\widehat { f } : \mathbb { A } ^ { 1 } \to \mathbb { P } ^ { 1 }$   
b. Not every morphism $f : \mathbb { A } ^ { 2 } \setminus \{ 0 \} \to \mathbb { P } ^ { 1 }$ can be extended to a morphism $\widehat { f } : \mathbb { A } ^ { 2 } \to \mathbb { P } ^ { 1 }$   
c. Every morphism $\mathbb { P } ^ { 1 } \to \mathbb { \mathbb { A } } ^ { 1 }$ is constant.

## Problem. (Gathmann 5.8)

Show that

a. Every isomorphism $f : \mathbb { P } ^ { 1 } \to \mathbb { P } ^ { 1 }$ is of the form

$$
f ( x ) = { \frac { a x + b } { c x + d } }
$$

$$
a , b , c , d \in k .
$$

where x is an affine coordinate on $\mathbb { A } ^ { 1 } \subset \mathbb { P } ^ { 1 }$

b. Given three distinct points $a _ { i } \in \mathbb { P } ^ { 1 }$ and three distinct points $b _ { i } \in \mathbb { P } ^ { 1 }$ , there is a unique isomorphism $f : \mathbb { P } ^ { 1 } \overset { \overline { { \mathbf { \phi } } } } {  } \mathbb { P } ^ { 1 }$ such that $f ( a _ { i } ) = b _ { i }$ for all i.

## Proposition 5.0.1(?).

There is a bijection

$$
X \to Y \} \{ \stackrel { \cdot 1 : 1 } { \longleftrightarrow } \} \{ K 
$$

$$
f \longmapsto f ^ { * }
$$

$$
\mathcal { O } _ { Y } ( Y )  \mathcal { O } _ { X } ( X ) \}
$$

Problem. (Gathmann 5.9)

Does the above bijection hold if

a. X is an arbitrary prevariety but Y is still affine?

b. Y is an arbitrary prevariety but X is still affine?