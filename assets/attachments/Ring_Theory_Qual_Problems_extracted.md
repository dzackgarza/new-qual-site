# ALGEBRA QUALIFYING EXAM PROBLEMSRING THEORY

Kent State University Department of Mathematical Sciences

Compiled and Maintained by Donald L. White

Version: August 29, 2017

## CONTENTS

RING THEORY\
General Ring Theory 1\
Prime, Maximal, and Primary Ideals 4\
Commutative Rings 6\
Domains 7\
Polynomial Rings 9\
Non-commutative Rings 10\
Local Rings, Localization, Rings of Fractions 1 1\
Chains and Chain Conditions 12

## RING THEORY

## General Ring Theory

1. Give an example of each of the following.

(a) An irreducible polynomial of degree 3 in $\mathbb { Z } _ { 3 } [ x ]$

(b) A polynomial in $\mathbb { Z } [ x ]$ that is not irreducible in $\mathbb { Z } [ x ]$ but is irreducible in $\mathbb { Q } [ x ]$

(c) A non-commutative ring of characteristic $p , p \mathrm { ~ a ~ }$ prime.

(d) A ring with exactly 6 invertible elements.

(e) An infinite non-commutative ring with only finitely many ideals.

(f) An infinite non-commutative ring with non-zero characteristic.

(g) An integral domain which is not a unique factorization domain.

(h) A unique factorization domain that is not a principal ideal domain.

(i) A principal ideal domain that is not a Euclidean domain.

(j) A Euclidean domain other than the ring of integers or a field.

(k) A finite non-commutative ring.

(l) A commutative ring with a sequence $\{ P _ { n } \} _ { n = 1 } ^ { \infty }$ of prime ideals such that $P _ { n }$ is properly contained in $P _ { n + 1 }$ for all n.

(m) A non-zero prime ideal of a commutative ring that is not a maximal ideal.

(n) An irreducible element of a commutative ring that is not a prime element.

(o) An irreducible element of an integral domain that is not a prime element.

(p) A commutative ring that has exactly one maximal ideal and is not a field.

(q) A non-commutative ring with exactly two maximal ideals.

2. (a) How many units does the ring Z/60Z have?
   Explain your answer.

(b) How many ideals does the ring Z/60Z have?
Explain your answer.

3. [NEW] How many ideals does the ring Z/90Z have?
   Explain your answer.

4. Denote the set of invertible elements of the ring $\mathbb { Z } _ { n }$ by $U _ { n }$

(a) List all the elements of $U _ { 1 8 }$

(b) Is $U _ { 1 8 }$ a cyclic group under multiplication?
Justify your answer.

5. [NEW] Denote the set of invertible elements of the ring $\mathbb { Z } _ { n }$ by $U _ { n }$

(a) List all the elements of $U _ { 2 4 }$

(b) Is $U _ { 2 4 }$ a cyclic group under multiplication?
Justify your answer.

6. [NEW] Find all positive integers n having the property that the group of units of $\mathbb { Z } / n \mathbb { Z }$ is an elementary abelian 2-group.

7. Let $U ( R )$ denote the group of units of a ring R. Prove that if m divides n, then the natural ring homomorphism $\mathbb { Z } _ { n } \to \mathbb { Z } _ { m }$ maps $U ( \mathbb { Z } _ { n } )$ onto $U ( \mathbb { Z } _ { m } )$

Give an example that shows that $U ( R )$ does not have to map onto $U ( S )$ under a surjective ring homomorphism $R \to S$ .

8. If p is a prime satisfying $p \equiv 1$ (mod 4), then p is a sum of two squares.

9. If ( ·· ) denotes the Legendre symbol, prove Euler’s Criterion: if p is a prime and a is any integer relatively prime to p, then $a ^ { ( p - 1 ) / 2 } \equiv \left( { \frac { a } { p } } \right)$ (mod p).

10. Let $R _ { 1 }$ and $R _ { 2 }$ be commutative rings with identities and let $R = R _ { 1 } \times R _ { 2 }$ . Show that every ideal I of R is of the form $I = I _ { 1 } \times I _ { 2 }$ with $I _ { i }$ an ideal of $R _ { i }$ for $i = 1 , 2$

11. Show that a non-zero ring R in which $x ^ { 2 } = x$ for all $x \in R$ is of characteristic 2 and is commutative.

12. Let R be a finite commutative ring with more than one element and no zero-divisors.
    Show that R is a field.

13. Determine for which integers n the ring $\mathbb { Z } / n \mathbb { Z }$ is a direct sum of fields.
    Prove your answer.

14. Let R be a subring of a field F such that for each x in F either $x \in R { \mathrm { ~ o r ~ } } x ^ { - 1 } \in R$ . Prove that if I and J are two ideals of R, then either $I \subseteq J { \mathrm { ~ o r ~ } } J \subseteq I$

15. The Jacobson Radical $J ( R )$ of a ring R is defined to be the intersection of all maximal ideals of R.

