# Symplectic Geometry Spring School, June 7–14, 2004, Utrecht

J.J. Duistermaat

Department of Mathematics, Utrecht University, Postbus 80.010, 3508 TA Utrecht, The Netherlands. E-mail: duis@math.uu.nl

## Contents

1 Symplectic Linear Algebra 2   
1.1 Symplectic Forms . . 2   
1.2 Orthogonal Complements in the Dual Space 3   
1.3 Orthogonal Complements for a Bilinear Form 3   
1.4 Isotropic Subspaces . 4   
1.5 Standard Form of the Sympctic Form 4   
1.6 The Lagrangian Grassmannian 5   
1.7 The Symplectic Linear Group 6   
1.8 Exterior Algebra 7   
1.9 Hermitian Forms 9   
1.10 Historical Remarks 10   
1.11 Exercises 10   
2 Symplectic Manifolds 1 2   
2.1 Definition 12   
2.2 The Cotangent Bundle . 12   
2.3 Reduction . 13   
2.4 Complex Projective Varieties 14   
2.5 Almost Complex Structure 15   
2.6 Cohomology Classes 16   
2.7 Exercises 16   
3 Hamiltonian Systems 18   
3.1 Flows of Vector Fields 18   
3.2 Lie Derivatives 18   
3.3 Hamiltonian Vector Fields 21   
3.4 The Legendre Transform 22   
3.5 Poisson Brackets . 26   
3.6 Darboux’s Lemma 27   
3.7 Hamiltonian Group Actions 28   
3.8 Poisson Structures 30   
3.9 Exercises 31   
4 Hamilton-Jacobi Theory 33   
4.1 Lagrange Manifolds . . 33   
4.2 Lie’s View on First Order PDE 34   
4.3 An Initial Value Problem 35   
4.4 Ray Bundles 36   
4.5 High Frequency Waves and Fourier Integral Operators 38   
4.6 Some History 40   
4.7 Exercises 40

## 1 Symplectic Linear Algebra

## 1.1 Symplectic Forms

Let E be a finite-dimensional vector space over a field $k ,$ which later usually will be R. A symplectic form on E is a nondegenerate two-form σ on E. Here the word ”two-form” means that σ is an antisymmetric bilinear form on E. A bilinear form on E is a mapping $\sigma : E \times E  k$ such that, for every choice of $u \in E , v \mapsto \sigma ( u , v ) : E \to k$ is a linear form and, for every choice of $v \in E , \sigma ( u , v )$ depends linearly on u. The bilinear form $\sigma$ is called antisymmetric if

$$
\sigma ( v , u ) = - \sigma ( u , v ) , \quad u , v \in E .\tag{1.1}
$$

The bilinear form $\sigma$ is called nondegenerate if $\boldsymbol { \sigma } ( u , v ) = 0$ for every $v \in E$ implies that $u = 0$

As usual, we identify a bilinear form σ on E with the linear mapping $u \mapsto ( v \mapsto \sigma ( u , v ) )$ from E to the dual space $E ^ { * }$ of $E ,$ this linear map will also be denoted by σ. The mapping which assigns to $v \in E$ the linear form $\alpha \mapsto \alpha ( v )$ on $E ^ { * }$ induces a linear isomorphism from E onto $( E ^ { * } ) ^ { * }$ , which is used to identify $( E ^ { * } ) ^ { * }$ with E. Then the dual (= transposed) mapping $\sigma ^ { * }$ of the linear map $\sigma : E  E ^ { * }$ is a linear mapping from $( E ^ { * } ) ^ { * } = E$ to $E ^ { * }$ and the antisymmetry of $\sigma$ is equivalent to the condition that $\sigma ^ { * } = - \sigma$

The nondegeneracy of σ means that the linear mapping $\sigma : E  E ^ { * }$ has zero kernel (= null space), and because dim $E ^ { * } = \dim E$ , this is equivalent to the condition that the linear mapping $\sigma : E  E ^ { * }$ is bijective.

More generally, any linear mapping from E to $E ^ { * }$ corresponds in the above fashion to a unique bilinear form on $E ,$ and the linear mapping $E \to E ^ { * }$ is bijective (= an isomorphism) if and only if the bilinear form is nondegenerate. In the case that the bilinear form is an inner product, i.e. symmetric and positive definite, then it is nondegenerate and we obtain the usual identification of $E$ with $E ^ { * }$ by means of the inner product. In this way we may think of a symplectic form as an antisymmetric analogue of an inner product.

Example 1.1 On $k ^ { 2 n } = k ^ { n } \times k ^ { n }$ we define σ by

$$
\sigma ( ( p , q ) , ( p ^ { \prime } , q ^ { \prime } ) ) = \sum _ { j = 1 } ^ { n } p _ { j } q _ { j } ^ { \prime } - p _ { j } ^ { \prime } q _ { j } .\tag{1.2}
$$

It is easy to verify that σ is a nondegenerate antisymmetric bilinear form on $k ^ { n } \times k ^ { n }$ . It is called the standard symplectic form on $k ^ { n } \times k ^ { n }$ . A coordinate free version is the symplectic form on ${ \boldsymbol { E } } = { \boldsymbol { F } } \times { \boldsymbol { F } } ^ { * }$ defined by

$$
\sigma ( ( x , \xi ) , ( y , \eta ) ) = \xi ( y ) - \eta ( x ) , \quad x , y \in F , \quad \xi , \eta \in F ^ { * } ,
$$

0

## 1.2 Orthogonal Complements in the Dual Space

If L is a linear subspace of E, then the orthogonal complement or annihilator $L ^ { 0 }$ of L in $E ^ { * }$ is defined as the set of all $\alpha \in E ^ { * }$ such that $\alpha ( v ) = 0$ for every $v \in L$ . Clearly $L ^ { 0 }$ is a linear subspace of $E ^ { * }$ and dim L0 = dim $E ^ { * } -$ dim L = dim E − dim $L = \operatorname { t }$ he codimension of L in E.

Similarly the orthogonal complement or annihilator $A ^ { 0 }$ in E of a linear subspace A of $E ^ { * }$ is defined as the common kernel of all the linear forms $\alpha \in A$ , i.e. the set of all $v \in E$ such that $\alpha ( v ) = 0$ for every $\alpha \in A . \ A ^ { 0 }$ is a linear subspace of E and dim $A ^ { 0 } = \dim E - \dim E .$

If L is a linear subspace of $E ,$ then obviously $L \subset ( L ^ { 0 } ) ^ { 0 }$ , and because $\dim ( L ^ { 0 } ) ^ { 0 } = \dim E -$ dim L0 = dim E − (dim E − dim L) = dim L, we conclude that $L = ( L ^ { 0 } ) ^ { 0 }$ . Similarly $A = ( A ^ { 0 } ) ^ { 0 }$ for any linear subspace A of $E ^ { * }$

If L and M are linear subspaces of E, then obviously $L \subset M$ implies $M ^ { 0 } \subset L ^ { 0 }$ . Therefore in general $L ^ { 0 } \subset ( L \cap M ) ^ { 0 }$ and $M ^ { 0 } \subset ( L \cap M ) ^ { 0 }$ , which implies that $L ^ { 0 } + M ^ { 0 } \subset ( L \cap M ) ^ { 0 }$ , and similarly $( L + M ) ^ { 0 } \subset L ^ { 0 } \cap M ^ { 0 }$ . Taking orthogonal complements these inclusions imply that

$$
L \cap M = ( ( L \cap M ) ^ { 0 } ) ^ { 0 } \subset ( L ^ { 0 } + M ^ { 0 } ) ^ { 0 } \subset ( L ^ { 0 } ) ^ { 0 } \cap ( M ^ { 0 } ) ^ { 0 } = L \cap M ,
$$

It follows that both inclusions are equalities and therefore $( L \cap M ) ^ { 0 } = L ^ { 0 } + M ^ { 0 }$ . Similiarly we have $( L + M ) ^ { 0 } = L ^ { 0 } \cap M ^ { 0 }$

## 1.3 Orthogonal Complements for a Bilinear Form

Let $\sigma$ be a nondegenerate bilinear form on $E ,$ not necessarily antisymmetric. If L is a linear subspace of $E _ { i }$ , then the σ-orthogonal complement $L ^ { \sigma }$ of $L$ in $E$ is defined as

$$
L ^ { \sigma } : = ( \sigma ( L ) ) ^ { 0 } = \left\{ u \in E \mid \sigma ( u , v ) = 0 \quad { \mathrm { f o r ~ e v e r y } } \quad v \in L \right\} .\tag{1.3}
$$

Clearly $L ^ { \sigma }$ is a linear subspace of E. Note that $L ^ { \sigma } = L ^ { \sigma ^ { * } }$ if $\sigma$ is symmetric or antisymmetric. That is, in these case we can interchange the role of u and v in the definition (1.3).

Because $\sigma : E  E ^ { * }$ is a linear isomorphism, the rules for annihilators in the dual spaces imply the rules

$$
\dim L ^ { \sigma } = \dim E - \dim L ,\tag{1.4}
$$

$$
L \subset M \Longrightarrow M ^ { \sigma } \subset L ^ { \sigma } ,\tag{1.5}
$$

$$
( L \cap M ) ^ { \sigma } = L ^ { \sigma } + M ^ { \sigma } \quad { \mathrm { a n d } } \quad ( L + M ) ^ { \sigma } = L ^ { \sigma } \cap M ^ { \sigma }\tag{1.6}
$$

for the σ-orthogonal complements. If $k = \mathbf { R }$ and $\sigma$ is an inner product, then the σ-orthogonal complement of $L$ is usual orthogonal complement denoted by $L ^ { \perp }$ , and we recognize (1.4), (1.5) and (1.6) as familiar properties of the orthogonal complementation. Note that for the inner product we have the additional property that $L \cap L ^ { \bot } = \{ 0 \}$ , which implies that $E$ is equal to the direct sum $L \oplus L ^ { \perp }$ of L and $L ^ { \perp }$

## 1.4 Isotropic Subspaces

In the sequel $( E , \sigma )$ will be a symplectic vector space, i.e. E is a finite-dimensional vector space and σ is a symplectic form on $E$

A linear subspace L is called isotropic with respect to σ if $L \subset L ^ { \sigma }$ , that is $\boldsymbol { \sigma } ( u , v ) = 0$ for all pairs of vectors $u , v \in L$ . A maximal isotropic linear subspace of E is called a Lagrange plane. Because of the finite-dimensionality of $E _ { i }$ , any striclty increasing sequence of isotropic subspaces terminates at a maximal one, which shows that every isotropic subspace is contained in at least one Lagrange plane.

The antisymmetry of $\sigma$ implies that $\sigma ( v , v ) = - \sigma ( v , v )$ , hence $2 \sigma ( v , v ) = 0$ . Therefore, if the characteristic of k is not equal to two, the antisymmetry (1.1) implies that

$$
\sigma ( v , v ) = 0 , \quad v \in E .\tag{1.7}
$$

Conversely, if (1.7) holds, then $0 = \sigma ( u + v , u + v ) = \sigma ( u , u ) + \sigma ( u , v ) + \sigma ( v , u ) + \sigma ( v , v ) =$ $\sigma ( u , v ) + \sigma ( v , u )$ , which implies (1.1). Therefore, if char $k \neq 2 ,$ , such as for $k = \mathbf { R }$ , then (1.1) is equivalent to (1.7). If char $k = 2 .$ , then everything what follows remains true if we replace the antisymmetry condition (1.1) by the stronger condition (1.7).

The condition (1.7) implies that every one-dimensional linear subspace of E is isotropic. This is very different from the situation for an inner product, where {0} is the only isotropic subspace.

If $L \subset L ^ { \sigma }$ and $L \ne L ^ { \sigma }$ , then for every $v \in L ^ { \sigma } \setminus L$ we have that $( L + k v ) ^ { \sigma } = L ^ { \sigma } \cap ( k v ) ^ { \sigma }$ contains L because $L ^ { \sigma } \supset L$ and k $v \subset L ^ { \sigma }$ implies $( k v ) ^ { \sigma } \supset L$ . it also contains v because $v \in L ^ { \sigma }$ and $v \in ( k v ) ^ { \sigma }$ . It follows that the linear subspace $( L + k v ) ^ { \sigma }$ contains $L + k v$ , which means that $L ^ { \prime } : = L + k v$ is isotropic, $L \subset L ^ { \prime }$ and dim $L ^ { \prime } = \dim L + 1$ . We conclude that L is a maximal isotropic linear subspace if and only if $L = L ^ { \sigma }$ . This is equivalent to the condition that L is isotropic and dim L = dim Lσ = dim $E - \dim L .$ , or equivalently dim $E = 2 \dim L$

In particular the dimension of a symplectic vector space must be even, say equal to 2n. We have that dim $L \leq n$ for every isotropic linear subspace L of E and that the maximal isotropic subspaces are the isotropic subspaces which have dimension equal to n.

## 1.5 Standard Form of the Sympctic Form

In order to identify the symptic form with the standard one of Example 1.1, we start with an $L \in \mathcal { L } ( E , \sigma )$ and introduce a second $M \in { \mathcal { L } } ( E , \sigma )$ such that $L \cap M = \{ 0 \}$ , which then implies that $E = L \oplus M$ The existence of such a Lagrange plane M follows from the fact that, if M is an isotropic subspace of $( E , \sigma )$ such that $M \neq M ^ { \sigma }$ and $L \cap M = \{ 0 \}$ , then there exists a $v \in M ^ { \sigma } \backslash$ M such that $L \cap M ^ { \prime } = \{ 0 \}$ if $M ^ { \prime } : = M + k v$ . If $L \cap M ^ { \prime } \neq \{ 0 \}$ then there exist $m \in M$ and $c \in K$ such that $l = m + c v$ is a nonzero element of $L ,$ which means that $v \in L + M$ . If this would hold for every $v \in M ^ { \sigma } \backslash M$ , then $M ^ { \sigma } \setminus L + M$ , which implies that ${ \cal L } \cap { \cal M } ^ { \sigma } = { \cal L } ^ { \sigma } \cap { \cal M } ^ { \sigma } = ( { \cal L } + { \cal M } ) ^ { \sigma } \subset$ $( M ^ { \sigma } ) ^ { \sigma } = M$ , which in view of $L \cap M = \{ 0 \}$ means that $L \cap M ^ { \sigma } = \{ 0 \}$ . However, dim $L = n$ and dim Mσ = dim E − dim $M >$ dim $E - n .$ hence dim L + dim $M ^ { \sigma } >$ dim $E ,$ which implies that dim(L ∩ Mσ) = dim L + dim Mσ − dim $E > 0$ , and we arrive at a contradiction.

The restriction S to M of the mapping $m \mapsto ( \sigma m ) | _ { L }$ is a linear isomorphism form M onto $L ^ { * }$ Indeed, $S m = 0$ means that $m \in L ^ { \sigma } = L$ , which in view of $L \cap M = \{ 0 \}$ implies that $m = 0$ . Now let $e _ { i }$ be a basis of $L$ and let $\epsilon _ { j }$ be the corresponding dual basis of $L ^ { * }$ , determined by the conditions that $\epsilon _ { j } ( e _ { i } )$ is equal to zero and zero when $i \neq j$ and $i = j$ , respectively. Let $f _ { j }$ be the basis of M such that $S f _ { j } = \epsilon _ { j }$ . Then we have $\sigma ( e _ { i } , e _ { i ^ { \prime } } ) = 0 , \sigma ( f _ { j } , f _ { j ^ { \prime } } ) = 0$ and − $\sigma ( e _ { i } , f _ { j } ) = \sigma ( f _ { j } , e _ { i } ) = \epsilon _ { j } ( e _ { i } ) = \delta _ { i j }$

The $e _ { i }$ and $f _ { j }$ together form a basis on which σ has a standard form. Such a basis is called a symplectic basis of $( E , \sigma )$

More precisely, if we write $\begin{array} { r } { u = \sum _ { i = 1 } ^ { n } p _ { i } e _ { i } + q _ { j } f _ { j } , v = \sum _ { i = 1 } ^ { n } p _ { i } ^ { \prime } e _ { i } + q _ { j } ^ { \prime } f _ { j } } \end{array}$ , then it follows that $\sigma ( u , v )$ is equal to the right hand side of (1.2). This means that the pull-back of $\sigma$ under the linear isomorphism $\begin{array} { r } { ( p , q ) \mapsto \sum _ { i = 1 } ^ { n } p _ { i } e _ { i } + q _ { j } f _ { j } } \end{array}$ from $k ^ { n } \times k ^ { n }$ onto E is equal to the standard symplectic form on $k ^ { n } \times k ^ { n }$

For an arbitrary antisymmetric bilinear form σ on a finite-dimensional vector space E over a field k, a basis on which $\sigma$ has a standard form is obtained as follows. If $N = \ker \sigma$ , then the equation $\sigma _ { E / N } ( u + N , v + N ) = \sigma ( u , v )$ leads to a well-defined antisymmetric bilinear form on $E / N$ which is nondegenerate, this is called the induced symplectic form on $E / N$ . Write $r =$ dim N , $N .$ $\begin{array} { r } { m = { \frac { 1 } { 2 } } \dim ( E / N ) } \end{array}$ , and choose $n _ { 1 } , . . . n _ { r } , e _ { 1 } , . . . e _ { m } , f _ { 1 } , . . . , f _ { m }$ in E such that the $n _ { 1 } , . . . . n _ { r }$ from a basis of N and the $e _ { 1 } + N , \ldots e _ { m } + N , f _ { 1 } + N , \ldots , f _ { m } + N$ form a symplectic basis of $\left( E / N , \sigma _ { E / N } \right)$ Then these $r + 2 m$ vectors for a basis of E, for which $\sigma ( n _ { i } , n _ { j } ) = \sigma ( n _ { i } , e _ { j } ) = \sigma ( n _ { i } , f _ { j } ) = 0$ , $\sigma ( e _ { i } , e _ { j } ) = \sigma ( f _ { i } , f _ { j } ) = 0$ 0, and $\sigma ( e _ { i } , f _ { j } ) = - \sigma ( f _ { j } , e _ { i } ) = \delta _ { i j }$

The fact that antisymmetric bilinear forms on vector spaces of the same dimension and with the same nullity (= dimension of the kernel) have the same normal form, differs from the situation for symmetric bilinear forms. If k has the property that every element of k has a square root in $k ,$ then all symmetric bilinear forms with the same nullity have the same normal form, but for general fields the classification of symmetric bilinear forms can be very complicated. For $k = \mathbf { R }$ the situation still is relatively simple, as a real symmetric bilinear form is determined by its nullity n0, and its positive and negativity index = the dimension $n _ { + }$ and $n _ { \cdot }$ − of any maximal linear subspace on which the form is positive definite and negative definite, respectively.

## 1.6 The Lagrangian Grassmannian

The set $\mathcal { L } = \mathcal { L } ( E \sigma )$ of all Lagrange planes in the symplectic vector space $( E , \sigma )$ is called the Lagrangian Grassmannian of $( E , \sigma )$ . It is a non-empty algebraic subvariety of the Grassmann manifold ${ \mathrm { G } } _ { n } ( E )$ of all n-dimensional linear subspaces of $E .$

If $L \in { \mathcal { L } }$ and $k \in \mathbf { Z } _ { > 0 }$ , then we denote by $\mathcal { L } _ { L , k }$ the set of all $M \in { \mathcal { L } }$ such that dim $L \cap M = k$ $\mathcal { L } _ { L , 0 }$ is an open subset of $\mathcal { L }$ , and in the previous subsection we have seen that it is not empty. Interchanging the roles of L and M we obtain that the $\mathcal { L } _ { L , 0 }$ for $L \in { \mathcal { L } }$ form an open covering of $\mathcal { L } .$ i.e. for every $M \in { \mathcal { L } }$ there exists an $L \in { \mathcal { L } }$ such that $M \in \mathcal { L } _ { L , 0 }$

Let $L , M \in \operatorname { G } _ { n } ( E )$ be such that $E = L \oplus M$ . For every $L ^ { \prime } \in \mathrm { G } _ { n } ( E )$ such that $L ^ { \prime } \cap M = \{ 0 \}$ there is a unique linear mapping $A : L \to M$ such that $L ^ { \prime } = \{ x + A x \mid x \in L \}$ . This leads to a bijctive mapping from the open subset $\{ L ^ { \prime } \in \mathrm { { G } } _ { n } ( E ) \mid L ^ { \prime } \cap M = \{ 0 \} \} \ \mathrm { { o f } } \ \mathrm { { G } } _ { n } ( E )$ onto the $n ^ { 2 } .$ -dimensional vector space $\operatorname { L i n } ( L , M )$ of all linear mappings from L onto $M ,$ , and the matrix coefficients of A with respect to any bases in $L$ and M define a coordinatization of the aformentioned open subset of ${ \mathrm { G } } _ { n } ( E )$ . These are the standard coordinatizations of ${ \mathrm { G } } _ { n } ( E )$ . The coordinate changes are rational mappings and in this way ${ \mathrm { G } } _ { n } ( E )$ is exhibited as a smooth $n ^ { 2 }$ -dimensional manifold.

Now assume that $L , M \in { \mathcal { L } } ( E , \sigma )$ . We have that $L ^ { \prime } \in \mathcal { L } ( E , \sigma )$ if and only if, for every x, $y \in L$

$$
0 = \sigma ( x + A x , y + A y ) = \sigma ( A x , y ) + \sigma ( x , A y ) = \sigma ( A x , y ) - \sigma ( A y , x ) ,
$$

where we have used in the second identity that $\sigma ( x , y ) = 0$ and $\sigma ( A x , A y ) = 0$ because L and M are isotropic. This means that the bilinear form $( x , y ) \mapsto \sigma ( A x , y )$ on L is symmetric. Because $A \mapsto ( ( x , y ) \mapsto \sigma ( A x , y ) )$ is a linear isomorphism from $\operatorname { L i n } ( L , M )$ onto the space of all bilinear forms on $L ,$ we see that in the aforementioned coordinatization the Lagrangian Grassmannian appears as the space of all symmetric bilinear forms on L, viewed as a linear subspace of the space of all bilinear forms on L. This exhibits ${ \mathcal { L } } ( E , \sigma )$ as a smooth ${ \frac { 1 } { 2 } } n ( n + 1 )$ )-dimensional linear submanifold of the $n ^ { 2 } .$ -dimensional manifold ${ \mathrm { G } } _ { n } ( E )$

