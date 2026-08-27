# Solution Outlines for Chapter 20

# 1: Describe the elements of $\mathbb { Q } ( { \sqrt [ 3 ] { 5 } } )$ .

$$
\mathbb { Q } ( 5 ^ { \frac { 1 } { 3 } } ) = \{ a + b 5 ^ { \frac { 1 } { 3 } } + c 5 ^ { \frac { 2 } { 3 } } | a , b , c \in \mathbb { Q } \}
$$

# 3: Find the splitting field of $x ^ { 3 } - 1$ over Q. Express your answer in the form Q(a).

First, notice that $x ^ { 3 } - 1 = ( x - 1 ) ( x ^ { 2 } + x + 1 )$ (see cyclotomic polynomials from class). So the roots of $x ^ { 3 } - 1$ are 1 and $( - 1 \pm { \sqrt { - 3 } } ) / 2$ . Notice that 1 is already in Q. By arguments like those in class, we see that we get $- ( 1 \pm { \sqrt { - 3 } } ) / 2$ by simply adjoining $\sqrt { - 3 }$ . So $\mathbb { Q } ( { \sqrt { - 3 } } )$ is the splitting field.

# 6: Let $a , b \in \mathbb { R }$ with $b \neq 0$ . Show that $\mathbb { R } ( a + b i ) = \mathbb { C }$ .

It is clear that $\mathbb { R } ( a + b i ) \subseteq \mathbb { C }$ . Now to see that $\mathbb { C } \subseteq \mathbb { R } ( a + b i )$ , I only need to show that $i \in \mathbb { R } ( a + b i )$ (note: it is clear that R is there so getting i gives us all of C). We see that $i = b ^ { - 1 } ( a + b i ) - b ^ { - 1 } a$ which is a real number times $( a + b i )$ plus a real number and so it is an element of $\mathbb { R } ( a + b i )$ . Thus we have equality.

# 7: Find a polynomial $p ( x )$ in $\mathbb { Q } [ x ]$ such that $\mathbb { Q } ( { \sqrt { 1 + { \sqrt { 5 } } } } )$ is ring isomorphic to $\mathbb { Q } [ x ] / < p ( x ) >$ .

I need a polynomial so that it has rational coefficients, it is irreducible over Q and has root $\sqrt { 1 + { \sqrt { 5 } } }$ . (Technically, we are using Theorem 20.3 that we haven’t done yet). So I want $f ( x )$ such that $f ( x ) = 0$ gives $x = { \sqrt { 1 + { \sqrt { 5 } } } }$ . This implies that $x ^ { 2 } = 1 + { \sqrt { 5 } }$ , or $x ^ { 2 } - 1 = { \sqrt { 5 } }$ . So $x ^ { 4 } - 2 x ^ { 2 } + 1 = 5$ or $x ^ { 4 } - 2 x ^ { 2 } - 4 = 0$ . Let $p ( x ) = x ^ { 4 } - 2 x ^ { 2 } - 4$ . Then $p ( x )$ is in $\mathbb { Q } [ x ]$ and has the needed root. Additionally, it is irreducible over Q (simply check in $\mathbb { Z } _ { 3 }$ ).

# 20: Let F be a field, and let a and b belong to F with $a \neq 0$ . If c belongs to some extension of F , prove that $F ( c ) = F ( a c + b )$ . (F “absorbs” its own elements.)

This is akin to exercise 6. First, it is clear that $a c + b \in F ( c )$ so $F ( a c + b ) \subseteq F ( c )$ . Now, $c = a ^ { - 1 } ( a c + b ) - a ^ { - 1 } b$ so $F ( c ) \subseteq F ( a c + b )$ and we are done.

# 21: Let $f ( x ) \in F [ x ]$ and let $a \in F$ . Show that $f ( x )$ and $f ( x + a )$ have the same splitting field over F .

Suppose that the zeros of $f ( x )$ are $a _ { 1 } , a _ { 2 } , \ldots , a _ { k }$ . Then the roots of $f ( x + a )$ are $a _ { 1 } - a , \ldots , a _ { k } - a$ . So by application of exercise 20 (up to k times), the splitting field $F ( a _ { 1 } , a _ { 2 } , \ldots , a _ { k } ) =$ $F ( a _ { 1 } - a , \ldots , a _ { k } - a )$ and the splitting fields are the same.

# 23: Determine all of the subfields of $\mathbb { Q } ( { \sqrt { 2 } } )$ .

First notice that $\mathbb { Q }$ and $\mathbb { Q } ( { \sqrt { 2 } } )$ are subfields. Now suppose we have another subfield, K. K must contain Q and some element $a + b { \sqrt { 2 } }$ where $b \neq 0$ . Now, K must contain $\mathbb { Q } ( a + b { \sqrt { 2 } } )$ , but by exercise 20 this is just $\mathbb { Q } ( { \sqrt { 2 } } )$ . So those are the only two subfields.

# 27: Prove or disprove that $\mathbb { Q } ( { \sqrt { 3 } } )$ and $\mathbb { Q } ( { \sqrt { - 3 } } )$ are ring isomorphic.

Suppose that there is some map $\phi$ that is a ring isomorphism from $\mathbb { Q } ( { \sqrt { - 3 } } )$ to $\mathbb { Q } ( { \sqrt { 3 } } )$ . Then $\phi ( 1 ) = 1$ so $\phi ( - 3 ) = - 3$ (as we’ve seen before). So $-3 = \phi ( - 3 ) = \phi ( \sqrt { - 3 } \sqrt { - 3 } ) = ( \phi ( { \sqrt { - 3 } } ) ) ^ { 2 }$ . But this is a contradiction since $\phi ( { \sqrt { - 3 } } )$ is a real number. Hence, no such isomorphism exists.

# 38: Show that $\mathbb { Q } ( { \sqrt { 7 } } , i )$ is the splitting field for $x ^ { 4 } - 6 x ^ { 2 } - 7$ (over Q).

First we need to factor $x ^ { 4 } - 6 x ^ { 2 } - 7$ . We see that it factors to $( x ^ { 2 } - 7 ) ( x ^ { 2 } + 1 )$ . Hence the roots are $\pm \sqrt { 7 }$ and $\pm i$ . Notice that adjoining $\sqrt { 7 }$ gives us $- { \sqrt { 7 } }$ for free. Similarly, adjoining $i$ also gives us $-i$ . So the splitting field is $\mathbb { Q } ( { \sqrt { 7 } } , i )$ .