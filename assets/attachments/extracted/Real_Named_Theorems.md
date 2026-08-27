# Real Variables Named Theorems

Kari Eifler

July 10, 2017

1 (Well-ordering Theorem) Given any set A, there is a well-order on A

2 (Axiom of Choice) If $\{ X _ { t } \mid t \in I \}$ is a family of non-empty sets then $\Pi _ { t \in I } X _ { t } \neq 0$ where $\Pi _ { t \in I } X _ { t } = \{ f : I \to \cup _ { t \in I } X _ { t } \ | \ \forall t \in I , f ( A ) \in X _ { t } \}$

3 (Cantor-Schr¨ıder-Bernstein) If card $( A ) \leq \operatorname { c a r d } ( B )$ and card $( B ) \leq \mathrm { c a r d } ( A )$ then card $( A ) = \operatorname { c a r d } ( B )$

4 (Zorn’s Lemma) Assume $( X , \leq )$ is a partially ordered set. Assume every limiting order subset (i.e. chain) of X has an upper bound. Then X has a maximal element.

5 (Hausdorff Maximal Principle) Let $( X , \leq )$ be a partially ordered set. Then there exists a maximal chain in X

i.e. if $Y \subseteq X$ such that $( Y , \leq )$ is linearly ordered and if $Z \subseteq X$ with Z linearly ordered and $Z \supseteq Y$ then $Z = Y$ •

6 (Caratheodory) Suppose $\mu ^ { * }$ is an outer measure on X and set ${ \mathcal { M } } = { \mathcal { M } } _ { \mu ^ { * } } = \mathrm { a l l }$ $\mu ^ { * }$ -measurable subsets of X. Then M is a σ-algebra and $\mu ^ { * } | _ { \mathcal { M } }$ is a complete measure.

7 (monotone convergence) I ${ \mathrm { ~ f ~ } } 0 \leq f _ { 1 } \leq f _ { 2 } \leq . .$ . with $f _ { n } \in L ^ { + }$ and $f \ = \ \operatorname* { l i m } _ { n } f _ { n }$ pointwise, then $\textstyle \int f _ { n } d \mu \to \int f d \mu$

8 (Fatou’s Lemma) For $f _ { n } \in L ^ { + }$ then

$$
\int \operatorname* { l i m } \operatorname* { i n f } f _ { n } \leq \operatorname* { l i m } \operatorname* { i n f } \int f _ { n }
$$

9 (Dominated Convergence Theorem, v1) If $0 \leq f _ { n } \leq g$ are all measurable and $f _ { n } \to _ { X } f , \int g < \infty$ then $\textstyle \int f _ { n } \to \int f$ .

10 (Dini’s Theorem) For $f _ { n } \in { \mathcal { C } } ( [ 0 , 1 ] ) , f _ { 1 } \geq f _ { 2 } \geq . . . , f _ { n } \to _ { [ 0 , 1 ] } 0$ then $f _ { n }$ converges to   
0 uniformly on [0, 1].

11 (Generalized Dominated Convergence Theorem) Let $g , g _ { n } \in L ^ { + }$ be measurable, $| f _ { n } | \leq g _ { n } \mu { \mathrm { - a . e . , ~ } } f _ { n } \to f$ and $g _ { n }  g \ \mu { \mathrm { - a . e } }$ . with $\textstyle \int g _ { n } \to \int g < \infty$

Then $\textstyle \int f _ { n } \to \int f$ . Moreover, $\textstyle \int \left| f - f _ { n } \right| \to 0$

12 (Egoroff ’s Theorem) Suppose $f _ { n } \to f { \mathrm { ~ a . e ~ } }$ . and $\mu ( D ) < \infty$ . Then $\chi _ { D } f _ { n }  \chi _ { D } f$ almost uniformly.

## 13 (types of convergence)

(A) $f _ { n } \implies f \ ( \mathrm { u n i f o r m } )$

