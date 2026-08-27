## Homework 8

1. Prove that if $f \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ then $\hat { f }$ is uniformly continuous on $\mathbb { R } ^ { n }$

Solution: Note that we have

$$
\begin{array} { r c l } { { \hat { f } ( y + h ) - \hat { f } ( y ) } } & { { = } } & { { \displaystyle \int _ { \mathbb { R } ^ { n } } f ( x ) \left( e ^ { - 2 \pi i x \cdot ( y + h ) } - e ^ { - 2 \pi i x \cdot y } \right) d x } } \\ { { } } & { { = } } & { { \displaystyle \int _ { \mathbb { R } ^ { n } } f ( x ) e ^ { - 2 \pi i x \cdot y } ( e ^ { - 2 \pi i x \cdot h } - 1 ) d x } } \end{array}
$$

Thus we have that

$$
{ \Big | } { \hat { f } } ( y + h ) - { \hat { f } } ( y ) { \Big | } \leq \int _ { \mathbb { R } ^ { n } } | f ( x ) | \left| e ^ { - 2 \pi i x \cdot h } - 1 \right| d x
$$

It suffices to show that this last expression can be made arbitrarily small as we let $h \to 0$ , independently of $y .$ The idea is to apply the Dominated Convergence Theorem. Set $g _ { h } ( x ) = f ( x ) e ^ { - 2 \pi i x \cdot ( y + h ) }$ . Then we have that $| g _ { h } | \leq | f |$ , and $g _ { h }  g _ { 0 } = f ( x ) e ^ { - 2 \pi i x \cdot y }$ almost everywhere in $\mathbb { R } ^ { n }$ . So we then have that

$$
\hat { f } ( y + h ) = \int _ { \mathbb { R } ^ { n } } g _ { h } ( x ) d x \to \int _ { \mathbb { R } ^ { n } } g _ { 0 } ( x ) d x = \hat { f } ( y )
$$

as $h \to 0$ by Dominated Convergence.

2. Give $f \in L ^ { 2 } ( \mathbb { R } ^ { n } )$ , prove that

$$
\xi  \int _ { | x | \leq N } f ( x ) e ^ { - 2 \pi i x \cdot \xi } d x
$$

converges to $\hat { f }$ in $L ^ { 2 } ( \mathbb { R } ^ { n } )$ as $N \to \infty$

Solution: Let

$$
g _ { N } ( \xi ) = \int _ { | x | \leq N } f ( x ) e ^ { - 2 \pi i x \cdot \xi } d x .
$$

Observe that

$$
\hat { f } ( \xi ) - g _ { N } ( \xi ) = \int _ { \mathbb { R } ^ { n } } f ( x ) 1 _ { \{ x : | x | > N \} } e ^ { - 2 \pi i x \cdot \xi } d x = f 1 \widehat { \{ x : | x | > N \} } ( \xi ) .
$$

Then we have that

$$
\begin{array} { r l r } { \Big \| \hat { f } - g _ { N } \Big \| _ { L ^ { 2 } ( \mathbb { R } ^ { n } ) } } & { = } & { \Big \| f 1 _ { \{ x : | x | > N \} } \Big \| _ { L ^ { 2 } ( \mathbb { R } ^ { n } ) } } \\ & { = } & { \Big \| f 1 _ { \{ x : | x | > N \} } \Big \| _ { L ^ { 2 } ( \mathbb { R } ^ { n } ) } } \end{array}
$$

But, for N large enough, we have that this last expression can be made smaller than any given $\epsilon > 0$ since $f \in L ^ { 2 } ( \mathbb { R } ^ { n } )$

3. If $f _ { k } , f \in { \cal S } ( \mathbb { R } ^ { n } )$ and $f _ { k } \to f$ in $S ( \mathbb { R } ^ { n } )$ , then $\hat { f } _ { k } \to \hat { f }$ and $\check { f } _ { k }  \check { f }$ in $S ( \mathbb { R } ^ { n } )$

Solution: Recall that $f _ { k } \to f \in { \mathcal { S } } ( \mathbb { R } ^ { n } )$ if for all multi-indices α and $\beta$ we have

$$
\rho _ { \alpha , \beta } ( f _ { k } - f ) = \operatorname* { s u p } _ { x \in \mathbb { R } ^ { n } }  x ^ { \alpha } ( \partial ^ { \beta } ( f _ { k } - f ) )   0
$$

as $k \to \infty$ . We then have that

