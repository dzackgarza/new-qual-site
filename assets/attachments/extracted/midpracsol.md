1. Let $E \subset \mathbb { R }$ be bounded, nonempty, and suppose sup $E \notin E .$ . Show that E is infinite. If E were finite, $E = \{ x _ { 1 } , \ldots , x _ { n } \}$ , then sup E would be the largest of $x _ { 1 } , \ldots , x _ { n }$ , and would belong to $E .$

(Or: assume $a = \operatorname* { s u p } E \notin E .$ , and choose $x _ { 1 } \in E$ . Then $x _ { 1 } < a ,$ so $x _ { 1 }$ is not an upper bound for E, so E contains $x _ { 2 } > x _ { 1 }$ . Again, $x _ { 2 } < a _ { }$ , so $x _ { 2 }$ is not an upper bound for E, so E contains $x _ { 3 } > x _ { 2 }$ . Proceeding by induction, we construct infinitely many distinct elements $x _ { n } \in E )$

2. Let $U , V \subset \mathbb { R } ^ { 2 }$ be open subsets satisfying $\bar { U } = \mathbb { R } ^ { 2 } , \bar { V } = \mathbb { R } ^ { 2 }$ . Prove that $\overline { { U \cap V } } = \mathbb { R } ^ { 2 }$ (Hint: if $E \subset X$ then ${ \bar { E } } = X$ if and only if every non-empty open set in X has non-empty intersection with E).

Using the hint: given a non-empty open subset $G \subset \mathbb { R } ^ { 2 } , G \cap U$ is non-empty (since U is dense) and open (G and U are open); so $( G \cap U ) \cap V = G \cap ( U \cap V )$ is non-empty (since V is dense). So every non-empty open subset of $\mathbb { R } ^ { 2 }$ intersects $U \cap V$ , so $U \cap V$ is dense in $\mathbb { R } ^ { 2 }$

(Proof of the hint: recall ${ \bar { E } } = X$ if and only if $\forall x \in X , \forall r > 0 , N _ { r } ( x )$ intersects E. First assume every non-empty open set in X intersects E, then $\forall x \in X , \forall r > 0 , N _ { r } ( x )$ is open and non-empty so $N _ { r } ( x )$ intersects E, which proves that ${ \bar { E } } = X$ . Conversely, ${ \bar { E } } = X$ and assume $G \subset X$ is open and non-empty. Take $x \in G$ : then x is interior of G, so there exists $r > 0$ such that $N _ { r } ( x ) \subset G$ Since $N _ { r } ( x )$ intersects $E ,$ we deduce that G also intersects E.)

Solution without using the hint: let $\boldsymbol { x } \in \mathbb { R } ^ { 2 }$ , and let $r > 0$ . We have to prove that $N _ { r } ( x )$ intersects $U \cap V$ (which shows that $x \in { \overline { { U \cap V } } } )$ . First, since $x \in { \bar { U } } = X$ , we know that $N _ { r } ( x )$ intersects $U ;$ let $y \in N _ { r } ( x ) \cap U$ . Since U and $N _ { r } ( x )$ are open, so is $N _ { r } ( x ) \cap U$ , so there exists $r ^ { \prime } > 0$ such that $N _ { r ^ { \prime } } ( y ) \subset N _ { r } ( x ) \cap U$ . Since $y \in { \bar { V } } = X$ , we know that $N _ { r ^ { \prime } } ( y )$ intersects V . Let $z \in N _ { r ^ { \prime } } ( y ) \cap V$ . Since $N _ { r ^ { \prime } } ( y ) \subset N _ { r } ( x ) \cap U$ , we have $z \in ( U \cap V ) \cap N _ { r } ( x )$ . Therefore $U \cap V$ intersects all neighborhoods of x, and so $x \in { \overline { { U \cap V } } }$ .

## 3. If A and B are compact subsets of X, show that $A \cup B$ is compact.

Let $\{ G _ { \alpha } \}$ be an open cover of $A \cup B \colon$ : then $\cup G _ { \alpha } \supset A$ , and A is compact, so there exist $\alpha _ { 1 } , \ldots , \alpha _ { n }$ such that $G _ { \alpha _ { 1 } } \cup \cdots \cup G _ { \alpha _ { n } } \supset A$ . Similarly, there exist $\alpha _ { 1 } ^ { \prime } , \ldots , \alpha _ { m } ^ { \prime }$ such that $G _ { \alpha _ { 1 } ^ { \prime } } \cup \dots \cup G _ { \alpha _ { m } ^ { \prime } } \supset B$ Then $G _ { \alpha _ { 1 } } \cup \cdots \cup G _ { \alpha _ { n } } \cup G _ { \alpha _ { 1 } ^ { \prime } } \cup \cdots \cup G _ { \alpha _ { m } ^ { \prime } }$ is a finite subcover of $A \cup B$ .