Let R be a commutative ring with 1 and let $x \in R$ . Show that $x \in J ( R )$ if and only if $1 - x y$ is a unit for all y in R.

16. Let R be any ring with identity, and n any positive integer.
    If $M _ { n } ( R )$ denotes the ring of $n \times n$ matrices with entries in R, prove that $M _ { n } ( I )$ is an ideal of $M _ { n } ( R )$ whenever I is an ideal of R, and that every ideal of $M _ { n } ( R )$ has this form.

17. Let m, n be positive integers such that m divides n. Then the natural map $\varphi : \mathbb { Z } _ { n } \to \mathbb { Z } _ { m }$ given by $a + ( n ) \mapsto a + ( m )$ is a surjective ring homomorphism.
    If $U _ { n } , U _ { m }$ are the units of $\mathbb { Z } _ { n }$ and $\mathbb { Z } _ { m }$ , respectively, show that $\varphi : U _ { n } \to U _ { m }$ is a surjective group homomorphism.

18. Let R be a ring with ideals A and B. Let $R / A \times R / B$ be the ring with coordinate-wise addition and multiplication.
    Show the following.

(a) The map $R \to R / A \times R / B$ given by $r \mapsto ( r + A , r + B )$ is a ring homomorphism.

(b) The homomorphism in part (a) is surjective if and only if $A + B = R$

19. Let m and n be relatively prime integers.

(a) Show that if c and d are any integers, then there is an integer x such that $x \equiv c ( \mathrm { m o d } m )$ and $x \equiv d ( \mathrm { m o d } n )$

(b) Show that $\mathbb { Z } _ { m n }$ and $\mathbb { Z } _ { m } \times \mathbb { Z } _ { n }$ are isomorphic as rings.

20. Let R be a commutative ring with 1 and let I and J be ideals of R such that $I + J = R$ Show that $R / ( I \cap J ) \cong R / I \oplus R / J$ .

21. [NEW] Let R be a commutative ring with identity and let $I _ { 1 } , I _ { 2 } , \ldots , I _ { n }$ be pairwise comaximal ideals of $R \ ( { \mathrm { i . e . , } } \ I _ { i } + I _ { j } = R { \mathrm { i f } } \ i \neq j )$ . Show that $I _ { i } + \bigcap I _ { j } = R$ for all i.

22. Let R be a commutative ring, not necessarily with identity, and assume there is some fixed positive integer n such that $n r = 0$ for all $r \in R .$ . Prove that R embeds in a ring S with identity so that R is an ideal of S and $S / R \cong \mathbb { Z } / n \mathbb { Z }$

23. Let R be a ring with identity 1 and $a , b \in R$ such that $a b = 1$ . Denote $X = \{ x \in R \mid a x = 1 \}$ Show the following.

(a) If $x \in X$ , then $b + ( 1 - x a ) \in X$

(b) If $\varphi : X \to X$ is the mapping given by $\varphi ( x ) = b + ( 1 - x a )$ , then $\varphi$ is one-to-one.

(c) If X has more than one element, then X is an infinite set.

24. Let R be a commutative ring with identity and define $U _ { 2 } ( R ) \ = \ \left\{ { \left[ \begin{array} { l l } { a } & { b } \\ { 0 } & { c } \end{array} \right] } \ | \ a , b , c \in R \right\}$ Prove that every R-automorphism of $U _ { 2 } ( R )$ is inner.

25. Let R be the field of real numbers and let F be the set of all $2 \times 2$ matrices of the form $\left[ { \begin{array} { r r } { a } & { b } \\ { - 3 b } & { a } \end{array} } \right]$ , where $a , b \in \mathbb { R }$ . Show that F is a field under the usual matrix operations.

26. Let R be the ring of all $2 \times 2$ matrices of the form $\left[ \begin{array} { r r } { a } & { b } \\ { - b } & { a } \end{array} \right]$ where a and b are real numbers.
    Prove that R is isomorphic to C, the field of complex numbers.

27. Let p be a prime and let R be the ring of all $2 \times 2$ matrices of the form $\left[ \begin{array} { c c } { a } & { b } \\ { p b } & { a } \end{array} \right]$ , where $a , b \in \mathbb { Z }$ . Prove that R is isomorphic to $\mathbb { Z } [ { \sqrt { p } } ]$

28. Let p be a prime and $F _ { p }$ the set of all $2 \times 2$ matrices of the form $\left[ \begin{array} { r r } { a } & { b } \\ { - b } & { a } \end{array} \right]$ , where $a , b \in \mathbb { Z } _ { p }$

(a) Show that $F _ { p }$ is a commutative ring with identity.

(b) Show that $F _ { 7 }$ is a field.

(c) Show that $F _ { 1 3 }$ is not a field.

29. Let $I \subseteq J$ be right ideals of a ring R such that $J / I \cong R$ as right R-modules.
    Prove that there exists a right ideal K such that $I \cap K = ( 0 )$ and $I + K = J$

30. A ring R is called simple if $R ^ { 2 } \neq 0$ and 0 and R are its only ideals.
    Show that the center of a simple ring is 0 or a field.

