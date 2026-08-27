## Week 5: Abstract Algebra & Complex Analysis Practice Problem Solutions

Problem 1. Suppose G is a group and $x \in G$ is only element in G of order 2. Show that $x a = a x$ for all $a \in G .$

Solution. Note that for any $a \in G .$ , we have

$$
( a x a ^ { - 1 } ) ^ { 2 } = a x a ^ { - 1 } a x a ^ { - 1 } = a x ^ { 2 } a ^ { - 1 } = a a ^ { - 1 } = e .
$$

This shows that $a x a ^ { - 1 }$ has order 2. But if x is the unique element of order 2, this means $a x a ^ { - 1 } = x \implies$ $a x = x a$

Problem 2. What is the units digit of $2 0 1 9 ^ { 2 0 1 9 } ?$

Solution. Consider the multiplicative group $\mathbb { Z } _ { 1 0 } ^ { * } = \{ 1 , 3 , 7 , 9 \}$ . In this group 2019 = 9. And we note that $9 ^ { 2 } = 1$ . Thus the units digit of $2 0 1 9 ^ { 2 0 1 9 }$ is given by

$$
2 0 1 9 ^ { 2 0 1 9 } ( { \mathrm { m o d ~ } } 1 0 ) = 9 ^ { 2 0 1 9 } ( { \mathrm { m o d ~ } } 1 0 ) = ( 9 ^ { 2 } ) ^ { 1 0 0 9 } \cdot 9 ( { \mathrm { m o d ~ } } 1 0 ) = 9 ( { \mathrm { m o d ~ } } 1 0 ) .
$$

So the answer is 9.

Problem 3. The continuous functions on [0, 1] form a ring under pointwise addition and pointwise multiplication. Show that this ring is not an integral domain.

Solution. To show that a ring is not an integral domain, one must exhibit two nonzero elements which multiply to zero. Here, let $f ( x ) = \operatorname* { m i n } \{ { \textstyle { \frac { 1 } { 2 } } } - x , 0 \}$ and $g ( x ) = \mathrm { m i n } \{ 0 , x - \textstyle { \frac { 1 } { 2 } } \}$ . Then $f ( x ) = 0 { \mathrm { ~ f o r ~ } } x \in [ 1 / 2 , 1 ]$ and $g ( x ) = 0$ for $x \in [ 0 , 1 / 2 ]$ so $f ( x ) g ( x ) \overline { { \equiv } } 0$ , while neither f nor g is the zero function.

Problem 4. Find all homomorphisms $\phi : U _ { 4 } \to U _ { 4 }$ where $U _ { 4 } = \{ 1 , i , - 1 , - i \}$

Solution. A homomorphism whose source space is cyclic is completely determined by the value it gives to a generator. Here a generator is i, so there are 4 homomorphisms:

1. $\phi ( x ) = 1$ for all $x \in U _ { 4 }$ (this homomorphism corresponds to $\phi ( i ) = 1 )$ ,

2. $\phi ( x ) = x$ for all $x \in U _ { 4 }$ (this homomorphism corresponds to $\phi ( i ) = i )$

3. $\phi ( x ) = - x$ for all $x \in U _ { 4 }$ (this homomorphism corresponds to $\phi ( i ) = - i )$

4. $\phi ( x ) = x ^ { 2 }$ for all $x \in U _ { 4 }$ (this homomorphism corresponds to $\phi ( i ) = - 1 )$

Problem 5. Classify all abelian groups of order 600 (up to isomorphism).

Solution. This is the classic problem requiring the fundamental theorem of finitely generated abelian groups. The answer will be the number of ways we can break 600 into a product of integers $m _ { 1 } , m _ { 2 } , \ldots , m _ { k }$ such that $m _ { 1 } \leq m _ { 2 } \leq \cdot \cdot \cdot \leq m _ { k }$ and $m _ { i } | m _ { i + 1 }$ or into a product of powers primes $p _ { 1 } ^ { k _ { 1 } } , \ldots , p _ { \ell } ^ { k _ { \ell } }$ where neither the primes nor the powers need to be distinct. To explicitly find the groups, notice:

$$
1 . \ 6 0 0 = 2 \cdot 1 0 \cdot 3 0
$$

$$
1 . ~ 6 0 0 = 2 \cdot 2 \cdot 2 \cdot 3 \cdot 5 \cdot 5
$$

$$
2 . \ 6 0 0 = 1 0 \cdot 6 0
$$

$$
\mathrm { 2 . ~ 6 0 0 = 2 \cdot 2 ^ { 2 } \cdot 3 \cdot 5 \cdot 5 }
$$

$$
3 . \ 6 0 0 = 5 \cdot 1 2 0
$$

$$
3 . \ 6 0 0 = 2 ^ { 3 } \cdot 3 \cdot 5 \cdot 5
$$

$$
4 . \ 6 0 0 = 2 \cdot 2 \cdot 1 5 0
$$

$$
4 . \ 6 0 0 = 2 \cdot 2 \cdot 2 \cdot 3 \cdot 5 ^ { 2 }
$$

$$
5 . \ 6 0 0 = 2 \cdot 3 0 0
$$

$$
5 . \ 6 0 0 = 2 \cdot 2 ^ { 2 } \cdot 3 \cdot 5 ^ { 2 }
$$

$$
6 . \ 6 0 0 = 6 0 0
$$

$$
6 . \ 6 0 0 = 2 ^ { 3 } \cdot 3 \cdot 5
$$

Thus the six groups are:

$$
1 . \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 1 0 } \times \mathbb { Z } _ { 3 0 } \cong \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 3 } \times \mathbb { Z } _ { 5 } \times \mathbb { Z } _ { 5 }
$$

$$
2 . \ \mathbb { Z } _ { 1 0 } \times \mathbb { Z } _ { 6 0 } \cong \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 ^ { 2 } } \times \mathbb { Z } _ { 3 } \times \mathbb { Z } _ { 5 } \times \mathbb { Z } _ { 5 }
$$

$$
3 . \ \mathbb { Z } _ { 5 } \times \mathbb { Z } _ { 1 2 0 } \cong \mathbb { Z } _ { 2 ^ { 3 } } \times \mathbb { Z } _ { 3 } \times \mathbb { Z } _ { 5 } \times \mathbb { Z } _ { 5 }
$$

$$
4 . \ \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 1 5 0 } \cong \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 3 } \times \mathbb { Z } _ { 5 ^ { 2 } }
$$

$$
{ \bf 5 . ~ } \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 3 0 0 } \cong \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 ^ { 2 } } \times \mathbb { Z } _ { 3 } \times \mathbb { Z } _ { 5 ^ { 2 } }
$$

