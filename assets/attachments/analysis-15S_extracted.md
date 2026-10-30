Students should solve four real analysis problems (numbered 1–6) and four complex analysis problems (numbered 7–12).

Problem 1. Let $f \in L ^ { 1 } ( \mathbf { R } )$ . Show that

$$
\operatorname* { l i m } _ { n \to \infty } \sum _ { k = - n ^ { 2 } } ^ { n ^ { 2 } } \left| \int _ { k / n } ^ { ( k + 1 ) / n } f ( x ) d x \right| = \int \left| f ( x ) \right| d x .
$$

Problem 2. Let $f \in L _ { \mathrm { l o c } } ^ { 2 } ( \mathbf { R } ^ { n } ) , g \in L _ { \mathrm { l o c } } ^ { 3 } ( \mathbf { R } ^ { n } )$ . Assume that for all real $r \geq 1$ , we have

$$
\int _ { r \leq | x | \leq 2 r } \left| f ( x ) \right| ^ { 2 } d x \leq r ^ { a } , \quad \int _ { r \leq | x | \leq 2 r } \left| g ( x ) \right| ^ { 3 } d x \leq r ^ { b } .
$$

Here $a , b \in \mathbf { R }$ are such that 3a $\cdot + 2 b + n < 0$ . Show that $f g \in L ^ { 1 } ( \mathbf { R } ^ { n } )$

Problem 3. Let $f \in L _ { \mathrm { l o c } } ^ { 1 } ( \mathbf { R } ^ { n } )$ and let

$$
M f ( x ) = \operatorname* { s u p } _ { r > 0 } { \frac { 1 } { m ( B ( r , x ) ) } } \int _ { B ( r , x ) } | f ( y ) | \ d y
$$

be the Hardy-Littlewood maximal function.

• Show that

$$
m ( \{ x : M f ( x ) > s \} ) \leq { \frac { C _ { n } } { s } } \int _ { | f ( x ) | > s / 2 } | f ( x ) | \ d x , \quad s > 0 ,
$$

where the constant $C _ { n }$ depends on n only. The Hardy-Littlewood maximal theorem may be used.

• Prove that if $\varphi \in C ^ { 1 } ( \mathbf R ) , \varphi ( 0 ) = 0$ , and $\varphi ^ { \prime } > 0$ then

$$
\int \varphi ( M f ( x ) ) d x \leq C _ { n } \int | f ( x ) | \left( \int _ { 0 < t < 2 | f ( x ) | } { \frac { \varphi ^ { \prime } ( t ) } { t } } d t \right) d x .
$$

Problem 4. Let $f \in L _ { \mathrm { l o c } } ^ { 1 } ( \mathbf { R } )$ be 2π-periodic. Show that linear combinations of the translates $f ( x - a ) , a \in \mathbf { R }$ , are dense in $L ^ { 1 } ( ( 0 , 2 \pi ) )$ if and only if each Fourier coefficient of f is 6= 0.

Problem 5. Let $u \in L ^ { 2 } ( \mathbf { R } )$ and let us set

$$
U ( x , \xi ) = \int e ^ { - ( x + i \xi - y ) ^ { 2 } / 2 } u ( y ) d y , \quad x , \xi \in \mathbf { R } .
$$

Show that $U ( x , \xi )$ is well defined on $\mathbf { R } ^ { 2 }$ and that there exists a constant $C > 0$ such that for all $u \in L ^ { 2 } ( \mathbf { R } )$ , we have

$$
\iint | U ( x , \xi ) | ^ { 2 } e ^ { - \xi ^ { 2 } } d x d \xi = C \int | u ( y ) | ^ { 2 } \ d y .
$$

Determine C explicitly.

Problem 6. When $B _ { 1 }$ and $B _ { 2 }$ are Banach spaces, we say that a linear operator $T : B _ { 1 } \to B _ { 2 }$ is compact if for any bounded sequence $( x _ { n } )$ in $B _ { 1 }$ , the sequence $\left( T x _ { n } \right)$ has a convergent subsequence. Show that if $T$ is compact then Im $T$ has a dense countable subset.

Problem 7. Let $\mathbf { D } = \{ z \in \mathbf { C } : | z | < 1 \}$ and $\mathbf { C } ^ { + } = \{ z \in \mathbf { C } : \mathrm { I m } z > 0 \}$ . Suppose $f _ { n } : \mathbf { D } \to \mathbf { C } ^ { + }$ is a sequence of holomorphic functions and $f _ { n } ( 0 ) \to 0 { \mathrm { ~ a s ~ } } n \to \infty$ . Show that $f _ { n } ( z ) \to 0$ uniformly on compact subsets of D.

Problem 8. Let $f : \mathbf { C }  \mathbf { C }$ be holomorphic and suppose

$$
\operatorname* { s u p } _ { x \in \mathbf { R } } \left\{ | f ( x ) | ^ { 2 } + | f ( i x ) | ^ { 2 } \right\} < \infty \quad { \mathrm { a n d } } \quad | f ( z ) | \leq e ^ { | z | } \quad { \mathrm { f o r ~ a l l ~ } } z \in \mathbf { C } .
$$

Deduce that $f ( z )$ is constant.

Problem 9. Let $\Omega = \{ z \in \mathbf { C } : | z | > 1$ and $\mathrm { R e } z > - 2 \}$ Suppose $u : \overline { { \Omega } }  \mathbf { R }$ is bounded, continuous, and harmonic on Ω and also that $u ( z ) = 1$ when $| z | = 1$ and that $u ( z ) = 0$ when $\mathrm { R e } ( z ) = - 2$ . Determine $u ( 2 )$ .

Problem 10. Determine

$$
\int _ { - \infty } ^ { \infty } { \frac { d y } { ( 1 + y ^ { 2 } ) ( 1 + [ x - y ] ^ { 2 } ) } }
$$

for all $x \in \mathbf { R }$ . Justify all manipulations.

Problem 11. Let $\Omega = \left\{ z \in \mathbf { C } : 0 < | z | < 1 \right\}$ . Prove that for every bounded harmonic function $u : \Omega \to { \bf R }$ there is a harmonic function $v : \Omega \to \mathbf { R }$ obeying

$$
{ \frac { \partial u } { \partial x } } = { \frac { \partial v } { \partial y } } \quad { \mathrm { a n d } } \quad { \frac { \partial u } { \partial y } } = - { \frac { \partial v } { \partial x } }
$$

Problem 12. Find all entire functions $f : \mathbf { C }  \mathbf { C }$ that obey

$$
f ^ { \prime } ( z ) ^ { 2 } + f ( z ) ^ { 2 } = 1 .
$$

Prove that your list is exhaustive.