$$
\mathrm { i . e . } \ \| f _ { n } - f \| _ { \operatorname* { s u p } } \to 0
$$

(B) $f _ { n } \to f { \mathrm { ~ p o i n t w i s e } }$

i.e. fn(x) → f (x) for all x

(C) $f _ { n } \to f { \mathrm { ~ a . e . } }$

i.e. $\mu ( \{ x \mid f _ { n } ( x ) \nrightarrow f ( x ) \} ) = 0$ (this is not a topological mode of convergence)

(D) $f _ { n } \to f \ ( \mu )$ (in measure)

$$
\forall \epsilon > 0 , \operatorname* { l i m } _ { n } \mu [ | f - f _ { n } | > \epsilon ] = 0
$$

(E) $L ^ { 1 } ( \mu )$ convergence

i.e. $\| f _ { n } - f \| _ { 1 } \to 0$

(F) $f _ { n }  f$ almost uniformly

i.e. $\forall \epsilon > 0 .$ , ∃E such that $\mu ( E ^ { C } ) < \epsilon$ and $f _ { n }  _ { E } f$

The following diagram shows the implications where blue arrows mean on any measure space and gray arrows mean it only holds on finite measure spaces.

<!-- image-->

(F) 9 (E) and (D) → (C) for a subsequence.

(C) or (D) + (dominated or monotonicity) → (E)

$f _ { n }  f$ in $L ^ { 1 } \Leftrightarrow$ every subsequence of $f _ { n }$ has a further subsequence which converges to f in $L ^ { 1 }$

14 (Tonelli) Let $( X , { \mathcal { M } } , \mu )$ and $( Y , \mathcal { N } , \nu )$ be σ-finite measure spaces, and $f : X \times Y $ [0, ∞] be a measurable function. Then

1. Define $f _ { x } : Y \to [ 0 , \infty ]$ by $y \mapsto f ( x , y )$ . Then $f _ { x }$ is measurable for all $x \in X$

2. $\textstyle x \mapsto \int f ( x , y ) d \nu ( y )$ is a measurable function on X

3. $\begin{array} { r } { \int f d ( \mu \times \nu ) = \int ( \int f ( x , y ) d \nu ( y ) ) d \mu ( x ) } \end{array}$

15 (Fubini) Let $( X , { \mathcal { M } } , \mu )$ and $( Y , \mathcal { N } , \nu )$ be σ-finite measure spaces, $f \in L ^ { 1 } ( \mu \times \nu )$ . Then

1. for $\mu { \mathrm { - a . e . ~ } } x \in X , f ( x , \cdot ) \in L ^ { 1 } ( \nu )$

2. $\begin{array} { r } { x \mapsto \int _ { Y } f ( x , y ) d \nu ( y ) \in L ^ { 1 } ( \mu ) } \end{array}$

3. $\begin{array} { r } { \int f d \mu \times \nu = \int ( \int f ( x , y ) d \nu ( y ) ) d \mu ( x ) } \end{array}$

If f is measurable on $X \times Y$ then $| f |$ is measurable on $X \times Y$

16 (Approximation properties of $m ^ { n } )$ We let $m ^ { n }$ be the completion of $m \times \cdots \times m$ where m is the Lebesgue measure on R. So ${ \mathcal { L } } ^ { n }$ is the Lebesgue measurable sets on $\mathbb { R } ^ { n }$

Take $E \in \mathcal { L } ^ { n }$ . Then

1. $m ^ { n } ( E ) = \operatorname* { i n f } \{ m ^ { n } ( { \mathcal { O } } ) \mid E \subseteq { \mathcal { O } }$ and O is open}

$= \operatorname* { s u p } \{ m ^ { n } ( K ) \mid K \subseteq E$ and K is compact}.

2. $E = A _ { 1 } \backslash N _ { 1 }$ where $A _ { 1 }$ is $G _ { \delta }$ and $m ^ { n } ( N _ { 1 } ) = 0$

