---
schema: qual/card@1
id: P-CAF10B
kind: problem
title: "Meromorphic functions asymptotic to tan z in the plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Poles
  - Liouville's Theorem
relations: []
review: draft
---

::: problem
Find all functions $f(z)$ that satisfy the two requirements:

(i) $f(z)$ is meromorphic in the plane $\mathbb{C}$.

(ii) There exists a constant $C > 0$ such that $|f(z) - \tan z| \leq C|f(z)|$ for all $z$ outside the poles of $f(z)$ and $\tan z$.
:::

::: solution
Every function
\[
f(z)=c\tan z,
\qquad c\in\mathbb C^*,
\]
satisfies the condition, since
\[
|f(z)-\tan z|=|c-1|\,|\tan z|
=\frac{|c-1|}{|c|}|f(z)|.
\]

Conversely, suppose $f$ satisfies the two requirements. On the set where the
quotient is defined, put
\[
g(z)=1-\frac{\tan z}{f(z)}
=\frac{f(z)-\tan z}{f(z)}.
\]
The hypothesis gives
\[
|g(z)|\le C.
\]
As a quotient of meromorphic functions, $g$ is meromorphic on $\mathbb C$.
Every possible singularity is removable, because $g$ is bounded on a punctured
neighborhood of that point. Hence $g$ extends to a bounded entire function.
By Liouville's theorem, $g\equiv\gamma$ for some constant $\gamma$.

Thus
\[
\frac{\tan z}{f(z)}=1-\gamma=:\lambda.
\]
We cannot have $\lambda=0$, since that would force $\tan z\equiv0$ wherever
$f$ is finite and nonzero, hence identically by analytic continuation.
Therefore
\[
f(z)=\lambda^{-1}\tan z.
\]
So the complete family is
\[
\boxed{f=c\tan z\quad(c\ne0).}
\]
:::
