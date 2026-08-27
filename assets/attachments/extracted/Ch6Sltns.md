## Solution Outlines for Chapter 6

## # 1: Find an isomorphism from the group of integers under addition to the group of even integers under addition.

Let $\phi : \mathbb { Z } \to 2 \mathbb { Z }$ be defined by $x \mapsto x + x = 2 x$ . Then $\phi ( x + y ) = 2 ( x + y ) = 2 x + 2 y =$ $\phi ( { \boldsymbol { x } } ) + \phi ( { \boldsymbol { y } } )$ , so φ is a homomorphism. Now, $\phi ( x ) = \phi ( y )$ if and only if $2 x = 2 y$ , which holds if and only if $x = y$ . Thus φ is one-to-one. Finally, let $y \in 2  { \mathbb { Z } }$ . Then $y = 2 k$ for some $k \in \mathbb { Z }$ Since $k \in \mathbb { Z }$ and $\phi ( k ) = 2 k = y , \phi$ is onto.

# 3: Let $\mathbb { R } ^ { + }$ be the group of positive real numbers under multiplication. Show√ that the mapping $\phi ( x ) = \sqrt { x }$ is an automorphism of $\mathbb { R } ^ { + }$ •

Let $\phi : \mathbb { R } ^ { + }  \mathbb { R } ^ { + }$ be defined by $\phi ( x ) ~ = ~ \sqrt { x }$ Since $\sqrt { x }$ will be in the positive reals, and the positive reals is an appropriate domain for $\phi , \phi$ is an automorphism. Now, $\phi ( x y ) ~ = ~ \sqrt { x y } ~ = ~ \sqrt { x } \sqrt { y } ~ = ~ \phi ( x ) \phi ( y )$ , so φ is a homomorphism. Notice that Ker $\phi \ : =$ $\{ x | \sqrt { x } = \mathrm { i } \} = \{ 1 \}$ , so φ is one to one. Finally, let $y \in \mathbb { R } ^ { + }$ . Then $y ^ { 2 } = x$ is also in $\mathbb { R } ^ { + }$ Moreover, $\phi ( x ) = \phi ( y ^ { 2 } ) = \sqrt { y ^ { 2 } } = y$ , so φ is onto.

# 4: Show that U(8) is not isomorphic to $U ( 1 0 )$

Observe that U (10) is cyclic while U (8) is not.

# 5: Show that U(8) is isomorphic to $U ( 1 0 )$

First notice that $U ( 8 ) = \{ 1 , 3 , 5 , 7 \} , U ( 1 2 ) = \{ 1 , 5 , 7 , 1 1 \}$ and all elements of both $U ( 8 )$ and U(12) square to the identity. Let φ be defined by $\phi ( 1 ) = 1 , \phi ( 3 ) = 5 , \phi ( 5 ) = 7 .$ 7, and $\phi ( 7 ) = 1 1$ You can check the multiplications of $\phi ( 1 a ) , \phi ( 3 \cdot 5 ) , \phi ( 3 \cdot 7 )$ and $\phi ( 5 \cdot 7 )$ in order to see that φ indeed is a homomorphism. It is clear by construction that φ is onto and one to one.

# 6: Prove that isomorphism is an equivalence relation.

Proof. To show that isomorphism is an equivalence relation, I must show reflexive, symmetric and transitive. First, notice that $G \approx G$ by the identity map. Thus the isomorphism relation is reflexive. Suppose that $G \approx H$ . Then there exists an isomorphism $\phi : G  H$ . But this implies that $\phi ^ { - 1 } : H \to G$ is also an isomorphism. Thus $H \approx G$ and the relation is symmetric. Finally, supposes that $G \approx H$ and $H \approx K$ . Then there exist two isomorphisms: $\phi : G \to H$ and $\sigma : H  K$ . Then $\sigma \phi : G  k$ is also an isomorphism (you have previously shown that the composition of bijections is a bijection; you should argue that the composition is still a homomorphism if you have not done so yet). Thus, the relation is transitive. □

# 10: Let G be a group. Prove that the mapping $\alpha ( g ) = g ^ { - 1 }$ for all g in G is an automorphism if and only if G is Abelian.

