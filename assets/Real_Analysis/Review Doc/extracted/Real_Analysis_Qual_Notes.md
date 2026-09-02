Real Analysis Qualifying Exam Review

## Table of Contents

## Contents

1 Basics 4   
1.1 Table of Notation . 4   
1.2 Useful Techniques 4   
1.3 The Absolute Essentials 6   
1.4 Quintessential Qual Problems 8   
1.5 Definitions . 9   
1.5.1 Convergence and Continuity 9   
1.5.2 Function Spaces 11   
1.5.3 Measure Theory 11   
1.5.4 Integrals and Lp Spaces 13   
1.5.5 Functional Analysis 14   
1.6 Theorems 15   
1.6.1 Topology / Sets . 16   
1.6.2 Functions 17   
1.6.3 Sequences and Series 18   
1.7 Uniform Convergence 18   
1.7.1 Series 19   
1.8 Commuting Limiting Operations 20   
1.9 Probabilist Tools: “Almost” Theorems 21   
1.10 Slightly Advanced Stuff 23   
1.11 Examples and Counterexamples 23   
1.11.1 Dirichlet function 24   
1.11.2 Dirichlet with a Continuous Point 24   
1.11.3 Dirichlet with a Differentiable Point 24   
1.11.4 Dirichlet with Two Functions 25   
1.12 The Thomae function: . . 26   
2 Measure Theory 26   
2.1 Abstract Measure Theory 27   
2.2 Outer Measure 30   
2.3 Measures on $\mathbb { R } ^ { d }$ 30   
2.4 Exercises 32   
3 Integration 32   
3.1 Unsorted 32   
3.2 Examples of (Non)Integrable Functions 39   
3.3 L1 Facts . 40   
3.4 Lp Facts 43   
3.5 Counterexamples 44   
4 Fourier Transform and Convolution 47   
4.1 The Fourier Transform 47   
4.2 Approximate Identities 49   
5 Functional Analysis 51   
5.1 Theorems 51   
6 Extra Problems: Measure Theory 56   
6.1 Greatest Hits 56   
6.2 By Topic 56   
6.2.1 Topology 56   
6.2.2 Continuity 57   
6.2.3 Differentiation 57   
6.2.4 Advanced Limitology 57   
6.2.5 Unsorted 59   
6.3 Rectangles . 60   
6.4 Outer Measure 60   
6.5 Lebesgue Measurable Sets 60   
6.6 Lebesgue Measurable Functions 60   
Extra Problems from Problem Sets 60   
7.1 2010 6.1 60   
7.2 2010 6.2 61   
7.3 2010 6.5 61   
7.4 2010 7.1 61   
7.5 2010 7.2 61   
7.6 2010 7.3 62   
7.7 2010 7.4 62   
7.8 2010 7.5 62   
7.9 2010 7.6 63   
7.10 2010 7.7 63   
7.11 2010 7 Challenge 1: Generalized Holder 64   
7.12 2010 7 Challenge 2: Young’s Inequality . 64   
7.13 2010 9.1 64   
7.14 2010 9.2 64   
7.15 2010 9.3 65   
7.16 2010 9.5b 65   
7.17 2010 9.6 65   
7.18 2010 9 Challenge 65   
7.19 2010 10.1 66   
7.20 2010 10.2 66   
7.21 2010 10.3 66   
7.22 2010 10.4 66   
8 Common Inequalities 67   
8.1 The GOATs 67   
8.2 Less common 69   
8.3 Inequalities that appear in proofs 72

## Basics

## 1.1 Table of Notation

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $\| f \| _ { \infty } : = \operatorname* { s u p } _ { x \in \mathrm { d o m } ( f ) } | f ( x ) |$ </td><td>The Sup norm</td></tr><tr><td></td><td></td></tr><tr><td> $\left\| f \right\| _ { L ^ { \infty } } : = \operatorname* { i n f } \left\{ M \geq 0 \bigg | | f ( x ) | \leq M \mathrm { ~ f o r ~ a . e . ~ } x \right\}$ </td><td>The  $L ^ { \infty }$  norm</td></tr><tr><td></td><td></td></tr><tr><td> $f _ { n } \stackrel { n \to \infty } { \to } f$ </td><td>Convergence of a sequence</td></tr><tr><td></td><td>Vanishing at</td></tr><tr><td> $f ( x ) \stackrel { | x |  \infty } { {  } } 0$ </td><td>infinity</td></tr><tr><td></td><td></td></tr><tr><td> $\int _ { | x | \geq N } f ^ { \ N \to \infty } 0$ </td><td>Having small tails</td></tr><tr><td></td><td></td></tr><tr><td></td><td>A Hilbert</td></tr><tr><td> $H , \mathcal { H }$ </td><td>space</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td>A topological</td></tr><tr><td></td><td></td></tr><tr><td>X</td><td>space</td></tr></table>

<!-- image-->

## 1.2 Useful Techniques

<!-- image-->

• General advice: try swapping the orders of limits, sums, integrals, etc.

## • Limits:

– Take the lim sup or lim inf, which always exist, and aim for an inequality like

$$
c \leq \operatorname* { l i m } \operatorname* { i n f } a _ { n } \leq \operatorname* { l i m } \operatorname* { s u p } a _ { n } \leq c .
$$

– lim $f _ { n }$ = lim sup $f _ { n } =$ lim inf $f _ { n }$ iff the limit exists, so to show some g is a limit, show

$$
\operatorname* { l i m } \operatorname* { s u p } f _ { n } \leq g \leq \operatorname* { l i m } \operatorname* { i n f } f _ { n } \qquad ( \Longrightarrow \ g = \operatorname* { l i m } f ) .
$$

– A limit does not exist if lim inf $a _ { n } >$ lim sup $a _ { n }$

## • Sequences and Series

– If $f _ { n }$ has a global maximum (computed using $f _ { n } ^ { \prime }$ and the first derivative test) $M _ { n } \to 0$ then $f _ { n } \to 0$ uniformly.

– For a fixed x, if $f = \sum f _ { n }$ converges uniformly on some $B _ { r } ( x )$ and each $f _ { n }$ is continuous at x, then $f$ is also continuous at x .

## • Equalities

– Split into upper and lower bounds:

$$
a = b \iff a \leq b { \mathrm { ~ a n d ~ } } a \geq b .
$$

– Use an epsilon of room:

$$
( \forall \epsilon , \ a < b + \varepsilon ) \implies a \le b .
$$

– Showing something is zero:

$$
( \forall \epsilon , \ \| a \| < \varepsilon ) \implies a = 0 .
$$

• Continuity / differentiability:

– Show it holds on [−M, M ] for all M to get it to hold on R.

– In higher dimensions: intersect with a ball $B _ { R } ( \mathbf { 0 } ) \subset \mathbb { R } ^ { n }$ about zero.

## • Simplifications:

– To show something for a measurable set, show it for bounded/compact/elementary sets and use approximations in measure.

– To show something for an arbitrary function, try various dense classes of functions: continuous, bounded, compactly supported, simple, indicator functions, etc and use approximations in norm.

– Replace $\varepsilon \to 0$ with an arbitrary countable sequence $( x _ { n } \to 0 )$

♦ Note: this is not always helpful, since you now have to predicate over all such sequences.

## • Integrals

– Calculus techniques: Taylor series, IVT, MVT, etc.

