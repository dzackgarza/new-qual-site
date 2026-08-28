# Math 150-01 Linear Algebra Final Exam Review Sheet

## Vector Operations

• Vector addition is a component-wise operation.
Two vectors v and w may be added together as long as they contain the same number n of components.
Their sum is another vector, whose ith component is the sum of the ith components of v and w:

$$
{ \Big [ } { \begin{array} { l } { 1 } \\ { 2 } \end{array} } { \Big ] } + { \Big [ } { \begin{array} { l } { 3 } \\ { 4 } \end{array} } { \Big ] } = { \Big [ } { \begin{array} { l } { 4 } \\ { 6 } \end{array} } { \Big ] }
$$

• Vectors may be multiplied by a scalar.
The product cv is a vector, whose ith component is the product of c and the ith component of v:

$$
5 \left[ { \binom { 1 } { 2 } } \right] = \left[ { \binom { 5 } { 10 } } \right]
$$

• A linear combination of vectors is a sum of scalar multiples of vectors (with the same number of components):

$$
5 \left[ 1 \right] + 6 \left[ 4 \right] - 3 \left[ - 1 \right] + \frac { 1 } { 2 } \left[ - 3 \right]
$$

• The dot product of two vectors is a scalar, and is only defined when the vectors have the same number of components.
It is the sum of the products of the ith components of the vectors:

$$
{ \big [ } 1 , 2 { \big ] } \cdot { \big [ } 3 , 4 { \big ] } = ( 1 ) ( 3 ) + ( 2 ) ( 4 )
$$

• The length of a vector is a scalar.
It is found by taking the square root of the sum of the squares of the vector’s components:

$$
\left\| { \left[ 1 , 2 , 3 \right] } \right\| = { \sqrt { 1 ^ { 2 } + 2 ^ { 2 } + 3 ^ { 2 } } }
$$

• A unit vector is a vector of length one.
For example, $[ 1 , 0 , 0 ]$ and $[ 1 / \sqrt { 2 } , 1 / \sqrt { 2 } ]$ are unit vectors.

• The angle θ between two vectors v and w is related to their lengths and dot products by the formula

$$
\cos ( \theta ) = \frac { \mathbf { v } \cdot \mathbf { w } } { \| \mathbf { v } \| \| \mathbf { w } \| }
$$

• Two vectors are perpendicular (also called orthogonal) if they have a dot product of 0.

## Matrix Operations

• Matrix addition is a component-wise operation.
Two matrices A and B may be added together as long as they have the same number of rows and columns.
Their sum is another matrix, whose (i, j)th entry is the sum of the $( i , j )$ th entries of A and B:

$$
{ \begin{array} { r } { { \left[ \begin{array} { l l } { 1 } & { 2 } \\ { 3 } & { 4 } \end{array} \right] } + { \left[ \begin{array} { l l } { 5 } & { 6 } \\ { 7 } & { 8 } \end{array} \right] } = { \left[ \begin{array} { l l } { 1 + 5 } & { 2 + 6 } \\ { 3 + 7 } & { 4 + 8 } \end{array} \right] } } \end{array} }
$$

• Matrices may be multiplied by a scalar.
The product cA is a matrix, whose (i, j)th entry is the product of c and the (i, j)th entry of A:

$$
5 \left[ { \begin{array} { c c } { 1 } & { 2 } \\ { 3 } & { 4 } \end{array} } \right] = \left[ { \begin{array} { c c } { ( 5 ) ( 1 ) } & { ( 5 ) ( 2 ) } \\ { ( 5 ) ( 3 ) } & { ( 5 ) ( 4 ) } \end{array} } \right]
$$

• Matrices may be multiplied as long as their dimensions are compatible.
The product AB is defined when A has n columns and B has n rows.
The (i, j)th entry of AB is the dot product of the ith row of A and the jth column of B:

$$
{ \begin{array} { r l } { { \left[ \begin{array} { l l l } { 1 } & { 2 } & { 3 } \\ { 4 } & { 5 } & { 6 } \end{array} \right] } { \left[ \begin{array} { l l } { 7 } & { 8 } \\ { 9 } & { 10 } \\ { 11 } & { 12 } \end{array} \right] } = { \left[ \begin{array} { l l } { ( 1 ) ( 7 ) + ( 2 ) ( 9 ) + ( 3 ) ( 11 ) } & { ( 1 ) ( 8 ) + ( 2 ) ( 10 ) + ( 3 ) ( 12 ) } \\ { ( 4 ) ( 7 ) + ( 5 ) ( 9 ) + ( 6 ) ( 11 ) } & { ( 4 ) ( 8 ) + ( 5 ) ( 10 ) + ( 6 ) ( 12 ) } \end{array} \right] } } \end{array} }
$$

