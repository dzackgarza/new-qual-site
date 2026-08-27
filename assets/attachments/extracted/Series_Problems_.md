# Solutions to Assignment-2

Only submit the questions in red.

1. (a) For any two sequences $\left\{ a _ { n } \right\}$ and $\left\{ b _ { n } \right\}$ show that

$$
\operatorname* { l i m } _ { n \to \infty } ( a _ { n } + b _ { n } ) \leq \operatorname* { l i m } _ { n \to \infty } a _ { n } + \operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { } b _ { n } ,
$$

unless the right hand side is of the form $\infty - \infty ,$

Solution: Assume both the limsups are finite (the other cases are also similar). Let $A =$ lim $\begin{array} { r } { \operatorname* { s u p } _ { n \to \infty } a _ { n } , \ B = } \end{array}$ lim su ${ \mathrm { p } } _ { n \to \infty } b _ { n }$ and $L = \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } ( a _ { n } + b _ { n } )$ Suppose $L > A + B$ Choose an $\varepsilon > 0$ such that $L - \varepsilon > A + B + \varepsilon$ . For any $N > 0$ there exists an $n > N$ such that

$$
a _ { n } + b _ { n } > L - \varepsilon .\tag{0.1}
$$

On the other hand, there exists $N _ { 1 }$ such that for all $n > N _ { 1 }$

$$
a _ { n } < A + { \frac { \varepsilon } { 2 } } ,
$$

and there exists $N _ { 2 }$ such that for all $n > N _ { 2 }$

$$
b _ { n } < B + \frac { \varepsilon } { 2 } .
$$

But then if $N = \operatorname* { m a x } ( N _ { 1 } , N _ { 2 } )$ , then for any $n > N$ we have

$$
a _ { n } + b _ { n } < A + B + \varepsilon < L - \varepsilon ,
$$

contradicting (0.1).

(b) Find sequences $\left\{ a _ { n } \right\}$ and $\left\{ b _ { n } \right\}$ with strict inequality above.

Solution: Let $a _ { n } = ( - 1 ) ^ { n }$ and $b _ { n } = ( - 1 ) ^ { n - 1 }$ . Then $a _ { n } + b _ { n } = 0$ for all n, and so lim su ${ \mathrm { p } } _ { n \to \infty } ( a _ { n } +$ $b _ { n } ) = 0$ while, lim $\begin{array} { r } { \operatorname* { s u p } _ { n \to \infty } a _ { n } + \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } b _ { n } = 1 + 1 = 2 . } \end{array}$

2. Let $\left\{ a _ { n } \right\}$ be a sequence of real numbers, and let

$S = \{ x \in \mathbb { R } \mid \exists$ a sub-sequence $\boldsymbol { a } _ { n _ { k } }$ such that $a _ { n _ { k } } \xrightarrow { k  \infty } x \}$

(a) Show that $L =$ lim sup $a _ { n }$ if and only if $L = \operatorname* { s u p } S .$

Solution: Suppose $L = \operatorname* { l i m } \operatorname* { s u p } a _ { n }$ . First, we claim that $L \in S$ . To see this, note that by the equivalent characterization of limsup, there exists $n _ { 1 }$ such that

$$
a _ { n _ { 1 } } > L - 1 .
$$

```latex
Given $n _ { 1 }$ , there exists $n _ { 2 } > n _ { 1 }$ such that
$a _ { n _ { 2 } } > L - { \frac { 1 } { 2 } } .$
Having chosen $n _ { 1 } < n _ { 2 } < \cdots < n _ { k - 1 } ,$ let $n _ { K } > n _ { k - 1 }$ such that
$a _ { n _ { k } } > L - { \frac { 1 } { k } } .$
Claim. $a _ { n _ { k } } \ { \xrightarrow { k \to \infty } } L .$
Proof. Let $\varepsilon > 0 .$ . Then there exists N such that for all $n > N$
$a _ { n } < L + \varepsilon .$
Since $n _ { k } \xrightarrow { k  \infty }$ , there exists a $K _ { 1 }$ such that for all $k > K _ { 1 } , n _ { k } > N$ . In particular, for all
$k > K _ { 1 }$ ,
$a _ { n _ { k } } < L + \varepsilon .$
Let $K _ { 2 }$ such that $1 / K _ { 2 } < \varepsilon .$ . Then by our choice of the subsequence $\boldsymbol { a } _ { n _ { k } }$ , for all $k > K _ { 2 } .$
$a _ { n _ { k } } > L - \frac { 1 } { k } > L - \frac { 1 } { K _ { 2 } } > L - \varepsilon .$
In particular, if $K = \operatorname* { m a x } ( K _ { 1 } , K _ { 2 } )$ , and $k > K$ then
$| a _ { n _ { k } } - L | < \varepsilon ,$
and hence $a _ { n _ { k } } \ { \xrightarrow { k \to \infty } } L .$
This shows that $L \in S .$ In particular, $L \leq \operatorname* { s u p } S .$ Suppose $L < \operatorname { s u p } S .$ Let $\varepsilon > 0$ such that
$L + \varepsilon < \operatorname* { s u p } S .$ There exists an N such that for all $n > N$
$a _ { n } < L + \varepsilon ,$
and so for any $x \in S , x < L + \varepsilon .$ ε. Taking sup,
$\operatorname* { s u p } S \leq L + \varepsilon ,$
a contradiction. Hence $L = \operatorname* { s u p } S .$
```

