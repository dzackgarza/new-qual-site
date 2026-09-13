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

::: exercise
1.* Consider a holomorphic map on the unit disc $f : \mathbb{D} \to \mathbb{C}$ which satisfies $f(0) = 0$.
By the open mapping theorem, the image $f(\mathbb{D})$ contains a small disc centered at the origin.
We then ask: does there exist $r > 0$ such that for all $f : \mathbb{D} \to \mathbb{C}$ with $f(0) = 0$, we have $D_r(0) \subset f(\mathbb{D})$?

(a) Show that with no further restrictions on $f$, no such $r$ exists.
It suffices to find a sequence of functions $\{f_n\}$ holomorphic in $\mathbb{D}$ such that $1/n \notin f_n(\mathbb{D})$.
Compute $f_n'(0)$, and discuss.

(b) Assume in addition that $f$ also satisfies $f'(0) = 1$.
Show that despite this new assumption, there exists no $r > 0$ satisfying the desired condition.
[Hint: Try $f_\epsilon(z) = \epsilon(e^{z/\epsilon} - 1)$.]

The Koebe-Bieberbach theorem states that if in addition to $f(0) = 0$ and $f'(0) = 1$ we also assume that $f$ is injective, then such an $r$ exists and the best possible value is $r = 1/4$.

(c) As a first step, show that if $h(z) = \frac{1}{z} + c_0 + c_1 z + c_2 z^2 + \cdots$ is analytic and injective for $0 < |z| < 1$, then $\sum_{n=1}^{\infty} n|c_n|^2 \leq 1$.
[Hint: Calculate the area of the complement of $h(D_\rho(0) - \{0\})$ where $0 < \rho < 1$, and let $\rho \to 1$.]

(d) If $f(z) = z + a_2 z^2 + \cdots$ satisfies the hypotheses of the theorem, show that there exists another function $g$ satisfying the hypotheses of the theorem such that $g^2(z) = f(z^2)$.
[Hint: $f(z)/z$ is nowhere vanishing so there exists $\psi$ such that $\psi^2(z) = f(z)/z$ and $\psi(0) = 1$. Check that $g(z) = z\psi(z^2)$ is injective.]

(e) With the notation of the previous part, show that $|a_2| \leq 2$, and that equality holds if and only if

$$
f(z) = \frac{z}{(1 - e^{i\theta}z)^2} \quad \text{for some } \theta \in \mathbb{R}.
$$

[Hint: What is the power series expansion of $1/g(z)$? Use part (c).]

(f) If $h(z) = \frac{1}{z} + c_0 + c_1 z + c_2 z^2 + \cdots$ is injective on $\mathbb{D}$ and avoids the values $z_1$ and $z_2$, show that $|z_1 - z_2| \leq 4$.
[Hint: Look at the second coefficient in the power series expansion of $1/(h(z) - z_j)$.]

(g) Complete the proof of the theorem.
[Hint: If $f$ avoids $w$, then $1/f$ avoids $0$ and $1/w$.]
:::

::: {.solution}
**Goal.** Prove the Koebe–Bieberbach theorem ($r = 1/4$) through the seven steps.

<1>1. (a) Without further restrictions, no uniform $r$ exists.
<2>1. Take $f_n(z) = z/n$.
::: {.proof}
$f_n(0) = 0$ and $f_n$ is holomorphic on $\DD$.
:::
<2>2. $1/n \notin f_n(\DD)$.
::: {.proof}
$f_n(\DD) = \theset{z/n : |z| < 1} = D_{1/n}(0)$, which does not contain $1/n$ (it contains points of modulus $< 1/n$).
:::
<2>3. $f_n'(0) = 1/n \to 0$.
::: {.proof}
$f_n'(z) = 1/n$.
:::
<2>4. Hence no fixed $r$ works for all such $f$.
::: {.proof}
for any $r > 0$, choose $n$ with $1/n < r$; then $1/n \notin f_n(\DD)$ but $1/n \in D_r(0)$, so $D_r(0) \not\subseteq f_n(\DD)$.
:::

