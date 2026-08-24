$\begin{array} { r } { g = \sum _ { k = 1 } ^ { N } \alpha _ { k } \chi _ { ( a _ { k } , b _ { k } ] } } \end{array}$ . Then we have (with the convention that $F _ { n } ( \infty ) = 1$ and $F _ { n } ( - \infty ) = 0 )$

$$
\begin{array} { l l l } { \displaystyle \left. \int g d \mu _ { n } - \int g d \mu _ { m } \right. } & { = } & { \displaystyle \left. \sum _ { k = 1 } ^ { N } \alpha _ { k } ( F _ { n } ( b _ { k } ) - F _ { n } ( a _ { k } ) ) - \sum _ { k = 1 } ^ { N } \alpha _ { k } ( F _ { m } ( b _ { k } ) - F _ { m } ( a _ { k } ) ) \right. } \\ { \displaystyle } & { \leqslant } & { \displaystyle \sum _ { k = 1 } ^ { N } \vert \alpha _ { k } \vert \left( \vert F _ { n } ( b _ { k } ) - F _ { m } ( b _ { k } ) \vert + \vert F _ { n } ( b _ { k } ) - F _ { n } ( a _ { k } ) \vert \right) . } \end{array}
$$

Fix $\epsilon > 0$ . Since the sequence $\left\{ F _ { n } \right\}$ converges uniformly, pick $n , m$ big enough so that ş $| | F _ { n } - F _ { m } | | _ { L ^ { \infty } } <$ $\epsilon / ( 2 \sum | \alpha _ { k } | )$ . Then the above estimate implies that for all such ş $n , m ,$ , we have $|  \int g d \mu _ { n } - \int g d \mu _ { m } | < \overline { { { \epsilon } } } .$ So the numbers $\left\{ \int g d \mu _ { n } \right\}$ form a Cauchy sequence in R and therefore converge.
This establishes the result for elements of $\mathcal { F }$

Now let $f$ be any bounded continuous function $\mathbb { R }  \mathbb { R }$ On any compact interval, f can be approximated in the $L ^ { \infty }$ norm by functions in ${ \mathcal F } .$ So just work on a compact interval that is big enough so that almost all of the mass of the $\mu _ { n }$ is inside that interval (this can be made precise using the fact that the $F _ { n }$ converge uniformly on R, but I don’t have time to write it down right now).
Fix $\epsilon > 0$ and pick $g \in { \mathcal { F } }$ such that $| | f - g | | _ { L ^ { \infty } } < \epsilon .$ Then for n, m big enough, we have

$$
\begin{array} { r c l } { { \displaystyle \left| \int f d \mu _ { n } - \int f d \mu _ { m } \right| ~ \leqslant } } & { { \displaystyle \left| \int f d \mu _ { n } - \int g d \mu _ { n } \right| + \left| \int g d \mu _ { n } - \int g d \mu _ { m } \right| + \displaystyle \left| \int g d \mu _ { m } - \int f d \mu _ { m } \right| } } \\ { { \displaystyle \leqslant } } & { { \displaystyle \int | f - g | d \mu _ { n } + \int | f - g | d \mu _ { m } + \epsilon } } \\ { { \displaystyle \leqslant } } & { { \displaystyle \epsilon \mu _ { n } ( \mathbb R ) + \epsilon \mu _ { m } ( \mathbb R ) + \epsilon ~ = ~ 3 \epsilon , } } \end{array}
$$

which establishes the desired result.

Problem 4. Consider the Banach space $V = C ( [ - 1 , 1 ] )$ of all real-valued continuous functions on $[ - 1 , 1 ]$ equipped with the supremum norm.
Let $B = \{ f \in V : \| f \| _ { L ^ { \infty } } \leqslant 1 \}$ be the closed unit ball in V . Show that there exists a bounded linear functional $\Lambda : V \to$ R such that ΛpBq is an open subset of R.

Solution.
Define $\Lambda : V \to \mathbb { R }$ by

$$
\Lambda ( f ) ~ = ~ - \int _ { - 1 } ^ { 0 } f ( x ) d x + \int _ { 0 } ^ { 1 } f ( x ) d x .
$$

It is clear that $| \Lambda ( f ) | \leqslant 2 \left| | f | \right| _ { L ^ { \infty } }$ for all $f \in V$ , so Λ is a bounded linear functional.
Since Λ is continuous and B is a connected set, $\Lambda ( B )$ is a connected subset of R and is therefore an interval.
We claim that $\Lambda ( B )$ is the open interval p´2, 2q.

Let $f _ { n }$ be the function which is equal to ´1 for $x \in [ - 1 , - 1 / n ]$ , equal to 1 for $x \in [ 1 / n , 1 ]$ , and linear on $[ - 1 / n , 1 / n ]$ Note that each $f _ { n } \in B$ , and we calculate $\Lambda ( f _ { n } ) = 2 - 1 / n$ . Since $\Lambda ( B )$ is an interval in R, this implies that $( - 2 , 2 ) \subseteq \Lambda ( B )$ . We now just need to check that Λ never achieves the values ˘2. But note that we have $\vert \Lambda ( f ) \vert \leqslant \int _ { - 1 } ^ { 1 } \vert f ( x ) \vert d x \leqslant 2$ But the second inequality is strict for all f which are not identically $\pm 1$ Since $\Lambda ( \pm 1 ) = 0$ , this shows that in fact the strict inequality $| \Lambda ( f ) | < 2$ holds for all $f \in B$ , so we conclude that $\Lambda ( B ) = ( - 2 , 2 )$ □

Problem 5. Suppose $f : \mathbb { R } \to \mathbb { R }$ is a bounded and measurable function satisfying $f ( x + 1 ) \ = \ f ( x )$ and $f ( 2 x ) = f ( x )$ for almost every $x \in \mathbb { R }$ . Show that then there exists a constant $c \in \mathbb { R }$ such that $f ( x ) = c$ for almost every $x \in \mathbb { R }$

Solution.
Let Z be the measure zero set of bad points for which the given property doesn’t hold.
Let $\tilde { Z }$ be the set of all points in R which are reachable from a point in $Z$ by a finite sequence of the operations $x \mapsto x + 1 , x \mapsto x - 1 , x \mapsto 2 x , { \mathrm { o r ~ } } x \mapsto x / 2$ . Then $\tilde { Z }$ is just a countable union of translates and dilates of $Z ,$ so $\tilde { Z }$ also has measure zero.
We will show that f is constant on the complement of $\widetilde { Z } .$ By construction of ${ \tilde { Z } } ,$ for any $x \notin \widetilde { Z }$ we have $2 ^ { - n } ( 2 ^ { n } x + 1 + 2 ^ { n } m ) = x + m + 2 ^ { - n } \not \in \widetilde { Z }$ for all integers $n , m$ . Let $Q$ be the set of numbers of the form $m + 2 ^ { - n }$ for n, m P Z.

Let $x _ { 0 } , y _ { 0 } \notin \widetilde { Z }$ and fix $\epsilon > 0$ . Since f is bounded, it is locally integrable.
Therefore by the Lebesgue differentiation theorem we can pick $r > 0$ such that

$$
\left| f ( x _ { 0 } ) - \frac { 1 } { 2 r } \int _ { x _ { 0 } - r } ^ { x _ { 0 } + r } f ( t ) d t \right| \ < \ \epsilon , \qquad \left| f ( y _ { 0 } ) - \frac { 1 } { 2 r } \int _ { y _ { 0 } - r } ^ { y _ { 0 } + r } f ( t ) d t \right| \ < \ \epsilon .
$$

Also, since $f$ is bounded we can find $\delta > 0$ such that for any set $A \subseteq \mathbb { R } , \lambda ( A ) < \delta$ implies $\int _ { A } \left| f ( t ) \right| d t < \epsilon r$ (here λ denotes Lebesgue measure).
We can pick a number $q \in Q$ such that $| ( x _ { 0 } + q ) - y _ { 0 } | { \overset { \cdot } { < } } \delta / 2$ 2. Then, since $f ( t + q ) = f ( t )$ for all $t \not \in \tilde { Z }$ , which is almost every t, we have the estimate

$$
\begin{array} { r l } { \displaystyle \left. \frac { 1 } { 2 r } \int _ { x _ { 0 } - r } ^ { x _ { 0 } + r } f ( t ) d t - \frac { 1 } { 2 r } \int _ { y _ { 0 } - r } ^ { y _ { 0 } + r } f ( t ) d t \right. ~ = ~ \displaystyle \frac { 1 } { 2 r } \displaystyle \left. \int _ { x _ { 0 } + q - r } ^ { x _ { 0 } + q + r } f ( t ) d t - \int _ { y _ { 0 } - r } ^ { y _ { 0 } + r } f ( t ) d t \right. } & { } \\ { ~ = ~ \displaystyle \frac { 1 } { 2 r } \displaystyle \left. \int _ { \left[ x _ { 0 } + q - r , x _ { 0 } + q + r \right] \Delta [ y _ { 0 } - r , y _ { 0 } + r ] } f ( t ) d t \right. ~ < ~ \epsilon / 2 . } \end{array}
$$

So combining the above three inequalities with the triangle inequality gives $| f ( x _ { 0 } ) - f ( y _ { 0 } ) | < ( 2 + 1 / 2 ) \epsilon$ , and taking $\epsilon \to 0$ shows that $f ( x _ { 0 } ) = f ( y _ { 0 } )$ , so f is constant on the complement of $\tilde { Z } . \ \sqcap$

Alternative Solution.
Let E be the measure zero set on which $f ( x ) \ \ne \ f ( 2 x )$ Then $f ( x ) ~ = ~ f ( 2 x )$ for all $x \in E ^ { c }$ , and so $f ( 2 ^ { k } x ) = f ( x )$ for all $x \in E ^ { c }$ and $k \in \mathbb N$ . Since we are only trying to show that $f$ is constant almost everywhere, we can discard E. So, we can suppose $f ( 2 ^ { k } x ) = f ( x )$ for all $x .$ . Moreover, $f ( x + 1 ) = f ( x )$ for almost all x means $f$ can be considered as a function on $S ^ { 1 } = \mathbb { R } / \mathbb { Z } = [ 0 , 1 )$ As a bounded measurable function on $S ^ { 1 } , f$ is in $L ^ { 1 } ( S ^ { 1 } )$ , and so has Fourier coefficients ${ \hat { f } } ( k )$ for all $k \in \mathbb { Z }$ . An elementary theorem says that $L ^ { 1 } ( S ^ { 1 } )$ functions are determined by their Fourier coefficients.
Therefore, to show $f$ is constant, it is enough to show that every nonzero Fourier coefficient of $f$ vanishes (since then $f$ will have the same Fourier coefficients as the constant function $x \mapsto { \hat { f } } ( 0 ) )$ ).

Now, for any $k \in \mathbb { N } .$ , and any $n \in \mathbb { Z } .$

$$
\begin{array} { l } { { \displaystyle \hat { f } ( n ) = \int _ { 0 } ^ { 1 } f ( x ) e ^ { - 2 \pi n i x } d x } } \\ { { \displaystyle \quad = \int _ { 0 } ^ { 1 } f ( 2 ^ { k } x ) e ^ { - 2 \pi n i x } d x } } \\ { { \displaystyle \quad = 2 ^ { - k } \int _ { 0 } ^ { 2 ^ { k } } f ( y ) e ^ { - 2 \pi i n 2 ^ { - k } y } d y } } \\ { { \displaystyle \quad = 2 ^ { - k } \sum _ { j = 0 } ^ { 2 ^ { k - 1 } } \int _ { 0 } ^ { 1 } f ( y ) e ^ { - 2 \pi i n 2 ^ { - k } ( y + j ) } d y } } \\ { { \displaystyle \quad = c _ { k , n } \cdot 2 ^ { - k } \int _ { 0 } ^ { 1 } f ( y ) e ^ { - 2 \pi i n 2 ^ { - k } y } d y , } } \end{array}
$$

where $c _ { k , n }$ is the constant

$$
c _ { k , n } = \sum _ { j = 0 } ^ { 2 ^ { k } - 1 } e ^ { - 2 \pi i n 2 ^ { - k } j } .
$$

But, if $n 2 ^ { - k }$ is not an integer, then

$$
c _ { k , n } = { \frac { ( e ^ { - 2 \pi i n 2 ^ { - k } } ) ^ { 2 ^ { k } } - 1 } { e ^ { - 2 \pi i n 2 ^ { - k } } - 1 } } = { \frac { e ^ { - 2 \pi i n } - 1 } { e ^ { - 2 \pi i n 2 ^ { - k } } - 1 } } = 0 ,
$$

and so ${ \hat { f } } ( n ) = 0$ in this case.
But $\mathrm { i f } \ n \neq 0$ , then of course there is some k P N with $n 2 ^ { - k } \notin \mathbb { Z }$ . Consequently ${ \hat { f } } ( n ) = 0 { \mathrm { ~ i f ~ } } n \neq 0$ , which completes the proof.

Problem 6. Let $f \in L ^ { 2 } ( \mathbb { C } )$ . For $z \in \mathbb { C }$ we define

$$
g ( z ) ~ = ~ \int _ { \{ w \in \mathbb { C } : | w - z | \leqslant 1 \} } { \frac { | f ( w ) | } { | z - w | } } d A ( w )
$$

where dA denotes integrations with respect to Lebesgue measure on C. Show that then $| g ( z ) | < \infty$ for almost every $z \in \mathbb { C }$ and that $g \in L ^ { 2 } ( \mathbb { C } )$

