# 2013 Complex Prelim Notes by Josh Swanson 9/6/2013

Sources: Marshall’s notes, unless otherwise noted, though statements have been reworded. Other works consulted include Ahlfors, Gamelin, and Rudin’s Real and Complex Analysis.

## 1 Basic Results

Theorem 1 (Schwarz’ Lemma) Let f be analytic on D with $| f ( z ) | \leq 1$ and $f ( 0 ) = 0$ . Then for all $z \in \mathbb { D }$

$$
| f ( z ) | \leq | z | \qquad a n d \qquad | f ^ { \prime } ( 0 ) | \leq 1 ,
$$

with either equality holding if and only $i f f ( z ) = c z$ for some $c \in \mathbb { C }$ with $| c | = 1$

Proof Idea: Consider $f ( z ) / z ;$ use the maximum principle on $| z | = r ;$ let $r  1$ . This is constant when equality holds at a point. 

Theorem 2 (“Invariant” form of Schwarz’ Lemma) Let f be analytic on D with $| f ( z ) | \leq 1$ . Then for all $w , z \in \mathbb { D }$ ,

$$
\left| { \frac { f ( w ) - f ( z ) } { 1 - { \overline { { f ( w ) } } } f ( z ) } } \right| \leq \left| { \frac { w - z } { 1 - { \overline { { w } } } z } } \right|
$$

and

$$
{ \frac { | f ^ { \prime } ( z ) | } { 1 - | f ( z ) | ^ { 2 } } } \leq { \frac { 1 } { 1 - | z | ^ { 2 } } } .
$$

Proof Idea: Let $\begin{array} { r } { T _ { c } ( z ) ~ = ~ \frac { c - z } { 1 - \overline { { c } } z } } \end{array}$ for $| c | < 1$ Apply Schwarz to $( T _ { f ( w ) } \circ f \circ T _ { w } ) ( \rho )$ Replace ρ with $T _ { w } ^ { - 1 } ( z ) = T _ { w } ( z )$ ; this gives the first inequality. For the second, rearrange and let $w  z ,$ . The same general trick works on other domains. 

Note: Wikipedia and random Google results call this Pick’s Lemma or Schwarz-Pick, though Marshall, Ahlfors, and Gamelin don’t use that name and the latter two only include fragments. Equality holds only for automorphisms of D (classified below), though none of my sources mention this. ✷

Theorem 3 (Maximum Modulus Principle) A non-constant analytic function f on a region Ω has no local maximum.

Alternatively, if f is non-constant analytic on a bounded region Ω and continuous on ${ \overline { { \Omega } } } ,$ then $\operatorname* { m a x } _ { \Omega } \left| f ( z ) \right|$ occurs on ∂Ω but not on Ω.

Alternatively, if f is analytic on a region Ω, then

$$
\operatorname* { s u p } _ { \Omega } | f | = \operatorname* { l i m } _ { z \to \partial \Omega } | f ( z ) | ,
$$

where we may have $\infty \in \partial \Omega$

Note: The lim sup can be interpreted by defining $z _ { n }  \partial \Omega$ to mean every compact subset of Ω contains only finitely many of the $z _ { n }$

Note: The “minimum modulus principle” is mentioned on Wikipedia but not by Marshall. The same principle as above applies to functions which don’t vanish, with max replaced by min, etc. (Look at $1 / f . )$

Proof Idea: Many. Parameterizing Cauchy’s Integral Formula gives the “mean value property” for analytic functions. Pulling | · | inside the integral gives |f| (strictly) subharmonic; use the subharmonic maximum principle. 

Theorem 4 (Open Mapping Theorem) A non-constant analytic function on a region is an open map.

Proof Idea: Pick $f ( z _ { 0 } ) \in f ( \Omega )$ and take Ω open. If w $\notin f ( \Omega )$ , the minimum modulus principle applies to $f ( z ) - w$ and says the closest f gets to w on Ω occurs on ∂Ω. Shrink Ω so $f ( z ) - f ( z _ { 0 } )$ is non-zero $\left( \mathrm { ^ { 6 6 } l a r g e ^ { 7 9 } } \right)$ on ∂Ω and pick w very close to $f ( z _ { 0 } )$ . Now $| f ( z ) - w |$ is large on ∂Ω but $\lvert f ( z _ { 0 } ) - w \rvert$ is small, so f gets closer to w on $z _ { \mathrm { 0 } }$ than on $\partial \Omega$ , contradicting the minimum modulus principle. 

Theorem 5 (Morera) Let f be a continuous complex function on an open set $\Omega \subset \mathbb { C }$ . If for every rectangle $R \subset \Omega$ with sides parallel to the axes, $\oint _ { R } f ( z ) d z = 0$ , then f is analytic in Ω.

Proof Idea: Say $\Omega = \mathbb { D }$ . Define g by integrating f along vertical then horizontal line segments. Use the FTC and rectangle property to show that $f ^ { \prime } = g$ from the limit definition of the derivative. 

Theorem 6 (Jordan Curve Theorem) Let J be a Jordan curve (i.e. a continuous injection from the unit circle to $\mathbb { C } ^ { * }$ , the Riemann sphere). Then $\mathbb { C } ^ { * } - J$ has exactly two simply-connected components, each of whose boundary is J.

Note: Not at all trivial to prove. Ahlfors and Gamelin don’t include a full statement. Marshall proves $i t ,$ though omits “simply connected”, however his definition of “simply connected” is that the complement in the Riemann sphere is connected, which is immediate here. ✷

Theorem 7 (Riemann Mapping Theorem) Let U be a simply connected proper subset of C. Then there is a conformal map f from U onto D. Moreover, for each $z _ { 0 } \in \mathbb { D }$ , there is a unique such map subject to the constraints $f ( z _ { 0 } ) = 0$ and $f ^ { \prime } ( z _ { 0 } ) > 0$

Proof Idea: First map into D. Say $0 \not \in U$ and define $\sqrt { z }$ on U. This is conformal onto a region omitting a ball; use an LFT to map into D. Now consider the (non-empty) normal family of conformal maps from U into D sending $z _ { \mathrm { 0 } }$ to 0; pick some f maximizing $\left| f ^ { \prime } ( z _ { 0 } ) \right|$ Suppose it misses $a \in \mathbb { D }$ . Let $T _ { c }$ denote the automorphism of D with $0  c$ . Now $T _ { a } \circ f$ misses 0 and $T _ { a } \circ f ( U )$ is simply-connected, so we may define $\sqrt { \cdot }$ on $T _ { a } \circ f ( U )$ . It follows that $[ T _ { \sqrt { a } } \circ \sqrt { \cdot } \circ T _ { a } ] \circ f$ is in the family. Moreover, the inverse of the piece in brackets is $T _ { a } \circ ( \cdot ) ^ { 2 } \circ T _ { \sqrt { a } } \colon \mathbb { D }  \mathbb { D }$ , which is not injective, so by Schwarz’ lemma it has derivative at 0 strictly less than 1 in magnitude. From the chain rule, our composite then has larger derivative than $f$ at $z _ { 0 }$ , a contradiction. Uniqueness also comes from Schwarz’ lemma. 

Proposition 1 (Automorphism Classifications) The automorphisms . . .

$\dots o f \mathbb { D }$ are all of the form

$$
c \frac { a - z } { 1 - \overline { { a } } z } , \qquad | c | = 1 , | a | < 1 .
$$

(Source: Gamelin, near Schwarz’ lemma; exercise in Marshall’s notes.)

$\dots o f \mathbb { C }$ are all of the form

$$
a z + b .
$$

• $\cdots o f$ the Riemann sphere are precisely the $L F T ' s$

## 2 Integral Formulas

Theorem 8 (Cauchy’s Integral Formula, version 1) Let f be analytic on a closed disk D centered at z. Let $\gamma$ be the boundary of D oriented positively. Then

$$
f ( z ) = { \frac { 1 } { 2 \pi i } } \int _ { \gamma } { \frac { f ( \zeta ) } { \zeta - z } } d \zeta .
$$

More generally,

$$
{ \frac { f ^ { ( n ) } ( z ) } { n ! } } = { \frac { 1 } { 2 \pi i } } \int _ { \gamma } { \frac { f ( \zeta ) } { ( \zeta - z ) ^ { n + 1 } } } d \zeta .
$$