$E = A _ { 2 } \cup N _ { 2 }$ where $A _ { 2 }$ is $F _ { \sigma }$ and $m ^ { n } ( N _ { 2 } ) = 0$

3. $m ^ { n } ( E ) < \infty$ implies $\forall \epsilon > 0 , \exists ( R _ { j } ) _ { j = 1 } ^ { N }$ of disjoint open rectangles such that $m ^ { n } ( E \triangle$ $( \cup R _ { j } ) ) = 0$

17 (Hahn-Decomposition Theorem) Let ν be a signed measure on $( X , M )$ . Then there exists $P \in { \mathcal { M } }$ which is positive for ν and $N = P ^ { C }$ is negative for ν.

Moreover, the decomposition $X = P \cup N$ is essentially unique: if $P _ { 1 }$ is positive for ν and $N _ { 1 } = P _ { 1 } ^ { C }$ is negative for ν, then $P \triangle P _ { 1 } = N \triangle N _ { 1 }$ is null for ν.

18 (Jordan Decomposition) Take the Hahn decomposition and let $\nu ^ { + } ( E ) : = \nu ( E \cap P )$ $\nu ^ { - } ( E ) : = - \nu ( E \cap N )$ so that $\nu = \nu ^ { + } - \nu ^ { - }$ −. Note that $\nu ^ { + } \perp \nu ^ { - }$

Note that the Jordan Decomposition is unique.

The total variation of ν is defined to be $| \nu | ( E ) = \nu ^ { + } ( E ) + \nu ^ { - } ( E )$

19 (Lebesgue Decomposition Theorem) Let µ be a measure on $( X , M )$ and ν a σ-finite signed measure. Then $\nu = \nu _ { 1 } + \nu _ { 2 }$ where $\nu _ { 1 } \perp \mu , \nu _ { 2 } \ll \mu$ . Moreover, this decomposition is unique.

20 (Radon-Nikodyn Theorem) If $( X , M )$ is a measurable space, µ a σ-finite measure

on M and ν a σ-finite signed measure on M with $\nu \ll \mu ,$ , then there exists an extended µ-integrable f such that $\nu = \nu _ { f }$ where $\textstyle \nu _ { f } ( E ) = \int _ { E } f d \mu$

Moreover, we have uniqueness. If $\nu _ { f } = \nu _ { g }$ then $f = g \ \mu { \mathrm { - a . e } }$

21 (Lebesgue Differential Theorem) Fix $x \in \mathbb { R } ^ { n }$ . We say $\{ E _ { r } \} \subseteq B _ { \mathbb { R } ^ { n } }$ shrinks nicely to x if

$E _ { r } \subseteq B ( r , x ) \qquad \forall r > 0$

$\exists \alpha > 0$ such that $\forall r > 0 , m ( E _ { r } ) \geq \alpha m ( B ( r , x ) )$

Lebesgue Differential Theorem: For $f \in L _ { l o c } ^ { 1 } ( \mathbb { R } ^ { n } )$ , then for all $x \in L _ { f }$ and for all $\{ E _ { r } \}$ shrinking nicely to x, we have

$$
\operatorname* { l i m } _ { r \to 0 ^ { + } } { \frac { \int _ { E _ { r } } | f ( y ) - f ( x ) | d y } { m ( E _ { r } ) } } = 0
$$

$$
f ( x ) = \operatorname* { l i m } _ { r \to 0 ^ { + } } { \frac { \int _ { E _ { r } } f ( y ) d y } { m ( E _ { r } ) } }
$$

22 (Urysohn’s Lemma) Let (X, T ) be normal. If A, B are disjoint closed sets and $a \neq b$ in R. Then there exists some $f \in C ( \boldsymbol { X } , [ a , b ] )$ such that $f | _ { A } \equiv a$ and $f | _ { B } \equiv b$

proof uses nastay lemma