Solution.
Let $C = \int _ { | u | \leqslant 1 } { \frac { 1 } { | u | } } d A ( u ) < \infty$ . We have

$$
\begin{array} { r l r } { | g ( z ) | ^ { 2 } = } & { \left( \displaystyle \int _ { | w - z | \leqslant 1 } \frac { | f ( w ) | } { | w - z | } d A ( w ) \right) ^ { 2 } \leqslant } & { \left( \displaystyle \int _ { | w - z | \leqslant 1 } \frac { | f ( w ) | ^ { 2 } } { | w - z | } d A ( w ) \right) \left( \displaystyle \int _ { | w - z | \leqslant 1 } \frac { 1 } { | w - z | } d A ( w ) \right) \quad \mathrm { b y ~ C a u c h y - S c h w a r z } } \\ { \leqslant } & { C \cdot \displaystyle \int _ { | w - z | \leqslant 1 } \frac { | f ( w ) | ^ { 2 } } { | w - z | } d A ( w ) . } \end{array}
$$

Therefore we can estimate

$$
\begin{array} { r c l } { { \displaystyle \int _ { \mathbb C } | g ( z ) | ^ { 2 } d A ( z ) \ \leqslant \ C \int _ { \mathbb C } \displaystyle \int _ { | w - z | \leqslant 1 } \displaystyle \frac { | f ( w ) | ^ { 2 } } { | w - z | } d A ( w ) d A ( z ) } } \\ { { \displaystyle \leqslant \ C \int _ { \mathbb C } | f ( w ) | ^ { 2 } \displaystyle \int _ { | z - w | \leqslant 1 } \displaystyle \frac { 1 } { | z - w | } d A ( z ) d A ( w ) } } & { { \mathrm { b y ~ T o n e l i } } } \\ { { \displaystyle \leqslant \ C ^ { 2 } \| f \| _ { L ^ { 2 } ( \mathbb C ) } ^ { 2 } \ < \ \infty . } } \end{array}
$$

This shows both that $| g ( z ) | < \infty$ for almost every $z \in \mathbb { C }$ and $g \in L ^ { 2 } ( \mathbb { C } )$

Problem 7. Prove that there exists a meromorphic function f on C with the following properties.

1. $f ( z ) = 0$ if and only ${ \mathrm { i f ~ } } z \in \mathbb { Z }$

2. $f ( z ) = \infty$ if and only ${ \mathrm { i f ~ } } z - 1 / 3 \in \mathbb { Z } .$

3. $| f ( x + i y ) | \leqslant 1$ for all $x \in \mathbb { R }$ and all $y \in \mathbb { R }$ with $| y | \geqslant 1$

Solution.
Let $\begin{array} { r } { f ( z ) = \frac { 1 } { 2 } \frac { \sin ( \pi z ) } { \sin ( \pi ( z - 1 / 3 ) ) } } \end{array}$ . It’s clear that f is meromorphic with $f ( z ) = 0$ if and only if $z \in \mathbb { Z }$ and $f ( z ) = \infty$ if and only i ${ \mathrm { ~ f ~ } } z - 1 / 3 \in \mathbb { Z } .$ Now we just estimate

$$
{ \begin{array} { r l } { { 2 } | f ( x + i y ) | } & { = \left| { \frac { \exp ( i \pi z ) - \exp ( - i \pi z ) } { \exp ( i \pi ( z - 1 / 3 ) ) - \exp ( - i \pi ( z - 1 / 3 ) ) } } \right| \leqslant { \frac { | \exp ( i \pi z ) | + | \exp ( - i \pi z ) | } { \| \exp ( i \pi ( z - 1 / 3 ) ) | - | \exp ( - i \pi ( z - 1 / 3 ) ) ) | } } } \\ & { = { \frac { \exp ( - \pi y ) + \exp ( \pi y ) } { | \exp ( - \pi y ) - \exp ( \pi y ) | } } \leqslant 2 \quad { \mathrm { w h e n ~ } } | y | \geqslant 1 . \quad \boxdot } \end{array} }
$$

Problem 8. Show that a harmonic function $u : \mathbb { D }  \mathbb { R }$ is uniformly continuous if and only if it admits the representation

$$
u ( z ) ~ = ~ \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \mathrm { R e } \left( \frac { e ^ { i \theta } + z } { e ^ { i \theta } - z } \right) f ( e ^ { i \theta } ) d \theta , ~ z \in \mathbb { D } ,
$$

with $f : \partial \mathbb { D } \to \mathbb { R }$ continuous.

Solution.
It is a standard fact that u is uniformly continuous on D if and only if it admits a continuous extension to BD. First suppose that u admits a continuous extension to BD. Then the Poisson integral formula is exactly the representation

$$
u ( z ) ~ = ~ \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \mathrm { R e } \left( \frac { e ^ { i \theta } + z } { e ^ { i \theta } - z } \right) u ( e ^ { i \theta } ) d \theta
$$

(To prove the Poisson integral formula, you simply apply the regular mean value formula to u composed with the conformal map $w \mapsto { \frac { w + z } { 1 + { \overline { { z } } } w } }$ and simplify the change of variables.
Not sure if proving that would be required for this problem or not).

Conversely, suppose u has the above representation.
We just need to show that the continuous function $f : \partial \mathbb { D } \to \mathbb { R }$ continuously extends u. Fix $e ^ { i \theta _ { 0 } } \in \partial \mathbb { D }$ . We need to show that $u ( z ) \to f ( e ^ { i \theta _ { 0 } } ) { \mathrm { ~ a s ~ } } z \to e ^ { i \theta _ { 0 } }$ in D. $\operatorname { F i x } \epsilon > 0$ . Pick $\delta _ { 1 }$ such that $| \theta - \theta _ { 0 } | < \delta _ { 1 }$ implies $| f ( e ^ { i \theta } ) - f ( e ^ { i \theta _ { 0 } } ) | < \epsilon \ \mathrm { ( b y }$ continuity of $f )$ . Also, since BD is compact, let $M = \mathrm { m a x } _ { \theta \in [ 0 , 2 \pi ] } \vert f ( e ^ { i \theta } )$ |. Now we can pick $\delta > 0$ to be small enough so that

$$
| z - e ^ { i \theta _ { 0 } } | < \delta \quad \mathrm { a n d } \quad | \theta - \theta _ { 0 } | \geqslant \delta _ { 1 } \quad \mathrm { i m p l y } \quad \frac { 1 - | z | ^ { 2 } } { | e ^ { i \theta } - z | ^ { 2 } } = \operatorname { R e } \left( \frac { e ^ { i \theta } + z } { e ^ { i \theta } - z } \right) < \frac { \epsilon } { 2 M } .
$$

Then for all $| z - e ^ { i \theta _ { 0 } } | < \delta$ , we have the estimate (using the fact that $\int _ { 0 } ^ { 2 \pi } { \frac { 1 - | z | ^ { 2 } } { | e ^ { i \theta } - z | ^ { 2 } } } d \theta = 2 \pi$ for any $z \in \mathbb { D } )$

$$
\begin{array} { l l l } { | u ( z ) - f ( e ^ { i \theta _ { 0 } } ) | } & { = } & { \displaystyle \frac { 1 } { 2 \pi } \left| \int _ { 0 } ^ { 2 \pi } \frac { 1 - | z | ^ { 2 } } { | e ^ { i \theta } - z | ^ { 2 } } f ( e ^ { i \theta } ) d \theta - \int _ { 0 } ^ { 2 \pi } \frac { 1 - | z | ^ { 2 } } { | e ^ { i \theta } - z | ^ { 2 } } f ( e ^ { i \theta _ { 0 } } ) d \theta \right| } \\ { \displaystyle } & { \leqslant } & { \displaystyle \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \frac { 1 - | z | ^ { 2 } } { | e ^ { i \theta } - z | ^ { 2 } } | f ( e ^ { i \theta } ) - f ( e ^ { i \theta _ { 0 } } ) | d \theta } \\ { \displaystyle } & { \leqslant } & { \displaystyle \frac { 1 } { 2 \pi } \left( \int _ { | \theta - \theta _ { 0 } | < \delta _ { 1 } } \frac { 1 - | z | ^ { 2 } } { | e ^ { i \theta } - z | ^ { 2 } } \epsilon d \theta + \int _ { | \theta - \theta _ { 0 } | \geqslant \delta _ { 1 } } \frac { \epsilon } { 2 M } 2 M d \theta \right) } \\ { \displaystyle } & { \leqslant } & { \displaystyle \frac { \epsilon } { 2 \pi } \left( 2 \pi + 2 \pi \right) = 2 \epsilon . } \end{array}
$$

This shows that $u ( z ) \to f ( e ^ { i \theta _ { 0 } } ) { \mathrm { ~ a s ~ } } z \to e ^ { i \theta _ { 0 } }$ so f is a continuous extension of u to $\partial \mathbb { D }$ and we are done.

Problem 9. Consider a map $F : \mathbb { C } \times \mathbb { C } \to \mathbb { C }$ with the following properties.

1. For each fixed $z \in \mathbb { C }$ the map $w \mapsto F ( z , w )$ is injective.

2. For each fixed $w \in \mathbb C$ the map $z \mapsto F ( z , w )$ is holomorphic.

3. $F ( 0 , w ) = w { \mathrm { ~ f o r ~ } } w \in \mathbb { C } .$

Show that then

$$
F ( z , w ) ~ = ~ a ( z ) w + b ( z )
$$

for $z , w \in \mathbb { C }$ , where a and b are entire functions with $a ( 0 ) = 1 , b ( 0 ) = 0$ , and $a ( z ) \neq 0$ for $z \in \mathbb { C } .$

Solution.
Define $\begin{array} { r } { G ( z , w ) = \frac { F ( z , w ) - F ( z , 0 ) } { F ( z , 1 ) - F ( z , 0 ) } } \end{array}$ We claim that $G ( z , w ) = w$ for all $z , w$ . Then we can just take $a ( z ) = F ( z , 1 ) - F ( z , 0 )$ and $b ( z ) = F ( z , 0 )$ and we will be done.
By the injectivity condition, the denominator of $G ( z , w )$ is never 0, so for each fixed $w , z \mapsto G ( z , w )$ is an entire function.
Also note that $G ( 0 , w ) = w$ and that $G ( z , 0 ) = 0$ for all z and $G ( z , 1 ) = 1$ for all z. So the desired condition is verified for $w = 0 , 1$ . Fix $w \ne 1$ Then by the injectivity condition, if $G ( z , w ) = 1$ for any z, then $w = 1$ , and if $G ( z , w ) = 0$ for any z, then $w = 0 . \mathrm { ~ S o ~ } z \mapsto G ( z , w )$ is an entire function that misses both 0 and 1, so by Picard’s little theorem, $z \mapsto G ( z , w )$ is constant.
Then the fact that $G ( 0 , w ) = w$ implies that $G ( z , w ) = w$ for all z, so we are done.
−

Problem 10. Let $\left\{ f _ { n } \right\}$ be a sequence of holomorphic functions on D with the property that

$$
F ( z ) : = \sum _ { n = 1 } ^ { \infty } | f _ { n } ( z ) | ^ { 2 } \leqslant 1
$$

for all $z \in \mathbb { D }$ . Show that the series defining $F ( z )$ converges uniformly on compact subsets of D and that $F$ is subharmonic.

Solution.
Since $f _ { n }$ is holomorphic, $| f _ { n } | ^ { 2 }$ is subharmonic.
Therefore each $\begin{array} { r } { g _ { N } : = \sum _ { n = 1 } ^ { N } | f _ { n } | ^ { 2 } } \end{array}$ is also subharmonic, and we have that $g _ { N }$ increases monotonically to $F$ pointwise.
Notice that if subharmonic were replaced by harmonic, we would be done automatically by Harnack’s Principle.
The following argument is just a modification of the proof of Harnack to work for subharmonic functions, where we rely heavily on the fact that F is bounded and that the $g _ { N }$ are partial sums rather than general subharmonic functions (it’s not true in general that an increasing limit of subharmonic functions converges locally uniformly to another subharmonic function).

First, suppose we knew that $g _ { N }  F$ locally uniformly on D. Then since each $g _ { N }$ is continuous, $F$ also is, and for any disc $B ( z _ { 0 } , r ) \subseteq \mathbb { D }$ , we have

$$
F ( z _ { 0 } ) ~ = ~ \operatorname* { l i m } _ { N  \infty } g _ { N } ( z _ { 0 } ) ~ \leqslant ~ \operatorname* { l i m } _ { N  \infty } \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } g _ { N } ( z _ { 0 } + r e ^ { i \theta } ) d \theta ~ = ~ \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } F ( z _ { 0 } + r e ^ { i \theta } ) d \theta
$$

by the monotone convergence theorem (or by uniform convergence on compact sets).
So F is continuous and satisfies the sub mean value property, so it is subharmonic.

Now we show local uniform convergence.
Fix a compact set $K \subseteq \mathbb { D }$ and $\epsilon > 0$ . By compactness, there is a radius $r > 0$ such that $B ( z , r ) \subseteq \mathbb { D }$ for any $z \in K$ . Also by compactness, we can cover $K$ with finitely many balls $B ( w _ { 1 } , r / 2 ) \cup . . . \cup B ( w _ { k } , r / 2 )$ . For any $z \in K$ ,

