# Basic Exam Fall 2009

INSTRUCTIONS FOR QUALIFYING EXAMS

Write your university identification number at the top of each shect of paper.

DO NOT WRITE YOUR NAME!

Complcte this sheet. Read the directions of the exam very carefully.

STUDENT ID NUMBEr:

DATE:

Home DepArTment:

INSTRUCTIONS: Do any 10 of the following questions. If you attempt more than 10 questions, indicate below which ones you would like to be considered for credit (otherwise the first 10 will be taken). Each question counts for 10 points. Little or no credit will be given for answers without adequate justification. You have 4 hours. Good luck.

NOTATION: We denote by N = 1,2... the natural numbers, by R and C the real and complex numbers respectively, and by $M _ { n } ( \mathbb { R } ) , M _ { n } ( \mathbb { C } )$ the $n \times n$ matrices with real and complex coefficients respectively.

<table><tr><td>#</td><td>Score</td><td>Counts in 10?</td></tr><tr><td>1</td><td></td><td></td></tr><tr><td>2</td><td></td><td></td></tr><tr><td>3</td><td></td><td></td></tr><tr><td>4</td><td></td><td></td></tr><tr><td>5</td><td></td><td></td></tr><tr><td>6</td><td></td><td></td></tr><tr><td>7</td><td></td><td></td></tr><tr><td>8</td><td></td><td></td></tr><tr><td>9</td><td></td><td></td></tr><tr><td>10</td><td></td><td></td></tr><tr><td>11</td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>12 Total</td><td></td><td></td></tr></table>

1. (i). For each $n \in N$ let $f _ { n } : \mathbb { N } \to \mathbb { R }$ be a function with $| f _ { n } ( m ) | \leq 1$ for all $m , n \in \mathbb { N } .$ Prove that there is an infinite subsequence of distinct positive integers $n _ { i } .$ such that for each m $\in \mathbb { N } , f _ { n _ { i } } ( m )$ converges.

(ii). For $n _ { i }$ as in (i), assume that in addition lin $_ { 1 _ { m }  \infty } \operatorname* { l i m } _ { i  \infty } f _ { n _ { i } } ( m )$ exists and equals 0. Prove or disprove: The same holds for the reverse double limit $\scriptstyle \operatorname* { l i m } _ { i \to \infty } \operatorname* { l i m } _ { m \to \infty } f _ { n _ { i } } ( m )$

2. (i). Let X be a complete metric space with respect to a distance function d. We say that a map $T : X \to X$ is a contraction if for some $0 < \lambda < 1$ and all $x , y \in X .$ $d ( f ( x ) , f ( y ) ) \leq \lambda d ( x , y )$ . Prove that if T is a contraction then it has a fixed point, i.e., there is an $x \in X$ such that $T ( x ) = x$

(ii). Using (i) show that given a differentiable function $f : \mathbb { R } \to \mathbb { R }$ whose first derivative satisfies $f ^ { \prime } ( x ) = e ^ { - x ^ { 2 } } - e ^ { - x ^ { 4 } }$ , there exists $\alpha \in \mathbb { R }$ with $f ( \alpha ) = \alpha$

3. The purpose of this problem is to give a multi variable calculus proof of the geometric and arithmetic means inequality along the concrete steps below. The inequality has numerous other proofs and naturally you are not allowed to use it (or them) below.

(i). Let $\mathbb { R } _ { + } ^ { n } \subset \mathbb { R } ^ { n }$ be the (open) subset of vectors all whose coordinates are positive, and $f : \mathbb { R } _ { + } ^ { n } \to \dot { \mathbb { R } }$ be defined by:

$$
f ( x _ { 1 } , \ldots , x _ { n } ) = x _ { 1 } + \cdots + x _ { n } + { \frac { 1 } { x _ { 1 } \cdot x _ { 2 } \cdot \cdot \cdot x _ { n } } }
$$

(i). Explain carefully why f attains a global (not necessarily unique) minimum at some $p \in \mathbb { R } _ { + } ^ { n }$ . (Hint: what happens when $x _ { i } \to 0 , \infty \ ? )$

(ii). Find p.

(iii). Deduce that if all $x _ { i } \in \mathbb { R }$ are positive and $\Pi x _ { i } = 1$ then $\Sigma x _ { i } \geq n _ { i }$ with equality iff $x _ { i } = 1$ for all i. (This is a special case of the geometric and arithmetic means inequality, from which the general statement can be immediately deduced  no need to write down this part here).

4. Let V be a finite dimensional dimensional R-vector space, whose dimension we denote by dim(V), equipped with an inner product

$$
< , > : V \times V  \mathbb { R } .
$$

For a vector subspace $U \subseteq V .$ ,denote by $U ^ { \bot }$ its orthogonal complement, i.e., the set of $v \in V$ such that $< v , u > = 0$ for all $u \in U$ . Show that dim $( U ) + \dim ( U ^ { \perp } ) = \dim ( V )$ •

