---
schema: qual/card@1
id: P-VT4TV
kind: problem
title: "Invert $\\sin(z)$, one coefficient at a time"
classification:
  areas:
  - complex-analysis
  topics:
  - laurent-series
  - power-series
  - trigonometry
relations: []
review: draft
solved: true
---
:::{.exercise title="Invert $\sin(z)$, one coefficient at a time"}
Find $1/\sin(z)$ using this method.
:::

:::{.solution}
Note that the leading coefficient of the expansion for $\sin(z)$ is 0, so this can't be inverted directly. 
A standard trick: factor out the smallest power of $z$ to get a piece with a nonzero leading coefficient, and invert that instead.
Write
\[
\sin(z) = z - {1\over 3!}z^3 + {1\over 5!}z^5 - \bigo(z^7) = z f(z) \da z(1 + c_2z^2 + c_4 z^4 + \bigo(z^6))
,\]
where

- $c_0 = 1$
- $c_2 = -{1\over 3!}$
- $c_4 = {1\over 5!}$
- $c_i = 0$ for $i$ odd.

Writing $B(z) \da {1\over f(z)} = \sum b_k z^k$, we have

- $b_0 = c_0\inv = 1$
- $b_2 = -(c_2 b_0 + c_1 b_1) = -c_2$
- $b_4 = -(c_4 b_0 + c_2 b_2) = c_2^2 - c_4$

Thus $1/B(z) = 1 -c_2z^2 + (c_2^2-c_4)z^4 + \bigo(z^6)$, and
\[
{1\over \sin(z)} 
&= {1\over z} {1\over B(z)} \\
&= {1\over z} - c_2 z + (c_2^2 - c_4)z^3 + \bigo(z^5) \\
&= {1\over z} + {1\over 3!} z + ({1\over 3! 3!} - {1\over 5!})z^3 + \bigo(z^5) \\
&=
{1\over z} + {1\over 3!}z + {7\over 360}z^3 + \bigo(z^5) 
.\]
:::

