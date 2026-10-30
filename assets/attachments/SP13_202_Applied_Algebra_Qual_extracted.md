# Applied Algebra Qualifying Exam: Part I

9:00am–Noon, AP&M 6402   
Tuesday May 28th, 2013

Name

<table><tr><td>#1</td><td>20</td><td></td></tr><tr><td>#2</td><td>20</td><td></td></tr><tr><td>#3</td><td>20</td><td></td></tr><tr><td>#4</td><td>20</td><td></td></tr><tr><td>Total</td><td>80</td><td></td></tr></table>

• Do all four problems.

• This part of the exam will represent 40% of your total score.

• Add your name in the box provided and staple this page to your solutions.

• Notation:

$\mathcal { M } _ { m , n }$ denotes the set of $m \times n$ matrices with complex entries.

$\mathrm { I f } \ m = n , \ M _ { m , n }$ is denoted by $\mathcal { M } _ { n }$

– Cn is the set of column vectors with n complex entries.

$x ^ { H }$ is the Hermitian transpose of a vector or matrix x.

– eig(A) is the set of eigenvalues of the matrix A (counting multiplicities).

– Re(λ) and Im(λ) denote the real and imaginary parts of the scalar λ.

## Question 1.

(a) (8 points) Prove the Schur decomposition theorem for a matrix $A \in M _ { n }$

(b) (12 points) Prove that for A, $B \in \mathcal { M } _ { n }$ , if $x ^ { H } A x = x ^ { H } B x$ for all $x \in \mathbb { C } ^ { n }$ , then $A = B$

## Question 2.

(a) (10 points) Prove that every $A \in \mathcal { M } _ { n }$ may be written uniquely as $A = S + i T$ where S and T are Hermitian.

(b) (10 points) For any $A \in \mathcal { M } _ { n }$ , consider the unique expansion $A = S + i T$ , where S and T are Hermitian. Prove that for any $\lambda \in \mathrm { e i g } ( A )$ , it holds that

$$
\lambda _ { n } ( S ) \leq \operatorname { R e } ( \lambda ) \leq \lambda _ { 1 } ( S ) \quad { \mathrm { a n d } } \quad \lambda _ { n } ( T ) \leq \operatorname { I m } ( \lambda ) \leq \lambda _ { 1 } ( T ) ,
$$

where, by convention, the eigenvalues of a Hermitian matrix $C \in \mathcal { M } _ { n }$ are arranged in nonincreasing order, i.e.,

$$
\lambda _ { 1 } ( C ) \geq \lambda _ { 2 } ( C ) \geq \cdots \geq \lambda _ { n } ( C ) .
$$

## Question 3.

(a) (4 points.) Define the p-norm $\| A \| _ { p }$ and Frobenius norm $\| A \| _ { F }$ of a matrix $A \in \mathcal { M } _ { m , n } .$

(b) (10 points) Suppose that $D \in \mathcal { M } _ { n }$ with $D = \operatorname { d i a g } ( d _ { 1 } , d _ { 2 } , \dotsc , d _ { n } )$ . Prove that for all $1 \leq p \leq \infty$ the p-norm of D is given by $\lVert D \rVert _ { p } = \operatorname* { m a x } _ { 1 \leq i \leq n } \left| d _ { i } \right|$

(c) (6 points) Given $b \in \mathbb { C } ^ { n - 1 }$ , find $\| B \| _ { 2 }$ for the matrices

$$
B = \left( \begin{array} { c c } { { 0 } } & { { b ^ { H } } } \\ { { b } } & { { 0 } } \end{array} \right) \quad \mathrm { a n d } \quad B = b b ^ { H } .
$$

(Show your work. Simply writing down the answer will not be sufficient.)

## Question 4.

(a) (15 points) Prove that if $A \in { \mathcal { M } } _ { n }$ is positive semidefinite, then there exists a unique positive semidefinite X such that $A = X ^ { 2 }$

(b) (5 points) Let X be a matrix whose columns define a basis for a subspace $\mathcal { X } \subset \mathbb { C } ^ { n }$ . Consider the matrix ${ \widehat { X } } = X | X | ^ { - 1 }$ , where $| X |$ denotes the modulus of $X , \mathrm { i . e . , } | X | = ( X ^ { H } X ) ^ { \frac { 1 } { 2 } }$ . Prove that $\widehat { X }$ exists and that $\widehat { X } \widehat { X } ^ { H }$ is an orthogonal projection onto X .

# Applied Algebra Qualifying Exam: Part II May 28, 2013

