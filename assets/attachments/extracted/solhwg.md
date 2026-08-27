# MORE HOMEWORK SOLUTIONS MATH 114

Problem set 8.

1. Let F be the splitting field of the polynomial $x ^ { 4 } + 2 5$ over $\mathbb { Q }$ . List all subfields in $F$ and the corresponding subgroups in the Galois group.

Solution. As we proved in class $( F / \mathbb { Q } ) = 4$ . The Galois group G is the Klein subgroup of $S _ { 4 }$ , isomorphic to $\mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 }$ . Note that F contains i and ${ \sqrt { 5 } } ,$ each subgroup of G of index 2 corresponds to a subfield of degree 2. There are 3 such subfiels $\mathbb { Q } \left( i \right)$ 2 $\mathbb { Q } \left( { \sqrt { 5 } } \right)$ and $\mathbb { Q } \left( { \sqrt { - 5 } } \right)$ . The trivial subgroup of G corresponds to F and G corresponds to Q.

2. Prove that the Galois group of $x ^ { 4 } - 5$ is isomorphic to $D _ { 4 }$ . Hint: prove that the degree of the splitting field is 8, then recall that the Galois group is a subgroup of $S _ { 4 }$

Solution. By Eisenstein criterion $x ^ { 4 } - 5$ is irreducible. Let $F$ be a splitting field, then we have the following chain of extensions

$$
\mathbb { Q } \subset \mathbb { Q } \left( \alpha \right) \subset \mathbb { Q } \left( \alpha , i \right) = F ,
$$

where α is a real root of $x ^ { 4 } - 5$ . Thus,

$$
\begin{array} { r } { \left( F / \mathbb { Q } \right) = \left( \mathbb { Q } \left( \alpha , i \right) / \mathbb { Q } \left( \alpha \right) \right) \left( \mathbb { Q } \left( \alpha \right) / \mathbb { Q } \right) = 2 \times 4 = 8 , } \end{array}
$$

the Galois group G is a subgroup of $S _ { 4 }$ of order 8. Since G is a Sylow subgroup of $S _ { 4 }$ and all such subgroups are conjugate, hence isomorphic, we obtain G is isomorphic to $D _ { 4 }$

3. Prove that the Galois group of $x ^ { 4 } + 5 x ^ { 2 } + 5$ over Q is cyclic of order 4. Hint: use the formula for the roots.

Solution. The polynomial is irreducible by Eisenstein criterion. The roots can be found from the formulae

$$
\alpha _ { 1 , 2 } = \left( \frac { - 5 \pm \sqrt { 5 } } { 2 } \right) ^ { 1 / 2 } , \alpha _ { 3 , 4 } = - \alpha _ { 1 , 2 } .
$$

First, we prove that the splitting field has degree 4. Indeed

$$
\alpha _ { 1 } \alpha _ { 2 } = \sqrt { 5 } = 2 \alpha _ { 1 } ^ { 2 } + 5 ,
$$

hence

$$
\alpha _ { 2 } = 2 \alpha _ { 1 } + \frac { 5 } { \alpha _ { 1 } } \in \mathbb { Q } \left( \alpha _ { 1 } \right) , \alpha _ { 3 } = - \alpha _ { 1 } \in \mathbb { Q } \left( \alpha _ { 1 } \right) , \alpha _ { 4 } = - \alpha _ { 2 } \in \mathbb { Q } \left( \alpha _ { 1 } \right) .
$$

The Galois group $G$ is a subgroup of $S _ { 4 }$ of order 4. There exists $s \in G$ such that $s \left( \alpha _ { 1 } \right) = \alpha _ { 2 }$ , then

$$
s \left( { \sqrt { 5 } } \right) = 2 s \left( \alpha _ { 1 } \right) ^ { 2 } + 5 = 2 \alpha _ { 2 } ^ { 2 } + 5 = - { \sqrt { 5 } } .
$$

Then

$$
s \left( \alpha _ { 2 } \right) = s \left( { \frac { \sqrt { 5 } } { \alpha _ { 1 } } } \right) = { \frac { - { \sqrt { 5 } } } { \alpha _ { 2 } } } = - \alpha _ { 1 } = \alpha _ { 3 } , s \left( \alpha _ { 3 } \right) = s \left( - \alpha _ { 1 } \right) = - \alpha _ { 2 } = \alpha _ { 4 } .
$$

