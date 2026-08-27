## Week 4: Differential Equations & Linear Algebra Practice Problem Solutions

Problem 1. Which of the following most closely represents the graph of the solution to $y ^ { \prime } = 1 + y ^ { 4 } \overset { \cdot } { : }$

<!-- image-->

Solution. The answer is (A). There are a number of ways one caould arrive at this answer, but perhaps most obviously, the equation gives $y ^ { \prime } \geq 1$ and thus the slope of the graph is always bigger than 1, whereas there are portions of graphs (B), (C), (D), (E) where there slope is very near zero. Another good heuristic, is that if we change $y ^ { 4 }$ to $y ^ { 2 } .$ , the dynamics shouldn’t change much qualitatively, and the equation $y ^ { \prime } = 1 + y ^ { 2 }$ has solution $y = \tan ( x )$ , so the solution to $y ^ { \prime } = 1 + y ^ { 4 }$ should look somewhat similar, which the graph of (A) does.

Problem 2. Solve the initial value problem $y ^ { \prime } + x y = x , y ( 0 ) = - 1$

Solution. The integrating factor here is $\mu ( x ) = e ^ { \int x d x } = e ^ { x ^ { 2 } / 2 }$ . We see

$$
e ^ { x ^ { 2 } / 2 } y ^ { \prime } + x e ^ { x ^ { 2 } / 2 } y = x e ^ { x ^ { 2 } / 2 } \implies \frac { d } { d x } \left[ e ^ { x ^ { 2 } / 2 } y ( x ) \right] = x e ^ { x ^ { 2 } / 2 } \implies e ^ { x ^ { 2 } / 2 } y ( x ) - y ( 0 ) = e ^ { x ^ { 2 } / 2 } - 1 .
$$

Thus

$$
\boxed { y ( x ) = 1 - 2 e ^ { - x ^ { 2 } / 2 } . }
$$

Problem 3. A tank initially contains a salt solution of 3 grams of salt dissolved in 100 liters of water. A salt solution containing 0.02 grams of salt per liter is pumped into the tank at 4 liters per minute. The tank is also draining at 4 liters per minute. Assuming the mixing is instantaneous, how many grams of salt are in the tank after 100 minutes?

Solution. Let $S$ denote the amount of salt in the tank in grams. Then $S ( 0 ) = 3$ , and the change in S is given by

$$
{ \frac { d S } { d t } } = \mathrm {  ~ \tilde { \ s a l t } ~ i n " ~ } - \mathrm {  ~ \tilde { \ s a l t } ~ o u t " ~ } = \left( 0 . 0 2 { \frac { g \mathrm { r a m s } } { \mathrm { l i t e r s } } } \right) \left( 4 \mathrm { \frac { l i t e r s } { s e c } } \right) - \left( { \frac { S } { 1 0 0 } } { \frac { g \mathrm { r a m s } } { \mathrm { l i t e r s } } } \right) \left( 4 { \frac { \mathrm { l i t e r s } } { s e c } } \right) = { \frac { 2 } { 2 5 } } - { \frac { S } { 2 5 } } .
$$

The particular solution is $S _ { p } ( t ) = 2$ and the homogeneous solution is $S _ { h } ( t ) = e ^ { - t / 2 5 }$ . Thus the solution is

$$
S ( t ) = 2 - C e ^ { - t / 2 5 } .
$$

and S(0) = 3 gives $C = - 1$ so

$$
S ( t ) = 2 + e ^ { - t / 2 5 } \quad \Longrightarrow \quad \Bigl \lceil S ( 1 0 0 ) = 2 + e ^ { - 4 } . \Bigr \rceil
$$

Problem 4. Find the solution of $x d y + ( y - x e ^ { x } ) d x = 0$ which passes through the point (1, 0).

Solution. This problem can be re-phrased

$$
x { \frac { d y } { d x } } + y = x e ^ { x } .
$$

The left-hand side is already a perfect derivative:

$$
{ \frac { d } { d x } } \left[ x y ( x ) \right] = x e ^ { x } \Longrightarrow x y ( x ) = x e ^ { x } - e ^ { x } + C \Longrightarrow y ( x ) = e ^ { x } - { \frac { e ^ { x } } { x } } + { \frac { C } { x } } .
$$

Now y(1) = 0 gives C = 0 and so $\boxed { y ( x ) = e ^ { x } - e ^ { x } / x . }$

Problem 5. Which of the following indicates the graphs of two functions satisfying $\begin{array} { r } { \left( \frac { d y } { d x } \right) ^ { 2 } + 2 y \frac { d y } { d x } + y ^ { 2 } = 0 ? } \end{array}$

<!-- image-->

Solution. The equation can be factored into $( y ^ { \prime } ( x ) + y ( x ) ) ^ { 2 } = 0 \mathrm { s o } y ^ { \prime } ( x ) = - y ( x )$ and we find $y ( x ) = C e ^ { - x }$ . Thus the graphs should decay to zero as $x \to \infty$ so $\mathrm { ( A ) }$ is the correct answer.

Problem 6. Find the general solution of $y ^ { \prime \prime \prime } - 3 y ^ { \prime \prime } + 3 y ^ { \prime } - y = 0$

