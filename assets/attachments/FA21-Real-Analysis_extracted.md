## MATH 240 Qualifying Exam

## September 14, 2021

Instructions: 3 hours, open book/notes (only Folland or personal lecture notes; no HW or other solutions). You may use without proofs results proved in Folland up to Section 8.3. Present your solutions clearly, with appropriate detail.

1. (30 pts) Let $f \in C ( \mathbb { R } )$ and let ${ \mathit { A } } \subseteq \mathbb { R }$ be a Borel set such that f is differentiable at each $x \in \mathbb { R } \setminus A$ and $f ^ { \prime } ( x ) = 0$ for all such x.

(a) If A is closed and countable, show that $f$ is constant.

(b) If A has Lebesgue measure 0, must $f$ be constant? Prove or find a counterexample.

2. (30 pts) Does there exist a Borel measurable function $f : \mathbb { R } \to [ 0 , \infty )$ such that $\textstyle \int _ { a } ^ { b } f ( x ) d x = \infty$ for all real numbers $a < b ?$ Either find an example or show that no such f exists.

3. (30 pts) Let $p \in ( 1 , \infty )$ , and for $f \in L ^ { p } ( \mathbb { R } )$ define $\textstyle T f ( x ) : = \int _ { 0 } ^ { 1 } f ( x + y ) d y$

(a) Show that $\| T f \| _ { p } \leq \| f \| _ { p }$ , and equality holds if and only if $f = 0$ almost everywhere.

(b) Prove that $( I - T ) ( L ^ { p } ( \mathbb { R } ) ) \neq L ^ { p } ( \mathbb { R } )$ , where I is the identity map on $L ^ { p } ( \mathbb { R } )$

4. (30 pts) Let functions $f _ { n } \in C ( [ 0 , 1 ] )$ satisfy $\operatorname* { s u p } _ { n } | f _ { n } ( x ) | < \infty$ for each $x \in [ 0 , 1 ]$ . Show that there are $0 \leq a < b \leq 1$ such that $\begin{array} { r } { \operatorname* { s u p } _ { n } \| f _ { n } \chi _ { ( a , b ) } \| _ { u } < \infty } \end{array}$

5. (20 pts) Let $f _ { n } , f \in L ^ { 2 } ( \mathbb { R } )$ satisfy $f _ { n }  f$ weakly and $\left\| { f _ { n } } \right\| _ { 2 } \to \left\| { f } \right\| _ { 2 }$ as $n \to \infty$ . Show that $f _ { n } \to f$ in $L ^ { 2 } ( \mathbb { R } )$

6. (30 pts) Let $\delta _ { x }$ denote the Dirac delta mass at $x \in \mathbb { R } ^ { n }$ . Let $\{ x _ { j } \} _ { j = 1 } ^ { \infty }$ be a sequence in $\mathbb { R } ^ { n }$ $\{ c _ { j } \} _ { j = 1 } ^ { \infty }$ a sequence of positive numbers, and $\mu$ the Borel measure on $\mathbb { R } ^ { n }$ corresponding to the series $\textstyle \sum _ { j = 1 } ^ { \infty } c _ { j } \delta _ { x _ { j } }$ . Prove that $\mu$ is Radon if and only if for all convergent subsequences $\{ x _ { j _ { k } } \} _ { k = 1 } ^ { \infty }$ it holds that $\textstyle \sum _ { k = 1 } ^ { \infty } c _ { j _ { k } } < \infty$

7. (30 pts) For any $f \in L ^ { 2 } ( \mathbb { R } ) \cap C ^ { 1 } ( \mathbb { R } )$ show that

$$
\left( \int _ { \mathbb { R } } x ^ { 2 } | f ( x ) | ^ { 2 } d x \right) \left( \int _ { \mathbb { R } } \xi ^ { 2 } | { \hat { f } } ( \xi ) | ^ { 2 } d \xi \right) \geq { \frac { 1 } { 1 6 \pi ^ { 2 } } } \left( \int _ { \mathbb { R } } | f ( x ) | ^ { 2 } d x \right) ^ { 2 }
$$

Here $\hat { f }$ is the Fourier transform of f and dx, $d \xi$ represent the Lebesgue measure on $\mathbb { R } .$