---
schema: qual/card@1
id: T-OW2QG
kind: theorem
title: Hahn-Banach
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Dual Spaces
relations: []
review: draft
---

::: {.theorem title="Hahn-Banach"}
Let $\mathcal X$ be a real vector space and $p: \mathcal X\to\RR$ a **sublinear functional**, i.e. $p(x+y) \leq p(x) + p(y)$ and $p(\lambda x) = \lambda p(x)$ for all $x,y\in \mathcal X$ and all $\lambda \geq 0$.
Let $\mathcal M \subseteq \mathcal X$ be a subspace and $f$ a linear functional on $\mathcal M$ with $f \leq p$ on $\mathcal M$.
Then $f$ extends to a linear functional $F$ on all of $\mathcal X$ with $\ro{F}{\mathcal M} = f$ and $F \leq p$ on $\mathcal X$.

Over $\CC$, with $p$ a **seminorm** and $\abs f \leq p$ on $\mathcal M$, the same conclusion holds with $\abs F \leq p$ on $\mathcal X$.

No norm and no topology appear in the hypotheses; the proof extends one dimension at a time and appeals to Zorn's lemma, so the extension is generally not unique.
:::

::: {.remark}
The normed-space consequences are what the theorem is used for.
For $\mathcal M \subseteq \mathcal X$ a closed subspace and $x\notin\mathcal M$ at distance $\delta \da \inf_{y\in \mathcal M}\norm{x-y}$, there is $f \in \mathcal X\dual$ with $\norm{f} = 1$, $\ro f {\mathcal M} = 0$ and $f(x) = \delta$.
Taking $\mathcal M = 0$ gives, for each $x\neq 0$, an $f\in \mathcal X\dual$ with $\norm f = 1$ and $f(x) = \norm x$.
So $\mathcal X\dual$ separates points, and $x \mapsto \hat x$, $\hat x(f) \da f(x)$, is a linear isometry $\mathcal X \injects \mathcal X^{\vee\vee}$.
:::

::: {.concept}
See Folland, *Real Analysis*, §5.2, Theorem 5.6 (real) and Theorem 5.7 (complex), pp. 157-158; the normed-space corollaries are Theorem 5.8.
:::
