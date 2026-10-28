---
schema: qual/card@1
id: P-GRECH7-22
kind: problem
title: Isomorphism among three drawn graphs
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 22 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The figure was not recovered by either extraction.
---

::: {.problem}
Which of the following graphs are isomorphic?

(A) None of the above
(B) I and II only
(C) I and III only
(D) II and III only
(E) I, II, and III
:::

::: {.remark}
The source shows the three graphs I, II and III in a figure that is not reproduced here.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

From the source figure, Graph I has edge set
$$
\{AB,BC,CD\},
$$
Graph II has edge set
$$
\{FG,FH,EG\},
$$
and Graph III has edge set
$$
\{JK,KL,LM\}.
$$


::: pf-proof

These are the three edges visibly incident to the four labeled vertices in each drawing. In Graph II, the two diagonal edges cross in the drawing but there is no vertex at the crossing; its only vertices are the labeled points $E,F,G,H$.

:::

:::

::: {.pf-step #s1-2}

Graphs I and II are isomorphic.


::: pf-proof

Define
$$
\phi(A)=E,
\qquad
\phi(B)=G,
\qquad
\phi(C)=F,
\qquad
\phi(D)=H.
$$
This is a bijection on the four vertices, and by step [](#s1-1){.pf-ref} it sends the three edges
$$
AB,\ BC,\ CD
$$
respectively to
$$
EG,\ GF,\ FH,
$$
which are exactly the edges of Graph II. Hence adjacency and nonadjacency are preserved.

:::

:::

::: {.pf-step #s1-3}

Graphs I and III are isomorphic.


::: pf-proof

Define
$$
\psi(A)=J,
\qquad
\psi(B)=K,
\qquad
\psi(C)=L,
\qquad
\psi(D)=M.
$$
By step [](#s1-1){.pf-ref}, the edges $AB,BC,CD$ map respectively to $JK,KL,LM$, exactly the edges of Graph III. Thus $\psi$ is a graph isomorphism.

:::

:::

::: {.pf-step #s1-4}

Consequently all three graphs are mutually isomorphic.


::: pf-proof

Steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} give Graph I isomorphic to both Graph II and Graph III. Isomorphism is transitive, so Graph II and Graph III are also isomorphic.

:::

:::

::: {.pf-step #s1-5}

Therefore the correct choice for the graph drawn in the source is
$$
\boxed{\text{I, II, and III}},
$$
which is (E), not the source's supplied answer (C).


::: pf-proof

This is exactly the conclusion of step [](#s1-4){.pf-ref}. The source solution only shows that one particular proposed bijection from I to II fails; failure of one bijection does not prove that two graphs are nonisomorphic, and step [](#s1-2){.pf-ref} gives an explicit isomorphism.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the requested classification and identifies the source-answer error.

:::

:::

:::
