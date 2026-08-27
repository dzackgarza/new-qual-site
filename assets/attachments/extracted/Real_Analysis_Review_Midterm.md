## MAT 320 Practice for Midterm 2 with Solutions

Remark. If you are comfortable with all of the following problems, you will be well prepared for Midterm 2.

Exam Policies. You must show up on time for all exams. Please bring your student ID card: ID cards may be checked, and students may be asked to sign a picture sheet when turning in exams. Other policies for exams will be announced / repeated at the beginning of the exam.

If you have a university-approved reason for taking an exam at a time different than the scheduled exam (because of a religious observance, a student-athlete event, etc.), please contact your instructor as soon as possible. Similarly, if you have a documented medical emergency which prevents you from showing up for an exam, again contact your instructor as soon as possible.

All exams are closed notes and closed book. Once the exam has begun, having notes or books on the desk or in view will be considered cheating and will be referred to the Academic Judiciary.

It is not permitted to use cell phones, calculators, laptops, MP3 players, Blackberries or other such electronic devices at any time during exams. If you use a hearing aid or other such device, you should make your instructor aware of this before the exam begins. You must turn off your cell phone, etc., prior to the beginning of the exam. If you need to leave the exam room for any reason before the end of the exam, it is still not permitted to use such devices. Once the exam has begun, use of such devices or having such devices in view will be considered cheating and will be referred to the Academic Judiciary. Similarly, once the exam has begun any communication with a person other than the instructor or proctor will be considered cheating and will be referred to the Academic Judiciary.

## Review Topics.

Definitions. Please know all of the following definitions. Monotone Sequence. Nondecreasing / Nonincreasing Sequence. Bounded Sequence. Limit Supremum / Limit Infimum. Cauchy Sequence. Subsequence. Subsequential Limit. Metric Space and Distance Function. Ball of Radius  Centered at $x _ { 0 }$ in a Metric Space. Sequence, Subsequence, Boundedness, Convergence, Cauchy Sequence in a Metric Space. Complete Metric Space. Interior of a Subset of a Metric Space. Open Subset / Closed Subset of a Metric Space. Closure of a Subset of a Metric Space. Boundary of a Subset of a Metric Space. Decreasing Sequence of Closed Bounded Subsets of a Metric Space. Open Cover / Subcover of an Open Cover. Compactness. Series. Convergence of a

Series / Divergence of a Series. Absolute Convergence of a Series. Geometric Series. Cauchy Criterion for Convergence of a Series. Continuity at $x _ { 0 }$ for a Real-Valued Function. Continuous Function / Discontinuous Function.

Results. Please know all of the following lemmas, propositions, theorems and corollaries.

Monotone Convergence Theorem. Every bounded monotone sequence of real numbers converges. Every unbounded monotone sequence either diverges to +∞ or diverges to −∞.

Test for Convergence Via Lim Inf and Lim Sup. A bounded sequence of real numbers converges if and only if the lim inf equals the lim sup, in which case both equal the limit of the sequence.

Cauchy Convergence Theorem. A sequence of real numbers converges if and only if it is a Cauchy sequence.

Convergence and Subsequences. Every subsequence of a convergent sequence converges to the same limit as the original sequence.

Subsequential Limits and Lim Inf / Lim Sup. Every subsequential limit is bounded below by lim inf and bounded above by lim sup. If lim inf is finite, resp. if lim sup is finite, then it is the limit of a monotone subsequence.

Bolzano-Weierstrass Theorem. Every bounded sequence of real numbers has a convergent subsequence.

Convergence in a Product Metric Space. A sequence of elements of $\mathbb { R } ^ { k }$ converges with the Euclidean metric if and only if each of the k component sequences converges in R.

Cauchy Convergence Theorem for $\mathbb { R } ^ { k }$ . Every Cauchy sequence in $\mathbb { R } ^ { k }$ (with the Euclidean metric) converges. Said differently, $\mathbb { R } ^ { k }$ with the Euclidean metric is a complete metric space.

Bolzano-Weierstrass Theorem for $\mathbb { R } ^ { k }$ . Every bounded sequence in $\mathbb { R } ^ { k }$ (with the Euclidean metric) has a convergent subsequence.

