## Homework 1: fundamentals

## Exercise 1: Calculus

Check the assertion from class that

$$
f ( x ) = { \left\{ \begin{array} { l l } { e ^ { - { \frac { 1 } { x } } } } & { x > 0 } \\ { 0 } & { x \leq 0 } \end{array} \right. }
$$

is a smooth function. A more specific and helpful claim is that there is a sequence of polynomials $P _ { k } ( t )$ so that

$$
f ^ { ( k ) } ( x ) = { \left\{ \begin{array} { l l } { P _ { k } ( { \frac { 1 } { x } } ) e ^ { - { \frac { 1 } { x } } } } & { x > 0 } \\ { 0 } & { x \leq 0 } \end{array} \right. } .
$$

## Exercise 2: de Rham cohomology with compact support

Let ω be a k-form on $\mathbb { R } ^ { n }$ . We say that ω is compactly supported if there is some compact set $K$ so that $\omega = 0$ on $\mathbb { R } ^ { n } \setminus K$ Write $\Omega _ { c } ^ { * } ( \mathbb { R } ^ { n } )$ for the set of compactly supported k-forms.

• Show that $\Omega _ { c } ^ { * } ( \mathbb { R } ^ { n } )$ is a subalgebra of $\Omega ^ { * } ( \mathbb { R } ^ { n } )$

• Show that the exterior derivative operator d restricts to an operation

$$
d : \Omega _ { c } ^ { * } ( \mathbb { R } ^ { n } )  \Omega _ { c } ^ { * } ( \mathbb { R } ^ { n } ) .
$$

• Define the compactly supported de Rham cohomology of $\mathbb { R } ^ { n }$ to be

$$
H _ { c , d R } ^ { k } ( \mathbb { R } ^ { n } ) = \frac { \ker ( d | _ { \Omega _ { c } ^ { k } } ) } { { \left( d | _ { \Omega _ { c } ^ { k - 1 } } \right) } } .
$$

Compute $H _ { c , d R } ^ { k } ( \mathbb { R } ^ { 0 } )$ and $H _ { c , d R } ^ { k } ( \mathbb { R } ^ { 1 } )$ . Compare your results and methods with the ones we used in class.

## Exercise 3: Smooth function hygiene

• Let M be a smooth manifold, let $U \subset M$ , and let $\phi : U \to \mathbb { R } ^ { k }$ be a chart. Let $f : U \to \mathbb { R } ^ { m }$ be a continuous function. Suppose that $f \circ \phi ^ { - 1 }$ is smooth. Let $\psi : U \to \mathbb { R } ^ { k }$ be another chart with the same domain. Show that $f \circ \phi ^ { - 1 }$ is smooth.

• A function $f : M \to \mathbb { R } ^ { k }$ is smooth if for every $p \in M$ there is a smooth chart $( U , \phi )$ with $p \in U$ so that $f \circ \phi ^ { - 1 }$ is smooth on $\phi ( U )$ . Show that if $f$ is smooth, then $f \circ \psi ^ { - 1 }$ is smooth for any chart $( V , \psi )$ around $p .$

• Show that the composition of smooth functions between manifolds is smooth. Show that the composition of diffeomorphisms is again a diffeomorphism.

• Write down a smooth function $\mathbb { R } $ R which is invertible but not a diffeomorphism.

## Exercise 4: Stereographic projection

In this exercise you will show that $S ^ { n }$ is a manifold which can be covered by two charts. Think of $S ^ { n } \subset \mathbb { R } ^ { n + 1 }$ as the set

$$
S ^ { n } = \{ x _ { 1 } ^ { 2 } + \cdot \cdot \cdot + x _ { n + 1 } ^ { 2 } = 1 : ( x _ { 1 } , \ldots , x _ { n + 1 } ) \in \mathbb { R } ^ { n + 1 } \}
$$

Write $N = ( 0 , \ldots , 0 , 1 )$ and ${ \cal S } = ( 0 , \ldots , 0 , - 1 )$ . (These are the north and south   
poles.)

• Define a map $p : S ^ { n } \setminus N \to \mathbb { R } ^ { n }$ as follows. Let $x \in S ^ { n } \setminus N$ . There is a unique line $\ell _ { x }$ between N and X. This line intersects the plane $\{ x _ { n + 1 } = 0 \}$ in one point. This point is $p ( x )$ . Identify $\mathbb { R } ^ { n }$ with the set

$$
\left\{ \left( x _ { 1 } , \ldots , x _ { n + 1 } \right) : x _ { n + 1 } = 0 \right\}
$$

so that $p$ really is a map to $\mathbb { R } ^ { n }$   
First, check that $p ( x )$ is well-defined: why does $\ell _ { x }$ intersect $\{ x _ { n + 1 } = 0 \}$ in   
exactly one point?

• Write down a nice expression for $p ( x )$ in terms of $\left( x _ { 1 } , \ldots , x _ { n + 1 } \right)$ . (Hint: your expression shouldn’t make sense if you try to set $x = N . )$

• Show that $p$ has an inverse and write down a nice expression for it.

$p ( \mathbb { R } ^ { n } )$ covers most of the sphere. Find another good chart which covers the rest.

• Show that $S ^ { n }$ cannot be covered by a single chart.

## Exercise 5

Prove (not just by picture!) that the union of the $x \mathrm { - }$ and y-axes in $\mathbb { R } ^ { 2 }$ is not a manifold.

## Exercise 6: Products and graphs

Let X and Y be smooth manifolds. Show that $X \times Y$ is a smooth manifold. Suppose that f and $g$ are smooth functions with domains X and $Y$ , respectively. Show that $( f \times g ) ( x , y ) = ( f ( x ) , g ( y ) )$ is a smooth function.   
Now suppose that $h : X \to Y$ . Show that the graph of $h ,$

$$
\mathrm { g r a p h } ( h ) = \{ ( x , h ( x ) ) : x \in X \}
$$

is a smooth manifold. (Hint: define a map $X  X \times Y$ which restricts to a diffeomorphism on the graph.)