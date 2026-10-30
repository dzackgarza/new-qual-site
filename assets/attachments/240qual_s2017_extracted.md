Name:

I.D. #:

Instructions: Clearly explain and justify your answers. You may cite theorems from the text, notes, or class as long as they are not what the problem explicitly asks you to prove. You may also use the results of prior problems or prior parts of the same problem when solving a problem – this is allowed even if you were unable to prove the previous results. Make sure to indicate the results that you are using and be sure to verify their hypotheses. All 8 problems have equal value.

Notation: m or dx is used to denote Lebesgue measure on the Borel σ-algebra $\mathbb { R } ^ { d }$ where d may be 1, 2, or an arbitrary integer in $\mathbb { N } : = \{ 1 , 2 , 3 , . . . \}$ . For two functions, $f , g , \mathrm { o n } \mathbb { R } ^ { d } , f \ast g$ denotes their convolution when this makes sense. Measurable means Borel measurable on this test unless otherwise indicated. As usual $\left\| \cdot \right\| _ { p }$ denotes the $L ^ { p } \left( \mu \right)$ -norm for the measure space appearing in the given problem.

$$
1 . \ L = \operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { 1 } { \frac { \operatorname* { m i n } \left( n x , 1 \right) } { x } } d x , \qquad 2 . \ L = \operatorname* { l i m } _ { n \to \infty } \int _ { 1 } ^ { \infty } { \frac { 1 } { x ^ { 3 / 2 } } } e ^ { i n x } d x \qquad 3 . \ L = \operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { \infty } e ^ { - n ^ { 2 } x ^ { 2 } } \cos \left( e ^ { - n ^ { 2 } x } \right) n ^ { 2 } x d x .
$$

Exercise 1. In each case below find $L$ (allowing for values of $\pm \infty )$ and justify the calculations:

Exercise 2. What is the closure of each of ${ \cal T } \subset \mathrm { R e } L ^ { 1 } \left( \mathbb { R } , m \right)$ in the Banach space norm, $\begin{array} { r } { \| f \| _ { 1 } : = \int _ { \mathbb { R } } | f | } \end{array}$ dm in each of the three cases listed below. Please briefly justify your answer.

$$
\mathrm { 1 ) } \quad T = C _ { c } ( \mathbb { R } , \mathbb { R } ) \qquad 2 ) \ : \ : T = \{ f \in C _ { c } ( \mathbb { R } , \mathbb { R } ) : f ( 0 ) = 0 \} . \qquad 3 ) \ : \ : T = \{ f \in C _ { c } ( \mathbb { R } , \mathbb { R } ) : \int _ { [ - 1 , 1 ] } f d m = 0 \} .
$$

Exercise 3. Let (H, h·|·i) be a Hilbert space, $\{ e _ { n } \} _ { n = 1 } ^ { \infty }$ and $\left\{ u _ { n } \right\} _ { n = 1 } ^ { \infty }$ be orthonormal bases for H, and $\left\{ \lambda _ { n } \right\} _ { n = 1 } ^ { \infty } \subset \mathbb { C }$ with $M : = \operatorname* { s u p } _ { n } \left| \lambda _ { n } \right| < \infty .$

1. Show $\begin{array} { r } { T h : = \sum _ { n = 1 } ^ { \infty } \lambda _ { n } \left. h | e _ { n } \right. u _ { n } } \end{array}$ exists in H for all $h \in H$

2. Show $\| T \| _ { o p } \leq M < \infty .$ , where $\| T \| _ { o p }$ is the operator norm of T.

3. Show T is a compact operator if $\scriptstyle \operatorname* { l i m } _ { n \to \infty } \lambda _ { n } = 0$

Exercise 4. Answer the following true or false. For the true statements give a brief justification why it is true and for the false statements give a counter example.

