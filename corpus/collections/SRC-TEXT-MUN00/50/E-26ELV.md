---
schema: qual/card@1
id: E-26ELV
kind: problem
title: Second countable locally compact Hausdorff spaces of finite dimension imbed as closed subspaces
classification:
  areas:
  - topology
  topics:
  - Dimension
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Prove the following.

Theorem.
Let $X$ be a locally compact Hausdorff space with a countable basis, such that every compact subspace of $X$ has topological dimension at most $m$.
Then $X$ is homeomorphic to a closed subspace of $\mathbb{R}^{2m+1}$.

If $f: X \to \mathbb{R}^N$ is a continuous map, we say $f(x) \to \infty$ as $x \to \infty$ if given $n$, there is a compact subspace $C$ of $X$ such that $f(x) > n$ for $x \in X - C$.

(a) Let $\bar{\rho}$ be the uniform metric on $\mathcal{C}(X, \mathbb{R}^N)$.
Show that if $f(x) \to \infty$ as $x \to \infty$ and $\bar{\rho}(f, g) < 1$, then $g(x) \to \infty$ as $x \to \infty$.

(b) Show that if $f(x) \to \infty$ as $x \to \infty$, then $f$ extends to a continuous map of one-point compactifications.
Conclude that if $f$ is injective as well, then $f$ is a homeomorphism of $X$ with a closed subspace of $\mathbb{R}^N$.

(c) Given $f: X \to \mathbb{R}^N$ and given a compact subspace $C$ of $X$, let

$$
U_\epsilon(C) = \ts{f \mid \Delta(f \mid C) < \epsilon}.
$$

Show that $U_\epsilon(C)$ is open in $\mathcal{C}(X, \mathbb{R}^N)$.

(d) Show that if $N = 2m + 1$, then $U_\epsilon(C)$ is dense in $\mathcal{C}(X, \mathbb{R}^N)$.
[Hint: Given $f$ and given $\epsilon, \delta > 0$, choose $g: C \to \mathbb{R}^N$ so that $d(f(x), g(x)) < \delta$ for $x \in C$, and $\Delta(g) < \epsilon$. Extend $f - g$ to $h: X \to [-\delta, \delta]^N$ using the Tietze theorem.]

(e) Show there exists a map $f: X \to \mathbb{R}^N$ such that $f(x) \to \infty$ as $x \to \infty$.
[Hint: Write $X$ as the union of compact subspaces $C_n$ such that $C_n \subset \operatorname{Int} C_{n+1}$ for each $n$.]

(f) Let $C_n$ be as in (e). Use the fact that $\bigcap U_{1/n}(C_n)$ is dense in $\mathcal{C}(X, \mathbb{R}^N)$ to complete the proof.
:::

::: solution
**Goal:** Prove that every second-countable locally compact Hausdorff space $X$ with $\dim C \le m$ for all compact $C \subset X$ embeds as a closed subspace of $\mathbb{R}^{2m+1}$.

<1>1. Part (a): Perturbation of proper maps.
*Proof:* <2>1. Let $n \in \mathbb{Z}_+$.
Since $f(x) \to \infty$, there exists a compact $C \subset X$ such that $\|f(x)\| > n + 1$ for all $x \in X \setminus C$.
<2>2. Since $\bar{\rho}(f, g) < 1$, $\|f(x) - g(x)\| \le 1$ for all $x \in X$.
<2>3. For any $x \in X \setminus C$: $$\|g(x)\| \ge \|f(x)\| - \|f(x) - g(x)\| > (n + 1) - 1 = n.$$ <2>4. Hence $g(x) \to \infty$ as $x \to \infty$.

<1>2. Part (b): Continuous extension to one-point compactifications and closed embeddings.
*Proof:* <2>1. Let $X^* = X \cup \{\infty_X\}$ and $(\mathbb{R}^N)^* = \mathbb{R}^N \cup \{\infty\}$ be the one-point compactifications.
<2>2. Define $f^*: X^* \to (\mathbb{R}^N)^*$ by $f^*(x) = f(x)$ for $x \in X$ and $f^*(\infty_X) = \infty$.
<2>3. For any neighborhood $V$ of $\infty$ in $(\mathbb{R}^N)^*$, $V$ contains $(\mathbb{R}^N \setminus \overline{B}_n) \cup \{\infty\}$.
Since $f(x) \to \infty$, there is a compact $C \subset X$ with $f(X \setminus C) \subseteq \mathbb{R}^N \setminus \overline{B}_n$, so $(f^*)^{-1}(V) \supseteq (X \setminus C) \cup \{\infty_X\}$, which is open in $X^*$.
Thus $f^*$ is continuous.
<2>4. If $f$ is injective, then $f^*$ is an injective continuous map from the compact Hausdorff space $X^*$ into the Hausdorff space $(\mathbb{R}^N)^*$, hence a topological embedding.
<2>5. The image $f^*(X^*)$ is compact, hence closed in $(\mathbb{R}^N)^*$.
<2>6. Restricting to $X$, $f(X) = f^*(X^*) \cap \mathbb{R}^N$ is closed in $\mathbb{R}^N$, and $f: X \to f(X)$ is a homeomorphism.