$$
\operatorname* { s u p } _ { x \in \mathbb { R } ^ { n } } \left. x ^ { \alpha } \partial ^ { \beta } ( \widehat { f } _ { k } - \widehat { f } ) \right. = C ( \alpha , \beta ) \operatorname* { s u p } _ { x \in \mathbb { R } ^ { n } } \left. \partial ^ { \alpha } ( \widehat { x ^ { \beta } ( f _ { k } - f ) } ) \right. \leq \left. \partial ^ { \alpha } ( x ^ { \beta } ( f _ { k } - f ) ) \right. _ { L ^ { 1 } ( \mathbb { R } ^ { n } ) }
$$

Recall that if $f _ { k }  f$ in $S ( \mathbb { R } ^ { n } )$ , then we have that $f _ { k }  f$ in $L ^ { p } ( \mathbb { R } ^ { n } )$ for any $0 < p \le \infty$ Moreover, we have

$$
\big \| \partial ^ { \beta } g \big \| _ { L ^ { p } ( \mathbb { R } ^ { n } ) } \leq C ( p , n ) \sum _ { | \alpha | = \lfloor \frac { n + 1 } { p } \rfloor + 1 } \rho _ { \alpha , \beta } ( g ) .
$$

Apply this estimate with $g \ = \ f _ { k } - f$ and $p = 1$ to conclude that $\hat { f } _ { k } \  \ \hat { f } .$ Similar computations prove the statement for $\check { f } _ { k }  \check { f }$

4. Find the set of eigenvalues of the Fourier transform, namely the λ such that

$$
{ \hat { f } } = \lambda f .
$$

Hint: Apply the Fourier transform to the above identity, and consider functions of the form xe− $\pi x ^ { 2 } , ( a + b x ^ { 2 } ) e ^ { - \pi x ^ { 2 } }$ and $( c x + d x ^ { 3 } ) e ^ { - \pi x ^ { 2 } }$ for good choices of $a , b , c , d .$

Solution: Note that we have

$$
{ \hat { \hat { f } } } ( x ) = f ( - x )
$$

and so $\hat { \hat { f } } ( x ) = f ( x )$ . If f is an eigenfunction then we see that the corresponding eigenvalue must satisfy

$$
\lambda ^ { 4 } - 1 = 0 .
$$

From this we see that the eigenvalues of the Fourier transform are $1 , - 1 , i , - i$ Using the remaining part of the hint, one can deduce the corresponding eigenfunctions to be Hermite polynomials.

5. If $0 < c < \infty$ , define $f _ { c } ( x ) = e ^ { - c x ^ { 2 } }$

(a) Compute $\hat { f } _ { c }$ in the following way: Let $\varphi = \hat { f } _ { c }$ and show that $4 \pi ^ { 2 } t \varphi ( t ) + 2 c \varphi ^ { \prime } ( t ) = 0$ and then solve the resulting differential equation;

(b) Show that there is one (and only one) value of c for which $f _ { c } = \hat { f } _ { c }$

(c) Show that $f _ { a } * f _ { b } = \gamma f _ { c }$ where $\gamma = \gamma ( a , b )$ and $c = c ( a , b )$

Solution: Part (a): Set

$$
\varphi ( t ) = \hat { f } _ { c } ( t ) = \int _ { \mathbb { R } } e ^ { - c x ^ { 2 } } e ^ { - 2 \pi i x t } d x .
$$

Then we have

$$
\begin{array} { l l l } { \displaystyle \varphi ^ { \prime } ( t ) } & { = } & { \displaystyle 2 \pi i \int _ { \mathbb R } x e ^ { - c x ^ { 2 } } e ^ { - 2 \pi i x t } d x } \\ { \displaystyle } & { = } & { \displaystyle - \frac \pi c i \int _ { \mathbb R } \frac { d } { d x } \left( e ^ { - c x ^ { 2 } } \right) e ^ { - 2 \pi i x t } d x } \\ { \displaystyle } & { = } & { \displaystyle - \frac \pi c i \int _ { \mathbb R } e ^ { - c x ^ { 2 } } \frac { d } { d x } \left( e ^ { - 2 \pi i x t } \right) d x } \\ { \displaystyle } & { = } & { \displaystyle - 2 \frac { \pi ^ { 2 } } { c } t \varphi ( t ) . } \end{array}
$$

Rearrangement gives the resulting differential equation. Interchange of the derivative with respect to t, and switching the derivative with respect to x is justified since $e ^ { - c x ^ { 2 } }$ is a Schwarz class function. Solving the resulting differential equation gives that

