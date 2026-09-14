# Qualifying Exam in Algebra, Winter 2018

Part I. True or false. Justify your answer by giving a proof or counterexample. 10 points each.

1. The extension $\mathbb { Q } ( { \sqrt { 2 + { \sqrt { 2 } } } } ) / \mathbb { Q }$ is normal.

Answer: TRUE. Let $\alpha = \sqrt { 2 + \sqrt { 2 } } ;$ it is a root of polynomial $( x ^ { 2 } - 2 ) ^ { 2 } =$ 2. Other roots are $\pm { \sqrt { 2 \pm { \sqrt { 2 } } } } ;$ note that $\sqrt { 2 - \sqrt { 2 } } \alpha = \sqrt { 2 } = \alpha ^ { 2 } - 2$ , that is $\textstyle { \sqrt { 2 - { \sqrt { 2 } } } } = { \frac { \alpha ^ { 2 } - 2 } { \alpha } }$ . Thus all the roots of $( x ^ { 2 } - 2 ) ^ { 2 } = 2$ are contained in $\mathbb { Q } ( \alpha )$ , so $\mathbb { Q } ( \alpha ) / \mathbb { Q }$ is a splitting field of this polynomial. Hence this is a normal extension.

2. Let $U _ { n } ( \mathbb { C } )$ be the ring of upper triangular $n \times n$ matrices with entries in C. Any irreducible $U _ { n } ( \mathbb { C } )$ −module is one dimensional over C.

Answer: TRUE. We have a homomorphism $U _ { n } ( \mathbb { C } ) \to \mathbb { C } \oplus \dots \oplus \mathbb { C }$ sending a matrix to its diagonal. The kernel of this homomorphism consists of strictly upper triangular matrices, so it is nilpotent and is contained in the Jacobson radical of $U _ { n } ( \mathbb { C } )$ (in fact its coincides with the Jacobson radical). Since the Jacobson radical acts by zero on an irreducible module we see that any irreducible $U _ { n } ( \mathbb { C } )$ −module is a pullback of irreducible $\mathbb { C } \oplus \cdots \oplus \mathbb { C } .$ −module. It is clear that any irreducible module over the latter algebra is 1-dimensional (since this algebra is commutative or by the classification of simple modules over semisimple rings).

3. The abelian group $\mathbb { Q } / \mathbb { Z }$ is flat.

Answer: FALSE. Consider the map $\mathbb { Z } \to \mathbb { Z }$ given by multiplication by 2. It is injective. If $\mathbb { Q } / \mathbb { Z }$ were flat, tensoring by $\mathbb { Q } / \mathbb { Z }$ would preserve injections, so the map $\mathbb { Q } / \mathbb { Z } \to \mathbb { Q } / \mathbb { Z }$ given by multiplication by 2 would be injective too. But for example the coset of $1 / 2$ goes to zero so it is not.

4. A $\mathbb { C } [ x , y ] .$ −module is semisimple if and only if its restrictions to both of the subalgebras $\mathbb { C } [ x ]$ and $\mathbb { C } [ y ]$ are semisimple.

Answer: TRUE. Let M be a semisimple $\mathbb { C } [ x , y ] { \mathrm { - m o d u l e } }$ Then it is a direct sum of irreducible $\mathbb { C } [ x , y ] .$ −modules which are 1-dimensional over C (since by Nullstellensatz any maximal ideal of $\mathbb { C } [ x , y ]$ is of codimension 1). Thus the restriction of M to any C−subalgebra is a direct sum of 1-dimensional modules, hence semisimple.

Conversely assume the restrictions of M to $\mathbb { C } [ x ]$ and $\mathbb { C } [ y ]$ are semisimple. Then $\begin{array} { r } { M \ = \ \sum _ { a \in \mathbb { C } } M _ { a } } \end{array}$ where $M _ { a } \ = \ \{ m \ \in \ M | x m \ = \ a m \}$ since $M _ { a }$ is a sum of all $\mathbb { C } [ x ]$ −submodules of M isomorphic to simple module $\mathbb { C } [ x ] / ( x - a )$ . It is clear that each $M _ { a }$ is $\mathbb { C } [ y ]$ −submodule of $M$ . Thus $M _ { a }$ decomposes into a sum of irreducible hence 1-dimensional C[y]−modules. Any such summand of $M _ { a }$ is clearly $\mathbb { C } [ x , y ]$ −submodule of M. Thus M is a sum of 1-dimensional hence irreducible $\mathbb { C } [ x , y ]$ −modules, hence it is semisimple.

5. The cyclotomic polynomial $\Phi _ { 2 5 5 } ( x )$ reduced modulo 2 is irreducible as an element of $\mathbb { F } _ { 2 } [ x ]$

