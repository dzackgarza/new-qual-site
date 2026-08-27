## Solution Outlines for Chapter 17

## # 2: Suppose that D is an integral domain and F is a field containing D. If $f ( x ) \in D [ x ]$ and $f ( x )$ is irreducible over F but reducible over $D _ { : }$ , what can you say about the factorization of $f ( x )$ over D?

Suppose that $f ( x )$ is reducible over D. Then $f ( x ) = g ( x ) h ( x )$ for some $g ( x ) , h ( x ) \in D [ x ]$ Now, all elements of D are in F , so $f ( x ) = g ( x ) h ( x )$ in $F [ x ]$ . But since $f ( x )$ is irreducible, $g ( x )$ or $h ( x )$ is a unit in F . So $f ( x ) = a g ( x )$ for some $g ( x )$ and some $a \in D$ that is not a unit in D but is a unit in F .

## # 8: Suppose that $f ( x ) \in \mathbb { Z } _ { p } [ x ]$ and $f ( x )$ is irreducible over $\mathbb { Z } _ { p }$ where $p$ is a prime. If $d e g ( f ( x ) ) = n$ n, prove that $\mathbb { Z } _ { p } [ x ] / < f ( x ) >$ is a field with $p ^ { n }$ elements.

Since $f ( x )$ is irreducible, $< f ( x ) >$ is maximal and $\mathbb { Z } _ { p } [ x ] / < f ( x ) >$ is a field. Now since the degree of $f ( x )$ is n, every element in $\mathbb { Z } _ { p } [ x ] / < f ( x ) >$ can be written as $a _ { n - 1 } x ^ { n - 1 } +$ $a _ { n - 2 } x ^ { n - 2 } + \cdot \cdot \cdot + a _ { 1 } x + a _ { 0 } + < f ( x ) >$ . [Not sure why the previous statement is true? Recall that for any polynomial $g ( x )$ in $\mathbb { Z } _ { p } [ x ] , g ( x ) = f ( x ) q ( x ) + r ( x )$ where the degree of $r ( x )$ is less than the degree of $f ( x )$ or $r ( x ) = 0$ . So $g ( x ) + < f ( x ) > = f ( x ) q ( x ) + r ( x ) + < f ( x ) > =$ $r ( x ) + < f ( x ) > . ]$ Since each $a _ { i }$ is in $\mathbb { Z } _ { p } .$ , there are p options for each coefficient in the coset representative. So there are $p \times p \times \cdot \cdot \cdot \times p = p ^ { n }$ possible standard representatives. Moreover, it is clear that each is unique.

## # 9: Construct a field of order 25.

Since $2 5 = 5 ^ { 2 }$ , start with $\mathbb { Z } _ { 5 } [ x ]$ Now, we must find a degree 2 polynomial, $p ( x )$ , that is irreducible over $\mathbb { Z } _ { 5 }$ . Then $\mathbb { Z } _ { 5 } [ x ] / < p ( x ) >$ is a field of order $5 ^ { * } 5 = 2 5$ . Now, lets start with $p ( x ) = x ^ { 2 } + x + a$ . Then $p ( 0 ) = a , p ( 1 ) = a + 2 , p ( 2 ) = a + 1 , p ( 3 ) = 2 + a$ , and $p ( 4 ) = a$ . So $a \neq 0 , 3 , 4$ . Choose $a = 1$ . Then $p ( x ) = x ^ { 2 } + x + 1$ is irreducible over $\mathbb { Z } _ { 5 }$ and works to give us the field we want.

## # 12: Determine which of the polynomials below is (are) irreducible over $\mathbb { Q } .$

a. $x ^ { 5 } + 9 x ^ { 4 } + 1 2 x ^ { 2 } + 6 \cdot$ : Irreducible. Use Eisenstein’s with $p = 3$

b. $x ^ { 4 } + x + 1$ : Irreducible. In $\mathbb { Z } _ { 2 } [ x ]$ this polynomial is $f ( x ) = x ^ { 4 } + x + 1$ (notice the degree is preserved). Now $f ( 0 ) = 1$ and $f ( 1 ) = 1$ so $f ( x )$ is irreducible over $\mathbb { Z } _ { 2 }$ and thus over Q. Alternately, the rational roots theorem tells us ±1 are the only possible rational roots and neither works.

c. $x ^ { 4 } + 3 x ^ { 2 } + 3 \colon$ : Irreducible. Use Eisenstein’s with $p = 3$

d. $x ^ { 5 } + 5 x ^ { 2 } + 1$ : Irreducible. In $\mathbb { Z } _ { 2 } [ x ]$ this polynomial is $f ( x ) = x ^ { 5 } + x ^ { 2 } + 1$ (notice the degree is preserved). Now $f ( 0 ) = 1$ and $f ( 1 ) = 1 \mathrm { \ s o \ } f ( \boldsymbol { x } )$ is irreducible over $\mathbb { Z } _ { 2 }$ and thus over Q. Alternately, the rational roots theorem tells us $\pm 1$ are the only possible rational roots and neither works.