(b) Formulate and prove the analogous statement for lim inf.   
Solution: The corresponding statement would be   
$\operatorname* { l i m } _ { n \to \infty } { \mathrm { i n f } } a _ { n } = { \mathrm { i n f } } S .$   
One can argue as above, or alternately, use the standard trick that if $b _ { n } = - a _ { n }$ , then   
$\operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } a _ { n } = - \operatorname* { l i m } _ { n \to \infty } b _ { n } .$

Note. From now on, you can use the conclusions of this exercise as a theorem. So now, you have a definition of lim sup and two other equivalent characterizations.

3. Find the lim sup and lim inf of the sequence $\left\{ a _ { n } \right\}$ defined recursively by

$$
a _ { 1 } = 0 , \ a _ { 2 m } = { \frac { a _ { 2 m - 1 } } { 2 } } , \ a _ { 2 m + 1 } = { \frac { 1 } { 2 } } + a _ { 2 m } .
$$

Justify your answers with complete proofs.

Solution: To get some intuition, we compute the first few terms of the sequence,

$$
a _ { 2 } = 0 , \ a _ { 3 } = { \frac { 1 } { 2 } } , \ a _ { 4 } = { \frac { 1 } { 4 } } , \ a _ { 5 } = { \frac { 3 } { 4 } } , \ a _ { 6 } = { \frac { 3 } { 8 } } , \ a _ { 7 } = { \frac { 7 } { 8 } } , \ a _ { 8 } = { \frac { 7 } { 1 6 } } , \ a _ { 9 } = { \frac { 1 5 } { 1 6 } } .
$$

Seeing a pattern, we make the claim -

Claim. lim i $\begin{array} { r } { \operatorname { r f } _ { n \to \infty } a _ { n } = \frac { 1 } { 2 } } \end{array}$ and lim s $\begin{array} { r } { \operatorname { l p } _ { n \to \infty } a _ { n } = 1 . } \end{array}$

Proof. The easiest proof is to simply find a formula for the $n ^ { t h }$ term. We claim that