If $\widetilde { M }$ is another Lagrange plane which is transversal to L and $L ^ { \prime } \in { \mathcal { L } }$ is transversal to both M and ${ \widetilde { M } } ,$ then we have a second coordinatization of $L ^ { \prime }$ by means of the $\widetilde { A } \in \mathrm { L i n } ( L , \widetilde { M } )$ such that ${ \cal L } ^ { \prime } = \{ y + \widetilde { A } y | y \in { \cal L }$ . On the other hand there exists $B \in \operatorname { L i n } ( M , L )$ such that ${ \widetilde { M } } = { }$ $\{ z + B z \mid z \in M \}$ . The elements of $L ^ { \prime }$ are of the form $x + A x = y + { \tilde { A } } y$ for unique $x , y \in L ,$ and $\ddot { A } y = z + B z$ for a unique $z \in M$ . Therefore $z = A x , y = x - B z = x - B A x$ , hence $x + A x = ( x - B A x ) + \widetilde { A } \left( x - B A x \right)$ . Taking the symplectic product with $u \in L$ , this leads to

$$
\sigma ( A x , u ) = \sigma ( \widetilde { A } ( x - B A x ) , u ) = \sigma ( \widetilde { A } x , u ) - \sigma ( \widetilde { A } B A x , u ) .
$$

For small A, which corresponds to $L ^ { \prime }$ close to $L ,$ we see that the symmetric bilinear form on L defined by the M differs from the symmetric bilinear form on L defined by M by a term which vanishes of second order in A. In this way the tangent space $\mathrm { T } _ { L } { \mathcal { L } }$ of L at the element $L \in { \mathcal { L } }$ is canonically identified with the space $\mathrm { S y m m } ^ { 2 } ( L )$ of all symmetric bilinear forms on $L .$

## 1.7 The Symplectic Linear Group

Let $( E , \sigma ) , ( F , \tau )$ be a symplectic vector spaces over a field k. A linear mapping $A : E  F$ is called a symplectic linear mapping from $( E , \sigma )$ to $( F , \tau ) , { \mathrm { i f ~ } } \tau ( A u , A v ) = \sigma ( u , v )$ for all $u , v \in E$ b, or $A ^ { * } \tau A = \sigma$ Because $\sigma : E  E ^ { * }$ is injective, A is injective, hence dim $E \le$ dim $F$ , and we have that A is bijective if and only dim $E = \dim { F }$ , in which case A is called a symplectic linear isomorphism from $( E , \sigma )$ onto $( F , \tau )$ . If dim $E <$ dim F , then A is a symplectic linear isomorphism from $( E , \sigma )$ onto the symplectic vector subspace $( A ( E ) , \tau | _ { A ( E ) \times A ( E ) }$ of $( F , \tau )$

A symplectic linear mapping from $( E , \sigma )$ to itself is called a symplectic linear transformation in $( E , \sigma )$ . The symplectic linear transformations form an algebraic subgroup of the group $\operatorname { G L } ( E )$ of all linear transformations in E, which is called the symplectic linear group $\operatorname { S p } ( E , \sigma )$

If $e _ { 1 } , \ldots , e _ { n } , f _ { 1 } , \ldots , f _ { n }$ is a symplectic basis, then a linear mapping A is symplectic if and only if $A e _ { 1 } , \ldots , A e _ { n } , A f _ { 1 } , \ldots , A f _ { n }$ is a symplectic basis. Because any basis of a Lagrange plane can be extended to a symplectic basis, it follows that the symplectic linear group $\operatorname { S p } ( E , \sigma )$ acts transitively on the Lagrangian Grassmannian $\operatorname { S p } ( E , \sigma )$ . If, for given $L \in { \mathcal { L } } ( E , \sigma ) , \operatorname { S p } ( E , \sigma ) _ { L } : =$ $\{ A \in \operatorname { S p } ( E , \sigma ) \mid A ( L ) = L \}$ denotes the stabilizer subgroup of L in $\operatorname { S p } ( E , \sigma )$ , then the Lagrangian Grassmannina ${ \mathcal { L } } ( E , \sigma )$ is identified with the homogeneous space $\mathrm { S p } ( E , \sigma ) / \mathrm { S p } ( E , \sigma ) _ { L }$

If we write $A = { \left( \begin{array} { l l } { \alpha } & { \beta } \\ { \gamma } & { \delta } \end{array} \right) }$ on a symplectic basis, in which $\alpha , \beta , \gamma , \delta$ are n × n-matrices, then $A \in \operatorname { S p } ( E , \sigma )$ if and only if $\alpha ^ { * } \gamma - \gamma ^ { * } \alpha = 0 , \beta ^ { * } \delta - \delta ^ { * } \beta = 0$ and $\alpha ^ { * } \delta - \beta ^ { * } \gamma = I$ . The first two equations mean that $\alpha ^ { * } \gamma = \epsilon$ and $\beta ^ { * } \delta = \eta$ are symmetric, and we see $2 ( { \textstyle { \frac { 1 } { 2 } } } n ( n - 1 ) ) + n ^ { 2 } = 2 n ^ { 2 } - n$ independent equations. If the first n vectors of the symplectic basis span L, then $A \in \operatorname { S p } ( E , \sigma ) _ { L }$ if and only if $\gamma = 0$ , and the equations are that $\delta = ( \alpha ^ { * } ) ^ { - 1 }$ and $\delta ^ { * } \beta = \alpha ^ { - 1 } \beta$ is symmetric. It follows that dim $\mathrm { S p } ( E , \sigma ) _ { L } = n ^ { 2 } + { \textstyle { \frac { 1 } { 2 } } } n ( n + 1 )$ , and therefore dim $\operatorname { S p } ( E , \sigma ) = n ^ { 2 } + n ( n + 1 ) = 2 n ^ { 2 } + n$ It follows that the codimension of $\operatorname { S p } ( n , E )$ in $\operatorname { G L } ( E )$ is equal to $2 n ^ { 2 } - n$ , in agreement with the number of independent equations for the matrices $\alpha , \beta , \gamma , \delta$

The equation $A ^ { * } \sigma A = \sigma$ for $A \in \operatorname { S p } ( E , \sigma )$ implies that $A ^ { * } = \sigma A \sigma ^ { - 1 }$ , which means that the linear isomorphism $\sigma : E  E ^ { * }$ conjugates the linear mapping $A : E  E$ with the linear mapping $( A ^ { * } ) ^ { - 1 } : E ^ { * } \to E ^ { * }$ . This implies that A has the same eigenvalues as $( A ^ { * } ) ^ { - 1 }$ with the same algebraic multiplicities. Because $A ^ { * }$ has the same eigenvalues with the same algebraic multiplicities as A, it follows that if λ is an eigenvalues of A with algebraic multiplicity $m ,$ then $1 / \lambda$ is also an eigenvalue of A with algebraic multiplicity m. If $k = \mathbf { R }$ , then a passage to the complexification leads to the conclusion that the the complex eigenvalues of A appear in foursomes $\lambda , { \overline { { \lambda } } } , 1 / \lambda , 1 / { \overline { { \lambda } } }$ with $\lambda \in \mathbf { C }$ , $\lambda \notin \mathbf { R } , \lambda \overline { { \lambda } } \neq 1$ , or in real pairs $\lambda , 1 / \lambda ,$ or in complex conjugate pairs on the unit circle, in each case with equal algebraic multiplicities.

The Lie algebra ${ \mathfrak { s p } } ( E , \sigma )$ of $\operatorname { S p } ( E , \sigma )$ consists of the linear mappings $A : E  E$ such that $\sigma ( A u , v ) + \sigma ( u , A v ) = 0$ for all $u , v \in E$ , or $\sigma A + A ^ { * } \sigma = 0$ . These A are called the infinitesimal symplectic linear transformations in $( E , \sigma )$ . Note also that the mapping which assigns to $A \in$ ${ \mathfrak { s p } } ( E , \sigma )$ the bilinear form $\sigma A : ( u , v ) \mapsto \sigma ( A u , v )$ is a linear isomomorphism from ${ \mathfrak { s p } } ( E , \sigma )$ onto the space $\operatorname { S y m m } ^ { 2 } ( E )$ of all symmetric bilinear forms on E. This shows that dim $\operatorname { S p } ( E , \sigma ) =$ : $\begin{array} { r } { \frac { 1 } { 2 } 2 n ( 2 n + 1 ) = 2 n ^ { 2 } + n } \end{array}$ , in agreement with our previous dimension calculations.

The equation $A ^ { * } = - \sigma A \sigma ^ { - 1 }$ implies that if λ is an eigenvalues of A with multiplicity $m ,$ then $- \lambda$ is also an eigenvalue of A with m,ultiplicity m. When $k = \mathbf { R }$ , this implies that the complex eigenvalues of A appear in foursomes $\lambda , { \overline { { \lambda } } } , - \lambda , - { \overline { { \lambda } } }$ with $\lambda \in { \bf C } , \lambda \notin { \bf R } , \lambda \notin \mathrm { i } { \bf R }$ , or in real pairs $\lambda , - \lambda$ , or in complex conjugate pairs on the imaginary axis, in each case with equal algebraic multiplicities.

For $k = \mathbf { R }$ a complete list of normal forms of infinetesimal symplectic linear transformations has been given by Williamson [30], and one has a corresponding list for the symplectic linear transformations, see also [2] and [4].

## 1.8 Exterior Algebra

Let E be any d-dimensional vector space over k. The space of all antisymmetric p-linear forms on E is denoted by $\Lambda ^ { p } E ^ { * }$ . For $\alpha \in \Lambda ^ { p } E ^ { * }$ and $\beta \in \Lambda ^ { q } E ^ { * }$ , one defines the exterior product $\alpha \wedge \beta \in \Lambda ^ { p + q } E ^ { * }$ by

$$
( \alpha \wedge \beta ) ( v _ { 1 } , \ldots , v _ { p + q } ) = \sum _ { \pi } \operatorname { s g n } \pi \alpha ( v _ { \pi ( 1 ) } , \ldots , v _ { \pi ( p ) } ) \beta ( v _ { \pi ( p + 1 ) } , \ldots , v _ { \pi ( p + q ) } )\tag{1.8}
$$

for all $v _ { 1 } , \dotsc , v _ { p + q } \in E$ . Here the sum is over all equivalence classes of permutations permutations $\pi$ of the indices $\{ 1 , \ldots , p + q \}$ , where π and $\pi \circ \psi$ are equivalent if $\psi$ maps the subsets $\{ 1 , \ldots , p \}$ and $\{ p + 1 , \ldots , p + q \}$ of indices to themselves. (Note that terms with equivalent permutations are equal.) The signature sgn π of the permutation is $+ 1 \ \mathrm { o r \ - 1 }$ when π consists of an even or odd number of transpositions, respectively.

With this product,

$$
\Lambda E ^ { * } : = \bigoplus _ { p \geq 0 } \Lambda ^ { p } E ^ { * }
$$

becomes an algebra, which is called the exterior algebra of $E ^ { * }$ . Here we have used the convention that $\Lambda ^ { 0 } E ^ { * } = k$ . Note also that $\Lambda ^ { 1 } E ^ { * } = E ^ { * }$ is a linear subspace of $\Lambda E ^ { * }$

The exterior product is associative, meaning that $( \alpha \wedge \beta ) \wedge \gamma = \alpha \wedge ( \beta \wedge \gamma )$ . It is anticommutative in the sense that α $\wedge \beta = ( - 1 ) ^ { p q } \beta \wedge$ α if $\alpha \in \Lambda ^ { p } E ^ { * }$ and $\beta \in \Lambda ^ { q } E ^ { * }$

Let $e _ { i }$ be any basis of E and $\epsilon _ { j }$ de corresponding dual basis of $E ^ { * }$ , characterized by $\epsilon _ { j } ( e _ { i } ) = \delta _ { i j }$ For any strictly increasing function $I : \{ 1 , \dots , p \} \to \{ 1 , \dots , d \}$ }, write $\epsilon _ { I } = \epsilon _ { I ( 1 ) } \wedge \ldots \wedge \epsilon _ { I ( p ) }$ and $e _ { I } = ( e _ { I ( 1 ) } , \dots , e _ { I ( p ) } )$ Then $\epsilon _ { I } ( e _ { J } ) = \delta _ { I J }$ Therefore, if $\alpha \in \Lambda ^ { p } E *$ , then $\begin{array} { r } { \alpha = \sum _ { I } \alpha ( e _ { I } ) \epsilon _ { I } } \end{array}$ 5 which follows from applying both sides to $e _ { J }$ and observing that the numbers $\alpha ( e _ { J } )$ determine α.

Conversely, if $\begin{array} { r } { \sum _ { I } c _ { I } \epsilon _ { I } = 0 } \end{array}$ , then application to $e _ { J }$ yields $c _ { J } = 0$ for every $^ { J , }$ and it follows that the $\epsilon _ { I }$ form a basis of $\Lambda ^ { p } E ^ { * }$ , which in turn implies that

$$
\mathrm { d i m } \Lambda ^ { p } E ^ { * } = \left( \begin{array} { l } { d } \\ { p } \end{array} \right) .\tag{1.9}
$$

In particular $\Lambda ^ { p } E ^ { * } = \{ 0 \}$ when $p > n$ and the space $\Lambda ^ { d } E ^ { * }$ of oriented volume forms on $E$ is one-dimensional.

If $\sigma \in \Lambda ^ { 2 } E ^ { * }$ is a symplectic form on E and $( e _ { 1 } , \ldots e _ { n } , f _ { 1 } , \ldots f _ { n } )$ is a symplectic basis, with corresponding dual basis $( \epsilon _ { 1 } , \ldots \epsilon _ { n } , \phi _ { 1 } , \ldots , \phi _ { n } )$ , then we see from (1.2) that

$$
\sigma = \sum _ { i = 1 } ^ { n } \epsilon _ { i } \wedge \phi _ { i }\tag{1.10}
$$

and therefore the n-the exterior power

$$
\sigma ^ { n } = \sigma \wedge . . . \wedge \sigma = n ! \epsilon _ { 1 } \wedge \phi _ { 1 } \wedge \epsilon _ { 2 } \wedge \phi _ { 2 } \wedge . . . \wedge \epsilon _ { n } \wedge \phi _ { n }\tag{1.11}
$$

of $\sigma$ is a nonzero volume form on E. (Note that the exterior product is commutative on the subalgebra generated by the two-forms $\epsilon _ { i } \wedge \phi _ { i } . )$ Here we assume that the field k has characteristic zero or, in the case of nonzero characteristic, char $k > n$ . This implies that also all the intermediate powers $\sigma ^ { m } \in \Lambda ^ { 2 m } E ^ { * } , 0 \leq m \leq n$ , are nonzero.

With the identification of E with $( E ^ { * } ) ^ { * }$ , the exterior algebra $\Lambda E$ of E is defined as the algebra of antisymmetric multilinear forms on $E ^ { * }$ . There is an natural identification of $\lambda E$ with the dual space of $\Lambda E ^ { * }$ and vice versa, as follows.

If $v \in ( \Lambda ^ { p } E ^ { * } ) ^ { * }$ , then

$$
i ( v ) ( \alpha _ { 1 } , \ldots , \alpha _ { p } ) : = v ( \alpha _ { 1 } \wedge \ldots \wedge \alpha _ { p } ) , \quad \alpha _ { i } \in E ^ { * } ,
$$

defines an antisymmetric p-linear form on $E ^ { * }$ , and therefore belongs to $\Lambda ^ { p } E$ . This defines a linear mapping $i : ( \Lambda ^ { p } E ^ { * } ) ^ { * } \to \Lambda ^ { p } E$ Furthermore, if $i ( v ) = 0$ , then v annihilates all $p { \mathrm { - f o l d } }$ exterior products of one-forms and therefore $v = 0$ because the $\epsilon _ { I }$ form a basis of $\Lambda ^ { p } E ^ { * }$ . We conclude that i is injective and because

$$
\mathrm { d i m } ( \Lambda ^ { p } E ^ { * } ) ^ { * } = \left( \begin{array} { c } { { d } } \\ { { p } } \end{array} \right) = \mathrm { d i m } \Lambda ^ { p } E ,
$$

we conclude that i is a linear isomorphism.

We have a similar linear isomorphism $j : ( \Lambda ^ { p } E ) ^ { * } \to \Lambda ^ { p } E ^ { * }$ . If $v _ { 1 } \land . . . \land v _ { p } = i ( v )$ and $\alpha _ { 1 } \wedge . . . \alpha _ { p } =$ $j ( \alpha )$ , then

$$
\begin{array} { l c l } { { \alpha ( i ( v ) ) } } & { { = } } & { { \displaystyle j ( \alpha ) ( v _ { 1 } , \ldots , v _ { p } ) = ( \alpha _ { 1 } \wedge \ldots \wedge \alpha _ { p } ) ( v _ { 1 } , \ldots , v _ { p } ) = \sum _ { \pi } \operatorname { s g n } \pi \prod _ { k = 1 } ^ { p } \alpha _ { k } ( v _ { \pi ( k ) } ) } } \\ { { } } & { { = } } & { { ( v _ { 1 } \wedge \ldots \wedge v _ { p } ) ( \alpha _ { 1 } , \ldots , \alpha _ { p } ) = i ( v ) ( \alpha _ { 1 } , \ldots , \alpha _ { p } ) = v ( j ( \alpha ) ) , } } \end{array}
$$

which shows that the mappings $i$ and $j$ are each others adjoints.

One uses i and j to identify $( \Lambda ^ { p } E ^ { * } ) ^ { * }$ with $\Lambda ^ { p } E$ and $( \Lambda ^ { p } E ) ^ { * }$ with $\Lambda ^ { p } E ^ { * }$ . With these identifications, one has the formulas $v ( \alpha _ { 1 } \wedge . . . \wedge \alpha _ { p } ) = v ( \alpha _ { 1 } , . . . \alpha _ { p } )$ for $v \in ( \Lambda ^ { p } E ^ { * } ) ^ { * } = \Lambda ^ { p } E$ and $\alpha _ { i } \in E ^ { * }$ and similarly $\alpha ( v _ { 1 } \wedge . . . v _ { p } ) = \alpha ( v _ { 1 } , . . . , v _ { p } )$ for $\alpha \in ( \Lambda ^ { p } E ) ^ { * } = \Lambda ^ { p } E ^ { * }$ and $v _ { i } \in E$

## 1.9 Hermitian Forms

Let E be an n-dimensional vector space over C and let $h : E \times E \to \mathbf { C }$ be a Hermitian form on $E _ { i }$ , i.e. for every $u \in E$ the mapping $v \mapsto h ( u , v )$ is complex antilinear $( h ( u , c v ) = \bar { c } h ( u , v ) )$ , for every $v \in E$ the mapping $u \mapsto h ( u , v )$ is complex linear, and $h ( v , v ) > 0$ for every nonzero element v of E.

From now on we regard E as a 2n-dimensional vector space over R. Then the real part $g : = { \mathrm { R e } } h$ of h is an inner product on $E _ { i }$ , and therefore a nondegenerate symmetric bilinear form. Because

$$
\mathrm { I m } h ( u , v ) = - \mathrm { R e } ( \mathrm { i } h ( u , v ) ) = - \mathrm { R e } h ( \mathrm { i } u , v ) = - \mathrm { R e } h ( v , \mathrm { i } u ) = \mathrm { R e } ( \mathrm { i } h ( v , u ) ) = - \mathrm { I m } h ( v , u ) ,
$$

we see that the imaginary part $\sigma : = \operatorname { I m } h$ is an antisymmetric bilinear form on E. These equations also show that $ \sigma = - g \circ J , { \mathrm { i f ~ } } J : E \to E$ is the real linear transformation in E defined by $J ( u ) = \mathrm { i } u$ $u \in E ,$ the complex multiplication by means of the complex number i. Because $J : E  E$ and $g : E \to E ^ { * }$ are injective, $\sigma : E  E ^ { * }$ is injective as well, and we conclude that σ is a symplectic form on E. Note that $J ^ { 2 } = - 1$ and therefore g can also be expressed in terms of σ by means of the formula $g = \sigma \circ J ,$ , and the Hermitian form is equal to $h = \sigma \circ J + \mathrm { i } \ \sigma$

In general, if E is a vector space over R, then a complex structure in E is defined as a real linear mapping $J : E  E$ such that $J ^ { 2 } = - 1$ . This makes E into a complex vector space if we define $( a + \mathrm { i } b ) v = a v + J ( b v )$ for any $a , b \in \mathbf { R }$ and $v \in E$ , and it follows that the real dimension of E is equal to 2n if n denotes the dimension of E as a complex vector space.

That every symplectic form is equal to the imaginary part of a Hermitian form with respect to a suitable complex structure, can be seen by bringing the symplectic form into the standard form (1.2), writing $z _ { j } = q _ { j } + \mathrm { i } \ p _ { j }$ and taking the standard Hermitian form

$$
h ( z , z ^ { \prime } ) = \sum _ { j = 1 } ^ { n } z _ { j } \overline { { z _ { j } ^ { \prime } } }\tag{1.12}
$$

in Cn .

The vectors $e _ { 1 } , \ldots , e _ { n } \in E$ form an h-orthonormal basis of the complex vector space $E ,$ if and only if they form a g-orthonormal basis of a Lagrange plane L. Let $\mathrm { U } ( E , h )$ denote the unitary group of all complex linear transformations $A : E  E$ such that $A ^ { * } ( h ) = h$ , in which the Hermitian form $A ^ { * } h$ on $E$ is defined by $( A ^ { * } h ) ( u , v ) = h ( A u , A v )$ for all $u , v \in E$ . Note that

$$
\operatorname { U } ( E , h ) = \operatorname { G L } _ { \mathbf { C } } ( E ) \cap \operatorname { O } ( E , g ) = \operatorname { G L } _ { \mathbf { C } } ( E ) \cap \operatorname { S p } ( E , \sigma ) = \operatorname { S p } ( E , \sigma ) \cap \operatorname { O } ( E , g ) ,
$$

in which $\mathrm { G L } _ { \mathbf { C } } ( E )$ denotes the group of complex linear transformations oin E and $ { \mathrm { O } } ( E , g )$ denotes the group of g-orthogonal real linear transformations in E. This is based on the fact that a real linear transformation A in E is complex linear if and only if $A \circ J = J \circ A$ , and $g = \sigma \circ J$ and $h = g + \mathrm { i } \ \sigma$

Because $\mathrm { U } ( E , h )$ acts transitively on the set of all h-orthonormal bases of $E ,$ the compact Lie group $\mathrm { U } ( E , h )$ also acts transitively on the Lagrangian Grassmannian. Because for any $A \in$ $\mathrm { U } ( E , h )$ we have that $A ( L ) = L$ if and only if A is the complex linear extension to $E$ of a $g -$ -orthogonal transformation in $L ,$ this leads to an identification of ${ \mathcal { L } } ( E , \sigma )$ with the homogeneous space $\mathrm { U } ( E , h ) / \mathrm { U } ( E , h ) _ { L }$ , in which $\mathrm { U } ( E , h ) _ { L }$ is isomorphic to $ { \mathrm { O } } ( L , g )$ . This is the meaning of the equation $\Lambda ( n ) = \mathrm { U } ( n ) / \mathrm { O } ( n )$ in [1].

## 1.10 Historical Remarks

The name ”symplectic” has been introduced in 1939 by Hermann Weyl as the Greek adjective corresponding to the word ”complex”, which for him referred to the linear line complexes introduced by Pl¨ucker, see Exercise 1.3. According to the footnote on p. 165 of [29]:

The name ”complex group” formerly advocated by me in allusion to line complexes, as they are defined by the vanishing of antisymmetric forms, has become more and more embarassing through collision with the word ”complex” in the connotation of complex number. I therefore propose to replace it by the corresponding Greek adjective ”symplectic”. Dickson calls the group ”Abelian linear group” in homage to Abel who first studied it.

(The name given by Dickson is even more embarassing, as ”Abelian group” nowadays is used for ”commutative group”, whereas the symplectic group is highly noncommutative.)

The names ”Lagrange plane” and ”Lagrangian Grassmannian” have been introduced by Arnol’d [1], after the name ”Lagrange manifold”, introduced by Maslov [23, p. 115] in 1965 for a manifold of which all tangent spaces are Lagrange planes.

## 1.11 Exercises

Exercise 1.1 In the notation of Subsection 1.9, prove that $J \in \mathrm { S p } ( E , \sigma )$ . Prove that if $L$ is a Lagrange plane, then $J ( L )$ is a Lagrange plane which is g-orthogonal to L, and therefore satisfies $J ( L ) \cap L = \{ 0 \}$ .

Exercise 1.2 It was the idea of Pl¨ucker (1846), to consider the projective lines in the threedimensional space as the elements (points) of a new space. The three-dimensional projective space is defined as the space $\mathrm { P } ( E )$ of all one-dimensional linear subspaces l of the four-dimensional vector space E. A projective line is equal to the set $\mathrm { P } ( L )$ of all one-dimensional linear subspaces l of a twodimensional linear subspace L of E. In this way, Pl¨ucker’s space is identified with the Grassmann manifold $\mathrm { G } _ { 2 } ( E )$ of all two-dimensional linear subspaces L of the four-dimensional vector space $E .$

Let $a , b \in E$ be linearly independent. Prove that $u = a \wedge b$ is a nonzero element of $\Lambda ^ { 2 } E$ such that $u \wedge u = 0$ . Prove that every nonzero $u \in \Lambda ^ { 2 } E$ such that u $\wedge u = 0$ arises in this way, and that $x \in E$ is equal to a linear combination of a and b, if and only if $u \wedge x = 0$ . Prove that the relation between $L \in \mathrm { G } _ { 2 } ( E )$ and $u \in \Lambda ^ { 2 } E$ , that $u = a \wedge b$ for a basis a, b of $L ,$ is equivalent to u $\wedge x = 0$ for every $x \in L$ . Prove that this relation defines a bijection between $\mathrm { G } _ { 2 } ( E )$ and the quadric Q in the five-dimensional projective space $\mathrm { ~ P ~ } ( \Lambda ^ { 2 } E )$ defined by the equation u $\wedge u = 0$ . Prove that $( u , v ) \mapsto u \wedge v$ is a nondegenerate symmetric bilinear form on $\Lambda ^ { 2 } E$ with values in the one-dimensional vector space $\Lambda ^ { 4 } E$ , and that, as a consequence, the quadric Q is smooth.

The co¨ordinates of $\Lambda ^ { 2 } E$ are called Pl¨ucker coordinates on $\mathrm { G } _ { 2 } ( E )$ Stricly speaking these should be regarded as projective co¨ordinates and, as functions on the projective coordinate patches of $\mathrm { ~ P ~ } ( \Lambda ^ { 2 } E )$ , be restricted to the quadric Q.

Exercise 1.3 Pl¨ucker [26] defined a line complex of degree m as the intersection of $Q$ with an algebraic hypersurface in $\mathrm { ~ \bar { P } ~ } ( \Lambda ^ { 2 } E )$ of degree m, defined by the equation $F ( u ) = 0$ in which $F$ is a homogeneous polynomial of degree m on $\Lambda ^ { 2 } E$ . He defined a linear line complex as a line complex of degree one.

Prove that a linear line complex corresponds to a nonzero two-form $\sigma \in \Lambda ^ { 2 } E ^ { * }$ on $E _ { i }$ unique up to a nonzero scalar multiple, such that $L \in \mathrm { G } _ { 2 } ( E )$ belongs to the linear line complex if and only if $L$ is σ-isotropic. Prove that if $\sigma$ is nondegenerate, then the linear line complex defined by $\sigma ,$ viewed as a subset of $\mathrm { G } _ { 2 } ( E )$ , is equal to the manifold ${ \mathcal { L } } ( E , \sigma )$ of all the Lagrange planes with respect to the symplectic form $\sigma$

Prove that if $\sigma$ is degenerate, then ker $\sigma \in \mathrm { G } _ { 2 } ( E )$ In this case Pl¨ucker called the corresponding linear line complex special and called ker σ the axis of the special linear line complex. Prove that the special linear line complex is equal to the set of all $L \in \mathrm { G } _ { 2 } ( E )$ such that $L \cap$ ker $\sigma \ne 0$ . In terms of projective lines: the special line complex is equal to the set of all projective lines which intersect its axis.

Exercise 1.4 We use the notation of Subsection 1.6.

Let $L \in \mathcal { L } ( E , \sigma ) , I \in \mathrm { G } _ { m } ( L )$ . Prove that σ induces a symplectic form on the $( 2 n - 2 m ) .$ -dimensional vector space $I ^ { \sigma } / I$ Prove that $L ^ { \prime } \in \mathcal { L } ( E , \sigma )$ and $L ^ { \prime } \cap L = I$ if and only if $L ^ { \prime } / I$ is a Lagrange plane in $I ^ { \sigma } / I$ which is transversal to $L / I$ . Prove that the mapping $L ^ { \prime } \mapsto L ^ { \prime } \cap L$ exhibits $\mathcal { L } _ { L , m }$ as a smooth bundle over $\mathrm { G } _ { m } ( L )$ of which each fiber is an affine space of dimension $\begin{array} { l } { { \frac { 1 } { 2 } } ( n - m ) ( n - m + 1 ) } \end{array}$ , Prove $\mathcal { L } _ { L , m }$ is a smooth submanifold of ${ \mathcal { L } } ( E , \sigma )$ of dimension equal to $\begin{array} { r } { { \frac { 1 } { 2 } } n ( n + 1 ) - { \frac { 1 } { 2 } } m ( m + 1 ) } \end{array}$ ). Prove that the closure of $\mathcal { L } _ { L , m }$ in ${ \mathcal { L } } ( E , \sigma )$ is equal to $\cup _ { l = m } ^ { n } \mathcal { L } _ { L , l } . \qquad \ O$

