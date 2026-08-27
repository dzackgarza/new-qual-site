1. (a) If A and B are subgroups of finite index in a group G, and $\left[ G : A \right]$ and $\left[ G : B \right]$ are relatively prime, then $G = A B$ . Solution: Firstly, if $\left[ G : B \right]$ is finite then, for any subgroup A of $G , [ A : A \cap B ]$ is finite and $\le [ G : B ]$ and moreover equality holds if and only if $G = A B$ . To see this let $g _ { 1 } B , \ldots , g _ { n } B$ be the left cosets of B such that $g _ { i } B \cap A \neq$ and let $a _ { i } \in g _ { i } B , a _ { i } \in A$ for each i. Then, the $a _ { i } ( A \cap B )$ are the cosets of $A \cap B$ in A. Also, if $g _ { 1 } B , \ldots , g _ { n } B$ are all the cosets of B, then $[ G : B ] = [ A : A \cap B ]$ and clearly every element of $G \in A B$ Now, since A∩B is a subgroup of both A and B, we have that [G : $A \cap B ] = [ G : A ] [ A : A \cap B ]$ ], and $[ G : A \cap B ] = [ G : B ] [ B : A \cap B ]$ Since $\left[ G : A \right]$ and $\left[ G : B \right]$ are mutually prime, this shows that $[ G : A \cap B ] \geq [ G : A ] [ G : B ]$ . But, from the previous paragraph we have that $[ G : A \cap B ] = [ G : A ] [ A : A \cap B ] \leq [ G : A ] [ G : B ]$ with equality if and only if $G = A B$ . Since, the equality holds, $G = A B$

(b) If H is a proper subgroup of a finite group G, then the set union $\cup _ { x \in G } x ^ { - 1 } H x$ is not the whole of G. Solution: The number of conjugates of H equals the index of its normalizer that is $[ G : N _ { H } ] \leq [ G : H ]$ since $H \subset N _ { H }$ . Let $| G | = n$ and $[ G : H ] = m$ . Since all conjugates have at least the identity in common, $| \cup _ { x \in G } x ^ { - 1 } H x | \leq 1 + m ( n / m - 1 ) = n - ( m - 1 ) < n ,$ since H is proper and hence $m = [ G : H ] > 1$

2. (a) List the Sylow subgroups of non-abelian groups of orders 21 and 39.

Solution: A non-abelian group of order 21 has seven Sylow 3- groups and one Sylow 7-group. A non-abelian group of order 39 must have thirteen Sylow 3-groups and one Sylow 13-group.

(b) Prove that there is no simple group of order 56.

Solution: Let G be a group of order 56. Consider the Sylow 7- groups. If G is simple then it must have eight Sylow 7-groups. Any two of these can intersect only at the indentity. Hence their union must have cardinality $1 + 8 ( 7 - 1 ) = 4 9$ . Hence, there must be a unique Sylow 2-group which would imply that G is not simple.

3. Let A be a commutative ring with identity which is not a field. Prove that the following conditions are equivalent.

(a) The sum of two non-invertible elements is non-invertible.

(b) The non-invertible elements form a proper ideal.

(c) The ring A possesses a unique maximal ideal.

Give an example of a ring satisfying the above conditions and describe its unique maximal ideal.

Solution:

$\mathrm { { ( a ) \Rightarrow ( b ) } }$ : Let $a \in A$ be non-invertible. Then −a is also non-invertible and 0 is non-invertible . Hence, the non-invertible elements form an additive subgroup of I of A. Morever, if $a \in I$ and $b \in A$ , then $b a \in I$ Otherwise, let $c \in A$ such that $b a c = 1$ which would imply that a is invertible. Since, 1 6∈ I this shows that I is a proper ideal.

$\mathrm { ( b ) \Rightarrow ( c ) }$ : Let I be the ideal of the non-invertible elements and let M be a maximal ideal in A. Then clearly every element of M must be non-invertible, otherwise $1 \in M$ . Hence, $M \subset I$ . But since, I is proper, $M = I$

