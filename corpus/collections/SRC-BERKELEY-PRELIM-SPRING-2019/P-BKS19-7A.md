---
schema: qual/card@1
id: P-BKS19-7A
kind: problem
title: Complex matrices with $A^{37}=I$ are diagonalizable
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2019 minimal-polynomial argument. The conclusion is correct; the solution below makes explicit the necessary squarefreeness of $x^{37}-1$.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified divisibility of the minimal polynomial, absence of repeated roots of $x^{37}-1$, and the minimal-polynomial criterion for diagonalizability.
---

::: {.problem}
Let $A$ be a complex $n\times n$ matrix satisfying $A^{37}=I$.
Show that $A$ is diagonalizable.
:::

::: {.solution}
Let $m_A(x)$ denote the minimal polynomial of $A$.

<1>1. The polynomial $m_A(x)$ divides $x^{37}-1$.

::: {.proof}
The hypothesis gives
$$
(A^{37}-I)=0,
$$
so the polynomial $p(x)=x^{37}-1$ annihilates $A$. By the defining divisibility property of the minimal polynomial, $m_A\mid p$.
:::

<1>2. The polynomial $x^{37}-1$ has no repeated root in $\mathbb C$.

::: {.proof}
Its derivative is
$$
37x^{36}.
$$
Any common root of $x^{37}-1$ and its derivative would have to be $0$, but $0^{37}-1=-1\neq0$. Hence
$$
\gcd(x^{37}-1,37x^{36})=1,
$$
so $x^{37}-1$ is squarefree. Since the field is $\mathbb C$, it therefore factors as a product of distinct linear factors.
:::

<1>3. The matrix $A$ is diagonalizable over $\mathbb C$.

::: {.proof}
By steps <1>1--<1>2, the minimal polynomial $m_A$ is a product of distinct linear factors. A complex matrix is diagonalizable exactly when its minimal polynomial splits into distinct linear factors. Therefore $A$ is diagonalizable.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves the assertion.
:::
:::
