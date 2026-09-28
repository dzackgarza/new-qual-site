---
schema: qual/card@1
id: P-BKF03-4B
kind: problem
title: Entire functions whose image misses a line are constant
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 4B of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified affine normalization of the omitted line, the half-plane image argument, and Liouville applied to the exponential.
---

::: {.problem}
Let L be a line in C, and let f be an entire function such that $f ( \mathbb { C } ) \cap L = \emptyset$ . Prove that $f$ is constant.
(Do not use the theorem of Picard that the image of a nonconstant entire function omits at most one complex number.)
:::


::: {.solution}
<1>1. By an affine change of the range, reduce to the case in which the omitted line is the imaginary axis.
::: {.proof}
Write the line as
\[
L=z_0+e^{i\theta}\mathbb R.
\]
Define
\[
g(z):=i e^{-i\theta}\bigl(f(z)-z_0\bigr).
\]
Then $g$ is entire, and multiplication by $ie^{-i\theta}$ sends the direction $e^{i\theta}\mathbb R$ to $i\mathbb R$.
Hence
\[
g(\mathbb C)\cap i\mathbb R=\varnothing.
\]
Moreover, $g$ is constant if and only if $f$ is constant.
Thus it suffices to prove the claim for $g$.
:::

<1>2. The connected set $g(\mathbb C)$ lies entirely in one of the two open half-planes
\[
\{w:\operatorname{Re}w>0\},
\qquad
\{w:\operatorname{Re}w<0\}.
\]
::: {.proof}
The complement $\mathbb C\setminus i\mathbb R$ has exactly those two connected components.
Since $\mathbb C$ is connected and $g$ is continuous, its image $g(\mathbb C)$ is connected.
Because it avoids $i\mathbb R$, it must be contained in a single component.
:::

<1>3. After replacing $g$ by $-g$ if necessary, assume
\[
\operatorname{Re}g(z)<0
\qquad(z\in\mathbb C).
\]
Then $e^{g}$ is a bounded entire function.
::: {.proof}
If the image lies in the right half-plane, replace $g$ by $-g$; this does not affect whether $g$ is constant.
Under the displayed assumption,
\[
|e^{g(z)}|=e^{\operatorname{Re}g(z)}<1
\]
for every $z$.
Thus $e^g$ is entire and bounded.
:::

<1>4. Therefore $g$, and hence $f$, is constant.
::: {.proof}
By Liouville's theorem, the bounded entire function $e^g$ is constant.
Differentiating gives
\[
0=(e^g)'=g'e^g.
\]
Since $e^g$ never vanishes, $g'=0$ identically.
Hence $g$ is constant, and by <1>1 so is $f$.
:::
:::

