## Week 6: Miscellaneous Topics (Analysis, Topology, Probability, etc) Practice Problem Solutions

Problem 1. Where is the function $f ( x ) = { \left\{ \begin{array} { l l } { x / 2 , } & { x \in \mathbb { Q } } \\ { x / 3 , } & { x \in \mathbb { R } \setminus \mathbb { Q } } \end{array} \right\} }$ continuous?

Solution. The given function is continuous only at $x \ = \ 0$ Indeed, if $x \neq 0$ , then take two sequences $\{ q _ { n } \} \subset \mathbb { Q }$ and $\{ r _ { n } \} \subset \mathbb { R } \setminus \mathbb { Q }$ approaching x (we can find each sequence since both $\mathbb { Q }$ and R \ Q are dense in R) and we will find that

$$
{ \frac { x } { 2 } } = \operatorname* { l i m } _ { n \to \infty } f ( q _ { n } ) \neq \operatorname* { l i m } _ { n \to \infty } f ( r _ { n } ) = { \frac { x } { 3 } } ,
$$

which shows that f is discontinuous by the sequential criterion theorem. Now at $x = 0$ , we can take any $\varepsilon > 0$ and set $\delta = \varepsilon / 3$ to find that $| f ( x ) - f ( 0 ) | < \varepsilon$ when $| x - 0 | < \delta$ , which shows that $f$ is continuous at $x = 0$

More generally, if $D \subset \mathbb { R }$ is such that D and $\mathbb { R } \backslash D$ are both dense in R (which is true when $D = \mathbb { Q } )$ and we define

$$
f ( x ) = { \left\{ \begin{array} { l l } { g ( x ) , } & { x \in D } \\ { h ( x ) , } & { x \in \mathbb { R } \setminus D } \end{array} \right\} }
$$

where $g , h : \mathbb { R }  \mathbb { R }$ are continuous, then f will be continuous at $x \in \mathbb { R } { \mathrm { ~ i f f ~ } } g ( x ) = h ( x )$

Problem 2. Fix $x > 0$ . Give a rigorous meaning to $\sqrt { x + { \sqrt { x + { \sqrt { x + \cdots } } } } }$ by proving that the sequence

$$
a _ { 0 } = \sqrt { x } , \quad a _ { n } = \sqrt { x + a _ { n - 1 } } , \ n = 1 , 2 , 3 , \dots .
$$

converges and finding the limit. What happens as $x \searrow 0 ?$

Solution. We prove that $a _ { n }$ is increasing an bounded above, and thus converges by the monotone convergence theorem. Note that $a _ { 1 } = { \sqrt { x + { \sqrt { x } } } } \geq { \sqrt { x } } = a _ { 0 }$ . Now assume that $a _ { n } \geq a _ { n - 1 }$ for some $n \in \mathbb { N }$ . Then

$$
x + a _ { n } \geq x + a _ { n - 1 } \implies \sqrt { x + a _ { n } } \geq \sqrt { x + a _ { n - 1 } } \implies a _ { n + 1 } \geq a _ { n } .
$$

This induction proves that $a _ { n }$ is an increasing sequence.√ √

Next, we see that $\begin{array} { r } { a _ { 0 } = \sqrt { x } = \frac { \sqrt { 4 x } } { 2 } \le \frac { 1 + \sqrt { 1 + 4 x } } { 2 } } \end{array}$ . Again, assume that $\textstyle a _ { n } \leq { \frac { 1 + { \sqrt { 1 + 4 x } } } { 2 } }$ for some $n \in \mathbb { N }$ . Note that

$$
\left( { \frac { 1 + { \sqrt { 1 + 4 x } } } { 2 } } \right) ^ { 2 } = { \frac { 1 + 2 { \sqrt { 1 + 4 x } } + 1 + 4 x } { 4 } } = x + { \frac { 1 + { \sqrt { 1 + 4 x } } } { 2 } } .
$$

Then

$$
a _ { n + 1 } = { \sqrt { x + a _ { n } } } \leq { \sqrt { x + { \frac { 1 + { \sqrt { 1 + 4 x } } } { 2 } } } } = { \sqrt { \left( { \frac { 1 + { \sqrt { 1 + 4 x } } } { 2 } } \right) ^ { 2 } } } = { \frac { 1 + { \sqrt { 1 + 4 x } } } { 2 } } .
$$

This shows by induction that $a _ { n }$ is bounded above. Hence there is a limit $a _ { n }  a \in \mathbb { R }$ . Taking the limit on both sides of the recursive relationship, we see

$$
a = { \sqrt { x + a } } \implies a ^ { 2 } - a - x = 0 \implies a = { \frac { 1 \pm { \sqrt { 1 + 4 x } } } { 2 } } .
$$

Note that each member of the sequence is positive and thus the limit is positive, and so we can ignore the false root. This shows that for $x > 0$ ,

$$
{ \sqrt { x + { \sqrt { x + { \sqrt { x + \cdots } } } } } } = { \frac { 1 + { \sqrt { 1 + 4 x } } } { 2 } } .
$$

However, this formula fails for $x = 0$ . If $x = 0$ , then $a _ { n } = 0$ for all n and thus the limit is zero, which does not agree with the limit of the above formula as x $\searrow 0$

Problem 3. Which of the following does not define a metric on R?

