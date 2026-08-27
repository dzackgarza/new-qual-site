## ALGEBRA HW 11

## CLAY SHONKWILER

## 1

Suppose $k \subset K$ is a separable field extension of degree n.

(a): Show that $K \simeq k [ x ] / ( f ( x ) )$ for some $f ( x ) \in k [ x ]$ of degree n.

Proof. By the primitive element theorem, $K = k [ \alpha ]$ for some $\alpha \in$ $K$ . If f is the minimal polynomial of α over $k ,$ , then $K = k [ \alpha ] \simeq$ $k [ x ] / ( f ( x ) )$ ). Then

$$
\deg f = [ K : k ] = n ,
$$

so we see that $K \simeq k [ x ] / ( f ( x ) )$ where $f ( x ) \in k [ x ]$ has degree n. 

(b): Show that $K \otimes _ { k } K \simeq K [ y ] / ( f ( y ) )$ as K-algebras.

Proof. Since $K \simeq k [ x ] / ( f ( x ) )$ , we see that

$$
K \otimes _ { k } K \simeq k [ x ] / ( f ( x ) ) \otimes _ { k } k [ y ] / ( f ( y ) ) \simeq k [ x , y ] / ( f ( x ) , f ( y ) ) .
$$

On the other hand,

$$
K [ y ] / ( f ( y ) ) \simeq ( k [ x ] / ( f ( x ) ) ) [ y ] / ( f ( y ) ) \simeq k [ x , y ] / ( f ( x ) , f ( y ) ) ,
$$

so we see that

$$
K \otimes _ { k } K \simeq k [ x , y ] / ( f ( x ) , f ( y ) ) \simeq K [ y ] / ( f ( y ) ) .
$$

(c): Deduce that if K is Galois over $k ,$ then $f ( y )$ splits over $K$ , and K $\otimes _ { k } K \simeq K ^ { n }$ as K-algebras.

Proof. If K is Galois over $k ,$ then, since $K \simeq k [ y ] / ( f ( y ) )$ , it must be the case that $f ( y )$ splits over K (else K would not be normal over k). Hence, $\begin{array} { r } { f ( y ) = \prod _ { i = 1 } ^ { n } ( y - \alpha _ { i } ) } \end{array}$ for $\alpha _ { i } \in K , i = 1 , \ldots , n$ . Since $( y - \alpha _ { i } )$ is maximal in $K [ y ]$ and $\begin{array} { r } { ( f ( x ) ) = ( \prod _ { i = 1 } ^ { n } ( y - \alpha _ { i } ) ) = ( y - \alpha _ { 1 } ) \cdot \cdot \cdot ( y - \alpha _ { n } ) } \end{array}$ 2 we know, by the Chinese Remainder Theorem, that

$$
K [ y ] / ( f ( x ) ) \simeq K [ y ] / ( y - \alpha _ { 1 } ) \times \cdot \cdot \cdot \times K [ y ] / ( y - \alpha _ { n } ) .
$$

Now, since $K [ y ] / ( y - \alpha _ { i } ) \simeq K$ , this implies that $K [ y ] / ( f ( x ) ) \simeq K ^ { n }$ Therefore, using the result from (b) above,

$$
K \otimes _ { k } K \simeq K [ y ] / ( f ( x ) ) \simeq K ^ { n } .
$$

Let R be an ordered field whose squares are the non-negative elements. Suppose that the elements of $R [ x ]$ satisfy the intermediate value theorem. Let $C = R [ x ] / ( x ^ { 2 } + 1 )$ .

(a): Show that R has characteristic 0, and that every odd degree polynomial over R has a root in R. Deduce that every non-trivial Galois extension of R has even degree.

Proof. Suppose R has characteristic p. Then, since $\leq$ respects addition, $1 \leq 1 + 1 \leq . . . \leq p - 1$ . However, $p - 1 + 1 = 0$ , and so we have $0 \leq 1 \leq 1 + 1 \leq \ldots \leq p - 1 \leq 0$ , meaning that $0 = 1$ , which is impossible. Therefore, it must be the case that R has characteristic 0.

