---
schema: qual/card@1
id: P-RBVY6
kind: problem
title: Let $f(x) = \frac{1}{x^2+1}$. Use residues to compute the Fourier tran…
classification:
  areas:
  - real-analysis
  topics:
  - fourier-analysis
  - residues
  - contour-integration
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $f(x) = \frac{1}{x^2+1}$.
Use residues to compute the Fourier transform $$\widehat{f}(t) = \int_{-\infty}^{+\infty} f(x)e^{-itx}dx.$$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Compute the Fourier transform $\hat f(t) = \int_{-\infty}^{+\infty} \frac{e^{-itx}}{x^2 + 1}\, dx$ of $f(x) = \frac{1}{x^2+1}$ using residues.

<1>1. The poles of $e^{-itz}/(z^2+1)$ are the simple poles $z = \pm i$, with residues $\Res_{z=i} = \frac{e^{t}}{2i}$ and $\Res_{z=-i} = \frac{e^{-t}}{-2i}$.
Proof: $z^2 + 1 = (z-i)(z+i)$; at $z = i$: $\Res = \lim_{z\to i}(z-i)\frac{e^{-itz}}{(z-i)(z+i)} = \frac{e^{t}}{2i}$; at $z = -i$: $\frac{e^{-t}}{-2i}$.

<1>2. Case $t > 0$: close the contour in the lower half-plane.
<2>1. The integral over the semicircle $\gamma_R: z = Re^{-i\theta}$, $\theta \in [0, \pi]$, tends to $0$ as $R \to \infty$.
Proof: on the arc, $|e^{-itz}| = e^{t\,\Im z} = e^{t(-R\sin\theta)} \le 1$ and $|z^2 + 1| \ge R^2 - 1$, so the arc integral is $O(R/(R^2 - 1)) \to 0$ (this is Jordan's lemma for $t > 0$). <2>2. $\int_{-\infty}^\infty \frac{e^{-itx}}{x^2+1}\,dx = -2\pi i\, \Res_{z=-i} \frac{e^{-itz}}{z^2+1}$.
Proof: residue theorem on the closed contour (real segment $[-R, R]$ plus lower semicircle, traversed negatively); <2>1 kills the arc, leaving $\int = -2\pi i \cdot \frac{e^{-t}}{-2i} = \pi e^{-t}$.

<1>3. Case $t < 0$: close in the upper half-plane to get $\hat f(t) = \pi e^{t}$.
Proof: on the upper semicircle, $|e^{-itz}| = e^{t\,\Im z} = e^{t R\sin\theta} \to 0$ (Jordan's lemma for $t < 0$); the residue theorem gives $\int = 2\pi i \cdot \frac{e^{t}}{2i} = \pi e^{t}$.

<1>4. Case $t = 0$: $\hat f(0) = \pi$.
Proof: $\int_{-\infty}^\infty \frac{dx}{x^2+1} = \arctan x\big|_{-\infty}^\infty = \pi$; also consistent with <1>2–<1>3 at $t = 0$.

<1>5. Q.E.D. Proof: <1>2–<1>4 give $\hat f(t) = \pi e^{-|t|}$.
:::