<1>3. Part (c): Openness of $U_\varepsilon(C)$.
*Proof:* <2>1. The condition $\Delta(f|_C) < \varepsilon$ is equivalent to saying that if $x_1, x_2 \in C$ with $d(x_1, x_2) \ge \varepsilon$, then $f(x_1) \neq f(x_2)$.
<2>2. The set $S = \{(x_1, x_2) \in C \times C : d(x_1, x_2) \ge \varepsilon\}$ is compact.
<2>3. If $f \in U_\varepsilon(C)$, the continuous function $(x_1, x_2) \mapsto \|f(x_1) - f(x_2)\|$ is strictly positive on $S$, so it achieves a minimum $\delta = \min_S \|f(x_1) - f(x_2)\| > 0$.
<2>4. If $\bar{\rho}(f, g) < \frac{\delta}{3}$, then for all $(x_1, x_2) \in S$: $$\|g(x_1) - g(x_2)\| \ge \|f(x_1) - f(x_2)\| - 2\bar{\rho}(f, g) \ge \delta - \frac{2\delta}{3} = \frac{\delta}{3} > 0.$$ <2>5. Thus $g \in U_\varepsilon(C)$, so $U_\varepsilon(C)$ is open.

<1>4. Part (d): Density of $U_\varepsilon(C)$ for $N = 2m + 1$.
*Proof:* <2>1. Since $\dim C \le m$, the classical Menger-Nöbeling embedding theorem shows that maps with $\Delta < \varepsilon$ are dense in $\mathcal{C}(C, \mathbb{R}^{2m+1})$.
<2>2. Given $f \in \mathcal{C}(X, \mathbb{R}^N)$ and $\delta > 0$, choose $g_0 \in \mathcal{C}(C, \mathbb{R}^N)$ such that $\|f|_C - g_0\| < \delta$ and $\Delta(g_0) < \varepsilon$.
<2>3. By the Tietze Extension Theorem, extend the coordinate functions of $g_0 - f|_C: C \to [-\delta, \delta]^N$ to a continuous map $h: X \to [-\delta, \delta]^N$.
<2>4. Define $g = f + h \in \mathcal{C}(X, \mathbb{R}^N)$.
Then $\bar{\rho}(f, g) \le \delta$ and $g|_C = g_0 \in U_\varepsilon(C)$, proving density.

<1>5. Part (e): Existence of a proper map $f_0: X \to \mathbb{R}^N$.
*Proof:* <2>1. Since $X$ is locally compact and second-countable, $X = \bigcup_{n=1}^\infty C_n$ where each $C_n$ is compact and $C_n \subset \operatorname{Int} C_{n+1}$.
<2>2. By Urysohn's Lemma, choose continuous functions $\phi_n: X \to [0, 1]$ with $\phi_n(C_n) = \{1\}$ and $\phi_n(X \setminus \operatorname{Int} C_{n+1}) = \{0\}$.
<2>3. Define $\psi: X \to \mathbb{R}$ by $\psi(x) = \sum_{n=1}^\infty (1 - \phi_n(x))$.
For $x \in X \setminus C_k$, $\psi(x) \ge k - 1$.
<2>4. The map $f_0(x) = (\psi(x), 0, \dots, 0) \in \mathbb{R}^N$ is continuous and satisfies $f_0(x) \to \infty$ as $x \to \infty$.

<1>6. Part (f): Synthesis via Baire Category Theorem.
*Proof:* <2>1. Since $\mathbb{R}^N$ is complete, $(\mathcal{C}(X, \mathbb{R}^N), \bar{\rho})$ is a complete metric space, hence a Baire space.
<2>2. Let $B = \{g \in \mathcal{C}(X, \mathbb{R}^N) : \bar{\rho}(f_0, g) < 1\}$.
$B$ is a non-empty open subspace, hence a Baire space.
<2>3. For each $n \in \mathbb{Z}_+$, $U_{1/n}(C_n) \cap B$ is open and dense in $B$ by <1>3 and <1>4. <2>4. By the Baire Category Theorem, the intersection $G = \bigcap_{n=1}^\infty U_{1/n}(C_n) \cap B$ is dense in $B$, hence non-empty.
<2>5. Choose $f \in G$.
Since $f \in B$, $f(x) \to \infty$ as $x \to \infty$ by <1>1. <2>6. For any distinct $x_1, x_2 \in X$, there exists $n$ such that $x_1, x_2 \in C_n$ and $d(x_1, x_2) \ge \frac{1}{n}$.
Since $f \in U_{1/n}(C_n)$, $f(x_1) \neq f(x_2)$.
Thus $f$ is injective.
<2>7. By <1>2, $f$ is a homeomorphism of $X$ onto a closed subspace of $\mathbb{R}^{2m+1}$.
Q.E.D.
:::
