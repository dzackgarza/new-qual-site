---
schema: qual/card@1
id: P-PRACT20-W6-24
kind: problem
title: Images and preimages of unions and intersections
classification:
  areas:
  - prelim
  topics:
  - Functions
  - Images and Preimages
relations: []
review: draft
---

::: {.problem}
Let $f : \RR \to \RR$ and let $X, Y \subseteq \RR$. Which of these are necessarily true?

(A) $f(X \cap Y) = f(X) \cap f(Y)$

(B) $f(X \cup Y) = f(X) \cup f(Y)$

(C) $f^{-1}(X \cap Y) = f^{-1}(X) \cap f^{-1}(Y)$

(D) $f^{-1}(X \cup Y) = f^{-1}(X) \cup f^{-1}(Y)$

Here for $A \subseteq \RR$, $f(A) = \{f(x) : x \in A\}$ and $f^{-1}(A) = \{x \in \RR : f(x) \in A\}$.
:::

::: {.solution}
(B), (C) and (D) are true; (A) is false. Preimages preserve unions and intersections, while images preserve only unions.

(B) $y\in f(X\cup Y)$ iff $y=f(x)$ for some $x\in X$ or some $x\in Y$, iff $y\in f(X)\cup f(Y)$.

(C) $x\in f^{-1}(X\cap Y)$ iff $f(x)\in X$ and $f(x)\in Y$, iff $x\in f^{-1}(X)\cap f^{-1}(Y)$.

(D) $x\in f^{-1}(X\cup Y)$ iff $f(x)\in X$ or $f(x)\in Y$, iff $x\in f^{-1}(X)\cup f^{-1}(Y)$.

(A) Let $f(x)=x^2$, $X=(-1,0)$ and $Y=(0,1)$. Then $X\cap Y=\emptyset$, so $f(X\cap Y)=\emptyset$, while $f(X)=f(Y)=(0,1)$, so $f(X)\cap f(Y)=(0,1)\neq\emptyset$. Only the inclusion $f(X\cap Y)\subseteq f(X)\cap f(Y)$ holds in general.
:::