• Matrix multiplication is not commutative.
In general, $A B \neq B A$

• The transpose of a matrix A, denoted $A ^ { T }$ , is the matrix whose (i, j)th entry is the (j, i)th entry of A:

$$
A = { \left[ \begin{array} { l l l } { 1 } & { 2 } & { 3 } \\ { 4 } & { 5 } & { 6 } \end{array} \right] } \qquad \Rightarrow \qquad A ^ { T } = { \left[ \begin{array} { l l } { 1 } & { 4 } \\ { 2 } & { 5 } \\ { 3 } & { 6 } \end{array} \right] }
$$

## Reduced Echelon Form

• A matrix is in reduced row echelon form (RREF) when

1. All rows containing nonzero entries are above any rows containing only zero

2. The first nonzero entry (from the left) in each row, called a pivot, is strictly to the right of the first nonzero entry of any rows above it

3. All entries above and below a pivot are 0

4. The pivot entries are all 1

The following matrices are in reduced row echelon form:

$$
\left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 2 } \\ { 0 } & { 1 } & { 0 } & { 3 } \\ { 0 } & { 0 } & { 1 } & { 5 } \end{array} \right] , \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 2 } \\ { 0 } & { 1 } & { 0 } & { - 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] , \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 3 } & { - 2 } \\ { 0 } & { 1 } & { 2 } & { 4 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] , \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 8 } \\ { 0 } & { 0 } & { 1 } & { 3 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right]
$$

• A matrix can be brought to its RREF by elementary row operations:

1. interchanging two rows

2. adding a multiple of one row to another

3. multiplying a row by a scalar

• The rank of a matrix is the number of pivots that appear in its RREF. The matrices above have rank 3, 2, 2, and 3, respectively.

## Some Special Matrices

• The identity matrix $I _ { n }$ is an n × n matrix whose diagonal entries are 1, and whose remaining entries are 0. It is the multiplicative identity, because if A is any m × n matrix, $A I _ { n } = I _ { m } A = A$ When the size n is understood, we can simply write I for the identity matrix.

• A zero matrix 0 is a matrix with every entry 0. It can be any size, and not necessarily square.
A zero matrix is never invertible.
It is the additive identity, since $A + 0 = 0 + A = A$ for any matrix A.

• An elementary matrix E is a square matrix which performs a row operation on a matrix A. There are three types of elementary matrices, all of which are invertible:

1. E can interchange two rows.
   An elementary matrix of this type is obtained from the identity by interchanging two of its rows.
   Such a matrix E is equal to its own inverse:

$$
E = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } \end{array} \right] } \qquad E ^ { - 1 } = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } \end{array} \right] }
$$

2. E can multiply a row by a constant, c. An elementary matrix of this type is obtained from the identity by multiplying one of its rows by c. Its inverse is obtained from the identity by multiplying one of its rows by $1 / c$:

$$
E = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { c } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] }
$$

$$
E ^ { - 1 } = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 / c } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] }
$$

3. E can add a multiple of one row to another.
   An elementary matrix of this type is obtained from the identity by making any off diagonal entry $c \neq 0$ . Its inverse is obtained from the identity by making that same off diagonal entry −c:

$$
E = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { c } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } \qquad E ^ { - 1 } = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { - c } \\ { 0 } & { 0 } & { 1 } \end{array} \right] }
$$

• A diagonal matrix is one whose main diagonal entries can take any value, but whose entries off the main diagonal are 0. It is invertible if all diagonal entries are nonzero.

• An upper triangular matrix is one whose main diagonal entries, as well as any entries above the diagonal, can take any value, but whose entries below the main diagonal are 0.

• A lower triangular matrix is one whose main diagonal entries, as well as any entries below the diagonal, can take any value, but whose entries above the main diagonal are 0.

• A symmetric matrix is one that is equal to its own transpose, $A = A ^ { T }$ . These can have any value on the main diagonal, but entries off the main diagonal must be paired: the (i, j)th entry must be equal to the (j, i)th entry.

• A permutation matrix is a square matrix such that every row and column contains exactly one entry of 1 and zeros elsewhere.
There are n! permutation matrices of size $n \times n$

• An orthogonal matrix is one whose transpose is equal to its inverse: $A ^ { T } = A ^ { - 1 }$

## Matrix Inverses

