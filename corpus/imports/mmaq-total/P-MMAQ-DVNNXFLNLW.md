---
schema: qual/card@1
id: P-MMAQ-DVNNXFLNLW
kind: problem
title: $P_n(z)=\sum_{k=1}^n k z^{k-1}$ has no zeros in $|z|<r<1$ for all sufficiently large $n$
classification:
  areas:
  - complex-analysis
  topics:
  - polynomials
  - holomorphic-functions
relations: []
review: draft
solved: true
---

::: problem
Let $0<r<1$.
Show that the polynomials $P_n(z)  = 1 + 2z + 3 z^2 + \cdots + n z^{n-1}$ have no zeros in $|z|<r$ for all sufficiently large $n$'s.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $0 < r < 1$.
Prove that the sequence of polynomials $P_n(z) = \sum_{k=1}^n k z^{k-1}$ has no zeros in the open disk $D(0, r) = \{z \in \mathbb{C} : |z| < r\}$ for all sufficiently large $n$.

* * *

### Step 1: Identify the Limiting Function

<1>1. **The geometric series $g(z) = \sum_{k=0}^\infty z^k = \frac{1}{1-z}$ converges for $|z| < 1$.** <2>1. For $|z| < 1$, the standard geometric series sum formula holds.
*Proof:* Fundamental property of geometric series.
<2>2. Term-by-term differentiation is valid inside the disk of convergence $|z| < 1$, yielding: $$f(z) \coloneqq g'(z) = \sum_{k=1}^\infty k z^{k-1} = \frac{1}{(1-z)^2}.$$ *Proof:* Power series may be differentiated term-by-term within their radius of convergence.
<2>3. Q.E.D.

<1>2. **$f(z) = \frac{1}{(1-z)^2}$ has no zeros in $\mathbb{D} = \{|z| < 1\}$.** <2>1. For any $z \in \mathbb{D}$, $1-z \neq 0$, so $|f(z)| = \frac{1}{|1-z|^2} > 0$.
*Proof:* The numerator is $1 \neq 0$ and the denominator does not vanish on $|z| < 1$.
<2>2. On the compact disk $\overline{D}(0, r) = \{|z| \leq r\}$, since $|1-z| \leq 1 + |z| \leq 1 + r$, we have the uniform positive lower bound: $$|f(z)| = \frac{1}{|1-z|^2} \geq \frac{1}{(1+r)^2} \eqqcolon m > 0.$$ *Proof:* Triangle inequality $|1-z| \leq 1+|z| \leq 1+r$.
<2>3. Q.E.D.

* * *

### Step 2: Uniform Convergence on Compact Disks

<1>3. **$P_n(z) \to f(z)$ uniformly on the closed disk $\overline{D}(0, r)$.** <2>1. The difference is the tail of the power series: $$|f(z) - P_n(z)| = \left| \sum_{k=n+1}^\infty k z^{k-1} \right| \leq \sum_{k=n+1}^\infty k |z|^{k-1} \leq \sum_{k=n+1}^\infty k r^{k-1}.$$ *Proof:* Triangle inequality for infinite series and $|z| \leq r$.
<2>2. Since $0 < r < 1$, the series $\sum_{k=1}^\infty k r^{k-1}$ converges (by the ratio test, $\lim_{k\to\infty} \frac{k+1}{k} r = r < 1$). *Proof:* Standard ratio test for numerical series.
<2>3. The tail of a convergent series tends to $0$: $$\lim_{n\to\infty} \left( \sum_{k=n+1}^\infty k r^{k-1} \right) = 0.$$ *Proof:* Definition of convergent series.
<2>4. Therefore, $\sup_{|z| \leq r} |f(z) - P_n(z)| \to 0$ as $n \to \infty$.
*Proof:* Follows from <2>1 and <2>3. <2>5. Q.E.D.

* * *

### Step 3: Vanishing of Zeros for Sufficiently Large $n$

<1>4. **There exists $N \in \mathbb{N}$ such that for all $n \geq N$, $P_n(z) \neq 0$ for all $|z| < r$.** <2>1. By <1>2.<2>2, $|f(z)| \geq m > 0$ for all $z \in \overline{D}(0, r)$, where $m = \frac{1}{(1+r)^2}$.
*Proof:* Uniform positive lower bound on $f$.
<2>2. By <1>3.<2>4, choose $N \in \mathbb{N}$ such that for all $n \geq N$: $$\sup_{|z| \leq r} |f(z) - P_n(z)| < m.$$ *Proof:* Uniform convergence allows choosing $N$ for $\varepsilon = m > 0$.
<2>3. For any $n \geq N$ and any $z \in \overline{D}(0, r)$, by the reverse triangle inequality: $$|P_n(z)| = |f(z) - (f(z) - P_n(z))| \geq |f(z)| - |f(z) - P_n(z)| > m - m = 0.$$ *Proof:* Reverse triangle inequality $|a - b| \geq |a| - |b|$.
<2>4. In particular, $|P_n(z)| > 0$ for all $|z| \leq r$, which implies $P_n(z)$ has no zeros in $|z| < r$ for any $n \geq N$ (alternatively, Hurwitz's Theorem applies since $f$ has no zeros in $D(0,r)$). *Proof:* Strict positivity of modulus implies non-vanishing.
<2>5. Q.E.D.
:::
