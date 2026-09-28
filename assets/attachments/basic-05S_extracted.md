Note: Throughout this exam, $M _ { n } ( \mathbb { C } )$ denotes the set of $n \times n$ matrices with complex entries.

## Linear Algebra.

1. Given $n \geq 1$ , let tr : $M _ { n } ( \mathbb { C } ) \to \mathbb { C }$ denote the trace of a matrix:

$$
\operatorname { t r } ( A ) = \sum _ { k = 1 } ^ { n } A _ { k , k } .
$$

(a) Determine a basis for the kernel (or null-space) of tr.

For $X \in M _ { n } ( C )$ , show that $\operatorname { t r } ( X ) = 0$ if and only if there exists an integer m and matrices $A _ { 1 } , \dots , A _ { m } , B _ { 1 } , \dots , B _ { m } \in M _ { n } ( \mathbb { C } )$ so that

$$
X = \sum _ { i = j } ^ { m } A _ { j } B _ { j } - B _ { j } A _ { j }
$$

2. Let V be a finite-dimensional vector space, and let $V ^ { \ast }$ denote the dual space; that is, the space of linear maps $\phi : V \to \mathbb { C }$ .For a set $W \subset V$ , let

$$
W ^ { \perp } = \{ \phi \in V ^ { \star } : \phi ( w ) = 0 \forall w \in W \} .
$$

For a subset $U \subset V ^ { \star }$ , let

$$
{ } ^ { \cdot ^ { \perp } U } = \{ v \in V : \phi ( v ) = 0 \forall \phi \in U \} .
$$

(a) Show that for any subset $W \subset V , \ { \mathsf { \ell } } ^ { \bot } ( W ^ { \bot } ) = \operatorname { s p a n } ( W ^ { \prime } )$ Recall that the span of a set of vectors is the smallest vector sub-space that contains these vectors.

) Let $W \subset V$ be a linear subspace. Give an explicit isomorphism between $( V / W ) ^ { \ast }$ and $W ^ { \perp }$ . Show that it is an isomorphism.

3. Let A be a Hermitian-symmetric n x n complex matrix. Show that if $\langle A v , v \rangle \geq 0$ for all $\boldsymbol { v } \in \mathbb { C } ^ { n }$ , then there exists an n × n matrix T so that $A = T ^ { * } T$

4. Let $\mathcal { A } \equiv M _ { n } ( \mathbb { C } )$ denote the set of all n x n matrices with complex entries. We say that $\mathcal { T } \subseteq A$ is a two-sided ideal in A if

(i) for all $A , B \in \mathcal { T } , A + B \in \mathcal { T }$

(ii) for all $A \in \mathcal { T }$ and $B ^ { \cdot } \in { \cal A } ,$ AB and BA belong to I Show that the only two-sided ideals in A are {0} and A itself.

Analysis.

1. For a subset $X \subset \mathbb { R } ,$ ,we say that X is algebraic, if there exists a family $\mathcal { F }$ of polynomials with rational coefficients, so that ${ \pmb x } \in { \pmb X }$ if and only if ${ \pmb p } ( { \pmb x } ) = 0$ for some $p \in { \mathcal { F } }$

(a) Show that the set Q of rational numbers is algebraic.

(b) Show that the set $\mathbb { R } \setminus \mathbb { Q }$ of irrational numbers is not algebraic.

2. Let X be the set of all infinite sequences $\{ \sigma _ { \mathfrak { n } } \} _ { \mathfrak { n } = 1 } ^ { \infty }$ of 1's and O's endowed with the metric

$$
\operatorname { d i s t } \bigl ( \{ \sigma _ { n } \} _ { n = 1 } ^ { \infty } , \{ \sigma _ { n } ^ { \prime } \} _ { n = 1 } ^ { \infty } \bigr ) = \sum _ { n = 1 } ^ { \infty } \frac { 1 } { 2 ^ { n } } | \sigma _ { n } - \sigma _ { n } ^ { \prime } | .
$$

Give a direct proof that every infinite subset of $\boldsymbol { \cal X }$ has an accumulation point.

3. Let $X , Y$ be two topological spaces. We say that a continuous function $f : X \to Y$ is proper if $f ^ { - 1 } ( K )$ is compact for any compact set $K \subset Y$

(a) Give an example of a function that is proper but not a homeomorphism.

(b) Give an example of a function that is continuous but not proper.

c) Suppose $f : \mathbb { R } \longrightarrow \mathbb { R } \mathrm { \ i s \ } C ^ { 1 }$ (that is, has a continuous derivative) and

$$
| f ^ { \prime } ( x ) | \geq 1 \qquad { \mathrm { f o r ~ a l l ~ } } x \in \mathbb { R } .
$$

Show that f is proper.

4. Suppose $f : \mathbb { R } \to \mathbb { R }$ is $C ^ { 1 }$ (i.e., continuously differentiable). Show that

$$
\operatorname* { l i m } _ { n \to \infty } \sum _ { j = 1 } ^ { n } { \big | } f ( { \frac { j - 1 } { n } } ) - f ( { \frac { j } { n } } ) { \big | }
$$

is equal to

$$
. \int _ { 0 } ^ { 1 } | f ^ { \prime } ( t ) | d t .
$$

5. (a) Suppose

$$
\operatorname* { l i m } _ { n \to \infty } a _ { n } = A
$$

Show that

$$
\operatorname* { l i m } _ { N  \infty } { \frac { 1 } { N } } \sum _ { n = 1 } ^ { N } a _ { n } = A
$$

(b) Show by example that the converse is false.

6. Consider the set of $f : [ 0 , 1 ] \to \mathbb { R }$ that obey

$$
| f ( x ) - f ( y ) | \leq | x - y | \qquad { \mathrm { a n d } } \qquad \int _ { 0 } ^ { 1 } f ( x ) d x = 1 .
$$

Show that this is a compact subset of $C ( [ 0 , 1 ] )$

7. Let us make $M _ { n } ( \mathbb { C } )$ into a metric space in the following fashion:

$$
\operatorname { d i s t } ( A , B ) = \left. \sum _ { i , j } \bigl | A _ { i , j } - B _ { i , j } \bigr | ^ { 2 } \right. ^ { 1 / 2 }
$$

(which is just the usual metric on $\mathbb { R } ^ { n ^ { 2 } } )$

(a) Suppose $F : \mathbb { R } \to M _ { n } ( \mathbb { C } )$ is continuous. Show that the set

$$
\left\{ x \in \mathbb { R } : F ( x ) { \mathrm { ~ i s ~ i n v e r t i b l e } } \right\}
$$

is open (in the usual topology on R).

(b) Show that on the set given above, $x \mapsto [ F ( x ) ] ^ { - 1 }$ is continuous.

8. Let $( X , d )$ be a metric space. Prove that the following are equivalent:

(a) There is a countable dense set.

) There is a countable basis for the topology.

Recall that a collection of open sets U is called a basis if every open set can be written as a union of elements of U.