Define α as above. Suppose that α is an automorphism. Then $\alpha ( a b ) = \alpha ( a ) \alpha ( b )$ for all $a , b \in G$ . This implies that $( a b ) ^ { - 1 } = a ^ { - 1 } b ^ { - 1 }$ . But this means that $b ^ { - 1 } a ^ { - 1 } = a ^ { - 1 } b ^ { - 1 }$ and multiplying we see that $a b = b a$ Now suppose instead that G is Abelian. Then reversing the previous argument shows that α must be a homomorphism. The kernel of α is $\{ g | g ^ { - 1 } = e \} = \{ e \}$ so α is one-to-one. Finally, let $a \in G$ . Then $a ^ { - 1 }$ is also in G since G is a group. Moreover, $\alpha ( a ^ { - 1 } ) = ( a ^ { - 1 } ) ^ { - 1 } = a$ so α is onto. (Note: You should recognize most of this problem from an earlier chapter).

# 11: If g and h are elements from a group, prove that $\phi _ { g } \phi _ { h } = \phi _ { g h }$

Proof. Let $x \in G$ . Then $( \phi _ { g } \phi _ { h } ) ( x ) = \phi _ { g } ( \phi _ { h } ( x ) ) = \phi _ { g } ( h x h ^ { - 1 } ) = g h x h ^ { - 1 } g ^ { - 1 } = ( g h ) x ( g h ) ^ { - 1 } =$ $\phi _ { g h } ( x )$ . Thus, $\phi _ { g } \phi _ { h } = \phi _ { g h }$

# 12: Find two groups G and H such that $G \not \approx H$ , but $\operatorname { A u t } ( G ) \approx \operatorname { A u t } ( H )$

Consider $G = \mathbb { Z } _ { 6 }$ and $H = \mathbb { Z } _ { 3 }$ . Since $| \mathbb { Z } _ { 6 } | \neq | \mathbb { Z } _ { 3 } | , G \neq H$ . But

$\mathrm { A u t ( \mathbb { Z } _ { 6 } ) } \approx U ( 6 ) = \{ 1 , 5 \} = < 5 > \approx \mathbb { Z } _ { 2 }$ and $\mathrm { A u t ( \mathbb { Z } _ { 3 } ) } \approx U ( 3 ) = \{ 1 , 2 \} = < 2 > \approx \mathbb { Z } _ { 2 }$ . Thus $\operatorname { A u t } ( G ) \approx \operatorname { A u t } ( H )$

# 14: Find $\operatorname { A u t } ( \mathbb { Z } _ { 6 } )$

As above, $\mathrm { A u t ( \mathbb { Z } _ { 6 } ) } \approx U ( 6 ) = < 5 > \approx \mathbb { Z } _ { 2 }$ . Thus there are only two elements in $\operatorname { A u t } ( \mathbb { Z } _ { 6 } )$ Clearly one is the identity map. Also, since the inverse map is an automorphism, this must be the second map. Thus ${ \cal A } u t ( \mathbb { Z } _ { 6 } ) \approx \{ i d , \phi \}$ where $\phi ( g ) = - g$

Alternately: The generators of $\mathbb { Z } _ { 6 }$ are 1 and 5. Thus $\mathrm { A u t } ( \mathbb { Z } _ { 6 } ) = \{ \phi _ { 1 } , \phi _ { 5 } \}$ where $\phi _ { i }$ is defined as the map that sends 1 to i. Since $\phi _ { 1 } ( 1 ) = 1 , \phi _ { 1 }$ is just the identity. Similarly, we can see that $\phi _ { 5 } ( 1 ) = 5$ implies that 2 maps to 4 and 3 maps to 3. Thus $\phi _ { 5 }$ is the inverse map that sends g to −g.

## # 15: If G is a group, prove that Aut(G) and Inn(G) are groups.

Proof. Clearly both Aut(G) and Inn(G) are associative because function composition is associative. Now consider $\phi _ { 1 } , \phi _ { 2 } \in \mathrm { A u t } ( G )$ Since the composition of an isomorphism is an isomorphism (if you don’t remember this, prove it to yourself), $\phi _ { 1 } \phi _ { 2 } \in \operatorname { A u t } ( G )$ , giving closure. Let $\phi _ { e }$ be the automorphism defined by $\phi _ { e } ( x ) = x$ . Then $\phi _ { 1 } \phi _ { e } ( x ) = \phi _ { 1 } ( x ) = \phi _ { e } \phi _ { 1 } ( x )$ so this is the identity map. Finally, by Theorem 6.1, property 1, we know that the inverse of an isomorphism is also an isomorphism, thus Aut(G) contains inverses. This completes the proof that Aut(G) is a group.