31. Give an example of a field F and a one-to-one ring homomorphism $\varphi : F  F$ which is not onto.
    Verify your example.

32. Let D be an integral domain and let $D [ x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ]$ be the polynomial ring over D in the n indeterminates $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ . Let

$$
V = \left[ \begin{array} { c c c c c } { x _ { 1 } ^ { n - 1 } } & { \cdot \cdot \cdot } & { x _ { 1 } ^ { 2 } } & { x _ { 1 } } & { 1 } \\ { x _ { 2 } ^ { n - 1 } } & { \cdot \cdot \cdot } & { x _ { 2 } ^ { 2 } } & { x _ { 2 } } & { 1 } \\ { \vdots } & { } & { \vdots } & { \vdots } & { \vdots } \\ { x _ { n } ^ { n - 1 } } & { \cdot \cdot \cdot } & { x _ { n } ^ { 2 } } & { x _ { n } } & { 1 } \end{array} \right] .
$$

Prove that the determinant of V is $\prod _ { 1 \leqslant i < j \leqslant n } ( x _ { i } - x _ { j } )$

33. Let $R = C [ 0 , 1 ]$ be the set of all continuous real-valued functions on [0, 1]. Define addition and multiplication on R as follows.
    For $f , g \in R$ and $x \in [ 0 , 1 ]$ ,

$$
( f + g ) ( x ) = f ( x ) + g ( x ) { \mathrm { ~ a n d ~ } } ( f g ) ( x ) = f ( x ) g ( x ) .
$$

(a) Show that R with these operations is a commutative ring with identity.

(b) Find the units of R.

(c) If $f \in R$ and $f ^ { 2 } = f ,$ , then $f = 0 _ { R }$ or $f = 1 _ { R }$

(d) If n is a positive integer and $f \in R$ is such that $f ^ { n } = 0 _ { R }$ , then $f = 0 _ { R }$

34. Let S be the ring of all bounded, continuous functions $f : \mathbb { R } \to \mathbb { R }$ , where R is the set of real numbers.
    Let I be the set of functions f in S such that $f ( t ) \to 0 { \mathrm { ~ a s ~ } } | t | \to \infty$

(a) Show that I is an ideal of S.

(b) Suppose $x \in S$ is such that there is an $i \in I$ with ix = x. Show that $x ( t ) = 0$ for all sufficiently large |t|.

35. Let Q be the field of rational numbers and $D = \{ a + b { \sqrt { 2 } } \mid a , b \in \mathbb { Q } \}$

(a) Show that D is a subring of the field of real numbers.

(b) Show that D is a principal ideal domain.

(c) Show that $\sqrt { 3 }$ is not an element of D.

36. Show that if p is a prime such that $p \equiv 1 { \bigl ( } { \mathrm { m o d ~ } } 4 { \bigr ) }$ , then $x ^ { 2 } + 1$ is not irreducible in $\mathbb { Z } _ { p } [ x ]$

37. Show that if p is a prime such that $p \equiv 3 ( { \bmod { 4 } } )$ , then $x ^ { 2 } + 1$ is irreducible in $\mathbb { Z } _ { p } [ x ]$

38. Show that if p is a prime such that $p \equiv 1 { \ : } ( \mathrm { m o d \ : } 6 )$ , then $x ^ { 3 } + 1$ splits in $\mathbb { Z } _ { p } [ x ]$

## Prime, Maximal, and Primary Ideals

39. Let R be a non-zero commutative ring with 1. Show that an ideal M of R is maximal if and only if $R / M$ is a field.

40. Let R be a commutative ring with 1. Show that an ideal P of R is prime if and only if $R / P$ is an integral domain.

41. (a) Let R be a commutative ring with 1. Show that if M is a maximal ideal of R then M is a prime ideal of R.

(b) Give an example of a non-zero prime ideal in a ring R that is not a maximal ideal.

42. Let R be a non-zero ring with identity.
    Show that every proper ideal of R is contained in a maximal ideal.

43. [NEW] Let $M _ { 1 } \neq M _ { 2 }$ be two maximal ideals in the commutative ring R and let $I = M _ { 1 } \cap M _ { 2 }$ Prove that $R / I$ is isomorphic to the direct sum of two fields.

44. Let R be a non-zero commutative ring with 1. Show that if I is an ideal of R such that $1 + a$ is a unit in R for all $a \in I ,$ , then I is contained in every maximal ideal of R.

45. [NEW] Let R be a commutative ring with identity.
    Suppose R contains an idempotent element a other than 0 or 1. Show that every prime ideal in R contains an idempotent element other than 0 or 1. (An element $a \in R$ is idempotent if $a ^ { 2 } = a . )$

46. Let R be a commutative ring with 1.

(a) Prove that (x) is a prime ideal in $R [ x ]$ if and only if R is an integral domain.

(b) Prove that (x) is a maximal ideal in R[x] if and only if R is a field.

