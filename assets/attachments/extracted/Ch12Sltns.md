## Solution Outlines for Chapter 12

## 3: Give an example of a subset of a ring that is a subgroup under addition but not a subring.

In $\mathbb { C }$ , $\{ b i | b \in \mathbb { Z } \}$ is a subgroup but not a subring since $i ^ { 2 } = - 1 \notin \{ b i \}$ . Similarly, in $\mathbb { R }$ , $\{ n { \sqrt { 2 } } | n \in \mathbb { Z } \}$ is a subgroup but not a subring.

## 4: Show, by example, that for any fixed nonzero elements a and b in a ring, the equation $a x = b$ can have more than one solution. How does this compare with groups?

Consider the ring $\mathbb { Z } _ { 4 }$ , and let $a = b = 2$ . Then $2 ( 1 ) = 2$ and $2 ( 3 ) = 2$ , so $2 x = 2$ has two solutions. This is in contrast to groups where there is only one solution, $x = a ^ { - 1 } b$ .

# 6: Find an integer n that shows that the rings $\mathbb { Z } _ { n }$ need not have the following properties that the ring of integers has. Then answer: Is the n you found prime?

1. $a ^ { 2 } = a$ implies a = 0 or a = 1. Let n = 6. Then $3 ^ { 2 } = 3$ but 3 is neither 0 nor 1.

2. $a b = 0$ implies a = 0 or b = 0. Let n = 6. Then $2 \cdot 3 = 0$ but $2 \neq 0$ and $3 \neq 0$ .

3. $a b = a c$ and $a \neq 0$ implies b = c. Let n = 6. $3 \cdot 2 = 0 = 3 \cdot 4$ but $3 \neq 0$ and $2 \neq 4 .$

# 9: Prove that the intersection of any collection of subrings of a ring R is a subring of R.

Let G be the intersection of any collection of subrings. Notice that the intersection must include 0 so it is a non-empty set. Let a and b be elements of G. Then a and b are in each ring. Thus $a - b$ and ab are in each ring. But since these are in every ring, $a - b$ and ab are also in the intersection. Hence it is a subring.

## 12: Let $a , b ,$ and c be elements of a commutative ring, and suppose that a is a unit. Prove that b divides c if and only if ab divides c.

Let $a , b ,$ and c be elements of a commutative ring where a is a unit. Suppose that b divides c. Then $c = b d$ for some d in the ring. Then $c = a b ( a ^ { - 1 } d )$ where $a ^ { - 1 } d$ is in the ring. Hence ab divides c. Suppose instead that ab divides c. Then $a b d = c$ for some d in the ring. So $b ( a d ) = c$ so b divides c.

## 17: Show that a ring that is cyclic under addition is commutative.

Suppose that R is a ring that is cyclic under addition. Call its additive generator a. Then any element in R is of the form na for some $n \in \mathbb { Z }$ . Further, $( n a ) ( m a ) = ( n m ) a ^ { 2 } = ( m a ) ( n a )$ by exercise 15. Hence R is commutative.

# 19: Let R be a ring. The center of R is the set $\{ x \in R \mid a x = x a \text { for all } a \in R \}$ . Prove that the center of a ring is a subring.

Clearly 0 is in the center since $0 x = 0 = x 0$ for all $x \in R$ . Hence the center is non-empty. Now, let a and b be elements of the center of R. Then $( a - b ) x = a x - b x = x a - x b = x ( a - b )$ so $a - b$ is in the center. Similarly, $( a b ) x = a ( b x ) = a ( x b ) = ( a x ) b = ( x a ) b = x ( a b )$ so ab is in the center. Hence, the center of a ring is a subring.

# 20: Describe the elements of $M _ { 2 } ( \mathbb { Z } )$ that have multiplicative inverses.

Let $A = { \left[ \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right] }$ be an element of $M _ { 2 } ( \mathbb { Z } )$ . Then A has a multiplicative inverse if and only if it has non-zero determinant so $a d - b c \neq 0$ . Moreover, the inverse is only in $M _ { 2 } ( \mathbb { Z } )$ if $\frac { 1 } { \operatorname { d e t } ( A ) } \in \mathbb { Z }$ (in order to ensure that the matrix entries are all integers). Thus the determinant of A must be $\pm 1$ . Thus the elements with multiplicative inverse are $\left\{ { \left[ \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right] } \ | a d - b c = \pm 1 \right\}$

# 27: Show that a unit of a ring divides every element of the ring.

Let a be a unit in a ring R. Let x be any element in R. Then $x = a a ^ { - 1 } x = a ( a ^ { - 1 } x )$ , and $a ^ { - 1 } x$ is also in R. Hence a divides x.

# 31: Give an example of ring elements a and b with the properties that $a b = 0$ but $b a \neq 0$ .

Let $R = M _ { 2 } ( \mathbb { Z } )$ . Then ${ \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 0 } \end{array} \right] } = 0$ but ${ \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} \right] } = { \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} \right] } .$