$$
\begin{array} { r l } & { \mathrm { ( A ) } \ \delta ( x , y ) = \left\{ \begin{array} { l l } { 0 , x = y , } \\ { 2 , x \neq y . } \end{array} \right. \quad \mathrm { ( B ) } \ \rho ( x , y ) = \operatorname* { m i n } \{ | x - y | , 1 \} \quad \mathrm { ( C ) } \ \sigma ( x , y ) = \frac { | x - y | } { 3 } } \\ & { \mathrm { ( D ) } \ \tau ( x , y ) = \frac { | x - y | } { | x - y | + 1 } \quad \mathrm { ( E ) } \ \omega ( x , y ) = ( x - y ) ^ { 2 } } \end{array}
$$

Solution. (A) is a scaled version of the discrete metric. (B) and (D) are bounded versions of the standard metric (i.e., the generate the standard topology even though they give bounded distance between points). (C) is a scaled version of the standard metric. (E) is not a metric because the triangle inequality is not satisfied. Indeed, let $\scriptstyle x = 0 , y = { \frac { 1 } { 2 } } , z = 1$ . Then

$$
\begin{array} { r } { 1 = \omega ( x , z ) \not \subseteq \omega ( x , y ) + \omega ( y , z ) = \left( { \frac { 1 } { 2 } } \right) ^ { 2 } + \left( { \frac { 1 } { 2 } } \right) ^ { 2 } = { \frac { 1 } { 2 } } } \end{array}
$$

Problem 4. Define $\textstyle f _ { n } ( x ) = { \frac { x ^ { n } } { 1 + x ^ { n } } }$ for $x \in [ 0 , 1 ] , n \in \mathbb { N }$ . Which of the following is true?

(A) The sequence $\{ f _ { n } \}$ converges pointwise on [0, 1] to a limit function $f .$

(B) The sequence $\{ f _ { n } \}$ converges uniformly on [0, 1] to a limit function $f .$

$$
( \mathrm { C } ) \operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { 1 } f _ { n } ( x ) d x = \int _ { 0 } ^ { 1 } \left( \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x ) \right) d x
$$

Solution. At $x = 1$ , we see that $f _ { n } ( 1 ) = 1 / 2$ for all $n \in \mathbb { N }$ so $f _ { n } ( 1 )  1 / 2$ 2. For any $x \in [ 0 , 1 )$ , we have

$$
0 \leq f _ { n } ( x ) = { \frac { x ^ { n } } { 1 + x ^ { n } } } \leq x ^ { n }  0 , \quad { \mathrm { ~ a s ~ } } \ n  \infty .
$$

Thus f converges pointwise to the function