4. Let $\{ x _ { n } \}$ be a sequence satisfying $\textstyle | x _ { n } | \leq { \frac { 1 } { 3 ^ { n } } }$ for each $n \geq 1$ . Put $y _ { n } = x _ { 1 } + \cdots + x _ { n } ,$ Prove that the sequence $\left\{ y _ { n } \right\}$ is convergent.

The series $\sum { \frac { 1 } { 3 ^ { n } } }$ is convergent, so by the comparison criterion (Theorem $3 . 2 5 ) \sum x _ { n }$ is convergent. $\begin{array} { r l } { \left( \mathrm { O r } \colon } & { { } \{ y _ { n } \} \right. } \end{array}$ is a Cauchy sequence since, for $m \geq n \geq N , \ | y _ { m } - y _ { n } | = | x _ { n + 1 } + \cdot \cdot \cdot + x _ { m } | \leq$ $\begin{array} { r } { \frac { 1 } { 3 ^ { n + 1 } } + \cdot \cdot \cdot + \frac { 1 } { 3 ^ { m } } \leq \frac { 1 } { 3 ^ { n + 1 } } ( 1 + \frac 1 3 + \frac 1 9 + \cdot \cdot \cdot ) = \frac 3 2 \frac { 1 } { 3 ^ { n + 1 } } \leq \frac 3 2 \frac { 1 } { 3 ^ { N + 1 } } } \end{array}$ , which can be made smaller than any $\epsilon > 0$ by taking N large enough.)

5. Find all the subsequential limits of each of the following sequences: $\begin{array} { r } { a _ { n } = n \sin { \frac { n \pi } { 4 } } } \end{array}$ ; $\begin{array} { r } { a _ { n } = 1 - \frac { ( - 1 ) ^ { n } } { n } ; a _ { n } = 1 - ( - 1 ) ^ { n } } \end{array}$ . Are these sequences bounded? convergent?

a) Observe that $a _ { n } = 0$ if n is a multiple of 4; $a _ { n } = \pm n$ if $n = 4 k + 2$ for some integer k; $a _ { n } = \pm n / \sqrt { 2 }$ if n is odd. Therefore 0 is a subsequential limit (take $\left\{ { { a } _ { 4 k } } \right\} )$ , and it is the only finite subsequential limit of $\left\{ a _ { n } \right\}$ since the non-zero terms all satisfy $| a _ { n } | \geq n / \sqrt { 2 } ;$ there are also subsequences which diverge to +∞ or $\mathrm { t o \mathrm { ~ - \infty } }$ . The sequence is not bounded, and not convergent.

b) $\begin{array} { r } { | a _ { n } - 1 | = \frac { 1 } { n } \to 0 } \end{array}$ , so $a _ { n } \to 1$ . The sequence is bounded and convergent, and all its subsequences converge to 1.

c) $a _ { n }$ equals 0 for even n, and 2 for odd $n ,$ so the subsequential limits are 0 and 2. The sequence is bounded but not convergent.

6. Let $\left\{ a _ { n } \right\}$ and $\left\{ b _ { n } \right\}$ be bounded sequences in R. Prove that lim $\operatorname* { s u p } ( a _ { n } + b _ { n } ) \ \leq$ lim sup $a _ { n } +$ lim sup $b _ { n }$ . Give an example to show that equality need not hold.

Let $a ^ { * } = \operatorname* { l i m } \operatorname* { s u p } a _ { n }$ and $b ^ { * } = \operatorname* { l i m } \operatorname* { s u p } b _ { n }$ , and fix $\epsilon > 0$ Then all but finitely many terms of $\left\{ a _ { n } \right\}$ satisfy $a _ { n } < a ^ { * } + \epsilon ,$ and all but finitely many terms of $\left\{ b _ { n } \right\}$ satisfy $b _ { n } < b ^ { * } + \epsilon$ (Theorem $3 . 1 7 ( \mathrm { b } ) )$ . Hence, there exists N such that $a _ { n } + b _ { n } < a ^ { * } + b ^ { * } + 2 \epsilon$ for all $n \geq N$ . This implies that lim $\operatorname* { s u p } ( a _ { n } + b _ { n } ) \leq a ^ { * } + b ^ { * } + 2 \epsilon$ . Since this holds for all $\epsilon > 0 .$ , we must have lim s $\textstyle \operatorname { l p } ( a _ { n } + b _ { n } ) \leq a ^ { * } + b ^ { * }$ .

Equality need not hold: let $a _ { n } = ( - 1 ) ^ { n } , b _ { n } = - ( - 1 ) ^ { n }$ , then lim sup $a _ { n } =$ lim sup $b _ { n } = 1$ , but $a _ { n } + b _ { n } = 0$ so lim sup $( a _ { n } + b _ { n } ) = 0 < 1 + 1$

