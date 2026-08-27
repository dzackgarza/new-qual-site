## Solution Outlines for Chapter 10, Part A

## 1: Prove that the mapping given in Example 2 is a homomorphism.

Let $\phi : G L ( 2 , \mathbb { R } ) \to \mathbb { R } ^ { * }$ be defined by $A \mapsto d e t ( A )$ . Let $A \in G L ( 2 , \mathbb { R } )$ . This means that A is invertible thus the $d e t ( A )$ is not zero, hence the $d e t ( A )$ is in $\mathbb { R } ^ { * }$ . So φ maps to $\mathbb { R } ^ { * }$ as claimed. Now let $A , B \in G L ( 2 , \mathbb { R } )$ . Then $\phi ( A B ) = d e t ( A B ) = d e t ( A ) d e t ( B ) = \phi ( A ) \phi ( B )$ , so $\phi$ is a homomorphism.

## 2: Prove that the mapping given in Example 3 is a homomorphism.

Let $\phi : \mathbb { R } ^ { * } \to \mathbb { R } ^ { * }$ be defined by $x \mapsto | x |$ . Then $\phi ( x y ) = | x y | = | x | | y | = \phi ( x ) \phi ( y )$ so $\phi$ is a homomorphism.

## 3: Prove that the mapping given in Example 4 is a homomorphism.

Let $\phi : \mathbb { R } [ x ] \to \mathbb { R } [ x ]$ be defined by $f \mapsto f ^ { \prime }$ . Then for $f , g \in \mathbb { R } [ x ] , \phi ( f + g ) = ( f + g ) ^ { \prime } =$ $f ^ { \prime } + g ^ { \prime } = \phi ( f ) + \phi ( g )$ so φ is a homomorphism.

# 6: Let G be the group of all polynomials with real coefficients under addition. For each f in G let R f denote the antiderivative of f that passes through the point (0, 0). Show that the mapping $f \mapsto \textstyle \int f$ from G to G is a homomorphism. What is the kernel of this mapping? Is this mapping a homomorphism if $\textstyle \int f$ denotes the antiderivative of f that passes through (0, 1)?

Let $\phi : \mathbb { R } [ x ] \to \mathbb { R } [ x ]$ be defined by $f \mapsto \int f$ Then $\phi ( f + g ) = \textstyle \int ( f + g ) + c $ where $c = - ( f + g ) ( 0 )$ and $\textstyle \int ( f + g )$ is the polynomial that is the antiderivative without a constant term. Now, $\begin{array} { r } { \phi ( f ) + \phi ( g ) = \int f + \int g + c _ { 1 } + c _ { 2 } } \end{array}$ where $c _ { 1 } = - f ( 0 )$ and $c _ { 2 } = - g ( 0 )$ . Hence $\phi ( f + g ) = \phi ( f ) + \phi ( g )$ for all $f , g \in \mathbb { R } [ x ]$ so $\phi$ is a homomorphism.

Now, the kernel of $\phi$ are the set of things that map to the identity, 0. So $K e r \phi = \{ f \vert \int f = 0 \} = \{ a _ { 0 } + a _ { 1 } x + \dotsc + a _ { n } x ^ { n } \vert a _ { 0 } x + \frac { a _ { 1 } } { 2 } x ^ { 2 } + \dotsc + \frac { a _ { n } } { n + 1 } x ^ { n + 1 } = 0 \} = \{ a _ { 0 } = a _ { 1 } = \dotsc = a _ { n } = 0 \} = \{ 0 \}$

If the function $\textstyle \int f$ goes through (0,1) instead, it is not a homomorphism. This is because $\phi ( f + g ) ( 0 ) = 1$ but $( \phi ( f ) + \phi ( g ) ) ( 0 ) = \phi ( f ) ( 0 ) + \phi ( g ) ( 0 ) = 1 + 1 = 2$ , so the functions are not the same.

## 7: If φ is a homomorphism from G to H and $\sigma$ is a homomorphism from H to K, show that σφ is a homomorphism from G to K. How are Kerφ and Kerσφ related?

Let $\phi : G \to H$ be a homomorphism and $\sigma : H \to K$ also be a group homomorphism. Then $\sigma \phi : G \to K$ and $\sigma \phi ( x y ) = \sigma ( \phi ( x ) \phi ( y ) ) = \sigma ( \phi ( x ) ) \sigma ( \phi ( y ) ) = \sigma \phi ( x ) \sigma \phi ( y )$ so the composition is a homomorphism.

Notice that $\sigma$ is a homomorphism so the ker $\phi$ maps to the identity in H. Since $\sigma$ is also a homomorphism, it maps this identity to the identity in K. Thus, $K e r \phi \subseteq K e r \sigma \phi$ . Note that more things from H could map to the identity in K so we do not know that the $K e r \phi = K e r \sigma \phi$

## 10: Let G be a subgroup of some dihedral group. For each x in G define $\phi ( x )$ to be +1 if x is a rotation and −1 if x is a reflection. Prove that $\phi$ is a homomorphism from G to the multiplicative group $\{ + 1 , \ - 1 \}$ . What is the kernel?

Let $\phi$ be defined as above. Now, elements in G either look like a rotation or a flip. So all elements are either of the form $r ^ { i }$ or $r ^ { i } f$ . Thus to show that $\phi$ is a homomorphism, I need to consider four cases: two rotations multiplied, two flips multiplied, a rotation times a flip, and a flip times a rotation (recall: not Abelian). We consider each in turn below and conclude that $\phi$ is a homomorphism.

$$
\bullet \ \phi ( r ^ { i } \circ r ^ { j } ) = \phi ( r ^ { i + j } ) = 1 = 1 \cdot 1 = \phi ( r ^ { i } ) \cdot \phi ( r ^ { j } )
$$

$$
\phi ( r ^ { i } f \circ r ^ { j } f ) = \phi ( r ^ { i } r ^ { n - j } f f ) = \phi ( r ^ { i + n - j } ) = 1 = - 1 \cdot - 1 = \phi ( r ^ { i } f ) \cdot \phi ( r ^ { j } f )
$$

• $\phi ( r ^ { i } \circ r ^ { j } f ) = \phi ( r ^ { i + j } f ) = - 1 = 1 \cdot - 1 = \phi ( r ^ { i } ) \cdot \phi ( r ^ { j } f )$

$$
\bullet \ \phi ( r ^ { i } f \circ r ^ { j } ) = \phi ( r ^ { i } r ^ { n - j } f ) = \phi ( r ^ { i + n - j } f ) = - 1 = - 1 \cdot 1 = \phi ( r ^ { i } f ) \cdot \phi ( r ^ { j } )
$$

$K e r \phi = \{ g \mid \phi ( g ) = 1 \} = \{ \text { rotations in } G \} = \langle r \rangle$

## 14: Explain why the correspondence $x \mapsto 3 x$ from $\mathbb { Z } _ { 1 2 }$ to $\mathbb { Z } _ { 1 0 }$ is not a homomorphism.

If the correspondence is a homomorphism, then it should preserve the operation. Let’s show this is not true via a counter example. Take $6 , 7 \in \mathbb { Z } _ { 1 2 }$ Then $\phi ( 6 + 7 ) = \phi ( 1 ) = 3$ . But $\phi ( 6 ) + \phi ( 7 ) = 1 8 + 2 1 = 8 + 1 = 9$ . Since $3 \neq 9$ in $\mathbb { Z } _ { 1 0 }$ the operation is not preserved.