$$
a _ { n } = \left\{ \begin{array} { l l } { \frac { 2 ^ { m } - 1 } { 2 ^ { m } } , ~ n = 2 m + 1 } \\ { \frac { 2 ^ { m - 1 } - 1 } { 2 ^ { m } } , ~ n = 2 m . } \end{array} \right.
$$

We prove this by induction. The base cases $n = 1$ are seen to be true. Suppose the formula is correct for some $n = 2 m - 1 = 2 ( m - 1 ) + 1$ . We then prove the formula for 2m and $2 m + 1 .$

$$
a _ { 2 m } = \frac { a _ { 2 m - 1 } } { 2 } = \frac { 2 ^ { m - 1 } - 1 } { 2 ^ { m } } .
$$

But then again by the recursion formula,

$$
a _ { 2 m + 1 } = { \frac { 1 } { 2 } } + a _ { 2 m } = { \frac { 1 } { 2 } } + { \frac { 2 ^ { m - 1 } - 1 } { 2 ^ { m } } } = { \frac { 2 ^ { m } - 1 } { 2 ^ { m } } } .
$$

Once we have the formula, note that $\{ a _ { 2 m + 1 } \}$ is a increasing to 1 and $\left\{ a _ { 2 m } \right\}$ is a sequence increasing to $1 / 2 .$ Then clearly, $u _ { N } = \operatorname* { s u p } \{ a _ { k } \ | \ k > N \} = 1$ , and $\begin{array} { r } { \dot { l _ { N } } = \operatorname* { i n f } \{ a _ { k } \ \dot { \mid } \ k > N \} > \frac { 2 ^ { N - 1 } - 1 } { 2 ^ { N } } } \end{array}$ . Letting $N \to \infty$ , we complete the proof of the claim.

4. (a) Let $\left\{ a _ { n } \right\}$ be a bounded sequence with the property that every convergent subsequence converges to the same limit a. Show that the entire sequence $\left\{ a _ { n } \right\}$ converges and $\operatorname* { l i m } _ { n \to \infty } a _ { n } = a .$

Solution: If not, then there exists an $\varepsilon > 0$ and a subsequence $b _ { k } = a _ { n _ { k } }$ such that   
$| b _ { k } - a | > \varepsilon$   
for all k. By Bozlano-Weierstrass, since $\left\{ b _ { k } \right\}$ is bounded, there exists a further sub-sequence   
$b _ { k _ { j } }$ which converges. But $b _ { k _ { j } } = a _ { n _ { k _ { j } } }$ is also a sub-sequence of $a _ { n }$ and since it converges, by   
the hypothesis, it must converge to a. But by our choice of $\{ b _ { k } \} , | b _ { k _ { j } } - a | > \varepsilon$ for all j, a   
contradiction.

(b) Now assume that $\left\{ a _ { n } \right\}$ is a sequence with the property that every subsequence has a further subsequence that converges to the same limit a. Show that the entire sequence $\left\{ a _ { n } \right\}$ converges and lim $_ { \substack { n  \infty } } a _ { n } = a .$

Solution: If not, then there is an $\varepsilon > 0$ and a sub-sequence $b _ { k } = a _ { n _ { k } }$ such that $| b _ { k } - a | > \varepsilon .$ By hypothesis, $b _ { k }$ has a subsequence, say $\{ b _ { k _ { j } } \}$ , that converges to a. But then

$$
\operatorname* { l i m } _ { j  \infty } | b _ { k _ { j } } - a | = 0 ,
$$

which contradicts the fact that $\left| b _ { k _ { j } } - a \right| > \varepsilon .$

5. Let $\{ a _ { n } \} _ { n = 0 } ^ { \infty }$ be a sequence of real numbers satisfying

$$
| a _ { n + 1 } - a _ { n } | \leq { \frac { 1 } { 2 } } | a _ { n } - a _ { n - 1 } | .
$$

Show that the sequence converges. Hint. Show that the sequence is Cauchy.

Solution: Inductively, we see that for any natural number $k ,$

$$
\vert a _ { k + 1 } - a _ { k } \vert \leq { \frac { 1 } { 2 ^ { k } } } \vert a _ { 1 } - a _ { 0 } \vert .
$$

Now if $m > n$ then by triangle inequality

$$
\left| a _ { m } - a _ { n } \right| = \left| a _ { m } - a _ { m - 1 } + a _ { m - 1 } - a _ { m - 2 } + a _ { m - 2 } - \cdot \cdot \cdot - a _ { n } \right|
$$

$$
\leq | a _ { m } - a _ { m - 1 } | + | a _ { m - 1 } - a _ { m - 2 } | + \cdots + | a _ { n + 1 } - a _ { n } |
$$

$$
\leq \left| a _ { 1 } - a _ { 0 } \right| \sum _ { k = n } ^ { m - 1 } { \frac { 1 } { 2 ^ { k } } }
$$

$$
\leq { \frac { | a _ { 1 } - a _ { 0 } | } { 2 ^ { n } } } \sum _ { k = 0 } ^ { \infty } { \frac { 1 } { 2 ^ { k } } }
$$

$$
\leq 2 ^ { - n } | a _ { 1 } - a _ { 0 } | .
$$

Given $\varepsilon > 0 ,$ , let $N$ such that $2 ^ { - N } | a _ { 1 } - a _ { 0 } | < \varepsilon$ . Then for any $m > n > N , | a _ { m } - a _ { n } | < \varepsilon$ , and the sequence is Cauchy.

6. Let ${ \cal S } = \{ n _ { 1 } , n _ { 2 } , \cdots \}$ denote the collection of those positive integers that do not have the digit 0 in their decimal representation. (For example $7 \in S$ but 101 $\notin \boldsymbol { S } )$ . Show that $\scriptstyle \sum _ { k = 1 } ^ { \infty } 1 / n _ { k }$ converges. Note. This should be a surprising result in that leaving out only a few (but of course still infinite) terms out of the harmonic series, we end up with a series that suddenly converges.

Solution: Consider the one-digit numbers in $S _ { ; }$ namely $\{ 1 , 2 , \cdots , 9 \}$ . Since each is bigger than one, the sum of reciprocals is

$$
1 + { \frac { 1 } { 2 } } \cdot \cdot \cdot + { \frac { 1 } { 9 } } < 9 .
$$

Next, consider the two-digit numbers in $S .$ There are 81 of them, and each is bigger than 10, and so the sum of reciprocals satisfies the estimate,

$$
{ \frac { 1 } { 1 1 } } + { \frac { 1 } { 1 2 } } + \cdots + { \frac { 1 } { 1 9 } } + { \frac { 1 } { 2 1 } } + \cdots + { \frac { 1 } { 9 8 } } + { \frac { 1 } { 9 9 } } < { \frac { 8 1 } { 1 0 } } .
$$

In general, consider the subset $S _ { k }$ of numbers in $S$ with $k$ digits, that is numbers between $1 0 ^ { k }$ and $1 0 ^ { k + 1 }$ . The number of such numbers is $9 ^ { k }$ . That is because there are $k$ digits, and each digit has 9 options. Moreover, all these numbers are bigger than $1 0 ^ { k }$ , and so

$$
\sum _ { n \in S _ { k } } { \frac { 1 } { n } } < { \frac { 9 ^ { k + 1 } } { 1 0 ^ { k } } } .
$$

Summing over the reciprocals of numbers with at-most m-digits,

$$
\sum _ { k = 1 } ^ { m } \sum _ { n \in S _ { k } } \frac { 1 } { n } < 9 \sum _ { k = 1 } ^ { m } \frac { 9 ^ { k } } { 1 0 ^ { k } } < \frac { 9 } { 1 0 } \sum _ { k = 0 } ^ { \infty } \frac { 9 ^ { k } } { 1 0 ^ { k } } < \frac { 8 1 } { 1 0 } \frac { 1 } { 1 - \frac { 9 } { 1 0 } } = 8 1 .
$$

In particular the partial sums of $\scriptstyle \sum _ { k = 1 } ^ { \infty } 1 / n _ { k }$ are bounded by 81 and since the terms in the series are positive by the monotone convergence theorem, the series converges.

7. The Fibonacci numbers $\{ f _ { n } \}$ are defined by

$$
f _ { 0 } = f _ { 1 } = 1 , { \mathrm { ~ a n d ~ } } f _ { n + 1 } = f _ { n } + f _ { n - 1 } { \mathrm { ~ f o r ~ } } n = 1 , 2 , \cdots .
$$

For $n = 1 , 2 , \cdots$ , we also define $r _ { n } = f _ { n + 1 } / f _ { n }$

(a) Find a formula for $r _ { n + 1 }$ in terms of $r _ { n }$ . Dividing the above recurrence by $f _ { n }$ , we obtain

$$
r _ { n } = 1 + { \frac { 1 } { r _ { n - 1 } } } ,
$$

or

$$
r _ { n + 1 } = 1 + { \frac { 1 } { r _ { n } } } .
$$

(b) Show that $f _ { n } \geq n$ for all $n \geq 2 .$

Solution: Easy proof by induction.

(c) Show that $f _ { n + 1 } f _ { n - 1 } - f _ { n } ^ { 2 } = ( - 1 ) ^ { n + 1 }$

Solution: We proceed by induction. For $n = 1 , f _ { n + 1 } f _ { n - 1 } - f _ { n } ^ { 2 } = f _ { 2 } f _ { 0 } - f _ { 1 } ^ { 2 } = 2 \cdot 1 - 1 ^ { 1 } = 1 =$ $( - 1 ) ^ { 1 + 1 }$ , and so the identity is verified. Suppose the identity is verified for $n - 1$ , that is we have $f _ { n } f _ { n - 2 } - f _ { n - 1 } ^ { 2 } = ( - 1 ) ^ { \bar { n } }$ . Then

$$
\begin{array} { l } { f _ { n + 1 } f _ { n - 1 } - f _ { n } ^ { 2 } = ( f _ { n } + f _ { n - 1 } ) f _ { n - 1 } - f _ { n } ^ { 2 } } \\ { \qquad = f _ { n - 1 } ^ { 2 } + f _ { n } ( f _ { n - 1 } - f _ { n } ) \qquad } \\ { \qquad = f _ { n - 1 } ^ { 2 } - f _ { n } f _ { n - 2 } = - ( - 1 ) ^ { n } = ( - 1 ) ^ { n + 1 } . } \end{array}
$$

(d) Hence show that if $n \geq 2 .$ , then

$$
| r _ { n + 1 } - r _ { n } | \leq { \frac { 1 } { ( n - 1 ) ^ { 2 } } } .
$$

Solution: Note that

$$
\left| { { r } _ { n } } - { { r } _ { n - 1 } } \right| = \left| \frac { { { f } _ { n + 1 } } } { { { f } _ { n } } } - \frac { { { f } _ { n } } } { { { f } _ { n - 1 } } } \right| = \frac 1 { { { f } _ { n } } { { f } _ { n - 1 } } }
$$

by the identity. By part (b), $f _ { n } \ > \ n$ for all $n \geq 2$ and so the proof is completed by the elementary observation that $( n - 1 ) ^ { 2 } < n ( n - 1 )$ .

(e) Hence show that the sequence of ratios $\{ r _ { n } \}$ converge, and compute it’s limit. Note. This limit is the so-called golden ratio.

Solution: For any $n < m ,$ by the triangle inequality and part(d),

$$
| r _ { m } - r _ { n } | \leq { \frac { 1 } { n ^ { 2 } } } + { \frac { 1 } { ( n + 1 ) ^ { 2 } } } + \cdots \frac 1 { ( m - 1 ) ^ { 2 } } .
$$

Since the right hand side is the tail end of a converging series, by the Cauchy criteria, for any $\varepsilon > 0 ,$ there exists an N such that for any $n , m > N$ , the right hand side can be made smaller than ε. This shows that $\left\{ r _ { n } \right\}$ is Cauchy, and hence converges. To find the actual limit, first note that if $L = \operatorname* { l i m } _ { n \to \infty } r _ { n } .$ , then $L \neq 0$ . letting $n \to \infty$ on both sides of the recurrence obtained in part(a) we obtain

$$
L = 1 + { \frac { 1 } { L } } .
$$

Solving the quadratic $L ^ { 2 } - L - 1 = 0$ , we see that the roots are $( 1 \pm { \sqrt { 5 } } ) / 2$ , of which the only positive root has to be L.

8. Investigate the behavior of each series (convergence, divergence, conditional convergence, absolute convergence). In cases that there is a parameter $( p , q { \mathrm { ~ o r ~ } } r )$ find the range of values where the series exhibits the above behavior.

1. $\textstyle \sum _ { n = 1 } ^ { \infty } p ^ { n } n ^ { p } \ ( p > 0 )$

$$
4 . \ \sum _ { n = 1 } ^ { \infty } \frac { n ! } { n ^ { n } }
$$

2. $\textstyle \sum _ { n = 1 } ^ { \infty } ( - 1 ) ^ { n } { \frac { { \sqrt { n + 1 } } - { \sqrt { n } } } { n ^ { p } } }$

3. $\textstyle \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { p ^ { n } - q ^ { n } } } , \ ( 0 < q < p )$

