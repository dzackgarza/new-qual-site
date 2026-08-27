# MATH 185: COMPLEX ANALYSIS FALL 2009/10 PROBLEM SET 7 SOLUTIONS

1. Let $\beta \in \mathbb { C } .$

(a) Show that for all $n = 0 , 1 , 2 , \ldots$

$$
\left( \frac { \beta ^ { n } } { n ! } \right) ^ { 2 } = \frac { 1 } { 2 \pi i } \int _ { \partial D ( 0 , 1 ) } \frac { \beta ^ { n } e ^ { \beta z } } { n ! z ^ { n + 1 } } d z .
$$

Solution. Applying generalized Cauchy’s integral formula, we get

$$
\frac { 1 } { 2 \pi i } \int _ { \partial D ( 0 , 1 ) } \frac { \beta ^ { n } e ^ { \beta z } } { n ! z ^ { n + 1 } } d z = \frac { \beta ^ { n } } { n ! } \left[ \frac { 1 } { 2 \pi i } \int _ { \partial D ( 0 , 1 ) } \frac { e ^ { \beta z } } { z ^ { n + 1 } } d z \right] = \frac { \beta ^ { n } } { n ! } \times \frac { 1 } { n ! } \frac { d ^ { n } } { d z ^ { n } } e ^ { \beta z } \bigg | _ { z = 0 } = \left( \frac { \beta ^ { n } } { n ! } \right) ^ { 2 } .
$$

(b) Show that

$$
\sum _ { n = 0 } ^ { \infty } \left( { \frac { \beta ^ { n } } { n ! } } \right) ^ { 2 } = { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } e ^ { 2 \beta \cos \theta } d \theta .
$$

[Hint: Consider power series expansion of $e ^ { \beta / z }$ and apply (a) on $z ^ { - 1 } e ^ { \beta ( z + 1 / z ) } . \big$ Solution. Note that

$$
e ^ { \beta / z } = \sum _ { n = 0 } ^ { \infty } { \frac { \beta ^ { n } } { n ! z ^ { n } } } .
$$

Multiplying by $e ^ { \beta z }$ and dividing by $z ,$ we get

$$
{ \frac { 1 } { z } } e ^ { \beta ( z + 1 / z ) } = \sum _ { n = 0 } ^ { \infty } { \frac { \beta ^ { n } e ^ { \beta z } } { n ! z ^ { n + 1 } } } .
$$

Integrating about $\partial D ( 0 , 1 )$ and using (a), we get

$$
\frac { 1 } { 2 \pi i } \int _ { \partial D ( 0 , 1 ) } \frac { 1 } { z } e ^ { \beta ( z + 1 / z ) } d z = \sum _ { n = 0 } ^ { \infty } \frac { \beta ^ { n } } { n ! } \left[ \frac { 1 } { 2 \pi i } \int _ { \partial D ( 0 , 1 ) } \frac { e ^ { \beta z } } { z ^ { n + 1 } } d z \right] = \sum _ { n = 0 } ^ { \infty } \left( \frac { \beta ^ { n } } { n ! } \right) ^ { 2 }
$$

Evaluating the line integral about the path $z : [ 0 , 2 \pi ] \to \mathbb { C } , z ( \theta ) = e ^ { i \theta }$ and noting that $e ^ { i \theta } + e ^ { - i \theta } = 2$ cos θ we get

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \partial D ( 0 , 1 ) } { \frac { 1 } { z } } e ^ { \beta ( z + 1 / z ) } d z = { \frac { 1 } { 2 \pi i } } \int _ { 0 } ^ { 2 \pi } e ^ { 2 \beta \cos \theta } d \theta .
$$

2. Let $f : \mathbb { C } \to \mathbb { C }$ be an entire function. Let $a \in \mathbb { R }$ be an arbitrary constant.

(a) Show that if Re $f ( z ) \leq a$ for all $z \in \mathbb { C }$ , then f is constant.

(b) Show that if Re $f ( z ) \geq a$ for all $z \in \mathbb { C } .$ , then f is constant.

(c) Show that i $\mathrm { ~ f ~ } [ \operatorname { R e } f ( z ) ] ^ { 2 } \leq [ \operatorname { I m } f ( z ) ] ^ { 2 }$ for all $z \in \mathbb { C }$ , then f is constant.

(d) Show that if $[ \mathrm { R e } f ( z ) ] ^ { 2 } \geq [ \mathrm { I m } f ( z ) ] ^ { 2 }$ for all $z \in \mathbb { C } .$ , then f is constant.

