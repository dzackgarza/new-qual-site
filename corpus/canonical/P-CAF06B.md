---
schema: qual/card@1
id: P-CAF06B
kind: problem
title: "Bounded harmonic functions on C are constant and the Poisson integral formula"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
solved: false
---

::: problem
Assume the representation formula
$$u(z) = \operatorname{Re}\left[\frac{1}{2\pi i}\int_{|\eta|=R} \frac{\eta - z}{\eta + z} u(\eta)\frac{d\eta}{\eta}\right]$$
for any harmonic function $u$ defined on $|z| < R$ and continuous up to $|z| \leq R$.

(a) If $u(z)$ is a harmonic function defined on $\mathbb{C}$ such that $\lim_{z \to \infty} \frac{|u(z)|}{|z|} = 0$, show that $u$ must be a constant.

(b) Show that
$$u(a) = \frac{1}{2\pi}\int_0^{2\pi} \frac{R^2 - |a|^2}{|Re^{i\theta} - a|^2} u(Re^{i\theta})\,d\theta.$$

Hint: The solution of (b) does not require (a).
:::
