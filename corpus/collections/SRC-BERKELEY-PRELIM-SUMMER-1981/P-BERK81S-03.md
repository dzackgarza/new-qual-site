---
schema: qual/card@1
id: P-BERK81S-03
kind: problem
title: $\QQ$ is not a countable intersection of open subsets of $\RR$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Argued by Baire category. If Q=intersection U_n with U_n open, then
    every U_n is dense because it contains the dense set Q. Enumerating
    Q={q_n}, the sets V_n=U_n\{q_n} are still open dense. Their intersection
    is empty: every rational q_n is removed at stage n, and no irrational
    lies in all U_n. This contradicts the Baire category theorem on R.
---

::: {.problem}
Prove or disprove: the set $\mathbb Q$ of rational numbers is the intersection of a countable family of open subsets of $\mathbb R$.
:::

::: {.solution}
<1>1. Suppose, toward a contradiction, that there are open sets
$$
U_1,U_2,\ldots\subseteq\RR
$$
such that
$$
\QQ=\bigcap_{n=1}^{\infty}U_n.
$$

::: {.proof}
This is the negation of the conclusion to be proved.
:::

<1>2. Every $U_n$ is dense in $\RR$.

::: {.proof}
By step <1>1,
$$
\QQ\subseteq U_n
$$
for every $n$. The rational numbers are dense in $\RR$, so every set
containing $\QQ$ is dense.
:::

<1>3. Enumerate the rationals as
$$
\QQ=\{q_1,q_2,\ldots\}
$$
and define
$$
V_n=U_n\sm\{q_n\}.
$$
Then every $V_n$ is open and dense in $\RR$.

::: {.proof}
The set
$$
\RR\sm\{q_n\}
$$
is open and dense. Hence
$$
V_n
=
U_n\cap(\RR\sm\{q_n\})
$$
is open.

By step <1>2, $U_n$ is open and dense, and
$\RR\sm\{q_n\}$ is also open and dense. The intersection of two open dense
subsets of $\RR$ is dense, so $V_n$ is dense.
:::

<1>4. One has
$$
\bigcap_{n=1}^{\infty}V_n=\varnothing.
$$

::: {.proof}
Let $x\in\RR$.

If $x$ is irrational, then by step <1>1,
$$
x\notin\bigcap_{n=1}^{\infty}U_n,
$$
so $x\notin U_m$ for some $m$, and hence $x\notin V_m$.

If $x$ is rational, then $x=q_k$ for some $k$. By definition,
$$
q_k\notin V_k.
$$

Thus no real number belongs to every $V_n$.
:::

<1>5. Step <1>4 contradicts the Baire category theorem.

::: {.proof}
The real line $\RR$ is a complete metric space. By the Baire category
theorem, a countable intersection of open dense subsets of $\RR$ is dense,
and in particular nonempty. Step <1>3 says that every $V_n$ is open and
dense, while step <1>4 says their intersection is empty. This is impossible.
:::

<1>6. Therefore the statement is false:
$$
\boxed{
\QQ\text{ is not a countable intersection of open subsets of }\RR.
}
$$

::: {.proof}
The assumption in step <1>1 led to the contradiction in step <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 gives the required disproof.
:::
:::
