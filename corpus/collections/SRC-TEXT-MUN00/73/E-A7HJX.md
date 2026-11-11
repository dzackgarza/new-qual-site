---
schema: qual/card@1
id: E-A7HJX
kind: problem
title: Kernels under a surjection and a quotient
classification:
  areas:
  - topology
  topics:
  - Free Groups
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §73 Exercise 3, printed p. 445, the lemma the proof of Exercise 2 uses for its induction. No
    complete published solution located; the searches are listed in the COMPLAINTS.md entry for §61--§73 of
    SRC-TEXT-MUN00, and Murayama's set skips it. The two steps the printed proof asks for are steps 1 and 2
    below; the reverse inclusion N contained in ker(g o f) is step 1's second half, which the printed outline
    leaves implicit. Checked against the definition of the least normal subgroup (printed p. 418) and Lemma
    68.9 (printed p. 420).
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

::: pf-step

$f(N)$ is normal in $H$.

::: pf-proof

For $n\in N$ and $h\in H$ write $h=f(\tilde h)$, possible since $f$ is onto. Then $h f(n)h^{-1}=f(\tilde h n \tilde h^{-1})\in f(N)$ because $N$ is normal in $G$. So $f(N)$ is a normal subgroup of $H$.

:::

:::

::: pf-step

$N\subseteq\ker(g\circ f)$.

::: pf-proof

Both $\ker f\subseteq\ker(gf)$ (as $f$ kills it) and $x_0\in\ker(gf)$, because $f(x_0)\in\ker g$ by hypothesis. Since $\ker(gf)$ is a normal subgroup of $G$ containing those two, it contains the least such group $N$.

:::

:::

::: pf-step

$\ker(g\circ f)=N$.

::: pf-proof

$\ker(gf)=f^{-1}(\ker g)$. Since $\ker g$ is the least normal subgroup of $H$ containing $f(x_0)$, it is contained in every normal subgroup of $H$ containing $f(x_0)$; by step 1, $f(N)$ is normal and contains $f(x_0)$, so $\ker g\subseteq f(N)$. Hence $\ker(gf)\subseteq f^{-1}f(N)=\theset{g'\in G: f(g')\in f(N)}=N\cdot\ker f\subseteq N$, the last inclusion because $\ker f\subseteq N$. With step 2, $\ker(gf)=N$.

:::

:::

::: pf-qed

$\ker(g\circ f)$ is the least normal subgroup of $G$ containing $\ker f$ and $x_0$.

:::

:::
:::
