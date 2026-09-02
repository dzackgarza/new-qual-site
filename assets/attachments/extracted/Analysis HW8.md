# Math 8100 Assignment 8 Basic Function Spaces

Due date: Tuesday the 26th of November 2019

1. Prove the following basic properties of $L ^ { \infty } = L ^ { \infty } ( X )$ , where X is a measurable subset of $\mathbb { R } ^ { n }$

(a) $\| \cdot \| _ { \infty }$ is a norm on $L ^ { \infty }$ and when equipped with this norm $L ^ { \infty }$ is a Banach space.

(b) $\| f _ { n } - f \| _ { \infty } \to 0$ iff there exists $E \in \mathbb { R } ^ { n }$ such that $m ( E ^ { c } ) = 0$ and $f _ { n }  f$ uniformly on $E .$

(c) Simple functions are dense in $L ^ { \infty }$ , but continuous functions with compact support are not.

Recall that $i f X \subseteq \mathbb { R } ^ { n }$ is measurable and f is a measurable function on $X$ , then we define

$$
\| f \| _ { \infty } = \operatorname* { i n f } \{ a \geq 0 : m ( \{ x \in X : | f ( x ) | > a \} ) = 0 \} ,
$$

with the convention that inf $\varnothing = \infty ,$ and

$$
L ^ { \infty } = L ^ { \infty } ( X ) = \{ f : X \to \mathbb { C } \ m e a s u a r a b l e : \ \lVert f \rVert _ { \infty } < \infty \} ,
$$

with the usual convention that two functions that are equal a.e. define the same element of $L ^ { \infty }$ . Thus $f \in L ^ { \infty }$ if and only if there is a bounded function g such that $f = g$ almost everywhere; we can take $g = f \chi _ { E }$ where $E = \{ x : | f ( x ) | \leq \| f \| _ { \infty } \}$

2. Let $X \subseteq \mathbb { R } ^ { n }$ be measurable.

(a) i. Prove that if $m ( X ) < \infty$ , then

$$
L ^ { \infty } ( X ) \subset L ^ { 2 } ( X ) \subset L ^ { 1 } ( X )\tag{1}
$$

with strict inclusion in each case, and that for any measurable $f : X \to \mathbb { C }$ one in fact has

$$
\| f \| _ { L ^ { 1 } ( X ) } \leq m ( X ) ^ { 1 / 2 } \| f \| _ { L ^ { 2 } ( X ) } \leq m ( X ) \| f \| _ { L ^ { \infty } ( X ) } .
$$

ii.
Give examples to show that no such result of the form (1) can hold if one drops the assumption that $m ( x ) < \infty$ . Prove, furthermore, that if $L ^ { 2 } ( X ) \subseteq L ^ { 1 } ( X )$ , then $m ( X ) < \infty$

(b) Prove that

$$
\underset { ( \star ) } { \underbrace { L ^ { 1 } ( X ) \cap L ^ { \infty } ( X ) \subset L ^ { 2 } ( X ) } } \subset L ^ { 1 } ( X ) + L ^ { \infty } ( X )
$$

and that in addition to (?) one in fact has

$$
\| f \| _ { L ^ { 2 } ( X ) } \leq \| f \| _ { L ^ { 1 } ( X ) } ^ { 1 / 2 } \| f \| _ { L ^ { \infty } ( X ) } ^ { 1 / 2 }
$$

for any measurable function $f : X \to \mathbb { C }$

3. Prove that

$$
\ell ^ { 1 } ( \mathbb { Z } ) \subset \ell ^ { 2 } ( \mathbb { Z } ) \subset \ell ^ { \infty } ( \mathbb { Z } )
$$

with strict inclusion in each case, and that for any sequence $a = \{ a _ { j } \} _ { j \in \mathbb { Z } }$ of complex numbers one in fact has

$$
\| a \| _ { \ell ^ { \infty } ( \mathbb { Z } ) } \leq \| a \| _ { \ell ^ { 2 } ( \mathbb { Z } ) } \leq \| a \| _ { \ell ^ { 1 } ( \mathbb { Z } ) } .
$$

Recall that for $p = 1 , 2 , \infty$ we define

$$
\ell ^ { p } ( \mathbb { Z } ) = \{ a = \{ a _ { j } \} _ { j \in \mathbb { Z } } \subseteq \mathbb { C } : \| a \| _ { \ell ^ { p } ( \mathbb { Z } ) } < \infty \}
$$

where

$$
\| a \| _ { \ell ^ { 1 } ( \mathbb { Z } ) } = \sum _ { j = - \infty } ^ { \infty } | a _ { j } | , \quad \| a \| _ { \ell ^ { 2 } ( \mathbb { Z } ) } = \Big ( \sum _ { j = - \infty } ^ { \infty } | a _ { j } | ^ { 2 } \Big ) ^ { 1 / 2 } , a n d \| a \| _ { \ell ^ { \infty } ( \mathbb { Z } ) } = \operatorname* { s u p } _ { j } | a _ { j } | .
$$

