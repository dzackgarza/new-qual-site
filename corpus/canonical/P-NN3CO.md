---
schema: qual/card@1
id: P-NN3CO
kind: problem
title: Galois group of $\QQ(\sqrt{2+\sqrt{2}})/\QQ$
classification:
  areas:
  - algebra
  topics:
  - fields
  - galois-theory
relations: []
review: draft
solved: true
---

::: problem
Show that the field extension $\mathbb Q\subseteq\mathbb Q\left(
\sqrt{2+\sqrt2}\right)$ is Galois and determine its Galois group.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $\alpha = \sqrt{2+\sqrt 2}$, and let $K = \QQ(\alpha)$.

1. **Minimal polynomial:**
   Squaring gives $\alpha^2 = 2 + \sqrt 2 \implies \alpha^2 - 2 = \sqrt 2 \implies (\alpha^2 - 2)^2 = 2 \implies \alpha^4 - 4\alpha^2 + 2 = 0$.
   Let $f(x) = x^4 - 4x^2 + 2 \in \QQ[x]$. By Eisenstein's criterion at $p=2$, $f(x)$ is irreducible over $\QQ$. Thus $[K : \QQ] = 4$.

2. **Roots of $f(x)$:**
   The four roots of $f(x)$ are:
   $$
   \pm \alpha = \pm \sqrt{2+\sqrt 2}, \qquad \pm \beta = \pm \sqrt{2-\sqrt 2}.
   $$
   Notice that:
   $$
   \alpha \beta = \sqrt{(2+\sqrt 2)(2-\sqrt 2)} = \sqrt{4 - 2} = \sqrt 2 = \alpha^2 - 2 \in \QQ(\alpha).
   $$
   Therefore, $\beta = \frac{\alpha^2 - 2}{\alpha} \in K$.
   Hence, all four roots $\pm \alpha, \pm \beta$ lie in $K = \QQ(\alpha)$.
   This proves that $K$ is the splitting field of the separable polynomial $f(x)$ over $\QQ$, so $K/\QQ$ is **Galois** of degree 4.

3. **Galois group:**
   Any $\sigma \in \Gal(K/\QQ)$ is determined by where it sends $\alpha$.
   Since $f(x)$ is irreducible and $K$ contains all its roots, there exists an automorphism $\sigma \in \Gal(K/\QQ)$ sending $\alpha \mapsto \beta$.
   Then:
   $$
   \sigma(\sqrt 2) = \sigma(\alpha^2 - 2) = \beta^2 - 2 = (2 - \sqrt 2) - 2 = -\sqrt 2.
   $$
   Now compute $\sigma(\beta)$:
   $$
   \sigma(\beta) = \sigma\left(\frac{\sqrt 2}{\alpha}\right) = \frac{-\sqrt 2}{\beta} = -\alpha.
   $$
   Applying $\sigma$ again:
   $$
   \sigma^2(\alpha) = \sigma(\beta) = -\alpha, \qquad \sigma^3(\alpha) = \sigma(-\alpha) = -\beta, \qquad \sigma^4(\alpha) = \sigma(-\beta) = \alpha.
   $$
   Thus $\sigma$ has order 4, which generates the group.
   Therefore, $\Gal(K/\QQ) \cong \ZZ_4$ (the cyclic group of order 4).
:::
