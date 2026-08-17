---
schema: qual/card@1
id: P-7J6TM
kind: problem
title: "Assume $f$ is an entire function such that $|f(z)|=1$ on $|z|=1$. Prove that $f(z)=e^{i \\theta} z^{n}$\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - maximum-modulus-principle
  - blaschke-factors
  - entire-functions
  - zeros
relations: []
review: draft
solved: true
---

::: problem
Assume $f$ is an entire function such that $|f(z)|=1$ on $|z|=1$.
Prove that $f(z)=e^{i \theta} z^{n}$, where $\theta$ is a real number and $n$ a non-negative integer.

> Suggestion: First use the maximum and minimum modulus theorem to show $$f(z)=e^{i \theta} \prod_{k=1}^{n} \frac{z-z_{k}}{1-\bar{z_{k}} z}$$ if $f$ has zeros.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Prove that if $f$ is entire and $\abs{f(z)} = 1$ on $\abs z = 1$, then $f(z) = e^{i\theta} z^n$ for some $\theta \in \RR$ and $n \in \ZZ^{\geq 0}$.

<1>1. $f$ has finitely many zeros in the closed unit disk, and none on the circle $\abs z = 1$.
Proof: Zeros of the nonzero entire function $f$ are isolated; the closed disk is compact, so only finitely many; and $\abs f = 1$ on the circle rules out zeros there.
($f \not\equiv 0$ since $\abs f = 1$ somewhere.)

<1>2. Let the zeros in $\abs z < 1$ be $z_1, \ldots, z_n$ (counted with multiplicity), and define the Blaschke product $B(z) := \prod_{k=1}^n \frac{z - z_k}{1 - \bar z_k z}$.
Proof: Each factor is analytic in a neighborhood of the closed unit disk (the pole $1/\bar z_k$ lies outside, since $\abs{z_k} < 1$).

<1>3. On $\abs z = 1$, $\abs{B(z)} = 1$.
Proof: For $\abs z = 1$, $\bar z = 1/z$, so $\abs{z - z_k} = \abs{z}\abs{1 - z_k/z} = \abs{1 - z_k \bar z} = \abs{1 - \bar z_k z}$; hence each factor has modulus $1$, and so does the product $B$.

<1>4. Define $g := f / B$; then $g$ is analytic on a neighborhood of the closed unit disk, has no zeros there, and $\abs g = 1$ on $\abs z = 1$.
Proof: $B$ has the same zeros as $f$ in the disk (<1>2), so $g$ is holomorphic; <1>3 and $\abs f = 1$ on the circle give $\abs g = 1$ there.

<1>5. $g$ is constant, and $\abs g \equiv 1$.
<2>1. $\abs g \leq 1$ in $\abs z \leq 1$.
Proof: Maximum modulus principle applied to $g$, using $\abs g = 1$ on the boundary.
<2>2. $\abs g \geq 1$ in $\abs z \leq 1$.
Proof: Minimum modulus principle applied to the zero-free $g$ (<1>4), again using the boundary values $\abs g = 1$.
<2>3. $\abs g \equiv 1$, so $g \equiv e^{i\theta}$ for some real $\theta$.
Proof: <2>1 and <2>2 force $\abs g = 1$ throughout the disk; a holomorphic function of constant modulus is constant, and its value lies on the unit circle.

<1>6. Hence $f(z) = e^{i\theta} B(z)$ on $\abs z \leq 1$.
Proof: $f = gB$ and <1>5.

<1>7. $f$ is entire, so the poles of $B$ must not occur; this forces all $z_k = 0$.
<2>1. $B$ is a rational function with possible poles at $1/\bar z_k$.
Proof: By definition, <1>2. <2>2. If some $z_k \neq 0$, then $1/\bar z_k$ is a pole of $B$ in $\CC \setminus \theset{0}$, contradicting the identity theorem applied to $f = e^{i\theta}B$ on $\CC$.
Proof: <1>6 gives equality on the open disk, hence on all of $\CC$ (identity theorem); but $f$ is entire while the right-hand side would have a pole.
Therefore every $z_k = 0$.
<2>3. With all zeros at $0$: $B(z) = z^n$.
Proof: Each factor $\frac{z - 0}{1 - 0 \cdot z} = z$.

<1>8. Q.E.D. Proof: <1>6 and <1>7 give $f(z) = e^{i\theta} z^n$, with $\theta \in \RR$ and $n$ the number of zeros in the disk.
:::
