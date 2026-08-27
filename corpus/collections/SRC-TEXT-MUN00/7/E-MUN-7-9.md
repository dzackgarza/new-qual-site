---
schema: qual/card@1
id: E-MUN-7-9
kind: exercise
title: "Recursion formulas that fall outside the standard principle"
subtitle: Munkres §7.9
classification:
  areas:
  - topology
  topics:
  - Countable and Uncountable Sets
relations: []
review: draft
---

::: {.exercise}

(a) The formula

(\*)

$$
\begin{array}{l} h (1) = 1, \\ h (2) = 2, \\ h (n) = [ h (n + 1) ] ^ {2} - [ h (n - 1) ] ^ {2} \quad \text { for } n \geq 2 \end{array}
$$

is not one to which the principle of recursive definition applies.
Show that nevertheless there does exist a function $h: \mathbb{Z}_+ \to \mathbb{R}$ satisfying this formula.
[Hint: Reformulate (\*) so that the principle will apply and require $h$ to be positive.]

(b) Show that the formula (\*) of part (a) does not determine $h$ uniquely.
[Hint: If $h$ is a positive function satisfying (\*), let $f(i) = h(i)$ for $i \neq 3$, and let $f(3) = -h(3)$ .]

(c) Show that there is no function $h: \mathbb{Z}_{+} \to \mathbb{R}$ satisfying the formula

$$
\begin{array}{l} h (1) = 1, \\ h (2) = 2, \\ h (n) = [ h (n + 1) ] ^ {2} + [ h (n - 1) ] ^ {2} \quad \text { for } n \geq 2. \end{array}
$$
:::
