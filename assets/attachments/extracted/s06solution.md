1A. Let G be the subgroup of the free abelian group $\mathbb { Z } ^ { 4 }$ consisting of all integer vectors $( x , y , z , w )$ such that $2 x + 3 y + 5 z + 7 w = 0$

(a) Determine a linearly independent subset of G which generates $G$ as an abelian group.

(b) Show that $\mathbb { Z } ^ { 4 } / G$ is a free abelian group and determine its rank.

Solution:

(b) The linear map

$$
\mathbb { Z } ^ { 4 } \mapsto \mathbb { Z } , ( x , y , z , w ) \mapsto 2 x + 3 y + 5 z + 7 w
$$

has kernel G, and is onto because 2 and 3 are relatively prime. Hence $\mathbb { Z } ^ { 4 } / G$ is isomorphic to the image $\mathbb { Z } ,$ which is a free abelian group of rank 1.

(a) There is a sequence of elementary column operations over $\mathbb { Z }$ (not involving divisions) that transforms the 1 × 4-matrix $( 2 ~ \mathrm { ~ 3 ~ ~ 5 ~ ~ 7 ~ } )$ into $\left( \begin{array} { c c c c } { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right)$ . For instance, subtract 3 times the first column from the fourth to get $\left( 2 \ \ \textrm { 3 } \ 5 \ \textrm { 1 } \right)$ , and then subtract appropriate multiples of the fourth from each of the first three columns to make them zero. The same sequence of operations applied to the $4 \times 4$ identity matrix eventually yields a matrix

$$
U = \left( \begin{array} { l l l l } { { 7 } } & { { 9 } } & { { 1 5 } } & { { - 3 } } \\ { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } \\ { { - 2 } } & { { - 3 } } & { { - 5 } } & { { 1 } } \end{array} \right)
$$

such that

$$
\left( 2 \phantom { 0 } 3 \phantom { 0 } 5 \phantom { 0 } 7 \right) U = \left( 0 \phantom { 0 } 0 \phantom { 0 } 0 \phantom { 0 } 1 \right) .
$$

Because of the way U was constructed, it has an inverse $U ^ { - 1 }$ with integer entries.

The first three columns of U are in G, and we claim that they span $G$ as an abelian group. Suppose $\mathbf { v } \in G$ . Then

$$
\begin{array} { r }  0 = \left( 2 \begin{array} { l l l } { 3 } & { 5 } & { 7 \right) \mathbf { v } = \left( 0 } & { 0 } & { 0 } & { 1 \right) U ^ { - 1 } \mathbf { v } , } \end{array} \end{array}
$$

so $U ^ { - 1 } \mathbf { v } = { \binom { \alpha } { \beta } }$ for some $\alpha , \beta , \gamma \in \mathbb { Z }$ . Thus

$$
\mathbf { v } = U \left( \begin{array} { l } { \alpha } \\ { \beta } \\ { \gamma } \\ { 0 } \end{array} \right) ,
$$

which is an integer combination of the first three columns of $U$ .

Finally these first three columns of U are linearly independent, since U is invertible.

2A. Find (with proof) all real numbers c such that the differential equation with boundary conditions

$$
f ^ { \prime \prime } - c f ^ { \prime } + 1 6 f = 0 , \qquad f ( 0 ) = f ( 1 ) = 1
$$

has no solution.

Solution: First suppose that the characteristic equation $x ^ { 2 } - c x + 1 6 = 0$ has a repeated root. This happens when $c = \pm 8$ . If $c = 8$ , the repeated root is 4, and the general solution to the differential equation without boundary conditions has the form

$$
f ( t ) = ( a t + b ) e ^ { 4 t } .
$$

The boundary conditions impose

$$
\begin{array} { r } { b = 1 } \\ { ( a + b ) e ^ { 4 } = 1 , } \end{array}
$$

and this system has a solution. Similarly, there is a solution in the case $c = - 8$

From now on, we suppose that the complex roots $\alpha , \beta$ of $x ^ { 2 } - c x + 1 6 = 0$ are distinct. Then the general solution is

$$
f ( t ) = a e ^ { \alpha t } + b e ^ { \beta t } ,
$$

where a, $b \in \mathbb { C }$ , and the boundary conditions impose

$$
\begin{array} { r } { a + b = 1 } \\ { a e ^ { \alpha } + b e ^ { \beta } = 1 . } \end{array}\tag{1}
$$

This system is guaranteed to have a solution if $e ^ { \alpha } \neq e ^ { \beta }$ . So assume $e ^ { \alpha } = e ^ { \beta }$ . Then $\alpha - \beta =$ 2πik for some $k \in \mathbb { Z }$ . By interchanging $\alpha , \beta ,$ , we may assume $k > 0$ . On the other hand, by the quadratic formula,

$$
( \alpha - \beta ) ^ { 2 } = c ^ { 2 } - 6 4 .
$$

Thus $4 \pi ^ { 2 } k ^ { 2 } = 6 4 - c ^ { 2 } \leq 6 4 $ . The only possibility is $k = 1$ , which leads to $c = \pm { \sqrt { 6 4 - 4 \pi ^ { 2 } } }$ In this case $e ^ { \alpha } = e ^ { \beta }$ , but the common value is not 1, since $e ^ { \alpha } e ^ { \beta } = e ^ { \alpha + \beta } = e ^ { c } \neq e ^ { 0 } = 1$ . So the system (1) has no solution.

Thus the set of values c for which the differential equation with boundary conditions has√ no solution is $\{ \pm { \sqrt { 6 4 - 4 \pi ^ { 2 } } } \}$

3A. Let $S = \{ ( x _ { 1 } , \ldots , x _ { n } ) \in \mathbb { R } ^ { n } \mid x _ { 1 } + \cdot \cdot \cdot + x _ { n } = 0 \}$ . Find (with justification) the $n \times n$ matrix P of the orthogonal projection from $\mathbb { R } ^ { n }$ onto S. That is, P has image S, and $P ^ { 2 } = P = P ^ { T }$

Solution: The orthogonal complement of S is one-dimensional, and spanned by the unit vector $\begin{array} { r } { w = \frac { 1 } { \sqrt { n } } ( 1 , \dots , 1 ) } \end{array}$ , because $v \in S \Leftrightarrow \langle v , w \rangle = 0$ . So the orthogonal projection is given by $\begin{array} { r } { P v = v \dot { - } \langle v , w \rangle w = v - \frac { v _ { 1 } + \dots + v _ { n } } { n } ( 1 , \dots , 1 ) } \end{array}$ . Therefore

$$
P = \operatorname { I d } - w ^ { T } w = \left( \begin{array} { c c c c } { \frac { n - 1 } { n } } & { \frac { - 1 } { n } } & { \cdot \cdot } & { \frac { - 1 } { n } } \\ { \frac { - 1 } { n } } & { \frac { n - 1 } { n } } & { \cdot \cdot } & { \frac { - 1 } { n } } \\ { \vdots } & { \cdot } & { \vdots } \\ { \frac { - 1 } { n } } & { \frac { - 1 } { n } } & { \cdot \cdot } & { \frac { n - 1 } { n } } \end{array} \right) .
$$

4A. Let $D = \{ z \in \mathbb { C } : | z | < 1 \}$ . Find all holomorphic functions $f \colon D  \mathbb { C }$ such that $f ( { \frac { 1 } { n } } + i e ^ { - n } )$ is real for all integers $n \geq 2$

Solution: We show that the only such functions are the real constant functions. Let

$$
f ( z ) = \sum a _ { n } z ^ { n }
$$

be the Taylor series for $f$ around 0. We first prove by contradiction that $a _ { k }$ are real. Suppose that k is the smallest index so that Im $. a _ { k } \neq 0$ . Then we must have

$$
\mathrm { I m } a _ { k } = \operatorname* { l i m } _ { x \to 0 , x \in \mathbb { R } } x ^ { - k } \mathrm { I m } f ( x )
$$

On the other hand, because there is a bound on $f ^ { \prime } ( z )$ in a closed disk containing all the numbers $\textstyle { \frac { 1 } { n } } + i e ^ { - n }$

$$
\mathrm { I m } f \bigl ( { \frac { 1 } { n } } \bigr ) = \mathrm { I m } f \bigl ( { \frac { 1 } { n } } + i e ^ { - n } \bigr ) + O \bigl ( e ^ { - n } \bigr ) = O \bigl ( e ^ { - n } \bigr )
$$

as $n \to \infty$ . Hence

$$
\operatorname { I m } a _ { k } = \operatorname* { l i m } _ { n \to \infty } n ^ { k } \mathrm { I m } f ( { \frac { 1 } { n } } ) = 0 ,
$$

which is a contradiction. As a consequence, $f ( { \frac { 1 } { n } } )$ must be real.

By bounding $f ^ { \prime \prime } ( z )$ on a closed disk, we may write

$$
f ( \frac { 1 } { n } + i e ^ { - n } ) = f ( \frac { 1 } { n } ) + i e ^ { - n } f ^ { \prime } ( \frac { 1 } { n } ) + O ( e ^ { - 2 n } )
$$

Taking imaginary parts we get

$$
\operatorname { R e } f ^ { \prime } ( { \frac { 1 } { n } } ) = O ( e ^ { - n } )
$$

Arguing as above, the Taylor series at 0 for $f ^ { \prime } ( z )$ has purely imaginary coefficients. We conclude that all ${ a } _ { k } { } ^ {  ' } \mathrm { s }$ must vanish with the exception of $a _ { 0 }$

5A. Consider the following four commutative rings:

$$
\mathbb { Z } , \mathbb { Z } [ x ] , \mathbb { R } [ x ] , \mathbb { R } [ x , y ] .
$$

Which of these rings contains a nonzero prime ideal that is not a maximal ideal?

Solution: In the ring of integers Z the nonzero prime ideals are $\langle p \rangle$ , where p is a prime number. Each of these ideals is maximal since $\mathbb { F } _ { p } = \mathbb { Z } / \langle p \rangle$ is a field. Hence every nonzero prime ideal in $\mathbb { Z }$ is maximal.

The polynomial ring $\mathbb { Z } [ x ]$ in one variable x over the ring of integers Z is not a principal ideal domain. For instance, $\langle 2 , x \rangle$ is not a principal ideal; it strictly contains the ideal $\langle 2 \rangle$ , which is therefore not a maximal ideal. The ideal h2i is a prime ideal, because $\mathbb { Z } [ x ] / \langle 2 \rangle = \mathbb { F } _ { 2 } [ x ]$ is a polynomial ring over a field, and hence an integral domain. Hence h2i is a nonzero prime ideal in $\mathbb { Z } [ x ]$ which is not maximal.

The polynomial ring $\mathbb { R } [ x ]$ in one variable x over the field R is a principal ideal domain. Hence every nonzero ideal has the form $\langle f ( x ) \rangle$ where $f ( x )$ is a nonzero polynomial with real coefficients. The ideal is prime if and only if $f ( x )$ is an irreducible polynomial, i.e., if $f ( x )$ is a linear polynomial or $f ( x )$ is a quadratic polynomial with no real roots. In either case, the quotient $\mathbb { R } [ x ] / \langle f \rangle$ is a field, namely, either R or C, which means that $\langle f \rangle$ is a maximal ideal. Hence every nonzero prime ideal in $\mathbb { R } [ x ]$ is a maximal ideal.

The polynomial ring $\mathbb { R } [ x , y ]$ in two variables $x , y$ over R has many nonzero prime ideals which are not maximal ideals. For instance, hxi is a prime ideal, but it is not maximal since it is contained in the ideal $\langle x , y \rangle$

6A. Let $u \colon  { \mathbb { R } } \to  { \mathbb { R } }$ be a function for which there exists $B > 0$ such that

$$
\sum _ { k = 1 } ^ { N - 1 } | u ( x _ { k + 1 } ) - u ( x _ { k } ) | ^ { 2 } \leq B
$$

for all finite increasing sequences $x _ { 1 } < x _ { 2 } < \dots < x _ { N }$ . Show that u has at most countably many discontinuities.

Solution: Let A be the set of points of discontinuity for u. Then

$$
A = \bigcup _ { n \geq 1 } A _ { n }
$$

where

$$
A _ { n } = \{ x \in \mathbb { R } : | \operatorname* { l i m } _ { y \to x } \operatorname* { s u p } u ( y ) - \operatorname* { l i m } _ { y \to x } \operatorname* { i n f } u ( y ) | > \frac { 1 } { n } \}
$$

To prove that A is countable, we will prove that

$$
\left| A _ { n } \right| \leq 4 n ^ { 2 } B .
$$

If $y _ { 1 } < y _ { 2 } < \dots < y _ { N }$ are in $A _ { n }$ then we can choose a strictly increasing sequence $( x _ { k } ) _ { k = 1 } ^ { 2 N }$ such that

$$
x _ { 2 k - 1 } < y _ { k } < x _ { 2 k }
$$

and

$$
| u ( x _ { 2 k } ) - u ( x _ { 2 k - 1 } ) | > \frac { 1 } { 2 n }
$$

for $k = 1 , \ldots , N$ . Summing over k gives the inequality on the right in

$$
B \geq \sum _ { k = 1 } ^ { 2 N - 1 } | u ( x _ { k + 1 } ) - u ( x _ { k } ) | ^ { 2 } \geq \sum _ { k = 1 } ^ { N } | u ( x _ { 2 k } ) - u ( x _ { 2 k - 1 } ) | ^ { 2 } \geq N \left( \frac { 1 } { 2 n } \right) ^ { 2 } .
$$

Hence $N \leq 4 n ^ { 2 } B .$ , which concludes the proof.

7A. Recall that $\mathrm { S L } ( 2 , \mathbb { R } )$ denotes the group of real $2 \times 2$ matrices of determinant 1. Suppose that $A \in \mathrm { S L } ( 2 , \mathbb { R } )$ does not have a real eigenvalue. Show that there exists $B \in \mathrm { S L } ( 2 , \mathbb { R } )$ such that $B A B ^ { - 1 }$ equals a rotation matrix $\left( \begin{array} { c c } { \cos \theta } & { - \sin \theta } \\ { \sin \theta } & { \cos \theta } \end{array} \right)$ for some $\theta \in \mathbb { R }$

Solution: Since the eigenvalues of A are solutions to a real quadratic equation, they are complex conjugates of each other, call them λ and λ. Since det $( A ) = 1$ , it follows that $\lambda \overline { { \lambda } } = 1$ , i.e. λ and $\bar { \lambda }$ are on the unit circle. Write $\lambda = \cos \theta + i$ sin θ. Pick a nonzero eigenvector $z \in \mathbb { C } ^ { 2 }$ with $A z = \lambda z$ . Write $z = v + i w$ with $v , w \in \mathbb { R } ^ { 2 }$ Taking the real and imaginary parts of the equation $A z = \lambda z \ \mathrm { g }$ ives the equations $A v = ( \cos \theta ) v - ( \sin \theta ) w$ , $A w = ( \sin \theta ) v + ( \cos \theta ) w$ Note also that $A ( v - i w ) = \overline { { { \lambda } } } ( v - i w )$ and $\lambda \neq { \overline { { \lambda } } } .$ , so $v + i w$ and $v - i w$ are linearly independent over C, so v and w are linearly independent over R. We can find $B \in \mathrm { S L } ( 2 , \mathbb { R } )$ taking the basis $\{ v , w \}$ to a real multiple of the standard basis for $\mathbb { R } ^ { 2 }$ Then $B A B ^ { - 1 } = \binom { \cos \theta } { - \sin \theta } \quad \sin \theta \quad$ . This is of the desired form, with θ in place of $- \theta .$

8A. Let $D = \{ z \in \mathbb { C } : | z | < 1 \}$ . Let $f \colon D  \mathbb { C }$ be holomorphic, and suppose that the restriction of $f$ to $D - \{ 0 \}$ is injective. Prove that $f$ is injective.

Solution: Suppose on the contrary that there is $a \in D - \{ 0 \}$ such that $f ( a ) = f ( 0 )$ . Let α be the common value. Choose disjoint open disks $D _ { 0 }$ and $D _ { a }$ contained in D, centered at 0 and a, respectively. By the Open Mapping Theorem $f ( D _ { 0 } )$ and $f ( D _ { a } )$ are open subsets of C containing α. Hence $G : = f ( D _ { 0 } ) \cap f ( D _ { a } )$ is a nonempty open subset of C. Choose $\xi \in G$ with $\xi \neq \alpha$ . Then there exist $z _ { 0 } \in D _ { 0 }$ and $z _ { a } \in D _ { a }$ such that $f ( z _ { 0 } ) = f ( z _ { a } ) = \xi$ . Since $\xi \neq \alpha$ , neither $z _ { 0 }$ nor $z _ { a }$ is 0. This contradicts the injectivity of f restricted to $D - \{ 0 \}$

9A. Let $p$ be a prime. Let G be a finite non-cyclic group of order $p ^ { m }$ for some m. Prove that G has at least $p + 3$ subgroups.

Solution: We will use the following two facts:

(i) A nontrivial p-group has a nontrivial center Z (nontrivial conjugacy classes have size divisible by $p ,$ as does the whole group, so {1} cannot be the only trivial one).

(ii) If G is a group with center $Z _ { i }$ , and $G / Z$ is cyclic, then G is abelian (since if $a \in G$ generates $G / Z$ , every element of $G$ is of the form $a ^ { n } z$ for some $n \in \mathbb { Z }$ and $z \in Z )$ We use induction on m.

Suppose $m \le 2$ Since G has order 1, $p ,$ or $p ^ { 2 }$ , it is abelian (for order $p ^ { 2 }$ , combine (i) and (ii) above). Since it is not cyclic, we have $G \simeq \mathbb { Z } / p \mathbb { Z } \times \mathbb { Z } / p \mathbb { Z }$ . So G has one trivial subgroup, $( p ^ { 2 } - 1 ) / ( p - 1 ) = p + \bar { 1 }$ subgroups of order $p ,$ and G itself. Thus G has exactly $p + 3$ subgroups.

Now suppose $m > 2$ By (i), the center $Z$ of G is nontrivial. Since G is a nontrivial $p { \mathrm { - g r o u p } }$ , it has a nontrivial center Z. If $G / Z$ is non-cyclic, then by the inductive hypothesis it has $\geq p + 3$ subgroups, and their inverse images in G are distinct subgroups of G. If $G / Z$ is cyclic, then G is abelian by (ii); but G is not cyclic, so by the structure theory of finite abelian groups, it must contain $\mathbb { Z } / p \mathbb { Z } \times \mathbb { Z } / p \mathbb { Z }$ , which already contains $p + 3$ subgroups.

1B. Let $A _ { 1 } \supseteq A _ { 2 } \supseteq \cdots$ · be compact connected subsets of $\mathbb { R } ^ { n }$ . Show that the set $A = \cap A _ { m }$ is connected.

Solution: The intersection A is nonempty, since otherwise $\left\{ A _ { 1 } - A _ { m } \right\}$ is a covering of $A _ { 1 }$ (by sets open in $A _ { 1 } )$ with no finite subcover.

Suppose that A is not connected. Then there exist sets $B _ { 0 } , C _ { 0 }$ open in A such that $B _ { 0 } \cup C _ { 0 } = A$ and $B _ { 0 } \cap C _ { 0 } = \varnothing$ . Then $B _ { 0 } , C _ { 0 }$ are also closed in A, which (as an intersection of closed sets) is closed in Rn, so $B _ { 0 } , C _ { 0 }$ are closed in $\mathbb { R } ^ { n }$ . Hence we can find disjoint sets $B , C$ open in $A _ { 1 }$ such that $B _ { 0 } \subseteq B , C _ { 0 } \subseteq C .$ : for instance, we could let B be the set of points in $A _ { 1 }$ that are strictly closer to $B _ { 0 }$ than to $C _ { 0 }$ , and vice versa for C.

Since $A = B _ { 0 } \cup C _ { 0 } \subseteq B \cup C$ , the sets $B , C _ { i }$ , and $A _ { 1 } - A _ { m }$ for $m \geq 1$ form a cover of $A _ { 1 }$ by sets open in $A _ { 1 } ;$ thus there is a finite subcover consisting of $B , C .$ , and $A _ { 1 } - A _ { m }$ for $m = 1 , \ldots , r .$ . So r is such that $A _ { r } \subseteq B \cup C$ Since $B , C$ are open, disjoint, and $B \cap A _ { r } \supseteq B _ { 0 } \cap A \neq \emptyset$ and $C \cap A _ { r } \supseteq C _ { 0 } \cap A \neq \emptyset$ , we have that $A _ { r }$ is not connected, a contradiction.

2B. Let $\mathbb { F } _ { 2 }$ be the field of 2 elements. Let n be a prime. Show that there are exactly $( 2 ^ { n } - 2 ) / n$ degree-n irreducible polynomials in $\mathbb { F } _ { 2 } [ x ]$

Solution: There is a unique field extension $\mathbb { F } _ { 2 ^ { r } }$ n of degree n over $\mathbb { F } _ { 2 }$ . It is Galois over $\mathbb { F } _ { 2 }$ (this is because it is a splitting field for the separable polynomial $x ^ { 2 ^ { n } } - x )$ x). If $a \in \mathbb { F } _ { 2 ^ { n } } - \mathbb { F } _ { 2 }$ then $\mathbb { F } _ { 2 } ( a )$ is a subfield of $\mathbb { F } _ { 2 ^ { n } }$ of degree dividing n but not equal to 1, so $\mathbb { F } _ { 2 } ( a ) = \mathbb { F } _ { 2 ^ { n } }$ . Hence the minimal polynomial $f _ { a }$ of a over $\mathbb { F } _ { 2 }$ is an irreducible polynomial of degree n over $\mathbb { F } _ { 2 }$ Thus we have a map

$$
\begin{array} { l } { { ( \mathbb { F } _ { 2 ^ { n } } - \mathbb { F } _ { 2 } ) \longrightarrow \{ \mathrm { d e g r e e } { - } n \mathrm { ~ i r r e d u c i b l e ~ p o l y n o m i a l s ~ i n ~ } \mathbb { F } _ { 2 } [ x ] \} } } \\ { { a \longmapsto f _ { a } . } } \end{array}
$$

On the other hand, if $f \in \mathbb { F } _ { 2 } [ x ]$ is any degree-n irreducible polynomial, then f has a zero in $\mathbb { F } _ { 2 ^ { n } }$ (since $\mathbb { F } _ { 2 ^ { n } }$ is the unique degree-n extension of $\mathbb { F } _ { 2 } )$ and it follows that f has n distinct zeros in $\mathbb { F } _ { 2 ^ { n } }$ (since $\mathbb { F } _ { 2 ^ { n } }$ is Galois over $\mathbb { F } _ { 2 } )$ . Moreover, f is automatically monic (the only nonzero element of $\mathbb { F } _ { 2 }$ is 1) so it is the minimal polynomial of each of its zeros. Thus our map is n-to-1.

Its domain has size $2 ^ { n } - 2 .$ , so its range has size $( 2 ^ { n } - 2 ) / n$

3B. Evaluate the integral

$$
\int _ { - \infty } ^ { \infty } { \frac { e ^ { i t x } } { e ^ { x } + e ^ { - x } } } d x
$$

for $t > 0$

Solution: The integral converges absolutely, since the numerator has absolute value 1, while the denominator decays exponentially in both directions.

Use a rectangular contour C bounded by $x = R , x = - R , y = 0$ and $y = \pi$ . As $R \to \infty$ the integrals along the vertical parts of the contour tend to 0, since

$$
\left| \int _ { 0 } ^ { \pi } { \frac { e ^ { i t ( R + i y ) } } { e ^ { R + i y } + e ^ { - R - i y } } } d y \right| \leq \int _ { 0 } ^ { \pi } { \frac { 1 } { e ^ { R } - e ^ { - R } } } d y = { \frac { \pi } { e ^ { R } - e ^ { - R } } } .
$$

The integral along the horizontal path $y = \pi$ equals

$$
\int _ { R } ^ { - R } \frac { e ^ { i t ( x + \pi i ) } } { e ^ { ( x + \pi i ) } + e ^ { - ( x + \pi i ) } } d x = \int _ { R } ^ { - R } \frac { e ^ { - \pi t } e ^ { i t x } } { - e ^ { x } - e ^ { - x } } d x = e ^ { - \pi t } \int _ { - R } ^ { R } \frac { e ^ { i t x } } { e ^ { x } + e ^ { - x } } d x .
$$

Let I denote the integral we have to find. Then

$$
\operatorname* { l i m } _ { R  \infty } \oint _ { C } { \frac { e ^ { i t z } } { e ^ { z } + e ^ { - z } } } d z = ( 1 + e ^ { - \pi t } ) I .
$$

On the other hand,

$$
\oint _ { C } { \frac { e ^ { i t z } } { e ^ { z } + e ^ { - z } } } d z = 2 \pi i \operatorname { R e s } _ { \frac { \pi i } { 2 } } ,
$$

since the only singular point inside the contour is $\textstyle { \frac { \pi i } { 2 } }$ . Now

$$
\mathrm { R e s } _ { \frac { \pi i } { 2 } } = \frac { e ^ { - \frac { \pi t } { 2 } } } { 2 i } ,
$$

so

$$
\oint _ { C } { \frac { e ^ { i t z } } { e ^ { z } + e ^ { - z } } } d z = \pi e ^ { - { \frac { \pi t } { 2 } } } ,
$$

$$
I = \pi \frac { e ^ { - \frac { \pi t } { 2 } } } { 1 + e ^ { - \pi t } } = \frac { \pi } { e ^ { \frac { \pi t } { 2 } } + e ^ { - \frac { \pi t } { 2 } } } .
$$

4B. Let n be a positive integer, and let ${ \mathrm { G L } } _ { n } ( \mathbb { R } )$ be the group of invertible $n \times n$ matrices. Let S be the set of $A \in \operatorname { G L } _ { n } ( \mathbb { R } )$ such that $A - I$ has rank $\leq 2$ . Prove that S generates ${ \mathrm { G L } } _ { n } ( \mathbb { R } )$ as a group.

Solution: By Gaussian elimination, ${ \mathrm { G L } } _ { n } ( \mathbb { R } )$ is generated by the elementary matrices obtained from the identity matrix by interchanging two rows, by multiplying one row by a nonzero scalar, or by adding a multiple of one row to a different row. For each such matrix A, the matrix $A - I$ has at most two nonzero rows and hence has rank $\leq 2 .$

5B. Prove that there exists no continuous bijection from (0, 1) to [0, 1]. (Recall that a bijection is a map that is both one-to-one and onto.)

Solution: Suppose on the contrary that there exists a continuous bijection $f \colon ( 0 , 1 ) $ $[ 0 , 1 ]$ . Then there exists $x \in ( 0 , 1 )$ such that $f ( x ) = 0$ . Let $A = ( 0 , x ) , B = ( x , 1 )$ . We have ${ \overset { \cdot } { A } } \cap B = \emptyset$ and since f is injective we have

$$
f ( A ) \cap f ( B ) = f ( A \cap B ) = \emptyset .\tag{∗}
$$

Since f is continuous and $( 0 , x ]$ is connected, $f ( \left( 0 , x \right] )$ contains an interval $[ 0 , a )$ for some $a > 0$ . Hence $f ( A )$ contains $( 0 , a )$ . Similarly, $f ( B )$ contains (0, b) for some $b > 0$ . This gives $f ( A ) \cap f ( B ) \neq \emptyset$ . Contradiction to (∗).

6B. Let A be the subring of $\mathbb { R } [ t ]$ consisting of polynomials $f ( t )$ such that $f ^ { \prime } ( 0 ) = 0$ . Is A a principal ideal domain?

Solution: No. Suppose A is a principal ideal domain. Then the A-ideal I generated by $t ^ { 2 }$ and $t ^ { 3 }$ would be principal. Let $p ( t )$ be a generator of I. Then $t ^ { 2 } = q ( t ) p ( t )$ for some $q ( t ) \in A$ , so $p ( t )$ divides $t ^ { 2 }$ also in the unique factorization domain R[t]. Hence $p ( t ) = u t ^ { m }$ for some unit u of R[t] and some $m \in \{ 0 , 1 , 2 \}$ . The case $m = 1$ is impossible, since $p ( t ) \in A$ If $m = 0$ , then $p ( t )$ is a unit also of A, and hence generates the unit ideal; this contradicts the fact that every element of I has constant term zero. If $m = 2$ , then $t ^ { 3 }$ is not a multiple of $p ( t )$ , since the element $t ^ { 3 } / p ( t ) \in \mathbb { R } [ t ]$ is not in A.

7B. Let m be a fixed positive integer.

(a) Show that if an entire function $f \colon \mathbb { C } \to \mathbb { C }$ satisfies $| f ( z ) | \leq e ^ { | z | }$ for all $z \in \mathbb { C }$ , then

$$
\vert f ^ { ( m ) } ( 0 ) \vert \leq \frac { m ! e ^ { m } } { m ^ { m } } .
$$

(b) Prove that there exists an entire function $f$ such that $| f ( z ) | \leq e ^ { | z | }$ for all z and

$$
\vert f ^ { ( m ) } ( 0 ) \vert = \frac { m ! e ^ { m } } { m ^ { m } } .
$$

Solution:

(a) Write $\begin{array} { r } { f ( z ) = \sum _ { n > 0 } a _ { n } z ^ { n } } \end{array}$ with $a _ { n } \in \mathbb { C }$ . Then $a _ { m }$ is the coefficient of $z ^ { - 1 }$ in the Laurent series of $f ( z ) / z ^ { m + 1 }$ , so

$$
a _ { m } = \frac { 1 } { 2 \pi i } \int _ { | z | = R } \frac { f ( z ) } { z ^ { m } } \frac { d z } { z } ,
$$

for any $R > 0$ , and we get

$$
| a _ { m } | \leq \frac { 1 } { 2 \pi } \left( \frac { e ^ { R } } { R ^ { m } } \right) \frac { 2 \pi R } { R } = \frac { e ^ { R } } { R ^ { m } } .
$$

Taking $R = m$ (which calculus shows minimizes the right hand side) and multiplying by m! gives

$$
| f ^ { ( m ) } ( 0 ) | = | m ! a _ { m } | \leq \frac { m ! e ^ { m } } { m ^ { m } } .
$$

(b) Examining the proof of part (a) shows also that in order to have equality, $\frac { f ( z ) } { z ^ { m } }$ must have constant modulus $e ^ { m } / m ^ { m }$ and constant argument on the circle $| z | = m$ . Thus we guess $\begin{array} { r } { f ( z ) = \frac { e ^ { m } } { m ^ { m } } z ^ { m } } \end{array}$ , and it remains to prove that $| f ( z ) | \leq e ^ { | z | }$ for all $z \in \mathbb { C }$ . Equivalently, we must show that the minimum value of $e ^ { x } / x ^ { m }$ on $( 0 , \infty )$ is $e ^ { m } / m ^ { m }$ . This can be seen by observing that the only zero of the derivative of log $\ u _ { \ u { \ u { \ u { \ u { \ u { \ u { \chi } } } } } } } ( e ^ { x } / x ^ { m } ) = x - m$ log x is at $x = m$ , while the second derivative is positive everywhere (it is $m / x ^ { 2 } )$

8B. Let $\langle ~ , ~ \rangle$ be the standard Hermitian inner product on Cn. Let A be an $n \times n$ matrix with complex entries. Suppose $\langle x , A x \rangle$ is real for all $x \in \mathbb { C } ^ { n }$ . Prove that A is Hermitian.

Solution: We have $\langle x , A x \rangle = x ^ { H } A x = { \overline { { x ^ { H } A x } } }$ (since xHAx is real) $= ( x ^ { H } A x ) ^ { H } = x ^ { H } A ^ { H } x$ Thus $x ^ { H } A x = x ^ { H } A ^ { H } x$ . So $\overset { \cdot } { x ^ { H } } ( A - A ^ { H } ) \overset { \cdot } { x } = 0$ for all $x \in \mathbb { C } ^ { n }$ . Let $\dot { B } = \dot { A } - A ^ { H }$ . We have

$$
x ^ { H } B x = 0\tag{∗}
$$

for all $x \in \mathbb { C } ^ { n }$ and $B ^ { H } = A ^ { H } - A = - B$ , so B is skew-Hermitian (hence normal). Let x be an eigenvector of B with the eigenvalue λ, so $B x = \lambda x$ Then $\overset { \vartriangle } { \boldsymbol { 0 } } = \boldsymbol { x } ^ { H } \boldsymbol { B } \boldsymbol { x }$ (by (∗)) $= \lambda x ^ { H } x = { \bar { \lambda } } \| x \| ^ { 2 }$ This gives $\lambda = 0$ Thus all eigenvalues of B are zero. Being normal, B is diagonalizable, so $B = 0$ . By definition of B, we get $A = A ^ { H }$ . Thus A is Hermitian.

9B. Find a bounded non-convergent sequence of real numbers $( a _ { n } ) _ { n \geq 1 }$ such that

$$
| 2 a _ { n } - a _ { n - 1 } - a _ { n + 1 } | \leq n ^ { - 2 }
$$

for all $n \geq 2 .$

Solution: We will let $a _ { n } = f ( n )$ , where $f ( x )$ is a function similar to the sine function but with oscillations that slow down as $x \longrightarrow \infty .$ , so that $f ^ { \prime \prime } ( x )  0$ . To be precise, we take

$$
f ( x ) : = { \frac { 1 } { 2 } } \sin ( \ln ( x + 1 ) ) .
$$

This sequence is bounded. It also does not converge, since the spacing between values of ln n tends to zero, which means that the values of (ln n) mod (2π) are dense in [0, 2π].

By Taylor’s theorem with remainder (centered at n),

$$
f ( n + 1 ) = f ( n ) + f ^ { \prime } ( n ) + { \frac { 1 } { 2 } } f ^ { \prime \prime } ( \xi _ { + } ) \quad { \mathrm { f o r ~ s o m e ~ } } \xi _ { + } \in ( n , n + 1 ) , { \mathrm { ~ a n d ~ } }
$$

$$
f ( n - 1 ) = f ( n ) - f ^ { \prime } ( n ) + { \frac { 1 } { 2 } } f ^ { \prime \prime } ( \xi _ { - } ) \quad \mathrm { f o r ~ s o m e ~ } \xi _ { - } \in ( n - 1 , n ) , \mathrm { ~ s o } ,
$$

$$
| 2 f ( n ) - f ( n - 1 ) - f ( n + 1 ) | = { \frac { 1 } { 2 } } | f ^ { \prime \prime } ( \xi _ { + } ) + f _ { \cdot } ^ { \prime \prime } ( \xi _ { - } ) | = | f ^ { \prime \prime } ( \xi ) | \quad { \mathrm { f o r ~ s o m e ~ } } \xi \in ( \xi _ { - } , \xi ^ { + } ) \subseteq ( n - 1 , n + 1 )
$$

by the intermediate value theorem. We compute

$$
f ^ { \prime } ( x ) = { \frac { 1 } { 2 ( x + 1 ) } } \cos ( \ln ( x + 1 ) )
$$

$$
f ^ { \prime \prime } ( x ) = - \frac { 1 } { 2 ( x + 1 ) ^ { 2 } } \left( \cos ( \ln ( x + 1 ) ) + \sin ( \ln ( x + 1 ) ) \right) ,
$$

$$
| f ^ { \prime \prime } ( x ) | \leq { \frac { 1 } { ( x + 1 ) ^ { 2 } } }
$$

$$
| f ^ { \prime \prime } ( \xi ) | \leq \frac { 1 } { ( \xi + 1 ) ^ { 2 } } \leq \frac { 1 } { n ^ { 2 } } .
$$

so

$$
| 2 a _ { n } - a _ { n - 1 } - a _ { n + 1 } | = | f ^ { \prime \prime } ( \xi ) | \leq n ^ { - 2 } .
$$