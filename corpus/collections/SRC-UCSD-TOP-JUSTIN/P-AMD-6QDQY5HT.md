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
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $CA$ be the cone on $A$, show that $\tilde H_*(X \union CA) \cong \tilde H_*(X, A)$.
:::

::: {.solution}
**Goal:** Let $(X, A)$ be a topological pair.
Let $CA = (A \times [0, 1]) / (A \times \{0\})$ be the cone on $A$, attached to $X$ along $A \times \{1\} \equiv A \subseteq X$, so $X \cup CA = X \cup_A CA$.
Prove that $\widetilde{H}_n(X \cup CA) \cong H_n(X, A)$ for all $n \ge 0$.

<1>1. Apply the long exact sequence of the pair $(X \cup CA, CA)$.
<2>1. For the pair $(Y, B) = (X \cup CA, CA)$, the long exact sequence in reduced homology is: $$\cdots \to \widetilde{H}_n(CA) \xrightarrow{i_*} \widetilde{H}_n(X \cup CA) \xrightarrow{j_*} H_n(X \cup CA, CA) \xrightarrow{\partial} \widetilde{H}_{n-1}(CA) \to \cdots$$ <2>2. The cone $CA$ is contractible to the cone vertex $v = [A \times \{0\}]$ via $H([(a, t)], s) = [(a, (1-s)t)]$.
<2>3. Since $CA$ is contractible, its reduced homology vanishes in all degrees: $\widetilde{H}_n(CA) = 0$ for all $n \ge 0$.
<2>4. The exact sequence becomes $0 \to \widetilde{H}_n(X \cup CA) \xrightarrow{j_*} H_n(X \cup CA, CA) \to 0$, which gives an isomorphism: $$j_* \colon \widetilde{H}_n(X \cup CA) \xrightarrow{\cong} H_n(X \cup CA, CA) \quad \text{for all } n \ge 0.$$
::: {.proof}
<2>5. Substituting $\widetilde{H}_n(CA) = 0$ and $\widetilde{H}_{n-1}(CA) = 0$ into the long exact sequence leaves the short exact sequence $0 \to \widetilde{H}_n(X \cup CA) \to H_n(X \cup CA, CA) \to 0$, whose middle map is an isomorphism.
:::

<1>2. Apply excision to relate $H_n(X \cup CA, CA)$ to $H_n(X, A)$.
<2>1. Let $q:A\times[0,1]\to CA$ be the cone quotient, with $q(A\times\{0\})$ the cone vertex and $q(a,1)$ identified with $a\in A\subseteq X$. Set
$$
U=q\bigl(A\times[0,1/2)\bigr)\subseteq CA\subseteq X\cup_A CA.
$$
<2>2. The set $U$ is open in $X\cup_A CA$, and its closure is contained in
$$
q\bigl(A\times[0,1/2]\bigr),
$$
which lies in the interior of $CA$ inside $X\cup_A CA$ because it is disjoint from the attaching locus $q(A\times\{1\})=A$.
::: {.proof}
The preimage $A\times[0,1/2)$ is open in $A\times[0,1]$ and is saturated for the cone quotient, hence its image is open in $CA$; since it is disjoint from the attaching locus, it is also open in the adjunction space. Likewise $q(A\times(1/2,1])$ is open, so the closure of $U$ is contained in $q(A\times[0,1/2])$. Every point with cone coordinate at most $1/2$ has a neighborhood contained in the cone part and away from the attaching locus.
:::
<2>3. Excision therefore gives an isomorphism
$$
H_n\bigl((X\cup_A CA)\setminus U,\,CA\setminus U\bigr)
\xrightarrow{\cong}
H_n(X\cup_A CA,CA).
$$
::: {.proof}
The closure of the excised open set $U$ is contained in the interior of the subspace $CA$, exactly the hypothesis of the excision theorem for the pair $(X\cup_A CA,CA)$.
:::
<2>4. The complementary pair is
$$
\bigl((X\cup_A CA)\setminus U,\,CA\setminus U\bigr)
=
\Bigl(X\cup_A q\bigl(A\times[1/2,1]\bigr),\,q\bigl(A\times[1/2,1]\bigr)\Bigr).
$$
<2>5. This pair deformation retracts onto $(X,A)$ by moving the cone coordinate linearly from $t\in[1/2,1]$ to $1$ while fixing $X$ pointwise.
::: {.proof}
For $s\in[0,1]$, send $q(a,t)$ to
$$
q\bigl(a,(1-s)t+s\bigr)
$$
and fix every point of $X$. At $t=1$ this agrees with the attaching identification $q(a,1)=a$, so the homotopy is well-defined on the adjunction space. It preserves the cone-collar subspace and at $s=1$ sends that subspace onto $A$ while fixing $(X,A)$ pointwise.
:::
<2>6. Hence
$$
H_n(X,A)\xrightarrow{\cong}
H_n\bigl((X\cup_A CA)\setminus U,\,CA\setminus U\bigr)
\xrightarrow{\cong}
H_n(X\cup_A CA,CA).
$$
::: {.proof}
The first isomorphism is induced by the deformation retraction in <2>5 and the second by excision in <2>3.
:::

<1>3. Combine isomorphisms.
<2>1. From <1>1 and <1>2: $$\widetilde{H}_n(X \cup CA) \cong H_n(X \cup CA, CA) \cong H_n(X, A) \quad \text{for all } n \ge 0.$$
::: {.proof}
<2>2. The isomorphism of <1>1 and the isomorphism of <1>2 compose to give $\widetilde{H}_n(X \cup CA) \cong H_n(X, A)$.
:::

<1>4. Q.E.D.
::: {.proof}
<2>1. Steps <1>1–<1>3 establish $\widetilde{H}_*(X \cup CA) \cong H_*(X, A)$.
:::
:::