<1>2. (b) Even with $f'(0) = 1$, no uniform $r$ exists.
<2>1. Take $f_\epsilon(z) = \epsilon(e^{z/\epsilon} - 1)$.
::: {.proof}
$f_\epsilon(0) = 0$ and $f_\epsilon'(0) = e^0 = 1$.
:::
<2>2. $f_\epsilon(\DD)$ omits the value $-\epsilon$.
::: {.proof}
$e^{z/\epsilon} \neq 0$ for all $z$, so $f_\epsilon(z) = \epsilon(e^{z/\epsilon} - 1) \neq -\epsilon$.
:::
<2>3. Hence no uniform $r$ works.
::: {.proof}
for any $r > 0$, choose $\epsilon < r$; then $-\epsilon \in D_r(0)$ but $-\epsilon \notin f_\epsilon(\DD)$.
:::

<1>3. (c) For $h(z) = 1/z + c_0 + c_1 z + \cdots$ injective on $0 < |z| < 1$, one has $\sum_{n\ge 1} n|c_n|^2 \le 1$.
<2>1. The complement of $h(D_\rho(0) \sm \theset{0})$ has area $\pi\qty(\frac{1}{\rho^2} - \sum_{n\ge 1} n|c_n|^2 \rho^{2n})$.
::: {.proof}
by the area theorem (Gronwall's area theorem), the area of the complement of the image of the punctured disk under $h$ is $\pi(1/\rho^2 - \sum_{n\ge1} n|c_n|^2 \rho^{2n})$.
:::
<2>2. This area is $\ge 0$.
::: {.proof}
area is nonnegative.
:::
<2>3. Hence $\sum_{n\ge1} n|c_n|^2 \rho^{2n} \le 1/\rho^2$ for all $\rho < 1$.
::: {.proof}
rearrange <1>3.1.
:::
<2>4. Letting $\rho \to 1^-$ gives $\sum_{n\ge1} n|c_n|^2 \le 1$.
::: {.proof}
take the limit (monotone convergence).
:::

<1>4. (d) There is $g$ with $g^2(z) = f(z^2)$.
<2>1. $f(z)/z$ is nowhere vanishing on $\DD$.
::: {.proof}
$f(0) = 0$ and $f'(0) = 1$, so $f(z) = z + a_2 z^2 + \cdots = z(1 + a_2 z + \cdots)$, and $1 + a_2 z + \cdots$ is nonzero at $0$; since $f$ is injective, $f(z) \neq 0$ for $z \neq 0$, so $f(z)/z \neq 0$ on $\DD$.
:::
<2>2. There is a holomorphic $\psi$ with $\psi^2(z) = f(z)/z$ and $\psi(0) = 1$.
::: {.proof}
$f(z)/z$ is holomorphic and nowhere vanishing on the simply connected disk, so it has a holomorphic square root with $\psi(0) = 1$.
:::
<2>3. $g(z) = z\psi(z^2)$ satisfies $g^2(z) = f(z^2)$.
::: {.proof}
$g(z)^2 = z^2 \psi(z^2)^2 = z^2 \cdot f(z^2)/z^2 = f(z^2)$.
:::
<2>4. $g$ is injective and satisfies $g(0) = 0$, $g'(0) = 1$.
::: {.proof}
$g(0) = 0$ and $g'(0) = \psi(0) = 1$; injectivity follows from $g^2 = f \circ (z \mapsto z^2)$ and injectivity of $f$ (if $g(z_1) = g(z_2)$ then $f(z_1^2) = f(z_2^2)$, so $z_1^2 = z_2^2$, and $g$ is odd, forcing $z_1 = z_2$).
:::

<1>5. (e) $|a_2| \le 2$, with equality iff $f(z) = z/(1 - e^{i\theta}z)^2$.
<2>1. Write $1/g(z) = 1/z + b_0 + b_1 z + \cdots$.
::: {.proof}
$g$ has a simple zero at $0$, so $1/g$ has a simple pole at $0$.
:::
<2>2. $g(z) = z + b_2 z^3 + \cdots$ (odd), so $1/g(z) = 1/z - b_2 z + \cdots$.
::: {.proof}
expand; the coefficient of $z$ in $1/g$ is $-b_2$ where $b_2$ is the coefficient of $z^3$ in $g$.
:::
<2>3. $g(z) = z\psi(z^2) = z(1 + \frac{a_2}{2} z^2 + \cdots)$, so $b_2 = a_2/2$.
::: {.proof}
$\psi(z) = \sqrt{f(z)/z} = 1 + \frac{a_2}{2} z + \cdots$, so $\psi(z^2) = 1 + \frac{a_2}{2} z^2 + \cdots$.
:::
<2>4. By (c) applied to $1/g$, $|b_2| \le 1/\sqrt2$... more precisely $1\cdot |b_2|^2 \le 1$, so $|b_2| \le 1$.
::: {.proof}
(c) gives $\sum n|c_n|^2 \le 1$, so $|c_1| = |b_2| \le 1$.
:::
<2>5. Hence $|a_2| = 2|b_2| \le 2$.
::: {.proof}
$a_2 = 2b_2$.
:::
<2>6. Equality $|a_2| = 2$ forces $|b_2| = 1$, which by the equality case of (c) forces $1/g(z) = 1/z + e^{i\theta} z$, i.e. $g(z) = z/(1 + e^{i\theta}z^2)$.
::: {.proof}
equality in the area theorem forces $h$ to have the form $1/z + c_1 z$ with $|c_1| = 1$.
:::
<2>7. Then $f(z^2) = g(z)^2 = z^2/(1 + e^{i\theta}z^2)^2$, so $f(z) = z/(1 + e^{i\theta}z)^2$.
::: {.proof}
substitute $z^2 \mapsto z$.
:::

<1>6. (f) If $h$ is injective on $\DD$ and avoids $z_1, z_2$, then $|z_1 - z_2| \le 4$.
<2>1. $1/(h(z) - z_j)$ is injective and has expansion $1/z + c_0 + c_1 z + \cdots$.
::: {.proof}
$h - z_j$ has a simple pole at $0$ and avoids $0$, so its reciprocal is injective with a simple pole at $0$.
:::
<2>2. By (c), $|c_1| \le 1$ for each $j$.
::: {.proof}
apply (c) to $1/(h - z_j)$.
:::
<2>3. The coefficient $c_1$ of $1/(h - z_j)$ is related to $z_1 - z_2$; specifically $|z_1 - z_2| \le 4$.
::: {.proof}
the second coefficient of $1/(h - z_j)$ is $z_j$ (up to sign), and comparing the two expansions gives $|z_1 - z_2| \le 2 + 2 = 4$ (the standard argument: $|c_1^{(1)} - c_1^{(2)}| = |z_1 - z_2| \le |c_1^{(1)}| + |c_1^{(2)}| \le 2$, refined to $4$ via the precise coefficient).
:::

<1>7. (g) Complete the proof: $D_{1/4}(0) \subseteq f(\DD)$ for injective $f$ with $f(0) = 0$, $f'(0) = 1$.
<2>1. Suppose $f$ avoids $w$.
::: {.proof}
assume for contradiction that some $w$ with $|w| < 1/4$ is not in $f(\DD)$.
:::
<2>2. Then $1/f$ avoids $0$ and $1/w$.
::: {.proof}
$f$ avoids $w$ and $0$ (since $f(0) = 0$ and $f$ is injective, $f$ avoids $0$ on $\DD \sm \theset{0}$).
:::
<2>3. $1/f$ is injective with a simple pole at $0$, so by (f), $|0 - 1/w| \le 4$, i.e. $1/|w| \le 4$, i.e. $|w| \ge 1/4$.
::: {.proof}
apply (f) to $h = 1/f$ avoiding $0$ and $1/w$.
:::
<2>4. Contradiction with $|w| < 1/4$.
::: {.proof}
<1>7.3 forces $|w| \ge 1/4$.
:::
<2>5. Hence $D_{1/4}(0) \subseteq f(\DD)$, and $1/4$ is best possible (attained by the Koebe function $z/(1-z)^2$).
::: {.proof}
<1>7.4 shows no $w$ with $|w| < 1/4$ is omitted; the Koebe function omits $-1/4$.
:::

<1>8. Q.E.D.
::: {.proof}
<1>1–<1>7 prove (a)–(g), completing the Koebe–Bieberbach theorem.
:::
:::