Axioms for a Topology. For a metric space $( S , d )$ , the empty set and S are both open subsets. The intersection of any finite collection of open subsets is an open subset. The union of any collection of open subsets is an open subset. Equivalently, both the empty set and S are closed subsets, the union of finitely many closed subsets is a closed subset, and the intersection of an arbitrary collection of closed subsets is a closed subset.

Interiors and Closures. For a subset T of a metric space $( S , d )$ , the interior of T equals the maximal open subset of S that is contained in T . The closure of T equals the minimal closed subset of S that contains T . In particular, S is open if and only if S equals its interior, resp. S is closed if and only if S equals its closure.

Countable Compactness and Sequential Compactness. For every metric space $( S , d )$ that satisfies the Bolzano-Weierstrass theorem (i.e., bounded, closed subsets are “sequentially compact”), every decreasing sequence of nonempty, bounded, closed subsets has nonempty intersection (i.e., bounded, closed subsets are “countably compact”).

Heine-Borel Theorem. Every bounded metric space $( S , d )$ that satisfies the Bolzano-Weierstrass theorem is compact: every open covering has a finite subcovering. In particular, every bounded, closed subset of $\mathbb { R } ^ { k }$ is compact.

Geometric Series Test. For $a \neq 0$ , the geometric series $\textstyle \sum _ { n = 0 } ^ { \infty } a r ^ { n }$ converges if and only $\mathrm { i f } \left| r \right| < 1$ in which case it converges absolutely.

p-Series Test. For $p > 0$ , the series $\scriptstyle \sum _ { n = 1 } ^ { \infty } ( 1 / n ^ { p } )$ converges if and only if $p > 1$

Cauchy Criterion for Convergence. A series converges if and only if the sequence of partial sums is a Cauchy sequence.

Comparison Test. A series that is bounded above termwise in absolute value by a convergent series is also convergent. A nonnegative series that is bounded below by a divergent nonnegative series is also divergent.

Ratio Test. A series of nonzero real numbers is absolutely convergent if the lim sup of the absolute values of successive ratios is less than 1. The series diverges if the lim inf of the absolute values of the successive ratios is greater than 1.

Root Test. A series $\textstyle \sum _ { n = 0 } ^ { \infty } a _ { n }$ is absolutely convergent if lim sup $\sqrt [ n ] { \left| a _ { n } \right| }$ is less than 1. The series diverges if lim sup $\sqrt [ n ] { \left| a _ { n } \right| }$ is greater than 1.

Integral Test. If $f ( x ) , x > 0$ is an integrable function such that $f ( x ) \geq a _ { n } \geq 0$ for every $n \in \mathbb { N }$ and for every $x \in [ n - 1 , n ]$ , and if $\textstyle \int _ { x = 0 } ^ { \infty } f ( x ) d x$ converges, then also $\textstyle \sum _ { n = 0 } ^ { \infty } a _ { n }$ converges and is bounded above by the improper integral. Conversely, if $a _ { n } \geq f ( x ) \geq 0$ for every $n \in \mathbb N$ and for every $x \in [ n - 1 , n ]$ , and if $\textstyle \int _ { x = 0 } ^ { \bar { \infty } } f ( x ) d { \bar { x } }$ diverges, then also $\textstyle \sum _ { n = 0 } ^ { \infty } a _ { n }$ diverges.

Alternating Series Test. For a nondecreasing sequence $\left( a _ { n } \right)$ of nonnegative real numbers, the alternating series $\textstyle \sum ( - 1 ) ^ { n } a _ { n }$ converges if and only if $\left( a _ { n } \right)$ converges to 0.

Sequential Convergence and Convergence. A function f defined at $x _ { 0 }$ satisfies the $\epsilon - \delta$ definition of continuity if and only if it satisfies the sequential definition of continuity.

Properties of Continuous Functions. The class of continuous functions (defined on a specified set, continuity measured at a specified point) is preserved by absolute values, scaling, sum, difference, product, and nonzero division. The composition of continuous functions is continuous.

Extremal Value Theorem. Every bounded, closed subset of R has a maximum, and it has a minimum. Every continuous, real-valued function defined on a compact set has a maximum value and a minimum value on that compact set.

Intermediate Value Theorem. Every continuous function defined on a bounded, closed interval takes on every value between its maximum value and its minimum value.