$$
\operatorname* { l i m } _ { N  \infty } \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } ( F ( z + \frac { r } { 2 } e ^ { i \theta } ) - g _ { N } ( z + \frac { r } { 2 } e ^ { i \theta } ) ) d \theta \ = \ 0
$$

again by the monotone convergence theorem (this is where we need the fact that F is bounded).
So let $N$ be large enough so that

$$
\operatorname * { m a x } _ { 1 \leqslant j \leqslant k } \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \left( F \left( z _ { j } + \frac { r } { 2 } e ^ { i \theta } \right) - g _ { N } \left( z _ { j } + \frac { r } { 2 } e ^ { i \theta } \right) \right) d \theta \ < \ \epsilon .
$$

Now for any $\begin{array} { r } { M > N , g _ { M } - g _ { N } = \sum _ { n = N + 1 } ^ { M } | f _ { n } | ^ { 2 } } \end{array}$ is still a positive subharmonic function (this is where we need the fact that the $g _ { N }$ are partial sums).
Therefore it satisfies the “sub Poisson integral formula” (regular Poisson integral formula but with a $\leqslant$ instead of “). For any $z \in K$ , we have $z \in B ( z _ { j } , r / 2 )$ for some $j ,$ so we apply the sub Poisson formula on $B ( z _ { j } , r )$ to obtain

$$
\begin{array}{c} g _ { M } ( z ) - g _ { N } ( z ) \ \leqslant \ \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \frac { r ^ { 2 } - | z - z _ { j } | ^ { 2 } } { | ( z _ { j } + r e ^ { i \theta } ) - z | ^ { 2 } } \left( g _ { M } ( z _ { j } + r e ^ { i \theta } ) - g _ { N } ( z _ { j } + r e ^ { i \theta } ) \right) \ d \theta  \\ { \leqslant \ \frac { r + | z - z _ { j } | } { r - | z - z _ { j } | } \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } ( g _ { M } - g _ { N } ) ( z _ { j } + r e ^ { i \theta } ) \ d \theta } \\ { \leqslant \ \frac { r + r / 2 } { r - r / 2 } \cdot \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } ( F - g _ { N } ) ( z _ { j } + r e ^ { i \theta } ) \ d \theta \ < \ 3 \epsilon . \qquad } \end{array}
$$

This shows that the sequence $g _ { N }$ is uniformly Cauchy on $K$ and therefore converges uniformly to $F$ on $K$ so $g _ { N }  F$ locally uniformly on D and we are done.

Problem 11. Let $f : \mathbb { D }  \mathbb { C }$ be an injective and holomorphic function with $f ( 0 ) = 0$ and $f ^ { \prime } ( 0 ) = 1$ Show that then

$$
\operatorname* { i n f } \{ | w | : w \notin f ( \mathbb { D } ) \} \ \leqslant \ 1
$$

with equality if and only if $f ( z ) = z { \mathrm { ~ f o r ~ a l l ~ } } z \in \mathbb { D }$

Solution.
We analyze the situation when in $\begin{array} { r } { \vdots \{ | w | : w \notin f ( \mathbb { D } ) \} \geqslant 1 } \end{array}$ . Then $\mathbb { D } \subseteq f ( \mathbb { D } )$ , and since $f$ is injective, it has a holomorphic inverse $g : { \mathbb { D } }  { \mathbb { D } }$ on the disk.
It’s clear that $g ( 0 ) = 0$ and $g ^ { \prime } ( 0 ) = 1$ , so by the Schwarz lemma (and the fact that $g ^ { \prime } ( 0 ) = 1 )$ we must have $g ( z ) = z$ . Thus $f ( z ) = z$ as well.
The

original statement follows.

Problem 12. Let $f , g ,$ and h be complex-valued functions on C with

$$
f \ = \ g \circ h .
$$

Show that if h is continuous, and both f and g are holomorphic, then h is holomorphic as well.

Solution.
Let B (for bad) be the set of points z for which $g ^ { \prime } ( h ( z ) ) = 0$ . For $z \in \mathbb { C } \backslash B$ , we can find an analytic local inverse $g _ { U } ^ { - 1 }$ for g on a neighborhood of U of $h ( z )$ . Thus on $U .$ , we can write $h = g _ { U } ^ { - 1 } \circ f ,$ which implies that h is analytic at z. So h is analytic on $\mathbb { C } \backslash B$

Since g is non-constant, we must have $g ^ { \prime } ( z ) = 0$ only on a discrete set.
Furthermore, h is continuous, so in fact B is discrete.
But h is continuous so by Riemann’s theorem on removable singularities, h must be analytic.

Remark.
It’s not true in general that the preimage of a discrete set under a continuous function is also discrete (a constant function is a counterexample), so that step takes a bit more work.
Let Z denote the zeros of $g ^ { \prime }$ and suppose that $h ^ { - 1 } ( Z )$ has a limit point.
Take a convergent sequence $z _ { n }$ with $\{ h ( z _ { n } ) \} \subseteq Z ,$ so it’s discrete.
The set $\{ h ( z _ { n } ) \}$ can’t be infinite, because its also discrete, so the limit would have to be infinity, but $z _ { n }$ converges to a non-infinite limit $z _ { \infty } .$ , which is impossible by the continuity of h. So $\{ h ( z _ { n } ) \}$ is a finite set, meaning that there is some subsequence $\left\{ z _ { n _ { k } } \right\}$ converging to $z _ { \infty }$ on which h is constant.
But then $f$ is also constant on $\left\{ z _ { n _ { k } } \right\}$ , and since f is holomorphic this implies $f$ is a constant, which is a contradiction.

## 19 Spring 2018

Problem 1. Suppose $f \in L ^ { 1 } ( \mathbb { R } )$ satisfies

$$
\operatorname* { l i m } _ { h \to 0 } \operatorname* { s u p } \int _ { \mathbb { R } } \left| { \frac { f ( x + h ) - f ( x ) } { h } } \right| d x = 0 .
$$

Show that $f = 0$ almost everywhere.

Solution.
Let $F ( x ) = \int _ { - \infty } ^ { x } | f ( t ) |$ dt.
We then consider the difference quotient

$$
\begin{array} { r l r } {  { | \frac { F ( x + h ) - F ( x ) } { h } | = \frac { 1 } { | h | } | \int _ { - \infty } ^ { x } | f ( t + h ) | - | f ( t ) | d t | } } \\ & { } & { \leqslant \int _ { - \infty } ^ { x } | \frac { f ( t + h ) - f ( t ) } { h } | } \\ & { } & { \leqslant \int _ { \mathbb { R } } | \frac { f ( t + h ) - f ( t ) } { h } | d x . } \end{array}
$$

By hypothesis, this last quantity tends to 0 as $h  0 .$ . So F is differentiable with derivativeş $0 ,$ and is therefore constant.
It follows (by continuity from below) that $\int _ { \mathbb { R } } \left| f ( t ) \right| d t = 0$ , and so $f = 0 ~ \mathrm { a . e } ,$

Alternate solution.
Let $F ( x ) = \int _ { - \infty } ^ { x } f ( t ) d t$ . Since f is integrable, by the Lebesgue differentiation theorem we have that for a.e. x P R,

$$
f ( x ) ~ = ~ \operatorname* { l i m } _ { h \to 0 } { \frac { 1 } { h } } \int _ { x } ^ { x + h } f ( t ) d t ~ = ~ \operatorname* { l i m } _ { h \to 0 } { \frac { F ( x + h ) - F ( x ) } { h } } .
$$

So for any two Lebesgue points $x > y .$ , we have

$$
\begin{array} { r l } { | f ( x ) - f ( y ) | } & { = \displaystyle \operatorname* { l i m } _ { h \to 0 } \left| \frac { F ( x + h ) - F ( x ) } { h } - \frac { F ( y + h ) - F ( y ) } { h } \right| } & { = \displaystyle \operatorname* { l i m } _ { h \to 0 } \left| \int _ { y + h } ^ { x + h } \frac { f ( t ) } { h } d t - \int _ { y } ^ { x } \frac { f ( t ) } { h } d t \right| } \\ & { = \displaystyle \operatorname* { l i m } _ { h \to 0 } \left| \int _ { y } ^ { x } \frac { f ( t + h ) - f ( t ) } { h } d t \right| \leqslant \displaystyle \operatorname* { l i m s u p } _ { h \to 0 } \int _ { \mathbb { R } } \left| \frac { f ( t + h ) - f ( t ) } { h } d t \right| ~ = ~ 0 . } \end{array}
$$

So $f$ is constant a.e., and since f is also integrable we must have $f = 0 ~ \mathrm { a . e }$

Problem 2. Given $f \in L ^ { 2 } ( \mathbb { R } )$ and $h > 0$ we define

$$
Q ( f , h ) \ = \ \int _ { \mathbb { R } } { \frac { 2 f ( x ) - f ( x + h ) - f ( x - h ) } { h ^ { 2 } } } f ( x ) d x .
$$

(a) Show that

$$
Q ( f , h ) \geqslant 0 \quad { \mathrm { f o r ~ a l l ~ } } f \in L ^ { 2 } ( \mathbb { R } ) { \mathrm { ~ a n d ~ a l l ~ } } h > 0 .
$$

(b) Show that the set

$$
E \ = \ \{ f \in L ^ { 2 } ( \mathbb { R } ) : \operatorname* { l i m } _ { h \to 0 } Q ( f , h ) \leqslant 1 \}
$$

is closed in $L ^ { 2 } ( \mathbb { R } )$

Solution.

(a) It suffices to show that

$$
\int _ { \mathbb { R } } 2 f ( x ) ^ { 2 } d x \geqslant \int _ { \mathbb { R } } f ( x ) ( f ( x + h ) - f ( x - h ) ) d x .
$$

Indeed by Cauchy-Schwarz

$$
\begin{array} { r l } { \displaystyle \int _ { \mathbb R } f ( x ) ( f ( x + h ) - f ( x - h ) ) d x \leqslant | | f | | _ { 2 } \cdot | | f ( x + h ) - f ( x - h ) | | _ { 2 } } & { } \\ { \displaystyle \leqslant | | f | | _ { 2 } \cdot ( | | f ( x + h ) | | _ { 2 } + | | f ( x - h ) | | _ { 2 } ) } & { } \\ { \displaystyle = | | f | | _ { 2 } \left( | | f | | _ { 2 } + | | f | | _ { 2 } \right) } & { } \\ { \displaystyle } & { = 2 | | f | | _ { 2 } ^ { 2 } , } \end{array}
$$

as desired.

(b) Let $g ( x ) ~ = ~ 2 f ( x ) - f ( x + h ) - f ( x - h )$ . Note $g \in L ^ { 2 }$ . Using the form of Plancherel that says $\langle f , g \rangle = \left. \hat { f } , \hat { g } \right.$ , we can rewrite

$$
Q ( f , h ) ~ = ~ \int _ { \mathbb { R } } \frac { 2 \widehat { f } ( u ) - e ^ { i h u } \widehat { f } ( u ) - e ^ { - i h u } \widehat { f } ( u ) } { h ^ { 2 } } \overline { { \widehat { f } ( u ) } } ~ d u ~ = ~ \int _ { \mathbb { R } } \frac { 2 - 2 \cos ( h u ) } { h ^ { 2 } } \left| \widehat { f } ( u ) \right| ^ { 2 } d u .
$$

Now let $f _ { n }$ be a sequence in E with $f _ { n }  f$ in $L ^ { 2 }$ . By passing to a subsequence if necessary, we may also assume that $f _ { n }  f$ almost everywhere.
By Plancherel, we also have ${ \widehat { f _ { n } } } \to { \widehat { f } } \sin L ^ { 2 }$ , and by passing to a further subsequence if necessary we can also assume ${ \widehat { f _ { n } } } \to { \widehat { f } }$ almost everywhere.
Then by Fatou’s lemma, since $1 - \cos ( h u ) \geqslant 0$ for all $h , u ,$ for each n we have

$$
\begin{array} { r l } { { 1 } } & { \geqslant \displaystyle \operatorname* { l i m s u p } _ { h  0 } \int _ { \mathbb R } \frac { 2 - 2 \cos ( h u ) } { h ^ { 2 } } | \widehat { f _ { n } } ( u ) | ^ { 2 } d u \geqslant \displaystyle \operatorname* { l i m i n f } _ { h  0 } \int _ { \mathbb R } \frac { 2 - 2 \cos ( h u ) } { h ^ { 2 } } | \widehat { f _ { n } } ( u ) | ^ { 2 } d u } \\ & { \geqslant \displaystyle \int _ { \mathbb R } \operatorname* { l i m i n f } _ { h  0 } \frac { 2 - 2 \cos ( h u ) } { h ^ { 2 } } | \widehat { f _ { n } } ( u ) | ^ { 2 } d u = \displaystyle \int _ { \mathbb R } u ^ { 2 } | \widehat { f _ { n } } ( u ) | ^ { 2 } d u . } \end{array}
$$

Then by applying Fatou’s lemma again, this time in n, we have

$$
\int _ { \mathbb R } u ^ { 2 } | { \widehat { f } } ( u ) | ^ { 2 } d u \ = \ \int _ { \mathbb R } \operatorname* { l i m i n f } u ^ { 2 } | { \widehat { f _ { n } } } ( u ) | ^ { 2 } d u \ \leqslant \ \operatorname* { l i m i n f } _ { n  \infty } \int _ { \mathbb R } u ^ { 2 } | { \widehat { f _ { n } } } ( u ) | ^ { 2 } d u \ \leqslant \ 1 ,
$$

