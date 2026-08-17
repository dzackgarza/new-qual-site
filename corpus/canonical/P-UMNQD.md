---
schema: qual/card@1
id: P-UMNQD
kind: problem
title: Let $F \subset K \subset L$ be finite degree field extensions. For each of...
classification:
  areas:
  - algebra
  topics:
  - galois-theory
  - field-extensions
  - counterexamples
relations: []
review: draft
solved: true
---

::: problem
Let $F \subset K \subset L$ be finite degree field extensions.
For each of the following assertions, give a proof or a counterexample.

(a) If $L/F$ is Galois, then so is $K/F$.

(b) If $L/F$ is Galois, then so is $L/K$.

(c) If $K/F$ and $L/K$ are both Galois, then so is $L/F$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**(a) FALSE (Counterexample):** Let $F = \QQ$, $K = \QQ(\sqrt[3]{2})$, and $L = \QQ(\sqrt[3]{2}, \omega)$ where $\omega = e^{2\pi i / 3}$.

- $L$ is the splitting field of the separable polynomial $x^3 - 2$ over $\QQ$, so $L/\QQ$ is Galois (with $\Gal(L/\QQ) \cong S_3$).

- However, $K/\QQ = \QQ(\sqrt[3]{2})/\QQ$ is not Galois because it contains one root of $x^3 - 2$ but not the complex roots $\omega \sqrt[3]{2}$ and $\omega^2 \sqrt[3]{2}$, so $K/\QQ$ is not normal.

**(b) TRUE (Proof):** Since $L/F$ is finite and Galois, $L/F$ is separable and normal.

1. **Separability:** Every element $\alpha \in L$ is separable over $F$.
   Since the minimal polynomial of $\alpha$ over $K$ divides the minimal polynomial of $\alpha$ over $F$, $\alpha$ is also separable over $K$.
   Thus $L/K$ is separable.

2. **Normality:** Since $L/F$ is normal, $L$ is the splitting field over $F$ of some polynomial $f(x) \in F[x]$.
   Since $F \subseteq K$, $f(x) \in K[x]$, and $L$ is generated over $K$ by the roots of $f(x)$.
   Thus $L$ is the splitting field of $f(x)$ over $K$, so $L/K$ is normal.
   Since $L/K$ is finite, separable, and normal, $L/K$ is **Galois**. (By the Galois correspondence, $\Gal(L/K) \leq \Gal(L/F)$.)

**(c) FALSE (Counterexample):** Let $F = \QQ$, $K = \QQ(\sqrt 2)$, and $L = \QQ(\sqrt[4]{2})$.

- $K/F = \QQ(\sqrt 2)/\QQ$ is a degree 2 extension, hence Galois (splitting field of $x^2 - 2$).

- $L/K = \QQ(\sqrt[4]{2})/\QQ(\sqrt 2)$ is a degree 2 extension (minimal polynomial $x^2 - \sqrt 2 \in K[x]$), hence Galois.

- However, $L/F = \QQ(\sqrt[4]{2})/\QQ$ is not Galois: the polynomial $x^4 - 2 \in \QQ[x]$ is irreducible over $\QQ$ by Eisenstein ($p=2$), and $L$ contains the real root $\sqrt[4]{2}$ but not the non-real roots $\pm i \sqrt[4]{2}$.
  Thus $L/\QQ$ is not normal, hence not Galois.
:::