47. Find all values of a in $\mathbb { Z } _ { 3 }$ such that the quotient ring

$$
\mathbb { Z } _ { 3 } [ x ] / ( x ^ { 3 } + x ^ { 2 } + a x + 1 )
$$

is a field.
Justify your answer.

48. Find all values of a in $\mathbb { Z } _ { 5 }$ such that the quotient ring

$$
\mathbb { Z } _ { 5 } [ x ] / ( x ^ { 3 } + 2 x ^ { 2 } + a x + 3 )
$$

is a field.
Justify your answer.

49. Let R be a commutative ring with identity and let U be maximal among non-finitely generated ideals of R. Prove U is a prime ideal.

50. Let R be a commutative ring with identity and let U be maximal among non-principal ideals of R. Prove U is a prime ideal.

51. Let R be a non-zero commutative ring with 1 and S a multiplicative subset of R not containing 0. Show that if P is maximal in the set of ideals of R not intersecting S, then P is a prime ideal.

52. Let R be a non-zero commutative ring with 1.

(a) Let S be a multiplicative subset of R not containing 0 and let P be maximal in the set of ideals of R not intersecting S. Show that P is a prime ideal.

(b) Show that the set of nilpotent elements of R is the intersection of all prime ideals.

53. Let R be a commutative ring with identity and let $x \in R$ be a non-nilpotent element.
    Prove that there exists a prime ideal P of R such that $x \notin P$

54. Let R be a commutative ring with identity and let S be the set of all elements of R that are not zero-divisors.
    Show that there is a prime ideal P such that $P \cap S$ is empty.
    (Hint: Use Zorn’s Lemma.)

55. Let R be a commutative ring with identity and let C be a chain of prime ideals of R. Show that $\cup _ { P \in { \mathcal { C } } } P$ and $\cap _ { P \in { \mathcal { C } } } P$ are prime ideals of R.

56. Let R be a commutative ring and P a prime ideal of R. Show that there is a prime ideal $P _ { 0 } \subseteq P$ that does not properly contain any prime ideal.

57. Let R be a commutative ring with 1 such that for every x in R there is an integer $n > 1$ (depending on x) such that $x ^ { n } = x$ . Show that every prime ideal of R is maximal.

58. Let R be a commutative ring with 1 in which every ideal is a prime ideal.
    Prove that R is a field.
    (Hint: For $a \neq 0$ consider the ideals (a) and $( a ^ { 2 } ) . \mathrm { , }$ )

59. Let D be a principal ideal domain.
    Prove that every nonzero prime ideal of D is a maximal ideal.

60. Show that if R is a finite commutative ring with identity then every prime ideal of R is a maximal ideal.

61. Let $R = C [ 0 , 1 ]$ be the ring of all continuous real-valued functions on [0, 1], with addition and multiplication defined as follows.
    For $f , g \in R$ and $x \in [ 0 , 1 ]$

$$
\begin{array} { l } { { ( f + g ) ( x ) = f ( x ) + g ( x ) } } \\ { { ( f g ) ( x ) = f ( x ) g ( x ) . } } \end{array}
$$

Prove that if M is a maximal ideal of R, then there is a real number $x _ { 0 } \in [ 0 , 1 ]$ such that $M = \{ f \in R \mid f ( x _ { 0 } ) = 0 \}$ .

62. Let R be a commutative ring with identity, and let $P \subset Q$ be prime ideals of R. Prove that there exist prime ideals $P ^ { * } , Q ^ { * }$ satisfying $P \subseteq P ^ { * } \subset Q ^ { * } \subseteq Q$ , such that there are no prime ideals strictly between $P ^ { * }$ and $Q ^ { * }$ . HINT: Fix $x \in Q - P$ and show that there exists a prime ideal $P ^ { * }$ containing P , contained in Q and maximal with respect to not containing x.

63. Let R be a commutative ring with 1. An ideal I of R is called a primary ideal if $I \neq R$ and for all $x , y \in R$ with $x y \in I$ , either $x \in I$ or $y ^ { n } \in I$ for some integer n $\geqslant 1$ .

(a) Show that an ideal I of R is primary if and only if $R / I \ne 0$ and every zero-divisor in $R / I$ is nilpotent.

(b) Show that if I is a primary ideal of R then the radical Rad(I) of I is a prime ideal.
(Recall that $\operatorname { R a d } ( I ) = \{ x \in R \mid x ^ { n } \in I$ for some n}.)

## Commutative Rings

64. Let R be a commutative ring with identity.
    Show that R is an integral domain if and only if R is a subring of a field.

65. Let R be a commutative ring with identity.
    Show that if x and y are nilpotent elements of R then $x + y$ is nilpotent and the set of all nilpotent elements is an ideal in R.

66. Let R be a commutative ring with identity.
    An ideal I of R is irreducible if it cannot be expressed as the intersection of two ideals of R neither of which is contained in the other.
    Show the following.

(a) If P is a prime ideal then P is irreducible.