23 (Tiktze Theorem) Version 1: Let (X, T ) be normal. If $A \subseteq X$ is closed and $f \in C ( A , ( a , b ) )$ then there exists some $F \in C ( X , [ a , b ] )$ such that $F | _ { A } = f .$

Version 2: Let (X, T ) be normal. If $A \subseteq X$ is closed and $f \in C ( A , ( a , b ) )$ then there exists some $F \in C ( X , \mathbb { R } )$ such that $F | _ { A } = f$

24 (Tychonoff Theorem) If $\left( X _ { \alpha } \right)$ are compact topological spaces, then $X = \Pi _ { \alpha \in { \mathcal { A } } } X _ { \alpha }$ (with the product topology) is compact.

Theorem: Axiom of Choice ⇔ Tychonoff

25 (Arzela-Ascoli) We say a metric space X is totally bounded if for any $r > 0$ , X can be covered by a finite number of balls of radius r.

Arzela-Ascoli Let X be a compact Hausdorff space. If F is an equicontinuous, pointwise bounded subset of $\mathcal C ( X )$ then $\mathcal { F }$ is totally bounded in the uniform metric and the closure of $\mathcal { F }$ in $\mathcal C ( X )$ is compact.

Alternative version 1: Let X be a σ-compact LCH space. If $\left\{ f _ { n } \right\}$ is an equicontinuous, pointwise bounded sequence in $\mathcal C ( X )$ , then there exists a $f \in { \mathcal { C } } ( X )$ and a subsequence of

$\left\{ f _ { n } \right\}$ that converges to f uniformly on compact sets.

Alternative version 2: Let X be compact and ${ \mathcal { F } } \subseteq { \mathcal { C } } ( X )$ . Then $\overline { { \mathcal { F } } }$ is compact in $\mathcal C ( X )$ IFF

1. F is equicontinuous

2. F is pointwise bounded

26 (Stone-Weierstrass) A is called an algebra if it is a real vector subspace of $C ( X )$ such that $f g \in { \mathcal { A } }$ whenever $f , g \in { \mathcal { A } }$

Let X be a compact, Hausdorff space and $B \subseteq { \mathcal { C } } ( X , \mathbb { R } )$ a subalgebra such that B separates points (that is, for $x \neq y , \exists f \in B$ with $f ( x ) \neq f ( y ) )$ . Then if there exists some $x _ { 0 } \in X$ such that $f ( x _ { 0 } ) = 0$ for all $f \in B$ , then $\overline { { B } } = \{ f \in \mathcal { C } ( X , \mathbb { R } ) \mid f ( x _ { 0 } ) = 0 \}$ . Otherwise, ${ \overline { { B } } } = { \mathcal { C } } ( X )$

27 (Hahn-Banach) For a real vector space X, we say $p : X  \mathbb { R }$ is a sublinear mapping if $p ( x + y ) \leq p ( x ) + p ( y )$ and $p ( \lambda x ) = \lambda p ( x )$ when $\lambda \geq 0$

Hahn-Banach: Let X be a real vector space, p a sublinear functional on X, M a subspace of X, and f a linear functional on M such that $f | _ { M } \leq p | _ { M }$ . Then there exists a linear functional F on X such that $F \leq p$ on X and $F | _ { M } = f$

For the complex case, we require $| f ( x ) | \leq p ( x )$ and we get $| F ( x ) | \leq p ( x )$

28 (Baire Category) We say C is nowhere dense if $( \overline { { C } } ) ^ { \circ } = \varnothing$

Theorem: Let X be a complete metric space. Then if $\left\{ U _ { n } \right\}$ is a sequence of open dense sets, $\cap U _ { n }$ is dense. Thus, X is not a countable union of nowhere dense sets.

A set that is a countable union of nowhere dense sets is said to be of first category (and it’s complement is called residual). A set which is not a countable union of nowhere dense sets is called second category.

