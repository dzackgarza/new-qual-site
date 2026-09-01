---
schema: qual/card@1
id: P-J64FR
kind: problem
title: Boundedness of $f\mapsto f(1)$ on a weighted Hardy space, its Riesz representer,
  and the maximum of $\operatorname{Re}f(1)$ on $\{f:\|f\|\le 1,\,f(0)=0\}$
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Riesz Representation
  - Series of Functions
relations: []
review: draft
---

::: {.problem}
Consider the complex Hilbert space $$H := \left\{f:\overline{\mathbb{D}}\to\mathbb{C}: f(z)=\sum_{k=0}^\infty \widehat{f}(k)z^k \text{ with } ||f||^2 := \sum_{k=0}^\infty (1+k^2)|\widehat{f}(k)|^2 < \infty\right\}.$$

a. Prove that the linear function $L:f\mapsto f(1)$ is bounded.

b. Find the element $g\in H$ representing $L$.

c. Show that $f\mapsto \text{Re}\,L(f)$ achieves its maximal value on the set $$B := \{f\in H: ||f||\le1 \text{ and } f(0)=0\},$$ that this maximum occurs at a unique point, and determine this maximal value.
:::

::: {.solution}
(a) We have $$|f(1)| \le \sum_{k=0}^\infty |\widehat{f}(k)| = \sum_{k=0}^\infty |\widehat{f}(k)|\sqrt{1+k^2}\frac{1}{\sqrt{1+k^2}} \le \left(\sum_{k=0}^\infty |\widehat{f}(k)|^2(1+k^2)\right)^{1/2}\left(\sum_{k=0}^\infty \frac{1}{1+k^2}\right)^{1/2} = C||f||$$ where $C^2 = \sum_{k=0}^\infty \frac{1}{1+k^2} < \infty$.

(b) We are implicitly assuming the inner product in $H$ is given by $$\langle f,g\rangle = \sum_{k=0}^\infty \widehat{f}(k)\overline{\widehat{g}(k)}(1+k^2).$$ If $g$ represents $L$ then we must have $$\langle f,g\rangle = \sum_{k=0}^\infty \widehat{f}(k)\overline{\widehat{g}(k)}(1+k^2) = f(1) = \sum_{k=0}^\infty \widehat{f}(k).$$ We verify that the choice $\widehat{g}(k)=\frac{1}{1+k^2}$ works: substituting into the inner product gives $$\langle f,g\rangle = \sum_{k=0}^\infty \widehat{f}(k)\overline{\frac{1}{1+k^2}}(1+k^2) = \sum_{k=0}^\infty \widehat{f}(k) = f(1),$$ since $\frac{1}{1+k^2}$ is real and $\frac{1}{1+k^2}(1+k^2) = 1$.
So we can define $$g(z) = \sum_{k=0}^\infty \frac{1}{1+k^2}z^k.$$ The series converges uniformly on $\overline{\mathbb{D}}$ so this definition actually makes sense (and in fact is holomorphic, but that's not necessary).
$\square$

(c) First we note that the maximum value of $\text{Re}(L(f))$ on $B$ must happen when $||f||=1$, otherwise we could normalize $f$ and increase the value of $\text{Re}(L(f))$.
The condition that $f(0)=0$ corresponds to having $\widehat{f}(0)=0$.
So the problem is reduced to maximizing $\sum_{k=1}^\infty \text{Re}(\widehat{f}(k))$ subject to the condition that $\sum_{k=1}^\infty (1+k^2)|\widehat{f}(k)|^2 = 1$.
Note that the constraint only depends on $|\widehat{f}(k)|$.
Thus we can always increase $\text{Re}(f(1))$ while keeping the norm constant if we assume that each $\widehat{f}(k)$ is real and positive.
So without loss of generality we can assume each $\widehat{f}(k)\ge 0$.
Using the same Cauchy-Schwarz argument from part (a), we have $$\sum_{k=1}^\infty \widehat{f}(k) \le \left(\sum_{k=1}^\infty |\widehat{f}(k)|^2(1+k^2)\right)^{1/2}\left(\sum_{k=1}^\infty \frac{1}{1+k^2}\right)^{1/2} = \left(\sum_{k=1}^\infty \frac{1}{1+k^2}\right)^{1/2}$$ and equality holds if and only if $\widehat{f}(k)\sqrt{1+k^2} = \frac{\alpha}{\sqrt{1+k^2}}$ for some $\alpha\in\mathbb{R}$.
This shows that the maximum on $B$ is achieved at a unique point, i.e. $$f(z) = \sum_{k=1}^\infty \frac{\alpha}{1+k^2} z^k.$$ Also, this $\alpha$ is determined by the condition that $f$ has norm 1: $$1 = \sum_{k=1}^\infty (1+k^2)|\widehat{f}(k)|^2 = \sum_{k=1}^\infty \frac{\alpha^2}{1+k^2},$$ so $\alpha = \left(\sum_{k=1}^\infty \frac{1}{1+k^2}\right)^{-1/2}$.
Thus the maximum value achieved is $$\sum_{k=1}^\infty \frac{\alpha}{1+k^2} = \left(\sum_{k=1}^\infty \frac{1}{1+k^2}\right)^{1/2}. \quad \square$$
:::