Strictly Increasing Functions. A strictly increasing function defined on an interval is continuous if and only if the image is an interval. In this case, the inverse function is also continuous.

Please review all of the homework exercises on Sections 10 - 18. In addition the following theoretical problems are good practice.

## Practice Problems.

(1) For a sequence of real numbers, if every monotone subsequence converges to a common limit, prove that the sequence converges to that limit.

Solution to (1) For a sequence $( s _ { n } ) _ { n \in \mathbb { N } }$ , if $( s _ { n } ) _ { n \in \mathbb { N } }$ is not bounded above, then there exists a monotone subsequence $\left( s _ { \overline { { n } } _ { k } } \right)$ that is not bounded above: define $\overline { { n } } _ { 1 }$ to be the smallest integer $n \in \mathbb { N }$ such that $s _ { \overline { { n } } _ { 1 } } ~ > ~ 1$ , and for every integer $k \in \mathbb N$ , recursively define $\overline { { n } } _ { k + 1 }$ to be the smallest integer $n \in \mathbb { N }$ such that $s _ { n } > \operatorname* { m a x } \{ k , s _ { 1 } , . . . , s _ { \overline { { n } } _ { k } } \}$ . Yet every convergent sequence is bounded above. Thus, if every monotone subsequence converges then $( s _ { n } ) _ { n \in \mathbb { N } }$ is bounded above. By a similar argument, also $( s _ { n } ) _ { n \in \mathbb { N } }$ is bounded below. In particular, since the sequence is bounded, both lim sup $s _ { n }$ and lim inf $s _ { n }$ are defined.

There exists a monotone subsequence $\left( { { s } _ { \overline { { { n } } } _ { k } } } \right)$ that converges to lim sup $s _ { n }$ . Similarly, there exists a monotone sequence $( s _ { \underline { { n } } _ { k } } )$ that converges to lim inf $s _ { n }$ . Thus, since these monotone sequences converge to a common limit, then lim sup $s _ { n }$ equals lim inf $s _ { n }$ . Therefore the bounded sequence $( s _ { n } ) _ { n \in \mathbb { N } }$ converges to the common limit lim $s _ { n } = \operatorname* { l i m } \operatorname* { s u p } s _ { n } = \operatorname* { l i m } \operatorname* { i n f } s _ { n }$

(2) Prove that every subsequence of a Cauchy sequence (in a specified metric space) is a Cauchy sequence. Prove that every subsequence of a convergent sequence is a convergent sequence, and the limits are equal.

Solution to (2) For a sequence $( s _ { n } ) _ { n \in \mathbb { N } }$ , a subsequence is a sequence of the form $( s _ { n _ { k } } ) _ { k \in \mathbb { N } }$ for a strictly increasing sequence of natural numbers $1 \leq n _ { 1 } < n _ { 2 } < n _ { 3 } < . . .$ . For every integer $k \in \mathbb N$ by induction on $k , n _ { k }$ is at least as large as k.

First, let $( s _ { n } ) _ { n \in \mathbb { N } }$ be a sequence that converges to s. Let $( s _ { n _ { k } } ) _ { k \in \mathbb { N } }$ be a subsequence. For every $\epsilon > 0$ , since $( s _ { n } ) _ { n \in \mathbb { N } }$ converges, there exists $N \in  { \mathbb { N } }$ such that for every $n \in \mathbb { N }$ with $n \geq N , | s _ { n } - s |$ is less than . For every $k \in \mathbb N$ with $k \geq N$ , since $n _ { k }$ is at least as large as $k _ { : }$ , in particular $n _ { k } \geq N$ Therefore, $| s _ { n _ { k } } - s |$ is less than . Thus $( s _ { n _ { k } } ) _ { k \in \mathbb { N } }$ converges to s.

Next, let $( s _ { n } ) _ { n \in \mathbb { N } }$ be a Cauchy sequence. For every $\epsilon > 0$ , there exists $N \in  { \mathbb { N } }$ such that for every $m , n \in \mathbb { N }$ with $m \geq N$ and with $n \geq N , \vert s _ { n } - s _ { m } \vert$ is less than . For every $k , l \in  { \mathbb { N } }$ with $k \geq N$ and with $l \geq N$ then $n _ { k } \ge k \ge N$ and $n _ { l } \ge l \ge N$ . Therefore, $| s _ { n _ { k } } - s _ { n _ { l } } |$ is less than . Thus $( s _ { n _ { k } } ) _ { k \in \mathbb { N } }$ is a Cauchy sequence.

