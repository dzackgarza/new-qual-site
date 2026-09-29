---
schema: qual/card@1
id: P-APAS26E
kind: problem
title: A faithful state yields a faithful tracial state
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $\mathcal{A}$ be an algebra which admits a faithful state $\sigma \colon \mathcal{A} \to \mathbb{C}$.
Prove that $\mathcal{A}$ admits a faithful tracial state $\tau \colon \mathcal{A} \to \mathbb{C}$.

Note: On this exam, an algebra is a finite-dimensional complex vector space equipped with an associative, bilinear, unital multiplication and an antilinear, antimultiplicative, involutive conjugation.
:::

::: {.solution}

::: pf

::: pf-step
Structure of the finite-dimensional $*$-algebra $\mathcal{A}$:

::: pf-proof

::: pf-step
The existence of a faithful state $\sigma$ defines an inner product on $\mathcal{A}$ by $\langle x, y \rangle = \sigma(y^* x)$, which satisfies $\langle x, x \rangle = \sigma(x^* x) > 0$ for all $x \neq 0$.

::: pf-proof
definition of a faithful state.
:::

:::

::: pf-step
Under this inner product, $\mathcal{A}$ has no non-zero nilpotent ideals (if $x \in \mathcal{A}$ with $x^2 = 0$ and $x^* x = 0$, faithfulness implies $x = 0$), so $\mathcal{A}$ is a finite-dimensional semisimple complex $*$-algebra ($C^*$-algebra).

::: pf-proof
GNS construction / finite-dimensional $C^*$-algebra theory.
:::

:::

::: pf-step
By the Artin–Wedderburn theorem for finite-dimensional $C^*$-algebras, $\mathcal{A}$ is $*$-isomorphic to a finite direct sum of full matrix algebras:
\[
\mathcal{A} \cong \bigoplus_{k=1}^m M_{n_k}(\mathbb{C}).
\]

::: pf-proof
Artin–Wedderburn theorem for finite-dimensional $C^*$-algebras.
:::

:::

:::

:::

::: {.pf-step #s2}
Construct the candidate tracial state $\tau$:

::: pf-proof

::: pf-step
Under the decomposition $a = (a_1, \dots, a_m) \in \bigoplus_{k=1}^m M_{n_k}(\mathbb{C})$, define:
\[
\tau(a) = \frac{1}{\sum_{k=1}^m n_k} \sum_{k=1}^m \operatorname{Tr}(a_k),
\]
where $\operatorname{Tr}$ is the standard matrix trace on $M_{n_k}(\mathbb{C})$.

::: pf-proof
definition of $\tau$.
:::

:::

::: pf-step
**Unital:** The unit element of $\mathcal{A}$ is $1 = (I_{n_1}, \dots, I_{n_m})$.
\[
\tau(1) = \frac{1}{\sum_{k=1}^m n_k} \sum_{k=1}^m \operatorname{Tr}(I_{n_k}) = \frac{\sum_{k=1}^m n_k}{\sum_{k=1}^m n_k} = 1.
\]

::: pf-proof
$\operatorname{Tr}(I_{n_k}) = n_k$.
:::

:::

::: pf-step
**Tracial property:** For any $a, b \in \mathcal{A}$, the componentwise products are $(ab)_k = a_k b_k$ and $(ba)_k = b_k a_k$.
Since the matrix trace is cyclic ($\operatorname{Tr}(a_k b_k) = \operatorname{Tr}(b_k a_k)$):
\[
\tau(ab) = \frac{1}{\sum n_k} \sum_{k=1}^m \operatorname{Tr}(a_k b_k) = \frac{1}{\sum n_k} \sum_{k=1}^m \operatorname{Tr}(b_k a_k) = \tau(ba).
\]

::: pf-proof
cyclicity of the matrix trace on $M_{n_k}(\mathbb{C})$.
:::

:::

::: pf-step
**Positivity and Faithfulness:** For any $a \in \mathcal{A}$, $(a^* a)_k = a_k^* a_k$.
\[
\tau(a^* a) = \frac{1}{\sum n_k} \sum_{k=1}^m \operatorname{Tr}(a_k^* a_k) = \frac{1}{\sum n_k} \sum_{k=1}^m \|a_k\|_{HS}^2 \ge 0,
\]
where $\|a_k\|_{HS}^2 = \sum_{i,j} |(a_k)_{ij}|^2$ is the Frobenius / Hilbert–Schmidt norm.

::: pf-proof
$\operatorname{Tr}(M^* M) = \sum |M_{ij}|^2 \ge 0$.
:::

:::

::: pf-step
Furthermore, $\tau(a^* a) = 0 \iff \|a_k\|_{HS}^2 = 0$ for all $k=1, \dots, m \iff a_k = 0$ for all $k \iff a = 0$.

::: pf-proof
sum of non-negative terms vanishes if and only if each term vanishes.
:::

:::

:::

:::

::: pf-step
Conclusion: $\tau$ is a faithful tracial state on $\mathcal{A}$.

::: pf-proof
step [](#s2){.pf-ref}.
:::

:::

:::
:::
