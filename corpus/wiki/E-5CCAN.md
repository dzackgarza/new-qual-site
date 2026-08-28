---
schema: qual/card@1
id: E-5CCAN
kind: exercise
title: $\mathbb{R}$ is not homeomorphic to $[0,\infty)$
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Connectedness
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: exercise
Show that $\RR$ is not homeomorphic to $[0, \infty)$.
:::

::: solution
**Goal:** Prove that the real line $\mathbb{R}$ and the closed half-line $[0, \infty)$ are not homeomorphic using a topological cut-point (connectedness) argument.

<1>1. Setting and hypothesis:
    Suppose for contradiction that there exists a homeomorphism $f: [0, \infty) \to \mathbb{R}$.

<1>2. Removal of the endpoint $0$:
    *Proof:*
    <2>1. The punctured subspace $[0, \infty) \setminus \{0\} = (0, \infty)$ is an open ray in $\mathbb{R}$, which is connected.
    <2>2. Since $f$ is a bijection, $f$ restricts to a bijection:
        $$f|_{(0, \infty)}: (0, \infty) \to \mathbb{R} \setminus \{f(0)\}.$$
    <2>3. Because $f$ is a homeomorphism, this restriction is a homeomorphism between $(0, \infty)$ and the subspace $\mathbb{R} \setminus \{f(0)\}$.
    <2>4. Connectedness is a topological invariant (preserved under homeomorphisms), so $\mathbb{R} \setminus \{f(0)\}$ must be connected.

<1>3. Contradiction from the disconnectedness of punctured $\mathbb{R}$:
    *Proof:*
    <2>1. Let $y_0 = f(0) \in \mathbb{R}$.
    <2>2. The punctured real line decomposes into:
        $$\mathbb{R} \setminus \{y_0\} = (-\infty, y_0) \cup (y_0, \infty).$$
    <2>3. The sets $(-\infty, y_0)$ and $(y_0, \infty)$ are non-empty, disjoint open subsets of $\mathbb{R} \setminus \{y_0\}$.
    <2>4. Thus $\mathbb{R} \setminus \{y_0\}$ is disconnected, directly contradicting <1>2.

<1>4. Conclusion:
    No homeomorphism between $\mathbb{R}$ and $[0, \infty)$ can exist. Q.E.D.
:::