7. Find a countable subset of R with (a) exactly two limit points; (b) countably many limit points; (c) uncountably many limit points.

a) $A = \{ \textstyle { \frac { 1 } { n } } , \ n = 1 , 2 , \dots \} \cup \{ 1 + { \frac { 1 } { n } } , \ n = 1 , 2 , \dots \}$ (the limit points are 0 and 1).

b) $\begin{array} { r } { A = \{ \frac { 1 } { m } + \frac { 1 } { n } , ~ m , n = 1 , 2 , \dots \} } \end{array}$ (the limit points are 0 and all the $\textstyle { \frac { 1 } { n } } )$

c) $A = \mathbb { Q }$ (all real numbers are limit points).

8. Let A, B be subsets of a metric space, and denote by $A ^ { \circ } , B ^ { \circ }$ the sets of interior points of A, B. Prove that $( A \cap B ) ^ { \circ } = A ^ { \circ } \cap B ^ { \circ }$

If $x \in ( A \cap B ) ^ { \circ }$ then x is an interior point of $A \cap B , { \mathrm { i . e . ~ } } \exists r > 0$ such that $N _ { r } ( x ) \subset A \cap B$ Then $N _ { r } ( x ) \subset A$ , so $x \in A ^ { \circ }$ , and $N _ { r } ( x ) \subset B$ , so $x \in B ^ { \circ }$ . Therefore $x \in A ^ { \circ } \cap B ^ { \circ }$ . This proves $( A \cap B ) ^ { \circ } \subset A ^ { \circ } \cap B ^ { \circ }$ Conversely, let $x \in A ^ { \circ } \cap B ^ { \circ }$ Since x is an interior point of $A , \exists r _ { 1 } > 0$ such that $N _ { r _ { 1 } } ( x ) \subset A ;$ similarly x is an interior point of B so $\exists r _ { 2 } > 0$ such that $N _ { r _ { 2 } } ( x ) \subset B$ . Let $r = \operatorname* { m i n } \{ r _ { 1 } , r _ { 2 } \}$ . Then $N _ { r } ( x ) \subset A \cap B$ . So $x \in ( A \cap B ) ^ { \circ }$ , so $A ^ { \circ } \cap B ^ { \circ } \subset ( A \cap B ) ^ { \circ }$

(Or, using results seen in lecture: $A ^ { \circ } \subset A , B ^ { \circ } \subset B$ are open, so $A ^ { \circ } \cap B ^ { \circ }$ is open and contained in $A \cap B ,$ , which implies that $A ^ { \circ } \cap B ^ { \circ } \subset ( A \cap B ) ^ { \circ }$ Conversely, $( A \cap B ) ^ { \circ }$ is open and contained in $A ,$ so it is contained in $A ^ { \circ } ;$ similarly it is open and contained in $B ,$ so contained in $B ^ { \circ }$ ; so $( A \cap B ) ^ { \circ } \subset A ^ { \circ } \cap B ^ { \circ } )$ .

9. Assume that $\sum a _ { n }$ is a convergent series and that $a _ { n } \geq 0 \forall n \geq N$ . Prove that $\sum { \frac { 1 } { n } } { \sqrt { a _ { n } } }$ converges. (Hint: consider the quantity $( { \sqrt { a _ { n } } } - { \frac { 1 } { n } } ) ^ { 2 }$ , and use the comparison criterion).

(Assigned on homework).

10. Give an example of a countable compact subset of $( \mathbb { R } , d )$

$\textstyle \{ { \frac { 1 } { n } } , \ n = 1 , 2 , \ldots \} \cup \{ 0 \}$ (closed and bounded, hence compact; see also Problem set 3).

11. True or false?

– if a subset $A \subset \mathbb { R }$ has a least upper bound in R then it also has a greatest lower bound in R;

False. Consider $\mathrm { e . g . \ ( - \infty , 0 ) }$

– if E is a finite subset of a metric space $( X , d )$ then E is closed in $X { \mathrm { ; } }$

True. E has no limit points, so all limit points of E belong to E.

– if K is a compact subset of a metric space $( X , d )$ and $F \subset X$ is closed in $X$ , then $K \cap F$ is closed in X.

True. K is closed in X (Theorem 2.34), so $K \cap F$ is closed. (In fact $K \cap F$ is even compact, by Theorem 2.35).

12. Let E be an open subset of $\mathbb { R } ^ { 2 }$ . Is every point of E a limit point of E? Same question if E is closed.