5. $\scriptstyle \sum _ { n = 1 } ^ { \infty } ( { \sqrt [ n ] { n } } - 1 ) ^ { n }$

6. $\scriptstyle \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { 1 + r ^ { n } } } .$

## Solution:

1. Let $a _ { n } = p ^ { n } n ^ { p }$ . Then $\sqrt [ n ] { a _ { n } } = p n ^ { p / n } \xrightarrow [ n  \infty ] { n  \infty } p$ . So by the root test, the series converges if $p < 1$ and diverges if $p > 1$ . If $p = 1$ , the series $\textstyle \sum n$ clearly diverges.

2. Let $\textstyle a _ { n } = ( - 1 ) ^ { n } { \frac { { \sqrt { n + 1 } } - { \sqrt { n } } } { n ^ { p } } }$ . Then

$$
\vert a _ { n } \vert = \frac { 1 } { n ^ { p } ( \sqrt { n + 1 } + \sqrt { n } ) } .
$$

Comparing this with $n ^ { - ( p + \frac { 1 } { 2 } ) }$ , we see that $\sum a _ { n }$ converges absolutely for $p > 1 / 2$ . On the other hand when $p < 0 ,$ clearly the series diverges. At $p = 0 ,$ the partial sums of the series are $\begin{array} { r } { s _ { n } = \sum _ { k = 1 } ^ { n } \sqrt { k + 1 } - \sqrt { k } = \sqrt { n + 1 } - 1 } \end{array}$ which clearly diverge. For $p \in ( 0 , 1 / 2 ]$ the series does not converge absolutely. To check for conditional convergence we apply alternating series test. Let $\begin{array} { r } { b _ { n } = \frac { \sqrt { n + 1 } - \sqrt { n } } { n ^ { p } } = \frac { 1 } { n ^ { p } ( \sqrt { n + 1 } + \sqrt { n } ) } } \end{array}$ , and hence decreases to 0 if $p > 0$ . So by the alternating series test the series converges conditionally in the range $p \in ( 0 , 1 / 2 ]$

