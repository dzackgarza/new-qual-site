# NOTES ON CONVERGENT SEQUENCES AND ON SUBSEQUENCES

DeÖnition 2.7. A sequence in a set X is a function $\mathbf { P } : \mathbb { N } \to X$ : We denote it by $\left\{ \mathbf { P } \left( n \right) \right\} \mathrm { ~ o r ~ }$ more commonly, by $\{ p _ { n } \}$

Let $\{ p _ { n } \} _ { n = 1 } ^ { \infty }$ be a sequence in a metric space. A subsequence of $\left\{ p _ { n } \right\} _ { n = 1 } ^ { \infty }$ is a sequence of the form $\left\{ p _ { n \left( i \right) } \right\} _ { i = 1 } ^ { \infty }$ , where $n \left( 1 \right) < n \left( 2 \right) < n \left( 3 \right) < \cdot \cdot \cdot$ : We typically write $\{ p _ { n _ { i } } \} _ { i = 1 } ^ { \infty }$ , that is, we replace $n \left( i \right)$ by the notation $n _ { i }$

Remark. In $\{ p _ { n } \}$ , n is represents a positive integer, i.e., $n = 1 , 2 , 3 , \ldots$ . Whereas, in $\left\{ p _ { n ( i ) } \right\}$ , n represents an increasing function $n : \mathbb { N } \to \mathbb { N }$ and $i = 1 , 2 , 3 , \dots$

Exercise. Convince yourself that a subsequence of a sequence $\mathbf { P } : \mathbb { N } \longrightarrow X$ is simply a function $\mathbf { P } \circ n : \mathbb { N }  X$ ; where $n : \mathbb { N } \to \mathbb { N }$ is increasing. Hint: The subsequence is $\{ \mathbf { P } \circ n ( i ) \}$ ; which may be rewritten as $\left\{ p _ { n ( i ) } \right\}$

DeÖnition 3.1. A sequence $\{ p _ { n } \}$ in X is said to converge to $p \in X$ if for every $\varepsilon > 0$ there exists $N \in  { \mathbb { N } }$ such that $n \geq N$ implies that $d \left( p _ { n } , p \right) < \varepsilon$

Example. Consider the sequence $\left\{ p _ { n } \right\} _ { n = 1 } ^ { \infty }$ ; where $p _ { n } = ( - 1 ) ^ { n }$ : Then $\{ p _ { 2 i } \} _ { i = 1 } ^ { \infty }$ is a subsequence (where we deÖne $n \left( i \right) = 2 i )$ . Here, the original sequence is $\{ - 1 , 1 , - 1 , 1 , . . . \}$ and the subsequence is $\{ 1 , 1 , 1 , 1 , \ldots \}$ : The original sequence diverges, whereas the subsequence converges.

Lemma. Suppose that $\{ a _ { n } \}$ is a sequence of positive numbers with li $\mathrm { n } _ { n  \infty } a _ { n } = 0$ . If $p \in X$ and $\{ p _ { n } \}$ is a sequence in X such that d $( p _ { n } , p ) \leq a _ { n }$ for each $n \in \mathbb { N }$ , then $\{ p _ { n } \}$ converges to p.

Proof. Let $\varepsilon > 0$ . Since $\scriptstyle \operatorname* { l i m } _ { n \to \infty } a _ { n } = 0$ , there exists $N \in \mathbb N$ such that $a _ { n } < \varepsilon { \mathrm { ~ f o r ~ } } n \geq N$ . This implies that

$$
d \left( p _ { n } , p \right) \leq a _ { n } < \varepsilon
$$

for $n \geq N . \ \square$

Theorem 3.7. The set of all subsequential limits of a sequence $\left\{ p _ { n } \right\}$ in a metric space X is a closed subset of X:

Proof. Let E be the set of all $p \in X$ with the property that there exists a subsequence of $\{ p _ { n } \}$ which converges to p. Let $q \in E ^ { \prime }$ . We need to show that $q \in E$

Let $n _ { 1 } = 1$ . Let $k \geq 2$ and suppose that we have chosen positive integers $n _ { 1 } < n _ { 2 } < \cdots < n _ { k - 1 }$ Since $q \in E ^ { \prime }$ , there exists $q _ { k } \in E$ such that $\begin{array} { r } { d \left( q _ { k } , q \right) < { \frac { 1 } { k } } } \end{array}$ : Since $q _ { k } \in E$ , there exists a subsequence of $\{ p _ { n } \}$ which converges to $q _ { k }$ . This implies there exists an integer $n _ { k } > n _ { k - 1 }$ such that $\begin{array} { r } { d \left( p _ { n _ { k } } , q _ { k } \right) < \frac { 1 } { k } } \end{array}$ Then

$$
d \left( p _ { n _ { k } } , q \right) \leq d \left( p _ { n _ { k } } , q _ { k } \right) + d \left( q _ { k } , q \right) < \frac 2 k .
$$

(We have deÖned the increasing sequence of positive integers $\{ n _ { k } \} _ { k = 1 } ^ { \infty }$ by induction.) Since the subsequence $\{ p _ { n _ { k } } \} _ { k = 1 } ^ { \infty }$ has the property that $\begin{array} { r } { d \left( p _ { n _ { k } } , q \right) < \frac { 2 } { k } } \end{array}$ for $k \geq 2$ and since lim $\begin{array} { r } { \mathfrak { l } _ { k  \infty } \frac { 2 } { k } = 0 } \end{array}$ , we conclude by the lemma that $\{ p _ { n _ { k } } \} _ { k = 1 } ^ { \infty }$ converges to q: Hence $q \in E , \sqsubseteq$