Now, suppose $f$ is an odd degree polynomial over R. Then $f ( x ) =$ $a _ { 2 n + 1 } x ^ { 2 n + 1 } + \ldots + a _ { 1 } x + a _ { 0 }$ Suppose $a _ { 2 n + 1 } ~ \leq ~ 0$ . Then, for x sufficiently small, the leading term dominates all other terms so, since $x ^ { 2 n + 1 } \leq 0$ for $x \le 0 , f ( x _ { 0 } ) \ge 0$ for $x _ { 0 }$ sufficiently small. On the other hand, for $x \geq 0 , x ^ { 2 n + 1 } \geq 0$ , so, for $x _ { 1 }$ sufficiently large, $f ( x _ { 1 } ) \leq 0$ . Therefore, since the elements of $R [ x ]$ (including $f )$ satisfy the intermediate value theorem, $f ( x ) = 0$ for some $x _ { 0 } \leq x \leq x _ { 1 }$ That is, $f$ has a root in R.

Now, suppose K is a finite extension of R. Then, by the primitive element theorem, there exists $\alpha \in K$ such that $K = R [ \alpha ]$ . In turn, since $R [ \alpha ] \simeq R [ x ] / ( f ( x ) )$ where $f ( x ) \in R [ x ]$ is the minimal polynomial of α over $R _ { : }$ we see that $K \simeq R [ x ] / ( f ( x ) )$ . Now, since $f$ is irreducible over $R ,$ it’s clear that deg f must be even, by the result proved above. However, since $[ K : R ] = \deg f .$ , this in turn means that K must have even degree as an extension of $R .$ Since our choice of K was arbitrary, we see that every finite extension of R must be of even degree. 

(b): Show that C is a field, that every element of C is a square of an element of $C ,$ and that C has no field extensions of degree 2.

Proof. Since the two roots of $x ^ { 2 } + 1$ in $\bar { R }$ are $\sqrt { - 1 }$ and $- { \sqrt { - 1 } }$ and the squares in R are the non-negative elements, $x ^ { 2 } + 1$ is irreducible, so $C = R [ x ] / ( x ^ { 2 } + 1 )$ is a field. Now, for any element in $R [ x ] / ( x ^ { 2 } + 1 )$ , we can reduce higher-order terms by $x ^ { 2 } = - 1$ , so a generic element in $C$ is of the form $a +$ bx for some $a , b \in R$ . If $a = b = 0$ , then it’s clear that $a + b x = 0 + 0 x = ( 0 + 0 x ) ^ { 2 }$ . Otherwise, let

$$
c = { \sqrt { \frac { a + { \sqrt { a ^ { 2 } + b ^ { 2 } } } } { 2 } } } \quad d = { \frac { b } { 2 } } { \sqrt { \frac { 2 } { a + { \sqrt { a ^ { 2 } + b ^ { 2 } } } } } } .
$$

Then, since ${ \sqrt { a ^ { 2 } + b ^ { 2 } } } \geq | a |$ , (where $| a | = a$ if $a \geq 0$ and $| a | = - a$ if $a \leq 0 )$ , so c and d are both in $R ,$ and so $c + d x \in C$ . Furthermore,