Now, let $\phi _ { g } , \phi _ { h } \in$ Inn(G). By homework problem 11, we know that $\phi _ { g } \phi _ { h } \in \operatorname { I n n } ( G )$ so it is closed. Using the same calculation (in problem 11), $\phi _ { g } \phi _ { e } = \phi _ { g e } = \phi _ { g } = \phi _ { e g } = \phi _ { e } \phi _ { g } ,$ , so the group identity is indeed $\phi _ { e }$ , which is in Inn(G). Similarly, we see $\phi _ { g } \phi _ { g ^ { - 1 } } = \phi _ { g g ^ { - 1 } } = \phi _ { e } =$ $\phi _ { g ^ { - 1 } g } = \phi _ { g ^ { - 1 } } \phi _ { g }$ and inverses exist in Inn(G). Thus Inn(G) is also a group.

## # 20: Show that Z has infinitely many subgroups isomorphic to Z.

Consider aZ where $a \in \mathbb { Z }$ . If $a \ = \ \pm 1 , \ a \mathbb { Z } \ = \ \mathbb { Z } .$ , and if $a ~ = ~ 0 , ~ a \mathbb { Z } ~ = ~ \{ 0 \}$ For all other a, aZ is a proper, non-trivial subgroup of Z (as shown previously). Consider $\phi : a \mathbb { Z } \to \mathbb { Z }$ defined by $a z \mapsto z$ (Note: φ clearly maps to $\mathbb { Z }$ by construction). Then $\phi ( a z _ { 1 } + a z _ { 2 } ) = \phi ( a ( z _ { 1 } + z _ { 2 } ) ) = z _ { 1 } + z _ { 2 } = \phi ( a z _ { 1 } ) + \phi ( a z _ { 2 } )$ , so $\phi$ is a homomorphism. Now, $\phi ( a z _ { 1 } ) = \phi ( a z _ { 2 } )$ implies that $z _ { 1 } = z _ { 2 }$ . But, since $a = a$ , this means $a z _ { 1 } = a z _ { 2 }$ thus $\phi$ is one to one. Finally, for any $z \in \mathbb { Z } , a z \in a Z$ thus our map is onto. Since there are an infinite number of $a \neq - 1 , 0 , 1$ , there are an infinite number of subgroups isomorphic to $\mathbb { Z } .$

$\#$ 35: Show that the mapping $\phi ( a + b i ) = a - b i$ is an automorphism of the group of complex numbers under addition. Show that $\phi$ preserves complex multiplication as well.

First, we show $\phi$ is a homomorphism: $\phi ( ( a + b i ) + ( c + d i ) ) = \phi ( ( a + c ) + ( b + d ) i ) = ( a +$ $c ) - ( b + d ) i = ( a - b i ) + ( c - d i ) = \phi ( a + b i ) + \phi ( c + d i )$ . Now suppose that $\phi ( a + b i ) = \phi ( c + d i )$ Then $a - b i = c - d i$ . But this implies that $a = c$ and $b = d .$ Hence, $a + b i = c + d i$ , and φ is 1-1. Finally, let $a + b i$ be any element of C. Then $a - b i$ is also in C and $\phi ( a - b i ) = a - ( - b ) i = a + b i$ Thus $\phi$ is onto.

We see that φ also preserves multiplication since $\phi ( ( a + b i ) ( c + d i ) ) = \phi ( ( a c - b d ) + ( a d +$ $b c ) i ) = ( a c - b d ) - ( a d + b c ) i$ , which is the same as $\phi ( a + b i ) \phi ( c + d i ) = ( a - b i ) ( c - d i ) =$ $( a c - b d ) - ( b c + a d )$

# 36: Let $G = \{ a + b { \sqrt { 2 } } | a ,$ b are rational} and $H = \left\{ \left\lceil { \begin{array} { c c } { a } & { 2 b } \\ { b } & { a } \end{array} } \right\rceil | a , \right.$ b are $\mathbf { r a t i o n a l } \Biggr \}$ Show that G and H are isomorphic under addition. Prove that G and H are closed under multiplication. Does your isomorphism preserve multiplication as well as addition?

