---
schema: qual/card@1
id: P-WESRA16-A4
kind: problem
title: 'Increasing simple approximation and countable indicator expansion'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Group A, problem A4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Let $f:\RR^d\to[0,\infty)$ be Lebesgue measurable.

(a) Using
$$
W_{n,k}=\{x:k2^{-n}\le f(x)<(k+1)2^{-n}\},
$$
construct simple functions $\varphi_n$ with $\varphi_0=0$, $\varphi_n\uparrow f$ pointwise, and $\varphi_n\le\varphi_{n+1}\le f$.

(b) Prove that there are nonnegative numbers $c_p$ and measurable sets $M_p$ such that
$$
f=\sum_{p=0}^\infty c_p\mathbf1_{M_p}.
$$
Hint: notice that $f=\sum_{n=0}^\infty(\varphi_{n+1}-\varphi_n)$.
:::

::: {.solution}

For $n\geq0$, define
$$
\varphi_n
=\sum_{k=0}^{n2^n-1}k2^{-n}\mathbf1_{W_{n,k}}
+n\mathbf1_{\{f\geq n\}},
$$
where the first sum is empty when $n=0$.

::: pf

::: {.pf-step #s1-1}

Each $\varphi_n$ is a nonnegative measurable simple function, and $\varphi_0=0$.


::: pf-proof

Each set $W_{n,k}$ is measurable because $f$ is measurable, and $\{f\geq n\}$ is measurable for the same reason. The displayed sum has only finitely many terms, so $\varphi_n$ is measurable and has finite range. For $n=0$, the first sum is empty and the second term is identically zero, hence $\varphi_0=0$.

:::

:::

::: {.pf-step #s1-2}

For every $n\geq0$ and $x\in\RR^d$,
$$
\varphi_n(x)=
\begin{cases}
2^{-n}\lfloor2^nf(x)\rfloor,&f(x)<n,\\
n,&f(x)\geq n.
\end{cases}
$$
In particular,
$$
0\leq\varphi_n(x)\leq f(x).
$$


::: pf-proof

If $f(x)<n$, there is a unique integer $k$ with
$$
0\leq k<n2^n,
\qquad
k2^{-n}\leq f(x)<(k+1)2^{-n}.
$$
Thus $x\in W_{n,k}$ and the sum defining $\varphi_n$ takes the value $k2^{-n}=2^{-n}\lfloor2^nf(x)\rfloor$. If $f(x)\geq n$, none of the sets $W_{n,k}$ occurring in the finite sum contains $x$, while the final indicator contributes $n$. Both formulas are nonnegative and at most $f(x)$.

:::

:::

::: {.pf-step #s1-3}

For every $n\geq0$ and $x\in\RR^d$,
$$
\varphi_n(x)\leq\varphi_{n+1}(x).
$$


::: pf-proof

Fix $x$ and write $t=f(x)$. If $t\geq n+1$, then
$$
\varphi_n(x)=n\leq n+1=\varphi_{n+1}(x).
$$
If $n\leq t<n+1$, then $\varphi_n(x)=n$, while step [](#s1-2){.pf-ref} gives either $\varphi_{n+1}(x)=n+1$ or
$$
\varphi_{n+1}(x)=2^{-(n+1)}\lfloor2^{n+1}t\rfloor\geq n,
$$
because $2^{n+1}t\geq n2^{n+1}$.

Finally, if $t<n$, then both values are dyadic floors. Put $q=\lfloor2^nt\rfloor$. Since
$$
2^{n+1}t\geq2q,
$$
one has $\lfloor2^{n+1}t\rfloor\geq2q$, and therefore
$$
\varphi_{n+1}(x)
=2^{-(n+1)}\lfloor2^{n+1}t\rfloor
\geq2^{-n}q
=\varphi_n(x).
$$

:::

:::

::: {.pf-step #s1-4}

For every $x\in\RR^d$,
$$
\varphi_n(x)\longrightarrow f(x).
$$


::: pf-proof

Fix $x$ and set $t=f(x)<\infty$. For every integer $n>t$, step [](#s1-2){.pf-ref} gives
$$
\varphi_n(x)=2^{-n}\lfloor2^nt\rfloor.
$$
Hence
$$
0\leq t-\varphi_n(x)<2^{-n}.
$$
The right-hand side tends to zero, so $\varphi_n(x)\to t=f(x)$.

:::

:::

::: {.pf-step #s1-5}

The sequence $(\varphi_n)$ satisfies all requirements of part (a):
$$
\boxed{\varphi_0=0,\qquad
\varphi_n\leq\varphi_{n+1}\leq f,
\qquad
\varphi_n\to f\text{ pointwise}.}
$$


::: pf-proof

Combine steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

For every $n\geq0$, the function
$$
\psi_n=\varphi_{n+1}-\varphi_n
$$
is a nonnegative measurable simple function.


::: pf-proof

By step [](#s1-3){.pf-ref}, $\psi_n\geq0$. It is measurable as a difference of measurable functions. Since $\varphi_n$ and $\varphi_{n+1}$ each have finite range, their difference also has finite range, so $\psi_n$ is simple.

:::

:::

::: {.pf-step #s1-7}

For each $n$, there are finitely many nonnegative numbers $d_{n,1},\ldots,d_{n,r_n}$ and measurable sets $E_{n,1},\ldots,E_{n,r_n}$ such that
$$
\psi_n=\sum_{j=1}^{r_n}d_{n,j}\mathbf1_{E_{n,j}}.
$$


::: pf-proof

By step [](#s1-6){.pf-ref}, $\psi_n$ is a nonnegative simple function. Let $d_{n,1},\ldots,d_{n,r_n}$ be its distinct nonzero values and set
$$
E_{n,j}=\{x:\psi_n(x)=d_{n,j}\}.
$$
These level sets are measurable and give the displayed finite representation. If $\psi_n=0$, take $r_n=0$.

:::

:::

::: {.pf-step #s1-8}

There are nonnegative numbers $(c_p)_{p\geq0}$ and measurable sets $(M_p)_{p\geq0}$ such that
$$
\boxed{f=\sum_{p=0}^\infty c_p\mathbf1_{M_p}}.
$$


::: pf-proof

The set of pairs
$$
\{(n,j):n\geq0,\ 1\leq j\leq r_n\}
$$
is countable because each $r_n$ is finite. Enumerate these pairs as $(n_p,j_p)$, and define
$$
c_p=d_{n_p,j_p},
\qquad
M_p=E_{n_p,j_p}.
$$
By step [](#s1-5){.pf-ref} and telescoping,
$$
f
=\lim_{N\to\infty}\varphi_{N+1}
=\sum_{n=0}^\infty(\varphi_{n+1}-\varphi_n)
=\sum_{n=0}^\infty\psi_n.
$$
Substituting the finite representation from step [](#s1-7){.pf-ref} and then using the enumeration gives
$$
f=\sum_{p=0}^\infty c_p\mathbf1_{M_p}.
$$
All terms are nonnegative, so this rearrangement of the countable family of summands is pointwise unambiguous. This proves part (b).

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves part (a), and step [](#s1-8){.pf-ref} proves part (b).

:::

:::

:::