e. $( { \textstyle { \frac { 5 } { 2 } } } ) x ^ { 5 } + ( { \textstyle { \frac { 9 } { 2 } } } ) x ^ { 4 } + 1 5 x ^ { 3 } + ( { \textstyle { \frac { 3 } { 7 } } } ) x ^ { 2 } + 6 x + { \textstyle { \frac { 3 } { 1 4 } } }$ : Irreducible. Call the polynomial $f ( x )$ . Then $1 \hat { 4 } f ( x ) = \hat { 3 } 5 x ^ { 5 } + 6 3 x ^ { 4 } + 1 \dot { 0 } 5 x ^ { 3 } + 6 x ^ { 2 } + \dot { 8 } 4 x + 3$ . Now $1 4 f ( x )$ is irreducible by Eisenstein’s with $p = 3$ . Hence $f ( x )$ is irreducible.

# 15: Let $f ( x ) = x ^ { 3 } + 6 \in \mathbb { Z } _ { 7 } [ x ]$ . Write $f ( x )$ as a product of irreducible polynomials over $\mathbb { Z } _ { 7 }$

Since the degree of $f ( x )$ is 3, any factor must correspond to a 0. So $f ( 0 ) = 3 , f ( 1 ) = 0$ $f ( 2 ) = 0 , f ( 3 ) = 5 , f ( 4 ) = 0 , f ( 5 ) = 5 , f ( 6 ) = 5 . \mathrm { ~ S o ~ } f ( x ) = ( x - 1 ) ( x - 2 ) ( x - 4 ) = 0 .$ $( x + 6 ) ( x + 5 ) ( x + 3 )$ . (Notice that each root occurs with multiplicity 1 because of the degree.)

# 19: Show that for every prime p there exists a field of order $p ^ { 2 } .$

Let’s think about $\mathbb { Z } _ { p } [ \boldsymbol { x } ]$ . By exercise $1 8 / 1 7$ (these are fundamentally the same problem), there is a degree 2 polynomial that is irreducible over $\mathbb { Z } _ { p } .$ , say $f ( x )$ . Thus $\mathbb { Z } _ { p } [ x ] / < f ( x ) >$ is a field of order $p ^ { 2 }$ or less (see exercise 9 if you don’t understand why this is the order). Now $a x + b + < f ( x ) > = c x + d + < f ( x ) >$ implies that $( a - c ) x + ( b - d )$ is divisible by $f ( x )$ This means that $a = c$ and $b = d .$ Thus the order is precisely $p ^ { 2 }$

# 20: Prove that, for every positive integer n, there are infinitely many polynomials of degree n in $\mathbb { Z } [ x ]$ that are irreducible over Q.

Fix n. Consider the infinite class of polynomials of order $x ^ { n } + p$ where p is a prime. Then, by Eisenstein’s, $x ^ { n } + p$ is irreducible over Q.

# 21: Show that the field given in Example 11 in this chapter is isomorphic to the field given in Example 9 in Chapter 13.

The example 11 field is: $\mathbb { Z } _ { 3 } [ x ] / < x ^ { 2 } + 1 >$ . The example 9 field is: $\mathbb { Z } _ { 3 } [ i ]$ . Define $\phi : \mathbb { Z } _ { 3 } [ x ] / <$ $x ^ { 2 } + 1 > \to \mathbb { Z } _ { 3 } [ i ]$ by φ $\ f ( x ) + < x ^ { 2 } + 1 > ) = f ( i )$ . Then $\phi ( f ( x ) + < x ^ { 2 } + 1 > + g ( x ) + < x ^ { 2 } + 1 >$ $) = \phi ( f ( x ) + g ( x ) + < x ^ { 2 } + 1 > ) = f ( i ) + g ( i ) = \phi ( f ( x ) + < x ^ { 2 } + 1 > ) + \phi ( g ( x ) + < x ^ { 2 } + 1 > )$ and $\phi ( ( f ( x ) + < x ^ { 2 } + 1 > ) ( g ( x ) + < x ^ { 2 } + 1 > ) ) = \phi ( f ( x ) g ( x ) + < x ^ { 2 } + 1 > ) = f ( \bar { \iota } ) g ( \bar { \iota } ) = 0 .$ $\phi ( f ( x ) + < x ^ { 2 } + 1 > ) \phi ( g ( x ) + < x ^ { 2 } + 1 > )$ . Thus φ is a homomorphism. Now, $k e r \phi =$ $\{ f ( x ) + < x ^ { 2 } + 1 > | f ( i ) = 0 \} = \{ a x + b + < x ^ { 2 } + 1 > | a i + b = 0$ where $a , b \in \mathbb { Z } _ { 3 } \} = < x ^ { 2 } + 1 >$ so φ is 1-1. Now let $a + b i \in \mathbb { Z } _ { 3 } [ i ]$ . Then $a + b x + < x ^ { 2 } + 1 >$ maps to $a + b i$ so φ is onto. Thus, these fields are isomorphic.

