# Basic Examination September, 2005

Do all problems

1. A real number α is said to be algebraic if for some finite set of integers $a _ { 0 } , \ldots , a _ { n } .$ not all 0,

$$
a _ { 0 } + a _ { 1 } \alpha + \cdot \cdot \cdot + a _ { n } \alpha ^ { n } = 0 .
$$

Prove that the set of algebraic real numbers is countable.

2. State some reasonable conditions on a real-valued function $f ( x , y )$ on $\mathbb { R } ^ { 2 }$ which guarantee that ${ \frac { \partial ^ { 2 } f } { \partial x d y } } = { \frac { \partial ^ { 2 } f } { \partial y \partial x } }$ at every point of $\mathbb { R } ^ { 2 }$ . Then prove that your conditions do in fact guarantee this equality.

3. (a) Prove that if $f _ { j } : [ 0 , 1 ] \to \mathbb { R }$ is a sequence of continuous functions which converges uniformly on $[ 0 , 1 ]$ to a (necessarily continuous) function $F : [ 0 , 1 ]  \mathbb { R }$ then

$$
\int _ { 0 } ^ { 1 } F ^ { 2 } ( x ) d x = \operatorname* { l i m } \int _ { 0 } ^ { 1 } f _ { j } ^ { 2 } ( x ) d x .
$$

(b) Give an example of a sequence $f _ { j } : [ 0 , 1 ] \to \mathbb { R }$ of continuous functions which converges to a continuous function $F : [ 0 , 1 ]  \mathbb { R }$ pointwise and for which

$$
\begin{array} { c } { { \displaystyle \operatorname* { l i m } \int _ { 0 } ^ { 1 } f _ { j } ^ { 2 } ( x ) d x \quad \mathrm { e x i s t s ~ b u t } } } \\ { { \displaystyle \operatorname* { l i m } \int _ { 0 } ^ { 1 } f _ { j } ^ { 2 } ( x ) d x \neq \int _ { 0 } ^ { 1 } F ^ { 2 } ( x ) d x } } \end{array}
$$

$( f _ { j }$ converges to F "pointwise" means that for each $x \in [ 0 , 1 ] , F ( x ) = \operatorname* { l i m } f _ { j } ( x ) )$

4. Suppose $F : [ 0 , 1 ]  [ 0 , 1 ]$ is a $C ^ { 2 }$ function with $F ( 0 ) = 0 , F ( 1 ) = 0$ , and $F ^ { \prime \prime } ( x ) < 0$ for all $x \in [ 0 , 1 ]$ . Prove that the arc length of the curve $\{ ( x , F ( x ) ) : x \in [ 0 , 1 ] \}$ is less than 3. (Suggestion: Remember that ${ \sqrt { a ^ { 2 } + b ^ { 2 } } } < | a | + | b |$ when you are looking at the arc length formula - and at picture of what $\{ ( x , f ( x ) \}$ could look like.)

5. Prove carefully that $\mathbb { R } ^ { 2 }$ is not a (countable) union of sets $S _ { i } , i = 1 , 2 \dots$ . with each $S _ { i }$ being a subset of some straight line $L _ { i }$ in $\mathbb { R } ^ { 2 }$

6. (a) Prove that if P is a real-coefficient polynomial and if A is a real symmetric matrix, then the eigenvalues of $P ( A )$ are exactly the numbers $P ( \lambda )$ , where λ is an eigenvalue of A.

(b) Use part (a) to prove that if A is a real symmetric matrix, then $A ^ { 2 }$ is nonnegative definite.

(c) Check part (b) by verifying directly that det $A ^ { 2 }$ and $\operatorname { t r a c e } ( A ^ { 2 } )$ are nonnegative when A is real symmetric.

7. Let A be a real $n \times m$ matrix. Prove that the maximum number of linearly independent rows of $A =$ the maximum number of linearly independent columns. ("Row rank = column rank").

8. For a real $n \times n$ matrix A, let $T _ { A } : \mathbb { R } ^ { n }  \mathbb { R } ^ { n }$ be the associated linear mapping. Set $\| A \| = \operatorname* { s u p } _ { { \vec { x } } \in \mathbb { R } ^ { n } } \| , \| { \vec { x } } \| = 1$ (here $\| { \vec { x } } \| =$ usual euclidean norm, i.e.

$$
\| ( x _ { 1 } , \dots , x _ { n } ) \| = ( x _ { 1 } ^ { 2 } + \cdot \cdot \cdot + x _ { n } ^ { 2 } ) ^ { 1 / 2 } ) .
$$

(a) Prove that $\| A + B \| \leq A \| + \| B \|$

(b) Use part (a) to check that the set M of all $n \times n$ matrices is a metric space if the distance function d is defined by

$$
d ( A , B ) = \lVert B - A \rVert .
$$

(c) Prove that M is a complete metric space with this "distance function". (Suggestion: The ijth element of $A = \langle T _ { A } e _ { j } , e _ { i } \rangle$ where $e _ { i } = ( 0 , \ldots , 1 \ldots 0 )$ , 1 in ith position.)

9. Suppose $V _ { 1 }$ and $V _ { 2 }$ are subspaces of a finite-dimensional vector space V.

(a) Show that

$$
\dim ( V _ { 1 } \cap V _ { 2 } ) = \dim ( V _ { 1 } ) + \dim ( V _ { 2 } ) - \dim ( \operatorname { s p a n } ( V _ { 1 } , V _ { 2 } ) )
$$

where span $( V _ { 1 } , V _ { 2 } )$ is by definition the smallest subspace that contains both $V _ { 1 }$ and

(b) Let $n =$ dim V. Use part (a) to show that, if $k < n$ ,then an intersection of k subspaces of dimension $n - 1$ always has dimension at least $n - k$ (Suggestion: Do induction on k

10. (a) For each $n = 2 , 3 , 4 , \dots ,$ is there an $n \times n$ matrix A with $A ^ { n - 1 } \neq 0$ but $A ^ { n } = 0 ?$ (Give example or proof of nonexistence.)

(b) Is there an $n \times n$ upper triangular matrix A with $A ^ { n } \neq 0$ but $A ^ { n + 1 } = 0 ?$ (Give example or proof of nonexistence.)

[Note: A square matrix is upper triangular if all the entries below the main diagonal are 0.]