$\mathrm { ( c ) \ \Rightarrow \ ( a ) }$ : Let M be the unique maximal ideal of A. Let $x , y$ be two non-invertible elements of A. Then, $\mathit { \Omega } ( x ) \subset M , ( y ) \subset M$ since, $( x ) , ( y )$ are proper ideals, and M is the unique maximal ideal. Then, $( x + y ) \subset M$ . Now, since $1 \ \notin \ M$ , this implies that $x + y$ is also non-invertible.

Example: The ring $k [ [ x ] ]$ with the unique maximal ideal (x).

4. (a) Let α be the real positive fourth root of 2 and $i = \sqrt { - 1 }$ . Find all intermediate fields in the extension $\mathbb { Q } ( \alpha , i )$ over $\mathbb { Q }$ Solution: Handwritten in a separate page.

(b) Let K be a finite field with $p ^ { n }$ elements. Show that every element of K has a unique p-th root in K.

Solution: Consider the Frobenius automorphism of $\sigma : K  K$ 2 sending $x \mapsto x ^ { p }$ . Since, this is an automorphism of K, it is clear that for each $x \in K$ , there exists a unique y such that $\sigma ( y ) = x$

5. Recall that a square matrix is nilpotent if $A ^ { p } = 0$ for some $p > 0$

(a) If A is an $n \times n$ complex nilpotent matrix, then $A ^ { n } = 0$

Solution: Let $p > 0$ be the largest integer such that $A ^ { p } \neq 0$ . Then, $A ^ { p } x ~ \ne ~ 0$ for some $x \in \mathbb { C } ^ { n }$ Then, the vectors $x , A x , \ldots , A ^ { p } x$ are linearly independent. Otherwise, let $\textstyle \sum _ { 0 \leq i \leq p } c _ { i } A ^ { i } x = 0$ and not all $c _ { i } ~ = ~ 0$ Let $1 ~ \leq ~ k ~ < ~ p$ be the least index such that $c _ { k } \neq 0$ . Then, $\begin{array} { r } { A ^ { k } x = \sum _ { k < i \leq p } \frac { c _ { i } } { c _ { k } } A ^ { i } x } \end{array}$ . Multiplying, by $A ^ { p - k }$ we get, $\begin{array} { r } { A ^ { p } x = \sum _ { k < i \leq p } \frac { c _ { i } } { c _ { k } } A ^ { p - k + i } x = 0 } \end{array}$ , because $A ^ { p + 1 } = 0$ , a contradiction. Hence, $p < n$

(b) Prove that the characteristic polynomial of a nilpotent matrix A of order n is equal to $\lambda ^ { n }$

Solution: The polynomial $\lambda ^ { n }$ annihilates A and hence the minimal polynomial of A is $\lambda ^ { m } , 0 \ \leq \ m \ \leq \ n$ Thus, the characteristic polynomial is $\lambda ^ { n }$

(c) Let A be a matrix of order n. Prove that A is nilpotent if and only if $t r ( A ^ { p } ) = 0$ for $p = 1 , \ldots , n$

One direction follows from the previous problem. In the other direction, first reduce the matrix A to its Jordan normal form and let $\lambda _ { 1 } , \ldots , \lambda _ { k }$ be its distinct non-zero eigenvalues. Let $n _ { i }$ be the sum of the orders of the Jordan blocks corresponding to the eigenvalue $\lambda _ { i }$ . Then, $\begin{array} { r } { t r ( A ^ { p } ) ~ = ~ \sum _ { 1 < i < k } n _ { i } \lambda _ { i } ^ { p } = 0 , 1 \le p \le k } \end{array}$ Looking at these equations as a system equations in the unknowns $n _ { i } .$ , we see that the determinant det $( ( \lambda _ { i } ^ { p } ) _ { i , p } ) \neq 0$ (Vandermonde). Thus, the only solution is $n _ { 1 } = \cdot \cdot \cdot = n _ { k } = 0$ . Thus, all eigenvalues are zero and the characteristic polynomial of A is $\lambda ^ { n }$ . Thus, $A ^ { n } =$ 0 and A is nilpotent.