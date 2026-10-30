May 28, 2008

## Qualifying Exam in Complex Analysis

Instructions. Do all 6 problems. You may use without proof anything which is proved in the text by Conway, unless otherwise stated. Either state the theorem by name, if it has one, or say what the theorem says. However, you must reprove items which were given as exercises.

Notation: For $a \in \mathbb { C } , B ( a ; r )$ denotes the open disk of radius r around a, while D denotes the open unit disk. If $G \subset \mathbb { C }$ is open, then $H ( G )$ denotes the space of all analytic functions on G with the usual notion of convergence. If $E \subset \mathbb { C }$ ,then $\overline { E }$ denotes the closure of E, and $E ^ { c }$ denotes the complement of E in C.

1. (25 pts.) State and prove Schwarz's Lemma.

2. (75 pts.) True or false. For each part, determine if it is always true or sometimes false. If true give a brief proof. If false give a counterexample or disprove it. No credit if reason or counterexample is missing or incorrect. It's OK to be brief here.

(a) If $f \in H ( \mathbb { D } )$ with $| f ( z ) | \leq 3$ for all z satisfying $| z | = 1 / 2$ , then $| f ^ { \prime \prime } ( 0 ) | \leq$ 24.

(b) Suppose $f \in H ( \mathbb { D } )$ and there exists $C > 0$ such that

$$
\begin{array} { r } { | f ^ { ( n ) } ( 0 ) | \leq C n ! \quad \forall n \in \mathbb { N } . } \end{array}
$$

Then f extends to an entire function, i.e. there exists F entire such that ${ \cal F } | _ { \mathbb { D } } = f .$

() Let $f , g \in H ( G )$ , where G is open and connected in C. If $f ( z ) g ( z ) \equiv 0$ then either f or g is identically zero in G.

d) Suppose $f \in H ( \mathbb { D } \setminus \{ 0 \} )$ such that for any positive integer m and any constant $R > 0$ ,there exists $z \in B ( 0 ; 1 / 2 ) \setminus \{ 0 \}$ with $| z ^ { m } f ( z ) | > R$ Then for any $c \in \mathbb { C }$ and any $\epsilon > 0$ there exists $z \in \mathbb { D } \setminus \{ 0 \}$ with $| f ( z ) - c | < \epsilon$

(e) If u(z) is a (real-valued) harmonic function defined in all of C and satisfying $u ( z ) \geq - 1$ for all $z \in \mathbb { C }$ , then u is constant.

3. (25 pts.) Suppose that $f _ { j } \to f$ in $H ( \{ \Im z > 0 \} )$ , with each $f _ { j }$ one-to-one.   
If f is not constant, show that f is one-to-one.

4.(25 pts.)

(a) Let m be a positive integer. Describe the set of all entire functions f for which there exist positive constants $C _ { 1 }$ and $C _ { 2 }$ such that

$$
| f ( z ) | \leq C _ { 1 } | z | ^ { m } , \quad \forall | z | \geq C _ { 2 }
$$

(b) Describe the set of all functions R, meromorphic in C, analytic except at z = ±1, and satisfying all of the following.

(i) R has a pole of order 1 at z = 1

(ii) R has a pole of order 2 at $z = - 1$

(ii) $| R ( z ) | \leq C | z | \quad \forall | z | \geq 2 .$

5. (25 pts.) For $a \in \mathbb { R }$ compute the integral

$$
\int _ { 0 } ^ { \infty } { \frac { x \sin x } { x ^ { 2 } + a ^ { 2 } } } d x .
$$

Be sure to show all your work any justify any limits.

6. (25 pts.) Prove that there exists a sequence of rational functions $R _ { n }$ analytic in $\mathbb { C } \setminus \{ 3 / 2 \}$ , satisfying both of the following:

i) ln $\mathfrak { n } _ { n  \infty } R _ { n } ( z ) = 1 \quad \forall z \in \mathbb { D } ,$

(ii) $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } R _ { n } ( z ) = 2 , \quad 2 \leq | z | \leq 3 . } \end{array}$

3. (30p) Let G be a Dirichlet region in the plane (i.e. a region in which the Dirichlet problem can be solved). Let

$$
\dot { \phi } _ { 1 } \leq \dot { \varphi } _ { 2 } \leq \ldots \leq \phi _ { n } \leq \ldots .
$$

be a sequence of continuous functions on $\partial _ { \infty } G$ and suppose that there exists a continuous function $\dot { \phi }$ on $\partial _ { \infty } G$ such that for every $z \in \partial _ { \infty } G$

$$
\phi ( z ) = \operatorname* { l i m } _ { n \to \infty } \phi _ { n } ( z )
$$

(pointwise!). Let $u _ { n }$ and u be the solutions to the Dirichlet problem in G with data $\phi _ { n }$ and ${ \dot { \phi } } ,$ respectively. Show that $u _ { n } \to u$ in $\operatorname { H a r } ( G )$

4. (30p) Let $f ( z )$ be analytic in the upper halfplane $H : = \{ \mathrm { I m } z > 0 \}$ . Suppose that for every $p > 1$ and every $z = x + i y$ in H, there is $M > 0$ such that

$$
| f ^ { ( n ) } ( z ) | \leq { \frac { n ! M } { y ^ { n / p } } } , \quad \forall n \geq 0 .
$$

Show that f can be analytically continued to an analytic function in the halfplane $\{ \mathrm { I m } z > - 1 \}$

Hint: For each fixed p, show that there is $0 < c _ { p } < 1$ , with lin $\begin{array} { r } { \mathfrak { n } _ { p \longrightarrow \infty } c _ { p } = 1 } \end{array}$ , such that f can be analytically continued to the halfplane {Im $z > - c _ { p } \big \}$

<!-- image-->

5. (30p) Let G be an open and bounded region in the plane. Suppose that f (z) is analytic in G, $f ( G ) \subset G ,$ and that there exists $a \in G$ with $f ( a ) = a$ and $f ^ { \prime } ( \alpha ) = 1$ . Show that f(z) is the identity $\begin{array} { r } { f ( z ) \equiv z . } \end{array}$

Hint: First, show that it suffices to prove the statement when $0 \in G$ and $a = 0 ,$ Then, suppose that the Taylor series of $f ( z ) - z$ at $a = 0$ is not identically zero. Consider the nth iterate $f ^ { n } : = f \circ f \circ . . . \circ f$ (n times) and compute the first nonvanishing term in the Taylor series of $f ^ { n } ( z ) - z { \mathrm { ~ a t ~ } } a = 0$