(3) For a metric space $( S , d )$ and a subset C, if C with its induced metric is a complete metric space, prove that C is a closed subset of S.

Solution to (3) Recall that a subset C of a metric space is a closed subset if and only if for every sequence $( c _ { n } ) _ { n \in \mathbb { N } }$ of elements $c _ { n } \in C$ that converges to an element s as a sequence in S, then, in fact, s is an element of C. As a convergent sequence in S, $( c _ { n } ) _ { n \in \mathbb { N } }$ is a Cauchy sequence in S. Thus, considered as a sequence in C with its induced metric, $( c _ { n } ) _ { n \in \mathbb { N } }$ is a Cauchy sequence in C. Since C is a complete metric space, $( c _ { n } ) _ { n \in \mathbb { N } }$ converges to an element of C. A sequence can converge to at most one limit (with respect to a given metric function), and thus the limit in C equals s. Therefore s is an element of C, and C is a closed subset of S.

(4) Give an example of a sequence of real numbers such that no subsequence is convergent. Prove your answer.

Solution to (4) Let $( s _ { n } ) _ { n \in \mathbb { N } }$ be a sequence. Let R be any positive real number. Consider the subset $A _ { R } \subset \mathbb { N }$ of integers n such that $| s _ { n } | \leq R$ . If $A _ { R }$ is infinite, say $\{ n _ { 1 } , n _ { 2 } , n _ { 3 } , . . . \}$ with $1 \leq n _ { 1 } < n _ { 2 } < . . . .$ then the subsequence $( s _ { n _ { k } } ) _ { n _ { k } \in A _ { R } }$ is a bounded sequence. Thus, by Bolzano-Weierstrass, this bounded sequence has a convergent subsequence. In particular, $( s _ { n } ) _ { n \in \mathbb { N } }$ has a convergent subsequence.

Conversely, if $( s _ { n _ { k } } ) _ { k \in \mathbb { N } }$ is a convergent subsequence, then it is bounded, i.e., there exists a positive real number R such that $\{ n _ { k } | k \in \mathbb { N } \}$ is an infinite subset of $A _ { R }$ . Therefore, the sequence $( s _ { n } ) _ { n \in \mathbb { N } }$ has a convergent subsequence if and only if $A _ { R }$ is infinite for some positive real number R. Contrapositively, $( s _ { n } ) _ { n \in \mathbb { N } }$ has no convergent subsequence if and only if, for every positive real number $R , A _ { R }$ is a finite set.

There are many such sequences. The simplest are the unbounded, strictly increasing (respectively strictly decreasing) sequences, e.g., $( s _ { n } ) _ { n \in \mathbb { N } } = ( n ) _ { n \in \mathbb { N } }$ and the like. However, any sequence $( s _ { n } ) _ { n \in \mathbb { N } }$ such that $( | s _ { n } | ) _ { n \in \mathbb { N } }$ is unbounded and strictly increasing gives another example, e.g., $( s _ { n } ) _ { n \in \mathbb { N } } =$ $( ( - 1 ) ^ { n } n ) _ { n \in \mathbb { N } }$

(5) For a metric space $( S , d )$ and complete subsets $C , C ^ { \prime }$ , prove that the union $C \cup C ^ { \prime }$ is again complete. For every collection $\left( C _ { i } \right)$ of complete subsets, prove that the common intersection $\cap _ { i } C _ { i }$ is complete.

Solution to (5) Let C and $C ^ { \prime }$ be complete subsets of $( S , d )$ . Let $( c _ { n } ) _ { n \in \mathbb { N } }$ be a Cauchy sequence of elements $c _ { n } \in C \cup C ^ { \prime }$ . Thus, for every $n \in \mathbb N$ , either $c _ { n }$ is in C or $c _ { n }$ is in $C ^ { \prime }$ (or both). Define $A \subset \mathbb { N }$ to be the set of n such that $c _ { n } \in C$ , and define $A ^ { \prime } \subset \mathbb { N }$ to be the set of n such that $c _ { n } \in C ^ { \prime }$ Then $A \cup A ^ { \prime }$ equals N, so that at least one of A or A0 is infinite. Without loss of generality, assume that A is infinite, say $A = \{ n _ { 1 } , n _ { 2 } , n _ { 3 } , . . . \}$ with $1 \leq n _ { 1 } < n _ { 2 } < n _ { 3 } < . . . .$