• The inverse of a square matrix A is the unique matrix $A ^ { - 1 }$ such that $A A ^ { - 1 } = A ^ { - 1 } A = I$

• Not all matrices are invertible.
If A has any of the following properties, it is NOT invertible:

1. A is not square

2. A has determinant 0

3. the rows or columns of A are not linearly independent

4. the equation $A x = 0$ has more than one solution

5. A has at least one eigenvalue of 0

• If a square $n \times n$ matrix has rank n, it is invertible.
Its RREF is the identity.

• If A and B are invertible $n \times n$ matrices, then their product is invertible, and $( A B ) ^ { - 1 } = B ^ { - 1 } A ^ { - 1 }$

• If A is invertible, then $A ^ { T }$ is invertible, and $( A ^ { T } ) ^ { - 1 } = ( A ^ { - 1 } ) ^ { T }$

• Suppose A is an $n \times n$ matrix.
To find the inverse of A (or determine that it doesn’t have one), reduce the augmented matrix $\left[ A \ I _ { n } \right]$ to reduced row echelon form via row operations.
If this augmented matrix can be put in the form $\left[ I _ { n } \mid B \right]$ , then $B = A ^ { - 1 }$ . Otherwise, $A ^ { - 1 }$ does not exist.
For example:

$$
\begin{array} { r } { \left[ { \begin{array} { r r r r } { 1 } & { 2 } & { 1 } & { 0 } \\ { 3 } & { 4 } & { 0 } & { 1 } \end{array} } \right] \to \left[ { \begin{array} { r r r r } { 1 } & { 2 } & { 1 } & { 0 } \\ { 0 } & { - 2 } & { - 3 } & { 1 } \end{array} } \right] \to \left[ { \begin{array} { r r r r } { 1 } & { 0 } & { - 2 } & { 1 } \\ { 0 } & { - 2 } & { - 3 } & { 1 } \end{array} } \right] \to \left[ { \begin{array} { r r r r } { 1 } & { 0 } & { - 2 } & { 1 } \\ { 0 } & { 1 } & { 3 / 2 } & { - 1 / 2 } \end{array} } \right] } \end{array}
$$

so $\left[ { \begin{array} { l l } { 1 } & { 2 } \\ { 3 } & { 4 } \end{array} } \right]$ has inverse $\left[ { \begin{array} { c c } { - 2 } & { 1 } \\ { 3 / 2 } & { - 1 / 2 } \end{array} } \right]$

• The inverse of a $2 \times 2$ matrix $A = { \left[ \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right] }$ can be found by the formula

$$
A ^ { - 1 } = { \frac { 1 } { a d - b c } } \left[ { \begin{array} { l l } { d } & { - b } \\ { - c } & { a } \end{array} } \right]
$$

• Diagonal or triangular matrices are invertible when all of their diagonal entries are nonzero.

• Permutation matrices are always invertible, and their inverse is equal to their transpose (they are orthogonal).

## Systems of Equations

• A system of equations (with m equations in n unknowns) can be represented by the matrix equation Ax = b:

$$
\begin{array} { r }  \begin{array} { c c c c c c c c c c c c c } { { 2 } x } & { + } & { 3 y } & & & & { = } & { 3 } & & & \\ { 4 x } & { + } & { y } & { + } & { 3 z } & { = } & { 6 } & & & { \Rightarrow } & & & { \left[ { \begin{array} { c c c } { 2 } & { 3 } & { 0 } \\ { 4 } & { 1 } & { 3 } \\ { 1 } & { - 2 } & { - 4 } \end{array} } \right] \left[ { \begin{array} { c } { x } \\ { y } \\ { z } \end{array} } \right] = \left[ { \begin{array} { c } { 3 } \\ { 6 } \\ { - 1 } \end{array} } \right] } \\ { x } & { - } & { 2 y } & { - } & { 4 z } & { = } & { - 1 } \end{array} \end{array}
$$

• A system can also be represented by an augmented matrix.
The matrix A above is augmented with the vector b:

$$
\begin{array} { r } { \begin{array} { r l r l r l r l r l r l r l r l } { { 2 } x } & { { } + } & { 3 y } & { } & { } & { { } = { } } & { 3 } & { } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { 4 x } & { { } + } & { y } & { { } + } & { 3 z } & { = { } } & { 6 } & { } & { { } } & { { } \Rightarrow } & { } & { } & { { } } & { { } } & { { } } & { { } } \\ { x } & { { } - } & { 2 y } & { { } - } & { 4 z } & { = } & { - 1 } & { } & { } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \end{array} \qquad \left[ \begin{array} { l l l l l } { 2 } & { { } 3 } & { { } 0 } & { { } 3 } \\ { 4 } & { { } 1 } & { { } 3 } & { { } 6 } \\ { 1 } & { { } - 2 } & { { } - 4 } & { { } - 1 } \end{array} \right] } \end{array}
$$

