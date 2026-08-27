Please begin your solution to each problem 1–5 on a new sheet.

When answering any part of a problem you may assume you have done the preceding parts.   
Notation: Z (resp. Q) is the ring of rational integers (resp. the field of rational numbers).

1. Let G be a group of order 105.

(a) Show that G has a normal subgroup of order 5 or 7. [points]:[4]

(b) Show that G has a cyclic normal subgroup of order 35. [4]

(c) Show that the Sylow 5- and 7-subgroups of G are both normal. [3]

(d) Classify groups of order 105.

Solution. (a) If a Sylow 5-subgroup F is not normal, then it has $1 + 5 k$ conjugates where $k \geq 1$ and 1 + 5k divides $1 0 5 / 5 = 2 1 $ , whence $1 + 5 k = 2 1$ and there are $2 1 \cdot 4 = 8 4$ elements of order 5. Similarly if a Sylow 7-subgroup S is not normal, then there are $1 5 \cdot 6 = 9 0$ elements of order 7. Since $8 4 + 9 0 > 1 0 5$ , at least one of F and S must be normal.

(b) Since at least one of F and S is normal, and (clearly) $| F \cap S | = 1$ , therefore $F S < G$ is a subgroup of order 35. Since 5 doesn’t divide $7 - 1$ , every group of order 35 is cyclic.

(c) The cyclic group F S has unique subgroups of orders 5 and 7, so it has 31 elements of order $\neq 5 .$ , and 29 elements of order $\neq 7$ . Hence, and since $| G | = 1 0 5 , G$ cannot have 84 elements of order 5 or 90 of order $7 ;$ so by the proof of (a), both F and S are normal.

(d) As in (b), if T is the Sylow 3-subgroup, then, since $S \triangleleft G$ , therefore $T S < G$ is a subgroup of order 21, a complement of $F \triangleleft G$ . Since $\lvert \mathrm { A u t } ( F ) \rvert = 4$ , any homomorphism $T S \to \operatorname { A u t } ( F )$ is trivial; and consequently G is the direct product $T S \times F$ . There are, up to isomorphism, just two groups of order 21, and one of order $5 ;$ correspondingly, there are just two possibilities for G.

2. Let $n > 1$ be in $\mathbb { Z } ,$ and let $R { : = } \mathbb { Z } [ { \sqrt { - n } } ]$

For $x = a + b { \sqrt { - n } } \in R \left( a , b \in \mathbb { Z } \right)$ , set ${ \bar { x } } = a - b { \sqrt { - n } } .$ , and define the norm

$$
N ( x ) = x \bar { x } = a ^ { 2 } + n b ^ { 2 } .
$$

(a) Assuming $x \neq 0$ , describe group isomorphisms $R / x R \cong R / \bar { x } R \cong x R / x \bar { x } R .$

[4]

$$
( \mathrm { b } ) \mathrm { \ D e d u c e \ f r o m \ ( a ) \ t h a t \ } N ( x ) ^ { 2 } = [ R : x R ] [ x R : x \bar { x } R ] = [ R : x R ] ^ { 2 } .\tag{[3]}
$$

(c) Deduce from (b) that if N (x) is prime in $\mathbb { Z }$ then x is prime in R. [4]

(d) Deduce from (c) that if p is a prime in $\mathbb { Z }$ then there is at most one way to represent p in the form $p = a ^ { 2 } + n b ^ { 2 }$ where a and b are positive integers. [4]

Solution. (a) The automorphism of R that takes any $y \in R$ to $\bar { y }$ induces the first isomorphism. Multiplication by x induces the second (which is clearly surjective, and also injective since if $x y = x { \bar { x } } z$ then, R being an integral domain, $y = { \bar { x } } z )$ .

(b) Taking $( a , b ) \in \mathbb { Z } \times \mathbb { Z }$ to $a + b { \sqrt { - n } } \in R$ gives a group isomorphism. For $n > 0 \in \mathbb { Z } .$ there results an isomorphism $\mathbb { Z } _ { n } \times \mathbb { Z } _ { n } \cong R / n R \mathrm { : }$ ; so the cardinality $| R / n R | = [ R : n R ] = n ^ { 2 }$ In particular, for $n = x { \bar { x } }$ one gets $N ( x ) ^ { 2 } = [ R : x { \bar { x } } R ] = [ R : x R ] [ x R : x { \bar { x } } R ] = [ R : x R ] ^ { 2 }$ where the last equality holds by (a).

(c) If $N ( x ) \stackrel { ( \mathrm { b } ) } { = } | R / x R |$ is prime, so that $R / x R$ has no nontrivial proper subgroup, then the ideal $x R$ is maximal, hence prime, i.e., x is prime in R.

