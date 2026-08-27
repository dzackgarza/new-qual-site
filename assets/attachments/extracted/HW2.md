## Homework 2

## Exercise 1

Let $\phi , \psi : U \to \mathbb { R } ^ { n }$ be two coordinate charts on a smooth manifold M. Let $m \in U$ Let $v \in T _ { m } U$ be given in φ-coordinates by $\sum v _ { i } \frac { \partial } { \partial x _ { i } }$ and in ψ-coordinates by $\sum w _ { i } \frac { \partial } { \partial y _ { i } }$ Determine $w _ { i }$ in terms of $v _ { i }$ and the maps $\phi \circ \psi ^ { \dot { - } 1 } , \psi \circ \phi ^ { - 1 }$ . (Start by making sure you understand what’s meant by φ-coordinates.)

## Exercise 2

Let $M , \phi , \psi , m ,$ , and U be as above. Let ω be a k-form on $U$ so that $\omega = \sum _ { I } f _ { I } d x _ { I }$ in φ-coordinates and $\begin{array} { r } { \omega = \sum _ { J } g _ { J } d y _ { J } } \end{array}$ in ψ-coordinates. Determine $g _ { J }$ in terms of $f _ { I }$ $\phi ,$ and $\psi .$

## Exercise 3

On the last homework, you showed that $M \times N$ gets a smooth structure from M and N. There are smooth ap $\pi _ { 1 } : M \times N \to M$ $\pi _ { 2 } : M \times N \to N$ by projecting onto the first or second coordiante. (You do not have to check that they are smooth.)

Use these maps to cook up an isomorphism $T _ { ( } p , q ) ( M \times N ) \cong T _ { p } M \times T _ { q } N .$

## Exercise 4

Let $F : M \to N$ be a smooth map of smooth manifolds so that $F _ { * } : T _ { p } \to T _ { F ( p ) }$ is the zero map for all $p .$ Show that $F$ must be constant if M is connected.

## Exercise 5

• Prove that the exterior derivative is not dependent on the choice of charts by proving the following coordinate-free formula. Let M be a smooth manifold. Let $\omega \in \Omega ^ { p } ( M )$ , and let $X ^ { 0 } , \ldots , X ^ { p }$ be vector fields on M. Then

$$
\begin{array} { l } { ( d \omega ) ( X ^ { 0 } , \dots , X ^ { p } ) = \displaystyle \sum _ { i = 0 } ^ { p } ( - 1 ) ^ { i } X _ { i } \omega ( X ^ { 0 } , \dots , \widehat { X ^ { i } } , \dots , X ^ { p } ) \medskip } \\ { + \displaystyle \sum _ { i < j } ( - 1 ) ^ { ( i + 1 ) } \omega ( [ X ^ { i } , X ^ { j } ] , X ^ { 0 } , \dots , \widehat { X ^ { i } } , \dots , \widehat { X ^ { j } } , \dots , X ^ { p } ) \medskip } \end{array}
$$

where summing over something with a hat means skipping it. (To clarify: $\omega ( X ^ { 0 } , . . . , \widehat { X ^ { i } } , . . . , X ^ { p } )$ is a function from $M  \mathbb { R } - \mathbf { w h y } ? )$

Prove this formula. (Hint: you need to compare this formula to the one in coordinates. So you’d really like to be able to replace the Xi with constant vector fields (defined only near m) like $\partial / \partial x _ { i }$ . Start by showing that if $X ^ { 0 } ( m ) = Y ^ { 0 } ( m )$ , then $( d \omega ) ( Y ^ { 0 } , X ^ { 1 } , \ldots , X ^ { p } ) = ( d \omega ) ( X ^ { 0 } , \ldots , X ^ { p } ) . )$

• Your classmate Adam is confused by the previous problem: “why are we thinking about vector fields in the first place? The hint tells us that we only need to think about the value of $X ^ { 0 }$ at m. So we may as well just define $( d \omega )$ on a $( p + 1 )$ )-tuple of vectors. Our professor gives us obsfuscated exercises!” Explain why Adam is wrong, at least about the mathematics.

## Exercise 6

Show that $H _ { 0 , d R } ( M )$ is determined by the point-set topology of M rather than the smooth structure on M. (To do so, describe $H _ { 0 , d R } ( M )$ in terms of the point-set topology of M .)

## Exercise 7

Compute $H _ { k , d R } ( S ^ { n } )$ for $k \in \mathbb N .$