(e) Suppose h is another entire functions and suppose there exists an $a \in \mathbb { R } , a > 0$ , such that Re $f ( z ) \leq a \operatorname { R e } h ( z ) $ for all $z \in \mathbb { C }$ . Show that there exist $\alpha , \beta \in \mathbb { C }$ such that

$$
f ( z ) = \alpha h ( z ) + \beta
$$

for all $z \in \mathbb { C } .$

[Hint: if f and g are both entire, then so are $f \circ g$ and $g \circ f ;$ find an appropriate g so that you may apply Liouville’s theorem.]

Solution. Note that $e ^ { x }$ is a monotone increasing function on $\mathbb { R }$ .

• For (a), we choose $g ( z ) = e ^ { z }$ and note that $| e ^ { \overleftarrow { f } ( z ) } | = | e ^ { \mathrm { R e } f ( z ) } e ^ { i \mathrm { I m } f ( z ) } | = e ^ { \mathrm { R e } f ( z ) } \leq e ^ { a }$

• For (c), we choose $g ( z ) = e ^ { z ^ { 2 } }$ and note that $| e ^ { f ( z ) ^ { 2 } } | = | e ^ { [ \mathrm { R e } f ( z ) ] ^ { 2 } - [ \mathrm { I m } \dot { f } ( z ) ] ^ { 2 } } e ^ { 2 i \mathrm { R e } f ( z ) \mathrm { I m } f ( z ) } | =$ $e ^ { [ \mathrm { R e } f ( z ) ] ^ { 2 } - [ \mathrm { I m } f ( z ) ] ^ { 2 } } \leq e ^ { 0 } = 1$

Applying Liouville’s theorem then implies that $e ^ { f ( z ) } , e ^ { f ( z ) ^ { 2 } }$ are constant functions. To show that f must also be a constant function, we differentiate $e ^ { f ( z ) }$ to get

$$
0 = ( e ^ { f ( z ) } ) ^ { \prime } = f ^ { \prime } ( z ) e ^ { f ( z ) } .
$$

Since $e ^ { f ( z ) }$ is never zero, we get $f ^ { \prime } ( z ) = 0$ and so f must be a constant function in (a). The same argument shows for (c) that $f ^ { 2 }$ must be a constant function and therefore f must be a constant function (since it is continuous). (b) could be deduced from (a) and (d) could be deduced from from (c) by applying (a) and (c) to −f. For (e), we just apply (a) to the entire function $f - a h$ which by assumption satisfies Re f(z) − a Re $h ( z ) \leq 0$ for all $z \in \mathbb { C }$

3. Let $f : \mathbb { C } \to \mathbb { C }$ be an entire function.

(a) Suppose there exists $\alpha , \beta \in \mathbb { C } ^ { \times }$ such that $\alpha / \beta \notin \mathbb { R }$ . Show that if f satisfies the following conditions

$$
f ( z + \alpha ) = f ( z ) , \quad f ( z + \beta ) = f ( z )
$$

for all $z \in \mathbb { C }$ , then $f$ is constant.

Solution. Given any real number $x \in \mathbb { R }$ , we will write $[ x ]$ for the integral part of x and hxi for the fractional part of x. For example $[ - 5 . 1 2 ] = - 5$ and $\langle - 5 . 1 2 \rangle = 0 . 1 2$ . Note that $[ x ] \in \mathbb { Z } , \langle x \rangle \in [ 0 , 1 )$ , and $x = [ x ] + \langle x \rangle$ for all $x \in \mathbb { R }$ . The condition $\alpha / \beta \notin$ R implies that $\alpha , \beta$ span C as a real vector space of dimension 2. In other words, any $z \in \mathbb { C }$ may be written as $z = x \alpha + y \beta$ where $x , y \in \mathbb { R }$ . Observe that the two conditions given may be applied recursively to obtain

$$
\begin{array} { r l } & { f ( z ) = f ( x \alpha + y \beta ) } \\ & { \qquad = f ( \alpha \langle { x } \rangle + \beta \langle { y } \rangle + \alpha [ x ] + \beta [ y ] ) } \\ & { \qquad = f ( \alpha \langle { x } \rangle + \beta \langle { y } \rangle ) . } \end{array}
$$

for any $z = x \alpha + y \beta \in \mathbb { C }$ . Note that for any $z = x \alpha + y \beta \in \mathbb { C } , \alpha \langle x \rangle + \beta \langle y \rangle \in [ 0 , \alpha ) \times [ 0 , \beta ) \subseteq$ $[ 0 , \alpha ] \times [ 0 , \beta ]$ , ie. the closed parallelogram bounded by the line segments from 0 to α and 0 to $\beta$ and this is compact, and so