– Break up $\mathbb { R } ^ { n } = \left\{ \left| x \right| \leq 1 \right\} \left[ { \big \lceil } \left\{ \left| x \right| > 1 \right\} \right.$

$\diamondsuit$ Or break integration region into disjoint annuli.

For pairs of functions $f , g \colon$ break up into $\{ f > g \} \operatorname { I I } \left\{ f = g \right\} \operatorname { I I } \left\{ f < g \right\}$

Tail estimates!

Most of what works for integrals will work for sums.

## • Measure theory:

– Always consider bounded sets, and if E is unbounded write $E = \bigcup _ { n \geq 0 } \left( B _ { n } ( 0 ) \cap E \right)$ and use countable subadditivity or continuity of measure.

$F _ { \sigma }$ sets are Borel, so establish something for Borel sets and use this to extend it to Lebesgue.

$- \ s = \operatorname* { i n f } \left\{ x \in X \right\} \implies$ for every ε there is an $x \in X$ such that $x \leq s + \varepsilon { \mathrm { ~ o r ~ } } x \in [ s , s + \varepsilon ]$

• Useful facts about continuous compactly supported $( C _ { c } ^ { 0 } ( \mathbb { R } ) )$ functions:

– Uniformly continuous

– Bounded almost everywhere

## 1.3 The Absolute Essentials

## Proposition 1.3.1(Convergent Sums Have Small Tails).

$$
\sum a _ { n } < \infty \implies a _ { n } \to 0 \quad \mathrm { a n d } \quad \sum _ { k = N } ^ { \infty } a _ { n } { \overset { N \to \infty } { \to } } 0
$$

## Theorem 1.3.2(Uniform Limit Theorem).

If $f _ { n }  f$ pointwise and uniformly with each $f _ { n }$ continuous, then f is continuous. a

aSlogan: a uniform limit of continuous functions is continuous.

## Proof .

• Follows from an $\varepsilon / 3$ argument:

$$
| F ( x ) - F ( y | \leq | F ( x ) - F _ { N } ( x ) | + | F _ { N } ( x ) - F _ { N } ( y ) | + | F _ { N } ( y ) - F ( y ) | \leq \varepsilon \to 0 .
$$

– The first and last $\varepsilon / 3$ come from uniform convergence of $F _ { N }  F$

```latex
– The middle $\varepsilon / 3$ comes from continuity of each $F _ { N }$
• So just need to choose $N$ large enough and δ small enough to make all $3 \ \varepsilon$ bounds hold.

Proposition 1.3.3(Uniform Limits Commute with Integrals).
If $f _ { n }  f$ uniformly, then $\int f _ { n } = \int f .$
Proposition 1.3.4(Weak $\begin{array} { r } { M \mathbf { - } \pmb { T e s t } ) . } \end{array}$
If $f _ { n } ( x ) \leq M _ { n }$ for a fixed x where $\sum M _ { n } < \infty ,$ , then the series $f ( x ) = \sum f _ { n } ( x )$ converges
pointwise.a
aNote that this is only pointwise convergence of $f ,$ whereas the full M-test gives uniform convergence.
Proposition 1.3.5(The Weierstrass $\mathbf { \Psi } _ { M - \pmb { T } e s t { \imath } } )$
If supx∈A $| f _ { n } ( x ) | \leq M _ { n }$ for each n where $\sum M _ { n } < \infty ,$ , then $\sum _ { n = 1 } ^ { \infty } f _ { n } ( x )$ converges uniformly and
absolutely on $A , \ a$ Conversely, if $\sum f _ { n }$ converges uniformly on A then $\operatorname* { s u p } _ { x \in A } | f _ { n } ( x ) |  0 .$
aIt suffices to show $| f _ { n } ( x ) | \leq M _ { n }$ for some $M _ { n }$ not depending on x.
Proposition 1.3.6(Borel Characterization of Measurable $S e t s )$
If E is Lebesgue measurable, then $E = H \amalg N$ where $H \in F _ { \sigma }$ and N is null.
Proof (of Borel characterization).
For every $\frac { 1 } { n }$ there exists a closed set $K _ { n } \subset E$ such that $m ( E \backslash K _ { n } ) \leq { \frac { 1 } { n } }$ . Take $K = \cup K _ { n }$ , wlog
$K _ { n } \nearrow K$ so $m ( K ) = \operatorname* { l i m } m ( K _ { n } ) = m ( E )$ . Take $N : = E \setminus K$ , then $m ( { \ddot { N } } ) = 0$
Theorem 1.3.7(Measurable sets can be approximated by open/closed/compact
sets.).
Suppose E is measurable; then for every $\varepsilon > 0 ,$
1. There exists an open $O \supset E$ with $m ( O \setminus E ) < \varepsilon$
2. There exists a closed $F \subset E$ with $m ( E \setminus F ) < \varepsilon$
3. There exists a compact $K \subset E$ with $m ( E \setminus K ) < \varepsilon .$
Proof (that measurable sets can be approximated).
• (1): Take $\{ Q _ { i } \} \equiv E$ and set $O = \cup Q _ { i } .$
• (2): Since $E ^ { c }$ is measurable, produce $O \supset E ^ { c }$ with $m ( O \setminus E ^ { c } ) < \varepsilon .$
– Set $F = O ^ { c } .$ , so $F$ is closed.
– Then $F \subset E$ by taking complements of $O \supset E ^ { c }$
$E \setminus F = O \setminus E ^ { c }$ and taking measures yields $m ( E \setminus F ) < \varepsilon$
```

• (3): Pick $F \subset E$ with $m ( E \setminus F ) < \varepsilon / 2$

– Set $K _ { n } = F \cap \mathbb { D } _ { n } , { \textrm { a } }$ ball of radius n about 0.

– Then $E \setminus K _ { n } \setminus E \setminus F$

– Since $m ( E ) < \infty ,$ , there is an N such that $n \geq N \implies m ( E \setminus K _ { n } ) < \varepsilon$

## 1.4 Quintessential Qual Problems

## Exercise 1.4.1 (?)

• Prove the Lebesgue integral is translation/dilation invariant.

• Prove continuity in L1: $\| \tau _ { h } f - f \| \stackrel { h \to 0 } { \longrightarrow } 0 .$

• Prove that E is measurable $\iff E = F [ [ Z$ with $F \in F _ { \sigma }$ and Z null $\iff E = G \setminus Z$ with $G \in G _ { \delta }$ and Z null.

• Show that $m ( E ) = \operatorname* { s u p } _ { K \subseteq E } m ( K ) \iff$ there exists $K = K ( \varepsilon )$ with $m ( K ) \in [ m ( E ) -$

ε, $, m ( E ) ]$

– What’s most useful here is the proof technique, not so much the result itself.

• Apply Fubini and Tonelli to literally anything.

• Prove that $\| f \| _ { p } \to \| f \| _ { \infty }$ over a finite measure space.

• Apply Cauchy-Schwarz to literally anything, in the form of $\| f g \| _ { 1 } \leq \| f \| _ { 2 } \| g \| _ { 2 } .$ .

## Proposition 1.4.2(Measurable Slices).

Let E be a measurable subset of $\mathbb { R } ^ { n }$ . Then

• For almost every $x \in \mathbb { R } ^ { n _ { 1 } }$ , the slice $E _ { x } : = \left\{ y \in \mathbb { R } ^ { n _ { 2 } } \Big | ( x , y ) \in E \right\}$ is measurable in $\mathbb { R } ^ { n _ { 2 } }$

• The function

$$
F : \mathbb { R } ^ { n _ { 1 } }  \mathbb { R }
$$

$$
x \mapsto m ( E _ { x } ) = \int _ { \mathbb { R } ^ { n _ { 2 } } } \chi _ { E _ { x } } \ d y
$$

is measurable and

$$
m ( E ) = \int _ { \mathbb { R } ^ { n _ { 1 } } } m ( E _ { x } ) \ d x = \int _ { \mathbb { R } ^ { n _ { 1 } } } \int _ { \mathbb { R } ^ { n _ { 2 } } } \chi _ { E _ { x } } \ d y \ d x .
$$

## Proof (of measurable slices).

:

• Let f be measurable on $\mathbb { R } ^ { n }$

• Then the cylinders $F ( x , y ) = f ( x )$ and $G ( x , y ) = f ( y )$ are both measurable on $\mathbb { R } ^ { n + 1 }$   
• Write $\mathcal { A } = \{ G \leq F \} \cap \{ G \geq 0 \}$ ; both are measurable.   
⇐= :   
• Let A be measurable in $\mathbb { R } ^ { n + 1 }$   
• Define $A _ { x } = \left\{ y \in \mathbb { R } \ \middle | \ ( x , y ) \in \mathcal { A } \right\}$ , then $m ( A _ { x } ) = f ( x )$   
• By the corollary, $A _ { x }$ is measurable set, $x \mapsto A _ { x }$ is a measurable function, and $m ( A ) =$   
$\int f ( x ) \ d x .$   
• Then explicitly, $f ( x ) = \chi _ { A }$ , which makes $f$ a measurable function.

## 1.5 Definitions

## 1.5.1 Convergence and Continuity

$$
\operatorname* { l i m } _ { n } \operatorname* { s u p } a _ { n } = \operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { j \geq n } a _ { j } = \operatorname* { i n f } _ { n \geq 0 } \operatorname* { s u p } _ { j \geq n } a _ { j }
$$

$$
\operatorname* { l i m } _ { n } \operatorname* { i n f } a _ { n } = \operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } _ { j \geq n } a _ { j } = \operatorname* { s u p } _ { n \geq 0 } \operatorname* { i n f } _ { j \geq n } a _ { j } .
$$

Definition 1.5.2 (Continuity and Uniform Continuity)   
A function f : R → R is continuous on X iff for all $x _ { 0 } \in X$   
∀ε $\exists \delta ( \varepsilon , x _ { 0 } )$ such that $\forall y , | x _ { 0 } - y | < \delta \qquad \implies | f ( x _ { 0 } ) - f ( y ) | < \varepsilon$   
⇐⇒ ∀ε ∃δ(ε, x0) such that ∀h, |h| < δ $\implies | f ( x _ { 0 } ) - f ( x _ { 0 } \pm h ) | < \varepsilon .$   
f is uniformly continuous on X iff   
∀ε ∃δ(ε) such that ∀x, y, ∈ X |x − y| < δ =⇒ |f (x) − f (y)| < ε   
⇐⇒ ∀ε ∃δ(ε) such that ∀x, h, |h| < δ =⇒ |f (x) − f (x ± h)| < ε.   
These follow from the substitutions $x _ { 0 } - y = \mp h \implies y = x _ { 0 } \pm h .$

Remark 1.5.3: The main difference is that δ may depend on $x _ { 0 }$ and $\varepsilon$ in continuity, but only depends on ε in the uniform version. I.e. once δ is fixed, for continuity one may only range over x, but in uniform continuity one can range over all pairs x, y.

Proposition 1.5.4(Lipschitz implies uniformly continuous). If f is Lipschitz on X, then f is uniformly continuous on $X$ Supposing that

$$
\| f ( x ) - f ( y ) \| \leq C \| x - y \| ,
$$

for a fixed ε take $\delta ( \varepsilon ) : = \varepsilon / C$ , then

$$
\begin{array} { c } { \| f ( x ) - f ( y ) \| \leq C \| x - y \| } \\ { \leq C \delta } \\ { = C \left( \varepsilon / C \right) } \\ { = \varepsilon . } \end{array}
$$

## Definition 1.5.5 (Topological Notions)

Let X be a metric space and A a subset. Let $A ^ { \prime }$ denote the limit points of A, and ${ \overline { { A } } } : = A \cup A ^ { \prime }$ to be its closure.

• A neighborhood of p is an open set $U _ { p }$ containing p.

• An ε-neighborhood of p is an open ball $B _ { r } ( p ) : = \left\{ q ~ \left| ~ d ( p , q ) < r \right. \right\}$ for some $r > 0$

• A point $p \in X$ is an accumulation point or a limit point of A iff every punctured neighborhood $U _ { p } \setminus \{ p \}$ contains a point $q \in A$ , so $q \neq p .$

• If $p \in A$ and p is not a limit point of A, then p is an isolated point of A.

• A is closed iff $A ^ { \prime } \subset A .$ , so A contains all of its limit points.

• A point $p \in A$ is interior iff there is a neighborhood $U _ { p } \subset A$ that is strictly contained in A.

• A is open iff every point of A is interior.

• A is perfect iff A is closed and $A \subset A ^ { \prime } ,$ so every point of A is a limit point of A.

• A is bounded iff there is a real number M and a point $q \in X$ such that $d ( p , q ) < M$ for all $p \in A$

• A is dense in X iff every point $x \in X$ is either a point of A, so $x \in A$ , or a limit point of A, so $x \in A ^ { \prime } .$ . I.e., $X \subset A \cup A ^ { \prime }$

– Alternatively, ${ \overline { { A } } } = X$ , so the closure of A is X.

## Definition 1.5.6 (Pointwise Convergence)

A sequence of functions $\{ f _ { j } \}$ is said to converge pointwise to f if and only if

$$
\begin{array} { r } { ( \forall \varepsilon > 0 ) ( \forall x \in S ) \left( \exists n _ { 0 } = n _ { 0 } ( x , \varepsilon ) \right) ( \forall n > n _ { 0 } ) \left( | f _ { n } ( x ) - f ( x ) | < \varepsilon \right) . } \end{array}
$$

Definition 1.5.7 (Uniform Convergence)   
(∀ε > 0) (∃n0 = n0(ε)) (∀x ∈ S) (∀n > n0) (|fn(x) − f (x)| < ε) .   
Negated:a   
(∃ε > 0) (∀n0 = n0(ε)) (∃x = x(n0) ∈ S) (∃n > n0) (|fn(x) − f (x)| ≥ ε) .   
aSlogan: to negate, find a bad x depending on n0 that are larger than some ε.

## 1.5.2 Function Spaces

Definition 1.5.8 (Completeness)

A metric space is complete if every Cauchy sequence converges.

Fact 1.5.9

If X is complete, then absolutely convergent implies convergent.

Definition 1.5.10 (Nowhere Dense Sets)

Recall that a set S in X is dense ⇐⇒ every open $U \subseteq X$ intersects S. A set S is nowhere dense in $X \iff$ the closure of S has empty interior ⇐⇒ every subset (or interval) contains an open set (or a subinterval) that does not intersect S. This just says S is not dense in any subset $S ^ { \prime } \subseteq X$ , by negating what it means to be dense.

Definition 1.5.11 (Meager Sets)

A set is meager if it is a countable union of nowhere dense sets.

Proposition 1.5.12(Finite unions of nowhere dense sets are still nowhere dense).   
A finite union of nowhere dense is again nowhere dense.

Definition 1.5.13 (Baire Space)

A space X is a Baire space if and only if every countable intersections of open, dense sets is still dense.

## 1.5.3 Measure Theory

Definition 1.5.14 (Limsup and Liminf of Sets)

$$
\operatorname* { l i m i n f } _ { n } E _ { n } : = \bigcup _ { N = 1 } ^ { \infty } \bigcap _ { n = N } ^ { \infty } E _ { n } = \left\{ x \Big | x \in E _ { n } { \mathrm { ~ f o r ~ a l l ~ b u t ~ f i n i t e l y ~ m a n y ~ } } n \right\}
$$

$$
\operatorname* { l i m } _ { n } \operatorname* { s u p } E _ { n } : = \bigcap _ { N = 1 } ^ { \infty } \bigcup _ { n = N } ^ { \infty } E _ { n } = \left\{ x \Big | x \in E _ { n } \mathrm { ~ f o r ~ i n f i n i t e l y ~ m a n y ~ } n \right\} .
$$

Remark 1.5.15: How to derive these definitions: use that inf corresponds to intersections/existence and sup corresponds to unions/forall.

• For lim inf $E _ { n }$

$x \in$ lim inf $\begin{array} { r l } { E _ { n } } & { { } \Longleftrightarrow } \end{array}$ there exists some N such that $x \in \cap _ { n \geq N } E _ { n } ,$ i.e. $x \in E _ { n }$ for all $n \geq N$ . So $x$ is in all but finitely many n.

– How to remember: lim inf n $x _ { n } = \operatorname* { s u p } _ { n } \operatorname* { i n f } _ { k \geq n } x _ { n }$ for sequences, where sups look like unions and infs look like intersections.

– Alternatively: there exists an n (union) such that for all $k \geq n$ (intersection). . .

• For lim sup $E _ { n }$

$x \in$ lim sup $E _ { n } \iff$ for every N , there exists some $n \geq N$ such that $x \in E _ { n }$ . So x is an infinitely many $E _ { n }$

– How to remember: lim sup $x _ { n } = \operatorname { i n f } n$ sup $k \geq n x _ { n }$ for sequences, where sups look like n unions and infs look like intersections.

– Alternatively: for all n (intersection) there exists a $k \geq n$ (union). . .

It’s also useful to note that lim inf $E _ { n } \subseteq \operatorname* { l i m } \operatorname* { s u p } E _ { n }$ , since lim inf $E _ { n }$ are elements that are eventually in all sets, and lim sup $E _ { n }$ are elements in infinitely many sets.

Why these are useful: for finite measure spaces,

$$
\mu \left( \operatorname* { l i m } _ { n } \operatorname* { i n f } E _ { n } \right) \leq \operatorname* { l i m } _ { n } \operatorname* { i n f } \mu ( E _ { n } ) \leq \operatorname* { l i m } _ { n } \mu ( E _ { n } ) \leq \operatorname* { l i m } _ { n } \operatorname* { s u p } \mu ( E _ { n } ) \leq \mu \left( \operatorname* { l i m } _ { n } \operatorname* { s u p } E _ { n } \right) .
$$

If the lim sup and lim inf sets are equal, then one can define the set lim $E _ { n } : = \cup _ { n } E _ { n } { \mathrm { ~ i f ~ } } E _ { n } \not \sim E$ or   
lim $E _ { n } : = \cap _ { n } E _ { n }$ if $E _ { n } \searrow E$ in which case continuity of measure states   
n

$$
\mu \left( \operatorname* { l i m } _ { n } E _ { n } \right) = \operatorname* { l i m } _ { n } \mu ( E _ { n } ) .
$$

Definition 1.5.16 $( F _ { \sigma }$ and $G _ { \delta } ~ \mathrm { S e t s } )$

An $F _ { \sigma }$ set is a union of closed sets, and a $G _ { \delta }$ set is an intersection of opens. a

aMnemonic: $^ { 6 6 } \mathrm { F } ^ { \prime 9 }$ stands for ferme, which is “closed” in French, and σ corresponds to a “sum”, i.e. a union.

## Definition 1.5.17 (Outer Measure)

The outer measure of a set is given by

$$
m _ { * } ( E ) : = \operatorname* { i n f } _ { \{ Q _ { i } \} \supset E } \sum | Q _ { i } | ,
$$

where $| Q _ { i } |$ is the standard Euclidean volume of a cube in $\mathbb { R } ^ { n }$

Definition 1.5.18 (Lebesgue Measurable Sets)   
A subset $E \subseteq \mathbb { R } ^ { n }$ is Lebesgue measurable iff for every $\varepsilon > 0$ there exists an open set $O \supseteq E$   
such that $m _ { * } ( O \setminus E ) < \varepsilon$ In this case, we define $m ( E ) : = m _ { * } ( E )$

Definition 1.5.19 $( L ^ { + }$ : Measurable non-negative functions.) $f \in L ^ { + }$ iff f is measurable and non-negative.

## 1.5.4 Integrals and $L ^ { p }$ Spaces

A measurable function is integrable iff $\left\| f \right\| _ { 1 } < \infty .$

Definition 1.5.21 (The Infinity Norm / Essential supremum / Essentially bounded)

$$
\left\| f \right\| _ { \infty } : = \operatorname* { i n f } _ { \alpha \geq 0 } \left\{ \alpha \mid \mu \left( \left\{ | f | \geq \alpha \right\} \right) = 0 \right\} .
$$

In words, this is the smallest upper bound that holds almost everywhere, so $| f ( x ) | \leq \| f \| _ { \infty }$ holds for almost every x. A function $f : X \to \mathbb { C }$ is essentially bounded iff there exists a real number c such that $\mu ( \{ | f | > x \} ) = 0 , { \mathrm { i . e . ~ } } \| f \| _ { \infty } < \infty$

Definition 1.5.22 $( L ^ { \infty } )$

$$
L ^ { \infty } ( X ) : = \left\{ f : X \to \mathbb { C } \ \middle \vert \ f \mathrm { ~ i s ~ e s s e n t i a l l y ~ b o u n d e d ~ } \right\} : = \left\{ f : X \to \mathbb { C } \ \middle \vert \ \Vert f \Vert _ { \infty } < \infty \right\} .
$$

Definition 1.5.23 (Convolution)

$$
f \ast g ( x ) = \int f ( x - y ) g ( y ) d y .
$$

Definition 1.5.24 (Fourier Transform)

$$
{ \widehat { f } } ( \xi ) = \int f ( x ) \ e ^ { 2 \pi i x \cdot \xi } \ d x .
$$

Definition 1.5.25 (Dilation)

$$
\varphi _ { t } ( x ) = t ^ { - n } \varphi \left( t ^ { - 1 } x \right) .
$$

Definition 1.5.26 (Approximations to the identity)   
For $\varphi \in L ^ { 1 }$ , the dilations satisfy $\int \varphi _ { t } = \int \varphi ,$ and if $\int \varphi = 1$ then $\varphi$ is an approximate identity.

## 1.5.5 Functional Analysis

Definition 1.5.27 (Dual Norm)

For X a normed vector space and $L \in X ^ { \vee }$ , the dual norm or operator norm is defined by

$$
\| L \| _ { X ^ { \vee } } : = \operatorname* { s u p } _ { \stackrel { x \in X } { \| x \| = 1 } } | L ( x ) | = \operatorname* { s u p } _ { \stackrel { x \in X } { \| x \| \leq 1 } } | L ( x ) | .
$$

Definition 1.5.28 (Orthonormal sequence )

A countable collection of elements $\{ u _ { i } \}$ is orthonormal if and only if

1. $\langle u _ { i } , \ u _ { j } \rangle = 0$ for all $j \neq k$ and

2. $\left\| u _ { j } \right\| ^ { 2 } : = \langle u _ { j } , \ u _ { j } \rangle = 1$ for all $j .$

Definition 1.5.29 (Basis of a Hilbert space)

A set $\{ u _ { n } \}$ is a basis for a Hilbert space H iff it is dense in H.

Definition 1.5.30 (Completeness of a Hilbert space)

A collection of vectors $\{ u _ { n } \} \subset H$ is complete iff $\langle x , \ u _ { n } \rangle = 0$ for all $n \iff x = 0$ in H .

Definition 1.5.31 (Dual of a Hilbert space)

The dual of a Hilbert space H is defined as

$$
\begin{array} { r } { H ^ { \vee } : = \{ L : H  \mathbb { C } \ \middle \vert \ L \ \mathrm { i s \ c o n t i n u o u s } \ \} . } \end{array}
$$

Definition 1.5.32 (Linear functionals)

A map $L : X  \mathbb { C }$ is a linear functional iff

$$
L ( \alpha \mathbf { x } + \mathbf { y } ) = \alpha L ( \mathbf { x } ) + L ( \mathbf { y } ) . .
$$

Definition 1.5.33 (Banach Space)

A space is a Banach space if and only if it is a complete normed vector space.

## Definition 1.5.34 (Hilbert Space)

A Hilbert space is an inner product space which is a Banach space under the induced norm.

## 1.6 Theorems

## Theorem 1.6.1(Folland 0.25).

For $E \subseteq ( X , d )$ a metric space, TFAE:

• E is complete and totally bounded.

• E is sequentially compact: Every sequence in E has a subsequence that converges to a point in $E .$

• E is compact: every open cover has a finite subcover.

Note that E is complete as a metric space with the induced metric iff E is closed in $X ,$ and E is bounded iff it is totally bounded.

## Theorem 1.6.2(Mean Value Theorem).

If $f : [ a , b ]$ → R is continuous on a closed interval and differentiable on $( a , b )$ , then there exists $\xi \in [ a , b ]$ such that

$$
f ( b ) - f ( a ) = f ^ { \prime } ( \xi ) ( b - a ) .
$$

## Theorem 1.6.3(Lagrange and Cauchy Remainders).

If f is n times differentiable on a neighborhood of a point p, say $N _ { \delta } ( p )$ , then for all points x in the deleted neighborhood $N _ { \delta } ( p ) - \{ p \}$ , there exists a point ξ strictly between x and $p$ such that

$$
x \in N _ { \delta } ( p ) - \{ p \} \implies f ( x ) = \sum _ { k = 0 } ^ { n - 1 } \frac { f ^ { ( k ) } ( p ) } { k ! } ( x - p ) ^ { k } + \frac { f ^ { ( n ) } ( \xi ) } { n ! } ( x - p ) ^ { n }
$$

$$
= \sum _ { k = 0 } ^ { n - 1 } { \frac { f ^ { ( k ) } ( p ) } { k ! } } ( x - p ) ^ { k } + \int _ { c } ^ { x } { \frac { 1 } { n ! } } { \frac { \partial ^ { n } f } { \partial x ^ { n } } } ( t ) ( x - t ) ^ { n } \ d t
$$

## Proposition 1.6.4(Sufficient condition for Taylor convergence).

Given a point c and some $\varepsilon > 0$ , if $f \in C ^ { \infty } ( I )$ and there exists an M such that

$$
x \in N _ { \varepsilon } ( c ) \implies \left| f ^ { ( n ) } ( x ) \right| \leq M ^ { n }
$$

then the Taylor expansion about c converges on $N _ { \varepsilon } ( c )$

## 1.6.1 Topology / Sets

Theorem 1.6.5(Heine-Cantor).

Every continuous function $f : X \to Y$ where X is a compact metric space is uniformly continuous.

Proof (?).

Fix $\varepsilon > 0$ , we’ll find a δ that works for all $x \in X$ uniformly. For every $x \in X$ , pick a $\delta _ { x }$ neighborhood satisfying the conditions for (assumed) continuity. Take an open cover by $\delta _ { x } / 2$ balls, extract a finite subcover, take δ the minimal radius.

Proposition 1.6.6(Compact if and only if sequentially compact for metric spaces). Metric spaces are compact iff they are sequentially compact, (i.e. every sequence has a convergent subsequence).

Proof (?).

Todo.

Proof.

Proposition 1.6.7(A unit ball that is not compact).

The unit ball in $C ( [ 0 , 1 ] )$ with the sup norm is not compact.

Proof (?).

Take $f _ { k } ( x ) = x ^ { n }$ , which converges to $\chi ( x = 1 )$ . The limit is not continuous, so no subsequence can converge.

Theorem 1.6.8(Heine-Borel).

$X \subseteq \mathbb { R } ^ { n }$ is compact ⇐⇒ X is closed and bounded.

Proposition 1.6.9(Geometric Series).

$$
\sum _ { k = 0 } ^ { \infty } x ^ { k } = { \frac { 1 } { 1 - x } } \iff | x | < 1 .
$$

Corollary 1.6.10(?).

$$
\sum _ { k = 0 } ^ { \infty } { \frac { 1 } { 2 ^ { k } } } = 1 .
$$

Proposition 1.6.11(?).   
The Cantor set is closed with empty interior.

Proof (?).

Its complement is a union of open intervals, and can’t contain an interval since intervals have positive measure and $m ( C _ { n } )$ tends to zero.

Corollary 1.6.12(?).   
The Cantor set is nowhere dense.

Singleton sets in R are closed, and thus Q is an $F _ { \sigma }$ set.

R is a Baire space Thus R can not be written as a countable union of nowhere dense sets.

Any nonempty set which is bounded from above (resp. below) has a well-defined supremum (resp. infimum).

## 1.6.2 Functions

Proposition 1.6.16(Existence of Smooth Compactly Supported Functions). There exist smooth compactly supported functions, e.g. take

$$
f ( x ) = e ^ { - { \frac { 1 } { x ^ { 2 } } } } \chi _ { ( 0 , \infty ) } ( x ) .
$$

Lemma 1.6.17(Function discontinuous on the rationals).   
There is a function discontinuous precisely on Q. Proof (?).   
$f ( x ) = { \frac { 1 } { n } } { \mathrm { ~ i f ~ } } x = r _ { n } \in \mathbb { Q }$ is an enumeration of the rationals, and zero otherwise. The limit at every point is 0.

Proposition 1.6.18(No functions discontinuous on the irrationals). There do not exist functions that are discontinuous precisely on $\mathbb { R } \setminus \mathbb { Q }$

$D _ { f }$ is always an $F _ { \sigma }$ set, which follows by considering the oscillation $\omega _ { f }$ Use that $\omega _ { f } ( x ) = $ $0 \iff f$ is continuous at x, and $D _ { f } = \cup _ { n } A _ { \frac { 1 } { n } }$ where $A _ { \varepsilon } = \{ \omega _ { f } \geq \varepsilon \}$ is closed.

Proposition 1.6.19(Lipschitz ⇐⇒ differentiable with bounded derivative.). A function $f : ( a , b ) $ R is Lipschitz ⇐⇒ f is differentiable and $f ^ { \prime }$ is bounded. In this case, $\left| f ^ { \prime } ( x ) \right| \leq C ,$ , the Lipschitz constant.

## 1.6.3 Sequences and Series

Proposition 1.6.20(The Cauchy condensation test). For $\{ a _ { k } \}$ is a non-increasing sequence in R then

$$
\sum _ { k \geq 1 } a _ { k } < \infty \Longleftrightarrow \sum _ { k \geq 1 } 2 ^ { k } a _ { 2 ^ { k } } < \infty .
$$

Proof (showing a useful trick). Show that

$$
\sum a _ { k } \le \sum 2 ^ { k } a _ { 2 ^ { k } } \le 2 \sum a _ { k }
$$

using

$$
\sum a _ { k } = a _ { 0 } + a _ { 1 } + a _ { 2 } + a _ { 3 } + \cdots \leq ( a _ { 1 } ) + ( a _ { 2 } + a _ { 2 } ) + ( a _ { 3 } + a _ { 3 } + a _ { 3 } + a _ { 3 } ) + \cdots .
$$

where each group with $a _ { k }$ has $2 ^ { k }$ terms.

## 1.7 Uniform Convergence

Proposition 1.7.1(Testing Uniform Convergence: The Sup Norm Test). $f _ { n }  f$ uniformly iff there exists an $M _ { n }$ such that $\left\| { f _ { n } - f } \right\| _ { \infty } \leq M _ { n } \to 0 .$

Remark 1.7.2(Negating the Sup Norm test): Negating: find an x which depends on n for which $\| f _ { n } \| _ { \infty } > \varepsilon$ (negating small tails) or $\| f _ { n } - f _ { m } \| > \varepsilon$ (negating the Cauchy criterion).

Proposition 1.7.3(C(I) is complete).   
The space $X = C ( [ 0 , 1 ] )$ , continuous functions $f : [ 0 , 1 ] \to \mathbb { R }$ , equipped with the norm   
kfk∞ := sup |f(x)|   
x∈[0,1]   
is a complete metric space.

Proof .

1. Let $\{ f _ { k } \}$ be Cauchy in $X .$

2. Define a candidate limit using pointwise convergence:

Fix an x; since

$$
| f _ { k } ( x ) - f _ { j } ( x ) | \leq \| f _ { k } - f _ { k } \| \to 0
$$

the sequence $\{ f _ { k } ( x ) \}$ is Cauchy in R. So define $f ( x ) : = \operatorname* { l i m } _ { k } f _ { k } ( x )$

3. Show that $\| f _ { k } - f \| \to 0 ;$

$$
| f _ { k } ( x ) - f _ { j } ( x ) | < \varepsilon \forall x \implies \operatorname* { l i m } _ { j } | f _ { k } ( x ) - f _ { j } ( x ) | < \varepsilon \forall x
$$

Alternatively, $\| f _ { k } - f \| \leq \| f _ { k } - f _ { N } \| + \| f _ { N } - f _ { j } \|$ , where $N , j$ can be chosen large enough to bound each term by $\varepsilon / 2$

4. Show that $f \in X \colon$

The uniform limit of continuous functions is continuous.

Remark 1.7.4: In other cases, you may need to show the limit is bounded, or has bounded derivative, or whatever other conditions define X.

## 1.7.1 Series

Proposition 1.7.5 $\scriptstyle ( p - t e s t s )$

Let n be a fixed dimension and set $B = \left\{ x \in \mathbb { R } ^ { n } \Big | \ \| x \| \leq 1 \right\}$

$$
\sum { \frac { 1 } { n ^ { p } } } < \infty \Longleftrightarrow p > 1
$$

$$
\int _ { \varepsilon } ^ { \infty } { \frac { 1 } { x ^ { p } } } < \infty \Longleftrightarrow p > 1
$$

$$
\int _ { 0 } ^ { 1 } { \frac { 1 } { x ^ { p } } } < \infty \Longleftrightarrow p < 1
$$

$$
\int _ { B } { \frac { 1 } { | x | ^ { p } } } < \infty \Longleftrightarrow p < n
$$

$$
\int _ { B ^ { c } } { \frac { 1 } { | x | ^ { p } } } < \infty \Longleftrightarrow p > n
$$

Proposition 1.7.6(Comparison Test).

If $0 \leq a _ { n } \leq b _ { n }$ , then

$\sum b _ { n } < \infty \implies \sum a _ { n } < \infty ,$ and

$\sum a _ { n } = \infty \implies \sum b _ { n } = \infty .$

Proposition 1.7.7(Small Tails for Series of Functions).

$\operatorname { I f } \sum f _ { n }$ converges then $f _ { n } \to 0$ uniformly.

Corollary 1.7.8(Term by Term Continuity Theorem).   
If $f _ { n }$ are continuous and $\sum f _ { n } \to f$ converges uniformly, then $f$ is continuous.

Proposition 1.7.9(Cauchy criterion for sums).

$f _ { n }$ are uniformly Cauchy (so $\| f _ { n } - f _ { m } \| _ { \infty } < \varepsilon )$ iff $f _ { n }$ is uniformly convergent.

## Derivatives

Theorem 1.7.10(Term by Term Differentiability Theorem). If $f _ { n }$ are differentiable, $\sum f _ { n } ^ { \prime } \to g$ uniformly, and there exists one pointa x0 such that $\sum f _ { n } ( x )$ converges, then there exist an $f$ such that $\sum f _ { n } \to f$ uniformly and $f ^ { \prime } = g . ^ { \mathit { b } }$

<!-- image-->

## 1.8 Commuting Limiting Operations

<!-- image-->

Proposition 1.8.1(Limits of bounded functions need not be bounded).

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { x \in X } | f _ { n } ( x ) | \neq \operatorname* { s u p } _ { x \in X } \Big | \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x ) \Big | .
$$

Proposition 1.8.2(Limits of continuous functions need not be continuous).

$$
\operatorname* { l i m } _ { k \to \infty } \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x _ { k } ) \neq \operatorname* { l i m } _ { n \to \infty } \operatorname* { l i m } _ { k \to \infty } f _ { n } ( x _ { k } ) .
$$

Proposition 1.8.3(Limits of differentiable functions need not be differentiable).

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { \partial } { \partial x } } f _ { n } \neq { \frac { \partial } { \partial n } } \left( \operatorname* { l i m } _ { n \to \infty } f _ { n } \right) .
$$

