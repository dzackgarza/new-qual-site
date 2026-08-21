---
schema: qual/card@1
id: P-P47SB
kind: problem
title: $|f(0)|\le|a|^2$ for holomorphic $f:\DD\to\DD$ vanishing at $\pm a$, and the
  equality case
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Schwarz Lemma
  - Zeros
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Let $\mathbb{D}:=\{z:|z|<1\}$ denote the open unit disk. Suppose that $f(z): \mathbb{D} \rightarrow \mathbb{D}$ is holomorphic, and that there exists $a \in \mathbb{D} \backslash\{0\}$ such that $f(a)=f(-a)=0$.

- Prove that $|f(0)| \leq|a|^{2}$.

- What can you conclude when $|f(0)|=|a|^{2} ?$

:::

:::{.solution}
**Part 1**:

Write $\psi_a(z) \da {a-z\over 1-\bar a z}$ for the Blaschke factor of $a$, and define
\[
g(z) \da {f(z) \over \psi_a(z) \psi_{-a}(z)}
.\]

:::{.claim}
$\abs{g(z)}\leq 1$ on $\DD$.
:::

:::{.proof title="of claim"}
$\abs{\psi_a(z)} = 1$ on $\bd \DD$, so $\lim_{r\to 1}\psi_a(re^{it}) = 1$ for any fixed $t$.
Then for any $f$ with $\abs{f} \leq 1$ in $\DD$,
\[
\abs{f(re^{it} ) \over \psi_a(re^{it} ) } 
\leq {1\over \psi_a(re^{it})} 
\leq {1\over \sup_{t} \psi_a(re^{it}) }
\convergesto{r\to 1} 1
.\]
So apply this to $f=g$ and $f={g\over \psi_a}$ to get it for ${f\over \psi_a \psi_{-a}}.$

:::

In particular, $\abs{g(0)} \leq 1$, so
\[
1\geq \abs{g(0)} = {\abs{f(0)} \over \abs{B_a(0)} \cdot \abs{B_{-a}(0)}}
= {\abs{f(0)} \over \abs{a}^2} \implies \abs{a}^2 \geq \abs{f(0)}
.\]

**Part 2**:
Applying Schwarz-Pick:
\[
\abs{f'(0)} \leq {1 - \abs{f(0)}^2 \over 1 - \abs{0}^2 } = 1-\abs{a}^2 < 1
,\]
using that $a\neq 0$, so $f$ is a contraction.

> Can write $f_e(z) \da {f(a) + f(-a) \over 2}$ to write $f_e(z) = g(z^2)$.
  Compose with some $\psi_a$ to get $0\to 0$ and apply Schwarz -- unclear how to unwind what happens in the case of equality though.

:::