## # 23: Find all monic irreducible polynomials of degree 2 over $\mathbb { Z } _ { 3 }$

So this means that the polynomial must look like $x ^ { 2 } + a x + b$ where $b \neq 0$ . Suppose $b = 1$ Then $x ^ { 2 } + a x + 1 = f ( x )$ Then $f ( 0 ) = 1 , f ( 1 ) = a + 2 ,$ and $f ( 2 ) = 2 + 2 a$ . So $a \neq 1 , 2$ Thus $x ^ { 2 } + 1$ is irreducible. Now suppose $b = 2 .$ . Then $f ( x ) = x ^ { 2 } + a x + 2 \qquad $ . So $f ( 0 ) = 2$ $f ( 1 ) = a$ a, and $f ( 2 ) = 2 a$ . Thus $a \neq 0$ So $x ^ { 2 } + x + 2$ and $x ^ { 2 } + 2 x + 2$ are irreducible. Final answer: $x ^ { 2 } + 1 , x ^ { 2 } + x + 2 , x ^ { 2 } + 2 x + 2$

# 24: Given that π is not the zero of a nonzero polynomial with rational coefficients, prove that $\pi ^ { 2 }$ cannot be written in the form $a \pi + b ,$ where a and b are rational.

Suppose that $\pi ^ { 2 }$ can be written as $a \pi + b$ . Then set $g ( x ) ~ = ~ x ^ { 2 } - a x - b . ~ \mathrm { S o } ~ g ( \pi ) ~ =$ $\pi ^ { 2 } - a \pi - b = a \pi + b - a \pi - b = 0 ~ \mathrm { s o } ~ \pi$ is a zero of a nonzero polynomial with rational coefficients, which is a contradiction.

# 26: Find all zeros of $f ( x ) = 3 x ^ { 2 } + x + 4$ over $\mathbb { Z } _ { 7 }$ by substitution. Find all zeros of $f ( x )$ by using the quadratic formula. Do your answers agree? Should they? Find all zeros of $g ( x ) = 2 x ^ { 2 } + x + 3$ over $\mathbb { Z } _ { 5 }$ by substitution. Try the quadratic formula on $g ( x )$ . Do your answers agree? State necessary and sufficient conditions for the quadratic formula to yield the zeros of a quadratic from $\mathbb { Z } _ { p } [ \boldsymbol { x } ]$ , where p is a prime greater than 2.

Using substitution we see $f ( 4 ) = 0 = f ( 5 )$ so the roots are 4 and 5 Using the quadratic√ formula, we have $( - 1 \pm { \sqrt { - 4 7 } } ) ( 6 ) ^ { - 1 } = ( 6 \pm { \sqrt { 2 } } ) ( 6 ) = ( 6 \pm 3 ) ( 6 ) = 4 , 5$

Now for $g ( x )$ , we see by substitution that there are no zeros in $\mathbb { Z } _ { 5 }$ . Using the quadratic formula, we have $( - 1 \pm { \sqrt { 2 } } ) ( 2 ^ { - 1 } )$ but no number in $\mathbb { Z } _ { 5 }$ squares to 5, so there are no solutions.

Since every number has a multiplicative inverse in $\mathbb { Z } _ { p } ,$ , the only problem occurs when $b ^ { 2 } -$ 4ac is not a square. Thus there are zeros in $\mathbb { Z } _ { p }$ when $b ^ { 2 } - 4 a c = d ^ { 2 }$ for some $d \in \mathbb { Z } _ { p }$

# 31: Let F be a field and let $p ( x )$ be irreducible over F . If E is a field that contains F and there is an element a in E such that $p ( a ) = 0$ , show that the mapping $\phi : F [ x ] \to E$ given by $f ( x )  f ( a )$ is a ring homomorphism with kernel $< p ( x ) >$

Let $\phi , \ F , \ p ( x )$ , E and a be defined as above. Then $\phi ( f ( x ) + g ( x ) ) = f ( a ) + g ( a ) =$ $\phi ( f ( x ) ) + \phi ( g ( x ) )$ and $\phi ( f ( x ) g ( x ) ) = f ( a ) g ( a ) = \phi ( f ( x ) ) \phi ( g ( x ) )$ Clearly $p ( x )$ is in the kernel of $\phi$ . Moreover, since $p ( x )$ is irreducible, $< p ( x ) >$ is a maximal ideal. So that means that the kernel of $\phi$ is precisely $< p ( x ) >$