Solution. Guessing $y ( x ) = e ^ { r x }$ , we have $r ^ { 3 } - 3 r ^ { 2 } + 3 r - 1 = 0$ which implies $( r - 1 ) ^ { 3 } = 0$ . This equation has a triple root at $r = 1$ , so the general solution is

$$
\boxed { y ( x ) = C _ { 0 } e ^ { 2 } + C _ { 1 } x e ^ { x } + C _ { 2 } x ^ { 2 } e ^ { x } . }
$$

Problem 7. Find all the solutions of the equation $y y ^ { \prime \prime } - 2 ( y ^ { \prime } ) ^ { 2 } = 0$ which pass through $x = 1 , y = 1$

Solution. Divide the equation by $y y ^ { \prime }$ to arrive at

$$
{ \frac { y ^ { \prime \prime } } { y ^ { \prime } } } - 2 { \frac { y ^ { \prime } } { y } } = 0 \quad \Longrightarrow \quad \log ( y ^ { \prime } ) - 2 \log ( y ) = C \quad \Longrightarrow \quad { \frac { y ^ { \prime } } { y ^ { 2 } } } = C
$$

where now $C > 0$ . Integrating again gives

$$
- { \frac { 1 } { y } } = C x + D \Longrightarrow y ( x ) = { \frac { 1 } { D - C x } }
$$

where again $C > 0$ . Plugging in $y ( 1 ) = 1$ shows that $D - C = 1 { \mathrm { ~ s o ~ } } D = 1 + C$ . So the set of all such solutions is

$$
{ \Bigg | } y ( x ) = { \frac { 1 } { 1 + C ( 1 - x ) } } , { \Bigg | } \quad \mathrm { f o r } \ C > 0 .
$$

Problem 8. (Cauchy-Euler Equations) Consider the equation $2 x ^ { 2 } y ^ { \prime \prime } + 3 x y ^ { \prime } - 1 5 y = 0$ for $x > 0$ . Find the general solution by either (1) making the substitution $x = e ^ { t }$ or (2) searching for a solution of the

form $y ( x ) = x ^ { \lambda }$ . If you try the latter, you will arrive at a quadratic polynomial for λ which has two roots. If the equation were changed so that the polynomial has only one root, you would only find one solution. How could you adjust to find another linearly independent solution?

Solution. We’ll do the problem both ways. First, guessing $y ( x ) = x ^ { \lambda }$ , we find that

$$
2 \lambda ( \lambda - 1 ) x ^ { \lambda } + 3 \lambda x ^ { \lambda } - 1 5 x ^ { \lambda } = 0 .
$$

Since this must hold for all $x ,$ we need $2 \lambda ^ { 2 } + \lambda - 1 5 = 0 \mathrm { ~ s o ~ } ( 2 \lambda - 5 ) ( \lambda + 3 ) = 0$ . Thus the general solution is given by

$$
\boxed { y ( x ) = C _ { 1 } x ^ { 5 / 2 } + C _ { 2 } x ^ { - 3 } } .
$$

Now we do this using the substitution $x = e ^ { t }$ . Indeed, define $Y ( t ) = y ( e ^ { t } )$ . We will find a differential equation for $Y ( t )$ . We see

$$
\begin{array} { l } { { Y ^ { \prime } ( t ) = e ^ { t } y ^ { \prime } ( e ^ { t } ) , } } \\ { { Y ^ { \prime \prime } ( t ) = e ^ { 2 t } y ^ { \prime \prime } ( e ^ { t } ) + e ^ { t } y ^ { \prime } ( e ^ { t } ) . } } \end{array}
$$

Thus

$$
2 Y ^ { \prime \prime } ( t ) + Y ^ { \prime } ( t ) = 2 ( e ^ { t } ) ^ { 2 } y ( e ^ { t } ) + 3 e ^ { t } y ^ { \prime } ( e ^ { t } ) = 1 5 y ( e ^ { t } ) = 1 5 Y ( t ) .
$$

Now we can solve for $Y ( t )$ by guessing $Y ( t ) = e ^ { r t }$ and we’ll find $r ^ { 2 } + r - 1 5 = 0 \mathrm { ~ s o ~ } r = 5 / 2 , - 3$ just as λ did above. Thus

$$
Y ( t ) = C _ { 1 } e ^ { \frac { 5 } { 2 } t } + C _ { 2 } e ^ { - 3 t } \implies \Big \lvert \ y ( x ) = Y ( \log ( x ) ) = C _ { 1 } x ^ { 5 / 2 } + C _ { 2 } x ^ { - 3 } . \Big \rvert
$$

This latter method was a bit more complicated, but it helps answer the last question: what if we had a repeated root for $\lambda ?$ In this case, we would transform the equation and find that the differential equation for $Y ( t )$ has a characteristic polynomial $( r - r _ { 1 } ) ^ { 2 } = 0$ and the solution would be

