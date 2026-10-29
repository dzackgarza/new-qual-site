---
schema: qual/card@1
id: P-UCLARA14S-05
kind: problem
title: Separability of sequence spaces and nonexistence of a quotient map from ell2 onto ell1
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2014 section.
---

::: {.problem}
(a) Prove that $\ell^1(\NN)$ and $\ell^2(\NN)$ are separable Banach spaces, while $\ell^\infty(\NN)$ is not separable.

(b) Prove that there is no bounded linear surjection
$$
T:\ell^2(\NN)\to\ell^1(\NN).
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $p\in\{1,2\}$, the space $\ell^p(\NN)$ is complete.


::: pf-proof

Let $(x^{(m)})_{m\ge1}$ be Cauchy in $\ell^p$, where
$$
x^{(m)}
=
(x^{(m)}_k)_{k\ge1}.
$$
For each fixed $k$,
$$
|x^{(m)}_k-x^{(n)}_k|
\le
\|x^{(m)}-x^{(n)}\|_p,
$$
so $(x^{(m)}_k)_m$ is Cauchy in the scalar field. Define
$$
x_k
\coloneqq
\lim_{m\to\infty}x^{(m)}_k.
$$

Fix $m$. By Fatou's lemma for counting measure,
$$
\sum_{k=1}^\infty
|x^{(m)}_k-x_k|^p
\le
\liminf_{n\to\infty}
\sum_{k=1}^\infty
|x^{(m)}_k-x^{(n)}_k|^p.
$$
Since $(x^{(m)})$ is Cauchy, for every $\varepsilon>0$ there is $M$ such that for $m,n\ge M$,
$$
\|x^{(m)}-x^{(n)}\|_p<\varepsilon.
$$
Thus for every $m\ge M$,
$$
\|x^{(m)}-x\|_p
\le
\varepsilon.
$$
In particular $x-x^{(M)}\in\ell^p$, so $x\in\ell^p$, and $x^{(m)}\to x$ in $\ell^p$. Hence $\ell^p$ is Banach.

:::

:::

::: {.pf-step #s1-2}

The spaces $\ell^1(\NN)$ and $\ell^2(\NN)$ are separable.


::: pf-proof

Let $\FF_0$ be $\QQ$ in the real case and $\QQ+i\QQ$ in the complex case. Define
$$
D
\coloneqq
\{x=(x_k):
x_k\in\FF_0,
\text{ and }x_k=0\text{ for all but finitely many }k\}.
$$
The set $D$ is countable.

Fix $x\in\ell^p$ and $\varepsilon>0$, with $p=1$ or $2$. Choose $N$ so that
$$
\sum_{k>N}|x_k|^p
<
\frac{\varepsilon^p}{2}.
$$
For each $1\le k\le N$, choose $q_k\in\FF_0$ so close to $x_k$ that
$$
\sum_{k=1}^N|x_k-q_k|^p
<
\frac{\varepsilon^p}{2}.
$$
Let
$$
q=(q_1,\dots,q_N,0,0,\dots)\in D.
$$
Then
$$
\|x-q\|_p^p
<
\varepsilon^p.
$$
Thus $D$ is countable and dense in both $\ell^1$ and $\ell^2$.

:::

:::

::: {.pf-step #s1-3}

The space $\ell^\infty(\NN)$ is not separable.


::: pf-proof

For each subset $A\subset\NN$, let
$$
\chi_A(k)
=
\begin{cases}
1,&k\in A,\\
0,&k\notin A.
\end{cases}
$$
Then $\chi_A\in\ell^\infty$. If $A\ne B$, there is $k$ in their symmetric difference, so
$$
\|\chi_A-\chi_B\|_\infty=1.
$$
Thus
$$
\{\chi_A:A\subset\NN\}
$$
is an uncountable $1$-separated subset of $\ell^\infty$.

If $D$ were a countable dense subset of $\ell^\infty$, the disjoint open balls
$$
B(\chi_A,1/3)
$$
would each contain a distinct point of $D$, which is impossible. Hence $\ell^\infty$ is not separable.

:::

:::

::: {.pf-step #s1-4}

Suppose, toward a contradiction, that
$$
T:\ell^2\to\ell^1
$$
is bounded and surjective. Then there is a constant $C>0$ such that for every $y\in\ell^1$ there exists $x\in\ell^2$ with
$$
Tx=y
\qquad\text{and}\qquad
\|x\|_2\le C\|y\|_1.
$$


::: pf-proof

The spaces $\ell^2$ and $\ell^1$ are Banach by step [](#s1-1){.pf-ref}. Since $T$ is bounded and surjective, the open mapping theorem implies that $T$ maps some ball about $0$ in $\ell^2$ onto a set containing a ball about $0$ in $\ell^1$. Rescaling gives the displayed uniform preimage estimate.

:::

:::

::: {.pf-step #s1-5}

The adjoint
$$
T^*:(\ell^1)^*=\ell^\infty
\longrightarrow
(\ell^2)^*=\ell^2
$$
is bounded below:
$$
\|\phi\|_\infty
\le
C\|T^*\phi\|_2
\qquad
(\phi\in\ell^\infty).
$$


::: pf-proof

Fix $\phi\in\ell^\infty$. For every $y\in\ell^1$ with $\|y\|_1\le1$, step [](#s1-4){.pf-ref} gives $x\in\ell^2$ with
$$
Tx=y,
\qquad
\|x\|_2\le C.
$$
Therefore
$$
|\phi(y)|
=
|\phi(Tx)|
=
|(T^*\phi)(x)|
\le
C\|T^*\phi\|_2.
$$
Taking the supremum over the unit ball of $\ell^1$ gives the claim.

:::

:::

::: {.pf-step #s1-6}

The range $T^*(\ell^\infty)$ is a closed subspace of $\ell^2$, and $T^*$ is an isomorphism from $\ell^\infty$ onto that range.


::: pf-proof

Step [](#s1-5){.pf-ref} shows that $T^*$ is injective and that its inverse on its range is bounded.

To see that the range is closed, suppose
$$
T^*\phi_n\to y
$$
in $\ell^2$. By step [](#s1-5){.pf-ref},
$$
\|\phi_n-\phi_m\|_\infty
\le
C\|T^*\phi_n-T^*\phi_m\|_2,
$$
so $(\phi_n)$ is Cauchy in the Banach space $\ell^\infty$. Let $\phi_n\to\phi$. Continuity of $T^*$ then gives
$$
T^*\phi=y.
$$
Thus the range is closed.

:::

:::

::: {.pf-step #s1-7}

The assumed surjection $T$ cannot exist.


::: pf-proof

By step [](#s1-2){.pf-ref}, $\ell^2$ is separable. Every subspace of a separable metric space is separable, so the closed subspace
$$
T^*(\ell^\infty)
\subset\ell^2
$$
is separable.

But step [](#s1-6){.pf-ref} says that $\ell^\infty$ is homeomorphic, via a bounded linear isomorphism, to this range. Hence $\ell^\infty$ would be separable, contradicting step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} prove part (a), and steps [](#s1-4){.pf-ref} through [](#s1-7){.pf-ref} prove part (b).

:::

:::

:::
