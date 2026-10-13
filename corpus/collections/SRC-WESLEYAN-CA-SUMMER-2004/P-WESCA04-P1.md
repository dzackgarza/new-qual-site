---
schema: qual/card@1
id: P-WESCA04-P1
kind: problem
title: "An entire function with real part bounded above is constant"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1.3, problem 1 (August 2, 2004) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Let $f$ be entire and suppose
\[
\operatorname{Re} f(z)\le 10
\qquad(z\in\mathbb C).
\]
Show that $f$ is constant.
:::

::: {.solution}
<1>1. Define
\[
g(z)
\coloneqq
e^{f(z)}.
\]
Then $g$ is entire.

::: {.proof}
The function $f$ is entire by hypothesis, and the exponential function is
entire on $\mathbb C$. Therefore their composition
\[
g=\exp\circ f
\]
is entire.
:::

<1>2. The function $g$ is bounded:
\[
|g(z)|
\le
e^{10}
\qquad
(z\in\mathbb C).
\]

::: {.proof}
For every complex number $w$,
\[
|e^w|
=
e^{\operatorname{Re}w}.
\]
Hence
\[
|g(z)|
=
|e^{f(z)}|
=
e^{\operatorname{Re}f(z)}
\le
e^{10}
\]
by the hypothesis.
:::

<1>3. Liouville's theorem implies that $g$ is constant.

::: {.proof}
Steps <1>1--<1>2 show that $g$ is a bounded entire function. Liouville's
theorem therefore gives
\[
g(z)\equiv c
\]
for some constant $c\in\mathbb C$.
:::

<1>4. The constant $c$ is nonzero.

::: {.proof}
The exponential function never vanishes:
\[
e^w\ne0
\qquad
(w\in\mathbb C).
\]
Thus
\[
g(z)=e^{f(z)}\ne0
\]
for every $z$, so its constant value is nonzero.
:::

<1>5. One has
\[
f'(z)=0
\qquad
(z\in\mathbb C).
\]

::: {.proof}
Differentiate the identity
\[
e^{f(z)}=c.
\]
The chain rule gives
\[
e^{f(z)}f'(z)=0.
\]
By step <1>4,
\[
e^{f(z)}=c\ne0.
\]
Therefore
\[
f'(z)=0
\]
for every $z$.
:::

<1>6. Hence
\[
\boxed{f\text{ is constant}.}
\]

::: {.proof}
An entire function with identically zero derivative is constant on the
connected plane $\mathbb C$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
