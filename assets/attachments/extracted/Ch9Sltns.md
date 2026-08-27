# 6: Let $H = \left\{ \left[ \begin{array} { l l } { a } & { b } \\ { 0 } & { d } \end{array} \right] \left| a , b , d \in \mathbb { R } , a d \neq 0 \right. \right\}$ . Is $H$ a normal subgroup of $G L ( 2 , \mathbb { R } ) ?$

No; Show directly by counter example or by multiplying the general case, $\left[ \begin{array} { l l } { f } & { g } \\ { h } & { j } \end{array} \right] \left[ \begin{array} { l l } { a } & { b } \\ { 0 } & { d } \end{array} \right] \left( \left[ \begin{array} { l l } { f } & { g } \\ { h } & { j } \end{array} \right] \right) ^ { - 1 }$ , to see it is not contained in $H$ .

# 8: Viewing $< 3 >$ and $< 1 2 >$ as subgroups of $\mathbb { Z }$ , prove that $< 3 > / < 1 2 >$ is isomorphic to $\mathbb { Z } _ { 4 }$ . Similarly, prove that $< 8 > / < 4 8 >$ is isomorphic to $\mathbb { Z } _ { 6 }$ . Generalize to arbitrary integers $k$ and $n$ .

First, notice $< 3 > = \{ \ldots , - 1 2 , - 9 , - 6 , - 3 , 0 , 3 , 6 , 9 , 1 2 , \ldots \}$ and $< 1 2 > = \{ \ldots , - 2 4 , - 1 2 , 0 , 1 2 , 2 4 , \ldots \}$ . Now $< 3 > / < 1 2 >$ looks like $\{ - 9 + < 1 2 > , - 6 + < 1 2 > , - 3 + < 1 2 > , < 1 2 > , 3 + < 1 2 > , 6 + < 1 2 > , 9 + < 1 2 > \}$ since multiples of 12 will be absorbed by $< 1 2 >$ . Recall $a H = b H$ if and only if $b ^ { - 1 } a \in H$ . Here this tells me that because $- ( 3 ) + - 9 = - 1 2 , 3 + < 1 2 > = - 9 + < 1 2 >$ . Similarly, $- 3 + < 1 2 > = 9 + < 1 2 >$ and $- 6 + < 1 2 > = 6 + < 1 2 >$ . So, $< 3 > / < 1 2 > = \{ < 1 2 > , 3 + < 1 2 > , 6 + < 1 2 > , 9 + < 1 2 > \}$ . Notice that $3 + < 1 2 >$ has order 4 and hence generates all of $< 3 > / < 1 2 >$ . Thus, $< 3 > / < 1 2 >$ is cyclic of order 4, and hence isomorphic to $\mathbb { Z } _ { 4 }$ .

Now, consider $< 8 > / < 4 8 >$ . Similar to before, it is clear that this group consists of $\left\{ < 4 8 > , 8 + < 4 8 > , 1 6 + < 4 8 > , 2 4 + < 4 8 > , 3 2 + < 4 8 > , 4 0 + < 4 8 > \right\}$ . Notice that still similar to before $8 + < 4 8 >$ is a generator of the quotient group and that the group has order 48 divided by 8, or 6. Hence, it is isomorphic to $\mathbb { Z } _ { 6 }$ .

In general, suppose $k$ divides $n$ . Then $< k > / < n >$ is of the form $\{ < n > , k + < n > , 2 k + < n > , \ldots , ( n - k ) + < n > \}$ . This is clearly cyclic with generator $k + < n >$ and has order $\frac { n } { k }$ . Hence $< k > / < n >$ is isomorphic to $\mathbb { Z } _ { \frac { n } { k } }$ .

# 11: Let $G = \mathbb { Z } _ { 4 } \oplus U ( 4 )$ , $H = < ( 2 , 3 ) >$ , and $K = < ( 2 , 1 ) >$ . Show that $G / H$ is not isomorphic to $G / K$ . (This shows that $H \approx K$ does not imply that $G / H \approx G / K$ .)

For clarity, we write out each of the groups: $G = \left\{ ( 0 , 1 ) , ( 1 , 1 ) , ( 2 , 1 ) , ( 3 , 1 ) , ( 0 , 3 ) , ( 1 , 3 ) , ( 2 , 3 ) , ( 3 , 3 ) \right\}$ , $H = \{ ( 2 , 3 ) , ( 0 , 1 ) \}$ , and $K = \{ ( 2 , 1 ) , ( 0 , 1 ) \}$ . Since $H$ and $K$ both have order 2, they are both isomorphic to $\mathbb { Z } _ { 2 }$ . Straightforward calculation shows,

