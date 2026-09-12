---
schema: qual/card@1
id: P-PRACT20-W6-13
kind: problem
title: "Week 6: Miscellaneous Topics, problem 13"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let X, Y be topological spaces and let $f : X \to Y$ be continuous.
Show that $f ( K )$ is compact in Y for any compact set $K \subseteq X$ . In short: show that the continuous image of a compact set is compact.
:::

::: {.solution}
Suppose that $K \subset X$ is compact.
We want to prove that $f ( K )$ is compact, so take an open cover {Vi} of $f ( K )$ . Since f is continuous, we have that $U _ { i } = f ^ { - 1 } ( V _ { i } )$ are open in X. Now if $x \in K$ , then $f ( x ) \in f ( K )$ which means that $f ( x ) \in V _ { i }$ for some i. But if $f ( x ) \in V _ { i }$ then $x \in U _ { i }$ . This shows that $\{ U _ { i } \}$ forms an open cover of K in X. Since K is compact, there is a finite subcover $U _ { 1 } , \ldots , U _ { n }$ . But then since $K \subset \cup _ { k = 1 } ^ { n } U _ { k }$ , we have $f ( K ) \subset \cup _ { k = 1 } ^ { n } f ( U _ { k } ) = \cup _ { k = 1 } ^ { n } V _ { k }$ , and so $V _ { 1 } , \ldots , V _ { n }$ forms a finite subcover of $f ( K )$ . Since $\{ V _ { i } \}$ was an arbitrary open cover of $f ( K )$ and we were able to extract a finite subcover, we conclude that $f ( K )$ is compact.
:::
