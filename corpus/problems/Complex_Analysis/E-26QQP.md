---
schema: qual/card@1
id: E-26QQP
kind: problem
title: $\sum_{k\in\mathbb{Z}}\frac{(-1)^k}{(k+a)^2}=\pi^2\cos(\pi a)\csc^2(\pi a)$
  for $a\in\mathbb{R}\setminus\mathbb{Z}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Meromorphic Functions
  - Series of Numbers
  - Trigonometry
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
\sum_{k\in \mathbb{Z}} { (-1)^k \over (k+a)^2} = \pi^2 \cos(\pi a)\csc^2(\pi a) \quad \text{for } a\in \mathbb{R}\setminus\mathbb{Z}
.\]

:::

::: solution
**Goal:** Evaluate the infinite series $\sum_{k \in \mathbb{Z}} \frac{(-1)^k}{(k+a)^2}$ for $a \in \mathbb{R} \setminus \mathbb{Z}$ using contour integration and the Cauchy Residue Theorem.

<1>1. Definition of the auxiliary meromorphic function:
    Consider the meromorphic function:
    $$f(z) = \frac{\pi \csc(\pi z)}{(z+a)^2} = \frac{\pi}{\sin(\pi z)(z+a)^2}.$$
    Since $a \notin \mathbb{Z}$, the poles of $f(z)$ consist of simple poles at the integers $z = k \in \mathbb{Z}$ and a double pole at $z = -a$.

<1>2. Residues at the simple poles $z = k \in \mathbb{Z}$:
    *Proof:*
    <2>1. Near $z = k$, the Taylor expansion of the sine function gives $\sin(\pi z) = (-1)^k \pi (z - k) + O((z-k)^3)$.
    <2>2. The residue is:
        $$\operatorname{Res}(f, k) = \lim_{z \to k} (z - k) f(z) = \lim_{z \to k} \frac{\pi (z - k)}{\sin(\pi z)} \frac{1}{(z+a)^2} = \frac{(-1)^k}{(k+a)^2}.$$

<1>3. Residue at the double pole $z = -a$:
    *Proof:*
    <2>1. Let $g(z) = \pi \csc(\pi z)$. Then $f(z) = \frac{g(z)}{(z+a)^2}$.
    <2>2. The residue at the order 2 pole $z = -a$ is given by $g'(-a)$:
        $$g'(z) = \frac{d}{dz}[\pi \csc(\pi z)] = -\pi^2 \csc(\pi z) \cot(\pi z).$$
    <2>3. Evaluating at $z = -a$:
        $$\operatorname{Res}(f, -a) = -\pi^2 \csc(-\pi a) \cot(-\pi a) = -\pi^2 (-\csc(\pi a))(-\cot(\pi a)) = -\pi^2 \csc(\pi a)\cot(\pi a) = -\frac{\pi^2 \cos(\pi a)}{\sin^2(\pi a)}.$$

<1>4. Vanishing of the contour integral along large squares:
    Let $C_N$ be the square contour with vertices $(N + \frac{1}{2})(\pm 1 \pm i)$ for $N \in \mathbb{Z}_+$.
    *Proof:*
    <2>1. There exists a constant $M > 0$ independent of $N$ such that $|\csc(\pi z)| \le M$ for all $z \in C_N$.
    <2>2. For $z \in C_N$, $|z| \ge N + \frac{1}{2}$, so $|z + a| \ge N + \frac{1}{2} - |a|$.
    <2>3. The length of $C_N$ is $8(N + \frac{1}{2})$.
    <2>4. The integral is bounded by:
        $$\left|\oint_{C_N} f(z) \, dz\right| \le 8\left(N + \frac{1}{2}\right) \cdot \frac{\pi M}{(N + \frac{1}{2} - |a|)^2} = O\left(\frac{1}{N}\right) \xrightarrow{N \to \infty} 0.$$

<1>5. Application of the Residue Theorem and conclusion:
    *Proof:*
    <2>1. For $N > |a|$, the contour $C_N$ encloses $-a$ and the integers $-N, \dots, N$.
    <2>2. By the Cauchy Residue Theorem:
        $$\frac{1}{2\pi i} \oint_{C_N} f(z) \, dz = \sum_{k=-N}^N \operatorname{Res}(f, k) + \operatorname{Res}(f, -a) = \sum_{k=-N}^N \frac{(-1)^k}{(k+a)^2} - \pi^2 \cos(\pi a)\csc^2(\pi a).$$
    <2>3. Taking $N \to \infty$ and applying <1>4:
        $$0 = \sum_{k \in \mathbb{Z}} \frac{(-1)^k}{(k+a)^2} - \pi^2 \cos(\pi a)\csc^2(\pi a) \implies \sum_{k \in \mathbb{Z}} \frac{(-1)^k}{(k+a)^2} = \pi^2 \cos(\pi a)\csc^2(\pi a).$$
    Q.E.D.
:::