$$
\begin{array} { r l } & { ( c + d x ) ^ { 2 } - c ^ { 2 } - d ^ { 2 } + 2 c d x } \\ & { \qquad = \frac { a + \sqrt { a ^ { 2 } + b ^ { 2 } } } { 2 } - \frac { b ^ { 2 } } { 4 } \left( \frac { 2 } { a + \sqrt { a ^ { 2 } + b ^ { 2 } } } \right) + 2 \left( \sqrt { \frac { a + \sqrt { a ^ { 2 } + b ^ { 2 } } } { 2 } } \right) \left( \frac { b } { 2 } \sqrt { \frac { 2 } { a + \sqrt { a ^ { 2 } + b ^ { 2 } } } } \right) x } \\ & { \qquad - \frac { \left( a + \sqrt { a ^ { 2 } + b ^ { 2 } } \right) ^ { 2 } } { 2 \left( a + \sqrt { a ^ { 2 } + b ^ { 2 } } \right) ^ { 2 } } - \frac { b ^ { 2 } } { 4 } \left( \frac { 4 } { 2 \left( a + \sqrt { a ^ { 2 } + b ^ { 2 } } \right) } \right) + 2 \frac { b } { 2 } \sqrt { \frac { 2 \left( a + \sqrt { a ^ { 2 } + b ^ { 2 } } \right) } { 2 \left( a + \sqrt { a ^ { 2 } + b ^ { 2 } } \right) } } x } \\ & { \qquad = \frac { a ^ { 2 } + 2 a \sqrt { a ^ { 2 } + b ^ { 2 } } + a ^ { 2 } + b ^ { 2 } } { 2 \left( a + \sqrt { a ^ { 2 } + b ^ { 2 } } \right) } - \frac { b ^ { 2 } } { 2 \left( a + \sqrt { a ^ { 2 } + b ^ { 2 } } \right) } + b x } \\ & { \qquad = \frac { 2 a ^ { 2 } + 2 a \sqrt { a ^ { 2 } + b ^ { 2 } } } { 2 \left( a + \sqrt { a ^ { 2 } + b ^ { 2 } } \right) } + b x } \\ & { \qquad = a + b x . } \end{array}
$$

Since our choice of $a + b x \in C$ was arbitrary, we see that every element of C is a square of an element of C.

Now, suppose K is a field extension of C of degree 2. Then, since C contains a second root of unity (namely −1), Kummer’s Theorem tells us that $K = C [ { \sqrt { \alpha } } ]$ for some $\alpha \in C$ . However, since, by the above result, $\alpha = \beta ^ { 2 }$ for some $\beta \in C ,$ we see that $K = C [ { \sqrt { \alpha } } ] =$ $C [ \beta ] = C$ , contradicting the supposition that K is an extension of degree 2. Therefore, we see that C has no field extensions of degree 2. 

(c): Show that if $R \subset C \subset L$ are finite field extensions and L is Galois over R with group G, then G is a 2-group.

Proof. Since, by (a), L must be an even extension of $R , \# G$ is divisible by 2, so $\# G = 2 ^ { r }$ m for some $r \geq 1$ and m relatively prime to 2. Furthermore, G contains a Sylow 2-subgroup H with $\# H = 2 ^ { r }$ Now, let $K \ = \ L ^ { H }$ , the fixed field of $H ;$ then L is Galois over K with Galois group H. Furthermore, since $[ L : R ] = 2 ^ { r } m$ and $[ L : K ] = \# H = 2 ^ { r } , [ K : R ] = m$ , which is relatively prime to 2 and, in particular odd. However, we showed that R has no non-trivial odd degree extensions, so it must be the case that $K = R$ and so $m = 1$ . Hence, $G = H$ , so G is a 2-group. 

(d): In the situation of (c), show that $L = C$

Proof. Since L is finite over $R , L = R [ \alpha ]$ for some $\alpha \in R$ . Let $f$ be the minimal polynomial of α over R. Then, since L is Galois over R, f splits over L. Thus, if g is the minimal polynomial of α over C, then $_ { g | f }$ and so g splits over $L ,$ meaning that L is normal over C. Since C has characteristic 0, L is necessarily separable over $C _ { i }$ so we see that L is Galois over C. Since $\left[ L : R \right] = 2 ^ { r }$ and $[ C : R ] = 2$ $[ L : C ] = 2 ^ { r - 1 }$ , so $\# \mathrm { G a l } ( L / C ) = 2 ^ { \bar { r } - 1 }$ . By Cauchy’s Theorem, $\operatorname { G a l } ( L / C )$ has a subgroup $H _ { 1 }$ of order 2. Let $K _ { 1 } = L ^ { H _ { 1 } }$ Then $[ L : \dot { K _ { 1 } } ] = 2 ^ { r - 2 }$ , so, if $r \geq 2 , [ K _ { 1 } : C ] = 2$ , contradicting the result proved in (b) above. Therefore, we see that $r = 1$ , meaning that $[ L : K ] = 2 ^ { { \dot { r } } - 1 } = 1$ , so $L = C$ 

