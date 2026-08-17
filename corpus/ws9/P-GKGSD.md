---
schema: qual/card@1
id: P-GKGSD
kind: problem
title: Let $f$ be a one-to-one analytic function defined on the unit disk $D$…
classification:
  areas:
  - real-analysis
  topics:
  - holomorphic-functions
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $f$ be a one-to-one analytic function defined on the unit disk $D$ centered at the origin and $f(0)=0$.
Show that the function $g(z) = \sqrt{f(z^2)}$ has a single-valued branch and is also one-to-one.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Let $f$ be one-to-one analytic on the unit disk $D$ with $f(0) = 0$.
Show that $g(z) = \sqrt{f(z^2)}$ has a single-valued analytic branch on $D$ and is one-to-one.

<1>1. $f(z) = z h(z)$ on $D$, where $h$ is analytic, $h(0) = f'(0) \ne 0$, and $h$ is zero-free on $D$.
<2>1. $f(z) = zh(z)$ with $h$ analytic and $h(0) = f'(0)$.
Proof: $h(z) = f(z)/z$ has a removable singularity at $0$ with value $f'(0)$.
<2>2. $f'(0) \ne 0$.
Proof: a one-to-one analytic function has nonvanishing derivative (if $f'(z_0) = 0$, $f$ is not injective on any neighborhood of $z_0$ by the local mapping theorem).
<2>3. $h$ has no zeros in $D$.
Proof: $h(z) = 0$ with $z \ne 0$ would give $f(z) = 0 = f(0)$, contradicting injectivity.

<1>2. $f(z^2) = z^2 h(z^2)$, and $h(z^2)$ is zero-free on $D$.
Proof: <1>1 with $z$ replaced by $z^2$; zeros of $h(z^2)$ are zeros of $h$.

<1>3. $h(z^2)$ has a holomorphic square root on $D$: $h(z^2) = w(z)^2$ with $w$ analytic and zero-free.
Proof: $D$ is simply connected and $h(z^2)$ is zero-free on $D$ (<1>2), so a holomorphic branch of the square root exists.

<1>4. $g(z) = zw(z)$ is a holomorphic single-valued branch of $\sqrt{f(z^2)}$.
Proof: $g(z)^2 = z^2 w(z)^2 = z^2 h(z^2) = f(z^2)$ (<1>2, <1>3).

<1>5. $g$ is one-to-one.
<2>1. If $g(z_1) = g(z_2)$ then $z_1^2 = z_2^2$.
Proof: squaring gives $f(z_1^2) = f(z_2^2)$; $f$ is injective (<1>1). <2>2. $z_1 = z_2$.
Proof: by <2>1, $z_2 = \pm z_1$.
If $z_2 = -z_1 \ne 0$, then $g(z_1) = g(-z_1)$ gives $z_1 w(z_1^2) = -z_1 w(z_1^2)$, so $2z_1 w(z_1^2) = 0$; since $z_1 \ne 0$ and $w$ is zero-free (<1>3), contradiction.
Hence $z_2 = z_1$.

<1>6. Q.E.D. Proof: <1>4 gives a single-valued branch; <1>5 shows it is one-to-one.
:::
