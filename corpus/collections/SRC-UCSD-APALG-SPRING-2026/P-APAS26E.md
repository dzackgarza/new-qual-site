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

::: problem
Let $\mathcal{A}$ be an algebra which admits a faithful state $\sigma \colon \mathcal{A} \to \mathbb{C}$.
Prove that $\mathcal{A}$ admits a faithful tracial state $\tau \colon \mathcal{A} \to \mathbb{C}$.

Note: On this exam, an algebra is a finite-dimensional complex vector space equipped with an associative, bilinear, unital multiplication and an antilinear, antimultiplicative, involutive conjugation.
:::

::: {.solution}
<1>1. Structure of the finite-dimensional $*$-algebra $\mathcal{A}$: <2>1. The existence of a faithful state $\sigma$ defines an inner product on $\mathcal{A}$ by $\langle x, y \rangle = \sigma(y^* x)$, which satisfies $\langle x, x \rangle = \sigma(x^* x) > 0$ for all $x \neq 0$.
Proof: definition of a faithful state.
<2>2. Under this inner product, $\mathcal{A}$ has no non-zero nilpotent ideals (if $x \in \mathcal{A}$ with $x^2 = 0$ and $x^* x = 0$, faithfulness implies $x = 0$), so $\mathcal{A}$ is a finite-dimensional semisimple complex $*$-algebra ($C^*$-algebra).
Proof: GNS construction / finite-dimensional $C^*$-algebra theory.
<2>3. By the Artin–Wedderburn theorem for finite-dimensional $C^*$-algebras, $\mathcal{A}$ is $*$-isomorphic to a finite direct sum of full matrix algebras:
\[
\mathcal{A} \cong \bigoplus_{k=1}^m M_{n_k}(\mathbb{C}).
\]
Proof: Artin–Wedderburn theorem for finite-dimensional $C^*$-algebras.

<1>2. Construct the candidate tracial state $\tau$: <2>1. Under the decomposition $a = (a_1, \dots, a_m) \in \bigoplus_{k=1}^m M_{n_k}(\mathbb{C})$, define:
\[
\tau(a) = \frac{1}{\sum_{k=1}^m n_k} \sum_{k=1}^m \operatorname{Tr}(a_k),
\]
where $\operatorname{Tr}$ is the standard matrix trace on $M_{n_k}(\mathbb{C})$.
Proof: definition of $\tau$.
<2>2. **Unital:** The unit element of $\mathcal{A}$ is $1 = (I_{n_1}, \dots, I_{n_m})$.
\[
\tau(1) = \frac{1}{\sum_{k=1}^m n_k} \sum_{k=1}^m \operatorname{Tr}(I_{n_k}) = \frac{\sum_{k=1}^m n_k}{\sum_{k=1}^m n_k} = 1.
\]
Proof: $\operatorname{Tr}(I_{n_k}) = n_k$.
<2>3. **Tracial property:** For any $a, b \in \mathcal{A}$, the componentwise products are $(ab)_k = a_k b_k$ and $(ba)_k = b_k a_k$.
Since the matrix trace is cyclic ($\operatorname{Tr}(a_k b_k) = \operatorname{Tr}(b_k a_k)$):
\[
\tau(ab) = \frac{1}{\sum n_k} \sum_{k=1}^m \operatorname{Tr}(a_k b_k) = \frac{1}{\sum n_k} \sum_{k=1}^m \operatorname{Tr}(b_k a_k) = \tau(ba).
\]
Proof: cyclicity of the matrix trace on $M_{n_k}(\mathbb{C})$.
<2>4. **Positivity and Faithfulness:** For any $a \in \mathcal{A}$, $(a^* a)_k = a_k^* a_k$.
\[
\tau(a^* a) = \frac{1}{\sum n_k} \sum_{k=1}^m \operatorname{Tr}(a_k^* a_k) = \frac{1}{\sum n_k} \sum_{k=1}^m \|a_k\|_{HS}^2 \ge 0,
\]
where $\|a_k\|_{HS}^2 = \sum_{i,j} |(a_k)_{ij}|^2$ is the Frobenius / Hilbert–Schmidt norm.
Proof: $\operatorname{Tr}(M^* M) = \sum |M_{ij}|^2 \ge 0$.
<2>5. Furthermore, $\tau(a^* a) = 0 \iff \|a_k\|_{HS}^2 = 0$ for all $k=1, \dots, m \iff a_k = 0$ for all $k \iff a = 0$.
Proof: sum of non-negative terms vanishes if and only if each term vanishes.

<1>3. Conclusion: $\tau$ is a faithful tracial state on $\mathcal{A}$.
Q.E.D. Proof: <1>2.
:::
