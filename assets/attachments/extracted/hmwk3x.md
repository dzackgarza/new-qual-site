# Math 655. Homework 3. Solutions

Problem 1. Let f be an analytic function on a connected open set $U \subset \mathbf { C }$

(1) Show that if f is real valued, then f is constant on U .

(2) Show that if f has constant absolute value, then f is constant on $U .$

Solution. (1) If $f = u + i v$ is real valued, then $v \equiv 0$ on U. The Cauchy-Riemann equations then imply that

$$
u _ { x } = v _ { y } = 0 \qquad \mathrm { a n d } \qquad u _ { y } = - v _ { x } = 0
$$

on U . Therefore,

$$
f ^ { \prime } = u _ { x } + i v _ { y } = 0 
$$

and so f is constant because U is connected.

(2) $\operatorname { I f } \ | \boldsymbol { f } |$ is constant, then $u ^ { 2 } + v ^ { 2 }$ is constant. If this constant is $0 ,$ we are done. Otherwise, differentiating $u ^ { 2 } + v ^ { 2 } = \mathrm { c o n s t }$ . and using the Cauchy-Riemann equations we obtain the system

$$
\left\{ \begin{array} { l l l } { { u _ { x } u - u _ { y } v } } & { { = } } & { { 0 } } \\ { { u _ { x } v + u _ { y } u } } & { { = } } & { { 0 } } \end{array} \right.
$$

Since the vectors $( u ( x , y ) , - v ( x , y ) )$ and $( v ( x , y ) , u ( x , y ) )$ are linearly independent at each point $z = x + i y$ of $U _ { : }$ , the coefficients $u _ { x } = u _ { y } = 0$ everywhere on $U .$ . Therefore $f$ is constant on $U _ { : }$ as in (1). □

Problem 2. Let f be analytic on C and real valued on $| z | = 1$ . Show that $f$ is constant.

Solution. Let $f = u + i v$ Then v is identically 0 on $| z | = 1$ hence it is identically 0 on $| z | \le 1$ by the Maximum and Minimum principles. Because of Problem $2 , f$ is constant on $| z | < 1$ , and because of the Identity Theorem, $f$ is constant on C. □

Problem 3. Let

$$
f ( z ) = \int _ { [ 1 , z ] } { \frac { 1 } { w } } d w
$$

where $[ 1 , z ]$ is the line segment from 1 to z in C. Show that $f$ is a well defined analytic function on $\mathbf { C } \setminus \left\{ z = x + i y \mid x \le 0 \right\}$ , and compute its power series expansion centered at the point $z _ { 0 } = 1$

Solution. Let $U = \mathbf { C } \setminus \{ z = x + i y \mid x \le 0 \}$ and $z _ { 0 } \in U$ . If h is sufficiently small in absolute value, then the triangle δ determined by the points $1 , z _ { 0 }$ and $z _ { 0 } + h$ is contained in U. Since $1 / z$ is analytic on U , Cauchy’s formula for a Triangle implies that

$$
\int _ { \partial \triangle } { \frac { 1 } { w } } d w = 0
$$

and so

$$
f ( z _ { 0 } + h ) - f ( z _ { 0 } ) = \int _ { [ z _ { 0 } + h , z _ { 0 } ] } { \frac { 1 } { w } } d w
$$

Next

$$
\begin{array} { r c l } { \displaystyle \left| \frac { f ( z _ { 0 } + h ) - f ( z _ { 0 } ) } { h } - \frac { 1 } { z _ { 0 } } \right| } & { \leq } & { \displaystyle \frac { 1 } { | h | } \int _ { [ z _ { 0 } + h , z _ { 0 } ] } \left| \frac { 1 } { w } - \frac { 1 } { z _ { 0 } } \right| d w } \\ & { \leq } & { \displaystyle \operatorname* { m a x } _ { w \in [ z _ { 0 } + h , z _ { 0 } ] } \frac { | w - z _ { 0 } | } { | w z _ { 0 } | } } \end{array}
$$

which converges to 0 as $h \to 0$

This shows that $f ^ { \prime } ( z ) = 1 / z$ . The coefficients of the power series representation $\textstyle \sum _ { n } a _ { n } ( z - 1 ) ^ { n }$ are

$$
a _ { n } = { \frac { f ^ { ( n ) } ( 1 ) } { n ! } } = { \frac { ( - 1 ) ^ { n } } { n } } .
$$

Problem 4. Show that if $P ( z ) = z ^ { n } + a _ { n - 1 } z ^ { n - 1 } + \cdot \cdot \cdot + a _ { 0 }$ is a polynomial of degree $n \geq 1$ 7 then $| P ( z ) | $ ∞ as $| z | \to \infty$ . In fact, show that if $| z | \geq$ max $\{ 1 , 2 n | a _ { n - 1 } | , \cdot \cdot \cdot , 2 n | a _ { 0 } | \}$ , then $| P ( z ) | \geq | z | ^ { n } / 2$

Solution. Write

$$
P ( z ) = z ^ { n } { \biggl ( } 1 + { \frac { a _ { n - 1 } } { z } } + \cdots + { \frac { a _ { 0 } } { z ^ { n } } } { \biggr ) } ,
$$

and let

$$
M = \operatorname* { m a x } \{ 1 , 2 n | a _ { n - 1 } | , \cdot \cdot \cdot , 2 n | a _ { 0 } | \}
$$

If $| z | \geq M$ , then $| z | ^ { k } \geq | z | \geq M$ for all k, and

$$
{ \frac { | a _ { n - k } | } { | z ^ { k } | } } \leq { \frac { | a _ { n - k } | } { | z | } } \leq { \frac { | a _ { n - k } | } { 2 n | a _ { n - k } | } } = { \frac { 1 } { 2 n } } .
$$

Therefore

$$
\left| { \frac { a _ { n - 1 } } { z } } + \cdot \cdot \cdot + { \frac { a _ { 0 } } { z ^ { n } } } \right| \leq n { \frac { 1 } { n } } = { \frac { 1 } { 2 } }
$$

and so

$$
\begin{array} { l l l } { | P ( z ) | } & { \ge } & { | z ^ { n } | \displaystyle \left| 1 + \frac { a _ { n - 1 } } { z } + \cdot \cdot \cdot + \frac { a _ { 0 } } { z ^ { n } } \right| } \\ & { \ge } & { | z ^ { n } | \displaystyle \left( 1 - \left| \frac { a _ { n - 1 } } { z } + \cdot \cdot \cdot + \frac { a _ { 0 } } { z ^ { n } } \right| \right) } \\ & { \ge } & { \displaystyle \frac { | z ^ { n } | } { 2 } . } \end{array}
$$

Problem 5. Let f be an entire function such that

$$
| f ( z ) | \leq A | z | ^ { k }
$$

for all $z \in \mathbf { C }$ , for some constant A and integer k. Show that f is a polynomial of degree max{0, k}.

Solution. If $k \leq 0$ , then $f$ is bounded and therefore constant because of Liouville’s theorem.

Assume thus that $k > 0$ . If $f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ on C, the Cauchy inequalities and the hypothesis $| f ( z ) | \leq A | z | ^ { k }$ imply that

$$
| a _ { n } | \leq { \frac { 1 } { r ^ { n } } } \operatorname* { m a x } _ { | z | = r } | f ( z ) | \leq { \frac { A r ^ { k } } { r ^ { n } } }
$$

for all $r > 0$ . Therefore $a _ { n } = 0 { \mathrm { ~ i f ~ } } n > k$