The order of s is 4, therefore G is isomorphic to $\mathbb { Z } _ { 4 }$

4. Let $f \left( x \right) = x ^ { 4 } + a x ^ { 2 } + b \in \mathbb { Q } \left[ x \right] , b \neq 0 .$

(a) Prove that if α is a root of $f \left( x \right)$ , then −α and $\textstyle { \frac { \sqrt { b } } { \alpha } }$ are also roots.

(b) Prove that the degree of the splitting field is 1,2,4 or 8.

(c) Prove that the Galois group is isomorphic to $\{ 1 \} , \mathbb { Z } _ { 2 } , \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 } , \mathbb { Z } _ { 4 }$ or $D _ { 4 }$

Solution. (a) can be done by direct check. Indeed,

$$
\left( { \frac { \sqrt { b } } { \alpha } } \right) ^ { 4 } + a \left( { \frac { \sqrt { b } } { \alpha } } \right) ^ { 2 } + b = { \frac { b ^ { 2 } + a b \alpha ^ { 2 } + b \alpha ^ { 4 } } { \alpha ^ { 4 } } } = { \frac { b + a \alpha ^ { 2 } + \alpha ^ { 4 } } { b \alpha ^ { 4 } } } = 0 .
$$

To show (b) denote the splitting filed by F . Then ${ \sqrt { b } } \in F$ and $\mathbb { Q } \left( \alpha , \sqrt { b } \right)$ clearly contains all roots of $x ^ { 4 } + a x ^ { 2 } + b . \ \left( \mathbb { Q } \left( \alpha \right) / \mathbb { Q } \right) = 1 , 2$ or 4 (this degree can not be $^ { 3 , }$ because the polynomial could not have only one rational root), $\left( \mathbb { Q } \left( \alpha , { \sqrt { b } } \right) / \mathbb { Q } \left( \alpha \right) \right) =$ 1 or 2. Hence

$$
( \mathbb { Q } ( \alpha , { \sqrt { b } } ) / \mathbb { Q } ) = ( \mathbb { Q } ( \alpha ) / \mathbb { Q } ) ( ( \mathbb { Q } ( \alpha , { \sqrt { b } } ) / \mathbb { Q } ( \alpha ) ) = 1 , 2 , 4 { \mathrm { ~ o r ~ } } 8 .
$$

Finally, for (c) note that the order of the Galos group is the same as the degree of the splitting field. Thus, if the order is 2, the group is $\mathbb { Z } _ { 2 }$ , if the order is 4 the group is either $\mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 }$ or $\mathbb { Z } _ { 4 }$ . If the order of the Galois group is 8, the group is isomorphic to $D _ { 4 }$ , because it is a subgroup of $S _ { 4 }$ (see the previous problem).

5. For a cubic polynomial $f \left( x \right) = x ^ { 3 } + a x + b$ the discriminant is given by the formula

$$
D = - 4 a ^ { 3 } - 2 7 b ^ { 2 } .
$$

Assume that $a$ and b are real numbers. Prove that D is negative if and only if $f \left( x \right)$ has exactly one real root.

Solution. Use

$$
D = \left( \alpha _ { 1 } - \alpha _ { 2 } \right) ^ { 2 } \left( \alpha _ { 2 } - \alpha _ { 3 } \right) ^ { 2 } \left( \alpha _ { 1 } - \alpha _ { 3 } \right) ^ { 2 } ,
$$

where $\alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 }$ are the roots. If all 3 roots are real, then D is a square of a real number. Hence $D \geq 0$ . Assume that $\alpha _ { 1 } , \alpha _ { 2 }$ are complex conjugate, $\alpha _ { 3 }$ is real. Write

$$
\alpha _ { 1 } = a + b i , \alpha _ { 2 } = a - b i , \alpha _ { 3 } = c .
$$

Then

$$
D = \left( b i \right) ^ { 2 } \left( a - c - b i \right) ^ { 2 } \left( a - c + b i \right) ^ { 2 } = - b ^ { 2 } \left( \left( a - c \right) ^ { 2 } + b ^ { 2 } \right) ^ { 2 } < 0 .
$$

6. Assume that $f \left( x \right) = g \left( x \right) h \left( x \right)$ for some separable polynomials $f \left( x \right) , g \left( x \right) , h \left( x \right) \in$ $F \left[ x \right]$ Denote by $E _ { f } , E _ { g }$ and $E _ { h }$ the splitting fields of the polynomials $f \left( x \right) , g \left( x \right)$ and $h \left( x \right)$ respectively. Let