Answer: FALSE. The polynomial $\Phi _ { 2 5 5 } ( x )$ is a divisor of $x ^ { 2 5 5 } - 1$ (both over Z and over $\mathbb { F } _ { 2 } )$ . Thus any root α of $\Phi _ { 2 5 5 } ( x )$ satisfies $\alpha ^ { 2 5 5 } = 1$ whence $\alpha ^ { 2 5 6 } = \alpha$ . Thus α is contained in $\mathbb { F } _ { 2 5 6 }$ which is the splitting field of $x ^ { 2 5 6 } - x$ over $\mathbb { F } _ { 2 }$ . Since $[ \mathbb { F } _ { 2 5 6 } : \mathbb { F } _ { 2 } ] = 8 .$ , the degree of the minimal polynomial of α over $\mathbb { F } _ { 2 }$ is $\leq 8$ . Thus $\Phi _ { 2 5 5 } ( x )$ is not irreducible as its degree $\phi ( 2 5 5 ) = 2 \cdot 4 \cdot 1 6 = 1 2 8 > 8$

Part II. Longer problems. 10 points each.

1. Describe all proper subgroups of the symmetric groups $S _ { n }$ of order strictly more than $( n - 1 ) !$

Solution: Let $H \subset S _ { n }$ be a proper subgroup with $| H | > ( n - 1 ) !$ . The group $S _ { n }$ then acts transitively (hence nontrivially) on the set of cosets $S _ { n } / H$ of size $m = | S _ { n } : H | < n$ . Thus we have a nontrivial homomorphism $S _ { n }  S _ { m }$ and its restriction to the alternating group $A _ { n } \to S _ { m }$ . The latter homomorphism must be trivial for $n \geq 5$ since the alternating group is simple and $\left| A _ { n } \right| = \textstyle { \frac { 1 } { 2 } } n ! > m ! = \left| S _ { m } \right|$ Thus the action factors through $S _ { n } / A _ { n } = \mathbb { Z } / 2 \mathbb { Z }$ and its orbit $S _ { n } \bar { / } H$ is of size $\leq 2$ Thus $H = A _ { n }$ since $A _ { n }$ is a unique subgroup of index 2 in $S _ { n }$

It remains to consider the cases when $n \leq 4$ . The cases $n = 1 , 2 , 3$ are trivial with a unique possibility $H = A _ { 3 } \subset S _ { 3 }$ . In the case $n = 4$ the index of H must be 2 or 3; if the index is 2 then the subgroup is $A _ { 4 } \subset S _ { 4 }$ . If the index is 3 then $| H | = 8$ and H is Sylow 2-subgroup of $S _ { 4 }$ . There are precisely 3 such subgroups.

Answer: Such subgroup is either the alternating group $A _ { n } \subset S _ { n }$ for $n \geq 3$ or one of three Sylow 2-subgroups of $S _ { 4 }$

2. Let G be a finite group and let $H \subset G$ be a subgroup. Let $g \in G$ be an element such that no conjugate of $g$ is contained in H. Prove that for any finite dimensional H−module V (over an arbitrary field) the trace of g in ${ \mathrm { I n d } } _ { H } ^ { G } V$ is zero.

Solution: Let $g _ { 1 } , \ldots , g _ { n }$ be $G / H$ coset representatives. Let $v _ { 1 } , \ldots , v _ { m }$ be a basis for V . Then $g _ { i } \otimes v _ { j }$ is a basis for the induced module. To compute the trace of $^ { g , }$ act on this basis. Say $g g _ { i } = g _ { k } h$ for $h \in H$ . Then $g ( g _ { i } \otimes v _ { j } ) = g _ { k } \otimes h v _ { j }$ . The diagonal entry of the matrix of $g$ in the basis above is the coefficient of $g _ { i } \otimes v _ { j }$ in the expansion of $g ( g _ { i } \otimes v _ { j } )$ . Thus to give a non-zero contribution to the trace, we must have that $k = i$ . But then $g g _ { i } = g _ { i } h$ contradicting the hypothesis on $g .$

3. For a partially ordered set $( X , \leq )$ , let $\mathcal { C } _ { X }$ be the corresponding category: the objects of $\mathcal { C } _ { X }$ are the elements of X and there is a unique morphism $\theta : x \mapsto y$ if and only if $x \leq y$ . For an order preserving map $f : X \to Y$ , let $F _ { f } : { \mathcal { C } } _ { X } \to { \mathcal { C } } _ { Y }$ be the corresponding functor. Viewing Z and R as partially ordered sets via the usual ordering ≤, the obvious embedding $i : \mathbb { Z } \to \mathbb { R }$ is an order preserving map. Find the right and left adjoints of the functor $F _ { i } : { \mathcal { C } } _ { \mathbb { Z } } \to { \mathcal { C } } _ { \mathbb { R } }$ , justifying your answer carefully.

Solution: Let $G : { \mathcal { C } } _ { \mathbb { R } } \to { \mathcal { C } } _ { \mathbb { Z } }$ be the left adjoint functor of $F _ { i }$ . Thus we must have a bijection Hom $( G x , m )$ ↔ Hom(x, Fim) for all $x \in \mathbb { R } , m \in \mathbb { Z }$ . Thus