(b) If x is a non-zero element of R, then there is an ideal $I _ { x }$ , maximal with respect to the property that $x \notin I _ { x } .$ , and $I _ { x }$ is irreducible.

(c) If every irreducible ideal of R is a prime ideal, then 0 is the only nilpotent element of R.

67. Let R be a commutative ring with 1 and let I be an ideal of R satisfying $I ^ { 2 } = \{ 0 \}$ . Show that if $a + I \in R / I$ is an idempotent element of $R / I$ , then the coset $a + I$ contains an idempotent element of R.

68. Let R be a commutative ring with identity that has exactly one prime ideal P . Prove the following.

(a) $R / P$ is a field.

(b) R is isomorphic to $R _ { P }$ , the ring of quotients of R with respect to the multiplicative set $R - P = \{ s \in R \mid s \not \in P \}$

69. Let R be a commutative ring with identity and $\sigma : R  R$ a ring automorphism.

(a) Show that $F = \{ r \in R \mid \sigma ( r ) = r \}$ is a subring of R and the identity of R is in F .

(b) Show that if $\sigma ^ { 2 }$ is the identity map on R, then each element of R is the root of a monic polynomial of degree two in $F [ x ]$

70. Let R be a commutative ring with identity that has exactly three ideals, {0}, I, and R.

(a) Show that if $a \not \in I ,$ then a is a unit of R.

(b) Show that if $a , b \in I$ then $a b = 0$

71. Let R be a commutative ring with 1. Show that if u is a unit in R and n is nilpotent, then $u + n$ is a unit.

72. Let R be a commutative ring with identity.
    Suppose that for every $a \in R$ , either a or $1 - a$ is invertible.
    Prove that $N = \{ a \in R \mid$ a is not invertible} is an ideal of R.

73. Let R be a commutative ring with 1. Show that the sum of any two principal ideals of R is principal if and only if every finitely generated ideal of R is principal.

74. Let R be a commutative ring with identity such that not every ideal is a principal ideal.

(a) Show that there is an ideal I maximal with respect to the property that I is not a principal ideal.

(b) If I is the ideal of part (a), show that $R / I$ is a principal ideal ring.

75. Recall that if $R \subseteq S$ is an inclusion of commutative rings (with the same identity) then an element $s \in S$ is integral over R if s satisfies some monic polynomial with coefficients in R. Prove the equivalence of the following statements.

(i) s is integral over R.

(ii) $R [ s ]$ is finitely generated as an R-module.

(iii) There exists a faithful $R [ s ]$ module which is finitely generated as an R-module.

76. Recall that if $R \subseteq S$ is an inclusion of commutative rings (with the same identity) then S is an integral extension of R if every element of S satisfies some monic polynomial with coefficients in R. Prove that if $R \subseteq S \subseteq T$ are commutative rings with the same identity, then S is integral over R and T is integral over S if and only if T is integral over R.

77. Let $R \subseteq S$ be commutative domains with the same identity, and assume that S is an integral extension of R. Let I be a nonzero ideal of S. Prove that I ∩ R is a nonzero ideal of R.

## Domains

78. Suppose R is a domain and I and J are ideals of R such that IJ is principal.
    Show that I (and by symmetry J) is finitely generated.

[Hint: If $I J = ( a )$ , then $a = \sum _ { i = 1 } ^ { n } x _ { i } y _ { i }$ for some $x _ { i } \in I$ and $y _ { i } \in J$ . Show the $x _ { i }$ generate I.]

79. [NEW] Prove that if D is a Euclidean Domain, then D is a Principal Ideal Domain.

80. Show that if p is a prime such that there is an integer b with $p = b ^ { 2 } + 4$ , then $\mathbb { Z } [ { \sqrt { p } } ]$ is not a unique factorization domain.

81. Show that if p is a prime such that $p \equiv 1 ( { \bmod { 4 } } )$ , then $\mathbb { Z } [ { \sqrt { p } } ]$ is not a unique factorization domain.

82. Let $D = \mathbb { Z } ( { \sqrt { 5 } } ) = \{ m + n { \sqrt { 5 } } \mid m , n \in \mathbb { Z } \} - \mathbf { a }$ subring of the field of real numbers and necessarily an integral domain (you need not show this) — and $F = \mathbb { Q } ( { \sqrt { 5 } } )$ its field of fractions.
    Show the following:

(a) $x ^ { 2 } + x - 1$ is irreducible in $D [ x ]$ but not in $F [ x ]$

(b) D is not a unique factorization domain.

83. Let $D = \mathbb { Z } ( { \sqrt { 2 1 } } ) = \{ m + n { \sqrt { 2 1 } } \mid m , n \in \mathbb { Z } \}$ and $F = \mathbb { Q } ( { \sqrt { 2 1 } } )$ , the field of fractions of D. Show the following:

(a) $x ^ { 2 } - x - 5$ is irreducible in $D [ x ]$ but not in $F [ x ]$

(b) D is not a unique factorization domain.