29 (uniform boundedness principle) Let X be a Banach space and Y a normed space, ${ \mathcal { S } } \subseteq L ( X , Y )$ where S is pointwise bounded $( { \mathrm { i . e . ~ } } \forall x \in X , \operatorname* { s u p } \{ \| T x \| \mid T \in S \} < \infty )$

Then S is uniformly bounded $\left( \mathrm { i . e . ~ \ s u p } _ { T \in S } \| T \| < \infty \right.$

30 (Banach-Steinhaus) Suppose X is a Banach space and Y is a normed space, and $\{ T _ { n } \} \subseteq L ( X , Y )$ and for all $x \in X , T _ { n } x \to T x$ in Y . Then $T \in L ( X , Y )$

31 (open mapping theorem) little open mapping theorem: Suppose X is a Banach space and Y is a normed space, $T \in L ( X , Y )$ and $r > 0$ . Then if $\overline { { T ( B ( 0 , 1 ) ) } } \supseteq B ( 0 , r )$ then $T ( B ( 0 , 1 ) ) \supseteq B ( 0 , r )$

open mapping theorem: Suppose $X , Y$ are Banach spaces and $T \in L ( X , Y )$ is surjective.   
Then $T$ is an open mapping.

Remark: For a linear map $T , T$ is open $\Leftrightarrow \exists r > 0$ such that $T ( B ( 0 , 1 ) ) \supseteq B ( 0 , r )$

32 (closed graph) For Banach spaces $X , Y$ and $T : X  Y$ linear, then $T \subseteq X \times Y$ is closed $\Leftrightarrow T$ is a bounded linear operator.

33 (Separation Theorem / Geometric Hahn-Banach) Say X is a LCTVS over R and $U , C \subseteq X$ are convex sets such that $U \cap C = \emptyset$ and $U ^ { \circ } \neq \emptyset$ . Then there exists some non-zero $f \in X ^ { * }$ and some $\alpha \in \mathbb { R }$ such that $U \subseteq [ f < \alpha ]$ and $C \subseteq [ f \geq \alpha ]$

Corollary 1: If (X, T ) is Hausdorff LCTVS, then $X ^ { * }$ separates points of X

Corollary 2: If (X, T ) is a LCTVS, $C \subseteq X$ is convex, then ${ \overline { { C } } } ^ { \mathrm { w e a k } } = { \overline { { C } } } ^ { T }$

Corollary 3: If X is a normed space and $A \subseteq X$ , then A is norm bounded $\Leftrightarrow A$ is weakly bounded (where A is weakly bounded if for all $x ^ { * } \in X ^ { * } , \operatorname* { s u p } _ { x \in X } \left| \langle x ^ { * } , x \rangle \right| < \infty$

34 (Banach-Alaoglu) If X is a normed space, then ${ \overline { { B _ { X ^ { * } } } } } = \{ x ^ { * } \in X ^ { * } \mid \| x ^ { * } \| \leq 1 \}$ is weak∗-compact.

Corollary: If X is reflexive, then $\overline { { B _ { X ^ { * } } } }$ is weakly compact.

X is reflexive if and only if $\overline { { B _ { X } } }$ is weakly compact.

35 (Goldstine) Suppose X is normed. Then $\widehat { B _ { X } }$ is weak∗-dense in $B _ { X ^ { * * } } , \widehat { B _ { X } } \subseteq B _ { X ^ { * } }$ where we have equality IFF X is reflexive.

36 (Riesz-Fisher) For $1 \leq p < \infty$ , Lp is complete

37 (H¨older’s inequality) Let q be the conjugate exponent of p so $\begin{array} { r } { { \frac { 1 } { p } } + { \frac { 1 } { q } } = 1 \ ( \mathrm { i . e . } \ q = { \frac { p } { p - 1 } } ) } \end{array}$

For measurable $f , g$ and $1 < p < \infty$ then $\| f g \| _ { 1 } \leq \| f \| _ { p } \| g \| _ { q } .$

If $f \in L ^ { p }$ and $g \in L ^ { q }$ if and only if $f = 0 ~ \mathrm { a . e }$ . OR $g = 0 \ \mathrm { a . e }$ . OR $| f | ^ { p }$ is a scalar multiple of $| g | ^ { q }$

If $f \in L ^ { p }$ then $\begin{array} { r } { \| f \| _ { p } = \operatorname* { m a x } \left\{ \int f g d \mu \mid \| g \| _ { q } \leq 1 \right\} } \end{array}$ (maximum is achieved! by $g = \operatorname { s g n } ( f ) )$

Alternate H¨older’s inequality: For $0 < \lambda < 1$ , then $\begin{array} { r } { \int | f | ^ { \lambda } | g | ^ { 1 - \lambda } \leq \left( \int | f | \right) ^ { \lambda } \left( \int | g | \right) ^ { 1 - \lambda } } \end{array}$

38 (Minkowski) For $1 \leq p < \infty , \| f + g \| _ { p } \leq \| f \| _ { p } + \| g \| _ { p }$

39 (Riesz-Thorin) If $1 \leq p _ { 0 } , p _ { 1 } \leq \infty , 1 \leq q _ { 0 } , q _ { 1 } \leq \infty$ and $0 < t < 1$ with

$$
{ \frac { 1 } { p _ { t } } } : = { \frac { t } { p _ { 0 } } } + { \frac { 1 - t } { p _ { 1 } } } \qquad { \frac { 1 } { q _ { t } } } : = { \frac { t } { q _ { 0 } } } + { \frac { 1 - t } { q _ { 1 } } }
$$

Suppose $X _ { 0 } = L ^ { p _ { 0 } } ( \mu ) , X _ { 0 } = L ^ { p _ { 1 } } ( \mu )$ and $Y _ { 0 } = L ^ { q _ { 0 } } ( \nu ) , Y _ { 1 } = L ^ { q _ { 1 } } ( \nu )$ (compatible couple).

Then for $0 < t < 1 , L ^ { p _ { t } } ( \mu ) + L ^ { q _ { t } } ( \nu )$ is an exact interpolation pair for $\widetilde { X } = ( X _ { 0 } , X _ { 1 } ) , \widetilde { Y } =$ $( Y _ { 0 } , Y _ { 1 } )$ .

40 (Marcinkiewicz Interpolation) Let $( X , { \mathcal { M } } , \mu )$ be a measure space and D a subspace of $L ^ { 0 } ( \mu )$ . We say $T : D \to L ^ { 0 } ( \nu )$ is sublinear if

1. $| T ( f + g ) | \leq | T f | + | T g |$

2. $| T ( c f ) | = c | T f | { \mathrm { ~ i f ~ } } c \geq 0$

T is said to be of strong type $( p , q )$ if $T ( L ^ { p } ( \mu ) ) \subseteq L ^ { q } ( \nu )$ and $\Vert T \bigr | _ { L ^ { p } ( \mu ) } \bigr | \bigr | _ { L ^ { p } ( \mu ) \to L ^ { q } ( \nu ) } < \infty$

$T$ is said to be of weak type $( p , q )$ if $T ( L ^ { p } ( \mu ) ) \ \subseteq \ L ^ { q , \infty } ( \nu )$ and $\Vert T | _ { L ^ { p } ( \mu ) } \Vert _ { L ^ { p } ( \mu )  L ^ { q , \infty } ( \nu ) } = :$ $\begin{array} { r } { \operatorname* { s u p } _ { \| \boldsymbol { x } \| _ { L ^ { p } ( \mu ) } \leq 1 } [ T x ] _ { q , \infty } < \infty } \end{array}$ where for $q < \infty , \ L ^ { q , \infty } ( \nu ) = \{ f \in L ^ { 0 } ( \nu ) \mid \operatorname * { s u p } _ { t } t ^ { 1 / q } \nu [ | f | > t ] = :$ $[ f ] _ { q , \infty } < \infty \}$

Weak type $( p , \infty )$ is the same as strong type $( p , \infty )$

Marcinkiewicz Interpolation Theorem: $1 \leq p _ { 0 } \leq q _ { 0 } \leq \infty$ and $1 \leq p _ { 1 } \leq q _ { 1 } \leq \infty$ $q _ { 0 } \neq q _ { 1 }$ and $0 < t < 1$ b,

$$
{ \frac { 1 } { p _ { t } } } : = { \frac { 1 - t } { p _ { 0 } } } + { \frac { t } { p _ { 1 } } } \qquad { \frac { 1 } { q _ { t } } } : = { \frac { 1 - t } { q _ { 0 } } } + { \frac { t } { q _ { 1 } } }
$$

If $T : L ^ { p _ { 0 } } ( \mu ) + L ^ { p _ { 1 } } ( \mu ) \to L ^ { 0 } ( \nu )$ is sublinear, and is of weak type $( p _ { 0 } , q _ { 0 }$ and weak type $( p _ { 1 } , q _ { 1 } )$ then $T$ is of strong type $( p _ { t } , q _ { t } )$ for all $0 < t < 1$ and

$$
\| T \| _ { L ^ { p _ { t } } \to L ^ { q _ { t } } } \leq \frac { C \Big ( \| T \| _ { L ^ { p _ { 0 } } \to L ^ { p _ { 0 } , \infty } } \vee \| T \| _ { L ^ { p _ { 1 } } \to L ^ { p _ { 1 } , \infty } } \Big ) } { t ( 1 - t ) }
$$

where $C = C ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } )$ is some constant $< \infty$

41 (Krein-Milman) If C is a convex set in a real vector space, then $x \in C$ is said to be an extreme point provided whenever $y , z \in C$ and $0 < \lambda < 1 , x = \lambda y + ( 1 - \lambda ) z$ then $x = y = z$

Krein-Milman Lemma: If X is a Hausdorff LCTVS, and $C \subseteq X$ is a non-empty, compact, convex set then ext $( C ) \neq \emptyset$

Krein-Milman Theorem: If X is a Hausdorff LCTVS, $C \subseteq X$ is a non-empty, compact, convex set, then $C = { \overline { { \mathrm { c o n v } ( \mathrm { e x t } ( C ) ) } } }$ , where ext $\begin{array} { r } { ( C ) = \left\{ \begin{array} { r l r l } \end{array} \right. } \end{array}$ all extreme points of $C \}$

42 (Banach-Stone) Suppose $K _ { 1 } , K _ { 2 }$ are compact Hausdorff. Then $C ( K _ { 1 } )$ is isometrically isomorphic to $C ( K _ { 2 } )$ if and only if $K _ { 1 }$ is homeomorphic to $K _ { 2 }$

43 (Milman) If X is Hausdorff LCTVS and $M \subseteq X$ is compact with $C = { \overline { { \mathrm { c o n v } ( M ) } } }$

compact. Then $\operatorname { e x t } ( C ) \subseteq M$

44 (Kakatani fixed point theorem) We say T is an affine transformation if $T ( \alpha x +$ $( 1 - \alpha ) y ) = \alpha T x + ( 1 - \alpha ) T y { \mathrm { ~ f o r ~ } } 0 \leq \alpha \leq 1 , x , y \in K$

G is equicontinuous if for all neighborhoods U of 0, there exists a neighborhood V of 0 such that for $x , y \in K$ , if $x - y \in V$ then for all $T \in G , T x - T y \in U$

We call p a fixed point of $G { \mathrm { ~ i f ~ } } G ( p ) = \{ T p \mid T \in G \} = \{ p \}$

Theorem: Suppose X is a LCTVS and $K \subseteq X$ is convex compact, and G is an equicontinuous group (under composition) of affine transformations on K. Then G has a fixed point.