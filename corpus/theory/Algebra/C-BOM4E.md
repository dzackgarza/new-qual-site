---
schema: qual/card@1
id: C-BOM4E
kind: corollary
title: Quadratic extensions of $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Galois Theory
  - Polynomials
relations: []
review: draft
---

::: {.corollary}
Let $E/\QQ$ be a field extension with $[E:\QQ] = 2$.
Then $E = \QQ(\sqrt q)$ for some squarefree integer $q \notin \theset{0, 1}$.
:::

::: {.proof}
Choose $\alpha\in E\setminus\QQ$.
Since $\QQ \subsetneq \QQ(\alpha) \subseteq E$ and $[E:\QQ]=2$, we have $E = \QQ(\alpha)$, and the minimal polynomial of $\alpha$ over $\QQ$ has the form $x^2 + bx + c$ with $b, c\in\QQ$.
By the quadratic formula, $\alpha = \frac{-b \pm \sqrt d}{2}$ with $d \coloneqq b^2 - 4c\in\QQ$, so $E = \QQ(\sqrt d)$, and $d$ is not a square in $\QQ$ because $\alpha\notin\QQ$.
Write $d = m/n$ with $m, n\in\ZZ$ and $n \neq 0$; then $\sqrt d = \sqrt{mn}/n$, so $E = \QQ(\sqrt{mn})$.
Write $mn = s^2 q$ with $s\in\ZZ\setminus\theset 0$ and $q$ a squarefree integer; then $E = \QQ(\sqrt q)$, and $q\notin\theset{0,1}$ because $d$ is not a square in $\QQ$.
:::
