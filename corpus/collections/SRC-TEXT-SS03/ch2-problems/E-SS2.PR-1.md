---
schema: qual/card@1
id: E-SS2.PR-1
kind: exercise
title: "Here are some examples of analytic functions on the unit disc that cannot be ext"
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
relations: []
review: draft
---

::: exercise
1. Here are some examples of analytic functions on the unit disc that cannot be extended analytically past the unit circle. The following definition is needed. Let $f$ be a function defined in the unit disc D, with boundary circle C. A point w on C is said to be regular for $f$ if there is an open neighborhood U of w and an analytic function $g$ on $U _ { i }$ , so that $f = g$ on $\mathbb { D } \cap U$ . A function f defined on D cannot be continued analytically past the unit circle if no point of C is regular for $f .$

(a) Let

$$
f (z) = \sum_ {n = 0} ^ {\infty} z ^ {2 ^ {n}} \quad \text { for } | z | <   1.
$$

Notice that the radius of convergence of the above series is 1. Show that f cannot be continued analytically past the unit disc. [Hint: Suppose $\theta = { 2 \pi p } / { 2 ^ { k } }$ , where $p$ and k are positive integers. Let $z = r e ^ { i \theta }$ ; then $| f ( r e ^ { i \theta } ) | \longrightarrow \infty \mathrm { \ a s \ } r \longrightarrow 1 . ]$

(b) ∗ Fix $0 < \alpha < \infty$ . Show that the analytic function f defined by

$$
f (z) = \sum_ {n = 0} ^ {\infty} 2 ^ {- n \alpha} z ^ {2 ^ {n}} \quad \text { for } | z | <   1
$$

extends continuously to the unit circle, but cannot be analytically continued past the unit circle. [Hint: There is a nowhere diferentiable function lurking in the background. See Chapter 4 in Book I.]

2.∗ Let

$$
F (z) = \sum_ {n = 1} ^ {\infty} d (n) z ^ {n} \quad \mathrm{for} | z | <   1
$$

where $d ( n )$ denotes the number of divisors of $n .$ Observe that the radius of convergence of this series is 1. Verify the identity

$$
\sum_ {n = 1} ^ {\infty} d (n) z ^ {n} = \sum_ {n = 1} ^ {\infty} \frac {z ^ {n}}{1 - z ^ {n}}.
$$

Using this identity, show that if $z = r$ with $0 < r < 1$ , then

$$
| F (r) | \geq c \frac {1}{1 - r} \log (1 / (1 - r))
$$

as $r \to 1$ . Similarly, if $\theta = 2 \pi p / q$ where $p$ and $q$ are positive integers and $z = r e ^ { i \theta }$ then

$$

| F (r e ^ {i \theta}) | \geq c _ {p / q} \frac {1}{1 - r} \log (1 / (1 - r))
:::
