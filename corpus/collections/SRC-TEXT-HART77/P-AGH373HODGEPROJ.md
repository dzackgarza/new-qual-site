---
schema: qual/card@1
id: P-AGH373HODGEPROJ
kind: problem
title: Hodge cohomology of projective space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Serre Duality
  - Sheaves of Differentials
  - Projective Space
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the full range of p and q with the retained Hartshorne III.7.3 transcription and checked the Euler-sequence computation against Stacks Project Lemmas 50.11.2 and 50.11.3. The proof works over every field, handles projective dimension zero separately, and gives explicit diagonal generators through connecting homomorphisms.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $k$ be a field, let $n\ge0$, and put $X=\PP_k^n$ and $\Omega_X^p=\bigwedge^p\Omega_{X/k}^1$.
Show that
$$
H^q(X, \Omega_X^p) =
\begin{cases}
0 & p \neq q \\
k & p = q
\end{cases}
$$
for $0 \leq p, q \leq n$.
:::

::: {.solution}
Put $E=\OO_X(-1)^{\oplus(n+1)}$ and $\Omega^0=\OO_X$.
All cohomology is coherent-sheaf cohomology for the Zariski topology.

::: pf

::: {.pf-step #s1}

For $1\le p\le n$, there is a short exact sequence
$$
0\longrightarrow\Omega_X^p\longrightarrow
\OO_X(-p)^{\oplus\binom{n+1}{p}}
\longrightarrow\Omega_X^{p-1}\longrightarrow0.
$$

::: pf-proof

The [[T-MODEULER|Euler sequence]] is
$$
0\longrightarrow\Omega_{X/k}^1\longrightarrow E
\xrightarrow{e}\OO_X\longrightarrow0
$$
[@Har10a, Theorem II.8.13].
It splits locally because its quotient is locally free.
Contraction by $e$ defines a map $\bigwedge^pE\to\bigwedge^{p-1}E$.
Locally write $E=\Omega^1\oplus\OO\sigma$ with $e(\sigma)=1$.
Contraction kills $\bigwedge^p\Omega^1$ and sends $\sigma\wedge\alpha$ to $\alpha$ for $\alpha\in\bigwedge^{p-1}\Omega^1$.
Its image is therefore $\Omega^{p-1}$ and its kernel is $\Omega^p$.
The contraction is defined globally, so these local sequences glue.
Finally, the monomial wedge basis gives $\bigwedge^pE\cong\OO(-p)^{\oplus\binom{n+1}{p}}$.

:::

:::

::: {.pf-step #s2}

For $1\le p\le n$, one has $H^0(X,\Omega_X^p)=0$, and the boundary maps give isomorphisms
$$
H^q(X,\Omega_X^{p-1})\xrightarrow{\cong}H^{q+1}(X,\Omega_X^p)
\qquad(q\ge0).
$$

::: pf-proof

For $1\le p\le n$, every cohomology group of $\OO_X(-p)$ vanishes by [[T-IJW1K]] [@Har10a, Theorem III.5.1].
Its degree-zero group vanishes because the twist is negative, its intermediate groups always vanish, and its top-degree group vanishes because $-p>-n-1$.
Groups above degree $n$ vanish as well.
Thus the middle term of step [](#s1){.pf-ref} has zero cohomology in all degrees.
Its long exact sequence gives the stated zero group and boundary isomorphisms.

:::

:::

::: {.pf-step #s3}

The requested cohomology groups are
$$
\boxed{H^q(\PP_k^n,\Omega_X^p)\cong
\begin{cases}
k,&p=q,\\
0,&p\ne q,
\end{cases}
\qquad 0\le p,q\le n.}
$$

::: pf-proof

For $p=0$, one has $H^0(X,\OO_X)=k$ and $H^q(X,\OO_X)=0$ for $q>0$, again by the projective-space cohomology calculation.
For $p>0$, step [](#s2){.pf-ref} gives zero in degree zero and shifts every positive-degree group down by one in both indices.
If $q<p$, iteration reaches a degree-zero group of a positive exterior power, which is zero.
If $q\ge p$, it reaches $H^{q-p}(X,\OO_X)$, which is $k$ exactly when $q=p$ and is otherwise zero.
This proves the formula when $n\ge1$.
For $n=0$, only $(p,q)=(0,0)$ is in the stated range and $X=\Spec k$, so the formula holds directly.

:::

:::

::: {.pf-step #s4}

The diagonal groups have concrete generators $\gamma_0=1$ and $\gamma_p=\partial_p(\gamma_{p-1})$, where $\partial_p$ is the boundary map from step [](#s2){.pf-ref}.

::: pf-proof

Each boundary is an isomorphism, so these elements are nonzero generators.
For an explicit representative, use the standard affine cover $U_i=D_+(x_i)$, ordered by $i$.
Let $\sigma_i=x_i^{-1}e_i\in\Gamma(U_i,E)$, where $e_i$ is the formal generator of the $i$th summand.
Then $e(\sigma_i)=1$.
Under the Euler injection, $\sigma_j-\sigma_i$ corresponds to $d\log(x_j/x_i)$.

In the exterior sequence of step [](#s1){.pf-ref}, the cochain
$$
\sigma_{i_0}\wedge\cdots\wedge\sigma_{i_{p-1}}
$$
lifts the representative of $\gamma_{p-1}$ on the corresponding intersection.
Its alternating Čech boundary is
$$
\sum_{a=0}^p(-1)^a
\sigma_{i_0}\wedge\cdots\wedge\widehat{\sigma_{i_a}}\wedge\cdots\wedge\sigma_{i_p}
=(\sigma_{i_1}-\sigma_{i_0})\wedge\cdots\wedge(\sigma_{i_p}-\sigma_{i_0}).
$$
The equality follows by expansion: all terms with two copies of $\sigma_{i_0}$ vanish.
Thus $\gamma_p$ is represented by
$$
d\log(x_{i_1}/x_{i_0})\wedge\cdots\wedge d\log(x_{i_p}/x_{i_0}).
$$
The affine cover and its intersections are affine, so these Čech classes compute the stated sheaf cohomology [@Har10a, Theorem III.4.5].
In particular, the calculation uses no characteristic-zero or analytic comparison theorem.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove all the required values, and step [](#s4){.pf-ref} specifies generators for the one-dimensional groups.

:::

:::

:::
