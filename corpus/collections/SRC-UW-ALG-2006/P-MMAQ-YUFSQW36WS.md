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

::: problem
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
<1>1. $G$ is the group of upper-triangular unipotent $3 \times 3$ matrices over $\mathbb{F}_p$, the Heisenberg group over $\mathbb{F}_p$.
Proof: the matrices $\begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix}$ form the Heisenberg group.

<1>2. $G$ is non-abelian.
Proof: e.g. $\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$ do not commute (their commutator is $\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \neq I$).

<1>3. Write $g = I + N$ where $N = \begin{pmatrix} 0 & a & b \\ 0 & 0 & c \\ 0 & 0 & 0 \end{pmatrix}$ is strictly upper-triangular, so $N^3 = 0$.
Proof: strictly upper-triangular $3 \times 3$ matrices are nilpotent of index $3$.

<1>4. $g^p = (I + N)^p = I + pN + \binom{p}{2}N^2 + \cdots$.
Proof: binomial theorem, and $N^3 = 0$ kills all higher terms.

<1>5. If $p$ is odd, then $p \equiv 0 \pmod p$ and $\binom{p}{2} = \frac{p(p-1)}{2} \equiv 0 \pmod p$ (since $p$ is odd, $p-1$ is even, so $\binom{p}{2}$ is divisible by $p$).
Proof: arithmetic in $\mathbb{F}_p$.

<1>6. Hence $g^p = I$ for all $g \in G$ when $p$ is odd.
Proof: <1>4 and <1>5 (all binomial coefficients $\binom{p}{k}$ for $1 \le k \le p-1$ are divisible by $p$).

<1>7. For $p = 2$, $G$ has order $2^3 = 8$.
Proof: there are $p^3 = 8$ choices of $(a, b, c) \in \mathbb{F}_2^3$.

<1>8. For $p = 2$, $G$ is non-abelian of order $8$, so it is either $D_8$ or the quaternion group $Q_8$.
Proof: <1>2, <1>7, and the given fact.

<1>9. $G$ has more than one element of order $2$ (e.g. $\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$ both have order $2$), whereas $Q_8$ has a unique element of order $2$.
Proof: in $Q_8$, only $-1$ has order $2$; in $G$, the two matrices above (and more) have order $2$.

<1>10. Hence $G \cong D_8$ (the dihedral group of order $8$).
Proof: <1>8 and <1>9.

<1>11. Q.E.D.
Proof: <1>2, <1>6, <1>10.
:::