To show G is isomorphic to H under addition, define $\phi : G \to H$ by the map $a + b { \sqrt { 2 } } \mapsto$ a 2 b b a Then $\phi ( a + b { \sqrt { 2 } } + c + d { \sqrt { 2 } } ) = \phi ( ( a + c ) + ( b + d ) { \sqrt { 2 } } ) = { \left[ \begin{array} { l l } { a + c } & { 2 b + 2 d } \\ { b + d } & { a + c } \end{array} \right] } = c + d { \sqrt { 2 } } .$ ${ \left[ \begin{array} { l l } { a } & { 2 b } \\ { b } & { a } \end{array} \right] } + { \left[ \begin{array} { l l } { c } & { 2 d } \\ { d } & { c } \end{array} \right] } = \phi ( a + b { \sqrt { 2 } } ) + \phi ( c + d { \sqrt { 2 } } )$ . It is clear that $\phi$ is onto since $\left[ \begin{array} { l l } { a } & { \hat { 2 } b } \\ { b } & { a } \end{array} \right]$ is mapped to by $a + b { \sqrt { 2 } }$ and in both cases $a , b \in \mathbb { Q }$ . Finally we see that $\phi$ is onto since $K e r \ \phi = \{ a + b { \sqrt { 2 } } { | \begin{array} { l l } { a } & { 2 b } \\ { b } & { a } \end{array} | } = { [ \begin{array} { l l } { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} ] } \} = \{ a + b { \sqrt { 2 } } { | { a = 0 = b } \} } = \{ 0 \}$

Because $( a + b { \sqrt { 2 } } ) ( c + d { \sqrt { 2 } } ) = ( a c + 2 b d ) + ( b c + a d ) { \sqrt { 2 } }$ and the rationals are closed under multiplication, G is closed under multiplication. We similarly see that H is closed under multiplication: $\left[ \begin{array} { c c } { { a } } & { { 2 b } } \\ { { b } } & { { a } } \end{array} \right] \left[ \begin{array} { c c } { { c } } & { { 2 d } } \\ { { d } } & { { c } } \end{array} \right] = \left[ \begin{array} { c c } { { \dot { a } c + 2 b d } } & { { 2 a d + 2 b d } } \\ { { b c + a d } } & { { 2 b d + a c } } \end{array} \right] ^ { \circ } = \left[ \begin{array} { c c } { { ( a c + 2 b d ) } } & { { 2 ( a d + b c ) } } \\ { { ( a d + b c ) } } & { { ( a c + 2 b d ) } } \end{array} \right] ^ { \circ }$

Finally, we also see that $\phi$ preserves multiplication since $\phi ( ( a + b { \sqrt { 2 } } ) ( c + d { \sqrt { 2 } } ) ) \ =$ $\phi ( ( a c + 2 b d ) + ( b c + a d ) { \sqrt { 2 } } ) = { \left[ \begin{array} { l l } { a c + 2 b d } & { 2 ( b c + a d ) } \\ { b c + a d } & { a c + 2 b d } \end{array} \right] } = { \left[ \begin{array} { l l } { a } & { 2 b } \\ { b } & { a } \end{array} \right] } { \left[ \begin{array} { l l } { c } & { 2 d } \\ { d } & { c } \end{array} \right] } = \phi ( a + 2 b ) .$ $b { \sqrt { 2 } } ) \phi ( c + d { \sqrt { 2 } } )$

# 37: Prove that Z under addition is not isomorphic to Q under addition.

The proof is simply that Z is cyclic while Q is not cyclic. We have already shown $\mathbb { Z } = < 1 >$ but, for completeness, we should argue that Q is not cyclic. Assume that it is cyclic. Then $\mathbb { Q } = < \mathbf { \Delta } _ { q } ^ { p } >$ for some reduced rational (note: $p , q \in \mathbb { Z } )$ But ${ \frac { p } { 2 q } } \neq ( { \frac { p } { q } } ) ^ { i }$ for any i [there is one case $q \stackrel { \cdot } { = } 2$ that has to be considered separate, but clearly $\mathbb { Q }$ is not generated by $\frac { p } { 2 }$ since you can’t get a third]. But this means that ${ \frac { p } { 2 q } } \not \in \mathbb { Q }$ , which is a contradiction.

