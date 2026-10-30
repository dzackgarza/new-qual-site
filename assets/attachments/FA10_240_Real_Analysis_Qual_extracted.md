September 10, 2010

## Qualifying Exam in Real Analysis

Instructions. You may use without proof anything which is proved in the text by Folland or other standard reference. Either state the theorem by name, if it has one, or say what the theorem says. However, you must reprove items which were given as exercises. Unless indicated otherwise, $( X , { \mathcal { M } } , \mu )$ is a measure space. The measure on subsets of R is assumed to be Lebesgue.

1 (90 pts.). For each of the following, determine if the statement is true (always) or false (not always true). If true, give a brief proof, citing appropriate theorem(s); if false, give a counterexample or prove it is false in some other rigorous way. No credit if reason or counterexample is wrong.

(a) Any bounded sequence in a Banach space has a convergent subsequence.

(b) There exists a sequence of functions $f _ { n } \in L ^ { 1 } ( [ 0 , 1 ] )$ such that $f _ { n }$ converges to 0 in $L ^ { 1 }$ , but there is no subsequence $f _ { n _ { k } }$ that converges pointwise to 0 a.e.

(c) The space $C ( [ 0 , 1 ] )$ is dense in $L ^ { \infty } ( [ 0 , 1 ] )$

(d) The sequence $e ^ { i 2 \pi n x }$ converges to 0 weakly in $L ^ { 2 } ( [ 0 , 1 ] )$

(e) Let $a _ { j } \in \mathbb { R } , j = 1 , \dots , n$ , and $\begin{array} { r } { \frac { 1 } { p } + \frac { 1 } { q } = 1 , 1 < p < \infty } \end{array}$ . Then

$$
\sum _ { j = 1 } ^ { n } a _ { j } \leq n ^ { 1 / p } \big ( \sum _ { j = 1 } ^ { n } | a _ { j } | ^ { q } \big ) ^ { 1 / q }
$$

(f) Let $Y = \{ f : \mathbb { R } \to [ - \pi , \pi ] \}$ . Let $[ - \pi , \pi ]$ have its natural topology, and give Y the weakest topology such that the mappings $p _ { r } : Y \to [ - \pi , \pi ]$ defined by $p _ { r } ( f ) : = f ( r )$ are continuous for all $r \in \mathbb { R }$ . Then $Y$ is compact.

2. (20 pts.) Let $f \in L ^ { 1 } ( \mathbb { R } )$ . Prove that the function

$$
g ( y ) = \int _ { \mathbb { R } } \sin ( y ^ { 2 } x ) \ f ( x ) d x
$$

is continuous and bounded on $\mathbb { R } .$

3. (25 pts.) Recall that a measure µ is semifinite if for all $E \in { \mathcal { M } }$ with $\mu ( E ) > 0$ there exists $A \in { \mathcal { M } }$ $A \subset E$ such that $0 < \mu ( A ) < \infty$ . If $\mu$ is semifinite, prove that for all $E \in { \mathcal { M } }$

$$
\mu ( E ) = \operatorname* { s u p } \{ \mu ( A ) : A \in { \mathcal { M } } , A \subseteq E , \mu ( A ) < \infty \} .
$$

4. (30 pts.) Let Y be a closed subspace of $L ^ { 2 } ( [ 0 , 1 ] )$ each of whose elements may be represented by a continuous function on [0, 1]. Prove that there exists $C > 0$ so that

$$
\| f \| _ { L ^ { \infty } ( [ 0 , 1 ] ) } \le C \| f \| _ { L ^ { 2 } ( [ 0 , 1 ] ) }
$$

for all $f \in Y$

5. (35 pts.) Recall that a bounded linear operator $T : { \mathcal { H } } \to { \mathcal { H } } .$ on a Hilbert space ${ \mathcal { H } } ,$ is self-adjoint if $\langle T v , w \rangle = \langle v , T w \rangle$ for all vectors $v , w \in \mathcal { H }$

(a) Suppose that T is a bounded self-adjoint operator such that $\| v \| \leq \| T v \|$ for all $v \in \mathcal { H }$ . Show that given any $y \in \mathcal { H }$ , there exists $x \in \mathcal { H }$ such that $T x = y$ . (Hint: Prove first that the range of $T$ is a closed subspace of $\mathcal { H } . )$

(b) Give an example of an injective bounded self-adjoint linear operator T in a Hilbert space H for which the equation $T x = y$ does not always have a solution.

(c) Can an example for (b) exist on a finite dimensional Hilbert space H?