$$
f ( x ) = { \left\{ \begin{array} { l l } { 0 , } & { x \in [ 0 , 1 ) } \\ { 1 / 2 , } & { x = 1 . } \end{array} \right. }
$$

Now each $f _ { n }$ is continuous, but this limit is discontinuous - we conclude that the convergence is not uniform since the uniform limit of continuous functions remains continuous. However, since the domain is compact and each $f _ { n }$ is bounded by 1 for all $x \in [ 0 , 1 ]$ , the limit of the integrals is the integral of the limit. More explicitly

$$
0 \leq \int _ { 0 } ^ { 1 } f _ { n } ( x ) d x = \int _ { 0 } ^ { 1 } { \frac { x ^ { n } d x } { 1 + x ^ { n } } } \leq \int _ { 0 } ^ { 1 } x ^ { n } d x = { \frac { 1 } { n + 1 } } \to 0
$$

and $\begin{array} { r } { \int _ { 0 } ^ { 1 } f ( x ) d x = 0 } \end{array}$ so $\begin{array} { r } { \int _ { 0 } ^ { 1 } f _ { n } ( x ) d x  \int _ { 0 } ^ { 1 } f ( x ) d x } \end{array}$ . Thus we conclude that (A) and (C) are true, while (B) is false.

Problem 5. Suppose that $f : ( 0 , 1 ) \to \mathbb { R }$ is uniformly continuous. Let $\{ x _ { n } \}$ be a sequence in $( 0 , 1 )$ such that $x _ { n } \to 0$ . Show that the sequence $\{ f ( x _ { n } ) \}$ converges. [Note: generalizing this fact, one can show that if $U \subset \mathbb { R } ^ { n }$ is open, then $f : U \to \mathbb { R }$ is uniformly continuous iff f can be continuously extended to the closure ${ \overline { { U } } } . ]$

Solution. Define the sequence $y _ { n } = f ( x _ { n } )$ . Let $\varepsilon > 0$ . Since f is uniformly continuous, there is $\delta > 0$ such that $| x - y | < \delta \implies | f ( x ) - f ( y ) | < \varepsilon$ for all $x , y \in [ 0 , 1 ]$ (that is, δ is independent of $x , y )$ . Since $x _ { n } \to 0$ , in particular $x _ { n }$ is a Cauchy sequence so there is $N \in  { \mathbb { N } }$ such that $| x _ { n } - x _ { m } | < \delta$ whenever $n , m \geq N$ . But then

$$
| y _ { n } - y _ { m } | = | f ( x _ { n } ) - f ( x _ { m } ) | < \varepsilon
$$

when $n , m \geq N$ This shows that $y _ { n }$ is a Cauchy sequence and thus converges to some limit $f _ { 0 } \in \mathbb { R }$ . [This concludes the proof, but performing the same construction for $z _ { n } = f _ { n } ( w _ { n } )$ where $w _ { n }$ is an arbitrary sequence in $( 0 , 1 )$ tending to 1, we find that $z _ { n }  f _ { 1 } \in \mathbb { R }$ Then defining $F ( 0 ) = f _ { 0 } , F ( 1 ) = f _ { 1 }$ , and $F ( x ) = f ( x )$ , for $x \in ( 0 , 1 )$ , we see that F is a continuous extension of f to [0, 1] which gives an idea of how prove the final note in the problem statement.]

Problem 6. Find examples of a function $f : ( - 1 , 1 ) \to \mathbb { R }$ which is

(A) continuous but not uniformly continuous,

(B) uniformly continuous but not Lipschitz continuous,

(C) Lipschitz continuous but not differentiable,

(D) differentiable but not continuously differentiable.

Solution. For (A), let $\textstyle f ( x ) = { \frac { 1 } { 1 - x } }$ . Then f is continuous, but it is not uniformly continuous. Indeed, the sequence $f ( 1 - 1 / n ) = n$ does not converge, which shows by Problem 4 (contrapositively) that f is not uniformly continuous.

For (B), consider $f ( x ) = { \sqrt { 1 - x } }$ . Then f is uniformly continuous because it is can be continuously extended to the compact set $[ - 1 , 1 ]$ However, f is not Lipschitz continuous. Indeed, notice that f is differentiable on $( - 1 , 1 )$ with $\begin{array} { r } { f ^ { \prime } ( x ) = \frac { 1 } { 2 \sqrt { 1 - x } }  \infty \mathrm { ~ a s ~ } x  1 } \end{array}$ . Thus for any $K > 0$ , we can find $\delta > 0$ such that $f ^ { \prime } ( x ) > K$ when $x \in ( 1 - \delta , 1 ]$ . But then by the mean value theorem, for any $x , y \in \left( 1 - \delta , 1 \right] x \neq y .$ , we can find c between x and y such that

$$
| f ( x ) - f ( y ) | = \left| f ^ { \prime } ( c ) \right| | x - y | > K | x - y |
$$

which shows that K is not a Lipschitz constant for f . Since $K > 0$ was arbitrary, we conclude that f is not Lipschitz continuous.

For (C), consider $f ( x ) = \left| x \right|$ . Then f is Lipschitz continuous with Lipschitz constant 1 by the reverse triangle inequality, but f is not differentiable at $x = 0$

For (D) consider the function

$$
f ( x ) = \left\{ \begin{array} { c c } { x ^ { 2 } \sin \left( \frac { 1 } { x } \right) , } & { x \in ( - 1 , 0 ) \cup ( 0 , 1 ) , } \\ { 0 , } & { x = 0 . } \end{array} \right.
$$

Certainly f is differentiable for $x \neq 0$ since it is the product of smooth functions in that domain. Indeed, we see that

$$
f ^ { \prime } ( x ) = 2 x \sin \left( { \frac { 1 } { x } } \right) - \cos \left( { \frac { 1 } { x } } \right) , x \in ( - 1 , 0 ) \cup ( 0 , 1 ) .
$$

Also at $x = 0$ , we see that

$$
\operatorname* { l i m } _ { x \to 0 } { \frac { f ( x ) - f ( 0 ) } { x - 0 } } = \operatorname* { l i m } _ { x \to 0 } x \sin \left( { \frac { 1 } { x } } \right) = 0
$$

which shows that $f ^ { \prime } ( 0 ) = 0$ . Thus f is differentiable for all $x \in ( - 1 , 1 )$ . However, the derivative is discontinuous because along the sequence $\begin{array} { r } { x _ { n } = \frac { 1 } { \sqrt { ( 2 n + 1 ) \pi } } } \end{array}$ , we have $f ^ { \prime } ( x _ { n } ) = 1 \not \to 0 = f ^ { \prime } ( 0 )$ even though $x _ { n } \to 0$

Problem 7. Let $f$ be the function whose graph is pictured on the right. Find the supremum of the set

$$
\left\{ \sum _ { k = 1 } ^ { n } \left| f ( x _ { k } ) - f ( x _ { k - 1 } ) \right| : \left\{ x _ { k } \right\} _ { k = 0 } ^ { n } { \mathrm { ~ i s ~ a ~ p a r t i t i o n ~ o f ~ } } [ 0 , 1 2 ] \right\}
$$

<!-- image-->

Solution. This notation is a bit hard to parse, but what we are really measuring when taking this supremum is the variation in $f ;$ i.e., how much f changes. Since the extreme points are roughly $f ( 0 ) = 1 , f ( 2 ) = 3 , f ( 5 ) = - 2 , f ( 8 ) = 5$ and $f ( 1 2 ) = 3$ , the total change in $f$ is

Problem 6

$$
| 3 - 1 | + | ( - 2 ) - 3 | + | 5 - ( - 2 ) | + | 3 - 5 | = 2 + 5 + 7 + 2 = 1 6 ,
$$

so 16 is the supremum of the set.

As an aside, for any function $f : [ a , b ]  \mathbb { R }$ one can define

$$
T V ( f , [ a , b ] ) : = \operatorname* { s u p } \left\{ \sum _ { k = 1 } ^ { n } | f ( x _ { k } ) - f ( x _ { k - 1 } ) | : \{ x _ { k } \} _ { k = 0 } ^ { n } { \mathrm { ~ i s ~ a ~ p a r t i t i o n ~ o f ~ } } [ a , b ] \right\} .
$$

For many such f this number will be $+ \infty$ , but one defines the set $B V ( [ a , b ] )$ to be the functions $f$ such that $T V ( f , [ a , b ] ) < \infty ;$ these are the functions of bounded (pointwise) variation. And one can prove that if $f : [ a , b ]  \mathbb { R }$ is continuously differentiable, then

$$
T V ( f , [ a , b ] ) = \int _ { a } ^ { b } \left| f ^ { \prime } ( x ) \right| d x .
$$

Problem 8. Which of the following exist?

(A) A continuous function from (0, 1) onto [0, 1]

(B) A continuous function from [0, 1] onto (0, 1)

(C) A continuous bijection from (0, 1) to [0, 1]

Solution. For (A), such a function does exist. Indeed, $f ( x ) = \sin ( 1 0 0 x )$ is an example of such a function.

For (B), no such function exists. The continuous image of a compact set remains compact, so a continuous function cannot map [0, 1] onto (0, 1) since [0, 1] is compact and (0, 1) isn’t.

For (C), again no such function exists. If $f : ( 0 , 1 )  [ 0 , 1 ]$ is a continuous surjection, there is $a \in ( 0 , 1 )$ such that $f ( a ) = 0$ and $b \in ( 0 , 1 )$ such that $f ( b ) = 1$ . But then by the intermediate value theorem, $f$ maps the interval $I = [ \operatorname* { m i n } \{ a , b \} , \operatorname* { m a x } \{ a , b \} ]$ onto [0, 1]. Thus it cannot be injective since for any $x \in ( 0 , 1 ) \backslash I$ , the image f(x) will already have been met by another value $y \in I$

Problem 9. Let $\alpha \neq K \subseteq \mathbb { R } ^ { n }$ . Which of the following statements are true?

(A) If K is compact, then every continuous real-valued function on K is bounded.

(B) If every continuous real-valued function on K is bounded, then K is compact.

(C) If K is compact, then K is connected.

Solution. (A) is true; indeed, defining $U _ { n } = f ^ { - 1 } ( [ - n , n ] )$ for $n \in \mathbb { N } .$ , we see that $U _ { n }$ forms an open cover of K. By compactness there is a finite subcover and since the sets $U _ { n }$ are nested, we will have $K \subset U _ { N }$ for some $N \in \mathbb { N } .$ . But then $| f ( x ) | \leq N$ for all $x \in K$

(B) is true. We prove this by contrapositive. If K is not compact, then it is either not closed or not bounded (by the Heine-Borel theorem). If K is not closed, then there is $x _ { 0 } \in \mathbb { R } ^ { n }$ such that $x _ { 0 } \notin K$ but $x _ { 0 }$ is a limit point of K. Then putting $\begin{array} { r } { f ( x ) = \frac { 1 } { \left\| x - x _ { 0 } \right\| } } \end{array}$ gives a function which is continuous and unbounded on K. If K is unbounded, then $f ( x ) = \| { \dot { x } } \|$ is continuous and unbounded on K. Contrapositively, if every continuous function on K is bounded, then K is compact.

(C) is false. The set $K = [ - 2 , - 1 ] ^ { n } \cup [ 1 , 2 ] ^ { n }$ is compact but not connected.

Problem 10. Find continuous functions $f , g : [ 0 , \infty ) \to \mathbb { R }$ such that

(A) $\textstyle \int _ { 0 } ^ { \infty } f ( x ) d x$ converges but $f ( x ) \neq 0$ as $x \to \infty$ ,

(B) $\{ g ( t + n ) \} _ { n \in \mathbb { N } }$ converges to zero as $n \to \infty$ for any fixed $t \geq 0$ but $g ( x ) \not \to 0$ as $x \to \infty$ Bonus: show that neither of these is possible if we stipulate that $f , g$ are uniformly continuous.

Solution. We can do these both with one example.

For $n \in \mathbb { N }$ , define the functions $f _ { n } : [ 0 , \infty ) \to \mathbb { R }$ by

$$
f _ { n } ( x ) = \left\{ \begin{array} { c c } { 2 n ^ { 2 } ( x - n ) , } & { n \leq x < n + \frac { 1 } { 2 n ^ { 2 } } , } \\ { } & { } \\ { 2 n ^ { 2 } \left( n + \frac { 1 } { n ^ { 2 } } - x \right) , } & { n + \frac { 1 } { 2 n ^ { 2 } } \leq x < n + \frac { 1 } { n ^ { 2 } } , } \\ { } & { } \\ { 0 , } & { \mathrm { o t h e r w i s e } . } \end{array} \right.
$$

Then the graph of each $f _ { n }$ is a spike of height 1 on the interval $[ n , n + 1 / n ^ { 2 } )$ . Let $\textstyle f ( x ) = \sum _ { n = 1 } ^ { \infty } f _ { n } ( x )$ for $x \in [ 0 , \infty )$ , so that f has each one of these spikes [f is pictured in Figure 2 below]. Each spike has integral $\begin{array} { r } { \int _ { 0 } ^ { \infty } f _ { n } ( x ) d x = \frac { 1 } { 2 } \cdot \frac { 1 } { n ^ { 2 } } \cdot 1 = \frac { 1 } { 2 n ^ { 2 } } } \end{array}$ and so we see

$$
\int _ { 0 } ^ { \infty } f ( x ) d x = \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { 2 n ^ { 2 } } } < \infty .
$$

Likewise if $t \ : = \ : 0 ,$ 1 then $t + n$ is an integer for any $n \in \mathbb N$ and so $f ( t + n ) = 0$ for all n so $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } f ( t + n ) = 0 . \mathrm { I f ~ } t \in ( 0 , 1 ) } \end{array}$ , then there is some $N \in \mathbb { N }$ such that $t > 1 / N ^ { 2 }$ . But then $f ( t + n ) = 0$ for all $n \geq N$ and so $\textstyle \operatorname* { l i m } _ { n \to \infty } f ( t + n ) = 0$ . Hence $\{ f ( t + n ) \} _ { n \in \mathbb { N } }$ goes to zero for any $t \in [ 0 , 1 ]$