so $u \mapsto u ^ { 2 } \left| { \widehat { f } } ( u ) \right| ^ { 2 }$ is integrable.
Note we have the estimate

$$
\frac { 2 - 2 \cos ( h u ) } { h ^ { 2 } } ~ = ~ u ^ { 2 } \frac { 2 - 2 \cos ( h u ) } { ( h u ) ^ { 2 } } ~ \leqslant ~ 5 u ^ { 2 }
$$

for all $h , u \in \mathbb { R }$ because $t \mapsto { \frac { 2 - 2 \cos ( t ) } { t ^ { 2 } } }$ is bounded by 5 for all real t. Therefore we have

$$
\frac { 2 - 2 \cos ( h u ) } { h ^ { 2 } } \left| \widehat { f } ( u ) \right| ^ { 2 } d u \leqslant 5 u ^ { 2 } \left| \widehat { f } ( u ) \right| ^ { 2 } d u
$$

for all $h , u \in \mathbb { R }$ , where the function on the right is integrable, so by the dominated convergence theorem we have

$$
1 \geqslant \int _ { \mathbb { R } } u ^ { 2 } | { \widehat { f } } ( u ) | ^ { 2 } d u = \int _ { \mathbb { R } ^ { h  0 } } { \frac { 2 - 2 \cos ( h u ) } { h ^ { 2 } } } | { \widehat { f } } ( u ) | ^ { 2 } d u = \operatorname* { l i m } _ { h  0 } \int _ { \mathbb { R } } { \frac { 2 - 2 \cos ( h u ) } { h ^ { 2 } } } | { \widehat { f } } ( u ) | ^ { 2 } d u = \operatorname* { l i m } _ { h  0 } Q ( f , h ) ,
$$

so $f \in E$ and thus E is closed in $L ^ { 2 }$ .

## Problem 3. Suppose $f \in L ^ { 1 } ( \mathbb { R } )$ satisfies

$$
\operatorname* { l i m } _ { \epsilon \to 0 } \operatorname* { s u p } _ { \mathbb { R } } \int _ { \mathbb { R } } \int _ { \mathbb { R } } \frac { | f ( x ) f ( y ) | } { | x - y | ^ { 2 } + \epsilon ^ { 2 } } d x d y < \infty .
$$

Show that $f = 0$ almost everywhere.

Solution.
By applying monotone convergence to the limit (after using Tonelli’s theorem to convert the double integral into an integral over $\mathbb { R } ^ { 2 } )$ , we have

$$
\int _ { \mathbb { R } } \int _ { \mathbb { R } } { \frac { | f ( x ) f ( y ) | } { \left| x - y \right| ^ { 2 } } } d x d y < \infty .
$$

If $f$ is not zero almost everywhere, then f has a Lebesgue point a with $| f ( a ) | > 0$ . We have

$$
\int _ { a - r } ^ { a + r } \int _ { a - r } ^ { a + r } { \frac { | f ( x ) f ( y ) | } { \left| x - y \right| ^ { 2 } } } d x d y \geqslant \int _ { a - r } ^ { a + r } \int _ { a - r } ^ { a + r } { \frac { | f ( x ) f ( y ) | } { ( 2 r ) ^ { 2 } } } d x d y = \left( { \frac { 1 } { 2 r } } \int _ { a - r } ^ { a + r } \left| f ( x ) \right| d x \right) ^ { 2 } .
$$

By the Lebesgue differentiation theorem, the right side tends to $f ( a ) ^ { 2 }$ as $r \to 0 ^ { + }$ . On the other hand, the left-most integral must tend to 0, since the integrand is in $L ^ { 1 }$ (in fact $L _ { \mathrm { l o c } } ^ { 1 }$ is enough).
This is a contradiction, so we must have $f = 0 ~ \mathrm { a . e }$

## Problem 4.

(a) Fix $1 < p < \infty$ . Show that

$$
f \mapsto [ M f ] ( x , y ) \ = \ \operatorname* { s u p } _ { r > 0 , \rho > 0 } { \frac { 1 } { 4 r \rho } } \int _ { - r } ^ { r } \int _ { - \rho } ^ { \rho } f ( x + h , y + \ell ) d h d \ell
$$

is bounded on $L ^ { p } ( \mathbb { R } ^ { 2 } )$

(b) Show that

$$
[ A _ { r } f ] ( x , y ) ~ = ~ { \frac { 1 } { 4 r ^ { 3 } } } \int _ { - r } ^ { r } \int _ { - r ^ { 2 } } ^ { r ^ { 2 } } f ( x + h , y + \ell ) d h d \ell
$$

converges to f a.e. in the plane as $r \to 0$

Solution.

(a) For $g : \mathbb { R } \to \mathbb { R }$ , let

$$
M g ( x ) : = \operatorname* { s u p } _ { r > 0 } { \frac { 1 } { 2 r } } \int _ { - r } ^ { r } | g ( x + h ) | d h
$$

be the usual maximal operator.
For $x \in \mathbb { R }$ , define $f _ { x } ( y ) : = f ( x , y )$ Since $f \in L ^ { p } ( \mathbb { R } ^ { 2 } ) , f _ { x } \in L ^ { p } ( \mathbb { R } )$ for a.e. $x \in \mathbb { R }$ (this is proved by Tonelli’s theorem).
Therefore by the usual Hardy-Littlewood maximal theorem, we have

$$
\int | M f _ { x } ( y ) | ^ { p } d y \ \lesssim \ \int | f _ { x } ( y ) | ^ { p } d y
$$

for $\mathrm { a . e . ~ } x \in \mathbb { R }$ . Now, for each $y \in \mathbb { R } ,$ , define $g _ { y } ( x ) : = M f _ { x } ( y )$ . Tonelli’s theorem and the above inequality show that $g _ { y } \in L ^ { p } ( \mathbb R )$ for a.e. $y \in \mathbb { R }$ :

$$
\begin{array} { r l r } { \displaystyle \int \left( \int | g _ { y } ( x ) | ^ { p } d x \right) d y } & { = } & { \displaystyle \iint | M f _ { x } ( y ) | ^ { p } d y d x } \\ & { } & { \lesssim } & { \displaystyle \iint | f _ { x } ( y ) | ^ { p } d y d x = | | f | | _ { L ^ { p } ( \mathbb { R } ^ { 2 } ) } ^ { p } < \infty . } \end{array}
$$

Therefore using Hardy-Littlewood again we have

$$
\int | M g _ { y } ( x ) | ^ { p } d x \ \lesssim \ \int | g _ { y } ( x ) | ^ { p } d x
$$

for $\mathrm { a . e . ~ } y \in \mathbb { R }$ . Now note that we have

$$
\begin{array} { r c l } { [ M f ] ( x , y ) } & { \leqslant } & { \displaystyle \operatorname* { s u p } _ { r > 0 } \frac { 1 } { 2 r } \int _ { - r } ^ { r } \displaystyle \operatorname* { s u p } _ { \rho > 0 } \frac { 1 } { 2 \rho } \int _ { - \rho } ^ { \rho } \left. f ( x + h , y + \ell ) \right. d \ell d h \quad \mathrm { b y ~ T o n e l i } } \\ & { = } & { \displaystyle \operatorname* { s u p } _ { r > 0 } \frac { 1 } { 2 r } \int _ { - r } ^ { r } M f _ { x + h } ( y ) d h } \\ & { = } & { M g _ { y } ( x ) . } \end{array}
$$

So by the above work we conclude that

$$
\iint | [ M f ] ( x , y ) | ^ { p } d x d y \leqslant \iint | M g _ { y } ( x ) | ^ { p } d x d y \leqslant \iint | g _ { y } ( x ) | ^ { p } d x d y \leqslant | | f | | _ { L ^ { p } ( \mathbb { R } ^ { 2 } ) } ^ { p } . \quad \square \smash { \vphantom { \int ^ { p } } \int } | [ M ] | _ { L ^ { p } ( \mathbb { R } ^ { 2 } ) } ^ { p } .
$$

(b) We mimic the proof of the Lebesgue differentiation theorem.
Define

$$
T _ { r } f ( x , y ) \ : = \ \frac { 1 } { 4 r ^ { 3 } } \int _ { - r } ^ { r } \int _ { - r ^ { 2 } } ^ { r ^ { 2 } } | f ( x , y ) - f ( x + h , y + \ell ) | \ d h \ d \ell , \qquad T f ( x , y ) \ : = \ \operatorname* { l i m } _ { r \to 0 } \operatorname* { s u p } _ { T _ { r } f } f ( x , y ) .
$$

It suffices to show that $T f \ = \ 0 \ \mathrm { a . e . }$ and for that it suffices to show that for any fixed $\alpha > 0 .$ $\lambda \{ ( x , y ) : T f ( x , y ) \geqslant \alpha \} = 0$ (where λ denotes 2-dimensional Lebesgue measure).
Fix $\alpha > 0$ and $\epsilon > 0$ Note that the desired result is obviously true for continuous functions.
Since continuous functions are dense in $L ^ { p }$ , write $f = g + u$ where g is continuous and $| | u | | _ { L ^ { p } } < \epsilon .$ . The operator $T _ { r }$ is subadditive, so $T _ { r } f \leqslant T _ { r } g + T _ { r } u ,$ and taking $r \to 0$ gives that $T f \leqslant T u$

We now estimate the quantity $\lambda \{ ( x , y ) : T u ( x , y ) \geqslant \alpha \}$ . Notice that

$$
T _ { r } u ( x , y ) \ \leqslant \ { \frac { 1 } { 4 r ^ { 3 } } } \int _ { - r } ^ { r } \int _ { - r ^ { 2 } } ^ { r ^ { 2 } } \left( | u ( x , y ) | + | u ( x + h , y + \ell ) | \right) d h \ d \ell \ \leqslant \ | u ( x , y ) | + [ M u ] ( x , y ) .
$$

So $\{ ( x , y ) : T u ( x , y ) \geqslant \alpha \} \subseteq \{ ( x , y ) : | u ( x , y ) | \geqslant \alpha / 2 \} \cup \{ ( x , y ) : M u ( x , y ) \geqslant \alpha / 2 \}$ , which implies that

$$
\lambda \{ ( x , y ) : T u ( x , y ) \geqslant \alpha \} \ \leqslant \ \lambda \{ ( x , y ) : | u ( x , y ) | \geqslant \alpha / 2 \} + \lambda \{ ( x , y ) : M u ( x , y ) \geqslant \alpha / 2 \}
$$

