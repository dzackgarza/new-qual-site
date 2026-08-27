## Homework 3

1. (Exercise 6.2, page 54 from B&T) Show that two vector bundles on a manifold M are isomorphic if and only if their cocycles are equivalent (relative to some open cover).

2. (Exercise 6.43, page 65 from B&T) Let $\pi \colon E  M$ be a rank two bundle. Then there is an isomorphism $H ^ { * } ( M ) \to H _ { c v } ^ { * + 2 } ( E )$ given by the wedge product with the Thom class Φ. It follows that any class $\omega \in H _ { c v } ^ { * + 2 } ( E )$ can be written $\Phi \wedge \pi ^ { * } u$ where $u \in H ^ { * } ( M )$

Give a nice description of the class u so that Φ $\wedge \pi ^ { * } u = \Phi \wedge \Phi$

3. (Exercise 6.45, page 77 from B&T) There is a special bundle on $\mathbb { C } P ^ { n }$ called the tautological line bundle (or “universal subbundle” in Bott and Tu). Recall that $\mathbb { C } P ^ { n }$ can be thought of as the space of complex lines in $\mathbb { C } ^ { n + 1 }$ . Consider the product bundle $\mathbb { C } P ^ { n } \times \mathbb { C } ^ { n + 1 }$ . An element of this space is a pair $( \ell , z )$ where \` is a line in $\mathbb { C } ^ { n + 1 }$ and z is a point in $\mathbb { C } ^ { n + 1 }$ . The tautological bundle is defined as the set

$$
L ^ { n } = \{ ( \ell , z ) : z \in \ell \} .
$$

Compute the Euler class of $L ^ { 1 }$ by writing down transition functions for $L ^ { 1 }$

4. (Exercise 6.46, abbreviated)

(a) Let $i \colon S ^ { n } \to S ^ { n }$ be the antipodal map. An invariant differential form is a form ω so that $i ^ { * } \omega = \omega$ . The space of such forms is closed under addition, wedge product, and exterior differentiation, so there is an invariant cohomology $H ^ { * } ( S ^ { n } ) ^ { I }$ . Show that $H ^ { * } ( \mathbb { R } P ^ { n } ) \cong H ^ { * } ( S ^ { n } ) ^ { I }$

(b) It turns out that the natural map $H ^ { * } ( S ^ { n } ) ^ { I } \to H ^ { * } ( S ^ { n } )$ is injective, but you don’t need to prove that.

(c) Show that i is orientation-preserving if and only if n is odd. Use this to conclude that, if [σ] generates $H ^ { n } ( S ^ { n } )$ , then $[ \sigma ]$ is invariant if and only if n is odd.

(d) Compute the de Rham cohomology of R $P ^ { n }$

$$
H ^ { q } ( \mathbb { R } P ^ { n } ) \cong { \left\{ \begin{array} { l l } { \mathbb { R } } & { q = 0 } \\ { \mathbb { R } } & { q = n { \mathrm { ~ a n d ~ } } n { \mathrm { ~ o d d } } } \\ { 0 } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }
$$

5. A division algebra D is a non-necessarily-associative algebra over a field with the property that, for $a , b , x \in D$ and $b \neq 0$ , if

$$
a = b x
$$

then there is an element y so that

$$
a = y b .
$$

Suppose that we have some multiplication rule on $\mathbb { R } ^ { n }$ which makes it into a division algebra. Write $e _ { i }$ for the point $( 0 , \ldots , 0 , \underbrace { 1 } _ { i } , 0 , \ldots , 0 ) \in \mathbb { R } ^ { n }$

(a) Let $p \in S ^ { n - 1 } \subset \mathbb { R } ^ { n }$ . Show that there is a unique $a \in \mathbb { R } ^ { n }$ so that $p = a e _ { 1 }$

(b) Let $b \in \mathbb { R } ^ { n }$ be non-zero. Show that $b e _ { 1 } , \ldots , b e _ { n }$ are linearly independent in $\mathbb { R } ^ { n }$ •

(c) Let $p = a e _ { 1 }$ as in the first bit. You can project $a e _ { 2 } , \ldots , a e _ { n }$ to $T _ { p } ( S ^ { n - 1 } )$ . Describe this projection and verify that the projections of $a e _ { 2 } , \ldots , a e _ { n }$ are still linearly independent.

(d) You may assume that multiplication by a fixed a is a continuous map. (But you are welcome to prove it.) Show that, if $\mathbb { R } ^ { n }$ can be given the structure of a division algebra, then $T S ^ { n - 1 }$ is trivial. Conclude that $\mathbb { R } ^ { 3 }$ cannot have the structure of a division algebra.