1. If X is a Banach space and $\left\{ \varphi _ { n } \right\} _ { n = 1 } ^ { \infty } \subset X ^ { * }$ satisfies $\operatorname* { s u p } _ { n } | \varphi _ { n } \left( x \right) | < \infty$ for all $x \in X$ , then $\begin{array} { r } { \operatorname* { s u p } _ { n } \operatorname* { s u p } _ { \| \boldsymbol { x } \| = 1 } | \varphi _ { n } \left( \boldsymbol { x } \right) | < \infty } \end{array}$

2. If X is a Banach space, D is a dense subspace of X, and $\{ \varphi _ { n } \} _ { n = 1 } ^ { \infty } \subset X ^ { * }$ satisfies $\operatorname* { s u p } _ { n } \left. \varphi _ { n } \left( x \right) \right. < \infty$ for all $x \in D$ , then $\begin{array} { r } { \operatorname* { s u p } _ { n } \operatorname* { s u p } _ { \| \boldsymbol { x } \| = 1 } | \varphi _ { n } \left( \boldsymbol { x } \right) | < \infty } \end{array}$

3. Suppose that $( \varOmega , \boldsymbol B , \mu )$ is a measure space, $\varOmega _ { n } \ \in \ B$ with $\varOmega _ { n } \ \uparrow \ \varOmega$ and $\mu \left( \varOmega _ { n } \right) < \infty$ for all $n \in \mathbb N$ . If $f : \varOmega \to \mathbb { C }$ is a measurable function such that

$$
\operatorname* { s u p } _ { n \in \mathbb { N } } \left. \int _ { \Omega _ { n } } f 1 _ { | f | \leq n } g d \mu \right. < \infty { \mathrm { ~ f o r ~ a l l ~ } } g \in L ^ { 2 } \left( \mu \right) ,
$$

then $f \in L ^ { 2 } \left( \mu \right)$

Exercise 5. For $t > 0$ , let $A _ { t } = { \left[ \begin{array} { l l } { t } & { 0 } \\ { 0 } & { t ^ { - 1 } } \end{array} \right] }$ and for $f : \mathbb { R } ^ { 2 } \to \mathbb { C }$ let

$$
T _ { t } f \left( x \right) = f \left( A _ { t } x \right) { \mathrm { ~ f o r ~ } } x \in \mathbb { R } ^ { 2 } .
$$

1. Show $\left\| T _ { t } f \right\| _ { 2 } = \left\| f \right\| _ { 2 }$ for all $f \in L ^ { 2 } \left( \mathbb { R } ^ { 2 } , m \right)$

2. Explain why lim $_ { { 1 } t  { 1 } } \| { \cal T } _ { t } f - f \| _ { 2 } = 0$ for all $f \in C _ { c } \left( \mathbb { R } ^ { 2 } \right)$

3. Show $\begin{array} { r } { \operatorname* { l i m } _ { t \to 1 } \| T _ { t } f - f \| _ { 2 } = 0 } \end{array}$ for all $f \in L ^ { 2 } ( \mathbb { R } ^ { 2 } , m )$

Exercise 6. Let $\varphi \in C _ { c } ^ { \infty } \left( \mathbb { R } , [ 0 , \infty ) \right)$ satisfy $\textstyle \int _ { \mathbb { R } } \varphi d m = 1$ and for $\varepsilon > 0$ let $\begin{array} { r } { \delta _ { \varepsilon } \left( x \right) = \frac { 1 } { \varepsilon } \varphi \left( \frac { 1 } { \varepsilon } x \right) } \end{array}$

1. $\mathrm { I f } \mathrm { ~ - \infty < } a < b < \infty$ and $h _ { \varepsilon } \left( x \right) : = 1 _ { [ a , b ] } \ast \delta _ { \varepsilon }$ , show $h _ { \varepsilon } ^ { \prime } \left( x \right) = \delta _ { \varepsilon } \left( x - a \right) - \delta _ { \varepsilon } \left( x - b \right)$

