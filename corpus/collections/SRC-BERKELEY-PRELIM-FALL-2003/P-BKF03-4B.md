---
schema: qual/card@1
id: P-BKF03-4B
kind: problem
title: Berkeley Fall 2003 prelim problem 4B
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
\n\n::: {.solution}\n<1>1. By an affine change of the range, reduce to the case in which the omitted line is the imaginary axis.\n::: {.proof}\nWrite the line as\n\[\nL=z_0+e^{i\theta}\mathbb R.\n\]\nDefine\n\[\ng(z):=i e^{-i\theta}\bigl(f(z)-z_0\bigr).\n\]\nThen $g$ is entire, and multiplication by $ie^{-i\theta}$ sends the direction $e^{i\theta}\mathbb R$ to $i\mathbb R$. Hence\n\[\ng(\mathbb C)\cap i\mathbb R=\varnothing.\n\]\nMoreover, $g$ is constant if and only if $f$ is constant. Thus it suffices to prove the claim for $g$.\n:::\n\n<1>2. The connected set $g(\mathbb C)$ lies entirely in one of the two open half-planes\n\[\n\{w:\operatorname{Re}w>0\},\n\qquad\n\{w:\operatorname{Re}w<0\}.\n\]\n::: {.proof}\nThe complement $\mathbb C\setminus i\mathbb R$ has exactly those two connected components. Since $\mathbb C$ is connected and $g$ is continuous, its image $g(\mathbb C)$ is connected. Because it avoids $i\mathbb R$, it must be contained in a single component.\n:::\n\n<1>3. After replacing $g$ by $-g$ if necessary, assume\n\[\n\operatorname{Re}g(z)<0\n\qquad(z\in\mathbb C).\n\]\nThen $e^{g}$ is a bounded entire function.\n::: {.proof}\nIf the image lies in the right half-plane, replace $g$ by $-g$; this does not affect whether $g$ is constant. Under the displayed assumption,\n\[\n|e^{g(z)}|=e^{\operatorname{Re}g(z)}<1\n\]\nfor every $z$. Thus $e^g$ is entire and bounded.\n:::\n\n<1>4. Therefore $g$, and hence $f$, is constant.\n::: {.proof}\nBy Liouville's theorem, the bounded entire function $e^g$ is constant. Differentiating gives\n\[\n0=(e^g)'=g'e^g.\n\]\nSince $e^g$ never vanishes, $g'=0$ identically. Hence $g$ is constant, and by <1>1 so is $f$.\n:::\n:::\n