We denote this augmented matrix as [A x].

• After reducing the augmented matrix [A x] to reduced row echelon form (RREF), one of three results is possible:

1. The system has no solution.
   This happens when the RREF contains a row of the form

$$
[ 0 \ 0 \ 0 \ \cdots \ 0 \ c ]
$$

where $c \neq 0$

2. The system has a unique solution.
   This happens when the rank of the matrix A is equal to the number of variables in the system.
   The following examples are reduced echelon forms of augmented matrices with exactly one solution:

$$
\left[ { \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 2 } \\ { 0 } & { 1 } & { 0 } & { 3 } \\ { 0 } & { 0 } & { 1 } & { 5 } \end{array} } \right] , \left[ { \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 2 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 5 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} } \right]
$$

The solutions to these systems are [2, 3, 5], and [2, 0, 5], respectively.

3. There are infinitely many solutions.
   This happens when the rank of the matrix A is less than the number of variables.
   The following examples are reduced echelon forms of augmented matrices with infinitely many solutions:

$$
{ \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 1 } & { 4 } \\ { 0 } & { 1 } & { 2 } & { 3 } \end{array} \right] } , { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 1 } & { 4 } \\ { 0 } & { 1 } & { 2 } & { 3 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] }
$$

Both of these systems have the same set of solutions:

$$
[ x _ { 1 } , x _ { 2 } , x _ { 3 } ] = [ 4 - c , 3 - 2 c , c ]
$$

where any value of c gives another solution to the system.

## Vector Spaces, Bases, and Dimension

• A vector space V is a set of vectors, together with the operations of addition and scalar multiplication, such that the following properties hold:

1. V contains the zero vector 0, a unique additive identity: $0 + \mathbf { v } = \mathbf { v }$

2. Addition is closed: if $\mathbf { v } _ { 1 }$ and $\mathbf { v } _ { 2 }$ are in V , then $\mathbf { v } _ { 1 } + \mathbf { v } _ { 2 }$ is in V

3. Addition is associative: $\mathbf { v } _ { 1 } + ( \mathbf { v } _ { 2 } + \mathbf { v } _ { 3 } ) = ( \mathbf { v } _ { 1 } + \mathbf { v } _ { 2 } ) + \mathbf { v } _ { 3 }$

4. Addition is commutative: $\mathbf { v } _ { 1 } + \mathbf { v } _ { 2 } = \mathbf { v } _ { 2 } + \mathbf { v } _ { 1 }$

5. Each v in V has an additive inverse −v, also in $V ; \mathbf { v } + ( - \mathbf { v } ) = - \mathbf { v } + \mathbf { v } = 0$

6. Scalar multiplication is closed: if v is in V and c is any scalar, cv is in V

7. Scalar multiplication is distributive across vector addition: $c ( \mathbf { v } _ { 1 } + \mathbf { v } _ { 2 } ) = c \mathbf { v } _ { 1 } + c \mathbf { v } _ { 2 }$

8. Scalar multiplication is distributive across scalar addition: $( c + d ) \mathbf { v } = c \mathbf { v } + d \mathbf { v }$

9. Scalar multiplication is associative: $c ( d \mathbf { v } ) = ( c d ) \mathbf { v }$

10. Scalar multiplication has an identity: $1 \mathbf { v } = \mathbf { v }$

• If W is a subset of a vector space V (meaning any vector in W also appears in V ), then W is a subspace if it satisfies the following:

1. Addition is closed: if $\mathbf { w } _ { 1 }$ and $\mathbf { w } _ { 2 }$ are in W , then $\mathbf { w } _ { 1 } + \mathbf { w } _ { 2 }$ is in W

2. Scalar multiplication is closed: if w is in W and c is any scalar, cw is in W

• A set of vectors is called linearly independent if no vector in the set can be written as a linear combination of other vectors in the set.
A set of n vectors with m components cannot be linearly independent if $n > m$ . If $n = m$ , we can test for independence by forming a matrix A from the vectors, where the vectors are either the rows or columns of A. If A is invertible, then the set is independent.

• A set of vectors is called a spanning set for a space V if every vector in V can be written as a linear combination of the vectors in the set.
The set is not required to be linearly independent, but it is a subset of V .

