---
schema: qual/card@1
id: P-VBXL4
kind: problem
title: "Apply Rouch\u00e9's Theorem to prove the Fundamental Theorem of\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - rouche
  - polynomials
  - zeros
relations: []
review: draft
solved: true
---

::: problem
Apply Rouché's Theorem to prove the Fundamental Theorem of Algebra: If $$P_n(z) = a_0 + a_1z + \cdots + a_{n-1}z^{n-1} + a_nz^n\quad  (a_n \neq 0)$$ is a polynomial of degree n, then it has n zeros in $\mathbf C$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $f(z) = a_n z^n$ and $g(z) = a_{n-1} z^{n-1} + \cdots + a_1 z + a_0$, so that $P_n(z) = f(z) + g(z)$.

Consider the circle $C_R = \{z \in \CC : |z| = R\}$.
On $C_R$:
$$
|f(z)| = |a_n| R^n,
$$
$$
|g(z)| \leq \sum_{k=0}^{n-1} |a_k| R^k.
$$
Dividing by $|f(z)|$:
$$
\frac{|g(z)|}{|f(z)|} \leq \sum_{k=0}^{n-1} \frac{|a_k|}{|a_n| R^{n-k}} \to 0 \quad \text{as } R \to \infty,
$$
since $n - k \geq 1$ for all $k \in \{0, \ldots, n-1\}$.

Thus, there exists $R > 0$ large enough such that:
$$
|g(z)| < |f(z)| \quad \text{for all } z \in C_R.
$$

By **Rouché's Theorem**, the functions $f(z)$ and $P_n(z) = f(z) + g(z)$ have the exact same number of zeros (counted with multiplicity) inside the circle $C_R$.
Since $f(z) = a_n z^n$ has a zero of order $n$ at $z = 0$ (and no other zeros), $f(z)$ has precisely $n$ zeros in $|z| < R$.
Therefore, $P_n(z)$ has precisely $n$ zeros in $|z| < R \subset \CC$ (counted with multiplicity).
:::