Do as many problems as you can, but you must attempt at least 5 problems where two of the problems are from problems 1-5, one problem for 6-7, and one problem are from problems 8-9. The point values are relative values for this part of the exam. Your final score will be scaled so that this part of the exam will represent 60% of your point total.

Let $\mathbb { N } = \{ 0 , 1 , 2 , . . . \} , \mathbb { Z } = \{ 0 , \pm 1 , \pm 2 , . . . \}$ , Q equal the rationals and C denote the complex numbers. Suppose that $\lambda = ( \lambda _ { 1 } \geq \lambda _ { 2 } \geq . . . \geq \lambda _ { k } )$ is a partition of n. Then $A ^ { \lambda }$ denotes the irreducible representation of the symmetric group $S _ { n }$ such that the Frobenius image of $\chi ^ { A ^ { \lambda } } = \chi ^ { \lambda }$ is the Schur function $S _ { \lambda } ( x _ { 1 } , \dots , x _ { N } )$ where $N > n$ and $S _ { \lambda _ { 1 } } \times \cdots \times S _ { \lambda _ { k } }$ denotes the Young subgroup of $S _ { n }$ corresponding to λ.

(1)(30 pts.) Let H be a subgroup of G and $A : H \to G L _ { n } ( \mathbb { C } )$ be a representation of H. Let $\chi ^ { A } : H \to \mathbb { C }$ be the character of A. Define $\chi ^ { \overline { { A } } } : G \to \mathbb { C }$ by

$$
\chi ^ { \overline { { A } } } ( \sigma ) = \left\{ \begin{array} { l l } { { \chi ^ { A } ( \sigma ) } } & { { \mathrm { i f ~ } \sigma \in H \mathrm { ~ a n d } } } \\ { { 0 } } & { { \sigma \in G - H . } } \end{array} \right.
$$

(a) Define the representation $A \uparrow _ { H } ^ { G }$

(b) Prove that $\begin{array} { r } { \chi ^ { A \uparrow _ { H } ^ { G } } = \frac { 1 } { | H | } \sum _ { \sigma \in G } \sigma \cdot \chi ^ { \overline { { A } } } \cdot \sigma ^ { - 1 } } \end{array}$

(c) State and prove the Frobenius Reciprocity Theorem.

(2) (40 pts)

(a) Compute the values of the character $\chi ^ { ( 1 , 2 ^ { 2 } ) }$ on the conjugacy classes of $S _ { 5 }$

(b) Find the character table of $S _ { 3 } \times S _ { 2 }$

(c) Decompose the $A ^ { ( 1 , 2 ^ { 2 } ) } \downarrow _ { S _ { 3 } \times S _ { 2 } } ^ { S _ { 5 } }$ as a sum of irreducible characters of $S _ { 3 } \times S _ { 2 }$

(3) (40 pts) Let Q be the quaternion group of order 8 defined by the relations

$$
a ^ { 4 } = 1 , \ a ^ { 2 } = b ^ { 2 } , \ \mathrm { a n d } \ b ^ { - 1 } a b = a ^ { 3 } .
$$

(a) Show that ba $\mathbf { \Delta } = { a b ^ { 3 } } \mathbf { \Delta } = { a ^ { 3 } b }$ and, hence, that every element of Q is of the form $a ^ { i }$ or $a ^ { i } b$ for some $i \in \{ 0 , 1 , 2 , 3 \}$

(b) Verify that the conjugacy classes of G are $C _ { 1 } \ = \ \{ 1 \} , \ C _ { 2 } \ = \ \{ a ^ { 2 } \} , \ C _ { 3 } \{ a , a ^ { 3 } \} , \ C _ { 4 } \ = \ \{ b , a ^ { 2 } b \}$ , and $\dot { C } _ { 5 } = \{ a b , a ^ { 3 } b \}$

c) Show that $H = \{ 1 , a ^ { 2 } \}$ is a normal subgroup of G for which G/H is isomorphic to $Z _ { 2 } \times Z _ { 2 }$

(d) Give the character character table for the lifting of the four linear characters of $Q / H$ to $Q .$

(e) Use parts (c) and (d) to give the complete character table for Q.

(4) (30 pts)

(a) Let T denote the trivial representation on the Young subgroup $S _ { 2 } \times S _ { 3 } \times S _ { 1 }$ of $S _ { 6 }$ and Alt denote the alternating representation on the Young subgroup $S _ { 2 } \times S _ { 3 } \times S _ { 1 }$ of $S _ { 6 }$ . Express the characters of

$$
T \uparrow _ { S _ { 2 } \times S _ { 3 } \times S _ { 1 } } ^ { S _ { 6 } } \mathrm { a n d } A l t \uparrow _ { S _ { 2 } \times S _ { 3 } \times S _ { 1 } } ^ { S _ { 6 } } .
$$

