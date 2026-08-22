---
schema: qual/card@1
id: E-SS4.EX-10
kind: exercise
title: "This exercise generalizes some of the properties of  related to the fact that it"
classification:
  areas:
  - complex-analysis
  topics: ['Fourier Transform', 'Poisson Summation']
relations: []
review: draft
solved: false
---

::: exercise
10. This exercise generalizes some of the properties of $e ^ { - \pi x ^ { 2 } }$ related to the fact that it is its own Fourier transform.

Suppose $f ( z )$ is an entire function that satisfies

$$

| f (x + i y) | \leq c e ^ {- a x ^ {2} + b y ^ {2}}

$$

for some $a , b , c > 0$ . Let

$$

\hat {f} (\zeta) = \int_ {- \infty} ^ {\infty} f (x) e ^ {- 2 \pi i x \zeta} d x.

$$

Then, $\hat { f }$ is an entire function of ζ that satisfies

$$

| \hat {f} (\xi + i \eta) | \leq c ^ {\prime} e ^ {- a ^ {\prime} \xi^ {2} + b ^ {\prime} \eta^ {2}}

$$

for some $a ^ { \prime } , b ^ { \prime } , c ^ { \prime } > 0$

[Hint: To prove $\hat { f } ( \xi ) = O ( e ^ { - a ^ { \prime } \xi ^ { 2 } } )$ , assume $\xi > 0$ and change the contour of integration to $x - i y$ for some $y > 0$ fixed, and $- \infty < x < \infty$ . Then

$$

\hat {f} (\xi) = O (e ^ {- 2 \pi y \xi} e ^ {b y ^ {2}}).

$$

Finally, choose $y = d \xi$ where d is a small constant.]
:::