$$
{ \hat { f } } _ { c } ( t ) = k e ^ { - { \frac { \pi ^ { 2 } } { c } } t ^ { 2 } }
$$

where k is some constant. Note that we have that $\begin{array} { r } { \hat { f } _ { c } ( 0 ) = k = \int _ { \mathbb { R } } e ^ { - c x ^ { 2 } } d x = \sqrt { \frac { \pi } { c } } . } \end{array}$ . Thus we have that

$$
{ \hat { f } } _ { c } ( t ) = { \sqrt { \frac { \pi } { c } } } e ^ { - { \frac { \pi ^ { 2 } } { c } } t } .
$$

Part (b): Suppose that we have a value of c such that

$$
f _ { c } ( t ) = \hat { f } _ { c } ( t ) .
$$

Then for all $t \in \mathbb { R }$ we have that

$$
{ \sqrt { \frac { \pi } { c } } } e ^ { t ^ { 2 } \left( { \frac { \pi ^ { 2 } } { c } } - c \right) } = 1 .
$$

In particular, it must be true when $t = 0 ,$ , and we obtain that $c = \pi$ is the only value that works.

Part (c): Taking the Fourier Transform, we have that

$$
\widehat { f _ { a } * f _ { b } } = \widehat { f _ { a } f _ { b } } = \frac { \pi } { \sqrt { a b } } e ^ { - \frac { \pi ^ { 2 } } { a } t ^ { 2 } } e ^ { - \frac { \pi ^ { 2 } } { b } t ^ { 2 } } = \frac { \pi } { \sqrt { a b } } e ^ { - \pi ^ { 2 } \left( \frac { 1 } { a } + \frac { 1 } { b } \right) t ^ { 2 } } = \frac { \pi } { \sqrt { a b } } e ^ { - \pi ^ { 2 } \frac { a + b } { a b } t ^ { 2 } } .
$$

Set $\textstyle c = c ( a , b ) = { \frac { a b } { a + b } }$ and $\begin{array} { r } { \gamma = \gamma ( a , b ) = \sqrt { \frac { \pi } { a + b } } . } \end{array}$ , then we have that

$$
{ \frac { \pi } { \sqrt { a b } } } e ^ { - \pi ^ { 2 } { \frac { a + b } { a b } } t ^ { 2 } } = \gamma { \sqrt { \frac { \pi } { c } } } e ^ { - { \frac { \pi ^ { 2 } } { c } } t ^ { 2 } } = \gamma { \hat { f } } _ { c } ( t ) .
$$

So we have that when $\textstyle c = c ( a , b ) = { \frac { a b } { a + b } }$ and $\begin{array} { r } { \gamma = \gamma ( a , b ) = \sqrt { \frac { \pi } { a + b } } } \end{array}$ that

$$
f _ { a } * f _ { b } = \gamma f _ { c } .
$$

6. Suppose that $f \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ and $f > 0$ . Show that $\left| \hat { f } ( y ) \right| < \hat { f } ( 0 )$ for $y \ne 0$

Solution: Note that for any $y \in \mathbb { R } ^ { n }$ we have

$$
\left| { \hat { f } } ( y ) \right| \leq \| f \| _ { L ^ { 1 } } = \int _ { \mathbb { R } ^ { n } } f ( x ) d x = { \hat { f } } ( 0 ) .
$$

Suppose that for some $y \ne 0$ we have that

$$
\left| { \hat { f } } ( y ) \right| = { \hat { f } } ( 0 ) .
$$

This then leads to a contradiction. Indeed, we have that

$$
\int _ { \mathbb R ^ { n } } f ( x ) d x = { \hat { f } } ( 0 ) = \left| \int _ { \mathbb R ^ { n } } f ( x ) e ^ { - 2 \pi i x \cdot y } d x \right| = \eta \int _ { \mathbb R ^ { n } } f ( x ) e ^ { - 2 \pi i x \cdot y } d x
$$

where $\eta$ is a constant complex number with $| \eta | = 1$ . Re-arrangement of this inequality gives that

$$
\int _ { \mathbb { R } ^ { n } } f ( x ) ( 1 - \eta e ^ { - 2 \pi i x \cdot y } ) d x = 0 .
$$

