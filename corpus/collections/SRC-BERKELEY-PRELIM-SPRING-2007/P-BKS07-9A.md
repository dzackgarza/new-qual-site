---
schema: qual/card@1
id: P-BKS07-9A
kind: problem
title: UC Berkeley Spring 2007 prelim 9A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Suppose b and L are positive constants and $f : [ 0 , b ] \to \mathbb { R }$ is continuous and satisfies

$$
f ( x ) \geq L \int _ { 0 } ^ { x } f ( t ) d t , \qquad ( 0 \leq x \leq b ) .
$$

Show that $f ( x ) \geq 0$ for $0 \leq x \leq b$
:::

::: {.solution}
Let $\textstyle F ( x ) = \int _ { 0 } ^ { x } f ( t ) d t$ . Since f is continuous, F is differentiable and we have

$$
F ^ { \prime } ( x ) = f ( x ) \geq L F ( x ) , \qquad ( 0 \leq x \leq b ) .
$$

Thus, for $0 \leq t \leq b$ we have

$$
F ^ { \prime } ( t ) - L F ( t ) \geq 0 ,
$$

$$
\begin{array} { r } { \big ( F ^ { \prime } ( t ) - L F ( t ) \big ) e ^ { - L t } \geq 0 , } \end{array}
$$

$$
\frac { d } { d t } \Big ( F ( t ) e ^ { - L t } \Big ) \geq 0 ,
$$

and since definite integrals preserve inequalities:

$$
F ( x ) e ^ { - L x } - F ( 0 ) e ^ { 0 } = \int _ { 0 } ^ { x } { \frac { d } { d t } } { \Big ( } F ( t ) e ^ { - L t } { \Big ) } d t \geq \int _ { 0 } ^ { x } 0 d t = 0 , \quad ( 0 \leq x \leq b ) .
$$

Since $F ( 0 ) = 0$ and $e ^ { - L x } > 0$ , we learn that $F ( x ) \geq 0 { \mathrm { ~ f o r ~ } } 0 \leq x \leq b$ , hence the original inequality $f ( x ) \geq L F ( x )$ gives the desired result.

An alternative proof might run as follows.
Let $x _ { 0 } = \operatorname* { s u p } \{ x < b ~ : ~ f ( t ) \geq 0$ for $t \in [ 0 , x ] \}$ We know $x _ { 0 } \geq 0$ since $f ( 0 ) \geq 0$ . We must show that $x _ { 0 } = b$ Suppose to the contrary that $x _ { 0 } < b$ . Since $f ( x )$ is continuous and non-negative to the left of $x _ { 0 } , f ( x _ { 0 } ) \geq 0$ . On the other hand, there are points $x > x _ { 0 }$ arbitrarily close to $x _ { 0 }$ at which $f ( x ) < 0$ . Thus $f ( x _ { 0 } ) = 0$ . The given inequality now implies that $f ( x ) = 0$ for $0 \leq x \leq x _ { 0 }$ . Now define $x _ { 1 } = \operatorname* { m i n } ( x _ { 0 } + L ^ { - 1 } , b )$ Then there is an $x _ { 2 }$ in the interval $x _ { 0 } < x _ { 2 } < x _ { 1 }$ which satisfies $f ( x _ { 2 } ) < 0$ . Let $\varepsilon = | f ( x _ { 2 } ) |$ The given inequality implies that $\begin{array} { r } { f ( x ) \geq L \int _ { x _ { 0 } } ^ { x } f ( t ) } \end{array}$ dt for $x _ { 0 } \leq x \leq x _ { 1 }$ . Thus $u ( x ) = f ( x ) + \varepsilon$ satisfies $u ( x _ { 0 } ) = \varepsilon , u ( x _ { 2 } ) = 0$ , and

$$
u ( x ) \geq L \int _ { x _ { 0 } } ^ { x } u ( t ) - \varepsilon d t + \varepsilon = \int _ { x _ { 0 } } ^ { x } u ( t ) d t + \varepsilon [ 1 - L ( x - x _ { 0 } ) ] \geq \int _ { x _ { 0 } } ^ { x } u ( t ) d t
$$

for $x _ { 0 } \leq x \leq x _ { 1 }$ But since u is continuous and $u ( x _ { 0 } ) = \varepsilon > 0$ , it’s impossible for u to reach 0 over the interval $x _ { 0 } < x < x _ { 1 }$ , for at the first crossing $x _ { 3 }$ where $u ( x _ { 3 } ) = 0$ , the integral $\textstyle \int _ { x _ { 0 } } ^ { x _ { 3 } } u ( x ) d x > 0$ . Thus the assumption that $u ( x _ { 2 } ) = 0$ leads to a contradiction, and we conclude that $x _ { 0 } = b$
:::