as a sum of irreducible characters of $S _ { 6 }$

(b) Find the decomposition of the Kronecker product $A ^ { ( 1 , 4 ) } \otimes A ^ { ( 1 , 2 ^ { 2 } ) }$ as a sum of irreducible representations of $S _ { 5 }$

(c) Find the decomposition of $A ^ { ( 1 , 2 ) } \times A ^ { ( 1 , 3 ) } \uparrow _ { S _ { 3 } \times S _ { 4 } } ^ { S ^ { 7 } }$ as a sum of irreducible representations of $S _ { 7 }$

(5) (40 pts.) Let G and H be finite groups and let $A : G \to G L _ { n } ( C )$ and ${ \cal B } : { \cal H }  { \cal G } L _ { m } ( C )$ be representations of G and H respectively.

a) Show that $A \times B : G \times H \to G L _ { n m } ( C )$ is representation where for $( \sigma , \tau ) \in G \times H$

$$
A \times B ( ( \sigma , \tau ) ) = A ( \sigma ) \otimes B ( \tau )
$$

and for matrices M and $N , M \otimes N$ is the Kronecker product of M and N .

b) Show that $A \times B$ is an irreducible representation of $G \times H$ if and only if A is an irreducible representation of G and B is an irreducible representation of H.

c) Show that every irreducible representation of $G \times H$ is of the form $A \times B$ where A is an irreducible representation of G and B is an irreducible representation of H.

(d) Show that it is not always the case that if C is a representation of $G \times H$ then C is similar to a representation of the form $A \times B : G \times H \to G L _ { n } ( \mathbb { C } )$ where A is representation of G and B is representation of H. (Hint: Consider the two dimensional representations of $S _ { 2 } \times S _ { 2 } . )$

(6) (40 pts.) Consider the equations

$$
\begin{array} { l l l } { { x ^ { 2 } - x y - 2 x } } & { { = } } & { { 0 } } \\ { { y ^ { 2 } - 2 x y - y } } & { { = } } & { { 0 } } \end{array}
$$

(a) Let I be the ideal of ${ \bf C } [ \boldsymbol { x } , \boldsymbol { y } ]$ generated by these equations. Find the reduced Groebner basis for I relative to lexicographic order where $y > x$

(b) Find a reduced Groebner basis for $\mathbf { C } [ { \boldsymbol { x } } ] \cap I$

(c) Find all solutions to these equations that lie $\mathbf { C } ^ { 2 }$

(d) Find a vector space basis for $\mathbf { C } [ x , y ] / I$

(7) (30 pts.) Let S be the parametric surface defined by

$$
\begin{array} { r l r } { x } & { { } = } & { u - 2 v } \end{array}
$$

$$
\begin{array} { r l r } { y } & { { } = } & { u v } \end{array}
$$

$$
 { \boldsymbol { z } }  { \boldsymbol { { \mathbf { \mathit { z } } } } } = { \boldsymbol { { \mathbf { \mathit { v } } } } }
$$

(a) Compute a reduced Groebner basis for the ideal generated by this set of equations relative to the lexicographic order where $u > v > x > y > z$

(b) Find the equation of the smallest variety V that contains S.

(c) Show that $S = V .$

(8) $\mathrm { ( 4 0 ~ p t s . ) }$ Let k be an algebraically closed field.

Two ideals I and J of $k [ x _ { 1 } , \dots , x _ { n } ]$ are said to be comaximal if and only if $I + J = k [ x _ { 1 } , \ldots , x _ { n } ]$

(a) State the Weak Nullstellenszat and Hilbert’s Nullstellensatz Theorem.

(b) Show that two ideals I and J are comaximal if and only if $V ( I ) \cap V ( J ) = \emptyset$

(c) Show that if I and J are ideals in $k [ x _ { 1 } , \dots , x _ { n } ]$ , then $I \cap J = ( t I + ( 1 - t ) J ) \cap k [ x _ { 1 } , \dotsc , x _ { n } ]$

(d) Show that if $I = \langle f \rangle$ and $J = \langle f \rangle$ , then $I \cap J = \langle h \rangle$ where h is a least common multiple of f and g.

(9) (30 pts.) Let $A = { \binom { 0 } { 1 } } \ { \begin{array} { l } { { - 1 } } \\ { { - 1 } } \end{array} } { \biggr ) }$

(a) Show that A generates a matrix group G of order three.

(b) Find a set of homogeneous G-invariant polynomials which generate $\mathbb { C } [ x , y ] ^ { G }$

(c) Compute the Hilbert Series of $\mathbb { C } [ x , y ] ^ { G }$