---
schema: qual/card@1
id: P-TIE-S15-23
kind: problem
title: Vitali's convergence theorem
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 23.
---

::: {.problem}
Assume $f_{n} \in H(\Omega)$ is a sequence of holomorphic functions on the region $\Omega$ that are uniformly bounded on compact subsets and $f \in H(\Omega)$ is such that the set $\{z \in \Omega \st \lim_{n \to \infty} f_{n}(z) = f(z)\}$ has a limit point in $\Omega$. Show that $f_{n}$ converges to $f$ uniformly on compact subsets of $\Omega$.
:::

::: {.solution}

Let
$$
E
\coloneqq
\{z\in\Omega:f_n(z)\to f(z)\}.
$$
By hypothesis, $E$ has a limit point in $\Omega$.

::: pf

::: {.pf-step #s1-1}

Every subsequence of $(f_n)$ has a further subsequence that converges uniformly on compact subsets of $\Omega$ to a holomorphic function.


::: pf-proof

The family
$$
\mathcal F
\coloneqq
\{f_n:n\ge1\}
$$
is locally uniformly bounded by hypothesis. Montel's theorem therefore implies that $\mathcal F$ is a normal family. Hence every sequence drawn from $\mathcal F$, and in particular every subsequence of $(f_n)$, has a further subsequence converging uniformly on compact subsets of $\Omega$ to a holomorphic function.

:::

:::

::: {.pf-step #s1-2}

Every locally uniform subsequential limit of $(f_n)$ equals $f$ on all of $\Omega$.


::: pf-proof

Let
$$
f_{n_j}\longrightarrow g
$$
uniformly on compact subsets of $\Omega$. Fix $z\in E$. Local uniform convergence implies pointwise convergence, so
$$
g(z)
=
\lim_{j\to\infty}f_{n_j}(z).
$$
But because $z\in E$, the full sequence satisfies
$$
f_n(z)\longrightarrow f(z),
$$
and therefore the subsequence has the same limit:
$$
g(z)=f(z).
$$
Thus
$$
g=f
$$
on the set $E$.

The functions $g$ and $f$ are holomorphic on the region $\Omega$, and $E$ has a limit point in $\Omega$. By the identity theorem,
$$
g\equiv f
$$
on $\Omega$.

:::

:::

::: {.pf-step #s1-3}

The full sequence $(f_n)$ converges uniformly to $f$ on every compact subset of $\Omega$.


::: pf-proof

Suppose not. Then there exist a compact set
$$
K\subset\Omega,
$$
a number $\varepsilon>0$, and a subsequence $(f_{n_j})$ such that
$$
\sup_{z\in K}
\abs{f_{n_j}(z)-f(z)}
\ge
\varepsilon
$$
for every $j$.

By step [](#s1-1){.pf-ref}, this subsequence has a further subsequence
$$
f_{n_{j_k}}
$$
that converges uniformly on compact subsets of $\Omega$ to a holomorphic function $g$. By step [](#s1-2){.pf-ref},
$$
g=f.
$$
Hence
$$
\sup_{z\in K}
\abs{f_{n_{j_k}}(z)-f(z)}
\longrightarrow0,
$$
contradicting the lower bound $\varepsilon$.

Therefore
$$
\boxed{
f_n\longrightarrow f
\quad
\text{uniformly on compact subsets of }\Omega.
}
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required conclusion.

:::

:::

:::