Proof Idea: Write a power series with exponents k. Averaging over a circle picks off the $k = - 1$ coefficient. Shift the indexing by dividing by $\zeta - z$ to pick off the appropriate derivative. 

Theorem 9 (Cauchy’s Integral Theorem and Formula, version 2) Let Γ be a cycle in a region $\Omega \subset$ C where for all $\alpha \not \in \Omega , n ( \Gamma , \alpha )$ (the winding number of Γ about α) is 0. If f is analytic on Ω, then

$$
\int _ { \Gamma } f ( z ) d z = 0 .
$$

Also, $i f z \in \mathbb { C } - \Gamma$ , then

$$
f ( z ) n ( \Gamma , z ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma } { \frac { f ( \zeta ) } { \zeta - z } } d \zeta .
$$

Theorem 10 (Schwarz’ Theorem or the Poisson Formula) $\mathit { I f g }$ is real-valued and continuous on $\partial \mathbb { D } _ { R }$ then

$$
u ( z ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \frac { R ^ { 2 } - | z | ^ { 2 } } { | R e ^ { i t } - z | ^ { 2 } } g ( R e ^ { i t } ) d t
$$

is a harmonic function on D and

$$
\operatorname* { l i m } _ { z \to e ^ { i t } } u ( z ) = g ( e ^ { i t } ) .
$$

In particular, if u is harmonic on $\mathbb { D } _ { R }$ and continuous on $\partial \mathbb { D } _ { R }$ , this formula recovers u on $\mathbb { D } _ { R }$ Letting $z = r e ^ { i \theta }$ , equivalent forms for the kernel include

$$
{ \frac { R ^ { 2 } - | z | ^ { 2 } } { | R e ^ { i t } - z | ^ { 2 } } } = \operatorname { R e } \left( { \frac { R e ^ { i t } + z } { R e ^ { i t } - z } } \right) = { \frac { R ^ { 2 } - r ^ { 2 } } { R ^ { 2 } - 2 R r \cos ( t - \theta ) + r ^ { 2 } } }
$$

Note: Equivalent forms taken from Ahlfors, who calls it the Poisson formula.

Proof Many. Idea: integrate against the kernel $\left( \textstyle { \frac { R e ^ { i t } + z } { R e ^ { i t } - z } } \right)$ to get an analytic function whose real part is $u ,$ which is then harmonic. Integrating just this kernel using its power series gives 1 for all z. You can then show continuity by writing $| u ( z ) - g ( e ^ { i t _ { 0 } } ) |$ as an integral, breaking it up into pieces near $ e ^ { i t _ { o } }$ and far from $ e ^ { i t _ { 0 } }$ and estimating each separately. 

Theorem 11 (Schwarz’ Formula) $I f f = u + i v$ is analytic on $\overline { { \mathbb { D } _ { R } } }$ , then

$$
f ( z ) = \frac { 1 } { 2 \pi i } \oint _ { | \zeta | = R } \frac { \zeta + z } { \zeta - z } u ( \zeta ) \frac { d \zeta } { \zeta } + i v ( 0 ) .
$$

Source: Ahlfors. We can recover the Poisson formula by taking the real part and parameterizing. This is probably the easiest kernel to remember. Marshall calls it the Herglotz kernel and formula, but nobody else does. There is a version on the upper half plane but it involves a growth condition. ✷

Theorem 12 (Jensen’s Formula) Let f be meromorphic on $\overline { { \mathbb { D } _ { R } } }$ with zeros $\zeta _ { i }$ and poles $\rho _ { i }$ (repeated with their order, possibly on the boundary). Then

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \log | f ( R e ^ { i t } ) | d t = + \sum \log \frac { R } { | \zeta _ { i } | } - \sum \log \frac { R } { | \rho _ { i } | } + \log | f ( 0 ) | .
$$

We require $0 \not \in \{ \zeta _ { i } \} \cup \{ \rho _ { i } \}$

Note: To remember the right-hand side, think “zeros minus $\boldsymbol { p o l e s } ^ { \prime \prime }$ , where we want each term non-negative.

Proof Idea: Suppose no zeros or poles are on $\partial \mathbb { D } _ { R }$ Factor out automorphisms of $\mathbb { D } _ { R }$ from f leaving g analytic in $\mathbb { D } _ { R }$ . Evaluate log $| g ( 0 ) |$ to get the right-hand side. The left-hand side is the real part of the average value of log g(z), which is log $| g ( 0 ) |$

If there are zeros or poles on $\partial \mathbb { D } _ { R }$ , it involves harder estimates; see Marshall’s notes.

Corollary 1 Let f be analytic on D with zeros $\{ \zeta _ { i } \}$ (possibly infinitely many). $I f$

$$
\operatorname* { s u p } _ { 0 \leq r < 1 } \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \log | f ( r e ^ { i t } ) | d t < \infty ,
$$

then

$$
\sum _ { i } ( 1 - | \zeta _ { i } | ) < \infty .
$$

## 3 Analytic Extensions

Theorem 13 (Riemann’s Theorem on Removable Singularities) Suppose f is analytic in a punctured disk centered at a. $\begin{array} { r } { I f \operatorname* { l i m } _ { z \to a } ( z - a ) f ( z ) = 0 } \end{array}$ , then f extends to be analytic in the full disk.

Proof Use Cauchy’s Integral Formula to compute f using a counterclockwise integral over a circle of radius $R \to 1$ and a clockwise integral over a circle of radius $r  0$ . From the condition, the clockwise integral is 0, and the counterclockwise integral is analytic at 0. 

Theorem 14 (Painleve) A compact set E in C has one-dimensional Hausdorff measure $\mathrm { ~ 0 ~ } i f$ it can be covered by finitely many balls, the sum $o f$ whose radii can be taken arbitrarily small.

Given E compact of one-dimensional Hausdorff measure 0, suppose $f$ is analytic and bounded on $U - E$ for $U \supset E$ open. Then f extends to be analytic on U. ✷

Theorem 15 (Schwarz Reflection) Let the region Ω be symmetric about the real axis.

i Suppose f is analytic on H ∩ Ω and suppose lim ${ \boldsymbol { 1 } } _ { z \to x }$ Im $f ( z ) = 0$ for all $x \in \mathbb { R } \cap \Omega$ . Then f extends to all of Ω via ${ \overline { { f ( { \overline { { z } } } ) } } } = f ( z )$

ii Similarly, if u is harmonic on H ∩ Ω and extends continuously to 0 on R ∩ Ω, then u extends to all of Ω via $u ( z ) = - u ( \overline { { z } } )$

Note: For the analytic version, no assumption on the real part of f is needed.

Note: You can use conformal maps to extend these results to other regions, eg. annuli or lines. This is mentioned by Marshall, though I haven’t found a clean, rigorous generalization that’s any more useful than remembering this general principle.

Proof Idea: For $u ,$ the suggested function is harmonic except possibly on R ∩ Ω. The mean value property holds there by symmetry, so it is harmonic on Ω. It is the imaginary part of an analytic function near R ∩ Ω which agrees with the imaginary part of the extended version of f except on $\mathbb { R } \cap \Omega$ , hence f is analytic even on R ∩ Ω. 

Theorem 16 (Laurent Series) Let $f$ be analytic in an annulus A centered at $z _ { 0 }$ with radii $0 < r < R \leq \infty$ Then for all $z \in A$

$$
f ( z ) = \sum _ { n = - \infty } ^ { \infty } a _ { n } ( z - z _ { 0 } ) ^ { n }
$$

for some constants $a _ { n } \in \mathbb { C }$ . The sum converges uniformly and absolutely on compact subsets of A.

Moreover, for any $r < s < R$

$$
a _ { n } = { \frac { 1 } { 2 \pi i } } \int _ { \partial \mathbb { D } _ { s } } { \frac { f ( \zeta ) } { ( \zeta - z _ { 0 } ) ^ { n + 1 } } } d \zeta .
$$

Note: Splitting the sum into pieces, this allows us to write $f ( z ) = g ( z ) + h ( z )$ where $g$ is analytic on $| z | < R$ and $h ( z )$ is analytic on $| z | > r$

Proof Idea: pick $r < s _ { 1 } < | z | < s _ { 2 } < R .$ Use Cauchy’s Integral Formula on $\partial \mathbb { D } _ { s _ { 2 } }$ and $- \partial \mathbb { D } _ { s _ { \perp } }$ to recover $f ( z )$ —the winding number about z is 1, and the winding number outside A is 0. The $s _ { 1 }$ piece contributes positive terms by expanding the denominator about 0. The $s _ { 2 }$ piece contributes negative terms by expanding about ∞. 

## 4 Root Finding

Theorem 17 (The Argument Principle) Let f be meromorphic in a region Ω with poles $\{ \rho _ { i } \}$ and zeros $\{ \zeta _ { i } \}$ , repeated according to their orders. Let Γ be a cycle in Ω missing the $\rho _ { i } \stackrel { \cdot } { s }$ and $\zeta _ { i } \ : s$ and such that α $\not \in \Omega \Rightarrow n ( \Gamma , \alpha ) = 0$ . Then

$$
n ( f \circ \Gamma , 0 ) = \int _ { \Gamma } { \frac { f ^ { \prime } ( z ) } { f ( z ) } } d z = \sum _ { i } n ( \Gamma , \zeta _ { i } ) - \sum _ { i } n ( \Gamma , \rho _ { i } ) .
$$

Proof Idea: Factor out the zeros and poles. Taking the logarithmic derivative gives winding number integrands plus an analytic function. Integrating gives the formula since the analytic piece is zero by Cauchy’s Integral Theorem. (The first equality is immediate from parameterizing the integral.)

Theorem 18 (Generalized Argument Principle) If also $g ( z )$ is analytic in Ω, then

$$
\int _ { \Gamma } g ( z ) \frac { f ^ { \prime } ( z ) } { f ( z ) } d z = \sum _ { i } n ( \Gamma , \zeta _ { i } ) g ( \zeta _ { i } ) - \sum _ { i } n ( \Gamma , \rho _ { i } ) g ( \rho _ { i } ) .
$$

Source: Ahlfors, §5.2, “The Argument Principle”.

Theorem 19 (Rouche) Let Ω be a region, γ a closed curve in Ω, and $n ( \gamma , \alpha ) = 0$ for all $\alpha \not \in \Omega$ . If f and g are analytic in Ω and

$$
| f ( z ) + g ( z ) | < | f ( z ) | + | g ( z ) | \qquad f o r \ a l l \ z \in \gamma ,
$$

then f and g have the same number of zeros enclosed by γ. (Each zero $\zeta$ is counted with weight ord $( \zeta ) n ( \gamma , \zeta )$ where ord(ζ) is its order.)

Proof Idea: The triangle inequality bit says $\textstyle { \frac { f } { g } }$ omits the ray $[ 0 , \infty )$ , so $\textstyle { \frac { f } { g } }$ winds around 0 precisely once. Apply the argument principle to $\textstyle { \frac { f } { g } }$ to see the number of zeros and poles must agree. 

Note: A common, weaker version assumes $| f ( z ) - g ( z ) | < | f ( z ) |$ with the rest unchanged. Wikipedia calls Marshall’s version the “symmetric” form. ✷

## 5 Uniform Approximations

Theorem 20 (Runge, version 1) Let f be analytic on a compact set K. For each $\epsilon > 0$ , there is a rational function r such that

$$
| f - r | \leq \epsilon \qquad o n K .
$$

Proof Idea: Find a cycle Γ encircling K on which $f | _ { K }$ is the Cauchy integral of Γ. Use the definition of a Riemann integral to get a rational function approximating f near a point of K and where all refinements keep the same approximation. Cover K with finitely many such neighborhoods and take a common refinement.

Theorem 21 (Runge, version 2) Let f be analytic on a compact set K. For each $\epsilon > 0$ , there is a rational function r such that

$$
| f - r | \leq \epsilon \mathrm { ~ \ o n ~ } K ,
$$

and r has poles only at points in $\left\{ a _ { n } \right\}$ , where precisely one $a _ { n }$ is in each bounded connected component of the complement of K. If no such components exist, r may be taken to be a polynomial. ✷

Corollary 2 For any open set Ω and f analytic on Ω, there is a sequence of rational functions with poles in C − Ω converging uniformly on compact subsets of Ω to f. ✷

## 6 Normal Families

Definition 1 (Normal Families) A family of continuous functions ${ \mathcal { F } } = \{ f _ { \alpha } \colon U  \mathbb { C } \}$ on a region U is normal (in the Euclidean metric) if every sequence of functions in $\mathcal { F }$ contains a subsequence which converges uniformly on compact subsets of U.

Note: Ahlfors allows convergence to ∞, though Gamelin and Marshall do not. I follow Marshall.

If we allow $f _ { \alpha } \colon U \to \mathbb { C } \cup \{ \infty \}$ , F is normal (in the spherical metric) if every sequence of functions in F contains a subsequence which converges uniformly on compact subsets of U with respect to the spherical metric on $\mathbb { C } \cup \{ \infty \}$ (formula omitted; see Marshall’s normal family notes; he uses $\chi )$ ✷

Proposition 2 For a “normal family of analytic functions”, either definition can be used, though the first is the default assumption. Using the Euclidean metric, the limit function is analytic. Using the spherical metric, the limit function is either analytic and convergence is uniform in the Euclidean metric, or the limit function is ∞.

For a “normal family of meromorphic functions”, the second definition is used, and the limit function is either meromorphic or ∞. ✷

Theorem 22 (Arzela–Ascoli) Let F be a family of continuous functions from a region U to $\mathbb { C } , \ \mathcal { F }$ is normal (in the Euclidean metric) if and only if

(i) $\mathcal { F }$ is equicontinuous on every compact subset K of U, i.e.

$$
\forall z \in K , \forall \epsilon > 0 , \exists \delta > 0 : \forall f \in \mathcal { F } , \forall w \in K , | z - w | < \delta \Rightarrow | f ( z ) - f ( w ) | < \epsilon .
$$

(ii) There is some $z _ { 0 } \in U$ such that $\{ f ( z _ { 0 } ) : f \in \mathcal { F } \}$ is bounded.

Theorem 23 (Montel, version 1) Let F be a family of analytic functions on a region U. F is normal if and only if for every compact subset K of $U , { \mathcal { F } }$ is uniformly bounded on K.

Note: None of Marshall, Ahlfors, or Gamelin name this result, though Wikipedia calls this Montel’s theorem, and an old prelim seems to imply the same. ✷

Theorem 24 (Montel, version 2) Let F be a family of meromorphic functions on a region U. If the family omits three points in $\mathbb { C } \cup \{ \infty \}$ , then F is normal (in the spherical metric).

Note: Gamelin and Marshall call this Montel’s Theorem. Wikipedia only treats the holomorphic special case. Ahlfors doesn’t seem to include it. ✷

Theorem 25 (Hurwitz, version 1) Let $\{ f _ { n } \colon U  \mathbb { C } \}$ be a sequence of nowhere-vanishing analytic functions on a region U converging uniformly on compact subsets to f. Then either $f \equiv 0 \ o r$ f is nowherevanishing. ✷

Theorem 26 (Hurwitz, version 2) Let $\{ f _ { n } \colon U  \mathbb { C } \}$ be a sequence of analytic functions on a region U converging uniformly on compact subsets to f. Then for each zero ζ of f of order N, there is an open disk D about ζ such that, for n large, $f _ { n }$ has precisely N zeros in D, and these zeros converge to z0 as $n \to \infty$

Proof Idea: Use the Argument Principle on a disk $z _ { 0 } \in D \subset \overline { { D } } \subset U$ . Make sure f has no zeros on ∂D, whence the integrands converge uniformly. Smaller D have the same property. 

Note: Taken from Gamelin.

Theorem 27 (Picard’s Great Theorem) Let f be meromorphic on a punctured disk D centered at $z _ { \mathrm { 0 } } \in$ $\mathbb { C } \cup \{ \infty \} . \ I f f ( D )$ omits three points $o f \mathbb { C } \cup \{ \infty \}$ , then f extends to be meromorphic on $D \cup \{ z _ { 0 } \}$

Equivalently, an analytic function omits at most one point of C in every neighborhood of an essential singularity. In particular $f ( z ) = w$ has infinitely many solutions z for each $w \in \mathbb { C }$ in a neighborhood of an essential singularity, with at most one exceptional w. ✷

Theorem 28 (Picard’s Little Theorem) The image of a non-constant entire function is $\mathbb { C } \ o r \mathbb { C } - \{ a \} . . \cup$

## 7 Harmonic and Subharmonic Functions

Definition 2 (Harmonic Functions) Let f be a continuous real-valued function on a region in C. f is harmonic if it satisfies the mean value property about every point for all sufficiently small circles.

Note: This is Marshall’s defintion. Gamelin defines a harmonic function as a twice continuously differentiable function satisfying Laplace’s equation. Ahlfors proves the equivalence of these definitions. Indeed, he shows harmonic functions are smooth. ✷

Definition 3 (Subharmonic Functions) Let f be a continuous function with values in $[ - \infty , \infty )$ on a region in C. f is subharmonic if it satisfies the mean value inequality about every point for all sufficiently small circles, that is, the center value is ≤ the average value.

Note: This is Marshall’s definition. Ahlfors requires the mean value inequality to hold for all circles whose closure is in the domain, not just sufficiently small ones; it is not clear to me if this is equivalent. Ahlfors remarks that a sufficient condition is for f to be twice continuously differentiable and have non-negative Laplacian, but that this is not necessary as a subharmonic function “need not have partial derivatives”. ✷

Proposition 3 If f is analytic on a region U, then

(i) Re f and Im f are harmonic,

(ii) $| f |$ is subharmonic,

(iii) log |f | is harmonic on $U - f ^ { - 1 } ( 0 )$ , and

(iv) log |f | is subharmonic on $U$

Theorem 29 (Maximum Principle) If u is a subharmonic function on a region Ω and $i f$ there is a point $z \in \Omega$ such that $u ( z ) = \operatorname* { s u p } _ { \Omega } u ;$ then u is constant.

Alternatively, a non-constant subharmonic function u on a region Ω has no local maximum.

Alternatively, $i f \Omega$ is bounded and u is continuous on ${ \overline { { \Omega } } } ,$ then

$$
\operatorname* { s u p } _ { \Omega } u = \operatorname* { s u p } _ { \partial \Omega } u .
$$

Alternatively, allowing $\infty \in \partial \Omega$

$$
\operatorname* { l i m } _ { z \to \partial \Omega } u ( z ) = \operatorname* { s u p } _ { \Omega } u .
$$

Proof Idea: The mean value inequality forces u constant on a disk centered at $z ;$ connectedness extends this to the whole region. 

Theorem 30 (Lindelof ’s Maximum Principle) Let u be a bounded subharmonic function on an open set Ω. Suppose $Z$ is a finite subset of ∂Ω with $\partial \Omega - Z \neq \emptyset$ . (Note: we may have $\infty \in \partial \Omega . \mathrm { ~ , ~ }$ If, for all $\zeta ,$

$$
\operatorname* { l i m } _ { z  \zeta \in \partial \Omega - Z } u ( z ) \leq m ,
$$

then $u ( z ) \leq m$ for all $z \in \Omega$

Proof Take $Z = \{ 0 \}$ First suppose $\Omega \subset \mathbb { D }$ Consider $u ( z ) + \epsilon \log | z |$ , which remains subharmonic even at 0 since u is bounded near 0. By the maximum principle for subharmonic functions, $u ( z ) + \epsilon \log | z | \leq m$ for all $z \in \Omega$ . Fix $z \in \Omega$ and let $\epsilon  0 ^ { + }$ . If Ω is unbounded, take $\propto \notin Z$ via a Mobius transform and apply the above on $\Omega \cap \left\{ | z | < R \right\}$ as $R \to \infty ;$ note that m will become $m + \delta _ { R }$ where lim $\relax _ { R \to \infty } \delta _ { R } = 0$ 

Note: The name appears very non-standard, but the theorem is in Marshall’s notes.

Theorem 31 (Cauchy–Riemann Equations) An analytic function $f = u + i v$ satisfies the Cauchy– Riemann equations

$$
u _ { x } = v _ { y } , \qquad u _ { y } = - v _ { x } .
$$

This can be summarized by saying the Jacobian of $f \colon  { \mathbb { R } } ^ { 2 } \to  { \mathbb { R } } ^ { 2 }$ at each point is of the form,

$$
\left( \begin{array} { l l } { a } & { b } \\ { - b } & { a } \end{array} \right) ,
$$

i.e. is an orientation- and angle-preserving linear transformation (note the non-negative determinant). Moreover,

$$
f ^ { \prime } = u _ { x } + i v _ { x } = v _ { y } - i u _ { y } .
$$

Proposition 4 A function u on a simply-connected domain Ω is harmonic if and only if $u = \operatorname { R e } f$ for some f analytic on Ω.

Note: Unnamed, but in Marshall’s notes.

Example 1 If $- \infty < a < b < \infty$ , the function $\begin{array} { r } { \theta ( z ) = \operatorname { I m } \log { \frac { z - b } { z - a } } } \end{array}$ is harmonic on H and is equal to the peak angle in the triangle azb. It is therefore bounded and extends continuously to $\mathbb { R } - \{ a , b \}$ with $\theta ( x ) = 0$ for $x < a$ or $x > b$ and $\theta ( x ) = \pi$ for $a < x < b$

We can take linear combinations of such functions and get bounded harmonic functions which take on specified values on finitely many segments of R excepting the end points. We can also precompose with conformal maps to get bounded harmonic functions with specified boundary behavior.

This can also be a source of counterexamples. log ${ \frac { z - b } { z - a } } $ is analytic on H and we can Schwarz reflect over $( - \infty , a ] \cup [ b , \infty )$ to get an analytic function with bounded imaginary part which does not extend continuously to $[ a , b ]$

Note that we can also simply consider Im $\log ( z - a )$ , which gives the angle between z and a and hence is 0 for $x > a$ and π for $x < a$ ✷

Theorem 32 (Harnack’s Principle) Let $\{ u _ { n } \}$ be a sequence of harmonic functions on a region Ω with $u _ { n } ( z ) \leq u _ { n + 1 } ( z )$ for all z ∈ Ω. Then $u _ { n }$ converges uniformly on compact subsets of Ω either to a harmonic function u or to ∞.

Proof Idea: Use Harnack’s inequality (see below) on differences $u _ { n } - u _ { m }$ . The limit is harmonic by passing the limit inside the mean value integral. 

## 8 Inequalities

Corollary 3 (Cauchy’s Estimate) Let f be analytic on a closed disk D centered at z of radius r. Then

$$
\left| { \frac { f ^ { ( n ) } ( z ) } { n ! } } \right| \leq { \frac { \operatorname* { s u p } _ { D } | f | } { r ^ { n + 1 } } } .
$$

Proof Immediate corollary of Cauchy’s Integral Formula.

Theorem 33 (Hadamard’s Three Circles) Let A be an (open) annulus centered at 0 with radii $0 < r <$ $R < \infty$ . Suppose f is analytic on A. Set $M ( s ) = \operatorname* { l i m } \operatorname* { s u p } _ { z  \partial \mathbb { D } _ { s } } | f ( z ) |$ |. Then for $a l l z \in A$ with $| z | = s$ 7

$$
\log | f ( z ) | \leq { \frac { \log R - \log s } { \log R - \log r } } \log M ( r ) + { \frac { \log s - \log r } { \log R - \log r } } \log M ( R ) .
$$

This says log $M ( s )$ is a convex function of log s.

Note: Taken from Rudin’s Real and Complex Analysis. Ahlfors and Marshall have equivalent but uglier statements. None of them note that the same statement holds for any subharmonic function instead of just $| f ( z )$ .

Proof The right-hand side is a harmonic function on $A ,$ so subtracting it from the subharmonic function $| f ( z ) |$ gives a subharmonic function. From the lim sup definition and the maximum principle, their difference is $\leq 0$ on A. 

Theorem 34 (Hadamard’s Three Lines) Let u be subharmonic on the strip $S = \{ 0 < \mathrm { R e } z < 1 \}$ and let $V _ { s }$ be the vertical line $\{ \mathrm { R e } z = s \}$ . Let $M _ { s } = \operatorname* { l i m } \operatorname* { s u p } _ { z \to V _ { s } } u ( z )$ . If u is bounded, then

$$
u ( x + i y ) \leq ( 1 - x ) M _ { 0 } + x M _ { 1 } , \qquad f o r \ a l l \ x + i y \in S .
$$

Proof Idea: the right-hand side is harmonic. Subtracting it from $u ( z )$ gives a subharmonic function $\leq 0$ on the boundary except at $\infty .$ , but this is alright by Lindelof’s Maximum Principle. 

Theorem 35 (Harnack’s Inequality, version 1) Let u be a non-negative harmonic function on $\mathbb { D } _ { R }$ . Then $f o r \ | z | = r < R$ ,

$$
{ \frac { R - r } { R + r } } u ( 0 ) \leq u ( z ) \leq { \frac { R + r } { R - r } } u ( 0 ) .
$$

Proof Idea: By taking a limit, we can assume u is harmonic on ${ \overline { { \mathbb { D } _ { R } } } } .$ . Note the following inequality for the Poisson kernel:

$$
{ \frac { R - r } { R + r } } = { \frac { R ^ { 2 } - r ^ { 2 } } { ( R + r ) ^ { 2 } } } \leq { \frac { R ^ { 2 } - | z | ^ { 2 } } { | R e ^ { i t } - z | ^ { 2 } } } \leq { \frac { R ^ { 2 } - r ^ { 2 } } { ( R - r ) ^ { 2 } } } = { \frac { R + r } { R - r } } .
$$

Use this in the Poisson kernel; since u is non-negative, the inequalities pass through the mean value integral.

Note: Marshall, Ahlfors, Gamelin, and Rudin all take u “positive” rather than non-negative, but the proof works in general. They give the version with $R = 1$ ✷

Theorem 36 (Harnack’s Inequality, version 2) Let u be harmonic on a region Ω containing a compact set K with $z _ { 0 } \in K$ Then there is a constant $0 < C < \infty$ depending only on K and Ω such that for all non-negative harmonic functions u on Ω,

$$
\frac { 1 } { C } u ( z _ { 0 } ) \leq u ( z ) \leq C u ( z _ { 0 } ) , \qquad f o r \ a l l \ z \in K .
$$

Theorem 37 (Borel-Caratheodory) Let f be analytic on a closed disk of radius R centered at the origin. Take $0 \leq | z | < r < R$ and set $A = \operatorname* { s u p } _ { | w | \leq R }$ Re f(w). Then

(i) $I f ~ f ( 0 ) = 0$ , then

$$
| f ( z ) | \leq { \frac { 2 r } { R - r } } A .
$$

(ii) In general,

$$
| f ( z ) | \leq \frac { 2 r } { R - r } A + \frac { R + r } { R - r } | f ( 0 ) | .
$$

Proof (ii) follows from (i) applied to $f ( z ) - f ( 0 )$ with some straightforward estimates. For (i), the image of f on the interior of its domain lies to the left of the line $x = A$ . Construct an LFT mapping the half-plane left of $x = A$ to the circle of radius $R$ centered at the origin, and apply Schwarz’s Lemma. Send 0 to 0, ∞ to $- R ,$ and A to $R ;$ this gives $\frac { R z } { 2 A - z }$ 

Note: Not in Marshall, Ahlfors, Gamelin, or Rudin. It does appear in Lang’s book (though the proof is poor) and has a Wikipedia page. ✷

## 9 Series

Theorem 38 (Mittag-Leffler) Let $\Omega \subset \mathbb { C }$ be open and pick a sequence $b _ { n } \to \partial \Omega$ (meaning every compact subset of Ω contains finitely many $b _ { n } \mathbf { \zeta } ^ { \prime } s ^ { \prime }$ . For each $b _ { n }$ , pick a polynomial $S _ { n }$ in $\displaystyle ( z - b _ { n } ) ^ { - 1 }$ . Then there is a meromorphic function on Ω analytic on $\Omega - \{ b _ { n } \}$ and with singular part $S _ { n }$ at $\textit { b } _ { n } \ f o r$ each n.

Proof Idea: Pick an increasing sequence of compact $K _ { n } \subset \Omega = \cup K _ { n }$ . Let $\Sigma _ { n }$ be the sum of the singular parts for points in $K _ { n + 1 }$ but not $K _ { n }$ . Approximate $\Sigma _ { n }$ very well on $K _ { n }$ using Runge by some $f _ { n }$ analytic on Ω. The sum of the differences $\Sigma _ { m } - f _ { m }$ for $m = 1$ to n − 1 has the required singular parts on Kn–the analytic functions $f _ { m }$ don’t change this. The differences $\Sigma _ { m } - f _ { m }$ for $m \geq n$ are small and analytic on $K _ { n } .$ , and by Weierstrass’ M-Test their sum converges to an analytic function on $K _ { n }$ . The full sum is the desired function.

Note: This proof can be made constructive by finding polynomials $f _ { m }$ explicitly. Expanding $\frac { 1 } { 1 - z }$ in a power series and cutting off after finitely many terms does the trick for this singular part. An example is the next result.

Theorem 39 $I f b _ { k } \to \infty$ and if for some $n < \infty$

$$
\sum _ { k = 1 } ^ { \infty } { \frac { | a _ { k } | } { | b _ { k } | ^ { n + 2 } } } < \infty
$$

then

$$
f ( z ) = \sum _ { k = 1 } ^ { \infty } \left( { \frac { a _ { k } } { z - b _ { k } } } - \left( { \frac { a _ { k } } { - b _ { k } } } \right) \sum _ { j = 0 } ^ { n } \left( { \frac { z } { b _ { k } } } \right) ^ { j } \right)
$$

is meromorphic in C with singular part $\frac { a _ { k } } { z - b _ { k } }$ at each $b _ { k }$ and no other poles.

Proof Idea: The sum is the nth Taylor polynomial of $\frac { a _ { k } } { z - b _ { k } }$ centered at 0. Take $| z | < R$ and consider the tail of the sum above for $| b _ { k } | > 2 R _ { ☉ }$ . The differences can themselves be estimated with the geometric series. The Weierstrass M-Test together with the growth condition on the sum gives convergence of the tail to an analytic function on $| z | < R$ 

## Example 2

$$
\frac { \pi ^ { 2 } } { \sin ^ { 2 } \pi z } = \sum _ { n = - \infty } ^ { \infty } \frac { 1 } { ( z - n ) ^ { 2 } } .
$$

Outline: Considering Weierstrass on tails of the RHS, it is meromorphic with only the obvious singular parts. sin πz has zeros of order 1 at the integers and lim $\begin{array} { r } { \mathfrak { l } _ { z \to 0 } \frac { \sin ^ { 2 } \pi z } { \pi ^ { 2 } z ^ { 2 } } = 1 } \end{array}$ , so the LHS has the same singular parts; their difference is then entire. Both are periodic under $z  z + 1$ An easy estimate shows | sin $\pi z |  \infty$ as | Im $z |  \infty$ , to the LHS tends to 0 in this limit. On the RHS, the terms’ magnitude gets large for large imaginary parts; this tends to 0 by comparison with the integral $\textstyle \int _ { 1 } ^ { \infty } d x / ( a + x ^ { 2 } )$ . Their difference is then a bounded entire function tending to 0, giving equality. ✷

## Example 3

$$
\pi \cot ( \pi z ) = { \frac { 1 } { z } } + \sum _ { n \neq 0 } \left( { \frac { 1 } { z - n } } + { \frac { 1 } { n } } \right) .
$$

Outline: Considering Weierstrass on tails of the RHS, it is meromorphic with only the obvious singular parts. We can differentiate the LHS and the RHS term-by-term to get the previous example, so the two sides differ by a constant. They are both 0 at 0. ✷

## 10 Products

Definition 4 (Infinite Product Convergence) $\textstyle \prod _ { n = 1 } ^ { \infty } a _ { n }$ means lim $\begin{array} { r } { N \to \infty \prod _ { n = 1 } ^ { N } a _ { n } } \end{array}$ and the infinite product converges if the limit exists, is finite, and is non-zero.

Note: Source: Ahlfors. Marshall is vague on details but seems to follow Ahlfors. Gamelin and Rudin fiddle with 0 differently. ✷

Proposition 5 $\textstyle \prod _ { n = 1 } ^ { \infty } a _ { n } \ f o r \ a _ { n } \neq 0$ converges to a non-zero complex number if and only $i f \sum _ { n = 1 } ^ { \infty } \log a _ { n }$ converges; here we $t a k e \mathrm { ~ } - \pi < \arg z \leq \pi$ ✷

Definition 5 (Infinite product Absolute Convergence) $\textstyle \prod _ { n = 1 } ^ { \infty } a _ { n }$ for $a _ { n } \neq 0$ converges absolutely $\mathrm { i f } \ \sum _ { n = 1 } ^ { \infty } \left| \log a _ { n } \right.$ converges; here we take $- \pi < \arg z \leq \pi ,$

Note: The usefulness of absolute convergence of products is that any rearrangement of the product also converges, and to the same value. ✷

Proposition 6 $\textstyle \prod _ { n = 1 } ^ { \infty } a _ { n } \ f o r \ a _ { n } \neq 0$ converges absolutely if and only if $\textstyle \sum _ { n = 1 } ^ { \infty } | 1 - a _ { n } |$ converges, i.e. if and only $i f \sum _ { n = 1 } ^ { \infty } ( 1 - { \overset { . . . } { a _ { n } } } )$ converges absolutely.

Proof Idea: Note that lim $\iota _ { a \to 1 } { \frac { \log a } { a - 1 } } = 1 ;$ estimate | log a| with |a − 1| for a near 1.

Definition 6 (Analytic Infinite Product Convergence) Let $\left\{ f _ { n } \right\}$ be a sequence of analytic functions on a region Ω. We say $\textstyle \prod _ { n = 1 } ^ { \infty } f _ { n } ( z )$ converges if

$$
\operatorname* { l i m } _ { N  \infty } \prod _ { n = 1 } ^ { N } f _ { n } ( z )
$$

converges uniformly on compact subsets of Ω to an analytic function f which is not identically 0.

Note: Hurwitz’ theorem can be used to show the zeros of f are precisely the union of the zeros of each $f _ { n \cdot \sqcup }$

Theorem 40 Let $\Omega \subset \mathbb { C }$ be open and take a sequence $\{ f _ { n } \}$ of analytic functions on Ω, none of which are identically zero in any component of Ω. If

$$
\sum _ { n = 1 } ^ { \infty } | 1 - f _ { n } ( z ) |
$$

converges uniformly on compact subsets of Ω, then $\textstyle \prod _ { n = 1 } ^ { \infty } f _ { n } ( z )$ converges, and the order of a zero of the product is the sum of the orders of the zeros of the factors.

Note: Taken from Rudin. Marshall glosses over this point.

Theorem 41 (Weierstrass Product Theorem) Let $\Omega \subset \mathbb { C }$ be open and let $\left\{ \zeta _ { n } \right\}$ be a sequence of points in Ω with $\zeta _ { n }  \partial \Omega$ (where we allow $\infty \in \partial \Omega )$ Then there is an analytic function on Ω with zeros precisely at the $\zeta _ { n } ;$ we are free to choose the order of the zero at each point. ✷

Theorem 42 (Genus Theorem) Suppose $\{ a _ { n } \} \subset \mathbb { C } - \{ 0 \}$ and suppose g is a non-negative integer such that

$$
\sum _ { n = 1 } ^ { \infty } { \frac { 1 } { | a _ { n } | ^ { g + 1 } } } < \infty .
$$

Then

$$
\prod _ { n = 1 } ^ { \infty } \left( 1 - { \frac { z } { a _ { n } } } \right) \exp \sum _ { j = 1 } ^ { g } { \frac { 1 } { j } } \left( { \frac { z } { a _ { n } } } \right) ^ { j }
$$

converges to an entire function with zeros at $\left\{ a _ { n } \right\}$ and no other zeros.

Note: The smallest g satisfying the sum condition above for a fixed list of $a _ { n }$ ’s is called the genus. (This is $A h l f o r ' s$ convention.)

Note: The sums are the partial sums of the Taylor series $\begin{array} { r } { f o r - \ln \left( 1 - \frac { z } { a _ { n } } \right) } \end{array}$ about 1, say $\begin{array} { r } { T _ { g } \left( \frac { z } { a _ { n } } \right) } \end{array}$ $B y$ letting g vary with n, one can always make this estimate work, even if no single g satisfies the given sum.

Proof Idea: $\left( \log ( 1 - w ) + T _ { g } ( w ) \right) / w ^ { g + 1 }$ is analytic on D, and in particular bounded on the disk of radius $1 / 2$ . We can plug in $\frac { z } { a _ { n } }$ for $| a _ { n } | \geq 2 | z |$ and apply this bound to show the tail $\left| a _ { n } \right| \geq 2 R$ of the series $\begin{array} { r } { \sum _ { n } \left| \log \left( 1 - \frac { z } { a _ { n } } \right) + T _ { g } \bigl ( \frac { z } { a _ { n } } \bigr ) \right| } \end{array}$ is finite in $| z | \leq R .$ . We can exponentiate the sum (ignoring the | · |) and still get uniform convergence, hence the tail of the stated product is an analytic and non-zero function. 

Example 4 We show

$$
\sin \pi z = \pi z \prod _ { n = - \infty , n \neq 0 } ^ { \infty } \left( 1 - { \frac { z } { n } } \right) \exp { \frac { z } { n } } .
$$

The product on the right-hand side has genus $g = 1$ The zeros are simple and coincide with sin πz’s (simple) zeros, so the quotient of the left and right sides is an entire non-vanishing function. Thus sin πz is the RHS times some $e ^ { g ( z ) }$ Take the logarithmic derivative of both sides. The left becomes $\pi \cot ( \pi z )$ and the right becomes the series for π cot(πz) from Example 2, plus $g ^ { \prime } ( z )$ , hence g is constant. Divide both sides by z and let $z  0$ to see that $e ^ { g ( 0 ) } = 1$ ✷

Theorem 43 Let $\Omega \subset \mathbb { C }$ be open and suppose $\left\{ a _ { n } \right\}$ is a sequence of distinct points in Ω tending to ∂Ω (where we allow $\infty \in \partial \Omega )$ . There is an analytic function f on Ω with $f ( a _ { n } ) = c _ { n }$ for arbitrarily chosen $c _ { n }$

Proof Idea: Use Weierstrass’ theorem to get g with simple zeros precisely at each $a _ { n }$ . Let $d _ { n } \neq 0$ be the limit as $\begin{array} { r } { z  a _ { n } \mathrm { ~ o f ~ } \frac { g ( z ) } { z - a _ { n } } } \end{array}$ Use Mittag-Leffler’s theorem to get h with simple poles of residue $c _ { n } / d _ { n }$ precisely at each $a _ { n }$ . The product gh has removable singularities with the correct value at each $a _ { n }$ 

Theorem 44 (Blaschke Products) Suppose $\left\{ a _ { n } \right\}$ is a sequence of complex numbers in D tending to ∂D with $\textstyle \sum _ { n } ( 1 - | a _ { n } | ) < \infty$ . Then the Blashke Product

$$
\prod _ { n } { \frac { \left| a _ { n } \right| } { a _ { n } } } { \frac { a _ { n } - z } { 1 - { \overline { { a _ { n } } } } z } }
$$

converges to an analytic function bounded by 1 with zeros precisely at the $a _ { n }$ . (Take the fraction to be 1 when $a _ { n } = 0 . )$

Proof Idea: WLOG take $a _ { n } \neq 0$ . Estimate the magnitude of the difference of a factor and 1 for $\vert z \vert < r < 1$ The sum of these differences will be bounded since $\textstyle \sum _ { n } ( 1 - | a _ { n } | ) < \infty$ , and the result follows from Rudin’s theorem above. (Each factor is bounded by 1.)

## 11 Analytic Continuation

Note: Marshall’s notes do not discuss analytic continuation. Of Ahlfors, Gamelin, and Rudin’s treatments, I prefer Gamelin’s, which is used below.

Definition 7 (Analytic Continuation) Let $\gamma \colon [ 0 , 1 ] \to \mathbb { C }$ be continuous. Start with a power series $P _ { 0 }$ with radius of convergence $r _ { 0 }$ centered at $\gamma ( 0 )$ . Suppose for each $t \in [ 0 , 1 ]$ we have a power series $P _ { t }$ with radius of convergence $r _ { t }$ centered at $\gamma ( t )$ . Suppose for each $t ,$ there is some δ such that for all $| t - s | < \delta , P _ { s }$ and $P _ { t }$ agree on the intersection of their (open) disks of convergence.

Then $P _ { 1 } ( z )$ is the analytic continuation of $P _ { 0 }$ along γ.

Proposition 7 Continuing the notation of the preceding definition,

(i) Analytic continuations are unique. (A literal reading of Gamelin gives only that $P _ { 1 }$ is unique given γ and $P _ { 0 } . \jmath$

(ii) The nth coefficient of the power series for $P _ { t }$ depends continuously on $t .$

(iii) The radius of convergence $r _ { t }$ of $P _ { t }$ depends continuously on t. In particular, $r _ { t } \ge \delta > 0$ for some fixed δ.

(iv) With δ as above, suppose λ is another curve with $\gamma ( 0 ) = \lambda ( 0 ) , \gamma ( 1 ) = \lambda ( 1 )$ , and $| \gamma ( t ) - \lambda ( t ) | < \delta$ for all t. Given an analytic continuation $Q _ { t }$ along $\lambda , Q _ { 1 } = P _ { 1 }$ ✷

Theorem 45 (Monodromy, Homotopy Version) Let $f ( z )$ be analytic in a disk centered at $z _ { \mathrm { 0 } }$ . Let $\gamma _ { 0 } ( t )$ and $\gamma _ { 1 } ( t )$ be two paths from $z _ { 0 } ~ t o ~ z _ { 1 }$ along which $f ( z )$ can be continued analytically. Suppose $\gamma _ { 0 } ( t )$ and $\gamma _ { 1 } ( t )$ are homotopic with intermediate paths $\gamma _ { s } ( t )$ , such that each $\gamma _ { s } ( t )$ goes from $z _ { \mathrm { 0 } }$ to $z _ { 1 }$ and $f ( z )$ can be analytically continued along $\gamma _ { s }$ . Then the analytic continuations of $f ( z )$ along $\gamma _ { 0 }$ and $\gamma _ { 1 }$ agree at $z _ { 1 }$ ✷

Theorem 46 (Monodromy, Simply-Connected Version) Suppose Ω is a simply-connected region where we can analytically continue along every curve in Ω starting from some $f ( z )$ analytic in a disk centered at $z _ { 0 } \in \Omega$ . Then there is some $g ( z )$ analytic on Ω with $g = f$ when they are both defined.

Proof Define $g ( z )$ as the endpoint of a continuation from $z _ { \mathrm { 0 } }$ to z. This is well-defined since any two continuations give the same end value from the homotopy version. It follows that $g$ agrees with any continuation near its endpoint, hence is analytic on Ω. 

## 12 Residues

Definition 8 (Residues) Denote the residue of a meromorphic function $f \colon \Omega  \mathbb { D }$ with a pole about $\rho$ as Res $( f , \rho )$

(i) In general, ${ \mathrm { R e s } } ( f , \rho )$ is the coefficient of the $\frac { 1 } { z - \rho }$ term of the Laurent expansion about $\rho .$

(ii) If the pole is simple,

$$
\operatorname { R e s } ( f , \rho ) = \operatorname* { l i m } _ { z \to \rho } ( z - \rho ) f ( z ) .
$$

(iii) If $f ( z ) = G ( z ) / ( z - \rho ) ^ { n }$ for $G$ analytic at $\rho ,$

$$
\operatorname { R e s } \left( { \frac { G ( z ) } { ( z - \rho ) ^ { n } } } , \rho \right) = { \frac { G ^ { ( n - 1 ) } ( \rho ) } { ( n - 1 ) ! } } .
$$

(Think of this in terms of power series.)

(iv) If $f ( z ) = G ( z ) / H ( z )$ for G analytic at $\rho$ and H analytic with a simple zero at $\rho ,$ then

$$
\operatorname { R e s } \left( { \frac { G ( z ) } { H ( z ) } } , \rho \right) = { \frac { G ( \rho ) } { H ^ { \prime } ( \rho ) } } .
$$

(Derive from the simple pole formula above.)

Theorem 47 (Residue Theorem) Let f be meromorphic on a region Ω with poles at $\{ \rho _ { n } \}$ . Let Γ be a cycle in Ω passing through no poles with $n ( \Gamma , \alpha ) = 0$ for all α $\not \in \Omega$ . Then

$$
\int _ { \Gamma } f ( z ) d z = 2 \pi i \sum _ { n } n ( \Gamma , \rho _ { n } ) \operatorname { R e s } ( f , \rho _ { n } ) .
$$

Proof Idea: By continuity, only finitely many of the $\rho _ { n }$ have $n ( \Gamma , \rho _ { n } ) \neq 0$ . For these, add a small circle to the cycle winding around $\rho _ { n }$ negatively $n ( \Gamma , \rho _ { n } )$ times. Now the cycle is homologous to 0 in Ω minus these $\rho _ { n } \mathrm { ^ s }$ . By Cauchy’s integral theorem, the overall integral is zero. We may compute the integral of f near each $\rho _ { n }$ using the Laurent expansion and the fundamental theorem of calculus, which gives the residue. 

## Example 5 (Basic Residue Theorem Examples)

(i) Rational functions.

(ii) $\textstyle \int _ { - \infty } ^ { \infty } { \frac { 1 } { 1 + x ^ { 4 } } }$ dx. Integrate using a semi-circle −R to R to iR. The integral over the circular part tends to 0. The integrand is “symmetric” so the pie slice 0 to R to iR also works.

(iii) $\begin{array} { r } { \int _ { 0 } ^ { 2 \pi } \frac { 1 } { 3 + \sin \theta } d \theta } \end{array}$ . Substitute $z = e ^ { i \theta }$ so sin $\begin{array} { r } { \theta = \frac { 1 } { 2 i } ( z + 1 / z ) } \end{array}$ . It becomes an integral of a rational function over $| z | = 1$ . The same trick generalizes to many similar integrands.

(iv) $\textstyle \int _ { - \infty } ^ { \infty } { \frac { \cos x } { x ^ { 2 } + 1 } } d x$ . This is the real part of the integral of $\frac { e ^ { i z } } { z ^ { 2 } + 1 }$ over the reals. Compute this using a semi-circle −R to R to iR. Note that $| e ^ { i z } | = e ^ { \mathrm { R e } ( i z ) } = e ^ { - y }$ for $z = x + i y$ dies off as $y  \infty$ ✷

Example 6 (Residue Theorem Fourier Transform) $\textstyle \int _ { - \infty } ^ { \infty } { \frac { x \sin \lambda x } { 1 + x ^ { 2 } } } d x = \pi e ^ { - \lambda }$ for $\lambda > 0$ . Replace the integrand with $\frac { z e ^ { i \lambda z } } { 1 + z ^ { 2 } }$ and take the imaginary part at the end. Use a rectangular contour from −A to B to $B + i ( A + B )$ to $- \tilde { \cal A } + i ( { \cal A } + { \cal B } )$ . Easy estimates show that as $A , B \to \infty$ , the top, left, and right integrals go to 0. ✷

Definition 9 (Cauchy Principal Value) Suppose f is continuous on a smooth curve $\gamma .$ . The Cauchy Principal Value of f along γ is

$$
P V \int _ { \gamma } f ( z ) d z = \operatorname* { l i m } _ { \delta \to 0 } \int _ { \gamma \cap \{ | z - a | \geq \delta \} } f ( z ) d z ,
$$

if the limit exists.

Proposition 8 Suppose f is meromorphic in $\{ \ln z \geq 0 \}$ such that $\begin{array} { r } { | f ( z ) | \le \frac { K } { | z | } } \end{array}$ when Im $z \geq 0$ and $| z | > R$ $I f \lambda > 0$ , then

$$
P V \int _ { - \infty } ^ { \infty } f ( x ) e ^ { i \lambda x } d x = 2 \pi i \sum _ { \mathrm { I m } a > 0 } \mathrm { R e s } ( e ^ { i \lambda z } f ( z ) , a ) + 2 \pi i \sum _ { \mathrm { I m } a = 0 } \frac { 1 } { 2 } \mathrm { R e s } ( e ^ { i \lambda z } f ( z ) , a ) .
$$

Proof Idea: Use the same technique as in the Residue Theorem Fourier Transform example; the top, left, and right integrals tend to 0. For the bottom integral, use small semicircles to avoid the singularities on R. In the limit as the radius goes to 0, the integral is half the residue (use the same derivation as in the Residue Theorem itself). 

Example 7 (Integral through Principal Value) $\textstyle \int _ { - \infty } ^ { \infty } { \frac { \sin x } { x } } d x \ = \ \pi$ . This is continuous at 0. If the principal value of the integral of $\frac { e ^ { i z } } { z }$ on R exists, it follows that the imaginary part is the original integral. Applying the preceding proposition gives the stated result. ✷

Example 8 (Mellin Transform/Keyhole Contour) $\textstyle \int _ { 0 } ^ { \infty } { \frac { x ^ { \alpha } } { x ^ { 2 } + 1 } } d x$ where $0 < \alpha < 1$ We can define $z ^ { \alpha }$ using $0 < \arg z < 2 \pi$ . Integrate $\frac { z ^ { \alpha } } { z ^ { 2 } + 1 }$ over a “keyhole” with branch through the positive reals. The residue theorem computes these integrals. The integral over the large circle tends to 0 as its radius goes to zero, and similarly for the small circle. The integral over the two nearly-positive-real segments do not cancel since log differs on the segments. Combine it all to $\mathrm { g e t } \ \frac { \pi } { 2 \cos { \alpha } \pi / 2 }$ ✷

Example 9 (Series via Residues)

$$
\sum _ { n = 0 } ^ { \infty } { \frac { 1 } { n ^ { 2 } + 1 } } = { \frac { \pi } { 2 } } \left[ { \frac { e ^ { \pi } + e ^ { - \pi } } { e ^ { \pi } - e ^ { - \pi } } } \right] - 1 .
$$

Let $\begin{array} { r } { f ( z ) = \frac { 1 } { z ^ { 2 } + 1 } ; f ( z ) } \end{array}$ π cot πz is meromorphic with simples poles of residue $f ( n )$ at $z = n$ . Integrate this around a square with special vertices, namely $( N + \textstyle { \frac { 1 } { 2 } } ) ( \pm 1 \pm i )$ for an integer N. π cot πz is uniformly bounded on each such square. The decay rate on the denominator ensures the integral is zero as $N \to \infty$ , and the residue theorem lets us compute the sum.

Note: The same type of technique works for $| f ( z ) | \leq C | z | ^ { - 2 }$ for |z| large. Beware of extra poles at the integers. ✷

Example 10 (Dog Bone Contour) $\begin{array} { r } { \int _ { 0 } ^ { 1 } \frac { 1 } { \sqrt { x ( 1 - x ) } } } \end{array}$ dx. Define the integrand to be analytic in $\mathbb { C } - [ 0 , 1 ]$ , hence analytic at ∞. Use a “dog bone” contour centered on [0, 1]. Alternatively, apply an $L F T$ sending [0, 1] to $[ 0 , \infty )$ and apply a keyhole. ✷

## 13 Conformal Maps

Definition 10 A conformal map is a bijective analytic map $f \colon U \to V$ with $U , V \subset \mathbb { C }$ open. There are both equivalent and inequivalent definitions, but this is equivalent to the most common ones in this context. (Marshall’s notes use “a one-to-one and analytic map”.) ✷

## 13.1 LFTs

• LFT’s map circles to circles, disks to disks. “Circle” may mean “line”, and “disk” may mean “half $\mathrm { p l a n e } ^ { \mathrm { 7 } }$

• Given two pairs of three points on the Riemann sphere, there is a unique LFT sending the first triple to the second triple.

• Every one-to-one analytic map on the punctured plane is an LFT.

• The Cayley Transform is $\frac { z - i } { z + i }$ and maps the upper half plane H to the disk D. One way to see this is to note that $\begin{array} { r } { \left| \frac { z - i } { z + i } \right| < 1 } \end{array}$ if and only ${ \mathrm { i f ~ } } | z - i | < | z + i |$ , i.e. if and only if the distance from z to i is less than the distance from $z \ { \mathrm { t o } } - i .$ , i.e. if and only $\ i f \ z \in \mathbb { H }$

## 13.2 $\begin{array} { r } { J ( z ) = \frac { 1 } { 2 } \left( z + \frac { 1 } { z } \right) } \end{array}$

Marshall calls this map the Joukovski map. Its domain is $\mathbb { C } - \{ 0 \}$

$J ( e ^ { i \theta } ) = \cos \theta$ . Hence, J(∂D) is a double cover of $[ - 1 , 1 ]$ (where ±1 are “order two”, i.e. $J ( z ) \mp 1$ has a double root at ±1).

• It hits every point of C exactly twice, excepting ±1.

• It has the symmetry $\begin{array} { r } { J ( z ) = J ( \frac { 1 } { z } ) } \end{array}$

• It maps the circle $z ( t ) = r e ^ { i t }$ for $r \neq 1$ onto an ellipse centered at the origin.

• It maps the ray $z ( r ) = r e ^ { i t }$ for $r \geq 0$ onto a branch of a hyperbola, if the ray is not on a coordinate axis.

• (Not in Marshall’s notes.) It maps $\{ | z | < 1 , \operatorname { I m } z > 0 \}$ and $\{ | z | > 1 , \operatorname { I m } z < 0 \}$ conformally onto the lower half plane.

• (Not in Marshall’s notes.) It maps $\{ | z | < 1 , \operatorname { I m } z < 0 \}$ and $\{ | z | < 1 , \operatorname { I m } z > 0 \}$ conformally onto the upper half plane.

• It maps the upper half plane conformally onto C minus the rays [1, ∞) and (−∞, −1]. By symmetry, it does the same to the lower half plane.

• It maps the complement of the closed unit disk conformally onto C minus the strip [−1, 1]. By symmetry, it does the same to the unit disk minus the origin.

## 13.3 How to map Ω conformally onto D

• Ω = D: the automorphisms of D are above.

$\Omega = \{ a < \arg z < b \}$ , an unbounded sector: use $z ^ { \alpha }$ for α making the angle π. Rotate and use the Cayley transform.

• Ω = intersection of two disks: use an LFT to send one point of intersection to 0 and the other to ∞.

$\Omega = \{ a < \arg z < b , | z | < R \}$ , a bounded circular sector: apply $z ^ { \alpha }$ to expand the angle of the sector to π. It is now the intersection of two disks.

• Ω = intersection of three disks: pick two disks; send their intersection points to 0 and $\infty .$ , which gives a bounded circular sector.

• Ω = H − [0, i], a slit half plane: $z ^ { 2 }$ maps C conformally onto the split plane $\mathbb { C } - [ - 1 , \infty )$ . Translate to an unbounded sector; take square root; Cayley. (A 90 degree angle is important. Just before introducing the Geodesic Algorithm, Marshall gives a lengthy discussion for H minus a segment starting at the origin at an arbitrary angle a. He suggests $C z ^ { \bar { 1 } - a } ( z - 1 ) ^ { a }$ maps H conformally onto this region, where C depends on the segment’s length.)

• Ω = half plane minus a perpendicular circular arc: use an LFT to keep the half plane boundary straight while straightening out the circular arc; it is now a slit half plane.

• Ω = region between two branches of a hyperbola: map H to a sector $\{ \pi / 2 - a < \arg z < \pi / 2 + a \}$ and use the Joukovsky map.

• Ω = exterior of an ellipse: apply the Joukovsky map to Dr for appropriate $r < 1$

• Ω = a parabola: apply $z ^ { 2 }$ to a half-plane $\{ \mathrm { R e } z > b \}$

$\Omega = \{ 0 < \mathrm { R e } z < \pi \}$ , a (vertical) strip: $e ^ { i z }$ maps Ω conformally onto H—vertical lines go to rays.

$\Omega = \{ 0 < \mathrm { I m } z < \pi , \mathrm { R e } z < 0 \}$ , a (horizontal) half strip: $e ^ { z }$ maps Ω onto H ∩ D, which the Joukovsky map sends to the lower half plane. Alternatively, after $e ^ { z }$ , we have the intersection of two disks.