84. Let $D = \mathbb { Z } ( { \sqrt { - 1 1 } } ) = \{ m + n { \sqrt { - 1 1 } } \mid m , n \in \mathbb { Z } \}$ and $F = \mathbb { Q } ( { \sqrt { - 1 1 } } )$ its field of fractions.
    Show the following:

(a) $x ^ { 2 } - x + 3$ is irreducible in $D [ x ]$ but not in $F [ x ]$

(b) D is not a unique factorization domain.

85. Let $D = \mathbb { Z } ( { \sqrt { 1 3 } } ) = \{ m + n { \sqrt { 1 3 } } \mid m , n \in \mathbb { Z } \}$ and $F = \mathbb { Q } ( { \sqrt { 1 3 } } )$ its field of fractions.
    Show the following:

(a) $x ^ { 2 } + 3 x - 1$ is irreducible in $D [ x ]$ but not in $F [ x ]$

(b) D is not a unique factorization domain.

86. Let D be an integral domain and F a subring of D that is a field.
    Show that if each element of D is algebraic over F , then D is a field.

87. Let R be an integral domain containing the subfield F and assume that R is finite dimensional over F when viewed as a vector space over F . Prove that R is a field.

88. Let D be an integral domain.

(a) For $a , b \in D$ define a greatest common divisor of a and b.

(b) For $x \in D$ denote $( x ) = \{ d x \mid d \in D \}$ . Prove that if $( a ) + ( b ) = ( d )$ , then d is a greatest common divisor of a and b.

89. Let D be a principal ideal domain.

(a) For $a , b \in D$ , define a least common multiple of a and b.

(b) Show that $d \in D$ is a least common multiple of a and b if and only if $( a ) \cap ( b ) = ( d )$

90. Let D be a principal ideal domain and let $a , b \in D$

(a) Show that there is an element $d \in D$ that satisfies the properties i. d|a and d|b and ii.
if e|a and e|b then $e | d .$

(b) Show that there is an element $m \in D$ that satisfies the properties d b|

i. a|m and b|m and

ii.
if $a | e$ and b|e then $m | e$

91. Let R be a principal ideal domain.
    Show that if (a) is a nonzero ideal in R, then there are only finitely many ideals in R containing (a).

92. Let D be a unique factorization domain and F its field of fractions.
    Prove that if d is an irreducible element in D, then there is no $x \in F$ such that $x ^ { 2 } = d .$

93. Let D be a Euclidean domain.
    Prove that every non-zero prime ideal is a maximal ideal.

94. Let π be an irreducible element of a principal ideal domain R. Prove that π is a prime element (that is, π | ab implies ${ \pi } \mid a \ \mathrm { o r } \ \pi \mid b )$

95. Let D with $\varphi : D - \{ 0 \} \to \mathbb { N }$ be a Euclidean domain.
    Suppose $\varphi ( a + b ) \leqslant$ max $\{ \varphi ( a ) , \varphi ( b ) \}$ for all $a , b \in D$ . Prove that D is either a field or isomorphic to a polynomial ring over a field.

96. Let D be an integral domain and F its field of fractions.
    Show that if g is an isomorphism of D onto itself, then there is a unique isomorphism h of F onto F such that $h ( d ) = g ( d )$ for all d in D.

97. Let D be a unique factorization domain such that if p and q are irreducible elements of $D$ then p and q are associates.
    Show that if A and B are ideals of D, then either $A \subseteq B$ or $B \subseteq A$

98. Let D be a unique factorization domain and p a fixed irreducible element of D such that if q is any irreducible element of $D ,$ then q is an associate of $p .$ Show the following.

(a) If d is a nonzero element of D, then d is uniquely expressible in the form $u p ^ { n }$ , where u is a unit of D and n is a non-negative integer.

(b) D is a Euclidean domain.

99. Prove that $\mathbb { Z } [ \sqrt { - 2 } ] = \{ a + b \sqrt { - 2 } \ | \ a , b \in \mathbb { Z } \}$ is a Euclidean domain.

100. Show that the ring Z[i] of Gaussian integers is a Euclidean ring and compute the greatest common divisor of $5 + i$ and 13 using the Euclidean algorithm.

## Polynomial Rings

101. Show that the polynomial $f ( x ) = x ^ { 4 } + 5 x ^ { 2 } + 3 x + 2$ is irreducible over the field of rational numbers.

102. Let D be an integral domain and $D [ x ]$ the polynomial ring over D. Suppose $\varphi : D [ x ]  D [ x ]$ is an isomorphism such that $\varphi ( d ) = d$ for all $d \in D$ . Show that $\varphi ( x ) = a x + b$ for some $a , b \in D$ and that a is a unit of D.

103. Let $f ( x ) = a _ { 0 } + a _ { 1 } x + \cdots + a _ { k } x ^ { k } + \cdots + a _ { n } x ^ { n } \in \mathbb { Z } [ x ]$ and p a prime such that $p | a _ { i }$ for $i = 1 , \ldots , k - 1 , p \nmid a _ { k } , p \nmid a _ { n }$ , and $p ^ { 2 } \nmid a _ { 0 }$ . Show that $f ( x )$ has an irreducible factor in $\mathbb { Z } [ x ]$ of degree at least k.

