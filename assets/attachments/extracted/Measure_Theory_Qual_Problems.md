## Measure Theory

The problems below are taken out of various textbooks on real variables, including “Real Analysis” by Elias M. Stein and Rami Shakarchi and “Real Analysis” by N. L. Carothers. Questions are also taken from real variables qualifying exams at CUNY Graduate Center. The problems are color-coded. The color green indicates that the problem came from a textbook and to the best of my knowledge was not featured on any qualifying exam. Yellow means that the problem was spotted in at least one qualifying exam. Red indicates that the problem or one just like it appeared in at least two qualifying exams.

1. Let X be a compact metric space and let  be an open cover of X. Show there exists a real number $\epsilon > 0$ such that any ball of radius less than e is contained in at least one of the sets comprising .

2. Suppose E is a given set and ${ \mathfrak { O } } _ { n }$ is the open set:

$$
\mathfrak { O } _ { n } = \{ \mathrm { x } : \mathrm { d } ( \mathrm { x } , \mathrm { E } ) < 1 / \mathrm { n } \}
$$

Show:

(a) If E is compact, then m $\begin{array} { r } { \mathbf { \Theta } ( \mathrm { E } ) = \operatorname* { l i m } _ { \mathbf { \Theta } _ { n  \infty } } \mathbf { m } ( \mathbf { \Theta } _ { n } ) } \end{array}$

(b) However, the conclusion in (a) may be false for E closed and unbounded; or E open and bounded.

3. Using translations and dilations, prove the following: Let B be a ball in $\boldsymbol { \textbf { R } ^ { d } }$ of radius r. Then $\mathbf { m } ( \mathbf { B } ) = \nu _ { d } r ^ { d }$ , where $\nu _ { d } = m ( B _ { 1 } )$ , and $B _ { 1 } = \{ { \boldsymbol { x } } \in \mathbf { R } ^ { d } \colon | { \boldsymbol { x } } | < 1 \}$

4. If $\boldsymbol \delta = ( \delta _ { \mathrm { 1 } } , . . . , \delta _ { \mathrm { 2 } } )$ is a d-tuple of positive numbers $\delta _ { i } > 0$ , and E is a subset of $\boldsymbol { \textbf { R } ^ { d } }$ , we define dE by

$$
\delta \mathrm { E } = \{ ( \delta _ { 1 } x _ { 1 } , . . . , \delta _ { d } x _ { d } ) \colon \mathrm { w h e r e ~ } ( x _ { 1 } , . . . , x _ { d } ) \epsilon \mathrm { E } \} .
$$

Prove that dE is measurable whenever E is measurable, and

$$
\begin{array} { r } { \mathbf { m } ( \delta \mathrm { E } ) = \delta _ { 1 } . . . \delta _ { d } \mathrm { m ( E ) } . } \end{array}
$$

5. Suppose L is a linear transformation of $\boldsymbol { \textbf { R } ^ { d } }$ . Show that if E is a measurable subset of $\boldsymbol { \textbf { R } ^ { d } }$ , then so is L(E), by proceeding as follows:

(a) Note that if E is compact, so is L(E). Hence if E is an $\mathrm { ~ F ~ } _ { \sigma }$ set, so is L(E).

(b) Because L automatically satisfies the inequality

$$
\left| \mathrm { L } ( \mathrm { x } ) - \mathrm { L } ( \mathrm { y } ) \right| \leq \mathrm { M } \left| \mathrm { x } - \mathrm { y } \right|
$$

for some M, we can see that L maps any cube of side length l into a cube of side length $c _ { d } \ M \ell$ , with $c _ { d } = 2 \sqrt { d }$ . Now if $\begin{array} { r } { \mathbf { m } ( \mathrm { E } ) = 0 . } \end{array}$ , there is a collection of cubes $\left\{ Q _ { j } \right\}$

such that $\operatorname { E } \subset \bigcup _ { j = 1 } ^ { \infty } Q _ { j }$ , and $\sum _ { j = 1 } ^ { \infty } m ( Q _ { j } ) < \varepsilon$ . Thus $\begin{array} { r } { \mathbf { m } ^ { * } ( \mathrm { L } ( \mathrm { E } ) ) \leq \mathrm { c } ^ { \prime } \varepsilon } \end{array}$ , and hence $\operatorname { m } ( \mathrm { L } ( \mathrm { E } ) ) =$ 0. Finally observe that L(E) is measurable if and only if L(E) is the union of an $\mathrm { ~ F ~ } _ { \sigma }$ set and a set of measure 0.

6. Give an example of an open set  with the following property: the boundary of the closure of  has positive Lebesgue measure.

7. Let A be the subset of [0, 1] which consists of all numbers which do not have the digit 4 appearing in their decimal expansion. Find m(A).

8. The following deals with $G _ { \delta }$ and $\mathrm { ~ F ~ } _ { \sigma }$ sets.

(a) Show that a closed set is a $G _ { \delta }$ and an open set an $\mathrm { ~ F ~ } _ { \sigma }$

(b) Give an example of an $\mathrm { ~ F ~ } _ { \sigma }$ which is not a $G _ { \delta }$

(c) Give an example of a Borel set which is not $\mathsf { a } \mathsf { G } _ { \delta }$ nor an $\mathrm { ~ F ~ } _ { \sigma }$

9. The outer Jordan content $\mathrm { J ^ { \ast } ( E ) }$ of a set E in R is defined by

$$
\ J ^ { \star } ( \mathrm { E } ) = \mathrm { i n f } \sum _ { j = 1 } ^ { N } I _ { j } \ ,
$$

where the inf is taken over every finite covering $\mathrm { E } \subset \bigcup _ { j = 1 } ^ { N } I _ { j }$

(a) Prove that $\ J ^ { \star } ( \mathrm { E } ) = \ J ^ { \star } ( \overline { { E } } )$ for every set E (here $\overline { E }$ denotes the closure of E).

(b) Exhibit a countable subset $\mathrm { E } \subset [ 0 , 1 ]$ such that $\mathrm { J ^ { \ast } ( E ) } = 1$ while $\mathrm { m } ^ { * } ( \mathrm { E } ) = 0$

10. The Borel-Cantelli lemma. Suppose $\{ E _ { k } \} _ { k = 1 } ^ { \infty }$ is a countable family of measurable subsets of $\mathbb { R } ^ { \ d }$ and that

$$
\sum _ { k = 1 } ^ { \infty } m ( E _ { k } ) < \infty
$$

Let

$\operatorname { E } = \{ \mathbf { x } \in \mathbf { R } ^ { d } : \mathbf { x } \in E _ { k }$ , for infinitely many $\operatorname { k }  \} = \operatorname* { l i m s u p } _ { k \to \infty } ( E _ { k } )$

(a) Show that E is measurable.

(b) Prove m(E) = 0

11. Let $\{ f _ { n } \}$ be a sequence of measurable functions on [0, 1] with $\mid f _ { n } \mid < \infty$ for a.e. x. Show that there exists a sequence $c _ { n }$ of positive real numbers such that

$$
\frac { f _ { n } ( x ) } { c _ { n } } \to 0 \ \mathrm { a . e . } \ x
$$

12. Suppose $\{ f _ { n } \}$ is a sequence of measurable functions on [0, 1] which converges to zero almost everywhere. Prove that there exists a sequence $\left\{ t _ { n } \right\}$ of real numbers such that $\sum _ { n = 1 } ^ { \infty } \mid t _ { n } f _ { n } ( x ) \mid < \infty { \mathrm { ~ a . e . ~ } } x \in [ 0 , 1 ]$

13. Prove the following assertion: Every measurable function is the limit a. e. of a sequence of continuous functions.

14. Here are some observations regarding the set operation $\mathrm { ~ A ~ } + \mathrm { ~ B ~ }$

(a) Show that if either A or B is open, then $\mathrm { \Delta A + B }$ is open.

(b) Show that if A and B are closed, then $\mathrm { \Delta A + B }$ is measurable.

(c) Show, however, that $\mathrm { \Delta A + B }$ might not be closed even though A and B are closed.

15. Show that there exist closed sets A and B with $\mathbf { m } ( \mathrm { A } ) = \mathbf { m } ( \mathrm { B } ) = 0 .$ , but $\mathrm { m ( A + B ) } > 0 \mathrm { : }$ (a) In R, let $\mathrm { A } = \Delta$ (the Cantor set), $\mathrm { B } = \Delta / 2$ . Note that $\mathrm { A } + \mathrm { B } \supset [ 0 , 1 ]$ (b) In $\mathbf { R } ^ { 2 }$ , observe that if $\mathrm { A } = [ 0 , 1 ] \times \{ 0 \}$ and $\mathrm { B } = \{ 0 \} \times [ 0 , 1 ]$ , then $\mathrm { A } + \mathrm { B } = [ 0 , 1 ] \times [ 0 , 1 ]$

16. Let $\mathrm { A } \subset \mathbf { R } . \mathrm { I f } \mathrm { m } ^ { * } ( \mathrm { A } ) > 0 .$ , show that A contains a nonmeasurable set.

17. Prove that there is a continuous function that maps a Lebesgue measurable set to a non-measurable set.

18. Show that there are measurable sets that are not Borel sets.

19. Does there exist an enumeration $\{ r _ { n } \} _ { n = 1 } ^ { \infty }$ of the rationals, such that the complement of

$$
\bigcup _ { n = 1 } ^ { \infty } \left( r _ { n } - { \frac { 1 } { n } } , \ r _ { n } + { \frac { 1 } { n } } \right)
$$

in R is non-empty?

20. Suppose $\mathbf { A } \subset \mathbf { E } \subset \mathbf { B } .$ , where A and B are measurable sets of finite measure. Prove that if $\mathbf { m } ( \mathbf { A } ) = \mathbf { m } ( \mathbf { B } )$ , then E is measurable.

21. Suppose $\mathbf { A } \subset \mathbf { R }$ is measurable with $\mathrm { m ( A ) } < \infty$ . Show that for every number $\mathbf { \boldsymbol { x } } \in ( 0 , \mathbf { \boldsymbol { m } } ( \mathbf { \boldsymbol { A } } ) )$ , there exists a compact set $\mathrm { F } \subset \mathrm { A }$ containing no rational numbers such that $\mathbf { m } ( \mathrm { F } ) = \mathbf { x }$

22. Suppose that $\operatorname { E } \subset \mathbf { R }$ and $\mathrm { m ^ { * } ( E ) > 0 }$ . Given $0 < \alpha < 1$ , show that there exists an open interval I such that $\mathbf { m } ^ { * } ( \mathrm { E } \cap \mathrm { I } ) > \alpha \mathbf { m } ( \mathrm { I } )$

23. Let $\operatorname { E } \subset \mathbf { R }$ be measurable with $\mathrm { m ( E ) > 0 }$ . Prove that $\mathrm { E - E } = \{ { \mathrm { x - y } } { \mathrm { : } } { \mathrm { x } } , { \mathrm { y } } \in \mathrm { E } \}$ contains an interval centered at 0.