(e): Conclude that C is algebraically closed.

Proof. Suppose K is an algebraic extension of C. Let $\widetilde { K }$ be the algebraic closure of K over C. Then we have $R \subset C \subset { \widetilde { K } }$ fulfilling the hypotheses of (c), so, by (c) and (d), $\widetilde K = C .$ . Therefore, $K = C$ Since our choice of K was arbitrary, we see that there are no nontrivial algebraic extensions of C, so C is algebraically closed. 

(f): Deduce in particular that the field C of complex numbers is algebraically closed.

Proof. Since R is an ordered field, the elements of R[x] satisfy the intermediate value theorem, and $\mathbb { C } = \mathbb { R } [ x ] / ( x ^ { 2 } + 1 )$ , we see that, by (a)-(e), C is algebraically closed. 

## 3

Let $p$ be a prime number, and let $K \subset L$ be a field extension of degree p that is separable but not Galois. Let $\widetilde { L }$ be the Galois closure of L over K. Show that $\widetilde { L }$ does not contain any subfield M which is Galois over K of degree p.

Proof. First, note that, by the primitive element theorem, $L = K [ \alpha ]$ for some $\alpha \in L$ and the minimal polynomial f of α has degree $p .$ Since L is separable, f is separable. $\widetilde { L }$ is obtained from $L$ simply by adjoining all the roots of $f$ and any K-automorphism of $\widetilde { L }$ permutes the roots of $f .$ Since there are $p$ roots of $f$ (since $f$ is separable), we see that $\operatorname { G a l } ( \widetilde { L } / K )$ is the subgroup of $S _ { p }$ consisting of the possible permutations of the roots of $f .$ . In particular, this means that $\# \mathrm { G a l } ( \widetilde { L } / K ) | p !$

Now, suppose $\widetilde { M }$ contains a subfield M which is Galois over K of degree $p .$ Then $\mathrm { { G a l } } ( M / K ) = C _ { p }$ . Hence, LM is Galois over L, and $\operatorname { G a l } ( L M / L )$ is a subgroup of $C _ { p }$ . Since the only such subgroups are the trivial group and $C _ { p }$ itself, we see that either $\operatorname { G a l } ( L M / L ) = 1$ or $\operatorname { G a l } ( L M / L ) = C _ { p } .$ In the first case, this implies that $L M = L$ , which is impossible, since this implies $M = L$ and $L$ is not Galois over K. On the other hand, if $\operatorname { G a l } ( L M / L ) = C _ { p }$ , then we have that $L \cap M = K$ , which in turn implies that $[ L M : K ] = \mathbf { \dot { [ } } L : K ] [ M : K ] = p ^ { 2 }$ . On the other hand,

$$
p ^ { 2 } = [ L M : K ] \mid [ { \widetilde L } : K ] = \# \mathrm { G a l } ( { \widetilde L } / K ) = p ! .
$$

This implies that $p | ( p - 1 )$ !, which is impossible since $p$ is prime. Therefore, we conclude that, in fact, there is no such $M .$ , so $\widetilde { L }$ does not contain any subfield M which is Galois over K of degree $p .$ 

(a): Prove that any polynomial $f ( x ) \in \mathbb { Q } [ x ]$ of degree $< 5$ is solvable by radicals.