(d) By (c), if $p \ = \ a ^ { 2 } + n b ^ { 2 } \ = \ x \bar { x } \ ( x : = \ a + b \sqrt { - n } )$ is a Z-prime then $p = x { \bar { x } }$ is a factorization of p into R-primes. By (b), any unit $u + v { \sqrt { - n } }$ in R has norm $\pm 1$ , i.e., $u ^ { 2 } + n v ^ { 2 } = \pm 1$ , whence $u = \pm 1$ and $v = 0$ . Since factorization into primes is unique up to multiplying by units and permuting the factors, it follows that if $p = a ^ { 2 } + n b ^ { 2 } = c ^ { 2 } + n d ^ { 2 }$ with $a , b ,$ c and d all positive then $a = c$ and $b = d .$

3. (a) Prove that in $\mathbb { Z } [ { \sqrt { - 5 } } ]$ , 7 is irreducible but not prime.

[10]

(b) Is $\mathbb { Z } [ { \sqrt { - 5 } } ]$ a Principal Ideal Domain? (Justify your answer.)

[5]

Solution. (a) By substituting $y$ for $\bar { x }$ in (a) and (b) of problem 2, one sees that $N ( x y ) = N ( x ) N ( y )$ . (You could also just say this was proved—differently—in class.)

If $7 = x y$ with neither x nor y a unit, then $N ( 7 ) = 4 9 = N ( x ) N ( y )$ , and since $N ( x ) > 1$ $N ( y ) > 1$ (cf. problem 2), therefore $N ( x ) = N ( y ) = 7$ . But this can’t be, since $a ^ { 2 } + 5 b ^ { 2 } = 7$ has no integer solution. Thus 7 is irreducible.

On the other hand, 7 divides $( 3 + { \sqrt { - 5 } } ) ( 3 - { \sqrt { - 5 } } )$ without dividing either factor; so 7 is not prime.

(b) $\mathbb { Z } [ { \sqrt { - 5 } } ]$ is not a Principal Ideal Domain, because Principal Ideal Domains are Unique Factorization Domains, rings in which irreducible elements are always prime.

4. Let K be a finite field of cardinality $q ,$ let $n > 0$ be an integer relatively prime to $q ,$ and let $\zeta$ be a primitive n-th root of unity lying in some field $L \supset K$ with $[ L : K ] = m$

(a) Show that n divides $q ^ { m } - 1$

[4]

(b) Show that $[ K ( \zeta ) : K ]$ is the order of $q$ in the group $( \mathbb { Z } / n \mathbb { Z } ) ^ { * }$ (units in $\mathbb { Z } / n \mathbb { Z } )$ . [6]

Solution. (a) $\mathrm { B y }$ the definition of “primitive n-th root of $\mathrm { { u n i t y } } , \mathrm { { \dot { \Omega } } }$ n is the order of $\zeta$ in the multiplicative group $L ^ { * } ;$ so $n | | L ^ { * } | = q ^ { m } - 1$

(b) By (a), the order $\mu$ of q divides $[ K ( \zeta ) : K ]$ . So $K ( \zeta )$ contains a subfield $L ^ { \prime } \supset K$ such that $[ L ^ { \prime } : K ] = \mu$ . The cyclic group $L ^ { \prime * }$ has order $q ^ { \mu } - 1$ divisible by $n ,$ so it contains a cyclic subgroup of order n, and therefore it contains all the n solutions of $X ^ { n } - 1$ , one of which is $\zeta ,$ , whence $L ^ { \prime } = K ( \zeta )$ and $[ K ( \zeta ) : K ] = [ L ^ { \prime } : K ] = \mu .$

5. Let $f ( X ) = X ^ { 6 } + a X ^ { 3 } + 1 \in \mathbb { Z } [ X ]$ be irreducible, and let $\mathcal G \subset S _ { 6 }$ be its galois group. (Analyzing possible factorizations, it is not hard to show—but you needn’t do so now—that f is reducible $\iff a = p ^ { 3 } - 3 p$ for some $p \in \mathbb { Z } . )$

Let $F$ be a splitting field of $f \ ( \mathrm { o v e r } \ \mathbb { Q } )$

(a) Show that $\mathrm { i f } \ | a | \geq 2$ then $f$ has a real root $x ,$ and that with ω a primitive cube root of unity, the other roots are ωx, $\omega ^ { 2 } x , 1 / x , \omega / x$ , and $\omega ^ { 2 } / x$ [6]

(b) Show that $\mathcal { G }$ is isomorphic to the order-12 dihedral group $D _ { 1 2 }$

[10]

Hint. Show that there is an order-6 automorphism ψ of F with $\psi x = \omega / x$ and $\psi \omega = \omega ^ { 2 }$ . Also, complex conjugation gives an automorphism γ of order 2.

(c) For x as in $\mathrm { ( a ) }$ , it is easily seen—and you may assume—that $x + 1 / x , \omega x + 1 / ( \omega x )$ and $\omega ^ { 2 } x + 1 / ( \omega ^ { 2 } x )$ make up a single $\mathcal { G } _ { \mathrm { - o r b i t } }$ , and are distinct roots of $X ^ { 3 } - 3 X + a$

Show that there are precisely three fields $E \subset F$ such that $[ E : \mathbb { Q } ] = 3$ , that these are conjugate to each other, and that each is generated over $\mathbb { Q }$ by a root of $X ^ { 3 } - 3 X + a$ . [9]

