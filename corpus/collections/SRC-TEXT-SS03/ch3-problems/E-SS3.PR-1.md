---
schema: qual/card@1
id: E-SS3.PR-1
kind: problem
title: Koebe-Bieberbach radius theorem for normalized univalent functions
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
Consider a holomorphic map on the unit disc $f : \DD \to \CC$ which satisfies $f(0) = 0$.
By the open mapping theorem, the image $f(\DD)$ contains a small disc centered at the origin.
We then ask: does there exist $r > 0$ such that for all $f : \DD \to \CC$ with $f(0) = 0$, we have $D_r(0) \subset f(\DD)$?

(a) Show that with no further restrictions on $f$, no such $r$ exists.
It suffices to find a sequence of functions $\{f_n\}$ holomorphic in $\DD$ such that $1/n \notin f_n(\DD)$.
Compute $f_n'(0)$, and discuss.

(b) Assume in addition that $f$ also satisfies $f'(0) = 1$.
Show that despite this new assumption, there exists no $r > 0$ satisfying the desired condition.
[Hint: Try $f_\epsilon(z) = \epsilon(e^{z/\epsilon} - 1)$.]

The Koebe-Bieberbach theorem states that if in addition to $f(0) = 0$ and $f'(0) = 1$ we also assume that $f$ is injective, then such an $r$ exists and the best possible value is $r = 1/4$.

(c) As a first step, show that if $h(z) = \frac{1}{z} + c_0 + c_1 z + c_2 z^2 + \cdots$ is analytic and injective for $0 < \abs{z} < 1$, then $\sum_{n=1}^{\infty} n\abs{c_n}^2 \leq 1$.
[Hint: Calculate the area of the complement of $h(D_\rho(0) - \{0\})$ where $0 < \rho < 1$, and let $\rho \to 1$.]

(d) If $f(z) = z + a_2 z^2 + \cdots$ satisfies the hypotheses of the theorem, show that there exists another function $g$ satisfying the hypotheses of the theorem such that $g^2(z) = f(z^2)$.
[Hint: $f(z)/z$ is nowhere vanishing so there exists $\psi$ such that $\psi^2(z) = f(z)/z$ and $\psi(0) = 1$. Check that $g(z) = z\psi(z^2)$ is injective.]

(e) With the notation of the previous part, show that $\abs{a_2} \leq 2$, and that equality holds if and only if

$$
f(z) = \frac{z}{(1 - e^{i\theta}z)^2} \quad \text{for some } \theta \in \RR.
$$

[Hint: What is the power series expansion of $1/g(z)$? Use part (c).]

(f) If $h(z) = \frac{1}{z} + c_0 + c_1 z + c_2 z^2 + \cdots$ is injective on $\DD$ and avoids the values $z_1$ and $z_2$, show that $\abs{z_1 - z_2} \leq 4$.
[Hint: Look at the second coefficient in the power series expansion of $1/(h(z) - z_j)$.]

(g) Complete the proof of the theorem.
[Hint: If $f$ avoids $w$, then $1/f$ avoids $0$ and $1/w$.]
:::

::: {.solution}
**Goal.** Prove the Koebe–Bieberbach theorem ($r = 1/4$) through the seven steps.

::: pf