Proof. Clearly, it suffices to show that any irreducible polynomial $f ( x ) \in \mathbb { Q } [ x ]$ of degree $< 5$ is solvable by radicals. To that end, let $f ( x ) \in \mathbb { Q } [ x ]$ be irreducible and of degree n $< 5 ;$ we may as well also assume $f$ is monic. Let $L$ be the splitting field of $f$ and let $a _ { 1 } , \ldots , a _ { n }$ be the roots of $f$ in ${ \overline { { \mathbb { Q } } } } .$ . Then any Q-automorphism of $L$ consists simply in permuting the $a _ { i } .$ , so we see that $\operatorname { G a l } ( L / \mathbb { Q } )$ is a subgroup of $S _ { n }$ . Since any subgroup of a solvable group is solvable and an irreducible polynomial in $\mathbb { Q } [ x ]$ is solvable by radicals if and only if the Galois group of its splitting field is solvable, we see that $f$ is solvable if and only if $S _ { n }$ is solvable.

Now, $S _ { 1 } = 1$ and $S _ { 2 } = 2$ are trivially solvable. Also, as a subgroup of $S _ { 3 } , \ \langle ( 1 2 3 ) \rangle \simeq C _ { 3 }$ is of index 2 in $S _ { 3 }$ and is, therefore, normal. Hence, we have the composition series

$$
1 \triangleleft \langle ( 1 2 3 ) \rangle \triangleleft S _ { 3 } , 
$$

the the quotients are $C _ { 3 }$ and $C _ { 2 }$ from left to right, so we see that $S _ { 3 }$ is solvable.

Finally, $A _ { 4 }$ is a subgroup of index 2 in $S _ { 4 } ,$ , so $A _ { 4 } \triangleleft S _ { 4 }$ . Now, let $G = \{ 1 , ( 1 2 ) ( 3 4 ) , ( 1 3 ) ( 2 4 ) , ( 1 4 ) ( 2 3 ) \}$ . Then, as we’ve seen, $G \triangleleft S _ { 4 }$ , so $G \triangleleft A _ { 4 }$ . Furthermore, since # $\mathbf { \partial } \cdot A _ { 4 } = 1 2$ and $\# G = 4$ , it must be the case that $A _ { 4 } / G \simeq C _ { 3 }$ . Since $A _ { 4 } \simeq C _ { 2 } \times C _ { 2 }$ , we see that we have the following composition series for $S _ { 4 }$

$$
1 \triangleleft C _ { 2 } \triangleleft G \triangleleft A _ { 4 } \triangleleft S _ { 4 } ,right.
$$

which has quotients $C _ { 2 } , C _ { 2 } , C _ { 3 } , C _ { 2 }$ from left to right, so we see that $S _ { 4 }$ is solvable. Since 1, 2, 3, 4 are the only possibilities for $n \textless 5$ , we see that $f$ must be solvable by radicals. Since our choice of $f$ was arbitrary, we see that any irreducible polynomial $f ( x ) \in \mathbb { Q } [ x ]$ of degree $< 5$ is solvable by radicals. 

(b): Find an $\alpha \in { \overline { { \mathbb { Q } } } }$ whose irreducible polynomial over Q has degree 5, and is solvable by radicals.

Example: Let $\alpha = \zeta _ { 1 1 } + \zeta _ { 1 1 } ^ { - 1 }$ Then, by the result proved in $\mathrm { P S 1 0 } \# 2 ( \mathrm { d } ) , ~ \mathbb { Q } ( \alpha )$ is Galois over Q with Galois group $C _ { 5 }$ . Since $\mathbb { Q } ( \alpha ) = \mathbb { Q } [ x ] / ( f ( x ) )$ ) where $f$ is the irreducible polynomial of α over $\mathbb { Q }$ , we see that deg $f = \# \mathrm { G a l } ( \mathbb { Q } ( \alpha ) / \mathbb { Q } ) = 5$ . Furthermore, since $C _ { 5 }$ is a solvable group (composition series: $1 \triangleleft C _ { 5 } )$ , we see that $f ( x )$ is solvable by radicals.

(a): Let $p$ be a prime number, and let $G$ be a subgroup of $S _ { p }$ . Suppose G contains a transposition and a p-cycle. Show that $G = S _ { p }$