$$
G / H = \{ H = ( 0 , 1 ) H = ( 2 , 3 ) H , ( 1 , 1 ) H = ( 3 , 3 ) H , ( 2 , 1 ) H = ( 0 , 3 ) H , ( 3 , 1 ) H = ( 1 , 3 ) H \}
$$

and

$$
G / K = \{ K = ( 0 , 1 ) K = ( 2 , 1 ) K , ( 1 , 1 ) K = ( 3 , 1 ) K , ( 0 , 3 ) K = ( 2 , 3 ) K , ( 3 , 3 ) K = ( 1 , 3 ) K \}
$$

Notice that each has 4 elements as expected since $4 \cdot 2 = 8$ .

Consider $( 1 , 3 ) H \colon < ( 1 , 3 ) H > = \{ ( 1 , 3 ) H , ( 2 , 1 ) H , ( 3 , 3 ) H , ( 0 , 1 ) H \} = G / H$ . So, $G / H$ is cyclic of order 4, and hence is isomorphic to $\mathbb { Z } _ { 4 }$ .

However, observe that $G / K$ is not cyclic since $< ( 0 , 1 ) K > = \{ K \} , < ( 1 , 1 ) K > = \{ ( 1 , 1 ) K , ( 2 , 1 ) K \} , < ( 0 , 3 ) K > = \{ ( 0 , 3 ) K , ( 0 , 1 ) K \}$ and $< ( 3 , 3 ) K > = \{ ( 3 , 3 ) K , ( 2 , 1 ) K \}$ . In fact, we recognize that this structure is the Klein-4 group, $\mathbb { Z } _ { 2 } \oplus \mathbb { Z } _ { 2 }$ . Hence $G / H \not \approx G / K$ .

## 13: Prove that a factor group of an Abelian group is Abelian.

Let $G$ be an Abelian group and consider its factor group $G / H$ , where $H$ is normal in $G$ . Let $a H$ and $b H$ be arbitrary elements of the quotient group. Then $a H b H = ( a b ) H = ( b a ) H = b H a H$ because $G$ is Abelian. Hence the factor group is also Abelian.

## 14: What is the order of the element $1 4 + < 8 >$ in the factor group $\mathbb { Z } _ { 2 4 } / < 8 > ?$

For completeness, observe $< 8 > = \{ 8 , 1 6 , 0 \}$ and $\mathbb { Z } _ { 2 4 } / < 8 > = \{ < 8 > , 1 + < 8 > , 2 + < 8 > , 3 + < 8 > , 4 + < 8 > , 5 + < 8 > , 6 + < 8 > , 7 + < 8 > \}$ . Now let’s observe $1 4 + < 8 > :$
$( 1 4 + < 8 > ) + ( 1 4 + < 8 > ) = 2 8 + < 8 > = 4 + < 8 > , ( 1 4 + < 8 > ) + ( 4 + < 8 > ) = 1 8 + < 8 > = 2 + < 8 > , ( 1 4 + < 8 > ) + ( 2 + < 8 > ) = 1 6 + < 8 > = < 8 >$ .
Hence the order of $1 4 + < 8 >$ is 4.

## 16: Recall that $Z ( D _ { 6 } ) = \{ e , r ^ { 3 } \}$ . What is the order of the element $r Z ( D _ { 6 } )$ in the factor group $D _ { 6 } / Z ( D _ { 6 } ) ?$

Notice that problem 16 here is rewritten in terms of generators and relations. Now it is clear that the order of $r Z ( D _ { 6 } )$ is 3 since $r ^ { 3 } \in Z ( D _ { 6 } )$ .

## 17: Let $G = \mathbb { Z } / < 2 0 >$ and $H = < 4 > / < 2 0 >$ . List the elements of $H$ and $G / H$ .

Observe: $< 4 > = \{ \dots , - 8 , - 4 , 0 , 4 , 8 , 1 2 , \dots \}$ and $< 2 0 > = \{ \ldots , - 2 0 , 0 , 2 0 , 4 0 , 6 0 , \ldots \}$ Hence $H = \{ < 2 0 > , 4 + < 2 0 > , 8 + < 2 0 > , 1 2 + < 2 0 > , 1 6 + < 2 0 > \} \approx \mathbb { Z } _ { 5 } .$

