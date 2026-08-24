Name:

Student ID#:

<table><tr><td rowspan=1 colspan=1>Problems/Page Numbers</td><td rowspan=1 colspan=1>Total Points</td><td rowspan=1 colspan=1>Your Score</td></tr><tr><td rowspan=1 colspan=1>Problem 1 / Page 2-3</td><td rowspan=1 colspan=1>40 Points</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 2 / Page 4</td><td rowspan=1 colspan=1>20 Points</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 3 / Page 5</td><td rowspan=1 colspan=1>20 Points</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 4 / Page 6</td><td rowspan=1 colspan=1>20 Points</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 5Page 7</td><td rowspan=1 colspan=1>20 Points</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 6 / Page 8</td><td rowspan=1 colspan=1>20 Points</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 7 /Page 9</td><td rowspan=1 colspan=1>20 Points</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 8 / Page 10</td><td rowspan=1 colspan=1>20 Points</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Total: 8 Problems / 10 Pages</td><td rowspan=1 colspan=1>Total: 180 Points</td><td rowspan=1 colspan=1></td></tr></table>

## General Instructions

1. This is a three-hour, closed-book, closed-note, and no-calculator exam. There are 8 problems of total 180 points.

2. Be sure to carefully motivate all (nontrivial) claims and statements. Be sure also to clearly explain and justify your answers.

3. You may cite without proof any results proved in the text or in the class, as long as they are not what the problem explicitly asks you to prove. You may also use the results of prior problems or prior parts of the same problem when solving a problem.

4. If you cite a result (a theorem, lemma, etc.) that is proved in the text or class, refer to it either by name (if it has one) or explain clearly what it states and verify explicitly all the hypotheses.

Notation: m is the Lebesgue measure.

Problem 1 (40 points). Determine if the statements below are True or False. If True, give a brief proof. If False, give a counterexample or prove your assertion in a different way as you prefer. If your claim follows from a theorem in the text, name the theorem or describe it otherwise, and explain carefully how the conclusion follows.

(a) (10 points) In an infinite-dimensional Hilbert space H, for any weakly convergent sequence $\{ x _ { n } \}$ , there exists a subsequence that is convergent with respect to the norm.

(b) (10 points) Since two iterated integrals exist and

$$
\int _ { ( 0 , 1 ) } \int _ { ( 0 , 1 ) } { \frac { x ^ { 2 } - y ^ { 2 } } { ( x ^ { 2 } + y ^ { 2 } ) ^ { 2 } } } d m ( x ) d m ( y ) = \int _ { ( 0 , 1 ) } \int _ { ( 0 , 1 ) } { \frac { x ^ { 2 } - y ^ { 2 } } { ( x ^ { 2 } + y ^ { 2 } ) ^ { 2 } } } d m ( y ) d m ( x )
$$

we can conclude, via the Tonelli-Fubini theorem, that the double integral exists.

(c) (10 points) There exists a function $f \geq 0 \mathrm { o n } \left( 0 , \infty \right)$ such that $f \in L ^ { p } ( ( 0 , \infty ) )$ if and only if $p = 1$

(d) (10 points)

$$
\operatorname* { l i m } _ { n  \infty } \int _ { 0 } ^ { \infty } { \frac { \sin ( { \frac { x } { n } } ) } { ( 1 + { \frac { x } { n } } ) ^ { n } } } d m ( x ) = 0
$$

Problem 2 (20 points). Let $( X , M , \mu )$ be a measure space. Prove that for any $0 < p < \infty$ $f \in L ^ { p }$ if and only if

$$
\sum _ { k = - \infty } ^ { \infty } 2 ^ { k p } \lambda _ { f } ( 2 ^ { k } ) < \infty
$$

where $\lambda _ { f } ( \alpha ) = \mu ( \{ x | | f | ( x ) > \alpha \} )$

Problem 3 (20 points). Let X be a locally compact Hausdorff space. Let Y be a closed subspace and $\mu$ be a Radon measure on Y . Define a linear functional on $C _ { c } ( X )$ by $\begin{array} { r } { I ( f ) = \int _ { Y } ( f | _ { Y } ) d \mu } \end{array}$

Prove that (i) I(f ) is a positive linear functional;

(ii) The functional $\textstyle I ( f ) = \int _ { X } f d \nu$ induces a Randon measure ν (via the Riesz-Markov theorem) which satisfies that

$$
\nu ( E ) = \mu ( E \cap Y ) .
$$

Precisely you need to show that (a) ν as defined above is a Randon measure; (b) the linear functional $I ( f )$ can be represented by $\int _ { X } f d \nu$

Problem 4 (20 points). Let X and Y be two Banach spaces and denote by $L ( X , Y )$ the space of all continuous linear operators from X to Y. Let $A _ { n } \in L ( X , Y ) ( n = 1 , 2 , . . . )$ Assume that lim $\scriptstyle \ldots \to \infty { \cal A } _ { n } ( x )$ exists for each $x \in X$ . Define $A ( x ) = \operatorname* { l i m } _ { n \to \infty } A _ { n } ( x )$ . Prove that $A \in L ( X , Y )$

Problem 5 (20 points). Let f be a real-valued function of bounded variation on R, and g be a smooth function of compact support on R. Is the integration by parts

$$
\int _ { - \infty } ^ { \infty } f ( x ) g ^ { \prime } ( x ) \ d m ( x ) = - \int _ { - \infty } ^ { \infty } f ^ { \prime } ( x ) g ( x ) d m ( x )
$$

always valid?

If yes, give a proof of it; if not, show a counter-example and find a condition under which it is valid (you need to justify your answer).

Problem 6 (20 points). Let $g _ { k } = \chi _ { [ - 1 , 1 ] } * \chi _ { [ - k , k ] }$ . Here $f * g$ is the convolution of $f$ and $g .$

(i) Compute $\| g _ { k } \| _ { L ^ { \infty } }$

(ii) Compute the inverse Fourier transform of $g _ { k }$ , namely ${ \mathcal { F } } ^ { - 1 } ( g _ { k } )$

(iii) Using the above computation show that the Fourier transform $\mathcal { F } : L ^ { 1 } ( \mathbb { R } ) \to C _ { 0 } ( \mathbb { R } )$ is not onto. Here $C _ { 0 } ( \mathbb { R } )$ is the space of the continuous functions which vanishes at the infinity (namely for any $f \in C _ { 0 } ( \mathbb { R } )$ , and $\epsilon > 0 , \{ x | | f | ( x ) \ge \epsilon \}$ is compact). Hint: Use the open mapping theorem.

Problem 7 (20 points). Let $X = [ - \pi , \pi ]$ and consider the Lebesgue measure. Let p be a real number with $1 \leq p < \infty$ . Define for each integer $k \geq 1$ that $f _ { k } ( x ) = \sin ( k x ) \ ( x \in X )$

(a) Prove that the sequence $\{ f _ { k } \}$ converges weakly to 0 in $L ^ { p } ( X )$

(b) Prove that the sequence $\{ f _ { k } \}$ does not converge to 0 strongly in $L ^ { p } ( X )$

Problem 8 (20 points). Let $f$ be a $C ^ { n }$ function on $[ 0 , + \infty )$ . Compute the distributional n-th derivative of $g ( x ) = f ( | x | )$ (which is viewed as a distribution of R). You may express your answer in terms of the delta distribution.

Hint: You may use the induction on n to prove the general formula which you may guess after working out the answer for $n = 1 , 2 , 3 ,$ ....