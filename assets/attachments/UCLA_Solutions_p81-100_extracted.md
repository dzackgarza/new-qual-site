and this tends to 0 as $| z | = r  \infty$

So pick R big enough so that $| g ( z ) | \leqslant M$ for all $z \in A$ with $| z | \geqslant R .$ Now $A \cap B ( 0 , R )$ is a bounded domain such that $| g ( z ) | \leqslant M$ everywhere on the boundary.
Thus, since g is holomorphic, it follows from the maximum principle that $| g | \leqslant M$ everywhere in $A \cap B ( 0 , R )$ . Thus by choice of $R , | g | \leqslant M$ on all of A. This means that for any $z \in A$

$$
| f ( z ) | \ \leqslant \ M \cdot \left| \exp ( \epsilon ( e ^ { - i \pi / 4 } z ) ^ { 3 / 2 } ) \right| .
$$

Since  is arbitrary, we can take $\epsilon \to 0$ and thus conclude that $| f ( z ) | \leqslant M$ for all $z \in A$

Since M is a bound for $| f ( z ) |$ on the entirety of the real and imaginary axes, we can repeat this argument in each of the other three quadrants and hence obtain that $| f ( z ) | \leqslant M$ for all $z \in \mathbb { C }$ , implying that f is a bounded entire function and thus f must be constant.
□

Problem 9. Let $\Omega = \{ z \in \mathbb { C } : | z | > 1$ and $\operatorname { R e } ( z ) > - 2 \}$ . Suppose $u : \overline { { \Omega } }  \mathbb { R }$ is bounded, continuous, and harmonic on Ω and also that $u ( z ) = 1$ when $| z | = 1$ and that $u ( z ) = 0$ when $\operatorname { R e } ( z ) = - 2$ . Determine $u ( 2 )$

Solution.
Note that Ω is a region on which the Dirichlet problem can be solved, so the function u is uniquely determined by its boundary values.
We want to conformally map Ω to an annulus, on which we can determine u easily.
Note that the map $z \mapsto 1 / z$ is a conformal map from Ω to $\Omega ^ { \prime } = \mathbb { D } \backslash \{ z \in \mathbb { C } : | z + 1 / 4 | \leqslant 1 / 4 \}$ We now want to conformally map Ω1 to the annulus $\left. z \in \mathbb { C } : r < | z | < 1 \right.$ . It suffices to find a conformal map which fixes the unit circle and maps 0 to r and $- 1 / 2$ to ´r. We know that the map

$$
\phi : z \to \frac { z - \alpha } { 1 - \overline { { \alpha } } z }
$$

fixes the unit circle, so we just need to pick an α such that $\phi ( 0 ) = r$ and $\phi ( - 1 / 2 ) = - r$ . Solving the system of equations, we find that $- \alpha = r = 2 - \sqrt { 3 }$ is the right choice.

So we know that $z \mapsto \phi ( 1 / z )$ is a conformal map from Ω to the annulus $A = \left\{ z \in \mathbb { C } : r < | z | < 1 \right\}$ with the line $\mathrm { R e } ( z ) = - 2$ mapping onto the inner circle $| z | = r$ and the unit circle mapping to itself.
So we find a harmonic function v on A with $v ( z ) = 0$ for $| z | = r$ and $v ( z ) = 1$ for $| z | = 1$ . The function

$$
v ( z ) ~ = ~ { \frac { \log | z / r | } { \log ( 1 / r ) } }
$$

accomplishes this.
Thus the original function u is given by

$$
u ( z ) ~ = ~ v ( \phi ( 1 / z ) ) ~ = ~ { \frac { 1 } { \log ( 1 / r ) } } \log \left| { \frac { 1 + r z } { r z + r ^ { 2 } } } \right| .
$$

So $\begin{array} { r } { u ( 2 ) = \frac { 1 } { \log ( 1 / r ) } \log \Big | \frac { 1 + 2 r } { 2 r + r ^ { 2 } } \Big | . \qquad \big | } \end{array}$

Problem 10. Determine

$$
\int _ { - \infty } ^ { \infty } { \frac { d y } { ( 1 + y ^ { 2 } ) ( 1 + ( x - y ) ^ { 2 } ) } }
$$

for all $x \in \mathbb { R }$

Solution.
For a fixed $x \in \mathbb { R }$ , integrate the function

$$
f ( z ) ~ = ~ \frac { 1 } { ( 1 + z ^ { 2 } ) ( 1 + ( x - z ) ^ { 2 } ) }
$$

around a half circle in the upper half plane from $R \mathrm { t o } - R$ and then along the real axis from ´R to R. After computing the residues and taking the limit (the contribution from the half circle goes to 0) you get that

the answer is $\frac { 2 \pi } { x ^ { 2 } + 4 }$

Problem 11. Let $\Omega = \mathbb { D } \backslash \{ 0 \}$ Prove that for every bounded harmonic function $u : \Omega \to \mathbb { R }$ there is a harmonic function $v : \Omega \to \mathbb { R }$ obeying

$$
{ \frac { \partial u } { \partial x } } \ = \ { \frac { \partial v } { \partial y } } , \quad { \frac { \partial u } { \partial y } } \ = \ - { \frac { \partial v } { \partial x } } .
$$

Solution.
Let ${ ^ { * } d u } = - u _ { y }$ dx $+ \ u _ { x }$ dy be the conjugate differential of u. We know that for any $0 < r < 1$ the function u satisfies

$$
\int _ { | z | = r } u ( r e ^ { i \theta } ) d \theta \ = \ \alpha \log ( r ) + \beta
$$

for some constants α and $\beta ,$ and α is given by the quantity

$$
\int _ { | z | = r } { ^ { * } d u } ,
$$

which is constant with respect to r. Since u is bounded on $\Omega ,$ write $| u | \leqslant M$ , then we have

$$
\left| \int _ { | z | = r } u ( r e ^ { i \theta } ) d \theta \right| \ \leqslant \ \int _ { | z | = r } | u ( r e ^ { i \theta } ) | d \theta \ \leqslant \ 2 \pi r M ,
$$

which tends to 0 as $r \to 0 ^ { + }$ This implies that we must have $\alpha = 0$ Thus in particular ş $\int _ { | z | = 1 / 2 } { ^ { \ast } d u } = 0 .$ Since the circle $| z | = 1 / 2$ forms a homology basis for Ω, this implies that $\int _ { \gamma } \ast d u = 0$ for any curve $\gamma \subseteq \Omega ,$ 2 so $^ { * } d u$ is an exact differential on Ω. This implies that there is a function v on Ω satisfying $d v = { ^ { * } d u } .$ , i.e. $v _ { x } = - u _ { y }$ and $v _ { y } = u _ { x }$ The only thing left to verify is that v is harmonic.
Note that we can define $f = u + i v$ on Ω and since $f$ satisfies the Cauchy-Riemann equations, it is holomorphic on Ω, and therefore its real and imaginary parts are harmonic, so v is harmonic on Ω.