$$
Y ( t ) = C _ { 1 } e ^ { r _ { 1 } t } + C _ { 2 } t e ^ { r _ { 1 } t } \quad \Longrightarrow \quad \left| y ( x ) = Y ( \log ( x ) ) = C _ { 1 } x ^ { r _ { 1 } } + C _ { 2 } x ^ { r _ { 1 } } \log ( x ) . \right|
$$

Problem 9. (Bernoulli Equations) Find the general solution of the differential equation $\begin{array} { r } { y ^ { \prime } + \frac { 4 } { x } y = x ^ { 3 } y ^ { 2 } } \end{array}$ by making the substitution $u = 1 / y$ . Can you generalize this substitution so that it would work if $y ^ { 2 }$ on the right hand side was replaced by $y ^ { \alpha }$ for any $\alpha \neq 0 , 1 2$

Solution. We find a differential equation that $u = 1 / y$ satisfies. Indeed,

$$
u ^ { \prime } = - { \frac { 1 } { y ^ { 2 } } } y ^ { \prime } = - { \frac { 1 } { y ^ { 2 } } } \left( - { \frac { 4 } { x } } y + x ^ { 3 } y ^ { 2 } \right) = { \frac { 4 } { x y } } - x ^ { 3 } = { \frac { 4 } { x } } u - x ^ { 3 } .
$$

This equation is now linear in u. We use an integrating factor:

$$
u ^ { \prime } - { \frac { 4 } { x } } u = - x ^ { 3 } \quad \Longrightarrow \quad { \frac { 1 } { x ^ { 4 } } } u ^ { \prime } - { \frac { 4 } { x ^ { 5 } } } u = - { \frac { 1 } { x } } \quad \Longrightarrow \quad { \frac { d } { d x } } \left[ { \frac { 1 } { x ^ { 4 } } } u \right] = - { \frac { 1 } { x } } .
$$

Integrating gives the general solution

$$
{ \frac { 1 } { x ^ { 4 } } } u ( x ) = C - \log ( x ) \Longrightarrow u ( x ) = C x ^ { 4 } - x ^ { 4 } \log ( x ) .
$$

Thus inverting gives

$$
\boxed { y ( x ) = \frac { 1 } { u ( x ) } = \frac { 1 } { C x ^ { 4 } - x ^ { 4 } \log ( x ) } } .
$$

To answer the last question, consider the equation

$$
y ^ { \prime } + p ( x ) y = q ( x ) y ^ { \alpha } .
$$

We want to make the substitution $u = y ^ { \beta }$ and solve for $\beta$ to linearize the equation. Indeed, this will give

$$
u ^ { \prime } = \beta y ^ { \beta - 1 } y ^ { \prime } = \beta y ^ { \beta - 1 } { \bigl ( } - p ( x ) y + q ( x ) y ^ { \alpha } { \bigr ) } = - \beta p ( x ) y ^ { \beta } + \beta q ( x ) y ^ { \alpha + \beta - 1 } = - \beta p ( x ) u + \beta q ( x ) y ^ { \alpha + \beta - 1 } .
$$

To eliminate the power of $y ,$ we choose $\beta = 1 - \alpha$ . Thus $u = y ^ { 1 - \alpha }$ satisfies the linear equation

$$
u ^ { \prime } + ( 1 - \alpha ) p ( x ) u = ( 1 - \alpha ) q ( x ) .
$$

Problem 10. Which of the following are linear subspaces of the continuous functions from R to R?

I. $\{ f : f$ is twice differentiable and $f ^ { \prime \prime } ( x ) - 2 f ^ { \prime } ( x ) + 3 f ( x ) = 0$ for all x}

II. $\{ g : g$ is twice differentiable and $g ^ { \prime \prime } ( x ) = 3 g ^ { \prime } ( x )$ for all x}

III. $\{ h : h$ is twice differentiable and $h ^ { \prime \prime } ( x ) = h ( x ) + 1 { \mathrm { ~ f o r ~ a l l ~ } } x \}$

Solution. The answer is that I. and II. are subspaces but III. is not. The problem with III. is that the set is not closed under addition or scaling. Indeed, it $h _ { 1 } , h _ { 2 }$ satisfy the equation, then

$$
( h _ { 1 } + h _ { 2 } ) ^ { \prime \prime } = ( h _ { 1 } + h _ { 2 } ) + 2
$$

which is a different equation, so $h _ { 1 } + h _ { 2 }$ does not lie in the solution set.

Problem 11. If V, W are 2-dimensional subspaces of $\mathbb { R } ^ { 4 }$ , what are the possible dimensions of $V \cap W ?$ What if $V , W$ are 4-dimensional subspaces of $\mathbb { R } ^ { 7 } ?$

Solution. Suppose that $V , W$ are subspaces of $\mathbb { R } ^ { n }$ . We have $V \cap W \subseteq V , W$ so the dimension of the intersection can no higher than that of $V$ or $W$ . But we also have the dimension formula

$$
\dim \left( V \cap W \right) = \dim \left( V \right) + \dim \left( W \right) - \dim \left( \operatorname { s p a n } \left( V \cup W \right) \right)
$$

and span $( V \cup W ) \subset \mathbb { R } ^ { n }$ . Thus