# 40: Let ${ \mathbb R } ^ { n } = \{ ( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } ) | a _ { i } \in { \mathbb R } \}$ . Show that the mapping $\phi : ( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } ) $ $( - a _ { 1 } , - a _ { 2 } , . . . , - a _ { n } )$ is an automorphism of the group $\mathbb { R } ^ { n }$ under component wise addition. This automorphism is called inversion. Describe the action of $\phi$ geometrically.

Clearly, $( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } ) \in \mathbb { R } ^ { n }$ implies that $( - a _ { 1 } , - a _ { 2 } , . . . , - a _ { n } )$ is also in $\mathbb { R } ^ { n }$ , thus $\phi : \mathbb { R } ^ { n } $ $\mathbb { R } ^ { n } \cdot \mathrm { \mathrm { ~ N o w } } , \ \phi ( ( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } ) + ( b _ { 1 } , b _ { 2 } , \ldots , b _ { n } ) ) = \phi ( ( a _ { 1 } + b _ { 1 } , a _ { 2 } + b _ { 2 } , \ldots , a _ { n } + b _ { n } ) ) = ( - ( a _ { 1 } + b _ { 2 } , \ldots , a _ { n } ) + \ldots , \ a _ { n } )$ $b _ { 1 } ) , - ( a _ { 2 } + b _ { 2 } ) , \ldots , - ( a _ { n } + b _ { n } ) ) = ( - a _ { 1 } - b _ { 1 } , - a _ { 2 } - b _ { 2 } , \ldots , - a _ { n } - b _ { n } ) = ( - a _ { 1 } , - a _ { 2 } , \ldots , - a _ { n } ) + \ldots$ $( - b _ { 1 } , - b _ { 2 } , \ldots , - b _ { n } ) = \phi ( ( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } ) ) + \phi ( ( b _ { 1 } , b _ { 2 } , \ldots , b _ { n } ) )$ . thus φ is a homomorphism. The ker $\phi = \{ ( a _ { 1 } , a _ { 2 } , \dots , a _ { n } ) | ( - a _ { 1 } , - a _ { 2 } , \dots , - a _ { n } ) = ( 0 , 0 , \dots , 0 ) \} = \{ ( a _ { 1 } , a _ { 2 } , \dots , a _ { n } ) | - a _ { i } = 0 \}$ $0 \forall i \} = \{ ( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } ) { \big | } a _ { i } = 0 \forall i \} = \{ ( 0 , 0 , \ldots , 0 ) \}$ . Thus, φ is one-to-one. Finally, we need to show φ is onto. Let $( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } ) \in \mathbb { R } ^ { n }$ . Then $( - a _ { 1 } , - a _ { 2 } , \ldots , - a _ { n } )$ is also in R and $\phi ( ( - a _ { 1 } , - a _ { 2 } , \ldots , - a _ { n } ) ) = ( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } )$

Geometrically, this is a reflection through the origin.

# 42: Suppose that G is a finite Abelian group and G has no element of order 2. Show that the mapping $g  g ^ { 2 }$ is an automorphism of G. Show, by example, that there is an infinite Abelian group for which the mapping $g  g ^ { 2 }$ is one-to-one and operation-preserving but not an automorphism.

Since G is closed under the operation, $g ^ { 2 } \in G$ for all $g \in G$ . Thus $\phi ,$ defined as above, maps G to G. Now, for $g , h \in G , \phi ( g h ) = ( g h ) ^ { 2 } = g ^ { 2 } h ^ { 2 } = \phi ( g ) \phi ( h )$ so φ is a homomorphism. [Recall, $( g h ) ^ { 2 } = g ^ { 2 } h ^ { 2 }$ because G is Abelian.] Let $\phi ( g ) = \phi ( h )$ . Then $g ^ { 2 } = h ^ { 2 }$ , which implies $g ^ { 2 } h ^ { - 2 } = ( g h ^ { - } 1 ) ^ { 2 } = e \qquad $ . Since G has no elements of order two, this means that $g h ^ { - 1 } = e$ so $g = h$ and $\phi$ is one-to-one. [Alternatively, ker $\phi = \{ g | g ^ { 2 } = e \} = \{ g | g = e \} = \{ e \}$ since there are no elements of order 2.] Since G is finite and $\phi$ is one-to-one, we know $\phi$ is onto. Thus $\phi$ is an automorphism.