104. Let D be an integral domain and $D [ x ]$ the polynomial ring over D in the indeterminate x. Show that if every nonzero prime ideal of $D [ x ]$ is a maximal ideal, then D is a field.

105. Let R be a commutative ring with 1 and let $f ( x ) \ \in \ R [ x ]$ be nilpotent.
     Show that the coefficients of f are nilpotent.

106. Show that if R is an integral domain and $f ( x )$ is a unit in the polynomial ring $R [ x ]$ , then $f ( x )$ is in R.

107. Let D be a unique factorization domain and F its field of fractions.
     Prove that if $f ( x )$ is a monic polynomial in $D [ x ]$ and $\alpha \in F$ is a root of $f ,$ then $\alpha \in D$ .

108. (a) Show that $x ^ { 4 } + x ^ { 3 } + x ^ { 2 } + x + 1$ is irreducible in $\mathbb { Z } _ { 3 } [ x ]$

(b) Show that $x ^ { 4 } + 1$ is not irreducible in $\mathbb { Z } _ { 3 } [ x ]$

109. Let $F [ x , y ]$ be the polynomial ring over a field F in two indeterminates $x , y$ . Show that the ideal generated by $\{ x , y \}$ is not a principal ideal.

110. Let F be a field.
     Prove that the polynomial ring $F [ x ]$ is a PID and that $F [ x , y ]$ is not a PID.

111. Let D be an integral domain and let c be an irreducible element in D. Show that the ideal $( x , c )$ generated by x and c in the polynomial ring $D [ x ]$ is not a principal ideal.

112. [CORRECTED] Show that if R is a commutative ring with 1 that is not a field, then $R [ x ]$ is not a principal ideal domain.

113. (a) Let $\begin{array} { r } { \mathbb { Z } \left[ \frac { 1 } { 2 } \right] = \left\{ \frac { a } { 2 ^ { n } } \ : \middle | \ : a , n \in \mathbb { Z } , n \geqslant 0 \right\} } \end{array}$ , the smallest subring of Q containing Z and $\frac { 1 } { 2 }$ . Let $( 2 x - 1 )$ be the ideal of Z[x] generated by the polynomial $2 x - 1$ Show that $\mathbb { Z } [ x ] / ( 2 x - 1 ) \cong \mathbb { Z } \left[ { \frac { 1 } { 2 } } \right]$

(b) Find an ideal I of $\mathbb { Z } [ x ]$ such that $( 2 x - 1 ) \subsetneq I \subsetneq \mathbb { Z } [ x ]$

## Non-commutative Rings

114. Let R be a ring with identity such that the identity map is the only ring automorphism of R. Prove that the set N of all nilpotent elements of R is an ideal of R.

115. Let p be a prime.
     A ring S is called a p-ring if the characteristic of S is a power of p. Show that if R is a ring with identity of finite characteristic, then R is isomorphic to a finite direct product of p-rings for distinct primes.

116. Let R be a ring.

(a) Show that there is a unique smallest (with respect to inclusion) ideal A such that $R / A$ is a commutative ring.

(b) Give an example of a ring R such that for every proper ideal $I , R / I$ is not commutative.
Verify your example.

(c) For the ring $R = \left\{ { \left[ \begin{array} { l l } { a } & { b } \\ { 0 } & { c } \end{array} \right] } \mid a , b , c \in \mathbb { Z } \right\}$ with the usual matrix operations, find the ideal A of part (a).

117. If R is any ring with identity, let $J ( R )$ denote the Jacobson radical of R. Show that if e is any idempotent of R, then $J ( e R e ) = e J ( R ) e$

118. If n is a positive integer and F is any field, let $M _ { n } ( F )$ denote the ring of $n \times n$ matrices with entries in F . Prove that $M _ { n } ( F )$ is a simple ring.
     Equivalently, End $F  ^ { ( V ) }$ is a simple ring if V is a finite dimensional vector space over F .

119. A ring R is nilpotent-free if $a ^ { n } = 0$ for $a \in R$ and some positive integer n implies $a = 0$

(a) Suppose there is an ideal I such that $R / I$ is nilpotent-free.
Show there is a unique smallest (with respect to inclusion) ideal A such that $R / A$ is nilpotent-free.

(b) Give an example of a ring R such that for every proper ideal $I , R / I$ is not nilpotent-free.
Verify your example.

(c) Show that if R is a commutative ring with identity, then there is a proper ideal I of R such that $R / I$ is nilpotent-free, and find the ideal A of part (a).

## Local Rings, Localization, Rings of Fractions

120. Let R be an integral domain.
     Construct the field of fractions F of R by defining the set F and the two binary operations, and show that the two operations are well-defined.
     Show that F has a multiplicative identity element and that every nonzero element of F has a multiplicative inverse.