4. Let $C ( [ 0 , 1 ] )$ denote the space of all continuous real-valued functions on [0, 1].

(a) Prove that $C ( [ 0 , 1 ] )$ is complete under the uniform norm $\| f \| _ { u } : = \operatorname* { s u p } _ { x \in [ 0 , 1 ] } | f ( x ) |$

(b) Prove that $C ( [ 0 , 1 ] )$ is not complete under the L1-norm $\| f \| _ { 1 } = \int _ { 0 } ^ { 1 } | f ( x ) | d x$

5. Let H be a Hilbert space with orthonormal basis $\{ u _ { n } \} _ { n = 1 } ^ { \infty }$

(a) Let $\{ a _ { n } \} _ { n = 1 } ^ { \infty }$ be a sequence of complex numbers.
Prove that

$\sum _ { n = 1 } ^ { \infty } a _ { n } u _ { n }$ converges in H $\iff \sum _ { n = 1 } ^ { \infty } | a _ { n } | ^ { 2 } < \infty ,$

and moreover that if $: \sum _ { n = 1 } ^ { \infty } | a _ { n } | ^ { 2 } < \infty$ , then $\Big \| \sum _ { n = 1 } ^ { \infty } a _ { n } u _ { n } \Big \| = \Big ( \sum _ { n = 1 } ^ { \infty } | a _ { n } | ^ { 2 } \Big ) ^ { 1 / 2 } .$

(b) i. Is there a continuous linear functional L on H such that $L ( u _ { n } ) = n ^ { - 1 }$ for all $n \in \mathbb { N } ?$ If L exists, find its norm.

ii.
Is there a continuous linear functional L on H such that $L ( u _ { n } ) = n ^ { - 1 / 2 }$ for all $n \in \mathbb { N } ?$ If L exists, find its norm.

6. For each $1 \leq p \leq \infty$ , define $\Lambda _ { p } : L ^ { p } ( [ 0 , 1 ] ) \to \mathbb { R }$ by

$$
\Lambda _ { p } ( f ) = \int _ { 0 } ^ { 1 } x ^ { 2 } f ( x ) d x .
$$

Explain why $\Lambda _ { p }$ is a continuous linear functional and compute its norm (in terms of $p )$

## Extra Practice Problems Not to be handed in with the assignment

1. Let f and g be two non-negative Lebesgue measurable functions on $[ 0 , \infty )$ . Suppose that

$$
A : = \int _ { 0 } ^ { \infty } f ( y ) y ^ { - 1 / 2 } d y < \infty \qquad \mathrm { a n d } \qquad B : = \left( \int _ { 0 } ^ { \infty } | g ( y ) | ^ { 2 } d y \right) ^ { 1 / 2 } < \infty
$$

Prove that

$$
\int _ { 0 } ^ { \infty } \left( \int _ { 0 } ^ { x } f ( y ) d y \right) { \frac { g ( x ) } { x } } d x \leq A B
$$

2. Let $\{ f _ { k } \}$ be any sequence of functions in $L ^ { 2 } ( [ 0 , 1 ] )$ satisfying $\| f _ { k } \| _ { 2 } \leq 1$ for all $k \in \mathbb N$

(a) i. Prove that if $f _ { k }  f$ either a.e. on [0, 1] or in $L ^ { 1 } ( [ 0 , 1 ] )$ , then $f \in L ^ { 2 } ( [ 0 , 1 ] )$ ) with $\| f \| _ { 2 } \leq 1$

ii.
Do either of the above hypotheses guarantee that $f _ { k }  f$ in $L ^ { 2 } ( [ 0 , 1 ] ) ?$

(b) Prove that if $f _ { k } \to f { \mathrm { ~ a . e . } }$ . on [0, 1], then this in fact implies that $f _ { k }  f$ in $L ^ { 1 } ( [ 0 , 1 ] )$ ).

3. Let $1 \leq p \leq \infty$ . Prove that if $\{ f _ { k } \} _ { k = 1 } ^ { \infty }$ is a sequence of functions in $L ^ { p } ( \mathbb { R } ^ { n } )$ with the property that

$$
\sum _ { k = 1 } ^ { \infty } \| f _ { k } \| _ { p } < \infty ,
$$

then $\sum f _ { k }$ converges almost everywhere to an $L ^ { p } ( \mathbb { R } ^ { n } )$ function with

$$
\left\| \sum _ { k = 1 } ^ { \infty } f _ { k } \right\| _ { p } \leq \sum _ { k = 1 } ^ { \infty } \| f _ { k } \| _ { p } .
$$
