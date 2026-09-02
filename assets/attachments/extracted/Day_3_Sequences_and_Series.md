## Day 3: Sequences and series

Relevant information. A metric space $( X , d )$ is called complete if every Cauchy sequence in X converges in X. For a real-valued sequence $\{ a _ { k } \}$ the limit superior and inferior are given by

$$
\operatorname* { l i m } _ { n \to \infty } a _ { n } = \operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } \{ a _ { k } : k \geq n \}
$$

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } a _ { n } = \operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } \{ a _ { k } : k \geq n \}
$$

Note that $\left\{ a _ { n } \right\}$ converges to $L \in \mathbb { R }$ if and only if lim sup an = lim inf $a _ { n } = L$

Theorem 2.1 (c.f. [Rud76, Thm. 3.14]). A monotone increasing (resp., decreasing) sequence converges if and only if it is bounded above (resp., below).

Theorem 2.2 (“nth term test” / [Rud76, Thm. 3.23]). $I f \sum _ { k = 1 } ^ { \infty }$ ak converges, then lim $\boldsymbol { \cdot } \boldsymbol { k } \to \infty \ : a _ { k } = 0$ Theorem 2.3 (Cauchy condensation test / [Rud76, Thm. 3.27]). If $a _ { 1 } \geq a _ { 2 } \geq \cdots \geq 0$ then $\textstyle \sum _ { n = 1 } ^ { \infty } a _ { n }$ converges if and only $i f \sum _ { k = 1 } ^ { \infty } 2 ^ { k } a _ { 2 ^ { k } }$ converges.

Theorem 2.4 (Root test / [Rud76, Thm. 3.33]). Set $\alpha = \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } \sqrt [ n ] { \left| a _ { n } \right| }$ . Then,

i) $I f \alpha < 1$ , then $\sum a _ { n }$ converges;

ii) $I f \alpha > 1$ , then $\sum a _ { n }$ diverges;

iii) $I f \alpha = 1$ , the test gives no information.

Theorem 2.5 (Ratio test / [Rud76, Thm. 3.34]). The series $\sum a _ { n }$

• converges if lim $\begin{array} { r } { \operatorname* { s u p } _ { n  \infty } | \frac { a _ { n + 1 } } { a _ { n } } | < 1 ; } \end{array}$

• diverges $\begin{array} { r } { i f \left| { \frac { a _ { n + 1 } } { a _ { n } } } \right| \geq 1 } \end{array}$ for all $n \geq n _ { 0 }$

Theorem 2.6 ([Rud76, Thm. 3.39]). Given the power series $\sum c _ { n } z ^ { n }$ , put

$$
\alpha = \operatorname* { l i m } _ { n \to \infty } \sqrt [ n ] { | c _ { n } | } , \qquad R = \frac { 1 } { \alpha } .
$$

Then $\sum c _ { n } z ^ { n }$ converges $i f \left| z \right| < R$ and diverges $i f \left| z \right| > R$ . R is called the radius of convergence of $\sum c _ { n } z ^ { n }$

## Warm-up problems.

1) For a real sequence $\{ x _ { n } \}$ , if $\scriptstyle \operatorname* { l i m } _ { n \to \infty } x _ { n } = x$ and $\scriptstyle \operatorname* { l i m } _ { n \to \infty } x _ { n } = y$ then $x = y$

2) If X is a metric space, $E \subset X$ , and x is a limit point of E, then there exists a sequence $\{ x _ { n } \} \subset E$ which converges to x.

3) (January 2003 #1) Let $\{ a _ { k } \}$ be a sequence of real numbers such that the series $\textstyle \sum _ { k = 1 } ^ { \infty } a _ { k }$ converges and $\textstyle \sum _ { k = 1 } ^ { \infty } a _ { k } ^ { 2 }$ diverges. Prove that $\textstyle \sum _ { k = 1 } ^ { \infty } a _ { k }$ does not converge absolutely. (See also June 2010 #3a where you are instead told that $\scriptstyle \sum _ { k = 1 } ^ { \infty } a _ { k } a _ { k + 1 }$ diverges and asked to show the same result. Compare this to June 2009 #3a and January 2005 #1b.)

4) ([KRD10, #3.1.D]) Let $\left\{ a _ { n } \right\}$ be a sequence such that lim $\operatorname { 1 } _ { n \to \infty } \left| a _ { n } \right| = 0$ . Prove that there is a subsequence of $\{ a _ { n _ { k } } \}$ of $\left\{ a _ { n } \right\}$ such that $\textstyle \sum _ { k = 1 } ^ { \infty } a _ { n _ { k } }$ converges.

5) (c.f. [Abb01, Exercise 2.4.5]) Let $x _ { 1 } = 2$ and define

$$
x _ { n + 1 } = { \frac { 1 } { 2 } } \left( x _ { n } + { \frac { 2 } { x _ { n } } } \right) .
$$

Find $\scriptstyle \operatorname* { l i m } _ { n \to \infty } x _ { n }$ . Hint: Show that $\{ x _ { n } \}$ is decreasing.

Problems.

6) (June 2013 #1a) Let $a _ { n } = { \sqrt { n } } \left( { \sqrt { n + 1 } } - { \sqrt { n } } \right)$ . Prove that $\textstyle \operatorname* { l i m } _ { n \to \infty } a _ { n } = 1 / 2$

7) (January 2014 #2) (a) Produce sequences $\{ a _ { n } \} , \{ b _ { n } \}$ of positive real numbers such that

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } ( a _ { n } b _ { n } ) > \left( \operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } a _ { n } \right) \left( \operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } b _ { n } \right) .
$$