Now notice that $G = \{ < 2 0 > , 1 + < 2 0 > , 2 + < 2 0 > , \ldots , 1 9 + < 2 0 > \} \approx \mathbb { Z } _ { 2 0 }$ . So $G / H = \{ 0 + < 2 0 > + H , 1 + < 2 0 > + H , 2 + < 2 0 > + H , 3 + < 2 0 > + H \} \approx \mathbb { Z } _ { 4 } .$

## 19: What is the order of the factor group $( \mathbb { Z } _ { 1 0 } \oplus U ( 1 0 ) ) / < ( 2 , 9 ) > ?$

The order of the factor group is $$\frac { | \mathbb { Z } _ { 1 0 } \oplus U ( 1 0 ) | } { | < ( 2 , 9 ) > | } = \frac { 1 0 \times 4 } { \operatorname { l c m } ( | 2 | , | 9 | ) } = \frac { 4 0 } { \operatorname { l c m } ( 5 , 2 ) } = \frac { 4 0 } { 1 0 } = 4 .$$

## 21: Prove that an Abelian group of order 33 is cyclic.

Let $G$ be an Abelian group of order 33. By Theorem 9.5, there exists an element of $G$ , say $a$ , such that $| a | = 3$ and an element of $G$ , say $b$ , such that $| b | = 1 1$ . Since $G$ is Abelian, $( a b ) ^ { 3 3 } = a ^ { 3 3 } b ^ { 3 3 } = e$ . So the order of $a b$ divides 33. However, it is clear $| a b |$ is not 1, 3, or 11. Hence $| a b | = 3 3$ so $a b \in G$ generates $G$ , and $G$ is cyclic.

## 23: Determine the order of $( \mathbb { Z } \oplus \mathbb { Z } ) / < ( 4 , 2 ) >$ . Is the group cyclic?

Notice that $( 1 , 1 ) + < ( 4 , 2 ) >$ has infinite order [Why? Suppose it is of finite order, say $n$ . Then $( n , n ) \in < ( 4 , 2 ) >$ means $( n , n ) = k ( 4 , 2 )$ for some $k$ . So $n = 4 k = 2 k$ , which means $n = 0$ since $n$ is an integer.]. Hence the group $( \mathbb { Z } \oplus \mathbb { Z } ) / < ( 4 , 2 ) >$ also has infinite order.

If the quotient group is cyclic, it must be isomorphic to $\mathbb { Z }$ (from previous work), so every non-identity element should have infinite order. However, $( 6 , 3 ) + < ( 4 , 2 ) >$ has order 2. Hence, it is not cyclic.

# 24: The group $\left( \mathbb { Z } _ { 4 } \oplus \mathbb { Z } _ { 1 2 } \right) / < ( 2 , 2 ) >$ is isomorphic to one of $\mathbb { Z } _ { 8 } , \ \mathbb { Z } _ { 4 } \oplus \mathbb { Z } _ { 2 }$ , or $\mathbb { Z } _ { 2 } \oplus \mathbb { Z } _ { 2 } \oplus \mathbb { Z } _ { 2 }$ . Determine which one by elimination.

Observe that $H = < ( 2 , 2 ) > = \{ ( 2 , 2 ) , ( 0 , 4 ) , ( 2 , 6 ) , ( 0 , 8 ) , ( 2 , 1 0 ) , ( 0 , 0 ) \}$ (which has order 6 as expected). Let $G = ( \mathbb { Z } _ { 4 } \oplus \mathbb { Z } _ { 1 2 } ) / < ( 2 , 2 ) >$ . Then $G = \left\{ H , ( 1 , 0 ) H , ( 0 , 1 ) H , ( 1 , 1 ) H , ( 0 , 2 ) H , ( 0 , 3 ) H , ( 3 , 0 ) H , ( 1 , 3 ) H \right\}$ and these cosets have orders $1 , 4 , 4 , 2 , 2 , 4 , 4$ , and 2 respectively. Hence, $G$ is not cyclic and not isomorphic to $\mathbb { Z } _ { 8 }$ . Further, since there is an element of order 4, $G$ is not isomorphic to $\mathbb { Z } _ { 2 } \oplus \mathbb { Z } _ { 2 } \oplus \mathbb { Z } _ { 2 }$ . Hence, $G \approx \mathbb { Z } _ { 4 } \oplus \mathbb { Z } _ { 2 }$ .