Exercise 1.5 Let $\gamma$ be a differentiable curve in $\mathcal { L } = \mathcal { L } ( E , \sigma )$ such that $\gamma ( t _ { 0 } ) \in \mathcal { L } _ { L , 1 }$ . Prove that $\gamma ( t )$ intersects $\mathcal { L } _ { L , 1 }$ transversally at $t = t _ { 0 }$ , i.e. $\gamma ^ { \prime } ( t _ { 0 } ) \notin \mathrm { T } _ { \gamma ( t _ { 0 } ) } \mathcal { L } _ { L , 1 }$ , if and only if the restriction to $\gamma ( t _ { 0 } ) \cap L$ of the symmetric bilinear on $\gamma ( t _ { 0 } )$ , which is assigned to $\gamma ^ { \prime } t ( t _ { 0 } ) \in \mathrm { T } \mathcal { L }$ as in Subsection 1.6, is nonzero. We will call the intersection positive or negative according to whether this restriction is positive or negative definite, respectively.

It is known that by slight perturbation every closed curve $\gamma$ . in $\mathcal { L }$ can be made such that all intersections with $\mathcal { L } _ { L , 1 }$ are transversal. prove that this implies that $\gamma$ intersects $\mathcal { L } _ { L , 1 }$ only finitely many times. Write $i ( \gamma )$ for the number of positive intersections minus the number of negative intersections.

It is also known that by slight perturbation any homotopy of closed curves, viewed as a mapping from a two-dimensional cylinder to $\mathcal { L }$ can be made to miss each of the manifolds $\mathcal { T } _ { L , m }$ with $m \geq 2$ , each of which has codimension $\geq 3$ in $\mathcal { L }$ . This shows that $i ( \gamma )$ only depends on the homotopy class of $\gamma _ { ; }$ , and i induces a homomorphism from the fundamental group $\pi _ { 1 } ( \mathcal { L } )$ of $\mathcal { L }$ to $\mathbf { Z }$

Prove that $\mathcal { L } _ { L , 1 }$ is connected and that $\mathcal { L } _ { L , 0 }$ is simply connected. Prove that if $i ( \gamma ) = 0$ , then $\gamma$ is contractible in $\mathcal { L }$ . Finally, find a smooth closed curve $\gamma$ in $\mathcal { L }$ such that $i ( \gamma ) = 1$ and prove that $i : \pi _ { 1 } ( { \mathcal { L } } ) \to \mathbf { Z }$ is an isomorphism.

Remark Maslov [23, p. 147–149] called the set $\Sigma = \overline { { \mathcal { L } _ { L , 1 } } }$ and the integer $i ( \gamma )$ the singular set and the index of the curve $\gamma ,$ respectively. Arnol’d [1] observed that Σ defines an oriented codimension one cycle in $\mathcal { L } .$ , that the index is equal to the topological intersection number of the one-dimensional cycle $\gamma$ with Σ and that the index defines an isomorphism of the fundamental group of $\mathcal { L }$ with $\mathbf { Z } .$

## 2 Symplectic Manifolds

## 2.1 Definition

Let M be a finite-dimensional smooth manifold. A symplectic form on M is a smooth differential form σ of degree two on M such that

i) For every $m \in M$ the bilinear form $\sigma _ { m }$ on $\mathrm { T } _ { m } M$ is nondegenerate, and

ii) σ is closed, i.e. d $\sigma = 0$

Condition i) means that, for every $m \in M , \sigma _ { m }$ is a symplectic form on $\mathrm { T } _ { m } M$ . This implies that dim M = dim $\mathrm { T } _ { m } M$ is even, say equal to 2n, cf. Subsection 1.4. A symplectic manifold is defined as a pair $( M , \sigma )$ , in which M is a finite-dimensional smooth manifold and σ is a symplectic form on M .

Example 2.1 Probably the simplest example is $\mathbf { R } ^ { n } \times \mathbf { R } ^ { n }$ provided with the ”constant” standard symplectic form of (1.2), which in differential form notation is equal to

$$
\sigma = \sum _ { j = 1 } ^ { n } \mathrm { d } p _ { j } \wedge \mathrm { d } q _ { j } .\tag{2.1}
$$

Here $p _ { j }$ and $q _ { j }$ are viewed as (coordinate) functions on $\mathbf { R } ^ { n } \times \mathbf { R } ^ { n }$

0

## 2.2 The Cotangent Bundle

An important generalization of the previous example is obtained by starting with an arbitrary ndimensional smooth manifold X. The cotangent bundle $\mathrm { T } ^ { * } X$ of X is defined as the vector bundle over X of which the fiber at the point $x \in X$ is equal to the dual $\mathrm { T } _ { x } ^ { * } X : = ( \mathrm { T } _ { x } X ) ^ { * }$ of $\mathrm { T } _ { x } X$ , the space of all linear forms ξ on the tangent space $\mathrm { T } _ { x } X$ of X at the point x.

Let π denote the projection from $M : = \Gamma _ { x } ^ { * } X$ onto X. which sends every element of T∗x X to x. Then, for every $\xi \in \mathrm { T } _ { x } ^ { * } X$ , the tangent map $\mathrm { T } _ { \xi } \pi$ is a linear mapping from $\mathrm { T } _ { \xi } M$ onto $\mathrm { T } _ { x } X$ , and if we subsequently apply the linear form $\xi \in ( \Gamma _ { x } \boldsymbol { X } ) ^ { * }$ to it, we obtain the linear form

$$
\tau _ { \xi } : = \xi \circ \mathrm { T } _ { \xi } \pi\tag{2.2}
$$

on $\mathrm { T } _ { \xi } M$ . This defines a special smooth differential form $\tau$ of degree one on M.

If α is any smooth differential form of degree one on X, then it can also be viewed as a smooth mapping α : $\colon X \to \mathrm { T } ^ { * } X$ such that $\pi \circ \alpha$ is equal to the identity on X. It follows that

$$
( \alpha ^ { * } \tau ) _ { x } = \tau _ { \alpha ( x ) } \circ \mathrm { T } _ { x } \alpha = \alpha ( x ) \circ \mathrm { T } _ { \alpha ( x ) } \pi \circ \mathrm { T } _ { x } \alpha = \alpha ( x ) \circ \mathrm { T } _ { x } ( \pi \circ \alpha ) = \alpha ( x ) ,
$$

where in the first, second, third and last identity we used the definition of pullback of a differential form, the definition of $\tau _ { : }$ , the chain rule for differentiation and $\pi \circ \alpha = \operatorname { I d }$ , respectively. The equation

$$
\alpha { = } \alpha ^ { * } \tau \quad \mathrm { f o r ~ e v e r y ~ o n e - f o r m ~ } \alpha \ \mathrm { o n } \ X\tag{2.3}
$$

says that every one-form on X is equal to the pullback of $\tau$ by means of the one-form viewed as a mapping from X to $\mathrm { T } ^ { * } X$ . For this reason τ is called the tautological one-form on the cotangent bundle.

The exterior derivative

$$
\sigma : = \mathrm { d } \tau\tag{2.4}
$$

of the tautological one-form is a two-form on $\mathrm { T } ^ { * } X$ , which is closed because $\mathrm { d } ( \mathrm { d } \omega ) = 0$ for every differential form $\omega$ (of any degree). Moroever, in local coordinates $( x _ { 1 } , \ldots , x _ { n } )$ on X, with corresponding dual coordinates $( \xi _ { 1 } , \ldots , \xi _ { n } )$ , the equation (2.2) takes the form

$$
\tau = \sum _ { i = 1 } ^ { n } \xi _ { i } \mathrm { d } x _ { i } ,\tag{2.5}
$$

and therefore

$$
\sigma = \sum _ { i = 1 } ^ { n } \mathrm { d } \xi _ { i } \wedge \mathrm { d } x _ { i } ,\tag{2.6}
$$

which shows that $\sigma$ is equal to the standard symplectic form if we substitute $x _ { i } = q _ { i }$ and $\xi _ { i } = p _ { i }$ This shows that $\sigma : = \mathrm { d } \tau$ is a symplectic form on $\mathrm { T } ^ { * } X$ , which is called the canonical symplectic form of the cotangent bundle.

## 2.3 Reduction

Let N be a smooth manifold and let $\omega$ be a closed smooth two-form on N for which the kernel has constant rank, i.e. there exists a nonnegative integer k such that, for every $n \in N$ , dim $( \ker \omega _ { n } ) = k$ This implies that the $K _ { n } : = \ker \omega _ { n } , n \in N .$ define a smooth vector subbundle K of the tangent bundle TN of N. (In the present differential geometric terminology, a smooth vector subundle of the tangent bundle of N is also called a distribution on $N ,$ not to be confused with the distributions in Analysis. In the 19-th century literature a smooth vector subbundle of the tangent bundle of N is called a Pfaffian system in N.)

A general smooth vector subbundle K of the tangent bundle TN of any finite-dimensional smooth manifold N is called integrable if for each $n _ { 0 } \in N$ there exists an open neighborhood $N _ { 0 }$ of $n _ { 0 }$ in N and a smooth fibration of $N _ { 0 }$ , such that, for each $n \in N _ { 0 } , K _ { n }$ is equal to the tangent space of the fiber through n. The theorem of Frobenius says that K is integrable if and only if $[ X , Y ] \subset K$ holds for any pair of smooth vector fields $X , Y$ on N such that $X \subset K$ and $Y \subset K$ .

Returning to our two-form ω with kernel of constant rank, the claim is that the closedness of ω implies that its kernel $K : = \ker \omega$ is integrable. For the proof we use that [X, Y ] is equal to the Lie derivative $\mathcal { L } _ { X } Y$ of Y with respect to the vector field X. In view of the Leibniz formula for Lie derivatives, it follows that

$$
\begin{array} { r } { \mathbf i _ { [ X , Y ] } \omega = \mathcal L _ { X } \left( \mathrm i _ { Y } \omega \right) - \mathrm i _ { Y } \left( \mathcal L _ { X } \omega \right) , } \end{array}
$$

whereas the homotopy formula for the Lie derivaritive yields that

$$
{ \mathcal { L } } _ { X } \omega = \mathrm { i } _ { X } ( \mathrm { d } \omega ) + \mathrm { d } \left( \mathrm { i } _ { X } \omega \right) .\tag{2.7}
$$

Therefore, $\mathrm { i } _ { Y } \omega = 0 , \mathrm { i } _ { X } \omega = 0$ and dω = 0 imply that $\operatorname { i } _ { [ X , Y ] } \omega = 0$

Now suppose that $\pi : N \to M$ is a fibration with connected fibers, such that, for each $n \in N$ , ker $\omega _ { n }$ is equal to the tangent space ker $\mathrm { T } _ { n } \pi$ of the fiber through the point n. Fix $m \in M$ . Then there exists, for each $n \in \pi ^ { - 1 } ( \{ m \} )$ , a unique two-form $\sigma _ { m , n }$ on $\mathrm { T } _ { m } M$ , such that $( \mathrm { T } _ { n } \pi ) ^ { * } \sigma _ { m , n } = \omega _ { n }$ However, for each smooth vector field X such that $X \subset K$ we see from (2.7) that ${ \mathcal { L } } _ { X \omega } = 0 .$ , which implies that $( \mathrm { e } ^ { t X } ) ^ { * } \omega = \omega$ , whereas on the other hand $\pi \circ \operatorname { e } ^ { t X } = \pi$ . This implies that $\sigma _ { m , n ^ { \prime } } = \sigma _ { m , n }$ if $n ^ { \prime } = \operatorname { e } ^ { t X } ( n )$ Because the compositions of the flows $e ^ { t X }$ with $X \subset K$ act locally transitively on the fibers, and therefore transitively because the fibers are connected, the conclusion is that $\sigma _ { m , n } = \sigma _ { m }$ does not depend on the choice of $n \in \pi ^ { - 1 } ( \{ m \} )$ .

The $\sigma _ { m } , m \in M$ , define a smooth two-form on M such that $\omega = \pi ^ { * } \sigma$ . Because

$$
\ker \mathrm { T } _ { n } \pi = \ker \omega _ { n } = \mathrm { T } _ { n } \pi ^ { - 1 } ( \ker \sigma _ { m } ) ,
$$

it follows that ker $\sigma _ { m } = \{ 0 \}$ , which means that $\sigma _ { m }$ is a symplectic form. Furthermore, $\pi ^ { * } ( \mathrm { d } \sigma ) =$ $\mathrm { d } ( \pi ^ { * } \sigma ) = \mathrm { d } \omega = 0$ , which in view of the surjectivity of the linear mappings $\mathrm { T } _ { n } \pi , n \in N$ implies that $\mathrm { d } \sigma = 0$ In other words, $( M , \sigma )$ is a symplectic manifold, which is called the reduced symplectic manifold of the pair $( N , \omega )$

## 2.4 Complex Projective Varieties

Let E be an n-dimensional complex vector space with Hermitian form h, which we provide with real inner product $g = \operatorname { R e } h$ and the symplectic form σ = Im h as in Subsection 1.9, which are related by $g = \sigma \circ J$ . Let

$$
S : = \{ z \in E \mid h ( z , z ) = g ( z , z ) = 1 \}
$$

be the unit sphere in E with respect to the inner product g. Then, for each $z \in S$

$$
\mathrm { T } _ { z } S = \{ v \in E \mid g ( z , v ) = 0 \} = \{ v \in E \mid \sigma ( \mathrm { i } z , v ) = 0 \} .
$$

It follows that $\mathrm { i } z \in \mathrm { T } _ { z } S _ { \mathrm { \Omega } }$ and i z belongs to the kernel of the restriction to $\mathrm { T } _ { z } S$ Because $\mathrm { T } _ { z } S$ has real codimension one in $E _ { \mathrm { { i } } }$ its symplectic orthogonal complement is real one-dimensional, and therefore equal to R i z. On the other hand $\mathbf { R } \mathrm { ~ i ~ } z$ is equal to the tangent space of the circle

$$
C _ { z } : = \{ c z \mid c \in \mathbf { C } , \mid c \mid = 1 \} = ( \mathbf { C } z ) \cap S
$$

through the point z. If we denote the identity mapping from S to E by ι, then $\iota ^ { * } \sigma$ is the restriction to S of the two-form $\sigma ,$ and the fibration of S by the integral curves of the kernels of $\iota ^ { * } \sigma$ is equal to the fibration of S by the circles $C _ { z } , z \in S$ . On the space M of these circles we have the reduced symplectic form ${ \widehat { \sigma } } .$ , the unique two-form $\widehat { \sigma }$ on M such that $\iota ^ { * } \sigma = \pi ^ { * } { \widehat { \sigma } } , { \mathrm { i f ~ } } \pi : S  M$ denotes the projection defined by $\pi ( z ) = C _ { z } , z \in S$

On the other hand the $\mathbf { C } z , z \in S .$ , are the complex one-dimensional linear subspaces l of E, which form the elements of the complex $( n - 1 )$ -dimensional projective space $\mathbf { C P } ( E )$ of E. The mapping $l \mapsto l \cap S$ is a diffeomorphism from $\mathbf { C P } ( E )$ onto M, which can be used in order to identify M with $\mathbf { C P } ( E )$ . Note that $\mathbf { C P } ( E )$ is a complex analytic manifold, with a complex multiplication $J _ { l }$ by i in each tangent space $\mathrm { T } _ { l } ( \mathbf { C P } ( E ) )$ . It is easily verified that $\widehat { \boldsymbol g } : = \widehat { \boldsymbol \sigma } \circ { \boldsymbol J }$ is the inner product on $\mathrm { T } _ { l } ( \mathbf { C P } ( E ) )$ which correpsonds to the restriction of g to the g-orthogonal complement of i z in $\mathrm { T } _ { z } S$

I $\mathbf { f } \mathbf { \Lambda } { \boldsymbol { E } } = \mathbf { C } ^ { n }$ and h is the standard hermitian structure on Cn, then the Hermitian inner product ${ \widehat { h } } : = { \textstyle { \frac { 1 } { \pi } } } \left( { \widehat { g } } + \mathrm { i } { \widehat { \sigma } } \right)$ is called the Fubini-Study metric on $\mathbf { C P } ( E ) = \mathbf { C P } _ { n - 1 }$ Here the factor $1 / \pi$ is inserted in order to arrange that the integral of $\omega : = { \frac { 1 } { \pi } } { \widehat { \sigma } }$ over any complex projective line in $\mathbf { C P } _ { n - 1 }$ is equal to one.

More generally, if M is a complex analytic manifold, then a K¨ahler structure on M is a smooth Hermitian inner product h on its tangent bundle, such that its imaginary part, the two-form σ := Im $h ,$ is closed. This implies that σ is a symplectic form on M, called the K¨ahler form of the

K¨ahler manifold (M, h). The Fubini-Study metric is a K¨ahler structure on the complex projective space.

I ${ \mathrm { ~ f ~ } } \iota : V \to M$ is a complex analytic submanifold of a K¨ahler manifold (M, h), then the restriction $\iota ^ { * } h$ of h to $\mathrm { T } V$ is a K¨ahler structure on V . This exhibits every smooth complex projective variety as a K¨ahler manifold, by providing it with the restriction to its tangent bundle of the Fubini-Study metric of the projective space of which it is a subvariety. This is a very rich source of examples of compact symplectic manifolds. Vice versa, this introduces symplectic differential geometry into complex algebraic geometry.

## 2.5 Almost Complex Structure

An almost complex structure J on a smooth manifold M is a complex structure $J _ { m }$ on each tangent space $\mathrm { T } _ { m } M$ , depending smoothly on $m \in M$ . As in Subsection 1.9, this turns each tangent space into a complex vector space. If n is the complex dimension of $\mathrm { T } _ { m }$ M with respect to the complex structure $J _ { m } ,$ then the real dimension is equal to $2 n$

An almost complex manifold is a pair $( M , J )$ in which M is a smooth manifold and J is an almost complex structure on M. The almost complex structure is called integrable if for every $m _ { 0 } \in M$ there is coordinate system in an open neighborhood of $m _ { 0 }$ in M, in which $m \mapsto J _ { m }$ is constant. If we use the constant complex structure in order to identify $\mathbf { R } ^ { 2 n }$ with $\mathbf { C } ^ { n }$ , we obtain a system of local coordinatizations for which the coordinate changes are complex analytic mappings. With these coordinatizations, M is a complex analytic manifold for which the $J _ { m }$ are the multiplications by i in the tangent spaces.

For each $m \in M$ one has the antisymmetric bilinear mapping $[ J , J ] _ { m }$ from $\mathrm { T } _ { m } M \times \mathrm { T } _ { m } M$ to $\mathrm { T } _ { m } M$ , which is defined by

$$
[ J , J ] ( v , w ) = [ J v , J w ] - J \left[ J v , w \right] - J \left[ v , J w \right] - [ v , w ] ,\tag{2.8}
$$

