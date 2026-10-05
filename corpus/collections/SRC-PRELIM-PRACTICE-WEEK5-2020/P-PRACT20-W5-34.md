---
schema: qual/card@1
id: P-PRACT20-W5-34
kind: problem
title: Nonconstant entire functions have dense image
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 34).
---

::: {.problem}
Suppose that $f : \CC \to \CC$ is non-constant and entire. Prove that the image of $f$ is dense in $\CC$; that is, for arbitrary $z_0 \in \CC$ and $\varepsilon > 0$, show that there exists $z \in \CC$ such that $\abs{f(z) - z_0} < \varepsilon$. [Note: this is a weaker version of Picard’s Little Theorem which says that the image of $f$ omits at most one point in $\CC$; you should prove this directly without reference to Picard’s Little Theorem.]
:::

::: {.solution}
<1>1. Suppose, toward a contradiction, that the image of $f$ is not dense in
$\mathbb C$. Then there exist $z_0\in\mathbb C$ and $\varepsilon>0$ such that
\[
|f(z)-z_0|\ge\varepsilon
\qquad(z\in\mathbb C).
\]

::: {.proof}
If $f(\mathbb C)$ is not dense, its closure is a proper closed subset of
$\mathbb C$. Choose
\[
z_0\notin\overline{f(\mathbb C)}.
\]
The complement of the closure is open, so some disk
\[
B_\varepsilon(z_0)
\]
is disjoint from $f(\mathbb C)$. This is exactly the displayed inequality.
:::

<1>2. The function
\[
g(z)=\frac1{f(z)-z_0}
\]
is entire and bounded.

::: {.proof}
By step <1>1,
\[
f(z)-z_0\ne0
\]
for every $z$, so $g$ is entire. The same inequality gives
\[
|g(z)|
=
\frac1{|f(z)-z_0|}
\le
\frac1{\varepsilon}.
\]
Thus $g$ is bounded.
:::

<1>3. The function $g$ is constant.

::: {.proof}
By step <1>2, $g$ is bounded and entire. Liouville's theorem therefore
implies that $g$ is constant.
:::

<1>4. The conclusion of step <1>3 forces $f$ to be constant.

::: {.proof}
If
\[
g(z)=c,
\]
then $c\ne0$ and
\[
\frac1{f(z)-z_0}=c.
\]
Hence
\[
f(z)=z_0+\frac1c,
\]
which is constant.
:::

<1>5. Therefore $f(\mathbb C)$ is dense in $\mathbb C$.

::: {.proof}
Step <1>4 contradicts the hypothesis that $f$ is nonconstant. Thus the
assumption in step <1>1 is false. Equivalently, for every $z_0\in\mathbb C$
and every $\varepsilon>0$, there exists $z\in\mathbb C$ such that
\[
\boxed{|f(z)-z_0|<\varepsilon}.
\]
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required density statement.
:::
:::
