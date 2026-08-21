---
schema: qual/card@1
id: P-AMD-6QDQY5HT
kind: problem
title: $\widetilde{H}_*(X \cup CA) \cong \widetilde{H}_*(X, A)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
solved: true
---

::: {.problem}
Let $CA$ be the cone on $A$, show that $\tilde H_*(X \union CA) \cong \tilde H_*(X, A)$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $(X, A)$ be a topological pair.
Let $CA = (A \times [0, 1]) / (A \times \{0\})$ be the cone on $A$, attached to $X$ along $A \times \{1\} \equiv A \subseteq X$, so $X \cup CA = X \cup_A CA$.
Prove that $\widetilde{H}_n(X \cup CA) \cong H_n(X, A)$ for all $n \ge 0$.

<1>1. Apply the long exact sequence of the pair $(X \cup CA, CA)$.
<2>1. For the pair $(Y, B) = (X \cup CA, CA)$, the long exact sequence in reduced homology is: $$\cdots \to \widetilde{H}_n(CA) \xrightarrow{i_*} \widetilde{H}_n(X \cup CA) \xrightarrow{j_*} H_n(X \cup CA, CA) \xrightarrow{\partial} \widetilde{H}_{n-1}(CA) \to \cdots$$ <2>2. The cone $CA$ is contractible to the cone vertex $v = [A \times \{0\}]$ via $H([(a, t)], s) = [(a, (1-s)t)]$.
<2>3. Since $CA$ is contractible, its reduced homology vanishes in all degrees: $\widetilde{H}_n(CA) = 0$ for all $n \ge 0$.
<2>4. The exact sequence becomes $0 \to \widetilde{H}_n(X \cup CA) \xrightarrow{j_*} H_n(X \cup CA, CA) \to 0$, which gives an isomorphism: $$j_* \colon \widetilde{H}_n(X \cup CA) \xrightarrow{\cong} H_n(X \cup CA, CA) \quad \text{for all } n \ge 0.$$ <2>5. Proof: Exactness of the pair sequence with vanishing end groups.
Q.E.D.

<1>2. Apply excision to relate $H_n(X \cup CA, CA)$ to $H_n(X, A)$.
<2>1. Let $v = [A \times \{0\}] \in CA$ be the cone vertex, and let $U = [A \times [0, 1/2)) \subset CA$ be the open cone neighborhood of $v$.
<2>2. The closure $\overline{U} = [A \times [0, 1/2]]$ is contained in the interior of $CA$ in $X \cup CA$ (relative to the collar structure).
<2>3. By the excision theorem for singular homology, excise $U$: $$H_n((X \cup CA) \setminus U, CA \setminus U) \xrightarrow[\cong]{\text{exc}} H_n(X \cup CA, CA).$$ <2>4. Note that $(X \cup CA) \setminus U = X \cup [A \times [1/2, 1])$ and $CA \setminus U = [A \times [1/2, 1])$.
<2>5. The interval $[1/2, 1]$ deformation retracts onto $\{1\}$, which yields a deformation retraction of the pair $(X \cup [A \times [1/2, 1]), [A \times [1/2, 1]))$ onto $(X, A)$.
<2>6. Therefore, the inclusion of pairs $(X, A) \hookrightarrow ((X \cup CA) \setminus U, CA \setminus U)$ induces an isomorphism on homology: $$H_n(X, A) \xrightarrow{\cong} H_n((X \cup CA) \setminus U, CA \setminus U).$$ <2>7. Composing with the excision isomorphism gives: $$H_n(X, A) \xrightarrow{\cong} H_n(X \cup CA, CA).$$ <2>8. Proof: By excision and homotopy invariance of pair homology.
Q.E.D.

<1>3. Combine isomorphisms.
<2>1. From <1>1 and <1>2: $$\widetilde{H}_n(X \cup CA) \cong H_n(X \cup CA, CA) \cong H_n(X, A) \quad \text{for all } n \ge 0.$$ <2>2. Proof: Composition of isomorphisms.
Q.E.D.

<1>4. Q.E.D. <2>1. Proof: Steps <1>1–<1>3 establish $\widetilde{H}_*(X \cup CA) \cong H_*(X, A)$.
:::