in which v and w are smooth vector fields on M and the brackets in the right hand side are the Lie brackets of vector fields. The theorem of Newlander and Nirenberg says that the almost complex structure J is integrable, if and only if $[ J , J ] = 0$ , cf. [25], [13], [22].

Lemma 2.2 Let σ be a symplectic form on M. Then there exists an almost complex structure J on M such that $h = \sigma \circ J + \mathrm { i } ~ \sigma$ is a Hermitian structure on TM . If σ is invariant under the action of a group G on M, and M carries a G-invariant Riemannian structure, then J can be chosen to be G-invariant as well.

Proof There exists a Riemannian structure g in M. Such a Riemannian structure exists in local coordinates. Let $\xi _ { j }$ be a smooth partition of unity subordinate to ta locally finite covering of M by means of open subsets $M _ { j }$ on which we have a Riemannian structure $g _ { j }$ . This means that the $\xi _ { j }$ are smooth real valued functions on M such that $\xi _ { j } \ge 0$ , the support of $\xi _ { j }$ is contained in $M _ { j }$ and $\textstyle \sum _ { j } \xi _ { j } = 1$ . Then $\begin{array} { r } { g = \sum _ { j } \xi _ { j } g _ { j } } \end{array}$ is the desired Riemannian structure on M.

Define, for each m ∈ M, $A _ { m } : = \sigma _ { m } ^ { - 1 } g _ { m }$ Then $g _ { m } \circ A _ { m } = g _ { m } \circ \sigma _ { m } ^ { - 1 } \circ g _ { m }$ is antisymmetric, or $A _ { m }$ is gm-antisymmetric, and there exists a $g _ { m }  – \mathbf { O } ]$ rthonormal basis in $\mathrm { T } _ { m } M$ on which the matrix of $A _ { m }$ consists of $2 \times 2$ -matrices $\left( \begin{array} { c c } { { 0 } } & { { - a _ { j } } } \\ { { a _ { j } } } & { { 0 } } \end{array} \right)$ along the diagonal, with $a _ { j } > 0$ . Let $B _ { m }$ be the linear transformation in $\mathrm { T } _ { m } M$ of which the matrix consists of the 2 × 2-matrices $\left( \begin{array} { c c } { 1 / a _ { j } } & { 0 } \\ { 0 } & { 1 / a _ { j } } \end{array} \right)$

along the diagonal. Then $J _ { m } : = A _ { m } \circ B _ { m } = \sigma _ { m } ^ { - 1 } \circ g _ { m } \circ B _ { m }$ is a complex structure on $\mathrm { T } _ { m } M$ $\widehat { g } _ { m } : = g _ { m } \circ B _ { m } = \sigma _ { m } \circ J _ { m }$ is an inner product on $\mathrm { T } _ { m } M$ and therefore $\sigma _ { m } \circ J _ { m } + \mathrm { i } ~ \sigma$ is a Hermitian bform on $\mathrm { T } _ { m } M$

At first sight this construction seems to depend on the choice of the $g _ { m } \mathrm { { - o r t h o n o r m a l } }$ basis, but $B _ { m } ^ { 2 } = - A _ { m } ^ { - 2 }$ , which shows that actually $B _ { m }$ is equal to the unique positive definite square root of the positive definite linear transformation $- A _ { m } ^ { - 2 }$ (all with respect to the inner product $g _ { m } )$ . This makes $J _ { m }$ globally well-defined and depending smoothly on $m \in M$ •

If σ and g are G-invariant, then the uniqueness of the $B _ { m } , m \in M$ , make that also B and J are G-invariant. ✷

It cannot always be arranged that in addition J is integrable. In other words, not every symplectic form is equal to a K¨ahler form on a complex analytic manifold. However, the weaker almost complex structure is sufficient for many purposes.

## 2.6 Cohomology Classes

It follows from the observation in Subsection 1.8 that the n-the power of a symplectic form is nonzero that $\sigma ^ { n }$ is a nowhere vanishing volume form on M.

Assume in the sequel that M is compact and connected. Then the de Rham cohomology class $[ \sigma ^ { n } ] \in \mathrm { H } ^ { 2 n } ( M )$ of the nowhere vanishing volume form $\sigma ^ { n }$ is nonzero, and therefore generates the one-dimensional vector space $\mathrm { H } ^ { 2 n } ( M )$ Because $[ \sigma ^ { n } ] = [ \sigma ] ^ { n }$ , this in turn implies that the element $[ \sigma ] ^ { k } \in { \mathrm { H } } ^ { 2 k } ( M )$ is nonzero for every $1 \leq k \leq n$

The fact that $H ^ { 2 k } ( M ) \neq 0 .$ or more precisely that there exists an $s \in \mathrm { H } ^ { 2 } ( M )$ such that $s ^ { k } \neq 0$ for every $1 \leq k \leq n .$ , puts a quite severe topological restriction on a compact smooth manifold for allowing a symplectic form. For instance, if M is a 2n-dimensional sphere, then $\mathrm { H } ^ { p } ( M ) = 0$ for all p except $p = 0$ and $p = 2 n$ , and therefore the only sphere which can carry a symplectic form is the two-dimensional one.

If M is the complex n-dimensional complex projective space, then $\mathrm { H } ^ { p } ( M ) = 0$ except when $p ~ = ~ 2 k , ~ 0 ~ \le ~ k ~ \le ~ n$ , in which case dim $H ^ { 2 k } ( M ) = 1$ . In other words, in this case the whole cohomology ring is generated by the cohomology class [ω] of the K¨ahler form $\omega$ defined by the Fubini-Study metric. This is even true for the cohomology ring with values in Z, cf. [9, pp. 60, 150].

## 2.7 Exercises

Exercise 2.1 let X and Y be smooth manifolds and let $\phi : X \to Y$ be a local diffeomorphism. Define the induced transformation $\Phi : \mathrm { T } ^ { * } X \to \mathrm { T } ^ { * } Y$ by

$$
\begin{array} { r } { \Phi ( x , \xi ) : = \left( \phi ( x ) , \left( \left( \mathrm { T } _ { x } \phi \right) ^ { * } \right) ^ { - 1 } ( \xi ) \right) , \quad x \in X , \xi \in \left( \mathrm { T } _ { x } X \right) ^ { * } . } \end{array}
$$

Prove that

$$
\Phi ^ { * } \tau _ { \mathrm { T } ^ { * } Y } = \tau _ { \mathrm { T } ^ { * } X }
$$

and that

$$
\Phi ^ { * } \sigma _ { \mathrm { T } ^ { * } Y } = \sigma _ { \mathrm { T } ^ { * } X } .
$$

In other words, the induced mapping is a canonical transformation, in the sense that it preserves the canonical symplectic forms.

## Exercise 2.2 Consider the standard coordinatization

$$
\boldsymbol \varphi : \left( z _ { 1 } , \ldots , z _ { n } \right) \mapsto \mathbf { C } \left( 1 , z _ { 1 } , \ldots , z _ { n } \right)
$$

of the open subset of the n-dimensional complex projective space which consist of the one-dimensional complex linear subspaces l which are not contained in the n-dimensional linear subspace defined by the equation $z _ { 0 } = 0$ . Write

$$
w = \psi ( z ) : = ( 1 + ( z , z ) ) ^ { - 1 / 2 } \left( 1 , z _ { 1 } , . . . , z _ { n } \right) ,
$$

$w _ { j } = u _ { j } + \mathrm { ~ i ~ } v _ { j }$ with $u _ { j } , v _ { j } \in \mathbf { R } , 0 \leq j \leq n$ , and $z _ { j } = x _ { j } + \mathrm { i } \ y _ { j }$ with xj , $y _ { j } \in \mathbf { R } , 1 \leq j \leq n$ . Prove that the pullback of the Fubini-Study K¨ahler form ω under $\varphi$ satisfies

$$
\begin{array} { r c l } { \pi \omega } & { : = } & { \displaystyle \psi ^ { * } \left( \sum _ { j = 0 } ^ { n } \mathrm { d } v _ { j } \wedge \mathrm { d } u _ { j } \right) = ( 1 + ( z , z ) ) ^ { - 1 } \sum _ { j = 1 } ^ { n } \mathrm { d } y _ { j } \wedge \mathrm { d } x _ { j } } \\ & & { \displaystyle - ( 1 + ( z , z ) ) ^ { - 2 } \sum _ { j , k = 1 } ^ { n } \left( x _ { j } x _ { k } + y _ { j } y _ { k } \right) \mathrm { d } y _ { j } \wedge \mathrm { d } x _ { k } + x _ { j } y _ { k } \left( \mathrm { d } x _ { j } \wedge \mathrm { d } x _ { k } + \mathrm { d } y _ { j } \wedge \mathrm { d } y _ { k } \right) . } \end{array}
$$

(This may be compared with [9, p. 30, 31].) How easy is it to verify by direct computation that the two-form in the right hand side is closed?

Verify that for $n = 1$ we have

$$
\pi \omega = ( 1 + x ^ { 2 } + y ^ { 2 } ) ^ { - 2 } ~ \mathrm { d } y \wedge \mathrm { d } x ,
$$

and that the integral of ω over the complex projective line is equal to 1.

0

Exercise 2.3 Let J be an almost complex structure on the manifold M. Prove that $[ J , J ] ( v , J v ) =$ 0 for any smooth vector field v on M and prove that J is integrable if dim $M = 2$ . Now assume that dim M = 2, that M is connected and that $\sigma$ is a nowhere vanishing area form = symplectic form on M. Prove that $g : = \sigma \circ J$ is a symmetric bilinear form on each tangent space which is invariant under the linear transformations $\mathrm { e } ^ { t J _ { m } }$ . Prove that $g$ is either positive definite or negative definite. In other words, M is a complex analytic ”curve” and either $\sigma \mathrm { o r } - \sigma$ is equal to the K¨ahler form of a K¨ahler structure on M.

Exercise 2.4 For which compact oriented surfaces is the cohomology ring generated by the class of a symplectic form?

Exercise 2.5 If $n = 2$ in Subsection 2.4, identify the projection $\pi : S \to \mathbf { C P } ( E )$ with the Hopf fibration.

## 3 Hamiltonian Systems

## 3.1 Flows of Vector Fields