24. If E and F are measurable, and $\mathrm { m ( E ) } > 0 , \mathrm { m ( F ) } > 0 .$ , prove that $\mathrm { E + F = \{ x + y } \mathrm { ; x \in E , y } \in F \}$ contains an interval.

25. Let $\operatorname { E } \subset \mathbf { R }$ be Lebesgue measurable, and let $\mathbf { r } \in \mathbf { R }$ . The Lebesgue density of E at r is defined to be

$$
\operatorname* { l i m } _ { h \downarrow 0 } { \frac { m ( E \cap [ r - h , ~ r + h ] } { 2 h } }
$$

provided the limit exists. Construct a measurable subset $\operatorname { E } \subset \mathbf { R }$ for which the density does not exist for at least one $\mathbf { r } \in \mathbf { R }$ .

Solutions:

1. Suppose that no such number e exists for the open cover  of X. Then there is a sequence $\{ x _ { n } \} _ { n = 1 } ^ { \infty }$ in X such that the open ball of radius $1 / { \mathfrak { n } }$ centered at $x _ { n } , B _ { 1 / n } \left( x _ { n } \right)$ , is not contained in any member $U _ { \lambda }$ of the collection . Since X is compact, any sequence of its elements has a convergent subsequence. Let $\left\{ x _ { n \left( k \right) } \right\} _ { k = 1 } ^ { \infty }$ be a convergent subsequence of $\{ x _ { n } \} _ { n = 1 } ^ { \infty }$ which converges to some element $\boldsymbol { \mathbf { \mathit { x } } } \in X .$ . This x is contained in some member $U _ { \lambda }$ of the open cover  and therefore there is some $\delta > 0$ such that $B _ { \delta } ( x ) \subset U _ { \lambda }$ . Letting k be large enough so that $1 / \mathrm { n ( k ) } < \delta / 2$ and $d ( x _ { n ( k ) } , \ x ) < \delta / 2$ , we obtain $B _ { 1 / n ( k ) } \big ( x _ { n ( k ) } \big ) \subset B _ { \delta } ( x ) \subset U _ { \lambda }$ , which contradicts the choice of the sequence $\left\{ x _ { n } \right\} _ { n = 1 } ^ { \infty }$

2. (a) We will show that for any $\epsilon > 0 , \mathrm { m ( E ) } < \mathrm { m ( \Theta ) } < \mathrm { m ( E ) } + \epsilon$ for all sufficiently large n. Since E is compact, then, in particular, E is bounded and $\mathrm { m ( E ) } < \infty$ . Therefore there exists an open set $\mathrm { U } \supset \mathrm { E }$ such that $\mathrm { m ( U ) } < \mathrm { m ( E ) } + \epsilon$

We can write

$$
U = \bigcup _ { y \in U } B _ { r ( y ) } { \bigl ( } y { \bigr ) }
$$

where $\mathbf { r } ( \mathbf { y } )$ is small enough so that $B _ { r ( y ) } ( y ) { \subset U }$

Observe that the collection $\left\{ B _ { r ( y ) } \left( y \right) : y \in U \right\}$ is an open cover of E. Consequently, there is some $\delta > 0$ such that for any $\qquad \mathbf { \boldsymbol { x } } \in \operatorname { E } ,$ there is a $\mathrm { y } \in \mathrm { U }$ for which $B _ { \delta } ( x ) \subset B _ { r ( y ) } ( y )$

For all n large enough so that $1 / \mathrm { n } < \delta , z \in \Theta _ { \mathfrak { n } } \Rightarrow \mathrm { d } ( \mathrm { z } , \mathrm { x } ) < 1 / \mathrm { n }$ for some $\mathbf { \boldsymbol { x } } \in \mathrm { E } \Rightarrow$ $z \in B _ { 1 / n } ( x ) \subset B _ { \delta } ( x ) \subset U$ . Consequently, ${ \mathfrak { O } } _ { n } \subset \mathrm { U }$ , which implies

$$
\mathrm { m ( E ) } < \mathrm { m ( { \mathfrak { O } } } _ { n } ) < \mathrm { m ( U ) } < \mathrm { m ( E ) } + \epsilon
$$

as desired.

(b) Consider $\mathrm { E } = \left\{ \sum _ { k = 1 } ^ { N } { \frac { 1 } { k } } \colon \ N \geq 1 \right\}$ . Then E is an unbounded closed set consisting of isolated points. Since E is countable, $\mathbf { m } ( \mathrm { E } ) = 0$

For any $\mathbf { n } > 0$ and $x \geq \sum _ { k = 1 } ^ { n } { \frac { 1 } { k } }$

$$
x \in \left[ \sum _ { k = 1 } ^ { N } \frac { 1 } { k } , \sum _ { k = 1 } ^ { N + 1 } \frac { 1 } { k } \right]
$$

for some $\Nu \geq \Nu$

Thus

$$
\mathrm { d } ( \mathrm { x } , \mathrm { E } ) < 1 / ( \mathrm { N } + 1 ) < 1 / \mathrm { n } ,
$$

and therefore

$$
\left[ \sum _ { k = 1 } ^ { N } \frac { 1 } { k } , \mathbf { \sigma } \infty \right) \subset \mathfrak { O } _ { n } .
$$

It follows that $\mathbf { m } ( { \mathcal { O } _ { n } } ) = \infty$

Now consider $\operatorname { E } = \bigcup _ { k = 1 } ^ { \infty } \left( r _ { k } - { \frac { \varepsilon } { 2 ^ { k + 1 } } } , \ r _ { k } + { \frac { \varepsilon } { 2 ^ { k + 1 } } } \right)$ , where the $r _ { k }$ are enumerating the set $[ 0 , 1 ] \cap \mathbf { Q }$ and $\varepsilon < 1$ . Then E is a bounded open set with m $( \operatorname { E } ) \leq \sum _ { k = 1 } ^ { \infty } { \frac { \varepsilon } { 2 ^ { k } } } = \varepsilon$ . Notice that E is dense in [0, 1]. Therefore, $[ 0 , 1 ] \subset \Theta _ { n } \Rightarrow \mathbf { m } ( \Theta _ { n } ) \geq 1$

3. Let $\mathrm { B } = \{ \mathbf { x } \in \mathbf { R } ^ { d } \colon \left| \mathbf { x } - \mathbf { a } \right| < \mathbf { r } \}$ . Then $\mathrm { B } = \{ { \mathrm { a } } + { \mathrm { r x } } { \mathrm { : } } x \epsilon B _ { \mathrm { 1 } } \} = { \mathrm { a } } + { \mathrm { r } } B _ { \mathrm { 1 } }$ . Thus B is just $B _ { 1 }$ dilated by the scalar r and translated by the vector a. It follows that $\begin{array} { r } { \mathbf { m ( B ) } = \mathbf { m ( a + r } ~ B _ { 1 } ^ { } ) = } \end{array}$ m $( \mathbf { r } B _ { 1 } ) = r ^ { d } \mathbf { m } ( B _ { 1 } )$

4. First observe that for any rectangle R, $\begin{array} { r } { \mathbf { m } ( \delta \mathrm { R } ) = \delta _ { 1 } . . . \delta _ { d } \mathrm { m ( R ) } } \end{array}$ . For a set E of finite outer measure $\mathrm { m ^ { * } ( E ) }$ and $\epsilon > 0$ we can find an open set $\Theta \supset \mathrm { E }$ such that $\mathrm { m ( { \odot } ) } < \mathrm { m ^ { * } ( E ) } + \epsilon$ . The set ${ \mathcal { O } } = \bigcup _ { j = 1 } ^ { \infty } { Q _ { j } }$ is a countable union of almost disjoint cubes. Therefore d $\Theta = \bigcup _ { j = 1 } ^ { \infty } \delta Q _ { j }$ is a countable union of almost disjoint rectangles whereby

$$
\mathrm { m } ( \delta \odot ) = \sum _ { j = 1 } ^ { \infty } m ( \delta Q _ { j } ) = \sum _ { j = 1 } ^ { \infty } \delta _ { 1 } . . . \delta _ { d } m ( Q _ { j } ) = \delta _ { 1 } . . . \delta _ { d } \mathrm { m } ( \odot ) .
$$

Since $\delta \odot \supset \delta \mathrm { E } ,$ we have

$$
\mathfrak { m } ^ { * } ( \delta \mathrm { E } ) \le \mathrm { m } ( \delta \odot ) = \delta _ { 1 } . . . \delta _ { d } \mathrm { m } ( \odot ) < \delta _ { 1 } . . . \delta _ { d } \mathrm { m } ^ { * } ( \mathrm { E } ) + \delta _ { 1 } . . . \delta _ { d } \ \epsilon .
$$

As e is arbitrary, it follows that

$$
\begin{array} { r } { \operatorname { m } ^ { * } ( \delta \mathrm { E } ) \leq \delta _ { 1 } . . . \delta _ { d } \operatorname { m } ^ { * } ( \mathrm { E } ) . } \end{array}\tag{1}
$$

Notice that $\operatorname { E } = \delta ^ { - 1 } \delta \operatorname { E } ,$ , where $\delta ^ { - 1 } = ( { \delta _ { 1 } } ^ { - 1 } , . . . , { \delta _ { d } } ^ { - 1 } )$ . Hence, by the inequality (1),

$$
\mathfrak { m } ^ { * } ( \mathrm { E } ) = \mathfrak { m } ^ { * } ( \delta ^ { - 1 } \delta \mathrm { E } ) \le \delta _ { 1 } ^ { - 1 } . . . \delta _ { d } ^ { \ - 1 } \mathfrak { m } ^ { * } ( \delta \mathrm { E } )\tag{2}
$$

It follows by inequality (2) that

$$
\delta _ { 1 } . . . \delta _ { d } \mathrm { m } ^ { * } ( \mathrm { E } ) \leq \mathrm { m } ^ { * } ( \delta \mathrm { E } ) .\tag{3}
$$

Inequalities (1) and (3) imply the desired equality.

Finally, to show that dE is measurable whenever E is, observe that if $\Theta \supset \mathrm { E }$ is open and $\mathrm { m } ^ { \ast } ( \Theta - \mathrm { E } ) < \epsilon ,$ then $\delta \odot \supset \delta \mathrm { E }$ is open and satisfies

$$
\begin{array} { r } { \mathfrak { m } ^ { * } ( \delta \mathcal { O } - \delta \mathrm { E } ) = \mathfrak { m } ^ { \star } ( \delta \left[ \mathcal { O } - \mathrm { E } \right] ) = \delta _ { 1 } . . . \delta _ { d } \mathfrak { m } ^ { \star } ( \mathcal { O } \mathrm { - } \mathrm { E } ) < \delta _ { 1 } . . . \delta _ { d } \epsilon . } \end{array}
$$

5. (a) Note that any linear map L on $\boldsymbol { \textbf { R } ^ { d } }$ is Lipschitz and therefore continuous. It follows that for any compact set K, the image of K under $\mathrm { L } , \mathrm { L } ( \mathrm { K } )$ , is compact. By letting $Q _ { j }$ be any increasing sequence of closed cubes such that $\begin{array} { r } { \mathbf { R } ^ { d } = \operatorname* { l i m } _ { j \to \infty } \mathcal { Q } _ { j } } \end{array}$ , observe that every closed subset F of $\boldsymbol { \textbf { R } ^ { d } }$ is a countable union of compact sets. That is $\mathrm { F } = \bigcup _ { j = 1 } ^ { \infty } F \cap Q _ { j }$ Hence any $\mathrm { ~ F ~ } _ { \sigma }$ set is a countable union of compact sets; If $\mathrm { H } = \bigcup _ { j = 1 } ^ { \infty } F _ { j }$ is the union of closed sets $\mathrm { ~ F ~ } _ { j }$ , then $\mathrm { H } = \bigcup _ { n = 1 } ^ { \infty } K _ { n }$ is the union of compact sets $\mathrm { K } _ { n }$ . Therefore $\mathrm { L ( H ) } =$ $\bigcup _ { n = 1 } ^ { \infty } L ( K _ { n } )$ is the union of compact sets as well, making L(H) an $\mathrm { ~ F ~ } _ { \sigma }$ set.

(b) Let E be a set of measure 0. Then, for $\epsilon > 0 ,$ , there is a sequence of closed cubes $Q _ { j }$ such that $\operatorname { E } \subset \bigcup _ { j = 1 } ^ { \infty } { Q } _ { j }$ and $\mathfrak { m } ( \mathrm { E } ) \leq \sum _ { j = 1 } ^ { \infty } m ( \mathcal { Q } _ { j } ) < \epsilon$ . We have that $\operatorname { L } ( \operatorname { E } ) \subset \bigcup _ { j = 1 } ^ { \infty } L ( Q _ { j } ) \subset \bigcup _ { j = 1 } ^ { \infty } \tilde { Q } _ { j }$ where $\tilde { \boldsymbol { Q } } _ { j }$ is a cube of side length $2 \sqrt { d } \mathrm { M } \ell _ { j }$ and $\ell _ { j }$ is the side length of $Q _ { j }$ (The choice of $\tilde { Q } _ { j }$ is dictated by the fact that for any $\operatorname { L } ( \mathbf { x } )$ and $\operatorname { L } ( \mathrm { y } )$ in $\operatorname { L } ( Q _ { j } ) , \mid \operatorname { L } ( \mathbf { x } ) - \operatorname { L } ( \mathbf { y } ) \mid \leq \mathbf { M } \mid \mathbf { x } - \mathbf { y } \mid \leq$ $\textbf { M } \sqrt { ( \ell _ { j } ) ^ { 2 } + . . . + ( \ell _ { j } ) ^ { 2 } } \ = \textbf { M } \sqrt { d ( \ell _ { j } ) ^ { 2 } } \ = \ \sqrt { d } \textbf { M } \ell _ { j } < 2 \sqrt { d } \textbf { M } \ell _ { j } )$ . Thus $\begin{array} { r } { \mathbf { m } ^ { * } ( \mathrm { L } ( \mathrm { E } ) ) \leq } \end{array}$ $\sum _ { j = 1 } ^ { \infty } m ( \tilde { Q } _ { j } ) < ( 2 \sqrt { d } \mathrm { M } ) ^ { d } \ \epsilon$ . And since $\epsilon > 0$ is arbitrary, it follows that $\mathrm { m } ^ { * } ( \mathrm { L } ( \mathrm { E } ) ) = 0$

Finally, if E is a measurable subset of $\boldsymbol { \mathbf { R } } ^ { d }$ , then E can be expressed as a union of an $\mathrm { ~ F ~ } _ { \sigma }$ set with a set of measure 0. By the above work, the image of this union under the linear map L is a union of an $\mathrm { ~ F ~ } _ { \sigma }$ set with a set of measure 0. Hence every linear operator on $\boldsymbol { \textbf { R } ^ { d } }$ maps measurable sets to measurable sets.

6. For $0 < \alpha < 1$ , let $\Delta _ { \alpha }$ be a Cantor-like set obtained as follows:

Step 1: Remove the middle open interval of length $\alpha / 3$ from [0, 1]

Step 2: Remove the middle open intervals of length $\left( \alpha / 3 \right) ^ { 2 }$ from each of the 2 surviving closed subintervals of [0, 1] after step 1.

Step n: Remove the middle open intervals of length $( \alpha / 3 ) ^ { n }$ from each of the $2 ^ { n - 1 }$ surviving closed subintervals of [0, 1] after step n – 1.

Continuing in this fashion, we obtain the open set $\mathrm { \Delta G } = \bigcup _ { n = 1 } ^ { \infty } J _ { n }$ where ${ \cal J } _ { n } = \bigcup _ { k = 1 } ^ { 2 ^ { n - 1 } } { \cal I } _ { k }$ is the union of the $2 ^ { n - 1 }$ middle open subintervals that were removed at step n. Hence

$$
\mathrm { m ( G ) } = \sum _ { n = 1 } ^ { \infty } m ( J _ { n } ) = \sum _ { n = 1 } ^ { \infty } { \frac { 2 ^ { n - 1 } \alpha ^ { n } } { 3 ^ { n } } } = { \frac { \alpha } { 3 } } { \frac { 1 } { 1 - ( 2 \alpha / 3 ) } } = { \frac { \alpha } { 3 - 2 \alpha } } .
$$

Thus, if we set $\alpha = { \sqrt [ 1 ] { 2 } } ,$ , for instance, we get $\mathrm { m } ( \mathrm { G } ) = { \% }$ and therefore m $\left( \Delta _ { \alpha } \right) = { } ^ { 3 / 4 } > 0$ Set $\displaystyle \mathcal { O } = \bigcup _ { n = 1 } ^ { \infty } J _ { 2 n - 1 }$ . Then the closure of  contains at least one boundary point of each interval obtained in steps $1 , 2 , . . . , \mathrm { n } ,$ etc. Since every point in $\Delta _ { \alpha }$ is a limit point of the boundary points of these intervals, the closure of ${ \mathfrak { O } } , { \mathrm { c l } } ( { \mathfrak { O } } )$ , must contain the entire set $\Delta _ { \alpha }$ . Similar analysis suggests that each point in $\Delta _ { \alpha }$ is also a limit point of $\displaystyle \mathfrak { O } ^ { \prime } = \bigcup _ { n = 1 } ^ { \infty } J _ { { } _ { 2 n } }$ We conclude that the boundary of the closure of , bdry(cl()), contains $\Delta _ { \alpha }$ as a subset and therefore $0 < \mathfrak { m } \left( \Delta _ { \alpha } \right) \leq \mathfrak { m } [ \mathrm { b d r y } ( \mathrm { c l } ( \mathfrak { O } ) ) ]$ ].

