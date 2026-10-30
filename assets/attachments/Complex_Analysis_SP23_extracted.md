# Complex Analysis Qualifying Exam

1:00pm–4:00pm (PDT), in person Thursday May 25, 2023

• Write your name and student PID at the top right corner of each page of your submission.

• The more detail you provide, the more accurately your work can be evaluated.

• By participating in this exam you are agreeing to abide by the UCSD Policy on Academic Integrity. The instructors reserve the right to require a follow-up oral examination.

• This is a closed-book examination. No cell-phone or Internet aids.

• Each problem is worth 10 points, except a bonus problem worth 3 points.

• Notation:

– C denotes the complex plane.

– D denotes the open unit disc in C.

– T = ∂D denotes the unit circle in C.

– D denotes the closed unit disc D ∪ T.

– C(K) = {continuous f : K → C}.

Question 1. Let $\begin{array} { r } { A ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n } } \end{array}$ be a power series with radius of convergence equal to one.

(a) Give an example where A(z) diverges at each point of T, and explain why.

(b) Give an example where A(z) converges absolutely on T, and explain why.

(c) Prove that A(z) has a singularity on T, i.e. cannot be analytically continued to an open set containing D.

(d) Prove that if $A ( z )$ has nonnegative coefficients, the point $z = 1$ is a singularity of $A ( z )$ . (Hint: the previous problem could be useful.)

(e) Verify that $\textstyle A ( z ) = \sum _ { n = 0 } ^ { \infty } z ^ { n ! }$ has radius of convergence one, and that each point of T is a singularity of $A ( z )$

Question 2. Let $z _ { 1 } , \ldots , z _ { n }$ be points on T. Prove that that there is $z _ { 0 } \in \mathbb { T }$ such that the product of the distances from $z _ { \mathrm { 0 } }$ to each of the given points is at least one.

Question 3. By evaluating an appropriate contour integral, show that

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \cos ^ { 2 n } ( t ) d t = \frac { ( 2 n - 1 ) ( 2 n - 3 ) \dots ( 3 ) } { ( 2 n ) ( 2 n - 2 ) \dots ( 2 ) } .
$$

Question 4. Let $f ( z )$ be analytic on an open set containing D. Suppose that $| f ( z ) | > m$ for $| z | = 1$ and $| f ( 0 ) | < m$ for a positive number $m$ . Prove that $f ( z )$ has a zero in D.

Question 5. Let f(z) be analytic on D. Prove the following statements.

(a) If $| f ^ { \prime } ( z ) - f ^ { \prime } ( 0 ) | < | f ^ { \prime } ( 0 ) |$ for all $z \in \mathbb { D }$ , then $f ( z )$ is injective.

(b) If $| f ( z ) | < 1$ for all $z \in \mathbb { D }$ and $f ( z )$ has two distinct fixed points, then $f ( z ) = z$ (Hint: Analytic automorphisms of D and Schwarz’s Lemma could be useful.)

Question 6. Let $\begin{array} { r } { f ( z ) = \frac { \cos z } { z ( z - 5 ) } } \end{array}$

(a) Prove that there is a sequence of rational functions $R _ { n } ( z )$ whose poles can only occur at 2 and 6 such that

$$
\operatorname* { l i m } _ { n  \infty } \operatorname* { s u p } _ { 3 \leq | z | \leq 4 } | f ( z ) - R _ { n } ( z ) | = 0 .\tag{1}
$$

(b) Does there exist a sequence of rational functions $R _ { n } ( z )$ whose poles can only occur at 6 such that (1) holds? Justify your answer.

Question 7. Let $a \in \mathbb { D }$ and $\mathbb { G } = \mathbb { D } \backslash \{ a \}$

(a) Construct a harmonic function v on G such that the following two conditions are satisfied:

$$
\operatorname* { l i m } _ { z \to z ^ { * } } v ( z ) = 0 \forall z ^ { * } \in \mathbb { T } \quad { \mathrm { a n d } } \quad \operatorname* { l i m } _ { z \to a } v ( z ) = + \infty .
$$

Write down an explicit formula for the function v you constructed. (Hint: you only need to find one such function; first think about the case $a = 0 .$ )

(b) Let $f \in { \mathcal { C } } ( \partial \mathbb { G } )$ be defined as $f ( z ) = 0$ for $z \in \mathbb { T }$ and $f ( a ) = 2$ . Prove that the Dirichlet problem on G with boundary data f has no solution: there is no harmonic function u on G such that lim $_ { 1 z  z _ { 0 } } u ( z ) = f ( z _ { 0 } )$ for all $z _ { 0 } \in \partial \mathbb { G }$ (Hint: argue by contradiction, making use of the function you constructed in part (a).)

Question 8. This is an optional bonus question. Precisely formulate a problem/question in complex analysis whose solution/answer is not yet known to you, but which you are are eager to learn.