Proof. Clearly, if $p = 2$ , then $S _ { 2 } ~ = ~ C _ { 2 } .$ so the only non-identity element is the unique 2-cycle, so G containing a 2-cycle means $G =$ $S _ { 2 }$ . Hence, suppose $p$ is an odd prime and suppose $\left( 1 a _ { 1 } \ldots a _ { p - 1 } \right)$ is the p-cycle in $G$ (we can always write a p-cycle in this form) and $\left( b _ { 1 } b _ { 2 } \right)$ is the transposition in $G$ . Then $b _ { 1 } = a _ { i }$ for some i and $b _ { 2 } = a _ { j }$ for some $j .$ . Then $( 1 a _ { 1 } \dots a _ { p - 1 } ) ^ { - 1 } = ( 1 a _ { p - 1 } \dots a _ { 1 } ) \qquad $ and

$$
( 1 a _ { 1 } \dots a _ { p - 1 } ) ( b _ { 1 } b _ { 2 } ) ( 1 a _ { p - 1 } \dots a _ { 1 } ) = ( 1 a _ { 2 } \dots a _ { p } ) ( a _ { i } a _ { j } ) ( 1 a _ { p } \dots a _ { 2 } ) = ( a _ { i + 1 } a _ { j + 1 } ) \in G ,
$$

where we figure $i + 1$ and $j + 1$ module p with $a _ { 0 } ~ = ~ 1$ . Now,

$( 1 a _ { 1 } \dots a _ { p - 1 } ) ^ { 2 } = ( 1 a _ { 2 } a _ { 4 } \dots a _ { p - 1 } a _ { 1 } a _ { 3 } \dots a _ { p - 2 } )$ . Then

$$
( 1 a _ { 2 } a _ { 4 } \ldots a _ { p - 1 } a _ { 1 } a _ { 3 } \ldots a _ { p - 2 } ) ( a _ { i } a _ { j } ) ( 1 a _ { p - 2 } a _ { p - 4 } \ldots a _ { 1 } a _ { p - 1 } a _ { p - 3 } \ldots a _ { 2 } ) = ( a _ { i + 2 } a _ { j + 2 } ) \in G ,
$$

again figuring $i + 2$ and $j + 2$ modulo $p .$ Iterating this process, we see that

$$
( a _ { i } a _ { j } ) , ( a _ { i + 1 } a _ { j + 1 } ) , \dots , ( a _ { i + ( p - 1 ) } a _ { j + ( p - 1 ) } ) \in G ,
$$

where we figure the $i + k$ and $j + k$ modulo p. Now, $a _ { i + ( p - i ) } = a _ { 0 } = 1$ so $( 1 a _ { j + ( p - i ) } ) \ \in \ G$ . Now, $j + ( p - i ) = i + k _ { 1 }$ for some $k _ { 1 }$ , so $( a _ { i + k _ { 1 } } a _ { j + ( p - i ) } ) \in G .$ , and so

$$
( a _ { i + k _ { 1 } } a _ { j + ( p - i ) } ) ( 1 a _ { j + ( p - i ) } ) ( a _ { i + k _ { 1 } } a _ { j + ( p - i ) } ) = ( 1 a _ { i + k _ { 1 } } ) \in G .
$$

In turn, $i + k _ { 1 } = j + k _ { 2 }$ for some $k _ { 2 }$ , so $( a _ { i + k _ { 2 } } a _ { i + k _ { 1 } } ) \in G$ and so

$$
( a _ { i + k _ { 2 } } a _ { i + k _ { 1 } } ) ( 1 a _ { i + k _ { 1 } } ) ( a _ { i + k _ { 2 } } a _ { i + k _ { 1 } } ) = ( 1 a _ { i + k _ { 2 } } ) \in G .
$$

Iterating this process, we see that

$$
( 1 2 ) , ( 1 3 ) , \ldots , ( 1 ( p - 1 ) ) \in G .
$$

