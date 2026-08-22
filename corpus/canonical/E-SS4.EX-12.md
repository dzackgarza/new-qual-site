---
schema: qual/card@1
id: E-SS4.EX-12
kind: exercise
title: "The principle that a function and its Fourier transform cannot both be too small"
classification:
  areas:
  - complex-analysis
  topics: ['Fourier Transform', 'Poisson Summation']
relations: []
review: draft
solved: false
---

::: exercise
12. The principle that a function and its Fourier transform cannot both be too small at infinity is illustrated by the following theorem of Hardy.

If $f$ is a function on R that satisfies

$$

f (x) = O (e ^ {- \pi x ^ {2}}) \quad \mathrm{and} \quad \hat {f} (\xi) = O (e ^ {- \pi \xi^ {2}}),

$$

then f is a constant multiple of $e ^ { - \pi x ^ { 2 } }$ . As a result, if $f ( x ) = O ( e ^ { - \pi A x ^ { 2 } } )$ , and $\hat { f } ( \xi ) = O ( e ^ { - \pi B \xi ^ { 2 } } )$ , with $A B > 1$ and $A , B > 0$ , then f is identically zero.

(a) If f is even, show that $\hat { f }$ extends to an even entire function. Moreover, if $g ( \dot { z } ) = \hat { f } ( z ^ { 1 / 2 } )$ , then $g$ satisfies

$$

| g (x) | \leq c e ^ {- \pi x} \quad \text { and } \quad | g (z) | \leq c e ^ {\pi R \sin^ {2} (\theta / 2)} \leq c e ^ {\pi | z |}

$$

when $x \in \mathbb { R }$ and $z = R e ^ { i \theta }$ with $R \geq 0$ and $\theta \in \mathbb { R }$

(b) Apply the Phragm´en-Lindel¨of principle to the function

$$

F (z) = g (z) e ^ {\gamma z} \quad \mathrm{where} \gamma = i \pi \frac {e ^ {- i \pi / (2 \beta)}}{\sin \pi / (2 \beta)}

$$

and the sector $0 \leq \theta \leq \pi / \beta < \pi$ , and let $\beta \to \pi$ to deduce that $e ^ { \pi z } g ( z )$ is bounded in the closed upper half-plane. The same result holds in the lower half-plane, so by Liouville’s theorem $e ^ { \pi z } g ( z )$ is constant, as desired.

(c) If $f$ is odd, then ${ \hat { f } } ( 0 ) = 0$ , and apply the above argument to $\hat { f } ( z ) / z$ to deduce that $\boldsymbol { f } = \boldsymbol { \hat { f } } = 0$ . Finally, write an arbitrary $f$ as an appropriate sum of an even function and an odd function.
:::
