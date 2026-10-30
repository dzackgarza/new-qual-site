---
schema: qual/card@1
id: P-BKS07-6B
kind: problem
title: An integral curve confined to a compact set has a limit at the right endpoint
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $U$ be a non-empty open subset of $\RR^{d}$ and let $f \colon U \to \RR^{d}$ be a continuous vector field defined on $U$. Let $K$ be a compact subset of $U$ and let $b > 0$. Suppose $\varphi \colon [0, b) \to K$ is a continuous function satisfying
$$
\varphi(t) = \varphi(0) + \int_{0}^{t} f(\varphi(s))\, ds, \qquad (0 \leq t < b).
$$
Prove that $\lim_{t \to b^{-}} \varphi(t)$ exists, where $t \to b^{-}$ means $t$ approaches $b$ from the left.
:::

::: {.solution}
Let $M = \operatorname* { s u p } _ { y \in K } \norm{ f ( y ) }$ . For any two points $t _ { 1 } , t _ { 2 } \in [ 0 , b )$

$$
\norm{ \varphi ( t _ { 2 } ) - \varphi ( t _ { 1 } ) } = \norm{ \int _ { t _ { 1 } } ^ { t _ { 2 } } f ( \varphi ( t ) ) d t } \leq M \abs{ t _ { 2 } - t _ { 1 } }
$$

so $\varphi$ is Lipschitz continuous on [0, b) and hence preserves Cauchy sequences.
Let $t _ { k } \to b$ from the left.
Then $\varphi ( t _ { k } )$ is Cauchy and hence converges to some $y _ { 0 } ~ \in ~ \RR ^ { d }$ . We claim that $\lim _ { t \to b ^ { - } } \varphi ( t ) = y _ { 0 }$. Let $\varepsilon > 0$ and choose k large enough that $\abs{ t _ { k } - b } < \frac { \varepsilon } { 4 ( M + 1 ) }$ and $\norm{ \varphi ( t _ { k } ) - y _ { 0 } } < \frac { \varepsilon } { 2 }$ . Then for $0 < b - t < \delta = \frac { \varepsilon } { 4 ( M + 1 ) }$ we have $\abs{ t - t _ { k } } < \frac { \varepsilon } { 2 ( M + 1 ) }$, so

$$
\begin{aligned} \norm{ \varphi ( t ) - y _ { 0 } } &\le \norm{ \varphi ( t ) - \varphi ( t _ { k } ) } + \norm{ \varphi ( t _ { k } ) - y _ { 0 } } \\ &\le M \abs{ t - t _ { k } } + \frac { \varepsilon } { 2 } < \frac { \varepsilon } { 2 } + \frac { \varepsilon } { 2 } = \varepsilon \end{aligned}
$$

as required.
:::

::: {.solution}
Because of the given integral equation, it suffices to apply the following claim to the function $g ( s ) = f ( \varphi ( s ) )$ : for any continuous bounded function $g \colon [ 0 , b ) \to \RR ^ { d }$ , the limit $\lim _ { t \to b ^ { - } } \int _ { 0 } ^ { t } g ( s ) \, ds$ exists.
To prove this, it suffices to prove that for every increasing sequence $\left( t _ { k } \right)$ in $[ 0 , b )$ tending to $b$, the limit $\lim _ { k \to \infty } \int _ { 0 } ^ { t _ { k } } g ( s ) \, ds$ exists.
This follows from the dominated convergence theorem applied to the sequence of functions

$$
g _ { k } ( s ) : = { \left\{ \begin{array} { l l } { g ( s ) , } & { { \mathrm { ~ i f ~ } } s \in [ 0 , t _ { k } ] } \\ { 0 , } & { { \mathrm { ~ i f ~ } } s \in ( t _ { k } , b ] . } \end{array} \right. }
$$
:::
