---
schema: qual/card@1
id: P-PRACT20-W6-02
kind: problem
title: The nested radical $\sqrt{x+\sqrt{x+\sqrt{x+\cdots}}}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Fix $x > 0$ . Give a rigorous meaning to $\sqrt { x + { \sqrt { x + { \sqrt { x + \cdots } } } } }$ by proving that the sequence

$$
a _ { 0 } = \sqrt { x } , \quad a _ { n } = \sqrt { x + a _ { n - 1 } } , \ n = 1 , 2 , 3 , \dots .
$$

converges and finding the limit.
What happens as $x \searrow 0 ?$
:::

::: {.solution}
We prove that $a _ { n }$ is increasing an bounded above, and thus converges by the monotone convergence theorem.
Note that $a _ { 1 } = { \sqrt { x + { \sqrt { x } } } } \geq { \sqrt { x } } = a _ { 0 }$ . Now assume that $a _ { n } \geq a _ { n - 1 }$ for some $n \in \mathbb { N }$ . Then

$$
x + a _ { n } \geq x + a _ { n - 1 } \implies \sqrt { x + a _ { n } } \geq \sqrt { x + a _ { n - 1 } } \implies a _ { n + 1 } \geq a _ { n } .
$$

This induction proves that $a _ { n }$ is an increasing sequence.√ √

Next, we see that $\begin{array} { r } { a _ { 0 } = \sqrt { x } = \frac { \sqrt { 4 x } } { 2 } \le \frac { 1 + \sqrt { 1 + 4 x } } { 2 } } \end{array}$ . Again, assume that $\textstyle a _ { n } \leq { \frac { 1 + { \sqrt { 1 + 4 x } } } { 2 } }$ for some $n \in \mathbb { N }$ . Note that

$$
\left( { \frac { 1 + { \sqrt { 1 + 4 x } } } { 2 } } \right) ^ { 2 } = { \frac { 1 + 2 { \sqrt { 1 + 4 x } } + 1 + 4 x } { 4 } } = x + { \frac { 1 + { \sqrt { 1 + 4 x } } } { 2 } } .
$$

Then

$$
a _ { n + 1 } = { \sqrt { x + a _ { n } } } \leq { \sqrt { x + { \frac { 1 + { \sqrt { 1 + 4 x } } } { 2 } } } } = { \sqrt { \left( { \frac { 1 + { \sqrt { 1 + 4 x } } } { 2 } } \right) ^ { 2 } } } = { \frac { 1 + { \sqrt { 1 + 4 x } } } { 2 } } .
$$

This shows by induction that $a _ { n }$ is bounded above.
Hence there is a limit $a _ { n }  a \in \mathbb { R }$ . Taking the limit on both sides of the recursive relationship, we see

$$
a = { \sqrt { x + a } } \implies a ^ { 2 } - a - x = 0 \implies a = { \frac { 1 \pm { \sqrt { 1 + 4 x } } } { 2 } } .
$$

Note that each member of the sequence is positive and thus the limit is positive, and so we can ignore the false root.
This shows that for $x > 0$ ,

$$
{ \sqrt { x + { \sqrt { x + { \sqrt { x + \cdots } } } } } } = { \frac { 1 + { \sqrt { 1 + 4 x } } } { 2 } } .
$$

However, this formula fails for $x = 0$ . If $x = 0$ , then $a _ { n } = 0$ for all n and thus the limit is zero, which does not agree with the limit of the above formula as x $\searrow 0$
:::