# 25: Let $G = U ( 3 2 )$ and $H = \{ 1 , 3 1 \}$ . The group $G / H$ is isomorphic to one of $\mathbb { Z } _ { 8 } , \mathbb { Z } _ { 4 } \oplus \mathbb { Z } _ { 2 }$ , or $\mathbb { Z } _ { 2 } \oplus \mathbb { Z } _ { 2 } \oplus \mathbb { Z } _ { 2 }$ . Determine which one by elimination.

First, we know that $| U ( 3 2 ) | = 2 ^ { 5 } - 2 ^ { 4 } = 1 6$ , so $G / H$ has order $\frac { 1 6 } { 2 } = 8$ as anticipated.

Consider $3 H = \{ 3 , 2 9 \} \in G / H \colon < 3 H > = \{ 3 H , 9 H , 2 7 H , 1 7 H , 1 9 H , 2 5 H , 1 1 H , H \}$ so the order of $3 H$ is 8. Hence $G / H = < 3 H > \approx \mathbb { Z } _ { 8 }$ .

# 27: Let $G = U ( 1 6 )$ , $H = \{ 1 , 1 5 \}$ and $K = \{ 1 , 9 \}$ . Are $H$ and $K$ isomorphic? Are $G / H$ and $G / K$ isomorphic?

It is obvious that $H \approx K \approx \mathbb { Z } _ { 2 }$ . Now, we need to check if $G / H$ and $G / K$ are isomorphic. We know that each has order 4 and that there are only two such groups. Consider $3 H$ : $< 3 H > = \{ 3 H , 9 H , 1 1 H , H \}$ so $3 H$ generates $G / H$ and $G / H \approx \mathbb { Z } _ { 4 }$ . Now observe $G / K$ : $< K > = \{ K \} , < 3 K > = \{ 3 K , K \} , < 5 K > = \{ 5 K , K \}$ and $< 7 K > = \{ 7 K , K \}$ . Thus $G / K \approx \mathbb { Z } _ { 2 } \oplus \mathbb { Z } _ { 2 }$ . Hence $G / K \not \approx G / H$ .

# 37: Let $G$ be a finite group and let $H$ be a normal subgroup of $G$ . Prove that the order of the element $g H$ in $G / H$ must divide the order of $g$ in $G$ .

Let $| g | = n$ . Then $( g H ) ^ { n } = g ^ { n } H = e H = H$ , so $| g H |$ must divide $n$ .

# 38: Let $H$ be a normal subgroup of $G$ and let $a$ belong to $G$ . If the element $a H$ has order 3 in the group $G / H$ and $| H | = 1 0$ , what are the possibilities for the order of $a ?$

First, $| G | = | a H | \times | H | = 3 \times 1 0 = 3 0$ . So $| a |$ divides 30. But we also know, by the previous problem, that 3 also has to divide $| a |$ . Hence the possible orders for $a$ are 3, 6, 15, and 30.

# 40: Let $\phi$ be an isomorphism from a group $G$ onto a group $\bar { G }$ . Prove that if $H$ is a normal subgroup of $G$ , then $\phi ( H )$ is a normal subgroup of $\bar { G }$ .

Let $H$ be normal in $G$ . We want to show $y \phi ( H ) y ^ { - 1 } \subseteq \phi ( H )$ for all $y \in { \bar { G } } = \phi ( G )$ . Since $y \in \phi ( G )$ , there exists an $x \in G$ such that $y = \phi ( x )$ . Thus $y \phi ( H ) y ^ { - 1 } = \phi ( x ) \phi ( H ) ( \phi ( x ) ) ^ { - 1 } = \phi ( x H x ^ { - 1 } ) = \phi ( H )$ since $H$ is normal in $G$ , and we are done.

# 42: An element is called a square if it can be expressed in the form $b ^ { 2 }$ for some $b$ . Suppose that $G$ is an Abelian group and $H$ is a subgroup of $G$ . If every element of $H$ is a square and every element of $G / H$ is a square, prove that every element of $G$ is a square. Does your proof remain valid when “square” is replaced by “nth power” where $n$ is any integer?

Let $G$ be an Abelian group, $H$ be a subgroup of $G$ and every element of both $H$ and $G / H$ be a square. Suppose $g \in G$ . Since $g \in G , g H \in G / H$ . But all elements of $G / H$ are squares so there exists an $a H \in G / H$ such that $g H = ( a H ) ^ { 2 } = a ^ { 2 } H$ . By properties of cosets, we now have that $( a ^ { 2 } ) ^ { - 1 } g \in H$ . But every element in $H$ is a square so there exists a $b \in H$ such that $( a ^ { 2 } ) ^ { - 1 } g = b ^ { 2 }$ . Solving for $g$ we see $g = a ^ { 2 } b ^ { 2 } = ( a b ) ^ { 2 }$ since $G$ is Abelian. But this means that $g$ is a square. Hence every element of $G$ is a square.

