---
schema: qual/card@1
id: P-GRECH7-04
kind: problem
title: Properties of a graph after deleting one edge
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 4 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The figure was not recovered by either extraction.
---

::: {.problem}
Using the undirected graph below, delete the edge DE. Which of the following must be true?

I. vertex D is even

II. the graph is a spanning tree of the previous graph

III. the graph is a forest

(A) None of the above
(B) I and II only
(C) I and III only
(D) II and III only
(E) I, II, and III
:::

::: {.remark}
The source shows the undirected graph in a figure that is not reproduced here.
:::

::: pf

::: pf-step

After deleting the edge $DE$, the remaining edge set is
$$
\{AB,BC,BD,BE\}.
$$


::: pf-proof

The source figure has the five edges $AB$, $BC$, $BD$, $BE$, and $DE$. Deleting $DE$ leaves exactly the four displayed edges.

:::

:::

::: pf-step

Statement I is false: vertex $D$ is odd.


::: pf-proof

By step <1>1, the only remaining edge incident to $D$ is $BD$. Thus $\deg(D)=1$, which is odd.

:::

:::

::: pf-step

Statement II is true: the resulting graph is a spanning tree of the original graph.


::: pf-proof

The deletion removes no vertices, so the resulting graph contains all five original vertices. By step <1>1, every vertex $A,C,D,E$ is joined directly to $B$, so the graph is connected. It has five vertices and four edges; a connected graph on $n$ vertices with $n-1$ edges is a tree. Hence it is a tree containing every original vertex, that is, a spanning tree of the original graph.

:::

:::

::: pf-step

Statement III is true: the resulting graph is a forest.


::: pf-proof

Every tree is acyclic, and every acyclic graph is a forest. Step <1>3 shows that the resulting graph is a tree.

:::

:::

::: pf-step

Therefore the true statements are
$$
\boxed{\text{II and III only}},
$$
so the answer is (D).


::: pf-proof

Step <1>2 rules out I, while steps <1>3 and <1>4 establish II and III.

:::

:::

::: pf-qed

Step <1>5 gives the required choice.

:::

:::
