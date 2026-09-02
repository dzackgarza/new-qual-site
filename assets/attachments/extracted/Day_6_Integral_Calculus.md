Relevant information. For a bounded function $f : [ a , b ] \to \mathbb { R }$ and a monotonically increasing function $\alpha : [ a , b ]  \mathbb { R }$ we say that $f$ is Riemann(-Steiltjes) integrable with respect to α and write $f \in { \mathcal { R } } ( \alpha )$ on $[ a , b ]$ provided

$$
\operatorname* { i n f } _ { P \in { \mathcal P } [ a , b ] } U ( P , f , \alpha ) = \operatorname* { s u p } _ { P \in { \mathcal P } [ a , b ] } L ( P , f , \alpha ) .
$$

The value of the integral is then this common quantity,

$$
\int _ { a } ^ { b } f d \alpha = \operatorname* { i n f } _ { P \in { \mathcal { P } } [ a , b ] } U ( P , f , \alpha ) = \operatorname* { s u p } _ { P \in { \mathcal { P } } [ a , b ] } L ( P , f , \alpha ) .
$$

Throughout, $\mathcal { P } [ a , b ]$ is the collection of all partitions of $[ a , b ]$

Theorem 5.1 (Riemann’s condition / [Rud76, Thm. 6.6], [Apo74, Thm. 7.19]). $f \in { \mathcal { R } } ( \alpha )$ on [a, b] $i f$ and only if for every $\epsilon > 0$ there exists a partition $P \in \mathcal { \dot { P } } [ a , b ]$ such that

$$
U ( P , f , \alpha ) - L ( P , f , \alpha ) < \epsilon .
$$

Frequently, we assume only that α is of bounded variation or even merely bounded. The following integration by parts formula is occasionally useful:

Theorem 5.2 ([Apo74, Thm. 7.6]). If $f \in { \mathcal { R } } ( \alpha )$ on [a, b] then $\alpha \in { \mathcal { R } } ( f )$ on $[ a , b ]$ and

$$
\int _ { a } ^ { b } f d \alpha = f ( b ) \alpha ( b ) - f ( a ) \alpha ( a ) - \int _ { a } ^ { b } \alpha d f .
$$

Remark. Some differences in the definition of ${ \mathcal { R } } ( \alpha )$ do exist between authors. Not all of these definitions are equivalent! This is unlikely to cause any issues when Riemann’s condition is satisfied.

The ordinary Riemann integral is the case where $\alpha ( x ) = x$ . In this instance, we write merely $f \in \mathcal { R }$ on $[ a , b ]$

Theorem 5.3 ([Rud76, Thm. 6.17]). Assume α increases monotonically and $\alpha ^ { \prime } \in \mathcal { R }$ on $[ a , b ]$ with $f : [ a , b ]  \mathbb { R }$ bounded. Then, $f \in { \mathcal { R } } ( \alpha )$ if and only if $f \alpha ^ { \prime } \in \mathcal { R }$ and, in that case,

$$
\int _ { a } ^ { b } f d \alpha = \int _ { a } ^ { b } f ( x ) \alpha ^ { \prime } ( x ) d x .
$$

Theorem 5.4 (First fundamental theorem of calculus / [Rud76, Thm. 6.20]). $I f \in { \mathcal { R } }$ on [a, b] and

$$
F ( x ) = \int _ { a } ^ { x } f ( t ) d t ,
$$

then F is continuous on $[ a , b ]$ and differentiable at any $x _ { 0 } ~ \in ~ [ a , b ]$ where f is continuous with $F ^ { \prime } ( x _ { 0 } ) = f ( x _ { 0 } )$

Theorem 5.5 (Mean value theorem). $I f f : [ a , b ] \to \mathbb { R }$ is continuous then there exists some $c \in ( a , b )$ such that

$$
{ \frac { 1 } { b - a } } \int _ { a } ^ { b } f ( x ) d x = f ( c ) .
$$

## Warm-up problems.

1) ([KRD10, 6.4.N]) If f and g are bounded on [a, b] and both are Riemann integrable on $[ a , b ]$ show that $f g \in { \mathcal { R } }$ on [a, b].

2) ([Apo74, 7.12] c.f. [Rud76, p. 138 #3]) Give an example of a bounded function f and an increasing function α defined on [a, b] such that $| f | \in { \mathcal { R } } ( \alpha )$ but $f \not \in { \mathcal { R } } ( \alpha )$

3) (January 2007 #1) Let $\textstyle f ( x ) = \int _ { 1 } ^ { x } { \frac { 1 } { t } }$ dt for $x > 0$ . (a) Use an -δ proof to show that f is continuous on (0, ∞). (b) Use an -δ proof to show that f is differentiable on $( 0 , \infty )$

4) ([Apo74, 7.2]) If $f \in { \mathcal { R } } ( \alpha )$ on [a, b] and $\textstyle \int _ { a } ^ { b } f d \alpha = 0$ for every f which is monotonic on [a, b], prove that α must be constant on [a, b].

## Problems.

5) (January 2006 #4b) Suppose that f is continuous and $f ( x ) \geq 0$ on [0, 1]. If $f ( 0 ) > 0$ , prove that $\textstyle \int _ { 0 } ^ { 1 } f ( x ) d x > 0$

6) (June 2005 #1b) Use the definition of the Riemann integral to prove that if f is bounded on [a, b] and is continuous everywhere except for finitely many points in $( a , b )$ , then $f \in { \mathcal { R } }$ on $[ a , b ]$

7) (January 2010 #5) Suppose that $f : [ a , b ] \to \mathbb { R }$ is continuous, $f \geq 0$ on [a, b], and put $M = \operatorname* { s u p } \{ f ( x ) : x \in [ a , b ] \}$ . Prove that

$$
\operatorname* { l i m } _ { p \to \infty } \left( \int _ { a } ^ { b } f ( x ) ^ { p } d x \right) ^ { 1 / p } = M .
$$

8) (January 2009 #4b) Let f be a continuous real-valued function on [0, 1]. Prove that there exists at least one point $\xi \in [ 0 , 1 ]$ such that $\textstyle \int _ { 0 } ^ { 1 } x ^ { 4 } f ( x ) d x = { \frac { 1 } { 5 } } f ( \xi )$

9) (June 2009 #5b) Let φ be a real-valued function defined on [0, 1] such that $\phi , \phi ^ { \prime } .$ , and $\phi ^ { \prime \prime }$ are continuous on [0, 1]. Prove that

$$
\int _ { 0 } ^ { 1 } \cos x \frac { x \phi ^ { \prime } ( x ) - \phi ( x ) + \phi ( 0 ) } { x ^ { 2 } } d x < \frac { 3 } { 2 } | | \phi ^ { \prime \prime } | | _ { \infty } ,
$$

where $| | \phi ^ { \prime \prime } | | _ { \infty } = \operatorname* { s u p } _ { [ 0 , 1 ] } | \phi ^ { \prime \prime } ( x ) |$ . Note that $3 / 2$ may not be the smallest possible constant.

10) (Essentialy June 2013 #7) Prove Theorem 5.3.

## References

[Apo74] Tom M. Apostol. Mathematical Analysis. Addison-Wesley, second edition, 1974.

[KRD10] Allan P. Donsig Kenneth R. Davidson. Real analysis and applications. Springer, 2010.

[Rud76] Walter Rudin. Principles of mathematical analysis. McGraw-Hill, Inc., USA, third edition, 1976.