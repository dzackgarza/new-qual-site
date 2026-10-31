---
schema: qual/card@1
id: P-PRACT20-W6-09
kind: problem
title: Compactness, boundedness of continuous functions and connectedness in $\RR^n$
classification:
  areas:
  - prelim
  topics:
  - Compactness
  - Heine-Borel Theorem
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the empty set misread as alpha, checked against Week6_solns.pdf (Problem 9).
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced OCR-garbled norm in the solution with the source's f(x) = ||x||, checked against Week6_solns.pdf page 5 (Problem 9).
---

::: {.problem}
Let $\emptyset \neq K \subseteq \RR^n$. Which of the following statements are true?

(A) If $K$ is compact, then every continuous real-valued function on $K$ is bounded.

(B) If every continuous real-valued function on $K$ is bounded, then $K$ is compact.

(C) If $K$ is compact, then $K$ is connected.
:::

::: {.solution}
(A) is true. Let $f$ be continuous on $K$ and set $U_n=f^{-1}((-n,n))$ for $n\in\NN$. These sets are open in $K$ and cover $K$. By compactness finitely many cover $K$, and since they are nested, $K\subset U_N$ for some $N$. Then $\abs{f(x)}<N$ for all $x\in K$.

(B) is true. We prove the contrapositive. If $K$ is not compact, then by the Heine--Borel theorem it is not closed or not bounded. If $K$ is not closed, there is $x_0\in\RR^n\setminus K$ that is a limit point of $K$; then $f(x)=\frac{1}{\norm{x-x_0}}$ is continuous and unbounded on $K$. If $K$ is unbounded, then $f(x)=\norm{x}$ is continuous and unbounded on $K$.

(C) is false. The set $K=[-2,-1]^n\cup[1,2]^n$ is compact but not connected.
:::
