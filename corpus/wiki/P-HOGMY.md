---
schema: qual/card@1
id: P-HOGMY
kind: problem
title: "Suppose that $f: \\mathbb{D} \\rightarrow \\mathbb{D}$ is holomorphic and\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - schwarz-lemma
  - fixed-points
  - sequences-of-functions
relations: []
review: draft
---
:::{.problem title="?"}
Suppose that $f: \mathbb{D} \rightarrow \mathbb{D}$ is holomorphic and $f(0)=0$. Let $n \geq 1$, and define the function $f_{n}(z)$ to be the $n$-th composition of $f$ with itself; more precisely, let

$$
f_{1}(z):=f(z), f_{2}(z):=f(f(z)), \text { in general } f_{n}(z):=f\left(f_{n-1}(z)\right) .
$$

Suppose that for each $z \in \mathbb{D}, \lim _{n \rightarrow \infty} f_{n}(z)$ exists and equals to $g(z)$. Prove that either $g(z) \equiv 0$ or $g(z)=z$ for all $z \in D$.

:::

:::{.solution}
Note that there is a unique fixed point.
We have $f(0) = 0$, so there is at least one, so suppose $a$ is another fixed point with $f(a) = a$.
By Schwarz, $\abs{f(z)}\leq \abs{z}$ with equality at any nonzero point implying $f$ is a rotation, and $f(a) = a\implies \abs{f(a)} = \abs{a}$, so write $f(z) = e^{i\theta}z$.
Now $f(a) = a = e^{i\theta }a$ forces $\theta = 0$, so $f(z) = z$ is the identity.


Since $f(0) = 0$, the Schwarz lemma applies and either

- $f(z) = e^{i\theta} z$ is a rotation, or
- $\abs{f'(0)} < 1$ and $\abs{f(z)} < z$ for all $z\in \DD$.

Supposing the latter, $f$ is a contraction, and $\abs{f_{n+1}(z)} < \abs{f_{n}(z)}$ for all $n$ and all $z$, so $\abs{f_n(z)} \convergesto{n\to\infty} 0$ for all $z$.
Since $f_n\to g$ pointwise, this means $g(z) = 0$ for all $z$, making $g\equiv 0$.

Otherwise, suppose $f$ is a rotation.
Then if $f(z) = e^{i\theta}z$, $f_n(z) = e^{in\theta}z$.
The pointwise limit $\lim_{n\to\infty}e^{in\theta}z$ can only exist if $\theta = 0$, otherwise this is periodic when $\theta$ is rational or the points $e^{i\theta}z, e^{2i\theta }z,\cdots$ form form a countably infinite set of distinct points.
So $f(z) = z$, making $\lim_{n\to \infty}f_n(z) = z$ as well.
:::