(b) If $\{ a _ { n } \} , \{ b _ { n } \}$ are sequences of positive real numbers and $\left\{ a _ { n } \right\}$ converges, prove that

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } ( a _ { n } b _ { n } ) = \left( \operatorname* { l i m } _ { n \to \infty } a _ { n } \right) \left( \operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } b _ { n } \right) .
$$

8) (May 2011 #4a) Determine the values of $x \in \mathbb { R }$ for which $\sum _ { n = 1 } ^ { \infty } { \frac { x ^ { n } } { 1 + n | x | ^ { n } } }$ converges, justifying your answer carefully.

9) (June 2005 #3b) If the series $\textstyle \sum _ { n = 0 } ^ { \infty } a _ { n }$ converges conditionally, show that the radius of convergence of the power series $\scriptstyle \sum _ { n = 0 } ^ { \infty } a _ { n } x ^ { n }$ is 1.

10) (January 2011 #5) Suppose $\left\{ a _ { n } \right\}$ is a sequence of positive real numbers such that li $\quad \mathrm { n } _ { n \to \infty } a _ { n } =$ 0 and $\sum a _ { n }$ diverges. Prove that for all $x > 0$ there exist integers $n ( 1 ) < n ( 2 ) < . . .$ . such that $\textstyle \sum _ { k = 1 } ^ { \infty } a _ { n ( k ) } = x$

(Note: Many variations on this problem are possible including more general rearrangements. You may also wish to show that $\operatorname { i f } \sum a _ { n }$ converges conditionally then given any $x \in \mathbb { R }$ there is a rearrangement of $\left\{ b _ { n } \right\}$ of $\{ a _ { n } \}$ such that $\textstyle \sum b _ { n } = r$ . See Rudin Thm. 3.54 for a further generalization.)

11) (June 2008 # 4b) Assume $\beta > 0 , a _ { n } > 0 , n = 1 , 2 , . . . _$ , and the series $\sum a _ { n }$ is divergent. Show that $\sum { \frac { a _ { n } } { \beta + a _ { n } } }$ is also divergent.

## More Problems.

12) (January 2012 #1a) Let $\{ a _ { n } \} , \{ b _ { n } \}$ be bounded sequences of positive real numbers. $\operatorname { I f } \sum b _ { n }$ is convergent, show that $\sum a _ { n } b _ { n }$ is also convergent.

13) Assume that Theorem 2.4 (the root test) is true and prove the ratio test (Theorem 2.5).

14) (January 2008 $\# 6 \mathrm { b } )$ Suppose that lim $\iota _ { n \to \infty } s _ { n } = s$ and lim $\mathfrak { l } _ { n \to \infty } t _ { n } = t$ with $s \neq t$ and $s _ { n } \neq t _ { n }$ for all n. Use and -δ proof to show that

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { s _ { n } + t _ { n } } { s _ { n } - t _ { n } } } = { \frac { s + t } { s - t } } .
$$

15) Prove theorems 2.1, 2.2, and 2.3.

16) (January 2006 #5) Let $a _ { m , n } \geq 0$ for $m , n \in \mathbb { N }$ and assume that the partial sums

$$
\sum _ { m = 1 } ^ { M } \sum _ { n = 1 } ^ { N } a _ { m , n }
$$

are bounded above. Prove carefully that $\scriptstyle \sum _ { m = 1 } ^ { \infty } ( \sum _ { n = 1 } ^ { \infty } a _ { m , n } )$ and $\textstyle \sum _ { n = 1 } ^ { \infty } ( \sum _ { m = 1 } ^ { \infty } a _ { m , n } )$ exist and are equal.

## References

[Abb01] Stephen Abbott. Understanding Analysis. Springer, 2001.

[KRD10] Allan P. Donsig Kenneth R. Davidson. Real analysis and applications. Springer, 2010.

[Rud76] Walter Rudin. Principles of mathematical analysis. McGraw-Hill, Inc., USA, third edition, 1976.