::: {.pf-step #s1}
(a) Without further restrictions, no uniform $r$ exists.

::: pf-proof

::: pf-step
Take $f_n(z) = z/n$.

::: pf-proof
$f_n(0) = 0$ and $f_n$ is holomorphic on $\DD$.
:::

:::

::: pf-step
$1/n \notin f_n(\DD)$.

::: pf-proof
$f_n(\DD) = \theset{z/n : \abs{z} < 1} = D_{1/n}(0)$, which does not contain $1/n$ (it contains points of modulus $< 1/n$).
:::

:::

::: pf-step
$f_n'(0) = 1/n \to 0$.

::: pf-proof
$f_n'(z) = 1/n$.
:::

:::

::: pf-step
Hence no fixed $r$ works for all such $f$.

::: pf-proof
for any $r > 0$, choose $n$ with $1/n < r$; then $1/n \notin f_n(\DD)$ but $1/n \in D_r(0)$, so $D_r(0) \not\subseteq f_n(\DD)$.
:::

:::

:::

:::

::: {.pf-step #s2}
(b) Even with $f'(0) = 1$, no uniform $r$ exists.

::: pf-proof

::: pf-step
Take $f_\epsilon(z) = \epsilon(e^{z/\epsilon} - 1)$.

::: pf-proof
$f_\epsilon(0) = 0$ and $f_\epsilon'(0) = e^0 = 1$.
:::

:::

::: pf-step
$f_\epsilon(\DD)$ omits the value $-\epsilon$.

::: pf-proof
$e^{z/\epsilon} \neq 0$ for all $z$, so $f_\epsilon(z) = \epsilon(e^{z/\epsilon} - 1) \neq -\epsilon$.
:::

:::

::: pf-step
Hence no uniform $r$ works.

::: pf-proof
for any $r > 0$, choose $\epsilon < r$; then $-\epsilon \in D_r(0)$ but $-\epsilon \notin f_\epsilon(\DD)$.
:::

:::

:::

:::

::: {.pf-step #s3}
(c) For $h(z) = 1/z + c_0 + c_1 z + \cdots$ injective on $0 < \abs{z} < 1$, one has $\sum_{n\ge 1} n\abs{c_n}^2 \le 1$.

::: pf-proof

::: {.pf-step #s3-1}
The complement of $h(D_\rho(0) \sm \theset{0})$ has area $\pi\qty(\frac{1}{\rho^2} - \sum_{n\ge 1} n\abs{c_n}^2 \rho^{2n})$.

::: pf-proof
Since $h$ is injective and $h(z) \to \infty$ as $z \to 0$, the curve $\Gamma_\rho : \theta \mapsto h(\rho e^{i\theta})$ is a Jordan curve, $h(D_\rho(0) \sm \theset{0})$ is its unbounded complementary component, and the complement of the image is the closed bounded region $K_\rho$ that $\Gamma_\rho$ encloses. Near $z = 0$ the term $1/z$ dominates, so $\Gamma_\rho$ goes around $K_\rho$ clockwise. By Green's theorem, the area of a region bounded by a positively oriented Jordan curve $\gamma$ is $\frac{1}{2i}\int_\gamma \overline w\,dw$, so
$$
\abs{K_\rho} = -\frac{1}{2i}\int_0^{2\pi} \overline{h(\rho e^{i\theta})}\,\frac{d}{d\theta}h(\rho e^{i\theta})\,d\theta.
$$
Put $c_{-1} = 1$. Then $h(\rho e^{i\theta}) = \sum_{n\ge -1} c_n\rho^n e^{in\theta}$ and $\frac{d}{d\theta}h(\rho e^{i\theta}) = \sum_{n \ge -1} in\,c_n\rho^n e^{in\theta}$, both converging uniformly in $\theta$. By orthogonality of $e^{in\theta}$,
$$
\abs{K_\rho} = -\frac{2\pi}{2i}\sum_{n\ge-1} in\abs{c_n}^2\rho^{2n} = \pi\qty(\frac{1}{\rho^2} - \sum_{n\ge1} n\abs{c_n}^2\rho^{2n}).
$$
:::

:::

::: pf-step
This area is $\ge 0$.

::: pf-proof
area is nonnegative.
:::

:::

::: pf-step
Hence $\sum_{n\ge1} n\abs{c_n}^2 \rho^{2n} \le 1/\rho^2$ for all $\rho < 1$.

::: pf-proof
rearrange step [](#s3-1){.pf-ref}.
:::

:::

::: pf-step
Letting $\rho \to 1^-$ gives $\sum_{n\ge1} n\abs{c_n}^2 \le 1$.

::: pf-proof
take the limit (monotone convergence).
:::

:::

:::

:::

::: {.pf-step #s4}
(d) There is $g$ with $g^2(z) = f(z^2)$.

::: pf-proof

::: pf-step
$f(z)/z$ is nowhere vanishing on $\DD$.

::: pf-proof
$f(0) = 0$ and $f'(0) = 1$, so $f(z) = z + a_2 z^2 + \cdots = z(1 + a_2 z + \cdots)$, and $1 + a_2 z + \cdots$ is nonzero at $0$; since $f$ is injective, $f(z) \neq 0$ for $z \neq 0$, so $f(z)/z \neq 0$ on $\DD$.
:::

:::

::: pf-step
There is a holomorphic $\psi$ with $\psi^2(z) = f(z)/z$ and $\psi(0) = 1$.

::: pf-proof
$f(z)/z$ is holomorphic and nowhere vanishing on the simply connected disk, so it has a holomorphic square root with $\psi(0) = 1$.
:::

:::

::: pf-step
$g(z) = z\psi(z^2)$ satisfies $g^2(z) = f(z^2)$.

::: pf-proof
$g(z)^2 = z^2 \psi(z^2)^2 = z^2 \cdot f(z^2)/z^2 = f(z^2)$.
:::

:::

::: pf-step
$g$ is injective and satisfies $g(0) = 0$, $g'(0) = 1$.

::: pf-proof
$g(0) = 0$ and $g'(0) = \psi(0) = 1$. $g$ is odd. If $g(z_1) = g(z_2)$, then $f(z_1^2) = f(z_2^2)$, so $z_1^2 = z_2^2$ by injectivity of $f$. If $z_1 = -z_2$, then $g(z_2) = g(z_1) = -g(z_2)$, so $g(z_2) = 0$; since $g(z)^2 = f(z^2)$ vanishes only at $z = 0$, $z_1 = z_2 = 0$. Hence $z_1 = z_2$ in every case.
:::

:::

:::

:::

::: {.pf-step #s5}
(e) $\abs{a_2} \le 2$, with equality iff $f(z) = z/(1 - e^{i\theta}z)^2$.

::: pf-proof

::: pf-step
Write $1/g(z) = 1/z + b_0 + b_1 z + \cdots$.

::: pf-proof
$g$ has a simple zero at $0$, so $1/g$ has a simple pole at $0$.
:::

:::

::: pf-step
$g(z) = z + b_2 z^3 + \cdots$ (odd), so $1/g(z) = 1/z - b_2 z + \cdots$.

::: pf-proof
expand; the coefficient of $z$ in $1/g$ is $-b_2$ where $b_2$ is the coefficient of $z^3$ in $g$.
:::

:::

::: pf-step
$g(z) = z\psi(z^2) = z(1 + \frac{a_2}{2} z^2 + \cdots)$, so $b_2 = a_2/2$.

::: pf-proof
$\psi(z) = \sqrt{f(z)/z} = 1 + \frac{a_2}{2} z + \cdots$, so $\psi(z^2) = 1 + \frac{a_2}{2} z^2 + \cdots$.
:::

:::

::: pf-step
$\abs{b_2} \le 1$.

::: pf-proof
$1/g$ is injective on $0 < \abs z < 1$ because $g$ is, so (c) applies to $1/g$; its coefficient of $z$ is $c_1 = -b_2$, and $\abs{c_1}^2 \le \sum n\abs{c_n}^2 \le 1$.
:::

:::

::: pf-step
Hence $\abs{a_2} = 2\abs{b_2} \le 2$.

::: pf-proof
$a_2 = 2b_2$.
:::

:::

::: pf-step
If $\abs{a_2} = 2$, write $a_2 = 2e^{i\theta}$; then $g(z) = z/(1 - e^{i\theta}z^2)$.

::: pf-proof
$\abs{c_1} = \abs{b_2} = 1$, so $\sum_{n\ge1} n\abs{c_n}^2 \le 1$ forces $c_n = 0$ for $n \ge 2$. $1/g$ is odd, so its constant term vanishes. Hence $1/g(z) = 1/z - b_2 z = (1 - e^{i\theta}z^2)/z$.
:::

:::

::: pf-step
Then $f(z) = z/(1 - e^{i\theta}z)^2$.

::: pf-proof
$f(z^2) = g(z)^2 = z^2/(1 - e^{i\theta}z^2)^2$ for $z \in \DD$, and every point of $\DD$ is a square of a point of $\DD$.
:::

:::

::: pf-step
Conversely, $f(z) = z/(1 - e^{i\theta}z)^2$ satisfies the hypotheses and has $\abs{a_2} = 2$.

::: pf-proof
$f(z) = \sum_{n\ge1} n e^{i(n-1)\theta}z^n$, so $a_2 = 2e^{i\theta}$. $f(z) = e^{-i\theta}k(e^{i\theta}z)$ with $k(z) = z/(1-z)^2 = \frac14\qty(\qty(\frac{1+z}{1-z})^2 - 1)$. The map $z \mapsto \frac{1+z}{1-z}$ is injective from $\DD$ onto the right half-plane, and squaring is injective there, so $k$ and $f$ are injective.
:::

:::

:::

:::

::: {.pf-step #s6}
(f) If $h$ is injective on $\DD$ and avoids $z_1, z_2$, then $\abs{z_1 - z_2} \le 4$.

::: pf-proof

::: pf-step
$H_j = 1/(h - z_j)$, extended by $H_j(0) = 0$, is holomorphic and injective on $\DD$.

::: pf-proof
$h - z_j$ never vanishes on $\DD \sm \theset{0}$ and has a simple pole at $0$, so $H_j$ is holomorphic on $\DD$ with $H_j(0) = 0$. It is injective on $\DD \sm \theset{0}$ because $h$ is, and $0$ is its only zero.
:::

:::

::: pf-step
$H_j(z) = z + (z_j - c_0)z^2 + \cdots$.

::: pf-proof
$H_j(z) = \frac{z}{1 + (c_0 - z_j)z + c_1z^2 + \cdots} = z\qty(1 - (c_0 - z_j)z + O(z^2))$.
:::

:::

::: pf-step
$\abs{z_1 - z_2} \le 4$.

::: pf-proof
By (e) applied to $H_j$, $\abs{z_j - c_0} \le 2$ for $j = 1, 2$, so $\abs{z_1 - z_2} \le \abs{z_1 - c_0} + \abs{c_0 - z_2} \le 4$.
:::

:::

:::

:::

::: {.pf-step #s7}
(g) Complete the proof: $D_{1/4}(0) \subseteq f(\DD)$ for injective $f$ with $f(0) = 0$, $f'(0) = 1$.

::: pf-proof

::: pf-step
Suppose $f$ avoids $w$.

::: pf-proof
assume for contradiction that some $w$ with $\abs{w} < 1/4$ is not in $f(\DD)$.
:::

:::

::: pf-step
Then $1/f$ avoids $0$ and $1/w$.

::: pf-proof
$1/f$ never vanishes because $f$ takes finite values, and $1/f = 1/w$ would mean $f = w$. Also $w \neq 0$, since $f(0) = 0$. Since $f$ is injective with a simple zero only at $0$, $1/f = 1/z - a_2 + \cdots$ is injective on $\DD \sm \theset{0}$, as (f) requires.
:::

:::

::: {.pf-step #s7-3}
$1/f$ is injective with a simple pole at $0$, so by (f), $\abs{0 - 1/w} \le 4$, i.e. $1/\abs{w} \le 4$, i.e. $\abs{w} \ge 1/4$.

::: pf-proof
apply (f) to $h = 1/f$ avoiding $0$ and $1/w$.
:::

:::

::: {.pf-step #s7-4}
Contradiction with $\abs{w} < 1/4$.

::: pf-proof
step [](#s7-3){.pf-ref} forces $\abs{w} \ge 1/4$.
:::

:::

::: pf-step
Hence $D_{1/4}(0) \subseteq f(\DD)$, and $1/4$ is best possible (attained by the Koebe function $z/(1-z)^2$).

::: pf-proof
step [](#s7-4){.pf-ref} shows no $w$ with $\abs{w} < 1/4$ is omitted; the Koebe function omits $-1/4$.
:::

:::

:::

:::

::: pf-qed
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref}, and [](#s7){.pf-ref} prove (a)–(g), completing the Koebe–Bieberbach theorem.
:::

:::
:::
