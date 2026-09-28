---
schema: qual/card@1
id: E-SS2.PR-1
kind: problem
title: Natural boundaries of the lacunary series $\sum z^{2^n}$ and $\sum 2^{-n\alpha}z^{2^n}$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
1. Here are some examples of analytic functions on the unit disc that cannot be extended analytically past the unit circle.
   The following definition is needed.
   Let $f$ be a function defined in the unit disc D, with boundary circle C. A point w on C is said to be regular for $f$ if there is an open neighborhood U of w and an analytic function $g$ on $U _ { i }$ , so that $f = g$ on $\mathbb { D } \cap U$ . A function f defined on D cannot be continued analytically past the unit circle if no point of C is regular for $f .$

(a) Let

$$
f (z) = \sum_ {n = 0} ^ {\infty} z ^ {2 ^ {n}} \quad \text { for } | z | <   1.
$$

Notice that the radius of convergence of the above series is 1. Show that f cannot be continued analytically past the unit disc.
[Hint: Suppose $\theta = { 2 \pi p } / { 2 ^ { k } }$ , where $p$ and k are positive integers. Let $z = r e ^ { i \theta }$ ; then $| f ( r e ^ { i \theta } ) | \longrightarrow \infty \mathrm { \ a s \ } r \longrightarrow 1 . ]$

(b) $^\ast$ Fix $0 < \alpha < \infty$ . Show that the analytic function f defined by

$$
f (z) = \sum_ {n = 0} ^ {\infty} 2 ^ {- n \alpha} z ^ {2 ^ {n}} \quad \text { for } | z | <   1
$$

extends continuously to the unit circle, but cannot be analytically continued past the unit circle.
[Hint: There is a nowhere diferentiable function lurking in the background. See Chapter 4 in Book I.]
:::

::: {.solution}
Throughout, a dyadic point is $e^{i\theta}$ with $\theta = 2\pi p / 2^k$, $p,k$ positive integers; dyadic points are dense in $C$. The set of regular points of a function on $\mathbb D$ is open in $C$, so if it contains no dyadic point, it is empty.

<1>1. (1a) $f(z)=\sum_{n\ge0} z^{2^n}$ cannot be continued analytically past $C$.

::: {.proof}
Let $\theta = 2\pi p / 2^k$. For $n \ge k$, $2^n\theta$ is a multiple of $2\pi$, so $(re^{i\theta})^{2^n} = r^{2^n}$ and
$$f(re^{i\theta}) = \sum_{n=0}^{k-1} (re^{i\theta})^{2^n} + \sum_{n=k}^{\infty} r^{2^n}.$$
Each term of the second sum tends to $1$ as $r\to1^-$, and the terms are nonnegative, so the second sum tends to $\infty$; hence $\abs{f(re^{i\theta})}\to\infty$. A function regular at a boundary point is bounded near it, so no dyadic point is regular, and no point of $C$ is regular.
:::

<1>2. (1b) $f(z)=\sum_{n\ge0} 2^{-n\alpha} z^{2^n}$ extends continuously to $\overline{\mathbb D}$ and cannot be continued analytically past $C$.

::: {.proof}
Since $\sum 2^{-n\alpha} < \infty$, the Weierstrass $M$-test shows that the series converges uniformly on $\overline{\mathbb D}$, so $f$ extends continuously. Suppose a dyadic point $e^{i\theta}$, $\theta = 2\pi p/2^k$, were regular. Then $f$ agrees near $e^{i\theta}$ with a function analytic on a neighborhood of $e^{i\theta}$, so for every $m$ the derivative $\frac{d^m}{dr^m}f(re^{i\theta})=e^{im\theta}f^{(m)}(re^{i\theta})$ stays bounded as $r\to1^-$. But $f(re^{i\theta})=P(r)+\sum_{n\ge k}2^{-n\alpha}r^{2^n}$ with $P$ a polynomial, and for an integer $m\ge\alpha$,
$$\frac{d^m}{dr^m}\sum_{n\ge k}2^{-n\alpha}r^{2^n}\ge\sum_{n\ge n_0}2^{-n\alpha}\bigl(2^{n-1}\bigr)^m r^{2^n-m},$$
where $n_0\ge k$ is chosen with $2^{n_0}\ge2m$, so that $2^n(2^n-1)\cdots(2^n-m+1)\ge(2^{n-1})^m$. As $r\to1^-$ the right side tends to $2^{-m}\sum_{n\ge n_0}2^{n(m-\alpha)}=\infty$. Hence no dyadic point is regular, and no point of $C$ is regular.
:::
:::