Let M be a smooth manifold. If v is a smooth vector field on M then the general theory of systems of ordinary differential equations, see for instance [3], implies the following statements. For every m ∈ M, there is a unique maximal solution $\gamma = \gamma _ { m } : I _ { m }  M$ of the differential equation $\mathrm { d } \gamma ( t ) / \mathrm { d } t = v ( \gamma ( t ) )$ , such that $\gamma ( 0 ) = m$ . The domain of definition $I _ { m }$ of this maximal solution γ is an open interval in R containing 0. If s := sup Im < ∞ or i := inf $I _ { m } > - \infty$ , then there exists for every compact subset K of M an $\epsilon > 0$ such that $\gamma ( t ) \notin K$ for every $t \in ] s - \epsilon .$ s[ or $t \in ] i , i + \epsilon [ ,$ respectively. In other words, the only way the maximal solutions do not exits for all time is that run out of every compact subset of M in a finite time. This implies that $\mathrm { i f } \ \gamma _ { m } ( t )$ stays within a compact subset of M for all $t \in I _ { m }$ , then $I _ { m } = \mathbf { R }$ . The set $D : = \{ ( t , m \in \mathbf { R } \times M \mid t \in I _ { m } \}$ is an open subset of $\mathbf { R } \times M$ which contains $\{ 0 \} \times M$ , and $A : ( t , m ) \mapsto \gamma _ { m } ( t )$ is a smooth mapping from D to M. If $s \in I _ { m }$ and $t \in I _ { \gamma _ { m } ( s ) }$ , then $s + t \in I _ { m }$ and $\gamma _ { m } ( s + t ) = \gamma _ { \gamma _ { m } ( s ) } ( t )$ This follows from the uniquenss of the solutions, because, as a function of $t , \gamma _ { m } ( s + t )$ and $\gamma _ { \gamma _ { m } ( s ) } ( t )$ satisfy the same differential equation and have the same initial value.

We say that the vector field v is complete if $D = { \bf R } \times M$ , in which case $A : \mathbf { R } \times M \to M$ is a smooth action of the additive group $( \mathbf { R } , + )$ on M. The mapping $m \mapsto \gamma _ { m } ( t ) : M \to M$ is called the time t flow of the vector field v an will be denoted by $\mathrm { e } ^ { t \boldsymbol { v } }$ . This notation reminds of the defining equation $\mathrm { d e } ^ { t v } / \mathrm { d } t = v \circ \mathrm { e } ^ { t v }$ and of the group homomorphism property $\mathrm { e } ^ { ( s + t ) v } = \mathrm { e } ^ { t v } \circ \mathrm { e } ^ { s v }$ . Because $\mathrm { e } ^ { t v } \circ \mathrm { e } ^ { - t v } = \dot { \mathrm { I d } } = \mathrm { e } ^ { - t v } \circ \mathrm { e } ^ { t v }$ , the time t flow is a diffeomorphism of M, i.e. it is bijective from M to M and has a smooth inverse (equal to $\mathrm { e } ^ { - t \boldsymbol { v } } )$

If D is a proper subset of $\mathbf { R } \times M$ , then the flow $\mathrm { e } ^ { t \boldsymbol { v } }$ is defined on the open subset

$$
M _ { t } : = \{ m \in M \mid ( t , m ) \in D \}
$$

of M, and $\mathrm { e } ^ { ( s + t ) v } ( m ) = \mathrm { e } ^ { t v } \circ \mathrm { e } ^ { s v } ( m )$ holds when $m \in M _ { s }$ and $\mathrm { e } ^ { s v } ( m ) \in M _ { t }$ , in which case $m \in M _ { s + t }$ $\mathrm { A l s o } , \mathrm { e } ^ { t v }$ is a diffeomorphism from the open subset $M _ { t }$ of M onto the open subset $M _ { - t }$ of $M ,$ with inverse equal to $\mathrm { e } ^ { - t \boldsymbol { v } }$ . If $D \neq \mathbf { R } \times M$ we don’t have a group action, but we have the same identities ”as far as the objects appearing in the formulas are defined”. Lie [21] called $t \mapsto \mathrm { e } ^ { t v }$ the oneparameter group of transformations generated by the vector field v, where he did not worry about domains of definition.

## 3.2 Lie Derivatives

Let $\Omega ^ { p } ( M )$ denote the space of smooth p-forms on the smooth manifold M, where $\Omega ^ { 0 } ( M ) = { \mathcal { F } } ( M )$ denotes the space of smooth real valued functions on M and $\Omega ^ { p } ( M ) = \{ 0 \}$ if $p >$ dim M. If M and N are smooth manifolds of any dimensions, and $\varphi : M \to N$ is a smooth map, then for any $\omega \in \Omega ^ { p } ( N )$ the pullback $\varphi ^ { * } \omega$ of ω under the map $\varphi$ is defined by

$$
\begin{array} { r } { ( \varphi ^ { \ast } \omega ) _ { m } \left( v _ { 1 } , \mathbf { \varphi } , v _ { n } \right) = \omega _ { \varphi ( m ) } \left( \mathrm { T } _ { m } \varphi v _ { 1 } , \mathbf { \varphi } , \mathrm { T } _ { m } \varphi v _ { n } \right) . } \end{array}\tag{3.1}
$$

Note that $\varphi ^ { * }$ defines a continuous linear operator from $\Omega ^ { p } ( N )$ to $\Omega ^ { p } ( M )$ , where the word ”pullback” reminds of the fact that this goes in the opposite direction of the map $\varphi : M \to N$ . For $p = 0$ we have $\varphi ^ { * } \omega = \omega \circ \varphi$ , which means that the pullback under $\varphi$ is just the substitution $n = \varphi ( m )$ in $\omega ( n )$ , and $\varphi ^ { * }$ is just a convenient notation for the linear mapping $\omega \mapsto \omega \circ \varphi$

The transposition symbol ∗ in the notation is a reminder to the transposition of $\varphi$ in the formula $\varphi ^ { * } \omega = \omega \circ \varphi$ . It also helps reminding that in the natural composition formula $( \psi \circ \varphi ) ^ { * } = \varphi ^ { * } \circ \psi ^ { * }$ the order is reversed: pullback is an antihomomorphism with respect to composition.

It is known that the exterior derivative d : $\Omega ^ { p } ( M ) \to \Omega ^ { p + 1 } ( M )$ of differential forms behaves naturally under smooth mappings, in the sense that

$$
\varphi ^ { * } ( \mathrm { d } \omega ) = \mathrm { d } \left( \varphi ^ { * } \omega \right) , \quad \omega \in \Omega ^ { p } ( N ) , \quad \varphi : M \to N .\tag{3.2}
$$

Let $\mathcal { X } ( M )$ denote the vector space of smooth vector fields on M. If $v \in \mathcal { X } ( M )$ , then the Lie derivative $\mathcal { L } _ { v } \omega$ of $\omega \in \Omega ^ { p } ( M )$ with respect to the vector field v is defined as

$$
\mathcal { L } _ { v } \omega : = \frac { \mathrm { d } } { \mathrm { d } t } \left( \mathrm { e } ^ { t v } \right) ^ { * } \omega \Big \vert _ { t = 0 } .\tag{3.3}
$$

If in

$$
\left( \mathrm { e } ^ { t v } \right) ^ { * } \circ ( \mathrm { e } ^ { s v } ) ^ { * } \omega = \left( \mathrm { e } ^ { s v } \circ \mathrm { e } ^ { t v } \right) ^ { * } \omega = \left( \mathrm { e } ^ { ( t + s ) v } \right) ^ { * } \omega
$$

we take the derivative with respect to s at $s = 0$ in the left and right hand side, we obtain that

$$
\left( \mathrm { e } ^ { t v } \right) ^ { * } { \mathcal { L } } _ { v } \omega = { \frac { \mathrm { d } } { { \mathrm { d } } t } } \left( \mathrm { e } ^ { t v } \right) ^ { * } \omega .
$$

This implies that $\mathcal { L } _ { v } \omega = 0$ if and only ${ \mathrm { i f ~ } } t \mapsto \left( \mathrm { e } ^ { t v } \right) ^ { * }$ ω is constant, hence equal to its value ω at $t = 0$ . We say that $\omega$ is called invariant under the flow of v if, for every $t \in \mathbf { R } , \left( \mathrm { e } ^ { t v } \right) ^ { * } \omega = \omega$ in $M _ { t }$ We have proved that $\omega$ is invariant under the flow of v if and only if the Lie derivative of $\omega$ with respect to v is equal to zero.

If $v \in \mathcal { X } ( M )$ and $\omega \in \Omega ^ { p } ( M )$ , then the inner product $\mathrm { i } _ { v } \omega \in \Omega ^ { p - 1 } ( M )$ of ω with v is defined by

$$
( \mathrm { i } _ { v } \omega ) _ { m } ( v _ { 2 } , . . . , v _ { n } ) = \omega _ { m } ( v ( m ) , v _ { 2 } , . . . , v _ { n } ) .\tag{3.4}
$$

In other words, $\mathrm { i } _ { v }$ is the continuous linear operator from $\Omega ^ { p } ( M )$ to $\Omega ^ { p - 1 } ( M )$ of inserting the vector field v at the first slot.

If $p = 0$ , then obviously $\mathcal { L } _ { v } \omega = \mathrm { i } _ { v } ( \mathrm { d } \omega )$ , which is the derivative of the function ω in the direction of the vector $\mathit { f i e l d } \mathit { v }$ . For general p we have the homotopy formula

$$
\begin{array} { r } { \mathcal { L } _ { v } \omega = \mathrm { i } _ { v } ( \mathrm { d } \omega ) + \mathrm { d } \left( \mathrm { i } _ { v } \omega \right) , } \end{array}\tag{3.5}
$$

or $\mathcal { L } _ { v } = \mathrm { i } _ { v } \circ \mathrm { d } + \mathrm { d } \circ \mathrm { i } _ { v }$ . Note that in the first summand d and $\mathrm { i } _ { v }$ is a linear operator from $\Omega ^ { p } ( M )$ to $\Omega ^ { p + 1 } ( M )$ and from $\Omega ^ { p + 1 } ( M )$ to $\Omega ^ { p } ( M )$ , respectively, whereas in the second summand $\mathrm { i } _ { v }$ and d is a linear operator from $\Omega ^ { p } ( M )$ to $\Omega ^ { p - 1 } ( M )$ and from $\Omega ^ { p - 1 } ( M )$ to $\Omega ^ { p } ( M )$ , respectively. This makes the beautiful formula (3.5) easy to remember.

Let $v \in \mathcal { X } ( M )$ and let $\varphi : M \to M$ be a smooth mapping for which, at each point $m \in M$ 7 $\mathrm { T } _ { m } \varphi : \mathrm { T } _ { m } M \to \mathrm { T } _ { \varphi ( m ) }$ M is invertible. Then the pullback $\varphi ^ { * } v \in \mathcal { X } ( M )$ on M of v under $\varphi$ is defined by

$$
( \varphi ^ { * } v ) ( m ) : = \left( \mathrm { T } _ { m } \varphi \right) ^ { - 1 } v ( \varphi ( m ) ) , \quad m \in M .\tag{3.6}
$$

This definition has been arranged in such a way that

$$
\varphi ^ { * } ( \mathrm { i } _ { v } \omega ) = \mathrm { i } _ { \varphi ^ { * } v } \ \varphi ^ { * } \omega
$$

for any $v \in \mathcal { X } ( M )$ and $\omega \in \Omega ^ { p } ( M )$ . If w is another smooth vector field on $M , \varphi = \mathrm { e } ^ { t w }$ , and we differentiate the left and right hand side with respect to t at $t = 0$ , then we obtain that

$$
\mathcal { L } _ { w } ( \mathrm { i } _ { v } \omega ) = \mathrm { i } _ { [ w , v ] } \omega + \mathrm { i } _ { v } \left( \mathcal { L } _ { w } \omega \right) ,\tag{3.7}
$$

if we define the Lie brackets $[ w , v ] \in \mathcal { X } ( M )$ of the vector fields w and v on M by means of

$$
[ v , w ] = { \mathcal { L } } _ { v } w : =  { \frac { \partial } { \partial t } } ( \mathrm { e } ^ { t v } ) ^ { * } w \ | _ { t = 0 } : =  { \frac { \partial } { \partial t } } ( { \frac { \partial } { \partial s } } \mathrm { e } ^ { - t v } \circ \mathrm { e } ^ { s w } \circ \mathrm { e } ^ { t v } \ | _ { s = 0 } ) \ | _ { t = 0 } .\tag{3.8}
$$

Note that this yields the opposite sign compared with the usual definition for the Lie agebra of a Lie group, but it is probably better to conform with the generally accepted definition of Lie brackets of vector fields.

In local coordinates, the Lie brackets of the vector fields v and w can be computed as

$$
[ v , w ] ( m ) = ( \mathrm { D } w ) ( m ) v ( m ) - ( \mathrm { D } v ) ( m ) w ( m ) .\tag{3.9}
$$

If in the local coordinates the vector fields are linear, then this leads to $[ v , w ] = w \circ v - v \circ w$ , where the right hand side is equal to the opposite of the commutator of w and v.

If in (3.7) we substitute $\omega = \operatorname { d } f$ in which f is a smooth function, then we obtain that

$$
\mathcal { L } _ { [ w , v ] } f = [ \mathcal { L } _ { w } , \mathcal { L } _ { v } ] f ,\tag{3.10}
$$

in which $[ A , B ] : = A \circ B - B \circ A$ denotes the commutator of the linear operators A and B. It is customary in differential geometry to identify the smooth vector field v with the derivation $D = \mathcal { L } _ { v }$ of functions in the direction of v, and with this identification the Lie brackets of vector fields is defined as their commutator. This definition has been adopted in Lie [21, Vol. I], where the identity

$$
\left( \mathrm { e } ^ { t v } \right) ^ { \ast } f = \mathrm { e } ^ { t \mathcal { L } _ { v } } \ f : = \sum _ { k = 0 } ^ { \infty } \frac { t ^ { k } } { k ! } \ ( \mathcal { L } _ { v } ) ^ { k } \ f ,
$$

which is valid if the vector field v and the function f are analytic, is presented as another motivation for the exponential notation for the one-parameter group of transformations generated by the vector field v.

Actually, since derivations are linear operators in the space of smooth functions, and linear operators are usually denoted by capital letters, the identification of vector fields with derivations has led to the custom in differential geometry and in Lie groups to denote vector fields and elements of the Lie algebra by capital letters, usually X. This in turn has led to the notation $\mathcal { X } ( M )$ for the Lie algebra of all smooth vector fields on M. Lie’s ”continuous groups” were subgroups G of the groups of diffeomorphism of a smooth manifold M, which depend smoothly on parameters. The corresponding infinitesimal transformations form a Lie subalgebra g of $\mathcal { X } ( M )$

If in the local coordinates the vector fields are linear, then (3.9) leads to $[ v , w ] = w \circ v - v \circ w .$ where the right hand side is equal to the opposite of the commutator of w and v. This is another consequence of the opposite sign choice for the Lie brackets of vector fields as compared to the one in the Lie algebra of a Lie group.

## 3.3 Hamiltonian Vector Fields

Let $( M , \sigma )$ be a symplectic manifold. Then, according to Subsection 3.2, the flow $\mathrm { e } ^ { t \boldsymbol { v } }$ of the smooth vector field $v \in \mathcal { X } ( M )$ leaves the symplectic form σ invariant, if and only if

$$
0 = \mathcal { L } _ { v } \sigma = \mathrm { i } _ { v } ( \mathrm { d } \sigma ) + \mathrm { d } \left( \mathrm { i } _ { v } \sigma \right) = \mathrm { d } \left( \mathrm { i } _ { v } \sigma \right) ,
$$

i.e. if and only if the one-form $\mathrm { i } _ { v } \sigma$ is closed. Here we have used the homotopy formula (3.5) for the Lie derivative in the second identity and the fact that $\sigma$ is closed in the third identity.

In turn the condition that $\mathrm { i } _ { v } \sigma$ is closed is locally equivalent to the condition that $\mathrm { i } _ { v } \sigma$ is equal to the total derivative of a smooth function. In formula:

$$
\mathrm { i } _ { v } \sigma = - \mathrm { d } f\tag{3.11}
$$

for a locally defined smooth function $f ,$ where the minus sign is a matter of convention. $\operatorname { I f } \mathrm { H } ^ { 1 } ( M ) =$ 0, then there is a globally defined function $f$ on M such that (3.11) holds, and if M is connected, then $f$ is uniquely determined up to an additive constant.

Conversely, if $f$ is a smooth function on M, then the fact that for every $m \in M$ the linear mapping

$$
\sigma _ { m } : v \mapsto \mathrm { i } _ { v } \sigma _ { m } : \mathrm { T } _ { m } M \to ( \mathrm { T } _ { m } M ) ^ { * }
$$

is bijective shows that there is a unique vector field v on M which satisfies (3.11). Moreover, v is smooth because $\mathrm { d } f$ and m $\mapsto \sigma _ { m } ^ { - 1 }$ are smooth. The smooth vector field v on M such that (3.11) holds is called the Hamiltonian vector field $\mathrm { H } _ { f }$ on M defined by the function $f .$ In the literature f is called the Hamiltonian function of the vector field v and denoted by H. However, we would like to stress that $f$ can be any smooth function on M. It is quite remarkable that there are so many smooth vector fields whose flows leave σ invariant: one for every closed one-form on M, or smooth function on M modulo an additive constant.

A system of coordinates $x _ { i } , \xi _ { i }$ in M is called a canonical system of coordinates if (2.6) holds. Let, in such a coordinate system, ${ \dot { x } } _ { i } , { \dot { \xi } } _ { i }$ denote the coordinates of the vector field

$$
v = \mathrm { H } _ { f } = \left( { \dot { x } } _ { 1 } , \dots , { \dot { x } } _ { n } ; { \dot { \xi } } _ { 1 } , \dots , { \dot { \xi } } _ { n } \right) .
$$

With these notations, the equation (3.11 reads

$$
\mathrm { i } _ { v } \sigma = \sum _ { i = 1 } ^ { n } \left( \dot { \xi } _ { i } \mathrm { d } x _ { i } - \dot { x } _ { i } \mathrm { d } \xi _ { i } \right) = - \sum _ { i = 1 } ^ { n } \left( \frac { \partial f } { \partial x _ { i } } \mathrm { d } x _ { i } + \frac { \partial f } { \partial \xi _ { i } } \mathrm { d } \xi _ { i } \right) ,
$$

from which obtain that

$$
\dot { x } _ { i } = \frac { \partial f ( x , \xi ) } { \partial \xi _ { i } } , \quad \dot { \xi } _ { i } = - \frac { \partial f ( x , \xi ) } { \partial x _ { i } } , \quad 1 \leq i \leq n .\tag{3.12}
$$

In other words, if dm $\boldsymbol { \mathbf { \ell } } ( t ) / \mathrm { d } t \boldsymbol { \mathbf { \ell } } = \boldsymbol { \mathbf { \ell } } v ( m ( t ) )$ is the differential equation for the flow defined by the vector field $v = \mathrm { H } _ { f }$ , then in canonical local coordinates we arrive at the system of ordinary differential equations (3.12), in which we replace ${ \dot { x } } _ { i }$ and $\dot { \xi } _ { i }$ by $\mathrm { d } x _ { i } ( t ) /$ dt and $\mathrm { d } \xi _ { i } ( t ) / \mathrm { d } t$ , respectively, and in the right hand side take the partial derivatives of $f$ at $x _ { i } = x _ { i } ( t ) , \xi _ { i } = \xi _ { i } ( t )$ . We recognize the resulting system of ordinary differential equations as the Hamiltonian system defined by the function $f$ as it appears in the textbooks in Classical Mechanics, where usually the position and momentum coordinates $x _ { i }$ and $\xi _ { i }$ are denoted by $q _ { i }$ and $p _ { i }$ , respectively.

Note that if we would have taken the other sign convention in (3.11), then the signs in (3.12) would be opposite to the standard ones in classical mechanics. Also note that the convention, to use Greek letters for the momentum coordinates corresponding to the Latin letters for the position coordinate, allows us to write for example the momentum coordinates coordinates corresponding to the position coordinates $x , y , z { \mathrm { ~ a s ~ } } \xi , \eta , \zeta$ , respectively.

Example 3.1 If X is an n-dimensional smooth manifold and $v \in { \mathcal { X } } ( X )$ , then the momentum function of the vector field v in the base manifold X is the function $\mu _ { v }$ on the cotangent bundle $M : = \Gamma ^ { * } X$ , defined by

$$
\mu _ { v } ( x , \xi ) = \xi ( v ( x ) ) , \quad x \in X , \quad \xi \in ( \operatorname { T } _ { x } X ) ^ { * } .\tag{3.13}
$$

Then the fiber derivative of $\mu _ { v }$ is equal to

$$
\dot { x } = \frac { \partial \mu _ { v } ( x , \xi ) } { \partial \xi } = v ( x ) \in \mathrm { T } _ { x } X = \left( ( \mathrm { T } _ { x } X ) ^ { * } \right) ^ { * } .
$$

It follows that the projection $\pi : ( x , \xi ) \to x : \mathrm { T } ^ { * } X \to X$ intertwines the $\mathrm { H } _ { \mu _ { 2 } }$ -flow in $\mathrm { T } ^ { * } X$ with the v-flow in X, in the sense that

$$
\pi \circ \mathrm { e } ^ { t \mathrm { H } _ { \mu _ { v } } } = \mathrm { e } ^ { t v } \circ \pi .
$$

More precisely, for every $x \in X$ and $\xi \in ( \Gamma _ { x } X ) ^ { * }$ we have that

$$
\mathrm { e } ^ { t \mathrm { H } _ { \mu _ { v } } } ( x , \xi ) = \left( \mathrm { e } ^ { t v } ( x ) , \left( \left( \mathrm { T } _ { x } \mathrm { e } ^ { t v } \right) ^ { * } \right) ^ { - 1 } ( \xi ) \right) .
$$

In other words, the flow in T∗ X of the Hamiltonian system defined by the function $\mu _ { v }$ is equal to the flow in $\mathrm { T } ^ { * } X$ which is induced by the flow in X of the vector field v.

## 3.4 The Legendre Transform

Let L be a smooth real-valued function on an open subset U of the tangent bundle TX of an n-dimensional smooth manifold X, where we will write $L ( x , v ) \in \mathbf { R }$ whenever x $\in X$ and $v \in \mathrm { T } _ { x } X$ For any smooth curve $\gamma : [ a , b ] \to X$ such that $( { \gamma } ( t ) , { \gamma } ^ { \prime } ( t ) ) \in U$ for all $t \in [ a , b ]$ , define the integral

$$
I ( \gamma ) = \int _ { a } ^ { b } L ( \gamma ( t ) , \gamma ^ { \prime } ( t ) ) \ \mathrm { d } t .\tag{3.14}
$$

The variational formula of Euler and Lagrange states that if $\gamma = \gamma _ { \epsilon }$ depends smoothly on a parameter , then

$$
\begin{array} { r c l } { \displaystyle \frac { \mathrm { d } I ( \gamma _ { \epsilon } ) } { \mathrm { d } \epsilon } } & { = } & { \displaystyle - \int _ { a } ^ { b } [ L ] ( t ) \delta ( t ) \mathrm { d } t } \\ & & { \displaystyle + \mu ( \gamma ( b ) , \gamma ^ { \prime } ( b ) ) \delta ( b ) - \mu ( \gamma ( a ) , \gamma ^ { \prime } ( a ) ) \delta ( a ) . } \end{array}\tag{3.15}
$$

Here

$$
\delta ( t ) : = \frac { \partial \gamma _ { \epsilon } ( t ) } { \partial \epsilon } \in \mathrm { T } _ { \gamma ( t ) } X\tag{3.16}
$$

denotes the ”variation with respect to $\epsilon ^ { \mathfrak { N } }$ of the curve $\gamma _ { \epsilon } ( t ) , \ [ L ] ( t )$ is the linear form on $\mathrm { T } _ { \gamma ( t ) } X$ which in local coordinates is given by

$$
[ L ] _ { i } : = \frac { \mathrm { d } \mu _ { i } ( \gamma ( t ) , \gamma ^ { \prime } ( t ) ) } { \mathrm { d } t } - \left. \frac { \partial L ( x , \gamma ^ { \prime } ( t ) } { \partial x _ { i } } \right| _ { x = \gamma ( t ) }\tag{3.17}
$$

and the linear form $\mu ( x , v ) = \mu _ { L } ( x , v )$ on $\mathrm { T } _ { x } X$ is defined by

$$
\mu ( x , v ) : = \frac { \partial L ( x , v ) } { \partial v } \in ( \mathrm { T } _ { x } X ) ^ { * } .\tag{3.18}
$$

The formula (3.15) is obtained by differentiating with respect to  under the integral sign, and then performing an integration by parts on the term with the factor

$$
\frac { \partial ^ { 2 } \gamma _ { \epsilon } ( t ) } { \partial \epsilon \partial t } = \frac { \partial ^ { 2 } \gamma _ { \epsilon } ( t ) } { \partial t \partial \epsilon } .
$$

The linear form $ { \mu } ( x , v )$ on the tangent space in (3.18), which is defined in a coordinate-independent way, is called the momentum vector assigned to the velocity vector v by means of the function $L .$

It is one of the basic observations of Lagrange [19, Tome I, Partie 2, Section IV] that, although the two summands in (3.17) transform in a quite complicated manner under a change of coordinates, the quantity $[ L ] ( t )$ transforms as a covector, an element of $\left( \mathrm { T } _ { \gamma ( t ) } X \right) ^ { * }$ His argument is that for any $w \in \mathrm { T } _ { \gamma ( t _ { 0 } ) }$ X the real number $- [ L ] ( t _ { 0 } )$ w is equal to the limit for $j \to \infty$ of the left hand side of (3.17), which is independent of any choice of coordinates, if we take $\gamma _ { \epsilon } ^ { j } ( t )$ in such a way that $\delta ^ { j } ( t ) = \partial \gamma _ { \epsilon } ^ { j } ( t ) / \partial \epsilon$ is only nonzero for t in a shrinking neighborhood of $t _ { 0 }$ and is asymptotically equal to a large multiple of $v ,$ in such a way that the integral over t remains equal to w. (Those who are familiar with the theory of distributions will recognize $\delta ^ { j } ( t )$ as a sequence of smooth functions which approximate the Dirac delta function at the point $t _ { 0 }$ times $w .$ , where the approximation is in the distributional sense.)

The velocity-to-momentum mapping

$$
\Phi = \Phi _ { L } : ( x , v ) \mapsto ( x , \mu ( x , v ) ) : U \to \mathrm { T } ^ { * } X
$$

is a local diffeomorphism if and only if its tangent mapping is invertible, which is equivalent to Legendre’s condition that

the symmetric bilinear form ${ \frac { \partial \mu ( x , v ) } { \partial v } } = { \frac { \partial ^ { 2 } L ( x , v ) } { \partial v ^ { 2 } } }$ on $\mathrm { T } _ { x } X$ is nondegenerate.

Here, in linear coordinates in $\mathrm { T } _ { x } X$ , the bilinear form $\partial ^ { 2 } L ( x , v ) / \partial v ^ { 2 }$ has the symmetric matrix $\partial ^ { 2 } L ( x , v ) / \partial v _ { i } \partial v _ { j } , 1 \leq i , j \leq n$ , the Hessian of the function $v \mapsto L ( x , v )$ . By restricting U to open subsets on which Φ is injective, we obtain a diffeomorphism from U onto an open subset V of the cotangent bundle $\mathrm { T } ^ { * } X$ of X .

A curve $\gamma ( t )$ is called a stationary curve for the integral I in (3.14), if it satisfies the Euler-Lagrange equations

$$
[ L ] ( t ) \equiv 0 ,\tag{3.19}
$$

i.e. if the integral in (3.15) vanishes for any variation $\delta ( t )$ of $\gamma ( t )$ . If the Legendre condition holds, then the Euler-Lagrange equations can be written in local coordinates as a second order system of ordinary differential equations

$$
\frac { \mathrm { d } ^ { 2 } \gamma _ { i } ( t ) } { \mathrm { d } t ^ { 2 } } = a _ { i } ( \gamma ( t ) , \gamma ^ { \prime } ( t ) ) , \quad 1 \leq i \leq n ,
$$

in which the components of the acceleration $a _ { i } ( x , v )$ are smooth functions of x and v. Actually, it is more convenient to view this second order system as a first order system

$$
x ^ { \prime } ( t ) = v ( t ) , \quad v ^ { \prime } ( t ) = a ( x ( t ) , v ( t ) ) ,
$$

defined by the vector field $( v , a ( x , v ) )$ in the tangent bundle.

Now define the functions H on $U$ and h on $V$ subsequently by means of the equations

$$
H ( x , v ) : = \langle v , \mu ( x , v ) \rangle - L ( x , v ) , \quad h = H \circ \Phi ^ { - 1 } .\tag{3.20}
$$

Here $\langle v , \xi \rangle$ is the customary, more symmetric notation for the value $\xi ( v )$ which the linear form $\xi$ takes on the vector v. The function $h$ on the open subset V of the cotangent bundle $\mathrm { T } ^ { * } X$ of $X$ is called the Legendre transform of the function $L .$

Write $v = v ( x , \xi )$ for the solution v of the equation $\mu ( x , v = \xi$ . Then

$$
h ( x , \xi ) = \langle v ( x , \xi ) , \xi \rangle - L ( x , v ( x , \xi ) ,
$$

hence

$$
\frac { \partial h ( x , \xi ) } { \partial \xi _ { i } } = \langle \frac { \partial v ( x , \xi ) } { \partial \xi _ { i } } , \xi \rangle + v _ { i } ( x , \xi ) - \langle \frac { \partial v ( x , \xi ) } { \partial \xi _ { i } } , \mu ( x , v ( x , \xi ) ) \rangle = v _ { i } ( x , \xi ) ,
$$

where in the first and second identity we have used the definition (3.18) of $\mu$ and the equation $\begin{array} { r } { \mu ( \boldsymbol { x } , \boldsymbol { v } ( \boldsymbol { x } , \boldsymbol { \xi } ) ) = \boldsymbol { \xi } . } \end{array}$ , respectively. Similarly we have

$$
\frac { \partial h ( x , \xi ) } { \partial x _ { i } } = \langle \frac { \partial v ( x , \xi ) } { \partial x _ { i } } , \xi \rangle - \left. \frac { \partial L ( x , v ) } { \partial x _ { i } } \right| _ { v = v ( x , \xi ) } - \langle \frac { \partial ( v , \xi ) } { \partial x _ { i } } , \mu ( x , v ( x , \xi ) ) \rangle = . \left. - \frac { \partial L ( x , v ) } { \partial x _ { i } } \right| _ { v = v ( x , \xi ) } ,
$$

where again in the first and second identity we have used the definition (3.18) of $\mu$ and the equation $\mu ( x , v ) = \xi$ , respectively.

The Euler-Lagrange equations are

$$
\frac { \mathrm { d } x ( t ) } { \mathrm { d } t } = v ( t ) , \quad \frac { \mathrm { d } \xi _ { i } ( t ) } { \mathrm { d } t } = \left. \frac { \partial L ( x , v ) } { \partial x _ { i } } \right| _ { v = v ( x , \xi ) } ,
$$

where in the second equation we have substituted $\xi = \mu ( x , v ) = \partial L ( x , v ) / \partial v$ . The point of the computation of the partial derivatives of the function $h ( x , \xi )$ is that the velocity-to-momentum mapping Φ transforms the Euler-Lagrange equations into the Hamiltonian system

$$
\frac { \mathrm { d } x _ { i } } { \mathrm { d } t } = \frac { \partial h ( x , \xi ) } { \partial \xi _ { i } } , \quad \frac { \mathrm { d } \xi _ { i } } { \mathrm { d } t } = - \frac { \partial h ( x , \xi ) } { \partial x _ { i } }
$$

on $V$ which is defined by the function $h .$

Conversely, if $h$ is a smooth real-valued function on an open subset V of $\mathrm { T } ^ { * } X$ for which the momentum-to-velocity mapping

$$
\Psi = \Psi _ { h } : ( x , \xi ) \mapsto \left( x , v ( x , \xi ) \right) , \quad v ( x , \xi ) : = \frac { \partial h ( x , \xi ) } { \partial \xi }
$$

is a diffeomorphism from V onto an open subset $U$ of $ { \mathrm { ~ T ~ } } X$ , then we can define subsequently

$$
l ( x , \xi ) : = \langle v ( x , \xi ) , \xi \rangle - h ( x , \xi ) , \quad L = l \circ \Psi ^ { - 1 } .
$$

It is then not hard to verify that $\Psi _ { h } = \Phi _ { L } ^ { - 1 }$ and h is equal to the Legendre transform of $L$ , which shows that $\Psi _ { L }$ transforms the Hamiltonian system defined by the function h into the Euler-Lagrange equations for the function L.

We now turn to the relation with Classical Mechanics. Lagrange [19, Tome 1, partie 2, Section IV] actually made his observation, that $[ L ]$ transforms under changes of local coordinates as a covector, in the case that $L ( x , v )$ is equal to the kinetic energy

$$
T ( x , v ) = { \frac { 1 } { 2 } } m ( x ) ( v , v )
$$

of a classical mechanical system. Here $m ( x )$ , the inertial mass tensor is an inner product on $\mathrm { T } _ { x } X$ If we have local coordinates in which $m ( x ) = m$ does not depend on $x ,$ then $[ T ] = \mathrm { d } ( m v ) /$ dt and we recognize the equation

$$
[ T ] = F = { \mathrm { ~ t h e ~ f o r c e ~ a c t i n g ~ o n ~ t h e ~ s y s t e m } }\tag{3.21}
$$

as Newton’s equations of motion. However, Lagrange observed that under arbitrary nonlinear changes of coordinates, such as the passage from recangular coordinates to polar coordinates, the acceleration $a = \mathrm { d } v / \mathrm { d }$ t transforms in a complicated way, not at all as a tensor, and the transformed equations of motion do not look like Newton’s equations $F = m a$ at all. (Also the inertial mass tensor in this case no longer is independent of the position.)

Because Lagrange had understood that in general a quantity of the form [L] transforms covariantly, he proposed to formulate the equations of motion for a general classical mechanical system as (3.21), in which $T$ is the kinetic energy function viewed as a smooth function on the tangent bundle. Moreover, the force field $F$ is (has to be equal to) a smooth mapping which assigns to each $x \in X$ and $v \in \mathrm { T } _ { x } X$ an element of $( \mathrm { T } _ { x } X ) ^ { * }$ , a linear form on $\mathrm { T } _ { x } X$ .

The force field F is called conservative, if $F ( x , v ) = F ( x )$ does noet depend on v and $F ( x ) =$ $- \operatorname { d } V ( x )$ for a potential energy function V which is a smooth real-valued function on X. In this case one has $F = \left\lceil V \right\rceil$ and we recognize the equations of motion (3.21) as the Euler-Lagrange equations $[ L ] = 0 ,$ in which $L = T - V$

The momentum defined by $L = T - V$ is equal to $\mu ( x , v ) = m ( x ) v .$ in which the inertial mass tensor $m ( x )$ is regarded as a bijective linear mapping from $\mathrm { T } _ { x } X$ onto $( \mathrm { T } _ { x } X ) ^ { * }$ . Using that $v \mapsto T ( x , v )$ is homogeneous of degree two, one obtains that its Legendre transform is equal to $T \circ \Phi ^ { - 1 }$ , whereas the Legendre transform of V is equal $\mathrm { t o } \_ - V$ . This yields that the Legendre transform of $L = T - V$ is equal to the total energy function $h = T \circ \Phi ^ { - 1 } + V$ , viewed as a function of the positions and the momenta. In this way the equations of motion for a classical mechanical system with a conservative force field are equivalent to the Hamiltonian system defined by the total energy function, viewed as a function on the cotangent bundle $\mathrm { T } ^ { * } X$ rather than on the tangent bundle T X.

Remark 3.1 Lagrange [19, Tome 1, Partie 2, Section V] explictly introduced the velocity-to--momentum mapping $\Phi = \Phi _ { L }$ and the two-form $\Phi _ { L } ^ { * } \sigma$ on the tangent bundle TX, but without mentioning the canonical two-form σ of the cotangent bundle $\mathrm { T } ^ { * } X$ . He also proved that $\Phi _ { L } ^ { * } \sigma$ is invariant under the flow defined by the Euler-Lagrange equations. His proof is paraphrased in Exercise 3.4

The equivalence between the Euler-Lagrange equations of variational calculus and Hamiltonian systems has been found for $L = T - V$ by Hamilton [11], and then it was soon realized by many authors that his proof holds for an arbitrary function L on the tangent bundle which satisfies Legendre’s condition. Earlier, the perturbation equations of a classical mechanical system in which the potential energy is perturbed were written in a Hamiltonian form by Lagrange [19, Tome I, p. 310]. He might have missed the general equivalence between Euler-Lagrange equations and Hamiltonian systems, because he probably was not aware of the Legendre transform.

## 3.5 Poisson Brackets

If f, $g \in { \mathcal { F } } ( M )$ , then the Poisson brackets $\{ f , g \}$ of f and $g$ are defined as the derivative of the function $g$ in the direction of the Hamiltonian vector field $\mathrm { H } _ { f }$ defined by the function $f \colon$

$$
\{ f , g \} : = \mathcal { L } _ { \mathrm { H } _ { f } } ( g ) = \mathrm { i } _ { \mathrm { H } _ { f } } ( \mathrm { d } g ) = - \mathrm { i } _ { \mathrm { H } _ { f } } \left( \mathrm { i } _ { \mathrm { H } _ { g } } \sigma \right) = \sigma \left( \mathrm { H } _ { f } , \mathrm { H } _ { g } \right) .\tag{3.22}
$$

Here we used (3.11) and the antisymmetry of $\sigma$ in the third and fourth identity, respectively. The right hand side shows that the Poisson brackets are antisymmetric in the sense that

$$
\{ g , \ : f \} = - \{ f , \ : g \} , \quad f , \ : g \in \mathcal { F } ( M ) .\tag{3.23}
$$

In canonical local coordinates the Poisson brackets are given by

$$
\{ f , g \} ( x , \xi ) = \sum _ { i = 1 } ^ { n } \left( \frac { \partial f ( x , \xi ) } { \partial \xi _ { i } } \frac { \partial g ( x , \xi ) } { \partial x _ { i } } - \frac { \partial f ( x , \xi ) } { \partial x _ { i } } \frac { \partial g ( x , \xi ) } { \partial \xi _ { i } } \right) .\tag{3.24}
$$

It follows immediately that the following conditions a)–d) are equivalent:

a) g is a constant of motion for the Hamiltonian system defined by the function $f ,$ in the sense that g is invariant under the $\mathrm { H } _ { f } .$ -flow.

b) $\left\{ f , g \right\} = 0 .$

c) $\{ g , f \} = 0 .$

d) f is a constant of motion for the Hamiltonian system defined by the function $g .$