The sequence $( c _ { n _ { k } } ) _ { n _ { k } \in A }$ is a subsequence of $( c _ { n } ) _ { n \in \mathbb { N } }$ that is a Cauchy sequence in C. Since C is complete, this Cauchy sequence converges to an element c in C. A Cauchy sequence converges if and only if at least one of its subsequences converges, and then the limits are (necessarily) equal. Thus, the entire sequence $( c _ { n } ) _ { n \in \mathbb { N } }$ also converges to the element c in C. Since c is an element in $C \cup C ^ { \prime }$ , the Cauchy sequence converges to an element in $C \cup C ^ { \prime }$ . A similar argument applies in case A0 is infinite. Thus, in both cases, the Cauchy sequence $( c _ { n } ) _ { n \in \mathbb { N } }$ converges to an element in $C \cup C ^ { \prime }$ Therefore $C \cup C ^ { \prime }$ is a complete metric space.

Next, let $( c _ { n } ) _ { n \in \mathbb { N } }$ be a Cauchy sequence of elements $c _ { n } \in \cap _ { i } C _ { i }$ . For every i, since every $c _ { n }$ is in $C _ { i } .$ the entire sequence $( c _ { n } ) _ { n \in \mathbb { N } }$ is a Cauchy sequence in $C _ { i }$ . Since $C _ { i }$ is complete, the Cauchy sequence converges to a limit $c ,$ and that limit c is in $C _ { i }$ . Since the limit of a convergent sequence is unique, the limit c is in $C _ { i }$ for every i. Thus c is in $\cap _ { i } C _ { i }$ . So the Cauchy sequence $( c _ { n } ) _ { n \in \mathbb { N } }$ converges to an element c in $\cap _ { i } C _ { i }$ . Therefore $\cap _ { i } C _ { i }$ is complete.

Here is a different proof of this. Since every complete subset of a metric space is a closed subset, and since every intersection of closed subsets is a closed subset, also $\cap _ { i } C _ { i }$ is a closed subset of S. For any particular $i , \cap _ { i } C _ { i }$ is a subset of $C _ { i }$ that is closed in S, hence closed in $C _ { i }$ . Every closed subset of a complete metric space is complete. Since $C _ { i }$ is a complete metric space, the closed subset $\cap _ { i } C _ { i }$ is also a complete metric space.

(6) For a metric space $( S , d )$ , prove that every compact subset is a closed subset. For compact subsets $C , C ^ { \prime }$ , prove that the union $C \cup C ^ { \prime }$ is again compact. For every collection (Ci) of compact subsets, prove that the common intersection $\cap _ { i } C _ { i }$ is a compact subset.

Solution to (6) Let C be a compact subset of $( S , d )$ There are two proofs that C is a closed subset of $S .$ . First, because of Heine-Borel, every sequence in C has a subsequence that converges to an element in C. In particular, every Cauchy sequence has a convergent subsequence, and thus the entire Cauchy sequence converges to an element in C. Thus C is complete, and hence C is a closed subset of S.

There is also a proof that does not (explicitly) use Heine-Borel, but instead uses the definition of compactness in terms of finite subcovers of (infinite) open covers. The goal is to prove that C is a closed subset, or, equivalently, to prove that the complement $S \backslash C$ is an open subset. Let $s \in S \backslash C$ be any point. For every $n \in \mathbb { N }$ , consider the closed subset

$$
{ \overline { { B } } } _ { 1 / n } ( s ) : = \{ t \in S | d ( t , s ) \leq 1 / n \} .
$$

This is closed because the distance function is continuous (using the triangle inequality). Thus the complement $S \setminus \overline { { B } } _ { 1 / n } ( s )$ is an open subset of S,

$$
S \setminus \overline { { B } } _ { 1 / n } ( s ) : = \{ t \in S | d ( t , s ) > 1 / n \} .
$$

