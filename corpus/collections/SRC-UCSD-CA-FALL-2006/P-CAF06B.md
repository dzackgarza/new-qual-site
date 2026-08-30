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
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Assume the representation formula $$u(z) = \operatorname{Re}\left[\frac{1}{2\pi i}\int_{|\eta|=R} \frac{\eta - z}{\eta + z} u(\eta)\frac{d\eta}{\eta}\right]$$ for any harmonic function $u$ defined on $|z| < R$ and continuous up to $|z| \leq R$.

(a) If $u(z)$ is a harmonic function defined on $\mathbb{C}$ such that $\lim_{z \to \infty} \frac{|u(z)|}{|z|} = 0$, show that $u$ must be a constant.

(b) Show that $$u(a) = \frac{1}{2\pi}\int_0^{2\pi} \frac{R^2 - |a|^2}{|Re^{i\theta} - a|^2} u(Re^{i\theta})\,d\theta.$$

Hint: The solution of (b) does not require (a).
:::

::: {.solution}
<1>1. From the representation, $u(a) = \operatorname{Re}\frac{1}{2\pi i}\int_{|\eta|=R} \frac{\eta-a}{\eta+a}u(\eta)\frac{d\eta}{\eta}$.
Proof: hypothesis.

<1>2. Bound $|u(z)|=o(|z|)$, let $R\to\infty$, then $\frac{\eta-a}{\eta+a}=1+O(R^{-1})$, so $u(a)=\operatorname{Re}\frac{1}{2\pi i}\int_{|\eta|=R} u(\eta)\frac{d\eta}{\eta}+o(1)$.
Proof: <1>1 and growth.

<1>3. The integral $\frac{1}{2\pi i}\int_{|\eta|=R} u(\eta)\frac{d\eta}{\eta}$ is bounded independent of $R$, so $u$ is constant by letting $R\to\infty$ for $u(a)-u(0)$.
Proof: <1>2 (difference tends to $0$).

<1>4. Part (b) follows by writing $\frac{\eta-a}{\eta+a}\frac{d\eta}{\eta}= \frac{R^2-|a|^2}{|Re^{i\theta}-a|^2}d\theta + i(\dots)$ and taking real part.
Proof: $\eta=Re^{i\theta}$, $d\eta=i\eta d\theta$.

<1>5. Q.E.D.
Proof: <1>3 and <1>4.
:::
