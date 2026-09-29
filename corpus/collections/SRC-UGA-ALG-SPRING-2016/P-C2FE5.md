---
schema: qual/card@1
id: P-C2FE5
kind: problem
title: Short five lemma
classification:
  areas:
  - algebra
  topics:
  - Exact Sequences
  - Homological Algebra
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.problem}
Let $R$ be a ring with the following commutative diagram of $R$-modules, where each row represents a short exact sequence of $R$-modules:

\begin{tikzcd}
0 \ar[r] & A \ar[d, "\alpha"] \ar[r, "f"] & B \ar[d, "\beta"] \ar[r, "g"] & C \ar[r] \ar[d, "\gamma"] & 0 \\
0 \ar[r] & A' \ar[r, "f'"] & B'\ar[r, "g'"] & C' \ar[r] & 0 
\end{tikzcd}

Prove that if $\alpha$ and $\gamma$ are **isomorphisms**, then $\beta$ is an **isomorphism** (The Short Five Lemma).
:::

::: {.solution}
**Goal:** Prove that $\beta$ is both injective and surjective by standard diagram chasing using exactness at all nodes and commutativity of squares.

::: pf

::: pf-step
Setting and Hypotheses:

::: pf-proof

::: pf-step
We are given two short exact sequences of $R$-modules:

- Top row exactness: $\ker(f) = 0$ ($f$ injective), $\operatorname{im}(f) = \ker(g)$, $\operatorname{im}(g) = C$ ($g$ surjective).
- Bottom row exactness: $\ker(f') = 0$ ($f'$ injective), $\operatorname{im}(f') = \ker(g')$, $\operatorname{im}(g') = C'$ ($g'$ surjective).
:::

::: pf-step
Diagram commutativity:
$$\beta \circ f = f' \circ \alpha, \qquad \gamma \circ g = g' \circ \beta.$$
:::

::: pf-step
$\alpha: A \to A'$ and $\gamma: C \to C'$ are given to be $R$-module isomorphisms (bijective).
:::

:::

:::

::: pf-step
Proof that $\beta$ is Injective ($\ker(\beta) = \{0\}$):

::: pf-proof

::: pf-step
Let $b \in B$ with $\beta(b) = 0 \in B'$.
:::

::: pf-step
By commutativity of the right square:
$$\gamma(g(b)) = g'(\beta(b)) = g'(0) = 0.$$
:::

::: pf-step
Since $\gamma$ is an isomorphism (in particular, injective), $\ker(\gamma) = 0$, so:
$$g(b) = 0 \implies b \in \ker(g).$$
:::

::: pf-step
By exactness of the top row at $B$, $\ker(g) = \operatorname{im}(f)$, so there exists $a \in A$ such that:
$$f(a) = b.$$
:::

::: pf-step
Applying $\beta$ and using commutativity of the left square:
$$f'(\alpha(a)) = \beta(f(a)) = \beta(b) = 0.$$
:::

::: pf-step
By exactness of the bottom row at $A'$, $f'$ is injective ($\ker(f') = 0$), which implies:
$$\alpha(a) = 0.$$
:::

::: pf-step
Since $\alpha$ is an isomorphism (in particular, injective), $\ker(\alpha) = 0$, so:
$$a = 0.$$
:::

::: pf-step
Therefore:
$$b = f(a) = f(0) = 0.$$
:::

::: pf-step
This proves $\ker(\beta) = \{0\}$, so $\beta$ is **injective**.
:::

:::

:::

::: pf-step
Proof that $\beta$ is Surjective ($\operatorname{im}(\beta) = B'$):

::: pf-proof

::: pf-step
Let $b' \in B'$ be any element.
:::

::: pf-step
Consider $g'(b') \in C'$. Since $\gamma: C \to C'$ is an isomorphism (in particular, surjective), there exists $c \in C$ such that:
$$\gamma(c) = g'(b').$$
:::

::: pf-step
Since the top row is exact at $C$, $g: B \to C$ is surjective, so there exists $b_1 \in B$ such that:
$$g(b_1) = c.$$
:::

::: pf-step
Consider the element $\beta(b_1) \in B'$. By commutativity of the right square:
$$g'(\beta(b_1)) = \gamma(g(b_1)) = \gamma(c) = g'(b').$$
:::

::: pf-step
Therefore:
$$g'(b' - \beta(b_1)) = g'(b') - g'(\beta(b_1)) = 0 \implies b' - \beta(b_1) \in \ker(g').$$
:::

::: pf-step
By exactness of the bottom row at $B'$, $\ker(g') = \operatorname{im}(f')$, so there exists $a' \in A'$ such that:
$$f'(a') = b' - \beta(b_1).$$
:::

::: pf-step
Since $\alpha: A \to A'$ is an isomorphism (in particular, surjective), there exists $a \in A$ such that:
$$\alpha(a) = a'.$$
:::

::: pf-step
Applying $f'$ and using commutativity of the left square:
$$\beta(f(a)) = f'(\alpha(a)) = f'(a') = b' - \beta(b_1).$$
:::

::: pf-step
Rearranging:
$$b' = \beta(b_1) + \beta(f(a)) = \beta(b_1 + f(a)).$$
:::

::: pf-step
Since $b_1 + f(a) \in B$, this shows that $b' \in \operatorname{im}(\beta)$.
:::

::: pf-step
Thus $\beta$ is **surjective**.
:::

:::

:::

::: pf-step
Conclusion:
Since $\beta$ is an injective and surjective $R$-module homomorphism, $\beta$ is an $R$-module isomorphism.
:::

:::
:::