121. A local ring is a commutative ring with 1 that has a unique maximal ideal.
     Show that a ring R is local if and only if the set of non-units in R is an ideal.

122. Let R be a commutative ring with $1 \neq 0$ in which the set of nonunits is closed under addition.
     Prove that R is local, i.e., has a unique maximal ideal.

123. Let D be an integral domain and F its field of fractions.
     Let P be a prime ideal in D and $D _ { P } = \{ a b ^ { - 1 } \mid a , b \in D , \ b \notin P \} \subseteq F$ . Show that $D _ { P }$ has a unique maximal ideal.

124. Let R be a commutative ring with identity and M a maximal ideal of R. Let $R _ { M }$ be the ring of quotients of R with respect to the multiplicative set $R - M = \{ s \in R \mid s \not \in M \}$ . Show the following.

(a) $\begin{array} { r } { M _ { M } = \{ \frac { a } { s } \mid a \in M , s \not \in M \} } \end{array}$ is the unique maximal ideal of $R _ { M }$

(b) The fields $R / M$ and $R _ { M } / M _ { M }$ are isomorphic.

125. Let R be an integral domain, S a multiplicative set, and let $\begin{array} { r } { S ^ { - 1 } R = \{ \frac { r } { s } \ | \ r \in R , \ s \in S \} } \end{array}$ (contained in the field of fractions of R). Show that if P is a prime ideal of R, then $S ^ { - 1 } P$ is either a prime ideal of $S ^ { - 1 } R$ or else equals $S ^ { - 1 } R$

126. Let R be a commutative ring with identity and P a prime ideal of R. Let $R _ { P }$ be the ring of quotients of R with respect to the set $R - P = \{ s \in R \mid s \not \in P \}$ . Show that $R _ { P } / P _ { P }$ is the field of fractions of the integral domain $R / P$

127. Let D be an integral domain and F its field of fractions.
     Denote by M the set of all maximal ideals of D. For $M \in \mathcal { M }$ , let $\begin{array} { r } { D _ { M } = \{ \frac { a } { s } \ | \ a , s \in D , s \not \in M \} \subset F } \end{array}$ . Show that $\bigcap _ { M \in { \mathcal { M } } } D _ { M } = D$

128. Let R be a commutative ring with 1 and D a multiplicative subset of R containing 1. Let J be an ideal in the ring of fractions $D ^ { - 1 } R$ and let

$$
I = \{ a \in R \mid { \frac { a } { d } } \in J { \mathrm { ~ f o r ~ s o m e ~ } } d \in D \} .
$$

Show that I is an ideal of R.

129. Let D be a principal ideal domain and let P be a non-zero prime ideal.
     Show that $D _ { P }$ , the localization of D at P , is a principal ideal domain and has a unique irreducible element, up to associates.

## Chains and Chain Conditions

130. Let R be a commutative ring with identity.
     Prove that any non-empty set of prime ideals of R contains maximal and minimal elements.

131. Let R be a commutative ring with 1. We say R satisfies the ascending chain condition if whenever $I _ { 1 } \subseteq I _ { 2 } \subseteq I _ { 3 } \subseteq \cdots$ · is an ascending chain of ideals, there is an integer N such that $I _ { k } = I _ { N }$ for all $k \geqslant N$ Show that R satisfies the ascending chain condition if and only if every ideal of R is finitely generated.

132. [NEW] Define Noetherian ring and prove that if R is Noetherian, then R[x] is Noetherian.

133. Let R be a commutative Noetherian ring with identity.
     Prove that there are only finitely many minimal prime ideals of R.

134. [NEW] Let R be a commutative Noetherian ring in which every 2-generated ideal is principal.
     Prove that R is a Principal Ideal Domain.

135. Let R be a commutative Noetherian ring with identity and let I be an ideal in R. Let $J = { \mathrm { R a d } } ( I )$ . Prove that there exists a positive integer n such that $j ^ { n } \in I$ for all $j \in J$

136. Let R be a commutative Noetherian domain with identity.
     Prove that every nonzero ideal of R contains a product of nonzero prime ideals of R.

137. Let R be a ring satisfying the descending chain condition on right ideals.
     If J(R) denotes the Jacobson radical of R, prove that J(R) is nilpotent.

138. Show that if R is a commutative Noetherian ring with identity, then the polynomial ring R[x] is also Noetherian.

139. Let P be a nonzero prime ideal of the commutative Noetherian domain R. Assume P is principal.
     Prove that there does not exist a prime ideal Q satisfying $( 0 ) < Q < P$

140. Let R be a commutative Noetherian ring.
     Prove that every nonzero ideal A of R contains a product of prime ideals (not necessarily distinct) each of which contains A.

141. Let R be a commutative ring with 1 and let M be an R-module that is not Artinian (Noetherian, of finite composition length).
     Let I be the set of ideals I of R such that there exists an R-submodule N of M with the property that N/NI is not Artinian (Noetherian, of finite composition length, respectively).
     Show that if $A \in \mathcal { T }$ is a maximal element of I, then A is a prime ideal of R.
