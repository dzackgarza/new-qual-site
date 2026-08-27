## Solution Outlines for Chapter 15

## # 11: Prove that the intersection of any collection of subfields of a field F is a subfield of F.

We know that every field contains 1 and 0, so the intersection of subfields is non-empty. Since a, b are in the intersection means that $a , b$ is in each subfield, ab and $a - b$ are in each subfield. Hence the intersection is an additive subgroup and is closed under multiplication. The only other thing to check that is not inherited is that every element in the intersection has a multiplicative inverse in the intersection but this is clear because the inverse must be in each subfield.

# 12: Let $\mathbb { Z } _ { 3 } [ i ] = \{ a + b i | a , b \in \mathbb { Z } _ { 3 } \}$ . Show that the field $\mathbb { Z } _ { 3 } [ i ]$ is ring-isomorphic to the field $\mathbb { Z } _ { 3 } [ x ] / < x ^ { 2 } + 1 >$

Define $\phi ( a + b i ) = a + b i + < x ^ { 2 } + 1 >$ . Then $\phi ( ( a + b i ) + ( c + d i ) ) = \phi ( ( a + c ) + ( b + d ) i ) =$ $( a + c ) + ( b + d ) i + < x ^ { 2 } + 1 > = ( a + b i ) + ( c + d i ) + < x ^ { 2 } + 1 > = ( a + b i + < x ^ { 2 } + 1 > ) + ( c + d i ) + < x ^ { 2 } + 1 >$ $x ^ { 2 } + 1 > = \phi ( a + b i ) + \phi ( c + d i )$ . Farther, $\phi ( ( a + b i ) ( c + d i ) ) = \phi ( ( a c - b d ) + ( a d + b c ) i ) =$ $( a c - b d ) + ( a d + b c ) i + < x ^ { 2 } + 1 > = ( a + b i ) ( c + d i ) + < x ^ { 2 } + 1 > = ( ( a + b i ) + < x ^ { 2 } + 1 > )$ $) ( ( c + d i ) + < x ^ { 2 } + 1 >$ . Hence, φ is a ring homomorphism.

# 15: Consider the mapping from $M _ { 2 } ( \mathbb { Z } )$ into Z given by ${ \left[ \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right] } \mapsto a$ . Prove or disprove that this is a ring homomorphism.

The map is not a ring homomorphism. While addition is preserved, multiplication is not. To see this observe: $\phi ( { \left[ \begin{array} { l l } { a } & { { \dot { b } } } \\ { c } & { d } \end{array} \right] } { \left[ \begin{array} { l l } { f } & { g } \\ { h } & { i } \end{array} \right] } = \phi ( { \left[ \begin{array} { l l } { a f + b { \dot { h } } } & { * } \\ { * } & { * } \end{array} \right] } ) = a f + b h \neq a f =$ $\phi ( { \left[ \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right] } ) \phi ( { \left[ \begin{array} { l l } { f } & { g } \\ { h } & { i } \end{array} \right] } )$

# 16: Let $R \ = \ \{ { [ \begin{array} { l l } { a } & { b } \\ { 0 } & { c } \end{array} ] } | a , b , c \in \mathbb { Z } \}$ Prove or disprove that the mapping ${ \left[ \begin{array} { l l } { a } & { b } \\ { 0 } & { c } \end{array} \right] } \mapsto a$ is a ring homomorphism.

This map is a ring homomorphism. Addition is preserved because $\phi ( { \left[ \begin{array} { l l } { a } & { b } \\ { 0 } & { c } \end{array} \right] } + { \left[ \begin{array} { l l } { d } & { f } \\ { 0 } & { g } \end{array} \right] } ) =$ $\phi ( { \left[ \begin{array} { l l } { a + d } & { b + f } \\ { 0 } & { c + g } \end{array} \right] } ) = a + d = \phi ( { \left[ \begin{array} { l l } { a } & { b } \\ { 0 } & { c } \end{array} \right] } ) + \phi ( { \left[ \begin{array} { l l } { d } & { f } \\ { 0 } & { g } \end{array} \right] } )$ . Farther, the multiplication is preserved since $\phi ( { \left[ \begin{array} { l l } { a } & { b } \\ { 0 } & { d } \end{array} \right] } { \left[ \begin{array} { l l } { f } & { g } \\ { 0 } & { i } \end{array} \right] } ^ { - } = \phi ( { \left[ \begin{array} { l l } { a f } & { * } \\ { * } & { * } \end{array} \right] } ) = a { \bar { f } } = \phi ( { \left[ \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right] } ) \phi ( { \left[ \begin{array} { l l } { f } & { g } \\ { h } & { i } \end{array} \right] } )$

$\# 1 7 { : }$ : Is the mapping from $\mathbb { Z } _ { 5 }$ to $\mathbb { Z } _ { 3 0 }$ given by $x \mapsto 6 x$ a ring homomorphism? Note that the image of the unity is the unity of the image but not the unity of $\mathbb { Z } _ { 3 0 }$ •

The mapping is a ring homomorphism. Addition is straightforward to show since $\phi ( x + y ) =$ $6 ( x + y ) = 6 x + 6 y = \phi ( x ) + \phi ( y )$ . For multiplication, $\phi ( x y ) = 6 x y$ and $\phi ( x ) \phi ( y ) = 6 x 6 y =$ 36xy = 6xy. Thus multiplication is preserved.

# 20: Recall that a ring element a is called an idempotent if $a ^ { 2 } = a$ . Prove that a ring homomorphism carries an idempotent to an idempotent.

Let a be an idempotent of a ring R. Then $\phi ( a ) = \phi ( a ^ { 2 } ) = ( \phi ( a ) ) ^ { 2 }$ . Hence, $\phi ( a )$ is an idempotent.

# 21: Determine all ring homomorphisms from $\mathbb { Z } _ { 6 }$ to $\mathbb { Z } _ { 6 }$ . Determine all ring homomorphisms from $\mathbb { Z } _ { 2 0 }$ to $\mathbb { Z } _ { 3 0 }$ •

Part 1: We know that a ring homomorphism must be a group homomorphism as well. Hence we know that the image of 1 has order 1, 2, 3 or 6. For the image to have order $1 , \ 1 \ \mapsto \ 0$ and this map clearly preserves multiplication. For the order to be $2 , \ 1 \ \mapsto \ 3$ Now $\phi ( x y ) = 3 x y$ and $\phi ( x ) \phi ( y ) = 9 x y = 3 x y$ so this is indeed a ring homomorphism as well. In the order three case, 1 maps to either 2 or 4. We observe that in the first instance $\phi ( x y ) = 2 x y \ne 4 x y = \phi ( x ) \phi ( y )$ so this is not a homomorphism. However, in the second instance $\phi ( x y ) = 4 x y$ and $\phi ( x ) \phi ( y ) = 1 6 x y = 4 x y$ so it is a ring homomorphism. Finally, for the image to have order 5, the element 1 maps to either 1 or 5. If it maps to 1, then this is the identity map and is clearly a ring homomorphism. However, if it maps to 5, $\phi ( x y ) = 5 x y$ but $\phi ( x ) \phi ( y ) = 2 5 x y = x y$ so it is not a ring homomorphism. Hence the ring homomorphisms are those determined by 1 7→ 0, 1 7→ 3, 1 7→ 4 and 1 7→ 1.

Part 2: We can use a similar logic for this part. Doing this shows that the homomorphisms are those defined by 1 maps to 0, 6, 15 or 21.

# 30: Prove that the sum of the squares of three consecutive integers can not be a square.

Let n be an integer. Then the sum of the squares of three consecutive integers can be represented as $n ^ { 2 } + { \overline { { ( n + 1 ) ^ { 2 } + ( n + 2 ) ^ { 2 } } } }$ . Now consider this expression modulus 3. Then it is $n ^ { 2 } + n ^ { 2 } + 2 n + 1 + n ^ { 2 } + 4 n + 4 = 3 n ^ { 2 } + 6 n + 5 = 2$ . For this expression to be a square then there must exist an element, x, in $\mathbb { Z } _ { 3 }$ such that $x ^ { 2 } = 2$ . But $0 ^ { 2 } = 0 , 1 ^ { 2 } = 1$ and $2 ^ { 2 } = 1$ so there is no such solution.

# 37: Show that no integer of the form 111, 111, 111, . . . , 111 is prime.

Consider $\phi _ { 3 }$ as defined in class. Then $\phi _ { 3 } ( 1 1 1 , 1 1 1 , 1 1 1 , \ldots , 1 1 1 ) = \phi _ { 3 } ( 1 \cdot 1 0 ^ { k } + 1 \cdot 1 0 ^ { k - 1 } +$ $\ldots + 1 \cdot 1 0 + 1 ) = \sum _ { i = 0 } ^ { k } \phi _ { 3 } ( 1 ) \phi _ { 3 } ( 1 0 ) ^ { i } = \sum _ { i = 0 } ^ { k } 1 \cdot \cdot \cdot 1 = 1 + 1 + 1 \cdot \cdot \cdot + 1$ but the 1’s come in threes so this expression is 0 in $\mathbb { Z } _ { 3 }$ . Hence 3 divides the integer so it can not be prime.

# 39: Suppose n is a positive integer written in the form $n = a _ { k } 3 ^ { k } + a _ { k - 1 } 3 ^ { k - 1 } +$ $\cdots + a _ { 1 } 3 + a _ { 0 }$ , where each of the $a _ { i } { \bf \dot { s } }$ is 0, 1, or 2. Show that n is even if and only if $a _ { k } + a _ { k - 1 } + \cdot \cdot \cdot + a _ { 1 } + a _ { 0 }$ is even.

Consider $\phi _ { 2 }$ as defined in class. Then $\phi _ { 2 } ( n ) = \phi _ { 2 } ( a _ { k } 3 ^ { k } + a _ { k - 1 } 3 ^ { k - 1 } + \cdot \cdot \cdot + a _ { 1 } 3 + a _ { 0 } ) =$ $\sum _ { i = 1 } ^ { k } \phi _ { 2 } ( a _ { i } ) \phi _ { 2 } ( 3 ) ^ { i } = \sum _ { i = 1 } ^ { k } \phi _ { 2 } ( a _ { i } ) \cdot 1 = \phi _ { 2 } ( a _ { 0 } + a _ { 1 } + a _ { 2 } + . . . + a _ { k } )$ . Hence, n is even iff the sum of its coefficients is even.

# 45: Is there a ring homomorphism from the reals to some ring whose kernel is the integers?

No. The kernel of a ring homomorphism is an ideal but the integers are not an ideal of the real numbers. For instance, $\pi \cdot 1 = \pi \notin \mathbb { Z }$

# 50: Show that if m and n are distinct positive integers, then mZ is not ringisomorphic to $n \mathbb { Z } .$

Let m and n be distinct positive integers. Because a ring isomorphism must take generators to generators, m would have to map to ±n. Consider the case of $m \mapsto n$ Then $\phi ( n n ) = \phi ( n + n + n + \cdot \cdot \cdot + n )$ with n copies of n. This is equal to $\phi ( n ) + \phi ( n ) + \cdot \cdot \cdot + \phi ( n ) =$ $m { + } m { + } \cdot \cdot { + } m = n m$ . But $\phi ( n n ) = \phi ( n ) \phi ( n ) = m m$ . Since n and m are distinct, nm $\neq$ mm so there can not be any such isomorphism.

# 66: Let $R = \left\{ { \left[ \begin{array} { l l } { a } & { b } \\ { b } & { a } \end{array} \right] } | a , b \in \mathbb { Z } \right\}$ , and let $\phi$ be the mapping that takes $\left[ \begin{array} { l l } { a } & { b } \\ { b } & { a } \end{array} \right]$ to $a - b .$

a. Show that φ is a homomorphism.

Addition is preserved since $\phi ( { \left[ \begin{array} { l l } { a } & { b } \\ { b } & { a } \end{array} \right] } + { \left[ \begin{array} { l l } { c } & { d } \\ { d } & { c } \end{array} \right] } ) = \phi ( { \left[ \begin{array} { l l } { a + c } & { b + d } \\ { b + d } & { a + c } \end{array} \right] } ) = ( a +$ $c ) - ( b + d ) = ( a - b ) + ( c - d ) = \phi ( { \left[ \begin{array} { l l } { a } & { b } \\ { b } & { a } \end{array} \right] } ) + \phi ( { \left[ \begin{array} { l l } { c } & { d } \\ { d } & { c } \end{array} \right] } )$ . We can also see that multiplication is preserved since $\phi ( { \left[ \begin{array} { l l } { { \bar { a } } } & { b } \\ { b } & { a } \end{array} \right] } { \left[ \begin{array} { l l } { c } & { d } \\ { d } & { c } \end{array} \right] } ^ { - } ) = \phi ( { \left[ \begin{array} { l l } { a c + b d } & { a d + b c } \\ { b c + a d } & { b d + a c } \end{array} \right] } ) ) =$ $( a c + b d ) - ( a d + b c ) = a ( c - d ) + \tilde { b ( } d - c ) \tilde { \bar { = } } \tilde { a } ( c - \bar { d } ) - b ( \tilde { c ( } - d ) = ( a - b ) ( c - d ) = 0 ,$ $\phi ( { \left[ \begin{array} { l l } { a } & { b } \\ { b } & { a } \end{array} \right] } ) \phi ( { \left[ \begin{array} { l l } { c } & { d } \\ { d } & { c } \end{array} \right] } )$

## b. Determine the kernel of $\phi .$

The kernel is the set of matrixes such that $a - b = 0$ 0, or $a = b$ . Hence it is the set of matrices of the form $\left[ \begin{array} { l l } { a } & { a } \\ { a } & { a } \end{array} \right]$ where $a \in \mathbb { Z }$

c. Show that $R / K e r \ \phi$ is isomorphic to Z.

The image of $\phi$ defined as above is Z. We know this since $\phi ( R ) \subseteq \mathbb { Z }$ , and the matrix with $a = a$ and $b = 0$ maps to a for any $a \in \mathbb { Z }$ •

## d. Is Ker φ a prime ideal?

Since Z is an integral domain, the kernel is a prime ideal.

e. Is Ker φ a maximal ideal?

Since Z is not a field, the kernel is not maximal.