$$
6 . \ \mathbb { Z } _ { 6 0 0 } \cong \mathbb { Z } _ { 2 ^ { 3 } } \times \mathbb { Z } _ { 3 } \times \mathbb { Z } _ { 5 ^ { 2 } }
$$

Problem 6. Up to isomorphism, how many abelian groups G have order 16 and satisfy $x + x + x + x = 0$ for all $x \in G ?$

Solution. Abelian groups of order 16 are isomorphic to one of

$$
\mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 } , \qquad \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 4 } , \qquad \mathbb { Z } _ { 4 } \times \mathbb { Z } _ { 4 } , \qquad \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 8 } , \qquad \mathbb { Z } _ { 1 6 } .
$$

If $4 x = 0$ for all $x \in G$ , then G has no element of order higher than 4, meaning there is no factor $\mathbb { Z } _ { n }$ for n higher than 4. Thus there are only three possibilities.

Problem 7. Show that a group is never the union of two of its proper subgroups. Show by example that a group can be the union of three of its proper subgroups.

Solution. Suppose that $A , B \leq G$ are proper subgroups of G and $A \neq B$ . If $A \leq B$ , then $A \cup B = B \neq G$ and we are done. Hence we need only consider the case when $A \not \leq B$ and, by symmetry, we may also assume that $B \not \leq A .$ Then there is $a \in A$ with $a \notin B$ and there is $b \in B$ with $b \not \in A$ . The element ab is contained in G, but is in neither A nor B. Indeed, since $a \in A$ , we know $a ^ { - 1 } \in A$ Thus if $a b \in A .$ we would also have $a ^ { - 1 } a b = b \in A$ , but b was selected such that $b \not \in A .$ , and thus we must conclude that ab $\not \in A .$ Likewise, $a b \notin B$ and so ab 6∈ $A \cup B$ and we conclude that $A \cup B \neq G$ . [Note: there is a much easier proof of this fact if G is a finite group: in that case, $\left| A \right| , \left| B \right| \leq \left| G \right| / 2$ by Lagrange’s theorem. But then since A, B both contain the identity, we have $| A \cup B | \leq | G | - 1 . ]$ The Klein-4 groups is a union of three of its proper subgroups. Indeed, if $\{ e , a , b , c \}$ is the Klein-4 group (so that $a ^ { 2 } = b ^ { 2 } = c ^ { 2 } = e$ , then we can write

$$
\{ e , a , b , c \} = \{ e , a \} \cup \{ e , b \} \cup \{ e , c \} .
$$

Problem 8. Let G be a group and define $\operatorname { A u t } ( G )$ to be the set of all isomorphisms of G to itself. Prove that $\operatorname { A u t } ( G )$ is a group under the operation of functional composition. For each $g \in G ,$ , define the map, $\phi _ { g } ( x ) = g x g ^ { - 1 }$ for $x \in G$ and let Inn $( G ) = \{ \phi _ { g } : g \in G \}$ . Show that Inn(G) is a subgroup of Aut(G). What does Inn(G) look like if G is abelian?

Solution. If $\phi , \psi \in \operatorname { A u t } ( G )$ , we must show that φ $\circ \psi \in \operatorname { A u t } ( G )$ . Indeed, if $x , y \in G x \neq y$ , then $\psi ( x ) \neq \psi ( y )$ since ψ is injective, and thys $( \phi \circ \psi ) ( x ) \neq ( \phi \circ \psi ) ( y )$ since φ is injective. This shows that $\phi \circ \psi$ is injective.

Likewise, for any $y \in G ,$ , there is $y ^ { \prime } \in G$ such that $\phi ( y ^ { \prime } ) = y$ since φ is surjective. But then there is $x \in G$ such that $\psi ( x ) = y ^ { \prime }$ since ψ is surjective. Then $( \phi \circ \psi ) ( x ) = y$ and so $\phi \circ \psi$ is surjective as well. Finally, since both ψ and φ respect group operations, we see

$$
( \phi \circ \phi ) ( x y ) = \phi ( \psi ( x y ) ) = \phi ( \psi ( x ) \psi ( y ) ) = \phi ( \psi ( x ) ) \phi ( \psi ( y ) ) = ( \phi \circ \psi ) ( x ) ( \phi \circ \psi ) ( y )
$$

for all $x , y \in G$ Thus φ $\circ \psi \in \operatorname { A u t } ( G )$ so $\operatorname { A u t } ( G )$ is closed under functional composition. The function $\iota : G  G$ defined by $\iota ( x ) = x$ for all $x \in G$ will serve as the identity isomorphism since $\iota \circ \phi = \phi \circ \iota$ for any $\phi \in \operatorname { A u t } ( G )$ , and if $\phi \in \operatorname { A u t } ( G )$ , the map $\phi ^ { - 1 } : G \to G$ defined by $\phi ^ { - 1 } ( x ) = y { \mathrm { ~ i f f ~ } } \phi ( y ) = x ,$ for $x , y \in G$ provides an inverse for φ. Lastly, functional composition is associative and we conclude that $\operatorname { A u t } ( G )$ is a group.

If $\phi , \psi \in \operatorname { I n n } ( G )$ , then there are $x , y \in G$ such that

$$
\phi ( g ) = x g x ^ { - 1 } , \quad \psi ( g ) = y g y ^ { - 1 } , \quad { \mathrm { ~ f o r ~ a l l ~ } } g \in G .
$$

It is easy to see that $\psi ^ { - 1 } ( g ) = y ^ { - 1 } g y$ for all $g \in G$ , and thus

$$
( \phi \circ \psi ^ { - 1 } ) ( g ) = x y ^ { - 1 } g y x ^ { - 1 } = x y ^ { - 1 } g ( x y ^ { - 1 } ) ^ { - 1 } = z g z ^ { - 1 } , \quad { \mathrm { ~ f o r ~ a l l ~ } } g \in G
$$

where $z = x y ^ { - 1 }$ This shows that $\phi \circ \psi ^ { - 1 } \in \operatorname { I n n } ( G )$ and since $\iota \in \operatorname { I n n } ( G )$ , we conclude that Inn(G) is a subgroup of $\operatorname { A u t } ( G )$ by the subgroup test. If G is abelian, then the only inner automorphism is the identity map since $x g x ^ { - 1 } = g$ for all $x , g \in G$

Problem 9. Suppose that a group has an element of order 7 but no element which is its own inverse (other than the identity). Which of the following is a possible order for this group?

$$
\mathrm { ( a ) ~ 2 7 ~ \phantom { - } ( b ) ~ 2 8 ~ \phantom { - } ( c ) ~ 3 5 ~ \phantom { - } ( d ) ~ 3 7 }\tag{e) 42}
$$

