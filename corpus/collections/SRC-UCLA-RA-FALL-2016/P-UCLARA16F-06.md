---
schema: qual/card@1
id: P-UCLARA16F-06
kind: problem
title: Weakly convergent sequences in $\ell^1$ converge in norm
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Banach Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Consider the Banach space $\ell^1$ consisting of all sequences $u=\{x_i\}$ in $\RR$ with
$$
\norm{ u}_1=\sum_{i=1}^{\infty}\abs{x_i}<\infty,
$$
and the Banach space $\ell^\infty$ consisting of all sequences $v=\{y_i\}$ in $\RR$ with
$$
\norm{ v}_\infty=\sup_{i\in\NN}\abs{y_i}<\infty.
$$
There is a well-defined dual pairing between $\ell^1$ and $\ell^\infty$ given by
$$
\langle u,v\rangle=\sum_{i=1}^{\infty}x_i y_i.
$$
With this dual pairing, $\ell^\infty=(\ell^1)^*$ is the dual space of $\ell^1$.

(a) Show that there exists no sequence $\{u_n\}$ in $\ell^1$ such that (i) $\norm{ u_n}_1\ge1$ for all $n\in\NN$ and (ii) $\langle u_n,v\rangle\to0$ for each $v\in\ell^\infty$.

(b) Show that every weakly convergent sequence $\{u_n\}$ in $\ell^1$ converges in the norm topology of $\ell^1$.
:::

::: {.solution}

## Part (a)

Suppose, toward a contradiction, that
$$
u_n=(x_i^{(n)})_{i\ge1}\in\ell^1
$$
satisfies
$$
\norm{u_n}_1\ge1
$$
for every $n$, and
$$
\langle u_n,v\rangle\to0
$$
for every $v\in\ell^\infty$.

::: pf