However, lim $_ { 1 x \to \infty } f ( x ) \neq 0$ because the sequence $\begin{array} { r } { x _ { n } = n + \frac { 1 } { 2 n ^ { 2 } } } \end{array}$ satisfies $x _ { n } \to \infty$ but $f ( x _ { n } ) = 1$ for all $n \in \mathbb { N }$ .

Problem 11. Which of the following necessarily holds for $\mathbb { Q } \subseteq A \subseteq \mathbb { R } ?$

(A) If A is open, then $A = \mathbb { R }$ (B) If A is closed, then $A = \mathbb { R }$ (C) If A is uncountable, then $A = \mathbb { R }$

(D) If A is uncountable, then A is open (E) If A is countable, then A is closed

<!-- image-->  
Figure 2: f, Problem 9

Solution. (A) is false, and this is a bit surprising because if A is open and contains each rationals, then it contains open intervals around each rational. Now if each interval had a fixed length, then we would have $A = \mathbb { R }$ by density of $\mathbb { Q } .$ . However, the intervals around the rationals could get infinitesimally small so that $A \neq \mathbb { R }$ . To make this really rigorous, one needs to know a bit about the Lebesgue measure, but the idea is this: let $\{ q _ { n } \} _ { n = 1 } ^ { \infty } = \mathbb { Q }$ and let $\begin{array} { r } { A = \cup _ { n = 1 } ^ { \infty } ( q _ { n } - \frac { 1 } { 2 ^ { n + 1 } } , q _ { n } + \frac { 1 } { 2 ^ { n + 1 } } ) } \end{array}$ Then certainly $\mathbb { Q } \subset A$ , but the total length of A satisfies

$$
\ell ( A ) \leq \sum _ { n = 1 } ^ { \infty } \ell \left( \left( q _ { n } - { \frac { 1 } { 2 ^ { n + 1 } } } , q _ { n } + { \frac { 1 } { 2 ^ { n + 1 } } } \right) \right) = \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { 2 ^ { n } } } = 1 ,
$$

whereas the length of R is +∞. Thus $A \neq \mathbb { R } { \mathrm { ~ s o ~ } } ( { \mathrm { A } } )$ is false. [Indeed, replacing $1 / 2 ^ { n + 1 }$ with $\varepsilon / 2 ^ { n + 1 }$ for arbitrarily small $\varepsilon > 0$ , this argument shows that the Lebesgue measure of $\mathbb { Q }$ [or any other countable set] is zero).

(C) is false: take $A = ( 0 , 1 ) \cup \mathbb { Q }$

(D) is false: take $A = ( 0 , 1 ) \cup \mathbb { Q }$

(E) is false: take $A = \mathbb { Q }$

(B) is true: if A is closed and contains the rationals, then it contains the closure of the rationals which is R, thus $A = \mathbb { R }$

