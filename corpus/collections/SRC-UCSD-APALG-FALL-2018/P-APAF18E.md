---
schema: qual/card@1
id: P-APAF18E
kind: problem
title: Character values are real when $g$ is conjugate to $g^{-1}$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
  note: Verified the inverse-character and conjugacy argument.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Five steps asserted their claim with no justification and each now carries one: the finiteness of the
    order of $\rho(g)$ from $\rho(g)^{\abs{G}} = \id_V$, the diagonalizability of $\rho(g)$ from the
    squarefree polynomial $x^{\abs{G}} - 1$ together with $\abs{\lambda_j} = 1$ and
    $\lambda_j^{-1} = \overline{\lambda_j}$, the eigenvalues of the inverse, the trace as the sum of the
    eigenvalues, and the conjugate of the sum. The container step carried a label and now states its
    claim, the two other steps carried run-in labels inside their claims and now state assertions, and the
    "Goal" paragraph restating the problem is gone. Sources are cited by numbered statement: the trace is
    the sum of the eigenvalues of a diagonalizable operator, and a linear operator annihilated by a
    polynomial with distinct roots is diagonalizable. No page reference is written in the body of this
    card or in the event above. The statement is unchanged. The collection retains the UCSD applied
    algebra qualifying exam of Fall 2018 and no solution sheet, so the argument is the card's own.
---

::: {.problem}
Let $G$ be a finite group, let $V$ be a finite-dimensional complex representation of $G$, and let $\chi\colon G\to\CC$ be the character of $V$.
Let $g\in G$ be a group element such that $g$ is conjugate to $g^{-1}$.
Prove that $\chi(g)$ is a real number.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
$\chi(g^{-1}) = \overline{\chi(g)}$ for all $g \in G$.

::: pf-proof

::: pf-step
Let $n = \dim_\CC(V)$. The representation $\rho: G \to \operatorname{GL}(V)$ assigns to $g$ an operator $\rho(g)$ of finite order dividing $\cardinality{G}$.

::: pf-proof
Each $\rho(g)$ is invertible with inverse $\rho(g^{-1})$ and $\rho(g)^{\abs{G}} = \rho(g^{\abs{G}}) = \rho(e) = \id_V$, so the order of $\rho(g)$ in $\operatorname{GL}(V)$ divides $\abs{G}$; in particular it is finite. Since $G$ is finite and $V$ is finite-dimensional over $\CC$, this is a representation of a finite group on a finite-dimensional complex space, so the order of the operator is a finite integer $m$ dividing $\abs{G}$.
:::

:::

::: pf-step
Hence $\rho(g)$ is diagonalizable with eigenvalues $\lambda_1, \dots, \lambda_n \in \CC$, each satisfying $\lambda_j^{\cardinality{G}} = 1$, so $\abs{\lambda_j} = 1$ and $\lambda_j^{-1} = \overline{\lambda_j}$ for all $j \in \{1, \dots, n\}$.

::: pf-proof
The minimal polynomial of $\rho(g)$ divides $x^m - 1$, whose roots are the distinct $m$-th roots of unity because $\CC$ has characteristic $0$; a minimal polynomial with distinct roots means the operator is diagonalizable. Every eigenvalue satisfies $\lambda^m = 1$, so $\abs{\lambda} = 1$ and $\lambda^{-1} = \overline{\lambda}$, since $\lambda\overline{\lambda} = \abs{\lambda}^2 = 1$.
:::

:::

::: pf-step
The eigenvalues of $\rho(g^{-1}) = \rho(g)^{-1}$ are $\lambda_1^{-1}, \dots, \lambda_n^{-1}$.

::: pf-proof
The eigenvalues of the inverse of a diagonalizable operator with eigenvalues $\lambda_j$ are the inverses $\lambda_j^{-1}$, because an eigenvector of $\rho(g)$ for $\lambda_j$ is an eigenvector of the inverse for $\lambda_j^{-1}$; and $\rho(g^{-1}) = \rho(g)^{-1}$ since $\rho$ is a homomorphism.
:::

:::

::: pf-step
The character value is the trace:
$$\chi(g) = \operatorname{tr}(\rho(g)) = \sum_{j=1}^n \lambda_j.$$

::: pf-proof
The trace is the sum of the eigenvalues counted with multiplicity, and the eigenvalues of $\rho(g)$ are $\lambda_1, \dots, \lambda_n$ with $n = \dim_\CC V$ because the operator is diagonalizable; the character is by definition the trace of $\rho(g)$.
:::

:::

::: pf-step
The character value at the inverse is:
$$\chi(g^{-1}) = \operatorname{tr}(\rho(g^{-1})) = \sum_{j=1}^n \lambda_j^{-1} = \sum_{j=1}^n \overline{\lambda_j} = \overline{\sum_{j=1}^n \lambda_j} = \overline{\chi(g)}.$$

::: pf-proof
Substituting the eigenvalues of $\rho(g^{-1})$ into the trace gives the second equality, $\lambda_j^{-1} = \overline{\lambda_j}$ gives the third, and the conjugate of a finite sum is the sum of the conjugates, which gives the last equality together with the previous step.
:::

:::

:::

:::

::: {.pf-step #s2}
If two elements $a, b \in G$ are conjugate, then $\chi(a) = \chi(b)$.

::: pf-proof
If $b = x a x^{-1}$ for some $x \in G$, then $\rho(b) = \rho(x)\rho(a)\rho(x)^{-1}$. By the cyclic property of the trace, $\operatorname{tr}(\rho(b)) = \operatorname{tr}(\rho(x)\rho(a)\rho(x)^{-1}) = \operatorname{tr}(\rho(a))$, hence $\chi(b) = \chi(a)$.
:::

:::

::: {.pf-step #s3}
$\chi(g) = \chi(g^{-1})$.

::: pf-proof
Direct consequence of step [](#s2){.pf-ref} with $a = g^{-1}$ and $b = g$.
:::

:::

::: pf-step
$\chi(g) \in \RR$, that is $\chi(g) = \boxed{\overline{\chi(g)}}$.

::: pf-proof
Combining step [](#s1){.pf-ref} and step [](#s3){.pf-ref} gives $\chi(g) = \overline{\chi(g)}$. Any complex number equal to its complex conjugate is real, so $\chi(g) \in \RR$.
:::

:::

:::
:::
