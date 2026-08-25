---
schema: qual/card@1
id: E-SS3.PR-1
kind: exercise
title: Koebe-Bieberbach radius theorem for normalized univalent functions
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
---

::: exercise
1.* Consider a holomorphic map on the unit disc $f : \mathbb{D} \to \mathbb{C}$ which satisfies $f(0) = 0$. By the open mapping theorem, the image $f(\mathbb{D})$ contains a small disc centered at the origin. We then ask: does there exist $r > 0$ such that for all $f : \mathbb{D} \to \mathbb{C}$ with $f(0) = 0$, we have $D_r(0) \subset f(\mathbb{D})$?

(a) Show that with no further restrictions on $f$, no such $r$ exists. It suffices to find a sequence of functions $\{f_n\}$ holomorphic in $\mathbb{D}$ such that $1/n \notin f_n(\mathbb{D})$. Compute $f_n'(0)$, and discuss.

(b) Assume in addition that $f$ also satisfies $f'(0) = 1$. Show that despite this new assumption, there exists no $r > 0$ satisfying the desired condition.
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

(g) Complete the proof of the theorem. [Hint: If $f$ avoids $w$, then $1/f$ avoids $0$ and $1/w$.]
:::