Problem 12. Let $d ( x , y ) = { \left\{ \begin{array} { l l } { 0 , x = y , } \\ { 1 , x \neq y . } \end{array} \right. }$ Which of the following hold in the metric space $( \mathbb { R } , d ) ?$

(A) $\{ x \}$ is open for each $x \in \mathbb { R }$ (B) Every subset of R is closed

(C) If $d ^ { \prime }$ is the ordinary metric on R, then the identity map $( \mathbb { R } , d ) \to ( \mathbb { R } , d ^ { \prime } )$ is continuous

(D) If $d ^ { \prime }$ is the ordinary metric on R, then the identity map $( \mathbb { R } , d ^ { \prime } )  ( \mathbb { R } , d )$ is continuous

Solution. This is the discrete metric which generates the discrete topology on R; thus every set is open. If every set is open, then every set is closed as well. Thus (A) and (B) are true.

For (C) and (D), consider any space X with two topologies $\tau _ { 1 } , \tau _ { 2 }$ Recall the identity $\iota :$ $( X , \tau _ { 1 } )  ( X , \tau _ { 2 } )$ is continuous iff $\iota ^ { - 1 } ( V ) \in \tau _ { 1 }$ whenever $V \in \tau _ { 2 }$ But $\iota ^ { - 1 } ( V ) = V$ Thus the identity is continuous iff $V \in \tau _ { 1 }$ whenever $V \in \tau _ { 2 }$ . rephrasing yet again, the identity is continuous iff $\tau _ { 2 } \subset \tau _ { 1 }$ which is true iff $\tau _ { 1 }$ is finer than $\tau _ { 2 }$ . The discrete topology is finer than any other topology on R so (D) is false while (C) is true.

Problem 13. Let X, Y be topological spaces and let $f : X \to Y$ be continuous. Show that $f ( K )$ is compact in Y for any compact set $K \subseteq X$ . In short: show that the continuous image of a compact set is compact.

Solution. Suppose that $K \subset X$ is compact. We want to prove that $f ( K )$ is compact, so take an open cover {Vi} of $f ( K )$ . Since f is continuous, we have that $U _ { i } = f ^ { - 1 } ( V _ { i } )$ are open in X. Now if $x \in K$ , then $f ( x ) \in f ( K )$ which means that $f ( x ) \in V _ { i }$ for some i. But if $f ( x ) \in V _ { i }$ then $x \in U _ { i }$ . This shows that $\{ U _ { i } \}$ forms an open cover of K in X. Since K is compact, there is a finite subcover $U _ { 1 } , \ldots , U _ { n }$ . But then since $K \subset \cup _ { k = 1 } ^ { n } U _ { k }$ , we have $f ( K ) \subset \cup _ { k = 1 } ^ { n } f ( U _ { k } ) = \cup _ { k = 1 } ^ { n } V _ { k }$ , and so $V _ { 1 } , \ldots , V _ { n }$ forms a finite subcover of $f ( K )$ . Since $\{ V _ { i } \}$ was an arbitrary open cover of $f ( K )$ and we were able to extract a finite subcover, we conclude that $f ( K )$ is compact.

Problem 14. Let $\tau$ be the topology on R generated by sets of the form $\{ [ a , b ) : a , b \in \mathbb { R } , a < b \}$ Which of the following are true in the topological space $( \mathbb { R } , \tau ) ?$

(A) [0, 1] is compact (B) [0, 1] is Hausdorff (C) [0, 1] is connected

Solution. (A) is false. In the lower limit topology, compact sets are at most countable. Indeed, suppose that $\overline { { \mathcal { D } \ne C \subset \mathbb { R } } }$ is compact in this topology. Take any $c \in C$ and consider the sets

$$
\begin{array} { r } { U _ { 0 } = [ c , \infty ) , \quad U _ { n } = \left( - \infty , c - \frac { 1 } { n } \right) , \ n \in \mathbb { N } . } \end{array}
$$

Then $\{ U _ { n } \} _ { n = 0 } ^ { \infty }$ is an open cover of C. Since C is compact, there is a finite subcover. Since $c \notin U _ { n }$ for $n \geq 1$ and since $U _ { n } \subset U _ { n + 1 }$ for all $n \geq 1$ , this finite subcover can be reduced to $\left\{ U _ { 0 } , U _ { N _ { c } } \right\}$ for some $N _ { c } \in \mathbb { N } .$ . Then $\begin{array} { r } { C \subset ( - \infty , c - \frac { 1 } { N _ { c } } ) \cup [ c , \infty ) } \end{array}$ . In particular $\begin{array} { r } { ( c - \frac { 1 } { N _ { c } } , c ] } \end{array}$ contains no points from $C$ except for c. Thus if $c , d \in C$ , we have $\begin{array} { r } { d \notin \left( c - \frac { 1 } { N _ { c } } , c \right] } \end{array}$ and $\begin{array} { r } { c \notin \left( d - \frac { 1 } { N _ { d } } , d \right] } \end{array}$ , meaning that

$$
\left( c - \frac { 1 } { N _ { c } } , c \right] \cap \left( d - \frac { 1 } { N _ { d } } , d \right] = \emptyset .
$$

Now for each $c \in C$ , we can find a rational $\begin{array} { r } { q _ { c } \in \left( c - \frac { 1 } { N _ { c } } , c \right] } \end{array}$ . Since these sets are pairwise disjoint, the map $c \mapsto q _ { c }$ is injective and hence C has at most the cardinality of Q.

(B) is true. Indeed, take $x , y \in [ 0 , 1 ] , x \neq y$ and wlog let $x \ : < y$ . Then the sets $\begin{array} { r } { U _ { x } = [ x , \frac { x + y } { 2 } ) } \end{array}$ and $\begin{array} { r } { U _ { y } = \left[ \frac { x + y } { 2 } , y + 1 \right) } \end{array}$ show that [0, 1] is Hausdorff.

(C) is false. Take $A = [ 0 , \frac { 1 } { 2 } )$ and $B = \left[ \textstyle { \frac { 1 } { 2 } } , 2 \right)$ . These are disjoint open sets such that $[ 0 , 1 ] \subset A \cup B$ which shows that [0, 1] is disconnected.

Problem 15. Let $S \subset [ 0 , 1 ] \times [ 0 , 1 ]$ consist of all points $( x , y ) \in [ 0 , 1 ] \times [ 0 , 1 ]$ such that x or y or both is irrational. Which of the following is true (with respect to the standard topology on $\mathbb { R } ^ { 2 } ) ?$

(A) S is open (B) S is closed (C) S is connected (D) S is totally disconnected (E) S is compact

Solution. (A) is false. By density of $\mathbb { Q } ^ { 2 }$ in $\mathbb { R } ^ { 2 }$ , any open ball centered at a point in S contains a point with rational coordinates which is not in S.

(B) is false. By density of $( \mathbb { R } \setminus \mathbb { Q } ) ^ { 2 }$ in $\mathbb { R } ^ { 2 }$ , S doesn’t contain all its limit points since we can take a sequence of points in $S$ converging to a point with rational coordinates which is not in S.

(E) is false. S is not compact since it is not closed.

(C) is true. In fact this set is path-connected. Consider for any $( x , y ) \in S .$ , one of x or $y$ is irrational. If x is irrational then the vertical line $V _ { x } = \{ ( x , t ) : t \in [ 0 , 1 ] \}$ is contained in S. Then we can travel along this line to the point $( x , \pi / 4 )$ . But the entire horizontal line $H _ { \pi / 4 } = \{ ( t , \pi / 4 )$ : $t \in [ 0 , 1 ] \}$ is contained in S and so we can then travel along this line to $( \pi / 4 , \pi / { \dot { 4 } } )$ . Likewise, if y is irrational, we can travel along the horizontal line $H _ { y }$ to the point $( \pi / 4 , y )$ and then along the vertical line $V _ { \pi / 4 }$ to the point $( \pi / 4 , \pi / 4 )$ . This shows that any point can be connected by a continuous path to $( \pi / 4 , \pi / 4 )$ , but then by composing paths, any two points can be connected to each other by a continuous path.

(D) is false since (C) is true.

Problem 16. Suppose X, Y are i.i.d. random variables taking value $n \in \mathbb N$ with probability $\frac { 1 } { 2 ^ { n } }$ What is the probability that max $\{ X , Y \} > 3 \}$