$$
\operatorname* { s u p } _ { z \in \mathbb { C } } | f ( z ) | = \operatorname* { s u p } _ { z \in [ 0 , \alpha ) \times [ 0 , \beta ) } | f ( z ) | \leq \operatorname* { m a x } _ { z \in [ 0 , \alpha ] \times [ 0 , \beta ] } | f ( z ) | .
$$

The last term is finite by the Extreme Value Theorem in Math 104 (since $[ 0 , \alpha ] \times [ 0 , \beta ]$ is compact and $f$ is analytic, therefore continuous) and so $f$ is bounded. Liouville’s theorem then implies that f is constant.

(b) Suppose

$$
\operatorname* { l i m } _ { | z | \to \infty } { \frac { f ( z ) } { z } } = 0 .
$$

Show that f is a constant function.

Solution. Define $g : \mathbb { C } \to \mathbb { C }$ by

$$
g ( z ) : = { \left\{ \begin{array} { l l } { { \underline { { f ( z ) - f ( 0 ) } } } } & { { z \neq 0 , } } \\ { { z - 0 } } & { { z = 0 . } } \end{array} \right. }
$$

By Corollary 4.4, g is an entire function too. Now,

$$
\operatorname* { l i m } _ { | z | \to \infty } | g ( z ) | = \operatorname* { l i m } _ { | z | \to \infty } \left| { \frac { f ( z ) } { z } } \right| = 0 .
$$

Let $\varepsilon > 0$ . Then there exists $R > 0$ such that

$$
| g ( z ) | < \varepsilon
$$

for all $| z | \geq R$ . In particular, $| g ( z ) | < \varepsilon$ for all $z \in \partial D ( 0 , R )$ . Applying maximum modulus theorem (or Corollary 4.15), we get

$$
\operatorname* { m a x } _ { z \in D ( 0 , R ) } | g ( z ) | = \operatorname* { m a x } _ { z \in \partial D ( 0 , R ) } | g ( z ) | \leq \varepsilon .
$$

Therefore $| g ( z ) | \leq \varepsilon$ for all $z \in \mathbb { C } .$ . Since $\varepsilon$ is arbitrary, we conclude that

$$
g ( z ) = 0
$$

for all $z \in \mathbb { C }$ . Hence $f ( z ) = f ( 0 )$ for all $z \in \mathbb { C }$ and so f is a constant function.

(a) Find all entire functions f that satisfy

$$
f ^ { \prime \prime } \left( { \frac { 1 } { n } } \right) + f \left( { \frac { 1 } { n } } \right) = 0
$$

for all $n \in \mathbb { N } .$

Solution. Note that if $f$ is an entire function, then so is $f ^ { \prime \prime }$ . In particular, $f ^ { \prime \prime } + f$ is continuous and so

$$
f ^ { \prime \prime } ( 0 ) + f ( 0 ) = \operatorname* { l i m } _ { n \to \infty } \left[ f ^ { \prime \prime } \left( { \frac { 1 } { n } } \right) + f \left( { \frac { 1 } { n } } \right) \right] = 0 .
$$

Hence $f ^ { \prime \prime } + f$ is zero on a subset of $\mathbb { C }$ with limit points, namely, $\{ n ^ { - 1 } \mid n \in \mathbb { N } \} \cup \{ 0 \}$ and thus by the uniqueness theorem, $f ^ { \prime \prime } + f \equiv 0$ on the whole of C. Now since $f$ is entire, its Taylor series expansion about 0 that converges everywhere in $\mathbb { C } ,$ and is given by

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } \frac { f ^ { ( n ) } ( 0 ) } { n ! } z ^ { n } .
$$

Likewise for $f ^ { \prime \prime }$ , we have

$$
f ^ { \prime \prime } ( z ) = \sum _ { n = 0 } ^ { \infty } { \frac { f ^ { ( n + 2 ) } ( 0 ) } { n ! } } z ^ { n } .
$$

Hence, for all $z \in \mathbb { C }$

$$
f ^ { \prime \prime } ( z ) + f ( z ) = \sum _ { n = 0 } ^ { \infty } \left[ \frac { f ^ { ( n + 2 ) } ( 0 ) } { n ! } + \frac { f ^ { ( n ) } ( 0 ) } { n ! } \right] z ^ { n } .
$$

Now since $f ^ { \prime \prime } + f \equiv 0$ , we must have $f ^ { ( n + 2 ) } ( 0 ) = - f ^ { ( n ) } ( 0 )$ for all $n \in \mathbb { N } \cup \{ 0 \}$ , ie.

