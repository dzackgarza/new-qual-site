<!-- image-->

## Basic Examination

Instructions: Do any ten of the following eleven problems.

1. (a) State some reasonably general conditions under which this "differentiation under the integral sign" formula is valid:

$$
{ \frac { d } { d x } } \int _ { a } ^ { b } f ( x , y ) d y = \int _ { a } ^ { b } { \frac { \partial f } { \partial x } } \ d y .
$$

ovhat heu lnhendins oavpr .

2. Prove that the unit interval [0, 1] is sequentially compact, i.e., that every infinite sequence has a convergent

[Prove this directly. Do not just quote general theorems like Heine-Borel.]

<!-- image-->

3. Prove that the open unit ball in $\mathbb { R } ^ { 2 }$

$$
\left\{ ( x , y ) \in \mathbb { R } ^ { 2 } : x ^ { 2 } + y ^ { 2 } < 1 \right\}
$$

is connected.

[You may assume that intervals in R are connected. You should not just quote other general results, but give a direct proof.]

4. Prove that the set of irrational numbers in $\mathbb { R }$ is not a countable union of closed sets.

5. (a) Let $f : U \to \mathbb { R } ^ { k }$ be a function on an open set U in $\mathbb { R } ^ { n }$ . Define what it means for f to be differentiable at a point $x \in U$

(b) State carefully the Chain Rule for the composition of differentiable functions of several variables.

(c) Prove the Chain Rule you stated in part (b).

6. (a) State some reasonably general conditions on a function $f : \mathbb { R } ^ { 2 } \to \mathbb { R }$ under which

<!-- image-->

$$
{ \frac { \partial } { \partial x } } \left( { \frac { \partial f } { \partial y } } \right) = { \frac { \partial } { \partial y } } \left( { \frac { \partial f } { \partial x } } \right) .
$$

<!-- image-->

(b) Prove the formula under the conditions you stated.

7. Suppose $F : \mathbb { R } ^ { 2 }  \mathbb { R } ^ { 2 }$ is everywhere differentiable and that its first derivative (Jacobian) matrix

$$
\left( \begin{array} { l l } { \frac { \partial F _ { 1 } } { \partial x } } & { \frac { \partial F _ { 1 } } { \partial y } } \\ { \frac { \partial F _ { 2 } } { \partial x } } & { \frac { \partial F _ { 2 } } { \partial y } } \end{array} \right)
$$

is continuous everywhere and nonsingular everywhere.

[Here we use the notation $F ( ( x , y ) ) = ( F _ { 1 } ( x , y ) , \ F _ { 2 } ( x , y ) ) \in \mathbb { R } ^ { 2 } . ]$

Suppose also that

$$
\| F ( ( x , y ) ) \| \geq 1 \quad { \mathrm { i f } } \quad \| ( x , y ) \| = 1 { \mathrm { a n d ~ t h a t } } F ( ( 0 , 0 ) ) = ( 0 , 0 ) .
$$

Prove that

$$
{ \cal F } \left( \left\{ ( x , y ) : x ^ { 2 } + y ^ { 2 } < 1 \right\} \right) \supset \left\{ ( x , y ) : x ^ { 2 } + y ^ { 2 } < 1 \right\} .
$$

(Hint: With $U = \{ ( x , y ) : x ^ { 2 } + y ^ { 2 } < 1 \}$ , prove that $F ( U ) \cap U$ is open and is closed in U.)

<!-- image-->

8. Let $T : V \to W$ and $S : W \to X$ be linear transformations of finite dimensional real vector spaces. Prove that

$$
\operatorname { r a n k } ( T ) + \operatorname { r a n k } ( S ) - \dim ( W ) \leq \operatorname { r a n k } ( S \circ T ) \leq \operatorname* { m a x } \{ \operatorname { r a n k } ( T ) , \operatorname { r a n k } ( S ) \} .
$$

[The rank of an linear transformation is the dimension of its image.]

9. Let V be a real vector space and $T : V  V$ be a linear transformation. Let $\lambda _ { 1 } , \ldots , \lambda _ { m }$ be distinct eigenvalues of T. Let $0 \neq v _ { i }$ be an eigenvector of T with eigenvalue $\lambda _ { i }$ for $1 \leq i \leq m$ Show that $\{ v _ { 1 } , \ldots , v _ { m } \}$ is linearly independent.

10. Let V be a finite dimensional complex inner product space and $f : V \to \mathbf { C }$ a linear functional. Show that there exists a vector $w \in V$ such that $f ( v ) = \langle v , w \rangle$ for all $v \in V$ •

11. Let V be a finite dimensional complex inner product space and $T : V \to V$ a linear transformation. Prove that there exists an orthonormal ordered basis for V such that the matrix representation A in this basis is upper triangular, i.e., $A _ { i j } = 0 { \mathrm { ~ i f ~ } } i < j$

[Hint: First show if $S : V \to V$ is a linear transformation and W is a subspace then $W$ is S-invariant if and only if $W ^ { \perp }$ is $S ^ { * }$ invariant where $S ^ { \ast }$ is the adjoint of S.]