---
schema: qual/card@1
id: P-MMAQ-EFQKE6KDK7
kind: problem
title: $\lim_{n\to\infty}\int_1^n\frac{n e^{-x}}{1+nx^2}\sin(x/n)\,dx=0$
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - convergence-of-functions
relations: []
review: draft
solved: true
---

::: problem
Compute the following limit:
$$
\lim _{n \rightarrow \infty} \int_{1}^{n} \frac{n e^{-x}}{1+n x^{2}} ~\sin \left(\frac x n\right) ~d x
$$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Compute $\lim_{n\to\infty} \int_1^n \frac{n e^{-x}}{1+nx^2} \sin(x/n) ~dx$.

<1>1. The answer is $0$.
<2>1. Reduce to an integral over $[1, \infty)$.
Proof: Extend each integrand by $0$ outside $[1, n]$; the limit of $\int_1^n f_n$ equals the limit of $\int_1^\infty f_n$ when the latter exists, since the two differ by $\int_n^\infty f_n$ and $f_n$ is dominated by an integrable function (see <1>2). <2>2. Establish the pointwise limit $f_n(x) \to 0$ for each fixed $x \geq 1$.
Proof: For $x \geq 1$ fixed and $n > x$, $\frac{n}{1+nx^2} \to \frac{1}{x^2}$ and $\sin(x/n) \to 0$, so $f_n(x) = \frac{n e^{-x}}{1+nx^2}\sin(x/n) \to \frac{e^{-x}}{x^2} \cdot 0 = 0$.
<2>3. Q.E.D. Proof: By <1>2, the pointwise limit of the (extended) integrands is the zero function.

<1>2. The sequence is dominated by an integrable function on $[1, \infty)$.
<2>1. For every $t \geq 0$, $\abs{\sin t} \leq t$.
Proof: Standard bound, e.g. from the mean value theorem or the alternating series for $\sin t$.
<2>2. With $t = x/n \geq 0$, $\abs{\sin(x/n)} \leq x/n$.
Proof: By <2>1 with $t = x/n$.
<2>3. Hence $\abs{f_n(x)} \leq \frac{n e^{-x}}{1+nx^2} \cdot \frac{x}{n} = \frac{x e^{-x}}{1+nx^2} \leq x e^{-x}$.
Proof: Multiply the bound of <2>2 by the positive factor $\frac{n e^{-x}}{1+nx^2}$, then drop the denominator $1+nx^2 \geq 1$.
<2>4. $\int_1^\infty x e^{-x} ~dx = 2 e^{-1} < \infty$.
Proof: Compute $\int_1^\infty x e^{-x} ~dx = \left[-(x+1)e^{-x}\right]_1^\infty = 2e^{-1}$ by integration by parts.
<2>5. Q.E.D. Proof: $x e^{-x}$ is integrable on $[1,\infty)$ and dominates every $f_n$ by <2>3.

<1>3. Conclusion: the limit is $0$.
Proof: By <1>2, the dominated convergence theorem applies: the dominated integrands converge pointwise to $0$ (<1>1), so $\lim_n \int_1^n f_n = \int_1^\infty 0 = 0$.
:::