Note that uniform convergence of $f _ { n }$ and $f _ { n } ^ { \prime }$ is sufficient to guarantee that f is differentiable.

Even worse: every continuous function is a uniform limit of polynomials by the Weierstrass approximation theorem.

Example 1.8.4(?): As a counterexample:

$$
f _ { n } ( x ) : = { \sqrt { x ^ { 2 } + { \frac { 1 } { n } } } } \ { \overset { n \to \infty } { \longrightarrow } } \ f ( x ) : = | x | ,
$$

and this convergence is even uniform.

Example 1.8.5(?):

$$
f _ { n } ( x ) : = { \frac { x } { 1 + n x ^ { 2 } } } .
$$

Then by Calculus, $f _ { n } ( x ) \leq 1 / 2 { \sqrt { n } } : = M _ { n }$ and $f _ { n } \to 0$ uniformly, so $f ^ { \prime } = 0$ . But

$$
f _ { n } ^ { \prime } ( x ) = { \frac { 1 - n x ^ { 2 } } { \left( 1 + n x ^ { 2 } \right) ^ { 2 } } } ,
$$

and $f _ { n } ^ { \prime } ( 0 ) \to 1$

Proposition 1.8.6(?).

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { a } ^ { b } f _ { n } ( x ) d x \neq \int _ { a } ^ { b } \operatorname* { l i m } _ { n \to \infty } \left( f _ { n } ( x ) \right) d x .
$$

## 1.9 Probabilist Tools: “Almost” Theorems

## Theorem 1.9.1(Egorov’s Theorem).

Let $E \subseteq \mathbb { R } ^ { d }$ be measurable of positive finite measure with $f _ { k }  f$ almost everywhere on E. Then for every $\varepsilon > 0$ there is a closed $A _ { \varepsilon } \subseteq E$ with $\mu ( E \setminus A _ { \varepsilon } ) < \varepsilon$ and $f _ { k }  f$ uniformly on $A _ { \varepsilon }$

Proof (of Egorov).

Proof. We may assume without loss of generality that $f _ { k } ( x )  f ( x )$ for every $x \in E$ . For each pair of non-negative integers n and k, let

$$
E _ { k } ^ { n } = \{ x \in E : | f _ { j } ( x ) - f ( x ) | < 1 / n , { \mathrm { ~ f o r ~ a l l ~ } } j > k \} .
$$

Now fix n and note that $E _ { k } ^ { n } \subset E _ { k + 1 } ^ { n }$ , and $E _ { k } ^ { n } \nearrow E$ as k tends to infinity. By Corollary 3.3, we find that there exists $k _ { n }$ such that $m ( E - E _ { k _ { n } } ^ { n } ) <$ $1 / 2 ^ { n }$ . By construction, we then have

$| f _ { j } ( x ) - f ( x ) | < 1 / n$ whenever $j > k _ { n }$ and $x \in E _ { k _ { n } } ^ { n }$

We choose N so that $\textstyle \sum _ { n = N } ^ { \infty } 2 ^ { - n } < \epsilon / 2$ , and let

$$
\tilde { A } _ { \epsilon } = \bigcap _ { n \geq N } E _ { k _ { n } } ^ { n } .
$$

We first observe that

$$
m ( E - \tilde { A } _ { \epsilon } ) \leq \sum _ { n = N } ^ { \infty } m ( E - E _ { k _ { n } } ^ { n } ) < \epsilon / 2 .
$$

Next, if $\delta > 0 .$ ,we choose $n \geq N$ such that $1 / n < \delta ,$ and note that $x \in$ $\tilde { A } _ { \epsilon }$ implies $x \in E _ { k _ { n } } ^ { n }$ . We see therefore that $| f _ { j } ( x ) - f ( x ) | < \delta$ whenever $j > k _ { n }$ . Hence $f _ { k }$ converges uniformly to f on $\tilde { A } _ { \epsilon }$

Finally, using Theorem 3.4 choose a closed subset $A _ { \epsilon } \subset \tilde { A } _ { \epsilon }$ with $m ( \tilde { A } _ { \epsilon } -$ $A _ { \epsilon } ) < \epsilon / 2$ As a result, we have $m ( E - A _ { \epsilon } ) < \epsilon$ and the theorem is proved.

## Theorem 1.9.2(Lusin’s Theorem).

If f is measurable and finite-valued on $E$ with $\mu ( E ) < \infty$ then for every $\varepsilon > 0$ there exists a closed set $F _ { \varepsilon }$ with

$$
F _ { \varepsilon } \subset F
$$

$$
\mu ( E - F _ { \varepsilon } ) \leq \varepsilon
$$

where $f$ restricted to $F _ { \varepsilon }$ is continuous.

Note: this means that the separate function $\tilde { f } : =$ $f \vert _ { F _ { \varepsilon } }$ is continuous, not that the function f defined on all of E is continuous at points of $F _ { \varepsilon }$

Proof (of Lusin).

Proof. Let $f _ { n }$ be a sequence of step functions so that $f _ { n }  f$ a.e. Then we may find sets $E _ { n }$ so that $m ( E _ { n } ) < 1 / 2 ^ { n }$ and $f _ { n }$ is continuous outside $E _ { n }$ . By Egorov's theorem, we may find a set $A _ { \epsilon / 3 }$ on which $f _ { n }  f$ uniformly and $m ( E - A _ { \epsilon / 3 } ) \leq \epsilon / 3$ . Then we consider

$$
F ^ { \prime } = A _ { \epsilon / 3 } - \bigcup _ { n \geq N } E _ { n }
$$

for N so large that $\textstyle \sum _ { n > N } 1 / 2 ^ { n } < \epsilon / 3$ . Now for every $n \geq N$ the function $f _ { n }$ is continuous on $F ^ { \prime } { ; }$ thus $f$ (being the uniform limit of $\left\{ f _ { n } \right\} )$ is also continuous on $F ^ { \prime }$ . To finish the proof, we merely need to approximate the set $F ^ { \prime }$ by a closed set $F _ { \epsilon } \subset F ^ { \prime }$ such that $m ( F ^ { \prime } - F _ { \epsilon } ) < \epsilon / 3$

## 1.10 Slightly Advanced Stuff

Theorem 1.10.1(Weierstrass Approximation).

If $[ a , b ] \subset \mathbb { R }$ is a closed interval and f is continuous, then for every $\varepsilon > 0$ there exists a polynomial $p _ { \varepsilon }$ such that $\| f - p _ { \varepsilon } \| _ { L ^ { \infty } ( [ a , b ] ) } \stackrel { \varepsilon \to 0 } { \longrightarrow } 0 .$ Equivalently, polynomials are dense in the Banach space $C ( [ 0 , 1 ] , \| - \| _ { \infty } )$

## 1.11 Examples and Counterexamples

Example 1.11.1(?): A series of continuous functions that does not converge uniformly but is still continuous:

$$
g ( x ) : = \sum \frac { 1 } { 1 + n ^ { 2 } x } .
$$

Take $x = 1 / n ^ { 2 }$

Let all of the following integrals to be over a compact interval $[ a , b ]$ with $0 \leq a < b .$

Questions to ask:

• Where is/isn’t f continuous?

• Where is/isn’t f differentiable?

• Is f Riemann integrable?

## 1.11.1 Dirichlet function