## 3. We can write

$$
a _ { n } = \frac { 1 } { p ^ { n } - q ^ { n } } = \frac { 1 } { p ^ { n } ( 1 - ( q / p ) ^ { n } ) } .
$$

Since $q < p , \operatorname* { l i m } _ { n \to \infty } ( q / p ) ^ { n } = 0$ , and so there exists an N such that for all $n > N , ( q / p ) ^ { n } < 1 / 2$ or $( 1 - ( q / p ) ^ { n } ) ^ { - 1 } < 2$ . On the other hand, for any n, $( 1 - ( q / p ) ^ { n } ) ^ { - 1 } > 1$ , and so for $n > N$

$$
\frac { 1 } { p ^ { n } } < a _ { n } < \frac { 2 } { p ^ { n } } .
$$

By comparison test the series converges if $p > 1$ and diverges if $0 < p \leq 1$

4. We use the ratio test. If $a _ { N } = n ^ { n } / n !$ , then

$$
{ \frac { a _ { n + 1 } } { a _ { n } } } = { \frac { ( n + 1 ) ^ { n + 1 } } { n ^ { n } ( n + 1 ) } } = { \frac { ( n + 1 ) ^ { n } } { n ^ { n } } } = \left( 1 + { \frac { 1 } { n } } \right) ^ { n } { \xrightarrow { n \to \infty } } e > 1 ,
$$

and so the series diverges.

5. We use root test. Let $a _ { n } = ( \sqrt [ n ] { n } - 1 ) ^ { n }$ . Then

$$
\sqrt [ n ] { a } _ { n } = \sqrt [ n ] { n } - 1 \xrightarrow [ n ] { n \to \infty } 0 < 1 ,
$$

and so the series converges.

6. Let $a _ { n } = ( 1 + r ^ { n } ) ^ { - 1 } . { \mathrm { ~ I f ~ } } | r | \leq 1$ , then $\left\{ a _ { n } \right\}$ does not converge to zero, and so the series diverges. If $| r | > 1$ , lim $_ { n \to \infty } r ^ { - n } = 0$ , and so there exists an $N \in \mathbb { N }$ such that $1 + r ^ { - n } > 1 / 2$ for all $n > N$ (note that r could be negative, or else $1 + r ^ { - n }$ is of course bigger than 1). Then for $n > N$

$$
| a _ { n } | = { \frac { | r | ^ { - n } } { 1 + r ^ { - n } } } < { \frac { 2 } { | r | ^ { n } } } ,
$$

and so by limit comparison test, the series is absolutely convergent for $| r | > 1 .$

9. (a) Let $\left\{ a _ { n } \right\}$ be a sequence of of positive real numbers. Show that

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } _ { a _ { n } } \frac { a _ { n + 1 } } { a _ { n } } \leq \operatorname* { l i m } _ { n \to \infty } \operatorname { i n f } _ { \varnothing _ { n } } ^ { \varnothing } \sqrt { a } _ { n } \leq \operatorname* { l i m } _ { n \to \infty } \operatorname { s u p } _ { \varnothing _ { n } } ^ { \varnothing } \frac { a _ { n + 1 } } { { n } \to { \infty } } .
$$