$$
\leqslant \frac { \| u \| _ { L ^ { p } } ^ { p } } { ( \alpha / 2 ) ^ { p } } + \frac { \| M u \| _ { L ^ { p } } ^ { p } } { ( \alpha / 2 ) ^ { p } } \quad \mathrm { b y ~ C h e b y s h e v ` s ~ i n e q u a l i t y }
$$

$\leqslant { \frac { \epsilon ^ { p } 2 ^ { p } } { \alpha ^ { p } } } + { \frac { C ^ { p } \epsilon ^ { p } 2 ^ { p } } { \alpha ^ { p } } }$ where C is the constant from part (a) on the boundedness of $f \mapsto [ M f ] .$

Since $T f \leqslant T u$ , we also have $\begin{array} { r } { \lambda \{ ( x , y ) : T f ( x , y ) \geqslant \alpha \} \leqslant \frac { \epsilon ^ { p } 2 ^ { p } } { \alpha ^ { p } } + \frac { C ^ { p } \epsilon ^ { p } 2 ^ { p } } { \alpha ^ { p } } } \end{array}$ . Now the left side does not depend on $\epsilon ,$ so we can take $\epsilon \to 0$ and conclude that $\lambda \{ ( x , { \bar { y } } ) : T f ( { \bar { x , } } y ) \geqslant \alpha \} = 0$ □

Problem 5. Let $\mu$ be a real-valued Borel measure on r0, 1s such that

$$
\int _ { 0 } ^ { 1 } \frac { 1 } { x + t } d \mu ( t ) = 0
$$

for all $x > 1$ . Show that $\mu = 0$

Solution.
Let S denote the real span of the functions of the form $\frac { 1 } { x + t }$ for $x > 1$ in $C ( [ 0 , 1 ] )$ . We $\mathrm { a p - }$ ply Stone-Weirstrass to show that S is dense in $C ( [ 0 , 1 ] )$ q. For $x _ { 0 } \neq x _ { 1 } > \mathrm { ~ i ~ }$ , we have

$$
{ \frac { 1 } { x _ { 0 } + t } } \cdot { \frac { 1 } { x _ { 1 } + t } } = { \frac { 1 } { x _ { 1 } - x _ { 0 } } } \left( { \frac { 1 } { x _ { 0 } + t } } - { \frac { 1 } { x _ { 1 } + t } } \right) ,
$$

which lies in S. We also have that

$$
{ \frac { 1 } { x + t } } \cdot { \frac { 1 } { x + t + \epsilon } } \to { \frac { 1 } { ( x + t ) ^ { 2 } } }
$$

uniformly on r0, 1s as $\epsilon \to 0 ^ { + }$ . Thus $\frac { 1 } { ( x + t ) ^ { 2 } }$ lies in $\overline { S }$ for $t > 1$ . Therefore the product of any two elements in S lies in ${ \overline { { S } } } .$ . This implies that $\overline { S }$ is closed under multiplication.
Indeed if $f$ and $g$ lie in $\overline { S }$ then we have sequences $f _ { i } \to f$ and $g _ { i } \to g$ uniformly with $f _ { i } , g _ { i } \in S .$ . Since $f$ and $g$ are bounded on r0, 1s, we have that $f _ { i } g _ { i }  f g$ uniformly, and so $f g \in \overline { { S } }$ .

Hence $\overline { S }$ is an algebra.
It’s clear that $\overline { S }$ separates points, and that there is no point $x _ { 0 }$ such every function in $\overline { S }$ vanishes at $x _ { 0 }$ . Thus ${ \overline { { S } } } = C ( [ 0 , 1 ] )$ .

So we have that $\int _ { 0 } ^ { 1 } f ( t ) d \mu ( t ) = 0$ for all $f$ in S, and by density for all $f$ in $C ( [ 0 , 1 ] )$ q. Note that $\mu$ is a finite measure, otherwise $\int _ { 0 } ^ { 1 } { \frac { 1 } { 2 + t } }$ would be either $\infty \ \mathrm { o r \ - } \infty$ . By the Riesz representation theorem, we must have $\mu = 0$

Remark.
We used a slighly non-standard (although well-known) version of Stone-Weirstrass here.
It’s easy to avoid this, and instead show that the constant function 1 lies in ${ \overline { { S } } } .$ For instance, the functions $\frac { x } { x + t }$ converge uniformly to 1 on $[ 0 , 1 ]$ as $x \to \infty$

Alternate Solution.
Let $a _ { k } = \int _ { 0 } ^ { 1 } t ^ { k } d \mu ( t )$ . For $x \in ( 0 , 1 )$ we have

$$
0 = \int _ { 0 } ^ { 1 } { \frac { 1 } { 1 / x + t } } d \mu ( t ) = \int _ { 0 } ^ { 1 } { \frac { x } { 1 + t x } } d \mu ( t ) = \int _ { 0 } ^ { 1 } \left( \sum _ { k = 0 } ^ { \infty } ( - 1 ) ^ { k } t ^ { k } x ^ { k + 1 } \right) d \mu ( t ) = \sum _ { k = 0 } ^ { \infty } ( - 1 ) ^ { k } a _ { k } x ^ { k + 1 } ,
$$

where swapping the order of summation and integration can be justified by Fubini-Tonelli, after noting that $\mu$ is finite (to prove Fubini-Tonelli for signed measures, one looks at a Jordan decomposition and applies Fubini separately to each piece).
This latter sum is a power a series in x which is identically 0 for ş $x \in ( 0 , 1 )$ , so each $a _ { k }$ must equal 0. By taking linear combinations of the $a _ { k }$ , we see that $\int { p ( x ) } { d \mu ( t ) } = 0$ for any polynomial $p .$ But polynomials are dense in $C ( [ 0 , 1 ] )$ , and so $\mu = 0$ by the Riesz representation theorem.

Problem 6. Let T denote the unit circle in the complex plane and let $\mathcal { P } ( \mathbb { T } )$ denote the space of Borel probability measures on T and $\mathcal { P } ( \mathbb { T } \times \mathbb { T } )$ denote the space of Borel probability measures on $\mathbb { T } \times \mathbb { T }$ . Fix $\mu , \nu \in \mathcal P ( \mathbb { T } )$ and define

$$
\begin{array} { r } { { \cal M } = \displaystyle \left\{ \gamma \in { \mathcal P } ( \mathbb { T } \times \mathbb { T } ) : \displaystyle \iint _ { \mathbb { T } \times \mathbb { T } } f ( x ) g ( y ) d \gamma ( x , y ) = \displaystyle \int _ { \mathbb { T } } f ( x ) d \mu ( x ) \cdot \displaystyle \int _ { \mathbb { T } } g ( y ) d \nu ( y ) \quad \mathrm { f o r ~ a l l ~ } f , g \in C ( \mathbb { T } ) \right\} . } \end{array}
$$

Show that $F : \mathcal { M }  \mathbb { R }$ defined by

$$
F ( \gamma ) ~ = ~ \int \int \sin ^ { 2 } \left( { \frac { \theta - \phi } { 2 } } \right) d \gamma ( e ^ { i \theta } , e ^ { i \phi } )
$$

achieves its minimum on $\mathcal { M } .$

Solution (trick).
Note that $\begin{array} { r } { \sin ^ { 2 } \left( \frac { \theta - \phi } { 2 } \right) \ = \ \frac { 1 } { 2 } ( 1 - \cos \theta \cos \phi + \sin \theta \sin \phi ) } \end{array}$ , which is just a sum of three functions of the form $f ( \theta ) g ( \phi )$ where each $f , g \in C ( \mathbb { T } )$ . So by definition of $\mathcal { M } , F ( \gamma )$ is actually independent of $\gamma ,$ so $F$ is constant on M and therefore obviously achieves its minimum.

Alternate solution (idea generalizes to other similar problems).
Let $I = \mathrm { i n f } _ { \gamma \in M } F ( \gamma )$ . Let $\gamma _ { n }$ be a sequence of measures in $\mathcal { M }$ such that $F ( \gamma _ { n } )  I$ as $n \to \infty$ . Since $\mathbb { T } \times \mathbb { T }$ is compact, one version of the Riesz representation theorem says that the space of complex Borel measures on $\mathbb { T } \times \mathbb { T }$ is isomorphic to $C ( \mathbb { T } \times \mathbb { T } ) ^ { * }$ , and the operator norm of a measure is its total variation.
Therefore $\mathcal { P } ( \mathbb { T } \times \mathbb { T } )$ is a subset of the unit ball in $C ( \mathbb { T } \times \mathbb { T } ) ^ { * }$ . By the Banach-Alaoglu theorem, this unit ball is weak-˚ compact, and since $C ( \mathbb { T } \times \mathbb { T } )$ is separable, it is actually sequentially compact.
Thus there is a subsequence $\left\{ \gamma _ { n _ { k } } \right\}$ that weak-˚ converges to some complex Borel measure γ in the unit ball of $C ( \mathbb { T } \times \mathbb { T } ) ^ { * }$

We claim that $\gamma$ is the minimizer of $F .$ . We need to verify that $\gamma \in \mathcal { M }$ and that $F ( \gamma ) = I$ . Note that $\gamma$ is a probability measure because

$$
\gamma ( \mathbb { T } \times \mathbb { T } ) \ = \ \iint _ { \mathbb { T } \times \mathbb { T } } 1 d \gamma \ = \ \operatorname* { l i m } _ { n \to \infty } \iint _ { \mathbb { T } \times \mathbb { T } } 1 d \gamma _ { n } \ = \ 1
$$

by weak-˚ convergence because 1 is continuous.
To show that $\gamma \in \mathcal { M }$ , let $f , g \in C ( \mathbb { T } )$ be fixed.
Then the function $( x , y ) \mapsto f ( x ) g ( y )$ is in $C ( \mathbb { T } \times \mathbb { T } )$ , so by weak-˚ convergence we have

$$
\int _ { \mathbb { T } \times \mathbb { T } } f ( x ) g ( y ) d \gamma ( x , y ) \ = \ \operatorname* { l i m } _ { n \to \infty } \int _ { \mathbb { T } \times \mathbb { T } } f ( x ) g ( y ) d \gamma _ { n } ( x , y ) \ = \ \int _ { \mathbb { T } } f ( x ) d \mu ( x ) \cdot \int _ { \mathbb { T } } g ( y ) d \nu ( y ) .
$$

Thus $\gamma \in \mathcal { M }$ . To show that $F ( \gamma ) = I ,$ just note that $\begin{array} { r } { \sin ^ { 2 } \left( \frac { \theta - \phi } { 2 } \right) } \end{array}$ is also continuous on $\mathbb { T } \times \mathbb { T }$ , so weak-˚ convergence implies $F ( \gamma ) = \mathrm { l i m } _ { n  \infty } F ( \gamma _ { n } )$ q. □

Problem 7. Let $F : \mathbb { C } \times \mathbb { C } \to \mathbb { C }$ be jointly continuous and holomorphic in each variable separately.\
Show that $z \mapsto F ( z , z )$ is holomorphic.

Solution.
Let $( a , b ) \in \mathbb { C } ^ { 2 }$ . Since $z \mapsto F ( z , b )$ is holomorphic, by the Cauchy Integral Formula

$$
F ( a , b ) = { \frac { 1 } { 2 \pi i } } \int _ { | z - a | = r _ { 1 } } { \frac { F ( z , b ) } { z - a } } d z .
$$

Similarly, for each $z ,$ the function $w \mapsto F ( z , w )$ is holormophic, so

$$
F ( z , b ) = { \frac { 1 } { 2 \pi i } } \int _ { | w - b | = r _ { 2 } } { \frac { F ( z , w ) } { w - b } } d w .
$$

Therefore,

$$
F ( a , b ) = { \frac { 1 } { ( 2 \pi i ) ^ { 2 } } } \int _ { | z - a | = r _ { 1 } } { \frac { 1 } { ( z - a ) } } \left[ \int _ { | w - b | = r _ { 2 } } { \frac { F ( z , w ) } { ( w - b ) } } d w \right] d z .
$$

Now, because $F$ is continuous on $\mathbb { C } ^ { 2 }$ , Fubini’s theorem allows us to rewrite this iterated integral as a multiple integral:

$$
F ( a , b ) = { \frac { 1 } { ( 2 \pi i ) ^ { 2 } } } \int _ { T _ { 1 } \times T _ { 2 } } { \frac { F ( z , w ) } { ( z - a ) ( w - b ) } } d w d z ,
$$

where $T _ { 1 } = \{ | z - a | = r _ { 1 } \} , T _ { 2 } = \{ | w - b | = r _ { 2 } \}$ u. Thus,

$$
f ( z ) = F ( z , z ) = { \frac { 1 } { ( 2 \pi i ) ^ { 2 } } } \int _ { T _ { 1 } \times T _ { 2 } } { \frac { F ( \zeta , \xi ) } { ( \zeta - z ) ( \xi - z ) } } d \zeta d \xi ,
$$

Since $F$ is continuous on the compact set $T _ { 1 } \times T _ { 2 }$ , we can now simply differentiate under the integral sign to see that $f$ is holomorphic.
(Note: this proof actually shows that $F$ is holomorphic on $\mathbb { C } ^ { 2 }$ , i.e. has a convergent power series in two variables.)
□

Problem 8. Determine the supremum of

$$
\left| \frac { \partial u } { \partial x } ( 0 , 0 ) \right|
$$

among all harmonic functions $u : \mathbb { D } \to [ 0 , 1 ]$

Solution.
The answer is $2 / \pi .$ . Since D is simply connected, any such u is the real part of an analytic function $f = u + i v : \mathbb { D } \to S : = \{ z \in \mathbb { C } : 0 \leqslant \operatorname { R e } ( z ) \leqslant 1 \}$ . Adding a pure imaginary constant doesn’t change anything, so we can assume $f ( 0 )$ is real.
We have $f ^ { \prime } = u _ { x } + i v _ { y } ,$ so we want to bound $\operatorname { R e } ( f ^ { \prime } ( 0 ) )$ . Since we can pre-compose f with a rotation without changing the absolute value of $f ^ { \prime }$ or changing the codomain of $f ,$ , this is the same as bounding $\left| f ^ { \prime } ( 0 ) \right|$ . This shows that the desired supremum is the same as the supremum of $\left| f ^ { \prime } ( 0 ) \right|$ over all $f : \mathbb { D } \to S$ holomorphic with $f ( 0 ) \in \mathbb { R }$ . Let $f$ be such a function.
Let $T : S  \mathbb { D }$ be the conformal map given by

$$
T ( z ) ~ = ~ \frac { \exp ( i \pi z ) - i } { \exp ( i \pi z ) + i } .
$$

Let $\alpha = T ( f ( 0 ) )$ and let $\begin{array} { r } { \psi ( z ) = \frac { z - \alpha } { 1 - \overline { { \alpha } } z } } \end{array}$ be the automorphism of D that sends α to 0. Then $g = \psi \circ T \circ f$ is a holomorphic function $\mathbb { D } \to \mathbb { D }$ with $g ( 0 ) = 0$ . So by the Schwarz lemma we have $| g ^ { \prime } ( 0 ) | \leqslant 1$ . Now we compute

$$
\begin{array} { r l r } { | g ^ { \prime } ( 0 ) | } & { = } & { | \psi ^ { \prime } ( \alpha ) | | T ^ { \prime } ( f ( 0 ) ) | | f ^ { \prime } ( 0 ) | \ = \ \frac { 1 } { 1 - | \alpha | ^ { 2 } } | T ^ { \prime } ( f ( 0 ) ) | | f ^ { \prime } ( 0 ) | \ \geqslant \ | T ^ { \prime } ( f ( 0 ) ) | | f ^ { \prime } ( 0 ) | } \\ & { \geqslant } & { 2 \pi \left| \frac { \exp ( i \pi f ( 0 ) ) } { \left( \exp ( i \pi f ( 0 ) ) + i ) ^ { 2 } \right| } \right| \ = \ \left| \frac { 2 \pi } { 2 i + 2 i \operatorname { I m } ( \exp ( i \pi f ( 0 ) ) ) } \right| \ \geqslant \ \frac { \pi } { 2 } } \end{array}
$$

because $\exp ( i \pi f ( 0 ) )$ lies on the top half of the unit circle because $f ( 0 ) \in [ 0 , 1 ]$ . Therefore we conclude

$$
1 \ \geqslant \ | g ^ { \prime } ( 0 ) | \ \geqslant \ \frac \pi 2 | f ^ { \prime } ( 0 ) | ,
$$

which shows that $2 / \pi$ is an upper bound for the desired quantity.
Now taking

$$
f ( z ) ~ = ~ T ^ { - 1 } ( z ) ~ = ~ \frac { 1 } { i \pi } \log \left( \frac { i + i z } { 1 - z } \right) ,
$$

where the log here is well-defined because $\frac { i + i z } { 1 - z } \in \mathbb { H }$ for $\mathrm { a l l } ~ z \in \mathbb { D }$ , it’s easy to calculate that $| f ^ { \prime } ( 0 ) | = 2 / \pi ,$ , so it must be the supremum and it’s actually attained.

Problem 9. Consider the formal product

$$
\prod _ { n = 1 } ^ { \infty } \left( 1 + { \frac { 1 } { n } } \right) ^ { z } \left( 1 - { \frac { z } { n } } \right) .
$$

(a) Show that the product converges for any $z \in ( - \infty , 0 )$

(b) Show that the resulting function extends from this interval to an entire function of $z \in \mathbb { C }$

Solution.

(a) For $z \in ( 0 , \infty )$ we have

$$
1 - { \frac { z } { n } } = 1 + { \frac { - z } { n } } \leqslant \left( 1 + { \frac { 1 } { n } } \right) ^ { - z }
$$

by Bernoulli’s inequality (or simply by looking at the generalized binomial expansion of the term on the right).
Thus each term in the product lies in p0, 1s. So the partial products form a decreasing sequence of positive real numbers and therefore the product converges.

## (b) MISSING

Problem 10. Let $\mathbb { C } ^ { * } = \mathbb { C } \cup \{ \infty \}$ be the Riemann sphere and let $\Omega = \mathbb { C } ^ { * } \backslash \{ 0 , 1 \}$ . Let $f : \Omega \to \Omega$ be a holomorphic function.

(a) Prove that if f is injective then $f ( \Omega ) = \Omega$

(b) Make a list of all such injective functions $f .$

Solution.
Part (a) follows from part (b) by just examining the list of all possible functions and observing that each of them is surjective.
For part (b) we first consider the same problem on a modified region $\tilde { \Omega } : = \mathbb { C } ^ { * } \backslash \{ 0 , \infty \}$ . Let $g : \widetilde \Omega \to \widetilde \Omega$ be injective and holomorphic.
First we show that the injectivity implies that when considered as a function on all of $\mathbb { C } ^ { * }$ , g has at worst simple poles at 0 and $\infty \ ( \mathrm { i . e . } \ g$ has either a removable singularity or a simple pole at 0 and $\infty )$ . Essential singularities are impossible by the big Picard theorem.
To show that higher order poles are impossible, suppose g has a pole of order $\geqslant ~ 2$ at 0 (the argument for $\infty$ is the same).
Then $1 / g$ has a zero of order $\geqslant 2$ at 0. Let $\gamma$ be a small circle around the origin; then the argument principle says that $( 1 / g ) ( \gamma )$ winds twice around 0. Thus there is a neighborhood U of 0 such that $( 1 / g ) ( \gamma )$ winds at least twice around every point of $U _ { : }$ and by the argument principle again, this means that $g$ achieves every value in $U$ at least twice inside of $\gamma .$ . This contradicts $g$ being injective unless it happens to be the case that every value in U is achieved by g at one point with multiplicity 2. But this is impossible because if $g ( z _ { 0 } ) = w _ { 0 }$ with multiplicity 2, then $g ^ { \prime }$ vanishes at $z _ { 0 } .$ So if the above situation happened, then $g ^ { \prime }$ would be identically zero on $( g ^ { \prime } ) ^ { - 1 } ( U )$ , which is an open set, so by uniqueness of analytic continuation this would imply that $g ^ { \prime }$ is identically zero, which is also a contradiction.
Thus we conclude that g has at worst simple poles at 0 and $\infty$

Therefore we have the representation $g ( z ) = a / z + b + c z$ for some $a , b , c \in \mathbb { C }$ . But note that by hypothesis, $g ( z )$ is never 0 for $z \in \widetilde { \Omega }$ . The equation $a / z + b + c z = 0$ always has a nonzero, non-infinite solution if $a \neq 0 \neq c ,$ so we must have $a = 0 \mathrm { o r } c = 0$ . And in either case, we must then also have $b = 0$ to avoid achieving 0. So the only possible functions g are $g ( z ) = a z$ and $g ( z ) = a / z \quad$ with $a \neq 0$

Now let $f : \Omega \to \Omega$ be injective and holomorphic.
This induces an injective holomorphic function $g = T ^ { - 1 } f T : \widetilde { \Omega } \to \widetilde { \Omega }$ where $T ( z ) = z / ( z + 1 )$ is an automorphism of $\mathbb { C } ^ { * }$ sending 0 to 0 and $\infty$ to 1. Therefore by the above we have

$$
g ( z ) ~ = ~ { \frac { f ( z / ( z + 1 ) ) } { f ( z / ( z + 1 ) ) - 1 } } ~ = ~ a z ~ \mathrm { o r } ~ { \frac { a } { z } } .
$$

After simplifying everything and changing variables $w = z / ( z + 1 )$ we find that the only possibilities for f are

$$
f ( w ) ~ = ~ 1 + { \frac { w - 1 } { ( a - 1 ) w + 1 } } , \qquad f ( w ) ~ = ~ 1 + { \frac { w } { ( a - 1 ) w - a } } \quad \mathrm { f o r ~ s o m e ~ } a \ne 0 .
$$

Since $a z$ and $a / z$ are both surjective as maps $\widetilde \Omega \to \widetilde \Omega$ , and we got the possibilities for f by composing with conformal maps, it’s clear that both of these possibilities are surjective as maps from $\Omega  \Omega . \qquad \bigtriangledown$

Comment Instead of using the big Picard theorem as above, we can cite the much simpler Casorati-Weierstrass theorem.

Problem 11. For $R > 1$ let $A _ { R }$ be the annulus $\{ 1 < | z | < R \}$ . Assume there is a conformal mapping F from $A _ { R _ { 1 } }$ onto $A _ { R _ { 2 } }$ . Prove that $R _ { 1 } = R _ { 2 }$

Solution.
See Spring 2017 #7.

Problem 12. Let $f ( z )$ be bounded and holomorphic on the unit disc D. Prove that for any $w \in \mathbb { D }$ we have

$$
f ( w ) ~ = ~ \frac { 1 } { \pi } \int _ { \mathbb { D } } \frac { f ( z ) } { ( 1 - \overline { { z } } w ) ^ { 2 } } d A ( z ) ,
$$

where $d A ( z )$ means integration with respect to Lebesgue measure.

Solution.
Consider f as an element of the Bergman space $A ^ { 2 } ( \mathbb { D } ) : = \{ f : \mathbb { D } \to \mathbb { C }$ holomorphic : $\int _ { \mathbb { D } } | f ( z ) | ^ { 2 } d A ( z ) < \infty \}$ This is a Hilbert space with inner product

$$
\langle f , g \rangle \ = \ \int _ { \mathbb { D } } f ( z ) { \overline { { g ( z ) } } } d A ( z )
$$

and orthonormal basis $\left\{ z \mapsto { \sqrt { \frac { n + 1 } { \pi } } } z ^ { n } \right\} _ { n = 0 } ^ { \infty }$ (It’s easy to check that these are actually an inner product and orthonormal basis).
For each fixed $w \in \mathbb { D } ,$ , we first show the map $f \mapsto f ( w )$ is a bounded linear functional on $A ^ { 2 }$ . We have

$$
| f ( w ) | ~ = ~ \left| { \frac { 1 } { \pi \left( { \frac { 1 - | w | } { 2 } } \right) ^ { 2 } } } \int _ { B ( w , ( 1 - | w | ) / 2 ) } f ( z ) d A ( z ) \right| \lesssim ~ \left( \int _ { B ( w , ( 1 - | w | ) / 2 ) } | f ( z ) | ^ { 2 } d A ( z ) \right) ^ { 1 / 2 } \lesssim ~ | | f | | _ { A ^ { 2 } }
$$

where the equality is by the mean value property of holomorphic functions and the first inequality is by Cauchy-Schwarz.
Thus $f \mapsto f ( w )$ is bounded, and it’s clearly linear.

Thus by the Riesz representation theorem, for each $w \in \mathbb { D }$ there is a function $g _ { w } \in A ^ { 2 }$ such that

$$
f ( w ) ~ = ~ \langle f , g _ { w } \rangle ~ = ~ \int _ { \mathbb { D } } f ( z ) { \overline { { g _ { w } ( z ) } } } d A ( z )
$$

for all $f \in A ^ { 2 }$ . So we just need to show that $\begin{array} { r } { g _ { w } ( z ) = \frac { 1 } { \pi ( 1 - \overline { { w } } z ) ^ { 2 } } } \end{array}$ . By definition of the functions $g _ { w } .$ for any z we have

$$
\begin{array} { r c l } { \displaystyle g _ { w } ( z ) = \langle g _ { w } , g _ { z } \rangle = \displaystyle \sum _ { n = 0 } ^ { \infty } \langle g _ { w } , e _ { n } \rangle \overline { { \langle g _ { z } , e _ { n } \rangle } } \quad \mathrm { b y ~ P a r s e v a l ~ ( w h e r e ~ } \{ e _ { n } \} \mathrm { ~ i s ~ t h e ~ o r t h n o r m a l ~ b a s i s ~ m e n t i o n e d ~ a b o v e ) } } \\ { \displaystyle } & { = \displaystyle \sum _ { n = 0 } ^ { \infty } \overline { { \langle } } \overline { { e _ { n } , g _ { w } \rangle } } \langle e _ { n } , g _ { z } \rangle = \displaystyle \sum _ { n = 0 } ^ { \infty } \overline { { e _ { n } ( w ) } } e _ { n } ( z ) = \displaystyle \sum _ { n = 0 } ^ { \infty } \frac { 1 } { \pi } ( n + 1 ) ( \overline { { w } } z ) ^ { n } = \displaystyle \frac { 1 } { \pi ( 1 - \overline { { w } } z ) ^ { 2 } } . } \end{array}
$$

## Alternative Solution

If $w = 0$ this is the mean value property for analytic functions, so assume $w \ne 0$ . Let

$$
d z = d x + i d y , \ d \overline { { { z } } } = d x - i d y ;
$$

then

$$
d \overline { { { z } } } \wedge d z = 2 i d x \wedge d y .
$$

Also let

$$
\frac { \hat { \sigma } g } { \hat { \sigma } z } = \frac { 1 } { 2 } \left( \frac { \hat { \sigma } g } { \hat { \sigma } x } - i \frac { \hat { \sigma } g } { \hat { \sigma } y } \right) ,
$$

$$
\frac { \hat { \sigma } g } { \hat { \sigma } z } = \frac { 1 } { 2 } \left( \frac { \hat { \sigma } g } { \hat { \sigma } x } + i \frac { \hat { \sigma } g } { \hat { \sigma } y } \right) ,
$$

for any function g. Then

$$
d g = \frac { \partial g } { \partial x } d x + \frac { \partial g } { \partial y } d y = \frac { \partial g } { \partial z } d z + \frac { \partial g } { \partial \overline { { z } } } d \overline { { z } } .
$$

Now, since f is analytic, we have

$$
\frac { \partial } { \partial \overline { { z } } } \left\{ \frac { f ( z ) } { 1 - w \overline { { z } } } \right\} = \frac { w f ( z ) } { ( 1 - w \overline { { z } } ) ^ { 2 } } .
$$

Thus, the 2-form in the integrand equals

$$
\frac { f ( z ) d x \wedge d y } { ( 1 - w \overline { { { z } } } ) ^ { 2 } } = \frac { 1 } { 2 i } d F ,
$$

where $F$ is the 1-form

$$
F = \frac { f ( z ) d z } { w ( 1 - w \overline { { z } } ) } .
$$

Therefore, by Stokes’ theorem,

$$
\begin{array} { c } { { { \frac { 1 } { \pi } } \displaystyle \int _ { \mathbb { D } } \displaystyle \frac { f ( z ) d x \wedge d y } { ( 1 - w \overline { { { z } } } ) ^ { 2 } } = \displaystyle \frac { 1 } { 2 \pi i } \displaystyle \int _ { \mathbb { D } } d F = \displaystyle \frac { 1 } { 2 \pi i } \displaystyle \int _ { \partial \mathbb { D } } F = \displaystyle \frac { 1 } { 2 \pi i w } \displaystyle \int _ { \partial \mathbb { D } } \displaystyle \frac { f ( z ) d z } { 1 - w \overline { { { z } } } } } } \\ { { { } } } \\ { { { } = \displaystyle \frac { 1 } { 2 \pi i w } \displaystyle \int _ { \partial \mathbb { D } } \displaystyle \frac { z f ( z ) } { z - w } d z = \displaystyle \frac { 1 } { w } w f ( w ) = f ( w ) , } } \end{array}
$$

by the Cauchy integral formula.

In general, if $f : \mathbb { D }  \mathbb { C }$ is analytic and bounded, let $f _ { r } ( z ) = f ( z )$ for $0 \textless r \textless 1$ . Then $f _ { r }$ is analytic on the larger disc $D ( 0 , 1 / r )$ and hence by the above

$$
f _ { r } ( w ) = \frac { 1 } { \pi } \int _ { \mathbb { D } } \frac { f _ { r } ( z ) } { ( 1 - w \overline { { z } } ) ^ { 2 } } d A ( z ) .
$$

By continuity, $f _ { r } ( w ) \to f ( w )$ as $r \to 1$ . Moreover, $f _ { r }  f$ pointwise on $\mathbb { D } ,$ and since $f , f _ { r }$ are bounded, the dominated convergence theorem implies

$$
f ( w ) = \operatorname* { l i m } _ { r \to 1 } f _ { r } ( w ) = \operatorname* { l i m } _ { r \to 1 } \frac { 1 } { \pi } \int _ { \mathbb { D } } \frac { f _ { r } ( z ) } { ( 1 - w \overline { { z } } ) ^ { 2 } } d A ( z ) = \frac { 1 } { \pi } \int _ { \mathbb { D } } \frac { f ( z ) } { ( 1 - w \overline { { z } } ) ^ { 2 } } d A ( z ) .
$$

## 20 Fall 2018

Problem 1. Let $\left\{ f _ { n } \right\}$ be a sequence of real-valued Lebesgue measurable functions on $\mathbb { R } ,$ and let $f$ be another such function.
Assume that

(a) $f _ { n }  f$ Lebesgue almost everywhere

(b) $\int | x | | f _ { n } ( x ) | d x \leqslant$ 100 for all $n ,$ and

(c) $\tilde { \int _ { } | f _ { n } ( x ) | ^ { 2 } } d x \leqslant 1 0 0$ for all n.

Prove that $f _ { n } \in L ^ { 1 }$ for all $n ,$ that $f \in L ^ { 1 }$ , and that $\vert \vert f _ { n } - f \vert \vert _ { L ^ { 1 } } \to 0$ . Also show that neither assumption (b) nor assumption (c) can be omitted while making these deductions.

Solution.
To show that $f _ { n } \in L ^ { 1 }$ , note that

$$
\int _ { \mathbb R } | f _ { n } | ~ = ~ \int _ { | x | \leqslant 1 } | f _ { n } | + \int _ { | x | > 1 } | f _ { n } | ~ \leqslant ~ \left( \int _ { | x | \leqslant 1 } | f _ { n } | ^ { 2 } \right) ^ { 1 / 2 } 2 ^ { 1 / 2 } + \int _ { | x | > 1 } | x | | f _ { n } ( x ) | ~ \leqslant ~ C ~ < \infty
$$

for some constant C independent of n by hypotheses (b) and (c). Now to show that $f \in L ^ { 1 }$ , note that by Fatou’s lemma we have

$$
\int | f | \ = \ \int \operatorname* { l i m i n f } _ { n \to \infty } | f _ { n } | \ \leqslant \ \operatorname* { l i m i n f } _ { n \to \infty } \int | f _ { n } | \ \leqslant \ C \ < \ \infty .
$$

Now we show $f _ { n }  f$ in $L ^ { 1 }$ . First we need two “uniformity” estimates:

$$
\begin{array} { l } { { \displaystyle \int _ { | x | > R } | f _ { n } | \leqslant \int _ { | x | > R } \frac { | x | } { R } | f _ { n } | \lesssim \frac { 1 } { R } } } \\ { { \displaystyle \int _ { E } | f _ { n } | \leqslant m ( E ) ^ { 1 / 2 } \left( \int _ { E } | f _ { n } | ^ { 2 } \right) ^ { 1 / 2 } \lesssim m ( E ) ^ { 1 / 2 } } . } \end{array}
$$

where the implied constant is independent of n in both.
By the same Fatou’s lemma argument, the aboveş ş estimates also hold for $f .$ Let $\epsilon > 0$ . Let R be big enough so that $\int _ { | x | > R } | f _ { n } | < \epsilon$ for all n and $\int _ { | x | > R } | f | < \epsilon .$ By Egorov’s theorem, there is a set $E \subseteq \left\{ | x | \leqslant R \right\}$ on whichş $f _ { n }  f$ uniformly, and by the second estimate above we may pick $m ( E ^ { c } )$ to be small enough so that $\int _ { E ^ { c } } | f _ { n } | , \int _ { E ^ { c } } | f _ { n } | < \epsilon .$ . Then we have

$$
\begin{array} { r c l } { \displaystyle \int | f _ { n } - f | } & { = } & { \displaystyle \int _ { | x | > R } | f _ { n } - f | + \int _ { E } | f _ { n } - f | + \int _ { E ^ { c } } | f _ { n } - f | } \\ { \displaystyle } & { \leqslant } & { \displaystyle \int _ { | x | > R } | f _ { n } | + \int _ { | x | > R } | f | + \int _ { E } | f _ { n } - f | + \int _ { E ^ { c } } | f _ { n } | + \int _ { E ^ { c } } | f | } \\ { \displaystyle } & { < } & { 4 \epsilon + \int _ { E } | f _ { n } - f | . } \end{array}
$$

Taking $n \to \infty$ , since we have uniform convergence on $E _ { i }$ , gives

$$
\operatorname* { l i m } _ { n \to \infty } | f _ { n } - f | < 4 \epsilon .
$$

This holds for any $\epsilon > 0 .$ , so the result follows.

Problem 2. Let $( X , \rho )$ be a compact metric space which has at least two points, and let $C ( X )$ be the space of continuous functions $X  \mathbb { R }$ with the uniform norm.
Let D be a dense subset of X and for each $y \in D$ define $f _ { y } \in C ( \boldsymbol { X } )$ by $f _ { y } ( x ) = \rho ( x , y )$ . Let A be the subalgebra of $C ( X )$ generated by the collection $\left\{ f _ { y } : y \in D \right\}$

(a) Prove that A is dense in CpXq under the uniform norm.

(b) Prove that CpXq is separable.

Solution.
(a) By one version of the Stone-Weierstrass theorem, it’s enough to check that A separates points (for all $x \neq y \in X$ there exists $f \in A$ with $f ( x ) \neq f ( y ) )$ and is nonvanishing (for all $x \in X$ there exists $f \in A$ with $f ( x ) \neq 0 )$ . Both of these are easily verified because X has at least two points by hypothesis.
For separating points, given $x \neq y$ let $f = f _ { y }$ . For nonvanishing, given x let $f = f _ { y }$ for any $y \ne x$

(b)

Problem 3. Let $( X , \rho )$ be a compact metric space and let $P ( X )$ be the set of all Borel probability measures on X. Assume $\mu _ { n } \to \mu$ in the weak-˚ topology on $P ( X )$ . Prove that $\mu _ { n } ( E ) \to \mu ( E )$ whenever $E$ is a Borel susbet of X such that $\mu ( \overline { { E } } ) = \mu ( E ^ { \circ } )$ , where E is the closure and $E ^ { \circ }$ is the interior.

Solution.
Applying the portmanteau theorem twice, since $E ^ { \circ }$ is open and $\overline { E }$ is closed, we have

$$
\mu ( E ^ { \circ } ) \ \leqslant \ \operatorname* { l i m i n f } _ { n \to \infty } \mu _ { n } ( E ^ { \circ } ) \ \leqslant \ \operatorname* { l i m i n f } _ { n \to \infty } \mu _ { n } ( E ) \ \leqslant \ \operatorname* { l i m s u p } _ { n \to \infty } \mu _ { n } ( E ) \ \leqslant \ \operatorname* { l i m s u p } _ { n \to \infty } \mu _ { n } ( \overline { { E } } ) \ \leqslant \ \mu ( \overline { { E } } )
$$

But by hypothesis, $\mu ( E ^ { \circ } ) = \mu ( { \overline { { E } } } )$ , so every inequality in the chain is actually an equality.
Since $\mu ( E )$ also necessarily fits somewhere in between $\mu ( E ^ { \circ } )$ and $\mu ( \overline { { E } } )$ , which are equal, we conclude

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } _ { \mu _ { n } } ( E ) \ = \ \operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { } \mu _ { n } ( E ) \ = \ \mu ( E ) . \quad \sqsubseteq
$$

Problem 4. Let T be the unit circle in the complex plane and for each $\alpha \in \mathbb { T }$ define the rotation map $R _ { \alpha } : \mathbb { T }  \mathbb { T }$ by $R _ { \alpha } ( z ) = \alpha z$ . A Borel probability measure $\mu$ on T is called α-invariant if $\mu ( R _ { \alpha } ( E ) ) = \mu ( E )$ for all Borel sets $E \subseteq \mathbb { T }$

(a) Let m be Lebesgue measure on T. Show that for every α P T, m is α-invariant.

(b) Prove that if α is not a root of unity, then the set of powers $\{ \alpha ^ { n } : n \in \mathbb { Z } \}$ is dense in T.

(c) Prove that if α is not a root of unity, then m is the only α-invariant Borel probability measure on T.

Solution.
Throughout, we identify T with the interval r0, 1q in the natural way, so $^ { 6 6 } \alpha$ is not a root of unity” is replaced by “α is irrational”.

(a) When viewed as a map on $[ 0 , 1 ) , R _ { \alpha } ( x ) = x + \alpha$ pmod 1q. We know that Lebesgue measure is translation invariant, so $R _ { \alpha }$ is measure preserving when considered as a map $[ 0 , 1 ) \to \mathbb { R }$ . But in the case where $E \subseteq [ 0 , 1 )$ has $R _ { \alpha } ( E ) \cap [ 1 , \infty ) \neq \emptyset , R _ { \alpha } ( E )$ may be reassembled as a subset of $[ 0 , 1 )$ by just translating $R _ { \alpha } ( E ) \cap [ 1 , \infty )$ to the left by 1, which still preserves Lebesgue measure.
Thus $R _ { \alpha }$ preserves m. □

(b) Method 1. It’s enough to show $\{ n \alpha : n \geqslant 0 \}$ is dense in T. Since α is irrational, the orbit contains infinitely many distinct points.
Therefore by the pigeonhole principle, for every $\epsilon > 0$ there exist some $n < m$ such that $\lVert n \alpha - m \alpha \rVert _ { \mathbb { T } } < \epsilon \ ( \lVert \cdot \rVert _ { \mathbb { T } }$ denotes “mod $1 ^ { \mathfrak { s } }$ distance).
Therefore the rotation $x \mapsto ( m - n ) \alpha$ is a rotation by less than , so $\{ j ( m - n ) \alpha : j \geqslant 0 \}$ is a subset of the orbit such that every point of T is at most  away from some $j ( m - n ) \alpha$ . Such subsets exist for any $\epsilon > 0$ , so the orbit is dense.

(b) Method 2. It’s enough to show tnα $: \ n \ \geqslant \ 0 \}$ is dense in T. In fact we show a stronger result which is the equidistribution theorem, i.e. for any $0 \leqslant a < b \leqslant 1$

$$
\operatorname* { l i m } _ { N \to \infty } { \frac { \# \{ n : a \leqslant n \alpha \leqslant b \} } { N } } \ = \ b - a .
$$

For any $f \in L ^ { 1 } ( \mathbb { T } )$ , set

$$
A _ { N } f : = \frac { 1 } { N } \sum _ { n = 0 } ^ { N - 1 } f ( n \alpha ) , \qquad I ( f ) : = \int _ { \mathbb { T } } f d m .
$$

The first step is to show that for $f \in C ( \mathbb { T } ) , A _ { N } f \to I ( f )$ as $N  \infty$ . It’s easy to see that this property is linear and behaves well under $L ^ { \infty }$ approximation, so since trig polynomials are dense in $C ( \mathbb { T } )$ , it’s enough

to show that this result holds for $f ( x ) = \exp ( 2 \pi i k x )$ for any $k \in \mathbb { Z }$ . We calculate directly

$$
A _ { N } f \ = \ { \frac { 1 } { N } } \sum _ { n = 0 } ^ { N - 1 } \exp ( 2 \pi i k \alpha ) ^ { n } \ = \ { \frac { 1 } { N } } \{ { \begin{array} { l l } { N } & { k = 0 } \\ { { \frac { 1 - \exp ( 2 \pi i N k \alpha ) } { 1 - \exp ( 2 \pi i R \alpha ) } } } & { k \neq 0 } \end{array} } \  = \ { \{ \begin{array} { l l } { 1 } & { k = 0 } \\ { O _ { k } ( 1 / N ) } & { k \neq 0 } \end{array}  }
$$

because $\exp ( 2 \pi i k \alpha ) \neq 1$ for all $k \neq 0$ because α is irrational.
Thus

$$
\operatorname* { l i m } _ { N  \infty } A _ { N } f \ = \ \{ 1 k = 0 \atop 0 k \neq 0  = \ I ( f ) .
$$

To finish the proof, we want to apply this convergence to the characteristic function $\chi _ { [ a , b ] }$ , but it’s not continuous, so we have to approximate.
Take sequences $f _ { k } , g _ { k }$ of continuous functions satisfying $0 \leqslant g _ { k } \leqslant$ $\chi _ { [ a , b ] } \leqslant f _ { k } \leqslant 1$ with $f _ { k }$ and $g _ { k }$ both converging Lebesgue almost everywhere to $\chi _ { [ a , b ] }$ . Then we have

$$
A _ { N } g _ { k } \ \leqslant \ A _ { N } \chi _ { [ a , b ] } \ \leqslant \ A _ { N } f _ { k } , \qquad I ( g _ { k } ) \ \leqslant \ I ( \chi _ { [ a , b ] } ) \ \leqslant \ I ( f _ { k } ) .
$$

Taking $N  \infty$ then gives

$$
I ( g _ { k } ) \ \leqslant \ \operatorname* { l i m } _ { N \to \infty } A _ { N } \chi _ { [ a , b ] } \ \leqslant \ \operatorname* { l i m } _ { N \to \infty } A _ { N } \chi _ { [ a , b ] } \ \leqslant \ I ( f _ { k } ) ,
$$

and by the Dominated Convergence Theorem taking $k \to \infty$ gives

$$
I ( \chi _ { [ a , b ] } ) \ \leqslant \ \operatorname* { l i m i n f } _ { N \to \infty } A _ { N } \chi _ { [ a , b ] } \ \leqslant \ \operatorname* { l i m } _ { N \to \infty } A _ { N } \chi _ { [ a , b ] } \ \leqslant \ I ( \chi _ { [ a , b ] } ) ,
$$

so they are all equal, as desired.
This finishes the proof because lim $N {  } \infty A _ { N } \chi _ { [ a , b ] }$ is exactly the expression on the left side and $I ( \chi _ { [ a , b ] } )$ is exactly the expression on the right side of the desired equation.

(c) Method 1. It’s enough to show that $\int f d \mu = \int f$ dm for all $f \in C ( \mathbb { T } )$ . Write

$$
\begin{array} { r l } { \displaystyle \int f ( x ) d \mu ( x ) - \displaystyle \int f ( z ) d m ( z ) } & { = \displaystyle \int \int ( f ( x ) - f ( z ) ) d m ( z ) d \mu ( x ) \ = \ \int \int ( f ( x ) - f ( x + z ) ) d m ( z ) d \mu ( x ) } \\ { \displaystyle } & { = \ \int \int ( f ( x ) - f ( x + z ) ) d \mu ( x ) d m ( z ) } \end{array}
$$

where the last equality is by Fubini and the second to last equality is by the translation invariance of ş $m .$ So it suffices to show that $\{ ( f ( x ) - f ( x + z ) ) d \mu ( x ) = 0$ for each fixed $z \in \mathbb { T }$ . By the density from part (b), there is a subsequence $n _ { j } \alpha  z { \mathrm { ~ a s ~ } } j  \infty$ Thus since $f$ is continuous and T is compact, we have $f ( x + n _ { j } \alpha ) \to f ( x + z )$ uniformly over $x \in \mathbb { T }$ as $j  \infty$ . Therefore, since we are assuming $\mu$ is invariant under rotations by α, we have

$$
\int ( f ( x ) - f ( x + z ) ) d \mu ( x ) ~ = ~ \int f ( x ) d \mu ( x ) - \int f ( x + z ) d \mu ( x ) ~ = ~ \int f ( x + n _ { j } \alpha ) d \mu ( x ) - \int f ( x + z ) d \mu ( x )
$$

for every $j ,$ and taking $j \to \infty$ makes the right side equal to 0 because the convergence is uniform and $f$ is continuous.

(c) Method 2 (motivated by ergodic theory).
Suppose α is irrational.
Then if $f$ is a trig polynomial, the same direct calculation from part (b) shows that

$$
A _ { N } f ( x ) \ : = \ { \frac { 1 } { N } } \sum _ { n = 0 } ^ { N - 1 } f ( x + n \alpha ) \to \int _ { \mathbb { T } } f d m
$$

as $N  \infty$ for any fixed $x \in \mathbb { T }$ . Let $\mu$ be any $R _ { \alpha }$ -invariant measure.
Then since trig polynomials are bounded, the Dominated Convergence Theorem gives

$$
\int A _ { N } f d \mu  \int ( \int f d m ) d \mu \ = \ \int f d m .
$$

But since $\mu$ is $R _ { \alpha }$ -invariant, the left side is equal to $\int f d \mu$ for all N. Thus $\int f d \mu = \int f$ dm for all trig polynomials $f ,$ and by density they are equal for all $f \in C ( { \overline { { \mathbb { T } } } } )$ , so by the Riesz representation theorem $\mu = m$ . □

Problem 5. Let $\left\{ f _ { n } \right\}$ be a sequence of continuous real-valued functions on r0, 1s and suppose $f _ { n } ( x )$ con\
verges to another real valued function $f ( x )$ at every $x \in [ 0 , 1 ]$\
(a) Prove that for every $\epsilon > 0$ there is a dense subset $D _ { \epsilon } \subseteq [ 0 , 1 ]$ such that if $x \in D _ { \epsilon }$ then there are an open\
interval $I \ni x$ and a positive integer $N _ { x }$ such that for all $\begin{array} { r } { n > N _ { x } , \operatorname* { s u p } _ { y \in I } | f _ { n } ( y ) - f ( y ) | \leqslant \epsilon } \end{array}$\
(b) Prove that f cannot be the characteristic function $\chi _ { \mathbb { Q } \cap \{ 0 , 1 \} }$

## Solution.

Problem 6. Let $f \in L ^ { 2 } ( \mathbb { R } )$ and assume the Fourier transform satisfies $\left| { \hat { f } } ( \xi ) \right| > 0$ for Lebesgue almost every $\xi \in \mathbb { R }$ . Prove the set of finite linear combinations of the translates $f _ { y } ( x ) = f ( x - y )$ is norm dense in $L ^ { 2 } ( \mathbb { R } )$

Solution.
See Spring 2012 # 6.

Problem 7. Let $f ( z )$ be an analytic function on the entire complex plane C such that the function $U ( z ) = \log | f ( z ) |$ is Lebesgue area integrable.
Prove f is constant.

Solution.
See Spring 2013 $\# 7$

Problem 8. Let D be the space of analytic function ş $f ( z )$ on the unit disc D such that $f ( 0 ) = 0$ and $\int _ { \mathbb { D } } | f ^ { \prime } ( z ) | ^ { 2 }$ dx $d y < \infty$

(a) Prove D is complete in the norm

$$
| | f | | \ = \ \left( \int _ { \mathbb { D } } | f ^ { \prime } ( z ) | ^ { 2 } d x d y \right) ^ { 1 / 2 } .
$$

(b) Give a necessary and sufficient condition on the coefficients $a _ { n }$ for the function $\begin{array} { r } { f ( z ) = \sum _ { n \geq 1 } a _ { n } z ^ { n } } \end{array}$ to belong to D.

Solution.
(a) Let $f _ { n }$ be a Cauchy sequence in D. Then by definition, $f _ { k } ^ { \prime }$ is a Cauchy sequence in $L ^ { 2 } ( \mathbb { D } )$ Since $L ^ { 2 }$ is known to be complete, there is some g with $f _ { k } ^ { \prime } \ \to \ g$ in $L ^ { 2 } ( \mathbb { D } )$ . We need to show that g is holomorphic, and for this we use the standard trick.
Fix $0 < r < 1$ , then for any $| z | \leqslant r$ and any $f \in { \mathcal { D } }$ we have

$$
| f ^ { \prime } ( z ) | = \left| \int _ { { \cal R } ( z , ( 1 - r ) / 2 ) } f ^ { \prime } ( w ) d { \cal A } ( w ) \right| \leqslant \int _ { { \cal B } ( z , ( 1 - r ) / 2 ) } | f ^ { \prime } ( w ) | d { \cal A } ( w ) \lesssim _ { r } \left( \int _ { { \cal R } ( z , ( 1 - r ) / 2 ) } | f ^ { \prime } ( w ) | ^ { 2 } d { \cal A } ( w ) \right) ^ { 1 / 2 } \leqslant | | f | | _ { \mathcal D } ,
$$

so $\| f ^ { \prime } \| _ { L ^ { \infty } \left( \overline { { B ( 0 , r ) } } \right) } \lesssim _ { r } \| f \| _ { \mathcal D }$ . Thus, since $f _ { n }$ is a Cauchy sequence in $\mathcal { D } , f _ { n } ^ { \prime }$ is a uniformly Cauchy sequence on $\overline { { B ( 0 , r ) } }$ . Since $L ^ { \infty } \left( \overline { { B ( 0 , r ) } } \right)$ is complete, we see that $f _ { n } ^ { \prime }$ converges uniformly to some limit function on $\overline { { B ( 0 , r ) } }$ . This holds for any $r < 1$ , so $f _ { n } ^ { \prime }$ has a locally uniform limit on D. But since $f _ { n } ^ { \prime }  g$ in $L ^ { 2 } ( \mathbb { D } )$ , it has a subsequence converging pointwise to $^ { g , }$ so in fact $f _ { n } ^ { \prime }  g$ locally uniformly on D, which implies g is holomorphic.
Let G be the unique primitive of g with $G ( 0 ) = 0$ . Then $| | f _ { n } - G | | _ { \mathcal { D } } = | | f _ { n } ^ { \prime } - g | | _ { L ^ { 2 } ( \mathbb { D } ) } \to 0 ,$ , so D is complete.

(b) We have $\begin{array} { r } { f ^ { \prime } ( z ) = \sum _ { n \geq 1 } n a _ { n } z ^ { n - 1 } } \end{array}$ . Write this as $\begin{array} { r } { f ^ { \prime } ( r e ^ { i \theta } ) = \sum _ { n \geq 1 } n a _ { n } r ^ { n - 1 } e ^ { i ( n - 1 ) \theta } } \end{array}$ and then we have

$$
\left| f ^ { \prime } ( r e ^ { i \theta } ) \right| ^ { 2 } ~ = ~ \sum _ { n , k \geqslant 1 } n k a _ { n } \overline { { { a _ { k } } } } r ^ { n + k - 2 } e ^ { i ( n - k ) \theta } ,
$$

so

$$
\begin{array} { r l } { \displaystyle \int _ { \mathbb { D } } | f ^ { \prime } ( z ) | ^ { 2 } d x d y = } & { \displaystyle \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 2 \pi } \sum _ { n , k \geq 1 } ^ { } n k d _ { n } \pi _ { n k } ^ { \alpha _ { k } - n + k - 2 } e ^ { i ( n - k ) \theta } r d \theta d r } \\ & { = \displaystyle \int _ { 0 } ^ { 1 } \sum _ { n , k \geq 1 } ^ { } n k d _ { n } \pi _ { n k } ^ { \alpha _ { k } } r ^ { n + k - 1 } \int _ { 0 } ^ { 2 \pi } e ^ { i ( n - k ) \theta } \mathrm { ~ b e c a u s e ~ t h e ~ s e r i c s ~ c o n v e r g e s ~ u n i f o r m l y ~ o n ~ c o m p a c t ~ s e t s } } \\ & { = \displaystyle \int _ { 0 } ^ { 1 } \sum _ { n \geq 1 } ^ { \infty } n ^ { 2 } | a _ { n } | ^ { 2 } r ^ { 2 n - 1 } d r \quad \mathrm { b y ~ o r t h o n o r m a l i t y } } \\ & { = \displaystyle \sum _ { n \geq 1 } ^ { \infty } n ^ { 2 } | a _ { n } | ^ { 2 } \int _ { 0 } ^ { 1 } r ^ { 2 n - 1 } d r \quad \mathrm { b y ~ t h e ~ M o n o t o n e ~ C o n v e r g e n c e ~ T h e o r e m } } \\ & { = \displaystyle \frac { 1 } { 2 } \sum _ { n \geq 1 } ^ { \infty } n | a _ { n } | ^ { 2 } . } \end{array}
$$

Thus a necessary and sufficient condition is that $\begin{array} { r } { \sum _ { n \geq 1 } n \left| a _ { n } \right| ^ { 2 } < \infty } \end{array}$

Problem 9. Consider the meromorphic function $g ( z ) = - \pi z \cot ( \pi z )$ on the entire plane C.

(a) Find all poles of g and determine the residue of g at each pole.ř

(b) In the Taylor series representation $\scriptstyle \sum _ { k = 0 } ^ { \infty } a _ { k } z ^ { k }$ of $g ( z )$ about $z = 0$ , show that for each $k \geqslant 1$

$$
a _ { 2 k } \ = \ \sum _ { n \geq 1 } { \frac { 2 } { n ^ { 2 k } } } .
$$

Solution.
See Spring 2013 # 11.

Problem 10. For $- 1 < \beta < 1$ evaluate

$$
\int _ { 0 } ^ { \infty } { \frac { x ^ { \beta } } { 1 + x ^ { 2 } } } d x .
$$

Solution.
See Spring 2014 $\# 1 1$

Problem 11. An analytic Jordan curve is a set of the form $\Gamma = f ( \{ | z | = 1 \} )$ where $f$ is analytic and one to one on an annulus $\{ r < | z | < 1 / r \} , 0 < r < 1$ Let $\mathbb { C } ^ { * } = \mathbb { C } \cup \{ \infty \}$ be the Riemann sphere, let $N < \infty ,$ , and let $\Omega \subseteq \mathbb { C } ^ { * }$ be a domain for which BΩ has N connected components, none of which are single points.
Prove there is a conformal mapping from Ω onto a domain bounded by N pairwise disjoint analytic Jordan curves.

Solution.

Problem 12. If $\alpha \in \mathbb { C }$ satisfies $0 < | \alpha | < 1$ and if $n \geqslant 1$ , show that the equation $e ^ { z } ( z - 1 ) ^ { n } = \alpha$ has exactly n simple roots in the half plane $\{ \mathrm { R e } ( z ) > 0 \}$ .

Solution.
