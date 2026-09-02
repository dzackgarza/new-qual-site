## Homework 7

D. Zack Garza

November 6, 2019

## Contents

1 Problem 1 1\
1.1 Part 1 1\
1.2 Part 2 2\
2 Problem 2 3\
2.1 Part 1 3\
2.2 Part 2 3\
3 Problem 3 3\
3.1 Part 1 3\
3.2 Part 2 4\
3.3 Part 3 5\
4 Problem 4 6\
5 Problem 5 7\
5.1 Part (a) 7\
5.2 Part (b) 8\
5.3 Part (c) 8\
5.4 Part (d) 9\
6 Problem 6 9\
7 Problem 7 10

## 1 Problem 1

## 1.1 Part 1

In order for IS to be a submodule of A, we need to show the following implication:

$$
x \in I S , \ a \in A \ \Longrightarrow \ x a , a x \in I S .
$$

Suppose $x \in I S$ . Then by definition, $\textstyle x = \sum _ { i = 1 } ^ { n } r _ { i } a _ { i }$ for some $r _ { i } \in R , a _ { i } \in A$

But then

$$
\begin{array} { l } { \displaystyle { x a = \left( \sum _ { i = 1 } ^ { n } r _ { i } a _ { i } \right) a } } \\ { \displaystyle { \quad = \sum _ { i = 1 } ^ { n } r _ { i } a _ { i } a } } \\ { \displaystyle { \quad : = \sum _ { i = 1 } ^ { n } r _ { i } a _ { i } ^ { \prime } , } } \end{array}
$$

where $a _ { i } ^ { \prime } : = a _ { i } a$ for each i, which is still an element of A since A itself is a module and thus closed under multiplication.

But this expresses xa as an element of IS. Similarly, we have

$$
\begin{array} { l } { a x = a \left( \displaystyle \sum _ { i = 1 } ^ { n } r _ { i } a _ { i } \right) } \\ { \displaystyle = \sum _ { i = 1 } ^ { n } a r _ { i } a _ { i } a } \\ { \displaystyle : = \sum _ { i = 1 } ^ { n } r _ { i } a a _ { i } , } \\ { \displaystyle : = \sum _ { i = 1 } ^ { n } r _ { i } a _ { i } , } \end{array}
$$

and so $a x \in I S$ as well.

## 1.2 Part 2

Letting $R / I \sim A / I A$ be the action given by $r + I \cap { } + I A : = r a + I A$ , we need to show the following:

• r.(x + y) = r.x + r.y,

$( r + r ^ { \prime } ) . x = r . x + r ^ { \prime } . x ,$

$( r s ) . x = r . ( s . x )$ ), and

$1 . x = x .$

Letting ⊕ denote the addition defined on cosets, we have

$$
{ \begin{array} { r l } { r \nsim ( x + I A \oplus y + I A ) : = r \cap x + y + I A } \\ & { : = r ( x + y ) + I A } \\ & { = r x + r y + I A } \\ & { : = r x + I A \oplus r y + I A } \\ & { : = \left( r \cap x + I A \right) \oplus ( r \cap y + I A ) . } \end{array} }
$$

$$
\begin{array} { r l } { ( r + s ) \cap x + x + I A : = ( r + s ) x + I A } & { } \\ & { : = r x + s x + I A } \\ & { : = r x + I A \oplus s x + I A } \\ & { : = ( r s \curvearrow I A ) \oplus ( s x \curvearrow I A ) . } \end{array}
$$

$$
\begin{array} { r l } { ( r s ) \cap x + I A : = r s x + I A } \\ & { = r ( s x ) + I A } \\ & { : = r \curvearrowright ( s x + I A ) } \\ & { = r \curvearrowright ( s x + I A ) . } \end{array}
$$

$$
1 \cap x + I A : = 1 x + I A = x + I A .
$$

## 2 Problem 2

## 2.1 Part 1