Solution. We see that max $\{ X , Y \} > 3$ iff $X > 3$ or $Y > 3$ and

$$
\operatorname* { P r o b } \{ X > 3 { \mathrm { ~ o r ~ } } Y > 3 \} = 1 - \operatorname* { P r o b } \{ X \leq 3 { \mathrm { ~ a n d ~ } } Y \leq 3 \} = 1 - \operatorname* { P r o b } \{ X \leq 3 \} \operatorname* { P r o b } \{ Y \leq 3 \}
$$

where the last step follows by independence. Now

$$
\operatorname { P r o b } \{ X \leq 3 \} = \sum _ { i = 1 } ^ { 3 } \operatorname { P r o b } \{ X = i \} = { \frac { 1 } { 2 } } + { \frac { 1 } { 4 } } + { \frac { 1 } { 8 } } = { \frac { 7 } { 8 } } ,
$$

and likewise for Y since they are identically distributed. Thus

$$
{ \mathrm { P r o b } } \{ X > 3 { \mathrm { ~ o r ~ } } Y > 3 \} = 1 - \left( { \frac { 7 } { 8 } } \right) ^ { 2 } = { \frac { 1 5 } { 6 4 } } .
$$

Problem 17. Two random numbers are drawn uniformly and independently from $\{ 1 , \ldots , 1 0 \}$ What is the probability that neither is the square of the other?

Solution. The only squares less than 10 are 1, 4, 9. Thus the only time that one is a square of the other is if we draw $( 1 , 1 ) , ( 2 , 4 ) , ( 4 , 2 ) , ( 3 , 9 ) , ( 9 , 3 )$ . Since all couples $( i , j ) , i , j = 1 , . . . , 1 0$ are equally likely (since the distributions are independent and uniform), the probability that neither is the square of the other is $\frac { 9 5 } { 1 0 0 }$

Problem 18. If X is drawn uniformly from [0, 3] and Y is drawn uniformly from [0, 4], what is the probability that $X < Y ?$

Solution. We can split this up into the cases that $Y \in [ 0 , 3 ]$ or $Y \in ( 3 , 4 ]$ . Since these cases are disjoint and cover all possibilities, the law of total probability says that

$$
\operatorname* { P r o b } \{ X < Y \} = \operatorname* { P r o b } \{ X < Y | Y \leq 3 \} \operatorname* { P r o b } \{ Y \leq 3 \} + \operatorname* { P r o b } \{ X < Y | Y > 3 \} \operatorname* { P r o b } \{ Y > 3 \} .
$$

Given that $Y \le 3 , Y$ is distributed uniformly in $[ 0 , 3 ]$ and so by symmetry, the probability that $X < Y$ is $1 / 2$ . If $Y > 3$ , then probability that $X < Y$ is 1. Thus we have

$$
\operatorname { P r o b } \{ X < Y \} = { \frac { 1 } { 2 } } \cdot { \frac { 3 } { 4 } } + 1 \cdot { \frac { 1 } { 4 } } = { \frac { 5 } { 8 } } .
$$

This fits with our intution: it should be slightly more like that $X \prec Y$ than $X \geq Y$ since Y is drawn from a larger set.

Problem 19. Two players take turns tossing a fair coin; the winner is the first who tosses heads. What is the probability that the first player wins?

Solution. Let H denote heads and T denote tails. If the first player wins, the sequence of events must be one of

$$
\{ H , T T H , T T T T H , T T T T T T . . . \} .
$$

That is, there must be 2n tails tossed and then a heads, where $n = 0 , 1 , 2 , \ldots$ Since the tosses are independent and the coin is fair, the probability of one such event occuring is $\left( { \frac { 1 } { 2 } } \right) ^ { 2 n } \cdot \left( { \frac { 1 } { 2 } } \right)$ . Summing over all $n ,$ we find that player one wins with probability

$$
\sum _ { n = 0 } ^ { \infty } \left( { \frac { 1 } { 2 } } \right) ^ { 2 n } \cdot \left( { \frac { 1 } { 2 } } \right) = { \frac { 1 } { 2 } } \sum _ { n = 0 } ^ { \infty } { \frac { 1 } { 4 ^ { n } } } = { \frac { 1 } { 2 } } \cdot { \frac { 1 } { 1 - 1 / 4 } } = { \frac { 2 } { 3 } } .
$$

