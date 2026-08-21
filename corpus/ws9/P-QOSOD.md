---
schema: qual/card@1
id: P-QOSOD
kind: problem
title: Maximum of $|f'(1/2)|$ for holomorphic self-maps of the disk with $f(1/2)=3/4$
classification:
  areas:
  - real-analysis
  topics:
  - Schwarz Lemma
  - Holomorphic Functions
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $D = \{z \in \mathbb{C} : |z| < 1\}$ denote the unit disk.
What is the maximum possible value of $|f'(\frac{1}{2})|$ for a holomorphic function $f : D \to D$ with $f(\frac{1}{2}) = \frac{3}{4}$?
Find all such functions $f$ that attain this maximum value.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Find $\max |f'(\tfrac{1}{2})|$ over holomorphic $f: D \to D$ with $f(\tfrac{1}{2}) = \tfrac{3}{4}$, and all extremal functions.

<1>1. State the Schwarz--Pick lemma.
Proof: for holomorphic $f: D \to D$ and $z \in D$, $|f'(z)| \le \frac{1 - |f(z)|^2}{1 - |z|^2}$, with equality iff $f$ is an automorphism of $D$.

<1>2. Apply Schwarz--Pick at $z = \tfrac{1}{2}$.
Proof: $|f'(\tfrac{1}{2})| \le \frac{1 - (\tfrac{3}{4})^2}{1 - (\tfrac{1}{2})^2} = \frac{1 - \tfrac{9}{16}}{1 - \tfrac{1}{4}} = \frac{\tfrac{7}{16}}{\tfrac{3}{4}} = \frac{7}{12}$.

<1>3. The bound $\tfrac{7}{12}$ is attained exactly when $f$ is an automorphism with $f(\tfrac{1}{2}) = \tfrac{3}{4}$.
Proof: equality in Schwarz--Pick (<1>1) holds iff $f \in \Aut(D)$, i.e. $f(z) = e^{i\theta}\frac{z - a}{1 - \bar a z}$, and the condition $f(\tfrac{1}{2}) = \tfrac{3}{4}$ determines $a$: the automorphism sending $\tfrac12 \mapsto \tfrac34$ is unique up to the rotation, namely $f(z) = \psi_{\tfrac34}^{-1}\qty(e^{i\theta}\,\psi_{\tfrac12}(z))$ where $\psi_w(z) = \frac{w - z}{1 - \bar w z}$ and $|e^{i\theta}| = 1$.

<1>4. Q.E.D. Proof: <1>2 gives the sharp upper bound $\tfrac{7}{12}$; <1>3 identifies the extremals.
:::