In the applications, one often has that the $\operatorname { H } _ { g } .$ -flow is a one-parameter group of symmetry for the function $f ,$ which means that d) holds. The conclusion, that in this case g is a constant of motion for the Hamiltonian system defined by the function $f ,$ is called Noether’s principle for Hamiltonian systems. In many examples we have $M = \mathrm { T } ^ { * } X$ and $g = \mu _ { v }$ , the momentum function of a smooth vector field v in the base manifold X, cf. Example 3.1.

It also follows from (3.23) that $\{ f , f \} = 0$ , meaning that the function f is a constant of motion for the Hamiltonian system defined by f. If f is equal to the total energy of a classical mechanical system as in Subsection 3.4, then this is the law of conservation of the total energy.

The derivative of $\{ f , g \}$ is equal to

$$
\mathrm { d } \{ f , g \} = \mathrm { d } { \mathcal { L } } _ { \mathrm { H } _ { f } } g = { \mathcal { L } } _ { \mathrm { H } _ { f } } \mathrm { d } g = - { \mathcal { L } } _ { \mathrm { H } _ { f } } \left( \mathrm { i } _ { \mathrm { H } _ { g } } \sigma \right) = - \mathrm { i } _ { [ \mathrm { H } _ { f } , \mathrm { H } _ { g } ] } \sigma .
$$

Here we used in the first, second, third and fourth identity the definition (3.22) of the Poisson brackets, the fact that exterior differenitation commutes with pullbacks and therefore with Lie

derivatives, the defintion (3.11) of Hamiltonian vector fields, and formula (3.7) together with the fact that $\mathcal { L } _ { \mathrm { H } _ { f } } \sigma = 0$

This formula for the derivative of $\{ f , g \}$ just means that

$$
[ \mathrm { H } _ { f } , \mathrm { H } _ { g } ] = \mathrm { H } _ { \{ f , g \} } .\tag{3.25}
$$

In words, the Lie brackets of the Hamiltonian vector fields of the functions f and $g$ is again a Hamiltonian vector field, namely of the Poisson brackets of $f$ and $g .$

If we now let act the left and right hand side of (3.25) on a third smooth function h on M, then we obtain, using (3.10), that

$$
\{ f , \{ g , h \} \} - \{ g , \{ f , h \} \} = \{ \{ f , g \} , h \} .
$$

Using the antisymmetry (3.23) at several places, this identity can be rewritten as the Jacobi identity for Poisson brackets:

$$
\{ \{ f , g \} , h \} + \{ \{ g , h \} , f \} + \{ \{ h , f \} , g \} = 0 .\tag{3.26}
$$

(Note the cyclic permuation of $f , g$ and h in the left hand side of (3.26). Together, (3.26) and (3.25) mean that

Theorem 3.2 The space of smooth functions ${ \mathcal { F } } ( M )$ on M is a Lie algebra with respect to the Poisson brackets, and the mapping which assigns to a smooth function its Hamiltonian vector field is a homomorphism of Lie algebras from ${ \mathcal { F } } ( M )$ to the Lie algebra $\mathcal { X } ( M )$ of smooth vector fields on M. The kernel of this homomorphism is equal to the space of function which are constant on the connected components of M.

Remark 3.2 The Jacobi identity for the Poisson brackets (3.26) (in canonical coordinates) goes back to the article of Jacobi [18], which appeared posthumously in 1862. Jacobi mentioned that (3.26) implies the earlier theorem of Poisson, which states that if g and h are constants of motion for the Hamiltonian system defined by the function $f ,$ then $\{ g , h \}$ also is a constant of motion for the Hamiltonian system defined by $f .$ It could very well be that Jacobi was led to (3.26) by means of an analysis of Poisson’s proof. This observation of Jacobi may also have led to adoption of the name ”Poisson brackets”, which brackets appeared earlier in the work of Lagrange [19, Tome I, p. 315].

Inspired by the Jacobi identity for Poisson brackets, Lie [21, Vol. 1, Kap. 5, §26 and Vol. 2, Kap. 7, §44, 45] introduced the Jacobi identity for vector fields, and coined the name ”Jacobi identity”.

## 3.6 Darboux’s Lemma

Let $( M , \sigma )$ be a symplectic manifold. The Darboux lemma states that locally σ form can be brought into the canonical form (2.6). This means that for every $m _ { 0 } \in M$ there exists an open neighborhood U of $m _ { 0 }$ in M and a diffeomorphism Φ from U onto an open subset V of $\mathbf { R } ^ { n } \times \mathbf { R } ^ { n }$ such that

$$
\Phi ^ { * } \left( \sum _ { i = 1 } ^ { n } \mathrm { d } \xi _ { i } \wedge \mathrm { d } x _ { i } \right) = \sigma \quad \mathrm { o n ~ } U .
$$

A proof can be given as follows. Let $\phi$ be any smooth function defined in a neighborhood of m0 such that $\phi ( m _ { 0 } ) = 0$ and $\mathrm { d } \phi _ { m _ { 0 } } \neq 0$ . Choose any codimension one smooth submanifold S of M through $m _ { 0 }$ such that $\mathrm { H } _ { \phi } ( m _ { 0 } ) \not \in \mathrm { T } _ { m _ { 0 } } S$ . Then there is a locally unique smooth function $f$ on a neighborhood of $m _ { 0 }$ such that $\{ \phi , f \} = \mathcal { L } _ { \mathrm { H } _ { \phi } } f = 1$ and $f = 0$ on S. It follows from (3.22) that the symplectic product of $\mathrm { H } _ { \phi }$ and $\mathrm { H } _ { f }$ is equal to one, which implies that at every points these vectors are linearly independent, which in turn implies that at every point dφ and $\mathrm { d } f$ are linearly independent. This implies in particular that

$$
N : = \{ m \in U \mid f ( m ) = \phi ( m ) = 0 \}
$$

is a smooth codimension 2 submanifold of the open neighborhood $U$ of $m _ { 0 }$ on which $\phi$ and $f$ are defined. Moreover, the restriction $\sigma _ { N }$ of $\sigma$ to N is a symplectic form, because the symplectic orthogonal complement of $\mathrm { T } _ { n } N$ is spanned by $\mathrm { H } _ { \phi } ( n )$ and $\mathrm { H } _ { f } ( n )$ , which space is complementary to the $\mathrm { T } _ { n } N = \ker ( \mathrm { d } \phi _ { n } )$ ∩ ker $\left( \operatorname { d } f _ { n } \right)$ , as is readily verified.

It follows from (3.25) and the fact that the Hamiltonian vector field of any constant function is equal to zero, that the vector fields $\mathrm { H } _ { \phi }$ and $\mathrm { H } _ { f }$ commute, which implies that their flows commute as well. Now define, for $n \in N$ and $t , \tau \in \mathbf { R }$ ,

$$
\Phi ( n , t , \tau ) : = \mathrm { e } ^ { t \mathrm { H } _ { \phi } } \circ \mathrm { e } ^ { - \tau \mathrm { ~ H } _ { f } } ( n ) = \mathrm { e } ^ { - \tau \mathrm { ~ H } _ { f } } \circ \mathrm { e } ^ { t \mathrm { ~ H } _ { \phi } } ( n ) .
$$

Then $\partial \Phi ( n , t , \tau ) / \partial t = \mathrm { H } _ { \phi } ( \Phi ( n , t , \tau ) )$ and $\partial \Phi ( n , t , \tau ) / \partial \tau = - \mathrm { H } _ { f } ( \Phi ( n , t , \tau ) )$ . It follows that the value s which $\big ( \Phi ^ { * } \sigma \big ) _ { ( n , t , \tau ) }$ takes on the pair of vectors $( \delta n , \delta t , \delta \tau )$ and $( \delta n ^ { \prime } , \delta t ^ { \prime } , \delta \tau ^ { \prime } )$ is equal to $\sigma _ { \Phi ( n , t , \tau ) } ( v , v ^ { \prime } )$ , in which

$$
v = \mathrm { T } _ { n } \left( \mathrm { e } ^ { t \mathrm { H } _ { \phi } } \circ \mathrm { e } ^ { - \tau \mathrm { ~ H } _ { \phi } } \right) \mathrm { ~ } \delta n + \delta t \mathrm { ~ H } _ { \phi } - \delta \tau \mathrm { ~ H } _ { f } ,
$$

and $v ^ { \prime }$ is given by the same formule with $\delta n , \delta t .$ , δτ replaced by $\delta n ^ { \prime } , \delta t ^ { \prime } , \delta \tau ^ { \prime }$ , respectively. Using again that $\sigma ( \mathrm { H } _ { \phi } , \mathrm { H } _ { f } ) = 1$ and that Hamiltonian flows preserve the symplectic form, we arrive at the conclusion that

$$
s = \sigma _ { n } ( \delta n , \delta n ^ { \prime } ) + \delta \tau \delta t ^ { \prime } - \delta \tau ^ { \prime } \delta t .
$$

This shows that $\Phi ^ { * } \sigma$ is equal to the direct sum of $\sigma _ { N }$ and the standard symplectic form in $\mathbf { R } ^ { 2 }$ . The proof of Darboux’s lemma now follows by induction on n.

Remark 3.3 Weinstein [27] gave a proof of the Darboux lemma which is based on a deformation argument which has been introduced in normal form theory by Moser [24]. The proof given above is closer to the one given by Darboux. Both proofs have their merits.

If we combine the Darboux lemma with the reduction in Subsection 2.3, then one obtains that any closed two-form of constant rank has a local normal form.

## 3.7 Hamiltonian Group Actions

If a Lie group G acts on the smooth manifold M, we will denote for each $g \in G$ the diffeomorphism $m \mapsto g m$ of M by $g M$ . For each element X in the Lie algebra g of G we have the infinitesimal action

$$
X _ { M } : = \left. { \frac { \mathrm { d } } { \mathrm { d } t } } \left( \exp ( t X ) \right) _ { M } \right| _ { t = 0 }
$$

of X on M, which is a smooth vector field on M. Note that, as a consequence, $( \exp ( t X ) ) _ { M } = \mathrm { e } ^ { t X _ { M } }$ for every $t \in \mathbf { R }$ •

The definition (3.8) of the Lie brackets of vector fields implies that

$$
[ X , Y ] _ { M } = - [ X _ { M } , Y _ { M } ] , \quad X , Y \in { \mathfrak { g } } ,\tag{3.27}
$$

i.e. the mapping $X \mapsto X _ { M }$ is an anti-homomorphism from the Lie algebra g to the Lie algebra $\mathcal { X } ( M )$

Now suppose that σ is a symplectic form on M. The action of G on M will be called Hamiltonian with respect to $\sigma _ { \mathrm { { ; } } }$ if for every $X \in { \mathfrak { g } }$ we have given a smooth function $\langle X , \mu \rangle$ on M such that

$$
X _ { M } = \operatorname { H } _ { \langle X , \mu \rangle } .\tag{3.28}
$$

It will furthermore be required that $\langle X , \mu \rangle$ depends linearly on $X \in { \mathfrak { g } }$ and that

$$
\{ \langle X , \mu \rangle , \langle Y , \mu \rangle \} = - \langle [ X , Y ] , \mu \rangle , \quad X , Y \in { \mathfrak { g } } .\tag{3.29}
$$

In other words, we require that $X \mapsto \langle X , \mu \rangle$ is an anti-homomorphism of Lie algebras from g to the Poisson Lie algebra ${ \mathcal { F } } ( M )$ of all smooth functions on M.

The condition that the infinitesimal actions are Hamiltonian implies that the one-parameter subgroups preserve the symplectic form. Therefore, if G is connected, it follows that the G-action leaves the symplectic form invariant. In other words, the action is a homomorphism from G to the group of canonical transformations in $( M , \sigma )$ .

For every $m \in M , \mu ( m ) : X \mapsto \langle X , \mu \rangle ( m )$ is a linear form on g, this defines a smooth mapping $\mu : M \to { \mathfrak { g } } ^ { * }$ which is called the momentum mapping of the Hamiltonian action of G on M. Note that the notation has been arranged such that $\langle X , \mu ( m ) \rangle = \langle X , \mu \rangle ( m )$ for every $m \in M$

On g we have the adjoint action $( g , X ) \mapsto ( \operatorname { A d } g ) ( X )$ of $G ,$ and transposition leads to the action

$$
( g , \xi ) \mapsto \left( ( \operatorname { A d } g ) ^ { * } \right) ^ { - 1 } ( \xi )
$$

on the dual ${ \mathfrak { g } } ^ { * }$ of the Lie algebra, which is called the co-adjoint action of G on ${ \mathfrak { g } } ^ { * }$ . The infinitesimal co-adjoint action of $X \in { \mathfrak { g } }$ is given by the linear mapping

$$
X _ { \mathfrak { g } ^ { * } } = - ( \mathrm { a d } X ) ^ { * } : \mathfrak { g } ^ { * } \longrightarrow \mathfrak { g } ^ { * } ,
$$

or, more explicitly,

$$
\langle Y , X _ { \mathfrak { g } ^ { * } } \xi \rangle = - \langle [ X , Y ] , \xi \rangle , \quad \xi \in \mathfrak { g } ^ { * } , X , Y \in \mathfrak { g } .\tag{3.30}
$$

If in (3.30) we substitute $\xi = \mu ( m )$ and combine the resulting equation with (3.29), and use that the left hand side of (3.29) is equal to $\mathcal { L } _ { X _ { M } } \left. Y , \mu \right.$ , we arrive at the conclusion that

$$
\mathcal { L } _ { X _ { M } } \mu = X _ { \mathfrak { g } ^ { * } } \mu ,\tag{3.31}
$$

which means that the momentum mapping $\mu : M \to { \mathfrak { g } } ^ { * }$ intertwines the infinitesimal action of g on M with the infinitesimal co-adjoint action of g on ${ \mathfrak { g } } ^ { * }$ . If G is connected, then this implies in turn that the momentum mapping intertwines the action of G on M with the co-adjoint action of $G$ on ${ \mathfrak { g } } ^ { * }$ , in the sense that

$$
g _ { _ M } ^ { \ast } \mu = \left( \left( \operatorname { A d } g \right) ^ { \ast } \right) ^ { - 1 } \mu , \quad g \in G .\tag{3.32}
$$

Example 3.3 A very simple, but important example of a Hamiltonian group action on $( M , \sigma )$ can be obtained as follows. Assume that $f _ { i } , 1 \leq i \leq k$ , are smooth functions on M which Poisson commute, i.e. $\{ f _ { i } , f _ { j } \} = 0$ for all $1 \leq i , j \leq k$ . Let $f : M \to \mathbf { R } ^ { k }$ be the mapping which has the $f _ { i }$ as components. Then for every $c \in \mathbf { R } ^ { k }$ the level set $M _ { c } : = \{ m \in M \mid f ( m ) = c \}$ is invariant under the flows of the Hamiltonian vector fields $\mathrm { H } _ { f _ { i } }$ . Let us assume that the Hamiltonian vector fields $\mathrm { H } _ { f _ { i } }$ are complete, which condition in view of the above is certainly satisfied if the level set $M _ { c }$ is compact.

In view of (3.25), the fact that the functions $f _ { i }$ Poisson commute implies that the Hamiltonian vector fields $\mathrm { H } _ { f _ { i } }$ commute, which in turn implies that their flows commute. This implies that

$$
\left( \left( t _ { 1 } , \ldots , t _ { k } \right) , m \right) \mapsto \mathrm { e } ^ { t _ { k } \mathrm { H } _ { f _ { k } } } \circ \dots \circ \mathrm { e } ^ { t _ { 1 } \mathrm { H } _ { f _ { 1 } } } ( m )
$$

defines an action of tha additive group $( \mathbf { R } ^ { k } , + )$ on M. This action is Hamiltonian, with $f$ as its momentum mapping. Because the Lie algebra $\mathbf { R } ^ { k }$ is commutative, the adjoint action is trivial, hence the co-adjoint action is trivial as well and the fact that f intertwines the action on M with the co-adjoint action reproduces the observation that the functions $f _ { i }$ are invariant under the action on $M .$

The system is called integrable if $k = n$ and the mapping f has regular values. If c is a regular value of $f ,$ then $M _ { c }$ is an n-dimensional smooth submanifold of M on which the action is locally transitive, and therefore is transitive on each connected component C of $M _ { c }$ . If we choose $m \in C$ then the period lattice $P _ { C }$ in $\mathbf { R } ^ { n }$ is defined as the set of all $T \in \mathbf { R } ^ { n }$ such that $T _ { M } ( m ) = m$ • $P _ { C }$ does not depend on the choice of $m \in C$ (but in general it depends sensitively on the level $c )$ , and $P _ { C }$ is a discrete subgroup of $\mathbf { R } ^ { n }$ . The mapping $t \mapsto t _ { M } ( m )$ induces a diffeomorphism from ${ \bf R } ^ { n } / P _ { C }$ Y onto $C ,$ which intertwines the translational action of $\mathbf { R } ^ { n }$ on ${ \bf R } ^ { n } / P _ { C }$ with the action of $\mathbf { R } ^ { n }$ on $C$

If C is compact, which certainly is the case if $M _ { c }$ is compact, then ${ \bf R } ^ { n } / P _ { C }$ is compact, hence a torus, and the flow of each of the Hamiltonian vector fields $\mathrm { H } _ { f _ { i } }$ is quasi-periodic, meaning that by means of a diffeomorphism it can be mapped to a constant speed motion on a standard torus.

## 3.8 Poisson Structures

It follows from the third expression in (3.22) and from (3.11) that

$$
\{ f , g \} ( m ) = - \sigma _ { m } ^ { - 1 } ( \mathrm { d } f ( m ) , \mathrm { d } g ( m ) ) ,
$$

in which $\pi _ { m } : = \sigma _ { m } ^ { - 1 } : ( \mathrm { T } _ { m } M ) ^ { * } \to \mathrm { T } _ { m } M$ is regarded as an antisymmetric bilinear form on $( \mathrm { T } _ { m } M ) ^ { * }$ or as an element of $\Lambda ^ { 2 }  { \mathrm { T } } _ { m } M$ , which is also called a two-vector in $\mathrm { T } _ { m } M$ .

For any smooth manifold M, a Poisson structure on M is defined as a smooth two-vector field $\pi _ { m } \in \Lambda ^ { 2 }  { \mathrm { T } } _ { m } M , m \in M$ , in such a way that the corresponding Poisson brackets $\{ f , g \}$ , defined by

$$
\{ f , g \} ( m ) = \pi _ { m } ( \mathrm { d } f ( m ) , \mathrm { d } g ( m ) ) , \quad m \in M ,\tag{3.33}
$$

satisfy the Jacobi identity (3.26).

Viewing $\pi _ { m }$ as a linear mapping from $( \mathrm { T } _ { m } M ) ^ { * }$ to $\mathrm { T } _ { m } M$ , we can defined the Hamiltonian vector field $\mathrm { H } _ { f }$ of the function f by $\mathrm { H } _ { f } ( m ) = \pi _ { m } \mathrm { ~ d } f ( m )$ . With this convention, $\left\{ f , g \right\} = { \mathcal { L } } _ { \mathrm { H } _ { f } } g .$

If $\pi _ { m }$ is surjective, then it is bijective, and we have that $\pi _ { m } = - \sigma _ { m } ^ { - 1 }$ for a symplectic form on M. We therefore only get really new examples of Poisson structures if $\pi _ { m }$ is not surjective.

Write $H _ { m } = \pi _ { m } \left( ( \Gamma _ { m } M ) ^ { * } \right)$ . If the rank of $\pi _ { m }$ , the dimension of $H _ { m }$ , is constant as a function of $m \in M$ , then the $H _ { m } , m \in M$ , define a smooth vector subbundle H of TM, and it follows from the Jacobi identity for the Poisson brackets that H is integrable. Furthermore, for each integral manifold I of H, the restriction of $\{ f , g \}$ to I only depends on $f | _ { I }$ and $g | _ { I }$ , and we obtain a Poisson structure on $I ,$ which turns out to be defined by a sysmplectic structure on I. In this way the Poisson manifold $( M , \pi )$ can be characterized as a manifold which is foliated by symplectic leaves, where the Poisson brackets are defined by taking the Poisson brackets of the restrictions of the functions to the symplectic leaves.

A prime example is the Poisson structure in ${ \mathfrak { g } } ^ { * }$ which is defined by

$$
\pi _ { \xi } ( X , Y ) = - \langle [ X , Y ] , \xi \rangle , \quad \xi \in { \mathfrak { g } } ^ { * } , \quad X , Y \in ( { \mathfrak { g } } ^ { * } ) ^ { * } = { \mathfrak { g } } .\tag{3.34}
$$

The symplectic leaves are the co-adjoint orbits in ${ \mathfrak { g } } ^ { * }$

The formula (3.29) shows that, for a Hamiltonian action of G on the symplectic manifold $( M , \sigma )$ the momentum mapping $\mu$ intertwines the Poisson structure on $( M , \sigma )$ with the Poisson structure on the dual of the Lie algebra of $G .$

Remark 3.4 The general concept of Poisson structures has been invented by Lichnerowicz [20].

However, Lie [21, Vol. 2, Kap. 8] introduced a ”function group” as a fibration $\phi$ of a symplectic manifold (M, σ) over a manifold N with the property that for every smooth pair of functions $f$ and $g$ on N the Poisson brackets $\{ f \circ \phi , g \circ \phi \}$ are constant along the fibers of $\phi .$ This means that there is a unique Poisson structure on N such that $\{ f \circ \phi , g \circ \phi \} = \{ f , g \} _ { N } \circ \phi$ for every $f , g \in { \mathcal { F } } ( N )$ .

Moreover, in [21, Vol. 2, Kap. 19], Lie discussed the dual ${ \mathfrak { g } } ^ { * }$ of the Lie algebra of a Lie group $G ,$ and showed that the projection from $\mathrm { T } ^ { * } G$ onto ${ \mathfrak { g } } ^ { * }$ by means of the left trivialization $\operatorname { T } ^ { * } G = G \times { \mathfrak { g } } ^ { * }$ is a ”function group”. The Poisson structure on ${ \mathfrak { g } } ^ { * }$ defined by this ”function group” is equal to the one in (3.34).

## 3.9 Exercises

Exercise 3.1 Prove that

$$
\mathcal { L } _ { [ u , v ] } \omega = [ \mathcal { L } _ { u } , \mathcal { L } _ { v } ] \omega
$$

for every u, $, v \in \mathcal { X } ( M ) , \omega \in \Omega ^ { p } ( M ) , p \in \mathbf { Z } _ { \geq 0 }$

0

Exercise 3.2 Prove that in canonical coordinates the vector field $\mathrm { H } _ { f }$ is linear, if and only if $f$ is equal to a quadratic form plus a constant. Prove that if f and $g$ are quadratic forms, then $\{ f , g \}$ is a quadratic form and we have the identity

$$
\mathrm { H } _ { \{ f , g \} } = \mathrm { H } _ { g } \circ \mathrm { H } _ { f } - \mathrm { H } _ { f } \circ \mathrm { H } _ { g }
$$

between 2n × 2n-matrices = linear mappings from $\mathbf { R } ^ { 2 n }$ to $\mathbf { R } ^ { 2 n }$ . Hint: verify first that we have $\mathrm { H } _ { \{ f , g \} } = \mathrm { H } _ { f } \circ \mathrm { H } _ { g } - \mathrm { H } _ { g } \circ \mathrm { H } _ { f }$ if we view the vector fields as derivations.

Exercise 3.3 Let $p \in M$ and $v \in \mathcal { X } ( M )$ . p is called an equilibrium point of v if it is a fixed point for the v-flows $\mathrm { e } ^ { t v } , t \in \mathbf { R }$ . Now let $v = \mathrm { H } _ { f }$ for a smooth function f on M. Prove that the following statements are equivalent:

i) p is an equilibrium point of $v = \mathrm { H } _ { f }$