5. Show that if $\alpha _ { 1 } , \ldots \alpha _ { n } \in \mathbb { R }$ are all different, and some $a _ { 1 } , \dots a _ { n } \in \mathbb { R }$ satisfy:

$$
\Sigma a _ { i } e ^ { \alpha _ { i } t } = 0 \qquad \forall t \in ( - 1 , 1 ) ,
$$

then necessarily $a _ { i } = 0$ for all $1 \leq i \leq n$ . (Hint: you may use the differentiation operator and a theorem in Linear Algebra on distinct eigenvalues.)

6. Consider the function $f ( x , y ) = \sin ^ { 3 } ( x y ) + y ^ { 2 } | x |$ defined on the region $S \subset \mathbb { R } ^ { 2 }$ given by

$$
S = \{ ( x , y ) \in \mathbb { R } ^ { 2 } ; \quad x ^ { 2 0 1 0 } + y ^ { 2 0 1 0 } \leq 1 \} .
$$

Define what it means for $f$ to be uniformly continuous on S and prove that $f$ is indeed uniformly continuous. (You can use any theorem you wish in the proof, as long as it is stated correctly and you justify properly why it can be applied, $\mathrm { e . g . }$ if you are using a general theorem on continuous functions, show that the function in question is indeed continuous, and if you are using a metric property of a set explain why it has it.)

7. Let $V \simeq \mathbb { R } ^ { n }$ be an n -dimensional vector space over $\mathbb { R } _ { : }$ ,and denote by $\operatorname { E n d } ( V )$ the vector space of R-linear transformations of $V .$ (Note that dim(End $( V ) ) = \dim ( V ) ^ { 2 } = n ^ { 2 } . )$ Then for $T \in \operatorname { E n d } ( V )$ show that the dimension of the subspace $W$ of End(V) spanned by $T ^ { k }$ , for $k$ running through non-negative integers, satisfies the inequality dim $( W ) \leq \dim ( V ) = n$ .

8. For a matrix $A \in M _ { n } ( \mathbb { R } )$ , define $\begin{array} { r } { e ^ { A } : = \sum _ { n = 0 } ^ { \infty } \frac { A ^ { n } } { n ! } } \end{array}$ . Let $v _ { 0 } \in \mathbb { R } ^ { n }$ Prove that the function $v : \mathbb { R }  \mathbb { R } ^ { n }$ given by $v ( t ) = e ^ { A t } v _ { 0 }$ solves the linear differential equation $v ^ { \prime } ( t ) = A v ( t )$ with the initial condition $v ( 0 ) = v _ { 0 }$ Explain precisely which theorems in calculus you are using in your proof and why they are applicable.

9. If $A \in M _ { 2 n + 1 } ( \mathbb { R } )$ is such that $A A ^ { t } = \operatorname { I d } _ { 2 n + 1 }$ the identity matrix, then prove that one of 1 $\mathfrak { o r } - \mathrm { 1 }$ is an eigenvalue of A.

10. (i). Let $I = [ 0 , 2 ]$ . If $f : I  \mathbb { R }$ is a continuous function such that $\textstyle \int _ { I } f ( x ) d x = 3 6$ prove that there is an $x \in I$ such that $f ( x ) = 1 8$

(ii) Consider $I ^ { 2 } \subset \mathbb { R } ^ { 2 }$ , and let $g : I ^ { 2 } \to { \mathbb { R } }$ be a continuous function such that $\begin{array} { r l } { \int _ { I ^ { 2 } } g ( x , y ) d x d y = } \end{array}$ 36. Prove that there is $( x , y ) \in I ^ { 2 }$ such that $g ( x , y ) = 9$

11. (i). State the Cayley-Hamilton theorem for matrices $A \in M _ { \mathfrak { n } } ( \mathbb { C } )$

(ii). Prove it directly for diagonalisable matrices.

(iii). Identify $M _ { n } ( \mathbb { C } ) \simeq \mathbb { C } ^ { n ^ { 2 } }$ through some (say, the natural) linear isomorphism. Through this identification $M _ { n } ( \mathbb { C } )$ becomes a metric space with the Euclidean metric. Fact: The subset of diagonalisable matrices in $M _ { n } ( \mathbb { C } ) ( \simeq \mathbb { C } ^ { n ^ { 2 } } )$ is dense. Use this fact, together with part (ii), to prove the Cayley-Hamilton theorem.

12. Let V be an $n ( \geq 2 )$ -dimensional vector space over C with a set of basis vectors $e _ { 1 } , \ldots , e _ { n }$ Let $T$ be a linear transformation of V satisfying $T ( e _ { 1 } ) = e _ { 2 } , \cdots , T ( e _ { n - 1 } ) = e _ { n } , T ( e _ { n } ) = e _ { 1 }$ (i). Show that $T$ has 1 as an eigenvalue and write down an eigenvector with eigenvalue 1. Show that up to scaling it is unique.

(ii). Is $T$ diagonalisable? (Hint: calculate the characteristic polynomial.)