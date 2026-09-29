---
schema: qual/card@1
id: P-MMAQ-YUFSQW36WS
kind: problem
title: The group of upper-triangular unipotent $3\times 3$ matrices over $\mathbb{F}_p$
  is nonabelian, $g^p=I$ for $p$ odd, and $D_8$ versus the quaternionic group for
  $p=2$
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Let $G$ be the group of matrices of the form `\begin{align*}
\begin{pmatrix}
  1 & a & b\\
  0 & 1 & c\\
  0 & 0 & 1
\end{pmatrix}
.\end{align*}`{=tex}

with entries in the finite field $\mathbb F_p$ of $p$ element, where $p$ is a prime.

- Prove that $G$ is non-abelian.

- Suppose $p$ is odd.
  Prove that $g^p=I_3$ for all $g\in G$.

- Suppose that $p=2$.
  It is known that there are exactly two non-abelian groups of order 8, up to isomorphism: the dihedral group $D_8$ and the quaternionic group.
  Assuming this fact without proof, determine which of these groups $G$ is isomorphic to.
:::

::: {.solution}

::: pf

::: pf-step

$G$ is the group of upper-triangular unipotent $3 \times 3$ matrices over $\mathbb{F}_p$, the Heisenberg group over $\mathbb{F}_p$.

::: pf-proof

the matrices $\begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix}$ form the Heisenberg group.

:::

:::

::: {.pf-step #s2}

$G$ is non-abelian.

::: pf-proof

e.g. $\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$ do not commute (their commutator is $\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \neq I$).

:::

:::

::: pf-step

Write $g = I + N$ where $N = \begin{pmatrix} 0 & a & b \\ 0 & 0 & c \\ 0 & 0 & 0 \end{pmatrix}$ is strictly upper-triangular, so $N^3 = 0$.

::: pf-proof

strictly upper-triangular $3 \times 3$ matrices are nilpotent of index $3$.

:::

:::

::: {.pf-step #s4}

$g^p = (I + N)^p = I + pN + \binom{p}{2}N^2 + \cdots$.

::: pf-proof

binomial theorem, and $N^3 = 0$ kills all higher terms.

:::

:::

::: {.pf-step #s5}

If $p$ is odd, then $p \equiv 0 \pmod p$ and $\binom{p}{2} = \frac{p(p-1)}{2} \equiv 0 \pmod p$ (since $p$ is odd, $p-1$ is even, so $\binom{p}{2}$ is divisible by $p$).

::: pf-proof

arithmetic in $\mathbb{F}_p$.

:::

:::

::: {.pf-step #s6}

Hence $g^p = I$ for all $g \in G$ when $p$ is odd.

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} (all binomial coefficients $\binom{p}{k}$ for $1 \le k \le p-1$ are divisible by $p$).

:::

:::

::: {.pf-step #s7}

For $p = 2$, $G$ has order $2^3 = 8$.

::: pf-proof

there are $p^3 = 8$ choices of $(a, b, c) \in \mathbb{F}_2^3$.

:::

:::

::: {.pf-step #s8}

For $p = 2$, $G$ is non-abelian of order $8$, so it is either $D_8$ or the quaternion group $Q_8$.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s7){.pf-ref}, and the given fact.

:::

:::

::: {.pf-step #s9}

$G$ has more than one element of order $2$ (e.g. $\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$ both have order $2$), whereas $Q_8$ has a unique element of order $2$.

::: pf-proof

in $Q_8$, only $-1$ has order $2$; in $G$, the two matrices above (and more) have order $2$.

:::

:::

::: {.pf-step #s10}

Hence $G \cong D_8$ (the dihedral group of order $8$).

::: pf-proof

Steps [](#s8){.pf-ref} and [](#s9){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s6){.pf-ref} and [](#s10){.pf-ref}.

:::

:::

:::