Solution. By Lagrange’s theorem, the order must be divisible by 7. If the order was divisible by 2, then by Cauchy’s theorem there would be a subgroup of order 2 (and hence an element of order 2) but the question specifies that no element is its own inverse and so the order cannot be divisible by 2. Thus the answer is (c) 35.

Problem 10. Suppose that subgroups H and K of some group have order 12 and 30 repectively. Which cannot be the order of the subgroup generated by H and K?

$$
\mathrm { ( a ) ~ 3 0 ~ ( b ) ~ 6 0 ~ ( c ) ~ 1 2 0 }\tag{d) 360 (e}
$$

Solution. We have the natural inclusions

$$
H , K \le [ H , K ]
$$

where $[ H , K ]$ is the subgroup generated by H and K. By Lagrange’s theorem this shows that $| H | \mid | [ H , K ] |$ and $| K | | | [ H , K ] |$ and so the order cannot be 30 since 12 doesn’t divide 30.

It is puzzling to some students that the order of the group generated by two finite groups could be infinite. But indeed this is possible. As an example, consider $\operatorname { S y m } ( \mathbb { Z } ) = \{ f : \mathbb { Z } \to \mathbb { Z } : f$ bijective} under functional composition and let $\iota : \mathbb { Z } \to \mathbb { Z }$ denote the identity map which is the identity element in this group: $\iota ( n ) = n$ for all $n \in \mathbb { Z }$ . This is a group and the maps