We want to show that every simple R-module M is cyclic, i.e. if the only ideals of M are (0) and M itself, that $M = \langle m \rangle$ for some element $m \in M$ .

Towards a contradiction, let M be a simple R-module and suppose M is not cyclic, so $M \ne \langle m \rangle$ for any $m \in M$ . But then let $a \in M$ be an arbitrary nontrivial element; then (a) is a non-empty ideal (since it contains a), so $( a ) \neq 0$ . Since M is simple, we must have $( a ) = M$ , a contradiction.

## 2.2 Part 2

Let $\phi : A  A$ be a module endomorphism on a simple module A. Then im $\phi : = \phi ( A )$ is a submodule of A. Since A is simple, we have either im $\phi = 0$ , in which case $\phi$ is the zero map, or im $\phi = A$ , so ϕ is surjective.
In this case, we can also consider ker ϕ, which is a submodule of A. Since A is simple, we can again only have ker $\phi = A$ , which can not happen if $\phi$ is not the zero map, or ker $\phi = 0$ , in which case $\phi$ is both a surjective and an injective map and thus an isomorphism of modules.

## 3 Problem 3

## 3.1 Part 1

We want to show that if A, B are R-modules then $X = ( \hom _ { R - \mathrm { m o d } } ( A , B ) , +$ is an abelian group.
Let $f , g , h \in X$ , we then need to show the following:

a. Closure: $f + g \in X$

b. Associativity: $f + ( g + h ) = ( f + g ) + h$

c. Identity: $\operatorname { i d } \in X$

d. Inverses: $f ^ { - 1 } \in X$

e. Commutativity: $f + g = g + f$

Closure: This follows from the definition, because $( f + g ) \curvearrowright x : = f ( x ) + g ( x )$ pointwise, which is well-defined homomorphism $A  B$ •

Associativity: We have

$$
{ \begin{array} { r l } & { f + ( g + h ) \curvearrowright \rangle \curvearrowright { x : = f ( x ) + ( g + h ) ( x ) } } \\ & { \qquad : = f ( x ) + ( g ( x ) + h ( x ) ) } \\ & { \qquad = ( f ( x ) + g ( x ) ) + h ( x ) } \\ & { \qquad = ( f + g ) + h \curvearrowright . } \end{array} }
$$

Identity: We can define $\mathbf { 0 } : A  B$ by $\mathbf { 0 } ( x ) = 0 \in B$ . Then

$$
( f + \mathbf { 0 } ) \curvearrowright x = f ( x ) + 0 = f ( x ) = 0 + f ( x ) = ( \mathbf { 0 } + f ) \curvearrowright x .
$$

Inverses: Given $f \in X$ , we can define $- f : A \to B { \mathrm { ~ a s ~ } } - f ( x ) = - x$ . Then

$$
\begin{array} { r l } & { ( f + - f ) \cap x = f ( x ) + - f ( x ) = f ( x ) - f ( x ) = x - x = 0 = 0 \cap x } \\ & { ( - f + f ) \cap x = - f ( x ) + f ( x ) = - f ( x ) + f ( x ) = - x + x = 0 = 0 \cap x . } \end{array}
$$

Commutativity: Since B is a module, by definition $( B , + )$ is an abelian group.
Thus

$$
( f + g ) \curvearrowright x = f ( x ) + g ( x ) = g ( x ) + f ( x ) = ( g + f ) \curvearrowright x .
$$

## 3.2 Part 2

By part 1, (hom $R – { \bmod { ( A , A ) } } , + )$ is an abelian group, We just need to check that $( \mathrm { h o m } _ { R } ( A , A ) , \circ )$ is a monoid, i.e.:

• Associativity: $f \circ ( g \circ h ) = ( f \circ g ) \circ h$

• Identity: id $\circ f = f$

• Closure: $f \circ g \in \hom _ { R \mathrm { - m o d } } ( A , A )$

Associativity: We have

$$
\begin{array} { r l } & { f \circ ( g \circ h ) \curvearrowright x : = ( f \circ ( g \circ h ) ) ( x ) } \\ & { \qquad = f ( ( g \circ h ) ( x ) ) } \\ & { \qquad = f ( g ( h ( x ) ) ) } \\ & { \qquad = ( f \circ g ) ( h ( x ) ) } \\ & { \qquad = ( ( f \circ g ) \circ h ) ( x ) } \\ & { \qquad : = ( f \circ g ) \circ h \curvearrowright x . } \end{array}
$$

Identity: Take $\operatorname { i d } _ { A } : A \to A$ given by $\operatorname { i d } _ { A } ( x ) = x$ , then

$$
f \circ \operatorname { i d } _ { A } \cap \varnothing \varnothing \varnothing = f ( \operatorname { i d } _ { A } ( x ) ) = f ( x ) = \operatorname { i d } _ { A } ( f ( x ) ) = \operatorname { i d } _ { A } \circ f \curvearrowright . \varnothing .
$$

Closure: If $f : A  A$ and $g : A  A$ are homomorphisms, then $f \circ g : A  A$ as a set map, and is an R-module homomorphism because

$$
\begin{array} { r l } { f \circ g \curvearrowright ( r + s ) ( x + y ) = f ( g ( ( r + s ) ( x + y ) ) ) } & { } \\ & { = f ( ( r + s ) ( g ( x ) + g ( y ) ) ) } \\ & { = ( r + s ) ( f ( g ( x ) ) + f ( g ( y ) ) ) } \\ & { = ( f \curvearrowright ( r + s ) ( x + y ) ) \circ ( g \curvearrowright ( r + s ) ( x + y ) ) . } \end{array}
$$

## 3.3 Part 3

For arbitrary $x , y \in A$ , we need to check the following:

$$
f \cap ( x + y ) = f \cap x + f \cap y
$$

b. $( f + g ) \cap x = f \cap x + g \cap x$

c. $f \circ g \curvearrowleft x = f \curvearrowleft ( g \curvearrowleft x )$

d. $\operatorname { i d } _ { a } \cap x = x$

For (a):

$$
{ \begin{array} { r l } { f \curvearrowleft( x + y ) : = f ( x + y ) } \\ { \quad } & { = f ( x ) + f ( y ) \qquad { \mathrm { s i n c e ~ } } f { \mathrm { ~ i s ~ a ~ h o m o m o r p h i s m } } } \\ { \quad } & { = f \curvearrowleft x + f \curvearrowleft y \quad \qquad { \mathrm { ~ i s ~ m a x e ~ } } f { \mathrm { ~ i s ~ a ~ h o m o m o r p h i s m } } } \\ { . \qquad } & { { \mathrm { ~ i s ~ } } } \end{array} }
$$

For (b):

$$
\begin{array} { r l } { ( f + g ) \curvearrowright \curvearrowright \negtharpoons ( f + g ) ( x ) } & { } \\ & { \qquad = f ( x ) + g ( x ) } \\ & { \qquad = f \curvearrowright \colon + g \curvearrowright } \end{array}
$$

For (c):

$$
\begin{array} { r l } & { f \circ g \curvearrowright \backprime \circ x = ( f \circ g ) ( x ) } \\ & { \qquad = f ( g ( x ) ) } \\ & { \qquad = f \curvearrowright } \\ & { \qquad = f \curvearrowright } \end{array}
$$

$$
\operatorname { i d } _ { A } \cap x = \operatorname { i d } _ { A } ( x ) = x .
$$

## 4 Problem 4

Injectivity: We have the following situation:

<!-- image-->

where we would like to show that f is a monomorphism, i.e. that ker $f = 0 .$ . So let $x \in$ ker $f ,$ so $y : = f ( x ) = 0 \in B _ { 3 }$

We will show that $x = 0 \in A _ { 3 }$

• Since $y = 0 \in B _ { 3 }$ , applying $B _ { 3 } \to B _ { 4 }$ yields $y \mapsto 0 \in B _ { 4 }$ since these maps are homomorphisms and always map zero to zero.

• Pull back $0 \in B _ { 4 }$ to $0 \in B _ { 3 }$ along $\alpha _ { 4 }$ , which can be done since $\alpha _ { 4 }$ is injective, giving $0 \in A _ { 4 }$

• Since this is 0 in $A _ { 4 }$ , it is in the kernel of $A _ { 3 }  A _ { 4 }$ , yielding some $x \in A _ { 3 }$

• By commutativity of the third square, x 7→ f (x) under $f : A _ { 3 } \to B _ { 3 }$

• Since $x \in \ker ( A _ { 3 } \to A _ { 4 } ) = \operatorname { i m } \left( A _ { 2 } \to A _ { 3 } \right)$ by exactness, there is some $\alpha \in A _ { 2 }$ such that $\alpha _ { 2 } ( a ) = x \in A _ { 3 }$

$\mathrm { B y }$ injectivity of α2, a maps to a unique element $\alpha _ { 2 } ( a ) \in B _ { 2 }$

• By commutativity of the middle square, since $a \in A _ { 2 } \mapsto 0 \in B _ { 3 }$ , we must have $\alpha _ { 2 } ( a ) \mapsto 0 f ( x )$ under $B _ { 2 } \to B _ { 3 }$

• Then $\alpha _ { 2 } ( a ) \in \ker ( B _ { 2 } \to B _ { 3 } ) = \mathrm { i m } ~ ( B _ { 1 } \to B _ { 2 } )$ , so it pulls back to some $b \in B _ { 1 }$

• By surjectivity of $\alpha _ { 1 } , b$ pulls back to some $a ^ { \prime } \in A _ { 1 }$

• By commutativity of square 1, $a ^ { \prime } \mapsto a$ under $A _ { 1 }  A _ { 2 }$

• So a 7→ x under $A _ { 1 }  A _ { 3 }$

• But then a ∈ im $( A _ { 1 } \to A _ { 2 } ) = \ker ( A _ { 2 } \to A _ { 3 } )$ , so $a \mapsto 0$ under $A _ { 1 }  A _ { 3 }$

• So $x = 0$ as desired.

Surjectivity: We now have this situation:

<!-- image-->

Let $y \in B _ { 3 } ;$ we want to then show that there exists an $x \in A _ { 3 }$ such that $f ( x ) = y$

• Apply $B _ { 3 } \to B _ { 4 }$ to y to obtain $y _ { 4 } \in B _ { 4 }$

• By surjectivity of $\alpha _ { 4 }$ , this pulls back to some $a _ { 4 } \in A _ { 4 }$

• Also by exactness of $B _ { 3 }  B _ { 4 }  B _ { 5 }$ , y4 pushes forward to $0 \in B _ { 5 }$

• By injectivity of $\alpha _ { 5 }$ , this pulls back to $0 \in A _ { 5 }$

• By commutativity of the right square, $y _ { 4 } \mapsto 0$ under $A _ { 4 } \to A _ { 5 }$

• Since $a _ { 4 } \in \ker ( A _ { 4 } \to A _ { 5 } )$ , it pulls back to some $x \in A _ { 3 }$ by exactness of $A _ { 3 }  A _ { 4 }  A _ { 5 }$

• Then $f ( x ) \in B _ { 3 }$ , and it remains to show that $f ( x ) = y .$

• By commutativity of the middle square, $f ( x ) \mapsto y _ { 4 }$ under $B _ { 3 } \to B _ { 4 }$

• Since $a \mapsto y _ { 4 }$ we as well, we have $z : = f ( x ) - y \in B _ { 3 }$ maps to $0 \in B _ { 4 }$

${ \mathrm { S i n c e ~ } } z \in \ker ( B _ { 3 } \to B _ { 4 } )$ , by exactness it pulls back to some $b _ { 2 } \in B _ { 2 }$

• By surjectivity of α2, this pulls back to some $a _ { 2 } \in A _ { 2 }$

• By commutativity of the first square, $a _ { 2 } \mapsto z \in B _ { 3 }$

$a _ { 2 } \mapsto a _ { 3 } \in A _ { 3 }$ , where a3 may not equal x, but $f ( a _ { 3 } ) = z : = f ( a ) - y .$

• Then $f ( a _ { 3 } ) = f ( x ) - y \implies y = f ( x ) - f ( a _ { 3 } ) = f ( x - a _ { 3 } )$ since f is a homomorphism.

• This shows that $x - a _ { 3 } \mapsto y$ under f, which is the element we wanted to produce.

## 5 Problem 5

## 5.1 Part (a)

We want to show that if $( p ) \leq R$ is a prime ideal then $R / ( p )$ is a field, so we’ll proceed by letting $x + ( p ) \in R / ( p )$ be arbitrary where $x \not \in ( p )$ and producing a multiplicative inverse.

Since R is a principal ideal domain, prime ideals are maximal, so (p) is maximal.
Then $x \in R \backslash ( p )$ so define

$$
I : = \{ p + r x \ \circ p \in ( p ) , r \in R \} \ \preceq R ,
$$

which is an ideal in R.

In particular, since $x \not \in ( p )$ , we have a strict containment $( p ) < I$ , but since (p) was maximal this forces $I = R$

Then $1 \in I .$ , so there exists some p, r such that $p + r x = 1$ , i.e. $r x - 1 \in ( p )$

But then

$$
r + ( p ) \cdot x + ( p ) = r x + ( p ) = 1 + ( p ) ,
$$

which says that $( x + ( p ) ) ^ { - 1 } = r + ( p )$ in $R / ( p )$

## 5.2 Part (b)

Images and kernels of module homomorphisms are always submodules, so define

$$
\phi : A  A
$$

$$
x \mapsto p x .
$$

This is a module homomorphism, and

$$
{ \mathrm { i m ~ } } \phi : = \{ p x ~ { \textrm { ‰} }
$$

$$
\ker \phi : = \{ a \in A \ \geqslant p A = 0 \} : = A [ p ] .
$$

## 5.3 Part (c)

Since $R / ( p )$ is a field, we just need to show that $A / p A \cap R / ( p )$ defines a module.

$$
r \cdot ( x + y ) = r x + r y \colon
$$

$$
\begin{array} { r l } { r + ( p ) \curvearrowright \backsimeq x + p A \oplus y + p A : = r + ( p ) \curvearrowright \backsimeq x + y + p A } & { } \\ & { \mathrel { \mathop : } = r ( x + y ) + p A } \\ & { = r x + r y + p A } \\ & { \mathrel { \mathop : } = r x + p A \oplus r y + p A } \\ & { \mathrel { \mathop : } = r \curvearrowright { x } + p A \oplus r \curvearrowright. } \end{array}
$$

$$
( r + s ) \cdot x = r x + s x \colon
$$

$$
{ \begin{array} { r l } { r + ( p ) \oplus s + ( p ) \curvearrow x + p A : = r + s + ( p ) \curvearrow x + p A } & { } \\ & { \mathrel { \mathop : } = ( r + s ) x + p A } \\ & { = r x + s x + p A } \\ & { \mathrel { \mathop : } = r x + p A \oplus s x + p A } \\ & { \mathrel { \mathop : } = r + ( p ) \curvearrow x + p A \oplus s + ( p ) \curvearrow x + p A . } \end{array} }
$$

$$
r s \cdot x = r \cdot ( s \cdot x ) \colon
$$

$$
\begin{array} { r l } { r + ( p ) \cdot s + ( p ) \curvearrowright \sim x + p A : = r s + ( p ) \curvearrowright \sim x + p A } & { } \\ & { = r s x + p A } \\ & { : = r + ( p ) \curvearrowright \ast s x + p A } \\ & { : = r + ( p ) \curvearrowright { s + ( p ) \curvearrowright } x + p A . } \end{array}
$$

$$
1 \cdot x = x \colon
$$

$$
1 _ { R } + ( p ) \curvearrowright x + p A = 1 _ { R } x + p A = x + p A .
$$

## 5.4 Part (d)

Similarly, since $R / ( p )$ is a field, it suffices to show that $R / ( p ) \sim A [ p ]$ defines a module.

$$
r \cdot ( x + y ) = r x + r y \colon
$$

$$
\begin{array} { c } { { r + ( p ) \curvearrowright ( a + a ^ { \prime } ) : = r ( a + a ^ { \prime } ) } } \\ { { { } } } \\ { { = r a + r a ^ { \prime } } } \\ { { { } } } \\ { { = r \curvearrowright a + r \curvearrowright a ^ { \prime } . } } \end{array}
$$

$$
( r + s ) \cdot x = r x + s x \colon
$$

$$
\begin{array} { c } { { r + s + ( p ) \curvearrow { a } = ( r + s ) a } } \\ { {  = r a + s a } } \\ { {  = r \curvearrow { a } + s \curvearrow { a } . } } \end{array}
$$

$$
r s \cdot x = r \cdot ( s \cdot x ) \colon
$$

$$
\begin{array} { c } { { r s + ( p ) \curvearrowright a = r s a } } \\ { {  = r \wedge s a } } \\ { {  = r \curvearrowright s \wedge a . } } \end{array}
$$

1 · x = x:

$$
1 _ { R } + ( p ) \curvearrowright a = 1 a = a .
$$

## 6 Problem 6

Supposing that dim $V = n ,$ let $B : = \{ \mathbf { b } _ { k } \mid 1 \leq k \leq n \}$ be a basis for $V ,$ and define

$$
\mathbf { e } _ { i } : = [ 0 , 0 , \cdots , 1 , \cdots , 0 ] \in V ^ { \oplus m }
$$

where the 1 occurs in the ith position.
The claim is that $B ^ { m } : = \{ \mathbf { e } _ { i } \mathbf { b } _ { k } \mid 1 \leq i \leq n , 1 \leq k \leq m \}$ forms a basis for $V ^ { \oplus m }$ •

Elements in ${ \boldsymbol { B } } ^ { m }$ are of the form

$$
\begin{array} { r } { [ { \bf b } _ { 1 } , 0 , 0 , \cdots , 0 ] } \\ { [ { \bf b } _ { 2 } , 0 , 0 , \cdots , 0 ] } \\ { \cdots \cdot \nabla } \\ { [ 0 , { \bf b } _ { 1 } , 0 , \cdots , 0 ] } \\ { [ 0 , { \bf b } _ { 2 } , 0 , \cdots , 0 ] } \\ { \cdots \cdot \nabla , } \end{array}
$$

and by construction, $| B | = m n = m$ dim V .

To see that this is a spanning set, let $\mathbf { x } \in V ^ { \oplus m }$ , so $\mathbf { x } = [ \mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } , \cdot \cdot \cdot , \mathbf { v } _ { m } ]$ where each $\mathbf { v } _ { i } \in V$ Then each $\mathbf { v } _ { i } \in \mathcal Ḋ B Ḍ$ , so $\begin{array} { r } { \mathbf { v } _ { i } = \sum _ { k = 1 } ^ { n } \alpha _ { k , i } \mathbf { b } _ { k } } \end{array}$ . But then

$$
\mathbf { x } = [ \sum _ { k = 1 } ^ { n } \alpha _ { k , 1 } \mathbf { b } _ { k } , \sum _ { k = 1 } ^ { n } \alpha _ { k , 2 } \mathbf { b } _ { k } , \cdots , \sum _ { k = 1 } ^ { n } \alpha _ { k , m } \mathbf { b } _ { k } ] : = \sum _ { i = 1 } ^ { m } \sum _ { k = 1 } ^ { n } \alpha _ { k , i } \mathbf { b } _ { k } \mathbf { e } _ { i } ,
$$

which exhibits $\mathbf { x } \in B ^ { m }$

To see that it is linearly independent, supposing that $\begin{array} { r } { \mathbf { x } = \sum _ { i } \sum _ { k } \alpha _ { k , i } \mathbf { b } _ { k } \mathbf { e } _ { i } = \boldsymbol { 0 } } \end{array}$ , this says that $\mathbf { x } = [ 0 , 0 , \cdots , 0 ]$ , which forces $\textstyle \sum _ { k } \alpha _ { k , i } \mathbf { b } _ { k }$ to be zero for each i.

But for a fixed $i ,$ since $\{ { \bf { b } } _ { k } \}$ was a basis for V , this means that $\alpha _ { k , i } = 0$ for all k. But then $\alpha _ { k , i } = 0$ for all pairs i, k.

## 7 Problem 7

Let $F _ { 1 } , F _ { 2 }$ be free, so they have bases $B _ { 1 } = \left\{ { \bf b } _ { 1 , k } \right\} , B _ { 2 } = \left\{ { \bf b } _ { 2 , k } \right\}$ . Supposing that they have the invariant dimension property, we can assume that $\# B _ { 1 } : = \mathrm { r a n k } F _ { 1 }$ and similarly $\# B _ { 2 } : = \mathrm { r a n k } F _ { 2 }$

The claim is that the set

$$
\mathcal { B } = \{ ( v , 0 ) ~ | ~ v \in \mathcal { B } _ { 1 } \} \bigcup \{ ( 0 , w ) ~ | ~ w \in \mathcal { B } _ { 2 } \}
$$

is a basis for $F _ { 1 } \oplus F _ { 2 }$ , where $\# B = \# B _ { 1 } + \# B _ { 2 } = \operatorname { r a n k } F _ { 1 } + \operatorname { r a n k } F _ { 2 }$

So see that B spans $F _ { 1 } \oplus F _ { 2 }$ , let $x \in F _ { 1 } \oplus F _ { 2 } = ( f _ { 1 } , f _ { 2 } )$ be arbitrary.
Since $f _ { 1 } \in F _ { 1 }$ , we have $\begin{array} { r } { f _ { 1 } = \sum _ { i } r _ { i } \mathbf { b } _ { 1 , i } } \end{array}$ , and similarly $\begin{array} { r } { f _ { 2 } = \sum _ { j } s _ { j } \mathbf { b } _ { 2 , j } } \end{array}$

We can then write

$$
x = ( f _ { 1 } , f _ { 2 } ) = ( f _ { 1 } , 0 ) + ( 0 , f _ { 2 } ) = ( \sum _ { i } r _ { i } \mathbf { b } _ { 1 , i } , 0 ) + ( 0 , \sum _ { j } s _ { j } \mathbf { b } _ { 2 , j } ) ,
$$

which exhibits x as a linear combination of elements in B.

To see linear independence, we just note that

$$
\begin{array} { l } { \displaystyle x = ( 0 , 0 ) } \\ { \displaystyle \quad = \sum _ { i } r _ { i } ( v _ { i } , 0 ) + \sum _ { j } s _ { j } ( 0 , w _ { j } ) } \\ { \displaystyle \quad = \sum _ { i } ( r _ { i } v _ { i } , 0 ) + \sum _ { j } ( 0 , s _ { j } w _ { j } ) } \\ { \displaystyle \quad = ( \sum _ { i } r _ { i } v _ { i } , \sum _ { j } s _ { j } w _ { j } ) } \\ { \displaystyle \quad \implies \sum _ { i } r _ { i } v _ { i } = 0 \quad \& \sum _ { j } s _ { j } w _ { j } = 0 , } \end{array}
$$

but since the $v _ { i }$ were a basis of $F _ { 1 }$ and the wj a basis of $F _ { 2 }$ , this forces $r _ { i } = 0 , w _ { j } = 0$ for all $i , j$