Let $x \in E$ , then x is an interior point of E, hence there is $r _ { 0 } > 0$ such that $N _ { r _ { 0 } } ( x ) \subset E$ Hence, for all $r > 0 , N _ { r } ( x ) \cap E \supset N _ { r } ( x ) \cap N _ { r _ { 0 } } ( x ) = N _ { \mathrm { m i n } ( r , r _ { 0 } ) } ( x )$ contains points other than x. (Note: this need not be true in a general metric space $( X , d )$ , it could be that this neighborhood contains no other point, if x is an isolated point of X! However, in $\mathbb { R } ^ { k }$ neighborhoods are uncountable). Hence x is a limit point of E.

This property does not hold for closed E: for example $E = \{ 0 \}$ is closed, but 0 is not a limit point of $E .$

13. If $s _ { 1 } = { \sqrt { 2 } } .$ , and $s _ { n + 1 } = \sqrt { 2 + s _ { n } } ~ ( n = 1 , 2 , 3 , \ldots )$ ), prove that $\left\{ s _ { n } \right\}$ converges, and that $s _ { n } < 2$ for all n. (Hint: show that $\left\{ s _ { n } \right\}$ is a monotonic sequence).

First, $s _ { 1 } = \sqrt { 2 } < s _ { 2 } = \sqrt { 2 + \sqrt { 2 } } < 2$ . By induction we prove that $s _ { n } < s _ { n + 1 } < 2$ for all n: assume that $s _ { n - 1 } < s _ { n } < 2$ , then $2 + s _ { n - 1 } < 2 + s _ { n } < 4$ , so $\sqrt { 2 + s _ { n - 1 } } < \sqrt { 2 + s _ { n } } < 2$ , i.e. $s _ { n } < s _ { n + 1 } < 2$ . This proves that $s _ { n } < 2$ for all $n ,$ and that $\left\{ s _ { n } \right\}$ is monotonically increasing. Since $\left\{ s _ { n } \right\}$ is monotonic and bounded, it converges.

14. Find lim sup $s _ { n }$ and lim inf $s _ { n } .$ where $\left\{ s _ { n } \right\}$ is the sequence defined by $s _ { 1 } = 0 , s _ { 2 m } =$ ${ \begin{array} { c } { { \frac { s _ { 2 m - 1 } } { 2 } } , { s _ { 2 m + 1 } } = { \frac { 1 } { 2 } } + { s _ { 2 m } } } \end{array} }$

The first few terms are: $0 , 0 , { \frac { 1 } { 2 } } , { \frac { 1 } { 4 } } , { \frac { 3 } { 4 } } , { \frac { 3 } { 8 } } , { \frac { 7 } { 8 } } , \ldots .$ Consider the odd terms: $s _ { 2 m + 1 } = { \textstyle \frac { 1 } { 2 } } + s _ { 2 m } =$ $\begin{array} { r } { \frac { 1 } { 2 } + \frac { 1 } { 2 } s _ { 2 m - 1 } = \frac { 1 } { 2 } ( 1 + s _ { 2 m - 1 } ) } \end{array}$ . By induction, $\begin{array} { r } { s _ { 2 m + 1 } = 1 - \frac { 1 } { 2 ^ { m } } } \end{array}$ , and $s _ { 2 m + 1 } \to 1$ . Moreover, $s _ { 2 m } =$ $\textstyle { \bar { \frac { 1 } { 2 } } } s _ { 2 m - 1 } = { \frac { 1 } { 2 } } ( 1 - { \frac { 1 } { 2 ^ { m - 1 } } } ) = { \frac { 1 } { 2 } } - { \frac { 1 } { 2 ^ { m } } }$ , and $s _ { 2 m } \to \frac { 1 } { 2 }$ . So lim inf $\begin{array} { r } { s _ { n } = \frac { 1 } { 2 } } \end{array}$ and lim sup $s _ { n } = 1$

15. Suppose $\left\{ p _ { n } \right\}$ is a Cauchy sequence in a metric space X, and some subsequence $\{ p _ { n _ { k } } \}$ converges to a point $p \in X$ . Prove that the full sequence $\left\{ p _ { n } \right\}$ converges to $p .$

Let $\epsilon > 0$ There exists N such that, for $n , m \ge N , d ( p _ { n } , p _ { m } ) < \epsilon$ Then, consider any $n \geq N ;$ for k sufficiently large (so that $n _ { k } \geq N )$ , $d ( p _ { n } , p _ { n _ { k } } ) < \epsilon$ . Taking the limit as $k  \infty$ , it follows that $d ( p _ { n } , p ) \leq \epsilon$ . Or: if k is sufficiently large then $d ( p _ { n _ { k } } , p ) < \epsilon$ (by the assumption $p _ { n _ { k } }  p )$ , so $d ( p _ { n } , p ) \leq d ( p _ { n } , p _ { n _ { k } } ) + d ( p _ { n _ { k } } , p ) < 2 \epsilon$ . In any case, we conclude that $d ( p _ { n } , p )$ becomes arbitrarily small for n large, i.e. $p _ { n } \to p$