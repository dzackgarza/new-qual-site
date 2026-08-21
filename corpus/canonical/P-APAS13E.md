---
schema: qual/card@1
id: P-APAS13E
kind: problem
title: Induced representations and Frobenius reciprocity
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
solved: false
---

::: problem
Let $H$ be a subgroup of $G$ and $A\colon H\to\mathrm{GL}_n(\mathbb{C})$ be a representation of $H$. Let $\chi^A\colon H\to\mathbb{C}$ be the character of $A$. Define $\chi^{\overline{A}}\colon G\to\mathbb{C}$ by
\[
\chi^{\overline{A}}(\sigma)=
\begin{cases}
\chi^A(\sigma) & \text{if }\sigma\in H,\\
0 & \text{if }\sigma\in G\setminus H.
\end{cases}
\]

(a) Define the representation $A\uparrow_H^G$.

(b) Prove that
\[
\chi^{A\uparrow_H^G}=\frac{1}{|H|}\sum_{\sigma\in G}\sigma\cdot\chi^{\overline{A}}\cdot\sigma^{-1}.
\]

(c) State and prove the Frobenius Reciprocity Theorem.
:::
