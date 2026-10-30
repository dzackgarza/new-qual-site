Complex Analysis Qualifying exam. September 7, 2011

General instructions: 3 hours. No books or notes. Be sure to motivate all (nontrivial) claims and statements. You may use without proof any result proved in the text by Conway, unless the problem specifies otherwise. Either give the name of the theorem or give the statement of the theorem. You need to reprove any result given as an exercise. The following notation will be used. The complex plane is denoted C, the real line is R, and the set of all integers is written Z. For $r > 0 , B ( a ; r ) : = \{ z \in \mathbb { C } : | z - a | < r \}$ and $\mathbb { D } : = B ( 0 ; 1 )$ . For an open set $G \subset \mathbb { C } .$ $H ( G )$ will denote the space of all analytic functions in G, with the metric induced from $C ( G , \mathbb { C } )$ , the set of all continuous, complex-valued functions on G.

1. (80 pts.) For each of the following, determine if the statement is always true or if it is false. If true, give a proof (including citing relevant theorems, if any). If false, give a counterexample or disprove it. You can be brief here, but an unsupported answer will get no credit.

(a) The infinite product $\prod _ { n = 1 } ^ { \infty } ( 1 + { \frac { i } { n } } )$ converges absolutely.

(b) Let $G = \mathbb { C } \setminus \{ \mathbb { R } \cap \mathbb { Z } \}$ . Suppose $f \in H ( G )$ such that $| f ( z ) | \leq 1$ for all $z \in G$ Then f is constant.

(c) There exists a function f analytic in $B ( 1 ; 2 ) \setminus \{ 1 \}$ such that

$$
\operatorname* { l i m } _ { z \to 1 } ( z - 1 ) ^ { k } f ( z ) = \infty , \quad \forall k \in \mathbb { Z } , k \geq 1 .
$$

(d) There exists an entire function f for which $\operatorname* { l i m } _ { | z | \to \infty } \left| { \frac { f ( z ) } { z ^ { k } } } \right|$ does not exist for any positive $k \in \mathbb { Z }$

(e) Let f be an analytic function defined in a simply connected bounded domain $G \subset \mathbb { C }$ with $i \in G$ . If $f ( G ) \subset G$ and $f ( i ) = i$ , then $| f ^ { \prime } ( i ) | \leq 1$

The other 4 problems are on the back of this sheet.

2. (30 pts.) Let X be a set and $\rho _ { n }$ a sequence of metrics on X. Define $\rho$ on $X \times X$ by

$$
\rho ( x , y ) : = \sum _ { n = 1 } ^ { \infty } \big ( \frac { 1 } { n ^ { 2 } } \big ) \frac { \rho _ { n } ( x , y ) } { 1 + \rho _ { n } ( x , y ) } .
$$

(a) Show that $\rho ( x , y ) < \infty$ for all $x , y \in X$ and prove that

$$
\rho ( x , y ) \leq \rho ( x , z ) + \rho ( z , y ) , \quad \forall x , y , z \in X .
$$

Hint: To show that $\frac { \rho _ { n } ( x , y ) } { 1 + \rho _ { n } ( x , y ) }$ satisfies the triangle inequality (which is stated, but not proved in Conway), you may use properties of the function $t \mapsto { \frac { t } { 1 + t } }$ for $t \geq 0$

(b) Let $\{ x _ { j } \}$ be a sequence in X, and $x \in X$ . Prove that $\operatorname* { l i m } _ { j \to \infty } \rho ( x _ { j } , x ) = 0$ i f and only lim $\rho _ { n } ( x _ { j } , x ) = 0$ for all $n \geq 1$ j→∞

3. (30 pts.) Let $f \in H ( \mathbb { D } )$ be nonconstant such that $f ( \mathbb { D } ) \subset \{ z \in \mathbb { C } : \mathrm { R e } \ z < 0 \}$ and $f ( 0 ) = - 1$ . Prove that for any $z \in \mathbb { D }$ ,

$$
{ \frac { 1 - | z | } { 1 + | z | } } \leq | f ( z ) | \leq { \frac { 1 + | z | } { 1 - | z | } } .
$$

4. (30 pts.) Let G be the open strip $\{ z \in \mathbb { C } : 1 < \operatorname { I m } z < 2 \}$

(a) Prove that there exists a function $f \in H ( G )$ with the following property: For any $z \in \partial G$ (the boundary of G in C) and any $\epsilon > 0$ there is no function $g \in H ( B ( z ; \epsilon ) )$ such that $g ( z ) = f ( z )$ for all $z \in G \cap B ( z ; \epsilon )$ . (This means that f does not extend analytically beyond any boundary point of G.)

(b) Prove or disprove the following: There is a function $f \in H ( G )$ satisfying the conditions of (a) and such that f has no zeroes in G.

5. (30 pts.) Let u be a real-valued continuous function in ${ \overline { { \mathbb { D } } } } .$ , and assume that u is harmonic in $\mathbb { D } \setminus \{ 0 \}$ . Prove that u is harmonic in D.

Hint: Consider $\textstyle v ( r ) : = \int _ { - \pi } ^ { \pi } u ( r e ^ { i \theta } ) d \theta$ . You may use without proof Laplace’s equation in polar coordinates:

$$
r \frac { \partial } { \partial r } ( r \frac { \partial U } { \partial r } ) + \frac { \partial ^ { 2 } U } { \partial \theta ^ { 2 } } = 0 ,
$$

where $U ( r , \theta ) = u ( r e ^ { i \theta } )$ . You may also use without proof the fact that a harmonic function in $\mathbb { D } \setminus \{ 0 \}$ that depends only on $| z |$ is necessarily of the form $u ( z ) =$ a $\log | z | + b$ , where a and b are real constants.