$$
f ( x ) = b + ( a - b ) \ \chi ( x \in \mathbb { Q } ) = { \left\{ \begin{array} { l l } { a , } & { x \in \mathbb { Q } } \\ { b , } & { { \mathrm { e l s e } } } \end{array} \right. }
$$

(usually take $a = 1 , b = 0 )$

• Continuous nowhere

• Discontinuous everywhere

• Not integrable

• Differentiable nowhere

## 1.11.2 Dirichlet with a Continuous Point

$$
f ( x ) = x \ \chi ( \mathbb { Q } ) = { \left\{ \begin{array} { l l } { x , } & { x \in \mathbb { Q } } \\ { 0 , } & { { \mathrm { e l s e } } } \end{array} \right. }
$$

• Continuous at 0

• Discontinuous at $\mathbb { R } - \{ 0 \}$

• Not integrable

$$
- \ U ( f ) > { \frac { 1 } { 4 } } \ \mathrm { b u t } \ L ( f ) = 0 .
$$

• Differentiable nowhere

## 1.11.3 Dirichlet with a Differentiable Point

$$
f ( x ) = x ^ { 2 } \ { \chi } ( \mathbb { Q } ) = { \left\{ x ^ { 2 } , \ { \begin{array} { l l } { x \in \mathbb { Q } } \\ { 0 , } \end{array}  } \operatorname { e l s e } }\right.
$$

• Continuous at 0

• Discontinuous at R − {0}

• Not integrable

• Differentiable at 0

## 1.11.4 Dirichlet with Two Functions

$$
f ( x ) = x \ \chi \mathbb { Q } + ( - x ) \chi ( \mathbb { R } - \mathbb { Q } ) = { \left\{ \begin{array} { l l } { x , } & { x \in \mathbb { Q } } \\ { - x , } & { { \mathrm { e l s e } } } \end{array} \right. }
$$

• Continuous at 0

• Discontinuous at $\mathbb { R } - \{ 0 \}$

• Differentiable nowhere.

• Not integrable

Proof (of non-integrability).

Restrict attention to $\left[ \frac { 1 } { 2 } , 1 \right]$

$$
\begin{array} { c } { { \displaystyle \int _ { 0 } ^ { 1 } f = \operatorname* { i n f } \Big \{ \sum \operatorname* { s u p } f ( x ) ( x _ { i } - x _ { i - 1 } ) \Big \} } } \\ { { \operatorname* { s u p } f ( x ) = x _ { i } \implies \sum \operatorname* { s u p } f ( x ) ( x _ { i } - x _ { i - 1 } ) = \sum x _ { i } ( x _ { i } - x _ { i - 1 } ) } } \\ { { > \sum \frac 1 2 ( x _ { i } - x _ { i - 1 } ) } } \\ { { = \displaystyle \frac 1 2 \left( \frac 1 2 \right) = \frac 1 4 } } \\ { { \implies \displaystyle \int _ { 0 } ^ { 1 } f \geq \frac 1 4 } } \end{array}
$$

and

$$
\int _ { 0 } ^ { 1 } f = \operatorname* { s u p } \left\{ \sum { \mathrm { i n f } } f ( x ) ( x _ { i } - x _ { i - 1 } ) \right\}
$$

$$
{ \begin{array} { r l } { \operatorname* { i n f } f ( x ) = - x _ { i } \implies \sum \operatorname* { i n f } f ( x ) ( x _ { i } - x _ { i - 1 } ) = \sum - x _ { i } ( x _ { i } - x _ { i - 1 } ) } \\ & { \qquad < - \sum { \frac { 1 } { 2 } } ( x _ { i } - x _ { i - 1 } ) } \\ & { \qquad = - { \frac { 1 } { 2 } } \left( { \frac { 1 } { 2 } } \right) = - { \frac { 1 } { 4 } } } \\ & { \qquad \implies \int _ { 0 } ^ { 1 } f \leq - { \frac { 1 } { 4 } } } \end{array} }
$$

So we have $\int _ { 0 } ^ { 1 } f \leq 0 \leq { \overline { { \int _ { 0 } ^ { 1 } } } } f .$

## 1.12 The Thomae function:

$$
f ( x ) = \left\{ { \frac { 1 } { q } } , \quad x = { \frac { p } { q } } \in \mathbb { Q } , \ ( p , q ) = 1 \right.
$$

• Continuous on $\mathbb { R } - \mathbb { Q }$

• Discontinuous on Q

• Integrable with $\int _ { a } ^ { b } f = 0$

• Differentiable nowhere

Exercises from Folland:

• Chapter 1: Exercises 3, 7, 10, 12, 14 (with the sets in 3(a) being non-empty) Exercises 15, 17, 18, 19, 22(a), 24, 28 Exercises 26, 30 (also check out 31)

• Chapter 2: Exercises 2, 3, 7, 9 (in 9(c) you can use Exercise 1.29 without proof Exercises 10, 12, 13, 14, 16, 19 Exercises 24, 25, 28(a,b), 33, 34, 35, 38, 41 (note that 24 shows that upper sums are not needed in the definition of integrals, and the extra hypotheses also show that they are not desired either) Exercises 40, 44, 47, 49, 50, 51, 52, 54, 56, 58, 59

• Chapter 3: Exercises 3(b,c), 5, 6, 9, 12, 13, 14, 16, 20, 21, 22

## 2 Measure Theory

Fact 2.0.1

Some useful tricks:

$\mu ( A \setminus B ) = \mu ( A ) - \mu ( B ) { \mathrm { ~ i f ~ } } \mu ( B ) < \infty$

• Write $f = f - f _ { n } + f _ { n }$

• If G is measurable, then there for every ε there exists an open $G \supseteq E$ such $m ( G ) \leq m ( E ) + \varepsilon$

• If E is measurable,

$- \mathbf { \nabla } E = F _ { \delta } [ [ N \mathbf { \nabla }$ for N a null set.

$- \ E [ [ N = G _ { \delta }$ for N a null set.

## 2.1 Abstract Measure Theory

Definition 2.1.1 (Measures on measurable spaces)   
If $( X , M )$ is a measurable space, then a measure is a function $\mu : { \mathcal { M } }  [ 0 , \infty ]$ such that   
$\mu ( \varnothing ) = 0 .$   
2. Countable additivity: if $\{ E _ { k } \} _ { k \ge 1 }$ is a countable union of disjoint sets in $X ,$ then   
$\mu \left( \operatorname { \mathrm { { I I } } } _ { k \geq 1 } E _ { k } \right) = \sum _ { k \geq 1 } \mu ( E _ { k } ) .$   
If (2) only holds for finitely indexed sums, we say $\mu$ is σ-additive.

$$
m ( A ) = m ( B ) + m ( C ) \quad { \mathrm { a n d } } \quad m ( C ) < \infty \implies m ( A ) - m ( C ) = m ( B ) .
$$

$$
( X , { \mathcal { M } } , \mu )
$$

$$
E \subseteq F \implies \mu ( E ) \leq \mu ( F ) .
$$

$$
E _ { k k \geq 1 }
$$

$$
\mu \left( \bigcup _ { k \geq 1 } E _ { k } \right) \leq \sum _ { k \geq 1 } \mu ( E _ { k } ) .
$$

Proposition 2.1.4(Continuity of Measure).

Continuity from below: $E _ { n } \nearrow E \implies m ( E _ { n } ) \stackrel { n \to \infty } { \longrightarrow } m ( E )$   
Continuity from above: $m ( E _ { 1 } ) < \infty$ and $E _ { n } \searrow E \implies m ( E _ { n } ) \stackrel { n \to \infty } { \longrightarrow } m ( E )$   
Mnemonic: lim $\mu ( E _ { n } ) = \mu ( \operatorname* { l i m } E _ { n } )$   
n

Proof (sketches).   
• From below: break into disjoint annuli $A _ { 2 } = E _ { 2 } \setminus E _ { 1 }$   
– Apply countable disjoint additivity to $E = \amalg A _ { i } .$   
• From above: funny step, use $E _ { 1 } = ( \mathrm { I } [ E _ { j } \setminus E _ { j + 1 } ) ] \mathrm { I } ( \cap E _ { j } )$   
– Taking measures yields a telescoping sum, and use countable additivity, then finite  
ness to subtract.

<!-- image-->  
Figure 1: image_2021-05-28-23-29-31

Proof (of continuity of measure from below, detailed).

For any measure $\mu ,$

$$
\mu ( F _ { 1 } ) < \infty , F _ { k } \searrow F \implies \operatorname* { l i m } _ { k \to \infty } \mu ( F _ { k } ) = \mu ( F ) ,
$$

where $F _ { k } \ \searrow F$ means $F _ { 1 } \supseteq F _ { 2 } \supseteq \cdots$ with $\cap _ { k = 1 } ^ { \infty } F _ { k } = F . .$ - Note that $\mu ( F )$ makes sense: each $F _ { k } \in B$ , which is a σ-algebra and closed under countable intersections.

• Take disjoint annuli by setting $E _ { k } : = F _ { k } \setminus F _ { k + 1 }$

• Funny step: write

$$
F _ { 1 } = F \mathrm { I I } \prod _ { k = 1 } ^ { \infty } E _ { k } .
$$

– This is because $x \in F _ { 1 }$ iff x is in every $F _ { k }$ , so in $F _ { ; }$ , or

$x \notin F _ { 1 }$ but $x \in F _ { 2 }$ , noting incidentally $x \in F _ { 3 } , F _ { 4 } , \cdot \cdot \cdot , \mathbf { o r }$

$- \ x \notin F _ { 2 }$ but $x \in F _ { 3 }$ and thus $F _ { 4 } , F _ { 4 } , \cdots$ , and so on.

• Now take measures, and note that we get a telescoping sum:

$$
 \begin{array} { r l } & { \| A ( F _ { i } ) - \mu ( F ) + \sum _ { j = 1 } ^ { \infty } \mu ( E _ { k } ) \| } \\ & { \qquad \leq \operatorname* { i n f } ( F _ { i } ) + \ \sum _ { k = 1 } ^ { \infty } \mu ( E _ { k } ) } \\ & { \qquad - \mu ( F ^ { 0 } ) + \underbrace { { \frac { 1 } { \sqrt { 3 } } } \mu ( E _ { k } ) } _ { \mathrm { K \setminus { S } \setminus \infty } } \ } \\ & { \qquad = \mu ( F ) + \ \underbrace { { \frac { 1 } { \sqrt { 3 } } } \mu ( E _ { k } ) } _ { \mathrm { K \setminus { S } \setminus \infty } } \ \sum _ { j = 1 } ^ { \infty } ( F ( E _ { k } ) \ \xi _ { j + 1 } ) } \\ & { \qquad = \mu ( F ) + \ \underbrace { { \frac { 1 } { \sqrt { 3 } } } \mu ( E _ { k } ) } _ { \mathrm { K \setminus { S } \setminus \infty } } \ \sum _ { j = 1 } ^ { \infty } ( F ( E _ { k } ) \ \xi _ { j } ) \qquad \qquad { \mathrm { t o b s i n t i t i c d } } } \\ & { \qquad \leq \mu ( F ) + \ \underbrace { { \frac { 1 } { \sqrt { 3 } } } \mu ( E _ { k } ) } _ { \mathrm { K \setminus { S } \setminus \infty } } \ \sum _ { j = 1 } ^ { \infty } ( F ( E _ { k } ) \ \xi _ { j } ) \qquad \mathrm { t r o b \ c i p t i t i c d } } \\ & { \qquad \leq \mu ( F ) + \ \underbrace { { \frac { 1 } { \sqrt { 3 } } } \mu ( E _ { k } ) } _ { \mathrm { K \setminus { S } \setminus \infty } } \ ( \mu ( F ) ) - \ \left. ( F ) \right\} + \ \mu ( F ) \ \xi _ { j } ) \ \qquad \cdots \qquad } \\ & { \qquad + \ \left( \mu ( F ) - \mu ( F ) \right) - \ \mu ( F ) \xi _ { j } ) \ \left( \dot { \mu } ( E _ { k } ) \right) - \ \mu ( F ) \xi _ { j } ) \qquad \mathrm { t a r } \ \left\| ( E _ { k } ) \right\| } \\ &  \qquad = \mu ( F ) + \ \sum _  k = 1 \end{array}
$$

• Justifying the measure subtraction: the general statement is that for any pair of sets $A \subseteq X , \mu ( X \setminus A ) = \mu ( X ) - \mu ( A )$ when $\mu ( A ) < \infty { : }$

$$
{ \begin{array} { r l r l } & { X = A [ \mathrm { I } ( X \setminus A ) } \\ & { \implies \mu ( X ) = \mu ( A ) + \mu ( X \setminus A ) } \\ & { \implies \mu ( X ) - \mu ( A ) = \mu ( X \setminus A ) } & & { \qquad { \mathrm { i f ~ } } \mu ( A ) < \infty . } \end{array} }
$$

• Now use that $\mu ( F _ { 1 } ) < \infty$ to justify subtracting it from both sides:

$$
\begin{array} { c } { { \displaystyle \mu ( F _ { 1 } ) = \mu ( F ) + \mu ( F _ { 1 } ) - \operatorname * { l i m } _ { N \to \infty } \mu ( F _ { N + 1 } ) } } \\ { { \displaystyle \Longrightarrow ~ 0 = \mu ( F _ { 1 } ) - \operatorname * { l i m } _ { N \to \infty } \mu ( F _ { N + 1 } ) } } \\ { { \displaystyle \operatorname * { l i m } _ { N \to \infty } \mu ( F _ { N + 1 } ) = \mu ( F _ { 1 } ) . } } \end{array}
$$

• Now use that $\operatorname* { l i m } _ { N \to \infty } \mu ( F _ { N + 1 } ) = \operatorname* { l i m } _ { N \to \infty } \mu ( F _ { N } )$ to conclude.

## 2.2 Outer Measure

Proposition 2.2.1(Properties of Outer Measure).   
1. Monotonicity: $E \subseteq F \implies m _ { * } ( E ) \leq m _ { * } ( F ) .$   
2. Countable Subadditivity: $m _ { * } ( \cup E _ { i } ) \leq \sum m _ { * } ( E _ { i } )$   
3. Approximation: For all E there exists a $\mathbf { \Delta } _ { \left| G \supseteq E \right. }$ such that $m _ { * } ( G ) \leq m _ { * } ( E ) + \varepsilon .$   
4. Disjointa Additivity: $m _ { * } ( A [ \operatorname { I } ^ { B } ) = m _ { * } ( A ) + m _ { * } ( B ) .$   
aThis holds for outer measure iff dis $( A , B ) > 0 .$   
Definition 2.2.2 (Lebesgue Measurability)   
A set E is measurable iff it can be approximated by an open set in $m _ { * } .$ , so there exists $G \supseteq E$   
with $m _ { * } ( G \backslash E ) < \varepsilon .$

<!-- image-->

## 2.3 Measures on Rd

Proposition 2.3.1(Opens are unions of almost disjoint intervals.).   
Every open subset of R (resp Rn) can be written as a unique countable union of disjoint (resp.   
almost disjoint) intervals (resp. cubes).

```latex
Proof (of translation/dilation invariance).
• This is obvious for cubes:
– For translation, if $Q _ { i }  E$ then $Q _ { i } + k \Longrightarrow E + k$ One can then show $m _ { * } ( E + k ) \leq$
$\sum | Q _ { i } + k | = \sum | Q _ { i } | \leq m _ { * } ( E ) + \varepsilon$ for all ε, and get the reverse inequality by
writing $E = ( E { \overline { { + } } } y ) - y .$
– For dilation, use that m∗ $\operatorname { \rho } _ { : } ( t ( A \operatorname { I } \operatorname { I } B ) ) = t m _ { * } ( A \operatorname { I } \operatorname { I } B )$ , which is useful because we cover
with disjoint cubes. Then use that $t Q _ { i } \stackrel { } { \longrightarrow } t E$ to get tm∗ $\quad ( E ) \leq t \sum | Q _ { i } | = \sum | t Q _ { i } | \leq$
m∗(tE) + ε and similarly reverse to get equality.
```

## Theorem 2.3.3(Non-measurable sets exist).

$$
{ \mathit { A } } \subseteq \mathbb { R } .
$$

Proof (Constructing a non-measurable set).   
• Use AOC to choose one representative from every coset of $\mathbb { R } / \mathbb { Q }$ on [0, 1), which is

countable, and assemble them into a set $N$   
Enumerate the rationals in $[ 0 , 1 ]$ as $q _ { j }$ , and define $N _ { j } = N + q _ { j }$ . These intersect trivially.   
• Define $M : = \coprod N _ { j }$ , then $[ 0 , 1 ) \subseteq M \subseteq [ - 1 , 2 )$ , so the measure must be between 1 and 3.   
By translation invariance, $m ( N _ { j } ) = m ( N )$ , and disjoint additivity forces $m ( M ) = 0 $ , a   
contradiction.

Proposition 2.3.4(Limsups/infs of measurable sets are measurable.).   
If $A _ { n }$ are all measurable, lim sup $A _ { n }$ and lim inf $A _ { n }$ are measurable.

Proof (That limsups/infs are measurable).   
Measurable sets form a sigma algebra, and these are expressed as countable unions/intersections   
of measurable sets.

Theorem 2.3.5(Borel-Cantelli).   
Let $\{ E _ { k } \}$ be a countable collection of measurable sets. Then   
$\sum _ { k } m ( E _ { k } ) < \infty \implies$ almost every $x \in \mathbb { R }$ is in at most finitely many $E _ { k }$

Proof (of Borel-Cantelli).   
• If $E =$ lim sup $E _ { j }$ with $\sum m ( E _ { j } ) <$ ∞ then $m ( E ) = 0 .$   
j   
• If $E _ { j }$ are measurable, then lim sup $E _ { j }$ is measurable.   
j   
$\mathrm { I f } \sum m ( E _ { j } ) < \infty .$ , then $\sum ^ { \infty } m ( E _ { j } ) \stackrel { N  \infty } {  } 0$ as the tail of a convergent sequence.   
$\overline { { j = N } }$   
• E = lim sup $E _ { j } = \cap _ { k = 1 } ^ { \infty } \bigcup _ { j = k } ^ { \infty } E _ { j } \implies E \subseteq \cup _ { j = k } ^ { \infty }$ for all k   
$E \subset \cup _ { j = k } ^ { \infty } \implies m ( E ) \leq \sum _ { j = k } ^ { \infty } m ( E _ { j } ) \stackrel { k \to \infty } {  } 0 .$

Proposition 2.3.6(Extending the class of measurable functions.).   
Characteristic functions are measurable   
• If $f _ { n }$ are measurable, so are $\left| f _ { n } \right|$ , lim sup $f _ { n }$ , lim inf $f _ { n }$ , lim $f _ { n } .$   
• Sums and differences of measurable functions are measurable,   
• Cones $F ( x , y ) = f ( x )$ are measurable,   
• Compositions $f \circ T$ for T a linear transformation are measurable,   
• “Convolution-ish” transformations $( x , y ) \mapsto f ( x - y )$ are measurable

$$
F ( x , y ) = f ( x )
$$

T = [1, −1; 1, 0].

A measure space $( X , { \mathcal { M } } , \mu )$ is σ-finite if X can be written as a union of countably many measurable sets with finite measure.

```perl
Proposition 2.3.8(Regularity of measure).
If $( X , B , \mu )$ is a Borel measure space where $\mu$ is finite on all balls of finite radius, then for any
$E \in B$ and any $\varepsilon > 0$
```

• There exists an open set O with $E \subset O$ and $\mu ( O \setminus E ) < \varepsilon$

• There exists a closed set F with $F \subset E$ and $\mu ( E \setminus F ) < \varepsilon$

Show that E is measurable iff E is regular in either sense above.

<!-- image-->

## 2.4 Exercises

```perl
Problem 2.4.1 (?)
Show that if $\sum \mu ( E _ { k } ) < \infty$ then almost every $x \in X$ is in at most finitely many $E _ { k } .$
```

## 3 Integration

## 3.1 Unsorted

Definition 3.1.1 (Measurable Function)   
A function $f : ( X , { \mathcal { M } } _ { X } ) \to ( Y , { \mathcal { M } } _ { Y } )$ is $( \mathcal { M } _ { X } , \mathcal { M } _ { Y } )$ -measurable iff $f ^ { - 1 } ( { \mathcal { M } } _ { Y } ) \subseteq { \mathcal { M } } _ { X }$ Equiva  
lently, if EY is a generating set for $B _ { Y } , f ^ { - 1 } ( { \mathcal { E } } _ { Y } ) \subseteq B _ { X }$   
• An functional on a general measurable space $f : f : ( X , { \mathcal { M } } _ { X } ) \to ( \mathbb { R } , { \mathcal { B } } _ { \mathbb { R } } )$ is measurable   
$\iff f$ is $\left( \mathcal { M } _ { X } , \boldsymbol { B } _ { \mathbb { R } } \right)$ -measurable.   
• A functional $f : \mathbb { R } ^ { d } $ R is Borel measurable iff f is $( \boldsymbol { B } _ { \mathbb { R } ^ { d } } , \boldsymbol { B } _ { \mathbb { R } } )$ -measurable.   
• A functional $f : \mathbb { R } ^ { d }  \mathbb { R }$ is Lebesgue measurable iff f is $( \mathcal { L } _ { \mathbb { R } ^ { d } } , B _ { \mathbb { R } } )$ -measurable.   
Using that $\boldsymbol { B _ { \mathbb { R } } }$ is generated by open/closed rays, it suffices to check any of the following (for   
all $\alpha \in \mathbb { R } )$   
$f ^ { - 1 } ( \alpha , \infty ) \in \mathcal { M }$

• $f ^ { - 1 } [ \alpha , \infty ) \in \mathcal { M }$

• $f ^ { - 1 } ( - \infty , \alpha ) \in \mathcal { M }$

$f ^ { - 1 } ( - \infty , \alpha ] \in \mathcal { M }$

Remark 3.1.2: Note that we still require Borel sets in the target for Lebesgue measurability! Taking $( \mathcal { L } _ { \mathbb { R } ^ { d } } , \mathcal { L } _ { \mathbb { R } } )$ functions is too stringent, e.g. this class does not contain continuous functionals.

## 4! Warning 3.1.3

If f is L-measurable and h is continuous, it’s not necessarily true that $k : = f \circ h$ is L-measurable. Standard counterexample: set $g ( x ) : = C ( x ) + x$ for C the Cantor-Lebesgue function, then $_ { \textit { g } : }$ $[ 0 , 1 ]  [ 0 , 2 ]$ is a homeomorphism. Then $m ( g ( C ) ) = 1$ since f is constant on intervals in $C ^ { c }$ , so use Vitali’s theorem: a set is null iff every subset is measurable. So $g ( C )$ contains a non-measurable set A. Define $B : = g ^ { - 1 } ( A )$ , then $B \subset C$ and $m ( C ) = 0$ implies B is measurable and $\chi _ { B }$ is a measurable function. But then $k : = \chi _ { B } \circ g ^ { - 1 }$ is not L-measurable, since $k ^ { - 1 } ( 1 ) = A$ is a non-measurable set, but $\chi _ { B }$ is L-measurable and $g ^ { - 1 }$ is continuous.

Proposition 3.1.4(Closure of measurable functions under operations).   
M-measurable functionals are closed under   
• Sums   
• Products   
• Sups/infs   
• Limsups/Liminfs   
• Limits when they exist, and the limiting function is measurable.   
• max $( f , g )$ and min(f, g).   
Characteristic functions on measurable sets are automatically measurable, since $E \in \mathcal { M } \implies$   
$E = \chi _ { E } ^ { - 1 } ( \{ 1 \} )$

## Remark 3.1.5(A common proof technique):

• Show something holds for indicator functions.

• Show it holds for simple functions by linearity.

• Use $s _ { k } \nearrow f$ and apply MCT to show it holds for $f .$

Remark 3.1.6(on notation):

$L ^ { + } ;$ : nonnegative measurable functions

$L ^ { 1 }$ : Lebesgue integrable functions, so $\int | f | < \infty$

Definition 3.1.7 (Simple Function)

A simple function $s : \mathbb { C } \to X$ is a finite linear combination of indicator functions of measurable sets, i.e.

$$
s ( x ) = \sum _ { j = 1 } ^ { n } c _ { j } \chi _ { E _ { j } } ( x ) .
$$

Definition 3.1.8 (Lebesgue Integral)

$$
\int _ { X } f : = \operatorname* { s u p } \left\{ \int s ( x ) d \mu { \Big | } 0 \leq s \leq f , s \operatorname { s i m p l e } \right\} .
$$

Note that if $s = \sum c _ { j } \chi _ { E _ { j } }$ is simple, then

$$
\int _ { X } s ( x ) d \mu : = \sum _ { j = 1 } ^ { n } c _ { j } \mu ( E _ { j } ) .
$$

Remark 3.1.9(Integrals split across disjoint sets): A useful fact: for $( X , M )$ a measure space, integrals split across disjoint sets:

$$
\int _ { X } f = \int _ { X \backslash A } f + \int _ { A } f
$$

$$
\forall A \in { \mathcal { M } } .
$$

Definition 3.1.10 (Essential supremum and infimum, essentially bounded)

$$
f
$$

$$
\left\{ x \mid f ( x ) < b \right\} = f ^ { - 1 } ( - \infty , b )
$$

$$
S _ { b } \quad : = \quad
$$

$$
f : = \operatorname* { s u p } _ { b } \left\{ b \ : \left| \ : \mu S _ { b } = 0 \right. \right\}
$$

Similarly an essential upper bound c is any number such that $S ^ { c } : = f ^ { - 1 } ( c , \infty )$ has measure zero, and the essential supremum is ess sup $f : = \operatorname* { i n f } _ { c } \left\{ c \Bigm \vert \mu S ^ { c } = 0 \right\}$ , which is the least upper bound almost everywhere.

A function is essentially bounded if $\| f \| _ { \infty } : = \operatorname { e s s s } \operatorname* { s u p } f < \infty$ These are functions which are bounded almost everywhere.

Example 3.1.11(An essentially bounded but not bounded function): $f ( x ) = x \chi _ { \mathbb { Q } } ( x )$ essentially bounded but not bounded.

Proposition 3.1.12 $( L ^ { \infty }$ functions are equivalent to bounded almost-everywhere functions). If $f \in L ^ { \infty } ( X )$ , then f is equal to some bounded function g almost everywhere.

Theorem 3.1.13(p-Test for Integrals).

$$
\int _ { 0 } ^ { 1 } { \frac { 1 } { x ^ { p } } } < \infty \Longleftrightarrow p < 1
$$

$$
\int _ { 1 } ^ { \infty } { \frac { 1 } { x ^ { p } } } < \infty \Longleftrightarrow p > 1 .
$$

Slogan 3.1.14

Large powers of x help us in neighborhoods of infinity and hurt around zero.

Theorem 3.1.15(Monotone Convergence).

If $f _ { n } : X \to [ 0 , \infty ) \in L ^ { + }$ and $f _ { n } \nearrow f$ almost everywhere, then

$$
\operatorname* { l i m } \int f _ { n } = \int \operatorname* { l i m } f _ { n } = \int f \quad { \mathrm { i . e . ~ } } \int f _ { n }  \int f .
$$

## Slogan 3.1.16

Measurable, non-negative, increasing pointwise a.e. allows commuting limits and integrals.

Proof (of MCT).

todo

## Theorem 3.1.17(Dominated Convergence).

If $f _ { n } \in L ^ { 1 }$ and $f _ { n }  f$ almost everywhere with $| f _ { n } | \leq g$ for some $g \in L ^ { 1 }$ , then $f \in L ^ { 1 }$ and

$$
\int | f _ { n } - f |  0 .
$$

As a consequence,

$$
\operatorname* { l i m } \int f _ { n } = \int \operatorname* { l i m } f _ { n } = \int f \quad { \mathrm { i . e . ~ } } \int f _ { n }  \int f < \infty
$$

Positivity not needed.

Proof (of DCT).

todo

## Theorem 3.1.18(Generalized DCT).

$f _ { n } \in L ^ { 1 }$ with $f _ { n }  f$ almost everywhere,

• There exist $g _ { n } \ge 0 \in L ^ { 1 }$ nonnegative with $| f _ { n } | \leq g _ { n }$

• $g _ { n }  g$ almost everywhere with $g \in L ^ { 1 }$ , and

$\operatorname* { l i m } \int g _ { n } = \int g ,$

then $f \in L ^ { 1 }$ and lim $\int f _ { n } = \int f < \infty .$

Note that this is the DCT with $\left| f _ { n } \right| < \left| g \right|$ relaxed to $| f _ { n } | < g _ { n } \to g \in L ^ { 1 }$

Proof .

Proceed by showing lim sup $\int f _ { n } \leq \int f \leq$ lim inf $\int f _ { n }$

$\int f \geq$ lim sup Z fn:

$$
\begin{array} { r l } {  { \int g - \int f = \int ( g - f ) } } \\ & { \leq \operatorname* { l i m i n f } \int ( g _ { n } - f _ { n } ) \quad \mathrm { F a t o u } } \\ & { = \operatorname* { l i m } \int g _ { n } + \operatorname* { l i m i n f } \int ( - f _ { n } ) } \\ & { = \operatorname* { l i m } \int g _ { n } - \operatorname* { l i m s u p } \int f _ { n } } \\ & { = \int g - \operatorname* { l i m s u p } \int f _ { n } } \end{array}
$$

$$
\implies \int f \geq \operatorname* { l i m } \operatorname* { s u p } \int f _ { n } .
$$

– Here we use $g _ { n } - f _ { n } \stackrel { n \to \infty } { \longrightarrow } g - f$ with $0 \leq | f _ { n } | - f _ { n } \leq g _ { n } - f _ { n }$ , so $g _ { n } - f _ { n }$ are nonnegative (and measurable) and Fatou’s lemma applies.

$\int f \leq$ lim inf $\int f _ { n } { \mathrm { : } }$

$$
\begin{array} { r l } {  { \int g + \int f = \int ( g + f ) } } \\ & { \leq \operatorname* { l i m i n f } \int ( g _ { n } + f _ { n } ) } \\ & { = \operatorname* { l i m } \int g _ { n } + \operatorname* { l i m i n f } \int f _ { n } } \\ & { = \int g + \operatorname* { l i m i n f } f _ { n } } \end{array}
$$

$$
\int f \leq \operatorname* { l i m } \operatorname* { i n f } \int f _ { n } .
$$

– Here we use that $g _ { n } + f _ { n } \to g + f$ with $0 \leq | f _ { n } | + f _ { n } \leq g _ { n } + f _ { n }$ so Fatou’s lemma again applies.

Proposition 3.1.19(Convergence in $L ^ { 1 }$ implies convergence of $L ^ { 1 }$ norm).If $f \in L ^ { 1 }$ , then

$$
\int | f _ { n } - f | \to 0 \iff \int | f _ { n } | \to \int | f | .
$$

Proof .

Let $g _ { n } = | f _ { n } | - | f _ { n } - f |$ , then $g _ { n }  | f |$ and

$$
| g _ { n } | = | | f _ { n } | - | f _ { n } - f | | \geq | f _ { n } - ( f _ { n } - f ) | = | f | \in L ^ { 1 } ,
$$

so the DCT applies to $g _ { n }$ and

$$
\| f _ { n } - f \| _ { 1 } = \int | f _ { n } - f | + | f _ { n } | - | f _ { n } | = \int | f _ { n } | - g _ { n }
$$

$$
 _ { D C T } \operatorname* { l i m } \int | f _ { n } | - \int | f | .
$$

## Theorem 3.1.20(Fatou).

If $f _ { n }$ is a sequence of nonnegative measurable functions, then

$$
\operatorname* { l i m } _ { n } \operatorname* { i n f } \int f _ { n } \geq \int \operatorname* { l i m } _ { n } \operatorname* { i n f } f _ { n }
$$

$$
\operatorname* { l i m } _ { n } \operatorname* { s u p } \int f _ { n } \leq \int \operatorname* { l i m } _ { n } \operatorname* { s u p } f _ { n } .
$$

Proof (of Fatou).

Prove Fatou

## Theorem 3.1.21(Tonelli (Non-Negative, Measurable)).

For $f ( x , y )$ non-negative and measurable, for almost every $x \in \mathbb { R } ^ { n }$

$f _ { x } ( y )$ is a measurable function

$F ( x ) = \int f ( x , y )$ dy is a measurable function,

• For E measurable, the slices $E _ { x } : = \left\{ y \ { \big | } \ ( x , y ) \in E \right\}$ are measurable.

$\int f = \int \int F , { \mathrm { i . e . } }$ any iterated integral is equal to the original.

## Theorem 3.1.22(Fubini (Integrable)).

For $f ( x , y )$ integrable, for almost every $x \in \mathbb { R } ^ { n }$ •

$f _ { x } ( y )$ is an integrable function

$F ( x ) : = \int f ( x , y )$ dy is an integrable function,

• For E measurable, the slices $E _ { x } : = \left\{ y \ { \big | } \ ( x , y ) \in E \right\}$ are measurable.

$\int f = \int \int f ( x , y )$ , i.e. any iterated integral is equal to the original

Theorem 3.1.23(Fubini-Tonelli).   
If any iterated integral is absolutely integrable, i.e. $\int \int | f ( x , y ) | < \infty .$ then $f$ is integrable   
and $\int f$ equals any iterated integral.

```latex
Proposition 3.1.24(Differentiating Under an Integral).
If $\bigg | \frac { \bar { \partial } } { \partial t } f ( x , t ) \bigg | \leq g ( x ) \in L ^ { 1 }$ , then letting $F ( t ) = \int f ( x , t ) \ d t ,$
${ \frac { \partial } { \partial t } } F ( t ) : = \operatorname* { l i m } _ { h \to 0 } \int { \frac { f ( x , t + h ) - f ( x , t ) } { h } } d x$
${ \stackrel { \mathrm { D C T } } { = } } \int { \frac { \partial } { \partial t } } f ( x , t ) d x .$
To justify passing the limit, let $h _ { k } \to 0$ be any sequence and define
$f _ { k } ( x , t ) = { \frac { f ( x , t + h _ { k } ) - f ( x , t ) } { h _ { k } } } ,$
so $f _ { k } \stackrel { k  \infty } { \longrightarrow } \frac { \partial f } { \partial t }$ pointwise.
Apply the MVT to $f _ { k }$ to get $f _ { k } ( x , t ) = f _ { k } ( \xi , t )$ for some $\xi \in [ 0 , h _ { k } ]$ , and show that $f _ { k } ( \xi , t ) \in L _ { 1 }$
```

```perl
Proposition 3.1.25(Commuting Sums with Integrals (non-negative)).
If $f _ { n }$ are non-negative and $\sum \int | f | _ { n } < \infty .$ , then $\sum \int f _ { n } = \int \sum f _ { n } .$
Proof . • Idea: MCT.
N
• Let $F _ { N } = \sum ^ { \mathbf { r } } f _ { n }$ be a finite partial sum;
• Then there are simple functions $\varphi _ { n } \nearrow f _ { n }$
• So $\sum \varphi _ { n } \nearrow F _ { N }$ and MCT applies
```

```perl
Theorem 3.1.26(Commuting Sums with Integrals (integrable)).
$\left\{ f _ { n } \right\}$ integrable with either $\sum \int | f _ { n } | < \infty$ or $\int \sum | f _ { n } | < \infty ,$ then
$\int \sum f _ { n } = \sum \int f _ { n } .$
```

$$
f _ { n } ( x ) \geq 0
$$

$$
n ,
$$

$$
\left| f _ { n } \right|
$$

Proposition 3.1.27(?).

If $f _ { k } \in L ^ { 1 }$ and $\sum \| f _ { k } \| _ { 1 } <$ ∞ then $\sum f _ { k }$ converges almost everywhere and in $L ^ { 1 }$

Proof (?).

Define $F _ { N } = \sum ^ { N } f _ { k }$ and $F = \operatorname* { l i m } _ { N } F _ { N }$ , then $\| F _ { N } \| _ { 1 } \le \sum ^ { N } \| f _ { k } \| < \infty$ so $F \in L ^ { 1 }$ and $\| F _ { N } - F \| _ { 1 } \to$ 0 so the sum converges in $L ^ { 1 } .$ Almost everywhere convergence: ?

## 3.2 Examples of (Non)Integrable Functions

Example 3.2.1(Examples of integrable functions):

$\int { \frac { 1 } { 1 + x ^ { 2 } } } = \arctan ( x ) \stackrel { x  \infty } {  } \pi / 2 < \infty$

• Any bounded function (or continuous on a compact set, by EVT)

$\int _ { 0 } ^ { 1 } { \frac { 1 } { \sqrt { x } } } < \infty$

$\int _ { 0 } ^ { 1 } \frac { 1 } { x ^ { 1 - \varepsilon } } < \infty$

$\int _ { 1 } ^ { \infty } { \frac { 1 } { x ^ { 1 + \varepsilon } } } < \infty$

Example 3.2.2(Examples of non-integrable functions):

$\int _ { 0 } ^ { 1 } { \frac { 1 } { x } } = \infty .$

$\int _ { { \frac { 1 } { a } } \infty } ^ { \infty } { \frac { 1 } { x } } = \infty .$

$\int _ { 1 } ^ { \infty } { \frac { 1 } { \sqrt { x } } } = \infty$

$\int _ { 1 } ^ { \infty } { \frac { \cdot } { x ^ { 1 - \varepsilon } } } = \infty$

$\int _ { 0 } ^ { 1 } { \frac { 1 } { x ^ { 1 + \varepsilon } } } = \infty$

3.3 $L ^ { 1 }$ Facts

Proposition 3.3.1(Zero in ${ \cal L } ^ { 1 } \ i f f$ zero almost everywhere).   
For $f \in L ^ { + }$ 2   
$\int f = 0 \quad \Longleftrightarrow \quad f \equiv 0$ almost everywhere.

## Proof .

• Obvious for simple functions:   
– If $f ( x ) = \sum _ { j = 1 } ^ { n } c _ { j } \chi _ { E _ { j } }$ , then $\int f = 0$ iff for each j, either $c _ { j } = 0 ~ { \mathrm { o r } } ~ m ( E _ { j } ) = 0 .$   
– Since nonzero $c _ { j }$ correspond to sets where $f \neq 0 ,$ this says m $( \{ f \neq 0 \} ) = 0 .$   
⇐= :   
If $f = 0$ almost everywhere and $\varphi \nearrow f ,$ then $\varphi = 0$ almost everywhere since   
$\varphi ( x ) \leq f ( x )$ -Then   
f = sup ϕ = sup 0 = 0.   
ϕ≤f ϕ≤f   
=⇒ :   
– Instead show negating $^ { 6 6 } f = 0$ almost everywhere” implies $\int f \neq 0 .$   
– Write $\{ f \neq 0 \} = \cup _ { n \in \mathbb { N } } S _ { n }$ where $S _ { n } : = { \bigg \{ } x { \Big | } f ( x ) \geq { \frac { 1 } { n } } { \bigg \} } .$   
– Since “not $f = 0$ almost everywhere”, there exists an n such that $m ( S _ { n } ) > 0 .$   
– Then   
0 < 1n χEn ≤ f =⇒ 0 < Z 1n χEn ≤ Z f.

## Proposition 3.3.2(Translation Invariance).

The Lebesgue integral is translation invariant, i.e.

$$
\int f ( x ) \ d x = \int f ( x + h ) \ d x
$$

for anyh.

## Proof .

• Let $E \subseteq X ;$ for characteristic functions,

$$
\int _ { X } \chi _ { E } ( x + h ) = \int _ { X } \chi _ { E + h } ( x ) = m ( E + h ) = m ( E ) = \int _ { X } \chi _ { E } ( x )
$$

by translation invariance of measure.

• So this also holds for simple functions by linearity.

For $f \in L ^ { + }$ , choose $\varphi _ { n } \nearrow f$ so $\int \varphi _ { n }  \int f .$

• Similarly, $\tau _ { h } \varphi _ { n } \nearrow \tau _ { h } f$ so $\int \tau _ { h } f  \int f$

• Finally $\left\{ \int \tau _ { h } \varphi \right\} = \left\{ \int \varphi \right\}$ by step 1, and the suprema are equal by uniqueness of limits.

## Proposition 3.3.3(Integrals distribute over disjoint sets).

If $X \subseteq A \cup B$ , then $\int _ { X } f \leq \int _ { A } f + \int _ { A ^ { c } } f$ with equality iff $X = A \amalg B$

$$
L ^ { 1 }
$$

If $f \in L ^ { 1 }$ and f is uniformly continuous, then $f ( x ) \stackrel { | x |  \infty } { {  } } 0 .$

## 4! Warning 3.3.5

This doesn’t hold for general $L ^ { 1 }$ functions, take any train of triangles with height 1 and summable areas.

## Theorem 3.3.6(Small Tails in $L ^ { 1 } )$

If $f \in L ^ { 1 }$ , then for every ε there exists a radius R such that if $A = B _ { R } ( 0 ) ^ { c }$ , then $\int _ { A } | f | < \varepsilon .$

## Proof .

• Approximate with compactly supported functions.

• Take $g \stackrel { L _ { \textstyle 1 } } {  } f$ with $g \in C _ { c }$

• Then choose N large enough so that $g = 0$ on $E : = B _ { N } ( 0 )$

• Then

$$
\int _ { E } | f | \leq \int _ { E } { \big | } f - g { \big | } + \int _ { E } | g { \big | } .
$$

## Proposition 3.3.7(L1 functions are absolutely continuous.).

$$
m ( E ) \to 0 \implies \int _ { E } f \to 0 .
$$

## Proof (?).

Approximate with compactly supported functions. Take $g \ { \stackrel { L _ { 1 } } { \to } } \ f _ { : }$ then $g \le M$ so $\int _ { E } f \leq$

$$
\int _ { E } f - g + \int _ { E } g \to 0 + M \cdot m ( E ) \to 0 .
$$

Proposition ${ \bf 3 . 3 . 8 } ( L ^ { 1 }$ functions are finite almost everywhere.). If $f \in L ^ { 1 }$ , then $m ( \{ f ( x ) = \infty \} ) = 0 .$

Proof (?).

$$
A = \{ f ( x ) = \infty \}
$$

$$
\infty > \int f = \int _ { A } f + \int _ { A ^ { c } } f = \infty \cdot m ( A )
$$

$$
\int _ { A ^ { c } } f \implies m ( X ) = 0 .
$$

Theorem 3.3.9(Continuity in $L ^ { 1 } )$

$$
\| \tau _ { h } f - f \| _ { 1 } \stackrel { h \to 0 } { \longrightarrow } 0
$$

Proof .

Approximate with compactly supported functions. Take $g \stackrel { L _ { \textstyle 1 } } {  } f$ with $g \in C _ { c }$

$$
\begin{array} { l } { \displaystyle \int f ( x + h ) - f ( x ) \le \int f ( x + h ) - g ( x + h ) + \int g ( x + h ) - g ( x ) + \int g ( x ) - f ( x ) \ d x } \\ { \displaystyle \qquad \overset { \triangledown \cdot  } \longrightarrow \mathrm { 2 } \varepsilon + \int g ( x + h ) - g ( x ) \qquad } \\ { \displaystyle \qquad = \int _ { K } g ( x + h ) - g ( x ) + \int _ { K ^ { c } } g ( x + h ) - g ( x ) \ d y } \\ { \displaystyle \qquad \overset { \triangledown \cdot  } \longrightarrow 0 , } \end{array}
$$

which follows because we can enlarge the support of g to K where the integrand is zero on $K ^ { c }$ , then apply uniform continuity on $K$

Proposition 3.3.10(Integration by parts, special case).

$$
\begin{array} { r } { F ( x ) : = \displaystyle \int _ { 0 } ^ { x } f ( y ) d y \quad \mathrm { ~ a n d ~ } \quad G ( x ) : = \int _ { 0 } ^ { x } g ( y ) d y } \\ { \implies \displaystyle \int _ { 0 } ^ { 1 } F ( x ) g ( x ) d x = F ( 1 ) G ( 1 ) - \int _ { 0 } ^ { 1 } f ( x ) G ( x ) d x . } \end{array}
$$

Proof (?).

Fubini-Tonelli, and sketch region to change integration bounds.

Theorem 3.3.11(Lebesgue Density).

$$
A _ { h } ( f ) ( x ) : = \frac { 1 } { 2 h } \int _ { x - h } ^ { x + h } f ( y ) d y \implies \| A _ { h } ( f ) - f \| \overset { h \to 0 } { \to } 0 .
$$

Proof (?).

Fubini-Tonelli, and sketch region to change integration bounds, and continuity in $L ^ { 1 }$

## 3.4 Lp Facts

## Proposition 3.4.1(Dense subspaces of $L ^ { 2 } ( I ) \ )$

The following are dense subspaces of $L ^ { 2 } ( [ 0 , 1 ] )$

• Simple functions

$\mathrm { S t e p }$ functions

$C _ { 0 } ( [ 0 , 1 ] )$

• Smoothly differentiable functions $C _ { 0 } ^ { \infty } ( [ 0 , 1 ] )$

• Smooth compactly supported functions $C _ { c } ^ { \infty }$

Theorem 3.4.2(?).

$$
m ( X ) < \infty \implies \operatorname* { l i m } _ { p \to \infty } \| f \| _ { p } = \| f \| _ { \infty } .
$$

Proof $( ? ) .$

Let $M = \| f \| _ { \infty } .$

• For any $L < M$ , let $S = \{ | f | \geq L \}$

• Then $m ( S ) > 0$ and

$$
\begin{array} { r l } {  { \| f \| _ { p } = ( \int _ { X } | f | ^ { p } ) ^ { \frac { 1 } { p } } } } \\ & { \ge ( \int _ { S } | f | ^ { p } ) ^ { \frac { 1 } { p } } } \\ & { \ge L m ( S ) ^ { \frac { 1 } { p } p } \xrightarrow { \to \infty } L } \\ & { \Longrightarrow \operatorname* { l i m } _ { p } \operatorname* { i n f } \| f \| _ { p } \ge M . } \end{array}
$$

We also have

$$
\begin{array} { r l r } {  { \| f \| _ { p } = ( \int _ { X } | f | ^ { p } ) ^ { \frac { 1 } { p } } } } \\ & { } & { \leq ( \int _ { X } M ^ { p } ) ^ { \frac { 1 } { p } } } \\ & { } & { = M \ m ( X ) ^ { \frac { 1 } { p } } \xrightarrow { p \to \infty } M } \\ & { } & { \Longrightarrow \ \operatorname* { l i m } _ { p } \| f \| _ { p } \leq M . } \end{array}
$$

Theorem 3.4.3(Duals for $L ^ { p }$ spaces).   
$1 \leq p < \infty , ( L ^ { p } ) ^ { \vee } \cong L ^ { q } .$

Proof (p = 2 case).   
Use Riesz Representation for Hilbert spaces.

```latex
Proposition 3.4.4(L1 is not quite the dual of $L ^ { \infty } \cdot \mathcal { \mathrm { I } } .$
$L ^ { 1 } \bar { \subset } ( L ^ { \infty } ) ^ { \vee }$ , since the isometric mapping is always injective, but never surjective.
```

## 3.5 Counterexamples

```latex
Proposition 3.5.1(a.e. convergence never implies $L ^ { p }$ convergence).
Lp
Sequences $f _ { k } \stackrel { a . e . } {  } f$ but $f _ { k } \not \to f \colon$
• For $1 \le p <$ ∞: The skateboard to infinity, $f _ { k } = \chi _ { [ k , k + 1 ] } .$
Then $f _ { k } \stackrel { a . e . } {  } 0$ but $\| f _ { k } \| _ { p } = 1$ for all $k .$
Converges pointwise and a.e., but not uniformly
and not in norm.
• For $p = \infty \colon$ The sliding boxes $f _ { k } = k \cdot \chi _ { [ 0 , \frac { 1 } { k } ] } .$
Then similarly $f _ { k } \ { \stackrel { a . e . } {  } } \ 0 ,$ but $\| f _ { k } \| _ { p } = 1$ and $\| f _ { k } \| _ { \infty } = k  \infty$
Converges $a . e . _ { \cdot }$ , but not uniformly, not pointwise,
and not in norm.
```

Proposition 3.5.2(The four big counterexamples in convergence).   
1. Uniform: $f _ { n }  f : \forall \varepsilon \exists N \mid n \geq N \implies | f _ { N } ( x ) - f ( x ) | < \varepsilon \forall x .$   
2. Pointwise: $f _ { n } ( x )  f ( x )$ for all $x .$ (This is just a sequence of numbers)   
3. Almost Everywhere: $f _ { n } ( x )  f ( x )$ for almost all $x .$   
4. Norm: $\| f _ { n } - f \| _ { 1 } = \int | f _ { n } ( x ) - f ( x ) | \to 0 .$   
We have $1 \implies 2 \implies 3 ,$ and in general no implication can be reversed, but (warning) none

of 1, 2, 3 imply 4 or vice versa.

$f _ { n } = ( 1 / n ) \chi _ { ( 0 , n ) }$ . This converges uniformly to 0, but the integral is identically 1. So this satisfies 1,2,3 and not 4.

<!-- image-->  
Figure 2: image_2021-05-21-16-38-30

$f _ { n } = \chi _ { ( n , n + 1 ) }$ (skateboard to infinity). This satisfies 2,3 but not 1, 4.

<!-- image-->  
Figure 3: image_2021-05-21-16-42-08

$f _ { n } = n \chi _ { ( 0 , \frac { 1 } { n } ) }$ . This satisfies 3 but not 1,2,4.

<!-- image-->  
Figure 4: image_2021-05-21-16-54-38

$f _ { n }$ : one can construct a sequence where $f _ { n } \to 0$ in $L ^ { 1 }$ but is not 1,2, or 3. The construction:

– Break I into 2 intervals, let $f _ { 1 }$ be the indicator on the first half, $f _ { 2 }$ the indicator on the second.

– Break I into $2 ^ { 2 } = 4$ intervals, like $f _ { 3 }$ be the indicator on the first quarter, $f _ { 4 }$ on the second, etc.

– Break I into $2 ^ { k }$ intervals and cyclic through k indicator functions.

<!-- image-->

Figure 5: image_2021-05-21-16-49-09

– Then $\int f _ { n } = 1 / 2 ^ { n } \to 0$ , but $f _ { n } \nrightarrow 0$ pointwise since for every x, there are infinitely many n for which $f _ { n } ( x ) = 0$ and infinitely many for which $f _ { n } ( x ) = 1$

Proposition 3.5.3(Functional analytic properties of $L ^ { 1 }$ and $L ^ { 2 } )$ . For any measure space $( X , { \mathcal { M } } , \mu )$

$L ^ { 1 } ( X )$ is Banach space.

$L ^ { 2 } ( X )$ is a (possibly non-separable) Hilbert space.

## Fourier Transform and Convolution

<!-- image-->

## 4.1 The Fourier Transform

<!-- image-->

Proposition 4.1.1(?).   
If $\widehat { f } = \widehat { g }$ then f = g almost everywhere.

Proposition 4.1.2(Riemann-Lebesgue: Fourier transforms have small tails.).

$$
f \in L ^ { 1 } \implies { \widehat { f } } ( \xi ) \to 0 { \mathrm { ~ a s ~ } } | \xi | \to \infty ,
$$

if $f \in L ^ { 1 }$ , then bf is continuous and bounded.

## Proof (?).

• Boundedness:

$$
\left| { \widehat { f } } ( \xi ) \right| \leq \int | f | \cdot \left| e ^ { 2 \pi i x \cdot \xi } \right| = \| f \| _ { 1 } .
$$

• Continuity:

$\left| { \widehat { f } } ( \xi _ { n } ) - { \widehat { f } } ( \xi ) \right|$

• Apply DCT to show $a \ { \overset { n \to \infty } { \to } } \ 0 .$

## Theorem 4.1.3(Fourier Inversion).

$$
f ( x ) = \int _ { \mathbb { R } ^ { n } } { \widehat { f } } ( x ) e ^ { 2 \pi i x \cdot \xi } d \xi .
$$

## 4! Warning 4.1.4

Fubini-Tonelli does not work here!

Proof (?).

Idea: Fubini-Tonelli doesn’t work directly, so introduce a convergence factor, take limits, and use uniqueness of limits.

• Take the modified integral:

$$
\begin{array} { r l } { \displaystyle I _ { t } ( x ) = \int \hat { f } ( \xi ) e ^ { 2 \pi i x \xi } \epsilon ^ { - \alpha \tau ^ { 2 } \left| \xi \right| ^ { 2 } } } \\ { = \int \hat { f } ( \xi ) \dot { \varphi } ( \xi ) } \\ { = \int f ( \xi ) \hat { \varphi } ( \xi ) } \\ { = \int f ( \xi ) \hat { \varphi } ( \xi - x ) } \\ { = \int f ( \xi ) \hat { \varphi } ( \xi - x ) } \\ { = \int f ( \xi ) g _ { t } ( x - \xi ) \ d \xi } \\ { = \int f ( y - x ) g _ { t } ( y ) \ d y } & { ( \xi = y - x ) } \\ { = \left( ( f + g _ { t } ) \right) } \\ { . . . \ \mathrm { ~ } } \\ { . . . \ \mathrm { ~ } } \\ { . . . \ } \end{array}
$$

• We also have

$$
\begin{array} { l } { \displaystyle \operatorname* { l i m } _ { t \to 0 } I _ { t } ( x ) = \displaystyle \operatorname* { l i m } _ { t \to 0 } \int \hat { f } ( \xi ) ~ e ^ { 2 \pi i x \cdot \xi } ~ e ^ { - \pi t ^ { 2 } | \xi | ^ { 2 } } } \\ { = \displaystyle \operatorname* { l i m } _ { t \to 0 } \int \hat { f } ( \xi ) \varphi ( \xi ) } \\ { = \displaystyle { D C T } \int \hat { f } ( \xi ) \operatorname* { l i m } _ { t \to 0 } \varphi ( \xi ) } \\ { = \displaystyle \int \hat { f } ( \xi ) ~ e ^ { 2 \pi i x \cdot \xi } } \end{array}
$$

• So

$$
I _ { t } ( x )  \int \widehat { f } ( \xi ) \ e ^ { 2 \pi i x \cdot \xi } \mathrm { p o i n t w i s e ~ a n d } \| I _ { t } ( x ) - f ( x ) \| _ { 1 }  0 .
$$

• So there is a subsequence $I _ { t _ { n } }$ such that $I _ { t _ { n } } ( x )  f ( x )$ almost everywhere

• Thus $f ( x ) = \int { \widehat { f } } ( \xi ) \ e ^ { 2 \pi i x \cdot \xi }$ almost everywhere by uniqueness of limits.

Proposition 4.1.5(Eigenfunction of the Fourier transform).

$$
g ( x ) : = e ^ { - \pi | t | ^ { 2 } } \implies \widehat { g } ( \xi ) = g ( \xi ) \quad \mathrm { a n d } \quad \widehat { g } _ { t } ( x ) = g ( t x ) = e ^ { - \pi t ^ { 2 } | x | ^ { 2 } } .
$$

## 4.2 Approximate Identities

Example 4.2.1(of an approximation to the identity.):

$$
\varphi ( x ) : = e ^ { - \pi x ^ { 2 } } .
$$

Theorem 4.2.2(Convolving against an approximate identity converges in $L ^ { 1 } . )$

$$
\| f * \varphi _ { t } - f \| _ { 1 } \stackrel { t \to 0 } { \to } 0 .
$$

Proof (?).

$$
\begin{array} { r l } { | I ^ { \prime } } & { \mathcal { I } \circ \varphi _ { 0 } | _ { 1 } - \int \hat { J } \circ \varphi _ { 0 } \int \hat { J } ( t ) } \\ & { - \int \hat { J } \circ \varphi _ { 0 } \int \varphi ( \theta , \theta ) d \theta - \int \int \hat { \sigma } ( t - \varphi _ { 0 } ) \hat { \varphi } ( \theta , \theta ) d \theta } \\ & { \quad - \int \int \hat { \sigma } ( t ) \theta \cdot \hat { \varphi } ( \theta , \theta ) d \theta } \\ & { \quad - \int \int \hat { \sigma } ( t \otimes \theta ) \big | \varphi ( \theta , \theta ) d \theta } \\ & { \quad - \int \int \hat { \sigma } ( t ) \theta \cdot \hat { \varphi } ( \theta , \theta ) d \theta } \\ & { \quad - \int \int \hat { \sigma } ( t ) \hat { \varphi } ( \theta , \theta ) d \theta } \\ & { \quad - \int \int \hat { \sigma } ( t ) \hat { \varphi } ( \theta , \theta ) d \theta } \\ & { \quad - \int \int \hat { \sigma } ( t ) \hat { \varphi } ( \theta , \theta ) \big | \theta } \\ & { \quad - \int \int \hat { \sigma } ( t ) \hat { \theta } ( \theta , \theta ) \big | \hat { \varphi } ( \theta , \theta ) d \theta } \\ & { \quad - \int \int _ { t _ { 0 } } \varphi ( \theta ) \big | \hat { \varphi } ( \theta , \theta ) \big | \hat { \varphi } ( \theta , \theta ) \big | \hat { \varphi } ( \theta , \varphi ) \big | \hat { \varphi } ( \theta , \theta ) } \\ & { \quad \le \int _ { t _ { 0 } } \varphi ( \theta ) d \theta - \int _ { t _ { 0 } } \varphi ( \theta ) ( | t | \theta | + | \varphi | ) | \hat { \varphi } ( \theta , \varphi ) \mathrm { c o n s i n g : ~ a l s ~ } \hat { \varphi } ( \theta ) } \\ & { \quad \le \int \int _ { t _ { 0 } } \varphi ( \theta ) \big | \int _ { t _ { 0 } } \varphi ( \theta | \hat { \varphi } ( \theta ) ) } \\ &  \quad \le \varphi - 2 | \hat { \varphi } | _ { 1 } - \ \end{array}
$$

Theorem 4.2.3(Convolutions vanish at infinity).

$$
f , g \in L ^ { 1 } { \mathrm { ~ a n d ~ b o u n d e d } } \implies \operatorname* { l i m } _ { | x | \to \infty } ( f * g ) ( x ) = 0 .
$$

Proof (?). • Choose $M \geq f , g .$

By small tails, choose N such that $\int _ { B _ { N } ^ { c } } | f | , \int _ { B _ { n } ^ { c } } | g | < \varepsilon$

• Note

$$
| f * g | \leq \int | f ( x - y ) | \ | g ( y ) | \ d y : = I .
$$

• Use $| x | \le | x - y | + | y |$ , take $| x | \geq 2 N$ so either

$$
| x - y | \geq N \implies I \leq \int _ { \{ x - y \geq N \} } | f ( x - y ) | M \ d y \leq \varepsilon M \to 0
$$

then

$$
| y | \geq N \implies I \leq \int _ { \{ y \geq N \} } M | g ( y ) | \ d y \leq M \varepsilon \to 0 .
$$

Proposition 4.2.4(Corollary of Young’s inequality). Take q = 1 in Young’s inequality to obtain

$$
\left\| f \ast g \right\| _ { p } \leq \left\| f \right\| p \| g \| 1 .
$$

```perl
Proposition 4.2.5 $( L ^ { 1 }$ is closed under convolution.).
If $f , g \in L ^ { 1 }$ then $f * g \in L ^ { 1 }$
```

## 5 Functional Analysis

## 5.1 Theorems

Fact 5.1.1 (Pythagoras)

$$
\langle v , \ w \rangle = 0 \ \Longrightarrow \ \| v + w \| = \| v \| + \| w \| .
$$

Theorem 5.1.2(Bessel’s Inequality).

For any orthonormal set $\{ u _ { n } \} \subseteq { \mathcal { H } } :$ a Hilbert space (not necessarily a basis),

$$
\left\| x - \sum _ { n = 1 } ^ { N } \left. x , u _ { n } \right. u _ { n } \right\| ^ { 2 } = \| x \| ^ { 2 } - \sum _ { n = 1 } ^ { N } | \langle x , u _ { n } \rangle | ^ { 2 }
$$

and thus

$$
\sum _ { n = 1 } ^ { \infty } | \langle x , u _ { n } \rangle | ^ { 2 } \leq \| x \| ^ { 2 } .
$$

Proof (of Bessel’s inequality).

Let $S _ { N } = \sum _ { n = 1 } ^ { N } \langle x , \ u _ { n } \rangle u _ { n }$

$$
\begin{array} { r l } { \left| \left| \mathbf { r } - \bar { S } _ { 3 } \right| ^ { 2 } - \bar { S } _ { 4 } ^ { \nu } - \mathcal { R } _ { 3 } , \quad \mathcal { L } _ { 3 } ^ { \nu } \right| ^ { 2 } } & { \quad \forall \theta \in \mathcal { R } _ { 3 } ^ { \nu } , } \\ & { = \left\| \left| \bar { \mathbf { r } } \right\| ^ { 2 } + \left\| \bar { \mathbf { s } } \right\| ^ { 2 } \left\| \mathbf { s } \right\| ^ { 2 } - 2 \mathbf { R } _ { 3 } ^ { \nu } \left\| \mathbf { s } \right\| ^ { 2 } , \quad \forall \theta \in \mathcal { R } _ { 3 } ^ { \nu } \right\} } \\ & { = \left\| \bar { \mathbf { r } } \right\| ^ { 2 } + \left\| \bar { \mathbf { s } } \right\| ^ { 2 } \left\| \mathbf { s } \right\| ^ { 2 } - 2 \mathbf { R } _ { 3 } ^ { \nu } \left\| \mathbf { s } \right\| ^ { 2 } , } \\ & { \quad - \left\| \bar { \mathbf { s } } \right\| ^ { 2 } + \left\| \bar { \mathbf { s } } \right\| ^ { 2 } - 2 \mathbf { R } _ { 3 } ^ { \nu } \left\| \bar { \mathbf { s } } \right\| ^ { 2 } , } \\ & { = - \left\| \bar { \mathbf { s } } \right\| ^ { 2 } + \left\| \bar { \mathbf { s } } \right\| ^ { 2 } - 3 \mathbf { R } _ { 3 } ^ { \nu } \left\| \bar { \mathbf { s } } \right\| ^ { 2 } , } \\ & { \quad - \left\| \bar { \mathbf { s } } \right\| ^ { 2 } - \left\| \bar { \mathbf { s } } \right\| ^ { 2 } - 3 \mathbf { R } _ { 3 } ^ { \nu } \left\| \bar { \mathbf { s } } \right\| ^ { 2 } , } \\ &  \quad - \left\| \bar { \mathbf { s } } \right\| ^ { 2 } + \left\| \bar { \mathbf { s } } \right\| ^ { 2 } - 3 \mathbf { R } _ { 3 } ^ { \nu } \left\| \bar { \mathbf { s } } \right\| ^ { 2 } - 2 \frac { \Delta }  \end{array}
$$

• By continuity of the norm and inner product, we have

$$
\begin{array} { c } { { \displaystyle \operatorname* { l i m } _ { N \to \infty } \| x - S _ { N } \| ^ { 2 } = \operatorname* { l i m } _ { N \to \infty } \| x \| ^ { 2 } - \displaystyle \sum _ { n = 1 } ^ { N } | \langle x , \ u _ { n } \rangle | ^ { 2 } } } \\ { { \displaystyle \Longrightarrow \ \left\| x - \operatorname* { l i m } _ { N \to \infty } S _ { N } \right\| ^ { 2 } = \| x \| ^ { 2 } - \operatorname* { l i m } _ { N \to \infty } \displaystyle \sum _ { n = 1 } ^ { N } | \langle x , \ u _ { n } \rangle | ^ { 2 } } } \\ { { \displaystyle \Longrightarrow \ \left\| x - \sum _ { n = 1 } ^ { \infty } \langle x , \ u _ { n } \rangle u _ { n } \right\| ^ { 2 } = \| x \| ^ { 2 } - \displaystyle \sum _ { n = 1 } ^ { \infty } | \langle x , \ u _ { n } \rangle | ^ { 2 } . } } \end{array}
$$

• Then noting that $0 \leq \| x - S _ { N } \| ^ { 2 }$

$$
\begin{array} { c } { { \displaystyle 0 \leq \| x \| ^ { 2 } - \displaystyle \sum _ { n = 1 } ^ { \infty } | \langle x , \ u _ { n } \rangle | ^ { 2 } } } \\ { { \Longrightarrow \displaystyle \sum _ { n = 1 } ^ { \infty } | \langle x , \ u _ { n } \rangle | ^ { 2 } \leq \| x \| ^ { 2 } { \bf \overline { { u } } } . } } \end{array}
$$

Theorem 5.1.3(Riesz Representation for Hilbert Spaces).

If Λ is a continuous linear functional on a Hilbert space H, then there exists a unique $y \in H$

## such that

$$
\forall x \in H , \quad \Lambda ( x ) = \langle x , y \rangle .
$$

Proof (?).

• Define M := ker Λ.

• Then M is a closed subspace and so $H = M \oplus M ^ { \perp }$

• There is some $z \in M ^ { \bot }$ such that $\| z \| = 1$ .

• Set $u : = \Lambda ( x ) z - \Lambda ( z ) x$

• Check

$$
\Lambda ( u ) = \Lambda ( \Lambda ( x ) z - \Lambda ( z ) x ) = \Lambda ( x ) \Lambda ( z ) - \Lambda ( z ) \Lambda ( x ) = 0 \implies u \in M
$$

• Compute

$$
0 = \langle u , ~ z \rangle
$$

$$
= \langle \Lambda ( x ) z - \Lambda ( z ) x , ~ z \rangle
$$

$$
= \langle \Lambda ( x ) z , \ z \rangle - \langle \Lambda ( z ) x , \ z \rangle
$$

$$
= \Lambda ( x ) \langle z , \ z \rangle - \Lambda ( z ) \langle x , \ z \rangle
$$

$$
= \Lambda ( x ) \| z \| ^ { 2 } - \Lambda ( z ) \langle x , \ z \rangle
$$

$$
= \Lambda ( x ) - \Lambda ( z ) \langle x , \ z \rangle
$$

$$
{ \bf \Omega } = \Lambda ( x ) - \Big \langle x , \overline { { \Lambda ( z ) } } z \Big \rangle ,
$$

• Choose $y : = \overline { { \Lambda ( z ) } } z$ z .

• Check uniqueness:

$$
\langle x , \ y \rangle = \langle x , \ y ^ { \prime } \rangle \quad \forall x
$$

$$
\implies \langle x , \ y - y ^ { \prime } \rangle = 0 \quad \forall x
$$

$$
\implies \left. y - y ^ { \prime } , ~ y - y ^ { \prime } \right. = 0
$$

$$
\implies \lVert y - y ^ { \prime } \rVert = 0
$$

$$
\implies y - y ^ { \prime } = \mathbf { 0 } \implies y = y ^ { \prime } .
$$

Theorem 5.1.4(Functionals are continuous if and only if bounded).

Let $L : X  \mathbb { C }$ be a linear functional, then the following are equivalent:

1. L is continuous

2. L is continuous at zero

3. L is bounded, i.e. ∃c $\geq 0$ such that $| L ( x ) |$ ≤ ckxk for all $x \in H$

Proof (?).   
2 =⇒ 3: Choose $\delta < 1$ such that   
$\| x \| \leq \delta \implies | L ( x ) | < 1 .$   
Then   
$| L ( x ) | = \left| L \left( { \frac { \| x \| } { \delta } } { \frac { \delta } { \| x \| } } x \right) \right|$   
$= { \frac { \| x \| } { \delta } } \left. L \left( \delta { \frac { x } { \| x \| } } \right) \right.$   
$\leq { \frac { \| x \| } { \delta } } 1 ,$   
so we can take $c = { \frac { 1 } { \delta } } .$   
3 =⇒ 1:   
We have $| L ( x - y ) | \leq c \| x - y \|$ , so given $\varepsilon \geq 0$ simply choose $\delta = \frac { \varepsilon } { c } .$

If H is a Hilbert space, then $( H ^ { \vee } , \| - \| _ { \mathrm { o p } } )$ is a normed space.

Proof (?).   
The only nontrivial property is the triangle inequality, but   
$\begin{array} { r } { \| L _ { 1 } + L _ { 2 } \| _ { \mathrm { o p } } = \operatorname* { s u p } | L _ { 1 } ( x ) + L _ { 2 } ( x ) | \leq \operatorname* { s u p } | L _ { 1 } ( x ) | + | \operatorname* { s u p } L _ { 2 } ( x ) | = \| L _ { 1 } \| _ { \mathrm { o p } } + \| L _ { 2 } \| _ { \mathrm { o p } } . } \end{array}$

Theorem 5.1.6(The operator norm on $X ^ { \vee }$ yields a Banach space).   
If X is a normed vector space, then $( X ^ { \vee } , \| - \| _ { \mathrm { o p } } )$ is a Banach space.

Proof (?).   
• Let $\left\{ L _ { n } \right\}$ be Cauchy in $X ^ { \vee }$   
• Then for all $x \in C , \{ L _ { n } ( x ) \} \subset \mathbb { C }$ is Cauchy and converges to something denoted $L ( x )$   
• Need to show L is continuous and $\| L _ { n } - L \| \to 0 .$   
• Since $\left\{ L _ { n } \right\}$ is Cauchy in $X ^ { \vee }$ , choose N large enough so that   
$n , m \geq N \implies \lVert L _ { n } - L _ { m } \rVert < \varepsilon \implies \lvert L _ { m } ( x ) - L _ { n } ( x ) \rvert < \varepsilon \quad \forall x \ \lvert \lVert x \rVert = 1 .$

• Take $n \to \infty$ to obtain

$$
m \geq N \implies | L _ { m } ( x ) - L ( x ) | < \varepsilon \quad \forall x \ \Big | \ \| x \| = 1
$$

$$
\implies \lVert L _ { m } - L \rVert < \varepsilon  0 .
$$

• Continuity:

$$
| L ( x ) | = | L ( x ) - L _ { n } ( x ) + L _ { n } ( x ) |
$$

$$
\leq | L ( x ) - L _ { n } ( x ) | + | L _ { n } ( x ) |
$$

$$
\leq \varepsilon \| x \| + c \| x \|
$$

$$
= ( \varepsilon + c ) \| x \| \mathbf { \overline { { u } } } .
$$

## Theorem 5.1.7(Riesz-Fischer).

Let $U = \{ u _ { n } \} _ { n = 1 } ^ { \infty }$ be an orthonormal set (not necessarily a basis), then

1. There is an isometric surjection

$$
\mathcal { H } \to \ell ^ { 2 } ( \mathbb { N } )
$$

$$
\mathbf { x } \mapsto \{ \langle \mathbf { x } , \ \mathbf { u } _ { n } \rangle \} _ { n = 1 } ^ { \infty }
$$

i.e. if $\{ a _ { n } \} \in \ell ^ { 2 } ( \mathbb { N } )$ , so $\sum \left| a _ { n } \right| ^ { 2 } < \infty$ , then there exists ${ \textrm { a x } } \in { \mathcal { H } }$ such that

$$
a _ { n } = \left. \mathbf { x } , ~ \mathbf { u } _ { n } \right. \quad \forall n .
$$

2. x can be chosen such that

$$
\left\| \mathbf { x } \right\| ^ { 2 } = \sum | a _ { n } | ^ { 2 }
$$

Note: the choice of x is unique $\begin{array} { r l } { \iff } & { { } \left\{ u _ { n } \right\} } \end{array}$ is complete, i.e. hx, uni = 0 for all n implies x = 0.

Proof (?).

• Given $\left\{ a _ { n } \right\}$ , define $S _ { N } = \sum ^ { N } a _ { n } { \bf u } _ { n }$

$S _ { N }$ is Cauchy in H and so $\overline { { S } } _ { N }  \mathbf { x }$ for some $\mathbf { x } \in \mathcal { H } .$

• $\langle x , \ u _ { n } \rangle = \langle x - S _ { N } , \ u _ { n } \rangle + \langle S _ { N } , \ u _ { n } \rangle \to a _ { n }$

• By construction, $\left\| x - S _ { N } \right\| ^ { 2 } = \left\| x \right\| ^ { 2 } - \sum ^ { l \mathrm { v } } | a _ { n } | ^ { 2 } \to 0 ,$ N so $\| x \| ^ { 2 } = \sum ^ { \infty } | a _ { n } | ^ { 2 } .$

## Extra Problems: Measure Theory

## 6.1 Greatest Hits

• ?: Show that for $E \subseteq \mathbb { R } ^ { n }$ , TFAE:

1. E is measurable

2. $E = H \cup Z$ here H is $F _ { \sigma }$ and $Z$ is null

3. $E = V \setminus Z ^ { \prime }$ where $V \in G _ { \delta }$ and $Z ^ { \prime }$ is null.

$\star :$ Show that if $E \subseteq \mathbb { R } ^ { n }$ is measurable then $m ( E ) = \operatorname* { s u p } \left\{ m ( K ) \ \big | \ K \subset E \right.$ compacto iff for all $\varepsilon > 0$ there exists a compact $K \subseteq E$ such that $m ( K ) \geq { \dot { m } } ( E ) - { \dot { \varepsilon } } .$

$\star :$ Show that cylinder functions are measurable, i.e. if f is measurable on $\mathbb { R } ^ { s } .$ , then $F ( x , y ) : =$ $f ( x )$ is measurable on $\mathbb { R } ^ { s } \times \mathbb { R } ^ { t }$ for any t.

• ?: Prove that the Lebesgue integral is translation invariant, i.e. if $\tau _ { h } ( x ) \ = \ x + h$ then $\int \tau _ { h } f = \int f .$

• ?: Prove that the Lebesgue integral is dilation invariant, i.e. if $f _ { \delta } ( x ) = \frac { f ( \frac { x } { \delta } ) } { \delta ^ { n } }$ then $\int f _ { \delta } = \int f .$

• ?: Prove continuity in $L ^ { 1 } .$ , i.e.

$$
f \in L ^ { 1 } \Longrightarrow \operatorname* { l i m } _ { h \to 0 } \int | f ( x + h ) - f ( x ) | = 0 .
$$

• ?: Show that

$$
f , g \in L ^ { 1 } \implies f * g \in L ^ { 1 } \quad \mathrm { a n d } \quad \| f * g \| _ { 1 } \leq \| f \| _ { 1 } \| g \| _ { 1 } .
$$

• ?: Show that if $X \subseteq \mathbb { R }$ with $\mu ( X ) < \infty$ then

$$
\left\| f \right\| _ { p } \to { \overset { p \to \infty } { \to } } \left\| f \right\| _ { \infty } .
$$

<!-- image-->

## 6.2 By Topic

## 6.2.1 Topology

• Show that every compact set is closed and bounded.

• Show that if a subset of a metric space is complete and totally bounded, then it is compact.

• Show that if K is compact and F is closed with K, F disjoint then dist $( K , F ) > 0$

## 6.2.2 Continuity

• Show that a continuous function on a compact set is uniformly continuous.

## 6.2.3 Differentiation

• Show that if $f \in C ^ { 1 } ( \mathbb { R } )$ and both $\operatorname* { l i m } _ { x \to \infty } f ( x )$ and $\operatorname* { l i m } _ { x \to \infty } f ^ { \prime } ( x )$ exist, then $\operatorname* { l i m } _ { x \to \infty } f ^ { \prime } ( x )$ must be zero.

## 6.2.4 Advanced Limitology

• If f is continuous, is it necessarily the case that $f ^ { \prime }$ is continuous?

• If $f _ { n }  f .$ , is it necessarily the case that $f _ { n } ^ { \prime }$ converges to $f ^ { \prime } ~ ( \mathrm { o r ~ a t ~ a l l } ) ?$

• Is it true that the sum of differentiable functions is differentiable?

• Is it true that the limit of integrals equals the integral of the limit?

• Is it true that a limit of continuous functions is continuous?

• Show that a subset of a metric space is closed iff it is complete.

• Show that if $m ( E ) < \infty$ and $f _ { n }  f$ uniformly, then lim $\int _ { E } f _ { n } = \int _ { E } f .$

## Uniform Convergence

• Show that a uniform limit of bounded functions is bounded.

• Show that a uniform limit of continuous function is continuous.

– I.e. if $f _ { n }  f$ uniformly with each $f _ { n }$ continuous then $f$ is continuous.

• Show that

$f _ { n } : [ a , b ] \to \mathbb { R }$ are continuously differentiable with derivatives $f _ { n } ^ { \prime }$

– The sequence of derivatives $f _ { n } ^ { \prime }$ converges uniformly to some function $g$

– There exists at least one point $x _ { 0 }$ such that lim $f _ { n } ( x _ { 0 } )$ exists,

– Then $f _ { n }  f$ uniformly to some differentiable $f ,$ and $f ^ { \prime } = g$

• Prove that uniform convergence implies pointwise convergence implies a.e. convergence, but none of the implications may be reversed.

• Show that $\sum { \frac { x ^ { n } } { n ! } }$ converges uniformly on any compact subset of R.

Measure Theory

• Show that continuity of measure from above/below holds for outer measures.

• Show that a countable union of null sets is null.

## Measurability

• Show that f = 0 a.e. iff $\int _ { E } f = 0$ for every measurable set E.

Integrability

• Show that if $f$ is a measurable function, then $f = 0 ~ \mathrm { a . e }$ . iff $\int f = 0$

• Show that a bounded function is Lebesgue integrable iff it is measurable.

• Show that simple functions are dense in $L ^ { 1 }$

• Show that step functions are dense in $L ^ { 1 }$

• Show that smooth compactly supported functions are dense in $L ^ { 1 }$

## Convergence

• Prove Fatou’s lemma using the Monotone Convergence Theorem.

• Show that if $\left\{ f _ { n } \right\}$ is in $L ^ { 1 }$ and $\sum \int | f _ { n } | < \infty$ then $\sum f _ { n }$ converges to an $L ^ { 1 }$ function and

$$
\int \sum f _ { n } = \sum \int f _ { n } .
$$

Convolution

• Show that if $f , g$ are continuous and compactly supported, then so is $f * g .$

• Show that if $f \in L ^ { 1 }$ and $g$ is bounded, then $f * g$ is bounded and uniformly continuous.

• If $f , g$ are compactly supported, is it necessarily the case that $f * g$ is compactly supported?

• Show that under any of the following assumptions, $f * g$ vanishes at infinity:

$. \ f , g \in L ^ { 1 }$ are both bounded.

$f , g \in L ^ { 1 }$ with just g bounded.

$f , g$ smooth and compactly supported (and in fact $f * g$ is smooth)

$f \in L ^ { 1 }$ and $g$ smooth and compactly supported (and in fact $f * g$ is smooth)

• Show that if $f \in L ^ { 1 }$ and $g ^ { \prime }$ exists with $\frac { \partial g } { \partial x _ { i } }$ all bounded, then

$$
{ \frac { \partial } { \partial x _ { i } } } \left( f * g \right) = f * { \frac { \partial g } { \partial x _ { i } } }
$$

Fourier Analysis

• Show that if $f \in L ^ { 1 }$ then $\widehat { f }$ is bounded and uniformly continuous.

• Is it the case that $f \in L ^ { 1 }$ implies $\widehat { f } \in L ^ { 1 } \}$

• Show that if $f , \widehat { f } \in L ^ { 1 }$ then f is bounded, uniformly continuous, and vanishes at infinity.

– Show that this is not true for arbitrary $L ^ { 1 }$ functions.

• Show that if $f \in L ^ { 1 }$ and $\widehat { f } = 0$ almost everywhere then $f = 0$ almost everywhere.

– Prove that $\widehat { f } = \widehat { g }$ implies that $f = g \mathrm { ~ a . e ~ }$

• Show that if $f , g \in L ^ { 1 }$ then

$$
\int { \widehat { f } } g = \int f { \widehat { g } } .
$$

Give an example showing that this fails if g is not bounded.

• Show that if $f \in C ^ { 1 }$ then $f$ is equal to its Fourier series.

Approximate Identities

• Show that if $\varphi$ is an approximate identity, then

$$
\| f * \varphi _ { t } - f \| _ { 1 } \stackrel { t \to 0 } { \to } 0 .
$$

– Show that if additionally $| \varphi ( x ) | \leq c ( 1 + | x | ) ^ { - n - \varepsilon }$ for some $c , \varepsilon > 0$ , then this converges is almost everywhere.

• Show that is $f$ is bounded and uniformly continuous and $\varphi _ { t }$ is an approximation to the identity, then $f * \varphi _ { t }$ uniformly converges to $f .$

$L ^ { p }$ Spaces

• Show that if $E \subseteq \mathbb { R } ^ { n }$ is measurable with $\mu ( E ) < \infty$ and $f \in L ^ { p } ( X )$ then

$$
\| f \| _ { L ^ { p } ( X ) } \stackrel { p \to \infty } { \to } \| f \| _ { \infty } .
$$

• Is it true that the converse to the DCT holds? I.e. if $\int f _ { n } \to \int f ;$ , is there a $g \in L ^ { p }$ such that $f _ { n } < g { \mathrm { ~ a . e ~ } }$ . for every n?

• Prove continuity in $L ^ { p } i$ If $f$ is uniformly continuous then for all $p ,$

$$
\| \tau _ { h } f - f \| _ { p } \stackrel { h \to 0 } { \to } 0 .
$$

• Prove the following inclusions of $L ^ { p }$ spaces for $m ( X ) < \infty { : }$

$$
L ^ { \infty } ( X ) \subset L ^ { 2 } ( X ) \subset L ^ { 1 } ( X )
$$

$$
\ell ^ { 2 } ( \mathbb { Z } ) \subset \ell ^ { 1 } ( \mathbb { Z } ) \subset \ell ^ { \infty } ( \mathbb { Z } ) .
$$

## 6.2.5 Unsorted

Proposition 6.2.1(Volumes of Rectangles).

If $\{ R _ { j } \} \ni R$ is a covering of R by rectangles,

$$
R = \prod _ { j } ^ { \circ } R _ { j } \implies | R | = \sum | R | _ { j }
$$

$$
R \subseteq \bigcup _ { j } R _ { j } \implies | R | \leq \sum | R | _ { j } .
$$

• Show that any disjoint intervals is countable.

• Show that every open $U \subseteq \mathbb { R }$ is a countable union of disjoint open intervals.

• Show that every open $U \subseteq \mathbb { R } ^ { n }$ is a countable union of almost disjoint closed cubes.

• Show that that Cantor middle-thirds set is compact, totally disconnected, and perfect, with outer measure zero.

• Prove the Borel-Cantelli lemma.

<!-- image-->

## 6.3 Rectangles

<!-- image-->

<!-- image-->

## 6.4 Outer Measure

<!-- image-->

<!-- image-->

## 6.5 Lebesgue Measurable Sets

<!-- image-->

<!-- image-->

# 6.6 Lebesgue Measurable Functions

<!-- image-->

<!-- image-->

## 7.1 2010 6.1

<!-- image-->

Show that

$$
\int _ { \mathbb { B } ^ { n } } { \frac { 1 } { | x | ^ { p } } } d x < \infty \iff p < n
$$

$$
\int _ { \mathbb { R } ^ { n } \setminus \mathbb { B } ^ { n } } { \frac { 1 } { | x | ^ { p } } } d x < \infty \iff p > n .
$$

## 7.2 2010 6.2

Show that

$$
\int _ { { \mathbb { R } } ^ { n } } | f | = \int _ { 0 } ^ { \infty } m ( A _ { t } ) d t
$$

$$
A _ { t } : = \left\{ x \in \mathbb { R } ^ { n } \mid | f ( x ) | > t \right\} .
$$

## 7.3 2010 6.5

Suppose $F \subseteq \mathbb { R }$ with $m ( F ^ { c } ) < \infty$ and let $\delta ( x ) : = d ( x , F )$ and

$$
I _ { F } ( x ) : = \int _ { \mathbb { R } } { \frac { \delta ( y ) } { \left| x - y \right| ^ { 2 } } } d y .
$$

a. Show that δ is continuous.

b. Show that if $x \in F ^ { c }$ then $I _ { F } ( x ) = \infty$

c. Show that $I _ { F } ( x ) < \infty$ for almost every x

## 7.4 2010 7.1

Let $( X , { \mathcal { M } } , \mu )$ be a measure space and prove the following properties of $L ^ { \infty } ( X , { \mathcal { M } } , \mu )$

• If $f , g$ are measurable on X then

$$
\left\| f g \right\| _ { 1 } \leq \left\| f \right\| _ { 1 } \left\| g \right\| _ { \infty } .
$$

$\| - \| _ { \infty }$ is a norm on $L ^ { \infty }$ making it a Banach space.

$\| f _ { n } - f \| _ { \infty } \stackrel { n \to \infty } { \to } 0 \iff$ there exists an $E \in { \mathcal { M } }$ such that $\mu ( X \backslash E ) = 0$ and $f _ { n }  f$ uniformly on E.

• Simple functions are dense in $L ^ { \infty }$

<table><tr><td></td></tr><tr><td>7.5 2010 7.2</td></tr></table>

Show that for $0 < p < q \leq \infty , \| a \| _ { \ell ^ { q } } \leq \| a \| _ { \ell ^ { p } }$ over C, where $\| a \| _ { \infty } : = \operatorname* { s u p } _ { j } | a _ { j } |$

## 7.6 2010 7.3

Let $f , g$ be non-negative measurable functions on [0, ∞) with

$$
A : = \int _ { 0 } ^ { \infty } f ( y ) y ^ { - 1 / 2 } d y < \infty
$$

$$
B : = \left( \int _ { 0 } ^ { \infty } | g ( y ) | \right) ^ { 2 } d y < \infty .
$$

Show that

$$
\int _ { 0 } ^ { \infty } \left( \int _ { 0 } ^ { \infty } f ( y ) d y \right) { \frac { g ( x ) } { x } } d x \leq A B .
$$

## 7.7 2010 7.4

Let $( X , { \mathcal { M } } , \mu )$ be a measure space and $0 < p < q < \infty$ . Prove that if $L ^ { q } ( X ) \subseteq L ^ { p } ( X )$ , then X does not contain sets of arbitrarily large finite measure.

## 7.8 2010 7.5

Suppose $0 < a < b \leq \infty$ , and find examples of functions $f \in L ^ { p } ( ( 0 , \infty ) )$ if and only if:

$a < p < b$

$a \leq p \leq b$

$p = a$

Hint: consider functions of the following form:

$$
f ( x ) : = x ^ { - \alpha } | \log ( x ) | ^ { \beta } .
$$

Define

$$
F ( x ) : = \left( \frac { \sin ( \pi x ) } { \pi x } \right) ^ { 2 }
$$

$$
G ( x ) : = { \left\{ \begin{array} { l l } { 1 - | x | } & { | x | \leq 1 } \\ { 0 } & { { \mathrm { e l s e } } . } \end{array} \right. }
$$

a. Show that ${ \widehat { G } } ( \xi ) = F ( \xi )$

b. Compute ${ \widehat { F } } .$

c. Give an example of a function $g \not \in L ^ { 1 } ( \mathbb { R } )$ which is the Fourier transform of an $L ^ { 1 }$ function.

Hint: write $\widehat { G } ( \xi ) = H ( \xi ) + H ( - \xi )$ where

$$
H ( \xi ) : = e ^ { 2 \pi i \xi } \int _ { 0 } ^ { 1 } y e ^ { 2 \pi i y \xi } d y .
$$

## 7.10 2010 7.7

Show that for each $\epsilon > 0$ the following function is the Fourier transform of an $L ^ { 1 } ( \mathbb { R } ^ { n } )$ function:

$$
F ( \xi ) : = \left( \frac { 1 } { 1 + \left| \xi \right| ^ { 2 } } \right) ^ { \epsilon } .
$$

Hint: show that

$$
\begin{array} { r l r } {  { K _ { \delta } ( x ) : = \delta ^ { - n / 2 } e ^ { \frac { - \pi | x | ^ { 2 } } { \delta } } } } \\ & { } & { f ( x ) : = \int _ { 0 } ^ { \infty } K _ { \delta } ( x ) e ^ { - \pi \delta } \delta ^ { \epsilon - 1 } d \delta } \\ & { } & { \Gamma ( s ) : = \displaystyle \int _ { 0 } ^ { \infty } e ^ { - t } t ^ { s - 1 } d t } \\ & { } & { \Longrightarrow \widehat { f } ( \xi ) = \displaystyle \int _ { 0 } ^ { \infty } e ^ { - \pi \delta | \xi | ^ { 2 } } e ^ { - \pi \delta } \delta ^ { \epsilon - 1 } = \pi ^ { - s } \Gamma ( \epsilon ) F ( \xi ) . } \end{array}
$$

## 7.11 2010 7 Challenge 1: Generalized Holder

Suppose that

$$
1 \leq p _ { j } \leq \infty ,
$$

$$
\sum _ { j = 1 } ^ { n } { \frac { 1 } { p _ { j } } } = { \frac { 1 } { r } } \leq 1 .
$$

Show that if $f _ { j } \in L ^ { p _ { j } }$ for each $1 \leq j \leq n$ , then

$$
\prod f _ { j } \in L ^ { r } ,
$$

$$
\left\| \prod f _ { j } \right\| _ { r } \leq \prod \| f _ { j } \| _ { p _ { j } } .
$$

## 7.12 2010 7 Challenge 2: Young’s Inequality

Suppose $1 \leq p , q , r \leq \infty$ with

$$
\frac { 1 } { p } + \frac { 1 } { q } = 1 + \frac { 1 } { r } .
$$

Prove that

$$
f \in L ^ { p } , g \in L ^ { q } \implies f * g \in L ^ { r } \mathrm { ~ a n d ~ } \| f * g \| _ { r } \leq \| f \| _ { p } \| g \| _ { q } .
$$

## 7.13 2010 9.1

Show that the set $\{ u _ { k } ( j ) : = \delta _ { i j } \} \subseteq \ell ^ { 2 } ( \mathbb { Z } )$ and forms an orthonormal system.

<!-- image-->

## 7.14 2010 9.2

<!-- image-->

Consider $L ^ { 2 } ( [ 0 , 1 ] )$ and define

$$
\begin{array} { l } { { e _ { 0 } ( x ) = 1 } } \\ { { e _ { 1 } ( x ) = \sqrt { 3 } ( 2 x - 1 ) . } } \end{array}
$$

a. Show that $\{ e _ { 0 } , e _ { 1 } \}$ is an orthonormal system.

b. Show that the polynomial $p ( x )$ where $\deg ( p ) = 1$ which is closest to $f ( x ) = x ^ { 2 } \mathrm { ~ i n ~ } L ^ { 2 } ( [ 0 , 1 ] )$ is given by

$$
h ( x ) = x - { \frac { 1 } { 6 } } .
$$

Compute $\| f - g \| _ { 2 }$

## 7.15 2010 9.3

Let $E \subseteq H$ a Hilbert space.

a. Show that $E \perp \subseteq H$ is a closed subspace.

b. Show that $( E ^ { \bot } ) ^ { \bot } = \mathrm { c l } _ { H } ( E )$

<!-- image-->

## 7.16 2010 9.5b

<!-- image-->

Let $f \in L ^ { 1 } ( ( 0 , 2 \pi ) )$

i. Show that for an $\epsilon > 0$ one can write $f = g + h$ where $g \in L ^ { 2 } ( ( 0 , 2 \pi ) )$ and $\| H \| _ { 1 } < \epsilon .$

<!-- image-->

## 7.17 2010 9.6

<!-- image-->

Prove that every closed convex $K \subset H { \mathrm { ~ a ~ } }$ Hilbert space has a unique element of minimal norm.

<!-- image-->

## 7.18 2010 9 Challenge

<!-- image-->

Let U be a unitary operator on H a Hilbert space, let $M : = \left\{ x \in H \ \left| \ U x = x \right. \right\}$ , let P be the orthogonal projection onto M, and define

$$
S _ { N } : = \frac { 1 } { N } \sum _ { n = 0 } ^ { N - 1 } U ^ { n } .
$$

Show that for all $x \in H$

$$
\| S _ { N } x - P x \| _ { H } \stackrel { N \to \infty } { \to } 0 .
$$

## 7.19 2010 10.1

Let $\nu , \mu$ be signed measures, and show that

$$
\nu \perp \mu \mathrm { ~ a n d ~ } \nu \ll | \mu | \implies \nu = 0 .
$$

<!-- image-->

## 7.20 2010 10.2

<!-- image-->

Let $f \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ with $f \neq 0 .$

a. Prove that there exists a $c > 0$ such that

$$
H f ( x ) \geq { \frac { c } { ( 1 + | x | ) ^ { n } } } .
$$

<!-- image-->

## 7.21 2010 10.3

Consider the function

$$
f ( x ) : = { \left\{ \begin{array} { l l } { \displaystyle { \frac { 1 } { | x | \left( \log \left( { \frac { 1 } { x } } \right) \right) ^ { 2 } } } } & { | x | \leq { \frac { 1 } { 2 } } } \\ { 0 } & { { \mathrm { e l s e } } . } \end{array} \right. }
$$

a. Show that $f \in L ^ { 1 } ( \mathbb { R } )$

b. Show that there exists $\mathrm { ~ a ~ } c > 0$ such that for all $| x | \le 1 / 2$

$$
H f ( x ) \geq { \frac { c } { | x | \log \left( { \frac { 1 } { | x | } } \right) } } .
$$

Conclude that Hf is not locally integrable.

<!-- image-->

## 7.22 2010 10.4

Let $f \in L ^ { 1 } ( \mathbb { R } )$ and let $\mathcal { U } : = \left\{ ( x , y ) \in \mathbb { R } ^ { 2 } \ \Big | \ y > 0 \right\}$ denote the upper half plane. For $( x , y ) \in \mathcal { U }$ define

$$
u ( x , y ) : = f * P y ( x )
$$

$$
{ \mathrm { w h e r e ~ } } P _ { y } ( x ) : = { \frac { 1 } { \pi } } \left( { \frac { y } { t ^ { 2 } + y ^ { 2 } } } \right) .
$$

a. Prove that there exists a constant C independent of $f$ such that for all $x \in \mathbb { R }$

$$
\operatorname* { s u p } _ { y > 0 } | u ( x , y ) | \leq C \cdot H f ( x ) .
$$

Hint: write the following and try to estimate each term:

$$
u ( x , y ) = \int _ { | t | < y } f ( x - t ) P _ { y } ( t ) d t + \sum _ { k = 0 } ^ { \infty } \int _ { A _ { k } } f ( x - t ) P _ { y } ( t ) d t \quad A _ { k } : = \left\{ 2 ^ { k } y \leq | t | < 2 ^ { k + 1 } y \right\} .
$$

b. Following the proof of the Lebesgue differentiation theorem, show that for $f \in L ^ { 1 } ( \mathbb { R } )$ and for almost every $x \in \mathbb { R }$ ,

$$
u ( x , y ) \stackrel { y \to 0 } { \to } f ( x ) .
$$

## 8 Common Inequalities

## 8.1 The GOATs

Proposition 8.1.1(Cauchy-Schwarz Inequality).

$$
| \langle f , \ g \rangle | = \leq \| f \| _ { 2 } \| g \| _ { 2 }
$$

$$
\mathrm { w i t h \ e q u a l i t y } \iff f = \lambda g .
$$

Remark 8.1.2(Different forms of CS): In general, Cauchy-Schwarz relates inner product to norm, and only happens to relate norms in $L ^ { 1 }$ . Some other useful forms:

$$
\left( \sum _ { k = 1 } ^ { n } a _ { k } b _ { k } \right) ^ { 2 } \leq \left( \sum _ { k = 1 } ^ { n } a _ { k } ^ { 2 } \right) \left( \sum _ { k = 1 } ^ { n } b _ { k } ^ { 2 } \right)
$$

$$
\left| \int _ { { \mathbb R } ^ { n } } f ( x ) { \overline { { g ( x ) } } } d x \right| ^ { 2 } \leq \int _ { { \mathbb R } ^ { n } } | f ( x ) | ^ { 2 } d x \int _ { { \mathbb R } ^ { n } } | g ( x ) | ^ { 2 } d x .
$$

Proposition 8.1.3(Reverse Triangle Inequality).

$$
| \| x \| - \| y \| | \leq \| x - y \| .
$$

Proposition 8.1.4(Holder’s Inequality).

$$
{ \frac { 1 } { p } } + { \frac { 1 } { q } } = 1 \implies \| f g \| _ { 1 } \leq \| f \| _ { p } \| g \| _ { q } .
$$

With integrals:

$$
\int _ { X } | f g | \leq \left( \int _ { X } | f | ^ { p } \right) ^ { \frac { 1 } { p } } \left( \int _ { X } | f | ^ { q } \right) ^ { \frac { 1 } { q } } .
$$

Proof (of Holder’s inequality).

It suffices to show this when $\left\| f \right\| _ { p } = \left\| g \right\| _ { q } = 1$ , since

$$
\| f g \| _ { 1 } \leq \| f \| _ { p } \| f \| _ { q } \Longleftrightarrow \int { \frac { | f | } { \| f \| _ { p } } } { \frac { | g | } { \| g \| _ { q } } } \leq 1 .
$$

Using $A B \leq { \frac { 1 } { p } } A ^ { p } + { \frac { 1 } { q } } B ^ { q } .$ , we have

$$
\int | f | | g | \leq \int { \frac { | f | ^ { p } } { p } } { \frac { | g | ^ { q } } { q } } = { \frac { 1 } { p } } + { \frac { 1 } { q } } = 1 .
$$

Example 8.1.5(Application of Holder’s inequality: containment of $L ^ { p }$ spaces): For finite measure spaces,

$$
1 \leq p < q \leq \infty \implies L ^ { q } \subset L ^ { p } \quad ( { \mathrm { ~ a n d ~ } } \ell ^ { p } \subset \ell ^ { q } ) .
$$

Proof (of containment of $L ^ { p }$ spaces).

Fix $p , q ,$ let $r = { \frac { q } { p } }$ and $s = { \frac { r } { r - 1 } } \ \mathrm { s o } \ r ^ { - 1 } + s ^ { - 1 } = 1$ . Then let $h = | f | ^ { p } \colon$

$$
\| f \| _ { p } ^ { p } = \| h \cdot 1 \| _ { 1 } \leq \| 1 \| _ { s } \| h \| _ { r } = \mu ( X ) ^ { \frac { 1 } { s } } \| f \| _ { \ell } ^ { \frac { q } { r } } \implies \| f \| _ { p } \leq \mu ( X ) ^ { \frac { 1 } { p } - \frac { 1 } { q } } \| f \| _ { q } .
$$

Note: doesn’t work for $\ell _ { p }$ spaces, but just note that $\sum | x _ { n } | < \infty \implies x _ { n } < 1$ for large enough $n ,$ and $t h u s p < q \Longrightarrow | x _ { n } | ^ { q } \leq | x _ { n } | ^ { q } .$

Proposition 8.1.6(Bessel’s Inequality).

For $x \in H$ a Hilbert space and $\{ e _ { k } \}$ an orthonormal sequence,

$$
\sum _ { k = 1 } ^ { \infty } \| \langle x , e _ { k } \rangle \| ^ { 2 } \leq \| x \| ^ { 2 } .
$$

Note that this does not need to be a basis.

## Proposition 8.1.7(Parseval’s Identity).

Equality in Bessel’s inequality, attained when $\{ e _ { k } \}$ is a basis, i.e. it is complete, i.e. the span of its closure is all of H. This states that if $\{ e _ { k } \}$ is an orthonormal basis for H, then

$$
\sum _ { k \geq 0 } | \langle x , \ e _ { k } \rangle | ^ { 2 } = \| x \| _ { H } ^ { 2 } .
$$

Remark 8.1.8: This appears in several other forms:

$$
{ \frac { 1 } { 2 \pi } } \int _ { ( - \pi , \pi ) } | f | ^ { 2 } = \sum _ { k \in \mathbb { Z } } | c _ { k } | ^ { 2 }
$$

$$
c _ { k } : = { \frac { 1 } { 2 \pi } } \int _ { ( - \pi , \pi ) } f ( x ) e ^ { - i k x } d x .
$$

Proposition 8.1.9(Plancherel).

$$
\| f \| _ { L ^ { 2 } } ^ { 2 } = \left\| \widehat { f } \right\| _ { L ^ { 2 } }
$$

$$
\int _ { \mathbb { R } ^ { d } } \left| f \right| ^ { 2 } = \int _ { \mathbb { R } ^ { d } } \left| { \widehat { f } } \right| ^ { 2 } .
$$

## 8.2 Less common

## Proposition 8.2.1(Markov/Chebyshev’s Inequality).

The most often used form here:

$$
\mu \left( f ^ { - 1 } \left( ( \alpha , \infty ) \right) \right) : = \mu \left( \left\{ x \in X \Big \vert | f ( x ) | > \alpha \right\} \right) \leq \frac { 1 } { \alpha } \| f \| _ { 1 } : = \frac { 1 } { \alpha } \int _ { X } | f | .
$$

Proof: let $S _ { \alpha }$ be the set appearing, then $\alpha \mu ( S _ { \alpha } )$ is the sum of areas of certain boxes below the graph of $f .$ Interpret $\int _ { X } f$ as the total area under the graph to make the inequality obvious.

<!-- image-->

The probability interpretation: $\mathbb { P } ( X \geq \alpha ) \leq { \frac { 1 } { \alpha } } \mathbb { E } ( X )$

The more general version:

$$
\mu \left( f ^ { - 1 } \left( ( \alpha , \infty ) \right) \right) : = \mu \left( \left\{ x \in X \biggm | | f ( x ) | > \alpha \right\} \right) \leq \frac { 1 } { \alpha ^ { p } } \| f \| _ { p } ^ { p } : = \frac { 1 } { \alpha ^ { p } } \int _ { X } | f | ^ { p } .
$$

Proof:

$$
\| f \| _ { p } ^ { p } = \int | f | ^ { p } \geq \int _ { S _ { \alpha } } | f | ^ { p } \geq \alpha ^ { p } \int _ { S _ { \alpha } } 1 = \alpha ^ { p } \mu ( S _ { \alpha } ) .
$$

Proposition 8.2.2(Minkowski’s Inequality).

$$
1 \leq p < \infty \implies \| f + g \| _ { p } \leq \| f \| _ { p } + \| g \| _ { p } .
$$

Remark 8.2.3: This does not handle $p = \infty$ case. Use to prove $L ^ { p }$ is a normed space.

Proof (of Minkowski’s inequality).

• We first note

$$
| f + g | ^ { p } = | f + g | | f + g | ^ { p - 1 } \leq \left( | f | + | g | \right) | f + g | ^ { p - 1 } .
$$

• Note that if $p , q$ are conjugate exponents then

$$
{ \frac { 1 } { q } } = 1 - { \frac { 1 } { p } } = { \frac { p - 1 } { p } }
$$

$$
q = { \frac { p } { p - 1 } } .
$$

• Then taking integrals yields

$$
\begin{array} { r l } { \| f - \theta \| _ { \infty } ^ { 3 } - \int \| f - \theta \| ^ { \prime } } & { = \theta ^ { \prime } , } \\ & { \leq \int \int \| f - \theta \| ^ { \prime } \| ^ { \prime } ( \frac { \theta } { \theta } ) ^ { \epsilon } ( \theta ^ { \prime } + \theta ^ { \prime \prime } ) ^ { \epsilon } } \\ & { - \int | ( \eta \| \cdot \| \rho \| ^ { \epsilon } ) ^ { \epsilon } ( 1 ) ^ { \epsilon } ( \frac { \theta } { \theta } ) ^ { \epsilon } ( \eta \| f - \theta ^ { \prime \prime } ) ^ { \epsilon } ( \frac { \theta } { \theta } ) ^ { \epsilon } ( \theta ^ { \prime } - \theta ^ { \prime \prime } ) } \\ & { - ( | f - \phi | ^ { \prime } | \frac { \theta } { \theta } ) ^ { \epsilon } ( \frac { \theta } { \theta } ) ^ { \epsilon } ( \theta ^ { \prime } + \theta ^ { \prime } ) ^ { 2 } \Big | _ { \epsilon } } \\ & { \leq \| \eta \| _ { \infty } ^ { \epsilon } \| ( \theta ^ { \prime } + \eta ^ { \prime \prime } ) ^ { \epsilon } \| _ { \epsilon } + \| \theta \| _ { \infty } ^ { \epsilon } \| \frac { \theta } { \theta } \| _ { \infty } ^ { 2 } ( \theta ^ { \prime } - \theta ^ { \prime \prime } ) \| _ { \epsilon } } \\ & { - ( | ( \eta _ { 1 } , \epsilon ) | _ { \infty } ^ { 2 } | | \theta ^ { \prime } | ^ { \prime } | ^ { \epsilon } | \phi ^ { \prime \prime } | ^ { \epsilon } ) | \ \epsilon \| _ { \infty } ^ { 2 } } \\ &  = ( | ( \eta _ { 1 } , \epsilon ) | \epsilon | ^ { \prime \prime } | \epsilon ^ { 2 } | \epsilon ^ { 2 } ) ( \int | f - \theta ^ { \prime \prime } | ^ { \prime \prime } )  \end{array}
$$

• Cancelling common terms yields

$$
\begin{array} { c } { 1 \leq \left( \left\| f \right\| _ { p } + \left\| g \right\| _ { p } \right) \displaystyle \frac { 1 } { \left\| f + g \right\| _ { p } } } \\ { \Longrightarrow \left\| f + g \right\| _ { p } \leq \left\| f \right\| _ { p } + \left\| g \right\| _ { p } . } \end{array}
$$

Proposition 8.2.4(Young’s Inequality).

$$
{ \frac { 1 } { p } } + { \frac { 1 } { q } } = { \frac { 1 } { r } } + 1 \implies \| f * g \| _ { r } \leq \| f \| _ { p } \| g \| _ { q }
$$

Remark 8.2.5(some useful special cases):

$$
\left\| f \ast g \right\| _ { 1 } \leq \left\| f \right\| _ { 1 } \left\| g \right\| _ { 1 }
$$

$$
\| f \ast g \| _ { p } \leq \| f \| _ { 1 } \| g \| p ,
$$

$$
\left\| f \ast g \right\| _ { \infty } \leq \left\| f \right\| _ { 2 } \left\| g \right\| _ { 2 }
$$

$$
\left\| f \ast g \right\| _ { \infty } \leq \left\| f \right\| _ { p } \left\| g \right\| _ { q } .
$$

## 8.3 Inequalities that appear in proofs

Proposition 8.3.1(AM-GM Inequality).

$$
{ \sqrt { a b } } \leq { \frac { a + b } { 2 } } .
$$

Proposition 8.3.2(Jensen’s Inequality).

$$
f ( t x + ( 1 - t ) y ) \leq t f ( x ) + ( 1 - t ) f ( y ) .
$$

Proposition 8.3.3(Young’s Product Inequality).

$$
A B \leq \frac { A ^ { p } } { p } + \frac { B ^ { q } } { q } .
$$

Proposition 8.3.4(?).

$$
( a + b ) ^ { p } \leq 2 ^ { p - 1 } ( a ^ { p } + b ^ { p } ) .
$$

Proposition 8.3.5(Bernoulli’s Inequality).

$$
( 1 + x ) ^ { n } \geq 1 + n x \quad x \geq - 1 , { \mathrm { ~ o r ~ } } n \in 2 \mathbb { Z } { \mathrm { ~ a n d ~ } } \forall x .
$$

As a consequence,

$$
1 - x \leq e ^ { - x } .
$$

Proposition 8.3.6(Exponential Inequality).

$$
\forall t \in \mathbb { R } , \quad 1 + t \leq e ^ { t } .
$$

Proof .

• It’s an equality when $t = 0$

$$
\bullet \ \frac { \partial } { \partial t } { 1 + t } < \frac { \partial t } { \partial e } ^ { \bar { t } } \iff t < 0
$$

Proposition 8.3.7(Young’s Convolution Inequality).

$$
{ \frac { 1 } { r } } : = { \frac { 1 } { p } } + { \frac { 1 } { q } } - 1 \implies \| f * g \| _ { r } \leq \| f \| _ { p } \| g \| q .
$$
