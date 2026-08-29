---
schema: qual/card@1
id: E-2GYXM
kind: exercise
title: 'Sum formulas: 1/(n-a)^2'
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Principal Parts
  - Poles
  - Trigonometry
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

:::{.exercise}
Show that
\[
\sum_{k\in \mathbb{Z}}{1\over (z-k)^2} = (\pi \csc(\pi z))^2 = \frac{\pi^2}{\sin^2(\pi z)}
.\]

:::

::: solution
**Goal:** Prove the identity $\sum_{k \in \mathbb{Z}} \frac{1}{(z-k)^2} = \pi^2 \csc^2(\pi z)$ for all $z \in \mathbb{C} \setminus \mathbb{Z}$ using the Cauchy Residue Theorem on an auxiliary meromorphic function.

<1>1. Definition of the auxiliary function:
    Fix $z \in \mathbb{C} \setminus \mathbb{Z}$. Consider the meromorphic function of $w$:
    $$g(w) = \frac{\pi \cot(\pi w)}{(w - z)^2} = \frac{\pi \cos(\pi w)}{\sin(\pi w) (w - z)^2}.$$

<1>2. Calculation of residues in the $w$-plane:
    *Proof:*
    <2>1. Simple poles at $w = k \in \mathbb{Z}$:
        Near $w = k$, $\sin(\pi w) = (-1)^k \pi (w - k) + O((w-k)^3)$ and $\cos(\pi k) = (-1)^k$.
        Thus:
        $$\operatorname{Res}(g, k) = \lim_{w \to k} (w - k) g(w) = \lim_{w \to k} \frac{\pi (w - k)}{\sin(\pi w)} \frac{\cos(\pi w)}{(w - z)^2} = \frac{1}{(k - z)^2} = \frac{1}{(z - k)^2}.$$
    <2>2. Double pole at $w = z$:
        Since $g(w) = \frac{h(w)}{(w - z)^2}$ with $h(w) = \pi \cot(\pi w)$, the residue is given by the derivative $h'(z)$:
        $$\operatorname{Res}(g, z) = h'(z) = \frac{d}{dw}[\pi \cot(\pi w)]_{w = z} = -\pi^2 \csc^2(\pi z).$$

<1>3. Contour integral estimates:
    Let $C_N$ be the square contour with vertices $(N + \frac{1}{2})(\pm 1 \pm i)$ for $N \in \mathbb{Z}_+$.
    *Proof:*
    <2>1. On $C_N$, $|\cot(\pi w)| \le M$ is uniformly bounded by a constant $M > 0$ independent of $N$.
    <2>2. For $w \in C_N$, $|w - z| \ge N + \frac{1}{2} - |z|$.
    <2>3. The length of $C_N$ is $8(N + \frac{1}{2})$.
    <2>4. The contour integral satisfies:
        $$\left|\oint_{C_N} g(w) \, dw\right| \le 8\left(N + \frac{1}{2}\right) \cdot \frac{\pi M}{(N + \frac{1}{2} - |z|)^2} = O\left(\frac{1}{N}\right) \xrightarrow{N \to \infty} 0.$$

<1>4. Application of the Residue Theorem and conclusion:
    *Proof:*
    <2>1. For $N > |z|$, the contour $C_N$ encloses $z$ and the integers $-N, \dots, N$.
    <2>2. By the Residue Theorem:
        $$\frac{1}{2\pi i} \oint_{C_N} g(w) \, dw = \sum_{k=-N}^N \operatorname{Res}(g, k) + \operatorname{Res}(g, z) = \sum_{k=-N}^N \frac{1}{(z - k)^2} - \pi^2 \csc^2(\pi z).$$
    <2>3. Taking $N \to \infty$:
        $$0 = \sum_{k \in \mathbb{Z}} \frac{1}{(z - k)^2} - \pi^2 \csc^2(\pi z) \implies \sum_{k \in \mathbb{Z}} \frac{1}{(z - k)^2} = \pi^2 \csc^2(\pi z).$$
    Q.E.D.
:::

