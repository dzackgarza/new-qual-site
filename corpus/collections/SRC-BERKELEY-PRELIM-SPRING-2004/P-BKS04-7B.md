---
schema: qual/card@1
id: P-BKS04-7B
kind: problem
title: A common eigenvector when $AB-BA$ is a linear combination of $A$ and $B$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Let $A$ and $B$ be $n\times n$ matrices with complex entries, such that $AB-BA$ is a linear combination of $A$ and $B$. Prove that there exists a nonzero vector $v$ that is an eigenvector of both $A$ and $B$.
:::

::: {.solution}
Let $AB-BA=C=\alpha A+\beta B$. If $\alpha=\beta=0$, then $A$ and $B$ commute.
By a theorem of linear algebra, commuting complex matrices have a common eigenvector.
Otherwise, assume without loss of generality that $\beta\neq0$. Then $B$ is a linear combination of $A$ and $C$, so it suffices to prove that $A$ and $C$ have a common eigenvector.
Note that $AC-CA=\beta C$. Since $A$ has finitely many eigenvalues, it must have one, call it $\lambda$, such that $\lambda+\beta$ is not an eigenvalue of $A$. Let $v$ be a nonzero vector with $Av=\lambda v$. Then $ACv=CAv+\beta Cv=(\lambda+\beta)Cv$, so $Cv=0$. Hence $v$ is a common eigenvector of $A$ and $C$.
:::