$$
\begin{array} { r } { \left( E _ { f } / F \right) = \left( E _ { g } / F \right) \left( E _ { h } / F \right) . } \end{array}
$$

Prove that the Galois group of $f \left( x \right)$ is isomorphic to the direct product of the Galois groups of $g \left( x \right)$ and $h \left( x \right)$

Solution. Let $G = \mathrm { A u t } _ { F } E _ { f }$ be the Galois group of $f \left( x \right) , K = \mathrm { A u t } _ { E _ { q } } E , H =$ $\operatorname { A u t } _ { E _ { h } } E$ . Since $E _ { g }$ and $E _ { h }$ are normal extensions of $F , K$ and H are normal subgroups of G and by fundamental theorem of Galois theory

$$
\mathrm { A u t } _ { F } E _ { h } \cong G / H , \mathrm { A u t } _ { F } E _ { g } \cong G / K .
$$

Consider the subgroup $U = K \cap H \subset G$ . Note that U fixes every element of $E _ { g }$ and $E _ { h } .$ but $E _ { g } E _ { h } = E _ { f }$ therefore $K \cap H = \{ 1 \}$ Consider the restriction map $r \colon G \to \mathrm { A u t } _ { F } E _ { h }$ , the kernel of r is H. Therefore $r : K \to \mathrm { A u t } _ { F } E _ { h }$ is injective as $K \cap H = \{ 1 \}$ . Note that r is surjective because

$$
| \operatorname { A u t } _ { F } E _ { h } | = ( E _ { h } / F ) = { \frac { ( E _ { f } / F ) } { ( E _ { g } / F ) } } = { \frac { | G | } { | G / K | } } = | K | .
$$

Thus, r is an isomorphism and we obtain $K \cong \mathrm { A u t } _ { F } E _ { h }$ . Similarly $H \cong \operatorname { A u t } _ { F } E _ { g }$ Finally $G = K H$ , because $| K H | = | K | | H | = | G |$

Problem set $\# 9$

1. Let $n = p ,$ or 2p where p is a prime number. Prove that the Galois group of the polynomial $x ^ { n } - 1$ over any field F is cyclic.

Solution. We may assume that the characteristic does not divide n, because otherwise the Galois group is trivial. Then the roots of $x ^ { n } - 1$ form a cyclic group, and the Galois group G of $x ^ { n } - 1$ is a subgroup of automorphisms of $\mathbb { Z } _ { n }$ , in other words $G \subset \mathbb { Z } _ { n } ^ { * }$ . If $n = p$ is prime, then $\mathbb { Z } _ { n } ^ { * }$ is cyclic as the multiplicative group of a finite field. If $n = 2 p , p \ : > \ : 2$ , then $\mathbb { Z } _ { 2 p } ^ { * }$ is isomorphic to $\mathbb { Z } _ { p } ^ { * } .$ (The isomorphism $f : \mathbb { Z } _ { p } ^ { * } \to \mathbb { Z } _ { 2 p } ^ { * }$ can be given, for example, by $f \left( x \right) = x$ for odd $x , f \left( x \right) = x + p$ for even x ). If $\bar { n } = 4$ , then $\mathbb { Z } _ { 4 } ^ { * } \cong \mathbb { Z } _ { 2 }$ is cyclic. A subgroup of a cyclic group is cyclic. Hence G is cyclic.

2. Show that the Galois group of $x ^ { 1 5 } - 1$ over Q is isomorphic to $\mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 4 }$

Solution. The Galois group of $x ^ { 1 5 } - 1$ is isomorphic to $\mathbb { Z } _ { 1 5 } ^ { * }$ . One has an isomorphism $\mathbb { Z } _ { 1 5 } ^ { * } \cong \mathbb { Z } _ { 3 } ^ { * } \times \mathbb { Z } _ { 5 } ^ { * } \cong \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 4 }$ . One can take 4 and $7$ as generators.

3. Find the Galois groups of $x ^ { 6 } - 1$ over $\mathbb { F } _ { 5 } , \mathbb { F } _ { 2 5 }$ and $\mathbb { F } _ { 1 2 5 }$

Solution. We know that the Galois group of a finite extension is always cyclic. Thus, we just have to find the degree of a splitting field. Since we have the decomposition