Notice that this did not depend on a property of 2, so the proof remains valid when 2 is replaced by $n \in \mathbb { Z }$ .

# 46: Show that $D _ { 1 3 }$ is isomorphic to $\operatorname { I n n } ( D _ { 1 3 } )$ .

First, recall that $Z ( D _ { 1 3 } ) = \{ e \}$ . Now, we know that $\operatorname { I n n } ( D _ { 1 3 } ) \approx D _ { 1 3 } / Z ( D _ { 1 3 } ) = D _ { 1 3 }$ .

# 49: Suppose that $G$ is a non-Abelian group of order $p ^ { 3 }$ where $p$ is prime and $Z ( G ) \neq \{ e \}$ . Prove that $| Z ( G ) | = p$ .

First recall that $Z ( G )$ is normal in $G$ . Since $G$ is non-Abelian, $Z ( G )$ does not have order $p ^ { 3 }$ . Further, since $Z ( G )$ is a non-trivial subgroup, its order is not 1 and divides $p ^ { 3 }$ , so it has order $p$ , or $p ^ { 2 }$ .

Suppose that the order of $Z ( G )$ is $p ^ { 2 }$ . Then $| G / Z ( G ) | = p$ and hence the quotient group $G / Z ( G )$ is cyclic. But this implies, by Theorem 9.3, that $G$ is Abelian, which is a contradiction. Hence $| Z ( G ) | = p$ .

# 50: If $| G | = p q$ where $p$ and $q$ are primes that are not necessarily distinct, prove that $| Z ( G ) | = 1$ or $p q$ .

Let $| G | = p q$ , as above. Since $Z ( G )$ is a normal subgroup of $G , | Z ( G ) | = 1 , p , q ,$ or $p q$ . If $G$ is Abelian, $| Z ( G ) | = p q$ .

Assume $G$ is not Abelian. Without loss of generality, let $| Z ( G ) | = p$ . Then $| G / Z ( G ) | = q$ which is prime. Hence $| G / Z ( G ) |$ is cyclic and $G$ is Abelian. But this is a contradiction. Hence $| Z ( G ) | = 1$ .

## 51: Let $N$ be a normal subgroup of $G$ and let $H$ be a subgroup of $G$ . If $N$ is a subgroup of $H$ , prove that $H / N$ is a normal subgroup of $G / N$ if and only if $H$ is a normal subgroup of $G$ .

Let $N$ be a normal subgroup of $G$ and let $H$ be any subgroup of $G$ . Assume $N \subseteq H$ .

$( \Rightarrow )$ Let $H / N$ be normal in $G / N$ . Then for all $g N \in G / N$ and $h N \in H / N , ( g N ) ( h N ) ( g N ) ^ { - 1 } = ( g h g ^ { - 1 } ) N \in H / N$ . Thus $g h g ^ { - 1 } N = h ^ { \prime } N$ for some $h ^ { \prime } \in H$ . Hence $g h g ^ { - 1 } = h ^ { \prime } n$ for some $n \in N$ . But $h ^ { \prime } \in H$ and $n \in H$ so $h ^ { \prime } n \in H$ . Hence $g H g ^ { - 1 } \subset H$ . Thus $H$ is normal in $G$ .

$( \Leftarrow )$ The argument above reverses.

## 56: Show that the intersection of two normal subgroups of $G$ is a normal subgroup of $G$ . Generalize.

Let $H$ and $K$ be normal subgroups of $G$ . Let $x \in H \cap K$ and $g \in G$ . Since $x \in H , g x g ^ { - 1 }$ is in $H$ . Similarly, $g x g ^ { - 1 }$ is in $K$ . Thus $g x g ^ { - 1 }$ is in $H \cap K$ for all $g \in G$ and $x \in H \cap K$ . Thus, $H \cap K$ is normal in $G$ . Note that in a previous chapter we showed that $H \cap K$ is a subgroup of $G$ , which completes the proof.

## 61: Let $H$ be a normal subgroup of a finite group $G$ and let $x \in G$ . If $\operatorname { g c d } ( | x | , | G / H | ) = 1$ , show that $x \in H$ .

