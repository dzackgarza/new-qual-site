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

(b) The inner product on $H$ is $$\langle f,g\rangle = \sum_{k=0}^\infty \widehat{f}(k)\overline{\widehat{g}(k)}(1+k^2).$$ If $g$ represents $L$ then we must have $$\langle f,g\rangle = \sum_{k=0}^\infty \widehat{f}(k)\overline{\widehat{g}(k)}(1+k^2) = f(1) = \sum_{k=0}^\infty \widehat{f}(k).$$ We verify that the choice $\widehat{g}(k)=\frac{1}{1+k^2}$ works: substituting into the inner product gives $$\langle f,g\rangle = \sum_{k=0}^\infty \widehat{f}(k)\overline{\frac{1}{1+k^2}}(1+k^2) = \sum_{k=0}^\infty \widehat{f}(k) = f(1),$$ since $\frac{1}{1+k^2}$ is real and $\frac{1}{1+k^2}(1+k^2) = 1$.
Define $$g(z) = \sum_{k=0}^\infty \frac{1}{1+k^2}z^k.$$ The series converges uniformly on $\overline{\mathbb{D}}$, and $\|g\|^2=\sum_{k\ge0}(1+k^2)^{-1}<\infty$, so $g\in H$.
$\square$

(c) The value $\text{Re}(L(f))$ is positive for some $f\in B$, so at a maximizer $||f||=1$: otherwise $f/||f||\in B$ has a larger value.
The condition $f(0)=0$ is $\widehat{f}(0)=0$.
So we maximize $\sum_{k=1}^\infty \text{Re}(\widehat{f}(k))$ subject to $\sum_{k=1}^\infty (1+k^2)|\widehat{f}(k)|^2 = 1$.
The constraint depends only on the moduli $|\widehat{f}(k)|$, and $\text{Re}\,\widehat{f}(k)\le|\widehat{f}(k)|$ with equality if and only if $\widehat{f}(k)\ge0$.
Hence replacing each $\widehat{f}(k)$ by $|\widehat{f}(k)|$ keeps $f$ in $B$ and strictly increases $\text{Re}(f(1))$ unless every $\widehat{f}(k)\ge0$, so a maximizer has $\widehat{f}(k)\ge 0$ for all $k$.
Using the same Cauchy-Schwarz argument from part (a), we have $$\sum_{k=1}^\infty \widehat{f}(k) \le \left(\sum_{k=1}^\infty |\widehat{f}(k)|^2(1+k^2)\right)^{1/2}\left(\sum_{k=1}^\infty \frac{1}{1+k^2}\right)^{1/2} = \left(\sum_{k=1}^\infty \frac{1}{1+k^2}\right)^{1/2}$$ and equality holds if and only if $\widehat{f}(k)\sqrt{1+k^2} = \frac{\alpha}{\sqrt{1+k^2}}$ for some $\alpha\in\mathbb{R}$.
This shows that the maximum on $B$ is achieved at a unique point, i.e. $$f(z) = \sum_{k=1}^\infty \frac{\alpha}{1+k^2} z^k.$$ Also, this $\alpha$ is determined by the condition that $f$ has norm 1: $$1 = \sum_{k=1}^\infty (1+k^2)|\widehat{f}(k)|^2 = \sum_{k=1}^\infty \frac{\alpha^2}{1+k^2},$$ so $\alpha = \left(\sum_{k=1}^\infty \frac{1}{1+k^2}\right)^{-1/2}$.
Thus the maximum value achieved is $$\sum_{k=1}^\infty \frac{\alpha}{1+k^2} = \left(\sum_{k=1}^\infty \frac{1}{1+k^2}\right)^{1/2}. \quad \square$$
:::