$$
\dim \left( V \cap W \right) \geq \dim \left( V \right) + \dim \left( W \right) - n .
$$

Applying both these results, we see in the first case

$$
0 \leq \dim \left( V \cap W \right) \leq 2
$$

and in the latter case

$$
1 \leq \dim \left( V \cap W \right) \leq 4 .
$$

It’s easy to achieve any value in between the bounds just using the coordinate vectors. For example, in the first case,

 if $V = { \mathrm { s p a n } } \left( e _ { 1 } , e _ { 2 } \right)$ and $W = \operatorname { s p a n } \left( e _ { 3 } , e _ { 4 } \right)$ , then dim $( V \cap W ) = 0$

 if $V = { \mathrm { s p a n } } \left( e _ { 1 } , e _ { 2 } \right)$ and $W = \mathrm { s p a n } \left( e _ { 1 } , e _ { 4 } \right)$ , then dim $( V \cap W ) = 1$

 if $V = { \mathrm { s p a n } } \left( e _ { 1 } , e _ { 2 } \right)$ and $W = \mathrm { s p a n } \left( e _ { 1 } , e _ { 2 } \right)$ , then dim $( V \cap W ) = 2$

Problem 12. Suppose that V is the vector space of real $2 \times 3$ matrices. If T is a linear transformation from V onto $\mathbb { R } ^ { 4 }$ , what is the dimension of the null space of T ?

Solution. T is mapping a 6-dimensional vector space onto a 4-dimensional vector space. By the Rank-Nullity theorem, we have

$$
\mathrm { d i m } \left( R ( T ) \right) + \mathrm { d i m } \left( N ( T ) \right) = 6
$$

and since T is onto, we have dim $( R ( T ) ) = \mathrm { d i m } ( \mathbb { R } ^ { 4 } ) = 4 \ \mathrm { s o } | \mathrm { d i m } ( N ( T ) ) = 2 .$

Problem 13. Let A be a $2 \times 2$ real matrix. Which of the following are necessarily true: (a) All entries of $A ^ { 2 }$ are non-negative, (b) the determinant of $A ^ { 2 }$ is non-negative, (c) if A has two distinct eigenvalues then $A ^ { 2 }$ has two distinct eigenvalues.

Solution. It is not necessarily the case that all entries of $A ^ { 2 }$ are positive. Indeed,

$$
A = { \binom { 1 } { 0 } } \quad { \overset { - 1 } { 1 } } \quad \implies \quad A ^ { 2 } = { \binom { 1 } { 0 } } \quad { \overset { - 2 } { 1 } } \quad
$$

which has a negative entry. Thus (a) is not necessarily true. For (c), notice that

$$
A = { \binom { - 1 } { 0 } } \quad 0 \quad \quad
$$

has distinct eigenvalues by $A ^ { 2 } = I$ does not. Thus (c) is not necessarily true. Property (b) is necessarily true since the determinant is multiplicative:

$$
\operatorname* { d e t } ( A ^ { 2 } ) = \operatorname* { d e t } ( A ) ^ { 2 } \geq 0 .
$$

Problem 14. Find the eigenvalues and eigenvectors of $M = { \left( \begin{array} { l } { 0 \ 1 \ 1 } \\ { 1 \ 0 \ 1 } \\ { 1 \ 1 \ 0 } \end{array} \right) }$

Solution. We see

$$
\operatorname* { d e t } ( M - \lambda I ) = { \left| \begin{array} { l l l } { - \lambda } & { 1 } & { 1 } \\ { 1 } & { - \lambda } & { 1 } \\ { 1 } & { 1 } & { - \lambda } \end{array} \right| } = - \lambda ( \lambda ^ { 2 } - 1 ) - ( - \lambda - 1 ) + ( 1 + \lambda )
$$

where we used co-factor expansion across the top row. We can factor (1 + λ) from all terms:

$$
\operatorname * { d e t } ( M - \lambda I ) = ( 1 + \lambda ) ( - \lambda ( \lambda - 1 ) + 2 ) = - ( 1 + \lambda ) ^ { 2 } ( \lambda - 2 ) .
$$

Thus the eigenvalues are $\lambda _ { 1 } = 2$ with multiplicity 1 and $\lambda _ { 2 } = - 1$ with multiplicity 2. We look for an eigenvector $v _ { 1 } = ( x , y , z ) ^ { t }$ corresponding to $\lambda _ { 1 } = 2$ . We see $( M - 2 I ) v _ { 1 } = 0$ implies

$$
\begin{array} { r } { - 2 x + y + z = 0 } \\ { x - 2 y + z = 0 } \\ { x + y - 2 z = 0 . } \end{array}
$$

Adding 3x to the first equation, $3 y$ to the second and $3 z$ to the third shows that $x = y = z$ thus an eigenvector corresponding to $\lambda _ { 1 } = 2$ is a scalar multiple of $v _ { 1 } = ( 1 , 1 , 1 ) ^ { t }$ .

Eigenvectors $\boldsymbol { v } = ( x , y , z )$ corresponding to $\lambda _ { 2 } = - 1$ satisfy $x + y + z = 0$ . All such vectors are linear combinations of $v _ { 2 } = ( 1 , 0 , - 1 ) ^ { t }$ and $v _ { 3 } = ( 1 , - 1 , 0 ) ^ { t }$