You may assume that each of the quantities is finite, even though the result holds true for extended reals. Hint. Proceed by contradiction. For instance, for the rightmost inequality, let $\begin{array} { r } { U = \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } \frac { a _ { n + 1 } } { a _ { n } } } \end{array}$ and $L = \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } \sqrt [ n ] { a } _ { n }$ and suppose $L > U$ . Then use the equivalent characterizations of lim sup to draw a contradiction.

Solution: We will show that

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname { \sqrt [ { n } ] { a _ { n } } } \leq \operatorname* { l i m } _ { n \to \infty } \operatorname* { a } _ { a _ { n } } .
$$

The other inequalities also follow in a similar fashion. Denote $L =$ lim su $\mathrm { p } _ { n \to \infty } \sqrt [ n ] { a } _ { n }$ and $\begin{array} { r } { U = \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } \frac { a _ { n + 1 } } { a _ { n } } } \end{array}$ . We proceed by contradiction, so suppose $L > U$ . Let $\beta \in ( U , L )$ . Then there exists an N such that for all $n > N$

$$
\displaystyle { \Big | \frac { a _ { n + 1 } } { a _ { n } } \Big | < \beta , }
$$

or equivalently, $| a _ { n + 1 } | < \beta | a _ { N } |$ . Inductively, one can conclude that $| a _ { n } | < \beta ^ { n - N } | a _ { N } | .$ . That is, for any $n > N$ ,

$$
| a _ { n } | ^ { 1 / n } < \beta ^ { 1 - N / n } | a _ { N } | ^ { 1 / n } .
$$

Now N is fixed, so taking limsup on both sides, since lim $\ L _ { \cdot n \to \infty } \beta ^ { 1 - N / n } | a _ { N } | ^ { 1 / n } = \beta ,$ we see that

$$
\operatorname* { l i m } _ { n \to \infty } | a _ { n } | ^ { 1 / n } \leq \beta ,
$$

which is a contradiction.

(b) Show that if $\sum a _ { n }$ converges by the ratio test, then $\sum a _ { n }$ also converges by the root test.

Solution: If $\sum a _ { n }$ converges by the ratio test, then lim $\begin{array} { r } { \operatorname* { s u p } _ { n  \infty } | a _ { n \pm 1 } / a _ { n } | < 1 } \end{array}$ . But then by the above set of inequalities, we necessarily have that lim $\begin{array} { r } { \operatorname* { s u p } _ { n  \infty } \sqrt [ n ] { | a _ { n } | } < 1 } \end{array}$ , and so the series also converges by the root test.

(c) Consider the sequence $\{ a _ { n } \} _ { n = 0 } ^ { \infty } ,$

$$
a _ { n } = { \frac { 1 } { 2 ^ { n + ( - 1 ) ^ { n } } } } = { \left\{ \begin{array} { l l } { { \frac { 1 } { 2 ^ { n - 1 } } } , \ n { \mathrm { ~ i s ~ o d d } } } \\ { { \frac { 1 } { 2 ^ { n + 1 } } } , \ n { \mathrm { ~ i s ~ e v e n . } } } \end{array} \right. }
$$

Compute (with proper justifications) lim sup $\sqrt [ n ] { \left| a _ { n } \right| }$ and lim sup $\left| a _ { n + 1 } / a _ { n } \right|$ . Show that the series converges by the root test. Does the ration test work?

Solution: Note that

$$
\sqrt [ n ] { | a _ { n } | } = \frac { 1 } { 2 ^ { 1 + ( - 1 ) ^ { n } / n } } \xrightarrow [ ] { n \to \infty } \frac { 1 } { 2 } ,
$$

and so lim sup $\sqrt [ n ] { | a _ { n } | } = 1 / 2$ . On the other hand,

$$
{ \frac { a _ { n + 1 } } { a _ { n } } } = { \left\{ \begin{array} { l l } { { \frac { 1 } { 8 } } , \ n { \mathrm { ~ i s ~ o d d } } } \\ { 2 , \ n { \mathrm { ~ i s ~ e v e n } } , } \end{array} \right. }
$$

and so lim sup $| a _ { n + 1 } / a _ { n } | = 2$ and lim inf $| a _ { n + 1 } / a _ { n } | = 1 / 8$ Since lim sup $\sqrt [ n ] { | a _ { n } | } = 1 / 2 < 1$ , the root test says that the series $\sum a _ { n }$ converges. On the other hand since

$$
\operatorname* { l i m } \operatorname* { i n f } { \bigg | } { \frac { a _ { n + 1 } } { a _ { n } } } { \bigg | } < 1 < \operatorname* { l i m } \operatorname* { s u p } { \bigg | } { \frac { a _ { n + 1 } } { a _ { n } } } { \bigg | } ,
$$

the ratio test is inconclusive.

(d) Let $b _ { n } = n ^ { n } / n !$ . Show that

$$
\operatorname* { l i m } _ { n \to \infty } \sqrt [ n ] { b _ { n } } = e .
$$

Hint. It is easier to compute the limiting ratios.

Solution: Note that

$$
{ \frac { a _ { n + 1 } } { a _ { n } } } = { \frac { ( n + 1 ) ^ { n + 1 } n ! } { ( n + 1 ) ! n ^ { n } } } = { \frac { ( n + 1 ) ^ { n + 1 } } { ( n + 1 ) n ^ { n } } } = { \frac { ( n + 1 ) ^ { n } } { n ^ { n } } } = \left( 1 + { \frac { 1 } { n } } \right) ^ { n } { \xrightarrow { n \to \infty } } e .
$$

So lim in $\begin{array} { r } { \mathrm { f } _ { n \to \infty } \frac { a _ { n + 1 } } { a _ { n } } = \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } \frac { a _ { n + 1 } } { a _ { n } } = e . } \end{array}$ . But then by the chain of inequalities in the first part the middle two terms are also equal, that is, lim in $\begin{array} { r } { \mathrm { f } _ { n \to \infty } \sqrt [ n ] { a } _ { n } = \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } \sqrt [ n ] { a } _ { n } = e , } \end{array}$ and so

