---
schema: qual/card@1
id: E-SS2.PR-1
kind: problem
title: Natural boundaries of lacunary series and growth of $\sum d(n)z^n$
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

2. $^\ast$ Let

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
$$
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

<1>3. (2) $\sum_{n\ge1} d(n) z^n = \sum_{n\ge1} \frac{z^n}{1 - z^n}$ for $\abs z<1$.

::: {.proof}
By the geometric series, $\frac{z^n}{1 - z^n} = \sum_{k\ge1} z^{kn}$. The double series converges absolutely, and the coefficient of $z^m$ in $\sum_n\sum_k z^{kn}$ is the number of pairs $(n,k)$ with $kn = m$, which is $d(m)$.
:::

<1>4. (2) $F(r) \ge c \frac{1}{1-r}\log\frac{1}{1-r}$ as $r \to 1^-$.

::: {.proof}
All terms of $F(r) = \sum_{n} \frac{r^n}{1-r^n}$ are positive. Using $1 - r^n \le n(1-r)$ and keeping the terms with $n \le N$, where $N$ is the integer part of $\frac{1}{1-r}$, gives $F(r)\ge\frac{r^N}{1-r}\sum_{n\le N}\frac1n$. Since $r^N$ is bounded below by a positive constant as $r\to1^-$ and $\sum_{n\le N}\frac1n\ge\log N$, this is at least $c \frac{1}{1-r}\log\frac{1}{1-r}$.
:::

<1>5. (2) For $\theta = 2\pi p/q$, $\abs{F(re^{i\theta})} \ge c_{p/q}\frac{1}{1-r}\log\frac{1}{1-r}$ as $r\to1^-$.

::: {.proof}
Assume $p/q$ is in lowest terms and put $z=re^{i\theta}$. For $q\mid n$, $z^n = r^n$, and the terms with $n=qj$ contribute $\sum_j\frac{r^{qj}}{1-r^{qj}}=F(r^q)$, which by step <1>4 is at least $c\frac{1}{1-r^q}\log\frac{1}{1-r^q}\ge \frac cq\frac{1}{1-r}\log\frac{1}{q(1-r)}$ since $1-r^q\le q(1-r)$. For $q\nmid n$, $e^{in\theta}$ is a $q$th root of unity different from $1$, so $\abs{1-z^n}\ge\delta_q>0$ for $r$ near $1$, and these terms contribute at most $\sum_n r^n/\delta_q=O\bigl(\frac1{1-r}\bigr)$. The logarithmic factor dominates, which gives the bound with a smaller constant $c_{p/q}$.
:::
:::
