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
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: exercise
1. Here are some examples of analytic functions on the unit disc that cannot be extended analytically past the unit circle.
   The following definition is needed.
   Let $f$ be a function defined in the unit disc D, with boundary circle C. A point w on C is said to be regular for $f$ if there is an open neighborhood U of w and an analytic function $g$ on $U _ { i }$ , so that $f = g$ on $\mathbb { D } \cap U$ . A function f defined on D cannot be continued analytically past the unit circle if no point of C is regular for $f .$

(a) Let

$$
f (z) = \sum_ {n = 0} ^ {\infty} z ^ {2 ^ {n}} \quad \text { for } | z | <   1.
$$

Notice that the radius of convergence of the above series is 1. Show that f cannot be continued analytically past the unit disc.
[Hint: Suppose $\theta = { 2 \pi p } / { 2 ^ { k } }$ , where $p$ and k are positive integers. Let $z = r e ^ { i \theta }$ ; then $| f ( r e ^ { i \theta } ) | \longrightarrow \infty \mathrm { \ a s \ } r \longrightarrow 1 . ]$

(b) ∗ Fix $0 < \alpha < \infty$ . Show that the analytic function f defined by

$$
f (z) = \sum_ {n = 0} ^ {\infty} 2 ^ {- n \alpha} z ^ {2 ^ {n}} \quad \text { for } | z | <   1
$$

extends continuously to the unit circle, but cannot be analytically continued past the unit circle.
[Hint: There is a nowhere diferentiable function lurking in the background. See Chapter 4 in Book I.]

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
$$
:::

::: {.solution}
**Part 1(a).**

<1>1. Let $\theta = 2\pi p / 2^k$ and $z = re^{i\theta}$.
::: {.proof}
take a dyadic rational angle.
:::

<1>2. For $n \ge k$, $z^{2^n} = r^{2^n} e^{i 2^n \theta} = r^{2^n} e^{i 2\pi p 2^{n-k}} = r^{2^n}$.
::: {.proof}
$2^n \theta = 2\pi p 2^{n-k}$ is an integer multiple of $2\pi$.
:::

<1>3. Hence $f(re^{i\theta}) = \sum_{n=0}^{k-1} z^{2^n} + \sum_{n=k}^{\infty} r^{2^n}$, and the second sum diverges to $\infty$ as $r \to 1^-$.
::: {.proof}
the tail $\sum_{n=k}^{\infty} r^{2^n}$ is a sum of nonnegative terms tending to $1$, so it diverges.
:::

<1>4. Therefore $|f(re^{i\theta})| \to \infty$ as $r \to 1^-$.
::: {.proof}
<1>3.
:::

<1>5. Hence no point $e^{i\theta}$ with $\theta$ a dyadic rational multiple of $2\pi$ is regular for $f$.
::: {.proof}
a function regular at a boundary point is bounded in a neighborhood of it, but <1>4 shows $f$ is unbounded near every such point.
:::

<1>6. The dyadic rational points are dense in the unit circle, so no point of $C$ is regular.
::: {.proof}
the set of regular points is open, and it contains no dyadic rational point (<1>5), so it is empty.
:::

<1>7. Hence $f$ cannot be continued analytically past the unit circle.
::: {.proof}
<1>6.
:::

**Part 1(b).**

<1>1. $f(z) = \sum_{n=0}^{\infty} 2^{-n\alpha} z^{2^n}$ converges uniformly on $\bar\DD$ (since $\sum 2^{-n\alpha} < \infty$), so $f$ extends continuously to the unit circle.
::: {.proof}
the Weierstrass $M$-test with $M_n = 2^{-n\alpha}$.
:::

<1>2. $f$ cannot be continued analytically past the unit circle.
::: {.proof}
the same argument as part (a): at a dyadic angle $\theta = 2\pi p/2^k$, the tail $\sum_{n=k}^{\infty} 2^{-n\alpha} r^{2^n}$ has derivative (with respect to $r$) tending to $\infty$ as $r \to 1^-$, so $f$ is not differentiable at $e^{i\theta}$; since the dyadic points are dense and the boundary values form a nowhere-differentiable (Weierstrass-type) function, no point of $C$ is regular.
:::

**Part 2.**

<1>1. $\sum_{n=1}^{\infty} d(n) z^n = \sum_{n=1}^{\infty} \frac{z^n}{1 - z^n}$.
<2>1. $\frac{z^n}{1 - z^n} = \sum_{k=1}^{\infty} z^{kn}$.
::: {.proof}
geometric series.
:::
<2>2. Hence $\sum_{n=1}^{\infty} \frac{z^n}{1-z^n} = \sum_{n=1}^{\infty} \sum_{k=1}^{\infty} z^{kn} = \sum_{m=1}^{\infty} d(m) z^m$.
::: {.proof}
the coefficient of $z^m$ counts the pairs $(n,k)$ with $kn = m$, i.e. the number $d(m)$ of divisors of $m$.
:::

<1>3. For $z = r$ with $0 < r < 1$, $|F(r)| \ge c \frac{1}{1-r}\log\frac{1}{1-r}$ as $r \to 1$.
::: {.proof}
$F(r) = \sum_{n} \frac{r^n}{1-r^n} \ge \sum_{n \le N} \frac{r^n}{1-r^n}$; taking $N \approx \frac{1}{1-r}$ and using $1 - r^n \le n(1-r)$ gives the lower bound $c \frac{1}{1-r}\log\frac{1}{1-r}$.
:::

<1>4. The same lower bound holds for $z = re^{i\theta}$ with $\theta = 2\pi p/q$.
::: {.proof}
for $n$ a multiple of $q$, $z^n = r^n$, so the same estimate applies to the subsequence of multiples of $q$, giving $|F(re^{i\theta})| \ge c_{p/q}\frac{1}{1-r}\log\frac{1}{1-r}$.
:::

<1>5. Q.E.D.
::: {.proof}
<1>7 (1a), <1>2 (1b), and <1>1, <1>3, <1>4 (2).
:::
:::