$$
f ( 0 ) = - f ^ { \prime \prime } ( 0 ) = \cdots = ( - 1 ) ^ { n } f ^ { ( 2 n ) } ( 0 ) = \cdots { } .
$$

$$
f ^ { \prime } ( 0 ) = - f ^ { \prime \prime \prime } ( 0 ) = \cdots = ( - 1 ) ^ { n } f ^ { ( 2 n + 1 ) } ( 0 ) = \cdots . .
$$

Hence

$$
\begin{array} { l } { f ( z ) = \displaystyle \sum _ { n = 0 } ^ { \infty } \frac { f ^ { ( n ) } ( 0 ) } { n ! } z ^ { n } } \\ { = f ( 0 ) \displaystyle \sum _ { n = 0 } ^ { \infty } \frac { ( - 1 ) ^ { n } } { ( 2 n ) ! } z ^ { 2 n } + f ^ { \prime } ( 0 ) \displaystyle \sum _ { n = 0 } ^ { \infty } \frac { ( - 1 ) ^ { n } } { ( 2 n + 1 ) ! } z ^ { 2 n + 1 } } \\ { = f ( 0 ) \cos z + f ^ { \prime } ( 0 ) \sin z . } \end{array}
$$

Note that the ‘splitting’ of the first power series into a sum of two power series is permissible because all three series have infinite radius of convergence. Hence an entire function that satisfies the given condition must be of the form

$$
f ( z ) = f ( 0 ) \cos z + f ^ { \prime } ( 0 ) \sin z .
$$

(b) Let $n \in \mathbb { N }$ and $n \geq 2$ . Find all entire functions f that satisfy

$$
f ( z ^ { n } ) = [ f ( z ) ] ^ { n }
$$

for all $z \in \mathbb { C }$

Solution. By Theorem 4.3, f has a power series expansion

$$
f ( z ) = \sum _ { m = 0 } ^ { \infty } a _ { m } z ^ { m }
$$

with infinite radius of convergence. By the given condition

$$
a _ { 0 } = f ( 0 ) = f ^ { n } ( 0 ) = a _ { 0 } ^ { n }
$$

and so either $a _ { 0 } = 0$ or $a _ { 0 } = e ^ { \frac { 2 p \pi i } { n - 1 } }$ for some $p \in \{ 1 , \ldots , n - 1 \}$

Case I. Suppose $a _ { 0 } = e ^ { \frac { 2 p \pi i } { n - 1 } }$ for some $p \in \{ 1 , \ldots , n - 1 \}$ and f is non-constant. Let $k \in \mathbb N$ be the smallest positive number such $a _ { k } \neq 0$ . Hence

$$
f ( z ^ { n } ) = 1 + a _ { k } z ^ { k n } + \mathrm { h i g h e r ~ o r d e r ~ t e r m s }
$$

and

$$
[ f ( z ) ] ^ { n } = 1 + n a _ { k } z ^ { k } + \mathrm { h i g h e r ~ o r d e r ~ t e r m s } .
$$

Since $f ( z ^ { n } ) = [ f ( z ) ] ^ { n }$ , comparing coefficients tells us that $n a _ { k } = 0$ and so $a _ { k } = 0 - \mathrm { ~ a ~ }$ contradiction. In other words, if $\smash { a _ { 0 } = e ^ { \frac { 2 p \pi i } { n - 1 } } }$ for some $p \in \{ 1 , \ldots , n - 1 \}$ , then f must be a constant function. Hence $f ( z ) = a _ { 0 } = e ^ { \frac { - r ^ { n } } { n - 1 } }$ for all $z \in \mathbb { C }$

Case II. Suppose $a _ { 0 } = 0$ and f is non-constant. Again we let k be as above and observe that

$$
f ( z ) = z ^ { k } [ a _ { k } + a _ { k + 1 } z + a _ { k + 2 } z ^ { 2 } + \cdot \cdot \cdot ] = : z ^ { k } g ( z ) .
$$

Note that g and f must have the same radii of convergence since

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { \mathbf { \alpha } } \sqrt [ n ] { | a _ { n } | } = \operatorname* { l i m } _ { n \to \infty } \mathbf { \alpha } \sqrt [ n ] { | a _ { n + k } | }
$$

and hence g is also an entire function. Also $f ( z ^ { n } ) = [ f ( z ) ] ^ { n }$ implies

$$
z ^ { n k } g ( z ^ { n } ) = z ^ { n k } [ g ( z ) ] ^ { n }
$$