For every $c \in C ,$ since $c \neq s$ , by the positive definiteness of the metric function, also $d ( c , s )$ is positive. Thus, by the Archimedean property of R, there exists $n \in \mathbb { N }$ such that $d ( c , s ) > 1 / n$ , i.e., c is in the open subset $S \setminus \overline { { B } } _ { 1 / n } ( s )$ . Therefore the collection of open subsets $( S \setminus \overline { { B } } _ { 1 / n } ( s ) ) _ { n \in \mathbb { N } }$ is an infinite open cover of C.

Since C is compact, this infinite open cover of C has a finite subcover. Since these open subsets are pairwise nested, among the finitely many opens in this finite subcover, there is a single open that contains C, i.e., C is contained in $S \setminus \overline { { B } } _ { 1 / n } ( s )$ for some $n \in \mathbb { N }$ . In particular C is disjoint from $\overline { { B } } _ { 1 / n } ( s )$ . Thus C is disjoint from the interior, i.e., the usual open ball $B _ { 1 / n } ( s )$ . Thus $B _ { 1 / n } ( s )$ is contained in $S \backslash C$ . Since for every s in $S \backslash C$ there exists $n \in \mathbb { N }$ with $B _ { 1 / n } ( s )$ contained in ${ \cal { S } } \backslash { \cal { C } }$ , it follows that $S \backslash C$ is an open subset of S. Hence the complement, $C ,$ is a closed subset of S. (This second proof easily adapts to any “Hausdorff” topological space.)

Next, let $C$ and $C ^ { \prime }$ be two compact subset of S. Let $( U _ { i } ) _ { i \in I }$ be an open covering of $C \cup C ^ { \prime }$ . In particular, it is an open covering of C. Thus, since C is compact, there exists a finite subset $J \subset I .$ such that already the finite collection of open sets $( U _ { i } ) _ { i \in J }$ covers C. Similarly, since $C ^ { \prime }$ is compact, there exists a finite subset $J ^ { \prime } \subset I$ , such that $( U _ { i } ) _ { i \in J ^ { \prime } }$ covers $C ^ { \prime }$ . Since both J and $J ^ { \prime }$ are finite, also the union $J \cup J ^ { \prime }$ is finite. Thus $( U _ { i } ) _ { i \in J \cup J ^ { \prime } }$ is a finite open cover of $C \cup C ^ { \prime }$ . Since every open covering of $C \cup C ^ { \prime }$ has a finite subcovering, $C \cup C ^ { \prime }$ is a compact subset of S.

Finally, let $( C _ { i } ) _ { i \in I }$ be any collection of compact subsets of S. By the argument above, every $C _ { i }$ is a closed subset of S. The intersection of an arbitrary collection of closed subset is a closed subset, hence $\cap _ { i \in I } C _ { i }$ is a closed subset of S. For any particular $i ,$ it is also contained in $C _ { i }$ , hence it is a closed subset of $C _ { i }$ . Therefore, as a closed subset of a compact metric space, $\cap _ { i \in I } C _ { i }$ is also a compact metric space.

(7) For a metric space $( S , d )$ and subsets A, B, prove that $( A \cup B ) ^ { - }$ equals $A ^ { - } \cup B ^ { - }$ Give an example proving that $( A \cap B ) ^ { - }$ may be strictly contained in $A ^ { - } \cap B ^ { - }$ . Similarly, prove that the interior of $A \cap B$ equals the intersection $A ^ { o } \cap B ^ { o }$ , yet the interior of $A \cup B$ may strictly contain $A ^ { o } \cup B ^ { o }$

Solution to (7) The set A− is a closed subset of S that contains A, and the set B− is a closed subset of S that contains B. The union of two closed subsets is a closed subset. Thus $A ^ { - } \cup B ^ { - }$ is a closed subset of S that contains $A \cup B$ . Since $( A \cup B ) ^ { - }$ is the minimal closed subset of S (with respect to set inclusion) that contains $A \cup B$ , it follows that $A ^ { - } \cup B ^ { - }$ contains $( A \cup B ) ^ { - }$

On the other hand, $( A \cup B )$ − is a closed subset of S that contains $A \cup B$ , and hence contains the subset A of $A \subset B$ . Since $A ^ { - }$ is the minimal closed subset of S that contains A, it follows that $( A \cup B )$ − contains A−. By a similar argument, also $( A \cup B )$ contains B−. Thus, since $( A \cup B )$ contains both A− and B−, also $( A \cup B )$ − contains $A ^ { - } \cup B ^ { - }$ −. Since we have both inclusions, (A∪B)− equals $A ^ { - } \cup B ^ { - }$ as subsets of S.