Let $G = \mathbb { Z } _ { \geq 0 }$ . Then $\phi$ is still 1-1 and a homomorphism. However, $\phi$ is not onto. For example, nothing maps to 3. Thus φ is not an automorphism.

# 43: Let G be a group and let $g \in G . { \textbf { I f } } z \in Z ( G )$ , show that the inner automorphism induced by g is the same as the inner automorphism induced by $z g$

Let $g \in G$ and $z \in Z ( G )$ . Then $\phi _ { z g } ( x ) = ( z g ) x ( z g ) ^ { - 1 } = z g x g ^ { - 1 } z ^ { - 1 } = z z ^ { - 1 } g x g ^ { - 1 }$ . This last step is true because z is in the center, and the center is a group so $z ^ { - 1 }$ is also in the center. Now $z z ^ { - 1 } g x g ^ { - 1 } = g x g ^ { - 1 } = \phi _ { g } ( x )$

$\#$ 45: Suppose that g and h induce the same inner automorphism of a group G.   
Prove that $h ^ { - 1 } g \in Z ( G )$ .

Proof. Suppose that g and h induce the same inner automorphism of a group G. Then for all $x \in G , \phi _ { g } ( x ) = \phi _ { h } ( x )$ Hence, gxg $^ { - 1 } = h x h ^ { - 1 }$ . Multiplying on the right of each side of the equation by g, we have $g x = h x h ^ { - 1 } g$ . Now we multiply each side on the left by $h ^ { - 1 }$ . this gives $h ^ { - 1 } g x = x h ^ { - 1 } g$ . Thus $h ^ { - 1 } g$ commutes with x for all $x \in G$ so $h ^ { - 1 } g \in Z ( G )$ □

$\#$ 48: Let $\phi$ be an isomorphism from a group G to a group $\overline { G }$ and let a belong to G. Prove that $\phi ( C ( a ) ) = C ( \phi ( a ) )$

We know that $a b =$ ba if and only if $\phi ( a ) \phi ( b ) = \phi ( b ) \phi ( a )$ . Let $g \in C ( a )$ Then $g a = a g$ which implies $\phi ( g ) \phi ( a ) = \phi ( a ) \phi ( g )$ . Hence, $\phi ( g ) \in C ( \phi ( a ) )$ , illustrating the first containment. Now let $h \in C ( \phi ( a ) )$ Then $h \phi ( a ) = \phi ( a ) h$ But φ is onto so there exists a $g \in G$ such that $h = \phi ( g )$ . Further, $g a = a g$ because h and $\phi ( a )$ commute. Thus $h \in \phi ( C ( a ) )$ Since both containments hold, $\phi ( C ( a ) ) = C ( \phi ( a ) )$ .

# 52: Given a group G, define a new group $G ^ { * }$ that has the same elements as G with the operation ∗ defined by $a * b =$ ba for all a and b in $G ^ { * }$ . Prove that the mapping from $G$ to G $G ^ { * }$ defined by $\phi ( x ) = x ^ { - 1 }$ for all x in G is an isomorphism from G onto $G ^ { * }$ .

Since $G ^ { * }$ contains the same elements of $G ,$ and G is closed under inverses, $\phi$ maps from $G$ to $G ^ { * }$ . Now for $g , h \in G , \phi ( g h ) = ( g h ) ^ { - 1 } = h ^ { - 1 } g ^ { - 1 } = \phi ( h ) \phi ( g ) = \phi ( g ) * \phi ( h )$ . Thus φ is a homomorphism. The kernel of $\phi$ is $\{ g \in G | \phi ( g ) = g ^ { - 1 } = e \} = \{ g \in G | g ^ { - 1 } g = e g \} =$ $\{ g \in G | e = g \} = \{ e \}$ . Hence, $\phi$ is also one to one. [Note: If G is finite, we are done since this implies φ is onto.] Now let $h \in G ^ { * }$ . Then $h ^ { - } 1 \in G ^ { * }$ , and hence in G. Farther, $\phi ( h ^ { - 1 } ) = ( h ^ { - 1 } ) ^ { - 1 } = h$ . Thus, $\phi$ is onto, which completes the proof that $\phi$ is an isomorphism.