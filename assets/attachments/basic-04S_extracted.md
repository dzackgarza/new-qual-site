## Basic Exam (S04)

In several problems you will need the usual $" \mathrm { n o r m } ?$ terminology. If V is a real vector space, then a norm on V is a map $\parallel \parallel : V \to [ 0 , \infty )$ such that $\| v + w \| \leq \| v \| + \| w \|$ $\| c v \| = | c | \| v \|$ , and $\lvert | \boldsymbol { v } \rvert | = 0$ if and only if $v = 0$ Each norm determines a metric d on V via the relation $d ( v , w ) = \lVert v - w \rVert$ . The Euclidean norm (also called the "inner product" norm)on $\mathbb { R } ^ { n }$ is given by

$$
\left\| \sum _ { k = 1 } ^ { n } x _ { k } e _ { k } \right\| _ { 2 } = [ \sum _ { k = 1 } ^ { n } | x _ { k } | ^ { 2 } ] ^ { 1 / 2 } .
$$

where $e _ { k }$ is the usual vector basis. Given a linear transformation $T : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ we define

$$
\| T \| = \operatorname* { s u p } \{ \| T ( x ) \| _ { 2 } : \| x \| _ { 2 } \leq 1 \} .
$$

For all $x , \| T ( x ) \| \leq \| T \| \| x \| ,$

1. Let S denote the set of sequences $a = ( a _ { 1 } , a _ { 2 } , \dots )$ , with $a _ { k } = 0$ or 1. Show that the mapping $\theta : { \mathcal { S } }  \mathbb { R }$ defined by

$$
\theta ( ( a _ { 1 } , a _ { 2 } , . . . ) ) = \frac { a _ { 1 } } { 1 0 } + \frac { a _ { 2 } } { 1 0 ^ { 2 } } + . . . .
$$

is an injection. Include an explanation of why the infinite series converges. Hint: if $a \neq b ,$ you may assume that

$$
\begin{array} { r c l } { { a } } & { { = } } & { { ( a _ { 1 } , \ldots , a _ { n - 1 } , 0 , a _ { n + 1 } , \ldots ) . } } \\ { { b } } & { { = } } & { { ( a _ { 1 } , \ldots , a _ { n - 1 } , 1 , b _ { n + 1 } , \ldots ) } } \end{array}
$$

2. Is $f ( x ) = { \sqrt { x } }$ uniformly continuous on $\lbrack 0 , \infty ) ?$ Prove your assertion.

3. a) Carefully define when a function f on [0, 1] is Riemann integrable. Show that if $f _ { n }$ are Riemann integrable functions on $[ 0 , 1 ]$ and $f _ { n }$ converges to f uniformly, then f is Riemann integrable.

4. Are there infinite compact subsets of Q? Prove your assertion.

5. Suppose that $G$ is an open set in $\mathbb { R } ^ { n } , f : G \to \mathbb { R } ^ { m }$ is a function, and that $x _ { 0 } \in G$

a) Carefully define what is meant by $f ^ { \prime } ( x _ { 0 } ) : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$

b) Suppose that I is a line segment in G such that $f ^ { \prime } ( x )$ is defined for all $x \in I$ Show that if f is differentiable at all the points of I, then for some point c in I

$$
\left\| f ( q ) - f ( p ) \right\| _ { 2 } \leq \left\| f ^ { \prime } ( c ) \right\| \left\| q - p \right\| _ { 2 } .
$$

Hint: let w be a unit vector with $\| f ( q ) - f ( p ) \| _ { 2 } = \left( f ( q ) - f ( p ) \right) \cdot w .$

6. Let $\left. \begin{array} { r l } \end{array} \right.$ be any norm on $\mathbb { R } ^ { n }$

a) Prove that there exists a constant d with $\| x \| \leq d \| x \| _ { 2 }$ for all $x \in \mathbb { R } ^ { n }$ , and use this to show that $N ( x ) = \| x \|$ is continuous in the usual topology on Rn.

b) Prove that there exists a constant c with $\| x \| \geq c \| x \| _ { 2 }$ (Hint: use the fact that N is continuous on the sphere $\{ x : \| x \| _ { 2 } = 1 \} )$

c) Show that if L is an n-dimensional subspace of an arbitrary normed vector space V, then L is closed.

7. Let V be a finite dimensional real vector space. Let $W _ { 1 } , W _ { 2 } \subset V$ be subspaces. Show both of the following:

a) $W _ { 1 } ^ { 0 } \cap W _ { 2 } ^ { 0 } = ( W _ { 1 } + W _ { 2 } ) ^ { 0 }$

b) $( \dot { W } _ { 1 } \cap W _ { 2 } ) ^ { 0 } = W _ { 1 } ^ { 0 } + W _ { 2 } ^ { 0 }$

[Note: $W _ { i } ^ { 0 }$ is the annihilator of $W _ { i \cdot } ]$

8. Let $T : \mathbf { R } ^ { 3 }  \mathbf { R } ^ { 3 }$ be a rotation about the axis $( 1 , 0 - 1 )$ by an angle of $3 0 ^ { o }$ (you can use either orientation).

a) Find the matrix representation $A \in \mathbf { M } _ { 3 } ( \mathbf { R } )$ of T in the standard basis. (You do not have to multiply out matrices but must evaluate inverses.)

Find all the eigenvalues of $A \in \mathbf { M } _ { 3 } ( \mathbf { R } )$

c)Find all the eigenvalues of $A \in \mathbf { M } _ { 3 } ( \mathbf { C } )$

9. Let V be a finite dimensional real inner product space under $\displaystyle ( \ , \ )$ and $T : V \to V$ a linear operator. Show the following are equivalent:

a) $( T x , T y ) = ( x , y )$ for all $x , y \in V$

b) $\vert \vert T ( x ) \vert \vert = \vert \vert x \vert \vert$ for all $x \in V$

) $T ^ { * } T = I d _ { V } ,$ where $T ^ { * }$ is the adjoint of $T$ .

d) $T T ^ { * } = I d _ { V }$

10. Let T be a real symmetric matrix. Show that T is similar to a diagonal matrix.

[You cannot use the Spectral Theorem.]