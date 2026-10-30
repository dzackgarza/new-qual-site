Name:

# Qualifier Exam in Applied Algebra

September 10, 2024

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Full</td><td rowspan=1 colspan=1>Real</td></tr><tr><td rowspan=1 colspan=1>#1</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>#2</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>#3</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>#4</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>#5</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>#6</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>#7</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>#8</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>#9</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1># 10</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Total</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1></td></tr></table>

Notes: 1) For computational questions, no credit will be given for unsupported answers obtained directly from a calculator. 2) For proof questions, no credit will be given for no reasons or wrong reasons.

1. (10 points) Let X be a finite dimensional vector space over a scalar field, and let $Y , Z \subseteq X$ be two subspaces. For simplicity, you may further assume $Y \cap Z \neq \{ 0 \}$ and $Y \not \subseteq Z$ and $Z \not \subseteq Y$ . Prove

$$
\dim ( Y + Z ) = \dim ( Y ) + \dim ( Z ) - \dim ( Y \cap Z ) ,
$$

where $Y + Z = \{ y + z \mid y \in Y , z \in Z \}$

2. (10 points) Consider $A \in M _ { n } ( \mathbb { C } ) = \mathbb { C } ^ { n \times n }$ . Prove the result: A is unitarily diagonalizable if and only if A is normal.

Note, mathematically, this can be written as: there exists $U \in { \cal M } _ { n } ( \mathbb { C } ) = \mathbb { C } ^ { n \times n }$ , satisfying $U ^ { H } U =$ $U U ^ { H } = I .$ , such that $U ^ { H } A U$ is diagonal if and only if $A ^ { H } A = A A ^ { H }$ , where $U ^ { H } = \overline { { U ^ { T } } }$ and $A ^ { H } = { \overline { { A ^ { T } } } }$

3. (10 points) Let $A , C \in M _ { n } ( \mathbb { C } ) = \mathbb { C } ^ { n \times n }$ be Hermitian and suppose the following:

• The n eigenvalues of A are notated and ordered as follows:

$$
\lambda _ { 1 } ( A ) \geq \lambda _ { 2 } ( A ) \geq \cdot \cdot \cdot \geq \lambda _ { n } ( A ) ;
$$

• The n eigenvalues of C are notated and ordered as follows:

$$
\lambda _ { 1 } ( C ) \geq \lambda _ { 2 } ( C ) \geq \cdots \geq \lambda _ { n } ( C ) ;
$$

• We have $C = A + B B ^ { H }$ for some rank 2 matrix $B \in M _ { n , m } ( \mathbb { C } ) = \mathbb { C } ^ { n \times m }$ with $m \geq 2$ Note: $B ^ { H } = \overline { { B ^ { T } } }$

Prove, for all $1 \leq k \leq n - 2$ , that

$$
\lambda _ { k + 2 } ( C ) \leq \lambda _ { k } ( A ) .
$$

4. (10 points) Let $A \in M _ { m , n } ( \mathbb { C } ) = \mathbb { C } ^ { m \times n }$ . Prove

$$
\| A \| _ { 1 } = \operatorname* { m a x } _ { 1 \leq j \leq n } \sum _ { i = 1 } ^ { m } | a _ { i j } |
$$

$$
\| A \| _ { 1 } = \operatorname* { m a x } _ { x \in \mathbb { C } ^ { n } \atop \| x \| _ { 1 } = 1 } \| A x \| _ { 1 } .
$$

from the definition of the induced matrix 1-norm in terms of vector 1-norms:

5. (10 points) Let A be a unital associative algebra over C equipped with an antilinear and antimultplicative involution $A \mapsto A ^ { * }$ . We say that $A \in { \mathcal { A } }$ is normal if A and $A ^ { * }$ commute (example: normal matrices are normal elements of $\mathbb { C } ^ { N \times N } )$ . Prove that A is a commutative algebra if and only if all its elements are normal.

6. (10 points) Let $( \mathrm { V } , \varphi )$ be a finite-dimensional unitary representation of a finite group G. A vector $v \in \mathrm { V }$ is said to be cyclic if $\{ \varphi ( g ) v \colon g \in \mathrm { G } \}$ spans V. Prove that $( \mathrm { V } , \varphi )$ is irreducible if and only if every nonzero vector in V is cyclic.

7. (10 points) Let $( \mathrm { V } , \varphi )$ be a finite-dimensional unitary representation of a finite group G. State the definition of the space $\mathrm { V } ^ { \mathrm { G } }$ of G-invariant vectors in V, and prove that $\begin{array} { r } { P = \frac { 1 } { | \mathrm { G } | } \sum _ { g \in \mathrm { G } } \varphi ( g ) } \end{array}$ is the orthogonal projection of V onto $\mathrm { V } ^ { \mathrm { G } }$

8. (10 points) State the definition of the standard representation of the symmetric group and compute its character in terms of the enumeration of fixed points in permutations. Using character theory or otherwise, prove that the standard representation is irreducible.

9. (10 points) Let k be a field and let $I \subseteq k [ x _ { 1 } , \ldots , x _ { n } ]$ be an ideal. Fix a monomial order $<$ and let $G = \{ g _ { 1 } , \ldots , g _ { r } \}$ be a Gr¨obner basis of I with respect to $<$ . Consider the set of monomials

$$
{ \mathcal { M } } : = \{ { \mathrm { m o n o m i a l s ~ } } m = x _ { 1 } ^ { a _ { 1 } } \cdot \cdot \cdot x _ { n } ^ { a _ { n } } : { \mathrm { L T } } ( g _ { i } ) \nmid m { \mathrm { ~ f o r ~ } } 1 \leq i \leq r \} .
$$

Here $\operatorname { L T } ( g _ { i } )$ is the leading term of $g _ { i }$ with respect to the monomial order $<$

(a) Prove that M descends to a spanning set of the k-vector space $k [ x _ { 1 } , . . . , x _ { n } ] / I .$

(b) If G is a basis of I which is not necessarily Gr¨obner, does the set $\mathcal { M }$ necessarily span $k [ x _ { 1 } , \dots , x _ { n } / I ?$ Prove or give a counterexample.

10. (10 points) Let $G \subseteq G L _ { 3 } ( \mathbb { C } )$ be the subgroup generated by the matrices

$$
\left( { \begin{array} { c c c } { 0 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} } \right) \quad { \mathrm { ~ a n d ~ } } \quad \left( { \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { - 1 } \end{array} } \right) .
$$

The group G acts on the polynomial ring $\mathbb { C } [ x _ { 1 } , x _ { 2 } , x _ { 3 } ]$ by linear substitutions. Find an explicit generating set of the invariant ring $\mathbb { C } [ x _ { 1 } , x _ { 2 } , x _ { 3 } ] ^ { G }$