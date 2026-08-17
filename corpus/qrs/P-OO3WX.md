---
schema: qual/card@1
id: P-OO3WX
kind: problem
title: $P_n(z)=\sum_{k=1}^n k z^{k-1}$ has no zeros in $|z|<r<1$ for large $n$
classification:
  areas:
  - complex-analysis
  topics:
  - rouche
  - zeros
  - polynomials
  - uniform-convergence
relations: []
review: draft
solved: true
---

::: problem
Let $0<r<1$.
Show that polynomials $P_n(z)  = 1 + 2z + 3 z^2 + \cdots + n z^{n-1}$ have no zeros in $|z|<r$ for all sufficiently large $n$'s.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Let $0 < r < 1$.
Show that $P_n(z) = 1 + 2z + 3z^2 + \cdots + nz^{n-1}$ has no zeros in $|z| < r$ for all sufficiently large $n$.

<1>1. Compute the closed form $P_n(z) = \frac{1 - (n+1)z^n + nz^{n+1}}{(1 - z)^2}$ for $z \ne 1$.
Proof: $P_n = \dv{z}\qty{z + z^2 + \cdots + z^n} = \dv{z}\frac{z(1 - z^n)}{1 - z} = \frac{(1 - (n+1)z^n)(1-z) + z(1-z^n)}{(1-z)^2}$; simplifying: numerator $= 1 - (n+1)z^n - z + (n+1)z^{n+1} + z - z^{n+1} = 1 - (n+1)z^n + nz^{n+1}$.

<1>2. $P_n \to \frac{1}{(1-z)^2}$ uniformly on $|z| \le r$.
Proof: for $|z| \le r < 1$, $|(n+1)z^n| \le (n+1)r^n \to 0$ and $|nz^{n+1}| \le nr^{n+1} \to 0$ (exponential decay $r^n$ beats linear $n$), so <1>1 gives uniform convergence.

<1>3. $\frac{1}{(1-z)^2}$ has no zeros in $|z| \le r$.
Proof: it is nonzero everywhere on $\CC \setminus \{1\}$, and $r < 1$ keeps $z = 1$ out of $|z| \le r$.

<1>4. $P_n$ has no zeros in $|z| < r$ for all sufficiently large $n$.
Proof: $m := \min_{|z| = r}\qty|\frac{1}{(1-z)^2}| > 0$ (compactness and <1>3). By <1>2, for $n$ large $|P_n(z) - \frac{1}{(1-z)^2}| < m$ on $|z| = r$; by Rouch\'e's theorem $P_n$ has the same number of zeros in $|z| < r$ as $\frac{1}{(1-z)^2}$, namely zero.

<1>5. Q.E.D. Proof: <1>1–<1>4 establish the claim.
:::
