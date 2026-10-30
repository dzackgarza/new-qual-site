# QUALIFYING EXAM: REAL ANALYSIS

May 18, 2026 (180 minutes).

Please turn all cell phones off completely and put them away.

No books, notes, or electronic devices are permitted during this exam.

You must show your work to receive credit.

Present your solutions clearly, and indicate which result you are using at every step.

You may use without proof any result (theorem, proposition, lemma, corollary) contained in Chapters 1-8 of Gerald B. Folland, Real Analysis. Be sure to explicitly check that all necessary assumptions are satisfied.

Name (print):

Student ID number:

1. [15 pts] Let $( \Omega , { \mathcal { M } } , \mu )$ be a measure space. We say that a sequence $( f _ { n } ) _ { n } \subset L ^ { 1 } ( \Omega , \mu )$ is equi-integrable if the following two conditions are satisfied:

a. for every $\epsilon > 0$ there is a $\delta > 0$ such that

$$
\operatorname* { s u p } _ { n } \int _ { E } \left| f _ { n } \right| d \mu < \epsilon \qquad \forall E \in { \mathcal { M } } { \mathrm { ~ s u c h ~ t h a t ~ } } \mu ( E ) < \delta
$$

b. for every $\epsilon > 0$ there is a $A _ { \epsilon } \in { \mathcal { M } }$ such that $\mu ( A _ { \epsilon } ) < + \infty$ and

$$
\operatorname* { s u p } _ { n } \int _ { \Omega \backslash A _ { \epsilon } } | f _ { n } | d \mu < \epsilon .
$$

(1) Show that if $( f _ { n } ) _ { n }$ is equi-integrable and $f _ { n } \to f \mu { \mathrm { - a . e } }$ . then $f \in L ^ { 1 } ( \Omega , \mu )$ and $f _ { n }  f$ strongly in $L ^ { 1 }$ . (Hint: use Egorov’s Theorem, Fatou’s Lemma, and the provided conditions to split the integral of $\vert f _ { n } - f \vert$ into three arbitrarily small parts).

(2) Show that if $( f _ { n } ) _ { n }$ converges strongly in $L ^ { 1 }$ then condition a. holds. (Hint: Use absolute continuity).

You can use this page

2. [20 pts] Consider the function

$$
d ( f , g ) : = \operatorname* { s u p } _ { 0 \leq x \leq 1 } \left. \int _ { 0 } ^ { x } ( f ( t ) - g ( t ) ) d t \right. \qquad f , g \in L ^ { 1 } ( [ 0 , 1 ] ) .
$$

Let $C : = \{ f \in L ^ { 1 } ( [ 0 , 1 ] ) : | f ( t ) | \leq 1$ for a.e. $t \in [ 0 , 1 ] \}$

(1) Prove that d is a metric in $L ^ { 1 } ( [ 0 , 1 ] )$

(2) Prove that C is compact in $( L ^ { 1 } ( [ 0 , 1 ] ) , d )$ (Hint: let $\begin{array} { r } { \tilde { C } = \{ F ( x ) : = \int _ { 0 } ^ { x } f : f \in C \} } \end{array}$ and use Arzela-Ascoli’s theorem).

You can use this page

3. [15 pts] Let X be a Banach space with open unit ball $B = \{ x \in X : \| x \| < 1 \}$ . Let $u \in X$ and ${ \dot { \mathcal { M } } } \subsetneq X$ be a proper vector subspace such that $X = \{ \lambda u + y : \lambda \in \mathbb { C } , \ y \in \mathcal { M } \}$ .

(1) Prove that $B + \mathcal { M } = X$ if and only if M is not closed.

(2) Prove that $B + { \mathcal { M } }$ is weakly open, regardless of whether or not M is closed. (You may combine your proofs for (a) and (b) if you like).

You can use this page

4. [20 pts] Let $\mathcal { M } ( [ 0 , 1 ] )$ denote the space of all complex Radon measures on $[ 0 , 1 ]$ , and $\mathcal { P } ( [ 0 , \dot { 1 } ] )$ the subset of probability measures (i.e. positive measures that assign measure 1 to the set $[ 0 , 1 ] )$ . Let $f \colon [ 0 , 1 ] \times [ 0 , 1 ] $ R be a continuous function, and let $U$ be the set of all $\mu \in \mathcal P ( [ 0 , 1 ] )$ satisfying

$$
\forall y \in [ 0 , 1 ] \qquad \left| \int _ { 0 } ^ { 1 } f ( x , y ) d \mu ( x ) \right| < 1 .
$$

Prove that U is a relatively open subset of ${ \mathcal { P } } ( [ 0 , 1 ] )$ with respect to the weak∗ topology.

You can use this page

5. [15 pts] Construct a meager (i.e. first category) subset E of R that is conull in R with respect to the Lebesgue measure $( { \mathrm { i . e . ~ } } m ( \mathbb { R } \setminus E ) = 0$ , where m is Lebesgue measure).

You can use this page

6. [25 pts] Let $f _ { k } \in L ^ { 2 } ( \mathbb { R } ^ { n } )$ and $\| f _ { k } \| _ { 2 } \le 1$ for each $k = 1 , 2 , \dots { }$ , and assume that

$$
\operatorname* { l i m } _ { R \to \infty } \operatorname* { s u p } _ { k \geq 1 } \int _ { \mathbb { R } ^ { n } \setminus B _ { R } ( 0 ) } \left( | f _ { k } ( x ) | ^ { 2 } + | { \hat { f } } _ { k } ( x ) | ^ { 2 } \right) d x = 0
$$

with $B _ { R } ( 0 )$ the ball of radius R centered at the origin. Show that $\{ f _ { k } \} _ { k \ge 1 }$ has a convergent subsequence (in $L ^ { 2 } ( \mathbb { R } ^ { n } ) )$ .

You can use this page