Let $\operatorname { g c d } ( | x | , | G / H | ) = 1$ as above. From an earlier problem we know that $| x H |$ must divide $| x |$ , so $\operatorname { g c d } ( | x H | , | G / H | )$ must also be 1. But we also know that $| x H |$ must divide $| G / H |$ because $x H$ is an element of this group. Hence $| x H | = 1$ , so $x H = H$ , which implies $x \in H$ .

# 63: If $N$ is a normal subgroup of $G$ and $| G / N | = m$ , show that $x ^ { m } \in N$ for all $x \in G$ .

Let $x \in G$ and $| G / N | = m$ . Then $x ^ { m } N = ( x N ) ^ { m } = ( x N ) ^ { | G / N | } = N$ , so $x ^ { m } \in N$ .

## 68: Recall that a subgroup $N$ of a group $G$ is called characteristic if $\phi ( N ) = N$ for all automorphisms $\phi$ of $G$ . If $N$ is a characteristic subgroup of $G$ , show that $N$ is a normal subgroup of $G$ .

Let $N$ be a characteristic subgroup of $G$ . Then $\phi ( N ) = N$ for all automorphisms of $G$ . In particular, $\phi _ { g } ( N ) = N$ when $\phi _ { g }$ is the conjugation map by $g$ . Thus $g N g ^ { - 1 } = N$ for all $g \in G$ . So $N$ is normal in $G$ .

# Team Problem Solutions for Ch 9

# 10: Let $H = \{ ( 1 ) , ( 1 2 ) ( 3 4 ) \}$ in $A _ { 4 }$ .

## a. Show that $H$ is not normal in $A _ { 4 }$ .

We know that $( 1 2 3 ) H = \{ ( 1 2 3 ) , ( 1 3 4 ) \}$ and $H ( 1 2 3 ) = \{ ( 1 2 3 ) , ( 3 2 4 ) \}$ . These are not equal so $H$ is not normal in $A _ { 4 }$ .

b. Referring to the multiplication table for $A _ { 4 }$ in Table 5.1 on page 111, show that, although $\alpha _ { 6 } H = \alpha _ { 7 } H$ and $\alpha _ { 9 } H = \alpha _ { 1 1 } H$ , it is not true that $\alpha _ { 6 } \alpha _ { 9 } H = \alpha _ { 7 } \alpha _ { 1 1 } H$ . Explain why this proves that the left cosets of $H$ do not form a group under coset multiplication.

$$
\alpha _ { 6 } \alpha _ { 9 } H = ( 2 4 3 ) ( 1 3 2 ) H = ( 1 2 ) ( 3 4 ) H = H \qquad \text { and } \qquad \alpha _ { 7 } \alpha _ { 1 1 } H = ( 1 4 2 ) ( 2 3 4 ) H = ( 1 4 ) ( 2 3 ) H \neq H .
$$

This shows that multiplication is not well defined for these cosets and hence the left cosets of $H$ do not form a group under coset multiplication. This does not surprise us since we know that normality was required for well-defined coset multiplication.

## 47: Suppose that $N$ is a normal subgroup of a finite group $G$ and $H$ is a subgroup of $G$ . If $| G / N |$ is prime, prove that $H$ is contained in $N$ or that $N H = G$ .

Let $N$ be a normal subgroup of a finite group $G$ , and $H$ be any subgroup of $G$ . Let $| G / N | = p ,$ a prime. Now we know that $N \subseteq N H \subseteq G$ . Therefore, $p = | G : N | = | G : N H | \times | N H : N |$ . Thus $| G : N H |$ is $p$ or 1. If $| G : N H | = 1$ , then $G = N H$ . If $| G : N H | = p$ , then $| N H : N | = 1$ so $N H = N$ , which means that $H \subseteq N$ .

# 65: If $G$ is non-Abelian, show that $\operatorname { A u t } ( G )$ is not cyclic.

Proof. Suppose not. Let $\operatorname { A u t } ( G )$ be cyclic. Then $\operatorname { I n n } ( G )$ is cyclic since $\operatorname { I n n } ( G )$ is a subgroup of $\operatorname { A u t } ( G )$ and subgroups of cyclic groups are cyclic. We know that $\operatorname { I n n } ( G ) \approx G / Z ( G )$ so $G / Z ( G )$ must be cyclic. But this implies that $G$ is Abelian, which is a contradiction. Thus $\operatorname { A u t } ( G )$ is not cyclic. □