# 33: Suppose that R is a ring such that $x ^ { 3 } = x $ for all x in R. Prove that $6 x = 0$ for all x in R.

Let R be a ring such that $x ^ { 3 } = x $ for all $x \in R$ . Then, for any $x , ( 2 x ) ^ { 3 } = 2 x$ and $8 x ^ { 3 } = 8 x$ . Hence $2 x = 8 x$ , so $6 x = 0$ .

# 38: Is $\mathbb { Z } _ { 6 }$ a subring of $\mathbb { Z } _ { 1 2 } ?$

No: The operations in $\mathbb { Z } _ { 6 }$ are different than the ones in $\mathbb { Z } _ { 1 2 }$

# 42: Let $R = \left\{ \begin{array} { c c } { a } & { a } \\ { b } & { b } \end{array} \right| a , b \in \mathbb { Z } \right\}$ . Prove or disprove that R is a subring of $M _ { 2 } ( \mathbb { Z } )$ Note that it is clear that $R \subseteq M _ { 2 } ( \mathbb { Z } )$ and since R contains the zero matrix (among many others), R is non-empty. Let $A = { \left[ \begin{array} { l l } { a } & { a } \\ { b } & { b } \end{array} \right] }$ and $C = { \left[ \begin{array} { l l } { c } & { c } \\ { d } & { d } \end{array} \right] }$ be matrices in R. Then $A - C = { \left[ \begin{array} { l l } { a - c } & { a - c } \\ { b - d } & { b - d } \end{array} \right] }$ , which is in R since the integers are closed under subtraction. Additionally, $A C = { \left[ \begin{array} { l l } { a c + a d } & { a c + a d } \\ { b c + b d } & { b c + b d } \end{array} \right] }$ . Since ac + ad and bc + bd are in Z, $A C \in R$ . Since R is closed under subtraction and multiplication, R is a subring.

# 43: Let $R = \mathbb { Z } \oplus \mathbb { Z } \oplus \mathbb { Z }$ and $S = \{ ( a , b , c ) \in R | a + b = c \}$ . Prove or disprove that S is a subring of R.

First, it is clear that S is contained in R and that S is not empty (S contains $( 0 , 0 , 0 )$ ). Let $x = ( a , b , c )$ and $\boldsymbol { y } = ( d , f , g )$ be elements of S. Then $x - y = ( a , b , c ) - ( d , f , g ) =$ $( a - d , b - f , c - g )$ . Since $x , y \in S , a + b = c$ and $d + f = g$ . Now, $( a - d ) + ( b - f ) =$ $( a + b ) - ( d + f ) = c - g$ so $x - y \in S$ . Now, consider the condition for $x y = ( a d , b f , c g )$ We have that $c g = ( a + b ) ( d + f ) = a d + b f + a f + b d$ so $x y$ is in S only if $a f + b d = 0$ . But this equality is not always true. For example, let $x = ( 1 , 2 , 3 )$ and $y = ( 4 , 5 , 9 )$ . Then $x y = ( 4 , 1 0 , 2 7 )$ but $4 + 1 0 \neq 2 7$ . Hence we can not say that $x y \in S$ . Thus, S is not a subring of R.

## 45: Let R be a ring with unity 1. Show that $S = \{ n \cdot 1 | n \in \mathbb { Z } \}$ is a subring of R.

We know that S is non-empty since $1 \cdot 1 = 1$ is in S. Now, let $a , b \in S$ . Then $a = x \cdot 1$ and $b = y \cdot 1$ for some $x , y \in \mathbb { Z }$ . So $a - b = x \cdot 1 - y \cdot 1 = ( x - y ) \cdot 1$ so $x - y \in S$ . Additionally, $a b = ( x \cdot 1 ) ( y \cdot 1 ) = ( x y ) \cdot 1$ so $a b \in S$ .

## 46: Show that $2 \mathbb { Z } \cup 3 \mathbb { Z }$ is not a subring of Z.

Notice that 2 and 3 are both in $2 \mathbb { Z } \cup 3 \mathbb { Z }$ but $2 + 3 = 5 \not \in 2 \mathbb { Z } \cup 3 \mathbb { Z }$

## 50: Suppose that R is a ring and that $a ^ { 2 } = a$ for all a in R. Show that R is commutative. (Note: Such a ring is called a Boolean ring.)

Let R be a ring such that $a ^ { 2 } = a$ for all $a \in R$ . We notice that $a + b = ( a + b ) ^ { 2 } = a ^ { 2 } + b ^ { 2 } +$ $a b + b a = a + b + a b + b a$ . Thus $a b + b a = 0$ , or $a b = - b a$ . Now $- b a = ( - b a ) ^ { 2 } = ( b a ) ^ { 2 } = b a$ . Therefore $a b = b a$ , and R is commutative.