Problem 15. Suppose that $f : \mathbb { R } ^ { 2 } \to \mathbb { R }$ is linear. If $f ( 1 , 1 ) = 1$ and $f ( - 1 , 0 ) = 2$ , what is $f ( 3 , 5 ) ?$

Solution. By linearity $\Big | f ( 3 , 5 ) = f ( 5 \cdot ( 1 , 1 ) + 2 \cdot ( - 1 , 0 ) ) = 5 f ( 1 , 1 ) + 2 f ( - 1 , 0 ) = 9 .$

Problem 16. Find the rank of the $n \times n$ matrix with entries which simply count up from 1 to $n ^ { 2 }$ in increasing order. For example, if $n = 3$ , we are considering the matrix $\left( \begin{array} { l l l } { 1 } & { \hat { 2 } } & { 3 } \\ { 4 } & { 5 } & { 6 } \\ { 7 } & { 8 } & { 9 } \end{array} \right)$

Solution. Call the matrix A. Then the $i , j$ entry of A is given by $A _ { i , j } = ( i - 1 ) n + j$ for $i , j = 1 , \ldots , n$ Now fixing $i > 2$ , we have

$$
\begin{array} { r l } & { A _ { i , j } = ( i - 1 ) n + j } \\ & { \quad \quad = ( i - 1 ) n + ( ( i - 1 ) - ( i - 2 ) ) j } \\ & { \quad \quad = ( i - 1 ) ( n + j ) - ( i - 2 ) j } \\ & { \quad \quad = ( i - 1 ) A _ { 2 , j } - ( i - 2 ) A _ { 1 , j } , \quad \mathrm { ~ f o r ~ a l l ~ } j = 1 , \dots , n . } \end{array}
$$

This shows that any row $A _ { i }$ for $i > 2$ can be written as a linear combination of the first two rows. The first two rows are linearly independent, so the matrix has rank 2 regardless of n. [Note: to see that the first two rows are linearly independent, you can consider the principle $2 \times 2$ submatrix: $\left( { \begin{array} { c } { 1 } \\ { n { + } 1 } \end{array} } { \begin{array} { c } { 2 } \\ { n { + } 2 } \end{array} } \right)$ . This matrix has determinant −n and is this invertible.]

Problem 17. What is the dimension of the space of all polynomials p of degree at most 3 such that $p ( - 1 ) = p ( 0 ) = p ( 1 ) = 0 ?$

Solution. As a general rule, each point you restrict will take away one degree of freedom. Since order 3 polynomials have 4 degrees of freedom, the dimension of the set of polynomials p satisfying $p ( - 1 ) = p ( 0 ) = p ( 1 ) = 0$ is 1. More explicitly, any polynomial satistying the equations has the form

$$
p ( x ) = \alpha x ( x - 1 ) ( x + 1 ) , \alpha \in \mathbb { R } .
$$

Problem 18. If A, B are subspaces of V , which of the following are necessarily subspaces of $V ?$ (a) A + B = {x + y : x ∈ A, y ∈ B}, (b) A ∪ B, (c) A ∩ B, (d) $A ^ { c } = \{ x \in V : x \notin A \}$

Solution. (a) and (c) are necessarily subspaces. To see that (d) doesn’t define a subspace, note that the zero vector is in A which means it is not in $A ^ { c }$ . To see that (b) does not necessarily define a subspace, consider $A = \operatorname { s p a n } \left( e _ { 1 } \right)$ and $B = \mathrm { s p a n } \left( e _ { 2 } \right)$ . Then $A \cup B$ is the coordinate axes. Both $\textstyle { \binom { 1 } { 0 } }$ and $\binom { 0 } { 1 }$ are in $A \cup B$ but the sum  1 is not.

Problem 19. Find the matrix for the transformation of the xy-plane which reflects each vector through the x-axis and doubles its length.

Solution. To reflect a vector through the x-axis, you need to flip the sign of the y component and to double its length you need to multiply it by 2. The matrix that accomplishes these is $\left( \begin{array} { l l } { 2 } & { \mathrm { ~ \small ~ \displaystyle ~ \frac { ~ 0 ~ } { ~ 2 ~ } ~ } } \end{array} \right)$ .

Problem 20. Assume that V is a finite dimensional vector space and $T : V  V$ is a linear transformation such that $T ^ { 2 } = T$ . Show that each $v \in V$ can be uniquely written as $v = v _ { 1 } + v _ { 2 }$ where $T ( v _ { 1 } ) = v _ { 1 }$ and $T ( v _ { 2 } ) = 0$

Solution. Since $T ^ { 2 } = T$ , T fixes members of it’s image: $T ( T ( v ) ) = T ( v ) \implies T ( T ( v ) - v ) = 0$ . This shows that for any $v \in V , T ( v ) - v \in N ( T )$ . Thus for any $v \in V$ , put $v _ { 1 } = T ( v )$ and $v _ { 2 } = v - T ( v )$ . Then $v = v _ { 1 } + v _ { 2 }$ , where $T ( v _ { 1 } ) = v _ { 1 }$ and $T ( v _ { 2 } ) = 0$ . Further, it $v = u _ { 1 } + u _ { 2 }$ is another such representation, then applying T shows that

