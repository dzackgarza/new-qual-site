---
schema: qual/card@1
id: E-A7HJX
kind: exercise
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

::: solution
**Goal:** Prove that if $f: G \to H$ is a surjective homomorphism and $\ker g = \langle\langle f(x_0) \rangle\rangle_H$, then $\ker(g \circ f)$ is the least normal subgroup $N = \langle\langle \ker f \cup \{x_0\} \rangle\rangle_G$.

<1>1. Inclusion $N \subseteq \ker(g \circ f)$:
    *Proof:*
    <2>1. $\ker(g \circ f) = \{x \in G \mid g(f(x)) = 1_K\} = f^{-1}(\ker g)$.
    <2>2. For any $k \in \ker f$, $(g \circ f)(k) = g(f(k)) = g(1_H) = 1_K$, so $\ker f \subseteq \ker(g \circ f)$.
    <2>3. For $x_0$, $(g \circ f)(x_0) = g(f(x_0)) = 1_K$ because $f(x_0) \in \ker g$, so $x_0 \in \ker(g \circ f)$.
    <2>4. Because $\ker(g \circ f)$ is the kernel of a homomorphism, it is a normal subgroup of $G$.
    <2>5. Since $N$ is defined as the least normal subgroup of $G$ containing $\ker f$ and $x_0$, we have $N \subseteq \ker(g \circ f)$.

<1>2. Normality of the image $f(N)$ in $H$:
    *Proof:*
    <2>1. Let $h \in H$ and $y \in f(N)$.
    <2>2. Since $f$ is surjective, choose $g \in G$ such that $f(g) = h$.
    <2>3. Choose $n \in N$ such that $f(n) = y$.
    <2>4. Then $h y h^{-1} = f(g) f(n) f(g)^{-1} = f(g n g^{-1})$.
    <2>5. Because $N \trianglelefteq G$, $g n g^{-1} \in N$, so $f(g n g^{-1}) \in f(N)$.
    <2>6. Thus $f(N)$ is a normal subgroup of $H$.

<1>3. Inclusion $\ker g \subseteq f(N)$:
    *Proof:*
    <2>1. Since $x_0 \in N$, $f(x_0) \in f(N)$.
    <2>2. By hypothesis, $\ker g$ is the least normal subgroup of $H$ containing $f(x_0)$.
    <2>3. Since $f(N)$ is a normal subgroup of $H$ containing $f(x_0)$, it follows that $\ker g \subseteq f(N)$.

<1>4. Inclusion $\ker(g \circ f) \subseteq N$:
    *Proof:*
    <2>1. Taking preimages under $f$ gives:
        $$\ker(g \circ f) = f^{-1}(\ker g) \subseteq f^{-1}(f(N)).$$
    <2>2. We claim $f^{-1}(f(N)) = N$:
        - We have $N \subseteq f^{-1}(f(N))$: for any $n \in N$, $f(n) \in f(N)$, so $n \in f^{-1}(f(N))$ by definition of the preimage.
        - If $x \in f^{-1}(f(N))$, then $f(x) = f(n)$ for some $n \in N$.
        - Then $f(x n^{-1}) = f(x) f(n)^{-1} = 1_H$, which means $x n^{-1} \in \ker f$.
        - Since $\ker f \subseteq N$, $x = (x n^{-1}) n \in N \cdot N = N$.
    <2>3. Thus $f^{-1}(f(N)) = N$, which proves $\ker(g \circ f) \subseteq N$.

<1>5. Conclusion:
    $\ker(g \circ f) = N$, so $\ker(g \circ f)$ is the least normal subgroup of $G$ containing $\ker f$ and $x_0$. Q.E.D.
:::
