---
schema: qual/card@1
id: P-NORI-GT-6-03
kind: problem
title: Additivity of the polynomial vanishing on a finite additive subgroup
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 6.3 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Let $F$ be a field of characteristic $p > 0$. Let $A$ be a finite additive subgroup of $F$.

Let $f_{A} \in F[X]$ be the product of $(X - a)$, taken over all $a \in A$.

(i) Prove that $f_{A}(X + a) = f_{A}(X)$ for all $a \in A$.

(ii) Deduce that $f_{A}(X + Y) = f_{A}(X) + f_{A}(Y) \in F[X, Y]$.

Hint: Let $C = F[Y]$ and let $h(X) = -f_{A}(X + Y) + f_{A}(X) + f_{A}(Y) \in C[X]$. Use (i) to find more $c \in C$ such that $h(c) = 0$ than the degree of $h \in C[X]$.
:::

::: {.solution}

Let
$$
q=\abs{A},
\qquad
f_A(X)=\prod_{b\in A}(X-b).
$$

::: pf

::: {.pf-step #s1-1}

For every $a\in A$,
$$
\boxed{f_A(X+a)=f_A(X)}.
$$


::: pf-proof

Fix $a\in A$. Since $A$ is an additive subgroup, translation by $a$ permutes $A$. Therefore
$$
\begin{aligned}
f_A(X+a)
&=\prod_{b\in A}(X+a-b)\\
&=\prod_{c\in A}(X-c)\\
&=f_A(X),
\end{aligned}
$$
where in the second product we reindex by $c=b-a$. This proves part (i).

:::

:::

::: {.pf-step #s1-2}

Define
$$
h(X)=-f_A(X+Y)+f_A(X)+f_A(Y)
\in F[Y][X].
$$
Then
$$
\deg_X h\leq q-1.
$$


::: pf-proof

The polynomial $f_A$ is monic of degree $q$. Hence both $f_A(X+Y)$ and $f_A(X)$ have leading $X$-term $X^q$. These leading terms cancel in
$$
-f_A(X+Y)+f_A(X),
$$
while $f_A(Y)$ has $X$-degree $0$. Therefore $\deg_X h\leq q-1$.

:::

:::

::: {.pf-step #s1-3}

Every element $a\in A$ is a root of $h(X)$.


::: pf-proof

Because $0\in A$, one has
$$
f_A(a)=0
$$
for every $a\in A$. By step [](#s1-1){.pf-ref}, applied with the indeterminate $Y$ in place of $X$,
$$
f_A(Y+a)=f_A(Y).
$$
Thus
$$
\begin{aligned}
h(a)
&=-f_A(a+Y)+f_A(a)+f_A(Y)\\
&=-f_A(Y)+0+f_A(Y)\\
&=0.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

One has
$$
h(X)=0
$$
in $F[Y][X]$.


::: pf-proof

The coefficient ring $F[Y]$ is an integral domain. A nonzero polynomial of degree at most $q-1$ over an integral domain has at most $q-1$ distinct roots in that domain. By step [](#s1-3){.pf-ref}, the polynomial $h$ has the $q$ distinct roots given by the elements of $A\subseteq F\subseteq F[Y]$. Together with the degree bound in step [](#s1-2){.pf-ref}, this forces $h=0$.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{f_A(X+Y)=f_A(X)+f_A(Y)}
$$
in $F[X,Y]$.


::: pf-proof

Step [](#s1-4){.pf-ref} says precisely that
$$
-f_A(X+Y)+f_A(X)+f_A(Y)=0.
$$
Rearranging gives the asserted identity, proving part (ii).

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part (i), and step [](#s1-5){.pf-ref} proves part (ii).

:::

:::

:::