$$
\underbrace { T ( v _ { 1 } ) } _ { = v _ { 1 } } + \underbrace { T ( v _ { 2 } ) } _ { = 0 } = \underbrace { T ( u _ { 1 } ) } _ { = u _ { 1 } } + \underbrace { T ( u _ { 2 } ) } _ { = 0 } \implies v _ { 1 } = u _ { 1 } ,
$$

whence $v _ { 1 } + v _ { 2 } = u _ { 1 } + u _ { 2 } \implies v _ { 2 } = u _ { 2 }$ . Thus the representation is unique. [Note: a linear operator T satisfying $T ^ { 2 } = T$ is called a projection operator.]

Problem 21. Suppose that A has distinct eigenvalues $\lambda _ { 1 } , \ldots , \lambda _ { k }$ with corresponding eigenvectors $v _ { 1 } , \dots v _ { k }$ . Show that $\{ v _ { 1 } \ldots , v _ { k } \}$ is a linearly independent set.

Solution. We use induction on $k . { \mathrm { ~ H ~ } } k = 1$ , the claim is trivial since $\{ v _ { 1 } \}$ is always a linearly independent set when $v _ { 1 } \neq 0$ . Suppose that any set of k eigenvectors corresponding to distinct eigenvalues is linearly independent and suppose that $\{ v _ { 1 } , \ldots , v _ { k } , v _ { k + 1 } \}$ is a set of $k + 1$ eigenvectors corresponding to distinct eigenvalues $\lambda _ { 1 } , \dots , \lambda _ { k } , \lambda _ { k + 1 }$ . Let $\alpha _ { 1 } , \ldots , \alpha _ { k } , \alpha _ { k + 1 } \in \mathbb { C }$ be such that

$$
\alpha _ { 1 } v _ { 1 } + \cdot \cdot \cdot + \alpha _ { k } v _ { k } + \alpha _ { k + 1 } v _ { k + 1 } = 0 .
$$

Apply the operator $A - \lambda _ { k + 1 } I$ to this equation and use that $( A - \lambda _ { k + 1 } I ) v _ { k + 1 } = 0$ and $( A - \lambda _ { k + 1 } I ) v _ { \ell } =$ $\lambda _ { \ell } v _ { \ell } - \lambda _ { k + 1 } v _ { \ell } = ( \lambda _ { \ell } - \lambda _ { k + 1 } ) v _ { \ell }$ for $\ell = 1 , \ldots , k$ . Then we see

$$
\alpha _ { 1 } ( \lambda _ { 1 } - \lambda _ { k + 1 } ) v _ { 1 } + \cdot \cdot \cdot + \alpha _ { k } ( \lambda _ { k } - \lambda _ { k + 1 } ) v _ { k } = 0 .
$$

However, these vectors are linearly independent by our inductive hypothesis. Thus

$$
\alpha _ { 1 } ( \lambda _ { 1 } - \lambda _ { k + 1 } ) = \cdots = \alpha _ { k } ( \lambda _ { k } - \lambda _ { k + 1 } ) = 0 .
$$

Since the eigenvalues are assumed to be distinct, we can divide by $\lambda _ { \ell } - \lambda _ { k + 1 }$ to see that $\alpha _ { \ell } = 0$ for all $\ell = 1 , \ldots , k$ . But then we have $\alpha _ { k + 1 } v _ { k + 1 } = 0$ which gives $\alpha _ { k + 1 } = 0$ as well, and we conclude that $\{ v _ { 1 } , \ldots , v _ { k } , v _ { k + 1 } \}$ is a linearly independent set.

Problem 22. Suppose that matrices A, $B \in \mathbb { R } ^ { n \times n }$ satisfy $A B - B A = A$ . Show that A is not invertible.   
If instead we assume $A \neq B , A ^ { 3 } = B ^ { 3 }$ and $A ^ { 2 } B = B ^ { 2 } A$ , show that $A ^ { 2 } + B ^ { 2 }$ is not invertible.

Solution. For the first part, if A was invertible, we would have

$$
( A B - B A ) A ^ { - 1 } = A A ^ { - 1 } \quad \Longrightarrow \quad A B A ^ { - 1 } = B + I .
$$

This would mean that B and $B + I$ are similar which is impossible since the $\operatorname { t r } ( B + I ) = n + \operatorname { t r } ( B )$ whereas similarity has to preserve the trace.

For the second part, notice that

$$
( A ^ { 2 } + B ^ { 2 } ) A = A ^ { 3 } + B ^ { 2 } A = B ^ { 3 } + A ^ { 2 } B = ( B ^ { 2 } + A ^ { 2 } ) B = ( A ^ { 2 } + B ^ { 2 } ) B .
$$

If $A ^ { 2 } + B ^ { 2 }$ was invertible, then we would have $A = B$ , but we’ve assumed that $A \neq B$ , and thus $A ^ { 2 } + B ^ { 2 }$ must not be invertible.

