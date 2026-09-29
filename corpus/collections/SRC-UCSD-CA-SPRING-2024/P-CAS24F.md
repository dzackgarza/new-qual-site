---
schema: qual/card@1
id: P-CAS24F
kind: problem
title: 'Iterates of a holomorphic self-map with $f(0)=0$ and $|f''(0)|<1$ tend to $0$'
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $U \subset \mathbb{C}$ be a bounded connected open set containing $0$, and $f : U \to U$ a holomorphic function which satisfies $f(0) = 0$ and $|f'(0)| < 1$.
Write
\[
f^{(n)} = \underbrace{f \circ f \circ \cdots \circ f}_{n\text{ times}}.
\]

(i) Show that there is a neighborhood $V$ of $0$ such that the sequence $f^{(n)}$ converges to $0$ locally uniformly on $V$.

Hint: $|f(z)| \le M|z|$ for a constant $M < 1$, for $|z|$ small.

(ii) Show that the sequence $f^{(n)}$ converges locally uniformly to $0$ on $U$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Part (i): Local uniform convergence on a neighborhood of $0$:

::: pf-proof

::: pf-step

Since $f(0) = 0$, the function $h(z) = \frac{f(z)}{z}$ has a removable singularity at $z = 0$ with $h(0) = f'(0)$.
Thus $\lim_{z \to 0} \left| \frac{f(z)}{z} \right| = |f'(0)| < 1$.

::: pf-proof

Taylor expansion of $f$ around $0$.

:::

:::

::: pf-step

Let $\lambda = |f'(0)| < 1$ and choose $M$ such that $\lambda < M < 1$.
There exists $r > 0$ such that the disk $V = B(0, r) \subset U$ satisfies:
\[
|f(z)| \le M |z| \quad \text{for all } z \in V.
\]

::: pf-proof

definition of limit.

:::

:::

::: pf-step

Since $M < 1$, for any $z \in V$ we have $|f(z)| \le M |z| < |z| < r$, so $f(V) \subset V$.
By induction, for every $n \ge 1$ and $z \in V$:
\[
|f^{(n)}(z)| \le M^n |z| \le M^n r.
\]

::: pf-proof

induction on $n$.

:::

:::

::: pf-step

As $n \to \infty$, $M^n \to 0$. Thus:
\[
\sup_{z \in V} |f^{(n)}(z)| \le M^n r \to 0.
\]
Hence $f^{(n)}$ converges uniformly to $0$ on $V$.

::: pf-proof

uniform bound tending to zero.

:::

:::

:::

:::

::: {.pf-step #s2}

Part (ii): Global locally uniform convergence on $U$:

::: pf-proof

::: pf-step

Since $U$ is bounded, there exists $R > 0$ such that $|z| \le R$ for all $z \in U$.
Because $f(U) \subseteq U$, every iterate satisfies $f^{(n)}(U) \subseteq U$, so:
\[
|f^{(n)}(z)| \le R \quad \text{for all } z \in U \text{ and } n \ge 1.
\]
Thus the sequence of iterates $(f^{(n)})_{n=1}^\infty$ is uniformly bounded on $U$.

::: pf-proof

invariance of $U$ under iteration and boundedness of $U$.

:::

:::

::: pf-step

By Montel’s Theorem, $(f^{(n)})$ is a normal family on $U$.
Let $(f^{(n_k)})$ be any subsequence that converges locally uniformly on $U$ to a holomorphic function $g: U \to \mathbb{C}$.

::: pf-proof

Montel's Theorem.

:::

:::

::: pf-step

By Part (i), on the neighborhood $V \subset U$, $f^{(n_k)} \to 0$ uniformly, so $g(z) = 0$ for all $z \in V$.

::: pf-proof

Part (i).

:::

:::

::: pf-step

Since $U$ is connected and $V$ is a non-empty open subset of $U$, the Identity Theorem for holomorphic functions implies that $g(z) \equiv 0$ on all of $U$.

::: pf-proof

Identity Theorem for connected domains.

:::

:::

::: pf-step

Since every convergent subsequence of $(f^{(n)})$ converges to the unique limit function $0$, the full sequence $f^{(n)}$ converges locally uniformly to $0$ on $U$.

::: pf-proof

compactness principle for normal families.

:::

:::

:::

:::

::: pf-step

Conclusion:
$f^{(n)} \to 0$ locally uniformly on $U$. Q.E.D.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

:::

:::
