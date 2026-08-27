## Basic Exam, Spring 2007

1. Let A be a real m x n matrix, $m > n ,$ , whose columns are linearly independent and b $\in \mathbb { R } ^ { m }$ Show that the vector $\mathbf { x ^ { * } } \in \mathbb { R } ^ { n }$ that minimizes the functional

$$
g ( \mathbf { x } ) = | | A \mathbf { x } - \mathbf { b } | | _ { 2 } ^ { 2 }
$$

is given by the solution of the normal equations

$$
A ^ { t } A \mathbf { x } = A ^ { t } \mathbf { b } .
$$

Here $\begin{array} { r } { \vert \vert \mathbf { z } \vert \vert _ { 2 } ^ { 2 } = \langle \mathbf { z } , \mathbf { z } \rangle = \sum _ { i } z _ { i } ^ { 2 } . } \end{array}$

2. Let $V , W , Z$ be n-dimensional vector spaces and $T : V \to W$ and $U : W \to Z$ be linear transformations. Prove that if the composite transformation $U T : V \to Z$ is invertible, then both T and U are invertible. (Do not use determinants in your proof!)

3. Consider the space of infinite sequences of real numbers

$$
{ \mathcal { S } } = \left\{ ( a _ { 0 } , a _ { 1 } , a _ { 2 } , . . . ) : a _ { n } \in \mathbb { R } , n = 0 , 1 , 2 , . . . \right\}
$$

endowed with the standard operations of addition and scalar multiplication:

$$
( a _ { 0 } , a _ { 1 } , \ldots ) + ( b _ { 0 } , b _ { 1 } , \ldots ) = ( a _ { 0 } + b _ { 0 } , a _ { 1 } + b _ { 1 } , \ldots ) ; \quad c ( a _ { 0 } , a _ { 1 } , \ldots ) = ( c a _ { 0 } , c a _ { 1 } , \ldots ) , \quad c \in \mathbb { R } .
$$

For each pair of real numbers A and B, prove that the set of solutions $( x _ { 0 } , x _ { 1 } , x _ { 2 } , \ldots )$ of the linear recursion

$$
x _ { n + 2 } = A x _ { n + 1 } + B x _ { n } , \quad n = 0 , 1 , 2 , \ldots
$$

is a linear subspace of S of dimension 2.

4. Suppose that A is a symmetric $n \times n$ real matrix with distinct eigenvalues $\lambda _ { 1 } , . . . , \lambda _ { l } , ( l \leq n )$ Find the sets

$$
X = \left\{ \mathbf { x } \in \mathbb { R } ^ { n } : \operatorname* { l i m } _ { k \to \infty } ( \mathbf { x } ^ { t } A ^ { 2 k } \mathbf { x } ) ^ { 1 / k } { \mathrm { ~ e x i s t s } } \right\}
$$

and

$$
L = { \biggl \{ } \operatorname* { l i m } _ { k \to \infty } ( \mathbf { x } ^ { t } A ^ { 2 k } \mathbf { x } ) ^ { 1 / k } : x \in X { \biggr \} } ,
$$

where $\mathbb { R } ^ { n }$ is identified with the set of real column vectors, and xt denotes the transpose of x. $\mathbf { x } ^ { t }$

5. Let T be a normal linear operator on a finite dimensional complex inner product linear space V. Prove that if v is an eigenvector of T, then v is also an eigenvector of its adjoint $T ,$ $T ^ { * }$

6. Consider the integral equation

$$
y ( t ) = y _ { 0 } + \int _ { 0 } ^ { t } f ( s , y ( s ) ) d s\tag{*}
$$

where $f ( t , y )$ is continuous on $[ 0 , T ] \times \mathtt { R }$ and is Lipschitz in y with Lipschitz constant K. Assume that you have shown that the iterates defined by

$$
y ^ { n } ( t ) = y _ { 0 } + \int _ { 0 } ^ { t } f ( s , y ^ { n - 1 } ( s ) ) d s , \quad y ^ { 0 } ( t ) \equiv y _ { 0 }
$$

