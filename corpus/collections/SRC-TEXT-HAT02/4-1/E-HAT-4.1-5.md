---
schema: qual/card@1
id: E-HAT-4.1-5
kind: problem
title: "Relative $\\pi_1$ as cosets"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher Section 4.1 Exercise 5 and the 2021-06-02 correction; corrected the stored coset from alpha H to H alpha.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

::: {.problem}
For a pair $(X, A)$ of path-connected spaces, show that $\pi_1(X, A, x_0)$ can be identified in a natural way with the set of cosets $H\alpha$ of the subgroup $H \subset \pi_1(X, x_0)$ represented by loops in $A$ at $x_0$.
:::

::: {.solution}
Use Hatcher's interval model for $\pi_1(X,A,x_0)$: an element is represented by a path
\[
u:I\to X,
\qquad
u(0)\in A,
\quad
u(1)=x_0,
\]
with homotopies keeping the endpoint at $x_0$ and allowing the initial point to move in $A$.

Since $A$ is path-connected, choose a path $v$ in $A$ from $x_0$ to $u(0)$. Then $vu$ is a loop at $x_0$. Associate to the relative class of $u$ the left coset
\[
H[vu],
\qquad
H=i_*\pi_1(A,x_0)\subseteq\pi_1(X,x_0).
\]
If $v'$ is another such path, then $v'v^{-1}$ is a loop in $A$ at $x_0$, so
\[
[v'u]=[v'v^{-1}][vu]
\]
and hence $H[v'u]=H[vu]$. A relative homotopy of $u$ changes $vu$ by the same sort of left multiplication, so the coset depends only on the relative class.

Conversely, a loop $\alpha$ at $x_0$, viewed as a relative path with initial point $x_0\in A$, gives an element of $\pi_1(X,A,x_0)$. Two loops $\alpha,\alpha'$ give the same relative class exactly when
\[
[\alpha'][\alpha]^{-1}\in H,
\]
that is, exactly when
\[
H[\alpha']=H[\alpha].
\]
Thus the two constructions are inverse natural bijections of pointed sets:
\[
\boxed{\pi_1(X,A,x_0)\cong H\backslash\pi_1(X,x_0).}
\]
:::