There is another clever way to reason through this problem without doing the computation. Let $p$ denote the probability that player one wins. Since the game is essentially reset if the first two tosses are tails, we have

$$
p = { \frac { 1 } { 2 } } + { \frac { 1 } { 4 } } p
$$

where $\begin{array} { l } { { \frac { 1 } { 2 } } } \end{array}$ represents the probability that player one wins on the first toss and ${ \scriptstyle { \frac { 1 } { 4 } } } p$ represents the probability of reaching the reset point and player one winning thereafter. Solving this gives $p = 2 / 3$ •

Problem 20. Let X be a random variable with density function $\textstyle f ( x ) = { \frac { 3 } { 4 } } ( 1 - x ^ { 2 } )$ , for $x \in [ - 1 , 1 ]$ (and $f ( x ) = 0$ elsewhere). What is the standard deviation of $X ?$

Solution. Recall, the variance of X if given by

$$
\operatorname { V a r } ( X ) = E ( X ^ { 2 } ) - E ( X ) ^ { 2 }
$$

and since X has distribution function $f ,$ we see that

$$
E ( g ( X ) ) = \int _ { \mathbb { R } } g ( x ) f ( x ) d x .
$$

Thus

$$
E ( X ) = \int _ { \mathbb { R } } x f ( x ) d x = { \frac { 3 } { 4 } } \int _ { - 1 } ^ { 1 } ( x - x ^ { 3 } ) d x = 0 { \mathrm { ~ s i n c e ~ t h e ~ i n t e g r a n d ~ i s ~ o d d } } .
$$

Next,

$$
E ( X ^ { 2 } ) = \int _ { \mathbb { R } } x ^ { 2 } f ( x ) d x = { \frac { 3 } { 4 } } \int _ { - 1 } ^ { 1 } ( x ^ { 2 } - x ^ { 4 } ) = { \frac { 3 } { 4 } } \left( { \frac { 2 } { 3 } } - { \frac { 2 } { 5 } } \right) = { \frac { 3 } { 4 } } \cdot { \frac { 4 } { 1 5 } } = { \frac { 1 } { 5 } } .
$$

The standard deviation is the square root of the variance so $\begin{array} { r } { \mathrm { S t D e v } ( X ) = \frac { 1 } { \sqrt { 5 } } } \end{array}$

Problem 21. How many surjective functions are there from {1, 2, 3, 4} to $\{ 1 , 2 , 3 \} \}$

Solution. Since there are 3 choices for the image of each of the four elements, there are $3 ^ { 4 } = 8 1$ total functions from {1, 2, 3, 4} to {1, 2, 3}. It is easier to count the functions that are not surjective. If a function is not surjective, then it maps {1, 2, 3, 4} into {1, 2}, {1, 3} or {2, 3}. There are three choices for which set to map into and there are $2 ^ { 4 }$ maps in each case, thus at first glance it seems there are 48 total maps. However, we have double counted the constant maps which send the set to a single point (the map $x \mapsto 1$ for all $x \in \{ 1 , 2 , 3 , 4 \}$ was counted as a map from {1, 2, 3, 4} into {1, 2} and counted again as a map from {1, 2, 3, 4} into {1, 3}). Adjusting for this double counting, we find there are 45 non-surjective maps and thus $8 1 - 4 5 = 3 6$ surjective maps.

Problem 22. For how many integers k does k! end in exactly 99 zeros?

Solution. We find that k! ends with n zeros when $k ! = K \cdot 1 0 ^ { n } = K \cdot 2 ^ { n } \cdot 5 ^ { n }$ where K is not divisible by 10. There will always be more factors of 2 than factors of 5 in k! so we gain a zero when we pass a multiple of five. Thus there will be 5 numbers k such that k! ends in exactly 99 zeros and they have the form $k = 5 N + \ell$ for $\ell = 0 , 1 , 2 , 3 , 4$ for some $N \in  { \mathbb { N } }$ .

Actually, it is possible that there are no natural numbers k such that k! ends in exactly 99 zeros. It is possible that some $k - 1$ is such that $( k - 1 ) !$ ends in exactly 98 zeros and that k is divisible by 25, meaning that at least two extra zeros get added and k! ends in 100 or more zeros. This is somewhat unlikely. Indeed, only $1 / 5$ multiples of 5 is divisible by 25, and $1 / 2 5$ of all multiples of 5 are divisible by 125, etc. which means (roughly speaking) that for a given number n, there is a

$$
\sum _ { j = 1 } ^ { \infty } { \frac { 1 } { 5 ^ { j } } } = { \frac { 1 / 5 } { 1 - 1 / 5 } } = { \frac { 1 } { 4 } }
$$

chance that there are no $k \in \mathbb N$ such that k! ends with exactly n zeros. To give a definitive answer, one would need to check that 99 is not such an n. Indeed, 99 doesn’t get skipped. Counting multiples of 5, we see that for each 100 numbers, $\{ 1 0 0 \ell + 1 , 1 0 0 \ell + 2 , \cdot \cdot \cdot , 1 0 0 ( \ell + 1 ) \} , \ell = 0 , 1 , 2 , 3 ,$ there are twenty multiples of 5, four of which are divisible by 25, and possibly one of which is divisible by 125. Thus, 100! ends in 24 zeros, 200! ends in 49 zeros, 300 ends in 74 zeros and 400! ends in 99 zeros (as do 401!, 402!, 403! and 404!).

Problem 23. Let $f : X \to Y$ . Write the negation of $^ { 6 6 } f$ is bijective” in terms of the following statements:

P: For each $x \in X$ , there is $y \in Y$ such that $f ( x ) = y$

Q: For each $y \in Y$ , there is $x \in X$ such that $f ( x ) = y$

R: There exist $x _ { 1 } , x _ { 2 } \in X$ with $x _ { 1 } \neq x _ { 2 }$ and $f ( x _ { 1 } ) = f ( x _ { 2 } )$

Solution. P is just the statement that f is a function. Q is the statement that $f$ is surjective. R is the statement that $f$ is not injective. Thus

$$
f { \mathrm { ~ i s ~ b i j e c t i v e } } \quad \Longleftrightarrow \quad { \mathrm { ~ Q ~ a n d ~ } } ( \lnot \mathrm { R } ) .
$$

So the negation is