converge uniformly to a solution $y ( t )$ of $( ^ { * } )$ . Show that if $Y ( t )$ is a solution of $( ^ { * } )$ and satisfies $| Y ( t ) - y _ { 0 } | \le C$ for some constant $C$ and all $t \in [ 0 , T ]$ , then $Y ( t ) \equiv y ( t )$ on [0, T].

7. Let $f : \mathbb { R }  \mathbb { R }$ be a twice continuously differentiable function with $f ^ { \prime \prime }$ uniformly bounded, and with a simple root at $x ^ { * } \ ( \mathrm { i . e . , } \ f ( x ^ { * } ) = 0 , f ^ { \prime } ( x ^ { * } ) \neq 0 )$ . Consider the fixed point iteration

$$
x _ { n } = F ( x _ { n - 1 } ) \qquad { \mathrm { w h e r e } } \qquad F ( x ) = x - { \frac { f ( x ) } { f ^ { \prime } ( x ) } } .
$$

Show that if $x _ { 0 }$ is sufficiently close to $x ^ { * }$ , then there exists a constant $C$ so that for all $n ,$

$$
| x _ { n } - x ^ { * } | \leq C | x _ { n - 1 } - x ^ { * } | ^ { 2 } .
$$

8. Suppose the functions $f _ { n }$ are twice continuously differentiable on [0, 1] and satisfy

lim fn(x) = f(x) for all $x \in [ 0 , 1 ]$ , and n→∞

$$
| f _ { n } ^ { \prime } ( x ) | \leq 1 , \quad | f _ { n } ^ { \prime \prime } ( x ) | \leq 1 \quad { \mathrm { f o r ~ a l l ~ } } x \in [ 0 , 1 ] , \ n \geq 1 .
$$

Prove that $f ( x )$ is continuously differentiable on [0, 1].

9. (a) Define $^ { 6 6 } f$ is Riemann integrable on $[ 0 , 1 ] "$

(b) Prove that every continuous function on [0, 1] is Riemann integrable.

10. Suppose the functions $f _ { n } ( x )$ on R satisfy:

(i) $0 \leq f _ { n } ( x ) \leq 1$ for all $\textstyle x \in \mathbb { R }$ and $n \geq 1$

(ii) $f _ { n } ( x )$ is increasing in x for every $n \geq 1$

(iii) $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } f _ { n } ( x ) = f ( x ) } \end{array}$ for each $x \in \mathbb { R }$ , where f is continuous on R.

(iv) lim $\mathfrak { i } _ { x \to - \infty } f ( x ) = 0$ and $\begin{array} { r } { \operatorname* { l i m } _ { x \to \infty } f ( x ) = 1 } \end{array}$

Show that $f _ { n } ( x )  f ( x )$ uniformly on R.

11. (a) Consider the equations

$$
u ^ { 3 } + x v - y = 0 , \quad v ^ { 3 } + y u - x = 0 .
$$

Can these equations be solved uniquely for $u , v$ in terms of $x , y$ in a neighborhood of $x =$ $0 , y = 1 , u = 1 , v = - 1 ?$ Explain your answer.

(b) Give an example in which the conclusion of the implicit function theorem is true but the hypothesis is not.

12. Let $c _ { 0 }$ be the normed space of real sequences $\boldsymbol { x } = ( x _ { 1 } , x _ { 2 } , \ldots )$ such that $\scriptstyle \operatorname* { l i m } _ { k \to 0 } x _ { k } = 0$ with the supremum norm $\left| \left| \boldsymbol { x } \right| \right| = \operatorname* { s u p } _ { k } \left| x _ { k } \right| .$

(a) Show that $c _ { 0 }$ is complete.

(b) Is the unit ball $\{ x \in c _ { 0 } : \| x \| \leq 1 \}$ compact? Prove your answer.

(c) Is the set $\textstyle \left\{ x \in c _ { 0 } : \sum _ { k } k | x _ { k } | \leq 1 \right\}$ compact? Prove your answer.