---
schema: qual/card@1
id: P-BKS04-7B
kind: problem
title: UC Berkeley Spring 2004 prelim 7B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let A and B be $n \times n$ matrices with complex entries, such that $A B - B A$ is a linear combination of A and B. Prove that there exists a nonzero vector v that is an eigenvector of both A and B.
:::

::: {.solution}
Let $A B - B A = C = \alpha A + \beta B$ . If $\alpha = \beta = 0$ , then A and B commute. By a theorem of linear algebra, commuting complex matrices have a common eigenvector. Otherwise, assume without loss of generality that $\beta \neq 0$ . Then B is a linear combination of A and C, so it suffices to prove that A and C have a common eigenvector. Note that $A C - C A = \beta C$ . Since A has finitely many eigenvalues, it must have one, call it λ, such that $\lambda + \beta$ is not an eigenvalue of A. Let v be a nonzero vector with $A v \ = \ \lambda v$ Then $A C v = C A v + \beta C v = ( \lambda + \beta ) C v , \mathrm { s o } C v = 0$ . Hence v is a common eigenvector of A and C.
:::