Total points:[80]

Solution. (a) A real cube root x of $( - 1 + \sqrt { a ^ { 2 } - 4 } ) / 2$ is a root of $f .$ It is easy to check that if y is any root of f then $\omega y , \omega ^ { 2 } y , 1 / y , \omega / y$ , and $\omega ^ { 2 } / y$ are also roots. Since $y \ne 0$ , therefore $y \ne$ ωy and $y \ne \omega ^ { 2 } y$ . If $y = \omega ^ { i } / y \ ( 0 \leq i \leq 2 )$ then $y ^ { 3 } = 1 / y ^ { 3 }$ , so $y ^ { 3 } = \pm 1$ , and $y ^ { 6 } + a y ^ { 3 } + 1 = 1 \pm a + 1 \neq 0$ because $a = \pm 2 \implies f$ reducible. So $y \neq \omega ^ { i } / y ;$ and as before $y \neq \omega ^ { j } y \ ( j = 1 , 2 )$ . Thus the roots are distinct, and (a) results.

(b) By $( \mathrm { a } ) , F = \mathbb { Q } ( x , \omega )$ ; and since x is real and $\omega$ is not, and x is a root of a degree-6 irreducible polynomial, therefore

$$
| \mathcal { G } | = [ F : \mathbb { Q } ] = [ \mathbb { Q } ( x , \omega ) : \mathbb { Q } ( x ) ] [ \mathbb { Q } ( x ) : \mathbb { Q } ] = 2 \cdot 6 = 1 2 .
$$

The two automorphisms of $\mathbb { Q } ( \omega )$ extend to automorphisms of the splitting field $F$ (shown in class). An extension θ is uniquely determined by $\theta ( x )$ , which is a root of $f ,$ so there are at most six extensions, and there must be exactly six because $F$ has twelve automorphisms. In other words, for each root $y$ of $f _ { : }$ there is $\textrm { a } \theta$ with $\theta ( x ) = y$ . Thus the nonidentity automorphism of $\mathbb { Q } ( \omega )$ , which takes ω to $\omega ^ { 2 }$ , extends to an automorphism $\psi$ of $F$ with $\psi x = \omega / x$ . Then

$$
\psi ^ { 2 } ( x ) = \psi ( \omega / x ) = \omega ^ { 2 } / ( \omega / x ) = \omega x \neq x ,
$$

whence $\psi ^ { 4 } ( x ) = \omega ^ { 2 } x$ and $\psi ^ { 6 } ( x ) = x ,$ . Also $\psi ^ { 3 } ( \omega ) = \omega ^ { 2 } \ne \omega ;$ and $\psi ^ { 6 } ( \omega ) = \omega$ . Hence $\psi ^ { 6 }$ is the identity, while $\psi ^ { 2 }$ and $\psi ^ { 3 }$ are not—that is, $\psi$ has order 6. So ψ generates a cyclic subgroup $\mathcal { C } \subset \mathcal { G }$ , which is of index 2 and hence normal.

An easy calculation shows that $\gamma \psi \gamma ^ { - 1 } = \psi ^ { - 1 }$ . (Just apply both sides to x and to $\omega . )$ So γ is not contained in C (which is commutative), and hence generates a complement of $\mathcal { C } .$ Thus $\mathcal { G } \cong \mathbb { Z } _ { 2 } \rtimes _ { \phi } \mathbb { Z } _ { 6 }$ where φ takes the generator of $\mathbb { Z } _ { 2 }$ to the automorphism $\xi \mapsto \xi ^ { - 1 }$ of $\mathbb { Z } _ { 6 }$ that is, $\mathcal { G } \cong D _ { 1 2 }$

(c) Fields $E$ with $[ E : \mathbb { Q } ] = 3$ correspond 1-1 to order-4 subgroups of $\mathcal { G } \cong D _ { 1 2 }$ , i.e., to Sylow 2-subgroups, of which there must be 1 or 3. There can’t be 1, because, $\mathrm { e . g . } , D _ { 1 2 }$ has seven elements of order 2 (as one sees, e.g., by representing $D _ { 1 2 }$ as a group of symmetries of a regular hexagon), each of which is contained in a Sylow 2-subgroup. So there are 3 subfields of degree 3, conjugate to each other (since that is true for the $\mathrm { S y }$ low 2-subgroups).

The polynomial $X ^ { 3 } - 3 X + a$ is irreducible over $\mathbb { Q } ,$ because it has the three given $\mathcal { G } _ { - }$ conjugate roots. So any of these roots generates a degree-3 subfield, whose conjugates are the subfields generated (respectively) by the other two roots. By the preceding paragraph, these must be the three sought-after subfields.

Supplementary exercise. Prove that F has precisely three quadratic subfields, generated by the square roots of $- 3 , a ^ { 2 } - 4$ and $( - 3 ) ( a ^ { 2 } - 4 )$ , respectively.

Which one is the fixed field of C ? Which contains the discriminant of f? $\mathrm { O f } X ^ { 3 } - 3 X + a ?$