$$
f { \mathrm { ~ i s ~ n o t ~ b i j e c t i v e } } \quad \Longleftrightarrow \quad ( \lnot \mathrm { Q } ) { \mathrm { ~ o r ~ } } \mathrm { R } .
$$

Problem 24. Let $f : \mathbb { R } \to \mathbb { R }$ and let $X , Y \subseteq \mathbb { R }$ . Which of these are necessarily true?

$$
f ( X \cap Y ) = f ( X ) \cap f ( Y )
$$

$$
f ^ { - 1 } ( X \cap Y ) = f ^ { - 1 } ( X ) \cap f ^ { - 1 } ( Y )
$$

$$
f ( X \cup Y ) = f ( X ) \cup f ( Y )
$$

$$
f ^ { - 1 } ( X \cup Y ) = f ^ { - 1 } ( X ) \cup f ^ { - 1 } ( Y )
$$

Here for $A \subseteq \mathbb { R } , f ( A ) = \{ f ( x ) : x \in A \}$ and $f ^ { - 1 } ( A ) = \{ x \in \mathbb { R } : f ( x ) \in A \}$

Solution. Pullbacks play nicely with both unions and intersections. Pushforwards only play nicely with unions. Thus (B), (C) and (D) are true while (A) is false.

I won’t prove that (B), (C), (D) are true (it isn’t too difficult), but to see that (A) is false, consider the function $f : \mathbb { R } \to \mathbb { R } , f ( x ) = x ^ { 2 }$ for $x \in \mathbb { R }$ and let $X = ( - 1 , 0 )$ and $Y = ( 0 , 1 )$ . Then $X \cap Y = \emptyset$ and so $f ( X \cap Y ) = \emptyset$ . However, $f ( X ) = ( 0 , 1 )$ and $f ( Y ) = ( 0 , 1 )$ so $f ( X \cap Y ) = \emptyset \neq$ $( 0 , 1 ) = f ( X ) \cap f ( Y )$

Problem 25. Let S, T, U be nonempty sets and $f : S \to T , g : T \to U$ be functions such that $g \circ f : S  U$ is one-to-one. Prove that f is one-to-one. Show by example that g need not be one-to-one.

Solution. If f is not one-to-one, there are x, $, y \in S , x \neq y$ such that $f ( x ) = f ( y )$ . But then $( g \circ f ) ( x ) = g ( f ( x ) ) = g ( f ( y ) ) = ( g \circ f ) ( y )$ shows that $g \circ f$ is not one-to-one. Contrapositively, if $g \circ f$ is one-to-one, then so is f . The latter part of the problem is a bit tricky because it seems false at first glance. However, if $g \circ f$ is one-to-one, we can only guarantee that g is one-to-one on the range of $f ;$ it may not be one-to-one on the entirety of T . Indeed, let $S = T = U = \mathbb { R }$ and take $f ( x ) = e ^ { x }$ and $g ( x ) = x ^ { 2 }$ for $x \in \mathbb { R }$ . Then $( g \circ f ) ( x ) = e ^ { 2 x }$ for $x \in \mathbb { R }$ is a one-to-one function while g is not a one-to-one function.

Problem 26. Let A, B be subsets of some set X. Define $S _ { 0 } = \{ A , B \}$ . For $i \geq 0$ , inductively define $S _ { i + 1 }$ to contain all sets of the form $C \cup D , C \cap D$ , and $X \backslash C$ where $C , D \in S _ { i }$ . What is the largest possible number of distinct sets contained in $\cup _ { i = 0 } ^ { \infty } S _ { i } ?$

Solution. This is another problem where half the battle is parsing the notation. It is easiest to understand by drawing and labeling a Venn diagram as in Figure 3 below. The idea is that any set that can be built out of a sequence of unions, intersections and complements of the two sets A, B can be written as of at most four disjoint pieces:

$$
X _ { 1 } = A \setminus B , \quad X _ { 2 } = B \setminus A , \quad X _ { 3 } = A \cap B , \quad X _ { 4 } = X \setminus ( A \cup B ) .
$$

Thus the total number of sets in the final collection $\cup _ { i = 0 } ^ { \infty } S _ { i }$ is the number of distinct combinations of $X _ { 1 } , X _ { 2 } , X _ { 3 } , X _ { 4 }$ . Since there are four sets and for each set, one can decide to include or exclude the set, there are $2 ^ { 4 } = 1 6$ different combinations so this is the maximum number of distinct sets in $\cup _ { i = 0 } ^ { \infty } S _ { i }$ (there could be less: if $A \subset B$ and $B \setminus A$ then there are only 8 sets; if $A = B$ , then there are only 4).

[More generally, if we perform this same procedure starting with $S _ { 0 } = \{ A _ { 1 } , \ldots , A _ { n } \}$ , then there can be as many as $2 ^ { n }$ distinct regions in the Venn diagram, and thus as many as $2 ^ { 2 ^ { n } }$ distinct sets in $\cup _ { i = 0 } ^ { \infty } S _ { i }$ . This hints at the fact that $\cup _ { i = 0 } ^ { \infty } S _ { i }$ has cardinality two steps larger than $S _ { 0 }$ (if $S _ { 0 }$ has cardinality ω, then $\cup _ { i = 0 } ^ { \infty } S _ { i }$ has cardinality $2 ^ { 2 ^ { \omega } } )$ . Indeed, in measure theory, the set $\cup _ { i = 0 } ^ { \infty } S _ { i }$ constructed in this manner is called the σ-algebra generated by $S _ { 0 }$ . The concept of a σ-algebra gives us the minimum amount of structure to reasonably discuss integration in the same way that a topology gives us the minimum amount a structure to reasonably discuss continuity. A famous property of σ-algebras is that they are never countably infinite: a σ-algebra is either finite or uncountable.]

<!-- image-->  
Figure 3: Venn diagram, Problem 26

Problem 27. What is the output of the following algorithms?

(A) (B)   
a = 273 n = 88 n = 123456   
b = 110 while n > 0   
while b > 0 while i < n j = n (mod 100)   
r = a (mod b) i = i+1 print j   
a = b n = floor(n/100)   
while k ≥ i end   
print r if i=k then print i   
end k = k - 1   
end   
end   
Solution.   
(A) 53, 4, 1, 0   
(B) 2, 3, 4, 5, . . . , 87, 88   
(C) 56, 34, 12