## 7. The set A can be constructed as follows:

Step 1: Subdivide the interval [0, 1] into 10 equal subintervals [0, 1/10], $[ 1 / 1 0 , 2 / 1 \bar { 0 } ]$ , etc, and remove the interval $[ 4 / 1 0 , 5 / 1 0 ]$

Step 2: Subdivide each of the 9 remaining subintervals further into 10 subintervals and remove all 9 intervals of the form [(10k+4)/100, (10k +5)/100] where k $\mathbf { \Psi } = 0 , 1 , . . . , 9 .$ , but does not take the value 4.

Step n: From each surviving subinterval from step n—1, remove $9 ^ { n - 1 }$ subintervals of the form $\left\lceil \sum _ { j = 1 } ^ { n - 1 } \frac { 1 0 ^ { j } k _ { j } + 4 } { 1 0 ^ { n } } , \ \sum _ { j = 1 } ^ { n - 1 } \frac { 1 0 ^ { j } k _ { j } + 5 } { 1 0 ^ { n } } \right\rceil$ where each k $\mathbf { \Phi } _ { j } = 0 , 1 , . . . , 9 ,$ , but does not take the value 4.

Continuing in this fashion, we see that the measure of the union of the sets removed in steps $1 , 2 , . . . , \mathrm { n } ,$ , etc. is the sum $\sum _ { n = 1 } ^ { \infty } { \frac { 9 ^ { n - 1 } } { 1 0 ^ { n } } } = { \frac { 1 } { 1 0 } } { \frac { 1 } { 1 - ( 9 / 1 0 ) } } = 1$ . Thus, $\mathrm { m } ( \mathrm { A } ) = 0$

8. (a) Let F be closed and consider $\mathfrak { O } _ { n } = \{ \mathrm { x } \colon \mathrm { d } ( \mathrm { x } , \mathrm { F } ) < 1 / \mathrm { n } \}$ . Then ${ \mathfrak { O } } _ { n }$ is open, because the function $\operatorname { f } ( \mathbf { x } ) = \operatorname { d } ( \mathbf { x } , \operatorname { F } )$ is Lipschitz in the metric d and therefore continuous. Clearly ${ \mathrm { ~ F } } \subset { \mathfrak { O } } _ { n }$ . Furthermore, $\mathbf { x } \in \cap \mathcal { O } _ { n }$ if and only if there is a sequence of elements in $\operatorname { F } , \{ x _ { n } \}$ , such that $x _ { n } \to x$ . Since F is closed, we see that $\mathbf { \boldsymbol { x } } \in \cap \Theta$ if and only if $\mathbf { \boldsymbol { x } } \in \operatorname { \mathrm { { F } } }$ . Thus ${ \mathrm { F } } = \cap { \mathfrak { O } } _ { n }$ and F is $\mathsf { a } \mathsf { G } _ { \delta }$ as desired.

(b) Observe that the set of all rational numbers Q can be written as a countable union of singleton sets, $\bigcup _ { n = 1 } ^ { \infty } \{ r _ { n } \}$ , where the $r _ { n }$ is an ordering of Q into a sequence. Thus Q is an $\mathrm { ~ F ~ } _ { \sigma }$ . Note however, that for any countable collection of open sets $\left\{ { \cal { G } } _ { n } : \mathbf { { Q } } \subset { \cal { G } } _ { n } \right\}$ , the intersection $G = \cap G _ { n }$ must be, according to Baire Category theorem, an uncountable dense set. Since Q is countable, we conclude that Q cannot be represented as a $G _ { \delta }$ set.