2. If $f \in C _ { c } \left( \mathbb { R } , \mathbb { R } \right)$ and $g \in L ^ { 1 } \left( \mathbb { R } , m \right)$ satisfy,

$$
\int _ { \mathbb R } f h ^ { \prime } d m = - \int _ { \mathbb R } g h d m { \mathrm { ~ f o r ~ a l l ~ } } h \in C _ { c } ^ { \infty } \left( \mathbb R \right) ,\tag{1.1}
$$

show $f$ is absolutely continuous and $f ^ { \prime } = g \ m { \mathrm { - a . e } }$

Exercise 7. Let g be a real valued function in $L ^ { 1 } \left( \left[ 0 , 1 \right] , m \right)$ and $h : [ 0 , 1 ] \ \to \ \mathbb { R }$ be a strictly increasing function (i.e. $h \left( x \right) < h \left( y \right)$ if $x < y )$ such that

$$
\int _ { 0 } ^ { 1 } g \left( x \right) \left[ h \left( x \right) \right] ^ { n } d m \left( x \right) = 0 { \mathrm { ~ f o r ~ } } n \in \mathbb { N } .\tag{1.2}
$$

1. Under the further assumption that h is continuous and $h \left( 0 \right) > 0$ , show $g \left( x \right) = 0 { \mathrm { ~ m - a . e . ~ } } x .$

2. Is it still true that $g \left( x \right) = 0 \ \mathrm { m { - } a . e }$ . when h is continuous with $h \left( 1 / 2 \right) = 0 ?$ [You must justify your answer!]

Extra credit. What are the possible choices for $g \in L ^ { 1 } \left( \left[ 0 , 1 \right] , m \right)$ if we only assume h is strictly increasing (not necessarily continuous) but (1.2) now holds for $n \in \mathbb { N } \cup \{ 0 \}$ , where $\left[ h \left( x \right) \right] ^ { 0 } \equiv 1$

Exercise 8. Suppose that $f \in L ^ { 2 } \left( \mathbb { R } , m \right)$ is a function such that $f \left( x \right) = 0 { \mathrm { ~ i f ~ } } | x | \geq 1$

1. Show ${ \hat { f } } \in C ^ { \infty } \left( \mathbb { R } , \mathbb { C } \right)$ and

$$
\operatorname* { s u p } _ { k \in \mathbb { R } } \left. \hat { f } ^ { ( \ell ) } \left( k \right) \right. \leq \frac { 1 } { \sqrt { 2 \pi } } \sqrt { \frac { 2 } { 2 \ell + 1 } } \left. f \right. _ { 2 } \forall \ \ell = 0 , 1 , 2 , \ldots .
$$

2. Let $\{ f _ { n } \} _ { n = 1 } ^ { \infty } \subset L ^ { 2 } \left( \mathbb { R } , m \right)$ satisfy $\| f _ { n } \| _ { 2 } ~ \le ~ 1$ and $f _ { n } \left( x \right) = 0 { \mathrm { ~ f o r ~ } } | x | \geq 1$ , shows for each $0 < M < \infty$ there exists $1 \leq n _ { 1 } < n _ { 2 } < n _ { 3 } < . .$ . in N such that $\left\{ \hat { f } _ { n _ { k } } \right\} _ { k = 1 } ^ { \infty }$ is uniformly convergent on $[ - M , M ]$ to some $g \in C \left( \left[ - M , M \right] , \mathbb { C } \right)$

Extra Credit. Find an explicit sequence $\{ f _ { n } \} _ { n = 1 } ^ { \infty } \subset L ^ { 2 } \left( \mathbb { R } , m \right)$ such that $\| f _ { n } \| _ { 2 } = 1$ and $f _ { n } \left( x \right) = 0 { \mathrm { ~ i f ~ } } | x | \geq 1$ such that $\hat { f } _ { n } \to 0$ uniformly [−M, M] for any $0 < M < \infty$