# QUALIFYING EXAM: REAL ANALYSIS

Tuesday, September 9, 2025 (180 minutes).

Please turn all cell phones off completely and put them away.

No books, notes, or electronic devices are permitted during this exam.

You must show your work to receive credit.

Present your solutions clearly, and indicate which result you are using at every step.

You may use without proof any result (theorem, proposition, lemma, corollary) contained in Chapters 1-6 and 8 of Gerald B. Folland, Real Analysis.

Name (print):

Student ID number:

1. [15 pts] Let M be an infinite σ-algebra of subsets of a set $X$

For ${ \dot { A ^ { \cdot } } } \subset X , { \dot { A } } \neq \emptyset , X$ , consider the collection $\mathcal { M } _ { A } : = \{ B \cap A : B \in \mathcal { M } \}$

(1) Prove that $\mathcal { M } _ { A }$ is a σ-algebra of subsets of A.

(2) Prove that at least one of $\mathcal { M } _ { A }$ and $\mathcal { M } _ { A ^ { c } }$ contains infinitely many elements.

(3) Prove that M contains infinitely many, pairwise disjoints sets.

(4) Prove that M is uncountable.

You can use this page

2. [20 pts] Let $K \subset \mathbb { R } ^ { 2 }$ be compact. Given $\delta > 0$ , consider the set

$$
K _ { \delta } : = \{ x \in \mathbb { R } ^ { 2 } : d ( x , K ) : = \operatorname* { i n f } _ { y \in K } | x - y | = \delta \} ,
$$

that is the collection of points at distance δ from $K$

(1) Prove that $K _ { \delta }$ is closed and that the distance is always realized, that is, for every $x \in K _ { \delta }$ there is $y _ { x } \in K$ such that $| y _ { x } - x | = \delta$ •

(2) Given $x \in K _ { \delta }$ and $\epsilon \in ( 0 , \delta )$ , show that

$$
\mathcal { L } ^ { 2 } ( B _ { \epsilon } ( x ) \cap K _ { \delta } ^ { c } ) \geq \frac { \pi \epsilon ^ { 2 } } { 4 } ,
$$

where $\mathcal { L } ^ { 2 }$ is the Lebesgue measure on $\mathbb { R } ^ { 2 } , B _ { \varepsilon } ( x )$ is the ball of radius ε centered at x and $K _ { \delta } ^ { c } = \mathbb { R } ^ { 2 } \setminus K _ { \delta }$

(3) Using the Lebesgue differentiation theorem show that $\mathcal { L } ^ { 2 } ( K _ { \delta } ) = 0$

You can use this page

3. [15 pts] Let $\Omega \subset \mathbb { R } ^ { n }$ be a Lebesgue measurable set, $f \colon \Omega  \mathbb { R }$ measurable and define

$X : = \{ u \in L ^ { \infty } ( \Omega ) : u \geq f$ a.e. in Ω} and $Y : = \{ u \in L ^ { \infty } ( \Omega ) : \int _ { \Omega } u \phi d x \geq \int _ { \Omega } f \phi d x \quad \forall \phi \in W \} ,$

where $W : = \{ \phi \in L ^ { 1 } ( \Omega ) : \phi f \in L ^ { 1 } ( \Omega ) , \ \phi \geq 0 \ \mathrm { a . e }$ . in Ω}.

(1) Prove that if $f \in L ^ { \infty } ( \Omega )$ , then $X = Y$

(2) Prove that (1) holds when f is just measurable.

(3) Prove that X is sequentially closed in the weak∗-topology in $L ^ { \infty } ( \Omega )$

You can use this page

4. [15 pts] Let Ω be a bounded, Lebesgue measurable subset of $\mathbb { R } ^ { n }$ such that ${ \mathcal { L } } ^ { n } ( \Omega ) > 0$ where ${ \mathcal { L } } ^ { n }$ is the Lebesgue measure on $\mathbb { R } ^ { n }$ . Let

$$
{ \mathcal { C } } : = \{ f \in L ^ { 2 } ( \Omega ) : \int _ { \Omega } f ( x ) d x = 0 \} .
$$

(1) Prove that C is a closed subspace of $L ^ { 2 } ( \Omega )$

(2) Prove that for every $g \in L ^ { 2 } ( \Omega )$ we have

$$
P c ( g ) = g - \frac { 1 } { \mathscr { L } ^ { n } ( \Omega ) } \int _ { \Omega } g ( x ) d x ,
$$

where $P _ { C } ( g )$ denotes the orthogonal projection of $g$ onto C.

(3) Prove that ${ \mathcal { C } } ^ { \perp } = \{ g \in L ^ { 2 } ( \Omega ) : g = c { \mathrm { ~ a . e ~ } }$ . in Ω for some $c \in \mathbb { C } \}$

You can use this page

5. [15 pts] Let $f \in \mathrm { L } ^ { 2 } ( \mathbb { R } ^ { n } )$ such that ${ \widehat { f } } ( \xi ) \neq 0$ , for a.e. $\xi \in \mathbb { R } ^ { n }$ . For $a \in \mathbb { R } ^ { n }$ , let $f _ { a } \in \mathrm { L } ^ { 2 } ( \mathbb { R } )$ be given by $f _ { a } ( x ) = f ( x - a )$ .

(1) Prove that if $a \in \mathbb { R } ^ { n }$ , then ${ \widehat { f } } _ { a } ( \xi ) = e ^ { - 2 \pi i \xi \cdot a } { \widehat { f } } ( \xi )$ , for a.e. $\xi \in \mathbb { R } ^ { n }$

Note: You can use without proof the fact that this identity holds if $f \in \operatorname { L } ^ { 1 } ( \mathbb { R } )$

(2) Prove that the linear span of $\{ f _ { a } : a \in \mathbb { R } ^ { n } \}$ is dense in $\operatorname { L } ^ { 2 } ( \mathbb { R } ^ { n } )$

You can use this page

6. [20 pts] Consider the Hilbert space $\ell ^ { 2 } ( \mathbb { N } )$ with the usual norm $\begin{array} { r } { \| f \| _ { 2 } = \big ( \sum _ { n \in \mathbb { N } } | f ( n ) | ^ { 2 } \big ) ^ { 1 / 2 } } \end{array}$

(1) Prove that $\ell ^ { 2 } ( \mathbb { N } )$ is separable, i.e., contains a countable dense subset.

(2) Let $S \subset \ell ^ { 2 } ( \mathbb { N } )$ be an uncountable set. Prove that S contains a convergent sequence which consists of pairwise distinct elements of S.

Hint: Use (1) to first prove that for every $\varepsilon > 0$ , there exists $\eta \in \ell ^ { 2 } ( \mathbb { N } )$ such that the set $\{ \xi \in S \ : \ \| \xi - \eta \| _ { 2 } < \varepsilon \}$ is uncountable.

You can use this page