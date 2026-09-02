Instructions: Do as many of the eight problems as you can.
Four completely correct solutions will be a pass; a few complete solutions will count more than many partial solutions.
Always carefully justify your answers.
If you skip a step or omit some details in a proof, point out the gap and, if possible, indicate what would be required to fill it in.

1. (a) Classify groups of order $2 0 0 9 = 7 ^ { 2 } \times 4 1$

(b) Suppose that F is a field and $K / F$ is a Galois extension of degree 2009. How many intermediate fields are there – that is, how many fields L are there with $F \subset L \subset K$ , both inclusions proper?
(There may be several cases to consider.)

2. Let K be a field.
   A discrete valuation on K is a function $\nu : K \backslash \{ 0 \}  \mathbb { Z }$ such that

(i) $\nu ( a b ) = \nu ( a ) + \nu ( b )$

(ii) ν is surjective

$$
\mathrm { ( i i i ) ~ } \nu ( a + b ) \geq \operatorname* { m i n } \{ \nu ( a ) , \nu ( b ) \} \forall a , b \in K \backslash \{ 0 \} \mathrm { ~ w i t h ~ } a + b \neq 0
$$

Let $R : = \{ x \in K \backslash \{ 0 \} : \nu ( x ) \geq 0 \} \cup \{ 0 \}$ . Then R is called the valuation ring of ν.

Prove the following:

(a) R is a subring of K containing the 1 in K.

(b) for all $x \in K \backslash \{ 0 \}$ , either $x \ \mathrm { o r } \ x ^ { - 1 }$ is in R.

(c) x is a unit of R if and only if $\nu ( x ) = 0$

(d) Let p be a prime number, $K = \mathbb { Q }$ and $\nu _ { p } : \mathbb { Q } \backslash \{ 0 \}  \mathbb { Z }$ be the function defined by $\begin{array} { r } { \nu _ { p } ( \frac { a } { b } ) = n } \end{array}$ where ${ \begin{array} { l } { { \frac { a } { b } } \ = \ p ^ { n } { \frac { c } { d } } } \end{array} }$ and p does not divide c and d. Prove that the corresponding valuation ring R is the ring of all rational numbers whose denominators are relatively prime to p.

3. Let F be a field of characteristic not equal to 2.

(a) Prove that any extension K of F of degree 2 is of the form $F ( \sqrt { D } )$ where $D \in F$ is not a square in F and conversely, that each such extension has degree 2 over F .

(b) Let $D _ { 1 } , D _ { 2 } \in F$ neither of which is a square in F . Prove that $[ F ( \sqrt { D _ { 1 } } , \sqrt { D _ { 2 } } )$ $F ] = 4 \mathrm { i f } D _ { 1 } D _ { 2 }$ is not a square in F and is of degree 2 otherwise.

4. Let F be a field and $p ( x ) \in F [ x ]$ an irreducible polynomial.

(a) Prove that there exists a field extension K of F in which $p ( x )$ has a root.

(b) Determine the dimension of K as a vector space over F and exhibit a vector space basis for K.

(c) If $\theta \in K$ denotes a root of $p ( x )$ , express $\theta ^ { - 1 }$ in terms of the basis found in part (b).

(d) Suppose $p ( x ) = x ^ { 3 } + 9 x + 6$ . Show $p ( x )$ is irreducible over Q. If θ is a root of $p ( x )$ , compute the inverse of $( 1 + \theta )$ in $\mathbb { Q } ( \theta )$

5. Let R be a ring and Q an R-module.
   According to Baer’s criterion, Q is injective if and only if for every ideal I of R, any R-module map $f : I  Q$ may be extended to an R-module map $g : R  Q$

<!-- image-->

(a) Suppose that p is prime and n is a positive integer with p dividing n. Then multiplication makes $\mathbb { Z } / p \mathbb { Z }$ into a module over the ring $\mathbb { Z } / n \mathbb { Z }$ . Show that $\mathbb { Z } / p \mathbb { Z }$ is injective as a $\mathbb { Z } / n \mathbb { Z }$ -module if and only if $p ^ { 2 }$ does not divide n.

