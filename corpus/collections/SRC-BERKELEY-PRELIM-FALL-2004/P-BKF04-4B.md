---
schema: qual/card@1
id: P-BKF04-4B
kind: problem
title: UC Berkeley Fall 2004 prelim 4B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Evaluate $I ( w ) : = \int _ { 0 } ^ { \infty } { \frac { e ^ { i w t } } { \sqrt { t } } }$ dt for every nonzero real number w. You may use the formula $\int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } } d x = { \sqrt { \pi } }$
:::

::: {.solution}
The substitution $t = u ^ { 2 }$ yields

$$
I ( w ) = 2 \int _ { 0 } ^ { \infty } f ( u ) d u .
$$

where $f ( u ) : = e ^ { i w u ^ { 2 } }$ . Suppose $w > 0$ . For $R > 0$ , let $\gamma _ { 1 }$ be the straight-line path from 0 to R, let $\gamma _ { 2 }$ be the circular arc $R e ^ { i t }$ for $t \in [ 0 , \pi / 4 ]$ , and let $\gamma _ { 3 }$ be the straight-line path from $R e ^ { i \pi / 4 }$ to 0. By Cauchy’s Theorem, $\textstyle \sum _ { j = 1 } ^ { 3 } \int _ { \gamma _ { j } } f ( u ) d u = 0$ . For $u = R e ^ { i t }$ , we have

$$
| f ( u ) | = e ^ { \mathrm { R e } ( i w u ^ { 2 } ) } = e ^ { - w \mathrm { I m } ( u ^ { 2 } ) } = e ^ { - w R ^ { 2 } \sin ( 2 t ) } \le e ^ { - w R ^ { 2 } ( 2 ( 2 t ) / \pi ) } ,
$$

where the last step comes from the inequality sin $x \leq 2 x / \pi$ for $x \in [ 0 , \pi / 2 ]$ (concavity of sin x on this interval). Therefore

$$
\left| \int _ { \gamma _ { 2 } } f ( u ) d u \right| \leq \int _ { 0 } ^ { \infty } e ^ { - w R ^ { 2 } ( 2 ( 2 t ) / \pi ) } d t = \frac { \pi } { 4 w R ^ { 2 } } ,
$$

which goes to 0 as $R \to \infty$ . Hence

$$
\begin{array} { r l } { \iota ( w ) - 2 \displaystyle \operatorname* { l i m } _ { m \to \infty } \int _ { \gamma } \langle w | \hat { \sigma } \rangle \ : d w } \\ { } & { = - 2 \displaystyle \operatorname* { l i m } _ { m \to \infty } \int _ { - \infty } ^ { \infty } \int _ { \gamma } \langle i ( \lambda ) ^ { m } \rangle } \\ { } & { = 2 \displaystyle \int _ { \gamma } \eta _ { \varepsilon } \langle i ( \lambda ) ^ { m } | \hat { \sigma } \rangle \ : d w } \\ { } & { = - 2 \displaystyle \int _ { \gamma } \int _ { \gamma } \langle i ( \lambda ^ { m } ) ^ { m } \rangle \ : \theta \ : \mathrm { d } w } \\ { } & { = - \theta ^ { \mathrm { d i d } } \displaystyle \int _ { - \infty } ^ { \infty } \theta ^ { \mathrm { d i d } } \int _ { \gamma } \theta ^ { \mathrm { d i d } } } \\ { } & { = \theta ^ { \mathrm { d i d } } \displaystyle \int _ { - \infty } ^ { \infty } \theta ^ { \mathrm { d i d } } \int _ { \gamma } \theta ^ { \mathrm { d i d } } } \\ { } & { = \frac { 1 + \frac { 1 } { 2 } } { \sqrt { 2 } } \displaystyle \int _ { - \infty } ^ { \infty } \theta ^ { \mathrm { d i d } } \int _ { \gamma } \theta ^ { \mathrm { d i d } } } \\ { } & { = ( 1 + \lambda ) \displaystyle \frac { 1 } { \sqrt { 2 } } \frac { 1 } { \omega ^ { m } } . } \end{array}
$$

Also, $I ( - w )$ is the complex conjugate of $I ( w )$ . Therefore, for any w $\neq 0$

$$
I ( w ) = ( 1 + i \mathrm { s g n } ( w ) ) \sqrt { \frac { \pi } { 2 | w | } } .
$$
:::
