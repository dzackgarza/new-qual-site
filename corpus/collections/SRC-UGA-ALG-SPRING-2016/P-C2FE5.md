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

::: problem
Let $R$ be a ring with the following commutative diagram of $R$-modules, where each row represents a short exact sequence of $R$-modules:

\begin{tikzcd}
0 \ar[r] & A \ar[d, "\alpha"] \ar[r, "f"] & B \ar[d, "\beta"] \ar[r, "g"] & C \ar[r] \ar[d, "\gamma"] & 0 \\
0 \ar[r] & A' \ar[r, "f'"] & B'\ar[r, "g'"] & C' \ar[r] & 0 
\end{tikzcd}

Prove that if $\alpha$ and $\gamma$ are **isomorphisms**, then $\beta$ is an **isomorphism** (The Short Five Lemma).
:::

::: solution
**Goal:** Prove that $\beta$ is both injective and surjective by standard diagram chasing using exactness at all nodes and commutativity of squares.

<1>1. Setting and Hypotheses:
    *Proof:*
    <2>1. We are given two short exact sequences of $R$-modules:
        - Top row exactness: $\ker(f) = 0$ ($f$ injective), $\operatorname{im}(f) = \ker(g)$, $\operatorname{im}(g) = C$ ($g$ surjective).
        - Bottom row exactness: $\ker(f') = 0$ ($f'$ injective), $\operatorname{im}(f') = \ker(g')$, $\operatorname{im}(g') = C'$ ($g'$ surjective).
    <2>2. Diagram commutativity:
        $$\beta \circ f = f' \circ \alpha, \qquad \gamma \circ g = g' \circ \beta.$$
    <2>3. $\alpha: A \to A'$ and $\gamma: C \to C'$ are given to be $R$-module isomorphisms (bijective).

<1>2. Proof that $\beta$ is Injective ($\ker(\beta) = \{0\}$):
    *Proof:*
    <2>1. Let $b \in B$ with $\beta(b) = 0 \in B'$.
    <2>2. By commutativity of the right square:
        $$\gamma(g(b)) = g'(\beta(b)) = g'(0) = 0.$$
    <2>3. Since $\gamma$ is an isomorphism (in particular, injective), $\ker(\gamma) = 0$, so:
        $$g(b) = 0 \implies b \in \ker(g).$$
    <2>4. By exactness of the top row at $B$, $\ker(g) = \operatorname{im}(f)$, so there exists $a \in A$ such that:
        $$f(a) = b.$$
    <2>5. Applying $\beta$ and using commutativity of the left square:
        $$f'(\alpha(a)) = \beta(f(a)) = \beta(b) = 0.$$
    <2>6. By exactness of the bottom row at $A'$, $f'$ is injective ($\ker(f') = 0$), which implies:
        $$\alpha(a) = 0.$$
    <2>7. Since $\alpha$ is an isomorphism (in particular, injective), $\ker(\alpha) = 0$, so:
        $$a = 0.$$
    <2>8. Therefore:
        $$b = f(a) = f(0) = 0.$$
    <2>9. This proves $\ker(\beta) = \{0\}$, so $\beta$ is **injective**.

<1>3. Proof that $\beta$ is Surjective ($\operatorname{im}(\beta) = B'$):
    *Proof:*
    <2>1. Let $b' \in B'$ be any element.
    <2>2. Consider $g'(b') \in C'$. Since $\gamma: C \to C'$ is an isomorphism (in particular, surjective), there exists $c \in C$ such that:
        $$\gamma(c) = g'(b').$$
    <2>3. Since the top row is exact at $C$, $g: B \to C$ is surjective, so there exists $b_1 \in B$ such that:
        $$g(b_1) = c.$$
    <2>4. Consider the element $\beta(b_1) \in B'$. By commutativity of the right square:
        $$g'(\beta(b_1)) = \gamma(g(b_1)) = \gamma(c) = g'(b').$$
    <2>5. Therefore:
        $$g'(b' - \beta(b_1)) = g'(b') - g'(\beta(b_1)) = 0 \implies b' - \beta(b_1) \in \ker(g').$$
    <2>6. By exactness of the bottom row at $B'$, $\ker(g') = \operatorname{im}(f')$, so there exists $a' \in A'$ such that:
        $$f'(a') = b' - \beta(b_1).$$
    <2>7. Since $\alpha: A \to A'$ is an isomorphism (in particular, surjective), there exists $a \in A$ such that:
        $$\alpha(a) = a'.$$
    <2>8. Applying $f'$ and using commutativity of the left square:
        $$\beta(f(a)) = f'(\alpha(a)) = f'(a') = b' - \beta(b_1).$$
    <2>9. Rearranging:
        $$b' = \beta(b_1) + \beta(f(a)) = \beta(b_1 + f(a)).$$
    <2>10. Since $b_1 + f(a) \in B$, this shows that $b' \in \operatorname{im}(\beta)$.
    <2>11. Thus $\beta$ is **surjective**.

<1>4. Conclusion:
    Since $\beta$ is an injective and surjective $R$-module homomorphism, $\beta$ is an $R$-module isomorphism. Q.E.D.
:::