$$
\operatorname* { l i m } _ { n \to \infty } \sqrt [ n ] { a _ { n } } = e .
$$

10. (a) Show that if $a _ { n } > 0$ , and lim $_ { 1 _ { n  \infty } n a _ { n } } = l \neq 0$ , then $\sum a _ { n }$ diverges.

Solution: Since $n a _ { n }  l \neq 0 .$ applying the definition of convergence with $\varepsilon = | l | / 2 > 0$ , there exists $N \in \mathbb N$ such that

$$
n > N \implies | n a _ { n } - l | < \frac { | l | } { 2 } .
$$

In particular, for $n > N , a _ { n } > | l | / 2 n$ . By the comparison test, since $\textstyle \sum 1 / n$ diverges, it follows that $\sum a _ { n }$ also diverges.

(b) Given that $\sum a _ { n }$ converges absolutely, show that $\sum a _ { n } ^ { p }$ also converges whenever $p > 1$ Give a   
counterexample, if $\sum a _ { n }$ only converges conditionally.   
Solution: Since $\sum a _ { n }$ converges absolutely, by the divergence test, $\left| a _ { n } \right| \to 0$ . In particular,   
there exists N such that for all $n > N , | a _ { n } | < 1$ But then for any $p > 1 , | a _ { n } | ^ { p } < | a _ { n } |$ when   
$n > N$ By comparison test, $\sum | a _ { n } | ^ { p }$ converges, and hence $\sum a _ { n } ^ { p }$ also converges. This is not   
true $\operatorname { i f } \sum a _ { n }$ only converges conditionally. For instance, consider $a _ { n } = ( - 1 ) ^ { n } / { \sqrt { n } }$ and $p = 2$ .   
11. Consider each of the following propositions. Provide short proofs for those that are true and counterex  
amples for any that are not.   
(a) $\operatorname { I f } \sum a _ { n }$ converges and the sequence $\left\{ b _ { n } \right\}$ also converges, then $\sum a _ { n } b _ { n }$ converges.   
(b) $\operatorname { I f } \sum a _ { n }$ converges conditionally, then $\textstyle \sum n ^ { 2 } a _ { n }$ diverges.   
Solution: The proposition is true. If not, then $\textstyle \sum n ^ { 2 } a _ { n }$ converges, and so li $\ O _ { 1 } \ l _ { n } \to \infty \ l _ { } n \ l ^ { 2 } a _ { n } = 0 .$   
In particular, there exists N such that for all $n > \overline { { N } } , | a _ { n } | < 1 / n ^ { 2 } .$ and so $\sum a _ { n }$ must converge   
absolutely by the comparison test. A contradiction!   
(c) If $\left\{ a _ { n } \right\}$ is a decreasing sequence, and $\sum a _ { n }$ converges, then $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } n a _ { n } = 0 . } \end{array}$   
Solution: The proposition is true. Since $\sum a _ { n }$ is convergent, lim $\iota _ { n \to \infty } a _ { n } = 0$ . But then since   
$a _ { n }$ is also decreasing, it follows that $a _ { n } \geq 0 .$ . By the Cauchy criteria, given any $\varepsilon > 0$ , there   
exists an N such that for all $n > m > N$ ,   
$\sum _ { k = m } ^ { n } a _ { k } < { \frac { \varepsilon } { 2 } } .$   
Applying this to $m = \lfloor n / 2 \rfloor$ with $n > 2 N .$ , and using the fact that $a _ { n }$ decreases   
${ \frac { \varepsilon } { 2 } } > \sum _ { \substack { n = 1 \ldots / { n } \mid 0 \mid } } ^ { n } a _ { k } > { \frac { n a _ { n } } { 2 } } .$   
k=bn/2c   
So given $\varepsilon > 0 , { \mathrm { i f } } n > 2 N$ , then $| n a _ { n } | < \varepsilon$ , and hence $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } n a _ { n } = 0 . } \end{array}$   
12. (a) For any $n \in \mathbb { N } ,$ , show that the function $p _ { n } ( x ) = x ^ { n }$ is continuous on all of R. Show the explicit   
dependence of δ on ε and the point that you are looking at.   
Solution: We prove continuity at $x = a .$ . Let $\varepsilon > 0$ be given. We need to estimate   
$| p _ { n } ( x ) - p _ { n } ( a ) | = | x ^ { n } - a ^ { n } |$   
$= | x - a | | x ^ { n - 1 } + x ^ { n - 2 } a + \cdot \cdot \cdot + a ^ { n - 1 } | .$   
Now, $| x - a | < \delta ,$ where $\delta > 0$ is to be chosen. Suppose, we choose $\delta \ < \ 1 .$ , then clearly   
$| x | < | a | + 1 . { \textrm { A } }$ general term on the right is of the form $x ^ { j } a ^ { n - 1 - j }$ for $j = 0 , \cdots , n - 1$ . So if   
$\delta < 1$ , we have   
$| x ^ { j } a ^ { n - 1 - j } | < ( | a | + 1 ) ^ { j } | a | ^ { n - 1 - j } < ( | a | + 1 ) ^ { n - 1 } .$   
Then by triangle inequality,   
$| x ^ { n - 1 } + x ^ { n - 2 } a + \cdot \cdot \cdot + a ^ { n - 1 } | < n ( 1 + | a | ) ^ { n - 1 } .$