Alternate solution.
It is a standard fact that a harmonic function on a simply connected domain has a harmonic conjugate.
So to show the existence of v it suffices to show that u can be extended to be harmonic on all of D. We know that u is continuous on the circle $| z | = 1 / 2 ,$ so let h be the function which is harmonic in $| z | < 1 / 2$ and solves the Dirichlet problem with boundary values $u ( w )$ for $| w | = 1 / 2$ . If we show that $u = h$ everywhere where they are both defined, then this shows that u can be extended to be harmonic at 0. Let $f = u - h$ Then f is a function which is harmonic in $| z | < 1 / 2$ and is equal to 0 everywhere on $| z | = 1 / 2$ . Also, since u and h are both bounded, f is bounded.
We now proceed with the standard  argument.
Fix $\epsilon > 0$ and consider the function $z \mapsto f ( z )$ \`  log |2z|. This function is harmonic in $| z | < 1 / 2$ and is equal to 0 on the boundary $| z | = 1 / 2$ . Furthermore, since f is bounded, this function tends $\mathrm { t o } - \infty$ as $z  0$ Therefore, we may pick $0 < r > 1 / 2$ such that $f ( z ) + \epsilon \log | 2 z | \leqslant 0$ for $| z | \leqslant r$ . Now since $f ( z ) +$  log |2z| is harmonic on $r < | z | < 1 / 2$ and vanishes on the boundary, by the maximum principle we conclude that $f ( z ) \leqslant - \epsilon \log | 2 z |$ for all $r < | z | < 1 / 2 .$ , and by choice of r we also have that $f ( z ) \leqslant - \epsilon \log | 2 z |$ for all $z \in \Omega$ . Now taking $\epsilon \to 0$ we conclude that $f ( z ) \leqslant 0$ for all $z \in \Omega .$ , so $u ( z ) \leqslant h ( z )$ in Ω. Now we can repeat the entire argument again with $\widetilde f : = h - u$ in place of $f ,$ and conclude that $h ( z ) \leqslant u ( z )$ in Ω, so $h = u$ and we are done.
□

Problem 12. Find all entire functions $f : \mathbb { C } \to \mathbb { C }$ that obey

$$
f ^ { \prime } ( z ) ^ { 2 } + f ( z ) ^ { 2 } ~ = 1 .
$$

Prove your list is exhaustive.

Solution.
By taking the derivative of the above equation, we see that a necessary condition is

$$
2 f ^ { \prime } ( z ) f ^ { \prime \prime } ( z ) + 2 f ( z ) f ^ { \prime } ( z ) \ = \ 2 f ^ { \prime } ( z ) ( f ^ { \prime \prime } ( z ) + f ( z ) ) \ = \ 0
$$

for all $z \in \mathbb { C }$ . This means we have $\{ z \in \mathbb { C } : f ^ { \prime } ( z ) = 0 \} \cup \{ z \in \mathbb { C } : f ^ { \prime \prime } ( z ) + f ( z ) = 0 \} = \mathbb { C }$ , so at least one of those sets must have a limit point, and since $f$ is holomorphic, both $f ^ { \prime }$ and $f ^ { \prime \prime } + f$ also are, and thus we either have $f ^ { \prime } = 0 \mathrm { ~ o r ~ } f ^ { \prime \prime } + f = 0$ on all of C.

If $f ^ { \prime } = 0$ , then $f$ is a constant, and the only constants which satisfy the original equation are $f ( z ) = \pm 1$ Now focus on the case $f ^ { \prime \prime } + f = 0$ We show that the most general function that satisfies this is given byř $f ( z ) = a \cos ( z ) + b \sin ( z )$ We can write $f$ as a power series $\begin{array} { r } { f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n } } \end{array}$ , and since $f ^ { \prime \prime } ( z ) = - f ( z )$ and power series can be differentiated term by term, we conclude that $a _ { n } = - ( n + 2 ) ( n + 1 ) a _ { n + 2 }$ for each $n .$ This shows that a solution $f$ is uniquely determined by its first two coefficients $a _ { 0 }$ and $a _ { 1 }$ , which means the set of solutions is a 2-dimensional subspace of the vector space of entire functions.
Since we know that $\cos ( z )$ and $\sin ( z )$ are two linearly independent solutions, it follows that $f ( z ) = a \cos ( z ) + b \sin ( z )$ is the most general solution.
Plugging this into the original condition, we get

$$
( - a \sin ( z ) + b \cos ( z ) ) ^ { 2 } + ( a \cos ( z ) + b \sin ( z ) ) ^ { 2 } \ = \ a ^ { 2 } + b ^ { 2 } \ = \ 1 .
$$

Thus we conclude that all of the solutions of the original equation are $f ( z ) = \pm 1 { \mathrm { ~ o r ~ } } f ( z ) = a \cos ( z ) + b \sin ( z )$ where $a ^ { 2 } + b ^ { 2 } = 1 . \square$

## 14 Fall 2015

Problem 1. Let $g _ { n }$ be a sequence of measurable functions on $\mathbb { R } ^ { d }$ , such that $| g _ { n } ( x ) | \leqslant 1$ for all x, and assume that $g _ { n } \to 0$ almost everywhere.
Let $f \in L ^ { 1 } ( \mathbb { R } ^ { d } )$ . Show that the sequence

$$
f * g _ { n } ( x ) = \int f ( x - y ) g _ { n } ( y ) \to 0
$$

uniformly on each compact subset of $\mathbb { R } ^ { d }$ , as $n \to \infty$

Solution.
Fix $r > 0$ and let $B _ { r }$ denote the closed ball of radius r centered at the origin.
We will show that $f * g _ { n }$ converges uniformly on $B _ { r }$

For an arbitrary $a > 0 .$ we and $x \in B _ { r }$ have

$$
\begin{array} { l } { \displaystyle | f * g _ { n } ( x ) | \leqslant \int | f ( x - y ) g _ { n } ( y ) | d y } \\ { \displaystyle = \int _ { B _ { a } } | f ( x - y ) | \cdot | g _ { n } ( y ) | d y + \int _ { \mathbb { R } \setminus B _ { a } } | f ( x - y ) | \cdot | g _ { n } ( y ) | d y } \\ { \displaystyle \leqslant \int _ { B _ { a } } | f ( x - y ) | \cdot | g _ { n } ( y ) | d y + \int _ { \mathbb { R } \setminus B _ { a } } | f ( x - y ) | d y } \end{array}
$$

We analyze each of these last two integrals separately.

For the second integral, we recall that $x \in B _ { r }$ , so we have

$$
\int _ { \mathbb { R } \backslash B _ { a } } | f ( x - y ) | \leqslant \int _ { \mathbb { R } \backslash B _ { a - r } } | f ( y ) | d y ,
$$

after a linear change of variables.
Then for fixed $\epsilon > 0$ we may choose an $a = a ( \epsilon )$ so that this integral is bounded by $\epsilon ^ { 2 }$

For the first integral, recall that the integral of an $L ^ { 1 }$ function over a set of small measure is small.
So byş Egarov we may find a measurable set $E \subseteq B _ { a }$ so that $f _ { n }  f$ uniformly on $B _ { a } \backslash E$ , and $\int _ { E } f ( x - y ) d y < \epsilon ^ { \prime } .$ Then for large enough n we have

$$
\begin{array} { r l } {  { \int _ { B _ { a } } | f ( x - y ) | \cdot | g _ { n } ( y ) | d y = \int _ { E } | f ( x - y ) | \cdot | g _ { n } ( y ) | d y + \int _ { B _ { a } \setminus E } | f ( x - y ) | \cdot | g _ { n } ( y ) | d y } } \\ & { \leqslant \int _ { E } | f ( x - y ) | d y + \epsilon ^ { \prime } \int _ { B _ { a } \setminus E } | g _ { n } ( y ) | d y } \\ & { \leqslant \epsilon ^ { \prime } ( 1 + \lambda _ { d } ( B _ { a } ) ) . } \end{array}
$$

Combining the two pieces, we have

$$
| f * g _ { n } ( x ) | \leqslant \epsilon ^ { \prime } \cdot ( 1 + \lambda _ { d } ( B _ { a ( \epsilon ) } ) ) + \epsilon .
$$

By choosing $\epsilon ^ { \prime } = \epsilon / ( 1 + \lambda _ { d } ( B _ { a ( \epsilon ) } ) )$ , we see that $| f * g _ { n } ( x ) | < 2 \epsilon$ for large enough n. Since this bound is independent of x, we conclude that $f * g _ { n } \to 0$ uniformly on $\begin{array} { r l } { B _ { r } . \quad } & { { } \sqcup } \end{array}$

Remark.
One can also solve this problem by first solving it when $f$ has compact support and then $\mathrm { a p - }$ plying an approximation argument.
This is equivalent, but perhaps conceptually simpler since some of the details get abstracted into the compact support case.

Problem 2. Let $f \in L ^ { p } ( \mathbb { R } ) , 1 < p < \infty$ , and let $a \in \mathbb { R }$ be such that $a > 1 - 1 / p$ . Show that the series

$$
\sum _ { n = 1 } ^ { \infty } \int _ { n } ^ { n + n ^ { - a } } \left| f ( x + y ) \right| d y
$$

converges for almost all $x \in \mathbb { R }$

Solution.
Let q be the conjugate exponent so that $1 / p + 1 / q = 1$ . Define

$$
g ( x ) ~ = ~ \sum _ { n = 1 } ^ { \infty } \int _ { n } ^ { n + n ^ { - a } } \left| f ( x + y ) \right| d y .
$$

With a change of variables we can write

$$
g ( x ) ~ = ~ \sum _ { n = 1 } ^ { \infty } n ^ { - a } \int _ { 0 } ^ { 1 } | f ( x + n + n ^ { - a } z ) | d z .
$$

Applying H¨older’s inequality for sums we have

$$
| g ( x ) | \ \leqslant \ \left( \sum _ { n = 1 } ^ { \infty } n ^ { - a q } \right) ^ { 1 / q } \left( \sum _ { n = 1 } ^ { \infty } \left( \int _ { 0 } ^ { 1 } | f ( x + n + n ^ { - a } z ) | d z \right) ^ { p } \right) ^ { 1 / p } .
$$

Since $a q > 1$ by hypothesis, the first term on the right side is just a constant C, and applying H¨older to the integral in the second term we get

$$
| g ( x ) | \leqslant C \left( \sum _ { n = 1 } ^ { \infty } \left( \left( \int _ { 0 } ^ { 1 } 1 ^ { q } \right) ^ { 1 / q } \left( \int _ { 0 } ^ { 1 } | f ( x + n + n ^ { - \alpha } z | ^ { p } d z \right) ^ { 1 / p } \right) ^ { p } \right) ^ { 1 / p } = C \left( \sum _ { n = 1 } ^ { \infty } \int _ { 0 } ^ { 1 } | f ( x + n + n ^ { - \alpha } z ) | ^ { p } d z \right) ^ { 1 / p } .
$$

To show $g$ is finite almost everywhere it is sufficient to show that $\int _ { N } ^ { N + 1 } | g ( x ) | ^ { p } d x < \infty$ for each $N \in \mathbb { Z }$ . We have

$$
\begin{array} { r } { \displaystyle \int _ { N } ^ { N + 1 } | g ( x ) | ^ { p } d x \ \leqslant \ C ^ { p } \displaystyle \int _ { N } ^ { N + 1 } \displaystyle \sum _ { n = 1 } ^ { \infty } \int _ { 0 } ^ { 1 } | f ( x + n + n ^ { - a } z ) | ^ { p } d z d x } \\ { \displaystyle = \ C ^ { p } \displaystyle \int _ { 0 } ^ { 1 } \displaystyle \sum _ { n = 1 } ^ { \infty } \int _ { N } ^ { N + 1 } | f ( x + n + n ^ { - a } z ) | ^ { p } d x d z } \end{array}
$$

by two applications of the Monotone Convergence Theorem and one application of Tonelli’s Theorem.
Changing variables again we get

$$
\begin{array} { r l r } {  { \int _ { N } ^ { N + 1 } | g ( x ) | ^ { p } d x \ \leqslant \ C ^ { p } \int _ { 0 } ^ { 1 } \sum _ { n = 1 } ^ { \infty } \int _ { N + n + n - a _ { z } } ^ { N + 1 + n + n - a _ { z } } | f ( u ) | ^ { p } d u d z } } \\ & { \leqslant \ C ^ { p } \int _ { 0 } ^ { 1 } \sum _ { n = 1 } ^ { \infty } \int _ { N + n } ^ { N + n + 2 } | f ( u ) | ^ { p } d u d z } \\ & { \leqslant \ C ^ { p } \displaystyle \int _ { 0 } ^ { 1 } 2 | | f | | _ { L ^ { p } } ^ { p } \ d z \ = \ 2 C ^ { p } | | f | | _ { L ^ { p } } ^ { p } \ < \ \infty . } \end{array}
$$

Thus $\int _ { N } ^ { N + 1 } | g | ^ { p }$ is finite for any integer N, so we conclude that $g ( x )$ is finite almost everywhere.

Problem 3. Let $f \in L _ { l o c } ^ { 1 } (  { \mathbb { R } } ^ { d } )$ be such that for some $0 < p < 1$ , we have

$$
\left| \int f ( x ) g ( x ) d x \right| \ \leqslant \ \left( \int | g ( x ) | ^ { p } \right) ^ { 1 / p } ,
$$

for all $g \in C _ { 0 } (  { \mathbb { R } } ^ { d } )$ (continuous functions with compact support).
Show that $f ( x ) = 0$ a.e.

Solution.

We would like to apply the condition of the problem when g is a characteristic function.
Unfortunately characteristic functions aren’t continuous, but we’re able to recover the same information via a suitable approximation.

Lemma.
Let K be a compact set.
Then $| \int _ { K } f ( x ) d x | \leqslant \lambda _ { d } ( K ) ^ { 1 / p } .$

Proof: Fix $\epsilon > 0$ and let U be an open set with compact closure containing K such that $\int _ { U \backslash K } | f ( x ) | d x < \epsilon$ (This is possible by continuity from above together with the fact that the integral of f over a set of small measure is small.)
By replacing U with a set of smaller measure if necessary, we may suppose in addition that $\lambda _ { d } ( U \backslash K ) < \epsilon$ . Let $g _ { K }$ be a continuous function $\mathbb { R } ^ { d } \to [ 0 , 1 ]$ which takes the value 1 on K and 0 outside of U (such a function exists by Urysohn).
We have

$$
\begin{array} { l } { \displaystyle \left. \int f ( x ) g _ { K } ( x ) d x - \int _ { K } f ( x ) d x \right. = \displaystyle \left. \int f ( x ) ( g _ { K } ( x ) - \chi _ { K } ( x ) ) d x \right. } \\ { \displaystyle \leqslant \int _ { U \backslash K } \lvert f ( x ) \rvert } \\ { \displaystyle < \epsilon . } \end{array}
$$

Then we have

$$
\begin{array} { l } { \displaystyle \left. \displaystyle \int _ { K } f ( \boldsymbol { x } ) d \boldsymbol { x } \right. \leqslant \epsilon + \displaystyle \left. \int f ( \boldsymbol { x } ) g _ { K } ( \boldsymbol { x } ) d \boldsymbol { x } \right. } \\ { \leqslant \epsilon + \left( \displaystyle \int \left. g _ { K } ( \boldsymbol { x } ) \right. ^ { p } \right) ^ { 1 / p } } \\ { \leqslant \epsilon + \lambda _ { d } ( U ) ^ { 1 / p } } \\ { \leqslant \epsilon + ( \lambda _ { d } ( K ) + \epsilon ) ^ { 1 / p } . } \end{array}
$$

But  was arbitrary, so we the lemma follows by taking the limit as $\epsilon \to 0 ^ { + }$

Now fix a cube $C \subseteq \mathbb { R } ^ { d }$ of side length s. For any positive integer N we may dissect C into $N ^ { d }$ cubes $\{ C _ { i } \} _ { i \in [ N ^ { d } ] }$ of side lengths $s / N$ . By the lemma,

$$
\int _ { C _ { i } } f ( x ) d x \leqslant \lambda _ { d } ( C _ { i } ) ^ { 1 / p } = \left( { \frac { s } { N } } \right) ^ { d / p } .
$$

Summing over all $C _ { i }$ we find that

$$
\int _ { C } f ( x ) d x \leqslant N ^ { d } \cdot \Big ( \frac { s } { N } \Big ) ^ { d / p } = s ^ { d / p } \cdot N ^ { d ( 1 - 1 / p ) } .
$$

But $1 - { \textstyle { \frac { 1 } { p } } } < 0$ , so the right-hand side tends to 0 as $N  \infty$ . Thus we conclude that $\int _ { C } f ( x ) d x$ for all cubes C.

Every open set is a union of countably many cubes with disjoint interiors.
Therefore ş $\int _ { U } f ( x ) d x = 0$ for any open set U. Then by continuity from above, $\textstyle \int _ { M } f ( x )$ must be zero for any measurable set M, from which it follows that f is 0 a.e.

Alternate solution.
Same idea as the first solution but the technical details are different.

Fix a large closed ball $S = \overline { { B ( 0 , R ) } }$ , it’s enough to show $f = 0 ~ \mathrm { a . e }$ . on S. Suppose not.
Then

Claim: There exists a ş $\delta > 0$ and a set $E \subseteq S$ with $\lambda ( E ) > 0$ with the property that for any subset $F \subseteq E$ $\left| \int _ { F } f ( x ) d x \right| > \delta \lambda ( F )$

Assume the claim for now.
A corollary of the claim is that there exist sets E of arbitrarily small positive measure satisfying the inequality in the claim.
Fix such a set E with measure small enough to satisfy $\delta \lambda ( E ) > \lambda ( E ) ^ { 1 / p }$ (possible because $1 / p > 1 )$ .

Fix $\epsilon > 0$ (assume w.l.o.g that $\epsilon < \lambda ( E ) / 1 0 )$ Since f is integrable on S, let $\alpha > 0$ be small enough so that $\lambda ( A ) < 2 \alpha$ and $A \subseteq S$ implies $\int _ { A } | f | < \epsilon$ . We may also pick $\alpha < \epsilon$ . Take a compact set K and an open

set U with $K \subseteq E \subseteq U \subseteq S$ and $\lambda ( E \backslash K ) , \lambda ( U \backslash E ) < \epsilon$ . Let g be a continuous function with $0 \leqslant g \leqslant 1 , g = 1$ on K, and $g = 0$ outside U. Then g also has compact support.
We have the estimates

$$
\begin{array} { r l } {  { ( \int | g ( x ) | ^ { p } d x ) ^ { 1 / p } = \ ( \int _ { K } | g ( x ) | ^ { p } + \int _ { U \setminus K } | g ( x ) | ^ { p } d x ) ^ { 1 / p } \ \leqslant \ ( \lambda ( K ) + 2 \epsilon ) ^ { 1 / p } \ \leqslant \ ( \lambda ( E ) + 2 \epsilon ) ^ { 1 / p } } } \\ & { \ | \int f ( x ) g ( x ) d x | = \ | \int _ { K } f ( x ) g ( x ) d x + \int _ { U \setminus K } f ( x ) g ( x ) d x | \ \geqslant \ | \int _ { K } f ( x ) d x | - \int _ { U \setminus K } | f ( x ) | d x } \\ & { \geqslant \ \delta \lambda ( K ) - \ \epsilon \ \geqslant \ \delta ( \lambda ( E ) + \epsilon ) - \epsilon \ = \ \delta \lambda ( E ) - ( \delta + 1 ) \epsilon . } \end{array}
$$

By the hypothesis of the problem, this implies

$$
\delta \lambda ( E ) - ( \delta + 1 ) \epsilon \ \leqslant \ ( \lambda ( E ) + 2 \epsilon ) ^ { 1 / p } .
$$

Since  was arbitrary, taking  Ñ 0 gives $\delta \lambda ( E ) \leqslant \lambda ( E ) ^ { 1 / p }$ , a contradiction by the choice of E at the beginning.

We need to prove the claim.
Suppose f is not a.e. 0. Then by continuity from below, there is some $\delta > 0$ such that $\lambda \{ x \in S : | f ( x ) | > 2 \delta \} > 0 .$ . For any k, we have the decomposition

$$
\begin{array} { r l } & { \{ x \in S : | f ( x ) | > 2 \delta \} = } \\ & { \{ x \in S : | f ( x ) | > 2 \delta , \arg ( f ) \in [ - 2 \pi / k , 2 \pi / k ) \} \cup \ldots \cup \{ x \in S : | f ( x ) | > 2 \delta , \arg ( f ) \in [ - 2 \pi ( k - 3 ) / k , 2 \pi ( k - 1 ) / k ) , \} } \end{array}
$$

so one of those sets has positive measure.
By multiplying f by a rotation, without loss of generality we can assume

$$
\lambda ( E ) : = \lambda \{ x \in S : | f ( x ) | > 2 \delta , \arg ( f ) \in [ - 2 \pi / k , 2 \pi / k ) \} \ > \ 0 .
$$

Let k be big enough so that $| f ( x ) | > 2 \delta$ and $\arg ( f ) \in [ - 2 \pi / k , 2 \pi / k )$ implies $\operatorname { R e } ( f ) > \delta$ . Then for any subset $F \subseteq E$ , we have

$$
\left| \int _ { \cal F } f \right| \geqslant \left| \int _ { \cal F } \mathrm { R e } ( f ) \right| > \delta \lambda ( F ) .
$$

This proves the claim, so we’re done.

Problem 4a. Let H be a separable infinite-dimensional Hilbert space and assume that $\left( e _ { n } \right)$ is an orthonormal system in H. Let $\left( f _ { n } \right)$ be another orthonormal system which is complete, i.e. the closure of theř span of $\left( f _ { n } \right)$ is all of H. Show that if $\begin{array} { r } { \sum _ { n = 1 } ^ { \infty } \left| \left| f _ { n } - e _ { n } \right| \right| ^ { 2 } < 1 } \end{array}$ then the orthonormal system $\left( e _ { n } \right)$ is also complete.

Solution.
Let v be a vector which is orthogonal to each of the ř $e _ { i }$ . It suffices to show that $v = 0 ,$ Since $( f _ { i } )$ is an orthonormal system, we can write ř $\begin{array} { r } { \dot { v } = \sum _ { n = 1 } ^ { \infty } \langle v , f _ { n } \rangle f _ { n } } \end{array}$ . Using this expression as motivation, we define $\textstyle w = \sum _ { n = 1 } ^ { \infty } \langle v , f _ { n } \rangle e _ { n }$ . Note that v and w are orthogonal, while the original condition suggests that they should be close in some suitable sense.
More precisely, by applying Cauchy-Schwarz we have

$$
\begin{array} { r l r } {  {   \boldsymbol { v } - \boldsymbol { w }   ^ { 2 } =   \sum _ { n = 1 } ^ { \infty }  \boldsymbol { v } , f _ { n }  ( f _ { n } - e _ { n } )   ^ { 2 } \leqslant ( \displaystyle \sum _ { n = 1 } ^ { \infty }   \boldsymbol { v } _ { n } , f _ { n }     f _ { i } - e _ { i }   ) ^ { 2 } } } \\ & { } & { \leqslant ( \displaystyle \sum _ { n = 1 } ^ { \infty }   \boldsymbol { v } , f _ { i }   ^ { 2 } ) \cdot ( \displaystyle \sum _ { n = 1 } ^ { \infty }   f _ { n } - e _ { n }   ^ { 2 } ) \leqslant   \boldsymbol { v }   ^ { 2 } . } \end{array}
$$

On the other hand, v and w are orthogonal, so $\left| \left| \boldsymbol { v } - \boldsymbol { w } \right| \right| ^ { 2 } = \left| \left| \boldsymbol { v } \right| \right| ^ { 2 } + \left| \left| \boldsymbol { w } \right| \right| ^ { 2 }$ . Thus $| | w | | ^ { 2 } = 0$ , and by our original definition of w we must have $\langle v , f _ { n } \rangle = 0$ for all n. Since $\left( f _ { n } \right)$ is a complete system, this means that $v = 0$ as desired.

Problem 4b. Assume we only have $\textstyle \sum _ { n = 1 } ^ { \infty } \left| \left| f _ { n } - e _ { n } \right| \right| ^ { 2 } < \infty$ . Prove that it is still true that $\left( e _ { n } \right)$ is complete.

Solution.
Let $E _ { N } = \overline { { { \mathrm { s p a n } } ( e _ { N } , e _ { N + 1 } , . . . ) } }$ and $F _ { N } = { \overline { { \operatorname { s p a n } ( f _ { N } , f _ { N + 1 } , . . . ) } } }$ . The condition that $\begin{array} { r } { \sum _ { n = 1 } ^ { \infty } \left| \left| f _ { n } - e _ { n } \right| \right| ^ { 2 } < } \end{array}$

8 tells us that for big $n , \ e _ { n }$ and $f _ { n }$ are very close together, so the subspaces $E _ { N }$ and $F _ { N }$ should also be “close together” when N is big enough.
For a closed subspace $M \subseteq { \mathcal { H } }$ , let $\pi _ { M } : \mathcal { H } \to M$ be the orthogonal projection onto M. We show that $| | \pi _ { E _ { N } } - \pi _ { F _ { N } } | | _ { o p } \to 0$ as $N  \infty$ (this is one way of saying the subspaces are close to each other).
For any $x \in \mathcal H$ we have

$$
\begin{array} { r l } { \| ( \pi _ { \mathrm { F } _ { N } } - \pi _ { \mathrm { F } _ { N } } ) ( x ) \| } & { = \bigg \| \displaystyle \sum _ { n = - N + 1 } ^ { \infty }  z , c _ { n } , c _ { n } , \zeta _ { n }  f _ { n } \bigg \| - \bigg \| \displaystyle \sum _ { n = - N + 1 } ^ { \infty }  z , c _ { n } , c _ { n } , \zeta _ { n }  + \displaystyle \sum _ { n = - N + 1 } ^ { \infty }  x , c _ { n } , \zeta _ { n } , - f _ { n } , \zeta _ { n }  } \\ & { \leqslant \displaystyle \sum _ { n = - N + 1 } ^ { \infty } \| ( \zeta , c _ { n } , e ) \| \| c _ { n } - f _ { n } \| + \bigg ( \bigg \| \displaystyle \sum _ { n = - N + 1 } ^ { \infty }  z , c _ { n } , - f _ { n } , \zeta _ { n }  f _ { n } \bigg \| ^ { 2 } \bigg ) ^ { 1 / 2 } } \\ & { \leqslant ( \displaystyle \sum _ { n = N + 1 } ^ { \infty } | ( \zeta , c _ { n } , \zeta _ { n } ) | ^ { 2 } ) ^ { 1 / 2 } ( \displaystyle \sum _ { n = - N + 1 } ^ { \infty } \| e _ { n } - f _ { n } \| ^ { 2 } ) ^ { 1 / 2 } + ( \displaystyle \sum _ { n = - N + 1 } ^ { \infty } |  x , e _ { n } - f _ { n } , \zeta  | ^ { 2 } ) ^ { 1 / 2 } } \\ & { \leqslant \| z \| ( \displaystyle \sum _ { n = - N + 1 } ^ { \infty } \| e _ { n } - f _ { n } \| ^ { 2 } ) ^ { 1 / 2 } + ( \displaystyle \sum _ { n = - N + 1 } ^ { \infty } \| z \| ^ { 2 } ) ^ { 1 / 2 } | c _ { n } - f _ { n } \| ^ { 2 } | ^ { 2 } \bigg ) ^ { 1 / 2 } } \\ &  \leqslant \| z \| \displaystyle \sum _ { n = - N + 1 } ^ { \infty } ( \ \end{array}
$$

where we have used Cauchy-Schwarz for sums, the Pythagorean theorem, and Cauchy-Schwarz in H. Thisř shows that $\begin{array} { r } { \left| \left| \pi _ { E _ { N } } - \pi _ { F _ { N } } \right| \right| _ { o p } ^ { 2 } \leqslant 4 \sum _ { n = N + 1 } ^ { \infty } \left| \left| e _ { n } - f _ { n } \right| \right| ^ { 2 } } \end{array}$ , which goes to 0 as $N  \infty$ by hypothesis.

We know that $\mathcal { H } = E _ { N } \oplus E _ { N } ^ { \perp }$ for any N because $E _ { N }$ is closed.
So to show that ${ \overline { { \operatorname { s p a n } ( \{ e _ { n } \} ) } } } = \mathcal { H } .$ it’s enough to find an N such that $\{ e _ { 1 } , \ldots , e _ { N } \}$ spans $E _ { N } ^ { \bot }$ . Since the $e _ { n }$ are orthonormal, we at least know that spa $\mathsf { \Gamma } _ { 1 } ( e _ { 1 } , \ldots , e _ { N } ) \subseteq E _ { N } ^ { \perp }$ for each N. The $e _ { j }$ are also independent, so it suffices to find an N such that dim $\left( E _ { N } ^ { \bot } \right) \ \leqslant \ N$ By the assumption that $\left\{ f _ { n } \right\}$ is a complete system, we also know that spanˇˇ $\mathfrak { c } ( f _ { 1 } , \dots , f _ { N } ) = F _ { N } ^ { \perp }$ , so dim $\left( F _ { N } ^ { \bot } \right) = N$ . Finally, since $\pi _ { S ^ { \perp } } = i d - \pi _ { S }$ for any closed subspace S, we haveˇˇ ˇˇ $| | \pi _ { E _ { N } ^ { \perp } } - \pi _ { F _ { N } ^ { \perp } } | | _ { o p } = | | \pi _ { E _ { N } } - \pi _ { F _ { N } } | | _ { o p } \to 0 { \mathrm { ~ a s ~ } } N \to \infty$ . Pick N to be large enough so that $\left| \left| \pi _ { E _ { N } ^ { \bot } } - \pi _ { F _ { N } ^ { \bot } } \right| \right| _ { o p } \leqslant 1 / 2 .$ Now the desired result follows from the following lemma.

Claim: Let S and T be two closed subspaces of H with $| | \pi _ { S } - \pi _ { T } | | _ { o p } \ \leqslant \ 1 / 2$ and dim $_ { \mathrm { ( } T \mathrm { ) } } = N < \infty$ Then dim $( S ) \leqslant N$

Proof: Let $x _ { 1 } , \ldots , x _ { N + 1 }$ be any $N + 1$ vectors in S. Then $\pi _ { T } ( x _ { 1 } ) , \dots , \pi _ { T } ( x _ { N + 1 } )$ are $N + 1$ vectors in an N-dimensional space, so we have

$$
0 ~ = ~ \alpha _ { 1 } \pi _ { T } ( x _ { 1 } ) + . . . + \alpha _ { N + 1 } \pi _ { T } ( x _ { N + 1 } ) ~ = ~ \pi _ { T } ( \alpha _ { 1 } x _ { 1 } + . . . + \alpha _ { N + 1 } x _ { N + 1 } )
$$

But also since each $x _ { j } \in S _ { }$ , we have $\pi _ { S } ( \alpha _ { 1 } x _ { 1 } + . . . + \alpha _ { N + 1 } x _ { N + 1 } ) = \alpha _ { 1 } x _ { 1 } + . . . + \alpha _ { N + 1 } x _ { N + 1 } , \mathrm { { s o } }$

$$
\begin{array} { r } { \begin{array} { r l } { \left| \left| \alpha _ { 1 } x _ { 1 } + \ldots + \alpha _ { N + 1 } x _ { N + 1 } \right| \right| } & { = \left| \left| \pi _ { S } \big ( \alpha _ { 1 } x _ { 1 } + \ldots + \alpha _ { N + 1 } x _ { N + 1 } \big ) - \pi _ { T } \big ( \alpha _ { 1 } x _ { 1 } + \ldots + \alpha _ { N + 1 } x _ { N + 1 } \big ) \right| \right| } \\ & { \leqslant \ \frac { 1 } { 2 } \left\| \alpha _ { 1 } x _ { 1 } + \ldots + \alpha _ { N + 1 } x _ { N + 1 } \right\| , } \end{array} } \end{array}
$$

which implies $\alpha _ { 1 } x _ { 1 } + . . . + \alpha _ { N + 1 } x _ { N + 1 } = 0$ , so the $x _ { j }$ are a dependent set.
So any set of $N + 1$ vectors in S is dependent, so dim $( S ) \leqslant N . \quad \bigtriangledown$

Problem 5. A function $f \in C ( \left[ 0 , 1 \right] )$ is called H¨older continuous of order $\delta > 0$ if there is a constant C such that $| f ( x ) - f ( y ) | \leqslant C | x - y | ^ { \delta }$ for all $x , y \in [ 0 , 1 ]$ . Show that the H¨older continuous functions form a meager set in $C ( [ 0 , 1 ] )$

Solution.
Define $\Lambda ^ { \delta }$ to be the set of all H¨older continuous functions of order δ on r0, 1s and let Λ be the set of all H¨older continuous functions of any order on r0, 1s. First note that $\delta > \eta$ implies that $\Lambda ^ { \delta } \subseteq \Lambda ^ { \eta }$ , so we can write

$$
\Lambda \ = \ \bigcup _ { n = 1 } ^ { \infty } \Lambda ^ { 1 / n } .
$$

Since a countable union of meager sets is meager, it suffices to show that $\Lambda ^ { \delta }$ is a meager subset of $C ( [ 0 , 1 ] )$ for any fixed δ. We can write

$$
\Lambda ^ { \delta } ~ = ~ \bigcup _ { m = 1 } ^ { \infty } \left\{ f \in \Lambda ^ { \delta } : \left. \left. f \right. \right. _ { \Lambda ^ { \delta } } \leqslant m \right\} ~ = : ~ \bigcup _ { m = 1 } ^ { \infty } E _ { m }
$$

where the norm $\vert \vert f \vert \vert _ { \Lambda ^ { \delta } }$ is defined by

$$
| f ( 0 ) | + \operatorname* { s u p } _ { x , y \in [ 0 , 1 ] } { \frac { | f ( x ) - f ( y ) | } { | x - y | ^ { \delta } } }
$$

(this is one of the standard norms on the space of H¨older continuous functions).
So it suffices to show that each $E _ { m }$ is closed and nowhere dense with respect to the $L ^ { \infty }$ norm.

To show $E _ { m }$ is closed, suppose that $f _ { n } \in E _ { m }$ and $f _ { n }$ converges uniformly to $f \in C ( [ 0 , 1 ] )$ . Fix $\epsilon > 0$ and for any $x , y \in [ 0 , 1 ]$ , let n be big enough so that $| f - f _ { n } | < \epsilon | x - y | ^ { \delta } \leqslant \epsilon \mathrm { ~ o n ~ } [ 0 , 1 ]$ . Then we have

$$
\begin{array} { r l } { | f ( 0 ) | + \displaystyle \frac { | f ( x ) - f ( y ) | } { | x - y | ^ { \delta } } } & { \leqslant \displaystyle | f ( 0 ) - f _ { n } ( 0 ) | + | f _ { n } ( 0 ) | + \displaystyle \frac { | f ( x ) - f _ { n } ( x ) | } { | x - y | ^ { \delta } } + \frac { | f _ { n } ( x ) - f _ { n } ( y ) | } { | x - y | ^ { \delta } } + \frac { | f _ { n } ( y ) - f ( y ) | } { | x - y | ^ { \delta } } } \\ & { \leqslant \ | | f _ { n } | | _ { \Lambda ^ { \delta } } + 3 \epsilon \leqslant M + 3 \epsilon , } \end{array}
$$

and since the left side does not depend on , we conclude that

$$
| f ( 0 ) | + \frac { | f ( x ) - f ( y ) | } { | x - y | ^ { \delta } } \ \leqslant \ m
$$

for all x, y, so $\vert \vert f \vert \vert _ { \Lambda ^ { \delta } } \leqslant m$ . Therefore $E _ { m }$ is closed.

For nowhere dense, let $f \in E _ { m }$ and fix $\epsilon > 0$ We just need to show the existence of some $h \notin \mathcal { E } _ { m }$ with $| | h - f | | _ { L ^ { \infty } } \leqslant \epsilon$ . Fix any $g \notin \Lambda ^ { \delta }$ (for example, $\overset { \cdot } { \boldsymbol { g } ( \boldsymbol { x } ) } = \boldsymbol { x } ^ { \delta / 2 }$ works) and by scaling, we may assume $| | g | | _ { L ^ { \infty } } = 1$ . Then let $\begin{array} { r } { h \ = \ f + \epsilon g } \end{array}$ . Then we clearly have $| | h - f | | _ { L ^ { \infty } } = \epsilon$ . Since $g \notin \Lambda ^ { \delta }$ , we can find points $x _ { n } , y _ { n }$ such that

$$
\frac { | g ( x _ { n } ) - g ( y _ { n } ) | } { | x _ { n } - y _ { n } | ^ { \delta } } \geqslant \frac { n } { \epsilon } .
$$

Then we have

$$
\begin{array} { r c l } { \displaystyle \frac { | h ( x _ { n } ) - h ( y _ { n } ) | } { | x _ { n } - y _ { n } | ^ { \delta } } ~ = ~ \frac { | f ( x _ { n } ) + \epsilon g ( x _ { n } ) - f ( y _ { n } ) - \epsilon g ( y _ { n } ) | } { | x _ { n } - y _ { n } | ^ { \delta } } } \\ { \displaystyle ~ \geqslant ~ \epsilon \frac { | g ( x _ { n } ) - g ( y _ { n } ) | } { | x _ { n } - y _ { n } | ^ { \delta } } - \frac { | f ( x _ { n } ) - f ( y _ { n } ) | } { | x _ { n } - y _ { n } | ^ { \delta } } ~ \geqslant ~ n - m , } \end{array}
$$

which goes to 8 as $n  \infty .$ , so $h \notin \Lambda ^ { \delta }$ . Therefore $E _ { m }$ is closed and nowhere dense, so we’re done.

Problem 6. Let $u \in L ^ { 2 } (  { \mathbb { R } } ^ { d } )$ and say that $u \in H ^ { 1 / 2 } ( \mathbb { R } ^ { d } )$ (a Sobolev space) if

$$
\left( 1 + | \xi | ^ { 1 / 2 } \right) \hat { u } ( \xi ) \in L ^ { 2 } ( \mathbb R ^ { d } ) .
$$

Here ˆu is the Fourier transform of u. Show that $u \in H ^ { 1 / 2 } ( \mathbb { R } ^ { d } )$ if and only if

$$
\iint \frac { | u ( x + y ) - u ( x ) | ^ { 2 } } { | y | ^ { d + 1 } } d x d y < \infty .
$$

Solution.
Since \` ˘ $u \in L ^ { 2 } ( \mathbb { R } ^ { d } )$ , we know immediately that $\hat { u } \in L ^ { 2 } ( \mathbb R ^ { d } )$ also, so we just need to show that $\left( 1 + | \xi | ^ { 1 / 2 } \right) \hat { u } ( \xi ) \in L ^ { 2 } ( \mathbb { R } ^ { d } )$ if and only if the above double integral is finite.
It suffices to prove that

$$
\int | \xi | | \hat { u } ( \xi ) | ^ { 2 } d \xi \lesssim \iint \frac { | u ( x + y ) - u ( x ) | ^ { 2 } } { | y | ^ { d + 1 } } d x d y \lesssim \int | \xi | | \hat { u } ( \xi ) | ^ { 2 } d \xi ,
$$

where throughout this problem $\lesssim$ denotes an implied constant which depends only on $d .$ First note that by Plancherel, we have

$$
\begin{array} { r } { \displaystyle \int \int \displaystyle \frac { | u ( x + y ) - u ( x ) | ^ { 2 } } { | y | ^ { d + 1 } } d x d y \ = \ \displaystyle \int \frac { 1 } { | y | ^ { d + 1 } } \int | 1 - e ^ { 2 \pi i y \cdot \xi } | ^ { 2 } | \hat { u } ( \xi ) | ^ { 2 } d \xi d y \ = \ \displaystyle \int | \hat { u } ( \xi ) | ^ { 2 } \int \displaystyle \frac { | 1 - e ^ { 2 \pi i y \cdot \xi } | ^ { 2 } } { | y | ^ { d + 1 } } d y d \xi , } \end{array}
$$

so it now suffices just to prove the estimates

$$
| \xi | \lesssim \int \frac { \big | 1 - e ^ { 2 \pi i y \cdot \xi } \big | ^ { 2 } } { | y | ^ { d + 1 } } d y \lesssim | \xi | .
$$

For the upper bound, we have the estimate

$$
\begin{array} { r } { \begin{array} { l l l } { \displaystyle \int \frac { \left| 1 - e ^ { 2 \pi i y \xi } \right| ^ { 2 } } { | y | ^ { d + 1 } } d y \ = \ \displaystyle \int _ { | y | \leq 1 / ( 2 | \xi | ) } \frac { \left| 1 - e ^ { 2 \pi i y \xi } \right| ^ { 2 } } { | y | ^ { d + 1 } } d y + \displaystyle \int _ { | y | > 1 / ( 2 | \xi | ) } \frac { \left| 1 - e ^ { 2 \pi i y \xi } \right| ^ { 2 } } { | y | ^ { d + 1 } } d y } \\ { \displaystyle \leqslant \ \displaystyle \int _ { | y | \leq 1 / ( 2 | \xi | ) } \frac { \left| 4 \pi y \cdot \xi \right| ^ { 2 } } { | y | ^ { d + 1 } } d y + \displaystyle \int _ { | y | > 1 / ( 2 | \xi | ) } \frac { 4 } { | y | ^ { d + 1 } d y } \mathrm { ~ b e c a u s e ~ } | 1 - e ^ { 2 } | \leqslant 2 | z | \mathrm { ~ f o r ~ } | z | \leqslant 1 / 2 } \\ { \displaystyle \lesssim \ | \xi | ^ { 2 } \displaystyle \int _ { | y | \leq 1 / ( 2 | \xi | ) } \frac { | y | ^ { 2 } } { | y | ^ { d + 1 } } d y + \displaystyle \int _ { | y | > 1 / ( 2 | \xi | ) } \frac { 1 } { | y | ^ { d + 1 } } d y } \\ { \displaystyle \lesssim \ | \xi | + | \xi | \lesssim \ | \xi | . } \end{array} } \end{array}
$$

Now we do the lower bound.
For ξ fixed, define $E = \{ y \in \mathbb { R } ^ { d } : | y \cdot \xi | \geqslant ( 1 / 2 ) | y | | \xi | \}$ . We estimate

$$
\begin{array}{c} \begin{array} { r } { \begin{array} { r l } { \displaystyle \int \frac { \left| 1 - e ^ { 2 \pi i y \cdot \xi } \right| ^ { 2 } } { | y | ^ { d + 1 } } d y } & { \geqslant } \end{array} \int _ { | y | \leqslant 1 / ( 3 | \xi | ) , y \in E } \frac { \left| 1 - e ^ { 2 \pi i y \cdot \xi } \right| ^ { 2 } } { | y | ^ { d + 1 } } d y } \\ & { \geqslant \displaystyle \int _ { | y | \leqslant 1 / ( 3 | \xi | ) , y \in E } \frac { \left| \pi y \cdot \xi \right| ^ { 2 } } { | y | ^ { d + 1 } } d y \mathrm { ~ ~ b e c a u s e ~ } | e ^ { z } - 1 | \geqslant ( 1 / 2 ) | z | \mathrm { ~ f o r ~ } | z | \leqslant 1 / 3 } \\ & { \gtrsim \displaystyle \int _ { | y | \leqslant 1 / ( 3 | \xi | ) , y \in E } \frac { ( 1 / 2 ) | y | ^ { 2 } | \xi | ^ { 2 } } { | y | ^ { d + 1 } } d y \gtrsim | \xi | ^ { 2 } \int _ { | y | \leqslant 1 / ( 3 | \xi | ) , y \in E } \frac { 1 } { | y | ^ { d - 1 } } d y . } \end{array}  \end{array}
$$

Now note that membership in E is determined only by the direction of y and is independent of the magnitude of $y .$ So since the above integrand is a function only of $| y |$ , and $E$ takes up a “positive proportion” of all of $\mathbb { R } ^ { d }$ (this can be made precise), it follows that the above integral is

$$
\gtrsim ~ | \xi | ^ { 2 } \int _ { | y | \leqslant 1 / ( 3 | \xi | ) } \frac { 1 } { | y | ^ { d - 1 } } d y \ \gtrsim \ | \xi | ,
$$

which concludes the proof of the lower bound, so we are done.

Problem 7. Assume that $f ( z )$ is analytic in D and continuous on ${ \overline { { \mathbb { D } } } } .$ . If $f ( z ) ~ = ~ f ( 1 / z )$ when $| z | = 1$ prove that $f ( z )$ is constant.

Solution.
Define the function $g$ by

$$
g ( z ) \ : = \ \left\{ { \begin{array} { l l } { f ( z ) } & { | z | \leqslant 1 } \\ { f ( 1 / z ) } & { | z | \geqslant 1 } \end{array} } . \right.
$$

Because of the condition that $f ( z ) = f ( 1 / z )$ for $| z | = 1$ , we see that $g$ is continuous on all of C. We now mimic the proof of the Schwarz reflection principle to show that g is analytic on all of C. By Morera’s theorem, it is enough to show that

$$
\int _ { \hat { \sigma } R } g ( z ) d z \ = \ 0
$$

for any rectangle R. It is clear from the definition that g is analytic inside D and so we don’t need to consider rectangles R that are contained in D. Also, since $z \mapsto 1 / z$ is a conformal map from $\mathbb { C } \backslash \mathbb { D }$ into $\mathbb { D } \backslash \{ 0 \}$ u, we also see that $g$ is analytic on the exterior of D, so we also don’t need to consider rectangles that are contained in the exterior of D. Thus we only need to consider rectangles which intersect the unit circle.
For such a rectangle, split the contour along the arc of the unit circle into a band of width $\delta$ (this is hard to explain without a picture).
Since $g$ is analytic on both the inside and the outside of D, the integral over this split contour is necessarily 0. Then, since $g$ is continuous everywhere, as we let $\delta \to 0$ , the integral over the splitş contour approaches the integral over the original rectangle, and so we conclude that $\int _ { \partial R } g ( z ) d z = 0$ for all rectangles R and thus g is analytic on all of C.

Now note that since $f$ is continuous on ${ \overline { { \mathbb { D } } } } ,$ which is compact, $f$ must be bounded, and thus g must also be bounded.
But g is entire, so g must be a constant, which means $f$ must also be a constant.

Problem 8. Assume that $f ( z )$ is an entire function that is 2π-periodic in the sense that $f ( z + 2 \pi ) = f ( z )$ and

$$
| f ( x + i y ) | \ \leqslant \ C e ^ { \alpha | y | }
$$

for some $C > 0$ , where $0 < \alpha < 1$ . Prove that $f$ is constant.

Solution.
Since $f ( z )$ is 2π periodic, we can express f as the pullback of a holomorphic function on the cylinder.
More formally, we can write

$$
f ( z ) = g ( e ^ { i z } )
$$

where we define g on $\mathbb { C } \backslash \{ 0 \}$ by $\begin{array} { r } { g ( z ) = f ( \frac { 1 } { i } \log ( z ) ) } \end{array}$ . Since f is 2π-periodic, the branch of log is irrelevant, and $g$ is well-defined.

The given bound implies that $| g ( e ^ { y } \cdot e ^ { i x } ) | \leqslant C e ^ { \alpha | y | }$ . Thus we have

$$
\begin{array} { r } { | g ( z ) | \leqslant C \exp ( \alpha | \log | z | | ) . } \end{array}
$$

$\mathrm { A s } \ | z | \to 0$ , we have $| g ( z ) | \leqslant C z ^ { - \alpha }$ , but $\alpha < 1$ , so g has a removable singularity at 0, and we can extend g to an analytic function on C. Similarly as $| z | \to 0$ , we have $| g ( z ) | \leqslant C z ^ { \alpha }$ , and so $g$ must be constant.
This immediately implies that f is constant.

Problem 9. Let $( f _ { j } )$ be a sequence of entire functions such that, writing $z = x + i y$ , we have

$$
\iint _ { \mathbb { C } } | f _ { j } ( z ) | ^ { 2 } e ^ { - | z | ^ { 2 } } d x d y \ \leqslant \ C , \quad j = 1 , 2 , \ldots
$$

for some constant $C > 0$ . Show that there exists a subsequence $( f _ { j _ { k } } )$ and an entire function $f$ such that we have

$$
\int \displaylimits _ { \mathbb { C } } | f _ { j _ { k } } ( z ) - f ( z ) | ^ { 2 } e ^ { - 2 | z | ^ { 2 } } d x d y \to 0 , \quad k \to \infty .
$$

Solution.
By the mean value property and Cauchy-Schwarz, for any $z \in \mathbb { C }$ with $| z | \geqslant 2$ and any $j$ we can write

$$
| f _ { j } ( z ) | \lesssim \int _ { B ( z , 1 ) } | f _ { j } ( w ) | \ d x d y \lesssim \left( \int _ { B ( z , 1 ) } | f _ { j } ( w ) | ^ { 2 } \ d x d y \right) ^ { 1 / 2 } \leqslant e ^ { \frac { 1 } { 2 } ( | z | + 1 ) ^ { 2 } } \left( \int _ { B ( z , 1 ) } | f _ { j } ( w ) | ^ { 2 } e ^ { - | w | ^ { 2 } } d x d y \right) ^ { 1 / 2 } \leqslant C e ^ { \frac { 1 } { 2 } ( | z | + 1 ) ^ { 2 } } .
$$

In particular, this implies that the sequence $\{ f _ { j } \}$ is uniformly bounded on every compact subset of $\mathbb { C } ,$ , so it is a normal family.
Thus it has a subsequence $\left\{ f _ { j _ { k } } \right\}$ which converges uniformly on every compact subset of C. Since each $f _ { j }$ is entire, we also know that the limit function f is entire and also satisfies the estimate

$$
\begin{array} { r } { | f ( z ) | \lesssim e ^ { \frac { 1 } { 2 } ( | z | + 1 ) ^ { 2 } } . } \end{array}
$$

for $| z | \geqslant 2$

To show the desired conclusion, fix $\epsilon > 0$ . Let R be big enough so that

$$
\int _ { | z | > R } e ^ { - | z | ^ { 2 } + | z | + 1 } d x d y < \epsilon .
$$

Since $f _ { j _ { k } } \to f$ uniformly on every compact subset of $\mathbb { C } ,$ we may choose k to be big enough so that

$$
\int _ { | z | \leqslant R } | f _ { j _ { k } } ( z ) - f ( z ) | ^ { 2 } e ^ { - 2 | z | ^ { 2 } } d x d y \ < \ \epsilon .
$$

Thus we have the estimate

$$
\begin{array} { r l } { \displaystyle \int _ { \mathbb { C } } | f _ { j _ { k } } ( z ) - f ( z ) | ^ { 2 } e ^ { - 2 | z | ^ { 2 } } d x d y \ = \ \displaystyle \int _ { | z | \leq R } | f _ { j _ { k } } ( z ) - f ( z ) | ^ { 2 } e ^ { - 2 | z | ^ { 2 } } d x d y + \displaystyle \int _ { | z | > R } | f _ { j _ { k } } ( z ) - f ( z ) | ^ { 2 } e ^ { - 2 | z | ^ { 2 } } d x d y } & { } \\ { \displaystyle < \ \epsilon + \displaystyle \int _ { | z | > R } ( C ^ { \prime } \cdot 2 e ^ { \frac { 1 } { 2 } ( | z | + 1 ) ^ { 2 } } ) ^ { 2 } e ^ { - 2 | z | ^ { 2 } } d x d y } & { } \\ { \displaystyle \leqslant \ \epsilon + C ^ { \prime \prime } \displaystyle \int _ { | z | > R } e ^ { - | z | ^ { 2 } + | z | + 1 } d x d y \ < \ ( 1 + C ^ { \prime \prime } ) \epsilon , } \end{array}
$$

which establishes the desired conclusion.

Problem 10. Use the Residue Theorem to prove that

$$
\int _ { 0 } ^ { \infty } e ^ { \cos x } \sin ( \sin x ) { \frac { d x } { x } } \ = \ { \frac { \pi } { 2 } } ( e - 1 )
$$

Use a large semicircle as part of the contour.

Solution.
For real $x ,$ the integrand can be written as ${ \scriptstyle { \frac { 1 } { x } } } \operatorname { I m } ( e ^ { e ^ { i x } } )$ . We can rewrite our integral as

$$
\int _ { 0 } ^ { \infty } \mathrm { I m } ( e ^ { e ^ { i x } } ) \frac { d x } { x } = \mathrm { I m } \int _ { - \infty } ^ { \infty } e ^ { e ^ { i x } } \frac { d x } { x } ,
$$

where the equality holds provided the second integral exists (which it will).

Set $\textstyle f ( z ) = { \frac { 1 } { z } } e ^ { e ^ { i z } }$ and let $\Gamma _ { R }$ denote a large semicircular contour of radius R with endpoints $\mathrm { a t } - R$ and R. Also let $\gamma _ { r }$ denote a small clockwise contour of radius r with endpoints at ´r and $r .$

Note that f is holomorphic everywhere except $z = 0$ , where it has a simple pole with residue $e .$ Thus by (a variant of) the residue theorem for “indented contours”, we have

$$
\operatorname* { l i m } _ { r \to 0 } \int _ { \gamma _ { r } } f ( z ) d z = - { \frac { 1 } { 2 } } \cdot 2 \pi i \cdot e = - i \pi e .
$$

On the outer contour we have

$$
\int _ { \Gamma _ { R } } f ( z ) d z = i \int _ { 0 } ^ { \pi } e ^ { e ^ { i R \exp ( i \theta ) } } d \theta .
$$

Note that for $\theta \in [ 0 , \pi ]$

$$
\left| e ^ { i R \exp ( i \theta ) } \right| = e ^ { - R \sin ( \theta ) } \leqslant 1 .
$$

Thus by the bound $| e ^ { z } | \leqslant e ^ { | z | }$ , our integrand is dominated by e. Also as $R \to \infty$ , the same bound shows that the integrand tends pointwise to $e ^ { 0 } = 1$ (except at $\theta = 0$ and $\theta = \pi )$ , so by dominated convergence,

$$
\int _ { \Gamma _ { R } } f ( z ) d z \to i \pi { \mathrm { ~ a s ~ } } R \to \infty .
$$

By Cauchy’s applying Cauchy’s theorem to a contour joining the two semicircles, we have

$$
0 = 2 \int _ { - r } ^ { R } f ( z ) d z + \int _ { \gamma _ { r } } f ( z ) d z + \int _ { \Gamma _ { R } } f ( z ) d z ,
$$

and taking the limit as $r \to 0$ and $R \to \infty$ gives

$$
\int _ { 0 } ^ { \infty } f ( x ) d x = i \frac { \pi } { 2 } ( e - 1 ) .
$$

Finally, the imaginary part of this is the desired value.

Problem 11. Let $\Omega = \{ ( x , y ) \in \mathbb { R } ^ { 2 } : x > 0 , y > 0 \}$ and let u be subharmonic in Ω, continuous in ${ \overline { { \Omega } } } ,$ such that

$$
u ( x , y ) \ \leqslant \ | x + i y | ,
$$

for large $( x , y ) \in \Omega$ . Assume that

$$
u ( x , 0 ) \ \leqslant \ a x , \quad u ( 0 , y ) \ \leqslant \ b y , \quad x , y \geqslant 0 ,
$$

for some $a , b > 0$ . Show that

$$
u ( x , y ) \ \leqslant \ a x + b y , \quad ( x , y ) \in \Omega .
$$

Solution.
We use the Phregman-Linedl¨of method.
Fix $\epsilon > 0$ and, writing $( x , y ) = r e ^ { i \theta }$ , define

$$
\phi ( x , y ) ~ = ~ a x + b y + \epsilon r ^ { 3 / 2 } \cos \left( \frac { - 3 \pi } { 8 } + \frac { 3 \theta } { 2 } \right) .
$$

Note that $\epsilon r ^ { 3 / 2 } \cos { \left( \frac { - 3 \pi } { 8 } + \frac { 3 \theta } { 2 } \right) }$ is the real part of the function $f ( z ) = - \epsilon ( e ^ { - i \pi / 4 } z ) ^ { 3 / 2 }$ , which is single-valued and analytic in Ω, so φ is harmonic in Ω (because $a x + b y$ is clearly harmonic).
Thus, since u is subharmonic in Ω, we know that $v : = u - \phi$ does not have any local maximum in Ω.

We want to show that $v ( x , y ) \to - \infty { \mathrm { ~ a s ~ } } r \to \infty$ in Ω. Note that since for $( x , y ) \in \Omega$ we have $\theta \in ( 0 , \pi / 2 )$ , we have $- 3 \pi / 8 + 3 \theta / 2 \in ( - 3 \pi / 8 , 3 \pi / 8 )$ and thus $\cos ( - 3 \pi / 8 + 3 \theta / 2 ) > \cos ( 3 \pi / 8 ) = : \delta > 0$ . So as $r \to \infty$ , by the hypothesis that $u ( x , y ) < r$ for r sufficiently large, we have

$$
v ( x , y ) ~ = ~ u ( x , y ) - a x - b y - \epsilon r ^ { 3 / 2 } \cos \left( \frac { - 3 \pi } { 8 } + \frac { 3 \theta } { 2 } \right) ~ \leqslant ~ r - \epsilon \delta r ^ { 3 / 2 } \to - \infty
$$

as $r  \infty$ . Thus we can pick an R large enough so that $v ( x , y ) \leqslant 0$ for all $r \geqslant R .$ . We also know from the other hypotheses that on the x-axis,

$$
v ( x , 0 ) = u ( x , y ) - a x - \epsilon r ^ { 3 / 2 } \cos \left( \frac { - 3 \pi } { 8 } + \frac { 3 \theta } { 2 } \right) ~ \leqslant ~ 0
$$

and similarly on the y-axis $v ( 0 , y ) \leqslant 0$ . Thus we can now apply the maximum principle to v on the bounded region $\left\{ ( x , y ) \in \Omega : r \leqslant R \right\}$ , and since $v \leqslant 0$ on the boundary, we conclude that $v \leqslant 0$ throughout the entire region, and thus by choice of $R , v ( x , y ) \leqslant 0$ for all $( x , y ) \in \Omega$ . This means that

$$
u ( x , y ) ~ \leqslant ~ a x + b y + \epsilon r ^ { 3 / 2 } \cos \left( \frac { - 3 \pi } { 8 } + \frac { 3 \theta } { 2 } \right)
$$

for each $( x , y ) \in \Omega$ , and since  is arbitrary, we conclude that $u ( x , y ) \leqslant a x + b y$ for all $( x , y ) \in \Omega . \qquad \bigsqcup$

Problem 12. Find a function $u ( x , y )$ harmonic in the region between the circles $| z | = 2$ and $| z - 1 | = 1$ which equals 1 on the outer circle and 0 on the inner circle (except at the point where the circles are tangent to each other).

Solution.
Let $\Omega = \{ z \in \mathbb { C } : | z | < 2 , | z - 1 | > 1 \}$ be the original region.
We want to conformally map Ω to a region on which such a function can easily be found and then pull it back.
The map $z \mapsto 1 / ( z - 2 )$ sends Ω to the strip $\{ z \in \mathbb { C } : - 1 / 2 < \mathrm { R e } ( z ) < - 1 / 4 \}$ , with the circle $| z | = 2$ going to the line $\operatorname { R e } ( z ) = - 1 / 4$ and the circle $| z - 1 | = 1$ going to the circle $\operatorname { R e } ( z ) = - 1 / 2$ . So we are looking for a harmonic function v which satisfies $v ( z ) = 0$ when $\operatorname { R e } ( z ) = - 1 / 2$ and $v ( z ) = 1$ when $\operatorname { R e } ( z ) = - 1 / 4$ The function $v ( z ) = \mathrm { R e } ( 4 z + 2 )$ clearly satisfies this and is harmonic because it is the real part of an analytic function.
Therefore the function

$$
u ( z ) ~ = ~ v \left( { \frac { 1 } { z - 2 } } \right) ~ = ~ \operatorname { R e } \left( { \frac { 4 } { z - 2 } } + 2 \right) ~ = ~ \operatorname { R e } \left( { \frac { 2 z } { z - 2 } } \right)
$$

is a harmonic function on Ω with the desired properties.

## 15 Spring 2016

Problem 1a. Let

$$
K _ { t } ( x ) \ = \ ( 4 \pi t ) ^ { - 3 / 2 } e ^ { - | x | ^ { 2 } / 4 t } , \quad x \in \mathbb { R } ^ { 2 } , \ t > 0 ,
$$

where $| x |$ is the Euclidean norm of $\mathbb { R } ^ { 3 }$ . Show that the linear map

$$
f \ \mapsto \ t ^ { 1 / 2 } ( K _ { t } * f ) , \quad L ^ { 3 } ( \mathbb { R } ^ { 3 } ) \to L ^ { \infty } ( \mathbb { R } ^ { 3 } )
$$

is bounded uniformly in $t > 0$

Solution.
Throughout this problem, we use the symbol $\lesssim$ to denote an implied constant which does not depend on $f , x \mathrm { ~ o r ~ } t .$ . For any $x \in \mathbb { R } ^ { 3 }$ , we calculate

$$
\Big | \mathtt { t } ^ { 1 / 2 } ( K _ { t } * f ) ( x ) \Big | \lesssim t ^ { - 1 } \int _ { \mathbb { R } ^ { 3 } } \mathtt { e x p } \left( \frac { - 1 } { 4 t } | x - y | ^ { 2 } \right) | f ( y ) | d y \leqslant t ^ { - 1 } \left( \int _ { \mathbb { R } ^ { 3 } } | f ( y ) | ^ { 3 } d y \right) ^ { 1 / 3 } \left( \int _ { \mathbb { R } ^ { 3 } } \exp \left( \frac { - 3 } { 8 t } | x - y | ^ { 2 } d y \right) \right) ^ { 2 / 3 }
$$

by H¨older’s inequality.
Making the change of variables $\begin{array} { r } { z = \frac { \sqrt { 3 } } { \sqrt { 8 } } ( x - y ) } \end{array}$ in the last integral, we $\mathrm { g e t }$

$$
\begin{array} { r l r } {  {  t ^ { 1 / 2 } ( K _ { t } \ast f ) ( x )  \ \lesssim \ t ^ { - 1 } \| f \| _ { L ^ { 3 } } ( \int _ { \mathbb { R } ^ { 3 } } \exp ( -  \frac { z } { \sqrt { t } }  ^ { 2 } ) d z ) ^ { 2 / 3 } } } \\ & { = } & { t ^ { - 1 } \| f \| _ { L ^ { 3 } } ( ( \int _ { \mathbb { R } } \exp ( - ( u / \sqrt { t } ) ^ { 2 } ) d u ) ^ { 3 } ) ^ { 2 / 3 } \ \mathrm { b y ~ T o n e l l i j s ~ t h e o r e m } } \\ & { \lesssim \ t ^ { - 1 } \| f \| _ { L ^ { 3 } } ( \sqrt { \pi t } ) ^ { 2 } \ \lesssim \| f \| _ { L ^ { 3 } } . } \end{array}
$$

Thus $\big | \big | t ^ { 1 / 2 } ( K _ { t } * f ) \big | \big | _ { L ^ { \infty } } \lesssim | | f | | _ { L ^ { 3 } }$ , so we see that $f \mapsto t ^ { 1 / 2 } ( K _ { t } * f )$ is a bounded linear operator whose operator norm is bounded uniformly in $t > 0 . \ \bigsqcup$

Problem 1b. Prove that $t ^ { 1 / 2 } | | K _ { t } * f | | _ { L ^ { \infty } } \to 0$ as $t  0 ,$ , for $f \in L ^ { 3 } ( \mathbb { R } ^ { 3 } )$

Solution.
We know that $C _ { c } ( \mathbb { R } ^ { 3 } )$ , the set of continuous functions with compact support, is dense in $L ^ { 3 } ( \mathbb { R } )$ If $g \in C _ { c } ( \mathbb { R } ^ { 3 } )$ , then we have

$$
| ( K _ { t } * g ) ( x ) | \ \leqslant \ \int _ { \mathbb { R } ^ { 3 } } | K _ { t } ( x - y ) g ( y ) | d y \ \leqslant \ \| g \| _ { L ^ { \infty } } \int _ { \mathbb { R } ^ { 3 } } | K _ { t } ( x - y ) | d y \ \leqslant \ \| g \| _ { L ^ { \infty } }
$$

where again the implied constant here does not depend on t. Thus we have $t ^ { 1 / 2 } | | K _ { t } * g | | _ { L ^ { \infty } }  0$ as $t  0$ for all $g \in C _ { c } ( \mathbb { R } ^ { 3 } )$ .

Now let f be any function in $L ^ { 3 } ( \mathbb { R } ^ { 3 } )$ . Let the linear operator $\phi _ { t } : L ^ { 3 } ( \mathbb { R } ^ { 3 } ) \to L ^ { \infty } ( \mathbb { R } ^ { 3 } )$ be defined by

$$
\phi _ { t } ( f ) ~ = ~ t ^ { 1 / 2 } ( K _ { t } * f ) .
$$

Recall that in part (a) we showed that there is a constant C, independent of t, such that $\| \phi _ { t } ( f ) \| _ { L ^ { \infty } } \leqslant C \| f \| _ { L ^ { 3 } }$ for all $f \in L ^ { 3 }$ . Fix $\epsilon > 0$ . By density, we can pick $g \in C _ { c } ( \mathbb { R } ^ { 3 } )$ such that $| | f - g | | _ { L ^ { 3 } } < \epsilon / 2 C$ . Since we have proved the result for functions in $C _ { c } ( \mathbb { R } ^ { 3 } )$ , we can now pick a $\delta > 0$ such that for all $t < \delta , | | \phi _ { t } ( g ) | | _ { L ^ { \infty } } < \epsilon / 2 .$ Then we conclude that for any $t < \delta$ we have

$$
t ^ { 1 / 2 } \left. K _ { t } * f \right. _ { L ^ { \infty } } = \left. \phi _ { t } ( f ) \right. _ { L ^ { \infty } } \leqslant \left. \phi _ { t } ( g ) \right. _ { L ^ { \infty } } + \left. \phi _ { t } ( f - g ) \right. _ { L ^ { \infty } } < \frac { \epsilon } { 2 } + C \left. f - g \right. _ { L ^ { 3 } } < \epsilon .
$$

This shows that lim $_ { 1  0 } t ^ { 1 / 2 } | | K _ { t } * f | | _ { L ^ { \infty } } = 0$ for any $f \in L ^ { 3 } ( \mathbb { R } ^ { 3 } ) . \quad \quad \bigsqcup$

Problem 2. Let $f \in L ^ { 1 } ( \mathbb { R } )$ . Show that the series

$$
\sum _ { n = 1 } ^ { \infty } { \frac { 1 } { \sqrt { n } } } f ( x - { \sqrt { n } } )
$$

converges absolutely for almost all $x \in \mathbb { R }$

Solution.
Let

$$
g ( x ) \ = \ \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { \sqrt { n } } } \left| f ( x - { \sqrt { n } } ) \right| .
$$

We show that $\int _ { M } ^ { M + 1 } g ( x )$ dx is finite for every integer M, which is enough to conclude that $g ( x ) < \infty$ for almost every $x \in [ M , M + 1 ]$ , which in turn implies that $g ( x )$ is finite almost everywhere, which is exactly what we need to prove.

For a fixed integer M, we have

$$
\int _ { M } ^ { M + 1 } g ( x ) d x \ = \ \int _ { M } ^ { M + 1 } \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { \sqrt { n } } } \left| f ( x - { \sqrt { n } } ) \right| \ = \ \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { \sqrt { n } } } \int _ { M } ^ { M + 1 } | f ( x - { \sqrt { n } } ) | d x
$$

by the Monotone Convergence Theorem, and after changing variables we get

$$
\int _ { M } ^ { M + 1 } g ( x ) d x \ = \ \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { \sqrt { n } } } \int _ { M - { \sqrt { n } } } ^ { M + 1 - { \sqrt { n } } } | f ( y ) | d y .
$$

For each integer k, there are $2 k + 1$ integers n such that $k < { \sqrt { n } } \leqslant k + 1$ . For each of these integers n, we have $[ M - \sqrt { n } , M + 1 - \sqrt { n } ] \subseteq [ M - k - 1 , M + 1 - k ]$ . Thus the above sum is bounded by

$$
\sum _ { k = 1 } ^ { \infty } ( 2 k + 1 ) \cdot { \frac { 1 } { k } } \int _ { M - k - 1 } ^ { M + 1 - k } | f ( y ) | d y \leqslant 3 \sum _ { k = 1 } ^ { \infty } \left[ \int _ { M - k - 1 } ^ { M - k } | f ( y ) | d y + \int _ { M - k } ^ { M + 1 - k } | f ( y ) | d y \right] \leqslant 6 \left\| f \right\| _ { L ^ { 1 } } .
$$

Thus we conclude that $\begin{array} { l } { \displaystyle { \int _ { M } ^ { M + 1 } g ( x ) < \infty , \mathrm { s o } g ( x ) } } \end{array}$ is finite almost everywhere.

Problem 3. Let $f \in L _ { l o c } ^ { 1 } (  { \mathbb { R } } )$ be real-valued and assume that for each integer $n > 0 .$ , we have

$$
f \left( x + { \frac { 1 } { n } } \right) \geqslant f ( x ) ,
$$

for almost all $x \in \mathbb { R } .$ . Show that for each real number $a \geqslant 0$ we have

$$
f ( x + a ) \ \geqslant \ f ( x )
$$

for almost all $x \in \mathbb { R } .$

Solution.
Let E be the (measure zero) set of Ť $x \in \mathbb { R } ^ { n }$ that do not have the property of the hypothesis.
Define $\begin{array} { r } { F = \bigcup _ { p \in \mathbb { Q } } ( E + p ) } \end{array}$ This is a countable union of measure zero sets so it also has measure zero.
If $a = 0$ , the result is obvious, so let $a > 0$ be fixed.
By the Lebesgue differentiation theorem, we know that

$$
f ( x + a ) - f ( x ) \ = \ \operatorname* { l i m } _ { r \to 0 ^ { + } } \frac { 1 } { 2 r } \int _ { x - r } ^ { x + r } \left( f ( y + a ) - f ( y ) \right) d y .
$$

for all x outside of some measure zero set $G$ . We show that $f ( x + a ) - f ( x ) \geqslant 0$ for all x outside of G. It is enough to show that for any interval $[ b , c ]$

$$
\int _ { b } ^ { c } f ( y + a ) d y \geqslant \int _ { b } ^ { c } f ( y ) d y ,
$$

or equivalently

$$
\int _ { b + a } ^ { c + a } f ( y ) d y \geqslant \int _ { b } ^ { c } f ( y ) d y .
$$

We can write a in binary as

$$
a ~ = ~ m + \sum _ { j = 1 } ^ { \infty } \frac { \epsilon _ { j } } { 2 ^ { j } } ~ = ~ \sum _ { j = 1 } ^ { \infty } \frac { 1 } { k _ { j } }
$$

where $\{ k _ { j } \}$ is some sequence of integers (not necessarily distinct, because there could by many 1s at the beginning).
Let $\begin{array} { r } { a _ { N } = \sum _ { i = 1 } ^ { N } 1 / k _ { j } } \end{array}$ . For any $y \notin F$ and any N, we know that $y + a _ { N } \notin E$ by construction of $F$ . Therefore we have $f { \ ' } ( y + a _ { N } ) = f ( y + a _ { N - 1 } + 1 / k _ { N } ) \geqslant f ( y + a _ { N - 1 } )$ By induction and the fact that $y + a _ { N } \notin E$ for each $N$ , we see that $f ( y + a _ { N } ) \geqslant f ( y )$ for all $N$ . Therefore, since $F$ has measure zero, this means

$$
\int _ { b + a _ { N } } ^ { c + a _ { N } } f ( y ) d y \ = \ \int _ { b } ^ { c } f ( y + a _ { N } ) d y \ \geqslant \ \int _ { b } ^ { c } f ( y ) d y .
$$

Defining $f _ { N } ( y ) = f ( y ) \chi _ { [ b + a _ { N } , c + a _ { N } ] } ( y )$ , we see that

$$
\int _ { \mathbb { R } } f _ { N } ( y ) d y \ \geqslant \ \int _ { b } ^ { c } f ( y ) d y .
$$

Since $f _ { N } \to { f \chi _ { [ b + a , c + a ] } }$ pointwise as $N  \infty$ and $| f _ { N } | \leqslant | f | \chi _ { [ b , c + a ] }$ for all $N _ { ; }$ , and $| f | \chi _ { [ b , c + a ] }$ is integrable, by the Dominated Convergence Theorem we conclude that

$$
\int _ { b + a } ^ { c + a } f ( y ) d y \ = \ \int _ { \mathbb { R } } f \chi _ { [ b + a , c + a ] } \ \geqslant \ \int _ { b } ^ { c } f ( y ) d y .
$$

Thus we conclude that $f ( x + a ) - f ( x ) \geqslant 0$ for all x for which the Lebesgue differentiation theorem applies to the function $x \mapsto f ( x + a ) - f ( x )$ , which is almost all $x \in \mathbb { R }$ □

Problem 4. Let $V _ { 1 }$ be a finite-dimensional subspace of the Banach space $V .$ Show that there exists a continuous projection $P : V \to V _ { 1 }$ , i.e., a continuous linear map $P : V \to V _ { 1 }$ such that $P ^ { 2 } = P$ and the range of $P$ is equal to $V _ { 1 }$

Solution.
Let $\{ e _ { 1 } , \ldots , e _ { n } \}$ be a basis for $V _ { 1 }$ . Without loss of generality we may assume that $| | e _ { j } | | = 1$ for each $j .$ For a fixed $j ,$ we know that span $\{ e _ { i } \} _ { i \neq j }$ is a closed subspace of $V .$ Thus by the Hahn-Banach theorem, there is a linear functional $f _ { j } \in V ^ { * }$ such that $f _ { j } ( e _ { j } ) = | | e _ { j } | | = 1$ and $f _ { j } ( x ) = 0$ for all $x \in \operatorname { s p a n } \{ e _ { i } \} _ { i \neq j }$ Now define the map $P : V \to V _ { 1 }$ by

$$
P ( x ) : = \sum _ { j = 1 } ^ { n } f _ { j } ( x ) e _ { j } .
$$

It is clear that Im $( P ) \subseteq V _ { 1 }$ by construction, and since each $f _ { j }$ is linear, $P$ is also linear.
We see that $P$ is continuous because

$$
\left| | P x - P y | \right| = \left| \left| \sum _ { j = 1 } ^ { n } f _ { j } ( x - y ) e _ { j } \right| \right| \leqslant \sum _ { j = 1 } ^ { n } | f _ { j } ( x - y ) | \left| | e _ { j } | \right| \leqslant \left( \sum _ { j = 1 } ^ { n } | | f _ { j } | | \right) \left| | x - y | \right| .
$$

Finally, for any $v \in V _ { 1 }$ , we write $v = v _ { 1 } e _ { 1 } + \ldots + v _ { n } e _ { n }$ and note that

$$
P v \ = \ \sum _ { j = 1 } ^ { n } f _ { j } \big ( v _ { 1 } e _ { 1 } + \ldots + v _ { n } e _ { n } \big ) e _ { j } \ = \ \sum _ { j = 1 } ^ { n } v _ { j } e _ { j } \ = \ v .
$$

This implies both that $P ^ { 2 } = P$ and that $V _ { 1 } \subseteq \operatorname { I m } ( P )$ , so ${ \mathrm { I m } } ( P ) = V _ { 1 }$ . Thus P is the desired map.

Problem 5. For $f \in C _ { 0 } ^ { \infty } (  { \mathbb { R } } ^ { 2 } )$ define $u ( x , t )$ by

$$
u ( x , t ) \ = \ \int _ { \mathbb { R } ^ { 2 } } e ^ { i x \cdot \xi } \frac { \sin ( t | \xi | ) } { | \xi | } f ( \xi ) d \xi , \quad x \in \mathbb { R } ^ { 2 } , \quad t > 0 .
$$

Show that lim $_ { t  \infty } | | u ( \cdot , t ) | | _ { L ^ { 2 } } = \infty$ for a set of f that is dense in $L ^ { 2 } ( \mathbb { R } )$

Solution.
We claim the desired result holds for all f in the set

$$
S : = \{ f \in L ^ { 2 } : \operatorname * { l i m } _ { x \to 0 } | f ( x ) | = \infty \} .
$$

Define

$$
g _ { t } ( \xi ) \ = \ \frac { \sin ( t | \xi | ) } { | \xi | } \overline { { { f ( \xi ) } } } ,
$$

then we see that

$$
u ( x , t ) \ = \ \int _ { \mathbb { R } ^ { 2 } } e ^ { i x \cdot \xi } \overline { { g _ { t } ( \xi ) } } d \xi \ = \ \overline { { \hat { g } _ { t } ( x ) } } .
$$

Therefore by Plancherel we have

$$
\begin{array} { r l } { \displaystyle | | u ( \cdot , t ) | | _ { L ^ { 2 } } ^ { 2 } = } & { \displaystyle | | \hat { g } _ { t } | | _ { L ^ { 2 } } ^ { 2 } = \mathrm { \# } | | g _ { t } | | _ { L ^ { 2 } } ^ { 2 } = \int \left( \frac { \sin ( t | \xi | ) } { | \xi | } \right) ^ { 2 } | f ( \xi ) | ^ { 2 } d \xi \gg \int _ { B ( 0 , \pi / ( 2 t ) ) } \left( \frac { \sin ( t | \xi | ) } { | \xi | } \right) ^ { 2 } | f ( \xi ) | ^ { 2 } d \xi } \\ & { \gtrsim \int _ { B ( 0 , \pi / ( 2 t ) ) } \left( \frac { t | \xi | } { | \xi | } \right) ^ { 2 } | f ( \xi ) | ^ { 2 } d \xi = t ^ { 2 } \int _ { B ( 0 , \pi / ( 2 t ) ) } | f ( \xi ) | ^ { 2 } d \xi } \\ & { \geqslant t ^ { 2 } \cdot \lambda _ { 2 } ( B ( 0 , \pi / ( 2 t ) ) ) \cdot \operatorname* { m i n } _ { | \xi | = \pi / ( 2 t ) } | f ( \xi ) | ^ { 2 } \approx \operatorname* { m i n } _ { | \xi | = \pi / ( 2 t ) } | f ( \xi ) | ^ { 2 } , } \end{array}
$$

which goes to 8 as $t \to \infty$ for $f \in S .$

Now we need to show $S$ is dense in $L ^ { 2 }$ . Fix $f \in L ^ { 2 } , \epsilon > 0$ . Let $g ( x ) = \vert x \vert ^ { - 1 / 2 } \cdot \chi _ { B ( 0 , 1 ) } ( x ) \in L ^ { 2 } ( \mathbb { R } ^ { 2 } )$ Pick a continuous function φ with $\| f - \phi \| _ { L ^ { 2 } } < \epsilon$ and let $h = \phi + \epsilon g$ . It’s clear that $h \in S$ and we have

$$
\| f - h \| _ { L ^ { 2 } } \ \leqslant \ \| f - \phi \| _ { L ^ { 2 } } + \| \epsilon g \| _ { L ^ { 2 } } \ \leqslant \ \epsilon ( 1 + \| g \| _ { L ^ { 2 } } ) .
$$

So S is dense in $L ^ { 2 } . \sqsupset$

Problem 6. Suppose that $\left\{ \phi _ { n } \right\}$ is an orthonormal system of continuous functions in $L ^ { 2 } ( [ 0 , 1 ] )$ and let S be the closure of the span of $\left\{ \phi _ { n } \right\}$ . If $\operatorname* { s u p } _ { f \in S \backslash \{ 0 \} } { \frac { | | f | | _ { L ^ { \infty } } } { | | f | | _ { L ^ { 2 } } } }$ is finite, prove that S is finite dimensional.

Solution.
We consider S as a subspace of $L ^ { 2 } ( [ 0 , 1 ] )$ equipped with the $L ^ { 2 }$ norm on $[ 0 , 1 ]$ . The sup condition on S tells us that there exists a constant M such that for any $f \in S , \| f \| _ { L ^ { \infty } } \leqslant M \| f \| _ { L ^ { 2 } }$ . For a fixed $x \in [ 0 , 1 ]$ , note that the map $f \mapsto f ( x )$ is a linear functional on S and that

$$
\vert f ( x ) \vert \ \leqslant \ \vert \vert f \vert \vert _ { L ^ { \infty } } \ \leqslant \ M \vert \vert f \vert \vert _ { L ^ { 2 } } ,
$$

which shows that this is in fact a bounded linear functional on S. Since S is a closed subspace of the Hilbert space $L ^ { 2 } ( [ 0 , 1 ] )$ , S is also a Hilbert space by itself, and thus by the Riesz representation theorem we know that there exists a function $g _ { x } \in S$ such that $f ( x ) = \langle f , g _ { x } \rangle$ for all $f \in S$ . Moreover, notice that

$$
| | g _ { x } | | _ { L ^ { 2 } } ^ { 2 } \ = \ \left. g _ { x } , g _ { x } \right. \ = \ | g _ { x } ( x ) | \ \leqslant \ | | g _ { x } | | _ { L ^ { \infty } } \ \leqslant \ M | | g _ { x } | | _ { L ^ { 2 } } ,
$$

which implies that $\| g _ { x } \| _ { L ^ { 2 } } \leqslant M$ for each $x \in [ 0 , 1 ]$

Now let $\{ f _ { 1 } , \ldots , f _ { N } \}$ be any orthonormal set in S. By Bessel’s inequality, for each $x \in [ 0 , 1 ]$ we have

$$
M ^ { 2 } ~ \geqslant ~ \left\| g _ { x } \right\| _ { L ^ { 2 } } ^ { 2 } ~ \geqslant ~ \sum _ { n = 1 } ^ { N } | \langle f _ { n } , g _ { x } \rangle | ^ { 2 } ~ = ~ \sum _ { n = 1 } ^ { N } | f _ { n } ( x ) | ^ { 2 } .
$$

Integrating both sides from 0 to 1 we obtain

$$
M ^ { 2 } \ \geqslant \ \sum _ { n = 1 } ^ { N } \int _ { 0 } ^ { 1 } | f _ { n } ( x ) | ^ { 2 } d x \ = \ \sum _ { n = 1 } ^ { N } \left| | f _ { n } | \right| _ { L ^ { 2 } } ^ { 2 } \ = \ N .
$$

This shows that any orthonormal set in S can contain no more than $M ^ { 2 }$ elements, which implies that dimpSq ď M 2.

Problem 7. Determine

$$
\int _ { 0 } ^ { \infty } { \frac { x ^ { a - 1 } } { x + z } } d x
$$

for $0 < a < 1$ and $\operatorname { R e } ( z ) > 0$

Solution.
Pick the branch of log with the positive real axis cut out and integrate

$$
f ( w ) : = \frac { w ^ { a - 1 } } { w + z } = \frac { \exp ( ( a - 1 ) \log ( w ) ) } { w + z } 
$$

along a “Pac-Man” contour with a circle of radius  around 0, a large semicircle of radius $R ,$ and an angle of α away from the positive real axis.
The integrals over the circles go to 0 in the limit and the two integrals along the straight paths combine in the limit as $\alpha \to 0$ to give

$$
( 1 - \exp ( 2 \pi i a ) ) \int _ { 0 } ^ { \infty } \frac { t ^ { a - 1 } } { t + z } d t .
$$

Then calculate the residue at $w = - z$ , it’s equal to $( - z ) ^ { a - 1 }$ (this is well-defined because since $\operatorname { R e } ( z ) > 0 ,$ ´z does not lie on the positive real axis).
So we conclude that the answer is

$$
\int _ { 0 } ^ { \infty } \frac { t ^ { a - 1 } } { t + z } d t \ = \ \frac { 2 \pi i ( - z ) ^ { a - 1 } } { 1 - \exp ( 2 \pi i a ) } . \quad \boxed { }
$$

Problem 8. Let $f _ { n } : \mathbb { H } \to \mathbb { H }$ be a sequence of holomorphic functions.
Show that unless $| f _ { n } | \to \infty$ uniformly on compact subsets of H, there exists a subsequence converging uniformly on compact subsets of H.

Solution.
By Marty’s Theorem, we know that the family $\left\{ f _ { n } \right\}$ is either a normal family or tends uniformly to 8 on every compact set if and only if the spherical derivatives

$$
\rho _ { n } ( z ) ~ = ~ { \frac { | f _ { n } ^ { \prime } ( z ) | } { 1 + | f _ { n } ( z ) | ^ { 2 } } }
$$

are uniformly bounded on every compact set.
So suppose that $f _ { n }$ does not tend uniformly to $\infty$ on every compact set.
Then if we show that $\left\{ f _ { n } \right\}$ is a normal family, it implies that $\left\{ f _ { n } \right\}$ has a subsequence that converges uniformly on all compact sets.
So it suffices to show that the quantites $\rho _ { n } ( z )$ above are uniformly bounded on compact sets.

Define

$$
g _ { n } ( z ) ~ = ~ { \frac { f _ { n } ( z ) - i } { f _ { n } ( z ) + i } } .
$$

Then each $g _ { n }$ is a holomorphic function $\mathbb { H } \to \mathbb { D }$ . In particular, the family $\left\{ g _ { n } \right\}$ is uniformly bounded on all of H, so $\left\{ g _ { n } \right\}$ is a normal family.
Thus we know that the quantities

$$
\frac { | g _ { n } ^ { \prime } ( z ) | } { 1 + | g _ { n } ( z ) | ^ { 2 } }
$$

are uniformly bounded on compact subsets of H. Now we have the calculation

$$
\frac { | g _ { n } ^ { \prime } ( z ) | } { 1 + | g _ { n } ( z ) | ^ { 2 } } ~ = ~ \frac { 4 \frac { | f _ { n } ^ { \prime } ( z ) | ^ { 2 } } { | f _ { n } ( z ) + i | ^ { 2 } } } { 1 + | f _ { n } ( z ) - i | ^ { 2 } } ~ = ~ \frac { 4 | f _ { n } ^ { \prime } ( z ) | ^ { 2 } } { | f _ { n } ( z ) + i | ^ { 2 } + | f _ { n } ( z ) - i | ^ { 2 } } ~ = ~ 2 \cdot \frac { | f _ { n } ^ { \prime } ( z ) | } { 1 + | f _ { n } ( z ) | ^ { 2 } } ~ = ~ 2 \rho _ { n } ( z ) .
$$

This shows that $\rho _ { n } ( z )$ must also be uniformly bounded on compact subsets of H and thus $\left\{ f _ { n } \right\}$ is a normal family, so we are done.

Alternate solution.
Without using Marty’s theorem (it’s not such a standard result).

Let $g _ { n }$ be defined as in the first solution, so that $g _ { n } : \mathbb { H } \to \mathbb { D }$ is holomorphic.
Fix a compact set $K \subseteq \mathbb { H }$ . The $g _ { n }$ are uniformly bounded, so there is a subsequence $g _ { n _ { k } }$ converging uniformly to another function g on $K .$ Let $v _ { k } = g _ { n _ { k } }$ . First suppose that $g \neq 1$ anywhere on K. Then, since $g ( K )$ is compact (g is continuous as a local uniform limit of continuous functions), $| g ( z ) - 1 |$ is bounded away from 0 for $z \in K$ . Therefore, letting

$$
f ~ = ~ \frac { - i ( g + 1 ) } { ( g - 1 ) } ,
$$

we have for any $z \in K$

$$
\left| f _ { n _ { k } } ( z ) - f ( z ) \right| = \left| { \frac { v _ { k } ( z ) + 1 } { v _ { k } ( z ) - 1 } } - { \frac { g ( z ) + 1 } { g ( z ) - 1 } } \right| = 2 \left| { \frac { v _ { k } ( z ) - g ( z ) } { ( v _ { k } ( z ) - 1 ) ( g ( z ) - 1 ) } } \right| \lesssim 2 \left| v _ { k } ( z ) - g ( z ) \right| ,
$$

which shows that $f _ { n _ { k } } \ \to \ f$ uniformly on K. This is the “subsequence converging uniformly on compact subsets of $\mathbb { H } ^ { \dag }$ part of the problem.

On the other hand, now assume that $g ( z _ { 0 } ) = 1$ for some $z _ { 0 } \in K$ . We want to show that in fact g is identically 1 and $v _ { k } \to 1$ uniformly on K. Fix a conformal map $T : \mathbb { D } $ H with $T ( 0 ) = z _ { 0 }$ and let $h _ { k } = v _ { k } \circ T$ Let

$$
\psi _ { k } ( z ) ~ = ~ { \frac { z + h _ { k } ( 0 ) } { 1 + \overline { { h _ { k } ( 0 ) } } } }
$$

be an automorphism of D taking 0 to $h _ { k } ( 0 )$ Let $u _ { k } \ = \ \psi _ { k } ^ { - 1 } \circ h _ { k }$ so that we have $h _ { k } \ = \ \psi _ { k } \circ u _ { k }$ where $u _ { k } : \mathbb { D }  \mathbb { D }$ is holomorphic and satisfies $u _ { k } ( 0 ) = 0$ . Since T is conformal, to show $v _ { k } \to 1$ locally uniformly it is enough to show $h _ { k } \to 1$ locally uniformly.
It’s enough to show $h _ { k } \to 1$ uniformly on the closed ball $\overline { { B ( 0 , r ) } }$ for $0 < r < 1$ By the Schwarz lemma, we have $u _ { n } ( \overline { { B ( 0 , r ) } } ) \subseteq \overline { { B ( 0 , r ) } }$ , so to show $h _ { k } \to 1$ uniformly on $\overline { { B ( 0 , r ) } }$ it’s enough to show $\psi _ { k }  1$ uniformly on $\overline { { B ( 0 , r ) } }$ . This is true because for any $z \in { \overline { { B ( 0 , r ) } } }$ we have

$$
| \psi _ { k } ( z ) - h _ { k } ( 0 ) | ~ = ~ \frac { | z | } { | 1 + \overline { { { h _ { k } } ( 0 ) } } z | } ( 1 - | h _ { n } ( 0 ) | ^ { 2 } ) ~ \leqslant ~ \frac { 2 r } { 1 - r } ( 1 - | h _ { n } ( 0 ) | ^ { 2 } )
$$

which tends to 0 uniformly for $z \in B ( 0 , r )$ . So we have shown $h _ { k } \to 1$ locally uniformly on D, which shows $v _ { k } \to 1$ locally uniformly.
It then follows that

$$
f _ { n _ { k } } \ = \ { \frac { ( - i ) ( v _ { k } + 1 ) } { v _ { k } - 1 } }
$$

tends locally uniformly to $\infty .$

So far we’ve only shown that a subsequence of the $f _ { n }$ tends locally uniformly to $\infty$ . But the argument above can be applied to any subsequence of the $f _ { n }$ to conclude that any subsequence of the $f _ { n }$ has a further subsequence converging locally uniformly to $\infty .$ , which implies that $f _ { n } \to \infty$ locally uniformly.

Problem 9. Let $f : \mathbb { C } \to \mathbb { C }$ be entire and assume that $| f ( z ) | = 1 { \mathrm { ~ w h e n ~ } } | z | = 1$ . Show that $f ( z ) = C z ^ { m }$ for some integer $m > 0$ and $C \in \mathbb { C }$ with $| C | = 1$

Solution.
We know that f is not identically zero, so the zeros of $f$ are isolated and thus $f$ has only finitely many zeros inside D. Denote them by $a _ { 1 } , \ldots , a _ { n } ,$ , where each root is listed as many times as its multiplicity.
Define

$$
B ( z ) : = \prod _ { j = 1 } ^ { n } { \frac { z - a _ { j } } { 1 - { \overline { { a _ { j } } } } z } } .
$$

Notice that B is a function which is analytic in $\mathbb { D } ,$ has exactly the same zeros as $f$ in D, and satisfies $| B ( z ) | = 1$ for all $| z | = 1$ . Thus $f / B$ and $B / f$ are two nonvanishing analytic functions in D which have modulus 1 on BD. By the maximum modulus principle, we conclude that $| B / f | \leqslant 1$ and $| f / B | \leqslant 1$ throughout
