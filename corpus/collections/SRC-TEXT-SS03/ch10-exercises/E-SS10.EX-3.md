---
schema: qual/card@1
id: E-SS10.EX-3
kind: exercise
title: "More generally, consider the diference equation given by the initial values u<su"
classification:
  areas:
  - complex-analysis
  topics: ['Theta Functions', 'Modular Forms', 'Partitions']
relations: []
review: draft
---

::: exercise
3. More generally, consider the diference equation given by the initial values u<sub>0</sub> and $u _ { 1 }$ , and the recurrence relation $u _ { n } = a u _ { n - 1 } + b u _ { n - 2 }$ for $n \geq 2$ . Define the generating function associated to $\{ u _ { n } \} _ { n = 0 } ^ { \infty }$ by $\textstyle U ( x ) = \sum _ { n = 0 } ^ { \infty } u _ { n } x ^ { n }$ . The recurrence relation implies that $U ( x ) ( 1 - a x - b x ^ { 2 } ) = u _ { 0 } + ( u _ { 1 } - a u _ { 0 } ) x$ in a neighborhood of the origin.
   If α and $\beta$ denote the roots of the polynomial $p ( x ) = x ^ { 2 } - a x - b ;$ then we may write

Figure 2. Appearance of the golden mean

$$
U (x) = \frac {u _ {0} + (u _ {1} - a u _ {0}) x}{(1 - \alpha x) (1 - \beta x)} = \frac {A}{1 - \alpha x} + \frac {B}{(1 - \beta x)} = A \sum_ {n = 0} ^ {\infty} \alpha^ {n} x ^ {n} + B \sum_ {n = 0} ^ {\infty} \beta^ {n} x ^ {n},
$$

where it is an easy matter to solve for A and B. Finally, this gives $u _ { n } = A \alpha ^ { n } +$ $B \beta ^ { n }$ . Note that this approach yields a solution to our problem if the roots of $p$ are distinct, namely $\alpha \neq \beta$ . A variant of the formula holds if $\alpha = \beta$
:::