• A set of vectors is called a basis of a space V if it is a linearly independent spanning set of V . A basis is not unique - any vector space has more than one basis.

• Every basis of a space V contains the same number of vectors.
This number is called the dimension of the space.

• A spanning set contains at least as many vectors as a basis.
It can be larger, but a basis is the smallest spanning set possible.

Ex: $\left\{ { \binom { 1 } { 2 } } , { \binom { 1 } { 3 } } \right\}$ is a basis for $\mathbb { R } ^ { 2 }$ . It contains two linearly independent vectors.

Ex: $\left\{ { \binom { 1 } { 2 } } , { \binom { 1 } { 3 } } , { \binom { 1 } { 4 } } \right\}$ is a spanning set for $\mathbb { R } ^ { 2 }$ . It spans $\mathbb { R } ^ { 2 }$ , but is not linearly independent.
(It’s too big!)

Ex: $\left\{ \binom { 1 } { 2 } \right\}$ is neither a spanning set nor a basis for $\mathbb { R } ^ { 2 }$ . It is linearly independent, but it does not span.
(It’s too small!)

## Some Important Vector Spaces

• The real numbers are a vector space, with dimension 1. Any set containing one real number is a basis.

• The set of vectors with n components, each a real number, is denoted $\mathbb { R } ^ { n }$ . This is a vector space with dimension n. Any set of n linearly independent vectors with n components is a basis of $\mathbb { R } ^ { n }$ The standard basis includes n vectors, each with a single entry of 1 in a different position, and 0’s elsewhere.
For instance, below is a basis for $\mathbb { R } ^ { 3 }$ :

$$
\left\{ { \left[ \begin{array} { c } { 1 } \\ { 0 } \\ { 0 } \end{array} \right] } , { \left[ \begin{array} { c } { 0 } \\ { 1 } \\ { 0 } \end{array} \right] } , { \left[ \begin{array} { c } { 0 } \\ { 0 } \\ { 1 } \end{array} \right] } \right\}
$$

• The set of $m \times n$ matrices, denoted $M _ { m , n }$ , is a vector space with dimension mn.
The standard basis includes mn matrices of size m × n, each containing an entry of 1 in a different location and 0’s elsewhere.
For instance, below is a basis for the $2 \times 3$ matrices:

$$
\left\{ \left[ { \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} } \right] , \left[ { \begin{array} { c c c } { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} } \right] , \left[ { \begin{array} { c c c } { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 0 } \end{array} } \right] , \left[ { \begin{array} { c c c } { 0 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } \end{array} } \right] , \left[ { \begin{array} { c c c } { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \end{array} } \right] , \left[ { \begin{array} { c c c } { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} } \right] \right\}
$$

• The set of all polynomials of degree at most n is a vector space with dimension $n + 1$ . The standard basis contains monomials of the form $x ^ { d }$ for $d = 0 , \ldots , n$ . For example, the space of polynomials with degree at most 5 has standard basis

$$
\{ 1 , x , x ^ { 2 } , x ^ { 3 } , x ^ { 4 } , x ^ { 5 } \}
$$

## Some Important Subspaces

• Every vector space has the subspace {0}, containing only the 0 vector.
Its dimension is 0.

• The nullspace of a matrix A is the set of all solutions x to the equation $A \mathbf { x } = 0$ . If A is invertible, the nullspace is {0}. Otherwise, it contains an infinite number of vectors, including {0}.

• The column space of a matrix A is the set of all linear combinations of the columns of A. If A has m rows, each of these vectors has m components.

• The row space of a matrix A is the set of all linear combinations of the rows of A. If A has n columns, each of these vectors has n components.

## Some Examples of Non-Subspaces

• The set of invertible $n \times n$ matrices is a subset of $M _ { n , n } ,$ but not a subspace, because it does not contain the 0 matrix.
It is also not closed under addition: I and −I are both in the set, but $I + ( - I ) = 0$ is not.

• The set of vectors of the form $[ a , 1 ]$ is a subset of $\mathbb { R } ^ { 2 }$ , but not a subspace.
It is not closed under scalar multiplication, since $5 [ 3 , 1 ] = [ 15 , 5 ]$ is not in the set.
It also does not contain 0 , and is therefore not a subspace .

• A line in $\mathbb { R } ^ { 2 }$ through the origin does define a subspace.
A line that does not pass through the origin is not a subspace.

## Determinants

• The determinant of a matrix is only defined when the matrix is square.

• The determinant of a 2 × 2 matrix $A = { \left[ \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right] }$ is det(A) = ad − bc.