$$
x ^ { 6 } - 1 = \left( x - 1 \right) \left( x + 1 \right) \left( x ^ { 2 } + x + 1 \right) \left( x ^ { 2 } - x + 1 \right) ,
$$

and if α is a root of $x ^ { 2 } + x + 1$ , then $- \alpha$ is a root of $x ^ { 2 } - x + 1$ , the splitting field for $x ^ { 6 } - 1$ coincides with the splitting field of $x ^ { 2 } + x + 1$ . Note that $x ^ { 2 } + x + 1$ does not have roots in $\mathbb { F } _ { 5 }$ , therefore it is irreducible over $\mathbb { F } _ { 5 }$ . Therefore the splitting field for $x ^ { 2 } + x + 1$ is isomorphic to $\mathbb { F } _ { 2 5 }$ . Thus, the Galois group over $\mathbb { F } _ { 5 }$ is isomorphic to $\mathbb { Z } _ { 2 }$ , the Galois group over $\mathbb { F } _ { 2 5 }$ is trivial. Note that $x ^ { 2 } + x + 1$ does not have roots in $\mathbb { F } _ { 1 2 5 }$ , because $\mathbb { F } _ { 1 2 5 }$ has degree 3 over $\mathbb { F } _ { 5 }$ and does not contain a subfield of degree 2. Thus, the Galois group over $\mathbb { F } _ { 1 2 5 }$ is again $\mathbb { Z } _ { 2 }$

4. Let $F \subset E$ be an extension of finite fields. Prove that

$$
| E | = | F | ^ { ( E / F ) } .
$$

Solution. Let $m = ( E / F )$ Choose a basis $\alpha _ { 1 } , \ldots , \alpha _ { m }$ in $E$ over F . Every element $\alpha \in E$ can be written uniquely as $\alpha = b _ { 1 } \alpha _ { 1 } + \cdot \cdot \cdot + b _ { m } \alpha _ { m }$ with $b _ { 1 } , \dots , b _ { m } \in F$ . Hence $| E | = | F | ^ { m }$

5. Let $f \left( x \right) \in \mathbb { Z } _ { p } \left[ x \right]$ be an irreducible polynomial of degree 3. Prove that $f \left( x \right)$ is irreducible over $\mathbb { F } _ { p ^ { 5 } }$

Solution. Assume that $f \left( x \right)$ is reducible over $\mathbb { F } _ { p ^ { 5 } }$ . Then there is root α of $f \left( x \right)$ lying in $\mathbb { F } _ { p ^ { 5 } }$ . Then $\mathbb { Z } _ { p } \left( \alpha \right)$ is a subfield of $\mathbb { F } _ { p ^ { 5 } }$ . On the other hand

$$
\left( \mathbb { F } _ { p ^ { 5 } } / \mathbb { Z } _ { p } \right) = 5 , \left( \mathbb { Z } _ { p } \left( \alpha \right) / \mathbb { Z } _ { p } \right) = 3 ,
$$

hence 3 divides 5. Contradiction.

6. Let $q = p ^ { k }$ for some prime $p , n$ be a number relatively prime to $p ,$ m be the minimal positive integer such that

$$
q ^ { m } \equiv 1 \mod n .
$$

Show that the Galois group of $x ^ { n } - 1$ over $\mathbb { F } _ { q }$ is isomorphic to $\mathbb { Z } _ { m }$

Solution. Let E be the unique extension of $\mathbb { F } _ { q }$ of degree m. We will prove that E is a splitting field of $x ^ { n } - 1$ over $\mathbb { F } _ { q }$ . Let $E ^ { * }$ denote the multiplicative group of E. Then $E ^ { * }$ is cyclic of order $q ^ { m } - 1$ . Since n divides $q ^ { m } - 1 , E ^ { * }$ contains a cyclic subgroup of order $n .$ . Elements of this cyclic subgroup are the roots of $x ^ { n } - 1$ . To check that E is a splitting field, we need to show that every proper subfield of E does not contain all roots for $x ^ { n } - 1$ . Indeed, let B be a subfield such that $F \subset B \subset E$ Then $| B | = q ^ { s }$ for some $s < m$ . Then n does not divide $| B ^ { * } | = q ^ { s } - 1$ and therefore $B ^ { * }$ can not contain a cyclic subgroup of order n.

To finish the problem, just note that the Galois group of $x ^ { n } - 1$ is $\operatorname { A u t } _ { \mathbb { F } _ { q } } E \cong \mathbb { Z } _ { m }$