This implies that $f ( x ) ( 1 - \eta e ^ { - 2 \pi i x \cdot y } ) = 0$ almost everywhere on $\mathbb { R } ^ { n }$ . But, since $y \ne 0$ , we have that $( 1 - \eta e ^ { - 2 \pi i x \cdot y } ) \neq 0$ almost everywhere on $\mathbb { R } ^ { n }$ , and so $f = 0$ almost everywhere on $\mathbb { R } ^ { n }$ . This is a contradiction to the conditions on $f ,$ and so there can not be a $y \ne 0$ with equality holding. Thus we must have for $y \ne 0$ that

$$
\left| { \hat { f } } ( y ) \right| < { \hat { f } } ( 0 ) .
$$

7. Compute the Fourier transform of $g ( x ) = e ^ { - 2 \pi | x | }$ using the following steps:

(a) Let $f \in L ^ { 1 } ( \mathbb { R } )$ and show that

$$
\int _ { \mathbb { R } } f ( x ) d x = \int _ { \mathbb { R } } f \left( x - { \frac { 1 } { x } } \right) d x .
$$

(b) Use part (a) with $f ( x ) = e ^ { - t x ^ { 2 } }$ and $t > 0$ to obtain the following identity:

$$
e ^ { - 2 t } = \frac { 1 } { \sqrt { \pi } } \int _ { 0 } ^ { \infty } e ^ { - y - \frac { t ^ { 2 } } { y } } \frac { d y } { \sqrt { y } } ;
$$

(c) Set $t = \pi \left| x \right|$ and integrate with respect to $e ^ { - 2 \pi i \xi \cdot x } d x$ to obtain that

$$
\widehat g ( \xi ) = \frac { \Gamma ( \frac { n + 1 } { 2 } ) } { \pi ^ { \frac { n + 1 } { 2 } } } \frac { 1 } { ( 1 + | \xi | ^ { 2 } ) ^ { \frac { n + 1 } { 2 } } } .
$$

Solution: Part (a): For one proof, one can check the identity when $f ( x ) = 1 _ { [ 0 , 1 ] } ( x )$ , and then use that simple functions are dense in $L ^ { 1 } ( \mathbb { R } )$ . Here is another proof that one can give. Note that we have

$$
\int _ { \mathbb { R } } f ( x ) d x = \int _ { 0 } ^ { \infty } f ( x ) d x + \int _ { - \infty } ^ { 0 } f ( x ) d x .
$$

We work with each of these integrands separately. For the first one, we have that

$$
\int _ { 0 } ^ { \infty } f ( x ) d x = \int _ { 1 } ^ { \infty } f \left( x - { \frac { 1 } { x } } \right) \left( 1 + { \frac { 1 } { x ^ { 2 } } } \right) d x .
$$

While for the second one, we have

$$
\int _ { - \infty } ^ { 0 } f ( x ) d x = \int _ { - \infty } ^ { - 1 } f \left( x - { \frac { 1 } { x } } \right) \left( 1 + { \frac { 1 } { x ^ { 2 } } } \right) d x .
$$

Now, note that we have

$$
\int _ { \mathbb R } f \left( x - { \frac { 1 } { x } } \right) d x = \int _ { - \infty } ^ { - 1 } f \left( x - { \frac { 1 } { x } } \right) d x + \int _ { - 1 } ^ { 1 } f \left( x - { \frac { 1 } { x } } \right) d x + \int _ { 1 } ^ { \infty } f \left( x - { \frac { 1 } { x } } \right) d x
$$

Using these identities from above, it is easy to see that

$$
\int _ { \mathbb R } f ( x ) d x = \int _ { \mathbb R } f \left( x - { \frac { 1 } { x } } \right) d x + \int _ { | x | > 1 } f \left( x - { \frac { 1 } { x } } \right) { \frac { d x } { x ^ { 2 } } } - \int _ { - 1 } ^ { 1 } f \left( x - { \frac { 1 } { x } } \right) d x .
$$

To conclude the computation, we are left with showing that

$$
\int _ { | x | > 1 } f \left( x - { \frac { 1 } { x } } \right) { \frac { d x } { x ^ { 2 } } } = \int _ { - 1 } ^ { 1 } f \left( x - { \frac { 1 } { x } } \right) d x .
$$

To prove this last identity one shows that

$$
\int _ { 0 } ^ { 1 } f \left( x - { \frac { 1 } { x } } \right) = \int _ { - \infty } ^ { - 1 } f \left( x - { \frac { 1 } { x } } \right) { \frac { d x } { x ^ { 2 } } }
$$

and

