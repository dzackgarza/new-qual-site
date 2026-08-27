# MATH 140A: FOUNDATIONS OF REAL ANALYSIS I SUMMARY OF KEY FACTS FOR EXAM 2

TODD KEMP

Throughout, reference numbers (like Definition 2.18 and Proposition 2.21) refer to the course lecture notes, also available on the website.

lim sup, lim inf, and the Extended Reals R

(1) Definition of lim sup and lim inf (Definition 2.18).

(2) The limit exists iff lim sup = lim inf (Proposition 2.21).

(3) The lim sup is the largest subsequential limit; the lim inf is the smallest subsequential limit (Theorem 2.24).

(4) The Bolzano-Weierstrass Theorem (Theorem 2.25): every bounded subsequence in R contains a convergent subsequence.

(5) The extended real numbers $\overline { { \mathbb { R } } } = \mathbb { R } \cup \{ \pm \infty \}$

## Complex Numbers

(1) Construction of C using matrices (Definition 3.7).

(2) Definition and properties of the complex modulus (Definition 3.9 and Lemma 3.10).

(3) Convergent and Cauchy sequences in C (Definition 3.11 and Theorem 3.12).

(4) Convergence and Cauchy in terms of Real and Imaginary parts (Proposition 3.13).

(5) Cauchy completeness (Theorem 3.14) and Bolzano-Weierstrass theorem (Theorem 3.15).

## Series

(1) Definition and convergence (Definition 4.2).

(2) Geometric series (Example 4.3).

(3) Harmonic series (Example 4.5).

(4) Cauchy criterion for convergence (Proposition 4.6).

(5) If $\sum a _ { n }$ converges then $a _ { n } \to 0$ (Corollary 4.7).

(6) Comparison test (Theorem 4.8).

(7) Lacunary series (Proposition 4.10); $\sum { \frac { 1 } { n ^ { p } } }$ converges iff $p > 1$ (Example 4.11).

(8) Root test (Theorem 4.12) and Ratio test (Theorem 4.15).

(9) The number e (Example 4.19, Lemma 4.20, Proposition 4.21).

(10) Absolute convergence (Definition 4.22); implies convergence (Lemma 4.23).

(11) Alternating series test (Proposition 4.24).

(12) Alternating harmonic series (Example 4.25).

(13) Rearrangements (Theorem 4.26).

## Metric Spaces

(1) Definition of a metric (Definition 5.1).

(2) p-metrics on $\mathbb { R } ^ { n }$ and $\mathbb { C } ^ { n }$ for $1 \leq p \leq \infty$ (Example 5.2(3)).

(3) Discrete metrics (Example 5.2(6)).

(4) Balls (Definition 5.3).

(5) Convergent and Cauchy sequences in a metric space (Definition 5.5).

(6) Limit points and isolated points (Definition 5.7).

(7) Closed sets (Definition 5.9); in terms of closure under limits (Proposition 5.11).

(8) Open sets (Definition 5.12).

(9) Balls are open sets (Proposition 5.14).

(10) A set is open iff its complement is closed (Proposition 5.15).

(11) Closure, interior, and boundary (Definition 5.17).

(12) Compact sets (Definition 5.22).

## Some Useful Hints.

(1) If $\alpha \neq A \subset \mathbb { R }$ is bounded above and $\alpha \in \mathbb { R }$ , to show that α = sup A it is necessary and sufficient to show two things: that α is an upper bound for A, and given any $x < \alpha$ there is some element $a \in A$ with $a \geq x .$ . Similarly, if A is bounded below and $\beta \in \mathbb { R }$ , to show $\beta = \operatorname { i n f } A$ it is necessary and sufficient to show two things: that $\beta$ is a lower bound for A, and given any $y > \beta$ there is some element $b \in A$ with $b \leq y$

(2) If $\emptyset \neq A \subset \mathbb { R }$ is bounded above and $\alpha = \operatorname* { s u p } A .$ , there exists an increasing sequence $a _ { n } \in A$ such that $a _ { n } \to \alpha$ . Similarly, if A is bounded below and $\beta = \operatorname { i n f } A$ , there exists a decreasing sequence $b _ { n } \in A$ such that $b _ { n } \to \beta$

(3) Statements about sup and inf, or about lim sup and lim inf, can be (carefully!) interchanged by multiplying by $- 1 \colon \operatorname* { s u p } ( - E ) = - \operatorname* { i n f } ( E )$ , and lim su $\operatorname { l p } ( - a _ { n } ) = - \operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } a _ { n }$ n→∞

(4) The Root test and Ratio test are not subtle tools. They essentially work by comparison to a geometric series, which converges or diverges fast. They can be useful for analyzing series whose terms have complicated expressions; but series that either converge or diverge slowly will fall under the “no information” case in these tests.

(5) Typically, the only property of a putative metric that is difficult to verify is the triangle inequality. This is no accident: by far the most important and most commonly used property of metrics is the triangle inequality.

(6) This is one of the rare times when it pays to do rote memorization in mathematics. You should have the definitions of limit point, isolated point, interior, closure, boundary, closed, open at your fingertips.