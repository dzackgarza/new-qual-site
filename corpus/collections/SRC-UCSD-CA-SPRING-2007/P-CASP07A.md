---
schema: qual/card@1
id: P-CASP07A
kind: problem
title: "True or False: metric space convergence, Möbius transformations, Liouville, removable singularities, and polynomial approximation"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Determine if the statements below are True or False.

(a) Let $(X, d)$ be a metric space, $x \in X$, and $\{x_n\}_{n=1}^{\infty}$ a sequence in $X$.
If every subsequence of $\{x_n\}_{n=1}^{\infty}$ has a subsequence that converges to $x$, then $\{x_n\}_{n=1}^{\infty}$ converges to $x$.

(b) Let $a \neq b$ be positive real numbers.
There exists a Möbius (linear fractional) transformation sending the circular sector $G_1 := \{x + iy : x^2 + y^2 < 1, \, x > 0, \, y > 0\}$ to the ellipsoidal sector $G_2 := \{x + iy : x^2/a^2 + y^2/b^2 < 1, \, x > 0, \, y > 0\}$.

(c) Let $D$ be a discrete subset of $\mathbb{C}$.
Every bounded analytic function in $\mathbb{C} \setminus D$ is constant.

(d) Suppose that $f(z)$ is analytic in $G := \mathbb{D} \setminus \{0\}$ and that $\int_\gamma z^p f(z)\,dz = 0$ for every closed curve $\gamma: [0,1] \to G$ and every nonnegative integer $p$.
Then $f(z)$ has a removable singularity at 0.

(e) Let $a$ be a complex number with $|a| > 1$.
There exists $\epsilon > 0$ such that if a polynomial $p(z)$ satisfies $|p(z)| < \epsilon$ on the closed unit disk $\overline{\mathbb{D}}$, then $|p(a)| < 1$.
:::

::: solution
(a) **True.** If $x_n$ did not converge to $x$, there would be
$\epsilon>0$ and a subsequence $x_{n_k}$ with
$d(x_{n_k},x)\ge\epsilon$ for every $k$. No subsequence of this subsequence
could converge to $x$, contradicting the hypothesis.

(b) **False.** Möbius transformations send generalized circles (circles or
lines) to generalized circles. The circular boundary arc of $G_1$ would
therefore have to map to a circular or linear arc. For $a\ne b$, the curved
boundary of $G_2$ is an ellipse arc, not a circle or line.

(c) **True.** Since $D$ is discrete, every point of $D$ is an isolated
singularity of the bounded holomorphic function and is therefore removable.
After filling all of them in, the function is bounded and entire; Liouville's
theorem makes it constant.

(d) **True.** Write the Laurent series
\[
f(z)=\sum_{k=-\infty}^{\infty}a_kz^k
\]
on $0<|z|<1$. Taking $\gamma$ to be a small positively oriented circle,
\[
\int_\gamma z^pf(z)\,dz=2\pi i\,a_{-p-1}.
\]
The hypothesis for every $p\ge0$ therefore kills every negative Laurent
coefficient. Hence the singularity at $0$ is removable.

(e) **False.** Given any $\epsilon>0$, choose
\[
p_N(z)=\frac\epsilon2 z^N.
\]
Then $|p_N(z)|<\epsilon$ on $\overline{\mathbb D}$, while
$|p_N(a)|=(\epsilon/2)|a|^N>1$ for all sufficiently large $N$.
:::
