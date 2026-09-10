---
schema: qual/card@1
id: P-JHUMAY11ANC
kind: problem
title: "A holomorphic self-map of a bounded domain has derivative at most one at a fixed point"
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared May 2011 problem 3 and its iteration hint on PDF page 24; retained boundedness without adding simple connectedness."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the common bound for all iterates, the derivative product at the fixed point, and the nth-root limit; separated the retained source hint from the statement."
---

3. Let U be a bounded domain in C, and let $f : U \to U$ such that f is holomorphic.
   Let $P \in U$ and suppose that $f ( P ) = P$ . Prove that $| f ^ { \prime } ( P ) | \leq 1$

::: hint
Consider the iterates $f_n=f\circ\cdots\circ f$ with $n$ factors.
:::

::: solution
<1>1. The derivatives of all iterates at $P$ have a common upper bound.

::: proof
Since $U$ is open and contains $P$, choose $r>0$ with
$\overline{D(P,r)}\subset U$. Boundedness of $U$ gives
a constant $M>0$ such that $|z|\leq M$ for every $z\in U$.
For $n\geq1$, the iterate $f_n=f^{\circ n}$ is
holomorphic on $U$, maps $U$ to itself and fixes $P$,
by induction using $f(U)\subset U$ and $f(P)=P$.
Thus $|f_n|\leq M$ on the same circle $|z-P|=r$ for
every $n$. Cauchy's derivative formula gives
$$
f_n'(P)=\frac{1}{2\pi i}\int_{|z-P|=r}
\frac{f_n(z)}{(z-P)^2}\,dz,
\qquad |f_n'(P)|\leq\frac Mr
$$
[@SS03]. Neither the radius nor this bound depends on $n$.
:::

<1>2. The chain rule forces $|f'(P)|\leq1$.

::: proof
Let $a=f'(P)$. Because every iterate fixes $P$, the
chain rule gives $f_{n+1}'(P)=f'(P)f_n'(P)$. Starting
with $f_1'(P)=a$, induction yields $f_n'(P)=a^n$.
Step <1>1 therefore implies
$$
|a|^n\leq M/r,\qquad |a|\leq(M/r)^{1/n}
\quad(n\geq1).
$$
Since $M/r$ is a fixed positive number, its $n$th root
tends to one. Passing to the limit proves $|f'(P)|\leq1$.
:::
:::