ii) $v ( p ) = 0 .$

iii) p is a stationary point of the function f in the sense that $1 f ( p ) = 0$

In the sequel assume that p is an equilibrium point of $v = \mathrm { H } _ { f }$ . Write $A ( t ) : = \mathrm { T } _ { p } \left( \mathrm { e } ^ { t v } \right)$ , which is a linear mapping from $E : = \mathrm { T } _ { \mathfrak { p } } M$ to itself. Write $B : = A ^ { \prime } ( 0 )$ , which also is a linear mapping from E to itself. Prove that ${ \cal A } ( t ) \dot { = } \mathrm { e } ^ { t B } , t \in { \bf R }$ , that $A ( t ) \in \mathrm { S p } ( E , \sigma _ { p } )$ , and that B is an infinitesimally symplectic matrix.

Prove that, if we view B as a (linear) vector field on $\mathrm { T } _ { p } M ,$ then $B = \mathrm { H } _ { f _ { 2 } }$ , in which $f _ { 2 }$ denotes the quadratic term in the Taylor expansion of f at the point $p ,$ where the Taylor expansion is written down in any suitable system of local coordinates. Prove that $f _ { 2 }$ is independent of the choice of the system of local coordinates.

Exercise 3.4 In (3.15), let  run over a finite-dimensional smooth manifold E. Define $\Gamma _ { t } : E $ TX by $\Gamma _ { t } ( \epsilon ) = ( \gamma _ { \epsilon } ( t ) , \gamma _ { \epsilon } ^ { \prime } ( t ) )$ , and define $i : E \to \mathbf { R }$ by $i ( \epsilon ) = I ( \gamma _ { \epsilon } )$ . Assume furthermore that, for every $\epsilon \in E , \gamma _ { \epsilon }$ is a solution of the Euler-Lagrange equations $[ L ] = 0$

Let $\Phi _ { L } : \mathrm { T } X \to \mathrm { T } ^ { * } X$ be the velocity-to-momentum mapping defined by L. Prove that

$$
\mathrm { d } i = \Gamma _ { b } ^ { * } \Phi _ { L } ^ { * } \tau - \Gamma _ { a } ^ { * } \Phi _ { L } ^ { * } \tau ,
$$

in which τ is the tautological one-form on $\mathrm { T } ^ { * } X$ . Prove that

$$
\Gamma _ { b } ^ { * } \Phi _ { L } ^ { * } \sigma = \Gamma _ { a } ^ { * } \Phi _ { L } ^ { * } \sigma .
$$

Now let, for every $( x , v ) \in \mathrm { T } X , t \mapsto \gamma _ { ( x , v ) } ( t )$ denote the solution $\gamma$ of the Euler-Lagrange equations such that $\gamma ( 0 ) = x$ and $\gamma ^ { \prime } ( 0 ) = v . ~ \mathrm { { \ A p p l y } }$ the previous equation to this family of curves in order to prove that $\Phi _ { L } ^ { * } \sigma$ is invariant under the Euler-Lagrange flow in TX.

Exercise 3.5 With the notation of (3.13), prove that $\{ \mu _ { v } , \mu _ { w } \} = \mu _ { [ v , w ] } .$

0

Exercise 3.6 Let $( M , \sigma )$ be a 2n-dimensional symplectic manifold and let $\Phi : M \to { \mathbf { R } } ^ { 2 n }$ be a smooth mapping with coordinate functions $x _ { 1 } , \ldots , x _ { n } , \xi _ { 1 } , \ldots , \xi _ { n }$ . Prove that

$$
\Phi ^ { * } \left( \sum _ { i = 1 } ^ { n } \mathrm { d } \xi _ { i } \wedge \mathrm { d } x _ { i } \right) = \sigma ,
$$

if and only if $\left\{ x _ { i } , x _ { j } \right\} = 0 , \left\{ \xi _ { i } , x _ { j } \right\} = \delta _ { i j } , \mathrm { a n d } \left\{ \xi _ { i } , \xi _ { j } \right\} = 0 .$

0

Exercise 3.7 Let β be a closed two-form on the configuration space $X$ , and let the force field F be given by $F ( x , v ) = - \mathrm { d } V ( x ) - \beta _ { x } ( v )$ for every $x \in X , v \in \mathrm { T } _ { x } X$ . Here we identify $\beta _ { x }$ in the usual way with a linear mapping from $\mathrm { T } _ { x } X$ to $( \mathrm { T } _ { x } X ) ^ { * }$ . The term $- \beta _ { x } ( v )$ is called a magnetic term in the force field.

Prove that $\sigma + \pi ^ { * } \beta$ is a symplectic form on $\mathrm { T } ^ { * } X$ . Prove that the velocity-to-momentum mapping $\begin{array} { r } { \Phi _ { T } : ( x , v ) \mapsto ( x , \frac { \partial T ( x , v ) } { \partial v } } \end{array}$ transforms the equations of motion $[ T ] = F$ into the Hamiltonian system defined by the function $h = ( T + V ) \circ \Phi _ { T } ^ { - 1 }$ , not with respect to the canonical symplectic form σ of $\mathrm { T } ^ { * } X$ , but with respect to the symplectic form $\sigma + \pi ^ { * } \beta ,$ the canonical stymplectic form ”shifted by the magnetic term”.

## 4 Hamilton-Jacobi Theory

## 4.1 Lagrange Manifolds

Consider a first order partial differential equation

$$
f ( x , \mathrm { d } \phi ( x ) ) = 0 ,\tag{4.1}
$$

in which the unknown function $\phi$ is a smooth function defined on an open subset U of an n--dimensional smooth manifold X and f is a given smooth function on an open subset V of the cotangent bundle $\mathrm { T } ^ { * } X$ of X .

If we write

$$
N : = \{ ( x , \xi ) \in V \mid f ( x , \xi ) = 0 \}\tag{4.2}
$$

for the zeroset of f in $\mathrm { T } ^ { * } X$ and

$$
\Lambda = \{ ( x , \mathrm { d } \phi ( x ) ) \in \mathrm { T } ^ { * } X \mid x \in U \}\tag{4.3}
$$

for the graph of dφ viewed as a subset of $\mathrm { T } ^ { * } X$ , then (4.1) is equivalent to the inclusion

$$
\Lambda \subset N\tag{4.4}
$$

between subsets of $\mathrm { T } ^ { * } X$

The mapping dφ $\mathbf { \chi } : x \mapsto ( x , \mathrm { d } \phi ( x ) )$ is a smooth mapping from U to $\mathrm { T } ^ { * } X$ , with image equal to Λ and with the canonical projection $\pi : \mathrm { T } ^ { * } X \to X$ as a left inverse. Therefore dφ is a smooth embedding and Λ is a smooth n-dimensional submanifold of $\mathrm { T } ^ { * } X$ . The fact that, for each $\lambda \in \Lambda$ the restriction to $\mathrm { T } _ { \lambda } \Lambda$ of $\mathrm { T } _ { \lambda }$ π is bijective from $\mathrm { T } _ { \lambda } \Lambda$ to $\mathrm { T } _ { \pi ( \lambda ) } X$ is equivalent to the condition that

$$
\mathrm { T } _ { \lambda } \Lambda \cap \ker \mathrm { T } _ { \lambda } \pi = 0 ,\tag{4.5}
$$

i.e. $\mathrm { T } _ { \lambda } \Lambda$ is complementary to the tangent space ker $\mathrm { T } _ { \lambda }$ π of the fiber through the point λ.

Conversely, if Λ is any smooth n-dimensional submanifold of $\mathrm { T } ^ { * } X$ which satisfies (4.5), then $\pi | _ { \Lambda }$ is a local diffeomorphism from Λ onto an open subset U of X. If moreover $\pi | _ { \Lambda }$ is injective, which can be arranged by restricting to a suitable open neighborhood of any given point of Λ, then $\pi | _ { \Lambda }$ is a diffeomorphism, and its inverse $\alpha : = ( \pi | _ { \Lambda } ) ^ { - 1 } : U \to \mathrm { T } ^ { * } X$ is a smooth one-form on U. Locally the condition that $\alpha = \mathrm { d } \phi$ for a smooth function φ is equivalent to the condition that α is closed, i.e. $\mathrm { d } \alpha = 0$

It follows from (2.3) and (2.4) that

$$
d \alpha = d ( \alpha ^ { * } \tau ) = \alpha ^ { * } ( \mathrm { d } \tau ) = \alpha ^ { * } \sigma ,
$$

and therefore α is closed if and only if $\alpha ^ { * } \sigma = 0$ . The latter condition means that, for every $x \in U$ 2

$$
\sigma _ { \alpha ( x ) } \left( \operatorname { T } _ { x } \alpha ( u ) , \operatorname { T } _ { x } \alpha ( v ) \right) = 0 , \quad u , v \in \operatorname { T } _ { x } X .\tag{4.6}
$$

On the other hand

$$
\mathrm { T } _ { ( x , \alpha ( x ) ) } \Lambda = \{ \mathrm { T } _ { x } \alpha ( v ) \mid v \in \mathrm { T } _ { x } X \} ,
$$

and therefore (4.6) means that $\mathrm { T } _ { \lambda } \Lambda$ is an isotropic linear subspace of $\mathrm { T } _ { \lambda } ( \mathrm { T } ^ { * } X )$ , if we write $\lambda =$ $( x , \alpha ( x ) )$ . Because dim $\mathrm { T } _ { \lambda } \Lambda = n ,$ , it is a Lagrange plane in $\mathrm { T } _ { \lambda } ( \mathrm { T } ^ { * } X )$ •

A Lagrange submanifold of a 2n-dimensional symplectic manifold $( M , \sigma )$ is defined as an ndimensional smooth submanifold Λ of M such that, for every $\lambda \in \Lambda , \mathrm { T } _ { \lambda } \Lambda$ is a Lagrange plane in $\mathrm { T } _ { \lambda } M$ , with respect to the symplectic form $\sigma _ { \lambda }$ . We have just proved above that a submanifold Λ of $\mathrm { T } ^ { * } X$ is equal to $\alpha ( U )$ for a closed one-form on an open subset U of X, if and only if

i) Λ is a Lagrange submanifold of $\mathrm { T } ^ { * } X$

ii) Λ is transversal to the fibers of T∗ X in the sense of (4.5), and

iii) The restriction of π to Λ is injective.

## 4.2 Lie’s View on First Order PDE

It is the idea of Lie, to generalize the concept of a solution of (4.1) slightly, by first investigating what the condition means for a Lagrange submanifold Λ of a symplectic manifold $( M , \sigma )$ to be contained in the given subset N of M. Thereby he dropped the conditions ii) and iii), which relate the position of Λ with respect to the projection $\pi .$

In the sequel we will assume that $\mathrm { d } f ( \boldsymbol n ) \ne 0$ for every $n \in N$ . This implies that N is a smooth $( 2 n - 1 )$ -dimensional submanifold of M, and $\mathrm { T } _ { n } N = \ker ( \mathrm { d } f ( n ) )$ ) for every $n \in N$ . Furthermore, $\Lambda \subset N$ implies that, for every $\lambda \in \Lambda$

$$
\mathrm { T } _ { \lambda } \Lambda \subset \mathrm { T } _ { \lambda } N = \ker ( \mathrm { d } f ( \lambda ) ) ,
$$

which is equivalent to the inclusion

$$
\mathbf { R } \ \mathrm { H } _ { f } ( \lambda ) = \ker ( \mathrm { d } f ( \lambda ) ) ^ { \sigma _ { \lambda } } \subset ( \mathrm { T } _ { \lambda } \Lambda ) ^ { \sigma _ { \lambda } } = \mathrm { T } _ { \lambda } \Lambda .\tag{4.7}
$$

of the $\sigma _ { \lambda }$ -orthogonal complements. In the first identity in (4.7) we have used that the codimension of ker $\cdot ( \mathrm { d } f ( \lambda )$ is equal to one, and that $\sigma _ { \lambda } ( u , \mathrm H _ { f } ( \lambda ) ) = \mathrm { d } f ( \lambda ) ( u ) = 0 { \mathrm { ~ i f ~ } } u \in \ker ( \mathrm { d } f ( \lambda ) )$ . In the third identity in (4.7) we have used that $\mathrm { T } _ { \lambda } \Lambda$ is a Lagrange plane with respect to the symplectic form $\sigma _ { \lambda }$ .

The inclusion (4.7) means that, at every point of Λ, the vector field $\mathrm { H } _ { f }$ is tangent tot Λ. This implies that Λ is foliated by the one-dimensional solution curves of the Hamiltonian system defined by the function $f .$

Clearly, every submanifold I of Λ is isotropic, in the sense that, for every $i \in I , \mathrm { T } _ { i } I$ is an isotropic linear subspace of $\mathrm { T } _ { i } M$ . Also we have obviously that $I \subset N$ and that the ”Hf -flow-out of $I ^ { \dag }$ , the set

$$
I ^ { \prime } : = \left\{ \mathrm { e } ^ { t \mathrm { H } _ { f } } ( i ) \mid ( i , t ) \in J \right\}
$$

is contained in Λ, if J is a suitable open neighborhood of $I \times \{ 0 \}$ in $I \times \mathbf { R }$ . If dim $I = n - 1$ and $\mathrm { H } _ { f } ( i ) \not \in \mathrm { T } _ { i } I$ for every $i \in I ,$ then the mapping

$$
( i , t ) \mapsto  { \mathrm { e } } ^ { t \textup { H } _ { f } } ( i )
$$

is a smooth immersion, hence its image is n-dimensional, and the conclusion is that $I ^ { \prime }$ is an open subset of Λ. In this sense Λ is locally the only Lagrange submanifold of M such that $I \subset \Lambda \subset N$ .

Now suppose conversely that I is an $( n - 1 )$ )-dimensional isotropic submanifold of M, $I \subset N$ and $\mathrm { H } _ { f } ( i ) \not \in \mathrm { T } _ { i } I$ for every $i \in I$ . Then I0 is an n-dimensional smooth submanifold of M. Furthermore $I ^ { \prime } \subset N$ , because f is invariant under the $\operatorname { H } _ { f ^ { - } } \operatorname { f l o w }$ , and therefore its zeroset N is invariant under the Hf -flow. $\operatorname { I f } i \in I$ then $\mathrm { T } _ { i } I \subset \mathrm { T } _ { i } N$ implies that

$$
\mathbf { R } \ \mathrm { H } _ { f } ( i ) = ( \mathrm { T } _ { i } N ) ^ { \sigma _ { i } } \subset ( \mathrm { T } _ { i } I ) ^ { \sigma }
$$

and therefore

$$
\mathrm { T } _ { i } I ^ { \prime } = \mathrm { T } _ { i } I + \mathbf { R } \mathrm { H } _ { f } ( i )
$$

is isotropic, and hence a Lagrange plane because it is n-dimensional. If $( i , t ) \in J$ and we write $\Phi = \operatorname { e } ^ { t \mathrm { ~ H ~ } _ { f } }$ , then

$$
\mathrm { T } _ { \Phi ( i ) } I ^ { \prime } = \mathrm { T } _ { i } \Phi \left( \mathrm { T } _ { i } I ^ { \prime } \right)
$$

is a Lagrange plane as well, because ${ \mathrm { T } } _ { i } \Phi$ preserves the symplectic form. The conclusion is that $I ^ { \prime }$ is a Lagrange submanifold of M such that $I \subset I ^ { \prime } \subset N$ , and we have a local existence and uniqueness theorem for Lagrange submanifolds Λ of M such that $I \subset \Lambda \subset N$

Remark 4.1 More generally, let N be a smooth submanifold of M of any dimension, and suppose that the dimension of $K _ { n } : = \mathrm { T } _ { n } N \cap ( \mathrm { T } _ { n } N ) ^ { \sigma }$ does not depend on $n \in N$ . Because $K _ { n }$ is equal to the kernel of the restriction to $\mathrm { T } _ { n } N$ of $\sigma _ { n } .$ , we are in the situation of Subsection (2.3) with $\omega = \sigma | _ { N }$ Let $\pi : N  P$ be a fibration as in Subsection (2.3), and let $\sigma _ { P }$ be the reduced symplect ic form, the symplectic form on $P$ such that $\sigma | _ { N } = \pi ^ { * } \sigma _ { P }$ . Then the Lagrange submanifolds Λ of M such that $\Lambda \subset N$ are locally of the form $\Lambda = \pi ^ { - 1 } ( \Lambda _ { P } )$ , in which $\Lambda _ { P }$ is an arbitrary Lagrange submanifold of P with respect to the symplectic form $\sigma _ { P }$ . This characterization is also due to Lie.

## 4.3 An Initial Value Problem

Let S be an $( n - 1 )$ -dimensional smooth submanifold of X and $\psi$ a smooth real-valued function on S. The above leads to a local existence and uniqueness theorem for solutions $\phi$ of (4.1) which satisfy the additional ”initial condition” that

$$
\phi ( s ) = \psi ( s ) , \quad s \in S .\tag{4.8}
$$

We will make the assumptions that $x _ { 0 } \in S , \xi _ { 0 } \in ( \mathrm { T } _ { x _ { 0 } } X ) ^ { * } , f ( x _ { 0 } , \xi _ { 0 } ) = 0 ,$

$$
\left. \frac { \partial f ( x _ { 0 } , \xi ) } { \partial \xi } \right| _ { \xi = \xi _ { 0 } } \notin \mathrm { T } _ { x _ { 0 } } S .\tag{4.9}
$$

and finally

$$
\mathrm { d } \psi ( x _ { 0 } ) = \xi _ { 0 } | _ { \mathrm { T } _ { x _ { 0 } } S } .\tag{4.10}
$$

Obviously the condition (4.10) is necessary if we want to have $\xi _ { 0 } = \mathrm { d } \phi ( x _ { 0 } )$ for a solution $\phi$ of (4.1) and (4.8). The transversality condition (4.9) is the natural one in order to avoid singularities in the solution.

For every $s \in S$ , the restriction mapping $\xi \mapsto \xi | _ { \mathrm { T } _ { s } S }$ is a linear mapping from $( \mathrm { T } _ { \boldsymbol { s } } \boldsymbol { X } ) ^ { * }$ onto $( \mathrm { T } _ { s } S ) ^ { * }$ with a one-dimensional kernel, equal to $( \mathrm { T } _ { s } S ) ^ { 0 }$ . Therefore the set

$$
l _ { s } : = \Big \{ \xi \in ( \mathrm { T } _ { s } X ) ^ { * } \ | \ \xi | _ { \mathrm { T } _ { s } S } = \mathrm { d } \psi ( s ) \Big \}
$$

is a straight line in $( \Gamma _ { s } X ) ^ { * }$ , and the condition (4.9) means that, at $\xi _ { 0 } , \ l _ { x _ { 0 } }$ is transversal to $N \cap ( \mathrm { T } _ { x _ { 0 } } X ) ^ { * }$ . It follows therefore from the implicit function theorem, that there is an open neighborhood $S _ { 0 }$ of $x _ { 0 }$ in $S$ and a neighborhood W of $( x _ { 0 } , \xi _ { 0 } )$ in $\mathrm { T } ^ { * } X$ , such that for each $s \in S _ { 0 }$ there is a unique $\xi = \xi ( s ) \in ( \mathrm { T } _ { s } X ) ^ { * }$ , such that $( x , \xi ) \in W$ and

$$
\xi | _ { \mathrm { T } _ { s } S } = \mathrm { d } \psi ( s ) \quad \mathrm { a n d } \quad f ( s , \xi ) = 0 .\tag{4.11}
$$

Moreover, $s \mapsto \left( s , \xi ( s ) \right)$ is a smooth mapping from $S _ { 0 }$ to $\mathrm { T } ^ { * } X$ . Because it has $\pi$ as a left inverse, it is an embedding and the image is a smooth $( n - 1 )$ )-dimensional subsmanifold I of $\mathrm { T } ^ { * } X$ , which by construction is contained in N.

Below we shall prove that I is isotropic. According to Subsection 4.2, locally there is a unique Lagrange submanifold Λ of $\mathrm { T } ^ { * } X$ such that $I \subset \Lambda \subset N$ , and

$$
\mathrm { T } _ { \lambda _ { 0 } } \Lambda = \mathrm { T } _ { \lambda _ { 0 } } I + { \bf R } \mathrm { H } _ { f } ( \lambda _ { 0 } )
$$

