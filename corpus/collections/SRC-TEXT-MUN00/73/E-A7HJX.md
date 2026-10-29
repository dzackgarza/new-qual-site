---
schema: qual/card@1
id: E-A7HJX
kind: problem
title: Kernels under surjective composites of homomorphisms
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Lemma.
Let $f: G \to H$ and $g: H \to K$ be homomorphisms; assume $f$ is surjective.
If $x_0 \in G$, and if $\ker g$ is the least normal subgroup of $H$ containing $f(x_0)$, then $\ker(g \circ f)$ is the least normal subgroup $N$ of $G$ containing $\ker f$ and $x_0$.

Proof.
Show that $f(N)$ is normal; conclude that $\ker(g \circ f) = f^{-1}(\ker g) \subset f^{-1}f(N) = N$.
:::

::: {.solution}
::: pf

::: {.pf-step #n-in-kernel}

$N \subseteq \ker(g \circ f)$.

::: pf-proof

::: pf-step

$\ker(g \circ f) = \{x \in G \mid g(f(x)) = 1_K\} = f^{-1}(\ker g)$.

:::

::: pf-step

For any $k \in \ker f$, $(g \circ f)(k) = g(f(k)) = g(1_H) = 1_K$, so $\ker f \subseteq \ker(g \circ f)$.

:::

::: pf-step

For $x_0$, $(g \circ f)(x_0) = g(f(x_0)) = 1_K$ because $f(x_0) \in \ker g$, so $x_0 \in \ker(g \circ f)$.

:::

::: pf-step

Because $\ker(g \circ f)$ is the kernel of a homomorphism, it is a normal subgroup of $G$.

:::

::: pf-step

Since $N$ is defined as the least normal subgroup of $G$ containing $\ker f$ and $x_0$, we have $N \subseteq \ker(g \circ f)$.

:::

:::

:::

::: {.pf-step #fn-normal}

The image $f(N)$ is a normal subgroup of $H$.

::: pf-proof

::: pf-step

Let $h \in H$ and $y \in f(N)$.

:::

::: pf-step

Since $f$ is surjective, choose $a \in G$ such that $f(a) = h$.

:::

::: pf-step

Choose $n \in N$ such that $f(n) = y$.

:::

::: pf-step

Then $h y h^{-1} = f(a) f(n) f(a)^{-1} = f(a n a^{-1})$.

:::

::: pf-step

Because $N \trianglelefteq G$, $a n a^{-1} \in N$, so $f(a n a^{-1}) \in f(N)$.

:::

::: pf-step

Thus $f(N)$ is a normal subgroup of $H$.

:::

:::

:::

::: {.pf-step #kerg-in-fn}

$\ker g \subseteq f(N)$.

::: pf-proof

::: pf-step

Since $x_0 \in N$, $f(x_0) \in f(N)$.

:::

::: pf-step

By hypothesis, $\ker g$ is the least normal subgroup of $H$ containing $f(x_0)$.

:::

::: pf-step

Since $f(N)$ is a normal subgroup of $H$ (step [](#fn-normal){.pf-ref}) containing $f(x_0)$, it follows that $\ker g \subseteq f(N)$.

:::

:::

:::

::: pf-step

$\ker(g \circ f) \subseteq N$, and hence $\ker(g \circ f) = N$.

::: pf-proof

::: {.pf-step #preimage-bound}

Taking preimages under $f$ of the inclusion in step [](#kerg-in-fn){.pf-ref} gives:
$$\ker(g \circ f) = f^{-1}(\ker g) \subseteq f^{-1}(f(N)).$$

:::

::: {.pf-step #preimage-image}

$f^{-1}(f(N)) = N$.

::: pf-proof

Clearly $N \subseteq f^{-1}(f(N))$.
Conversely, if $x \in f^{-1}(f(N))$, then $f(x) = f(n)$ for some $n \in N$, so $f(x n^{-1}) = 1_H$ and $x n^{-1} \in \ker f \subseteq N$; hence $x = (x n^{-1}) n \in N$.

:::

:::

::: pf-qed

Steps [](#preimage-bound){.pf-ref} and [](#preimage-image){.pf-ref} give $\ker(g \circ f) \subseteq N$, and step [](#n-in-kernel){.pf-ref} gives the reverse inclusion.

:::

:::

:::

:::

:::