• The determinant of a $3 \times 3$ matrix $A = { \left[ \begin{array} { l l l } { a } & { b } & { c } \\ { d } & { e } & { f } \\ { g } & { h } & { i } \end{array} \right] }$ can be found by the “big formula”:

$$
\operatorname* { d e t } ( A ) = a e i + b f g + c d h - c e g - b d i - a f h
$$

• The determinant of any n×n matrix A can be found by cofactor (also known as Laplace) expansion.
Let $M _ { i , j }$ denote the submatrix obtained from A by removing the ith row and jth column.
Let $C _ { i , j }$ denote the number

$$
C _ { i , j } = ( - 1 ) ^ { i + j } \operatorname* { d e t } ( M _ { i , j } )
$$

Expanding along any row k, we obtain the formula

$$
\operatorname* { d e t } ( A ) = a _ { k , 1 } C _ { k , 1 } + a _ { k , 2 } C _ { k , 2 } + \cdots + a _ { k , n } C _ { k , n }
$$

where $a _ { k , j }$ is the entry of A in row k and column j. We can also expand along any column k by the formula

$$
\operatorname* { d e t } ( A ) = a _ { 1 , k } C _ { 1 , k } + a _ { 2 , k } C _ { 2 , k } + \cdots + a _ { n , k } C _ { n , k }
$$

No matter which row or column we use for the expansion, we’ll get the same result.

• The determinant of a diagonal or triangular matrix is the product of its diagonal entries.

• The determinant of a matrix is 0 if and only if the matrix is not invertible.
If the matrix contains a row or column of zeros, or if its rows or columns are not linearly independent, its determinant is 0.

• Properties of the determinant:

1. $\operatorname* { d e t } ( A B ) = \operatorname* { d e t } ( A ) \operatorname* { d e t } ( B )$

2. $\operatorname* { d e t } ( A ^ { T } ) = \operatorname* { d e t } ( A )$

3. $\operatorname* { d e t } ( A ^ { - 1 } ) = \frac { 1 } { \operatorname* { d e t } ( A ) }$

• Suppose an object has volume V . If A acts on the object, we obtain a new object with volume $V | \operatorname* { d e t } ( A ) |$

• In the two dimensional setting, a matrix A transforms an object in the plane.
If the original object had area V , then the transformed object has area $V | \operatorname* { d e t } ( A ) |$ . When a matrix acts on the unit square, we obtain a parallelogram with area $| \operatorname* { d e t } ( A ) |$ .

## Eigenvalues, Eigenvectors, and Diagonalization

• If A is a square matrix and $A \mathbf { x } = \lambda \mathbf { x }$ for some vector x and scalar $\lambda ,$ we say x is an eigenvector of A with associated eigenvalue λ.

• The characteristic polynomial of a matrix A is det $( A - \lambda I )$ . If A is $n \times n$ , this is an nth degree polynomial.

• The eigenvalues of A are the roots of the characteristic polynomial.
Every $n \times n$ matrix has n eigenvalues, though they may not be distinct.

• Once the eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ of the $n \times n$ matrix A have been found, an eigenvector $\mathbf { x } _ { i }$ associated to each can be found by solving the equation $( A - \lambda _ { i } I ) \mathbf { x } _ { i } = 0$

• Example: Let $A = \left[ { \begin{array} { l l } { 2 } & { 7 } \\ { - 1 } & { - 6 } \end{array} } \right]$ . The characteristic polynomial of A is

$$
\operatorname* { d e t } ( A - \lambda I ) = \left| \begin{array} { c c } { 2 - \lambda } & { 7 } \\ { - 1 } & { - 6 - \lambda } \end{array} \right| = ( 2 - \lambda ) ( - 6 - \lambda ) - ( 7 ) ( - 1 ) = \lambda ^ { 2 } + 4 \lambda - 5 = ( \lambda + 5 ) ( \lambda - 1 )
$$

The eigenvalues are the roots of this polynomial, $\lambda _ { 1 } = - 5$ and $\lambda _ { 2 } = 1$ . To find an eigenvector associated to $\lambda _ { 1 } = - 5$ , we find a solution of the equation $( A + 5 I ) \mathbf { x } = 0$