Now, if $( a b ) \in S _ { p }$ is a transposition, then

$$
( 1 a ) ( 1 b ) ( 1 a ) = ( a b ) \in G .
$$

Therefore, we see that all transpositions are in $G ;$ since the transpositions generate $S _ { p }$ , this, in turn, implies that $S _ { p } \subset G$ . Since $G \subset S _ { p } ,$ we see that $G = \dot { S } _ { p }$ 

(b): Suppose that $f ( x ) \in K [ x ]$ is a separable irreducible polynomial of degree $p ,$ and let G be the Galois group of $f$ over $K$ . Show that $G$ is a subgroup of $S _ { p } ;$ that $p$ divides the order of $G ;$ and that G contains a p-cycle.

Proof. Let L be the splitting field of $f$ over $K$ . Then L is Galois over K since $f$ is separable. Now, if $a _ { 1 } , \dotsc , a _ { p }$ are the $p$ distinct roots of f (again, f has exactly $p$ distinct roots since it is separable), then any K-automorphism of $L$ is a permutation of the $a _ { i } .$ , so we see that $G = \operatorname { G a l } ( L / K ) \subset S _ { p }$ . Now, $K [ a _ { 1 } ] \subset L$ is a field extension. Since $f$ is satisfied by a1, the minimal polynomial of $a _ { 1 }$ over $K$ must divide $f$ and, hence, since $f$ is irreducible, the minimal polynomial must also be of degree $p .$ . Hence, $[ K [ a _ { 1 } ] : K ] = p$ . Since $L = K [ a _ { 1 } , \dotsc , a _ { p } ]$ ,

$$
\# G = [ L : K ] = [ K [ a _ { 1 } ] : K ] [ K [ a _ { 1 } , a _ { 2 } ] : K [ a _ { 1 } ] ] \cdot \cdot \cdot [ L : k [ a _ { 1 } , \ldots , a _ { p - 1 } ] ] ,
$$

${ \mathrm { s o } } ,$ since $[ K [ a _ { 1 } ] : K ] = p .$ we see that p divides the order of G. Since $p$ divides the order of G, G must contain an element of order $p ,$ by Cauchy’s Theorem. Now, the only elements of $S _ { p }$ of order $p$ are the p-cycles, so we see that $G$ contains a p-cycle. 

(c): Suppose that $f ( x ) \in \mathbb { Q } [ x ]$ is irreducible of degree $p$ and that exactly two of its roots do not lie in R. Let G be the Galois group of $f .$ Show that $G$ contains a transposition, and deduce that $G$ is isomorphic to $S _ { p }$

Proof. Let L be the splitting field of $f .$ . Let $a + b i$ and $a - b i$ be the two non-real roots of $f$ (we know they are of this form, since any non-real roots must come in conjugate pairs). Let $\phi : L \to L$ be the map such that $\phi ( r ) = r$ for all real $r \in L$ and $\phi ( a + b i ) = a - b i$ . Since $L = \mathbb { Q } [ a _ { 1 } , \dots , a _ { p } ]$ where the $a _ { i }$ are the roots of $f , \phi$ in fact defines a Q-automorphism of $L$ , since it simply fixes all the $a _ { i }$ except $a +$ bi and $a - b i$ , which it swaps. Hence, $\phi \in G$ . Since $\phi \circ \phi = i d ,$ , φ has order 2 and so corresponds to a transposition.

Therefore, G contains a transposition and, by our work in (b) above, a p-cycle. Therefore, by the result proved in (a), $G = S _ { p }$ . 

(d): Deduce that $3 x ^ { 5 } - 6 x - 2$ is not solvable by radicals.

Proof. First, note that 2 does not divide 3, 2 does divide −6 and −2, but 4 does not divide −2, so, by Eisenstein’s Criterion, $3 x ^ { 5 } - 6 x - 2$ is irreducible. Let $f ( x ) = 3 x ^ { 5 } - 6 x - 2$ . Then

