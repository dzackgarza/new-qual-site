# Math 200a (Fall 2016) - Homework 6

Professor D. Rogalski

Posted November 5–Due Mon. November 14 at 3pm

## 1 Reading

Read Chapter 7.

## 2 Exercises to submit on Mon. November 14

Exercise 1. Let G be a group (do not assume that G is finite).

(a). Show that if G is nilpotent, then all subgroups and quotient groups of G are also nilpotent. (Hint: it is probably easiest to use the lower central series).

(b). Show that if $G / Z ( G )$ is nilpotent, then G is nilpotent.

Exercise 2. (a). Prove that a finite group G is nilpotent if and only if whenever $a , b \in G$ are elements with relatively prime orders, then a and b commute.

(b). Prove that the dihedral group $D _ { 2 n }$ is nilpotent if and only if n is a power of 2. (one way is to use part (a)).

Exercise 3. Let G be a finite group. The Frattini subgroup of a group $G ,$ denoted $\Phi ( G )$ , is the intersection of all of the maximal subgroups of G.

(a). Prove that Φ(G) is a characteristic subgroup of G.

(b). Prove that Φ(G) is a nilpotent group. (Hint: use Frattini’s argument).

(c). Now let $G = P$ be a p-group for some prime p. Recall that an elementary abelian p-group is a finite direct product of copies of $\mathbb { Z } _ { p }$ . Show that $P / \Phi ( P )$ is an elementary abelian p-group, and that $\Phi ( P )$ is the unique smallest normal subgroup with this property, i.e. if N is any normal subgroup of P such that $P / N$ is elementary abelian, then $\Phi ( P ) \subseteq N$ •

Exercise 4. An element x of a ring R is called nilpotent if $x ^ { n } = 0$ for some $n \geq 1$

(a). Prove that if R is a commutative ring with nilpotent elements x, y, then $x + y$ is nilpotent. (Hint: the binomial formula is valid in any commutative ring). Use this to show that the set I of nilpotent elements in R is an ideal of R. (I is called the nilradical of R).

(b). Again if R is a commutative ring, prove that if u is any unit in $R ,$ and x is nilpotent, then $u + x$ is again a unit in R. (Hint : first do the case $u = - 1 .$ )

(c). Give an example of a noncommutative ring R and nilpotent elements x, $y \in R$ such that $x + y$ is not nilpotent.

Exercise 5. Let R be a commutative ring. The ring $R [ [ x ] ]$ of formal power series in one variable is the ring whose elements are formal sums $\begin{array} { r } { \sum _ { n = 0 } ^ { \infty } a _ { n } x ^ { n } = a _ { 0 } + a _ { 1 } x + a _ { 2 } x ^ { 2 } + . . } \end{array}$ . for some $a _ { n } \in R$ (Note that any choice of coefficients $a _ { n } \in R$ defines a power series, and two power series are equal by definition if and only if they have the same coefficients. “Convergence" of the power series is meaningless in this general context.) Addition and multiplication of power series are defined analogously as for polynomials. (See Section 7.2 exercise 3). You should convince yourself that $R [ [ x ] ]$ satisfies the axioms of a ring.

(a). Prove that $\scriptstyle \sum _ { n = 0 } ^ { \infty } a _ { n } x ^ { n }$ is a unit in the ring $R [ [ x ] ]$ if and only if $a _ { 0 }$ is a unit in R.

(b). Prove that if R is a domain, then $R [ [ x ] ]$ is a domain.

(c). Suppose that R is a field. Show that the set of power series in $R [ [ x ] ]$ whose constant term is 0 is a maximal ideal I of $R [ [ x ] ]$ . Prove that I is the unique maximal ideal of R. (remark: a ring with a unique maximal ideal is called local.)

Exercise 6. Recall that the center of a ring R is

$$
Z ( R ) = \{ r \in R | r s = s r { \mathrm { ~ f o r ~ a l l ~ } } s \in R \} .
$$

It is a subring of R.

Now let R be any commutative ring, and G any finite group. Consider the group ring RG.

(a). Suppose that $\boldsymbol { K } = \{ k _ { 1 } , \dots , k _ { m } \}$ is a conjugacy class in the group $G .$ . Prove that the element $K = k _ { 1 } + k _ { 2 } + \cdot \cdot \cdot + k _ { m } \in R G$ is an element of $Z ( R G )$

(b). Let $\mathcal { K } _ { 1 } , \ldots , \mathcal { K } _ { r }$ be the distinct conjugacy classes in G and for each i let $K _ { i }$ be the sum of the elements in $\kappa _ { i } ,$ as in part (a). Prove that $Z ( R G ) = \{ a _ { 1 } K _ { 1 } + \cdot \cdot \cdot + a _ { r } K _ { r } | a _ { i } \in R$ for all $1 \leq i \leq r \}$ In other words, the center consists of all R-linear combinations of the $K _ { i }$

Exercise 7. Let R be a ring, and consider the matrix ring $M _ { n } ( R )$ for some $n \geq 1$

(a). Given a (two-sided) ideal I of $R ,$ show that $M _ { n } ( I )$ is an ideal of $M _ { n } ( R )$ . (Here, $M _ { n } ( I )$ means the set of matrices $( a _ { i j } )$ such that $a _ { i j } \in I$ for all $i , j . )$ Show that there is an isomorphism of rings $M _ { n } ( R ) / M _ { n } ( I ) \cong M _ { n } ( R / I )$

(b). Show that every ideal of $M _ { n } ( R )$ is of the form $M _ { n } ( I )$ for some ideal I of R. Conclude that if R is a division ring, then $M _ { n } ( R )$ is a simple ring, that is, that {0} and $M _ { n } ( R )$ are the only ideals of $M _ { n } ( R )$ .