Problem 23. Show that there is no $A \in \mathbb { R } ^ { 2 \times 2 }$ satisfying

$$
A ^ { 1 0 0 } = \binom { - 1 } { 0 } - \alpha \biggr )
$$

when $\alpha > 1$ . If α = 1, find $A \in \mathbb { R } ^ { 2 \times 2 }$ satisfying the equation.

Solution. Suppose that λ is an eigenvalue of A with eigenvector v. Then we see

$$
A v = \lambda v \quad \Longrightarrow \quad A ^ { 2 } v = \lambda A v = \lambda ^ { 2 } v \quad \Longrightarrow \quad A ^ { 3 } v = \lambda ^ { 2 } A v = \lambda ^ { 3 } v \quad \Longrightarrow \quad A ^ { k } v = \lambda ^ { k } v , \quad \mathrm { f o r ~ a l l ~ } k \in \mathbb { N } .
$$

In particular the eigenvalues of $A ^ { 1 0 0 } \mathrm { ~ a r e ~ } - 1$ and −α and so $\lambda ^ { 1 0 0 } ~ < ~ 0 ~$ meaning that λ has non-zero imaginary part. But since A has real entries (and this a real characteristic polynomial), the complex eigenvalues of A come in conjugate pairs. Hence the eigenvalues of A are λ and λ. But then $| \lambda | = | { \overline { { \lambda } } } |$ makes it impossible that $| \lambda ^ { 1 0 0 } | = 1$ while $\left| \overline { { \lambda } } ^ { 1 0 0 } \right| = \alpha > 1$ (or vice versa).

If $\alpha = 1$ so that $A ^ { 1 0 0 } = \left( \begin{array} { c c } { { - 1 } } & { { 0 } } \\ { { 0 } } & { { - 1 } } \end{array} \right)$ . We can accomplish this with a rotation matrix. Indeed, let

$$
A _ { \theta } = \left( { \begin{array} { c c } { \cos ( \theta ) } & { - \sin ( \theta ) } \\ { \sin ( \theta ) } & { \cos ( \theta ) } \end{array} } \right) .
$$

Then

$$
{ \begin{array} { r l } { A _ { \theta } A _ { \varphi } = { \binom { \cos ( \theta ) } { \sin ( \theta ) } } \ - \sin ( \theta ) } { \binom { \cos ( \varphi ) } { \sin ( \varphi ) } } \ - \sin ( \varphi ) } \\ { = { \binom { \cos ( \theta ) \cos ( \varphi ) - \sin ( \theta ) \sin ( \varphi ) } { \cos ( \varphi ) \sin ( \theta ) + \cos ( \theta ) \sin ( \varphi ) } } \ - ( \cos ( \theta ) \sin ( \varphi ) + \cos ( \varphi ) \sin ( \theta ) ) } \\ { = { \binom { \cos ( \varphi ) \sin ( \theta ) + \cos ( \theta ) \sin ( \varphi ) } { \cos ( \varphi ) \sin ( \theta ) + \cos ( \theta ) \sin ( \varphi ) } } \ } & { \cos ( \theta ) \cos ( \varphi ) - \sin ( \theta ) \sin ( \varphi ) } \end{array} 
$$

And now remembering that $\cos ( a + b ) = \cos ( a ) \cos ( b ) - \sin ( a ) \sin ( b )$ and $\sin ( a + b ) = \cos ( a ) \sin ( b ) +$ $\cos ( b ) \sin ( a )$ , we have

$$
A _ { \theta } A _ { \varphi } = { \binom { \cos ( \theta + \varphi ) } { \sin ( \theta + \varphi ) } } \quad - \sin ( \theta + \varphi ) \biggr ) = A _ { \theta + \varphi } .
$$

Now put $\theta = \pi / 1 0 0$ . Then

$$
A _ { \theta } ^ { 1 0 0 } = A _ { 1 0 0 \theta } = A _ { \pi } = \left( \begin{array} { r r } { { - 1 } } & { { 0 } } \\ { { 0 } } & { { - 1 } } \end{array} \right) .
$$

Problem 24. Show that there are no polynomials $a , b , c , d : \mathbb { R } \to \mathbb { R }$ such that

$$
1 + x y + x ^ { 2 } y ^ { 2 } = a ( x ) b ( y ) + c ( x ) d ( y )
$$

for all $x , y \in \mathbb { R }$

Solution. First, suppose that $\alpha , \beta , \gamma$ are such that

$$
\alpha \cdot ( 1 ) + \beta \cdot ( x ^ { 2 } + x + 1 ) + \gamma \cdot ( x ^ { 2 } - x + 1 ) = 0 .
$$

Then

$$
\alpha + \beta + \gamma = 0 , \quad \beta - \gamma = 0 , \quad \mathrm { a n d } \quad \beta + \gamma = 0 .
$$

Adding the second and third equation gives $\beta = 0$ . But then the second equation gives $\gamma = 0$ and then the first gives $\alpha = 0$ . This shows that $\left\{ 1 , x ^ { 2 } + x + 1 , x ^ { 2 } - x + 1 \right\}$ are linearly independent in the vector space of real polynomials.