So if $\delta < 1$ and $| x - a | < \delta ,$ then

$$
| p _ { n } ( x ) - p _ { n } ( a ) | < n \delta ( 1 + | a | ) ^ { n - 1 } .
$$

Our aim is to make this smaller than $\varepsilon ,$ and so simply choose

$$
\delta < { \frac { \varepsilon } { n ( 1 + | a | ) ^ { n - 1 } } } .
$$

Together with $\delta < 1$ , we see that if

$$
\delta = \operatorname* { m i n } \Big ( 1 , \frac { \varepsilon } { n ( 1 + | a | ) ^ { n - 1 } } \Big ) ,
$$

then

$$
| x - a | < \delta \implies | p _ { n } ( x ) - p _ { n } ( a ) | < \varepsilon .
$$

(b) Show that $f ( x ) = { \sqrt { x } }$ is continuous on $( 0 , \infty )$

Solution: Let $\varepsilon > 0 ,$ and $| x - a | < \delta$ for some $\delta > 0$ to be chosen later. Clearly

$$
| { \sqrt { x } } - { \sqrt { a } } | = { \frac { | x - a | } { | { \sqrt { x } } + { \sqrt { a } } | } } < { \frac { \delta } { | { \sqrt { x } } + { \sqrt { a } } | } } .
$$

Now, $a > 0 ,$ by choosing $\delta < a / 2 ,$

$$
| x - a | < \delta \implies x > a / 2 .
$$

So

$$
{ \sqrt { x } } + { \sqrt { a } } > 3 { \sqrt { a } } / 2 ,
$$

and

So simply pick

$$
| { \sqrt { x } } - { \sqrt { a } } | < { \frac { 2 \delta } { 3 { \sqrt { a } } } } .
$$

$$
\delta = \operatorname* { m i n } { \left( { \frac { a } { 2 } } , { \frac { 3 { \sqrt { a } } } { 2 } } \varepsilon \right) } .
$$

(c) Show that $f _ { n } ( x ) = x ^ { 1 / n }$ is continuous on $( 0 , \infty )$

Solution: Again, we prove continuity at $x = a .$ . Let $\varepsilon > 0 .$ . From the identity, we see that

$$
x - a = ( x ^ { 1 / n } - a ^ { 1 / n } ) ( x ^ { 1 - 1 / n } + x ^ { 1 - 2 / n } a ^ { 1 / n } \cdot \cdot \cdot + a ^ { 1 - 1 / n } )
$$

Then

$$
| f _ { n } ( x ) - f _ { n } ( a ) | = { \frac { | x - a | } { | x ^ { 1 - 1 / n } + x ^ { 1 - 2 / n } a ^ { 1 / n } \cdots + a ^ { 1 - 1 / n } | } } .
$$

Again as before, since $a > 0 ,$ if $\delta < a / 2$ , then $x > a / 2$ and so

$$
x ^ { 1 - 1 / n } + x ^ { 1 - 2 / n } a ^ { 1 / n } \cdot \cdot \cdot + a ^ { 1 - 1 / n } > n a ^ { 1 - 1 / n } c _ { n } ,
$$

where $c _ { n }$ is the constant (independent of a)

$$
c _ { n } = 2 ^ { 1 - 1 / n } + 2 ^ { 1 - 2 / n } + \cdot \cdot \cdot + 1 .
$$

And so $\mathrm { i f ~ } | x - a | < \delta$ and $\delta < a / 2$ we have

$$
| f _ { n } ( x ) - f _ { n } ( a ) | < { \frac { \delta } { n c _ { n } a ^ { 1 - 1 / n } } } .
$$

So simply pick

$$
\delta = \operatorname* { m i n } \left( { \frac { a } { 2 } } , \ n c _ { n } a ^ { 1 - 1 / n } \varepsilon \right) .
$$

Hint. For all parts the following identity might be useful.

$$
a ^ { n } - b ^ { n } = ( a - b ) ( a ^ { n - 1 } + a ^ { n - 2 } b + \cdot \cdot \cdot + a b ^ { n - 2 } + b ^ { n - 1 } ) .
$$