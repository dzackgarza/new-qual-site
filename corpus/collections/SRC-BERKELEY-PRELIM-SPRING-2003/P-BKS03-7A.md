---
schema: qual/card@1
id: P-BKS03-7A
kind: problem
title: When a union of subgroups is a subgroup
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
(a) If $H_1,H_2\le G$ and $H_1\cup H_2$ is a subgroup, prove that $H_1\subseteq H_2$ or $H_2\subseteq H_1$.

(b) For every $n\ge3$, construct a group $G$ with subgroups $H_1,\dots,H_n$, none contained in another, such that $H_1\cup\cdots\cup H_n$ is a subgroup.
:::

::: {.solution}
(a) If not, there exists $h _ { 1 } \in H _ { 1 } - H _ { 2 }$ and $h _ { 2 } \in H _ { 2 } - H _ { 1 }$ . Since $h _ { 1 }$ and $h _ { 2 }$ belong to the subgroup $H _ { 1 } \cup H _ { 2 }$ , we also have $h _ { 1 } h _ { 2 } \in H _ { 1 } \cup H _ { 2 }$ . If $h _ { 1 } h _ { 2 } \in H _ { 1 }$ , we get the contradiction $h _ { 2 } = h _ { 1 } ^ { - 1 } ( h _ { 1 } h _ { 2 } ) \in H _ { 1 } . \mathrm { ~ I f ~ } h _ { 1 } h _ { 2 } \in H _ { 2 } , \mathrm { ~ w e ~ g e t }$ the contradiction $h _ { 1 } = ( h _ { 1 } h _ { 2 } ) h _ { 2 } ^ { - 1 } \in H _ { 2 }$

(b) Let $G = ( \mathbb { Z } / 2 \mathbb { Z } ) ^ { n - 1 }$ . For $1 \leq i \leq n - 1$ , let $H _ { i } = \{ ( x _ { 1 } , \dots , x _ { n - 1 } ) \in G : x _ { i } = 0 \}$ . Then $H _ { 1 } \cup \ldots \cup H _ { n - 1 } = G - \{ ( 1 , 1 , \ldots , 1 ) \}$ . Let $H _ { n } = \left\{ \left( x _ { 1 } , \dots , x _ { n - 1 } \right) \in G : x _ { 1 } + x _ { 2 } = 0 \right\}$ . Then $( 1 , 1 , \ldots , 1 ) \in H _ { n } , \ s o \ H _ { 1 } \cup \cdots \cup H _ { n } = G$ . No $H _ { i }$ is contained in any other, since they are distinct subgroups of the same order.
:::