For an example where $( A \cap B ) ^ { - }$ is strictly contained in $A ^ { - } \cap B ^ { - }$ , let S be $\mathbb { R } .$ , and let d be the usual metric, $d ( x , y ) = | x - y |$ . Let A be $\mathbb { Q }$ and let B be $\mathbb { R } \setminus \mathbb { Q }$ . By the density of the rationals, $\mathbb { Q } ^ { - }$ equals R. Similarly, $( \mathbb { R } \setminus \mathbb { Q } )$ − equals R. Thus $A ^ { - } \cap B$ − equals R $\cap \mathbb { R } = \mathbb { R }$ . On the other hand, $A \cap B$ is the empty set, so that $( A \cap B ) ^ { - }$ equals ∅. Therefore $( A \cap B ) ^ { - }$ is strictly contained in $A ^ { - } \cap B ^ { - }$

For every subset E of S, the interior $E ^ { o }$ equals $S \setminus ( S \setminus E ) ^ { - }$ . In particular, by De Morgan’s Laws, $E ^ { o } \cap F ^ { o }$ equals $S \setminus [ ( S \setminus E ) ^ { - } \cup ( S \setminus F ) ^ { - } ]$ . By the argument above, $( S \setminus E ) ^ { - } \cup ( S \setminus F ) ^ { - }$ equals $[ ( S \setminus E ) \cup ( S \setminus F ) ] ^ { - }$ . Finally, by De Morgan’s Laws once more, $( S \setminus E ) \cup ( S \setminus F )$ equals $S \setminus ( E \cap F )$ Therefore $E ^ { o } \cap F ^ { o }$ equals $S \setminus [ S \setminus ( E \cap F ) ] ^ { - } , { \mathrm { i . e . , ~ } } E ^ { o } \cap F ^ { o }$ equals $( E \cap F ) ^ { o }$

For an example where $A ^ { o } \cup B ^ { o }$ is strictly contained in $( A \cup B ) ^ { o }$ , let S be R with the usual metric, let E be $\mathbb { Q } .$ , and let F be $\mathbb { R } \setminus \mathbb { Q }$ . Then $E ^ { o }$ and $F ^ { o }$ are both empty, so that $E ^ { o } \cup F ^ { o }$ equals ∅. On the other hand, $E \cup F$ equals S, so that $( E \cup F ) ^ { o }$ equals S.

(8) If a series of nonnegative real numbers $\textstyle \sum _ { n = 0 } ^ { \infty } a _ { n }$ converges, prove that also the series $\textstyle \sum _ { n = 0 } ^ { \infty } a _ { n } ^ { 2 }$ converges. Does the series $\textstyle \sum _ { n = 0 } ^ { \infty } { \sqrt { a _ { n } } }$ necessarily converge?

Solution to (8) Since the series $\textstyle \sum _ { n = 0 } ^ { \infty } a _ { n }$ converges, by the Cauchy criterion, for every $\epsilon > 0$ there exists an integer $N \in  { \mathbb { N } }$ such that for every pair of integers m, l with $\begin{array} { r } { l \geq m \geq N , \vert \sum _ { n = m } ^ { l } a _ { n } \vert } \end{array}$ is less than . In particular, taking $\epsilon = 1$ and taking $l = m$ , there exists an integer $N \in  { \mathbb { N } }$ such that for every $m \ge N , 0 \le a _ { m } < 1$ . Thus, by the order axioms, also $0 \leq a _ { m } ^ { 2 } < a _ { m } < 1$ Therefore the series $\textstyle \sum _ { n = N } ^ { \infty } a _ { n } ^ { 2 }$ is bounded by the convergent series $\textstyle \sum _ { n = N } ^ { \infty } a _ { n }$ . By the Comparison Test, the series $\textstyle \sum _ { n = N } ^ { \infty } { a _ { n } ^ { 2 } }$ is convergent. Since the tail of the series is convergent, the entire series $\textstyle \sum _ { n = 0 } ^ { \infty } a _ { n } ^ { 2 }$ is convergent.