and so $g ( z ^ { n } ) = [ g ( z ) ] ^ { n }$ . In other words, g satisfies the conditions of Case I. Hence g is a constant function and $g ( z ) = e ^ { \frac { 2 p \pi i } { n - 1 } }$ for some $p \in \{ 1 , \ldots , n - 1 \}$ . Therefore $f ( z ) = e ^ { \frac { 2 p \pi i } { n - 1 } } z ^ { k }$ for all $z \in \mathbb { C } .$

Combining Cases I and II, we see that an entire function that satisfies the given condition must be of the form $f ( z ) = e ^ { \frac { 2 p \pi i } { n - 1 } } z ^ { k }$ for $k = 0 , 1 , 2 , . . .$ . and $p \in \{ 1 , \ldots , n - 1 \}$ .

4. Let $\Omega \subseteq \mathbb { C }$ be a region. Let f be analytic on Ω and let $z _ { 0 } \in \Omega$ . Suppose $f ^ { \prime } ( z _ { 0 } ) \neq 0$ . Show that there is an $r > 0$ such that

$$
\int _ { \Gamma } { \frac { f ^ { \prime } ( z _ { 0 } ) } { f ( z ) - f ( z _ { 0 } ) } } d z = 2 \pi i
$$

where $\Gamma = \partial D ( z _ { 0 } , r )$

Solution. We know that there is an $R > 0$ such that f has a Taylor series expansion about $z _ { \mathrm { 0 } }$ . So

$$
f ( z ) = f ( z _ { 0 } ) + a _ { 1 } ( z - z _ { 0 } ) + \sum _ { n = 2 } ^ { \infty } a _ { n } ( z - z _ { 0 } ) ^ { n }
$$

holds for all $z ~ \in ~ D ( z _ { 0 } , R )$ . Now since $a _ { 1 } ~ = ~ f ^ { \prime } ( z _ { 0 } ) ~ \neq ~ 0$ and since $f ^ { \prime }$ is continuous at $z _ { 0 } .$ there is an $\delta > 0$ such that $f ( z ) - f ( z _ { 0 } ) \neq 0$ for all $z \in D ( z _ { 0 } , \delta ) \backslash \{ z _ { 0 } \}$ (if not, we can find a sequence $z _ { n }  z _ { 0 } , z _ { n } \neq z _ { 0 }$ , such that $f ( z _ { n } ) - f ( z _ { 0 } ) = 0$ for all $n \in \mathbb { N } -$ this will imply that $0 = \mathrm { l i m } _ { n  \infty } ( f ( z _ { n } ) - f ( z _ { 0 } ) ) / ( z _ { n } - z _ { 0 } ) = f ^ { \prime } ( z _ { 0 } )$ , a contradiction). Let $r = \operatorname* { m i n } \{ R , \delta \}$ and let the function $g : D ( z _ { 0 } , r ) \to \mathbb { C }$ be defined by

$$
g ( z ) = { \left\{ \begin{array} { l l } { { \displaystyle { \frac { f ( z ) - f ( z _ { 0 } ) } { z - z _ { 0 } } } } } & { z \neq z _ { 0 } , } \\ { { \displaystyle f ^ { \prime } ( z _ { 0 } ) } } & { z = z _ { 0 } . } \end{array} \right. }
$$

Now observe that g is analytic in $D ( z _ { 0 } , r )$ by a result in the lectures. Furthermore, g is non-zero on $D ( z _ { 0 } , r )$ . Hence the function $h : D ( z _ { 0 } , r ) \to \mathbb { C }$ defined by

$$
h ( z ) = { \frac { 1 } { g ( z ) } }
$$

is analytic on $D ( z _ { 0 } , r )$ . Cauchy’s integral formula applied to h yields

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \Gamma } { \frac { h ( z ) } { z - z _ { 0 } } } d z = h ( z _ { 0 } )
$$

but since

$$
h ( z ) = \left\{ { \begin{array} { l l } { \displaystyle { \frac { z - z _ { 0 } } { f ( z ) - f ( z _ { 0 } ) } } } & { z \neq z _ { 0 } , } \\ { \displaystyle { \frac { 1 } { f ^ { \prime } ( z _ { 0 } ) } } } & { z = z _ { 0 } , } \end{array} } \right.
$$

we get

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \Gamma } { \frac { 1 } { f ( z ) - f ( z _ { 0 } ) } } d z = { \frac { 1 } { f ^ { \prime } ( z _ { 0 } ) } }
$$

and thus

$$
\int _ { \Gamma } { \frac { f ^ { \prime } ( z _ { 0 } ) } { f ( z ) - f ( z _ { 0 } ) } } d z = 2 \pi i
$$

as required.