if $\lambda _ { 0 } = \left( x _ { 0 } , \xi _ { 0 } \right)$ . Because $\mathrm { T } _ { \lambda _ { 0 } } \pi$ maps $\mathrm { T } _ { \lambda _ { 0 } } I$ onto $\mathrm { T } _ { x _ { 0 } } S$ and maps $\mathrm { H } _ { f } ( \lambda _ { 0 } )$ to $\partial f / \partial \xi ( \lambda _ { 0 } ) \not \in \mathrm { T } _ { x _ { 0 } } S$ cf. (4.9, we have that the restriction to $\mathrm { T } _ { \lambda _ { 0 } } \Lambda$ of $\mathrm { T } _ { \lambda _ { 0 } } \pi$ is surjective from $\mathrm { T } _ { \lambda _ { 0 } } \Lambda$ to $\mathrm { T } _ { x _ { 0 } } X$ , hence bijective, because both vector spaces have the same dimension n. It follows that the transversality condition (4.5) holds at $\lambda = \lambda _ { 0 }$ , and therefore Λ is locally equal to the graph of dφ for a smooth function φ, which is a solution of (4.1) because $\Lambda \subset N$ . On the other hand $I \subset \Lambda$ implies that for all s in a connected neighborhood $S _ { 0 }$ of x0 in S we have that the restriction to $\mathrm { T } _ { s } S$ of $\mathrm { d } \phi ( s )$ is equal to $\mathrm { d } \psi ( s )$ , which implies that d $\big ( \phi \big | _ { S _ { 0 } } \big ) = \mathrm { d } \psi$ ψ, or $\phi | _ { S _ { 0 } } - \psi = c$ is a constant. Replacing φ by $\phi - c$ we arrive at the locally unique solution of the initial value problem (4.1), (4.8).

In order to prove that I is an isotropic submanifold of $\mathrm { T } ^ { * } X$ , we consider the submanifold T∗S X of all $( x , \xi ) \in \mathrm { T } ^ { * } X$ such that $x \in S$ and $\xi \in ( \Gamma _ { x } X ) ^ { * }$ . Let ι denote the identity as a mapping from $\mathrm { T } _ { S } ^ { * } X$ to $\mathrm { T } ^ { * } X$ , and define the restriction mapping $\rho : \mathrm { T } _ { S } ^ { * } X \to \mathrm { T } ^ { * } S$ by

$$
\begin{array} { r } { \rho ( x , \xi ) = \left( x , \xi \vert _ { \mathrm { T } _ { x } S } \right) , \quad x \in S , \quad \xi \in \left( \mathrm { T } _ { x } X \right) ^ { * } . } \end{array}
$$

Then

$$
\iota ^ { * } \left( \tau _ { \mathrm { T } ^ { * } X } \right) = \rho ^ { * } \left( \tau _ { \mathrm { T } ^ { * } S } \right) \quad \mathrm { o n } \quad \mathrm { T } _ { S } ^ { * } X ,
$$

which is a tautology if one writes out the definitions of the left and right hand side. Taking the exterior derivative of the left hand side and using that the exterior derivative commutes with pullbacks by smooth mappings, we obtaine that

$$
\iota ^ { * } \left( \sigma _ { \mathrm { T } ^ { * } X } \right) = \rho ^ { * } \left( \sigma _ { \mathrm { T } ^ { * } S } \right) \quad \mathrm { o n } \quad \mathrm { T } _ { S } ^ { * } X .
$$

Because the graph of dψ is an isotropic submanifold $\Lambda _ { S }$ of $\mathrm { T } ^ { * } S _ { \mathrm { \large : } }$ it follows that $\rho ^ { - 1 } ( \Lambda _ { S } )$ is an isotropic submanifold of $\mathrm { T } ^ { * } X$ , and therefore $I = \rho ^ { - 1 } ( \Lambda _ { S } ) \cap N$ is isotropic as well.

## 4.4 Ray Bundles

It is a classical observation that the bundles of rays (= straight lines) which appear in geometrical optics, are orthogonal to some hypersurface S. An example is the bundle of rays which emanate from a given source point, these are the normals to every sphere with center at the source point. In the plane every bundle of rays = one-parameter familty of straight lines is orthogonal to some curve, for this it suffices to take a solution curve of a vector field which is orthogonal to the rays. However, in higher dimensions n it is a quite special property of an $( n - 1 )$ -parameter family of rays to be normal to a hypersuface S.

Let S be an oriented hypersurface, which leads to an orientation of the normals of S. Let $\phi$ be the function which is equal to zero on S and has derivative in the direction of the oriented normals equal to 1. Then, at least where the normals define a fibration of the space, $\phi$ is a smooth function, and the rays are orthogonal to every level hypersurface of $\phi .$ Indeed, if $n ( s )$ denotes the normal vector to $S$ at the point $s \in S$ , then the level set of $\phi$ at the level t is equal to the set of points

$$
S _ { t } = \{ s + t n ( s ) \mid s \in S \}
$$

and its tangent space consists of the points $\delta s + t \operatorname { D } n ( s )$ δs in which $\delta s$ is tangent to $S .$ It follows from $\langle n ( s ) , n ( s ) \rangle \equiv 1$ that $\langle \mathrm { D } n ( s ) \delta s , n ( s ) \rangle = 0$ , and therefore $\begin{array} { r } { \langle \delta \boldsymbol { s } + \boldsymbol { t } \operatorname { D } n ( \boldsymbol { s } ) \delta \boldsymbol { s } , n ( \boldsymbol { s } ) \rangle = \langle \delta \boldsymbol { s } , n ( \boldsymbol { s } ) \rangle = 0 . } \end{array}$

It follows that the gradient of $\phi$ at the point $s + t n ( s )$ is equal to $n ( s )$ , which means that the function $\phi$ satisfies the nonlinear first order partial differential equation

$$
\sum _ { i = 1 } ^ { n } \left( { \frac { \partial \phi ( x ) } { \partial x _ { i } } } \right) ^ { 2 } = 1 .\tag{4.12}
$$

Conversely, if $\phi$ satisfies (4.12), then the normals to the level hypersurfaces of $\phi$ form an $( n - 1 )$ parameter family of straight lines.

Hamilton [10] discovered this bijective correspondence between the ray bundles in geometrical optics and real-valued function $\phi$ which satisfy a partial differential equation of the form $\left( 4 . 1 2 \right)$ , where the rays are the the lines which are orthogonal to the level surfaces of φ. He called φ the characteristic function of the ray bundle, and the partial differential equation (4.12) is sometimes called the eikonal equation of geometrical optics.

The equation (4.12) is of the form (4.1), if we take

$$
f ( x , \xi ) = \sum _ { i = 1 } ^ { n } \left( \xi _ { i } \right) ^ { 2 } - 1 .\tag{4.13}
$$

The corresponding Hamiltonian system is dx $/ \mathrm { d } t = 2 \xi , \mathrm { d } \xi / \mathrm { d } t = 0$ , we obtain that the velocity vector $\mathrm { d } x ( t ) / \mathrm { d } t$ does not depend on t. Moreover, it is pointing in the direction of $\xi = \operatorname { g r a d } \phi .$ which means that the projections $x ( t )$ to the position space $X = \mathbf { R } ^ { n }$ are straight lines orthogonal to the level hypersurfaces of $\phi ,$ they form the ray bundle corresponding to solution $\phi$ of the eikonal equation.

In the construction of the characteristic function, it is essential that the rays define a fibration of X, which is the case as long as the Lagrange manifold Λ, which is supposed to be the graph of dφ, is transversal to the fibers, cf. (4.5). However, it is a very common phenomenon that at some points the rays start criss-crossing, which correspond to points where the transversality condition (4.5) no longer holds. At such a point the density of the rays becomes infinite, and for this reason such a point is called a caustic point, a point ”where the light burns”. At caustic points the characteristic function is no longer smooth, and at points through which more than one ray passes the function $\phi$ becomes multi-valued.

The good news is that, even if such singularities in the ray bundle and its characteristic function occur, the Lagrange manifold Λ remains a smoothly immersed submanifold $o f \operatorname { T } ^ { * } X$ . Therefore, in order to include ray bundles with caustics, we propose the following definition:

A ray bundle consists of the projections to the base manifold X of the Hf -solution curves in a smoothly immersed Lagrange submanifold of $\mathrm { T } ^ { * } X$ , which is contained in the zeroset of $f .$

This makes Lie’s point of view, of allowing any smoothly immersed Lagrange submanifold of $\mathrm { T ^ { * } }$ X which is contained in the zeroset of $f$ as a solution of (4.1), not just aan matter of abstract generalization, but very relevant from the point of view of practical applications.

Ray propagation in inhomogenous media, where the local speed of propagation $c ( x )$ depends smoothly on the position $x \in X$ , is described by the above theory in which the function f in (4.13) is replaced by

$$
f ( x , \xi ) = c ( x ) ^ { 2 } \sum _ { i = 1 } ^ { n } { ( \xi _ { i } ) ^ { 2 } } - 1 .
$$

Ray bundles defined by other types of functions $f$ on $\mathrm { T } ^ { * } X$ also have applications.

## 4.5 High Frequency Waves and Fourier Integral Operators

Huygens [15] could not convince the physicists of the wave nature of light, but Young and especially Fresnel [8] did, with their beautiful quantitative analysis of interference patterns, which have no decent explanation in a particle model.

Let us consider waves which are solutions of the standard wave equation

$$
\Pi : = \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } - \Delta u : = \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } - \sum _ { j = 1 } ^ { n } \frac { \partial ^ { 2 } u } { \partial x _ { j } ^ { 2 } } .\tag{4.14}
$$

Let us see what happens if we apply the wave operator ✷ to a simple progressing wave

$$
u ( x , t ) = e ^ { i \omega ( t - \phi ( x ) ) } a ( x ) ,\tag{4.15}
$$

in which $\phi ( x )$ and $a ( x )$ are real valued functions of $x ,$ called the phase function and the amplitude function of the simple progressing wave, where the level surfaces $\phi ( x ) = t$ in the position space, the x-space, are the wave fronts. ω is a frequency variable, and we are in particular interested in the asymptotic behaviour as $\omega  \infty$ . (Due to the small wave length and the very high speed of propagation, visible light has an extremely high frequency.)

We have

$$
( \sqcup u ) ( x , t ) = e ^ { i \omega ( t - \phi ( x ) ) } \left[ \omega ^ { 2 } u _ { 2 } ( x , t ) + i \omega u _ { 1 } ( x , t ) + u _ { 0 } ( x , t ) \right] ,
$$

in which

$$
u _ { 2 } ( x , t ) = \left( \sum _ { j = 1 } ^ { n } \left( \frac { \partial \phi ( x ) } { \partial x _ { j } } \right) ^ { 2 } - 1 \right) a ( x ) ,
$$

$$
u _ { 1 } ( x , t ) = 2 \sum _ { j = 1 } ^ { n } \frac { \partial \phi ( x ) } { \partial x _ { j } } \frac { \partial a ( x ) } { \partial x _ { j } } + ( \Delta \phi ) ( x ) a ( x )
$$

and $u _ { 0 } ( x , t ) = - \Delta a ( x )$

If $a ( x ) \neq 0$ , then $( \boldsymbol { \Pi } \boldsymbol { u } ) ( \boldsymbol { x } , t )$ grows quadratically as a function of $\omega$ for $\omega \longrightarrow \infty$ , unless the phase function $\phi ( x )$ satisfies the eikonal equation (4.12).

Assuming that $\phi$ satisfies the eikonal equation, the leading term in ✷u grows linearly with $\omega ,$ unless the amplitude satisfies the homogeneous linear first order partial differential equation

$$
u _ { 1 } ( x , t ) = 2 \sum _ { j = 1 } ^ { n } \frac { \partial \phi ( x ) } { \partial x _ { j } } \frac { \partial a ( x ) } { \partial x _ { j } } + ( \Delta \phi ) ( x ) a ( x ) = 0 ,\tag{4.16}
$$

called the transport equation for the amplitude.

In order to analyse (4.16), we consider the solutions $x ( s )$ of the system of ordinary differential equations

$$
\frac { \mathrm { d } x _ { j } } { \mathrm { d } s } = 2 \frac { \partial \phi ( x ) } { \partial x _ { j } } , 1 \leq j \leq n .\tag{4.17}
$$

The solution curves of (4.17) are orthogonal to the wave fronts $\phi ( x ) = $ constant, and therefore are equal to the rays of the ray bundle of which $\phi$ is the characteristic function. The transport equation (4.16) then is equivalent to

$$
\frac { \mathrm { d } a \big ( x ( s ) \big ) } { \mathrm { d } s } + ( \Delta \phi ) ( x ( s ) \big ) a \big ( x ( s ) \big ) = 0 ,
$$

a homogeneous first order linear ordinary differential equation for the function $s \mapsto a ( x ( s ) )$ . This implies that we can prescribe $a ( x )$ freely on an $( n - 1 )$ )-dimensional manifold S which is transversal to the rays. If we choose the ”initial amplitude” a|S equal to zero outside a small neighborhood of a given point $x _ { 0 }$ then the solution $a ( x )$ will be equal to zero outisde a narrow tube along the ray through the point $x _ { 0 }$ . In this sense the waves u of the form (4.15) which are asymptotic solutions of (4.14) in the sense that ✷u remains bounded as $\omega  \infty$ , will propagate along the rays. In this sense geometrical optics is the high frequency limit of wave optics.

The procedure can be refined by replacing the amplitude function $a ( x )$ in (4.15) by an asymptotic expansion of the form

$$
a ( x , \omega ) \sim \sum _ { k = 0 } ^ { \infty } a _ { j } ( x ) \omega ^ { - k } , \quad \omega \to \infty
$$

in negative powers of the frequency ω. One may verify that by successively solving inhomogenous linear ordinary differential equations along the rays for the $a _ { k } ( x ) , k \geq 1$ , one can arrange that, for any K, $\begin{array} { r } { \boxed { u } = \mathcal { O } ( \omega ^ { - K } ) } \end{array}$ as $\omega \longrightarrow \infty$

As observed in Subsection 4.4, the construction of the phase function $\phi ( x )$ , and therefore of the simple progressing wave (4.15), brakes down at caustic points, and the amplitude $a ( x )$ becomes infinite if one approaches such a point. It turns out that near such points one can still obtain asymptotic solutions of the wave equation by replacing the simple progressing wave (4.15) by a ”continuous superposition” of such waves, an oscillatory integral of the form

$$
u ( x , t ) \sim \sum _ { k = 0 } ^ { \infty } \omega ^ { N / 2 - k } \int _ { \mathbf { R } ^ { N } } \mathrm { e } ^ { \omega \left( t - \phi ( x , \theta ) \right) } a _ { k } ( x , \theta ) \mathrm { d } \theta , \quad \omega \to \infty .\tag{4.18}
$$

Here, in order to avoid any problems with the convergence of the integral over the auxiliary $\theta _ { - }$ -variables, it is assumed that $a _ { k } ( x , \theta ) = 0$ for all θ outside a compact subset. Maslov [23] showed that for quite general linear partial differential equations $P u = 0$ one can construct oscillatory integrals (4.18) which are global asymptotic solutions, i.e. also in neighborhoods of caustic points. These oscillatory integrals correspond to Lagrange submanifolds Λ of $\mathrm { T } ^ { * } X$ which are contained in the zeroset of a certain function $p$ on $\mathrm { T } ^ { * } X$ which is called the principal symbol of the linear differential operator P . Cf. [6] for a survey.

If one also integrates over the frequency variable $\omega ,$ then one obtains distributions, which are called Fourier integral distributions, invented by H¨ormander [14]. The singularities of a Fourier integral distribution, i.e. its behaviour near points where it is not equal to a smooth function, have a very precise description in terms of the corresponding Lagrange submanifold of $\mathrm { T } ^ { * } X$ .

A simple example is Dirac’s delta function situated at a point $x \in X$ . It is a Fourier integral distribution and the Lagrange manifold corresponding to it is the fiber $( \mathrm { T } _ { x } X ) ^ { * }$ of the cotangent bundle T∗ X over the point $x .$ This is an extreme example of a Lagrange manifold which does not satisfy the transversality condition (4.5).

Linear integral operators from ${ \mathcal { F } } ( Y )$ to ${ \mathcal { F } } ( X )$ which have a distribution kernel on $X \times Y$ which is a Fourier integral distribution are called Fourier integral operators. These form a very wide class of operators, which include all the propagation operators = ”Green functions” of linear partial differential equations $P u = 0$ of wave type. The aforementioned description of the singularites of Fourier integral distributions leads to very detailed descriptions of the propagation of singularities of the solutions of the partial differential equation $P u = 0$ , or of the corresponding inhomogenous equation $P u = f$ , cf. [5].

## 4.6 Some History

As already mentioned, Hamilton [10] found the description of ray bundles in geometrical optics in terms of their characteristic functions, together with the nonlinear partial differential equation (4.12 satisfied by the characteristic function.

However, he did not ask the question how to solve a general nonlinear partial differential equation of the form $( 4 . 1 ) . \mathrm { ~ - ~ i t }$ was Jacobi [16], [17] who observed that the solution of such a partial differential equation can be reduced to the solution of a Hamiltonian system of ordinary differential equations. Since then the theory is called ”Hamilton-Jacobi theory”.

Lie developed the idea of viewing the solution as a Lagrange submanifold of the cotangent bundle in a series of articles in 1872–78, and stressed the point that it is based on the fact that the flow of the Hamiltonian system of the function f leaves the canonical two-form $\sigma$ of the cotangent bundle invariant. For him the use of the group of transformations which leave f and σ invariant was analogous to the use of the Galois group in the solution of polynomial equations. Engel introduced the name ${ } ^ { \mathrm { { ? } V e r e i n " } } = { } ^ { \mathrm { { ? } v } } \mathrm { { c l u b " } }$ for any submanifold of the cotangent bundle. Lie followed this, but later authors like Elie Cartan didn’t. An accessible account of Lie’s ideas on first order partial ´ differential equations is the book of Engel and Faber [7].

The fact that Lagrange manifolds are fundamental in so many situations made Weinstein [28] talk about the Symplectic Creed: ”Everything is a Lagrange manifold”. More recently so-called special Lagrange manifolds, invented by Harvey and Lawson [12], made their appearance in mirror symmetry.

## 4.7 Exercises

Exercise 4.1 In the notation of Example 3.3 on integrable systems, prove that the level sets $M _ { c }$ are Lagrange submanifolds of M. If $M = \mathrm { T } ^ { * } X$ and the connected component C of $M _ { c }$ is compact, then C can only be equal to dφ for some smooth function $\phi$ on X, if X is diffeomorphic to a torus.

Exercise 4.2 Prove that, for any given $x \in X$ , the fiber $( \mathrm { T } _ { x } X )$ j over x is a Lagrange submanifold of $\mathrm { T } ^ { * } X$ . Define

$$
I = \left\{ \xi \in ( \mathrm { T } _ { x } X ) ^ { * } \mid f ( x , \xi ) = 0 \right\} .
$$

Suppose that $\partial f ( x , \xi ) / \partial \xi \neq 0$ for every $\xi \in I$ . Prove that N is an $( n - 1 )$ -dimensional isotropic submanifold of $\mathrm { T } ^ { * } X$ , that $( i , t ) \mapsto  { \mathrm { e } } ^ { t \mathrm { H } _ { f } } ( i )$ defines a smooth immersion from an open subset J of $I \times \mathbf { R }$ to $\mathrm { T } ^ { * } X$ , and that the image is a smoothly immersed Lagrange submanifold Λ of $\mathrm { T } ^ { * } X$ such that $\Lambda \subset N$ , where N denotes the zeroset of f in $\mathrm { T } ^ { * } X$ . Verify that the the projections in X of the Hf -solution curves in Λ all pass through the given point x. This is called the ray bundle emanating from x, for a general function f on $\mathrm { T } ^ { * } X$

## References

[1] V.I. Arnol’d: Characteristic class entering in quantization condition. Func. Anal. Appl. 1 (1967) 1–13.

[2] N. Burgoyne and R. Cushman: Conjugacy classes in linear groups. J. Algebra 44 (1977) 339– 362.

[3] E.A. Coddington and N. Levinson: Theory of Ordinary Differential Equations. McGraw-Hill Book Company, Inc., New York, etc., 1955.

[4] R. Cushman and J.J. Duistermaat: The behavior of the index of a periodic linear hamiltonian system under iteration. Advances in Math. 23 (1977) 1–21.

[5] J.J. Duistermaat and L. H¨ormander: Fourier integral operators II. Acta Math. 128 (1972) 183–269.

[6] J.J. Duistermaat: Osicllatory integrals, Lagrange immersions and unfoldings of singularities. Comm. Pure Appl. Math. 27 (1974) 207–281.

[7] F. Engel und K. Faber: Die Liesche Theorie der partiellen Differentialgleichungen Erster Ordnung. Teubner, Berlin, 1935.

[8] A. Fresnel: M´emoire sur la diffraction de la lumi\`ere, couronn´e par l’Acad´emie des Sciences en 1819. pp. 247–382 in vol. 1 of: Œuvres Compl\`etes d’Augustin Fresnel. Paris, 1866. Johnson Reprint Corporation, New York, 1965.

[9] P. Griffiths and J. Harris: Principles of Algebraic Geometry. John Wiley and Sons, New York, etc,. 1978.

[10] W.R. Hamilton: Essay on the theory of systems of rays, with three supplements. Trans. Royal Irish Acad. 15 (1828) 69–174, 16 (1830 and 1831) 4–62 and 85–92, 17 (1837) 1–144.

[11] W.R. Hamilton: On a general method in dynamics. Phil. Trans. Royal Soc. London (1834) 247–308, (1835) 95–144.

[12] R. Harvey and H.B. Lawson, Jr.: Calibrated geometries. Acta Math. 148 (1982) 47–157.

[13] L. H¨ormander: An Introduction to Complex Analysis in Several Variables. North-Holland Publ. Co., Amsterdam, 1973.

[14] L. H¨ormander: Fourier integral operators I. Acta Math. 127 (1971) 79–183.

[15] C. Huygens: Trait´e de la Lumi\`ere. Van der Aa, Leyden, 1690.

[16] C.G.J. Jacobi: Uber die Reduction der Integration der partiellen Differentialgleichungen er- ¨ ster ordnung zwischen irgend einer Zahl Variabeln auf die Integration eines einzigen Systemes gew¨ohnlicher Differentialgelichungen. Crelle’s Journal f¨ur die reine und angewandte Mathematik 1 (8137) 97–162 = Gesammelte Werke, 4. Band, 1886. Reprint Chelsea Publ. Cy., New York, 1969.

[17] C.G.J. Jacobi: Vorlesungen ¨uber Dynamik. Gehalten an der Universit¨at K¨onigsberg im Wintersemester 1842–43 und nach einem von C.W. Borchardt ausgearbeiteten Hefte. Verlag G. Reimer, Berlin, 1881. Reprint Chelsea Publ. Cy., New York, 1969.

[18] C.G.J. Jacobi: Nova methodus, equationes differentiales partiales primi orins inter numerum variabilium quemcuque propositas integrandi. Crelle journal f¨ur die reine und angewandte Mathematik 60 (1862) 1–181. Also in: Gesammelte Werke, V. Band, 1–189., Berlin 1890. Reprint Chelsea Publ. Cy., New York, 1969.

[19] J.-L. Lagrange: M´ecanique Analytique. First print 1788 in Paris. Reprint by A. Blanchard, Paris, 1965.

[20] A. Lichnerowicz: Les vari´et´es de Poisson et leurs alg\`ebres de Lie associ´ees. J. Differential Geometry 12 (1977) 253–300.

[21] S. Lie: Theorie der Transformationsgruppen I–III. Unter Mitwirkung von Prof.dr. F. Engel. Teubner, Leipzig, 1888, 1890, 1893.

[22] B. Malgrange: Sur l’integrabilit´e des structures presques-complexes. pp. 289-296 in: Symposia Mathematica II, INDAM, Rome, 1968.

[23] V.P. Maslov: Th´eorie des Perturbations et M´ethodes Asymptotiques. Dunod, Gauthier-Villars, Paris, 1972. This is a French translation of the book published in 1965 by the University of Moscow, with some additions.

[24] J. Moser: On the volume elements on a manifold. Trans. Amer. Math. Soc. 120 (1965) 286–294.

[25] A. Newlander and L. Nirenberg: Complex analytic coordinates in an almost complex manifold. Annals of Math. 65 (1957) 391–404.

[26] Julius Pl¨ucker: Neue Geometrie des Raumes, gegr¨undet auf die Betrachtung der gerade Linie als Raumelement. Teubner Verlag, Leipzig, 1868/89.

[27] A. Weinstein: Symplectic manifolds and their Lagrangian submanifolds. Advances in Mathematics 6 (1971) 329–346.

[28] A. Weinstein: Symplectic geometry. Bull. Amer. Math. Soc. 5 (1981) 1–13.

[29] Hermann Weyl: The Classical Groups, their invariants and representations. Princeton University Press, Princeton, N.J., 1939, 1946.

[30] John Williamson: On the algebraic problem concerning normal forms of linear dynamical systems. Amer. J. Math. 58 (1936) 141–163.
