---
schema: qual/card@1
id: E-3C4WF
kind: problem
title: The Hausdorff metric on closed bounded subsets
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $(X, d)$ be a metric space.
If $A \subset X$ and $\epsilon > 0$, let $U(A, \epsilon)$ be the $\epsilon$-neighborhood of $A$.
Let $\mathcal{H}$ be the collection of all (nonempty) closed, bounded subsets of $X$.
If $A, B \in \mathcal{H}$, define

$$
D(A, B) = \inf\ts{\epsilon \mid A \subset U(B, \epsilon) \text{ and } B \subset U(A, \epsilon)}.
$$

(a) Show that $D$ is a metric on $\mathcal{H}$; it is called the Hausdorff metric.

(b) Show that if $(X, d)$ is complete, so is $(\mathcal{H}, D)$.
[Hint: Let $A_n$ be a Cauchy sequence in $\mathcal{H}$; by passing to a subsequence, assume $D(A_n, A_{n+1}) < 1/2^n$. Define $A$ to be the set of all points $x$ that are the limits of sequences $x_1, x_2, \ldots$ such that $x_i \in A_i$ for each $i$ and $d(x_i, x_{i+1}) < 1/2^i$. Show $A_n \to \overline{A}$.]

(c) Show that if $(X, d)$ is totally bounded, so is $(\mathcal{H}, D)$.
[Hint: Given $\epsilon$, choose $\delta < \epsilon$ and let $S$ be a finite subset of $X$ such that the collection $\ts{B_d(x, \delta) \mid x \in S}$ covers $X$. Let $\mathcal{A}$ be the collection of all nonempty subsets of $S$; show that $\ts{B_D(A, \epsilon) \mid A \in \mathcal{A}}$ covers $\mathcal{H}$.]

(d) Theorem.
If $X$ is compact in the metric $d$, then the space $\mathcal{H}$ is compact in the Hausdorff metric $D$.
:::

::: {.solution}

::: pf

::: pf-step

Part (a): $D$ is a well-defined metric on $\mathcal{H}$.
    *Proof:*

::: pf-proof

::: pf-step

**Finiteness:** For bounded sets $A, B \in \mathcal{H}$, picking $a_0 \in A, b_0 \in B$ gives $d(a, b) \le \operatorname{diam}(A) + d(a_0, b_0) + \operatorname{diam}(B) < \infty$, so $D(A, B) < \infty$.

:::

::: pf-step

**Non-negativity and Identity of Indiscernibles:** $D(A, B) \ge 0$ because it is the infimum of a set of non-negative real numbers (each $\varepsilon$ in the defining set is $\ge 0$).
        $$D(A, B) = 0 \iff \forall \varepsilon > 0, A \subseteq U(B, \varepsilon) \text{ and } B \subseteq U(A, \varepsilon) \iff A \subseteq \overline{B} = B \text{ and } B \subseteq \overline{A} = A \iff A = B.$$

:::

::: pf-step

**Symmetry:** $D(A, B) = D(B, A)$ by the symmetric definition.

:::

::: pf-step

**Triangle inequality:** If $A \subseteq U(B, \varepsilon_1)$ and $B \subseteq U(C, \varepsilon_2)$, then for any $a \in A$, there exists $b \in B$ with $d(a, b) < \varepsilon_1$, and there exists $c \in C$ with $d(b, c) < \varepsilon_2$. Then $d(a, c) \le d(a, b) + d(b, c) < \varepsilon_1 + \varepsilon_2$, so $A \subseteq U(C, \varepsilon_1 + \varepsilon_2)$. By symmetry, $C \subseteq U(A, \varepsilon_1 + \varepsilon_2)$. Taking infimums over $\varepsilon_1, \varepsilon_2$ yields $D(A, C) \le D(A, B) + D(B, C)$.

:::

:::

:::