$$
f ^ { \prime } ( x ) = 1 5 x ^ { 4 } - 6 .
$$

Hence, the only real critical points of f are ${ \sqrt [ 4 ] { \frac { 6 } { 1 5 } } } { \mathrm { ~ a n d - } } { \sqrt [ 4 ] { \frac { 6 } { 1 5 } } } ,$ , so f has at most 2 local extrema and, therefore, $f ( \dot { x } ) = 0$ for at most 3 real values of x. On the other hand, $f ( - 2 ) = - 8 6 , f ( - 1 ) = 1 , f ( 0 ) = - 2$ and $f ( 2 ) = 8 8$ , so, by the intermediate value theorem, $f$ has at least 3 real roots: between −2 and −1, between −1 and $0 ,$ and between 0 and 2. Therefore, $f$ has exactly 3 real roots and, hence, exactly two roots that do not lie in R. Hence, if G is the Galois group of $f$ over Q, G contains a p-cycle by (b) and a transposition by (c), so $G = S _ { 5 }$ 2 by (a). Since $S _ { 5 }$ is not solvable, we see that $f ( x ) = 3 x ^ { 5 } - 6 x - 2$ is not solvable by radicals. 

## 6

For which positive integers n is it possible, with straightedge and compass, to divide any given angle into n equal parts? Prove your assertions.

Answer: We claim that we can n-sect an angle if and only if $n = 2 ^ { r }$ for some $r \in \mathbb N$ . Clearly, by iteratively bisecting an angle, we can $2 ^ { r } .$ -sect an angle for all $r \in \mathbb N$ . On the other hand, note first that if we can mn-sect an angle for some $m , n \in \mathbb { N }$ , then, by taking $m$ of the mn-sections that are adjacent to eachother, we have effectively n-sected the angle. Therefore, it suffices to show that we cannot p-sect an angle for any odd prime p.

Now, suppose $p$ is an odd prime. Note that, as we saw in class, we can construct an angle of $\frac { 2 \pi } { n }$ only if we can construct a regular n-gon. Since we can only construct a regular n-gon if $n = 2 ^ { r } p _ { 1 } \cdots p _ { k }$ for $p _ { i }$ Fermat primes and $2 < p _ { 1 } < . . . < p _ { k }$ , it’s clear that if $p$ is not a Fermat prime, then we cannot construct a regular 6p-gon, and so we cannot construct an angle of $\frac { 2 \pi } { 6 p }$ radians. On the other hand, we can construct the angle $\begin{array} { r } { \frac { \pi } { 3 } = \frac { 2 \pi } { 6 } } \end{array}$ , so this implies that we cannot p-sect the $6 0 ^ { \circ }$ angle. On the other hand, suppose $p$ is a Fermat prime. Then it is possible that we can construct the angle of $\frac { 2 \pi } { 6 p }$ radians. If not, then, again, we cannot $p { \vdash }$ -sect the angle $\frac { \pi } { 3 }$ . If so, then we claim that we cannot $p \mathrm { - }$ sect the constructible angle $\frac { 2 \pi } { 6 p }$ . To see why, simply note that $6 p ^ { 2 }$ is not of the form $2 ^ { r } p _ { 1 } \cdots p _ { k }$ where the $p _ { i }$ are Fermat primes and $2 < p _ { 1 } < . . . < p _ { k }$ , since we have $6 p ^ { 2 } = 2 \cdot 3 \cdot p \cdot p .$ . 3 and $p$ are Fermat primes, but $p \not \prec p$ Therefore, since we cannot construct the regular $6 p ^ { 2 } .$ gon, we cannot construct the angle $\frac { 2 \pi } { 6 p ^ { 2 } }$ , which means we cannot p-sect the constructible angle $\frac { 2 \pi } { 6 p }$

Having examined all cases, we see that we cannot p-sect the angle for any odd prime $p ,$ and so we cannot n-sect an angle unless $n = 2 ^ { r }$ for some $r \in \mathbb N$