$$
\int _ { - 1 } ^ { 0 } f \left( x - { \frac { 1 } { x } } \right) = \int _ { 1 } ^ { \infty } f \left( x - { \frac { 1 } { x } } \right) { \frac { d x } { x ^ { 2 } } }
$$

via a standard change of variables. Part (b): We use part (a) applied to the function $f ( x ) = e ^ { - t x ^ { 2 } }$ . Now observe that

$$
\int _ { \mathbb { R } } e ^ { - t x ^ { 2 } } d x = { \sqrt { \frac { \pi } { t } } } .
$$

But, we also have that

$$
\int _ { \mathbb { R } } e ^ { - t \left( x - { \frac { 1 } { x } } \right) ^ { 2 } } d x = e ^ { 2 t } \int _ { \mathbb { R } } e ^ { - t x ^ { 2 } - t { \frac { 1 } { x ^ { 2 } } } } d x
$$

$$
\quad = \quad { \frac { e ^ { 2 t } } { \sqrt { t } } } \int _ { \mathbb { R } } e ^ { - y ^ { 2 } - { \frac { t ^ { 2 } } { y ^ { 2 } } } } d y
$$

$$
= \ { \frac { e ^ { 2 t } } { \sqrt { t } } } \int _ { 0 } ^ { \infty } e ^ { - u - { \frac { t ^ { 2 } } { u } } } { \frac { d u } { \sqrt { u } } } .
$$

Using Part (a), we have that

$$
\sqrt { \frac { \pi } { t } } = \frac { e ^ { 2 t } } { \sqrt { 2 t } } \int _ { 0 } ^ { \infty } e ^ { - u - \frac { t ^ { 2 } } { u } } \frac { d u } { \sqrt { u } } .
$$

Rearrangement gives the result.

Part (c): Now set $t = \pi \left| x \right|$ in Part (b) and obtain,

$$
e ^ { - 2 \pi | x | } = { \frac { 1 } { \sqrt { \pi } } } \int _ { 0 } ^ { \infty } e ^ { - y - { \frac { \pi ^ { 2 } | x | ^ { 2 } } { y } } } { \frac { d y } { \sqrt { y } } } .
$$

Then integrate this expression with respect to $e ^ { - 2 \pi i x \cdot \xi } d x$ to obtain that

$$
\begin{array} { r l } { \hat { g } ( \xi ) } & { = \displaystyle \int _ { \mathbb { R } ^ { n } } e ^ { - z \pi | z | } e ^ { - z \pi z \cdot | z | } } \\ & { = \displaystyle \int _ { \mathbb { R } ^ { n } } \left( \frac { 1 } { \sqrt { \pi } } \int _ { 0 } ^ { \infty } e ^ { - z \frac { z ^ { 2 } } { \tau } | z | } \frac { \mathrm { d } y } { \sqrt { \pi } } \right) e ^ { - z \pi i z \cdot \xi } d z } \\ & { = \displaystyle \frac { 1 } { \sqrt { \pi } } \int _ { 0 } ^ { \infty } e ^ { - y } \left( \int _ { \mathbb { R } ^ { n } } e ^ { - \frac { z ^ { 2 } } { \tau } | z | ^ { 2 } } e ^ { - z \pi i z \cdot \xi } d z \right) \frac { d y } { \sqrt { \pi } } } \\ & { = \displaystyle \frac { 1 } { \pi ^ { \frac { 1 } { 2 \pi ^ { \frac { 1 } { 2 } } } } } \int _ { 0 } ^ { \infty } e ^ { - y ( 1 | \xi | ^ { 2 } ) } y ^ { \frac { 1 } { \pi } - 1 } d y } \\ & { = \displaystyle \frac { 1 } { \pi ^ { \frac { 1 } { 2 \pi ^ { \frac { 1 } { 2 } } } } } \left( 1 + | \xi | ^ { 2 } \right) ^ { \frac { 1 } { \pi ^ { \frac { 1 } { 2 } } } } \int _ { 0 } ^ { \infty } y ^ { \frac { 1 } { \pi ^ { \frac { 1 } { 2 } } } - \epsilon ^ { - 1 } } d y } \\ & { = \displaystyle \frac { \Gamma ( \frac { 1 + 1 } { 2 \pi } ) } { \pi ^ { \frac { 1 } { 2 \pi ^ { \frac { 1 } { 2 } } } } } \frac { 1 } { \left( 1 + | \xi | ^ { 2 } \right) ^ { \frac { 1 } { \pi ^ { \frac { 1 } { 2 } } } + \frac { 1 } { 2 } } } . } \end{array}
$$