(b) Prove that if R is a PID, then an R-module Q is injective if and only if $r Q = Q$ for every nonzero $r \in R$

6. Fix a ring R, an R-module M, and an R-module homomorphism $f : M \to M$

(a) If M satisfies the descending chain condition on submodules, show that if f is injective, then f is surjective.
(Hint: note that if f is injective, so are $f \circ f , f \circ f \circ f , \mathrm { e t c . } )$

(b) Give an example of a ring R, an R-module M, and an injective R-module homomorphism $f : M \to M$ which is not surjective.

(c) If M satisfies the ascending chain condition on submodules, show that if f is surjective, then f is injective.

(d) Give an example of a ring R, an R-module M, and a surjective R-module homomorphism $f : M \to M$ which is not injective.

7. Let G be a finite group, k an algebraically closed field, and V an irreducible k-linear representation of G.

(a) Show that ${ \mathrm { H o m } } _ { k G } ( V , V )$ is a division algebra with k in its center.

(b) Show that V is finite-dimensional over k, and conclude that ${ \mathrm { H o m } } _ { k G } ( V , V )$ is also finite-dimensional.

(c) Show the inclusion $k  \mathrm { H o m } _ { k G } ( V , V )$ found in (a) is an isomorphism.
(For $f \in \mathrm { H o m } _ { k G } ( V , V )$ , view f as a linear transformation and consider $f - \alpha I ,$ , where α is an eigenvalue of $f . )$

8. Recall the following basic definitions and facts about ideals and varieties.
   Let k be a field and n be a positive integer.

• If $S \subseteq k ^ { n }$ , the ideal of S is ${ \mathcal { T } } ( S ) : = \{ f \in k [ x _ { 1 } , \ldots , x _ { n } ] : f ( s ) = 0 \forall s \in$ $S \} . \ T ( S )$ is a radical ideal in $k [ x _ { 1 } , \dots , x _ { n } ]$

• If $I \subseteq k [ x _ { 1 } , \ldots , x _ { n } ]$ is an ideal, then the variety of I in $k ^ { n }$ is $\mathcal { V } ( I ) : = \{ s \in$ $k ^ { n } : f ( s ) = 0 \forall f \in I \}$

• If $S \subseteq k ^ { n }$ , then $\nu ( \pi ( S ) )$ is the smallest variety containing S and is called the Zariski closure of S, denoted as S.

• Hilbert’s Nullstellensatz: If k is algebraically closed and I is an ideal in $k [ x _ { 1 } , \dots , x _ { n } ]$ then $\mathcal { T } ( \mathcal { V } ( I ) ) = \sqrt { I }$ , where I is the radical of I.

(a) If I and J are ideals in $k [ x _ { 1 } , \dots , x _ { n } ]$ , the ideal quotient of I by J is

$$
I : J = \{ f \in k [ x _ { 1 } , \ldots , x _ { n } ] : f g \in I \forall g \in J \} .
$$

You may use without proof the fact that $I : J$ is an ideal in $k [ x _ { 1 } , \dots , x _ { n } ]$ containing I.

Compute $\langle x z , y z \rangle : \langle z \rangle$ in $k [ x , y , z ]$

(b) Compute $\mathcal { V } ( \langle x z , y z \rangle ) , \mathcal { V } ( \langle z \rangle )$ and $\mathcal { V } ( \langle x z , y z \rangle : \langle z \rangle )$

(c) Let I and J be ideals in $k [ x _ { 1 } , \dots , x _ { n } ]$

(i) Prove that $\mathcal { V } ( I : J ) \supseteq \overline { { \mathcal { V } ( I ) \backslash \mathcal { V } ( J ) } }$

(ii) If k is algebraically closed and $I = { \sqrt { I } }$ then prove that $\mathcal { V } ( I : J ) =$ $\overline { { \mathcal { V } ( I ) \backslash \mathcal { V } ( J ) } }$ . (Check this statement in the example from parts (a) and (b).)