(c) Let $S = \mathrm { A } \cup \mathrm { B }$ , where $\mathbf { A } = [ 0 , 1 ] \cap \mathbf { Q }$ and $\mathbf { B } = [ 2 , 3 ] - \mathbf { Q }$ . Then A is an $\mathrm { ~ F ~ } _ { \sigma }$ that is not $\mathsf { a } \mathsf { G } _ { \delta }$ and B is $\mathsf { a } \mathsf { G } _ { \delta }$ that is not an $\mathrm { F } _ { \sigma } ( \mathrm { w h y } ? )$ . It is immediately clear from the properties of $\sigma$ algebra that S is a Borel set. However, neither S nor $\mathbf { R } - \mathsf { S }$ are $\mathrm { ~ F ~ } _ { \sigma }$ sets: If S were an $\mathrm { ~ F ~ } _ { \sigma }$ set, then for some sequence of closed sets $\operatorname { F } _ { n } , \mathbf { S } = \bigcup _ { n = 1 } ^ { \infty } F _ { n }$ and $\mathrm { B } =$ $\bigcup _ { n = 1 } ^ { \infty } F _ { n } \cap [ 2 , 3 ]$ , contradicting the fact that B is not an $\mathrm { ~ F ~ } _ { \sigma }$ set. Similarly, if $\mathbf { R } - \mathsf { S }$ is an $\mathrm { ~ F ~ } _ { \sigma }$ then for some sequence of closed sets $\mathbf { C } _ { n } , \mathbf { R } - \mathbf { S } = \bigcup _ { n = 1 } ^ { \infty } C _ { n }$ and, since $[ 0 , 1 ] - \mathbf { Q } \subset \mathbf { R } - S ,$ $[ 0 , 1 ] - \mathbf { Q } = \bigcup _ { n = 1 } ^ { \infty } C _ { n } \cap [ 0 , 1 ]$ . This is impossible as $[ 0 , 1 ] - \mathbf { Q }$ is not an $\mathrm { ~ F ~ } _ { \sigma }$ . Thus, neither S nor $\mathbf { R } - \mathsf { S }$ are $\mathrm { ~ F ~ } _ { \sigma }$ , which is equivalent to the assertion that S is neither $\mathrm { ~ F ~ } _ { \sigma }$ nor $G _ { \delta }$

9. (a) Notice first that just like $\mathrm { m } ^ { \ast } , \mathrm { J } ^ { \ast }$ is an increasing function: If $\mathrm { ~ A ~ C ~ B ~ }$ , then $J ^ { * } ( \mathrm { A } ) \leq$ $\mathrm { J ^ { * } ( B ) }$ . Hence we immediately have

$$
\ J ^ { \star } ( \mathrm { E } ) \leq \ J ^ { \star } ( \overline { { E } } ) .\tag{1}
$$

To get the reverse inequality, observe that if $\textstyle { \mathrm { E } } \subset \bigcup _ { j = 1 } ^ { N } I _ { j }$ then $\overline { { E } } \subset \bigcup _ { j = 1 } ^ { N } \overline { { I } } _ { j }$ , because the set $\biguplus _ { j = 1 } ^ { N } \bar { I } _ { j }$ is closed. Consequently,

$$
\ J ^ { * } ( \mathrm { E } ) = \ \mathrm { i n f } \ \sum _ { j = 1 } ^ { N } \mid I _ { j } \mid \ = \ \mathrm { i n f } \ \sum _ { j = 1 } ^ { N } \mid \bar { I } _ { j } \mid \ \ge \ J ^ { * } ( \overline { { E } } ) .\tag{2}
$$

It follows from inequalities (1) and (2) that $\ J ^ { * } ( \mathrm { E } ) = \ J ^ { * } ( \overline { { E } } )$ as desired.

(b) Let ${ \mathrm { E } } = [ 0 , 1 ] \cap { \mathbf { Q } }$ . By the work done in part $( { \mathrm { a } } ) , { \mathrm { J } } ^ { \star } ( { \mathrm { E } } ) = { \mathrm { J } } ^ { \star } ( { \overline { { E } } } { \mathrm { \Omega } } ) = { \mathrm { J } } ^ { \star } ( [ 0 , 1 ] ) = 1$ While $\mathrm { m ^ { * } ( E ) = 0 }$

Remark: $\mathbf { J } ^ { * } ( [ 0 , 1 ] ) = 1$ , because the sum of the lengths of any finite covering of [0, 1] by open intervals is necessarily bigger than 1 and for any $\mathrm { n } , \mathsf { J } ^ { \star } ( [ 0 , 1 ] ) < \ell ( - 1 / \bar { 2 } \mathrm { n } , 1 + 1 / 2 \bar { \mathrm { n } } ) =$ $1 + 1 / \mathrm { n }$

10. (a) Notice that $\mathbf { x } \in E _ { k }$ for infinitely many k if and only if $\boldsymbol { x } \in \bigcup _ { k = j } ^ { \infty } \boldsymbol { E } _ { k }$ for every j if

and only $\operatorname { i f } x \in \bigcap _ { j = 1 } ^ { \infty } { \big | } E _ { k }$ . Thus

$$
\mathrm { E } = \bigcap _ { j = 1 } ^ { \infty } { \bigcup _ { k = j } ^ { \infty } { E _ { k } } } \ .
$$

Since the unions and intersections of measurable sets are again measurable, we conclude that E is measurable.

(b) Assume that $\sum _ { k = 1 } ^ { \infty } m ( E _ { k } ) < \infty$ . For $\varepsilon > 0$ , let j be such that $\sum _ { k = j } ^ { \infty } m ( E _ { k } ) < \varepsilon$

Therefore

$$
\mathrm { m } ( \mathrm { E } ) \leq \mathrm { m } ( \bigcup _ { k = j } ^ { \infty } E _ { k } \ ) { \leq } \sum _ { k = j } ^ { \infty } m ( E _ { k } ) < \varepsilon .
$$

This proves that m(E) = 0.

11. Set $E _ { k } ^ { n } = \{ x \in [ 0 , \ 1 ] \colon | \ f _ { n } ( x ) | < k \}$ . Then each $E _ { k } ^ { n }$ is measurable and for fixed n, $E _ { k } ^ { n } \subset E _ { k + 1 } ^ { n }$ . Letting $E ^ { n } = \bigcup _ { k = 1 } ^ { \infty } E _ { k } ^ { n } = \operatorname* { l i m } _ { k \to \infty } E _ { k } ^ { n }$ , we get that, since $\mid f _ { n } \mid < \infty$ for a.e. x,

$$
m ( [ 0 , 1 ] - E ^ { n } ) = 0
$$

Since $\operatorname* { l i m } _ { k \to \infty } \operatorname { m } ( E _ { k } ^ { n } ) = \operatorname { m } ( E ^ { n } )$ , for each n, we can pick an increasing sequence of integers $\mathbf { k } ( \mathbf { n } ) .$ , so that for each $\mathbf { n } , \mathbf { k } ( \mathbf { n } )$ is large enough to satisfy

$$
\begin{array} { r } { \mathbf { m } ( E ^ { n } - E _ { k ( n ) } ^ { n } ) < 2 ^ { - n } . } \end{array}
$$

Define

$$
\mathrm { E } = \bigcup _ { j = 1 } ^ { \infty } \bigcap _ { n = j } ^ { \infty } E _ { k ( n ) } ^ { n } .
$$

Then E is measurable and

$$
\mathrm { m } ( [ 0 , 1 ] - \mathrm { E } ) \leq \mathrm { m } ( [ 0 , 1 ] - \bigcap _ { n = j } ^ { \infty } E _ { k ( n ) } ^ { n } ) \leq \sum _ { n = j } ^ { \infty } m ( [ 0 , ~ 1 ] - E _ { k ( n ) } ^ { n } ) = \sum _ { n = j } ^ { \infty } m ( E ^ { n } - E _ { k ( n ) } ^ { n } ) \leq \sum _ { n = j } ^ { \infty } 2 ^ { - n }
$$

Thus, given $\epsilon > 0$ , we can choose j large enough so that $\sum _ { n = j } ^ { \infty } 2 ^ { - n } < \epsilon ,$ which shows that $\mathrm { m } ( [ 0 , 1 ] - \mathrm { E } ) = 0$

Set $c _ { n } = [ k ( n ) ] ^ { 2 }$ and observe that if $x \in \mathrm { E } , x \in \bigcap _ { n = j } ^ { \infty } E _ { k ( n ) } ^ { n }$ for at least one j and therefore, for all $\boldsymbol { \mathrm { n } } \geq \boldsymbol { \mathrm { j } } , \mid f _ { n } \mid < \boldsymbol { \mathrm { k } } ( \boldsymbol { \mathrm { n } } )$ and

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { \left| f _ { n } ( x ) \right| } { c _ { n } } } { = } \operatorname* { l i m } _ { n \to \infty } [ k ( n ) ] ^ { - 1 } { \frac { \left| f _ { n } ( x ) \right| } { k ( n ) } } \leq \operatorname* { l i m } _ { n \to \infty } [ k ( n ) ] ^ { - 1 } = 0
$$

12. Let ${ \mathrm { A } } = \{ { \mathbf { x } } \in [ 0 , 1 ] \colon \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x ) = 0 \}$ . Then $\mathrm { m } ^ { * } ( [ 0 , 1 ] - \mathrm { A } ) = 0$ and A is measurable (since the limit a.e. of measurable functions is again a measurable function). For each $\boldsymbol { \mathrm { k } } \in \mathbb { N } ,$ , define

$$
\operatorname { E } _ { n } ^ { k } = { \big \{ } { \mathbf { x } } \in { \mathrm { A } } { \mathrm { : } } \mid f _ { j } ( x ) \mid < 1 / k { \mathrm { ~ f o r ~ a l l } } j \geq \mathrm { n } { \big \} }
$$

Notice that $\operatorname { E } _ { n } ^ { k } \subset \operatorname { E } _ { n + 1 } ^ { k } \lambda \operatorname { A }$ . Therefore, we may pick an increasing sequence

$\mathrm { n ( 1 ) } < \mathrm { n ( 2 ) } < \ldots < \mathrm { n ( k ) } < \ldots$ such that m $. ( \mathrm { A } - \mathrm { E } _ { n ( k ) } ^ { k } ) < 2 ^ { - k }$ and set

$$
\mathrm { E } = \bigcup _ { r = 1 } ^ { \infty } \bigcap _ { k = r } ^ { \infty } E _ { n ( k ) } ^ { k } .
$$

Then for any $\mathbf { r , }$

$$
\mathrm { m } ( [ 0 , 1 ] - \mathrm { E } ) = \mathrm { m } ( \mathrm { A } - \mathrm { E } ) \leq \mathrm { m } ( \mathrm { A } - \bigcap _ { k = r } ^ { \infty } E _ { n ( k ) } ^ { k } \ ) \leq \sum _ { k = r } ^ { \infty } 2 ^ { - k } \ ,
$$

implying that $\mathrm { m } ( [ 0 , 1 ] - \mathrm { E } ) = 0$

Define