::: {.pf-step #s2}

Part (b): Completeness of $(\mathcal{H}, D)$ when $(X, d)$ is complete.
    *Proof:*

::: pf-proof

::: {.pf-step #s2-1}

Let $(A_n)$ be a Cauchy sequence in $(\mathcal{H}, D)$. Pass to a subsequence (still denoted $A_n$) satisfying $D(A_n, A_{n+1}) < 2^{-n}$ for all $n \ge 1$.

:::

::: pf-step

Define $A_\infty$ to be the set of all limits $\lim_{n \to \infty} x_n$ of sequences $(x_n)$ such that $x_n \in A_n$ and $d(x_n, x_{n+1}) < 2^{-n}$ for all $n$.

:::

::: pf-step

Since $(X, d)$ is complete and $d(x_n, x_{n+p}) < \sum_{k=n}^{n+p-1} 2^{-k} < 2^{-(n-1)}$, every such sequence is Cauchy, so the limit $x \in X$ exists.

:::

::: pf-step

Let $A = \overline{A_\infty}$. Then $A \in \mathcal{H}$ is closed and bounded.

:::

::: pf-step

For any $x = \lim x_k \in A_\infty$, $d(x_n, x) \le 2^{-(n-1)}$, which implies $x \in \overline{U(A_n, 2^{-(n-1)})} \subseteq U(A_n, 2^{-(n-2)})$, so $A \subseteq U(A_n, 2^{-(n-2)})$.

:::

::: pf-step

Conversely, given $y_n \in A_n$, inductively choose $y_{k+1} \in A_{k+1}$ with $d(y_k, y_{k+1}) < 2^{-k}$ for all $k \ge n$, and $y_k \in A_k$ with $d(y_k, y_{k+1}) < 2^{-k}$ for $k = n-1, \ldots, 1$; both choices exist because $D(A_k, A_{k+1}) < 2^{-k}$. The limit $y = \lim y_k \in A_\infty \subseteq A$ satisfies $d(y_n, y) \le 2^{-(n-1)}$, so $A_n \subseteq U(A, 2^{-(n-1)})$.

:::

::: pf-step

Thus $D(A_n, A) \le 2^{-(n-2)} \to 0$ as $n \to \infty$, so the subsequence of step [](#s2-1){.pf-ref} converges to $A$. A Cauchy sequence with a convergent subsequence converges to the same limit, so the original sequence converges to $A$, and $(\mathcal{H}, D)$ is complete.

:::

:::

:::

::: {.pf-step #s3}

Part (c): Total boundedness of $(\mathcal{H}, D)$ when $(X, d)$ is totally bounded.
    *Proof:*

::: pf-proof

::: pf-step

Given $\varepsilon > 0$, choose $\delta = \frac{\varepsilon}{2}$.

:::

::: pf-step

Since $(X, d)$ is totally bounded, there exists a finite subset $S \subset X$ such that $\{B_d(s, \delta)\}_{s \in S}$ covers $X$.

:::

::: pf-step

Let $\mathcal{A} = \mathcal{P}(S) \setminus \{\emptyset\}$ be the finite collection of all non-empty subsets of $S$.

:::

::: pf-step

For any $A \in \mathcal{H}$, define $A_S = \{s \in S : B_d(s, \delta) \cap A \neq \emptyset\} \in \mathcal{A}$.

:::

::: pf-step

For any $a \in A$, there is $s \in S$ with $d(a, s) < \delta$, which forces $s \in A_S$, so $A \subseteq U(A_S, \delta)$.

:::

::: pf-step

For any $s \in A_S$, there is $a \in A$ with $d(s, a) < \delta$, so $A_S \subseteq U(A, \delta)$.

:::

::: pf-step

Thus $D(A, A_S) \le \delta < \varepsilon$, so $\{B_D(A', \varepsilon) : A' \in \mathcal{A}\}$ is a finite cover of $\mathcal{H}$ by $\varepsilon$-balls.

:::

::: pf-step

Hence $(\mathcal{H}, D)$ is totally bounded.

:::

:::

:::

::: pf-step

Part (d): Compactness of $(\mathcal{H}, D)$ when $(X, d)$ is compact.
    *Proof:*

::: pf-proof

::: pf-step

A metric space is compact if and only if it is complete and totally bounded.

:::

::: pf-step

Since $X$ is compact, $(X, d)$ is complete and totally bounded.

:::

::: pf-step

By step [](#s2){.pf-ref}, $(\mathcal{H}, D)$ is complete.

:::

::: pf-step

By step [](#s3){.pf-ref}, $(\mathcal{H}, D)$ is totally bounded.

:::

::: pf-step

Therefore $(\mathcal{H}, D)$ is compact. Q.E.D.

:::

:::

:::

:::

:::