::: {.pf-step #s1-1}

For every fixed coordinate $i$,
$$
\boxed{x_i^{(n)}\to0}.
$$


::: pf-proof

Let $e^{(i)}\in\ell^\infty$ be the coordinate vector
$$
e^{(i)}_j=
\begin{cases}
1,&j=i,\\
0,&j\ne i.
\end{cases}
$$
Then
$$
\langle u_n,e^{(i)}\rangle
=
x_i^{(n)}.
$$
The assumed weak convergence to $0$ gives the result.

:::

:::

::: {.pf-step #s1-2}

Choose any $n_1$, and then choose $N_1$ so large that
$$
\sum_{i>N_1}\abs{x_i^{(n_1)}}<\varepsilon.
$$


::: pf-proof

The vector $u_{n_1}$ belongs to $\ell^1$, so its tails tend to zero.

:::

:::

::: {.pf-step #s1-3}

Suppose $N_{k-1}$ and $n_{k-1}$ have been chosen. Then one can choose $n_k>n_{k-1}$ such that
$$
\sum_{i\le N_{k-1}}
\abs{x_i^{(n_k)}}
<
\varepsilon.
$$


::: pf-proof

For each fixed
$$
1\le i\le N_{k-1},
$$
step [](#s1-1){.pf-ref} gives
$$
x_i^{(n)}\to0.
$$
Since there are only finitely many such coordinates, their absolute-value sum tends to $0$. Hence it is eventually $<\varepsilon$.

:::

:::

::: {.pf-step #s1-4}

After choosing $n_k$, choose $N_k>N_{k-1}$ such that
$$
\sum_{i>N_k}
\abs{x_i^{(n_k)}}
<
\varepsilon.
$$


::: pf-proof

Again use that $u_{n_k}\in\ell^1$.

:::

:::

::: pf-step

Thus the required subsequence and block endpoints exist.


::: pf-proof

Steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref} give the induction.

:::

:::

::: {.pf-step #s1-6}

The $\ell^1$-mass of $u_{n_k}$ outside $I_k$ satisfies
$$
\boxed{
\sum_{i\notin I_k}
\abs{x_i^{(n_k)}}
<
2\varepsilon}.
$$


::: pf-proof

The coordinates outside $I_k$ split into
$$
i\le N_{k-1}
$$
and
$$
i>N_k.
$$
Each contribution is $<\varepsilon$ by construction.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
\sum_{i\in I_k}
\abs{x_i^{(n_k)}}
>
1-2\varepsilon}.
$$


::: pf-proof

Since
$$
\norm{u_{n_k}}_1
=
\sum_{i\in I_k}\abs{x_i^{(n_k)}}
+
\sum_{i\notin I_k}\abs{x_i^{(n_k)}}
\ge1,
$$
apply step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

The vector $v$ belongs to $\ell^\infty$ and
$$
\boxed{\norm{v}_\infty\le1}.
$$


::: pf-proof

The blocks $I_k$ are disjoint and cover a subset of $\NN$, so the definition is unambiguous. Every coordinate satisfies
$$
\abs{v_i}\le1.
$$
Set $v_i=0$ on coordinates not belonging to any block.

:::

:::

::: {.pf-step #s1-9}

On the block $I_k$,
$$
\sum_{i\in I_k}
x_i^{(n_k)}v_i
=
\sum_{i\in I_k}
\abs{x_i^{(n_k)}}.
$$


::: pf-proof

By definition,
$$
v_i=\operatorname{sgn}(x_i^{(n_k)})
$$
on $I_k$.

:::

:::

::: {.pf-step #s1-10}

The contribution from outside $I_k$ satisfies
$$
\abs{
\sum_{i\notin I_k}
x_i^{(n_k)}v_i
}
<
2\varepsilon.
$$


::: pf-proof

Since $\abs{v_i}\le1$,
$$
\abs{
\sum_{i\notin I_k}
x_i^{(n_k)}v_i
}
\le
\sum_{i\notin I_k}
\abs{x_i^{(n_k)}}
<
2\varepsilon
$$
by step [](#s1-6){.pf-ref}.

:::

:::

::: pf-step

Hence
$$
\langle u_{n_k},v\rangle
>
1-4\varepsilon.
$$


::: pf-proof

Using steps [](#s1-7){.pf-ref} and [](#s1-9){.pf-ref}, and [](#s1-10){.pf-ref},
$$
\begin{aligned}
\langle u_{n_k},v\rangle
&=
\sum_{i\in I_k}
x_i^{(n_k)}v_i
+
\sum_{i\notin I_k}
x_i^{(n_k)}v_i\\
&\ge
\sum_{i\in I_k}
\abs{x_i^{(n_k)}}
-
\abs{
\sum_{i\notin I_k}
x_i^{(n_k)}v_i
}\\
&>
(1-2\varepsilon)-2\varepsilon\\
&=
1-4\varepsilon.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-12}

Since $\varepsilon=1/8$,
$$
\boxed{
\langle u_{n_k},v\rangle>\frac12}
$$
for every $k$.


::: pf-proof

$$
1-4\varepsilon
=
1-\frac12
=
\frac12.
$$

:::

:::

::: {.pf-step #s1-13}

This contradicts the assumption that
$$
\langle u_n,v\rangle\to0
$$
for every $v\in\ell^\infty$.


::: pf-proof

The fixed vector $v\in\ell^\infty$ from step [](#s1-8){.pf-ref} has pairings along the subsequence bounded below by $1/2$, by step [](#s1-12){.pf-ref}.

:::

:::

::: {.pf-step #s1-14}

Therefore no sequence satisfying conditions (i) and (ii) exists.


::: pf-proof

The assumption of its existence led to the contradiction in step [](#s1-13){.pf-ref}.

:::

:::

::: {.pf-step #s1-15}

Define
$$
w_n=u_n-u.
$$
Then
$$
\boxed{
w_n\rightharpoonup0}.
$$


::: pf-proof

For every $v\in\ell^\infty$,
$$
\langle w_n,v\rangle
=
\langle u_n,v\rangle-\langle u,v\rangle
\to0.
$$

:::

:::

::: {.pf-step #s1-16}

Suppose, toward a contradiction, that
$$
\norm{w_n}_1\not\to0.
$$


::: pf-proof

This is the negation of norm convergence.

:::

:::

::: {.pf-step #s1-17}

Then there exist
$$
\delta>0
$$
and a subsequence $(w_{n_k})$ such that
$$
\boxed{
\norm{w_{n_k}}_1\ge\delta}
$$
for every $k$.


::: pf-proof

Failure of convergence to $0$ gives an $\varepsilon$-subsequence bounded away from $0$.

:::

:::

::: pf-step

Define
$$
\boxed{
z_k=\frac1\delta w_{n_k}}.
$$


::: pf-proof

Since $\delta>0$, this is well defined.

:::

:::

::: {.pf-step #s1-19}

Then
$$
\boxed{
\norm{z_k}_1\ge1}
$$
for every $k$.


::: pf-proof

By step [](#s1-17){.pf-ref},
$$
\norm{z_k}_1
=
\frac1\delta
\norm{w_{n_k}}_1
\ge1.
$$

:::

:::

::: {.pf-step #s1-20}

Also
$$
\boxed{
z_k\rightharpoonup0}.
$$


::: pf-proof

For every $v\in\ell^\infty$,
$$
\langle z_k,v\rangle
=
\frac1\delta
\langle w_{n_k},v\rangle
\to0
$$
by step [](#s1-15){.pf-ref}.

:::

:::

::: pf-step

Steps [](#s1-19){.pf-ref} through [](#s1-20){.pf-ref} contradict part (a).


::: pf-proof

Part (a), step [](#s1-14){.pf-ref}, says no weakly null sequence in $\ell^1$ can have all norms at least $1$.

:::

:::

::: {.pf-step #s1-22}

Therefore
$$
\boxed{
\norm{u_n-u}_1\to0}.
$$


::: pf-proof

The assumption in step [](#s1-16){.pf-ref} is impossible, and
$$
\norm{u_n-u}_1=\norm{w_n}_1.
$$

:::

:::

::: {.pf-step #s1-23}

Thus every weakly convergent sequence in $\ell^1$ converges in norm.


::: pf-proof

This is step [](#s1-22){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-14){.pf-ref} proves part (a), and step [](#s1-23){.pf-ref} proves part (b).

:::

:::

:::