$$
t _ { n } = { \left\{ \begin{array} { l l } { 0 } & { i f ~ n \neq n ( k ) } \\ { 1 / k } & { i f ~ n = n ( k ) } \end{array} \right. } .
$$

Then $\sum _ { n = 1 } ^ { \infty } t _ { n } = \sum _ { k = 1 } ^ { \infty } { \frac { 1 } { k } } = \infty$ . However, for $\mathbf { \boldsymbol { x } } \in \mathrm { E } ,$ , there is some r such that $\displaystyle x \in \bigcap _ { k = r } ^ { \infty } E _ { n ( k ) } ^ { k }$ . Thus, $\mid f _ { n ( k ) } ( x ) \mid < 1 / k$ for all $\mathbf { k } \geq \mathbf { r }$ and, consequently,

$$
\sum _ { n = 1 } ^ { \infty } t _ { n } \mid f _ { n } ( x ) \mid = \sum _ { k = 1 } ^ { \infty } { \frac { \mid f _ { n ( k ) } ( x ) \mid } { k } } = \sum _ { k = 1 } ^ { r - 1 } { \frac { \mid f _ { n ( k ) } ( x ) \mid } { k } } + \sum _ { k = r } ^ { \infty } { \frac { \mid f _ { n ( k ) } ( x ) \mid } { k } } \leq \sum _ { k = 1 } ^ { r - 1 } { \frac { \mid f _ { n ( k ) } ( x ) \mid } { k } } + \sum _ { k = r } ^ { \infty } { \frac { 1 } { k ^ { 2 } } } < \infty .
$$

13. For any measurable function f on $\boldsymbol { \mathbf { R } } ^ { d }$ there is a sequence of step functions $\left\{ \psi _ { n } \right\} _ { n = 1 } ^ { \infty }$ such that $\psi _ { n } \to f \mathrm { a . e . } \ x .$ . Therefore, to show that f is the limit of a sequence of continuous functions a.e., it suffices to establish this in the spatial case when f is a step function. Since every step function $\psi = \sum _ { j = 1 } ^ { N } a _ { j } \chi _ { R } \mathbf { \chi } _ { j }$ is a finite linear combination of characteristic functions over rectangles, we may assume further without any loss of generality that $f = \chi _ { _ R }$ where $R = [ a _ { 1 } , \ b _ { 1 } ] { \times } \cdots { \times } [ a _ { d } , \ b _ { d } ]$

Notice that

$$
\chi _ { R } = \chi _ { [ a _ { 1 } , \ b _ { 1 } ] } \cdot \ldots \cdot \chi _ { [ a _ { d } , \ b _ { d } ] }
$$

and for each $1 \leq \mathrm { j } \leq \mathrm { d }$ , we may define a sequence of continuous functions $F _ { n } ^ { j } \colon \mathbf { R }  \mathbf { R }$ that are given by

$$
F _ { _ n } ^ { j } ( x ) = \left\{ \begin{array} { c c c } { { 0 } } & { { i f } } & { { x \not \in ( a _ { j } - 1 / n , ~ b _ { j } + 1 / n ) } } \\ { { 1 } } & { { i f } } & { { x \in ( a _ { j } , ~ b _ { j } ) } } \\ { { p i e c e w i s e ~ l i n e a r } } & { { o t h e r w i s e } } & \end{array} \right.
$$

Below are the plots of $F _ { 2 } ^ { j }$ (in blue) and $F _ { 5 } ^ { j }$ (in red) in the special instance when $a _ { j } = 1$ and $b _ { j } = 3$ •

<!-- image-->

Clearly,

$$
F _ { n } ^ { j } \to \chi _ { { } _ { [ a _ { j } , \ b _ { j } ] } ( \mathrm { p o i n t w i s e } ) . }
$$

Define $f _ { n } \colon  { \mathbb { R } } ^ { d } \to  { \mathbb { R } }$ by

$$
f _ { n } ( x _ { 1 } , . . . , x _ { d } ) = F _ { n } ^ { 1 } ( x _ { 1 } ) \cdot . . . \cdot F _ { n } ^ { d } ( x _ { d } ) .
$$

Then

$$
\operatorname* { l i m } _ { n \to \infty } f _ { n } = f
$$

as desired.

14. (a) Assume that A is open. Then for any $\mathbf { x } \in \mathbf { A }$ , there is some $\epsilon > 0$ such that B (x)

For any $\mathrm { y } \in \mathrm { B } ,$ the open ball

$$
B _ { \varepsilon } ( x + y ) = y + B _ { \varepsilon } ( x ) \subset \mathsf { A } + \mathsf { B } .
$$

This shows that $\mathrm { \Delta A + B }$ is open.

(b) Assume now that A and B are both closed. Then $\mathrm { A } = \bigcup _ { k = 1 } ^ { \infty } A _ { k }$ and $\mathrm { B } = \bigcup _ { j = 1 } ^ { \infty } B _ { j }$ where the $A _ { k }$ and $B _ { j }$ are compact sequences of sets. It follows that

$$
\mathrm { A } + \mathrm { B } = \bigcup _ { k , j } A _ { k } + B _ { j }
$$

Where the union is taken over all combinations of k and j.

Notice that each set $A _ { k } + B _ { j }$ must be compact: Let $x _ { n } + y _ { n }$ be a sequence in $A _ { k } + B _ { j }$ . Since $A _ { k }$ is compact, there is a subsequence $x _ { n ( p ) }$ of $x _ { n }$ such that $x _ { n ( p ) } \to x \in A _ { k }$ . Since $B _ { j }$ is compact, there is a subsequence $y _ { n ( p ( r ) ) }$ of $y _ { n ( p ) }$ such that $y _ { n ( p ( r ) ) } \to y \in B _ { j }$ . Therefore the sequence $x _ { n } + y _ { n }$ has $x _ { n ( p ( r ) ) } + y _ { n ( p ( r ) ) }$ as a convergent subsequence, which converges in $A _ { k } + B _ { j }$

It follows that $\mathrm { \Delta A + B }$ is the countable union of compact sets and is therefore an $\mathrm { ~ F ~ } _ { \sigma }$

(c) Counterexample in R:

Let $\operatorname { A } = \{ - \boldsymbol { \mathrm { n } } \colon \boldsymbol { \mathrm { n } } \in \mathbf { N } \}$ and $\mathsf { B } = \{ \boldsymbol { \mathrm { n } } + 1 / \boldsymbol { \mathrm { n } } \colon \boldsymbol { \mathrm { n } } \in \boldsymbol { \mathrm { N } } \}$ . Then A and B are closed. However, $\mathrm { \Delta A + B }$ is not closed as it contains the sequence $1 / { \mathfrak { n } } ,$ , but doesn’t contain 0.

Counterexample in $\mathbf { R } ^ { 2 }$

Let $\operatorname { A } = \left\{ ( \boldsymbol { \mathrm { n } } , 1 - 1 / \boldsymbol { \mathrm { n } } ) ; \boldsymbol { \mathrm { n } } \in \mathbf { N } \right\}$ and ${ \mathbf B } = \{ ( \boldsymbol { x } , 0 ) \colon \boldsymbol { x } \in { \mathbf R } \}$ . Then A and B are closed, whereas $\mathrm { ~ A ~ } + \mathrm { ~ B ~ }$ isn’t; Every point in the set $\{ ( \mathsf { x } , 1 ) \colon \mathsf { x } \in \mathbf { R } \}$ is a limit point of $\mathrm { ~ A ~ } + \mathrm { ~ B ~ }$ that is not contained in $\mathrm { \Delta A + B }$

15. (a) Observe that the cantor set $\Delta$ is the set of all $\mathbf { x } \in [ 0 , 1 ]$ that have a ternary representation that uses only 0 and 2. That is, $x = \sum _ { n = 1 } ^ { \infty } { \frac { 2 a _ { n } } { 3 ^ { n } } }$ where $a _ { n } = 0$ or 1. Any

$z \in [ 0 , 1 ]$ can be represented as a sum of two elements, $\boldsymbol { z } = \boldsymbol { \mathsf { x } } + \boldsymbol { \mathsf { y } } ,$ where x has a ternary representation that only uses 0 and 2 and y has a ternary representation that uses only 0 and 1. For example, 0.010211 (mod $3 ) = 0 . { \dot { 0 } } 0 0 2 0 0 + 0 . 0 1 { \dot { 0 } } 0 1 1$ (mod 3). Cleary $\mathrm { y } \in \Delta / 2$ and $[ 0 , 1 ] \subset \Delta + \Delta / 2$ . Hence m $( \Delta + \Delta / 2 ) \ge \mathrm { m } ( [ 0 , 1 ] ) = 1$ . Since $\mathrm { m } ( \Delta ) = 0 , \mathrm { m } ( \Delta / 2 ) = 1 / _ { 2 } \mathrm { m } ( \Delta ) = 0$ .

(b) Let $\mathrm { A } = [ 0 , 1 ] \times \{ 0 \}$ and $\mathbf { B } = \{ 0 \} \times [ 0 , 1 ] .$ , then $\mathrm { A } + \mathrm { B } = [ 0 , 1 ] \times [ 0 , 1 ]$ . In $\mathbf { R } ^ { 2 }$ m $\begin{array} { r } { \left( \mathbb { A } + \mathbb { B } \right) = 1 } \end{array}$ , since $\mathrm { \Delta A + B }$ is a unit square. $\mathbf { m } ( \mathrm { A } ) = \mathbf { m } ( \mathrm { B } ) = 0 .$ , however, because for any $\epsilon >$ 0 the set A, for instance, can be contained in the rectangular strip $[ 0 , 1 ] \times [ - \epsilon , \epsilon ]$ . Since the $\mathbf { R } ^ { 2 }$ measure of a rectangle is its area, we see that $\mathtt { n ( A ) } < \mathtt { m ( [ 0 , 1 ] } \times [ \mathtt { - epsilon , \epsilon } ] ) = 2 \epsilon$

16. Suppose that $\mathrm { m } ^ { * } ( \mathrm { A } ) > 0 .$ , where $\mathbf { A } \subset \mathbf { R }$ . Then ${ \mathrm { A } } = \bigcup _ { n = - \infty } ^ { \infty } A \cap [ n , ~ n + 1 ]$ and $\mathrm { m } ^ { \ast } ( \mathrm { A } ) \leq$

$\sum _ { n = - \infty } ^ { \infty } m ^ { * } ( A \cap [ n , ~ n + 1 ] )$ and it follows that for at least one $\mathtt { n } , \mathtt { m } ^ { * } ( \mathrm { A } \cap [ \mathtt { n } , \mathtt { n } + 1 ] ) > 0$

We will therefore attempt to construct a nonmeasurable subset of $\mathrm { ~ A ~ } \cap [ \mathrm { n } , \mathrm { n } + 1 ] .$ : For any $\alpha \in \mathrm { A } \cap [ \mathrm { n } , \mathrm { n } + 1 ]$ , let $\xi _ { \alpha } = \{ { \boldsymbol { \mathbf { x } } } \in { \boldsymbol { \mathbf { \mathit { A } } } } \cap [ { \boldsymbol { \mathbf { n } } } , { \boldsymbol { \mathbf { n } } } + 1 ] ; { \boldsymbol { \mathbf { \mathit { x } } } } - \alpha \in \mathbf { \mathbf { \boldsymbol { Q } } } \}$ . Then for $\alpha , \beta \in \mathrm { A } \cap [ \mathrm { n } , \mathrm { n } + 1 ]$ ,

$$
\xi _ { \alpha } \cap \xi _ { \beta } = \varnothing { \mathrm { i f } } \alpha \neq \beta
$$

and

$$
\xi _ { \alpha } = \xi _ { \beta } \mathrm { o t h e r w i s e } .
$$

Pick exactly one representative a from each $\xi _ { \alpha }$ and set N to be the collection of these representatives. Observe that for any $\mathrm { { x } , \mathrm { { y } \in \left[ n , n + 1 \right] } }$ , we have $\left| x - y \right| \leq 1$ Consequently,

$\mathrm { ~ A ~ } \cap [ \mathbf { n } , \mathbf { n } + 1 ] \subset \bigcup _ { n = 1 } ^ { \infty } ( r _ { n } + N ) \subset [ \mathbf { n - 1 } , \mathbf { n } + 2 ] .$ , where $r _ { n }$ enumerates all the rational numbers in [-1, 1]. Notice also that for n ∫ m, the sets $r _ { n } + \Nu$ and $r _ { m } + \Nu$ are disjoint, because for any

$\alpha , \beta \in \mathrm { N } , \ r _ { n } \ + \alpha = \ r _ { m } \ + \beta$ if and only if $\xi _ { \alpha } = \xi _ { \beta }$ which, by the construction of $\mathrm { N } ,$ can only happen if and only if $\alpha = \beta , \ r _ { n } = \ r _ { m }$ , and therefore ${ \mathfrak { n } } = { \mathfrak { m } }$

Thus the set N cannot be measurable, for otherwise we have

$$
0 < \mathfrak { m } ^ { \star } ( \mathbb { A } \cap [ \bar { \mathfrak { n } } , \mathfrak { n } + 1 ] ) \le m \left( \bigcup _ { n = 1 } ^ { \infty } ( r _ { n } + N ) \right) = \sum _ { n = 1 } ^ { \infty } m ( r _ { n } + N ) = \sum _ { n = 1 } ^ { \infty } m ( N ) \le \mathfrak { m } ( [ \mathfrak { n } - 1 , \mathfrak { n } + 2 ] ) = 3
$$

which is impossible.

17. Let $\mathsf { c } \colon \Delta \to [ 0 , 1 ]$ be the Cantor function defined by $\mathsf { c } ( \mathsf { x } ) = \sum _ { n = 1 } ^ { \infty } \frac { a _ { n } } { 2 ^ { n } }$ when $x = \sum _ { n = 1 } ^ { \infty } { \frac { 2 a _ { n } } { 3 ^ { n } } }$

$( a _ { n } = 1 \ \mathrm { o r } \ 2 )$ is an element of the Cantor set represented in ternary decimal expansion. Then c is an increasing function on D that is onto [0, 1]. This function can be extended to an increasing continuous onto function g: $[ 0 , 1 ]  [ 0 , 1 ]$ which is given by

$\mathtt { g } ( \mathrm { x } ) = \mathtt { s u p } \mathtt { c } ( \mathrm { y } )$ , where the sup is taken over all $\mathrm { y } \leq \mathrm { x }$ . We construct a strictly increasing, onto, continuous function f: $[ 0 , 1 ]  [ 0 , 2 ]$ by setting $\operatorname { f } ( \mathbf { x } ) = \mathbf { x } + \operatorname { g } ( \mathbf { x } )$

Since f and g are continuous, they map compacts sets to compact sets. Hence, because the Cantor set $\Delta$ is compact, both f(D) and $\mathrm { g } ( \Delta )$ are compact and therefore measurable and of finite measure. Recall that $\mathrm { g } ( \Delta ) = [ 0 , 1 ]$ and therefore m $( \mathrm { g } ( \Delta ) ) = 1$ . We claim m $( \operatorname { f } ( \Delta ) ) \geq \mathbf { m } ( \mathrm { g } ( \Delta ) )$ . To see this, for $\epsilon > 0 ,$ , let $\Theta \supset \operatorname { f } ( \Delta )$ be an open set such that $\mathbf { m } ( \mathfrak { O } ) <$ $\mathbf { m } ( \mathbf { f } ( \Delta ) ) + \boldsymbol { \epsilon }$ . Then ${ \mathcal { O } } = \bigcup _ { n = 1 } ^ { \infty } I _ { n }$ is a countable union of disjoint open intervals. For each $I _ { n }$ pick $x _ { n } \in \Delta$ such that $\operatorname { f } ( x _ { n } ) \in I _ { n }$ and set

$$
J _ { n } = I _ { n } - x _ { n } = \{ \mathrm { y } - x _ { n } : \mathrm { y } \in I _ { n } \} .
$$

Then the open set ${ \mathcal { O } } ^ { \prime } { = } \bigcup _ { n = 1 } ^ { \infty } J _ { \mathit { r } }$ contains $[ 0 , 1 ] = \operatorname { g } ( \Delta )$ . To verify this, select any $\boldsymbol { x } \in \Delta$ and since $\mathfrak { O } \supset \mathrm { f } ( \Delta )$ , we must have $\mathbf { f } ( \mathbf { x } ) \in I _ { n }$ for some n. This implies that $\operatorname { g } ( \mathbf { x } ) = \operatorname { f } ( \mathbf { x } ) - \mathbf { x } \in \ J _ { n }$ as verified by analyzing the following two cases:

Case 1: Suppose $\mathbf { x } \leq x _ { n }$ . Then $[ { \mathrm { f } } ( \times ) , { \mathrm { f } } ( x _ { n } ) ] \subset I _ { n }$ and

$$
[ \operatorname { g } ( \mathbf { x } ) , \operatorname { g } ( x _ { n } ) ] = [ \operatorname { f } ( \mathbf { x } ) - \mathbf { x } , \operatorname { f } ( x _ { n } ) - x _ { n } ] \subset [ \operatorname { f } ( \mathbf { x } ) - x _ { n } , \operatorname { f } ( x _ { n } ) - x _ { n } ] \subset J _ { n } .
$$

In particular, $\mathbf { g } ( \mathbf { x } ) \in J _ { n }$

Case 2: Suppose $\mathbf { x } \geq x _ { n }$ . Then $[ { \mathrm { f } } ( x _ { n } ) , { \mathrm { f } } ( \times ) ] { \subset I } _ { n }$ and

$$
[ \operatorname { g } ( x _ { n } ) , \operatorname { g } ( \mathbf { x } ) ] = [ \operatorname { f } ( x _ { n } ) - x _ { n } \ , \operatorname { f } ( \mathbf { x } ) - \mathbf { x } ] \subset [ \operatorname { f } ( x _ { n } ) - x _ { n } \ , \operatorname { f } ( \mathbf { x } ) - x _ { n } ] \subset J _ { n } .
$$

In particular, $\mathbf { g } ( \mathbf { x } ) \in J _ { n }$

It follows that

$$
\operatorname { m } ( \operatorname { g } ( \Delta ) ) \leq \operatorname { m } ( \mathbb { O } ^ { \prime } ) \leq \sum _ { n = 1 } ^ { \infty } m ( J _ { n } ) = \sum _ { n = 1 } ^ { \infty } m ( I _ { n } ) = \operatorname { m } ( \mathbb { O } ) < \operatorname { m } ( \operatorname { f } ( \Delta ) ) + \epsilon .
$$

Hence

$$
\begin{array} { r } { \operatorname { m } ( \mathrm { f } ( \Delta ) ) \geq \operatorname { m } ( \mathrm { g } ( \Delta ) ) = \operatorname { m } ( [ 0 , 1 ] ) = 1 . } \end{array}
$$

By the previous exercise, we may pick a nonmeasurable subset $\mathrm { ~ N ~ } \subset \mathrm { { f } } ( \Delta )$ and set $\mathrm { A } =$ ${ \mathsf { f } } ^ { - 1 } \left( \mathsf { N } \right) \subset \Delta$ . Then A has measure 0 and is therefore measurable, whereas $\mathrm { f ( A ) } = \mathrm { N }$ is not. Thus a continuous function may map a measurable set to a nonmeasurable set even with the added hypothesis that the function is strictly increasing.

18. Consider the function f: $[ 0 , 1 ]  [ 0 , 2 ]$ from the previous exercise. Notice that any continuous function on a compact set is a closed map. That is, f maps closed subsets of [0, 1] to closed subsets of [0, 2]. Since f is strictly increasing and onto, f is invertible with a continuous inverse $\mathrm { f } ^ { - 1 } \colon [ 0 , 2 ]  [ 0 , 1 ] ( \mathrm { I f ~ F } \subset [ 0 , 1 ]$ is closed, then $( \mathrm { f } ^ { - 1 } ) ^ { - 1 } ( \mathrm { F } ) = \mathrm { f } ( \mathrm { F } )$ is a closed subset of [0, 2]. Thus, the inverse image of a closed set under $\mathbf { f } ^ { - 1 }$ is closed, which means that $\mathbf { f } ^ { - 1 }$ must be continuous.) In particular, f is a homeomorphism; f maps closed sets to closed sets and open sets to open sets.

Because f is bijective, for any sequence of subsets $H _ { n } \subset [ 0 , 1 ]$ , we have

$$
f \biggl ( \bigcup _ { n = 1 } ^ { \infty } H _ { n } \biggr ) = \bigcup _ { n = 1 } ^ { \infty } f ( H _ { n } ) \mathrm { ~ a n d ~ } f \biggl ( \bigcap _ { n = 1 } ^ { \infty } H _ { n } \biggr ) = \bigcap _ { n = 1 } ^ { \infty } f ( H _ { n } ) .\tag{1}
$$

Thus, f maps an $\mathrm { ~ F ~ } _ { \sigma }$ to an $\mathrm { ~ F ~ } _ { \sigma }$ -set and a $G _ { \delta }$ to a ${ \mathrm { ~ \cal ~ G ~ } } _ { \delta } { \mathrm {  ~ \Gamma ~ } } ^ { }$ . Moreover, a closer investigation of the identities (1) reveals that f maps any Borel set to a set of the same type. For

instance, if B is an $\operatorname { F } _ { \sigma \delta } \lnot \mathrm { e t } , \operatorname { B } = \bigcap _ { j = 1 } ^ { \infty } \bigcup _ { k = 1 } ^ { \infty } F _ { k } ^ { j }$ , where the $F _ { k } ^ { j }$ are closed. Then

$$
\mathrm { f ( B ) } = \bigcap _ { j = 1 } ^ { \infty } f \left( \bigcup _ { k = 1 } ^ { \infty } F _ { k } ^ { j } \right) { = } \bigcap _ { j = 1 } ^ { \infty } \bigcup _ { k = 1 } ^ { \infty } f ( F _ { k } ^ { j } ) ,
$$

where $\operatorname { f } ( F _ { k } ^ { j } )$ is closed. Hence f(B) is also an $\mathrm { F } _ { \sigma \delta } { - } \mathrm { s e t }$

Let $\mathrm { ~ A ~ C ~ } \Delta$ be as in the previous exercise. Then A is measurable, while $\mathrm { f ( A ) = N i s n ^ { \prime } t }$ . But if A were a Borel set, $\mathrm { f ( A ) }$ would have been a Borel set as well, which is impossible as all Borel sets are measurable.

19. Observe that there is a one-to-one correspondence between the set $\mathbf { N } ^ { 2 } = \left\{ n ^ { 2 } : n \in \mathbf { N } \right\}$ and $\mathbf { R } - [ 0 , 1 ] \cap \mathbf { Q }$ and a one-to-one correspondence between the set of square free integers ${ \bf N } - { \bf N } ^ { 2 }$ and $[ 0 , 1 ] \cap \mathbf { Q }$ . Thus, Q can be ordered into a sequence $\{ r _ { n } \} _ { n = 1 } ^ { \infty }$ such that $r _ { n } \in [ 0 , 1 ] \cap \mathbf { Q }$ whenever $ { \mathbf { n } } \in  { \mathbf { N } } -  { \mathbf { N } } ^ { 2 }$ and $r _ { n } \in \mathrm { { \bf ~ R } } - [ 0 , 1 ] \cap \mathrm { { \bf ~ Q } }$ when $\mathbf { n } \in \mathbf { N } ^ { 2 }$ . In this case

$$
m \Bigg ( \bigcup _ { n = 1 } ^ { \infty } \Bigg ( r _ { n } - \frac { 1 } { n } , ~ r _ { n } + \frac { 1 } { n } \Bigg ) \Bigg ) = m \Bigg ( \bigcup _ { n \in N - N ^ { 2 } } \Bigg ( r _ { n } - \frac { 1 } { n } , ~ r _ { n } + \frac { 1 } { n } \Bigg ) \bigcup _ { n \in N ^ { 2 } } \Bigg ( r _ { n } - \frac { 1 } { n } , ~ r _ { n } + \frac { 1 } { n } \Bigg ) \Bigg ) .
$$

Since 2 is the smallest number in ${ \bf N } - { \bf N } ^ { 2 }$

$$
\bigcup _ { n \in N - N ^ { 2 } } \left( r _ { n } - { \frac { 1 } { n } } , \ r _ { n } + { \frac { 1 } { n } } \right) \subset ( - 1 / 2 , 1 + 1 / 2 ) \subset ( - 1 , 2 ) .
$$

Therefore,

$$
m { \binom { \bigcup } { n = 1 } } { \binom { r _ { n } - { \frac { 1 } { n } } , \ r _ { n } + { \frac { 1 } { n } } } { n } } \leq \ m { \left( \bigcup _ { n \in N - N ^ { 2 } } { \binom { r _ { n } - { \frac { 1 } { n } } , \ r _ { n } + { \frac { 1 } { n } } } { n } } \right) } + m { \left( \bigcup _ { n \in N ^ { 2 } } { \left( r _ { n } - { \frac { 1 } { n } } , \ r _ { n } + { \frac { 1 } { n } } \right) } \right) } ,
$$

which implies

$$
m \{ \bigcup _ { n = 1 } ^ { \infty } \left( r _ { n } - { \frac { 1 } { n } } , \ r _ { n } + { \frac { 1 } { n } } \right) \} \leq 3 + \sum _ { k = 1 } ^ { \infty } { \frac { 1 } { k ^ { 2 } } } < \infty .
$$

The compliment of $\bigcup _ { n = 1 } ^ { \infty } \left( r _ { n } - { \frac { 1 } { n } } , \ r _ { n } + { \frac { 1 } { n } } \right)$ has, consequently, an infinite measure and

therefore must contain an uncountably infinite collection of real numbers.

20. Notice that $\mathrm { E } = \mathrm { A } \cup \mathrm { E - A }$ where $\operatorname { E - A } \subset \operatorname { B - A }$ . Since A and B are measurable sets of finite measure satisfying $\mathsf { A } \subset$ B and ${ \mathfrak { m } } ( { \mathrm { A } } ) = { \mathfrak { m } } ( { \mathrm { B } } )$ , we have

$$
\mathfrak { m } ^ { * } ( \mathrm { \mathrm { E - A } } ) \leq \mathfrak { m } ( \mathrm { B - A } ) = \mathfrak { m } ( \mathrm { B } ) - \mathfrak { m } ( \mathrm { A } ) = 0 .
$$

Thus, upon recalling that all sets of zero measure are measurable, we see that E is the union of two measurable sets. Hence E is measurable.

21. Let $\mathrm { B } = \mathrm { A } - \mathbf { Q }$ . Then $\mathbf { m } ( \mathbf { B } ) = \mathbf { m } ( \mathbf { A } )$ . Observe that $\mathrm { B } = \bigcup _ { n = 1 } ^ { \infty } B _ { n }$ where $B _ { n } = \mathbf { B } \cap [ - \mathbf { n } , \mathbf { n } ]$ is an increasing sequence of bounded measurable sets with $B _ { n } \nearrow \mathrm { ~ B ~ }$ . Thus, there exists an n large enough so that $\mathsf { x } < \mathsf { m } ( B _ { n } ) < \mathsf { m } ( \mathsf { B } )$ . And because $B _ { n }$ is measurable,

for $\epsilon = \mathrm { m } { ( B _ { n } ) } - \mathrm { x } .$ , there is a closed set ${ \mathsf { C } } \subset B _ { n }$ such that m $\begin{array} { r } { ( B _ { n } - \mathrm { C } ) = \mathrm { m } ( B _ { n } ) - \mathrm { m } ( \mathrm { C } ) < \epsilon . } \end{array}$ Hence $\mathbf { m } ( \mathbf { C } ) > \mathbf { x }$ . Note that C is closed and bounded and therefore compact. Let $\mathsf { a } = \operatorname { i n f } \mathsf { C }$ and b = sup C. Also, C is a subset of B and therefore contains no rational numbers.

Define $\mathrm { f } ( \mathrm { t } ) = \mathrm { m } ( ( \mathrm { - } \infty , \mathrm { t } ] \cap \mathrm { C } )$ . Then f is Lipschitz:

Observe that for $\mathrm { t } < \mathrm { s } , \mathrm { f } ( \mathrm { t } ) \leq \mathrm { f } ( \mathrm { s } )$ and

$$
\mathrm { f } ( \mathsf { s } ) = \mathrm { m } ( \{ ( \mathrm { - } \infty , \mathrm { t } ] \cup ( \mathrm { t } , \mathsf { s } ] \} \cap \mathsf { C } ) = \mathrm { f } ( \mathsf { t } ) + \mathrm { m } ( ( \mathrm { t } , \mathsf { s } ] \cap \mathsf { C } ) \leq \mathrm { f } ( \mathsf { t } ) + ( \mathrm { s } - \mathsf { t } ) .
$$

Thus,

$$
| { \mathrm { ~ f ( s ) - f ( t ) ~ } } | = { \mathrm { f ( s ) - f ( t ) } } \leq s - { \mathrm { t } } = { \mathrm { ~ } } | s - { \mathrm { t } } | .
$$

In particular, f is continuous.

Let a = inf C and $\mathsf { b } = \mathsf { s u p C }$ . Since C is bounded, a and b are finite numbers for which $\mathrm { f } ( \mathsf { a } ) = 0$ and $\mathrm { f ( b ) = m ( C ) > x }$ . By the intermediate value property, there is some number $\mathsf { a } < \mathsf { t } _ { 0 } <$ b such that $\mathrm { f } ( \mathrm { t } _ { 0 } ) = \mathrm { x }$ . Then $\mathrm { F } = \left( \mathrm { - } \infty , \mathrm { t } _ { 0 } \right] \cap \mathrm { C }$ is the desired set.

22. We may assume that E is a bounded set, because $\mathrm { m ^ { * } ( E ) > 0 }$ implies that $\mathbf { m } ^ { * } ( \mathrm { E } \cap \left[ \mathbf { - n } , \mathbf { n } \right] ) > 0$ for all large enough n. Thus, without loss of generality, $\mathrm { m ^ { * } ( E ) } < \infty$ Recall that $\mathfrak { m } ^ { * } ( \mathrm { E } ) = \mathrm { i n f } \mathfrak { m } ( \vartheta )$ where the infimum is taken over all open sets $\vartheta \supset \mathrm { E }$ . For

$0 < \alpha < 1$ , pick $\epsilon > 0$ that satisfies $\alpha = 1 / ( 1 + \epsilon )$ and along with it pick an open set $\vartheta \supset \mathrm { E } ,$ such that

$$
\begin{array} { r } { \mathbf { m } ( \vartheta ) < ( 1 + \epsilon ) \mathbf { m } ^ { * } ( \mathrm { E } ) . } \end{array}\tag{1}
$$

Notice that inequality (1) is equivalent to $\alpha \mathrm { m } ( \vartheta ) < \mathrm { m } ^ { \ast } ( \mathrm { E } )$ . Upon expressing $\vartheta = \bigcup _ { n = 1 } ^ { \infty } I _ { n }$ as the union of disjoint open intervals, we see that

$$
\sum _ { n = 1 } ^ { \infty } m ( \alpha \ I _ { n } ) = \alpha { \bmod { ( } } \vartheta ) < { \mathbf { m } } ^ { * } ( { \mathrm { E } } ) \leq \sum _ { n = 1 } ^ { \infty } m ^ { * } ( E \cap I _ { n } )\tag{2}
$$

Since the series on the right side of (2) is bigger than the left series, it follows that for at least one n, ( m α $I _ { n } ) \leq m ^ { * } ( E \cap I _ { n } )$

23. By exercise 22, we can find an open interval I of finite length such that $\mathbf { m } ( \mathrm { E } \cap \mathrm { I } ) > \alpha \mathbf { m } ( \mathrm { I } )$ , where $0 < \alpha < 1$ . Under the appropriate choice of a, we will show that $\mathrm { E } - \mathrm { E }$ contains the interval $\mathrm { J } = ( - \mathrm { m ( I ) } / 2 , \mathrm { m ( I ) } / 2 )$ . Now $\mathrm { E } \cap \mathrm { I } - \mathrm { E } \cap$ I contains J if and only if for each $\mathbf { \boldsymbol { x } } \in \mathbf { \boldsymbol { J } } .$ , the sets x + E … I and E … I are not disjoint. We prove that $( \mathbf { x } + \mathrm { E } \cap \mathrm { I } ) \cap ( \mathrm { E } \cap \mathrm { I } ) \neq \phi$ by establishing

$$
\mathbf { m } ( ( \mathbf { x } + \mathrm { E } \cap \mathrm { I } ) \cup ( \mathrm { E } \cap \mathrm { I } ) ) < \mathbf { m } ( \mathbf { x } + \mathrm { E } \cap \mathrm { I } ) + \mathbf { m } ( \mathrm { E } \cap \mathrm { I } ) = 2 \mathbf { m } ( \mathrm { E } \cap \mathrm { I } )
$$

for all $\mathbf { \boldsymbol { x } } \in \mathbf { \boldsymbol { J } }$

We have

$$
\mathbf { m } ( ( \mathbf { x } + \mathrm { E } \cap \mathrm { I } ) \cup ( \mathrm { E } \cap \mathrm { I } ) ) \leq \mathbf { m } ( ( \mathbf { x } + \mathrm { I } ) \cup \mathrm { I } ) \leq \mathbf { m } ( ( \mathrm { s u p } ( \mathrm { J } ) + \mathrm { I } ) \cup \mathrm { I } ) = ( 3 / 2 ) \mathbf { m } ( \mathrm { I } ) < 2 \mathbf { m } ( \mathrm { I } ) .
$$

Where, in the inequality above we note that $\mathrm { m } ( ( \boldsymbol { \times } + \mathrm { I } ) \cup \mathrm { I } )$ is maximized when $\boldsymbol { \mathsf { x } } + \boldsymbol { \mathsf { I } }$ is shifted away from I as far as possible. The largest shift is smaller than $\mathbf { x } = \mathbf { m } ( \mathrm { I } ) / 2$ and therefore $\boldsymbol { \mathsf { x } } + \boldsymbol { \mathsf { I } }$ and I must have an open interval whose length is not smaller than $\mathbf { m } ( \mathrm { I } ) / 2$ . In particular $\boldsymbol { \mathsf { x } } + \boldsymbol { \mathsf { I } }$ and I are never disjoint.

$$
\mathbf { m } ( ( \mathbf { x } + \mathrm { E } \cap \mathrm { I } ) \cup ( \mathrm { E } \cap \mathrm { I } ) ) \leq ( 3 / 2 ) \mathbf { m } ( \mathrm { I } ) < ( 3 / 2 ) \ ( 1 / \alpha ) \mathbf { m } ( \mathrm { E } \cap \mathrm { I } ) < 2 \mathbf { m } ( \mathrm { E } \cap \mathrm { I } )
$$

whenever $\left( 3 / 2 \right) \left( 1 / \alpha \right) < 2$ or equivalently, when $\alpha > \%$

24. We will reduce the proof to the special case E – E treated in the previous exercise with the help of the following observations:

Observation 1: By setting $\operatorname { K } = - \operatorname { F } = \{ - \mathbf { x } \colon \mathbf { x } \in \operatorname { F } \} , \operatorname { E } + \operatorname { F }$ becomes $\mathrm { E } - \mathrm { K }$ . Thus, without loss of generality, we only need to prove that $\mathrm { E } - \mathrm { F }$ contains an interval.

Observation 2: If $\mathbf { r } \in \mathbf { R } , ( \mathbf { r } + \mathrm { E } ) - \mathrm { F } = \mathbf { r } + ( \mathrm { E } - \mathrm { F } )$ . Hence, $\mathrm { E } - \mathrm { F }$ contains the interval I if and only if $\left( \mathbf { r } + \mathrm { E } \right) - \mathrm { F }$ contains the interval r + I.

Observation 3: For each $0 < \alpha < 1$ , there exist open intervals I and J with $\mathbf { m } ( \mathrm { I } ) =$ $\mathbf { m } ( \mathrm { J } )$ such that m $( \mathrm { E } \cap \mathrm { I } ) > \alpha \ : \mathrm { m } ( \mathrm { I } )$ and $\mathrm { m ( F \cap J ) } > \alpha \mathrm { m ( J ) }$ . To see this, first notice that every open set $\vartheta \subset \mathbf { R } ^ { d }$ can be written as a countable union of almost disjoint closed cubes. Furthermore, we may construct these cubes so that the side length of each cube is some integer power of 2. Thus, if U is an open set containing E and satisfying a $\mathbf { m } ( \mathrm { U } ) < \mathbf { m } ( \mathrm { E } )$ , we can repeat the argument in exercise 22 to find (this time closed) interval I  with $\mathbf { m } ( \mathrm { I } _ { 1 } ) = 2 ^ { n }$ for some $\mathbf { n } \in \mathbf { Z }$ so that a $\mathbf { m } ( \mathrm { I } _ { 1 } ) < \mathbf { m } ( \mathrm { E } \cap \mathrm { I } _ { 1 } )$ . Similarly, we can find a closed interval J with $\mathbf { m ( J _ { 1 } ) } = 2 ^ { \mathfrak { m } }$ for some $\mathbf { m } \in \mathbf { Z }$ so that $\alpha \mathrm { m ( J _ { 1 } ) } < \mathrm { m ( F } \cap \mathrm { J _ { 1 } ) }$ . Without loss of generality, $\mathbf { n } ( \mathrm { J } _ { 1 } ) \leq \mathbf { m } ( \mathrm { I } _ { 1 } )$ and it follows by construction that $\mathrm { m ( I _ { 1 } ) = k m ( J _ { 1 } ) }$ , where k is a positive integer. In particular, $\mathrm { I } _ { 1 }$ is the union of k almost disjoint closed intervals $\boldsymbol { \mathrm { I } } _ { 1 } ^ { 1 } , . . . , \boldsymbol { \mathrm { I } } _ { 1 } ^ { k }$ with m $\left( \mathrm { I } _ { 1 } ^ { j } \right) = \mathbf { m } ( \mathrm { J } _ { 1 } )$ for each j. Finally, since

$$
\alpha \mathrm { m } ( \mathrm { I } _ { \mathrm { 1 } } ) = \sum _ { j = 1 } ^ { k } \alpha m ( I _ { \mathrm { 1 } } ^ { j } ) < \mathrm { m } ( \mathrm { E } \cap \mathrm { I } _ { \mathrm { 1 } } ) = \sum _ { j = 1 } ^ { k } m ( E \cap I _ { \mathrm { 1 } } ^ { j } ) ,
$$

it follows that for at least one $\mathrm { j } , \alpha \mathrm { m } ( \mathrm { I } _ { 1 } ^ { j } ) < \mathrm { m } ( \mathrm { E } \cap \mathrm { I } _ { 1 } ^ { j } )$ . The intervals ${ \mathrm { I } } = { \mathrm { i n t e r i o r } } ( { \mathrm { I } } _ { 1 } ^ { j } )$ and $\mathrm { J } = \mathrm { i n t e r i o r } ( \mathrm { J } _ { 1 } )$ establish our claim.

We proceed to show that $\mathrm { m } ( ( \mathrm { r } + \mathrm { E } ) \cap \mathrm { F } ) > 0$ for some r. It will then follow that $\left( \mathbf { r } + \mathrm { E } \right) - \mathrm { F }$ must contain a set of the form $\mathrm { K } - \mathrm { K } ,$ where $\mathrm { K } = \left( \mathbf { r } + \mathrm { E } \right) \cap \mathrm { F }$ is a set of positive measure. Pick open intervals I and J obtained in observation 3. Shift the interval I by an appropriate r so that $\mathbf { r } + \mathrm { I } = \mathrm { J }$ . Then, for an appropriately chosen value of a (to be specified below),

$$
\mathrm { m } ( [ ( \mathbf { r } + \mathrm { E } ) \cap \mathrm { J } ] \cap [ \mathrm { F } \cap \mathrm { J } ] ) > 0 .
$$

Otherwise,

$$
\operatorname { m } ( \boldsymbol { \mathrm { J } } ) \geq \operatorname { m } ( [ ( \boldsymbol { \mathrm { r } } + \boldsymbol { \mathrm { E } } ) \cap \boldsymbol { \mathrm { J } } ] \cup [ \boldsymbol { \mathrm { F } } \cap \boldsymbol { \mathrm { J } } ] ) = \operatorname { m } ( ( \boldsymbol { \mathrm { r } } + \boldsymbol { \mathrm { E } } ) \cap \boldsymbol { \mathrm { J } } ) + \operatorname { m } ( \boldsymbol { \mathrm { F } } \cap \boldsymbol { \mathrm { J } } ) > 2 \alpha \operatorname { m } ( \boldsymbol { \mathrm { J } } ) .
$$

But $\mathbf { m } ( \mathrm { J } ) >$ 2a m(J) if and only if $\alpha < \%$ . Thus $\textstyle { 1 / 2 \leq \alpha < 1 }$ guarantees $\mathrm { m } ( ( \mathrm { r } + \mathrm { E } ) \cap \mathrm { F } ) > 0$ as desired.

25. Let $\mathbf { r } = 0$ and $\mathrm { E } = \bigcup _ { 2 k = 0 } ^ { \infty } E _ { 2 k }$ , where $E _ { 2 k } = I _ { 2 k } \cup ( - I _ { 2 k } )$ and $I _ { 2 k } = [ 2 ^ { - 2 k - 1 } , ~ 2 ^ { - 2 k } ]$ . Set

$h _ { n } = \sum _ { k = n } ^ { \infty } 2 ^ { k } = 2 ^ { - n + 1 }$ . We show that

$$
\operatorname* { l i m } _ { n \to \infty } \frac { m ( E \cap [ - h _ { 2 n } , \ h _ { 2 n } ] } { 2 h _ { 2 n } } \neq \operatorname* { l i m } _ { n \to \infty } \frac { m ( E \cap [ - h _ { 2 n + 1 } , \ h _ { 2 n + 1 } ] } { 2 h _ { 2 n + 1 } } .
$$

Now,

$$
\operatorname* { l i m } _ { n \to \infty } \frac { m ( E \cap [ - h _ { 2 n } , \ h _ { 2 n } ] } { 2 h _ { 2 n } } = \operatorname* { l i m } _ { n \to \infty } \frac { \displaystyle \sum _ { k = n } ^ { \infty } m ( I _ { 2 k } ) } { \displaystyle 2 ^ { - 2 n + 1 } } = \operatorname* { l i m } _ { n \to \infty } \frac { \displaystyle \sum _ { k = n } ^ { \infty } 2 ^ { - 2 k - 1 } } { \displaystyle 2 ^ { - 2 n + 1 } } = \frac { 1 } { 3 } ,
$$

Whereas

$$
\operatorname * { l i m } _ { n  \infty } { \frac { m ( E \cap [ - h _ { 2 n + 1 } , ~ h _ { 2 n + 1 } ] } { 2 h _ { 2 n + 1 } } } = \operatorname* { l i m } _ { n  \infty } { \frac { \displaystyle \sum _ { k = n } ^ { \infty } m ( I _ { 2 k + 2 } ) } { \displaystyle 2 ^ { - 2 n } } } = \operatorname* { l i m } _ { n  \infty } { \frac { \displaystyle \sum _ { k = n } ^ { \infty } 2 ^ { - 2 k - 3 } } { \displaystyle 2 ^ { - 2 n } } } = { \frac { 1 } { 6 } }
$$

and we are done.