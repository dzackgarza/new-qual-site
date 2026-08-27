# BASIC QUAL WINTER 2006 (February 18, 2006)

Problem 1. Show that for each $\epsilon > 0$ there exists a sequence of intervals $\left( I _ { n } \right)$ with the properties

$$
\bigcup _ { n = 1 } ^ { \infty } I _ { n } \supset \mathbb { Q } \quad { \mathrm { a n d } } \quad \sum _ { n = 1 } ^ { \infty } | I _ { n } | < \epsilon .
$$

Problem 2. Let $( a _ { n } ) _ { n \geq 1 }$ be a decreasing sequence of positive numbers such that $\textstyle \sum _ { n = 1 } ^ { \infty } a _ { n } = \infty$ Under what condition(s) is the function

$$
f ( x ) = \sum _ { n = 1 } ^ { \infty } ( - 1 ) ^ { n } a _ { n } x ^ { n }
$$

well-defined and left-continuous at $x = 1$ Carefully prove your assertion.

Problem 3. Consider a function $f \colon [ a , b ] \to \mathbb { R }$ which is twice continuously differentiable (including the endpoints). Let $a = x _ { 0 } < x _ { 1 } < \cdots < x _ { n } = b$ be the uniform partition of $[ a , b ]$ i.e., $x _ { i + 1 } - x _ { i } = ( b - a ) / n$ for all $0 \leq i < n$ Show that there exists M such that for all $n \geq 1$

$$
\left| { \frac { 1 } { n } } { \Big ( } { \frac { 1 } { 2 } } f ( x _ { 0 } ) + f ( x _ { 1 } ) + \cdots + f ( x _ { n - 1 } ) + { \frac { 1 } { 2 } } f ( x _ { n } ) { \Big ) } - \int _ { a } ^ { b } f ( x ) \mathrm { d } x \right| \leq { \frac { M } { n ^ { 2 } } } .
$$

[Recall that the sum is an approximation of the integral in the Trapezoid Rule. It may be instructive to first solve the problem for $n = 1$ and then address the general case.]

Problem 4. Consider a decreasing sequence of continuous functions $f _ { n } \colon [ 0 , 1 ] \to \mathbb { R }$ obeying the uniform bound $| f _ { n } | \ \leq \ M$ for some $M \ \in \ ( 0 , 1 )$ Suppose the point-wise limit $f ( x ) =$ $\scriptstyle \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x )$ is continuous on [0, 1]. Prove that $f _ { n } \to f$ uniformly on [0, 1]. [You may use without proof that [0, 1] is compact as well as sequentially compact.]

Problem 5. Consider a function $f ( x , y )$ which is twice continuously differentiable. Suppose that f has its unique minimum at $( x , y ) = ( 0 , 0 )$ . Carefully prove that then at (0, 0),

$$
{ \frac { \partial ^ { 2 } f } { \partial x ^ { 2 } } } { \frac { \partial ^ { 2 } f } { \partial y ^ { 2 } } } \geq \left( { \frac { \partial ^ { 2 } f } { \partial x \partial y } } \right) ^ { 2 }
$$

[You may use without proof that the mixed partials are equal for $C ^ { 2 }$ functions.]

Problem 6. Let $- \infty < a < b < \infty$ Prove that a continuous function $f \colon [ a , b ] \to \mathbb { R }$ attains all values in $[ f ( a ) , f ( b ) ]$

Problem 7. Let V be a complex inner product space and $v , w \in V$ Prove the Cauchy-Schwarz inequality

$$
| ( v , w ) | \leq | v | | w | .
$$

Problem 8. Let $T \colon V \to W$ be a linear transformation of finite dimensional real inner product spaces. Show that there exists a unique linear transformation $T ^ { t } \colon W \to V$ such that

$$
\langle T ( v ) , w \rangle _ { W } = \langle v , T ^ { t } ( w ) \rangle _ { V } \mathrm { f o r a l l } v \in V \mathrm { a n d } w \in W
$$

where $\langle ~ , ~ \rangle _ { X }$ is the inner product on $X = V$ or W.

Problem 9. Let $A \in \mathbb { M } _ { 3 } ( \mathbb { R } )$ be invertible and satisfy $A = A ^ { t }$ and det $A = 1$ . Prove that A has one as an eigenvalue.

Problem 10. Let $T \colon V \to V$ be a linear operator on a finite dimensional complex inner product space. Show that there exists an ordered orthonormal basis for V such that the matrix representation A of T in this basis is upper triangular, i.e, $A = \left( a _ { i j } \right)$ with $a _ { i j } = 0 { \mathrm { i f } } j < i$

[You cannot use canonical form theorems without proof.]