Now supposing such polynomials $a , b , c ,$ d exist, we can plug in $y = 0 , 1$ , −1 and let $b ( 0 ) = b _ { 0 } , b ( 1 ) =$ $b _ { 1 } , b ( - 1 ) = b _ { 2 }$ (and similarly for d) to see that

$$
\begin{array} { r } { 1 = b _ { 0 } a ( x ) + d _ { 0 } c ( x ) , } \\ { x ^ { 2 } + x + 1 = b _ { 1 } a ( x ) + d _ { 1 } c ( x ) , } \\ { x ^ { 2 } - x + 1 = b _ { 2 } a ( x ) + d _ { 2 } c ( x ) . } \end{array}
$$

This is impossible because two vectors $a ( x )$ and $c ( x )$ cannot span a 3-dimensional space.

Problem 25. Consider an $n \times n$ matrix in which each entry is either zero or one. If the matrix is invertible, what is the maximum amount of ones in the matrix?

Solution. The maximum amount of ones in the matrix is $n ^ { 2 } - n + 1$ . Indeed, we can think of starting with a matrix full of ones and removing entries and replacing them with zero. If we have removed less than $n - 1$ entries, then two columns have remained untouched, meaning there are still two columns full of ones and the matrix is singular since its columns are linearly dependent. Thus there can be a most $n ^ { 2 } - n + 1$ ones.

Now we exhibit a matrix that actually has this number of ones. Define $A \in \mathbb { R } ^ { n \times n }$ by

$$
A = \left( \begin{array} { l l l l l l l } { 1 } & { 1 } & { 1 } & { 1 } & { \cdots } & { 1 } \\ { 0 } & { 1 } & { 1 } & { 1 } & { \cdots } & { 1 } \\ { 1 } & { 0 } & { 1 } & { 1 } & { \cdots } & { 1 } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & & { \vdots } \\ & & { \ddots } & { \ddots } & { \ddots } & { \vdots } \\ { 1 } & { 1 } & { \cdots } & { 1 } & { 0 } & { 1 } \end{array} \right) .
$$

That is, A is full of ones except the first subdiagonal is zero. Then A has $n ^ { 2 } - n + 1$ ones and A is invertible. Indeed, if

$$
A x = 0
$$

then

$$
\begin{array} { c } { { x _ { 1 } + x _ { 2 } + \cdots + x _ { n - 1 } + x _ { n } = 0 , } } \\ { { \qquad x _ { 2 } + \cdots + x _ { n - 1 } + x _ { n } = 0 , } } \\ { { \qquad x _ { 1 } + \qquad \cdots + x _ { n - 1 } + x _ { n } = 0 , } } \\ { { \qquad \vdots } } \\ { { \qquad x _ { 1 } + x _ { 2 } + \cdots \qquad \quad + x _ { n } = 0 . } } \end{array}
$$

Subtracting the second equation from the first gives $x _ { 1 } = 0$ . Then subtracting the third from the first gives $x _ { 2 } = 0$ . Continuing this procedure, subtracting the $k ^ { \mathrm { t h } }$ equation from the first will give $x _ { k } = 0$ until the last equation simply reads $x _ { n } = 0$ . Thus $x = 0$ is the only solution to $A x = 0$ and so A is invertible. (One can also show by induction on the dimension n that det $( A ) = 1$ , though this is a bit tricky).

Problem 26. Let $I _ { n }$ by the $n \times n$ identity matrix and let $J _ { n }$ be the $n \times n$ matrix with all entries equal to 1. Determine the values of $\sigma \in \mathbb { R }$ so that $I _ { n } + \sigma J _ { n }$ is invertible. Find $( I _ { n } + \sigma J _ { n } ) ^ { - 1 }$ for such σ.

Solution. Note that regardless of σ 1 is an eigenvalue of $I _ { n } + \sigma J _ { n }$ of multiplicity at least $n - 1$ since $\left( I _ { n } + \sigma J _ { n } \right) - 1 \cdot I _ { n } = \sigma J _ { n }$ has rank 1. Next, note that $\vec { \bf 1 } = ( 1 , 1 , \dots , 1 ) ^ { t }$ satisfies

$$
( I _ { n } + \sigma J _ { n } ) \vec { \bf 1 } = ( 1 + \sigma n ) \vec { \bf 1 } ,
$$

so the other eigenvalue is $1 + \sigma n$ . Thus the matrix is invertible unless $\sigma = - 1 / n$ . To find the inverse, consider

$$
( I _ { n } + \sigma J _ { n } ) ( I _ { n } + \tau J _ { n } ) = I _ { n } + ( \sigma + \tau + n \sigma \tau ) J _ { n } .
$$

If $\sigma \neq - 1 / n _ { \colon }$ , we can take $\textstyle \tau = - { \frac { \sigma } { 1 + n \sigma } }$ to see that

$$
\boxed { ( I _ { n } + \sigma J _ { n } ) ^ { - 1 } = I _ { n } - \frac { \sigma } { 1 + n \sigma } J _ { n } . }
$$