$$
f ( n ) = { \left\{ \begin{array} { l l } { n + 1 , } & { n { \mathrm { ~ o d d } } , } \\ { n - 1 , } & { n { \mathrm { ~ e v e n } } , } \end{array} \right. }
$$

and

$$
g ( n ) = { \left\{ \begin{array} { l l } { n - 1 , } & { n { \mathrm { ~ o d d } } , } \\ { n + 1 , } & { n { \mathrm { ~ e v e n } } . } \end{array} \right. }
$$

For any $n \in \mathbb { Z } , { \mathrm { i f ~ } } \cdot$ n is odd then $n + 1$ is even and $( f \circ f ) ( n ) = f ( f ( n ) ) = f ( n + 1 ) = ( n + 1 ) - 1 = n$ , and if n is even then $n - 1$ is odd and $( f \circ f ) ( n ) = f ( f ( n ) ) = f ( n - 1 ) = ( n - 1 ) + 1 = n$ . Thus $f ^ { 2 } = \iota$ and so

$F = \{ \iota , f \} \leq \operatorname { S y m } ( \mathbb { Z } )$ . The same holds for g and so $G = \{ \iota , g \} \leq \mathrm { S y m } ( \mathbb { Z } )$ . However, the element $g \circ f$ lies in the generated group $[ F , G ]$ , and

$$
( g \circ f ) ( n ) = { \left\{ \begin{array} { l l } { n + 2 , } & { n { \mathrm { ~ o d d , ~ } } } \\ { n - 2 , } & { n { \mathrm { ~ e v e n , } } } \end{array} \right. }
$$

and this element satifies

$$
( g \circ f ) ^ { k } ( n ) = { \left\{ \begin{array} { l l } { n + 2 k , } & { n { \mathrm { ~ o d d , ~ } } } \\ { n - 2 k , } & { n { \mathrm { ~ e v e n , ~ } } } \end{array} \right. }
$$

for any $k \in \mathbb N$ and thus has infinite order since $( g \circ f ) ^ { k } \neq \iota$ for any $k \in \mathbb N$ . Thus the two finite groups $F , G$ have generated an infinite group $[ F , G ]$

Problem 11. Let G be a group and $H \subset G$ be a subgroup. H is said to be a normal subgroup of G if $g h g ^ { - 1 } \in H$ whenever $h \in H$ and $g \in G$ . If $\phi : G \to G ^ { \prime }$ is a homomorphism (where $G ^ { \prime }$ is some other arbitrary group), show that ker φ is a normal subgroup of G.

Solution. First, the identity $e \in G$ is always in ker φ and if $x , y \in$ ker $\phi$ , then $\phi ( x y ^ { - 1 } ) = \phi ( x ) \phi ( y ^ { - 1 } ) =$ $\phi ( x ) \phi ( y ) ^ { - 1 } = e ^ { \prime } ( e ^ { \prime } ) ^ { - 1 } = e ^ { \prime }$ where $e ^ { \prime } \in G ^ { \prime }$ is the identity in $G ^ { \prime }$ . This shows that ker φ is a subgroup of G by the subgroup test. Next, for any $g \in G$ and any $h \in$ ker φ, we see that

$$
\phi ( g h g ^ { - 1 } ) = \phi ( g ) \phi ( h ) \phi ( g ) ^ { - 1 } = \phi ( g ) \phi ( g ) ^ { - 1 } = e ^ { \prime }
$$

which shows that $g h g ^ { - 1 } \in \ker \phi .$ Hence ker φ is a normal subgroup of G. [Note: normal subgroups H of a group $G$ are those subgroups for which we can define a quotion group $G / H$ The fact that ker φ is a normal subgroup is then key in the First Isomorphism Theorem which tells us that if $\phi : G \to G ^ { \prime }$ is a surjective homomorphism, then $G ^ { \prime }$ is canonically isomorphic to $G / \mathrm { k e r } \phi . ]$

Problem 12. Let R be a ring with unity. A set $I \subset R$ is said to be a right ideal of $R \operatorname { i f } \left( I , + \right)$ is a subgroup of $( R , + )$ and $x r \in I$ whenever $x \in I$ and $r \in R .$ Suppose R has exactly two distinct right ideals. Show that every element in R has a multiplicative inverse (except for the additive identity).

Solution. The two distinct right ideals must be {0} and R itself. For any $r ~ \in ~ R$ consider the set $I _ { r } = \{ r s \ : \ s \in \ R \}$ . This is a right ideal; indeed if $x \in I _ { r }$ , then $x = r s$ for some $s \in R$ . But then for any $y \in R , x y = r s y = r ( s y ) \in I _ { r }$ Thus xy ∈ Ir whenever $x \in I _ { r }$ , and we conclude that $I _ { r }$ is a right ideal. If $r \neq 0 .$ , then $I _ { r } \ne \{ 0 \}$ since $r \in I _ { r } ,$ and thus we must have $I _ { r } = R$ In particular, this means that $1 \in I _ { r }$ and so there is $s \in R$ such that $r s = 1$ . Since $0 \neq 1$ , we know that $s \neq 0 .$ , so using the same logic as above (i.e. considering the ideal $I _ { s } )$ we find that there is $t \in R$ such that $s t = 1$ . But then multiplying on the right by $t ,$ we see $r s = 1 \quad \implies \quad r s t = t \quad \implies \quad r = t$ Thus $s r = r s = 1$ and we conclude that $r$ has a multiplicative inverse. [Note: this is part of a larger fact. An ideal $I \subset R$ is called maximal if for any ideal $J \neq I ,$ we have $I \subset J \implies J = R . \mathrm { ~ A ~ }$ theorem tells us that if we quotient a ring by a maximal ideal, we create a field. Here {0} is a maximal ideal and $R / \{ 0 \} \cong R$ so R must be a field.]

Problem 13. Suppose that $r ^ { 2 } = r$ for all r in a ring R. Show that R is commutative.

Solution. First note that for any $r \in R$

$$
2 r = r + r = ( r + r ) ^ { 2 } = r ^ { 2 } + 2 r + r ^ { 2 } = 4 r \quad \Longrightarrow \quad 2 r = 0 \quad \Longrightarrow \quad r = - r .
$$

Then for any $r , s \in R .$

$$
r + s = ( r + s ) ^ { 2 } = r ^ { 2 } + r s + s r + s ^ { 2 } = r = r s + s r + s \quad \Longrightarrow \quad r s + s r = 0 \quad \Longrightarrow \quad r s = - s r \quad \Longrightarrow \quad r s = s r .
$$

Problem 14. Let $p , q$ be distinct primes. If J is a proper subgroup of $( \mathbb { Z } , + )$ containing exactly three of $\{ p , p + q , p q , p ^ { q } , q ^ { p } \}$ , which three elements does J include?

Solution. The three elements are $p , p q$ and $p ^ { q }$ - these are the ones that can be obtained by repeatedly adding p to itself.

Problem 15. Find all group and ring homomorphisms from $\mathbb { Z } \to \mathbb { Z }$

Solution. Note that any group homomorphism from $\mathbb { Z } \to \mathbb { Z }$ is completely determined by the image of 1 since 1 is a generator. Indeed, if $\phi : \mathbb { Z } \to \mathbb { Z }$ is a group homomorphism, then $\phi ( n ) = n \phi ( 1 )$ and so group homomorphisms have the form $n \mapsto$ kn for some $k \in \mathbb { Z }$

For ring homomorphisms, the function must respect both addition and multiplication. Thus if $\phi : \mathbb { Z } \to \mathbb { Z }$ is a ring homomorphism, then we still have $\phi ( n ) = n \phi ( 1 )$ for all $n \in \mathbb { Z }$ , but now we also have $\phi ( 1 ) =$ $\phi ( 1 \cdot 1 ) = \phi ( 1 ) \cdot \phi ( 1 )$ This shows that $\phi ( 1 ) = 0 ~ \mathrm { o r } ~ \phi ( 1 ) = 1$ Thus the only ring homomorphisms are the trivial homomorphisms: $\phi ( n ) = 0$ for all $n \in \mathbb { Z }$ Z, or $\phi ( n ) = n$ for all $n \in \mathbb { Z }$

Problem 16. Let F be a finite field or order p. How many non-invertible $2 \times 2$ matrices with entries in F have trace 1?

Solution. The matrix $\scriptstyle { \left( \begin{array} { l } { a } \ { b } \\ { c } \end{array} \right) }$ is non-invertible if $a d = b c$ . It has trace 1 if $a + d = 1$ . Once we’ve chosen a, we have also chosen d since $d = 1 - a$ . We break this down into two cases.

Case 1. If $a = 0$ or $a = 1$ , then $b c = 0 .$ Since F has not zero divisors, this means that $b = 0$ or $c = 0$ . If $c = 0 .$ we have p choices for b and if b is zero we have p choices for c, so, since we’ve double counted the case when $b = c = 0$ , there are $2 p - 1$ choices for b, c in this case. Since there were 2 choices for a, this gives $\left| 4 p - 2 \right|$ choices in this case.

Case 2. If $a \not \in \{ 0 , 1 \}$ , then ad $\neq 0 .$ . Thus we must choose $b \neq 0$ and we will have $c = b ^ { - 1 } a d$ . There are $p - 2$ choices for a and $p - 1$ choices for b, giving $\left| { p ^ { 2 } - 3 p + 2 } \right|$ total choices in thics case.

Adding the two cases, the total number of non-invertible matrices with trace 1 is $p ^ { 2 } + p .$

Problem 17. Let G be a non-empty set with a binary operation which is associative and fully cancellative (i.e. $x z = y z \implies x = y$ and $z x = z y \implies x = y$ for all $x , y , z \in G )$ . Further assume that $\{ x ^ { n } : n = 1 , 2 , 3 , \ldots \}$ is finite for all $x \in G$ . Show that G is a group.

Solution. We need to show that there is an identity element, and that each element has an inverse. Take $x \in G$ . Since $\{ x ^ { n } : n = 1 , 2 , 3 , . . . \}$ is finite, there must by n 6= m such that $x ^ { n } = x ^ { m }$ . Without loss of generality, let $n = m + k$ for some $k \in \mathbb N$ . Note that

$$
x ^ { m } x ^ { k + 1 } = x ^ { m + k + 1 } = x ^ { n + 1 } = x ^ { n } x = x ^ { m } x .
$$

Using cancellation, we get $x ^ { k + 1 } = x$ . Now define $e = x ^ { k }$ . We will show that e is an identity element for the group. We’ve already shown that $e x = x e = x ^ { k + 1 } = x ,$ , so e works as an identity for x. Now let $y \in G$ . Then using associativity and left cancellation, we see

$$
x y = ( x e ) y = x ( e y ) \quad \Longrightarrow \quad y = e y .
$$

Likewise

$$
y x = y ( e x ) = ( y e ) x \quad \Longrightarrow \quad y = y e .
$$

Thus we have $e y = y e = y$ for any $y \in G$ and this proved that e is an identity element for the group. Now for any $y \in G$ , just as we did for x above, we can find $\ell \in \mathbb { N }$ such that $y ^ { \ell + 1 } = y$ . But this will give $y y ^ { \ell } = y e \quad \Longrightarrow \quad y ^ { \ell } = e ,$ . Thus

$$
y y ^ { \ell - 1 } = y ^ { \ell - 1 } y = e
$$

which shows that y has an inverse element and it is exactly $y ^ { \ell - 1 }$ . Hence G is a group.

Problem 18. What is the set of points $z \in \mathbb { C }$ such that $z ^ { 2 } = | z | ^ { 2 } ?$

Solution. $\operatorname { I f } z = x + i y$ , then the equation gives $x ^ { 2 } - y ^ { 2 } + 2 i x y = x ^ { 2 } + y ^ { 2 }$ . From the real parts we see that $y = 0$ , whence any value of x will satisfy the equation. Thus this set of points is the real line.

Problem 19. For $a , b \in \mathbb { C }$ , sketch the set of points $z \in \mathbb { C }$ such that $\begin{array} { r } { \left| \frac { z - a } { z - b } \right| < 1 } \end{array}$

Solution. Draw the line connecting a to b and then draw the line that is normal to the connecting line and intersects it at ${ \frac { a + b } { 2 } } $ . This normal line is the set where $| z - a | = | z - b |$ . The points on the a side of the line are the points where $| z - a | < | z - b | \iff \left| { \frac { z - a } { z - b } } \right| < 1 ,$

Problem 20. Let $z = e ^ { 2 \pi i / 5 }$ . Evaluate $1 + z + z ^ { 2 } + z ^ { 3 } + 5 z ^ { 4 } + 4 z ^ { 5 } + 4 z ^ { 6 } + 4 z ^ { 7 } + 4 z ^ { 8 } + 5 z ^ { 9 } .$

Solution. Note that $z ^ { 5 } = 1$ , and so

$$
1 + z + z ^ { 2 } + z ^ { 3 } + 5 z ^ { 4 } + 4 z ^ { 5 } + 4 z ^ { 6 } + 4 z ^ { 7 } + 4 z ^ { 8 } + 5 z ^ { 9 } = 5 + 5 z + 5 z ^ { 2 } + 5 z ^ { 3 } + 1 0 z ^ { 4 } .
$$

But

$$
\sum _ { n = 0 } ^ { 4 } z ^ { n } = { \frac { 1 - z ^ { 5 } } { 1 - z } } = 0
$$

so

$$
1 + z + z ^ { 2 } + z ^ { 3 } + 5 z ^ { 4 } + 4 z ^ { 5 } + 4 z ^ { 6 } + 4 z ^ { 7 } + 4 z ^ { 8 } + 5 z ^ { 9 } = 5 z ^ { 4 } = 5 e ^ { 8 \pi i / 5 } = - 5 e ^ { 3 \pi i / 5 } .
$$

Problem 21. Find $\operatorname* { l i m } _ { z \to 0 } { \frac { ( \overline { { { z } } } ) ^ { 2 } } { z ^ { 2 } } }$ or show that the limit does not exist.

Solution. Letting $z = x + i y$ iy, we see that

$$
{ \frac { ( \overline { { { z } } } ) ^ { 2 } } { z ^ { 2 } } } = { \frac { x ^ { 2 } - y ^ { 2 } - 2 i x y } { x ^ { 2 } - y ^ { 2 } + 2 i x y } } .
$$

Approaching zero along the real axis $\quad ( \sec y = 0$ , we see $\begin{array} { r } { \frac { ( \overline { { z } } ) ^ { 2 } } { z ^ { 2 } } = 1 } \end{array}$ but approaching along the line $y = x ,$ , we see $\begin{array} { r } { \frac { ( \overline { { z } } ) ^ { 2 } } { z ^ { 2 } } = - 1 } \end{array}$ so the limit does not exist.

Problem 22. Put $( 1 + i ) ^ { 1 0 }$ in the form $a + b i$ for $a , b \in \mathbb { R }$

Solution. In polar coordinates, we have $1 + i = { \sqrt { 2 } } e ^ { \pi i / 4 }$ . Thus $( 1 + i ) ^ { 1 0 } = 2 ^ { 5 } e ^ { 1 0 \pi i / 4 }$ . But $e ^ { 8 \pi i / 4 } = 1$ so

$$
( 1 + i ) ^ { 1 0 } = 3 2 e ^ { 2 \pi i / 4 } = 3 2 e ^ { \pi / 2 } = 3 2 i .
$$

Problem 23. If $f$ is an entire function which maps the complex plane into the real axis, then which of the following are the possible images of the imaginary axis under $f ?$

(a) the point $0  { \mathrm { ~ \textrm ~ { ~ ~ } ~ } } (  { \mathrm { b } } )$ any arbitrary point in $\begin{array} { r l } { \mathbb { R } } & { { } \mathit { \Omega } ( \mathrm { c } ) } \end{array}$ a half line (i.e., a set $( a , \infty ) \ \mathrm { o r } \ ( - \infty , a ) )$ (d) the whole real line

Solution. If f is entire and non-constant than $f ( \mathbb { C } ) = \mathbb { C }$ or $f ( \mathbb { C } ) \cup \{ a \} = \mathbb { C }$ for some $a \in \mathbb { C }$ . Thus if $f ( \mathbb { C } ) \subset \mathbb { R }$ , then f is constant, so the only possibilities are (a) and (b).

Problem 24. If $f ( z ) = ( 2 x + 3 y ) + i g ( x , y )$ is analytic and $g ( 2 , 3 ) = 1$ , what is $g ( x , y ) ?$

Solution. We need the real and imaginary parts of $f$ to satisfy the Cauchy-Riemann equations. This entails that

$$
{ \frac { \partial } { \partial x } } ( 2 x + 3 y ) = { \frac { \partial g } { \partial y } } \qquad { \mathrm { a n d } } \qquad { \frac { \partial } { \partial y } } ( 2 x + 3 y ) = - { \frac { \partial g } { \partial x } } .
$$

Using the first equation, we know that $\begin{array} { r } { \frac { \partial g } { \partial u } = 2 \mathrm { ~ s o ~ } g ( x , y ) = 2 y + h ( x ) } \end{array}$ . Differentiating with respect to x and using the second equation, we see $\tilde { h ^ { \prime } ( x ) } = - 3 \mathrm { ~ s o ~ } g ( x , y ) = 2 y - 3 x + C . \mathrm { ~ I f ~ } g ( 2 , 3 ) = 1$ , then $C = 1$ so $g ( x , y ) = 2 y - 3 x + 1$

Problem 25. Let $f , g : \mathbb { C } \to \mathbb { C }$ be entire. Show that if $e ^ { f ( z ) } + e ^ { g ( z ) } = 1$ for all $z \in \mathbb { C }$ , then f and $g$ are constant.

Solution. If this equation holds, then $e ^ { f }$ and $e ^ { g }$ both omit the points 0 and 1 and hence are both constant by Picard’s Little Theorem. Thus $f , g$ are constant as well.

Problem 26. Let $r > 0$ and let $P : \mathbb { C }  \mathbb { C }$ be a polynomial. What is $\oint _ { \{ | z | = r \} } P ( z ) d z ?$

Solution. Since P is entire, the integral is zero by Cauchy’s Integral Theorem.

Problem 27. Evaluate $\int _ { 0 } ^ { 2 \pi } e ^ { e ^ { i t } } d t .$

Solution. Make the substitution $z \ = \ e ^ { i t }$ . As t goes from 0 to $2 \pi , \ z$ traverses the unit circle. Also $d z = i e ^ { i t } d t \implies d t = d z / ( i z )$ . Thus

$$
\int _ { 0 } ^ { 2 \pi } e ^ { e ^ { i t } } d t = \frac { 1 } { i } \int _ { \{ | z | = 1 \} } \frac { e ^ { z } } { z } d z .
$$

But the residue theorem, we simply need to calculate the residue at zero. We see

$$
\operatorname* { l i m } _ { z \to 0 } z \cdot \frac { e ^ { z } } { z } = 1 .
$$

Thus

$$
\int _ { 0 } ^ { 2 \pi } e ^ { e ^ { i t } } d t = { \frac { 1 } { i } } \int _ { \{ | z | = 1 \} } { \frac { e ^ { z } } { z } } d z = { \frac { 1 } { i } } \cdot 2 \pi i \{ \mathrm { s u m ~ o f ~ r e s i d u e s } \} = 2 \pi .
$$

Problem 28. Let C be the circle $| z | = \pi ,$ , oriented positively. Evaluate $\oint _ { c } \left( \sin ( z ) - { \frac { \cos ( z ) } { z - \pi / 4 } } \right) d z$

Solution. The function sin(z) is entire, so the integral around the closed contour is zero. For the $\frac { \cos ( z ) } { z - \pi / 4 }$ we simply need to calculate the residue at $z = \pi / 4$ . We see

$$
\operatorname* { l i m } _ { z \to \pi / 4 } ( z - \pi / 4 ) { \frac { \cos ( z ) } { z - \pi / 4 } } = \cos ( \pi / 4 ) = { \sqrt { 2 } } 2 .
$$

Thus

$$
\oint _ { \mathcal { C } } \left( \sin ( z ) - { \frac { \cos ( z ) } { z - \pi / 4 } } \right) d z = 2 \pi i \left( { \frac { \sqrt { 2 } } { 2 } } \right) = \pi i { \sqrt { 2 } } .
$$

Problem 29. Let C be the circle $| z | = 2$ , oriented positively. Evaluate $\oint _ { c } { \frac { \cosh ( \pi z ) d z } { z ( z ^ { 2 } + 1 ) } }$

Solution. Again, we calculate the residues. Here there are first order poles at $z = 0 , \pm i . \mathrm { \ A t \ } z = 0$ , we see

$$
\operatorname* { l i m } _ { z \to 0 } z \cdot \frac { \cosh ( \pi z ) } { z ( z ^ { 2 } + 1 ) } = \frac { \cosh ( 0 ) } { 1 } = 1 .
$$

At $z = \pm i$ , we see

$$
\operatorname* { l i m } _ { z \to \pm i } = ( z \mp i ) { \frac { \cosh ( \pi z ) d z } { z ( z ^ { 2 } + 1 ) } } = \operatorname* { l i m } _ { z \to \pm i } { \frac { \cosh ( \pi z ) } { z ( z \pm i ) } } = { \frac { \cosh ( \pm i \pi ) } { ( \pm i ) \cdot ( \pm 2 i ) } } = { \frac { \cos ( \pi ) } { ( - 2 ) } } = { \frac { 1 } { 2 } } .
$$

Thus

$$
\oint _ { \mathcal { C } } \frac { \cosh ( \pi z ) d z } { z ( z ^ { 2 } + 1 ) } = 2 \pi i ( 1 + { \textstyle { \frac { 1 } { 2 } } } + { \textstyle { \frac { 1 } { 2 } } } ) = 4 \pi i .
$$

Problem 30. Evaluate $\int _ { - \infty } ^ { \infty } { \frac { d x } { 1 + x ^ { 4 } } } .$

Solution. Solving for $z ^ { 4 } = - 1$ , we see that the roots are $z = e ^ { i \pi / 4 } , e ^ { 3 \pi i / 4 } , e ^ { 5 \pi i / 4 } , e ^ { 7 \pi / 4 }$ . Or in real/imaginary coordinates, the roots are

$$
z _ { 1 } = \frac { \sqrt { 2 } } { 2 } ( 1 + i ) , ~ z _ { 2 } = \frac { \sqrt { 2 } } { 2 } ( - 1 + i ) , ~ z _ { 3 } = \frac { \sqrt { 2 } } { 2 } ( - 1 - i ) , ~ z _ { 4 } = \frac { \sqrt { 2 } } { 2 } ( 1 - i ) .
$$

Consider the function $\textstyle f ( z ) = { \frac { 1 } { 1 + z ^ { 4 } } }$ . We will integrate $f ( z )$ around the contour C pictured in figure 1 below and let $R \to \infty$

<!-- image-->  
Figure 1: Problem 30.

We have

$$
\oint _ { \mathcal { C } } f ( z ) d z = 2 \pi i \big ( \mathrm { R e s } ( f , z _ { 1 } ) + \mathrm { R e s } ( f , z _ { 2 } ) \big ) .
$$

Along the half-circle (call this ${ \mathcal { C } } _ { R } )$ , we use the ML-inequality and the reverse triangle inequality to find

$$
\left| \int _ { { \mathcal { C } } _ { R } } f ( z ) d z \right| \leq \ell ( { \mathcal { C } } _ { R } ) \cdot \operatorname* { s u p } _ { z \in { \mathcal { C } } _ { R } } { \frac { 1 } { | z ^ { 4 } + 1 | } } \leq { \frac { \pi R } { R ^ { 4 } - 1 } } \to 0 , \quad { \mathrm { ~ a s ~ } } ~ R \to \infty .
$$

Thus

$$
\int _ { - \infty } ^ { \infty } \frac { d x } { 1 + x ^ { 4 } } = 2 \pi i \big ( \mathrm { R e s } ( f , z _ { 1 } ) + \mathrm { R e s } ( f , z _ { 2 } ) \big ) .
$$

Now

$$
\operatorname { R e s } ( f , z _ { 1 } ) = \operatorname* { l i m } _ { z  z _ { 1 } } { ( z - z _ { 1 } ) } \cdot { \frac { 1 } { 1 + z ^ { 4 } } } = { \frac { 1 } { ( z _ { 1 } - z _ { 2 } ) ( z _ { 1 } - z _ { 3 } ) ( z _ { 1 } - z _ { 4 } ) } } = { \frac { 1 } { { \sqrt { 2 } } \cdot { \sqrt { 2 } } ( 1 + i ) \cdot i { \sqrt { 2 } } } } = { \frac { 1 } { 4 { \sqrt { 2 } } } } ( - 1 - i ) .
$$

Likewise

$$
\operatorname { R c s } ( f , z _ { 2 } ) = \operatorname* { l i m } _ { z  z _ { 2 } } ( z - z _ { 2 } ) \cdot { \frac { 1 } { 1 + z ^ { 4 } } } = { \frac { 1 } { ( z _ { 2 } - z _ { 1 } ) ( z _ { 2 } - z _ { 3 } ) ( z _ { 2 } - z _ { 4 } ) } } = { \frac { 1 } { ( - { \sqrt { 2 } } ) \cdot i { \sqrt { 2 } } \cdot { \sqrt { 2 } } ( - 1 + i ) } } = { \frac { 1 } { 4 { \sqrt { 2 } } } } ( 1 - i ) .
$$

Thus

$$
\int _ { - \infty } ^ { \infty } { \frac { d x } { 1 + x ^ { 4 } } } = 2 \pi i \left( { \frac { 1 } { 4 \sqrt { 2 } } } ( - 1 - i ) + { \frac { 1 } { 4 \sqrt { 2 } } } ( 1 - i ) \right) = { \frac { \pi } { \sqrt { 2 } } } .
$$

[Using similar methods, one can show more generally that $\begin{array} { r } { \int _ { - \infty } ^ { \infty } \frac { d x } { 1 + x ^ { 2 n } } = \frac { \pi } { n } \csc \left( \frac { \pi } { 2 n } \right) \mathrm { f o r } n \in \mathbb { N } . \mathrm { ] } } \end{array}$

Problem 31. Using the substitution $z = e ^ { i x }$ (or otherwise), evaluate $\int _ { 0 } ^ { 2 \pi } { \frac { d x } { 1 0 - 8 \cos ( x ) } } .$

Solution. The substitution $z = e ^ { i x }$ turns the integral into a contour integral around the unit circle. Also $d x = d z / ( i z )$ and since $\cos ( x ) = { \textstyle { \frac { 1 } { 2 } } } ( e ^ { i x } + e ^ { - i x } )$ , we have

$$
\int _ { 0 } ^ { 2 \pi } { \frac { d x } { 1 0 - 8 \cos ( x ) } } = { \frac { 1 } { i } } \int _ { \{ | z | = 1 \} } { \frac { d z } { z ( 1 0 - 4 z - 4 z ^ { - 1 } ) } } = - { \frac { 1 } { 2 i } } \int _ { \{ | z | = 1 \} } { \frac { d z } { 2 z ^ { 2 } - 5 z + 2 } } = - { \frac { 1 } { 2 i } } \int _ { \{ | z | = 1 \} } { \frac { d z } { ( 2 z - 1 ) ( z - 2 ) } } .
$$

Letting $\begin{array} { r } { f ( z ) = \frac { 1 } { ( 2 z - 1 ) ( z - 2 ) } } \end{array}$ , we see that f has residues at $z = 1 / 2$ and $z = 2 ,$ . The only one of these that lies in the contour is $z = 1 / 2$ so that is the only residue that matters. We see

$$
\mathrm { R e s } ( f , \frac { 1 } { 2 } ) = \operatorname * { l i m } _ { z \to 1 / 2 } ( z - 1 / 2 ) \cdot \frac { 1 } { ( 2 z - 1 ) ( z - 2 ) } = \frac { 1 } { 2 ( \frac { 1 } { 2 } - 2 ) } = - \frac { 1 } { 3 } .
$$

Thus

$$
\int _ { 0 } ^ { 2 \pi } { \frac { d x } { 1 0 - 8 \cos ( x ) } } = - { \frac { 1 } { 2 i } } \cdot 2 \pi i \left( - { \frac { 1 } { 3 } } \right) = { \frac { \pi } { 3 } } .
$$

Problem 32. Find two different Laurent expansions for $f ( z ) = { \frac { 1 } { z ( z ^ { 2 } + 1 ) } }$ and specify the regions in which they converge.

Solution. When $| z | < 1$

$$
{ \frac { 1 } { 1 + z ^ { 2 } } } = \sum _ { n = 0 } ^ { \infty } ( - 1 ) ^ { n } z ^ { 2 n } .
$$

Thus we have the Laurent expansion

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } ( - 1 ) ^ { n } z ^ { 2 n - 1 } = { \frac { 1 } { z } } - z + z ^ { 3 } - z ^ { 5 } + \cdots , \quad { \mathrm { ~ w h e n ~ } } \quad 0 < | z | < 1 .
$$

When $| z | > 1$ , we have $\begin{array} { r } { \frac { 1 } { | z | } < 1 } \end{array}$ and so

$$
{ \frac { 1 } { 1 + z ^ { 2 } } } = { \frac { 1 } { z ^ { 2 } } } \cdot { \frac { 1 } { 1 + { \frac { 1 } { z ^ { 2 } } } } } = { \frac { 1 } { z ^ { 2 } } } \sum _ { n = 0 } ^ { \infty } ( - 1 ) ^ { n } { \frac { 1 } { z ^ { 2 n } } } = \sum _ { n = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { n } } { z ^ { 2 n + 2 } } } .
$$

Thus we have the Laurent expansion

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { n } } { z ^ { 2 n + 3 } } } = { \frac { 1 } { z ^ { 3 } } } - { \frac { 1 } { z ^ { 5 } } } + { \frac { 1 } { z ^ { 7 } } } - { \frac { 1 } { z ^ { 9 } } } + \cdots , \mathrm { w h e n } 1 < \vert z \vert .
$$

Problem 33. Evaluate the integral $\oint _ { \{ | z | = 3 \} } \frac { e ^ { \frac { 1 } { 1 - z } } } { z } d z .$

Solution. There are singularities at $z = 0$ and z = 1. At z = 1, there is an essential singularity so we find the first coefficient in the Laurent expansion at $z = 1$ . We see in a punctured neighborhood of $z = 1$ b,

$$
{ \frac { e ^ { 1 / ( 1 - z ) } } { z } } = { \frac { e ^ { 1 / ( 1 - z ) } } { 1 - ( 1 - z ) } } = \left( \sum _ { n \geq 0 } { \frac { ( 1 - z ) ^ { - n } } { n ! } } \right) \left( \sum _ { n \geq 0 } ( 1 - z ) ^ { n } \right) .
$$

Now using the Cauchy product formula:

$$
\left( \sum _ { n \geq 0 } a _ { n } \right) \left( \sum _ { n \geq 0 } b _ { n } \right) = \sum _ { n \geq 0 } \sum _ { 0 \leq k \leq n } a _ { k } b _ { n - k } .
$$

We have

$$
{ \frac { e ^ { 1 / ( 1 - z ) } } { z } } = \sum _ { n \geq 0 } \sum _ { 0 \leq k \leq n } { \frac { ( 1 - z ) ^ { - k } } { k ! } } ( 1 - z ) ^ { n - k } = \sum _ { n \geq 0 } \sum _ { 0 \leq k \leq n } { \frac { ( 1 - z ) ^ { n - 2 k } } { k ! } } .
$$

Now if n is even, then $n - 2 k \neq - 1$ for any k. If n is odd then $n = 2 m - 1$ for some $m = 1 , 2 , . . .$ . and $n - 2 k = - 1 { \mathrm { ~ f o r ~ } } k = m$ . This shows that the coefficient of $( 1 - z ) ^ { - 1 }$ in this expansion is

$$
\sum _ { m \geq 1 } { \frac { 1 } { m ! } } = e - 1 ,
$$

but we need the coefficient of $( z - 1 ) ^ { - 1 }$ so we take the negative: $1 - e .$ . Thus since the residue at $z = 0$ is given by

$$
\operatorname* { l i m } _ { z \to 0 } z \cdot { \frac { e ^ { 1 / ( 1 - z ) } } { z } } = e ,
$$

we have

$$
\oint _ { \{ | z | = 3 \} } { \frac { e ^ { 1 / ( 1 - z ) } } { z } } \mathrm { d } z = 2 \pi i \{ \mathrm { s u m ~ o f ~ r e s i d u e s } \} = 2 \pi i ( e + ( 1 - e ) ) = 2 \pi i .
$$

Alternatively, making the transformation $w = 1 / z$ , we see $d w = - d z / z ^ { 2 }$ which is the same as $d z = - d w / w ^ { 2 }$ Note, in making the transformation you also reverse the orientation of the contour: if z traverses the circle counterclockwise (positive orientation), then w traverses the circle clockwise (negative orientation) and this results in an additional sign change (which cancels the sign change from $d z = - d w / w ^ { 2 } )$ . Then

$$
\oint _ { \{ | z | = 3 \} } \frac { e ^ { 1 / ( 1 - z ) } } { z } d z = \oint _ { \{ | w | = 1 / 3 \} } w e ^ { 1 / ( 1 - 1 / w ) } \frac { d w } { w ^ { 2 } } = \oint _ { \{ | w | = 1 / 3 \} } \frac { e ^ { w / ( w - 1 ) } } { w } d w .
$$

Now there is only one singularity inside the contour of integration which is at $w = 0$ . Thus

$$
\oint _ { \{ | z | = 3 \} } { \frac { e ^ { 1 / ( 1 - z ) } } { z } } d z = \oint _ { \{ | w | = 1 / 3 \} } { \frac { e ^ { w / ( w - 1 ) } } { w } } d w = 2 \pi i \operatorname* { l i m } _ { w \to 0 } w \cdot { \frac { e ^ { w / ( w - 1 ) } } { w } } = 2 \pi i .
$$

Problem 34. Suppose that $f : \mathbb { C } \to \mathbb { C }$ is non-constant and entire. Prove that the image of f is dense in $\mathbb { C } ;$ that is, for arbitrary $z _ { 0 } \in \mathbb { C }$ and $\varepsilon > 0 ,$ , show that there exists $z \in \mathbb { C }$ such that $| f ( z ) - z _ { 0 } | < \varepsilon$ [Note: this is a weaker version of Picard’s Little Theorem which says that the image of f omits at most one point in C; you should prove this directly without reference to Picard’s Little Theorem.]

Solution. Suppose that $f$ is entire and $f ( \mathbb { C } )$ is not dense in C. Then there is $z _ { 0 } \in \mathbb { C }$ and $\varepsilon > 0$ such that $| f ( z ) - z _ { 0 } | \geq \varepsilon$ for all $z \in \mathbb { C }$ . Consider the function $g ( z ) = 1 / ( f ( z ) - z _ { 0 } )$ . Since $f$ is entire and bounded away from $z _ { 0 } , \textit { g }$ is also entire. We see $| g ( z ) | = 1 / \left| f ( z ) - z _ { 0 } \right| \le \frac { 1 } { \varepsilon }$ Thus $g$ is bounded. By Liouville’s theorem, g must be constant and this implies that $f$ is constant. Thus we’ve proven that if f is entire and $f ( \mathbb { C } )$ is not dense in C, then f is constant. Contrapositively, if f is entire and non-constant, then f (C) is dense in C.

Problem 35. Suppose that $f : \mathbb { C } \to \mathbb { C }$ is an entire function such that $| f ( z ) | \leq C | z |$ for all z sufficienty large. Prove that $f ( z ) = c _ { 1 } + c _ { 2 } z $ for some constants $c _ { 1 } , c _ { 2 }$ . [Note: this is a generalization of Liouville’s Theorem. It can actually be generalized further: if f is entire and $| f ( z ) | \leq C | z | ^ { n }$ for sufficiently large $z ,$ then $f$ is a polynomial of degree $\leq n . ]$

Solution. Use induction on n. The base case $n = 0$ is Liouvillie’s theorem. Suppose the theorem holds for some fixed n, and assume that f is entire and $\left| f ( z ) \right| \leq C \left| z \right| ^ { n + 1 }$ for all z sufficiently large. Then the function

$$
g ( z ) = \left\{ { \begin{array} { l l } { { { \frac { f ( z ) - f ( 0 ) } { z } } , } } & { { z \neq 0 , } } \\ { { } } & { { } } \\ { { f ^ { \prime } ( 0 ) , } } & { { z = 0 } } \end{array} } \right.
$$

is entire and $| g ( z ) | \leq C | z | ^ { n }$ for z sufficiently large. Since the theorem holds for n by the inductive hypothesis, we see that g is a polynomial of degree n, whence $f ( z ) = f ( 0 ) \bot z g ( z )$ for all $z \neq 0$ shows that $f$ is a polynomial of degree $n + 1$