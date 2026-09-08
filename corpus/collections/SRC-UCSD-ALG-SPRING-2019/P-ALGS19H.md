---
schema: qual/card@1
id: P-ALGS19H
kind: problem
title: "Real subfield of cyclotomic field and powers of algebraic numbers in Q"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Suppose $\zeta_n := e^{\frac{2\pi i}{n}} \in \mathbb{C}$, and $K_n := \mathbb{Q}[\zeta_n] \cap \mathbb{R}$.

(a) Prove that $K_n/\mathbb{Q}$ is a Galois extension.

(b) Suppose $\alpha \in K_n$, $r := \alpha^m \in \mathbb{Q}$ and $m$ is the smallest such positive integer (i.e.\ $\alpha^i \notin \mathbb{Q}$ for $1 \leq i < m$). Prove that $m \leq 2$.

Hint: Think about the minimal polynomial of $\alpha$ over $\mathbb{Q}$.
:::


::: {.solution}
<1>1. Let \(L=\mathbb Q(\zeta_n)\). Then \(L/\mathbb Q\) is Galois and
\[
\operatorname{Gal}(L/\mathbb Q)\cong (\mathbb Z/n\mathbb Z)^\times,
\]
so its Galois group is abelian.
::: {.proof}
The field \(L\) is the splitting field over \(\mathbb Q\) of the separable polynomial \(x^n-1\). Its automorphisms are determined by \(\zeta_n\mapsto \zeta_n^a\) for \(a\in(\mathbb Z/n\mathbb Z)^\times\), giving the stated abelian Galois group.
:::

<1>2. Complex conjugation \(c\in\operatorname{Gal}(L/\mathbb Q)\) has fixed field exactly
\[
L^{\langle c\rangle}=L\cap\mathbb R=K_n.
\]
::: {.proof}
An element of \(L\) is fixed by complex conjugation exactly when it is real.
:::

<1>3. The extension \(K_n/\mathbb Q\) is Galois.
::: {.proof}
Since \(\operatorname{Gal}(L/\mathbb Q)\) is abelian, the subgroup \(\langle c\rangle\) is normal. By the fundamental theorem of Galois theory, the fixed field \(K_n=L^{\langle c\rangle}\) is therefore Galois over \(\mathbb Q\).
:::

<1>4. Now suppose \(\alpha\in K_n\) and \(\alpha^m=r\in\mathbb Q\), with \(m\) minimal positive. If \(\alpha=0\), then \(m=1\). Hence assume \(\alpha\ne0\).
::: {.proof}
If \(\alpha=0\), then already \(\alpha^1=0\in\mathbb Q\), so the minimal positive exponent is \(1\).
:::

<1>5. Let \(f\in\mathbb Q[x]\) be the minimal polynomial of \(\alpha\). Every root \(\beta\) of \(f\) lies in \(K_n\), hence is real, and satisfies \(\beta^m=r=\alpha^m\).
::: {.proof}
By <1>3, \(K_n/\mathbb Q\) is Galois. Therefore every \(\mathbb Q\)-conjugate of \(\alpha\) lies in \(K_n\). Since \(K_n\subseteq\mathbb R\), every such conjugate is real. Also \(f\) divides \(x^m-r\), because \(f(\alpha)=0\) and \(\alpha^m-r=0\); hence every root \(\beta\) of \(f\) satisfies \(\beta^m=r\).
:::

<1>6. Every root \(\beta\) of \(f\) is equal to \(\alpha\) or \(-\alpha\). Thus \(\deg f\le2\).
::: {.proof}
Since \(\alpha\ne0\) and \(\beta^m=\alpha^m\), one has \((\beta/\alpha)^m=1\). Hence \(\beta/\alpha\) is an \(m\)-th root of unity. But both \(\alpha\) and \(\beta\) are real, so \(\beta/\alpha\in\mathbb R\). The only real roots of unity are \(1\) and \(-1\). Therefore \(\beta=\pm\alpha\). Since a minimal polynomial is separable in characteristic \(0\), it has at most these two distinct roots, so \(\deg f\le2\).
:::

<1>7. If \(\deg f=1\), then \(\alpha\in\mathbb Q\), so \(m=1\). If \(\deg f=2\), then the roots of \(f\) are \(\alpha\) and \(-\alpha\), so
\[
f(x)=x^2-\alpha^2\in\mathbb Q[x].
\]
Hence \(\alpha^2\in\mathbb Q\), and therefore \(m\le2\).
::: {.proof}
The degree-one case is immediate. In degree two, <1>6 shows that the two distinct conjugates are \(\alpha\) and \(-\alpha\). Since \(f\) is monic,
\[
f(x)=(x-\alpha)(x+\alpha)=x^2-\alpha^2.
\]
Because \(f\in\mathbb Q[x]\), its constant coefficient \(-\alpha^2\) is rational. Thus a positive exponent at most \(2\) already sends \(\alpha\) into \(\mathbb Q\), so the minimal such exponent satisfies \(m\le2\).
:::
:::
