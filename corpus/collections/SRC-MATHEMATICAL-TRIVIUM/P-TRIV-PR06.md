---
schema: qual/card@1
id: P-TRIV-PR06
kind: problem
title: 'Pairwise but not mutual independence: Bernstein''s tetrahedron'
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 6, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. The source includes Figure 6 of the colored tetrahedron. Flash preserves only an image placeholder, but the face-color description is present in text.
---

::: {.problem}
Three faces of a tetrahedron are painted red (R), green (G) and blue (B), while the forth face is painted in all three colors (see the figure).
Denote by P (A) the probability that it falls on a face containing the color A, A = R, G, B.

The source also includes Figure 6 showing the tetrahedron; Flash preserves only the textual face-color description.

(a) Check if $P ( A \cap B ) = P ( A ) P ( B )$ for all $A , B = R , G , B$

(b) Check if $P ( R \cap G \cap B ) = P ( R ) P ( G ) P ( B )$ . Are the events R, G, B pairwise independent?
Are they mutually independent?
:::

::: {.solution}
Assume the tetrahedron is fair, so each face has probability $1/4$. The four faces are $R$, $G$, $B$, and $RGB$.

<1>1. Each color event has probability
\[
P(R)=P(G)=P(B)=\frac12.
\]

::: {.proof}
The event $R$ occurs on the red-only face and on the $RGB$ face, two of the four equally likely faces. The same argument applies to $G$ and $B$.
:::

<1>2. For any two distinct colors $A,B\in\{R,G,B\}$,
\[
P(A\cap B)=\frac14.
\]

::: {.proof}
The only face containing any prescribed pair of distinct colors is the $RGB$ face, whose probability is $1/4$.
:::

<1>3. Hence every pair of distinct color events is independent:
\[
P(A\cap B)=P(A)P(B)=\frac14.
\]

::: {.proof}
By step <1>1, $P(A)P(B)=(1/2)(1/2)=1/4$, which equals the intersection probability in step <1>2.
:::

<1>4. The triple intersection has probability
\[
P(R\cap G\cap B)=\frac14,
\]
whereas
\[
P(R)P(G)P(B)=\frac18.
\]

::: {.proof}
All three colors occur simultaneously exactly on the $RGB$ face, so the triple intersection has probability $1/4$. Step <1>1 gives the product $(1/2)^3=1/8$.
:::

<1>5. Therefore $R,G,B$ are pairwise independent but not mutually independent.

::: {.proof}
Pairwise independence is step <1>3. Mutual independence would require the triple-intersection identity, which fails by step <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>3--<1>5 answer parts (a) and (b).
:::
:::
