---
schema: qual/card@1
id: P-BKF04-2B
kind: problem
title: UC Berkeley Fall 2004 prelim 2B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $f \colon  { \mathbb { R } } ^ { 3 } \to  { \mathbb { R } }$ be a continuous function of compact support $( \mathrm { i . e . , ~ } f$ vanishes outside some bounded set).

(a) Show that

$$
u ( x ) : = \int { \frac { f ( y ) } { | x - y | } } d y
$$

converges, where the integral is over all $\boldsymbol { y } \in \mathbb { R } ^ { 3 }$

(b) Show that $\scriptstyle \operatorname* { l i m } _ { | x | \to \infty } u ( x ) | x |$ exists.
:::

::: {.solution}
(a) Let M be the maximum value of $| f |$ (this exists, since f is 0 outside some compact set and is continuous). Fix x. Choose R large enough that $f ( y ) = 0 { \mathrm { ~ i f ~ } } | x - y | > R$ Using polar coordinates centered at x, we have

$$
\int { \frac { | f ( y ) | } { | x - y | } } d y \leq \int _ { 0 } ^ { R } { \frac { M } { r } } ( 4 \pi r ^ { 2 } d r ) ,
$$

which converges, so the integral defining $u ( x )$ converges absolutely.

(b) By writing $f ( y ) = \operatorname* { m a x } \{ f ( y ) , 0 \} + \operatorname* { m i n } \{ f ( y ) , 0 \}$ , we may reduce to the case that $f$ is nonnegative everywhere. Let $R _ { 0 } > 0$ be such that $f ( y ) = 0$ for $| y | > R _ { 0 }$ $\operatorname { I f } \left| x \right| \geq n R _ { 0 }$ where n is large, and $| y | \le R _ { 0 }$ , then

$$
{ \frac { | x | } { | x - y | } } \leq { \frac { | x | } { | x | - | y | } } = { \frac { 1 } { 1 - | y | / | x | } } \leq { \frac { 1 } { 1 - 1 / n } } = { \frac { n } { n - 1 } }
$$

$$
{ \frac { | x | } { | x - y | } } \geq { \frac { | x | } { | x | + | y | } } = { \frac { 1 } { 1 + | y | / | x | } } \leq { \frac { 1 } { 1 + 1 / n } } = { \frac { n } { n + 1 } } .
$$

Hence

$$
{ \frac { n } { n + 1 } } \int f d y \leq u ( x ) | x | \leq { \frac { n } { n - 1 } } \int f d y
$$

for large x. Thus lim $| x | {  } \infty u ( x ) | x | = \textstyle \int f d y$
:::
