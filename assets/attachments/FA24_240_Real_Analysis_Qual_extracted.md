## MATH 240 Qualifying Exam

Sept. 12, 2024

Instructions: 3 hours, open book/notes (only Folland or personal lecture notes; no HW or other solutions). You may use without proofs results proved in Folland Chapters 1-8. Present your solutions clearly, with appropriate detail.

1. (25 pts) Let $E \subseteq \mathbb { R }$ be (Lebesgue) measurable and satisfy $E + r = E$ for every rational number r. Show that either E or $E ^ { c }$ has measure 0.

2. (40 pts) For any $n \in \mathbb N$ , find all Lebesgue measurable sets $E \subseteq \mathbb { R } ^ { n }$ such that there exists some $f _ { E } \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ satisfying

$$
\operatorname* { l i m } _ { r  0 } \frac { 1 } { m ( B ( r , x ) ) } \int _ { B ( r , x ) } f _ { E } ( y ) d y = \infty
$$

$$
{ \mathrm { f o r ~ e a c h ~ } } x \in E .
$$

3. (30 pts) Let X be a topological vector space. A net (or, less generally, a sequence) $\langle x _ { \alpha } \rangle _ { \alpha \in A }$ in X is Cauchy if the net of pairwise differences $\langle x _ { \alpha } - x _ { \beta } \rangle _ { ( \alpha , \beta ) \in A \times A }$ , with $A \times A$ directed by the rule $( \bar { \alpha } , \beta ) \lesssim ( \alpha ^ { \prime } , \beta ^ { \prime } ) \stackrel { - } { \Leftrightarrow } ( \alpha \lesssim \alpha ^ { \prime }$ and $\beta \lesssim \beta ^ { \prime } )$ , converges to $0 \in X$ . Prove that if X is first countable and every Cauchy sequence in X converges, then every Cauchy net in X converges.

4. (25 pts) Recall that the Riemann-Lebesgue lemma implies that for all $f \in L ^ { 1 } ( [ 0 , 1 ] , m )$

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { 1 } f ( x ) e ^ { i n x } \ d x = 0 .
$$

Show that there is no rate of convergence for the above limit that is independent of $f .$ Specifically, show that there cannot exist any sequence of positive numbers $\left( a _ { n } \right)$ such that $a _ { n } \to \infty$ and for every $f \in L ^ { 1 } ( [ 0 , 1 ] , m )$ there is a constant $C _ { f } < \infty$ with

$$
\left| \int _ { 0 } ^ { 1 } f ( x ) e ^ { i n x } ~ d x \right| \leq { \frac { C _ { f } } { a _ { n } } }
$$

$$
\mathrm { f o r ~ e a c h } \ n \in \mathbb { N } .
$$

Hint: If such $\left( a _ { n } \right)$ existed, find a sequence of linear functionals that yields a contradiction.

5. (40 pts) Let X be an LCH space.

(a) $\operatorname { I f } \mu$ is a Radon measure on X satisfying $\mu ( X ) = \infty$ , prove that there is a non-negative function $f \in C _ { 0 } ( X )$ satisfying $\textstyle { \int { f }  d \mu = \infty }$

(b) Prove that every positive linear functional on $C _ { 0 } ( X )$ is bounded.

6. (25 pts) Show that for any $p > 1$ , there is a constant $C _ { p } < \infty$ such that

$$
\sum _ { k = - \infty } ^ { \infty } | { \hat { f } } ( k ) | \leq \| f \| _ { L ^ { 1 } } + C _ { p } \| f ^ { \prime } \| _ { L ^ { p } }
$$

$$
f \in C ^ { 1 } ( \mathbb { T } )
$$