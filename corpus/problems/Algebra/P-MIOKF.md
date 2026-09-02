---
schema: qual/card@1
id: P-MIOKF
kind: problem
title: Proper subfields of $\CC$ isomorphic to $\CC$
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Transcendence
  - Automorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Can it happen that a proper subfield of $\mathbb{C}$ is isomorphic to $\mathbb{C}$?
How?
:::

::: solution
**Goal:** Prove that $\mathbb{C}$ has proper subfields isomorphic to $\mathbb{C}$, and construct an explicit example using transcendence bases.

<1>1. Answer: **Yes**, it can happen.
An isomorphism $\phi: \mathbb{C} \to K$ onto a subfield $K \subsetneq \mathbb{C}$ is equivalent to a non-surjective field endomorphism (embedding) of $\mathbb{C}$ into itself.

<1>2. Steinitz's Theorem on Algebraically Closed Fields: *Proof:* <2>1. By Steinitz's classification of algebraically closed fields, an algebraically closed field of characteristic 0 is completely determined up to isomorphism by its **transcendence degree** over $\mathbb{Q}$.
<2>2. The cardinality of $\mathbb{C}$ is $|\mathbb{C}| = 2^{\aleph_0} = \mathfrak{c}$ (the continuum).
<2>3. Because any field extension of transcendence degree $\kappa$ has cardinality $\max(\aleph_0, \kappa)$, the transcendence degree of $\mathbb{C}$ over $\mathbb{Q}$ is: $$\operatorname{tr.deg}(\mathbb{C}/\mathbb{Q}) = 2^{\aleph_0} = \mathfrak{c}.$$

<1>3. Explicit Construction of a Proper Subfield Isomorphic to $\mathbb{C}$: *Proof:* <2>1. By Zorn's Lemma (Axiom of Choice), choose a transcendence basis $B$ for $\mathbb{C}$ over $\mathbb{Q}$.
<2>2. The cardinality of $B$ is $|B| = \mathfrak{c}$.
<2>3. Since $B$ is an infinite set, we can choose a proper subset $B_0 \subsetneq B$ such that $|B_0| = |B| = \mathfrak{c}$ (for example, pick a single element $t \in B$ and let $B_0 = B \setminus \{t\}$). <2>4. Let $K = \overline{\mathbb{Q}(B_0)}$ be the algebraic closure of the purely transcendental extension $\mathbb{Q}(B_0)$ inside $\mathbb{C}$.
<2>5. **$K$ is a proper subfield of $\mathbb{C}$ ($K \ne \mathbb{C}$):** - The element $t \in B \setminus B_0$ is algebraically independent over $\mathbb{Q}(B_0)$.

- Therefore, $t$ is not algebraic over $\mathbb{Q}(B_0)$, which means $t \notin K$.

- Thus $K \subsetneq \mathbb{C}$.
  <2>6. **$K \cong \mathbb{C}$:** - $K$ is an algebraically closed field of characteristic 0. - The transcendence degree of $K$ over $\mathbb{Q}$ is $\operatorname{tr.deg}(K/\mathbb{Q}) = |B_0| = \mathfrak{c} = \operatorname{tr.deg}(\mathbb{C}/\mathbb{Q})$.

- By Steinitz's Theorem, any two algebraically closed fields of the same characteristic and same infinite transcendence degree are isomorphic.

- Therefore, $K \cong \mathbb{C}$.

<1>4. Endomorphism perspective: *Proof:* <2>1. Choose any bijection $f: B \to B_0 \subsetneq B$.
<2>2. $f$ extends uniquely to a field isomorphism $\tilde{f}: \mathbb{Q}(B) \to \mathbb{Q}(B_0)$.
<2>3. By the extension theorem for algebraically closed fields, $\tilde{f}$ extends to an isomorphism of their algebraic closures: $$\Phi: \overline{\mathbb{Q}(B)} = \mathbb{C} \xrightarrow{\cong} \overline{\mathbb{Q}(B_0)} = K \subsetneq \mathbb{C}.$$ <2>4. $\Phi$ is an injective, non-surjective field endomorphism of $\mathbb{C}$.

<1>5. Conclusion: Yes; the algebraic closure $\overline{\mathbb{Q}(B \setminus \{t\})}$ of a transcendence basis minus one element has transcendence degree $\mathfrak{c}$, so it is a proper subfield isomorphic to $\mathbb{C}$.
Q.E.D.
:::