$$
G x \leq m \Leftrightarrow \operatorname { H o m } ( G x , m ) \neq \varnothing \Leftrightarrow \operatorname { H o m } ( x , F _ { i } m ) \neq \varnothing \Leftrightarrow x \leq m \Leftrightarrow \left[ x \right] \leq m ,
$$

where $\lceil \begin{array} { l } { } \end{array} \rceil : \mathbb { R }  \mathbb { Z }$ is the ceiling function. Notice that this function is order preserving. Thus it is natural to expect that $G = F _ { \harpoonright }$ This is indeed the case:

we have a unique bijection Hom $( F _ { \lceil \mathit { \rceil } } x , m )  \mathrm { H o m } ( x , F _ { i } m )$ since both sets have the same cardinality which $\mathrm { i s } \leq 1$ . This bijection is natural in both variables as all the Hom−sets in the naturality diagram are of cardinality $\leq 1$ , so it must be commutative.

Similarly, the right adjoint functor of $F _ { i }$ is $F _ { \lfloor \rfloor }$ where $\lfloor \rfloor : \mathbb { R } \to \mathbb { Z }$ is the floor function. Here is a cheap way to see this: observe that the map $x \mapsto - x$ gives an equivalence to opposite categories (coming from opposite posets) and note that $\lfloor x \rfloor = - \lceil - x \rceil$

4. Let $I \triangleleft \mathbb { C } [ x _ { 1 } , \ldots , x _ { n } ]$ be an ideal such that $\sqrt { I }$ is maximal. Prove that $\mathbb { C } [ x _ { 1 } , \ldots , x _ { n } ] / I$ is finite dimensional over C.

Solution: Let ${ \sqrt { I } } = \left( x _ { 1 } - c _ { 1 } , \ldots , x _ { n } - c _ { n } \right)$ for $( c _ { 1 } , \ldots , c _ { n } ) \in \mathbb { C } ^ { n }$ . The monomials $\textstyle \prod _ { i = 1 } ^ { n } ( x _ { i } - c _ { i } ) ^ { m _ { i } }$ with $m _ { i } ~ \in ~ \mathbb { Z } _ { \geq 0 }$ form a basis of $\mathbb { C } [ x _ { 1 } , \ldots , x _ { n } ]$ (e.g. apply the automorphism $x _ { i } \mapsto x _ { i } - c _ { i }$ to the standard monomial basis of $\mathbb { C } [ x _ { 1 } , \dots , x _ { n } ]$ . By definition of ${ \sqrt { I } } ,$ for any $i = 1 , \ldots , n$ there is $n _ { i } \in \mathbb { Z } _ { > 0 }$ such that $( x _ { i } - c _ { i } ) ^ { n _ { i } } \in I .$ Thus the monomials $\textstyle \prod _ { i = 1 } ^ { n } ( x _ { i } - c _ { i } ) ^ { m _ { i } }$ with $0 \leq m _ { i } < n _ { i }$ for all i span $\mathbb { C } [ x _ { 1 } , \ldots , x _ { n } ] / I$ Hence $\mathbb { C } [ x _ { 1 } , \ldots , x _ { n } ] / I$ is finite dimensional of dimension $\leq \prod _ { i = 1 } ^ { n } n _ { i }$

5. Let V be a finite dimensional vector space over a field F , and let $f : V \to V$ be a linear transformation. Prove that $\operatorname { 2 t r } ( { \bar { S } } ^ { 2 } f ) = \operatorname { t r } ( f ) ^ { 2 } + \operatorname { t r } ( f ^ { 2 } )$ .

Solution: As the extension of the field does not change the traces we can and will assume that F is algebraically closed. Pick a basis $v _ { 1 } , . . , v _ { n }$ with respect to which $f$ is upper triangular with $\lambda _ { 1 } , \ldots , \lambda _ { n }$ on the diagonal (e.g. Jordan normal form basis would work). Then $v _ { i } v _ { j }$ with $i \leq j$ is a basis for ${ \dot { S } } ^ { 2 } V$ and the matrix of $S ^ { 2 } f$ has $\lambda _ { i } \lambda _ { j }$ on its diagonal. We deduce that $\begin{array} { r } { 2 \mathrm { t r } ( S ^ { 2 } f ) = 2 \sum _ { i < j } \lambda _ { i } \lambda _ { j } } \end{array}$ . On the other hand $\begin{array} { r } { ( \mathrm { t r } ( f ) ) ^ { 2 } + \mathrm { t r } ( f ^ { 2 } ) = \sum \lambda _ { i } ^ { 2 } + 2 \sum _ { i < j } \lambda _ { i } \lambda _ { j } + \sum \lambda _ { i } ^ { 2 } } \end{array}$ . The result follows.