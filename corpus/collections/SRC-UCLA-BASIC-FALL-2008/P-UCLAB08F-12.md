---
schema: qual/card@1
id: P-UCLAB08F-12
kind: problem
title: Nonuniqueness in least squares comes from the nullspace
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
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Fall 2008.
---

::: {.problem}
Consider
\[
\min_{\mathbf x\in\mathbb R^n}\|A\mathbf x-\mathbf b\|_2,
\qquad A\in\mathbb R^{m\times n},\quad m\ge n.
\]
Prove that if $\mathbf x$ and $\mathbf x+\alpha\mathbf z$ are both minimizers for some $\alpha\ne0$, then $\mathbf z\in\ker A$.
:::

::: {.solution}
Let
\[
\Phi(\mathbf y)=\|A\mathbf y-\mathbf b\|_2^2.
\]

<1>1. Every minimizer $\mathbf y$ of $\Phi$ satisfies the normal equation
\[
A^t(A\mathbf y-\mathbf b)=0.
\]

::: {.proof}
Fix any vector $\mathbf h\in\mathbb R^n$ and consider
\[
g(t)=\Phi(\mathbf y+t\mathbf h).
\]
Since $\mathbf y$ minimizes $\Phi$, the one-variable function $g$ has a minimum at $t=0$, so
\[
g'(0)=0.
\]
Now
\[
\begin{aligned}
g(t)
&=
\|A\mathbf y-\mathbf b+tA\mathbf h\|_2^2\\
&=
\|A\mathbf y-\mathbf b\|_2^2
+
2t\,(A\mathbf y-\mathbf b)^tA\mathbf h
+
t^2\|A\mathbf h\|_2^2.
\end{aligned}
\]
Hence
\[
0=g'(0)
=
2\mathbf h^tA^t(A\mathbf y-\mathbf b).
\]
Since this holds for every $\mathbf h$, one must have
\[
A^t(A\mathbf y-\mathbf b)=0.
\]
:::

<1>2. The two minimizers in the problem satisfy
\[
A^t(A\mathbf x-\mathbf b)=0
\]
and
\[
A^t(A(\mathbf x+\alpha\mathbf z)-\mathbf b)=0.
\]

::: {.proof}
Apply step <1>1 first to $\mathbf y=\mathbf x$ and then to
\[
\mathbf y=\mathbf x+\alpha\mathbf z.
\]
:::

<1>3. One has
\[
A^tA\mathbf z=0.
\]

::: {.proof}
Subtract the two equations from step <1>2:
\[
\alpha A^tA\mathbf z=0.
\]
Since $\alpha\ne0$, divide by $\alpha$.
:::

<1>4. One has
\[
A\mathbf z=0.
\]

::: {.proof}
Take the Euclidean inner product of the equation in step <1>3 with $\mathbf z$:
\[
0
=
\mathbf z^tA^tA\mathbf z
=
\|A\mathbf z\|_2^2.
\]
Therefore
\[
A\mathbf z=0.
\]
:::

<1>5. Thus
\[
\boxed{\mathbf z\in\ker A}.
\]

::: {.proof}
Step <1>4 is exactly the defining condition for membership in $\ker A$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