$$
\left[ \begin{array} { l l l } { 2 + 5 } & { 7 } & { 0 } \\ { - 1 } & { - 6 + 5 } & { 0 } \end{array} \right] \to \left[ \begin{array} { l l l } { 7 } & { 7 } & { 0 } \\ { - 1 } & { - 1 } & { 0 } \end{array} \right] \to \left[ \begin{array} { l l l } { 1 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right]
$$

There are infinitely many solutions, one of which is $\mathbf { x } _ { 1 } = \left[ 1 , - 1 \right]$ . To find an eigenvector associated to $\lambda _ { 2 } = 1$ , find any solution to the equation $( A - I ) \mathbf { x } = 0 .$

$$
\left[ \begin{array} { l l l } { 2 - 1 } & { 7 } & { 0 } \\ { - 1 } & { - 6 - 1 } & { 0 } \end{array} \right] \to \left[ \begin{array} { l l l } { 1 } & { 7 } & { 0 } \\ { - 1 } & { - 7 } & { 0 } \end{array} \right] \to \left[ \begin{array} { l l l } { 1 } & { 7 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right]
$$

so one choice would be $\mathbf { x } _ { 2 } = [ 7 , - 1 ]$

• The product of the eigenvalues of A is equal to the determinant of A.

• The sum of the eigenvalues of A is equal to its trace, the sum of the diagonal entries.

• The eigenvalues of a diagonal or triangular matrix are the diagonal entries.

• A matrix is only diagonalizable if its eigenvectors are linearly independent.

• A matrix is diagonalizable if its eigenvalues are all distinct.

• A matrix is called positive definite if all of its eigenvalues are positive.

• The eigenvalues of a symmetric matrix are always real.

## Similar Matrices

• Two matrices A and B are called similar if there exists an invertible matrix M such that $B = M ^ { - 1 } A M$

• If a matrix A is diagonalizable, it is similar to the diagonal matrix whose diagonal entries are the eigenvalues of A.

• If a matrix A is not diagonalizable, it is still similar to a matrix in Jordan form.

• If A and B are similar, they have the same:

1. determinant

2. trace

3. eigenvalues

4. number of linearly independent eigenvectors

5. Jordan form

• Even if two matrices share the above characteristics, we cannot assume they are similar.

## Linear Transformations

• A transformation $T : V \to W$ is a map from one vector space V to another, W . T is called a linear transformation if

1. $T ( \mathbf { v } _ { 1 } + \mathbf { v } _ { 2 } ) = T ( \mathbf { v } _ { 1 } ) + T ( \mathbf { v } _ { 2 } )$

2. $T ( c \mathbf { v } ) = c T ( \mathbf { v } )$

• Example: The transformation $T : \mathbb { R } ^ { 2 } \to \mathbb { R } ^ { 2 }$ defined by $T ( x , y ) = ( 2 x , x - y )$ is a linear transformation, since

$$
\begin{array} { c } { { T ( ( x , y ) + ( a , b ) ) = T ( x + a , y + b ) = ( 2 ( x + a ) , ( x + a ) - ( y + b ) ) } } \\ { { { } } } \\ { { { } = ( 2 x + 2 a , ( x - y ) + ( a - b ) ) = T ( x , y ) + T ( a , b ) } } \\ { { { } } } \\ { { T ( c ( x , y ) ) = T ( c x , c y ) = ( 2 c x , c x - c y ) = c ( 2 x , x - y ) = c T ( x , y ) } } \end{array}
$$

• Example: The transformation $T : \mathbb { R } ^ { 2 } \to \mathbb { R } ^ { 2 }$ defined by $T ( x , y ) = ( x ^ { 2 } , y )$ is not a linear transformation, since

$$
T ( c ( x , y ) ) = T ( c x , c y ) = ( ( c x ) ^ { 2 } , c y ) = c ( c x ^ { 2 } , y ) \neq c T ( x , y )
$$

• Some examples of linear transformations include: rotations, scaling, stretching, shearing, reflecting across a line through the origin, and projection onto a line through the origin.

• Any linear transformation $T : V \to W$ where V has dimension n and W has dimension m can be represented by a $m \times n$ matrix.
Finding this matrix first requires choosing a basis $\{ v _ { 1 } , v _ { 2 } , \ldots , v _ { n } \}$ for V and a basis $\{ w _ { 1 } , w _ { 2 } , \ldots , w _ { m } \}$ for W . For each basis vector $v _ { i }$ in V , we write $T ( v _ { i } )$ as a linear combination of the basis vectors for W :

$$
T ( v _ { i } ) = c _ { 1 } w _ { 1 } + c _ { 2 } w _ { 2 } + \cdots c _ { m } w _ { m }
$$

The ith column of the transformation matrix contains the entries $c _ { 1 } , c _ { 2 } , \ldots , c _ { m } .$

• If the matrix of a transformation has determinant 1, the transformation is area/volume preserving.

• Other examples of linear transformations include the derivative and the integral.

## Review Problems

It is highly recommended that you work on as many of these problems as possible.
This is not an exhaustive list of the types of questions you might see.
You should also review previous in-class exams, review sheets, and homework problems.

1. Compute the dot product u · v and the length of each vector u and v when $\mathbf { u } = [ 4 , 1 , 3 ]$ and $\mathbf { v } = [ - 2 , 0 , 1 ]$

2. Find the inverse of each matrix, or explain why it does not exist:

$$
( \mathrm { a } ) \ \bigg [ \begin{array} { l l } { 3 } & { 2 } \\ { 1 } & { 3 } \end{array} \bigg ]
$$

(b)

$$
\left[ { \begin{array} { l l l } { 1 } & { 2 } & { 4 } \\ { - 1 } & { 2 } & { 0 } \end{array} } \right]
$$

(c)

$$
\left[ \begin{array} { l l l } { 1 } & { 3 } & { 3 } \\ { 1 } & { 4 } & { 3 } \\ { 1 } & { 3 } & { 4 } \end{array} \right]
$$

(d)

$$
\left[ \begin{array} { l l l } { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \\ { 1 } & { 0 } & { 0 } \end{array} \right]
$$

3. Find the determinant of the following matrices:

$$
( \mathrm { a } ) \ \left[ \begin{array} { l l } { 5 } & { 2 } \\ { 3 } & { 1 } \end{array} \right]
$$

(b)

$$
\left[ { \begin{array} { c c c } { 6 } & { 1 } & { 3 } \\ { 0 } & { 3 } & { 3 } \\ { 0 } & { 0 } & { - 3 } \end{array} } \right]
$$

(c)

$$
\left[ { \begin{array} { r r r } { 2 } & { 0 } & { 4 } \\ { 1 } & { 3 } & { - 2 } \\ { 3 } & { 3 } & { 2 } \end{array} } \right]
$$

(d)

$$
\left[ { \begin{array} { c c c } { 2 } & { 3 } & { - 2 } \\ { 1 } & { 0 } & { 1 } \\ { 4 } & { 1 } & { 2 } \end{array} } \right]
$$

4. Find the solution(s), if they exist, for each of the following equations $A \mathbf { x } = \mathbf { b }$

(a)

$$
{ \left[ \begin{array} { l l l } { 3 } & { 3 } & { 4 } \\ { 3 } & { 5 } & { 9 } \\ { 5 } & { 9 } & { 17 } \end{array} \right] } \ { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] } = { \left[ \begin{array} { l } { 1 } \\ { 2 } \\ { 4 } \end{array} \right] }
$$

(b)

$$
{ \left[ \begin{array} { l l l } { 3 } & { 1 } & { 2 } \\ { 6 } & { 2 } & { 4 } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] } = { \left[ \begin{array} { l } { 5 } \\ { 2 } \end{array} \right] }
$$

(c)

$$
{ \left[ \begin{array} { l l l } { 3 } & { 1 } & { 2 } \\ { 6 } & { 2 } & { 4 } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] } = { \left[ \begin{array} { l } { 0 } \\ { 0 } \end{array} \right] }
$$

5. Decide which of the following sets are vector spaces.
   It is valid to show a set is a subspace, but you must indicate which vector space it is a subset of.
   If the set is a vector space, find a basis for it.

(a) The set of $3 \times 3$ diagonal matrices.

(b) The set of vectors of the form $[ a , b , 0 ]$

(c) The set of vectors of the form $[ a , 6 ]$

(d) The set of $3 \times 3$ symmetric matrices.

6. Find the characteristic polynomial of the matrix $A = { \left[ \begin{array} { l l } { 2 } & { - 4 } \\ { - 1 } & { - 1 } \end{array} \right] }$ . Then, find its eigenvalues and associated eigenvectors.

7. Decide which of the following transformations are linear.
   For those that are, find the matrix of the transformation (using the standard bases):

(a) $T : \mathbb { R } ^ { 2 } \to \mathbb { R } ^ { 2 }$ is defined by $T ( x , y ) = ( 2 x , y )$

(b) $T : \mathbb { R } ^ { 2 } \to \mathbb { R } ^ { 2 }$ is defined by $T ( x , y ) = ( x + 1 , y + 2 )$

(c) $T : \mathbb { R } ^ { 2 } \to \mathbb { R } ^ { 2 }$ rotates an object by an angle of $\pi / 3$

(d) $T : \mathbb { R } ^ { 3 } \to \mathbb { R } ^ { 2 }$ is defined by $T ( x , y ) = ( x + 2 y , x + 3 y )$