For a convergent series $\textstyle \sum _ { n = 0 } ^ { \infty } a _ { n }$ , the series $\textstyle \sum _ { n = 0 } ^ { \infty } a _ { n }$ need not converge. One example is the series $\textstyle \sum _ { n = 0 } ^ { \infty } ( 1 / n ^ { 2 } )$ , which converges to $\zeta ( 2 ) = \pi ^ { 2 } / 6$ , although the associated series $\textstyle \sum _ { n = 0 } ^ { \infty } ( 1 / n )$ , i.e., the harmonic series, diverges to ∞ by comparison to the divergent improper integral $\scriptstyle \int _ { x = 1 } ^ { x = \infty } ( 1 / x ) d x$

(9) For a series $\left( a _ { n } \right)$ , if the series $\textstyle \sum _ { n = 1 } ^ { \infty } a _ { n }$ converges, does it necessarily follow that for every subsequence $a _ { n _ { k } }$ , the series $\textstyle \sum _ { k = 1 } ^ { \infty } a _ { n _ { k } }$ converges? $\textstyle \operatorname { I f } \sum _ { n = 1 } ^ { \infty } a _ { n }$ converges absolutely, does $\textstyle \sum _ { k = 1 } ^ { \infty } a _ { n _ { k } }$ converge absolutely?

Solution to (9) First, let $( a _ { n } ) _ { n \in \mathbb { N } }$ be a sequence such that the series $\textstyle \sum _ { n = 1 } ^ { \infty } a _ { n }$ that converges absolutely. Let $( a _ { n _ { k } } ) _ { k \in \mathbb { N } }$ be any subsequence. Define $( b _ { n } ) _ { n \in \mathbb { N } }$ to be the sequence such that $b _ { n }$ equals $a _ { n }$ if n equals $n _ { k }$ for some $k \in \mathbb N$ , or else $b _ { n }$ equals 0. Then for every $n \in \mathbb { N } , | b _ { n } |$ is at most $\left| a _ { n } \right|$ Thus, by the Comparison Test, also the series $\sum _ { n = 1 } ^ { \infty } b _ { n }$ converges absolutely. Of course $\textstyle \sum _ { n = 1 } ^ { \infty } b _ { n }$ is the same as the series $\textstyle \sum _ { k = 1 } ^ { \infty } a _ { n _ { k } }$ , hence the series $\textstyle \sum _ { k = 1 } ^ { \infty } a _ { n _ { k } }$ converges absolutely.

On the other hand, for a series $\textstyle \sum _ { n = 1 } ^ { \infty } a _ { n }$ that converges conditionally, for a subsequence $( a _ { n _ { k } } ) _ { k \in \mathbb { N } }$ the series $\textstyle \sum _ { k = 1 } ^ { \infty } a _ { n _ { k } }$ need not converge. For instance, for the alternating harmonic series $( a _ { n } ) _ { n \in \mathbb { N } } =$ $( ( - 1 ) ^ { n } / n ) _ { n \in \mathbb { N } }$ , the series $\scriptstyle \sum _ { n = 1 } ^ { \infty } ( - 1 ) ^ { n } / n$ does converge conditionally. Yet for the subsequence $( a _ { 2 } , a _ { 4 } , a _ { 6 } , \dots )$ , the associated series is $\textstyle \sum _ { k = 1 } ^ { \infty } ( - 1 ) ^ { 2 k } / 2 { \bar { k } } = 2 \sum _ { k = 1 } ^ { \infty } 1 / k$ , and this diverges.

(10) For a continuous function f defined on R, if f is constant on the terms of a convergent sequence, prove that f takes the same value at the limit of the sequence. Conclude that if f is constant on a set T , then f is also constant on the closure T − of T .

Solution to (10) Let f be constant with value c on the convergent sequence $( s _ { n } ) _ { n \in \mathbb { N } }$ Denote the limit of the sequence by s. Since f is continuous, the inverse image of every open subset is an open subset. Combined with De Morgan’s Laws, also the inverse image of every closed subset is a closed subset. Since the singleton set {c} is closed, the inverse image $f ^ { - 1 } ( \{ c \} )$ is a closed subset. Since this subset contains $( s _ { n } ) _ { n \in \mathbb { N } }$ , also this subset contains the limit s. Thus f (s) equals c.