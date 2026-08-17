---
schema: qual/card@1
id: P-SXZZW
kind: problem
title: $\int_{|z|=1}\bigl(z+\frac1z\bigr)^{2n}\frac{dz}{z}$ and $\int_0^{2\pi}\cos^{2n}\theta\,d\theta=2\pi\frac{1\cdot 3\cdots(2n-1)}{2\cdot 4\cdots(2n)}$
classification:
  areas:
  - complex-analysis
  topics:
  - residues
  - contour-integration
  - integrals
  - trigonometry
relations: []
review: draft
solved: true
---

::: problem
Compute
\[
\int_{\abs z = 1} \qty{z + {1\over z}}^{2n} {dz \over z}
\]
and use it to show that
\[
\int_0^{2\pi} \cos^{2n}(\theta) \, d\theta = 2\pi \qty{1\cdot 3 \cdot 5 \cdots (2n-1) \over 2 \cdot 4 \cdot 6 \cdots (2n)}
.\]
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Compute $\int_{\abs z = 1} \qty{z + \frac1z}^{2n} \frac{dz}{z}$ and use it to show $\int_0^{2\pi} \cos^{2n}\theta\, d\theta = 2\pi \frac{1\cdot 3 \cdots (2n-1)}{2\cdot 4 \cdots (2n)}$.

<1>1. Expand $\qty{z + \frac1z}^{2n} = z^{-2n}(z^2 + 1)^{2n} = \sum_{k=0}^{2n} \binom{2n}{k} z^{2k - 2n}$.
    Proof: $z + 1/z = z^{-1}(z^2 + 1)$; raising to the power $2n$ and applying the binomial theorem gives the stated expansion (valid for $z \neq 0$, in particular on $\abs z = 1$).

<1>2. The coefficient of $z^{-1}$ in $\qty{z + \frac1z}^{2n} \frac1z$ is $\binom{2n}{n}$.
    Proof: By <1>1, $\qty{z + \frac1z}^{2n} \frac1z = \sum_{k=0}^{2n} \binom{2n}{k} z^{2k - 2n - 1}$. The power $z^{-1}$ occurs when $2k - 2n - 1 = -1$, i.e. $k = n$, with coefficient $\binom{2n}{n}$.

<1>3. $\int_{\abs z = 1} \qty{z + \frac1z}^{2n} \frac{dz}{z} = 2\pi i \binom{2n}{n}$.
    Proof: By the residue theorem, the integral around the positively oriented unit circle is $2\pi i$ times the residue at $z = 0$, which by <1>2 is the coefficient of $z^{-1}$, namely $\binom{2n}{n}$ (there are no other singularities on or inside the circle).

<1>4. Parametrize $z = e^{i\theta}$, $0 \leq \theta \leq 2\pi$: the integral becomes $i\int_0^{2\pi} \qty(2\cos\theta)^{2n} d\theta$.
    Proof: $z + 1/z = e^{i\theta} + e^{-i\theta} = 2\cos\theta$, and $dz/z = ie^{i\theta} d\theta / e^{i\theta} = i\, d\theta$.

<1>5. Equate <1>3 and <1>4: $\int_0^{2\pi} \cos^{2n}\theta\, d\theta = \frac{2\pi}{2^{2n}}\binom{2n}{n}$.
    Proof: From <1>3 and <1>4, $i\cdot 2^{2n}\int_0^{2\pi}\cos^{2n}\theta\, d\theta = 2\pi i \binom{2n}{n}$; dividing by $i\cdot 2^{2n}$ gives the formula.

<1>6. $\frac{1}{2^{2n}}\binom{2n}{n} = \frac{1\cdot 3 \cdots (2n-1)}{2\cdot 4 \cdots (2n)}$.
    Proof: $\binom{2n}{n} = \frac{(2n)!}{(n!)^2}$. Write $(2n)! = (1\cdot 3 \cdots (2n-1))(2\cdot 4 \cdots (2n))$ and $n! = \frac{2\cdot 4 \cdots (2n)}{2^n}$ (each factor $k$ replaced by $2k/2$), so $\frac{(2n)!}{(n!)^2} \frac1{2^{2n}} = \frac{(1\cdot 3 \cdots (2n-1))(2\cdot 4 \cdots (2n))}{(2\cdot 4 \cdots (2n))^2/2^{2n}} \cdot \frac1{2^{2n}} = \frac{1\cdot 3 \cdots (2n-1)}{2\cdot 4 \cdots (2n)}$.

<1>7. Q.E.D.
    Proof: <1>5 and <1>6 give $\int_0^{2\pi}\cos^{2n}\theta\, d\theta = 2\pi\frac{1\cdot 3 \cdots (2n-1)}{2\cdot 4 \cdots (2n)}$, as required.

:::
